"""Materialize and strictly validate issue #32 Checkpoint C without inference."""

from __future__ import annotations

import hashlib
import json
import os
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from .canonical import canonical_json, require_exact_keys, stable_id
from .checkpoint_a_v2 import EXPECTED_CHECKPOINT_A_V2_ID, read_checkpoint_a_v2
from .checkpoint_b_v2 import EXPECTED_CHECKPOINT_B_V2_ID, read_checkpoint_b_v2
from .conditions import (
    Condition,
    ConditionCell,
    build_donor_condition,
    build_fixed_condition,
    build_relevant_condition,
)
from .interchange import ExperimentBundle, read_bundle, write_bundle
from .panel import (
    ADJACENT_DONORS,
    DISTANT_DONORS,
    GENERIC_STRATEGY_CONTROL,
    PANEL_ID,
    Presentation,
    get_control,
    get_target_identity,
)
from .prompts import (
    WHOLE_PROOF_CONTINUATION,
    PromptTemplate,
    inspect_prompt_parity,
    render_prompt,
)
from .records import (
    GeneratorRole,
    IntuitionSample,
    LeakageDecision,
    TokenCounter,
    escape_lean_block_comment,
)
from .results import FormalWorkerRun

CHECKPOINT_C_SCHEMA_VERSION = "intuition_fertility_checkpoint_c_v1"
DEFAULT_CHECKPOINT_C_PATH = Path(__file__).with_name("checkpoint_c_v1.json")
DEFAULT_CHECKPOINT_C_BUNDLE_PATH = Path(__file__).with_name(
    "checkpoint_c_bundle_v1.json"
)
EXPECTED_CHECKPOINT_C_ID = (
    "checkpoint_c_f3bebc4787712fec867107ecb0ca26cf9c9ee0cacaad9bac3e4fa5078fa17ccc"
)

_REPOSITORY_ROOT = Path(__file__).parents[2]
_MATHIA_MAIN_COMMIT = "0f4da8f2a9520345c2aa450f756b9a9319d5ae8b"
_CHECKPOINT_A_V2_SHA256 = (
    "f6a64a9545e86e1667476f4e68a8e644153953c9fd4f4039e4d50f544a3bdd61"
)
_CHECKPOINT_B_V2_SHA256 = (
    "4ad38162d14f9301689878675d1c699eb9a108e80d0462a5eece288f37cca45a"
)
_DESIGN_AMENDMENT_URL = (
    "https://github.com/murillo128/mathia/issues/32#issuecomment-5317507813"
)
_FORMAL_PROMPT_RESOLUTION = {
    "qwen_lean_commit": "ef09f5e0f11a54a25fcb95b324d766f675be49a3",
    "phase5_selection_function": "select_phase5_heldout_workload",
    "renderer_call": "render_sft_prompt(record)_calls_render_proof_request(record.declaration)",
    "source_preamble_present": False,
    "prefix_semantics": "whole_proof_instruction_then_newline_then_record_local_declaration",
    "source_files": {
        "src/qwen_lean/phase3.py": "a2b87e7ee0dcd1e1cfb90bb436f2ce05b812d50781f243d98be7c474132d5b44",
        "src/qwen_lean/prompt.py": "2b4af79a4d39da023120b0d2ab073708a1c90bea60e3b823eb3a506d05209c54",
        "src/qwen_lean/phase5.py": "c1f0f7b6a2c9e363b8fee72d27bee4bfbb22093d084733e91896256d46d72179",
    },
}

_TOKENIZER_IDENTITY = {
    "model": "Qwen/Qwen3-8B-Base",
    "revision": "49e3418fbbbca6ecbdf9608b4d22e5a407081db4",
    "add_special_tokens": False,
}
_CONTROL_TOKEN_COUNTS = {
    "A": {"factual_control": 75, "generic_strategy_control": 48},
    "B": {"factual_control": 61, "generic_strategy_control": 48},
    "C": {"factual_control": 38, "generic_strategy_control": 48},
    "D": {"factual_control": 51, "generic_strategy_control": 48},
    "E": {"factual_control": 39, "generic_strategy_control": 48},
    "F": {"factual_control": 36, "generic_strategy_control": 48},
    "G": {"factual_control": 44, "generic_strategy_control": 48},
}

_WHOLE_PROOF_INSTRUCTION = (
    "/- Complete the proof below.\n"
    "Return only Lean code continuing after `by`; do not use `sorry` or `admit`. -/"
)
_PROMPT_PREFIX = f"{_WHOLE_PROOF_INSTRUCTION}\n".encode()

# Exact Phase-2 record-local declarations. Their hashes are independently bound by
# the accepted panel and checked again by PromptTemplate.
_RECORD_DECLARATIONS = {
    "A": """theorem eqOn_zero_of_preconnected_of_eventuallyEq_zero_aux [CompleteSpace F] {f : E → F} {U : Set E}
    (hf : AnalyticOnNhd 𝕜 f U) (hU : IsPreconnected U)
    {z₀ : E} (h₀ : z₀ ∈ U) (hfz₀ : f =ᶠ[𝓝 z₀] 0) :
    EqOn f 0 U""",
    "B": """lemma disjoint_genEigenspace [IsDomain R] [IsTorsionFree R M]
    (f : End R M) {μ₁ μ₂ : R} (hμ : μ₁ ≠ μ₂) (k l : ℕ∞) :
    Disjoint (f.genEigenspace μ₁ k) (f.genEigenspace μ₂ l)""",
    "C": """theorem linearIndependent_sum {v : ι ⊕ ι' → M} :
    LinearIndependent R v ↔
      LinearIndependent R (v ∘ Sum.inl) ∧
        LinearIndependent R (v ∘ Sum.inr) ∧
          Disjoint (Submodule.span R (range (v ∘ Sum.inl)))
            (Submodule.span R (range (v ∘ Sum.inr)))""",
    "D": """theorem nonempty_hom_of_forall_finite_subgraph_hom [Finite W]
    (h : ∀ G' : G.Subgraph, G'.verts.Finite → G'.coe →g F) : Nonempty (G →g F)""",
    "E": """theorem church_rosser (h : ∀ a b c, r a b → r a c → ∃ d, ReflGen r b d ∧ ReflTransGen r c d)
    (hab : ReflTransGen r a b) (hac : ReflTransGen r a c) : Join (ReflTransGen r) b c""",
    "F": """lemma MeasurableSet.eq_preimage_restrict_countable
    [∀ i, MeasurableSpace (α i)] {s : Set (Π i, α i)} (hs : MeasurableSet s) :
    ∃ I : Set ι, ∃ t, I.Countable ∧ s = I.restrict ⁻¹' t""",
    "G": """theorem card_orbit_mul_card_stabilizer_eq_card_group (b : X) [Fintype G] [Fintype <| orbit G b]
    [Fintype <| stabilizer G b] :
    Fintype.card (orbit G b) * Fintype.card (stabilizer G b) = Fintype.card G""",
}

_PRIMARY_LOGICAL_CONDITION_ORDER = (
    "no_guidance",
    "factual_control",
    "generic_strategy_control",
    "qwen_base_intuition",
    "qwen_base_adjacent_cross_theorem_strategy",
    "qwen_base_distant_mismatched_strategy",
    "codex_reference_intuition",
    "codex_reference_adjacent_cross_theorem_strategy",
    "codex_reference_distant_mismatched_strategy",
)


def _sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _require_equal(actual: Any, expected: Any, field: str) -> None:
    if actual != expected:
        raise ValueError(f"checkpoint C {field} does not match the frozen contract")


class _FrozenControlTokenCounter:
    """Reconstruct fixed control cells from the observed pinned-tokenizer counts."""

    def __init__(self, theorem_id: str) -> None:
        self.theorem_id = theorem_id
        self._counts = {
            escape_lean_block_comment(get_control(theorem_id).factual_control): (
                _CONTROL_TOKEN_COUNTS[theorem_id][Condition.FACTUAL_CONTROL.value]
            ),
            escape_lean_block_comment(GENERIC_STRATEGY_CONTROL): (
                _CONTROL_TOKEN_COUNTS[theorem_id][
                    Condition.GENERIC_STRATEGY_CONTROL.value
                ]
            ),
        }

    @property
    def identity(self) -> dict[str, Any]:
        return dict(_TOKENIZER_IDENTITY)

    def count(self, text: str) -> int:
        try:
            return self._counts[text]
        except KeyError as error:
            raise ValueError("unknown fixed-control tokenizer input") from error


def _load_b_v2_records() -> tuple[list[IntuitionSample], list[LeakageDecision]]:
    freeze = read_checkpoint_b_v2()
    samples = [IntuitionSample.from_dict(item) for item in freeze.value["samples"]]
    sample_by_id = {sample.sample_id: sample for sample in samples}
    decisions = [
        LeakageDecision.from_dict(item, sample=sample_by_id[item["sample_id"]])
        for item in freeze.value["leakage_decisions"]
    ]
    return samples, decisions


def _build_cells(
    samples: list[IntuitionSample], decisions: list[LeakageDecision]
) -> list[ConditionCell]:
    sample_by_key = {
        (sample.theorem_id, sample.generator_role): sample for sample in samples
    }
    decision_by_sample = {decision.sample_id: decision for decision in decisions}
    cells: list[ConditionCell] = []
    for theorem_id in "ABCDEFG":
        counter = _FrozenControlTokenCounter(theorem_id)
        cells.append(
            build_fixed_condition(
                theorem_id=theorem_id,
                presentation=Presentation.STANDARD,
                condition=Condition.NO_GUIDANCE,
                token_counter=counter,
            )
        )
        for condition in (
            Condition.FACTUAL_CONTROL,
            Condition.GENERIC_STRATEGY_CONTROL,
        ):
            cells.append(
                build_fixed_condition(
                    theorem_id=theorem_id,
                    presentation=Presentation.STANDARD,
                    condition=condition,
                    token_counter=counter,
                )
            )
        for role in (
            GeneratorRole.QWEN_BASE.value,
            GeneratorRole.CODEX_REFERENCE.value,
        ):
            anchor = sample_by_key[(theorem_id, role)]
            cells.append(
                build_relevant_condition(
                    sample=anchor, decision=decision_by_sample[anchor.sample_id]
                )
            )
            if theorem_id == "G":
                continue
            for donor_kind in ("adjacent", "distant"):
                mapping = (
                    ADJACENT_DONORS if donor_kind == "adjacent" else DISTANT_DONORS
                )
                donor = sample_by_key[(mapping[theorem_id], role)]
                cells.append(
                    build_donor_condition(
                        receiver_theorem_id=theorem_id,
                        anchor_sample=anchor,
                        donor_kind=donor_kind,
                        donor_sample=donor,
                        donor_decision=decision_by_sample[donor.sample_id],
                    )
                )
    return cells


def _prompt_template(theorem_id: str) -> PromptTemplate:
    identity = get_target_identity(theorem_id)
    return PromptTemplate(
        theorem_id=theorem_id,
        canonical_target=identity.canonical_target,
        theorem_record_id=identity.record_id,
        prefix=_PROMPT_PREFIX,
        declaration=_RECORD_DECLARATIONS[theorem_id].encode()
        + WHOLE_PROOF_CONTINUATION,
    )


def _build_run() -> FormalWorkerRun:
    freeze = read_checkpoint_a_v2()
    contract = freeze.materialized_scientific_contract()
    binding = contract["formal_worker_binding"]["resolved_identity"]
    generation = contract["formal_worker_generation"]
    settings = {
        key: value
        for key, value in generation.items()
        if key not in {"candidate_budget_per_eligible_cell", "repeat_seeds"}
    }
    return FormalWorkerRun.create(
        qwen_lean_identity={
            "status": contract["formal_worker_binding"]["status"],
            "qwen_lean_source": binding["qwen_lean_source"],
            "adapter": binding["adapter"],
            "formal_worker_tokenizer": binding["tokenizer"],
            "whole_proof_prompt": binding["whole_proof_prompt"],
            "runtime": binding["runtime"],
        },
        base_model_identity=binding["base_model"],
        tokenizer_identity=_TOKENIZER_IDENTITY,
        formal_environment_identity={
            **binding["formal_environment"],
            "verifier": binding["verifier"],
        },
        mathlib_revision=binding["formal_environment"]["mathlib_revision"],
        lean_version=binding["formal_environment"]["lean_toolchain"].split(":")[-1],
        generation_settings=settings,
        candidate_budget=generation["candidate_budget_per_eligible_cell"],
        seeds=generation["repeat_seeds"],
    )


def _logical_condition_name(
    cell: ConditionCell, samples: dict[str, IntuitionSample]
) -> str:
    if cell.condition in {
        Condition.NO_GUIDANCE.value,
        Condition.FACTUAL_CONTROL.value,
        Condition.GENERIC_STRATEGY_CONTROL.value,
    }:
        return cell.condition
    anchor = samples[cell.anchor_sample_id]  # type: ignore[index]
    if cell.experimental_role == "relevant_strategy":
        return f"{anchor.generator_role}_intuition"
    return f"{anchor.generator_role}_{cell.condition}"


def _build_materialization() -> tuple[
    ExperimentBundle, list[ConditionCell], FormalWorkerRun
]:
    samples, decisions = _load_b_v2_records()
    cells = _build_cells(samples, decisions)
    prompts = [
        render_prompt(_prompt_template(cell.theorem_id), cell)
        for cell in cells
        if cell.eligible
    ]
    run = _build_run()
    bundle = ExperimentBundle.create(
        samples=samples,
        decisions=decisions,
        cells=cells,
        prompts=prompts,
        runs=[run],
        results=[],
    )
    return bundle, cells, run


def _prompt_manifest(
    *, cells: list[ConditionCell], bundle: ExperimentBundle, token_counter: TokenCounter
) -> list[dict[str, Any]]:
    _require_equal(token_counter.identity, _TOKENIZER_IDENTITY, "prompt tokenizer")
    prompt_by_cell = {prompt.condition_cell_id: prompt for prompt in bundle.prompts}
    manifest: list[dict[str, Any]] = []
    for cell in cells:
        if not cell.eligible:
            manifest.append(
                {
                    "condition_cell_id": cell.cell_id,
                    "theorem_id": cell.theorem_id,
                    "condition": cell.condition,
                    "eligible": False,
                    "ineligibility_reasons": list(cell.ineligibility_reasons),
                    "prompt_id": None,
                    "prompt_hash": None,
                    "prompt_token_count": None,
                    "max_prompt_tokens": 1024,
                    "context_eligible": False,
                    "non_intervention_bytes_identical": None,
                }
            )
            continue
        prompt = prompt_by_cell[cell.cell_id]
        template = _prompt_template(cell.theorem_id)
        parity = inspect_prompt_parity(template, prompt)
        prompt_token_count = token_counter.count(prompt.prompt_bytes.decode("utf-8"))
        manifest.append(
            {
                "condition_cell_id": cell.cell_id,
                "theorem_id": cell.theorem_id,
                "condition": cell.condition,
                "eligible": True,
                "ineligibility_reasons": [],
                "prompt_id": prompt.prompt_id,
                "prompt_hash": prompt.prompt_hash,
                "prompt_token_count": prompt_token_count,
                "max_prompt_tokens": 1024,
                "context_eligible": prompt_token_count <= 1024,
                "non_intervention_bytes_identical": parity[
                    "non_intervention_bytes_identical"
                ],
            }
        )
    return manifest


def build_checkpoint_c_value(
    *, bundle_path: Path, token_counter: TokenCounter
) -> dict[str, Any]:
    """Build the C freeze from exact A v2/B v2 records and tokenizer evidence."""

    a_freeze = read_checkpoint_a_v2()
    b_freeze = read_checkpoint_b_v2()
    bundle, cells, run = _build_materialization()
    committed_bundle = read_bundle(bundle_path)
    _require_equal(committed_bundle, bundle, "bundle materialization")
    sample_by_id = {sample.sample_id: sample for sample in bundle.samples}
    prompt_manifest = _prompt_manifest(
        cells=cells, bundle=bundle, token_counter=token_counter
    )
    if not all(
        row["non_intervention_bytes_identical"] is True
        for row in prompt_manifest
        if row["eligible"]
    ):
        raise ValueError("checkpoint C prompt parity failed")
    if not all(row["context_eligible"] for row in prompt_manifest if row["eligible"]):
        raise ValueError("checkpoint C prompt exceeds the frozen context budget")
    ordered_cells = [
        {
            "submission_order": index,
            "theorem_id": cell.theorem_id,
            "logical_condition": _logical_condition_name(cell, sample_by_id),
            "condition_cell_id": cell.cell_id,
            "prompt_id": next(
                (
                    prompt.prompt_id
                    for prompt in bundle.prompts
                    if prompt.condition_cell_id == cell.cell_id
                ),
                None,
            ),
        }
        for index, cell in enumerate((item for item in cells if item.eligible), start=1)
    ]
    slot_mapping = [
        {
            "candidate_index": seed_index * 4 + within_seed_index,
            "candidate_order": seed_index * 4 + within_seed_index + 1,
            "seed": seed,
            "within_seed_candidate_index": within_seed_index,
        }
        for seed_index, seed in enumerate(run.seeds)
        for within_seed_index in range(4)
    ]
    codex_g = next(
        cell
        for cell in cells
        if cell.theorem_id == "G"
        and cell.condition == Condition.CODEX_REFERENCE_INTUITION.value
    )
    return {
        "schema_version": CHECKPOINT_C_SCHEMA_VERSION,
        "controlling_issue": "murillo128/mathia#32",
        "design_amendment": {
            "url": _DESIGN_AMENDMENT_URL,
            "authorization": "checkpoint_c_only_on_merged_a_v2_and_b_v2",
        },
        "frozen_at_utc": datetime.now(UTC)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z"),
        "source_contract": {
            "mathia_main_commit": _MATHIA_MAIN_COMMIT,
            "checkpoint_a_v2": {
                "path": "experiments/intuition_fertility/checkpoint_a_v2.json",
                "freeze_id": a_freeze.freeze_id,
                "artifact_sha256": _CHECKPOINT_A_V2_SHA256,
            },
            "checkpoint_b_v2": {
                "path": "experiments/intuition_fertility/checkpoint_b_v2.json",
                "freeze_id": b_freeze.freeze_id,
                "artifact_sha256": _CHECKPOINT_B_V2_SHA256,
            },
            "panel_id": PANEL_ID,
            "formal_prompt_resolution": _FORMAL_PROMPT_RESOLUTION,
        },
        "bundle": {
            "path": "experiments/intuition_fertility/checkpoint_c_bundle_v1.json",
            "artifact_sha256": _sha256_file(bundle_path),
            "bundle_id": bundle.bundle_id,
            "candidate_results_frozen": 0,
        },
        "formal_worker": run.to_dict(),
        "materialization": {
            "condition_cell_count": len(bundle.cells),
            "eligible_cell_count": sum(cell.eligible for cell in bundle.cells),
            "ineligible_cell_count": sum(not cell.eligible for cell in bundle.cells),
            "rendered_prompt_count": len(bundle.prompts),
            "formal_worker_run_count": len(bundle.runs),
            "candidate_result_count": len(bundle.results),
            "planned_candidate_slot_count": len(bundle.prompts) * run.candidate_budget,
            "primary_cell_count": sum(cell.theorem_id != "G" for cell in bundle.cells),
            "calibration_cell_count": sum(
                cell.theorem_id == "G" for cell in bundle.cells
            ),
            "donor_cell_count": sum(
                cell.condition
                in {
                    Condition.ADJACENT_CROSS_THEOREM_STRATEGY.value,
                    Condition.DISTANT_MISMATCHED_STRATEGY.value,
                }
                for cell in bundle.cells
            ),
            "codex_reference_g": {
                "condition_cell_id": codex_g.cell_id,
                "eligible": codex_g.eligible,
                "ineligibility_reasons": list(codex_g.ineligibility_reasons),
                "disposition": "preserved_ineligible_not_rendered_not_scheduled",
            },
        },
        "execution_plan": {
            "run_id": run.run_id,
            "run_order": run.to_dict()["generation_settings"]["run_order"],
            "logical_condition_order": list(_PRIMARY_LOGICAL_CONDITION_ORDER),
            "eligible_cell_submission_order_id": stable_id(
                "eligible_cell_submission_order", ordered_cells
            ),
            "eligible_cells": ordered_cells,
            "candidate_slot_mapping": slot_mapping,
        },
        "prompt_manifest": prompt_manifest,
        "gates": {
            "checkpoint_c_scope_only": True,
            "checkpoint_c_complete": True,
            "checkpoint_a_v2_and_b_v2_used_exactly": True,
            "qwen_lean_inference_performed": False,
            "lean_verification_performed": False,
            "gpu_work_performed": False,
            "historical_B_seed0_draws_opened": False,
            "candidate_outputs_or_item_level_results_exist": False,
            "phase4_checkpoint_used": False,
            "intermediate_phase5_checkpoint_used": False,
            "protected_formal_worker_execution_authorized": False,
            "checkpoint_d_authorized": False,
            "merge_or_auto_merge_authorized": False,
            "fresh_independent_review_required": True,
        },
    }


@dataclass(frozen=True)
class CheckpointCFreeze:
    value: dict[str, Any]
    bundle: ExperimentBundle
    freeze_id: str

    def to_summary(self) -> dict[str, Any]:
        return {
            "schema_version": self.value["schema_version"],
            "freeze_id": self.freeze_id,
            "bundle_id": self.bundle.bundle_id,
            "valid": True,
            **self.value["materialization"],
            "run_id": self.value["execution_plan"]["run_id"],
            "checkpoint_c_complete": self.value["gates"]["checkpoint_c_complete"],
            "protected_formal_worker_execution_authorized": self.value["gates"][
                "protected_formal_worker_execution_authorized"
            ],
            "checkpoint_d_authorized": self.value["gates"]["checkpoint_d_authorized"],
        }


def validate_checkpoint_c(
    value: dict[str, Any], *, bundle_path: str | Path = DEFAULT_CHECKPOINT_C_BUNDLE_PATH
) -> CheckpointCFreeze:
    require_exact_keys(
        value,
        required={
            "schema_version",
            "controlling_issue",
            "design_amendment",
            "frozen_at_utc",
            "source_contract",
            "bundle",
            "formal_worker",
            "materialization",
            "execution_plan",
            "prompt_manifest",
            "gates",
        },
        field="Checkpoint C",
    )
    _require_equal(value["schema_version"], CHECKPOINT_C_SCHEMA_VERSION, "schema")
    _require_equal(value["controlling_issue"], "murillo128/mathia#32", "issue")
    _require_equal(
        value["design_amendment"],
        {
            "url": _DESIGN_AMENDMENT_URL,
            "authorization": "checkpoint_c_only_on_merged_a_v2_and_b_v2",
        },
        "design amendment",
    )
    source = value["source_contract"]
    _require_equal(source["mathia_main_commit"], _MATHIA_MAIN_COMMIT, "main source")
    _require_equal(source["panel_id"], PANEL_ID, "panel")
    _require_equal(
        source["formal_prompt_resolution"],
        _FORMAL_PROMPT_RESOLUTION,
        "Phase-5 prompt resolution",
    )
    for name, expected_id, expected_sha in (
        ("checkpoint_a_v2", EXPECTED_CHECKPOINT_A_V2_ID, _CHECKPOINT_A_V2_SHA256),
        ("checkpoint_b_v2", EXPECTED_CHECKPOINT_B_V2_ID, _CHECKPOINT_B_V2_SHA256),
    ):
        binding = source[name]
        _require_equal(binding["freeze_id"], expected_id, f"{name} identity")
        _require_equal(binding["artifact_sha256"], expected_sha, f"{name} hash")
        _require_equal(
            _sha256_file(_REPOSITORY_ROOT / binding["path"]),
            expected_sha,
            f"{name} artifact",
        )

    actual_bundle_path = Path(bundle_path)
    bundle = read_bundle(actual_bundle_path)
    expected_bundle, ordered_cells, expected_run = _build_materialization()
    _require_equal(bundle, expected_bundle, "bundle content")
    _require_equal(value["bundle"]["bundle_id"], bundle.bundle_id, "bundle identity")
    _require_equal(
        value["bundle"]["artifact_sha256"],
        _sha256_file(actual_bundle_path),
        "bundle hash",
    )
    _require_equal(value["bundle"]["candidate_results_frozen"], 0, "result freeze")
    _require_equal(value["formal_worker"], expected_run.to_dict(), "formal worker")

    materialization = value["materialization"]
    _require_equal(materialization["condition_cell_count"], 59, "cell count")
    _require_equal(materialization["eligible_cell_count"], 58, "eligible count")
    _require_equal(materialization["ineligible_cell_count"], 1, "ineligible count")
    _require_equal(materialization["rendered_prompt_count"], 58, "prompt count")
    _require_equal(materialization["formal_worker_run_count"], 1, "run count")
    _require_equal(materialization["candidate_result_count"], 0, "result count")
    _require_equal(materialization["planned_candidate_slot_count"], 928, "slot count")
    _require_equal(materialization["primary_cell_count"], 54, "primary cells")
    _require_equal(materialization["calibration_cell_count"], 5, "calibration cells")
    _require_equal(materialization["donor_cell_count"], 24, "donor cells")

    ineligible = [cell for cell in bundle.cells if not cell.eligible]
    _require_equal(len(ineligible), 1, "single ineligible cell")
    codex_g = ineligible[0]
    _require_equal(codex_g.theorem_id, "G", "ineligible theorem")
    _require_equal(
        codex_g.condition,
        Condition.CODEX_REFERENCE_INTUITION.value,
        "ineligible condition",
    )
    _require_equal(
        materialization["codex_reference_g"],
        {
            "condition_cell_id": codex_g.cell_id,
            "eligible": False,
            "ineligibility_reasons": ["leakage_label_borderline"],
            "disposition": "preserved_ineligible_not_rendered_not_scheduled",
        },
        "Codex-G preservation",
    )

    sample_by_id = {sample.sample_id: sample for sample in bundle.samples}
    prompt_by_cell = {prompt.condition_cell_id: prompt for prompt in bundle.prompts}
    expected_order = [
        {
            "submission_order": index,
            "theorem_id": cell.theorem_id,
            "logical_condition": _logical_condition_name(cell, sample_by_id),
            "condition_cell_id": cell.cell_id,
            "prompt_id": prompt_by_cell[cell.cell_id].prompt_id,
        }
        for index, cell in enumerate(
            (item for item in ordered_cells if item.eligible), start=1
        )
    ]
    plan = value["execution_plan"]
    _require_equal(plan["run_id"], expected_run.run_id, "planned run")
    _require_equal(
        plan["run_order"],
        "for_each_seed_ascending_submit_eligible_cells_in_theorem_id_then_logical_condition_order",
        "run order",
    )
    _require_equal(
        plan["logical_condition_order"],
        list(_PRIMARY_LOGICAL_CONDITION_ORDER),
        "condition order",
    )
    _require_equal(plan["eligible_cells"], expected_order, "cell submission order")
    _require_equal(
        plan["eligible_cell_submission_order_id"],
        stable_id("eligible_cell_submission_order", expected_order),
        "cell submission order identity",
    )
    expected_slots = [
        {
            "candidate_index": seed_index * 4 + within,
            "candidate_order": seed_index * 4 + within + 1,
            "seed": seed,
            "within_seed_candidate_index": within,
        }
        for seed_index, seed in enumerate((1, 2, 3, 4))
        for within in range(4)
    ]
    _require_equal(plan["candidate_slot_mapping"], expected_slots, "candidate slots")

    manifest = value["prompt_manifest"]
    _require_equal(len(manifest), 59, "prompt manifest count")
    _require_equal(
        [row["condition_cell_id"] for row in manifest],
        [cell.cell_id for cell in ordered_cells],
        "prompt manifest order",
    )
    for row, cell in zip(manifest, ordered_cells, strict=True):
        _require_equal(row["theorem_id"], cell.theorem_id, "prompt theorem")
        _require_equal(row["condition"], cell.condition, "prompt condition")
        _require_equal(row["eligible"], cell.eligible, "prompt eligibility")
        _require_equal(
            row["ineligibility_reasons"],
            list(cell.ineligibility_reasons),
            "prompt ineligibility",
        )
        _require_equal(row["max_prompt_tokens"], 1024, "prompt context budget")
        if not cell.eligible:
            for field in (
                "prompt_id",
                "prompt_hash",
                "prompt_token_count",
                "non_intervention_bytes_identical",
            ):
                _require_equal(row[field], None, f"ineligible {field}")
            _require_equal(row["context_eligible"], False, "ineligible context")
            continue
        prompt = prompt_by_cell[cell.cell_id]
        _require_equal(row["prompt_id"], prompt.prompt_id, "prompt id")
        _require_equal(row["prompt_hash"], prompt.prompt_hash, "prompt hash")
        if (
            not isinstance(row["prompt_token_count"], int)
            or isinstance(row["prompt_token_count"], bool)
            or row["prompt_token_count"] < 0
        ):
            raise ValueError("checkpoint C prompt token count is invalid")
        _require_equal(row["context_eligible"], True, "prompt context")
        _require_equal(row["non_intervention_bytes_identical"], True, "prompt parity")
        parity = inspect_prompt_parity(_prompt_template(cell.theorem_id), prompt)
        _require_equal(
            parity["non_intervention_bytes_identical"], True, "rendered parity"
        )

    gates = value["gates"]
    for field in (
        "qwen_lean_inference_performed",
        "lean_verification_performed",
        "gpu_work_performed",
        "historical_B_seed0_draws_opened",
        "candidate_outputs_or_item_level_results_exist",
        "phase4_checkpoint_used",
        "intermediate_phase5_checkpoint_used",
        "protected_formal_worker_execution_authorized",
        "checkpoint_d_authorized",
        "merge_or_auto_merge_authorized",
    ):
        _require_equal(gates[field], False, f"gate {field}")
    for field in (
        "checkpoint_c_scope_only",
        "checkpoint_c_complete",
        "checkpoint_a_v2_and_b_v2_used_exactly",
        "fresh_independent_review_required",
    ):
        _require_equal(gates[field], True, f"gate {field}")

    freeze_id = stable_id("checkpoint_c", value)
    _require_equal(freeze_id, EXPECTED_CHECKPOINT_C_ID, "content id")
    return CheckpointCFreeze(value=value, bundle=bundle, freeze_id=freeze_id)


def read_checkpoint_c(
    path: str | Path = DEFAULT_CHECKPOINT_C_PATH,
    *,
    bundle_path: str | Path = DEFAULT_CHECKPOINT_C_BUNDLE_PATH,
) -> CheckpointCFreeze:
    try:
        value = json.loads(Path(path).read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError("Checkpoint-C artifact is not valid JSON") from error
    if not isinstance(value, dict):
        raise ValueError("Checkpoint-C artifact must be a JSON object")
    return validate_checkpoint_c(value, bundle_path=bundle_path)


def write_checkpoint_c(
    *,
    token_counter: TokenCounter,
    path: str | Path = DEFAULT_CHECKPOINT_C_PATH,
    bundle_path: str | Path = DEFAULT_CHECKPOINT_C_BUNDLE_PATH,
) -> str:
    """Write both C artifacts once; this function never performs formal inference."""

    output_bundle = Path(bundle_path)
    output_freeze = Path(path)
    if output_bundle.exists() or output_freeze.exists():
        raise RuntimeError("refusing to replace a frozen Checkpoint-C artifact")
    bundle, _, _ = _build_materialization()
    write_bundle(output_bundle, bundle)
    value = build_checkpoint_c_value(
        bundle_path=output_bundle, token_counter=token_counter
    )
    rendered = (canonical_json(value) + "\n").encode("utf-8")
    descriptor = os.open(output_freeze, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
    with os.fdopen(descriptor, "wb") as output:
        output.write(rendered)
    return stable_id("checkpoint_c", value)
