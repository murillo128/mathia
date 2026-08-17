"""Strict loader for the issue #32 Checkpoint-A v2 freeze."""

from __future__ import annotations

import copy
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .canonical import canonical_json, require_exact_keys, stable_id, text_sha256
from .checkpoint_a import (
    DEFAULT_CHECKPOINT_A_PATH,
    EXPECTED_CHECKPOINT_A_ID,
    CheckpointAFreeze,
    read_checkpoint_a,
)

CHECKPOINT_A_V2_SCHEMA_VERSION = "intuition_fertility_checkpoint_a_v2"
DEFAULT_CHECKPOINT_A_V2_PATH = Path(__file__).with_name("checkpoint_a_v2.json")
EXPECTED_CHECKPOINT_A_V2_ID = (
    "checkpoint_a_v2_bf521c46c79d64ac7e250989e82cb58cdadec40e08de2159839ad4c15ed688dc"
)
_V1_ARTIFACT_SHA256 = "a50372c672db60edd650aa5bdd36ef30af90c45b097d5dbd57de69e43db842f9"
_UNCHANGED_SECTION_SHA256 = {
    "source_contract": "72f63d6e90b1266cacc97c9c14c1946f31975466072bfbcd265e4adea0c2a16c",
    "panel": "15cd0879a7d248731c25c2c963b2f9da52d7ac5be82b9d8d38c3fa65a6287313",
    "generator_protocol": "ce267d841a7edab1f63d567dd56ba4ad575111f842130dcef0648b60240de7e2",
    "sample_policy": "a85d828cce19b9201b91496125898b7b4e94c229b60f2b86f3fc5bce18351631",
    "leakage_policy": "1439eb55bc4f635b1129330b13f11fdb00538aa0091df9905327e3e58214a892",
    "condition_materialization": (
        "8903ecb35e186a9b960716f042f5cfff25b23174ee38482c62bb425020351154"
    ),
    "formal_worker_binding": (
        "174d61e4e054bfb5e0e415244b9c3d19512dc3217541cb5b11ea334337cb7878"
    ),
    "prompt_contract": "0e6e5a49f4d5564809d465d92410a4d0baa6bfc6dfed177a9dfaf03259ebfa41",
    "analysis_contract": (
        "f18133d27e111401c77a20b73d5644d78d6a960eaf2939b52583986b27fcb033"
    ),
}
_TARGET_IDS = tuple("ABCDEFG")
_PROTECTED_SEED_COUNT = 4


def _require_equal(actual: Any, expected: Any, field: str) -> None:
    if actual != expected:
        raise ValueError(f"checkpoint A v2 {field} does not match the frozen contract")


def derive_first_unused_seeds(
    historical_draws: list[dict[str, Any]], *, count: int = _PROTECTED_SEED_COUNT
) -> list[int]:
    """Derive the first nonnegative formal-worker seeds absent from prior draws."""

    if not isinstance(count, int) or isinstance(count, bool) or count <= 0:
        raise ValueError("checkpoint A v2 seed count must be a positive integer")
    used: set[int] = set()
    for draw in historical_draws:
        seed = draw.get("seed")
        if not isinstance(seed, int) or isinstance(seed, bool) or seed < 0:
            raise ValueError(
                "checkpoint A v2 historical draw seeds must be nonnegative integers"
            )
        used.add(seed)
    selected: list[int] = []
    candidate = 0
    while len(selected) < count:
        if candidate not in used:
            selected.append(candidate)
        candidate += 1
    return selected


@dataclass(frozen=True)
class CheckpointAV2Freeze:
    value: dict[str, Any]
    base_v1: CheckpointAFreeze
    freeze_id: str

    @property
    def protected_execution_authorized(self) -> bool:
        return self.value["gates"]["protected_formal_worker_execution_authorized"]

    @property
    def protected_seeds(self) -> list[int]:
        return list(self.value["formal_worker_generation"]["repeat_seeds"])

    def materialized_scientific_contract(self) -> dict[str, Any]:
        """Return the unchanged v1 contract with only the reviewed seed delta."""

        materialized = {
            name: copy.deepcopy(self.base_v1.value[name])
            for name in _UNCHANGED_SECTION_SHA256
        }
        materialized["formal_worker_generation"] = copy.deepcopy(
            self.value["formal_worker_generation"]
        )
        return materialized

    def to_summary(self) -> dict[str, Any]:
        return {
            "schema_version": self.value["schema_version"],
            "freeze_id": self.freeze_id,
            "valid": True,
            "checkpoint_status": self.value["checkpoint_status"]["status"],
            "checkpoint_a_v2_freeze_complete": self.value["gates"][
                "checkpoint_a_v2_freeze_complete"
            ],
            "historical_draw_count": len(
                self.value["historical_execution_audit"]["historical_draws"]
            ),
            "burned_seeds": self.value["seed_derivation"]["used_seeds"],
            "protected_seeds": self.protected_seeds,
            "candidates_per_seed": self.value["formal_worker_generation"][
                "candidates_per_seed"
            ],
            "candidate_budget_per_eligible_cell": self.value[
                "formal_worker_generation"
            ]["candidate_budget_per_eligible_cell"],
            "protected_formal_worker_execution_authorized": (
                self.protected_execution_authorized
            ),
            "checkpoints_b_through_f_authorized": self.value["gates"][
                "checkpoints_b_through_f_authorized"
            ],
        }


def _validate_base_v1(path: str | Path) -> CheckpointAFreeze:
    base_path = Path(path)
    actual_sha256 = hashlib.sha256(base_path.read_bytes()).hexdigest()
    _require_equal(actual_sha256, _V1_ARTIFACT_SHA256, "historical v1 artifact hash")
    base = read_checkpoint_a(base_path)
    _require_equal(base.freeze_id, EXPECTED_CHECKPOINT_A_ID, "historical v1 id")
    return base


def validate_checkpoint_a_v2(
    value: dict[str, Any], *, base_v1_path: str | Path = DEFAULT_CHECKPOINT_A_PATH
) -> CheckpointAV2Freeze:
    """Reject drift outside the seed-only amendment and its blind audit ledger."""

    require_exact_keys(
        value,
        required={
            "schema_version",
            "controlling_issue",
            "design_amendment",
            "frozen_at_utc",
            "checkpoint_status",
            "historical_checkpoint_a_v1",
            "unchanged_contract",
            "historical_execution_audit",
            "seed_derivation",
            "formal_worker_generation",
            "gates",
        },
        field="checkpoint A v2",
    )
    _require_equal(value["schema_version"], CHECKPOINT_A_V2_SCHEMA_VERSION, "schema")
    _require_equal(value["controlling_issue"], "murillo128/mathia#32", "issue")

    amendment = value["design_amendment"]
    _require_equal(amendment["issue_comment_id"], 5313977571, "design amendment")
    _require_equal(
        amendment["url"],
        "https://github.com/murillo128/mathia/issues/32#issuecomment-5313977571",
        "design amendment URL",
    )

    status = value["checkpoint_status"]
    _require_equal(status["checkpoint_a_v2_freeze_complete"], True, "freeze status")
    _require_equal(status["blocker_code"], None, "blocker")
    _require_equal(
        status["panel_disposition"],
        "retain_B_and_all_other_v1_targets_unchanged",
        "B retention",
    )
    _require_equal(
        status["scientific_contract_delta"],
        "formal_worker_repeat_seeds_only",
        "allowed delta",
    )

    historical_v1 = value["historical_checkpoint_a_v1"]
    _require_equal(historical_v1["pull_request"], "murillo128/mathia#37", "v1 PR")
    _require_equal(
        historical_v1["head_commit"],
        "76d64ddb61825bf76a6fc12f5d26b1facad59fcf",
        "v1 commit",
    )
    _require_equal(historical_v1["artifact_sha256"], _V1_ARTIFACT_SHA256, "v1 hash")
    _require_equal(historical_v1["freeze_id"], EXPECTED_CHECKPOINT_A_ID, "v1 id")
    _require_equal(historical_v1["mutated_by_v2"], False, "v1 preservation")

    base_v1 = _validate_base_v1(base_v1_path)
    section_hashes = {
        name: text_sha256(canonical_json(base_v1.value[name]))
        for name in _UNCHANGED_SECTION_SHA256
    }
    _require_equal(section_hashes, _UNCHANGED_SECTION_SHA256, "base section hashes")
    _require_equal(
        value["unchanged_contract"]["section_sha256"],
        _UNCHANGED_SECTION_SHA256,
        "unchanged section hashes",
    )

    audit = value["historical_execution_audit"]
    _require_equal(audit["method"], "membership_and_run_metadata_only", "audit method")
    _require_equal(
        audit["qwen_lean_source_commit"],
        "ef09f5e0f11a54a25fcb95b324d766f675be49a3",
        "audit source commit",
    )
    evidence_hashes = {
        source["path"]: source["sha256"] for source in audit["metadata_sources"]
    }
    _require_equal(
        evidence_hashes,
        {
            "evidence/phase5/workloads.json": (
                "6e73c71cc09a042c9078f72a1e3260b96ff35034acdf8192b494e366757b4e45"
            ),
            "evidence/phase5/heldout-comparison.json": (
                "fd9d0443c9a9f83f792522c2959bd22a8f052d40ffe1e206695b751ba47cb6e0"
            ),
            "evidence/phase5/adapter-reload.json": (
                "2f7c7507eb61225ce2d6084345e8a41678fd9fc46c1060e9d86d7f21491d6c0a"
            ),
            "evidence/phase5/minif2f.json": (
                "3feb898e181bf526eef1bd911d2d828a425a1c4e7e9fa692f2673f3ee3d8dff4"
            ),
        },
        "audit evidence hashes",
    )

    target_records = base_v1.value["panel"]["target_records"]
    expected_targets = [
        {"theorem_id": record["theorem_id"], "record_id": record["record_id"]}
        for record in target_records
    ]
    observed_targets = [
        {"theorem_id": record["theorem_id"], "record_id": record["record_id"]}
        for record in audit["target_membership"]
    ]
    _require_equal(observed_targets, expected_targets, "audited A-G membership")
    _require_equal(
        [record["theorem_id"] for record in target_records],
        list(_TARGET_IDS),
        "base target order",
    )
    overlapping_targets = [
        record["theorem_id"]
        for record in audit["target_membership"]
        if record["candidate_generation_memberships"]
    ]
    _require_equal(overlapping_targets, ["B"], "historical target overlaps")
    b_membership = audit["target_membership"][1]["candidate_generation_memberships"]
    _require_equal(
        b_membership,
        [
            {
                "workload_id": "phase5-heldout512-v1",
                "selected_record_index_zero_based": 351,
                "selected_record_position_one_based": 352,
                "condition": "no_guidance",
                "seed": 0,
                "candidate_indexes": [0, 1, 2, 3],
            }
        ],
        "historical B membership",
    )

    draws = audit["historical_draws"]
    _require_equal(len(draws), 4, "historical draw count")
    _require_equal(
        [draw["candidate_index"] for draw in draws],
        [0, 1, 2, 3],
        "historical candidate indexes",
    )
    for draw in draws:
        _require_equal(draw["theorem_id"], "B", "historical draw target")
        _require_equal(draw["condition"], "no_guidance", "historical condition")
        _require_equal(draw["seed"], 0, "historical seed")
        _require_equal(draw["burned"], True, "burned disposition")
        _require_equal(draw["sealed"], True, "sealed disposition")
        _require_equal(draw["excluded"], True, "excluded disposition")

    blinding = audit["outcome_blinding"]
    for field in (
        "candidate_outputs_opened",
        "item_level_verification_results_opened",
        "aggregate_outcomes_used_for_draw_selection",
        "historical_draws_may_enter_future_bundles_or_metrics",
    ):
        _require_equal(blinding[field], False, f"outcome blinding {field}")

    derived = derive_first_unused_seeds(draws)
    seed_derivation = value["seed_derivation"]
    _require_equal(seed_derivation["used_seeds"], [0], "burned seed set")
    _require_equal(seed_derivation["derived_protected_seeds"], derived, "derived seeds")
    _require_equal(derived, [1, 2, 3, 4], "protected seeds")

    formal = value["formal_worker_generation"]
    expected_formal = copy.deepcopy(base_v1.value["formal_worker_generation"])
    expected_formal["repeat_seeds"] = derived
    expected_formal["same_seed_set_across_theorems_A_to_G"] = True
    _require_equal(formal, expected_formal, "formal-worker generation")
    _require_equal(
        formal["candidate_budget_per_eligible_cell"],
        len(formal["repeat_seeds"]) * formal["candidates_per_seed"],
        "candidate budget",
    )

    gates = value["gates"]
    for field in (
        "qwen_inference_performed",
        "codex_generation_performed",
        "qwen_lean_inference_performed",
        "gpu_work_performed",
        "candidate_outputs_or_item_level_results_inspected",
        "phase4_checkpoint_used",
        "intermediate_phase5_checkpoint_used",
        "protected_formal_worker_execution_authorized",
        "checkpoints_b_through_f_authorized",
        "merge_or_auto_merge_authorized",
    ):
        _require_equal(gates[field], False, f"gate {field}")
    _require_equal(gates["checkpoint_a_scope_only"], True, "scope gate")
    _require_equal(gates["checkpoint_a_v2_freeze_complete"], True, "freeze gate")
    _require_equal(gates["fresh_independent_review_required"], True, "review gate")

    freeze_id = stable_id("checkpoint_a_v2", value)
    _require_equal(freeze_id, EXPECTED_CHECKPOINT_A_V2_ID, "content id")
    return CheckpointAV2Freeze(value=value, base_v1=base_v1, freeze_id=freeze_id)


def read_checkpoint_a_v2(
    path: str | Path = DEFAULT_CHECKPOINT_A_V2_PATH,
    *,
    base_v1_path: str | Path = DEFAULT_CHECKPOINT_A_PATH,
) -> CheckpointAV2Freeze:
    try:
        value = json.loads(Path(path).read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError("checkpoint A v2 artifact is not valid JSON") from error
    if not isinstance(value, dict):
        raise ValueError("checkpoint A v2 artifact must be a JSON object")
    return validate_checkpoint_a_v2(value, base_v1_path=base_v1_path)
