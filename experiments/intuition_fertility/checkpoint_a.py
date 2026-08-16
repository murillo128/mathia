"""Strict loader for the issue #32 Checkpoint-A pre-registration artifact."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .canonical import canonical_json, require_exact_keys, stable_id, text_sha256
from .panel import (
    ADJACENT_DONORS,
    DISTANT_DONORS,
    INTUITION_REQUEST,
    PANEL_ID,
    PANEL_VERSION,
    Presentation,
    generator_payload,
    get_target_identity,
    panel_snapshot,
)
from .prompts import (
    COMMENT_CLOSE,
    COMMENT_OPEN,
    PROMPT_SCHEMA_VERSION,
    PROMPT_TEMPLATE_SCHEMA_VERSION,
    WHOLE_PROOF_CONTINUATION,
)
from .records import MAX_GUIDANCE_TOKENS

CHECKPOINT_A_SCHEMA_VERSION = "intuition_fertility_checkpoint_a_v1"
DEFAULT_CHECKPOINT_A_PATH = Path(__file__).with_name("checkpoint_a_v1.json")
EXPECTED_CHECKPOINT_A_ID = (
    "checkpoint_a_68dc6f09ac292213b4734ec2c6d87d91c5952a217d64e1bdd30cdd354c762f2d"
)
LEAKAGE_REVIEW_PROMPT_TEMPLATE = (
    "Classify proof transmission only. Do not judge mathematical correctness, elegance, "
    "expected proof success, or similarity to another explanation.\n\n"
    "Labels:\n"
    "- strategic: gives a mechanism, representation, obstruction, or a small number of "
    "subgoals while leaving substantial local mathematical and formal proof work unresolved.\n"
    "- borderline: gives an ordered local derivation or implementation skeleton that resolves "
    "a major proof subproblem enough to make causal interpretation unsafe.\n"
    "- proof_like: supplies a near-complete proof route, detailed induction/case structure, "
    "exact coefficient/constructor derivation, exact lemma chain, Lean code, tactics, or "
    "equivalent transcription-ready content.\n\n"
    "Set uncertain to true if the rubric does not determine a clear label. Return only the "
    "required JSON object.\n\n"
    "Theorem statement:\n{theorem_statement}\n\n"
    "Candidate guidance:\n{candidate_guidance}\n"
)
_REPOSITORY_ROOT = Path(__file__).parents[2]
_CONTRACT_FILE_HASHES = {
    "docs/INTUITION_FERTILITY_PRETEST_V3.md": "430ba1c893e3c94dcdfff21845e42a45c178edbf17cdc4c3ffbf69d6fd922122",
    "docs/INTUITION_FERTILITY_PANEL_V2.md": "14e6839b65dded3acdbda4ab171089d403d1ee446347833a65dd306453495dd1",
    "docs/INTUITION_FERTILITY_TARGET_IDENTITY_AUDIT_V1.md": "aa0cb021a5cc6aeb60432451f5c33020a537035f0101378cca090675159047b6",
}
_HARNESS_FILE_HASHES = {
    "experiments/intuition_fertility/panel.py": "5683b31e5982ef37691d7672a976ef2551bc34cd017038b85586c9af7caa39f7",
    "experiments/intuition_fertility/_private_panel.py": "fe9ce47d16b353a3ac404b3990d91f89379d7417b3dccc09c8ce2f9cfe095b74",
    "experiments/intuition_fertility/prompts.py": "24de593ac7cbaa19ab5c434ff9bc734c91398d7ab4890c0e5d77bc2a8d47c2ef",
    "experiments/intuition_fertility/metrics.py": "0157c6158011d5255cc01ba0703fe671951c91b99a26afb962e7bb584df6455d",
}


def render_generator_prompt(theorem_id: str) -> str:
    """Render the exact common, standard-presentation generator prompt."""

    payload = generator_payload(theorem_id, Presentation.STANDARD)
    return (
        f"Theorem statement:\n{payload['theorem_statement']}\n\n"
        f"Request:\n{payload['intuition_request']}\n\nStrategy:\n"
    )


def render_leakage_review_prompt(
    *, theorem_statement: str, candidate_guidance: str
) -> str:
    """Render the exact blinded classifier prompt without other sample context."""

    return LEAKAGE_REVIEW_PROMPT_TEMPLATE.replace(
        "{theorem_statement}", theorem_statement
    ).replace("{candidate_guidance}", candidate_guidance)


def _expected_target_records() -> list[dict[str, Any]]:
    fields = (
        "theorem_id",
        "role",
        "canonical_target",
        "reported_artifact_target",
        "record_id",
        "record_local_declaration_name",
        "record_declaration_hash",
        "source_path",
        "source_revision",
        "phase2_status",
    )
    return [
        {field: getattr(get_target_identity(theorem_id), field) for field in fields}
        for theorem_id in "ABCDEFG"
    ]


def _require_equal(actual: Any, expected: Any, field: str) -> None:
    if actual != expected:
        raise ValueError(f"checkpoint A {field} does not match the frozen contract")


def _validate_frozen_files(expected: dict[str, str]) -> None:
    for relative_path, digest in expected.items():
        actual = hashlib.sha256(
            (_REPOSITORY_ROOT / relative_path).read_bytes()
        ).hexdigest()
        _require_equal(actual, digest, f"source file {relative_path}")


@dataclass(frozen=True)
class CheckpointAFreeze:
    value: dict[str, Any]
    freeze_id: str

    @property
    def protected_execution_authorized(self) -> bool:
        return self.value["gates"]["protected_formal_worker_execution_authorized"]

    @property
    def blocker_code(self) -> str:
        return self.value["formal_worker_binding"]["blocker_code"]

    def to_summary(self) -> dict[str, Any]:
        return {
            "schema_version": self.value["schema_version"],
            "freeze_id": self.freeze_id,
            "valid": True,
            "protected_formal_worker_execution_authorized": (
                self.protected_execution_authorized
            ),
            "blocker_code": self.blocker_code,
        }


def validate_checkpoint_a(value: dict[str, Any]) -> CheckpointAFreeze:
    """Reject any drift from the reviewed Checkpoint-A decisions."""

    require_exact_keys(
        value,
        required={
            "schema_version",
            "controlling_issue",
            "frozen_at_utc",
            "source_contract",
            "panel",
            "generator_protocol",
            "sample_policy",
            "leakage_policy",
            "condition_materialization",
            "formal_worker_binding",
            "formal_worker_generation",
            "prompt_contract",
            "analysis_contract",
            "gates",
            "evidence_basis",
        },
        field="checkpoint A",
    )
    _require_equal(value["schema_version"], CHECKPOINT_A_SCHEMA_VERSION, "schema")
    _require_equal(value["controlling_issue"], "murillo128/mathia#32", "issue")

    source = value["source_contract"]
    _require_equal(
        source["accepted_mathia_main_commit"],
        "185754c55344760ac44365915643bdae447b3416",
        "accepted source commit",
    )
    _require_equal(
        source["contract_files_sha256"], _CONTRACT_FILE_HASHES, "contract file hashes"
    )
    _require_equal(
        source["harness_files_sha256"], _HARNESS_FILE_HASHES, "harness file hashes"
    )
    _validate_frozen_files({**_CONTRACT_FILE_HASHES, **_HARNESS_FILE_HASHES})

    panel = value["panel"]
    _require_equal(panel["panel_version"], PANEL_VERSION, "panel version")
    _require_equal(panel["panel_id"], PANEL_ID, "panel id")
    _require_equal(
        panel["panel_snapshot_sha256"],
        text_sha256(canonical_json(panel_snapshot(include_private=True))),
        "panel snapshot hash",
    )
    _require_equal(panel["presentation"], Presentation.STANDARD.value, "presentation")
    _require_equal(panel["primary_theorem_ids"], list("ABCDEF"), "primary panel")
    _require_equal(panel["calibration_theorem_ids"], ["G"], "calibration panel")
    _require_equal(
        panel["target_records"], _expected_target_records(), "target records"
    )
    _require_equal(
        panel["generator_payload_sha256"],
        {
            theorem_id: text_sha256(
                canonical_json(generator_payload(theorem_id, Presentation.STANDARD))
            )
            for theorem_id in "ABCDEFG"
        },
        "generator payload hashes",
    )
    _require_equal(
        panel["genericity_variants_in_primary_analysis"],
        False,
        "genericity separation",
    )

    generator = value["generator_protocol"]
    _require_equal(
        generator["intuition_request"], INTUITION_REQUEST, "intuition request"
    )
    _require_equal(
        generator["prompt_template"],
        "Theorem statement:\n{theorem_statement}\n\nRequest:\n{intuition_request}\n\nStrategy:\n",
        "generator prompt template",
    )
    _require_equal(
        generator["prompt_sha256"],
        {
            theorem_id: text_sha256(render_generator_prompt(theorem_id))
            for theorem_id in "ABCDEFG"
        },
        "generator prompt hashes",
    )
    qwen = generator["qwen_base"]
    for field in ("model", "revision", "tokenizer", "tokenizer_revision"):
        expected = (
            "Qwen/Qwen3-8B-Base"
            if field in {"model", "tokenizer"}
            else "49e3418fbbbca6ecbdf9608b4d22e5a407081db4"
        )
        _require_equal(qwen[field], expected, f"Qwen {field}")
    _require_equal(qwen["chat_template"], None, "Qwen chat template")
    _require_equal(qwen["add_special_tokens"], False, "Qwen special tokens")
    _require_equal(qwen["max_new_tokens"], 96, "Qwen output limit")
    _require_equal(qwen["do_sample"], False, "Qwen decoding")
    _require_equal(qwen["sample_count"], 1, "Qwen sample count")
    _require_equal(qwen["seed"], 0, "Qwen seed")
    codex = generator["codex_reference"]
    _require_equal(codex["product"], "OpenAI Codex CLI", "Codex product")
    _require_equal(codex["cli_version"], "0.147.0", "Codex CLI version")
    _require_equal(codex["model"], "gpt-5.6-sol", "Codex model")
    _require_equal(codex["reasoning_effort"], "xhigh", "Codex reasoning effort")
    _require_equal(codex["sample_count"], 1, "Codex sample count")
    _require_equal(codex["session"], "fresh_ephemeral_per_theorem", "Codex session")
    _require_equal(codex["tool_calls_allowed"], False, "Codex tool isolation")

    samples = value["sample_policy"]
    _require_equal(samples["samples_per_theorem_per_generator"], 1, "sample count")
    _require_equal(samples["selected_sample_indexes"], [0], "sample indexes")
    _require_equal(samples["regeneration_attempts"], 0, "regeneration budget")
    _require_equal(
        samples["maximum_guidance_tokens"], MAX_GUIDANCE_TOKENS, "guidance cap"
    )
    _require_equal(
        samples["over_budget_action"], "preserve_ineligible_cell", "over-budget action"
    )
    _require_equal(
        samples["missing_or_ineligible_action"],
        "preserve_missing_or_ineligible_cell_without_replacement",
        "missing-sample action",
    )

    leakage = value["leakage_policy"]
    _require_equal(
        leakage["labels"], ["strategic", "borderline", "proof_like"], "leakage labels"
    )
    _require_equal(leakage["uncertain_or_disputed"], "borderline", "leakage fallback")
    _require_equal(leakage["reviewer_count"], 2, "leakage reviewer count")
    _require_equal(
        leakage["review_prompt_template"],
        LEAKAGE_REVIEW_PROMPT_TEMPLATE,
        "leakage review prompt",
    )
    _require_equal(
        leakage["review_prompt_template_sha256"],
        text_sha256(LEAKAGE_REVIEW_PROMPT_TEMPLATE),
        "leakage review prompt hash",
    )
    _require_equal(leakage["blind_to_generator_identity"], True, "classifier blinding")
    _require_equal(leakage["blind_to_private_metadata"], True, "classifier privacy")
    _require_equal(leakage["blind_to_formal_worker_outcomes"], True, "outcome blinding")

    conditions = value["condition_materialization"]
    _require_equal(conditions["adjacent_donors"], ADJACENT_DONORS, "adjacent donors")
    _require_equal(conditions["distant_donors"], DISTANT_DONORS, "distant donors")
    _require_equal(conditions["mathia_intuition_included"], False, "Mathia exclusion")
    _require_equal(
        conditions["primary_cell_count_before_ineligibility"], 54, "primary cells"
    )
    _require_equal(
        conditions["calibration_cell_count_before_ineligibility"], 5, "G cells"
    )

    worker = value["formal_worker_binding"]
    _require_equal(
        worker["status"], "blocked_pending_phase5_selected_adapter", "worker status"
    )
    _require_equal(worker["blocker_code"], "PENDING_PHASE5_SELECTED_ADAPTER", "blocker")
    _require_equal(worker["dependency"], "murillo128/qwen-lean#19", "worker dependency")
    _require_equal(worker["phase4_allowed"], False, "Phase 4 prohibition")
    _require_equal(
        worker["intermediate_phase5_allowed"], False, "Phase 5 midpoint prohibition"
    )
    if not worker["required_binding_fields"]:
        raise ValueError("checkpoint A worker binding fields must be explicit")

    formal = value["formal_worker_generation"]
    _require_equal(formal["candidate_budget_per_eligible_cell"], 16, "candidate budget")
    _require_equal(formal["repeat_seeds"], [0, 1, 2, 3], "formal seeds")
    _require_equal(formal["candidates_per_seed"], 4, "candidates per seed")
    _require_equal(formal["do_sample"], True, "formal sampling")
    _require_equal(formal["temperature"], 0.8, "formal temperature")
    _require_equal(formal["top_p"], 0.95, "formal top-p")
    _require_equal(formal["top_k"], -1, "formal top-k")
    _require_equal(formal["max_new_tokens"], 1024, "formal output limit")
    _require_equal(formal["max_model_len"], 2048, "formal model length")
    _require_equal(formal["verifier_timeout_seconds"], 300.0, "verifier timeout")
    if formal["candidate_budget_per_eligible_cell"] != (
        len(formal["repeat_seeds"]) * formal["candidates_per_seed"]
    ):
        raise ValueError(
            "checkpoint A candidate budget does not match its repeat policy"
        )

    prompt = value["prompt_contract"]
    _require_equal(prompt["schema_version"], PROMPT_SCHEMA_VERSION, "prompt schema")
    _require_equal(
        prompt["template_schema_version"],
        PROMPT_TEMPLATE_SCHEMA_VERSION,
        "prompt template schema",
    )
    _require_equal(prompt["comment_open_utf8"], COMMENT_OPEN.decode(), "comment open")
    _require_equal(
        prompt["comment_close_utf8"], COMMENT_CLOSE.decode(), "comment close"
    )
    _require_equal(
        prompt["whole_proof_continuation_utf8"],
        WHOLE_PROOF_CONTINUATION.decode(),
        "whole-proof continuation",
    )
    _require_equal(prompt["non_intervention_bytes_identical"], True, "prompt parity")
    _require_equal(
        prompt["semantic_padding_or_truncation_allowed"], False, "prompt mutation"
    )

    analysis = value["analysis_contract"]
    required_metrics = {
        "verified_candidate_count",
        "verified_rate",
        "pass_at_k",
        "completeness_status",
        "matched_deltas",
        "adjacent_transfer_outcome",
        "relevant_distant_length_eligibility",
        "leakage_rates",
        "first_verified_candidate_rank",
        "generated_tokens_to_first_verified",
        "theorem_floor_ceiling_status",
    }
    if not required_metrics.issubset(analysis["per_theorem_condition_metrics"]):
        raise ValueError("checkpoint A analysis omits a required theorem-level metric")
    _require_equal(
        analysis["primary_theorem_ids"], list("ABCDEF"), "analysis primaries"
    )
    _require_equal(analysis["calibration_reported_separately"], "G", "G separation")
    _require_equal(analysis["missing_cell_imputation"], None, "missing-cell handling")
    _require_equal(
        analysis["opaque_primary_aggregate"], None, "opaque aggregate prohibition"
    )

    gates = value["gates"]
    _require_equal(gates["checkpoint_a_scope_only"], True, "execution scope")
    _require_equal(gates["qwen_inference_performed"], False, "Qwen execution claim")
    _require_equal(gates["codex_generation_performed"], False, "Codex execution claim")
    _require_equal(
        gates["qwen_lean_inference_performed"], False, "qwen-lean execution claim"
    )
    _require_equal(gates["gpu_work_performed"], False, "GPU execution claim")
    _require_equal(
        gates["protected_formal_worker_execution_authorized"],
        False,
        "protected execution gate",
    )

    freeze_id = stable_id("checkpoint_a", value)
    _require_equal(freeze_id, EXPECTED_CHECKPOINT_A_ID, "content id")
    return CheckpointAFreeze(value=value, freeze_id=freeze_id)


def read_checkpoint_a(
    path: str | Path = DEFAULT_CHECKPOINT_A_PATH,
) -> CheckpointAFreeze:
    try:
        value = json.loads(Path(path).read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError("checkpoint A artifact is not valid JSON") from error
    if not isinstance(value, dict):
        raise ValueError("checkpoint A artifact must be a JSON object")
    return validate_checkpoint_a(value)
