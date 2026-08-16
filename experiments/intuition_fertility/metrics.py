"""Deterministic theorem-level metrics and matched comparisons."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import asdict, dataclass
from typing import Any, Iterable

from .canonical import stable_id
from .conditions import (
    Condition,
    ConditionCell,
    relevant_distant_length_eligibility,
)
from .panel import get_public_target
from .records import IntuitionSample, LeakageDecision, LeakageLabel
from .results import CandidateResult, FormalWorkerRun

METRIC_SCHEMA_VERSION = "intuition_fertility_metrics_v1"


@dataclass(frozen=True)
class CellMetrics:
    run_id: str
    theorem_id: str
    presentation: str
    target_role: str
    condition: str
    experimental_role: str
    condition_cell_id: str
    generator_config_id: str | None
    candidate_budget: int
    observed_candidates: int
    complete: bool
    verified_count: int
    verified_rate: float
    pass_at_k: bool
    first_verified_rank: int | None
    generated_tokens_to_first_verified: int | None
    runtime_comparable: bool
    runtime_comparability_id: str | None
    mean_runtime_seconds: float | None


@dataclass(frozen=True)
class MatchedComparison:
    run_id: str
    theorem_id: str
    presentation: str
    condition_cell_id: str
    condition: str
    control_condition: str
    control_cell_id: str
    raw_verified_rate_delta: float
    content_claim_eligible: bool
    exclusion_reasons: tuple[str, ...]


@dataclass(frozen=True)
class LeakageSummary:
    theorem_id: str
    presentation: str
    generator_role: str
    generator_config_id: str
    total_samples: int
    classified_samples: int
    missing_decisions: int
    strategic_count: int
    borderline_count: int
    proof_like_count: int
    strategic_rate: float | None
    borderline_rate: float | None
    proof_like_rate: float | None


@dataclass(frozen=True)
class PrimaryAggregate:
    run_id: str
    presentation: str
    condition: str
    generator_config_id: str | None
    theorem_ids: tuple[str, ...]
    verified_count: int
    candidate_budget: int
    verified_rate: float
    pass_count: int


@dataclass(frozen=True)
class IneligibleCellSummary:
    theorem_id: str
    presentation: str
    condition: str
    condition_cell_id: str
    generator_config_id: str | None
    ineligibility_reasons: tuple[str, ...]


@dataclass(frozen=True)
class MetricReport:
    schema_version: str
    cell_metrics: tuple[CellMetrics, ...]
    matched_comparisons: tuple[MatchedComparison, ...]
    adjacent_transfer_cells: tuple[str, ...]
    leakage_summaries: tuple[LeakageSummary, ...]
    ineligible_cells: tuple[IneligibleCellSummary, ...]
    primary_aggregates: tuple[PrimaryAggregate, ...]
    input_run_ids: tuple[str, ...]
    input_cell_ids: tuple[str, ...]
    input_sample_ids: tuple[str, ...]
    input_result_ids: tuple[str, ...]
    input_decision_ids: tuple[str, ...]
    report_id: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "cell_metrics": [asdict(item) for item in self.cell_metrics],
            "matched_comparisons": [
                {**asdict(item), "exclusion_reasons": list(item.exclusion_reasons)}
                for item in self.matched_comparisons
            ],
            "adjacent_transfer_cells": list(self.adjacent_transfer_cells),
            "leakage_summaries": [asdict(item) for item in self.leakage_summaries],
            "ineligible_cells": [
                {
                    **asdict(item),
                    "ineligibility_reasons": list(item.ineligibility_reasons),
                }
                for item in self.ineligible_cells
            ],
            "primary_aggregates": [
                {**asdict(item), "theorem_ids": list(item.theorem_ids)}
                for item in self.primary_aggregates
            ],
            "input_run_ids": list(self.input_run_ids),
            "input_cell_ids": list(self.input_cell_ids),
            "input_sample_ids": list(self.input_sample_ids),
            "input_result_ids": list(self.input_result_ids),
            "input_decision_ids": list(self.input_decision_ids),
            "report_id": self.report_id,
        }


def _cell_metrics(
    *, run: FormalWorkerRun, cell: ConditionCell, results: list[CandidateResult]
) -> CellMetrics:
    if not cell.eligible:
        raise ValueError("ineligible cells cannot carry formal-worker outcomes")
    indexes = [result.candidate_index for result in results]
    orders = [result.candidate_order for result in results]
    if len(set(indexes)) != len(indexes) or len(set(orders)) != len(orders):
        raise ValueError("candidate indexes and orders must be unique within a cell")
    if any(result.run_id != run.run_id for result in results):
        raise ValueError("cell contains a result from another run")
    if any(result.condition_cell_id != cell.cell_id for result in results):
        raise ValueError("cell contains a result rebound from another condition")
    verified = [result for result in results if result.verified]
    first_rank = min((result.candidate_order for result in verified), default=None)
    tokens_to_first: int | None = None
    if first_rank is not None:
        through_first = [
            result for result in results if result.candidate_order <= first_rank
        ]
        if len(through_first) == first_rank and all(
            result.generated_token_count is not None for result in through_first
        ):
            tokens_to_first = sum(
                result.generated_token_count or 0 for result in through_first
            )
    runtime_ids = {result.runtime_comparability_id for result in results}
    runtime_comparable = (
        bool(results) and None not in runtime_ids and len(runtime_ids) == 1
    )
    mean_runtime = None
    runtime_id = None
    if runtime_comparable:
        runtimes = [result.runtime_seconds for result in results]
        if all(runtime is not None for runtime in runtimes):
            mean_runtime = sum(runtime or 0.0 for runtime in runtimes) / len(runtimes)
            runtime_id = next(iter(runtime_ids))
        else:
            runtime_comparable = False
    return CellMetrics(
        run_id=run.run_id,
        theorem_id=cell.theorem_id,
        presentation=cell.presentation,
        target_role=get_public_target(cell.theorem_id).role,
        condition=cell.condition,
        experimental_role=cell.experimental_role,
        condition_cell_id=cell.cell_id,
        generator_config_id=cell.generator_config_id,
        candidate_budget=run.candidate_budget,
        observed_candidates=len(results),
        complete=len(results) == run.candidate_budget,
        verified_count=len(verified),
        verified_rate=len(verified) / run.candidate_budget,
        pass_at_k=bool(verified),
        first_verified_rank=first_rank,
        generated_tokens_to_first_verified=tokens_to_first,
        runtime_comparable=runtime_comparable,
        runtime_comparability_id=runtime_id,
        mean_runtime_seconds=mean_runtime,
    )


def _leakage_summaries(
    samples: Iterable[IntuitionSample], decisions: Iterable[LeakageDecision]
) -> tuple[LeakageSummary, ...]:
    decision_by_sample = {decision.sample_id: decision for decision in decisions}
    grouped: dict[tuple[str, str, str, str], list[IntuitionSample]] = defaultdict(list)
    for sample in samples:
        grouped[
            (
                sample.theorem_id,
                sample.presentation,
                sample.generator_role,
                sample.generator_config_id,
            )
        ].append(sample)
    output: list[LeakageSummary] = []
    for (theorem_id, presentation, role, config_id), members in sorted(grouped.items()):
        counts = {label.value: 0 for label in LeakageLabel}
        classified = 0
        for sample in members:
            decision = decision_by_sample.get(sample.sample_id)
            if decision is not None:
                counts[decision.label] += 1
                classified += 1

        def rate(count: int) -> float | None:
            return count / classified if classified else None

        output.append(
            LeakageSummary(
                theorem_id=theorem_id,
                presentation=presentation,
                generator_role=role,
                generator_config_id=config_id,
                total_samples=len(members),
                classified_samples=classified,
                missing_decisions=len(members) - classified,
                strategic_count=counts[LeakageLabel.STRATEGIC.value],
                borderline_count=counts[LeakageLabel.BORDERLINE.value],
                proof_like_count=counts[LeakageLabel.PROOF_LIKE.value],
                strategic_rate=rate(counts[LeakageLabel.STRATEGIC.value]),
                borderline_rate=rate(counts[LeakageLabel.BORDERLINE.value]),
                proof_like_rate=rate(counts[LeakageLabel.PROOF_LIKE.value]),
            )
        )
    return tuple(output)


def compute_metrics(
    *,
    runs: Iterable[FormalWorkerRun],
    cells: Iterable[ConditionCell],
    results: Iterable[CandidateResult],
    samples: Iterable[IntuitionSample] = (),
    decisions: Iterable[LeakageDecision] = (),
) -> MetricReport:
    run_list = tuple(runs)
    cell_list = tuple(cells)
    sample_list = tuple(samples)
    decision_list = tuple(decisions)
    run_by_id = {run.run_id: run for run in run_list}
    cell_by_id = {cell.cell_id: cell for cell in cell_list}
    sample_by_id = {sample.sample_id: sample for sample in sample_list}
    if len(run_by_id) != len(run_list):
        raise ValueError("duplicate formal worker run in metric input")
    if len(cell_by_id) != len(cell_list):
        raise ValueError("duplicate condition cell in metric input")
    if len(sample_by_id) != len(sample_list):
        raise ValueError("duplicate intuition sample in metric input")
    decision_samples = [decision.sample_id for decision in decision_list]
    if len(set(decision_samples)) != len(decision_samples):
        raise ValueError("duplicate leakage decision in metric input")
    if any(sample_id not in sample_by_id for sample_id in decision_samples):
        raise ValueError(
            "leakage decision references a sample outside the metric input"
        )
    result_list = list(results)
    grouped_results: dict[tuple[str, str], list[CandidateResult]] = defaultdict(list)
    result_slots: set[tuple[str, str, int]] = set()
    for result in result_list:
        if result.run_id not in run_by_id:
            raise ValueError(f"result references unknown run {result.run_id}")
        if result.condition_cell_id not in cell_by_id:
            raise ValueError(
                f"result references unknown cell {result.condition_cell_id}"
            )
        slot = (result.run_id, result.condition_cell_id, result.candidate_index)
        if slot in result_slots:
            raise ValueError("duplicate candidate slot in metric input")
        result_slots.add(slot)
        grouped_results[(result.run_id, result.condition_cell_id)].append(result)

    metric_pairs: list[tuple[CellMetrics, ConditionCell]] = []
    for (run_id, cell_id), members in sorted(grouped_results.items()):
        cell = cell_by_id[cell_id]
        metric_pairs.append(
            (_cell_metrics(run=run_by_id[run_id], cell=cell, results=members), cell)
        )
    metrics = tuple(pair[0] for pair in metric_pairs)

    lookup: dict[
        tuple[str, str, str, str, str | None],
        list[tuple[CellMetrics, ConditionCell]],
    ] = defaultdict(list)
    for metric, cell in metric_pairs:
        lookup[
            (
                metric.run_id,
                metric.theorem_id,
                metric.presentation,
                metric.condition,
                cell.generator_config_id,
            )
        ].append((metric, cell))

    def select_control(
        metric: CellMetrics,
        condition: Condition,
        generator_config_id: str | None = None,
        anchor_sample_id: str | None = None,
    ) -> tuple[CellMetrics, ConditionCell] | None:
        candidates = lookup.get(
            (
                metric.run_id,
                metric.theorem_id,
                metric.presentation,
                condition.value,
                generator_config_id,
            ),
            [],
        )
        if anchor_sample_id is not None:
            candidates = [
                candidate
                for candidate in candidates
                if candidate[1].anchor_sample_id == anchor_sample_id
            ]
        if len(candidates) > 1:
            raise ValueError("ambiguous matched control cell")
        return candidates[0] if candidates else None

    comparisons: list[MatchedComparison] = []
    adjacent_cells = [
        cell.cell_id
        for cell in cell_by_id.values()
        if cell.experimental_role == "transfer_probe"
    ]
    fixed_controls = (
        Condition.NO_GUIDANCE,
        Condition.FACTUAL_CONTROL,
        Condition.GENERIC_STRATEGY_CONTROL,
    )
    for metric, cell in metric_pairs:
        if metric.condition == Condition.NO_GUIDANCE.value:
            continue
        for control_condition in fixed_controls:
            control = select_control(metric, control_condition)
            if control is None:
                continue
            control_metric, control_cell = control
            reasons: list[str] = []
            if not metric.complete:
                reasons.append("incomplete_condition_results")
            if not control_metric.complete:
                reasons.append("incomplete_control_results")
            comparisons.append(
                MatchedComparison(
                    run_id=metric.run_id,
                    theorem_id=metric.theorem_id,
                    presentation=metric.presentation,
                    condition_cell_id=cell.cell_id,
                    condition=metric.condition,
                    control_condition=control_condition.value,
                    control_cell_id=control_cell.cell_id,
                    raw_verified_rate_delta=metric.verified_rate
                    - control_metric.verified_rate,
                    content_claim_eligible=(
                        cell.eligible and control_cell.eligible and not reasons
                    ),
                    exclusion_reasons=tuple(reasons),
                )
            )
        if cell.experimental_role == "relevant_strategy":
            distant = select_control(
                metric,
                Condition.DISTANT_MISMATCHED_STRATEGY,
                cell.generator_config_id,
                cell.anchor_sample_id,
            )
            if distant is not None:
                distant_metric, distant_cell = distant
                length = relevant_distant_length_eligibility(cell, distant_cell)
                reasons: list[str] = []
                if not cell.eligible:
                    reasons.extend(cell.ineligibility_reasons)
                if not distant_cell.eligible:
                    reasons.extend(distant_cell.ineligibility_reasons)
                if not metric.complete:
                    reasons.append("incomplete_condition_results")
                if not distant_metric.complete:
                    reasons.append("incomplete_control_results")
                if not length.eligible:
                    reasons.append(
                        "relevant_distant_length_difference_exceeds_20_percent"
                    )
                comparisons.append(
                    MatchedComparison(
                        run_id=metric.run_id,
                        theorem_id=metric.theorem_id,
                        presentation=metric.presentation,
                        condition_cell_id=cell.cell_id,
                        condition=metric.condition,
                        control_condition=Condition.DISTANT_MISMATCHED_STRATEGY.value,
                        control_cell_id=distant_cell.cell_id,
                        raw_verified_rate_delta=(
                            metric.verified_rate - distant_metric.verified_rate
                        ),
                        content_claim_eligible=not reasons,
                        exclusion_reasons=tuple(sorted(set(reasons))),
                    )
                )

    aggregate_groups: dict[tuple[str, str, str, str | None], list[CellMetrics]] = (
        defaultdict(list)
    )
    for metric, _ in metric_pairs:
        if metric.target_role == "primary":
            aggregate_groups[
                (
                    metric.run_id,
                    metric.presentation,
                    metric.condition,
                    metric.generator_config_id,
                )
            ].append(metric)
    aggregates: list[PrimaryAggregate] = []
    for (run_id, presentation, condition, config_id), members in sorted(
        aggregate_groups.items(),
        key=lambda item: tuple("" if part is None else part for part in item[0]),
    ):
        verified_count = sum(member.verified_count for member in members)
        budget = sum(member.candidate_budget for member in members)
        aggregates.append(
            PrimaryAggregate(
                run_id=run_id,
                presentation=presentation,
                condition=condition,
                generator_config_id=config_id,
                theorem_ids=tuple(sorted(member.theorem_id for member in members)),
                verified_count=verified_count,
                candidate_budget=budget,
                verified_rate=verified_count / budget,
                pass_count=sum(member.pass_at_k for member in members),
            )
        )

    leakage = _leakage_summaries(sample_list, decision_list)
    ineligible = tuple(
        IneligibleCellSummary(
            theorem_id=cell.theorem_id,
            presentation=cell.presentation,
            condition=cell.condition,
            condition_cell_id=cell.cell_id,
            generator_config_id=cell.generator_config_id,
            ineligibility_reasons=cell.ineligibility_reasons,
        )
        for cell in sorted(cell_by_id.values(), key=lambda item: item.cell_id)
        if not cell.eligible
    )
    run_ids = tuple(sorted(run_by_id))
    cell_ids = tuple(sorted(cell_by_id))
    sample_ids = tuple(sorted(sample.sample_id for sample in sample_list))
    result_ids = tuple(sorted(result.result_id for result in result_list))
    decision_ids = tuple(sorted(decision.decision_id for decision in decision_list))
    report_input = {
        "schema_version": METRIC_SCHEMA_VERSION,
        "run_ids": list(run_ids),
        "cell_ids": list(cell_ids),
        "sample_ids": list(sample_ids),
        "result_ids": list(result_ids),
        "decision_ids": list(decision_ids),
    }
    return MetricReport(
        schema_version=METRIC_SCHEMA_VERSION,
        cell_metrics=metrics,
        matched_comparisons=tuple(
            sorted(
                comparisons,
                key=lambda item: (
                    item.run_id,
                    item.theorem_id,
                    item.condition_cell_id,
                    item.control_condition,
                ),
            )
        ),
        adjacent_transfer_cells=tuple(sorted(adjacent_cells)),
        leakage_summaries=leakage,
        ineligible_cells=ineligible,
        primary_aggregates=tuple(aggregates),
        input_run_ids=run_ids,
        input_cell_ids=cell_ids,
        input_sample_ids=sample_ids,
        input_result_ids=result_ids,
        input_decision_ids=decision_ids,
        report_id=stable_id("metrics", report_input),
    )
