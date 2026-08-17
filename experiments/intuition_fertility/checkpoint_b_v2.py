"""Build and strictly validate issue #32 Checkpoint-B v2."""

from __future__ import annotations

import json
import os
from collections import Counter
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from .canonical import canonical_json, require_exact_keys, stable_id, text_sha256
from .checkpoint_a import render_generator_prompt, render_leakage_review_prompt
from .checkpoint_a_v2 import EXPECTED_CHECKPOINT_A_V2_ID, read_checkpoint_a_v2
from .checkpoint_b import (
    EXPECTED_CHECKPOINT_B_ID,
    _PinnedTokenizerCounter,
    _evidence_manifest,
    _expected_codex_generation_command,
    _load_json,
    _parse_codex_transcript,
    _require_equal,
    _sha256_file,
    _verify_file_hash,
    read_checkpoint_b,
)
from .checkpoint_b_v2_runner import BREVITY_INSTRUCTION, render_generator_prompt_v2
from .panel import Presentation, generator_payload
from .records import (
    FrozenIntuitionStore,
    GeneratorRole,
    IntuitionSample,
    LeakageDecision,
    LeakageDecisionStore,
    LeakageLabel,
    deterministic_leakage_flags,
    escape_lean_block_comment,
    sample_eligibility,
)

CHECKPOINT_B_V2_SCHEMA_VERSION = "intuition_fertility_checkpoint_b_v2"
DEFAULT_CHECKPOINT_B_V2_PATH = Path(__file__).with_name("checkpoint_b_v2.json")
DEFAULT_CHECKPOINT_B_V2_EVIDENCE_DIR = Path(__file__).with_name(
    "checkpoint_b_evidence_v2"
)
EXPECTED_CHECKPOINT_B_V2_ID = (
    "checkpoint_b_v2_7c9e79db2be94f2e8aa5907b1918e63c407fd435954e315f28e75315aa3904c9"
)
_REPOSITORY_ROOT = Path(__file__).parents[2]
_MATHIA_MAIN_COMMIT = "f29c4388a8eb4cf88c03f1810a96a03a2f8aa1dc"
_CHECKPOINT_B_V1_SHA256 = (
    "31bf0a493ef19560777c85936dba1362c6b6ebcd48df0a268b2276fadd789068"
)
_RUNNER_SHA256 = "e05cbe535d4b950ca954d36b8679b18c3b9156999bca10d1e811837fd714fdab"
_OUTPUT_SCHEMA_SHA256 = (
    "616312c41934b1b3ad654fab72a327bb7cf358250c542342a197ed4aac172734"
)
_TOKENIZER_IDENTITY = {
    "model": "Qwen/Qwen3-8B-Base",
    "revision": "49e3418fbbbca6ecbdf9608b4d22e5a407081db4",
    "add_special_tokens": False,
}
_THEOREM_IDS = tuple("ABCDEFG")
_GENERATOR_ROLES = (
    GeneratorRole.QWEN_BASE.value,
    GeneratorRole.CODEX_REFERENCE.value,
)
_V2_PROMPT_TEMPLATE = (
    "Theorem statement:\n{theorem_statement}\n\n"
    "Request:\n{intuition_request}\n"
    f"{BREVITY_INSTRUCTION}\n\nStrategy:\n"
)


def _validate_prompt_amendment() -> dict[str, Any]:
    prompt_hashes: dict[str, str] = {}
    base_hashes: dict[str, str] = {}
    for theorem_id in _THEOREM_IDS:
        base = render_generator_prompt(theorem_id)
        amended = render_generator_prompt_v2(theorem_id)
        expected = base.removesuffix("\n\nStrategy:\n")
        expected += f"\n{BREVITY_INSTRUCTION}\n\nStrategy:\n"
        _require_equal(amended, expected, f"amended prompt {theorem_id}")
        _require_equal(
            amended.replace(f"\n{BREVITY_INSTRUCTION}", "", 1),
            base,
            f"base prompt preservation {theorem_id}",
        )
        _require_equal(
            amended.count(BREVITY_INSTRUCTION), 1, f"brevity sentence {theorem_id}"
        )
        base_hashes[theorem_id] = text_sha256(base)
        prompt_hashes[theorem_id] = text_sha256(amended)
    return {
        "amendment_issue_comment": (
            "https://github.com/murillo128/mathia/issues/32#issuecomment-5315885633"
        ),
        "brevity_instruction": BREVITY_INSTRUCTION,
        "placement": "after_unchanged_intuition_request_before_strategy_delimiter",
        "base_prompt_template": (
            "Theorem statement:\n{theorem_statement}\n\n"
            "Request:\n{intuition_request}\n\nStrategy:\n"
        ),
        "amended_prompt_template": _V2_PROMPT_TEMPLATE,
        "base_prompt_sha256": base_hashes,
        "amended_prompt_sha256": prompt_hashes,
        "actual_eligibility_gate_unchanged": (
            "at_most_96_qwen_lean_tokens_after_comment_escaping"
        ),
        "word_instruction_is_not_a_repair_or_eligibility_override": True,
    }


def _validate_codex_generation_record(
    record: dict[str, Any], theorem_id: str, evidence_dir: Path
) -> None:
    require_exact_keys(
        record,
        required={
            "schema_version",
            "theorem_id",
            "presentation",
            "sample_index",
            "capture_identity",
            "prompt_sha256",
            "transcript_path",
            "transcript_sha256",
            "stderr_path",
            "stderr_sha256",
            "started_at_utc",
            "finished_at_utc",
            "command",
            "working_directory",
            "returncode",
            "final_message",
            "disallowed_item_types",
            "valid_capture",
        },
        field="Checkpoint-B v2 Codex generation record",
    )
    _require_equal(
        record["schema_version"],
        "checkpoint_b_v2_codex_generation_v1",
        "Codex record schema",
    )
    _require_equal(record["theorem_id"], theorem_id, "Codex theorem")
    _require_equal(record["presentation"], "standard", "Codex presentation")
    _require_equal(record["sample_index"], 0, "Codex sample index")
    _require_equal(
        record["prompt_sha256"],
        text_sha256(render_generator_prompt_v2(theorem_id)),
        "Codex prompt hash",
    )
    _require_equal(record["returncode"], 0, "Codex return code")
    _require_equal(record["valid_capture"], True, "Codex capture")
    _require_equal(record["disallowed_item_types"], [], "Codex tool isolation")
    _require_equal(
        record["working_directory"],
        "fresh_empty_non_repository_temporary_directory",
        "Codex working directory",
    )
    _require_equal(
        record["command"], _expected_codex_generation_command(), "Codex command"
    )
    if not isinstance(record["final_message"], str) or not record["final_message"]:
        raise ValueError("Checkpoint-B v2 Codex final message is missing")
    for prefix in ("transcript", "stderr"):
        _verify_file_hash(
            evidence_dir, record[f"{prefix}_path"], record[f"{prefix}_sha256"]
        )
    final_message, disallowed_items = _parse_codex_transcript(
        evidence_dir / record["transcript_path"]
    )
    _require_equal(final_message, record["final_message"], "Codex transcript output")
    _require_equal(disallowed_items, [], "Codex transcript tool isolation")


def _validate_qwen_generation_record(record: dict[str, Any], freeze: Any) -> None:
    require_exact_keys(
        record,
        required={
            "schema_version",
            "started_at_utc",
            "finished_at_utc",
            "generator_config",
            "runtime",
            "captures",
        },
        field="Checkpoint-B v2 Qwen generation record",
    )
    _require_equal(
        record["schema_version"],
        "checkpoint_b_v2_qwen_generation_v1",
        "Qwen record schema",
    )
    _require_equal(
        record["generator_config"],
        freeze.base_v1.value["generator_protocol"]["qwen_base"],
        "Qwen generator config",
    )
    runtime = record["runtime"]
    _require_equal(runtime["gpu"], "NVIDIA RTX 4000 Ada Generation", "Qwen GPU")
    _require_equal(runtime["vllm"], "0.10.2", "Qwen vLLM")
    _require_equal(runtime["torch"], "2.8.0+cu128", "Qwen Torch")
    _require_equal(
        runtime["inference_execution"],
        "project_controlled_local_cuda",
        "Qwen execution",
    )
    _require_equal(
        [capture["theorem_id"] for capture in record["captures"]],
        list(_THEOREM_IDS),
        "Qwen target order",
    )
    for capture in record["captures"]:
        require_exact_keys(
            capture,
            required={
                "theorem_id",
                "presentation",
                "sample_index",
                "capture_identity",
                "prompt_sha256",
                "prompt_token_ids",
                "prompt_token_ids_sha256",
                "raw_text",
                "generated_token_ids",
                "finish_reason",
                "stop_reason",
            },
            field="Checkpoint-B v2 Qwen capture",
        )
        theorem_id = capture["theorem_id"]
        _require_equal(capture["presentation"], "standard", "Qwen presentation")
        _require_equal(capture["sample_index"], 0, "Qwen sample index")
        _require_equal(
            capture["prompt_sha256"],
            text_sha256(render_generator_prompt_v2(theorem_id)),
            "Qwen prompt hash",
        )
        _require_equal(
            capture["prompt_token_ids_sha256"],
            text_sha256(canonical_json(capture["prompt_token_ids"])),
            "Qwen prompt token hash",
        )
        if not isinstance(capture["raw_text"], str) or not capture["raw_text"]:
            raise ValueError("Checkpoint-B v2 Qwen output is missing")
        if len(capture["generated_token_ids"]) > 96:
            raise ValueError("Checkpoint-B v2 Qwen exceeded its generation limit")


def _generation_inputs(
    evidence_dir: Path, freeze: Any
) -> tuple[dict[tuple[str, str], dict[str, Any]], dict[str, str]]:
    manifest = _evidence_manifest(evidence_dir)
    qwen = _load_json(evidence_dir / "qwen_base.json")
    _validate_qwen_generation_record(qwen, freeze)
    captures: dict[tuple[str, str], dict[str, Any]] = {}
    for capture in qwen["captures"]:
        captures[(capture["theorem_id"], "qwen_base")] = {
            **capture,
            "source_record_path": "qwen_base.json",
            "source_record_sha256": manifest["qwen_base.json"],
            "transcript_path": None,
            "transcript_sha256": None,
        }

    for theorem_id in _THEOREM_IDS:
        relative_path = f"codex_reference_{theorem_id}.json"
        record = _load_json(evidence_dir / relative_path)
        _validate_codex_generation_record(record, theorem_id, evidence_dir)
        captures[(theorem_id, "codex_reference")] = {
            "theorem_id": theorem_id,
            "presentation": record["presentation"],
            "sample_index": record["sample_index"],
            "capture_identity": record["capture_identity"],
            "prompt_sha256": record["prompt_sha256"],
            "raw_text": record["final_message"],
            "source_record_path": relative_path,
            "source_record_sha256": manifest[relative_path],
            "transcript_path": record["transcript_path"],
            "transcript_sha256": record["transcript_sha256"],
        }
    _require_equal(
        set(captures),
        {
            (theorem_id, role)
            for theorem_id in _THEOREM_IDS
            for role in _GENERATOR_ROLES
        },
        "sample capture membership",
    )
    return captures, manifest


def _load_and_validate_review(
    *,
    evidence_dir: Path,
    manifest: dict[str, str],
    theorem_id: str,
    role: str,
    reviewer_index: int,
    raw_text: str,
) -> tuple[dict[str, Any], dict[str, Any]]:
    relative_path = f"leakage/{role}_{theorem_id}_reviewer_{reviewer_index}.json"
    record = _load_json(evidence_dir / relative_path)
    _require_equal(
        record["schema_version"],
        "checkpoint_b_v2_leakage_review_v1",
        "review schema",
    )
    _require_equal(record["theorem_id"], theorem_id, "review theorem")
    _require_equal(record["generator_role"], role, "review source binding")
    _require_equal(record["reviewer_index"], reviewer_index, "reviewer index")
    statement = generator_payload(theorem_id, Presentation.STANDARD)[
        "theorem_statement"
    ]
    prompt = render_leakage_review_prompt(
        theorem_statement=statement, candidate_guidance=raw_text
    )
    _require_equal(record["prompt_sha256"], text_sha256(prompt), "review prompt hash")
    flags = deterministic_leakage_flags(
        {"theorem_statement": statement, "candidate_guidance": raw_text}
    )
    if flags:
        _require_equal(record["model_invoked"], False, "marker review bypass")
        _require_equal(
            record["status"], "deterministic_overt_lean_marker", "marker review"
        )
        _require_equal(record["flags"], list(flags), "marker flags")
        _require_equal(record["label"], "proof_like", "marker label")
        _require_equal(record["uncertain"], False, "marker uncertainty")
    else:
        _require_equal(record["model_invoked"], True, "model review execution")
        _require_equal(record["status"], "valid_model_review", "model review status")
        _require_equal(record["returncode"], 0, "review return code")
        _require_equal(record["valid_capture"], True, "review capture")
        _require_equal(record["disallowed_item_types"], [], "review tool isolation")
        _require_equal(
            record["working_directory"],
            "fresh_empty_non_repository_temporary_directory",
            "review working directory",
        )
        command = record["command"]
        _require_equal(
            command[:-3],
            _expected_codex_generation_command()[:-1],
            "review command prefix",
        )
        _require_equal(command[-3], "--output-schema", "review schema option")
        _require_equal(
            Path(command[-2]).name,
            "checkpoint_b_output_schema.json",
            "review schema path",
        )
        _require_equal(command[-1], "-", "review stdin prompt")
        parsed = json.loads(record["final_message"])
        _require_equal(
            parsed,
            {"label": record["label"], "uncertain": record["uncertain"]},
            "review output",
        )
        for prefix in ("transcript", "stderr"):
            _verify_file_hash(
                evidence_dir, record[f"{prefix}_path"], record[f"{prefix}_sha256"]
            )
        final_message, disallowed_items = _parse_codex_transcript(
            evidence_dir / record["transcript_path"]
        )
        _require_equal(final_message, record["final_message"], "review transcript")
        _require_equal(disallowed_items, [], "review transcript tool isolation")
    review_id = stable_id("leakage_review", record)
    return record, {
        "theorem_id": theorem_id,
        "generator_role": role,
        "reviewer_index": reviewer_index,
        "review_id": review_id,
        "evidence_path": relative_path,
        "evidence_sha256": manifest[relative_path],
        "model_invoked": record["model_invoked"],
        "status": record["status"],
        "label": record["label"],
        "uncertain": record["uncertain"],
        "transcript_path": record.get("transcript_path"),
        "transcript_sha256": record.get("transcript_sha256"),
    }


def _resolve_reviews(
    records: list[dict[str, Any]], flags: tuple[str, ...]
) -> tuple[str, bool, bool]:
    if flags:
        return LeakageLabel.PROOF_LIKE.value, False, False
    valid = all(record["status"] == "valid_model_review" for record in records)
    labels = [record["label"] for record in records]
    any_uncertain = any(record["uncertain"] for record in records)
    if valid and not any_uncertain and len(set(labels)) == 1:
        return labels[0], False, False
    return (
        LeakageLabel.BORDERLINE.value,
        (not valid or any_uncertain),
        len(set(labels)) > 1,
    )


def build_checkpoint_b_v2_value(
    *, evidence_dir: str | Path = DEFAULT_CHECKPOINT_B_V2_EVIDENCE_DIR
) -> dict[str, Any]:
    """Materialize B v2 from the write-once generation/review evidence."""

    evidence_path = Path(evidence_dir)
    freeze = read_checkpoint_a_v2()
    _require_equal(
        freeze.freeze_id, EXPECTED_CHECKPOINT_A_V2_ID, "Checkpoint-A v2 identity"
    )
    historical = read_checkpoint_b()
    _require_equal(historical.freeze_id, EXPECTED_CHECKPOINT_B_ID, "B v1 identity")
    _require_equal(
        _sha256_file(Path(__file__).with_name("checkpoint_b_v1.json")),
        _CHECKPOINT_B_V1_SHA256,
        "B v1 artifact hash",
    )
    _require_equal(
        _sha256_file(Path(__file__).with_name("checkpoint_b_v2_runner.py")),
        _RUNNER_SHA256,
        "execution runner hash",
    )
    _require_equal(
        _sha256_file(Path(__file__).with_name("checkpoint_b_output_schema.json")),
        _OUTPUT_SCHEMA_SHA256,
        "review schema hash",
    )
    prompt_amendment = _validate_prompt_amendment()
    captures, manifest = _generation_inputs(evidence_path, freeze)
    _require_equal(len(manifest), 106, "evidence file count")
    counter = _PinnedTokenizerCounter()
    sample_store = FrozenIntuitionStore()
    samples: list[IntuitionSample] = []
    capture_evidence: list[dict[str, Any]] = []
    generator_protocol = freeze.base_v1.value["generator_protocol"]
    for theorem_id in _THEOREM_IDS:
        for role in _GENERATOR_ROLES:
            capture = captures[(theorem_id, role)]
            sample = IntuitionSample.capture(
                theorem_id=theorem_id,
                presentation=Presentation.STANDARD,
                generator_role=role,
                generator_config=generator_protocol[role],
                capture_identity=capture["capture_identity"],
                sample_index=0,
                raw_text=capture["raw_text"],
                token_counter=counter,
            )
            sample_store.add(sample)
            samples.append(sample)
            token_ids = counter.token_ids(escape_lean_block_comment(sample.raw_text))
            _require_equal(
                len(token_ids), sample.token_count, "post-escape token count"
            )
            if role == GeneratorRole.QWEN_BASE.value:
                _require_equal(
                    capture["prompt_token_ids"],
                    counter.token_ids(render_generator_prompt_v2(theorem_id)),
                    "Qwen pretokenized prompt",
                )
                decoded = counter._tokenizer.decode(
                    capture["generated_token_ids"], skip_special_tokens=True
                )
                _require_equal(
                    decoded, sample.raw_text, "Qwen generated token decoding"
                )
            capture_evidence.append(
                {
                    "sample_id": sample.sample_id,
                    "theorem_id": theorem_id,
                    "generator_role": role,
                    "source_record_path": capture["source_record_path"],
                    "source_record_sha256": capture["source_record_sha256"],
                    "prompt_sha256": capture["prompt_sha256"],
                    "raw_text_sha256": sample.text_hash,
                    "post_escape_token_ids": token_ids,
                    "post_escape_token_ids_sha256": text_sha256(
                        canonical_json(token_ids)
                    ),
                    "post_escape_token_count": len(token_ids),
                    "over_96_token_budget": sample.over_budget,
                    "transcript_path": capture["transcript_path"],
                    "transcript_sha256": capture["transcript_sha256"],
                }
            )

    leakage_policy = freeze.base_v1.value["leakage_policy"]
    decision_store = LeakageDecisionStore()
    decisions: list[LeakageDecision] = []
    review_summaries: list[dict[str, Any]] = []
    eligibility_rows: list[dict[str, Any]] = []
    for sample in samples:
        statement = generator_payload(sample.theorem_id, sample.presentation)[
            "theorem_statement"
        ]
        flags = deterministic_leakage_flags(
            {"theorem_statement": statement, "candidate_guidance": sample.raw_text}
        )
        review_records: list[dict[str, Any]] = []
        sample_review_ids: list[str] = []
        for reviewer_index in (0, 1):
            record, summary = _load_and_validate_review(
                evidence_dir=evidence_path,
                manifest=manifest,
                theorem_id=sample.theorem_id,
                role=sample.generator_role,
                reviewer_index=reviewer_index,
                raw_text=sample.raw_text,
            )
            review_records.append(record)
            sample_review_ids.append(summary["review_id"])
            review_summaries.append({"sample_id": sample.sample_id, **summary})
        requested_label, uncertain, disputed = _resolve_reviews(review_records, flags)
        classifier_identity = {
            "reviewer_identity": leakage_policy["reviewer_identity"],
            "reviewer_count": leakage_policy["reviewer_count"],
            "review_resolution": leakage_policy["review_resolution"],
            "overt_lean_marker_rule": leakage_policy["overt_lean_marker_rule"],
            "review_ids": sample_review_ids,
        }
        decision = LeakageDecision.create(
            sample=sample,
            classifier_identity=classifier_identity,
            requested_label=requested_label,
            uncertain=uncertain,
            disputed=disputed,
        )
        decision_store.add(decision)
        decisions.append(decision)
        eligible, reasons = sample_eligibility(sample, decision)
        eligibility_rows.append(
            {
                "sample_id": sample.sample_id,
                "theorem_id": sample.theorem_id,
                "generator_role": sample.generator_role,
                "token_count": sample.token_count,
                "over_96_token_budget": sample.over_budget,
                "leakage_label": decision.label,
                "eligible": eligible,
                "ineligibility_reasons": list(reasons),
            }
        )

    label_counts = Counter(decision.label for decision in decisions)
    generator_counts = Counter(sample.generator_role for sample in samples)
    eligible_count = sum(row["eligible"] for row in eligibility_rows)
    return {
        "schema_version": CHECKPOINT_B_V2_SCHEMA_VERSION,
        "controlling_issue": "murillo128/mathia#32",
        "frozen_at_utc": datetime.now(UTC)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z"),
        "historical_checkpoint_b_v1": {
            "path": "experiments/intuition_fertility/checkpoint_b_v1.json",
            "freeze_id": EXPECTED_CHECKPOINT_B_ID,
            "artifact_sha256": _CHECKPOINT_B_V1_SHA256,
            "disposition": "preserved_historical_only_not_mixed_selected_or_substituted",
        },
        "source_contract": {
            "mathia_main_commit": _MATHIA_MAIN_COMMIT,
            "checkpoint_a_v2_id": EXPECTED_CHECKPOINT_A_V2_ID,
            "execution_runner_path": (
                "experiments/intuition_fertility/checkpoint_b_v2_runner.py"
            ),
            "execution_runner_sha256": _RUNNER_SHA256,
            "leakage_output_schema_path": (
                "experiments/intuition_fertility/checkpoint_b_output_schema.json"
            ),
            "leakage_output_schema_sha256": _OUTPUT_SCHEMA_SHA256,
        },
        "protocol": {
            "inherited_checkpoint_a_generator_protocol": generator_protocol,
            "prompt_amendment": prompt_amendment,
            "sample_policy": freeze.base_v1.value["sample_policy"],
            "leakage_policy": leakage_policy,
        },
        "execution_notes": {
            "system_python_preflight": {
                "result": "failed_before_tokenizer_model_loading_or_generation",
                "reason": "ModuleNotFoundError_no_torch_in_system_python",
                "sample_attempt_performed": False,
                "capture_created": False,
                "regeneration_attempt": False,
            },
            "qwen_actual_generation_batches": 1,
            "qwen_samples_per_target": 1,
            "codex_generation_sessions": 7,
            "leakage_review_sessions": 28,
            "retries": 0,
        },
        "evidence_manifest_sha256": manifest,
        "samples": [sample.to_dict() for sample in samples],
        "sample_capture_evidence": capture_evidence,
        "leakage_reviews": review_summaries,
        "leakage_decisions": [decision.to_dict() for decision in decisions],
        "eligibility": eligibility_rows,
        "summary": {
            "sample_count": len(samples),
            "samples_by_generator": {
                role: generator_counts.get(role, 0) for role in _GENERATOR_ROLES
            },
            "leakage_review_count": len(review_summaries),
            "leakage_labels": {
                label.value: label_counts.get(label.value, 0) for label in LeakageLabel
            },
            "eligible_count": eligible_count,
            "ineligible_count": len(samples) - eligible_count,
            "over_budget_count": sum(sample.over_budget for sample in samples),
            "disputed_count": sum(decision.disputed for decision in decisions),
            "uncertain_count": sum(decision.uncertain for decision in decisions),
        },
        "gates": {
            "checkpoint_b_v2_scope_only": True,
            "qwen_base_generation_performed": True,
            "codex_reference_generation_performed": True,
            "blind_leakage_classification_performed": True,
            "checkpoint_b_v1_samples_mixed_selected_or_substituted": False,
            "qwen_lean_inference_performed": False,
            "lean_verification_performed": False,
            "historical_B_seed0_draws_opened": False,
            "semantic_regeneration_rewriting_or_truncation_performed": False,
            "selection_by_expected_quality_performed": False,
            "checkpoint_b_v2_complete": True,
            "checkpoint_c_authorized": False,
            "protected_formal_worker_execution_authorized": False,
            "merge_or_auto_merge_authorized": False,
        },
    }


@dataclass(frozen=True)
class CheckpointBV2Freeze:
    value: dict[str, Any]
    freeze_id: str

    def to_summary(self) -> dict[str, Any]:
        return {
            "schema_version": self.value["schema_version"],
            "freeze_id": self.freeze_id,
            "valid": True,
            **self.value["summary"],
            "checkpoint_b_v2_complete": self.value["gates"]["checkpoint_b_v2_complete"],
            "checkpoint_c_authorized": self.value["gates"]["checkpoint_c_authorized"],
            "protected_formal_worker_execution_authorized": self.value["gates"][
                "protected_formal_worker_execution_authorized"
            ],
        }


def validate_checkpoint_b_v2(
    value: dict[str, Any],
    *,
    evidence_dir: str | Path = DEFAULT_CHECKPOINT_B_V2_EVIDENCE_DIR,
) -> CheckpointBV2Freeze:
    require_exact_keys(
        value,
        required={
            "schema_version",
            "controlling_issue",
            "frozen_at_utc",
            "historical_checkpoint_b_v1",
            "source_contract",
            "protocol",
            "execution_notes",
            "evidence_manifest_sha256",
            "samples",
            "sample_capture_evidence",
            "leakage_reviews",
            "leakage_decisions",
            "eligibility",
            "summary",
            "gates",
        },
        field="Checkpoint B v2",
    )
    _require_equal(value["schema_version"], CHECKPOINT_B_V2_SCHEMA_VERSION, "schema")
    _require_equal(value["controlling_issue"], "murillo128/mathia#32", "issue")
    freeze = read_checkpoint_a_v2()
    historical = read_checkpoint_b()
    _require_equal(historical.freeze_id, EXPECTED_CHECKPOINT_B_ID, "B v1 loader")
    _require_equal(
        value["historical_checkpoint_b_v1"],
        {
            "path": "experiments/intuition_fertility/checkpoint_b_v1.json",
            "freeze_id": EXPECTED_CHECKPOINT_B_ID,
            "artifact_sha256": _CHECKPOINT_B_V1_SHA256,
            "disposition": "preserved_historical_only_not_mixed_selected_or_substituted",
        },
        "historical B v1 preservation",
    )
    _require_equal(
        _sha256_file(_REPOSITORY_ROOT / value["historical_checkpoint_b_v1"]["path"]),
        _CHECKPOINT_B_V1_SHA256,
        "historical B v1 file",
    )
    source = value["source_contract"]
    _require_equal(source["mathia_main_commit"], _MATHIA_MAIN_COMMIT, "main source")
    _require_equal(
        source["checkpoint_a_v2_id"], EXPECTED_CHECKPOINT_A_V2_ID, "A v2 source"
    )
    _require_equal(source["execution_runner_sha256"], _RUNNER_SHA256, "runner source")
    _require_equal(
        source["leakage_output_schema_sha256"],
        _OUTPUT_SCHEMA_SHA256,
        "review schema source",
    )
    _require_equal(
        _sha256_file(_REPOSITORY_ROOT / source["execution_runner_path"]),
        _RUNNER_SHA256,
        "runner file",
    )
    _require_equal(
        _sha256_file(_REPOSITORY_ROOT / source["leakage_output_schema_path"]),
        _OUTPUT_SCHEMA_SHA256,
        "review schema file",
    )
    expected_protocol = {
        "inherited_checkpoint_a_generator_protocol": freeze.base_v1.value[
            "generator_protocol"
        ],
        "prompt_amendment": _validate_prompt_amendment(),
        "sample_policy": freeze.base_v1.value["sample_policy"],
        "leakage_policy": freeze.base_v1.value["leakage_policy"],
    }
    _require_equal(value["protocol"], expected_protocol, "inherited protocol")
    _require_equal(
        value["execution_notes"],
        {
            "system_python_preflight": {
                "result": "failed_before_tokenizer_model_loading_or_generation",
                "reason": "ModuleNotFoundError_no_torch_in_system_python",
                "sample_attempt_performed": False,
                "capture_created": False,
                "regeneration_attempt": False,
            },
            "qwen_actual_generation_batches": 1,
            "qwen_samples_per_target": 1,
            "codex_generation_sessions": 7,
            "leakage_review_sessions": 28,
            "retries": 0,
        },
        "execution notes",
    )

    evidence_path = Path(evidence_dir)
    _require_equal(
        value["evidence_manifest_sha256"],
        _evidence_manifest(evidence_path),
        "evidence manifest",
    )
    _require_equal(len(value["evidence_manifest_sha256"]), 106, "evidence file count")
    captures, _ = _generation_inputs(evidence_path, freeze)

    samples = [IntuitionSample.from_dict(item) for item in value["samples"]]
    _require_equal(len(samples), 14, "sample count")
    _require_equal(
        [(sample.theorem_id, sample.generator_role) for sample in samples],
        [
            (theorem_id, role)
            for theorem_id in _THEOREM_IDS
            for role in _GENERATOR_ROLES
        ],
        "sample membership",
    )
    sample_by_id = {sample.sample_id: sample for sample in samples}
    _require_equal(len(sample_by_id), 14, "unique samples")
    for sample in samples:
        capture = captures[(sample.theorem_id, sample.generator_role)]
        _require_equal(sample.presentation, "standard", "sample presentation")
        _require_equal(sample.sample_index, 0, "sample index")
        _require_equal(
            sample.capture_identity, capture["capture_identity"], "capture id"
        )
        _require_equal(sample.raw_text, capture["raw_text"], "capture raw text")
        _require_equal(
            json.loads(sample.generator_config_json),
            value["protocol"]["inherited_checkpoint_a_generator_protocol"][
                sample.generator_role
            ],
            "generator identity",
        )
        _require_equal(
            json.loads(sample.tokenizer_json), _TOKENIZER_IDENTITY, "tokenizer identity"
        )

    capture_rows = value["sample_capture_evidence"]
    _require_equal(len(capture_rows), 14, "capture evidence count")
    for capture_row in capture_rows:
        sample = sample_by_id[capture_row["sample_id"]]
        source_capture = captures[(sample.theorem_id, sample.generator_role)]
        _require_equal(capture_row["theorem_id"], sample.theorem_id, "capture theorem")
        _require_equal(
            capture_row["generator_role"], sample.generator_role, "capture generator"
        )
        _require_equal(
            capture_row["source_record_path"],
            source_capture["source_record_path"],
            "capture source path",
        )
        _require_equal(
            capture_row["prompt_sha256"], source_capture["prompt_sha256"], "prompt hash"
        )
        _require_equal(capture_row["raw_text_sha256"], sample.text_hash, "capture text")
        _require_equal(
            capture_row["post_escape_token_count"], sample.token_count, "capture tokens"
        )
        _require_equal(
            len(capture_row["post_escape_token_ids"]),
            sample.token_count,
            "token list",
        )
        _require_equal(
            capture_row["post_escape_token_ids_sha256"],
            text_sha256(canonical_json(capture_row["post_escape_token_ids"])),
            "token list hash",
        )
        _require_equal(
            capture_row["over_96_token_budget"], sample.over_budget, "budget status"
        )
        _require_equal(
            value["evidence_manifest_sha256"][capture_row["source_record_path"]],
            capture_row["source_record_sha256"],
            "capture source hash",
        )
        if capture_row["transcript_path"] is not None:
            _require_equal(
                value["evidence_manifest_sha256"][capture_row["transcript_path"]],
                capture_row["transcript_sha256"],
                "capture transcript hash",
            )

    reviews = value["leakage_reviews"]
    _require_equal(len(reviews), 28, "review count")
    reviews_by_sample: dict[str, list[dict[str, Any]]] = {
        sample.sample_id: [] for sample in samples
    }
    reconstructed_reviews: dict[tuple[str, str, int], dict[str, Any]] = {}
    for sample in samples:
        for reviewer_index in (0, 1):
            _, summary = _load_and_validate_review(
                evidence_dir=evidence_path,
                manifest=value["evidence_manifest_sha256"],
                theorem_id=sample.theorem_id,
                role=sample.generator_role,
                reviewer_index=reviewer_index,
                raw_text=sample.raw_text,
            )
            reconstructed_reviews[
                (sample.theorem_id, sample.generator_role, reviewer_index)
            ] = summary
    review_ids: set[str] = set()
    for review in reviews:
        sample = sample_by_id[review["sample_id"]]
        expected_review = reconstructed_reviews[
            (sample.theorem_id, sample.generator_role, review["reviewer_index"])
        ]
        _require_equal(
            {key: value for key, value in review.items() if key != "sample_id"},
            expected_review,
            "review evidence summary",
        )
        if review["review_id"] in review_ids:
            raise ValueError("Checkpoint-B v2 duplicate review identity")
        review_ids.add(review["review_id"])
        reviews_by_sample[sample.sample_id].append(review)
    for sample_reviews in reviews_by_sample.values():
        _require_equal(
            [review["reviewer_index"] for review in sample_reviews],
            [0, 1],
            "per-sample reviewer indexes",
        )

    decisions = [
        LeakageDecision.from_dict(item, sample=sample_by_id[item["sample_id"]])
        for item in value["leakage_decisions"]
    ]
    _require_equal(len(decisions), 14, "leakage decision count")
    decision_by_sample = {decision.sample_id: decision for decision in decisions}
    _require_equal(len(decision_by_sample), 14, "unique leakage decisions")
    for decision in decisions:
        identity = json.loads(decision.classifier_identity_json)
        _require_equal(identity["reviewer_count"], 2, "classifier reviewer count")
        _require_equal(
            identity["review_ids"],
            [review["review_id"] for review in reviews_by_sample[decision.sample_id]],
            "classifier review binding",
        )
        sample = sample_by_id[decision.sample_id]
        records = [
            _load_json(
                evidence_path
                / f"leakage/{sample.generator_role}_{sample.theorem_id}_reviewer_{index}.json"
            )
            for index in (0, 1)
        ]
        statement = generator_payload(sample.theorem_id, sample.presentation)[
            "theorem_statement"
        ]
        flags = deterministic_leakage_flags(
            {"theorem_statement": statement, "candidate_guidance": sample.raw_text}
        )
        label, uncertain, disputed = _resolve_reviews(records, flags)
        _require_equal(decision.label, label, "resolved leakage label")
        _require_equal(decision.uncertain, uncertain, "resolved uncertainty")
        _require_equal(decision.disputed, disputed, "resolved dispute")

    eligibility = value["eligibility"]
    _require_equal(len(eligibility), 14, "eligibility count")
    for row in eligibility:
        sample = sample_by_id[row["sample_id"]]
        decision = decision_by_sample[sample.sample_id]
        eligible, reasons = sample_eligibility(sample, decision)
        _require_equal(row["theorem_id"], sample.theorem_id, "eligibility theorem")
        _require_equal(
            row["generator_role"], sample.generator_role, "eligibility generator"
        )
        _require_equal(row["token_count"], sample.token_count, "eligibility tokens")
        _require_equal(row["leakage_label"], decision.label, "eligibility leakage")
        _require_equal(row["eligible"], eligible, "eligibility state")
        _require_equal(
            row["ineligibility_reasons"], list(reasons), "ineligibility reasons"
        )

    expected_summary = {
        "sample_count": 14,
        "samples_by_generator": {"qwen_base": 7, "codex_reference": 7},
        "leakage_review_count": 28,
        "leakage_labels": {
            label.value: sum(decision.label == label.value for decision in decisions)
            for label in LeakageLabel
        },
        "eligible_count": sum(row["eligible"] for row in eligibility),
        "ineligible_count": sum(not row["eligible"] for row in eligibility),
        "over_budget_count": sum(sample.over_budget for sample in samples),
        "disputed_count": sum(decision.disputed for decision in decisions),
        "uncertain_count": sum(decision.uncertain for decision in decisions),
    }
    _require_equal(value["summary"], expected_summary, "summary")

    gates = value["gates"]
    for field in (
        "checkpoint_b_v1_samples_mixed_selected_or_substituted",
        "qwen_lean_inference_performed",
        "lean_verification_performed",
        "historical_B_seed0_draws_opened",
        "semantic_regeneration_rewriting_or_truncation_performed",
        "selection_by_expected_quality_performed",
        "checkpoint_c_authorized",
        "protected_formal_worker_execution_authorized",
        "merge_or_auto_merge_authorized",
    ):
        _require_equal(gates[field], False, f"gate {field}")
    for field in (
        "checkpoint_b_v2_scope_only",
        "qwen_base_generation_performed",
        "codex_reference_generation_performed",
        "blind_leakage_classification_performed",
        "checkpoint_b_v2_complete",
    ):
        _require_equal(gates[field], True, f"gate {field}")

    freeze_id = stable_id("checkpoint_b_v2", value)
    _require_equal(freeze_id, EXPECTED_CHECKPOINT_B_V2_ID, "content id")
    return CheckpointBV2Freeze(value=value, freeze_id=freeze_id)


def read_checkpoint_b_v2(
    path: str | Path = DEFAULT_CHECKPOINT_B_V2_PATH,
    *,
    evidence_dir: str | Path = DEFAULT_CHECKPOINT_B_V2_EVIDENCE_DIR,
) -> CheckpointBV2Freeze:
    try:
        value = json.loads(Path(path).read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError("Checkpoint-B v2 artifact is not valid JSON") from error
    if not isinstance(value, dict):
        raise ValueError("Checkpoint-B v2 artifact must be a JSON object")
    return validate_checkpoint_b_v2(value, evidence_dir=evidence_dir)


def write_checkpoint_b_v2(
    path: str | Path = DEFAULT_CHECKPOINT_B_V2_PATH,
    *,
    evidence_dir: str | Path = DEFAULT_CHECKPOINT_B_V2_EVIDENCE_DIR,
) -> str:
    value = build_checkpoint_b_v2_value(evidence_dir=evidence_dir)
    rendered = (canonical_json(value) + "\n").encode("utf-8")
    output_path = Path(path)
    try:
        descriptor = os.open(output_path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
    except FileExistsError as error:
        raise RuntimeError(
            f"refusing to replace frozen artifact: {output_path}"
        ) from error
    with os.fdopen(descriptor, "wb") as output:
        output.write(rendered)
    return stable_id("checkpoint_b_v2", value)
