"""Formal-worker run and formally verified whole-proof result interchange."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any

from .canonical import (
    canonical_json,
    parse_canonical_object,
    require_exact_keys,
    stable_id,
    text_sha256,
)
from .conditions import ConditionCell
from .panel import PANEL_ID, get_target_identity
from .prompts import RenderedPrompt

RUN_SCHEMA_VERSION = "formal_worker_run_v1"
RESULT_SCHEMA_VERSION = "formal_worker_result_v1"
VERIFICATION_SCHEMA_VERSION = "formal_verification_v1"


class VerificationCategory(str, Enum):
    VERIFIED_PROOF = "verified_proof"
    LEAN_REJECTION = "lean_rejection"
    EMPTY_GENERATION_FAILURE = "empty_generation_failure"
    VERIFIER_TIMEOUT = "verifier_timeout"
    VERIFIER_INFRASTRUCTURE_ERROR = "verifier_infrastructure_error"


class VerifierStatus(str, Enum):
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    TIMEOUT = "timeout"
    ERROR = "error"


@dataclass(frozen=True)
class FormalWorkerRun:
    schema_version: str
    panel_id: str
    qwen_lean_identity_json: str
    qwen_lean_identity_id: str
    base_model_identity_json: str
    base_model_identity_id: str
    tokenizer_identity_json: str
    tokenizer_identity_id: str
    formal_environment_identity_json: str
    formal_environment_identity_id: str
    mathlib_revision: str
    lean_version: str
    generation_settings_json: str
    candidate_budget: int
    seeds: tuple[int, ...]
    run_id: str

    @classmethod
    def create(
        cls,
        *,
        qwen_lean_identity: dict[str, Any],
        base_model_identity: dict[str, Any],
        tokenizer_identity: dict[str, Any],
        formal_environment_identity: dict[str, Any],
        mathlib_revision: str,
        lean_version: str,
        generation_settings: dict[str, Any],
        candidate_budget: int,
        seeds: list[int] | tuple[int, ...],
    ) -> FormalWorkerRun:
        if (
            not isinstance(candidate_budget, int)
            or isinstance(candidate_budget, bool)
            or candidate_budget <= 0
        ):
            raise ValueError(
                "candidate_budget must be a positive integer supplied by the run"
            )
        if not isinstance(mathlib_revision, str) or not mathlib_revision:
            raise ValueError("mathlib_revision must be an explicit non-empty string")
        if not isinstance(lean_version, str) or not lean_version:
            raise ValueError("lean_version must be an explicit non-empty string")
        if any(not isinstance(seed, int) or isinstance(seed, bool) for seed in seeds):
            raise ValueError("seeds must contain integers")
        if len(set(seeds)) != len(seeds):
            raise ValueError("seeds must not contain duplicates")
        identities = {
            "qwen_lean": qwen_lean_identity,
            "base_model": base_model_identity,
            "tokenizer": tokenizer_identity,
            "formal_environment": formal_environment_identity,
        }
        if any(
            not isinstance(value, dict) or not value for value in identities.values()
        ):
            raise ValueError("every run identity must be a non-empty object")
        serialized = {key: canonical_json(value) for key, value in identities.items()}
        ids = {key: stable_id(key, value) for key, value in identities.items()}
        settings_json = canonical_json(generation_settings)
        identity_input = {
            "schema_version": RUN_SCHEMA_VERSION,
            "panel_id": PANEL_ID,
            "qwen_lean_identity_id": ids["qwen_lean"],
            "base_model_identity_id": ids["base_model"],
            "tokenizer_identity_id": ids["tokenizer"],
            "formal_environment_identity_id": ids["formal_environment"],
            "mathlib_revision": mathlib_revision,
            "lean_version": lean_version,
            "generation_settings": generation_settings,
            "candidate_budget": candidate_budget,
            "seeds": list(seeds),
        }
        return cls(
            schema_version=RUN_SCHEMA_VERSION,
            panel_id=PANEL_ID,
            qwen_lean_identity_json=serialized["qwen_lean"],
            qwen_lean_identity_id=ids["qwen_lean"],
            base_model_identity_json=serialized["base_model"],
            base_model_identity_id=ids["base_model"],
            tokenizer_identity_json=serialized["tokenizer"],
            tokenizer_identity_id=ids["tokenizer"],
            formal_environment_identity_json=serialized["formal_environment"],
            formal_environment_identity_id=ids["formal_environment"],
            mathlib_revision=mathlib_revision,
            lean_version=lean_version,
            generation_settings_json=settings_json,
            candidate_budget=candidate_budget,
            seeds=tuple(seeds),
            run_id=stable_id("run", identity_input),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "panel_id": self.panel_id,
            "qwen_lean_identity": parse_canonical_object(
                self.qwen_lean_identity_json, field="qwen_lean_identity_json"
            ),
            "qwen_lean_identity_id": self.qwen_lean_identity_id,
            "base_model_identity": parse_canonical_object(
                self.base_model_identity_json, field="base_model_identity_json"
            ),
            "base_model_identity_id": self.base_model_identity_id,
            "tokenizer_identity": parse_canonical_object(
                self.tokenizer_identity_json, field="tokenizer_identity_json"
            ),
            "tokenizer_identity_id": self.tokenizer_identity_id,
            "formal_environment_identity": parse_canonical_object(
                self.formal_environment_identity_json,
                field="formal_environment_identity_json",
            ),
            "formal_environment_identity_id": self.formal_environment_identity_id,
            "mathlib_revision": self.mathlib_revision,
            "lean_version": self.lean_version,
            "generation_settings": parse_canonical_object(
                self.generation_settings_json, field="generation_settings_json"
            ),
            "candidate_budget": self.candidate_budget,
            "seeds": list(self.seeds),
            "run_id": self.run_id,
        }

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> FormalWorkerRun:
        fields = {
            "schema_version",
            "panel_id",
            "qwen_lean_identity",
            "qwen_lean_identity_id",
            "base_model_identity",
            "base_model_identity_id",
            "tokenizer_identity",
            "tokenizer_identity_id",
            "formal_environment_identity",
            "formal_environment_identity_id",
            "mathlib_revision",
            "lean_version",
            "generation_settings",
            "candidate_budget",
            "seeds",
            "run_id",
        }
        require_exact_keys(value, required=fields, field="formal worker run")
        if (
            value["schema_version"] != RUN_SCHEMA_VERSION
            or value["panel_id"] != PANEL_ID
        ):
            raise ValueError("unsupported run schema or panel identity")
        rebuilt = cls.create(
            qwen_lean_identity=value["qwen_lean_identity"],
            base_model_identity=value["base_model_identity"],
            tokenizer_identity=value["tokenizer_identity"],
            formal_environment_identity=value["formal_environment_identity"],
            mathlib_revision=value["mathlib_revision"],
            lean_version=value["lean_version"],
            generation_settings=value["generation_settings"],
            candidate_budget=value["candidate_budget"],
            seeds=value["seeds"],
        )
        if rebuilt.to_dict() != value:
            raise ValueError("formal worker run content or identity is inconsistent")
        return rebuilt


@dataclass(frozen=True)
class VerificationEvidence:
    schema_version: str
    status: str
    formal_environment_identity_id: str
    evidence_json: str
    evidence_id: str

    @classmethod
    def create(
        cls,
        *,
        status: VerifierStatus | str,
        formal_environment_identity_id: str,
        evidence: dict[str, Any],
    ) -> VerificationEvidence:
        selected = VerifierStatus(status)
        if not formal_environment_identity_id:
            raise ValueError(
                "verification evidence requires a formal environment identity"
            )
        if not isinstance(evidence, dict) or not evidence:
            raise ValueError("verification evidence payload must be a non-empty object")
        evidence_json = canonical_json(evidence)
        identity_input = {
            "schema_version": VERIFICATION_SCHEMA_VERSION,
            "status": selected.value,
            "formal_environment_identity_id": formal_environment_identity_id,
            "evidence": evidence,
        }
        return cls(
            schema_version=VERIFICATION_SCHEMA_VERSION,
            status=selected.value,
            formal_environment_identity_id=formal_environment_identity_id,
            evidence_json=evidence_json,
            evidence_id=stable_id("verification", identity_input),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "status": self.status,
            "formal_environment_identity_id": self.formal_environment_identity_id,
            "evidence": parse_canonical_object(
                self.evidence_json, field="evidence_json"
            ),
            "evidence_id": self.evidence_id,
        }

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> VerificationEvidence:
        fields = {
            "schema_version",
            "status",
            "formal_environment_identity_id",
            "evidence",
            "evidence_id",
        }
        require_exact_keys(value, required=fields, field="verification evidence")
        if value["schema_version"] != VERIFICATION_SCHEMA_VERSION:
            raise ValueError("unsupported verification evidence schema_version")
        if not isinstance(value["evidence"], dict):
            raise ValueError("verification evidence payload must be an object")
        rebuilt = cls.create(
            status=value["status"],
            formal_environment_identity_id=value["formal_environment_identity_id"],
            evidence=value["evidence"],
        )
        if rebuilt.to_dict() != value:
            raise ValueError(
                "verification evidence content or identity is inconsistent"
            )
        return rebuilt


_CATEGORY_STATUS = {
    VerificationCategory.VERIFIED_PROOF: VerifierStatus.ACCEPTED,
    VerificationCategory.LEAN_REJECTION: VerifierStatus.REJECTED,
    VerificationCategory.VERIFIER_TIMEOUT: VerifierStatus.TIMEOUT,
    VerificationCategory.VERIFIER_INFRASTRUCTURE_ERROR: VerifierStatus.ERROR,
}


@dataclass(frozen=True)
class CandidateResult:
    schema_version: str
    run_id: str
    theorem_id: str
    canonical_target: str
    theorem_record_id: str
    condition: str
    condition_cell_id: str
    prompt_id: str
    prompt_hash: str
    guidance_id: str | None
    guidance_hash: str | None
    guidance_token_count: int | None
    candidate_index: int
    candidate_order: int
    raw_continuation: str
    continuation_hash: str
    finish_reason: str
    generation_metadata_json: str
    verification_category: str
    verification_evidence: VerificationEvidence | None
    generated_token_count: int | None
    runtime_seconds: float | None
    runtime_comparability_id: str | None
    result_id: str

    @classmethod
    def capture(
        cls,
        *,
        run: FormalWorkerRun,
        cell: ConditionCell,
        prompt: RenderedPrompt,
        canonical_target: str,
        theorem_record_id: str,
        candidate_index: int,
        candidate_order: int,
        raw_continuation: str,
        finish_reason: str,
        generation_metadata: dict[str, Any],
        verification_category: VerificationCategory | str,
        verification_evidence: VerificationEvidence | None,
        generated_token_count: int | None = None,
        runtime_seconds: float | None = None,
        runtime_comparability_id: str | None = None,
    ) -> CandidateResult:
        identity = get_target_identity(cell.theorem_id)
        if (
            canonical_target != identity.canonical_target
            or theorem_record_id != identity.record_id
        ):
            raise ValueError(
                "formal result target identity does not match the frozen panel"
            )
        if not cell.eligible:
            raise ValueError(
                "formal-worker outcomes cannot be attached to an ineligible cell"
            )
        if (
            prompt.condition_cell_id != cell.cell_id
            or prompt.theorem_id != cell.theorem_id
        ):
            raise ValueError("prompt is not bound to the supplied condition cell")
        if prompt.condition != cell.condition:
            raise ValueError("prompt condition does not match the condition cell")
        if not isinstance(finish_reason, str) or not finish_reason:
            raise ValueError("finish_reason must be a non-empty string")
        if not isinstance(generation_metadata, dict):
            raise ValueError("generation_metadata must be an object")
        if not isinstance(raw_continuation, str):
            raise ValueError("raw_continuation must be a string")
        if (
            cell.tokenizer_id is not None
            and cell.tokenizer_id != run.tokenizer_identity_id
        ):
            raise ValueError(
                "guidance token count does not use the formal worker tokenizer identity"
            )
        if (
            not isinstance(candidate_index, int)
            or isinstance(candidate_index, bool)
            or not 0 <= candidate_index < run.candidate_budget
        ):
            raise ValueError(
                "candidate_index must be within the frozen candidate budget"
            )
        if (
            not isinstance(candidate_order, int)
            or isinstance(candidate_order, bool)
            or not 1 <= candidate_order <= run.candidate_budget
        ):
            raise ValueError(
                "candidate_order must be within the frozen candidate budget"
            )
        if generated_token_count is not None and (
            not isinstance(generated_token_count, int)
            or isinstance(generated_token_count, bool)
            or generated_token_count < 0
        ):
            raise ValueError("generated_token_count must be a non-negative integer")
        if runtime_seconds is not None and (
            not isinstance(runtime_seconds, (int, float))
            or isinstance(runtime_seconds, bool)
            or runtime_seconds < 0
        ):
            raise ValueError("runtime_seconds must be a non-negative number")
        if (runtime_seconds is None) != (runtime_comparability_id is None):
            raise ValueError(
                "runtime requires a comparability identity, and vice versa"
            )
        if runtime_comparability_id is not None and (
            not isinstance(runtime_comparability_id, str)
            or not runtime_comparability_id
        ):
            raise ValueError("runtime_comparability_id must be a non-empty string")
        category = VerificationCategory(verification_category)
        if category is VerificationCategory.EMPTY_GENERATION_FAILURE:
            if verification_evidence is not None:
                raise ValueError("generation failure cannot carry verifier evidence")
        else:
            if verification_evidence is None:
                raise ValueError(
                    f"{category.value} requires formal verification evidence"
                )
            expected_status = _CATEGORY_STATUS[category].value
            if verification_evidence.status != expected_status:
                raise ValueError(
                    f"{category.value} requires verifier status {expected_status}"
                )
            if (
                verification_evidence.formal_environment_identity_id
                != run.formal_environment_identity_id
            ):
                raise ValueError(
                    "verification evidence uses another formal environment"
                )
        if (
            category is VerificationCategory.VERIFIED_PROOF
            and not raw_continuation.strip()
        ):
            raise ValueError(
                "a verified proof requires a non-empty generated continuation"
            )
        metadata_json = canonical_json(generation_metadata)
        continuation_hash = text_sha256(raw_continuation)
        identity_input = {
            "schema_version": RESULT_SCHEMA_VERSION,
            "run_id": run.run_id,
            "theorem_id": cell.theorem_id,
            "canonical_target": canonical_target,
            "theorem_record_id": theorem_record_id,
            "condition_cell_id": cell.cell_id,
            "prompt_id": prompt.prompt_id,
            "prompt_hash": prompt.prompt_hash,
            "guidance_id": cell.guidance_id,
            "guidance_hash": cell.guidance_hash,
            "guidance_token_count": cell.token_count,
            "candidate_index": candidate_index,
            "candidate_order": candidate_order,
            "continuation_hash": continuation_hash,
            "finish_reason": finish_reason,
            "generation_metadata": generation_metadata,
            "verification_category": category.value,
            "verification_evidence_id": (
                verification_evidence.evidence_id if verification_evidence else None
            ),
            "generated_token_count": generated_token_count,
            "runtime_seconds": runtime_seconds,
            "runtime_comparability_id": runtime_comparability_id,
        }
        return cls(
            schema_version=RESULT_SCHEMA_VERSION,
            run_id=run.run_id,
            theorem_id=cell.theorem_id,
            canonical_target=canonical_target,
            theorem_record_id=theorem_record_id,
            condition=cell.condition,
            condition_cell_id=cell.cell_id,
            prompt_id=prompt.prompt_id,
            prompt_hash=prompt.prompt_hash,
            guidance_id=cell.guidance_id,
            guidance_hash=cell.guidance_hash,
            guidance_token_count=cell.token_count,
            candidate_index=candidate_index,
            candidate_order=candidate_order,
            raw_continuation=raw_continuation,
            continuation_hash=continuation_hash,
            finish_reason=finish_reason,
            generation_metadata_json=metadata_json,
            verification_category=category.value,
            verification_evidence=verification_evidence,
            generated_token_count=generated_token_count,
            runtime_seconds=runtime_seconds,
            runtime_comparability_id=runtime_comparability_id,
            result_id=stable_id("result", identity_input),
        )

    @property
    def verified(self) -> bool:
        return self.verification_category == VerificationCategory.VERIFIED_PROOF.value

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "run_id": self.run_id,
            "theorem_id": self.theorem_id,
            "canonical_target": self.canonical_target,
            "theorem_record_id": self.theorem_record_id,
            "condition": self.condition,
            "condition_cell_id": self.condition_cell_id,
            "prompt_id": self.prompt_id,
            "prompt_hash": self.prompt_hash,
            "guidance_id": self.guidance_id,
            "guidance_hash": self.guidance_hash,
            "guidance_token_count": self.guidance_token_count,
            "candidate_index": self.candidate_index,
            "candidate_order": self.candidate_order,
            "raw_continuation": self.raw_continuation,
            "continuation_hash": self.continuation_hash,
            "finish_reason": self.finish_reason,
            "generation_metadata": parse_canonical_object(
                self.generation_metadata_json, field="generation_metadata_json"
            ),
            "verification_category": self.verification_category,
            "verification_evidence": (
                self.verification_evidence.to_dict()
                if self.verification_evidence
                else None
            ),
            "generated_token_count": self.generated_token_count,
            "runtime_seconds": self.runtime_seconds,
            "runtime_comparability_id": self.runtime_comparability_id,
            "result_id": self.result_id,
        }

    @classmethod
    def from_dict(
        cls,
        value: dict[str, Any],
        *,
        run: FormalWorkerRun,
        cell: ConditionCell,
        prompt: RenderedPrompt,
    ) -> CandidateResult:
        fields = {
            "schema_version",
            "run_id",
            "theorem_id",
            "canonical_target",
            "theorem_record_id",
            "condition",
            "condition_cell_id",
            "prompt_id",
            "prompt_hash",
            "guidance_id",
            "guidance_hash",
            "guidance_token_count",
            "candidate_index",
            "candidate_order",
            "raw_continuation",
            "continuation_hash",
            "finish_reason",
            "generation_metadata",
            "verification_category",
            "verification_evidence",
            "generated_token_count",
            "runtime_seconds",
            "runtime_comparability_id",
            "result_id",
        }
        require_exact_keys(value, required=fields, field="candidate result")
        if value["schema_version"] != RESULT_SCHEMA_VERSION:
            raise ValueError("unsupported candidate result schema_version")
        evidence_value = value["verification_evidence"]
        evidence = (
            VerificationEvidence.from_dict(evidence_value)
            if evidence_value is not None
            else None
        )
        rebuilt = cls.capture(
            run=run,
            cell=cell,
            prompt=prompt,
            canonical_target=value["canonical_target"],
            theorem_record_id=value["theorem_record_id"],
            candidate_index=value["candidate_index"],
            candidate_order=value["candidate_order"],
            raw_continuation=value["raw_continuation"],
            finish_reason=value["finish_reason"],
            generation_metadata=value["generation_metadata"],
            verification_category=value["verification_category"],
            verification_evidence=evidence,
            generated_token_count=value["generated_token_count"],
            runtime_seconds=value["runtime_seconds"],
            runtime_comparability_id=value["runtime_comparability_id"],
        )
        if rebuilt.to_dict() != value:
            raise ValueError("candidate result content or binding is inconsistent")
        return rebuilt


class CandidateResultStore:
    def __init__(self) -> None:
        self._by_id: dict[str, CandidateResult] = {}
        self._by_slot: dict[tuple[str, str, str, int], str] = {}

    def add(self, result: CandidateResult) -> None:
        if result.result_id in self._by_id:
            raise ValueError(f"duplicate result: {result.result_id}")
        slot = (
            result.run_id,
            result.theorem_id,
            result.condition_cell_id,
            result.candidate_index,
        )
        if slot in self._by_slot:
            raise ValueError("candidate slot is already bound to another result")
        self._by_id[result.result_id] = result
        self._by_slot[slot] = result.result_id

    def values(self) -> tuple[CandidateResult, ...]:
        return tuple(self._by_id[key] for key in sorted(self._by_id))
