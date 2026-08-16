"""Small versioned JSON interchange for inspection, transport, and scoring."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from .canonical import canonical_json, require_exact_keys, stable_id
from .conditions import ConditionCell
from .metrics import MetricReport, compute_metrics
from .panel import PANEL_ID
from .prompts import RenderedPrompt, import_rendered_prompt
from .records import (
    FrozenIntuitionStore,
    IntuitionSample,
    LeakageDecision,
    LeakageDecisionStore,
)
from .results import CandidateResult, CandidateResultStore, FormalWorkerRun

BUNDLE_SCHEMA_VERSION = "intuition_fertility_bundle_v1"


@dataclass(frozen=True)
class ExperimentBundle:
    samples: tuple[IntuitionSample, ...]
    decisions: tuple[LeakageDecision, ...]
    cells: tuple[ConditionCell, ...]
    prompts: tuple[RenderedPrompt, ...]
    runs: tuple[FormalWorkerRun, ...]
    results: tuple[CandidateResult, ...]
    bundle_id: str

    @classmethod
    def create(
        cls,
        *,
        samples: Iterable[IntuitionSample] = (),
        decisions: Iterable[LeakageDecision] = (),
        cells: Iterable[ConditionCell] = (),
        prompts: Iterable[RenderedPrompt] = (),
        runs: Iterable[FormalWorkerRun] = (),
        results: Iterable[CandidateResult] = (),
    ) -> ExperimentBundle:
        ordered_samples = tuple(sorted(samples, key=lambda item: item.sample_id))
        ordered_decisions = tuple(sorted(decisions, key=lambda item: item.decision_id))
        ordered_cells = tuple(sorted(cells, key=lambda item: item.cell_id))
        ordered_prompts = tuple(sorted(prompts, key=lambda item: item.prompt_id))
        ordered_runs = tuple(sorted(runs, key=lambda item: item.run_id))
        ordered_results = tuple(sorted(results, key=lambda item: item.result_id))
        collections = (
            ("sample", [item.sample_id for item in ordered_samples]),
            ("leakage decision", [item.decision_id for item in ordered_decisions]),
            ("condition cell", [item.cell_id for item in ordered_cells]),
            ("rendered prompt", [item.prompt_id for item in ordered_prompts]),
            ("formal worker run", [item.run_id for item in ordered_runs]),
            ("candidate result", [item.result_id for item in ordered_results]),
        )
        for name, identities in collections:
            if len(set(identities)) != len(identities):
                raise ValueError(f"duplicate {name} in bundle")
        sample_ids = {item.sample_id for item in ordered_samples}
        decision_samples = {item.sample_id for item in ordered_decisions}
        decision_ids = {item.decision_id for item in ordered_decisions}
        cell_ids = {item.cell_id for item in ordered_cells}
        prompt_ids = {item.prompt_id for item in ordered_prompts}
        run_ids = {item.run_id for item in ordered_runs}
        if not decision_samples <= sample_ids:
            raise ValueError("bundle leakage decision references an unknown sample")
        if len(decision_samples) != len(ordered_decisions):
            raise ValueError("bundle has more than one leakage decision for a sample")
        for cell in ordered_cells:
            referenced_samples = {
                item
                for item in (cell.anchor_sample_id, cell.guidance_sample_id)
                if item is not None
            }
            if not referenced_samples <= sample_ids:
                raise ValueError("bundle condition cell references an unknown sample")
            if (
                cell.guidance_leakage_decision_id is not None
                and cell.guidance_leakage_decision_id not in decision_ids
            ):
                raise ValueError(
                    "bundle condition cell references an unknown leakage decision"
                )
        if any(prompt.condition_cell_id not in cell_ids for prompt in ordered_prompts):
            raise ValueError("bundle prompt references an unknown condition cell")
        result_slots: set[tuple[str, str, int]] = set()
        for result in ordered_results:
            if result.run_id not in run_ids:
                raise ValueError("bundle result references an unknown run")
            if result.condition_cell_id not in cell_ids:
                raise ValueError("bundle result references an unknown condition cell")
            if result.prompt_id not in prompt_ids:
                raise ValueError("bundle result references an unknown prompt")
            slot = (result.run_id, result.condition_cell_id, result.candidate_index)
            if slot in result_slots:
                raise ValueError("bundle has two results for one candidate slot")
            result_slots.add(slot)
        payload = _bundle_payload(
            samples=ordered_samples,
            decisions=ordered_decisions,
            cells=ordered_cells,
            prompts=ordered_prompts,
            runs=ordered_runs,
            results=ordered_results,
        )
        return cls(
            samples=ordered_samples,
            decisions=ordered_decisions,
            cells=ordered_cells,
            prompts=ordered_prompts,
            runs=ordered_runs,
            results=ordered_results,
            bundle_id=stable_id("bundle", payload),
        )

    def to_dict(self) -> dict[str, Any]:
        payload = _bundle_payload(
            samples=self.samples,
            decisions=self.decisions,
            cells=self.cells,
            prompts=self.prompts,
            runs=self.runs,
            results=self.results,
        )
        return {**payload, "bundle_id": self.bundle_id}

    def metrics(self) -> MetricReport:
        return compute_metrics(
            runs=self.runs,
            cells=self.cells,
            results=self.results,
            samples=self.samples,
            decisions=self.decisions,
        )

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> ExperimentBundle:
        fields = {
            "schema_version",
            "panel_id",
            "samples",
            "leakage_decisions",
            "condition_cells",
            "rendered_prompts",
            "formal_worker_runs",
            "candidate_results",
            "bundle_id",
        }
        require_exact_keys(value, required=fields, field="experiment bundle")
        if (
            value["schema_version"] != BUNDLE_SCHEMA_VERSION
            or value["panel_id"] != PANEL_ID
        ):
            raise ValueError("unsupported bundle schema or panel identity")
        for field in fields - {"schema_version", "panel_id", "bundle_id"}:
            if not isinstance(value[field], list):
                raise ValueError(f"bundle field {field} must be an array")

        sample_store = FrozenIntuitionStore()
        for item in value["samples"]:
            sample_store.add(IntuitionSample.from_dict(item))
        samples = {sample.sample_id: sample for sample in sample_store.values()}

        decision_store = LeakageDecisionStore()
        for item in value["leakage_decisions"]:
            try:
                sample = samples[item["sample_id"]]
            except (KeyError, TypeError) as error:
                raise ValueError(
                    "leakage decision references an unknown sample"
                ) from error
            decision_store.add(LeakageDecision.from_dict(item, sample=sample))
        decisions = {
            decision.sample_id: decision for decision in decision_store.values()
        }

        cells: dict[str, ConditionCell] = {}
        for item in value["condition_cells"]:
            cell = ConditionCell.from_dict(item, samples=samples, decisions=decisions)
            if cell.cell_id in cells:
                raise ValueError(f"duplicate condition cell: {cell.cell_id}")
            cells[cell.cell_id] = cell

        prompts: dict[str, RenderedPrompt] = {}
        for item in value["rendered_prompts"]:
            try:
                cell = cells[item["condition_cell_id"]]
            except (KeyError, TypeError) as error:
                raise ValueError(
                    "rendered prompt references an unknown condition cell"
                ) from error
            prompt = import_rendered_prompt(item, cell=cell)
            if prompt.prompt_id in prompts:
                raise ValueError(f"duplicate rendered prompt: {prompt.prompt_id}")
            prompts[prompt.prompt_id] = prompt

        runs: dict[str, FormalWorkerRun] = {}
        for item in value["formal_worker_runs"]:
            run = FormalWorkerRun.from_dict(item)
            if run.run_id in runs:
                raise ValueError(f"duplicate formal worker run: {run.run_id}")
            runs[run.run_id] = run

        result_store = CandidateResultStore()
        for item in value["candidate_results"]:
            try:
                run = runs[item["run_id"]]
                cell = cells[item["condition_cell_id"]]
                prompt = prompts[item["prompt_id"]]
            except (KeyError, TypeError) as error:
                raise ValueError(
                    "candidate result references an unknown run, cell, or prompt"
                ) from error
            result_store.add(
                CandidateResult.from_dict(item, run=run, cell=cell, prompt=prompt)
            )

        rebuilt = cls.create(
            samples=sample_store.values(),
            decisions=decision_store.values(),
            cells=cells.values(),
            prompts=prompts.values(),
            runs=runs.values(),
            results=result_store.values(),
        )
        if rebuilt.to_dict() != value:
            raise ValueError("bundle content, ordering, or identity is inconsistent")
        return rebuilt


def _bundle_payload(
    *,
    samples: Iterable[IntuitionSample],
    decisions: Iterable[LeakageDecision],
    cells: Iterable[ConditionCell],
    prompts: Iterable[RenderedPrompt],
    runs: Iterable[FormalWorkerRun],
    results: Iterable[CandidateResult],
) -> dict[str, Any]:
    return {
        "schema_version": BUNDLE_SCHEMA_VERSION,
        "panel_id": PANEL_ID,
        "samples": [item.to_dict() for item in samples],
        "leakage_decisions": [item.to_dict() for item in decisions],
        "condition_cells": [item.to_dict() for item in cells],
        "rendered_prompts": [item.to_dict() for item in prompts],
        "formal_worker_runs": [item.to_dict() for item in runs],
        "candidate_results": [item.to_dict() for item in results],
    }


def write_bundle(path: str | Path, bundle: ExperimentBundle) -> None:
    Path(path).write_text(canonical_json(bundle.to_dict()) + "\n", encoding="utf-8")


def read_bundle(path: str | Path) -> ExperimentBundle:
    try:
        value = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"could not read experiment bundle: {error}") from error
    if not isinstance(value, dict):
        raise ValueError("experiment bundle root must be an object")
    return ExperimentBundle.from_dict(value)
