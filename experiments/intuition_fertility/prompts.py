"""Byte-inspectable qwen-lean whole-proof prompt intervention."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .canonical import require_exact_keys, stable_id
from .conditions import Condition, ConditionCell

PROMPT_SCHEMA_VERSION = "formal_worker_prompt_v1"
COMMENT_OPEN = b"/- Mathia guidance (frozen; natural language only)\n"
COMMENT_CLOSE = b"\n-/\n"


@dataclass(frozen=True)
class PromptTemplate:
    """Exact baseline split immediately before the declaration to be completed."""

    prefix: bytes
    declaration: bytes

    def __post_init__(self) -> None:
        if not self.declaration:
            raise ValueError("declaration must not be empty")
        if self.declaration.count(b":= by") != 1:
            raise ValueError(
                "declaration must contain exactly one ':= by' continuation point"
            )
        _, suffix = self.declaration.split(b":= by", 1)
        if suffix.strip():
            raise ValueError("declaration must end at the ':= by' continuation point")
        try:
            self.baseline.decode("utf-8")
        except UnicodeDecodeError as error:
            raise ValueError("formal-worker prompt must be valid UTF-8") from error

    @property
    def baseline(self) -> bytes:
        return self.prefix + self.declaration


def escape_lean_block_comment(text: str) -> str:
    """Escape only Lean block-comment delimiters; preserve the frozen raw record separately."""

    if "\x00" in text:
        raise ValueError("guidance containing NUL cannot be rendered")
    return text.replace("/-", "/ -").replace("-/", "- /")


def _comment_bytes(text: str) -> bytes:
    return (
        COMMENT_OPEN + escape_lean_block_comment(text).encode("utf-8") + COMMENT_CLOSE
    )


@dataclass(frozen=True)
class RenderedPrompt:
    schema_version: str
    condition_cell_id: str
    theorem_id: str
    condition: str
    baseline_hash: str
    prompt_hash: str
    prompt_id: str
    baseline_bytes: bytes
    prompt_bytes: bytes
    insertion_start: int | None
    insertion_end: int | None

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "condition_cell_id": self.condition_cell_id,
            "theorem_id": self.theorem_id,
            "condition": self.condition,
            "baseline_hash": self.baseline_hash,
            "prompt_hash": self.prompt_hash,
            "prompt_id": self.prompt_id,
            "baseline_prompt_utf8": self.baseline_bytes.decode("utf-8"),
            "prompt_utf8": self.prompt_bytes.decode("utf-8"),
            "insertion_start": self.insertion_start,
            "insertion_end": self.insertion_end,
        }


def _bytes_hash(value: bytes) -> str:
    import hashlib

    return hashlib.sha256(value).hexdigest()


def render_prompt(template: PromptTemplate, cell: ConditionCell) -> RenderedPrompt:
    if not cell.eligible:
        raise ValueError("cannot render an ineligible experimental cell")
    baseline = template.baseline
    baseline_hash = _bytes_hash(baseline)
    if cell.condition == Condition.NO_GUIDANCE.value:
        if cell.guidance_text is not None:
            raise ValueError("no_guidance cell unexpectedly carries guidance")
        prompt = baseline
        start = end = None
    else:
        if cell.guidance_text is None:
            raise ValueError("guided cell is missing guidance text")
        insertion = _comment_bytes(cell.guidance_text)
        start = len(template.prefix)
        end = start + len(insertion)
        prompt = template.prefix + insertion + template.declaration
    prompt_hash = _bytes_hash(prompt)
    prompt_id = stable_id(
        "prompt",
        {
            "schema_version": PROMPT_SCHEMA_VERSION,
            "condition_cell_id": cell.cell_id,
            "baseline_hash": baseline_hash,
            "prompt_hash": prompt_hash,
        },
    )
    return RenderedPrompt(
        schema_version=PROMPT_SCHEMA_VERSION,
        condition_cell_id=cell.cell_id,
        theorem_id=cell.theorem_id,
        condition=cell.condition,
        baseline_hash=baseline_hash,
        prompt_hash=prompt_hash,
        prompt_id=prompt_id,
        baseline_bytes=baseline,
        prompt_bytes=prompt,
        insertion_start=start,
        insertion_end=end,
    )


def import_rendered_prompt(
    value: dict[str, Any], *, cell: ConditionCell
) -> RenderedPrompt:
    fields = {
        "schema_version",
        "condition_cell_id",
        "theorem_id",
        "condition",
        "baseline_hash",
        "prompt_hash",
        "prompt_id",
        "baseline_prompt_utf8",
        "prompt_utf8",
        "insertion_start",
        "insertion_end",
    }
    require_exact_keys(value, required=fields, field="rendered prompt")
    if value["schema_version"] != PROMPT_SCHEMA_VERSION:
        raise ValueError("unsupported prompt schema_version")
    if value["condition_cell_id"] != cell.cell_id:
        raise ValueError("prompt is bound to another condition cell")
    baseline = value["baseline_prompt_utf8"].encode("utf-8")
    prompt = value["prompt_utf8"].encode("utf-8")
    if value["baseline_hash"] != _bytes_hash(baseline):
        raise ValueError("baseline prompt hash does not match its bytes")
    if value["prompt_hash"] != _bytes_hash(prompt):
        raise ValueError("rendered prompt hash does not match its bytes")
    start = value["insertion_start"]
    end = value["insertion_end"]
    if cell.condition == Condition.NO_GUIDANCE.value:
        if start is not None or end is not None or prompt != baseline:
            raise ValueError("no_guidance import must exactly reproduce the baseline")
    else:
        if (
            not isinstance(start, int)
            or isinstance(start, bool)
            or not isinstance(end, int)
            or isinstance(end, bool)
        ):
            raise ValueError("guided prompt requires integer insertion offsets")
        if not 0 <= start < end <= len(prompt):
            raise ValueError("guided prompt insertion offsets are invalid")
        expected_insertion = _comment_bytes(cell.guidance_text or "")
        if prompt[start:end] != expected_insertion:
            raise ValueError(
                "guided prompt insertion is not the frozen wrapped guidance"
            )
        if prompt[:start] + prompt[end:] != baseline:
            raise ValueError("non-intervention prompt bytes changed")
    expected_id = stable_id(
        "prompt",
        {
            "schema_version": PROMPT_SCHEMA_VERSION,
            "condition_cell_id": cell.cell_id,
            "baseline_hash": value["baseline_hash"],
            "prompt_hash": value["prompt_hash"],
        },
    )
    if value["prompt_id"] != expected_id:
        raise ValueError("prompt identity does not match its content")
    imported = RenderedPrompt(
        schema_version=PROMPT_SCHEMA_VERSION,
        condition_cell_id=cell.cell_id,
        theorem_id=value["theorem_id"],
        condition=value["condition"],
        baseline_hash=value["baseline_hash"],
        prompt_hash=value["prompt_hash"],
        prompt_id=value["prompt_id"],
        baseline_bytes=baseline,
        prompt_bytes=prompt,
        insertion_start=start,
        insertion_end=end,
    )
    if (
        imported.to_dict() != value
        or imported.theorem_id != cell.theorem_id
        or imported.condition != cell.condition
    ):
        raise ValueError("prompt content or binding is inconsistent")
    return imported


def inspect_prompt_parity(
    template: PromptTemplate, rendered: RenderedPrompt
) -> dict[str, Any]:
    """Expose the precise insertion while checking every non-intervention byte."""

    baseline = template.baseline
    if rendered.insertion_start is None:
        matches = rendered.prompt_bytes == baseline
        inserted = b""
    else:
        start = rendered.insertion_start
        end = rendered.insertion_end
        assert end is not None
        matches = (
            rendered.prompt_bytes[:start] == template.prefix
            and rendered.prompt_bytes[end:] == template.declaration
        )
        inserted = rendered.prompt_bytes[start:end]
    return {
        "baseline_hash": _bytes_hash(baseline),
        "prompt_hash": _bytes_hash(rendered.prompt_bytes),
        "non_intervention_bytes_identical": matches,
        "inserted_utf8": inserted.decode("utf-8"),
        "insertion_start": rendered.insertion_start,
        "insertion_end": rendered.insertion_end,
    }
