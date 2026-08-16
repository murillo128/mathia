"""Frozen condition, donor, token-budget, and length-matching mechanics."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any

from .canonical import require_exact_keys, stable_id, text_sha256
from .panel import (
    ADJACENT_DONORS,
    DISTANT_DONORS,
    GENERIC_STRATEGY_CONTROL,
    PANEL_ID,
    Presentation,
    get_control,
    get_public_target,
)
from .records import (
    GeneratorRole,
    IntuitionSample,
    LeakageDecision,
    TokenCounter,
    sample_eligibility,
)

CONDITION_SCHEMA_VERSION = "condition_cell_v1"


class Condition(str, Enum):
    NO_GUIDANCE = "no_guidance"
    FACTUAL_CONTROL = "factual_control"
    GENERIC_STRATEGY_CONTROL = "generic_strategy_control"
    ADJACENT_CROSS_THEOREM_STRATEGY = "adjacent_cross_theorem_strategy"
    DISTANT_MISMATCHED_STRATEGY = "distant_mismatched_strategy"
    QWEN_BASE_INTUITION = "qwen_base_intuition"
    CODEX_REFERENCE_INTUITION = "codex_reference_intuition"
    MATHIA_INTUITION = "mathia_intuition"


PRIMARY_CONDITIONS = tuple(Condition)
CALIBRATION_CONDITIONS = (
    Condition.NO_GUIDANCE,
    Condition.FACTUAL_CONTROL,
    Condition.GENERIC_STRATEGY_CONTROL,
    Condition.QWEN_BASE_INTUITION,
    Condition.CODEX_REFERENCE_INTUITION,
    Condition.MATHIA_INTUITION,
)

_ROLE_CONDITION = {
    GeneratorRole.QWEN_BASE.value: Condition.QWEN_BASE_INTUITION,
    GeneratorRole.CODEX_REFERENCE.value: Condition.CODEX_REFERENCE_INTUITION,
    GeneratorRole.MATHIA.value: Condition.MATHIA_INTUITION,
}


@dataclass(frozen=True)
class ConditionCell:
    schema_version: str
    panel_id: str
    theorem_id: str
    presentation: str
    condition: str
    experimental_role: str
    anchor_sample_id: str | None
    guidance_sample_id: str | None
    guidance_leakage_decision_id: str | None
    generator_config_id: str | None
    donor_theorem_id: str | None
    guidance_text: str | None
    guidance_hash: str | None
    guidance_id: str | None
    tokenizer_id: str | None
    token_count: int | None
    eligible: bool
    ineligibility_reasons: tuple[str, ...]
    cell_id: str

    @classmethod
    def _create(
        cls,
        *,
        theorem_id: str,
        presentation: Presentation | str,
        condition: Condition,
        experimental_role: str,
        anchor_sample_id: str | None = None,
        guidance_sample_id: str | None = None,
        guidance_leakage_decision_id: str | None = None,
        generator_config_id: str | None = None,
        donor_theorem_id: str | None = None,
        guidance_text: str | None = None,
        guidance_id: str | None = None,
        tokenizer_id: str | None = None,
        token_count: int | None = None,
        ineligibility_reasons: tuple[str, ...] = (),
    ) -> ConditionCell:
        target = get_public_target(theorem_id)
        presentation_value = Presentation(presentation).value
        allowed = (
            PRIMARY_CONDITIONS if target.role == "primary" else CALIBRATION_CONDITIONS
        )
        if condition not in allowed:
            raise ValueError(
                f"condition {condition.value} is not allowed for {target.role} target {theorem_id}"
            )
        guidance_hash = (
            text_sha256(guidance_text) if guidance_text is not None else None
        )
        identity_input = {
            "schema_version": CONDITION_SCHEMA_VERSION,
            "panel_id": PANEL_ID,
            "theorem_id": theorem_id,
            "presentation": presentation_value,
            "condition": condition.value,
            "experimental_role": experimental_role,
            "anchor_sample_id": anchor_sample_id,
            "guidance_sample_id": guidance_sample_id,
            "guidance_leakage_decision_id": guidance_leakage_decision_id,
            "generator_config_id": generator_config_id,
            "donor_theorem_id": donor_theorem_id,
            "guidance_hash": guidance_hash,
            "guidance_id": guidance_id,
            "tokenizer_id": tokenizer_id,
            "token_count": token_count,
            "eligible": not ineligibility_reasons,
            "ineligibility_reasons": list(ineligibility_reasons),
        }
        return cls(
            schema_version=CONDITION_SCHEMA_VERSION,
            panel_id=PANEL_ID,
            theorem_id=theorem_id,
            presentation=presentation_value,
            condition=condition.value,
            experimental_role=experimental_role,
            anchor_sample_id=anchor_sample_id,
            guidance_sample_id=guidance_sample_id,
            guidance_leakage_decision_id=guidance_leakage_decision_id,
            generator_config_id=generator_config_id,
            donor_theorem_id=donor_theorem_id,
            guidance_text=guidance_text,
            guidance_hash=guidance_hash,
            guidance_id=guidance_id,
            tokenizer_id=tokenizer_id,
            token_count=token_count,
            eligible=not ineligibility_reasons,
            ineligibility_reasons=ineligibility_reasons,
            cell_id=stable_id("condition", identity_input),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "panel_id": self.panel_id,
            "theorem_id": self.theorem_id,
            "presentation": self.presentation,
            "condition": self.condition,
            "experimental_role": self.experimental_role,
            "anchor_sample_id": self.anchor_sample_id,
            "guidance_sample_id": self.guidance_sample_id,
            "guidance_leakage_decision_id": self.guidance_leakage_decision_id,
            "generator_config_id": self.generator_config_id,
            "donor_theorem_id": self.donor_theorem_id,
            "guidance_text": self.guidance_text,
            "guidance_hash": self.guidance_hash,
            "guidance_id": self.guidance_id,
            "tokenizer_id": self.tokenizer_id,
            "token_count": self.token_count,
            "eligible": self.eligible,
            "ineligibility_reasons": list(self.ineligibility_reasons),
            "cell_id": self.cell_id,
        }

    @classmethod
    def from_dict(
        cls,
        value: dict[str, Any],
        *,
        samples: dict[str, IntuitionSample],
        decisions: dict[str, LeakageDecision],
    ) -> ConditionCell:
        fields = {
            "schema_version",
            "panel_id",
            "theorem_id",
            "presentation",
            "condition",
            "experimental_role",
            "anchor_sample_id",
            "guidance_sample_id",
            "guidance_leakage_decision_id",
            "generator_config_id",
            "donor_theorem_id",
            "guidance_text",
            "guidance_hash",
            "guidance_id",
            "tokenizer_id",
            "token_count",
            "eligible",
            "ineligibility_reasons",
            "cell_id",
        }
        require_exact_keys(value, required=fields, field="condition cell")
        if (
            value["schema_version"] != CONDITION_SCHEMA_VERSION
            or value["panel_id"] != PANEL_ID
        ):
            raise ValueError("unsupported condition schema or panel identity")
        if not isinstance(value["eligible"], bool):
            raise ValueError("condition eligible must be a boolean")
        if not isinstance(value["ineligibility_reasons"], list) or any(
            not isinstance(reason, str) for reason in value["ineligibility_reasons"]
        ):
            raise ValueError(
                "condition ineligibility_reasons must be an array of strings"
            )
        if value["token_count"] is not None and (
            not isinstance(value["token_count"], int)
            or isinstance(value["token_count"], bool)
            or value["token_count"] < 0
        ):
            raise ValueError("condition token_count must be a non-negative integer")
        selected = Condition(value["condition"])
        if selected is Condition.NO_GUIDANCE:
            rebuilt = cls._create(
                theorem_id=value["theorem_id"],
                presentation=value["presentation"],
                condition=selected,
                experimental_role="baseline",
            )
        elif selected in {
            Condition.FACTUAL_CONTROL,
            Condition.GENERIC_STRATEGY_CONTROL,
        }:
            expected_text = (
                get_control(value["theorem_id"]).factual_control
                if selected is Condition.FACTUAL_CONTROL
                else GENERIC_STRATEGY_CONTROL
            )
            expected_role = (
                "factual_control"
                if selected is Condition.FACTUAL_CONTROL
                else "generic_control"
            )
            expected_guidance_id = stable_id(
                "control",
                {
                    "panel_id": PANEL_ID,
                    "theorem_id": value["theorem_id"],
                    "condition": selected.value,
                    "text_hash": text_sha256(expected_text),
                },
            )
            rebuilt = cls._create(
                theorem_id=value["theorem_id"],
                presentation=value["presentation"],
                condition=selected,
                experimental_role=expected_role,
                guidance_text=expected_text,
                guidance_id=expected_guidance_id,
                tokenizer_id=value["tokenizer_id"],
                token_count=value["token_count"],
            )
        elif selected in {
            Condition.QWEN_BASE_INTUITION,
            Condition.CODEX_REFERENCE_INTUITION,
            Condition.MATHIA_INTUITION,
        }:
            try:
                sample = samples[value["guidance_sample_id"]]
            except KeyError as error:
                raise ValueError(
                    "relevant condition references an unknown sample"
                ) from error
            rebuilt = build_relevant_condition(
                sample=sample, decision=decisions.get(sample.sample_id)
            )
        else:
            try:
                anchor = samples[value["anchor_sample_id"]]
            except KeyError as error:
                raise ValueError(
                    "donor condition references an unknown anchor sample"
                ) from error
            donor_id = value["guidance_sample_id"]
            donor = samples.get(donor_id) if donor_id is not None else None
            rebuilt = build_donor_condition(
                receiver_theorem_id=value["theorem_id"],
                anchor_sample=anchor,
                donor_kind=(
                    "adjacent"
                    if selected is Condition.ADJACENT_CROSS_THEOREM_STRATEGY
                    else "distant"
                ),
                donor_sample=donor,
                donor_decision=decisions.get(donor_id)
                if donor_id is not None
                else None,
            )
        if rebuilt.to_dict() != value:
            raise ValueError("condition cell content or identity is inconsistent")
        return rebuilt


def build_fixed_condition(
    *,
    theorem_id: str,
    presentation: Presentation | str,
    condition: Condition | str,
    token_counter: TokenCounter,
) -> ConditionCell:
    selected = Condition(condition)
    if selected is Condition.NO_GUIDANCE:
        return ConditionCell._create(
            theorem_id=theorem_id,
            presentation=presentation,
            condition=selected,
            experimental_role="baseline",
        )
    if selected is Condition.FACTUAL_CONTROL:
        text = get_control(theorem_id).factual_control
        role = "factual_control"
    elif selected is Condition.GENERIC_STRATEGY_CONTROL:
        text = GENERIC_STRATEGY_CONTROL
        role = "generic_control"
    else:
        raise ValueError(
            "build_fixed_condition accepts only baseline and fixed controls"
        )
    tokenizer_identity = token_counter.identity
    if not isinstance(tokenizer_identity, dict) or not tokenizer_identity:
        raise ValueError("tokenizer identity must be a non-empty object")
    tokenizer_id = stable_id("tokenizer", tokenizer_identity)
    count = token_counter.count(text)
    if not isinstance(count, int) or isinstance(count, bool) or count < 0:
        raise ValueError("token counter must return a non-negative integer")
    guidance_id = stable_id(
        "control",
        {
            "panel_id": PANEL_ID,
            "theorem_id": theorem_id,
            "condition": selected.value,
            "text_hash": text_sha256(text),
        },
    )
    return ConditionCell._create(
        theorem_id=theorem_id,
        presentation=presentation,
        condition=selected,
        experimental_role=role,
        guidance_text=text,
        guidance_id=guidance_id,
        tokenizer_id=tokenizer_id,
        token_count=count,
    )


def build_relevant_condition(
    *, sample: IntuitionSample, decision: LeakageDecision | None
) -> ConditionCell:
    condition = _ROLE_CONDITION[sample.generator_role]
    eligible, reasons = sample_eligibility(sample, decision)
    del eligible
    return ConditionCell._create(
        theorem_id=sample.theorem_id,
        presentation=sample.presentation,
        condition=condition,
        experimental_role="relevant_strategy",
        anchor_sample_id=sample.sample_id,
        guidance_sample_id=sample.sample_id,
        guidance_leakage_decision_id=(decision.decision_id if decision else None),
        generator_config_id=sample.generator_config_id,
        guidance_text=sample.raw_text,
        guidance_id=sample.sample_id,
        tokenizer_id=sample.tokenizer_id,
        token_count=sample.token_count,
        ineligibility_reasons=reasons,
    )


def build_donor_condition(
    *,
    receiver_theorem_id: str,
    anchor_sample: IntuitionSample,
    donor_kind: str,
    donor_sample: IntuitionSample | None,
    donor_decision: LeakageDecision | None,
) -> ConditionCell:
    if receiver_theorem_id == "G":
        raise ValueError("calibration G has no adjacent or distant donor condition")
    if anchor_sample.theorem_id != receiver_theorem_id:
        raise ValueError(
            "anchor sample must be the relevant sample for the receiving theorem"
        )
    if donor_kind == "adjacent":
        mapping = ADJACENT_DONORS
        condition = Condition.ADJACENT_CROSS_THEOREM_STRATEGY
        role = "transfer_probe"
    elif donor_kind == "distant":
        mapping = DISTANT_DONORS
        condition = Condition.DISTANT_MISMATCHED_STRATEGY
        role = "negative_control"
    else:
        raise ValueError("donor_kind must be adjacent or distant")
    expected_donor = mapping[receiver_theorem_id]
    if donor_sample is None:
        return ConditionCell._create(
            theorem_id=receiver_theorem_id,
            presentation=anchor_sample.presentation,
            condition=condition,
            experimental_role=role,
            anchor_sample_id=anchor_sample.sample_id,
            generator_config_id=anchor_sample.generator_config_id,
            donor_theorem_id=expected_donor,
            ineligibility_reasons=("missing_donor_sample",),
        )
    if donor_sample.theorem_id != expected_donor:
        raise ValueError(
            f"{donor_kind} donor for {receiver_theorem_id} must be theorem {expected_donor}"
        )
    if donor_sample.presentation != anchor_sample.presentation:
        raise ValueError("donor and relevant samples must use the same presentation")
    if donor_sample.generator_config_id != anchor_sample.generator_config_id:
        raise ValueError("donor must use the same frozen generator configuration")
    if donor_sample.generator_role != anchor_sample.generator_role:
        raise ValueError("donor must use the same generator role")
    if donor_sample.tokenizer_id != anchor_sample.tokenizer_id:
        raise ValueError(
            "donor and relevant token counts must use the same tokenizer identity"
        )
    _, reasons = sample_eligibility(donor_sample, donor_decision)
    return ConditionCell._create(
        theorem_id=receiver_theorem_id,
        presentation=anchor_sample.presentation,
        condition=condition,
        experimental_role=role,
        anchor_sample_id=anchor_sample.sample_id,
        guidance_sample_id=donor_sample.sample_id,
        guidance_leakage_decision_id=(
            donor_decision.decision_id if donor_decision else None
        ),
        generator_config_id=anchor_sample.generator_config_id,
        donor_theorem_id=expected_donor,
        guidance_text=donor_sample.raw_text,
        guidance_id=donor_sample.sample_id,
        tokenizer_id=donor_sample.tokenizer_id,
        token_count=donor_sample.token_count,
        ineligibility_reasons=reasons,
    )


@dataclass(frozen=True)
class LengthEligibility:
    eligible: bool
    relevant_tokens: int
    distant_tokens: int
    difference: int
    maximum: int
    criterion: str = "absolute_difference <= 20_percent_of_longer"


def relevant_distant_length_eligibility(
    relevant: ConditionCell, distant: ConditionCell
) -> LengthEligibility:
    if relevant.experimental_role != "relevant_strategy":
        raise ValueError(
            "relevant cell must contain theorem-specific generated strategy"
        )
    if distant.condition != Condition.DISTANT_MISMATCHED_STRATEGY.value:
        raise ValueError("comparison cell must be distant_mismatched_strategy")
    if relevant.theorem_id != distant.theorem_id:
        raise ValueError("length comparison requires the same receiving theorem")
    if relevant.generator_config_id != distant.generator_config_id:
        raise ValueError("length comparison requires the same generator configuration")
    if relevant.tokenizer_id != distant.tokenizer_id:
        raise ValueError("length comparison requires the same tokenizer identity")
    if relevant.token_count is None or distant.token_count is None:
        raise ValueError("length comparison requires both token counts")
    difference = abs(relevant.token_count - distant.token_count)
    maximum = max(relevant.token_count, distant.token_count)
    eligible = maximum == 0 or difference * 5 <= maximum
    return LengthEligibility(
        eligible=eligible,
        relevant_tokens=relevant.token_count,
        distant_tokens=distant.token_count,
        difference=difference,
        maximum=maximum,
    )
