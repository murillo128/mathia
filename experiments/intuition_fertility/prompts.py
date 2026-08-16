"""Byte-inspectable qwen-lean whole-proof prompt intervention."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .canonical import require_exact_keys, stable_id
from .conditions import Condition, ConditionCell
from .panel import get_target_identity
from .records import escape_lean_block_comment

PROMPT_SCHEMA_VERSION = "formal_worker_prompt_v1"
PROMPT_TEMPLATE_SCHEMA_VERSION = "formal_worker_prompt_template_v1"
COMMENT_OPEN = b"/- Mathia guidance (frozen; natural language only)\n"
COMMENT_CLOSE = b"\n-/\n"
WHOLE_PROOF_CONTINUATION = b" := by\n  "


def _bytes_hash(value: bytes) -> str:
    import hashlib

    return hashlib.sha256(value).hexdigest()


@dataclass(frozen=True)
class PromptTemplate:
    """Exact baseline split immediately before the declaration to be completed."""

    theorem_id: str
    canonical_target: str
    theorem_record_id: str
    prefix: bytes
    declaration: bytes

    def __post_init__(self) -> None:
        identity = get_target_identity(self.theorem_id)
        if (
            self.canonical_target != identity.canonical_target
            or self.theorem_record_id != identity.record_id
        ):
            raise ValueError("prompt template target does not match the frozen panel")
        if not self.declaration:
            raise ValueError("declaration must not be empty")
        if not self.declaration.endswith(WHOLE_PROOF_CONTINUATION):
            raise ValueError("declaration must use the exact whole-proof continuation")
        record_declaration = self.declaration[: -len(WHOLE_PROOF_CONTINUATION)]
        if _bytes_hash(record_declaration) != identity.record_declaration_hash:
            raise ValueError(
                "prompt declaration does not match the bound Phase-2 record"
            )
        try:
            declaration_text = self.declaration.decode("utf-8")
            self.prefix.decode("utf-8")
        except UnicodeDecodeError as error:
            raise ValueError("formal-worker prompt must be valid UTF-8") from error
        declaration_head = declaration_text.split(None, 2)
        if (
            len(declaration_head) < 2
            or declaration_head[0] not in {"theorem", "lemma"}
            or declaration_head[1] != identity.record_local_declaration_name
        ):
            raise ValueError(
                "prompt declaration does not use the bound record-local name"
            )

    @property
    def baseline(self) -> bytes:
        return self.prefix + self.declaration

    @property
    def declaration_offset(self) -> int:
        return len(self.prefix)

    @property
    def prefix_hash(self) -> str:
        return _bytes_hash(self.prefix)

    @property
    def declaration_hash(self) -> str:
        return _bytes_hash(self.declaration)

    @property
    def baseline_hash(self) -> str:
        return _bytes_hash(self.baseline)

    @property
    def template_id(self) -> str:
        return stable_id(
            "prompt_template",
            {
                "schema_version": PROMPT_TEMPLATE_SCHEMA_VERSION,
                "theorem_id": self.theorem_id,
                "canonical_target": self.canonical_target,
                "theorem_record_id": self.theorem_record_id,
                "prefix_hash": self.prefix_hash,
                "declaration_hash": self.declaration_hash,
                "declaration_offset": self.declaration_offset,
            },
        )


def _comment_bytes(text: str) -> bytes:
    return (
        COMMENT_OPEN + escape_lean_block_comment(text).encode("utf-8") + COMMENT_CLOSE
    )


@dataclass(frozen=True)
class RenderedPrompt:
    schema_version: str
    condition_cell_id: str
    theorem_id: str
    canonical_target: str
    theorem_record_id: str
    condition: str
    template_id: str
    prefix_hash: str
    declaration_hash: str
    declaration_offset: int
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
            "canonical_target": self.canonical_target,
            "theorem_record_id": self.theorem_record_id,
            "condition": self.condition,
            "template_id": self.template_id,
            "prefix_hash": self.prefix_hash,
            "declaration_hash": self.declaration_hash,
            "declaration_offset": self.declaration_offset,
            "baseline_hash": self.baseline_hash,
            "prompt_hash": self.prompt_hash,
            "prompt_id": self.prompt_id,
            "baseline_prompt_utf8": self.baseline_bytes.decode("utf-8"),
            "prompt_utf8": self.prompt_bytes.decode("utf-8"),
            "insertion_start": self.insertion_start,
            "insertion_end": self.insertion_end,
        }


def render_prompt(template: PromptTemplate, cell: ConditionCell) -> RenderedPrompt:
    if not cell.eligible:
        raise ValueError("cannot render an ineligible experimental cell")
    if template.theorem_id != cell.theorem_id:
        raise ValueError("prompt template is bound to another theorem")
    baseline = template.baseline
    baseline_hash = template.baseline_hash
    if cell.condition == Condition.NO_GUIDANCE.value:
        if cell.guidance_text is not None:
            raise ValueError("no_guidance cell unexpectedly carries guidance")
        prompt = baseline
        start = end = None
    else:
        if cell.guidance_text is None:
            raise ValueError("guided cell is missing guidance text")
        insertion = _comment_bytes(cell.guidance_text)
        start = template.declaration_offset
        end = start + len(insertion)
        prompt = template.prefix + insertion + template.declaration
    prompt_hash = _bytes_hash(prompt)
    prompt_id = stable_id(
        "prompt",
        {
            "schema_version": PROMPT_SCHEMA_VERSION,
            "condition_cell_id": cell.cell_id,
            "template_id": template.template_id,
            "baseline_hash": baseline_hash,
            "prompt_hash": prompt_hash,
        },
    )
    return RenderedPrompt(
        schema_version=PROMPT_SCHEMA_VERSION,
        condition_cell_id=cell.cell_id,
        theorem_id=cell.theorem_id,
        canonical_target=template.canonical_target,
        theorem_record_id=template.theorem_record_id,
        condition=cell.condition,
        template_id=template.template_id,
        prefix_hash=template.prefix_hash,
        declaration_hash=template.declaration_hash,
        declaration_offset=template.declaration_offset,
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
        "canonical_target",
        "theorem_record_id",
        "condition",
        "template_id",
        "prefix_hash",
        "declaration_hash",
        "declaration_offset",
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
    baseline_text = value["baseline_prompt_utf8"]
    prompt_text = value["prompt_utf8"]
    declaration_offset = value["declaration_offset"]
    if not isinstance(baseline_text, str) or not isinstance(prompt_text, str):
        raise ValueError("prompt byte fields must be UTF-8 strings")
    baseline = baseline_text.encode("utf-8")
    prompt = prompt_text.encode("utf-8")
    if value["baseline_hash"] != _bytes_hash(baseline):
        raise ValueError("baseline prompt hash does not match its bytes")
    if value["prompt_hash"] != _bytes_hash(prompt):
        raise ValueError("rendered prompt hash does not match its bytes")
    if (
        not isinstance(declaration_offset, int)
        or isinstance(declaration_offset, bool)
        or not 0 <= declaration_offset < len(baseline)
    ):
        raise ValueError("prompt declaration offset is invalid")
    template = PromptTemplate(
        theorem_id=value["theorem_id"],
        canonical_target=value["canonical_target"],
        theorem_record_id=value["theorem_record_id"],
        prefix=baseline[:declaration_offset],
        declaration=baseline[declaration_offset:],
    )
    expected = render_prompt(template, cell)
    if expected.to_dict() != value:
        raise ValueError("prompt content or binding is inconsistent")
    return expected


def inspect_prompt_parity(
    template: PromptTemplate, rendered: RenderedPrompt
) -> dict[str, Any]:
    """Expose the precise insertion while checking every non-intervention byte."""

    baseline = template.baseline
    bindings_match = (
        rendered.theorem_id == template.theorem_id
        and rendered.canonical_target == template.canonical_target
        and rendered.theorem_record_id == template.theorem_record_id
        and rendered.template_id == template.template_id
        and rendered.prefix_hash == template.prefix_hash
        and rendered.declaration_hash == template.declaration_hash
        and rendered.declaration_offset == template.declaration_offset
        and rendered.baseline_hash == template.baseline_hash
        and rendered.baseline_bytes == baseline
    )
    if rendered.insertion_start is None:
        matches = bindings_match and rendered.prompt_bytes == baseline
        inserted = b""
    else:
        start = rendered.insertion_start
        end = rendered.insertion_end
        assert end is not None
        matches = (
            bindings_match
            and start == template.declaration_offset
            and rendered.prompt_bytes[:start] == template.prefix
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
