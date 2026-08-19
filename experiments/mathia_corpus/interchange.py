from __future__ import annotations

import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


INTERCHANGE_VERSION = "mathia-corpus-interchange-v1"
OBJECT_ROLES = frozenset({"source", "interpretation", "synthesis"})
ACCEPTANCE_STATES = frozenset(
    {"accepted", "quarantined", "rejected", "evaluation_only"}
)
SIDECAR_NECESSITY = frozenset({"essential", "helpful", "provenance_only"})


def canonical_json(value: Any) -> str:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def normalize_content(value: str) -> str:
    value = value.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in value.split("\n")]
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()
    normalized: list[str] = []
    blank = False
    for line in lines:
        if not line:
            if normalized and not blank:
                normalized.append("")
            blank = True
        else:
            normalized.append(line)
            blank = False
    return "\n".join(normalized)


def build_record(
    *,
    corpus_release: str,
    corpus_origin: str,
    object_id: str,
    object_role: str,
    content: str,
    source_ids: Sequence[str],
    lineage: Sequence[Mapping[str, Any]],
    parent_ids: Sequence[str] = (),
    teacher_provenance: Mapping[str, Any] | None = None,
    acceptance_state: str = "accepted",
    training_eligible: bool = True,
    exclusion_reason: str | None = None,
    licensing: Mapping[str, Any],
    representation_dependencies: Sequence[Mapping[str, Any]] = (),
    local_metadata: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    normalized = normalize_content(content)
    return {
        "interchange_version": INTERCHANGE_VERSION,
        "corpus_release": corpus_release,
        "corpus_origin": corpus_origin,
        "object_id": object_id,
        "object_role": object_role,
        "content": normalized,
        "content_sha256": sha256_text(normalized),
        "source_ids": list(source_ids),
        "lineage": [dict(item) for item in lineage],
        "parent_ids": list(parent_ids),
        "teacher_provenance": dict(teacher_provenance) if teacher_provenance else None,
        "acceptance_state": acceptance_state,
        "training_eligible": training_eligible,
        "exclusion_reason": exclusion_reason,
        "licensing": dict(licensing),
        "representation_dependencies": [
            dict(item) for item in representation_dependencies
        ],
        "local_metadata": dict(local_metadata or {}),
    }


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        raise ValueError(f"missing JSONL file: {path}")
    records = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{line_number}: invalid JSON: {exc}") from exc
        if not isinstance(value, dict):
            raise ValueError(f"{path}:{line_number}: expected object")
        records.append(value)
    return records


def write_jsonl(path: Path, records: Iterable[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = "".join(canonical_json(dict(record)) + "\n" for record in records)
    path.write_text(text, encoding="utf-8")


def _source_records_for(
    record: Mapping[str, Any], records_by_id: Mapping[str, Mapping[str, Any]]
) -> list[Mapping[str, Any]]:
    sources = []
    for parent_id in record["parent_ids"]:
        parent = records_by_id[parent_id]
        if parent["object_role"] == "source":
            sources.append(parent)
    return sources


def render_record(
    record: Mapping[str, Any], records_by_id: Mapping[str, Mapping[str, Any]]
) -> str:
    if not record["training_eligible"]:
        raise ValueError(f'ineligible record cannot render: {record["object_id"]}')
    role = record["object_role"]
    if role == "source":
        rendered = f'# Mathematical source\n\n{record["content"]}'
    elif role == "interpretation":
        sources = _source_records_for(record, records_by_id)
        if not sources:
            raise ValueError(
                f'interpretation has no source parent: {record["object_id"]}'
            )
        source_text = "\n\n".join(source["content"] for source in sources)
        rendered = (
            f'# Mathematical source\n\n{source_text}\n\n'
            f'# Conceptual interpretation\n\n{record["content"]}'
        )
    elif role == "synthesis":
        sources = _source_records_for(record, records_by_id)
        if len(sources) < 2:
            raise ValueError(f'synthesis has fewer than two source parents: {record["object_id"]}')
        source_text = "\n\n".join(
            f'## Source {index}\n\n{source["content"]}'
            for index, source in enumerate(sources, 1)
        )
        rendered = (
            f'# Mathematical sources\n\n{source_text}\n\n'
            f'# Cross-source synthesis\n\n{record["content"]}'
        )
    else:
        raise ValueError(f"unknown object role: {role}")
    return normalize_content(rendered)


def _validate_sidecars(
    sidecars: Sequence[Mapping[str, Any]], root: Path | None
) -> tuple[list[str], dict[str, Mapping[str, Any]]]:
    errors: list[str] = []
    by_id: dict[str, Mapping[str, Any]] = {}
    for sidecar in sidecars:
        sidecar_id = sidecar.get("sidecar_id")
        if not isinstance(sidecar_id, str) or not sidecar_id:
            errors.append("sidecar missing sidecar_id")
            continue
        if sidecar_id in by_id:
            errors.append(f"duplicate sidecar id: {sidecar_id}")
        by_id[sidecar_id] = sidecar
        if sidecar.get("necessity") not in SIDECAR_NECESSITY:
            errors.append(f"invalid sidecar necessity: {sidecar_id}")
        available = sidecar.get("available")
        if not isinstance(available, bool):
            errors.append(f"sidecar availability must be boolean: {sidecar_id}")
        path = sidecar.get("path")
        if available:
            if not isinstance(path, str) or not path:
                errors.append(f"available sidecar missing path: {sidecar_id}")
            elif root is not None:
                full_path = root / path
                if not full_path.is_file():
                    errors.append(f"missing sidecar file: {sidecar_id}: {path}")
                elif hashlib.sha256(full_path.read_bytes()).hexdigest() != sidecar.get(
                    "sha256"
                ):
                    errors.append(f"sidecar hash mismatch: {sidecar_id}")
        elif not sidecar.get("unavailable_reason"):
            errors.append(f"unavailable sidecar lacks reason: {sidecar_id}")
    return errors, by_id


def validate_release(
    records: Sequence[Mapping[str, Any]],
    sidecars: Sequence[Mapping[str, Any]],
    manifest: Mapping[str, Any],
    *,
    root: Path | None = None,
) -> list[str]:
    errors, sidecars_by_id = _validate_sidecars(sidecars, root)
    records_by_id: dict[str, Mapping[str, Any]] = {}
    for record in records:
        object_id = record.get("object_id")
        if not isinstance(object_id, str) or not object_id:
            errors.append("record missing object_id")
            continue
        if object_id in records_by_id:
            errors.append(f"duplicate object id: {object_id}")
        records_by_id[object_id] = record

    for object_id, record in records_by_id.items():
        if record.get("interchange_version") != INTERCHANGE_VERSION:
            errors.append(f"interchange version mismatch: {object_id}")
        if record.get("object_role") not in OBJECT_ROLES:
            errors.append(f"invalid object role: {object_id}")
        if record.get("acceptance_state") not in ACCEPTANCE_STATES:
            errors.append(f"invalid acceptance state: {object_id}")
        content = record.get("content")
        if not isinstance(content, str) or not content:
            errors.append(f"missing content: {object_id}")
        elif content != normalize_content(content):
            errors.append(f"content is not normalized: {object_id}")
        elif record.get("content_sha256") != sha256_text(content):
            errors.append(f"content hash mismatch: {object_id}")
        eligible = record.get("training_eligible")
        accepted = record.get("acceptance_state") == "accepted"
        if not isinstance(eligible, bool):
            errors.append(f"training_eligible must be boolean: {object_id}")
        elif eligible != accepted:
            errors.append(f"acceptance/eligibility mismatch: {object_id}")
        if not eligible and not record.get("exclusion_reason"):
            errors.append(f"ineligible record lacks exclusion reason: {object_id}")
        if eligible and record.get("exclusion_reason") is not None:
            errors.append(f"eligible record has exclusion reason: {object_id}")
        source_ids = record.get("source_ids")
        lineage = record.get("lineage")
        if not isinstance(source_ids, list) or not source_ids:
            errors.append(f"record lacks source ids: {object_id}")
        if not isinstance(lineage, list) or not lineage:
            errors.append(f"record lacks lineage: {object_id}")
        else:
            lineage_sources = {item.get("source_id") for item in lineage}
            if isinstance(source_ids, list) and not set(source_ids) <= lineage_sources:
                errors.append(f"source ids missing from lineage: {object_id}")
            for item in lineage:
                if not item.get("exact_span") or not item.get("source_url"):
                    errors.append(f"incomplete lineage span: {object_id}")
        licensing = record.get("licensing")
        if not isinstance(licensing, dict) or not all(
            licensing.get(field)
            for field in ("license_id", "attribution", "redistribution")
        ):
            errors.append(f"incomplete licensing: {object_id}")
        parent_ids = record.get("parent_ids")
        if not isinstance(parent_ids, list):
            errors.append(f"parent ids must be a list: {object_id}")
            parent_ids = []
        missing_parents = [parent for parent in parent_ids if parent not in records_by_id]
        if missing_parents:
            errors.append(f"unresolved parent ids: {object_id}: {missing_parents}")
        role = record.get("object_role")
        if role == "source" and parent_ids:
            errors.append(f"source record has parents: {object_id}")
        if role == "interpretation" and not parent_ids:
            errors.append(f"interpretation lacks source parent: {object_id}")
        if role == "synthesis":
            if len(parent_ids) < 2:
                errors.append(f"synthesis has fewer than two parents: {object_id}")
            if len(set(source_ids or [])) < 2:
                errors.append(f"synthesis has fewer than two source ids: {object_id}")
        for dependency in record.get("representation_dependencies") or []:
            sidecar_id = dependency.get("sidecar_id")
            sidecar = sidecars_by_id.get(sidecar_id)
            if sidecar is None:
                errors.append(f"unresolved sidecar: {object_id}: {sidecar_id}")
                continue
            if dependency.get("necessity") != sidecar.get("necessity"):
                errors.append(f"sidecar necessity mismatch: {object_id}: {sidecar_id}")
            if eligible and dependency.get("necessity") == "essential" and not sidecar.get(
                "available"
            ):
                errors.append(f"eligible record has unavailable essential sidecar: {object_id}")

    expected_manifest = sorted(
        object_id
        for object_id, record in records_by_id.items()
        if record.get("training_eligible")
    )
    manifest_ids = manifest.get("eligible_object_ids")
    if manifest.get("interchange_version") != INTERCHANGE_VERSION:
        errors.append("manifest interchange version mismatch")
    if manifest_ids != expected_manifest:
        errors.append("trainable manifest does not exactly match eligible records")
    if len(manifest_ids or []) != len(set(manifest_ids or [])):
        errors.append("trainable manifest contains duplicate ids")

    origins = sorted({record.get("corpus_origin") for record in records})
    private_markers = [str(origin).casefold() for origin in origins if origin]
    for object_id in expected_manifest:
        record = records_by_id[object_id]
        try:
            rendered = render_record(record, records_by_id)
        except (KeyError, ValueError) as exc:
            errors.append(f"render failure: {object_id}: {exc}")
            continue
        folded = rendered.casefold()
        for marker in private_markers:
            if marker and re.search(
                rf"(?<![a-z0-9_]){re.escape(marker)}(?![a-z0-9_])", folded
            ):
                errors.append(f"corpus origin leaked into rendering: {object_id}")
        for private_value in (
            object_id,
            record.get("acceptance_state"),
            canonical_json(record.get("teacher_provenance")),
        ):
            if private_value and str(private_value).casefold() in folded:
                errors.append(f"private metadata leaked into rendering: {object_id}")
    return errors


def duplicate_content_groups(
    releases: Sequence[Sequence[Mapping[str, Any]]],
) -> list[dict[str, Any]]:
    groups: dict[tuple[str, str], list[Mapping[str, Any]]] = defaultdict(list)
    for records in releases:
        for record in records:
            groups[(record["object_role"], record["content_sha256"])].append(record)
    duplicates = []
    for (role, content_hash), records in sorted(groups.items()):
        origins = {record["corpus_origin"] for record in records}
        if len(records) > 1 and len(origins) > 1:
            duplicates.append(
                {
                    "object_role": role,
                    "content_sha256": content_hash,
                    "object_ids": sorted(record["object_id"] for record in records),
                    "corpus_origins": sorted(origins),
                }
            )
    return duplicates


def materialize_mixed_manifest(
    releases: Sequence[Sequence[Mapping[str, Any]]], *, per_release: int
) -> dict[str, Any]:
    if per_release < 1:
        raise ValueError("per_release must be positive")
    selected: list[Mapping[str, Any]] = []
    for records in releases:
        eligible = sorted(
            (record for record in records if record["training_eligible"]),
            key=lambda record: (record["object_role"], record["object_id"]),
        )
        if len(eligible) < per_release:
            raise ValueError("release does not contain enough eligible records")
        release_selection: list[Mapping[str, Any]] = []
        for role in ("source", "interpretation", "synthesis"):
            match = next((record for record in eligible if record["object_role"] == role), None)
            if match is not None and len(release_selection) < per_release:
                release_selection.append(match)
        for record in eligible:
            if len(release_selection) >= per_release:
                break
            if record not in release_selection:
                release_selection.append(record)
        selected.extend(release_selection)
    by_id = {record["object_id"]: record for records in releases for record in records}
    seen_source_hashes: set[str] = set()
    rows = []
    for record in selected:
        if record["object_role"] == "source":
            if record["content_sha256"] in seen_source_hashes:
                continue
            seen_source_hashes.add(record["content_sha256"])
        rendered = render_record(record, by_id)
        rows.append(
            {
                "object_id": record["object_id"],
                "object_role": record["object_role"],
                "content_sha256": record["content_sha256"],
                "rendered_text": rendered,
                "rendered_sha256": sha256_text(rendered),
                "private_analysis": {"corpus_origin": record["corpus_origin"]},
            }
        )
    payload = {
        "interchange_version": INTERCHANGE_VERSION,
        "mix_purpose": "compatibility_dry_run_only_no_training_ratio_decision",
        "per_release_requested": per_release,
        "duplicate_groups": duplicate_content_groups(releases),
        "records": rows,
    }
    payload["mixed_manifest_sha256"] = sha256_text(canonical_json(payload))
    return payload
