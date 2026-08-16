"""Provider-neutral frozen intuition and leakage-screening records."""

from __future__ import annotations

import re
from dataclasses import dataclass
from enum import Enum
from typing import Any, Protocol

from .canonical import (
    canonical_json,
    parse_canonical_object,
    require_exact_keys,
    stable_id,
    text_sha256,
)
from .panel import Presentation, generator_payload, get_public_target

INTUITION_SCHEMA_VERSION = "intuition_sample_v1"
LEAKAGE_SCHEMA_VERSION = "leakage_decision_v1"
MAX_GUIDANCE_TOKENS = 96


class GeneratorRole(str, Enum):
    QWEN_BASE = "qwen_base"
    CODEX_REFERENCE = "codex_reference"
    MATHIA = "mathia"


class LeakageLabel(str, Enum):
    STRATEGIC = "strategic"
    BORDERLINE = "borderline"
    PROOF_LIKE = "proof_like"


class TokenCounter(Protocol):
    """Minimal adapter #32 can implement with its frozen qwen-lean tokenizer."""

    @property
    def identity(self) -> dict[str, Any]: ...

    def count(self, text: str) -> int: ...


@dataclass(frozen=True)
class WhitespaceTokenCounter:
    """Synthetic deterministic adapter for mechanics tests, never a model tokenizer."""

    name: str = "synthetic_whitespace"
    revision: str = "v1"

    @property
    def identity(self) -> dict[str, Any]:
        return {"adapter": self.name, "revision": self.revision, "synthetic": True}

    def count(self, text: str) -> int:
        return len(text.split())


@dataclass(frozen=True)
class IntuitionSample:
    schema_version: str
    theorem_id: str
    presentation: str
    generator_role: str
    generator_config_json: str
    generator_config_id: str
    capture_identity: str
    sample_index: int
    raw_text: str
    text_hash: str
    tokenizer_json: str
    tokenizer_id: str
    token_count: int
    sample_id: str

    @classmethod
    def capture(
        cls,
        *,
        theorem_id: str,
        presentation: Presentation | str,
        generator_role: GeneratorRole | str,
        generator_config: dict[str, Any],
        capture_identity: str,
        sample_index: int,
        raw_text: str,
        token_counter: TokenCounter,
    ) -> IntuitionSample:
        get_public_target(theorem_id)
        presentation_value = Presentation(presentation).value
        role_value = GeneratorRole(generator_role).value
        if not isinstance(capture_identity, str) or not capture_identity:
            raise ValueError("capture_identity must be a non-empty string")
        if (
            not isinstance(sample_index, int)
            or isinstance(sample_index, bool)
            or sample_index < 0
        ):
            raise ValueError("sample_index must be a non-negative integer")
        if not isinstance(raw_text, str) or not raw_text:
            raise ValueError("raw_text must be a non-empty string")
        if not isinstance(generator_config, dict) or not generator_config:
            raise ValueError("generator_config must be a non-empty object")
        tokenizer_identity = token_counter.identity
        if not isinstance(tokenizer_identity, dict) or not tokenizer_identity:
            raise ValueError("tokenizer identity must be a non-empty object")
        generator_json = canonical_json(generator_config)
        tokenizer_json = canonical_json(tokenizer_identity)
        token_count = token_counter.count(raw_text)
        if (
            not isinstance(token_count, int)
            or isinstance(token_count, bool)
            or token_count < 0
        ):
            raise ValueError("token counter must return a non-negative integer")
        generator_id = stable_id("generator", generator_config)
        tokenizer_id = stable_id("tokenizer", tokenizer_identity)
        text_hash = text_sha256(raw_text)
        identity_input = {
            "schema_version": INTUITION_SCHEMA_VERSION,
            "theorem_id": theorem_id,
            "presentation": presentation_value,
            "generator_role": role_value,
            "generator_config_id": generator_id,
            "capture_identity": capture_identity,
            "sample_index": sample_index,
            "text_hash": text_hash,
            "tokenizer_id": tokenizer_id,
            "token_count": token_count,
        }
        return cls(
            schema_version=INTUITION_SCHEMA_VERSION,
            theorem_id=theorem_id,
            presentation=presentation_value,
            generator_role=role_value,
            generator_config_json=generator_json,
            generator_config_id=generator_id,
            capture_identity=capture_identity,
            sample_index=sample_index,
            raw_text=raw_text,
            text_hash=text_hash,
            tokenizer_json=tokenizer_json,
            tokenizer_id=tokenizer_id,
            token_count=token_count,
            sample_id=stable_id("intuition", identity_input),
        )

    @property
    def over_budget(self) -> bool:
        return self.token_count > MAX_GUIDANCE_TOKENS

    @property
    def binding_key(self) -> tuple[str, str, str, str, int]:
        return (
            self.theorem_id,
            self.presentation,
            self.generator_config_id,
            self.capture_identity,
            self.sample_index,
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "theorem_id": self.theorem_id,
            "presentation": self.presentation,
            "generator_role": self.generator_role,
            "generator_config": parse_canonical_object(
                self.generator_config_json, field="generator_config_json"
            ),
            "generator_config_id": self.generator_config_id,
            "capture_identity": self.capture_identity,
            "sample_index": self.sample_index,
            "raw_text": self.raw_text,
            "text_hash": self.text_hash,
            "tokenizer": parse_canonical_object(
                self.tokenizer_json, field="tokenizer_json"
            ),
            "tokenizer_id": self.tokenizer_id,
            "token_count": self.token_count,
            "sample_id": self.sample_id,
        }

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> IntuitionSample:
        fields = {
            "schema_version",
            "theorem_id",
            "presentation",
            "generator_role",
            "generator_config",
            "generator_config_id",
            "capture_identity",
            "sample_index",
            "raw_text",
            "text_hash",
            "tokenizer",
            "tokenizer_id",
            "token_count",
            "sample_id",
        }
        require_exact_keys(value, required=fields, field="intuition sample")
        if value["schema_version"] != INTUITION_SCHEMA_VERSION:
            raise ValueError("unsupported intuition sample schema_version")
        get_public_target(value["theorem_id"])
        Presentation(value["presentation"])
        GeneratorRole(value["generator_role"])
        if (
            not isinstance(value["generator_config"], dict)
            or not value["generator_config"]
        ):
            raise ValueError("generator_config must be a non-empty object")
        if not isinstance(value["tokenizer"], dict) or not value["tokenizer"]:
            raise ValueError("tokenizer must be a non-empty object")
        if (
            not isinstance(value["sample_index"], int)
            or isinstance(value["sample_index"], bool)
            or value["sample_index"] < 0
        ):
            raise ValueError("sample_index must be a non-negative integer")
        if (
            not isinstance(value["token_count"], int)
            or isinstance(value["token_count"], bool)
            or value["token_count"] < 0
        ):
            raise ValueError("token_count must be a non-negative integer")
        if not isinstance(value["raw_text"], str) or not value["raw_text"]:
            raise ValueError("raw_text must be a non-empty string")
        if (
            not isinstance(value["capture_identity"], str)
            or not value["capture_identity"]
        ):
            raise ValueError("capture_identity must be a non-empty string")
        generator_json = canonical_json(value["generator_config"])
        tokenizer_json = canonical_json(value["tokenizer"])
        generator_id = stable_id("generator", value["generator_config"])
        tokenizer_id = stable_id("tokenizer", value["tokenizer"])
        text_hash = text_sha256(value["raw_text"])
        identity_input = {
            "schema_version": INTUITION_SCHEMA_VERSION,
            "theorem_id": value["theorem_id"],
            "presentation": value["presentation"],
            "generator_role": value["generator_role"],
            "generator_config_id": generator_id,
            "capture_identity": value["capture_identity"],
            "sample_index": value["sample_index"],
            "text_hash": text_hash,
            "tokenizer_id": tokenizer_id,
            "token_count": value["token_count"],
        }
        expected_id = stable_id("intuition", identity_input)
        expected = {
            "generator_config_id": generator_id,
            "tokenizer_id": tokenizer_id,
            "text_hash": text_hash,
            "sample_id": expected_id,
        }
        for field, expected_value in expected.items():
            if value[field] != expected_value:
                raise ValueError(f"intuition sample {field} does not match its content")
        return cls(
            schema_version=value["schema_version"],
            theorem_id=value["theorem_id"],
            presentation=value["presentation"],
            generator_role=value["generator_role"],
            generator_config_json=generator_json,
            generator_config_id=generator_id,
            capture_identity=value["capture_identity"],
            sample_index=value["sample_index"],
            raw_text=value["raw_text"],
            text_hash=text_hash,
            tokenizer_json=tokenizer_json,
            tokenizer_id=tokenizer_id,
            token_count=value["token_count"],
            sample_id=expected_id,
        )


class FrozenIntuitionStore:
    """Append-only in-memory freeze with duplicate/conflict checks."""

    def __init__(self) -> None:
        self._by_id: dict[str, IntuitionSample] = {}
        self._by_binding: dict[tuple[str, str, str, str, int], str] = {}

    def add(self, sample: IntuitionSample) -> None:
        existing = self._by_id.get(sample.sample_id)
        if existing is not None:
            if existing != sample:
                raise ValueError(
                    f"conflicting content for frozen sample {sample.sample_id}"
                )
            raise ValueError(f"duplicate frozen sample {sample.sample_id}")
        bound_id = self._by_binding.get(sample.binding_key)
        if bound_id is not None and bound_id != sample.sample_id:
            raise ValueError(
                "capture binding is already frozen; changed text requires a new capture identity or sample index"
            )
        self._by_id[sample.sample_id] = sample
        self._by_binding[sample.binding_key] = sample.sample_id

    def get(self, sample_id: str) -> IntuitionSample:
        try:
            return self._by_id[sample_id]
        except KeyError as error:
            raise ValueError(f"unknown frozen sample: {sample_id}") from error

    def values(self) -> tuple[IntuitionSample, ...]:
        return tuple(self._by_id[key] for key in sorted(self._by_id))


@dataclass(frozen=True)
class LeakageDecision:
    schema_version: str
    sample_id: str
    classifier_payload_json: str
    classifier_payload_hash: str
    classifier_identity_json: str
    classifier_identity_id: str
    requested_label: str
    label: str
    uncertain: bool
    disputed: bool
    decision_id: str

    @classmethod
    def create(
        cls,
        *,
        sample: IntuitionSample,
        classifier_identity: dict[str, Any],
        requested_label: LeakageLabel | str,
        uncertain: bool = False,
        disputed: bool = False,
    ) -> LeakageDecision:
        label = LeakageLabel(requested_label)
        if not isinstance(classifier_identity, dict) or not classifier_identity:
            raise ValueError("classifier_identity must be a non-empty object")
        if not isinstance(uncertain, bool) or not isinstance(disputed, bool):
            raise ValueError("uncertain and disputed must be booleans")
        effective = LeakageLabel.BORDERLINE if uncertain or disputed else label
        statement = generator_payload(sample.theorem_id, sample.presentation)[
            "theorem_statement"
        ]
        payload = {
            "theorem_statement": statement,
            "candidate_guidance": sample.raw_text,
        }
        payload_json = canonical_json(payload)
        classifier_json = canonical_json(classifier_identity)
        classifier_id = stable_id("classifier", classifier_identity)
        payload_hash = text_sha256(payload_json)
        identity_input = {
            "schema_version": LEAKAGE_SCHEMA_VERSION,
            "sample_id": sample.sample_id,
            "classifier_payload_hash": payload_hash,
            "classifier_identity_id": classifier_id,
            "requested_label": label.value,
            "label": effective.value,
            "uncertain": uncertain,
            "disputed": disputed,
        }
        return cls(
            schema_version=LEAKAGE_SCHEMA_VERSION,
            sample_id=sample.sample_id,
            classifier_payload_json=payload_json,
            classifier_payload_hash=payload_hash,
            classifier_identity_json=classifier_json,
            classifier_identity_id=classifier_id,
            requested_label=label.value,
            label=effective.value,
            uncertain=uncertain,
            disputed=disputed,
            decision_id=stable_id("leakage", identity_input),
        )

    @property
    def primary_eligible(self) -> bool:
        return self.label == LeakageLabel.STRATEGIC.value

    def classifier_payload(self) -> dict[str, Any]:
        return parse_canonical_object(
            self.classifier_payload_json, field="classifier_payload_json"
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "sample_id": self.sample_id,
            "classifier_payload": self.classifier_payload(),
            "classifier_payload_hash": self.classifier_payload_hash,
            "classifier_identity": parse_canonical_object(
                self.classifier_identity_json, field="classifier_identity_json"
            ),
            "classifier_identity_id": self.classifier_identity_id,
            "requested_label": self.requested_label,
            "label": self.label,
            "uncertain": self.uncertain,
            "disputed": self.disputed,
            "decision_id": self.decision_id,
        }

    @classmethod
    def from_dict(
        cls, value: dict[str, Any], *, sample: IntuitionSample
    ) -> LeakageDecision:
        fields = {
            "schema_version",
            "sample_id",
            "classifier_payload",
            "classifier_payload_hash",
            "classifier_identity",
            "classifier_identity_id",
            "requested_label",
            "label",
            "uncertain",
            "disputed",
            "decision_id",
        }
        require_exact_keys(value, required=fields, field="leakage decision")
        if value["schema_version"] != LEAKAGE_SCHEMA_VERSION:
            raise ValueError("unsupported leakage decision schema_version")
        if value["sample_id"] != sample.sample_id:
            raise ValueError("leakage decision is bound to another sample")
        rebuilt = cls.create(
            sample=sample,
            classifier_identity=value["classifier_identity"],
            requested_label=value["requested_label"],
            uncertain=value["uncertain"],
            disputed=value["disputed"],
        )
        if rebuilt.to_dict() != value:
            raise ValueError("leakage decision content or identity is inconsistent")
        return rebuilt


class LeakageDecisionStore:
    def __init__(self) -> None:
        self._by_sample: dict[str, LeakageDecision] = {}

    def add(self, decision: LeakageDecision) -> None:
        if decision.sample_id in self._by_sample:
            raise ValueError(
                f"sample already has a frozen leakage decision: {decision.sample_id}"
            )
        self._by_sample[decision.sample_id] = decision

    def get(self, sample_id: str) -> LeakageDecision | None:
        return self._by_sample.get(sample_id)

    def values(self) -> tuple[LeakageDecision, ...]:
        return tuple(self._by_sample[key] for key in sorted(self._by_sample))


_LEAN_MARKERS = (
    (re.compile(r"(?m)^\s*(?:theorem|lemma|example)\b"), "Lean declaration"),
    (re.compile(r"(?m)(?::=\s*by\b|^\s*by\s*$)"), "Lean proof opener"),
    (
        re.compile(
            r"(?m)^\s*(?:rw|simp|simpa|exact|apply|intro|rintro|constructor|induction)\b"
        ),
        "Lean tactic",
    ),
)


def deterministic_leakage_flags(classifier_payload: dict[str, Any]) -> tuple[str, ...]:
    """Flag overt Lean transmission without pretending to judge mathematical quality."""

    if set(classifier_payload) != {"theorem_statement", "candidate_guidance"}:
        raise ValueError(
            "classifier payload may contain only theorem_statement and candidate_guidance"
        )
    guidance = classifier_payload["candidate_guidance"]
    if not isinstance(guidance, str):
        raise ValueError("candidate_guidance must be a string")
    return tuple(
        description
        for pattern, description in _LEAN_MARKERS
        if pattern.search(guidance)
    )


def sample_eligibility(
    sample: IntuitionSample, decision: LeakageDecision | None
) -> tuple[bool, tuple[str, ...]]:
    reasons: list[str] = []
    if decision is None:
        reasons.append("missing_leakage_decision")
    elif decision.sample_id != sample.sample_id:
        raise ValueError("leakage decision is bound to another sample")
    elif decision.label != LeakageLabel.STRATEGIC.value:
        reasons.append(f"leakage_label_{decision.label}")
    if sample.over_budget:
        reasons.append("over_96_token_budget")
    return not reasons, tuple(reasons)
