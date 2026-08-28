"""Render and validate the issue #63 canonical prior-art projection."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import unicodedata
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
PRIOR_ART_ROOT = REPO_ROOT / "research" / "prior_art"
CATALOG_PATH = PRIOR_ART_ROOT / "catalog.json"
NOTE_REQUIRED_SECTIONS = (
    "what_it_is",
    "relation_to_research",
    "scope_and_limits",
)
FRONTMATTER_KEYS = ("id", "type", "canonical_name", "aliases", "kind", "topics")


class ProjectionError(ValueError):
    """Raised when the projection contract is violated."""


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def canonical_slug(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    separated = "".join(
        character
        if character.isascii() and character.isalnum()
        else ""
        if unicodedata.combining(character)
        else "-"
        for character in normalized
    )
    ascii_value = separated.encode("ascii", "ignore").decode()
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", ascii_value.lower())).strip("-")


def note_filename(node_id: str) -> str:
    return f"{node_id[3:]}.md"


def yaml_scalar(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def evidence_line(evidence: dict[str, Any], bindings: dict[str, Any]) -> str:
    binding = bindings[evidence["family"]]
    if binding["kind"] == "mathia-interchange":
        source_ids = ", ".join(f"`{value}`" for value in evidence["source_ids"])
        unit_ids = ", ".join(f"`{value}`" for value in evidence["source_unit_ids"])
        return (
            f"- **{binding['label']}:** `{binding['objects_path']}#"
            f"{evidence['object_id']}`; source {source_ids}; unit {unit_ids}."
        )
    if binding["kind"] == "qwen-atlas":
        source_ids = ", ".join(f"`{value}`" for value in evidence["source_ids"])
        record_path = binding["entries_path"]
        record_id = evidence.get("entry_id")
        record_label = "entry"
        if record_id is None:
            record_path = binding["sources_path"]
            record_id = evidence["atlas_source_id"]
            record_label = "source record"
        return (
            f"- **{binding['label']}:** `{binding['repository']}@{binding['revision']}:"
            f"{record_path}#{record_id}`; {record_label}; source {source_ids}."
        )
    raise ProjectionError(f"unsupported evidence family: {evidence['family']}")


def render_note(node: dict[str, Any], catalog: dict[str, Any]) -> str:
    lines = ["---"]
    lines.append(f"id: {node['id']}")
    lines.append("type: prior-art")
    lines.append(f"canonical_name: {yaml_scalar(node['canonical_name'])}")
    if node["aliases"]:
        lines.append("aliases:")
        lines.extend(f"  - {yaml_scalar(alias)}" for alias in node["aliases"])
    else:
        lines.append("aliases: []")
    lines.append(f"kind: {node['kind']}")
    lines.append("topics:")
    lines.extend(f"  - {topic}" for topic in node["topics"])
    lines.extend(
        [
            "---",
            "",
            f"# {node['canonical_name']}",
            "",
            "## What it is",
            "",
            node["sections"]["what_it_is"],
            "",
            "## Relation to RH / Mathia research",
            "",
            node["sections"]["relation_to_research"],
            "",
            "## Known scope and limits",
            "",
            node["sections"]["scope_and_limits"],
            "",
            "## Related prior art",
            "",
        ]
    )
    if node["related"]:
        by_id = {item["id"]: item for item in catalog["nodes"]}
        for relation in node["related"]:
            target = by_id[relation["id"]]
            lines.append(
                f"- [{target['canonical_name']}]({note_filename(target['id'])}) — "
                f"`{relation['relation']}`"
            )
    else:
        lines.append("- None recorded in the retained evidence used for this projection.")
    lines.extend(["", "## Evidence and provenance", ""])
    lines.extend(evidence_line(item, catalog["bindings"]) for item in node["evidence"])
    lines.extend(
        [
            f"- **Projection decision:** `research/prior_art/catalog.json#{node['id']}`.",
            "",
        ]
    )
    return "\n".join(lines)


def _load_mathia_indexes(catalog: dict[str, Any]) -> dict[str, dict[str, Any]]:
    indexes: dict[str, dict[str, Any]] = {}
    for family, binding in catalog["bindings"].items():
        if binding["kind"] != "mathia-interchange":
            continue
        records = load_jsonl(REPO_ROOT / binding["objects_path"])
        indexes[family] = {record["object_id"]: record for record in records}
        freeze = load_json(REPO_ROOT / binding["freeze_path"])
        if freeze.get("freeze_id") != binding["freeze_id"]:
            raise ProjectionError(f"{family}: freeze ID does not match retained file")
    return indexes


def _qwen_file(binding: dict[str, Any], qwen_root: Path, path_key: str) -> str:
    path = binding[path_key]
    result = subprocess.run(
        ["git", "-C", str(qwen_root), "show", f"{binding['revision']}:{path}"],
        check=True,
        capture_output=True,
        text=True,
    )
    blob = subprocess.run(
        ["git", "-C", str(qwen_root), "rev-parse", f"{binding['revision']}:{path}"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    if blob != binding[f"{path_key.removesuffix('_path')}_git_blob"]:
        raise ProjectionError(f"qwen atlas {path} does not match the pinned Git blob")
    return result.stdout


def _qwen_records(
    binding: dict[str, Any], qwen_root: Path
) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    entries_text = _qwen_file(binding, qwen_root, "entries_path")
    sources_text = _qwen_file(binding, qwen_root, "sources_path")
    entries = {
        record["id"]: record
        for record in (json.loads(line) for line in entries_text.splitlines() if line)
    }
    sources = {record["id"]: record for record in json.loads(sources_text)}
    return entries, sources


def validate_catalog(catalog: dict[str, Any], qwen_root: Path | None = None) -> list[str]:
    errors: list[str] = []
    ids: set[str] = set()
    names: set[str] = set()
    identities: dict[str, str] = {}
    nodes = catalog.get("nodes", [])
    node_ids = {node.get("id") for node in nodes}
    mathia_indexes = _load_mathia_indexes(catalog)
    qwen_binding = next(
        (binding for binding in catalog["bindings"].values() if binding["kind"] == "qwen-atlas"),
        None,
    )
    qwen_indexes = _qwen_records(qwen_binding, qwen_root) if qwen_root and qwen_binding else None

    for node in nodes:
        node_id = node.get("id", "<missing-id>")
        expected_id = f"PA-{canonical_slug(node.get('canonical_name', ''))}"
        if node_id != expected_id:
            errors.append(f"{node_id}: expected deterministic ID {expected_id}")
        if node_id in ids:
            errors.append(f"{node_id}: duplicate ID")
        ids.add(node_id)
        canonical_key = node.get("canonical_name", "").casefold()
        if canonical_key in names:
            errors.append(f"{node_id}: duplicate canonical name")
        names.add(canonical_key)
        for key in ("aliases", "kind", "topics", "sections", "related", "evidence", "review"):
            if key not in node:
                errors.append(f"{node_id}: missing {key}")
        for section in NOTE_REQUIRED_SECTIONS:
            text = node.get("sections", {}).get(section, "")
            if not text.strip():
                errors.append(f"{node_id}: missing section {section}")
            if len(text) > 1800:
                errors.append(f"{node_id}: section {section} is too long for a condensed note")
        if not node.get("evidence"):
            errors.append(f"{node_id}: no positive evidence")
        for identity in node.get("canonical_identity", []):
            if identity in identities:
                errors.append(
                    f"{node_id}: canonical identity {identity} already belongs to {identities[identity]}"
                )
            identities[identity] = node_id
        for relation in node.get("related", []):
            if relation.get("id") not in node_ids:
                errors.append(f"{node_id}: dangling related node {relation.get('id')}")
        for evidence in node.get("evidence", []):
            family = evidence.get("family")
            binding = catalog["bindings"].get(family)
            if not binding:
                errors.append(f"{node_id}: unknown evidence family {family}")
                continue
            if binding["kind"] == "mathia-interchange":
                record = mathia_indexes[family].get(evidence.get("object_id"))
                if not record:
                    errors.append(f"{node_id}: unresolved object {evidence.get('object_id')}")
                    continue
                if record.get("quality_state") != "accepted":
                    errors.append(f"{node_id}: non-accepted positive evidence {record['object_id']}")
                if sorted(record.get("source_ids", [])) != sorted(evidence.get("source_ids", [])):
                    errors.append(f"{node_id}: source IDs disagree for {record['object_id']}")
                if sorted(record.get("source_unit_ids", [])) != sorted(
                    evidence.get("source_unit_ids", [])
                ):
                    errors.append(f"{node_id}: unit IDs disagree for {record['object_id']}")
            elif binding["kind"] == "qwen-atlas" and qwen_indexes is not None:
                qwen_index = qwen_indexes[0] if "entry_id" in evidence else qwen_indexes[1]
                record_key = evidence.get("entry_id", evidence.get("atlas_source_id"))
                record = qwen_index.get(record_key)
                if not record:
                    errors.append(f"{node_id}: unresolved qwen record {record_key}")
                    continue
                record_source_ids = (
                    record.get("source_ids", [])
                    if "entry_id" in evidence
                    else [record["id"]]
                )
                if sorted(record_source_ids) != sorted(evidence.get("source_ids", [])):
                    errors.append(f"{node_id}: qwen source IDs disagree for {record['id']}")
    if not nodes:
        errors.append("catalog has no nodes")
    return errors


def validate_rendered_notes(catalog: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    expected_files = {note_filename(node["id"]): node for node in catalog["nodes"]}
    actual_files = {
        path.name
        for path in PRIOR_ART_ROOT.glob("*.md")
        if path.name not in {"README.md", "COVERAGE.md", "REVIEW.md"}
    }
    if actual_files != set(expected_files):
        errors.append(
            f"rendered note set differs: missing={sorted(set(expected_files) - actual_files)}, "
            f"extra={sorted(actual_files - set(expected_files))}"
        )
    for filename, node in expected_files.items():
        path = PRIOR_ART_ROOT / filename
        if not path.exists():
            continue
        rendered = render_note(node, catalog)
        actual = path.read_text(encoding="utf-8")
        if actual != rendered:
            errors.append(f"{filename}: content differs from deterministic rendering")
        if len(actual.encode("utf-8")) > 12_000:
            errors.append(f"{filename}: note exceeds compact-note size boundary")
        if re.search(r"\]\((?!https?://)([^)#]+\.md)\)", actual):
            for target in re.findall(r"\]\((?!https?://)([^)#]+\.md)\)", actual):
                if not (PRIOR_ART_ROOT / target).exists():
                    errors.append(f"{filename}: dangling Markdown link {target}")
    return errors


def render_all(catalog: dict[str, Any]) -> None:
    expected = {note_filename(node["id"]) for node in catalog["nodes"]}
    for path in PRIOR_ART_ROOT.glob("*.md"):
        if path.name not in expected and path.name not in {"README.md", "COVERAGE.md", "REVIEW.md"}:
            path.unlink()
    for node in catalog["nodes"]:
        (PRIOR_ART_ROOT / note_filename(node["id"])).write_text(
            render_note(node, catalog), encoding="utf-8"
        )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("render", "check"))
    parser.add_argument("--qwen-root", type=Path)
    args = parser.parse_args()
    catalog = load_json(CATALOG_PATH)
    errors = validate_catalog(catalog, args.qwen_root)
    if args.command == "render" and not errors:
        render_all(catalog)
    if args.command == "check" and not errors:
        errors.extend(validate_rendered_notes(catalog))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    external = "verified" if args.qwen_root else "format-only"
    print(f"prior-art projection OK: {len(catalog['nodes'])} notes; qwen evidence {external}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
