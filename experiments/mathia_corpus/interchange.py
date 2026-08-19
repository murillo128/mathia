"""Neutral trainable interchange for the issue #42/#44 Mathia corpora.

The module deliberately owns only compatibility mechanics: record identity,
validation, deterministic rendering, sidecar checks, dedup detection, and a
small mixed-manifest dry run. Corpus acquisition and mathematical QA remain
corpus-local.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping


CONTRACT_VERSION = "mathia-interchange-v1"
OBJECT_ROLES = {"source", "interpretation", "synthesis"}
QUALITY_STATES = {"accepted", "quarantined", "rejected", "evaluation_only"}
ELIGIBILITY_STATES = {"eligible", "ineligible"}
SIDECAR_RELATIONSHIPS = {"essential", "useful", "provenance_only"}
SIDECAR_AVAILABILITY = {"available", "unavailable"}
REQUIRED_FIELDS = {
    "contract_version",
    "corpus_release_id",
    "object_id",
    "object_role",
    "corpus_origin",
    "source_ids",
    "source_unit_ids",
    "span_lineage",
    "content_sha256",
    "parent_ids",
    "derivation_ids",
    "teacher_provenance",
    "quality_state",
    "training_eligibility",
    "exclusion_reason",
    "licensing_boundary",
    "representation_dependencies",
    "canonical_source_keys",
}

INTERPRETATION_REQUEST = (
    "Give a source-grounded conceptual reading of the mathematical material. "
    "Identify the mechanism, representation choices, and meaningful limits "
    "without replacing the mathematics with generic explanation."
)
SYNTHESIS_REQUEST = (
    "Develop a source-grounded synthesis of the mathematical materials. "
    "State the shared structure and also the points where the analogy or "
    "transfer stops."
)

ContentLoader = Callable[[Mapping[str, Any]], str]


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def normalize_visible_text(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError("model-visible content must be text")
    value = unicodedata.normalize("NFC", value.replace("\r\n", "\n").replace("\r", "\n"))
    # PDF extractors sometimes emit C0 bytes where a mathematical glyph could
    # not be decoded. Keep that loss visible rather than deleting or guessing
    # the symbol. Form feeds are document page breaks; every other
    # non-whitespace C0 byte becomes an explicit Unicode replacement marker.
    value = value.replace("\f", "\n")
    value = "".join(
        character if ord(character) >= 32 or character in "\n\t" else "\ufffd"
        for character in value
    )
    lines = [line.rstrip() for line in value.split("\n")]
    normalized = "\n".join(lines).strip()
    return re.sub(r"\n{3,}", "\n\n", normalized)


def stable_object_id(
    object_role: str,
    content_sha256: str,
    canonical_source_keys: Iterable[str],
    parent_ids: Iterable[str],
) -> str:
    identity = {
        "contract_version": CONTRACT_VERSION,
        "object_role": object_role,
        "content_sha256": content_sha256,
        "canonical_source_keys": sorted(set(canonical_source_keys)),
        "parent_ids": list(parent_ids),
    }
    return f"mathia_{object_role}_" + sha256_text(canonical_json(identity))


def record_content(record: Mapping[str, Any], loader: ContentLoader | None) -> str:
    has_inline = isinstance(record.get("content"), str)
    has_reference = isinstance(record.get("content_ref"), str)
    if has_inline == has_reference:
        raise ValueError(f"{record.get('object_id')}: exactly one content carrier is required")
    if has_inline:
        return normalize_visible_text(str(record["content"]))
    if loader is None:
        raise ValueError(f"{record.get('object_id')}: content_ref requires a loader")
    return normalize_visible_text(loader(record))


def _source_ancestors(
    record: Mapping[str, Any], records_by_id: Mapping[str, Mapping[str, Any]]
) -> list[Mapping[str, Any]]:
    result: list[Mapping[str, Any]] = []
    seen: set[str] = set()

    def visit(current: Mapping[str, Any]) -> None:
        object_id = str(current["object_id"])
        if object_id in seen:
            return
        seen.add(object_id)
        if current["object_role"] == "source":
            result.append(current)
            return
        for parent_id in current.get("parent_ids") or []:
            parent = records_by_id.get(parent_id)
            if parent is not None:
                visit(parent)

    visit(record)
    return result


def render_training_example(
    record: Mapping[str, Any],
    records_by_id: Mapping[str, Mapping[str, Any]],
    loader: ContentLoader,
) -> str:
    """Render one eligible object without consulting private corpus metadata."""
    if record.get("quality_state") != "accepted" or record.get("training_eligibility") != "eligible":
        raise ValueError(f"{record.get('object_id')}: only accepted eligible objects render")
    role = record.get("object_role")
    if role not in OBJECT_ROLES:
        raise ValueError(f"{record.get('object_id')}: unsupported object role")
    if role == "source":
        return "## Mathematical material\n\n" + record_content(record, loader) + "\n"

    sources = _source_ancestors(record, records_by_id)
    if not sources:
        raise ValueError(f"{record.get('object_id')}: derivative has no source ancestor")
    sections: list[str] = []
    for index, source in enumerate(sources, start=1):
        heading = "## Mathematical material" if len(sources) == 1 else f"## Mathematical material {index}"
        sections.append(heading + "\n\n" + record_content(source, loader))
    if role == "interpretation":
        request = INTERPRETATION_REQUEST
    else:
        if len(sources) < 2:
            raise ValueError(f"{record.get('object_id')}: synthesis needs at least two source ancestors")
        request = SYNTHESIS_REQUEST
    sections.extend(("## Task\n\n" + request, "## Response\n\n" + record_content(record, loader)))
    return "\n\n".join(sections) + "\n"


def _validate_sidecars(record: Mapping[str, Any], errors: list[str]) -> None:
    object_id = record.get("object_id")
    dependencies = record.get("representation_dependencies")
    if not isinstance(dependencies, list):
        errors.append(f"{object_id}: representation_dependencies must be a list")
        return
    for dependency in dependencies:
        if not isinstance(dependency, dict):
            errors.append(f"{object_id}: sidecar descriptor must be an object")
            continue
        required = {"asset_id", "relationship", "availability", "content_ref", "content_sha256"}
        if set(dependency) != required:
            errors.append(f"{object_id}: sidecar fields mismatch")
            continue
        if dependency["relationship"] not in SIDECAR_RELATIONSHIPS:
            errors.append(f"{object_id}: invalid sidecar relationship")
        if dependency["availability"] not in SIDECAR_AVAILABILITY:
            errors.append(f"{object_id}: invalid sidecar availability")
        if dependency["availability"] == "available":
            if not dependency["content_ref"] or not re.fullmatch(r"[0-9a-f]{64}", dependency["content_sha256"] or ""):
                errors.append(f"{object_id}: available sidecar needs a reference and SHA-256")
        elif dependency["content_ref"] is not None or dependency["content_sha256"] is not None:
            errors.append(f"{object_id}: unavailable sidecar must not invent content")
        if (
            dependency["relationship"] == "essential"
            and dependency["availability"] == "unavailable"
            and record.get("training_eligibility") == "eligible"
        ):
            errors.append(f"{object_id}: missing essential representation cannot be eligible")


def validate_release(
    records: Iterable[Mapping[str, Any]], loader: ContentLoader | None = None
) -> list[str]:
    records = list(records)
    errors: list[str] = []
    ids = [record.get("object_id") for record in records]
    if any(not isinstance(object_id, str) or not object_id for object_id in ids):
        errors.append("every record needs a non-empty object_id")
    if len(ids) != len(set(ids)):
        errors.append("object_id values are not unique")
    records_by_id = {str(record.get("object_id")): record for record in records}
    release_ids = {record.get("corpus_release_id") for record in records}
    if len(release_ids) != 1:
        errors.append("a release must use exactly one corpus_release_id")

    for record in records:
        object_id = record.get("object_id")
        missing = REQUIRED_FIELDS - set(record)
        if missing:
            errors.append(f"{object_id}: missing required fields {sorted(missing)}")
            continue
        if record.get("contract_version") != CONTRACT_VERSION:
            errors.append(f"{object_id}: contract_version mismatch")
        if record.get("object_role") not in OBJECT_ROLES:
            errors.append(f"{object_id}: invalid object_role")
        if record.get("quality_state") not in QUALITY_STATES:
            errors.append(f"{object_id}: invalid quality_state")
        if record.get("training_eligibility") not in ELIGIBILITY_STATES:
            errors.append(f"{object_id}: invalid training_eligibility")
        eligible = record.get("training_eligibility") == "eligible"
        if eligible != (record.get("quality_state") == "accepted"):
            errors.append(f"{object_id}: only accepted records may be eligible")
        if eligible and record.get("exclusion_reason") is not None:
            errors.append(f"{object_id}: eligible record has an exclusion_reason")
        if not eligible and not record.get("exclusion_reason"):
            errors.append(f"{object_id}: ineligible record needs an exclusion_reason")
        for field in ("source_ids", "source_unit_ids", "span_lineage", "parent_ids", "derivation_ids", "canonical_source_keys"):
            if not isinstance(record.get(field), list):
                errors.append(f"{object_id}: {field} must be a list")
        if not isinstance(record.get("teacher_provenance"), dict):
            errors.append(f"{object_id}: teacher_provenance must be an object")
        if not isinstance(record.get("licensing_boundary"), str) or not record.get("licensing_boundary"):
            errors.append(f"{object_id}: licensing_boundary is required")
        if not re.fullmatch(r"[0-9a-f]{64}", str(record.get("content_sha256") or "")):
            errors.append(f"{object_id}: invalid content_sha256")
        expected_id = stable_object_id(
            str(record.get("object_role")),
            str(record.get("content_sha256")),
            record.get("canonical_source_keys") or [],
            record.get("parent_ids") or [],
        )
        if object_id != expected_id:
            errors.append(f"{object_id}: stable object id mismatch")
        for parent_id in record.get("parent_ids") or []:
            if parent_id not in records_by_id:
                errors.append(f"{object_id}: unresolved parent {parent_id}")
        if record.get("object_role") == "source" and record.get("parent_ids"):
            errors.append(f"{object_id}: source object cannot have parents")
        if record.get("object_role") != "source" and not record.get("parent_ids"):
            errors.append(f"{object_id}: derivative needs parent_ids")
        _validate_sidecars(record, errors)
        has_inline = isinstance(record.get("content"), str)
        has_reference = isinstance(record.get("content_ref"), str)
        if has_inline == has_reference:
            errors.append(f"{object_id}: exactly one content carrier is required")
        if has_inline or (has_reference and loader is not None):
            try:
                content = record_content(record, loader)
            except (OSError, TypeError, ValueError) as error:
                errors.append(f"{object_id}: content resolution failed: {error}")
            else:
                if sha256_text(content) != record.get("content_sha256"):
                    errors.append(f"{object_id}: content hash mismatch")

    if not errors and loader is not None:
        for record in records:
            if record.get("training_eligibility") != "eligible":
                continue
            try:
                rendered = render_training_example(record, records_by_id, loader)
                counterfactual = copy.deepcopy(record)
                counterfactual["corpus_origin"] = "counterfactual-private-origin"
                counterfactual["corpus_release_id"] = "counterfactual-private-release"
                rerendered = render_training_example(counterfactual, records_by_id, loader)
            except (OSError, TypeError, ValueError) as error:
                errors.append(f"{record.get('object_id')}: rendering failed: {error}")
            else:
                if rendered != rerendered:
                    errors.append(f"{record.get('object_id')}: private metadata changes rendering")
    return errors


def duplicate_groups(releases: Iterable[Iterable[Mapping[str, Any]]]) -> list[dict[str, Any]]:
    by_hash: dict[str, list[tuple[str, str]]] = defaultdict(list)
    by_key: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for records in releases:
        for record in records:
            if record.get("object_role") == "source":
                member = (
                    str(record.get("corpus_release_id")),
                    str(record.get("object_id")),
                )
                by_hash[str(record.get("content_sha256"))].append(member)
                for key in record.get("canonical_source_keys") or []:
                    by_key[str(key)].append(member)
    groups: list[dict[str, Any]] = []
    for kind, mapping in (("content_sha256", by_hash), ("canonical_source_key", by_key)):
        for value, members in sorted(mapping.items()):
            unique = sorted(set(members))
            if len({release_id for release_id, _object_id in unique}) > 1:
                groups.append(
                    {
                        "match_kind": kind,
                        "match_value": value,
                        "members": [
                            {"corpus_release_id": release_id, "object_id": object_id}
                            for release_id, object_id in unique
                        ],
                    }
                )
    return groups


def materialize_mixed_manifest(
    releases: Iterable[Iterable[Mapping[str, Any]]],
    loaders: Iterable[ContentLoader],
    per_release: int = 3,
) -> dict[str, Any]:
    release_lists = [list(records) for records in releases]
    loader_list = list(loaders)
    if len(release_lists) != len(loader_list) or len(release_lists) < 2:
        raise ValueError("mixed dry run needs matching loaders for at least two releases")
    selections: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    seen_source_hashes: set[str] = set()
    for records, loader in zip(release_lists, loader_list, strict=True):
        by_id = {str(record["object_id"]): record for record in records}
        eligible = [record for record in records if record.get("training_eligibility") == "eligible"]
        role_order = {"source": 0, "interpretation": 1, "synthesis": 2}
        eligible.sort(key=lambda record: (role_order[str(record["object_role"])], str(record["object_id"])))
        chosen = 0
        for record in eligible:
            if record["object_id"] in seen_ids:
                continue
            if record["object_role"] == "source" and record["content_sha256"] in seen_source_hashes:
                continue
            rendered = render_training_example(record, by_id, loader)
            selections.append(
                {
                    "corpus_release_id": record["corpus_release_id"],
                    "object_id": record["object_id"],
                    "object_role": record["object_role"],
                    "rendered_sha256": sha256_text(rendered),
                    "rendered_bytes": len(rendered.encode("utf-8")),
                }
            )
            seen_ids.add(str(record["object_id"]))
            if record["object_role"] == "source":
                seen_source_hashes.add(str(record["content_sha256"]))
            chosen += 1
            if chosen == per_release:
                break
        if chosen == 0:
            raise ValueError("each release needs at least one eligible non-duplicate record")
    identity = {
        "contract_version": CONTRACT_VERSION,
        "selections": selections,
        "duplicate_groups": duplicate_groups(release_lists),
    }
    return {
        **identity,
        "manifest_id": "mathia_mixed_" + sha256_text(canonical_json(identity)),
        "purpose": "compatibility dry run only; no training ratio or training authorization",
    }


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _fixture_records() -> list[dict[str, Any]]:
    release = "mathia-agnostic-representative-v1"
    source_texts = [
        (
            "fixture_group_quotient",
            "Let G be a group and N a normal subgroup. The quotient map q:G→G/N "
            "forgets which representative of a coset was chosen while preserving multiplication: "
            "q(xy)=q(x)q(y). A map from G that is constant on cosets factors uniquely through q.",
        ),
        (
            "fixture_linear_duality",
            "For a finite-dimensional vector space V, a linear map T:V→V induces the dual map "
            "T*:V*→V* by precomposition. The annihilator of an invariant subspace is invariant "
            "under T*, translating a statement about restriction into one about a quotient.",
        ),
    ]
    records: list[dict[str, Any]] = []
    source_ids: list[str] = []
    for source_unit_id, content in source_texts:
        content = normalize_visible_text(content)
        digest = sha256_text(content)
        keys = [f"fixture:{source_unit_id}"]
        object_id = stable_object_id("source", digest, keys, [])
        source_ids.append(object_id)
        records.append(
            {
                "contract_version": CONTRACT_VERSION,
                "corpus_release_id": release,
                "object_id": object_id,
                "object_role": "source",
                "corpus_origin": "agnostic",
                "source_ids": [source_unit_id],
                "source_unit_ids": [source_unit_id],
                "span_lineage": [
                    {
                        "source_id": source_unit_id,
                        "source_unit_id": source_unit_id,
                        "line_start": 1,
                        "line_end": 1,
                        "source_normalized_sha256": digest,
                        "unit_sha256": digest,
                    }
                ],
                "content_sha256": digest,
                "content": content,
                "parent_ids": [],
                "derivation_ids": ["representative-fixture-authored-for-contract-validation"],
                "teacher_provenance": {"kind": "human-authored-fixture", "model": None},
                "quality_state": "accepted",
                "training_eligibility": "eligible",
                "exclusion_reason": None,
                "licensing_boundary": "repository-authored CC0-compatible fixture",
                "representation_dependencies": [],
                "canonical_source_keys": keys,
            }
        )
    interpretation = normalize_visible_text(
        "The quotient is not merely a smaller set: it is the universal representation that "
        "deliberately discards variation inside each coset while retaining every operation visible "
        "to coset-constant maps. Normality is the structural condition that makes the forgotten "
        "choice irrelevant to multiplication. If N were not normal, representative dependence "
        "would return and the proposed compression would stop being a group quotient."
    )
    interpretation_hash = sha256_text(interpretation)
    interpretation_id = stable_object_id(
        "interpretation", interpretation_hash, ["fixture:fixture_group_quotient"], [source_ids[0]]
    )
    records.append(
        {
            "contract_version": CONTRACT_VERSION,
            "corpus_release_id": release,
            "object_id": interpretation_id,
            "object_role": "interpretation",
            "corpus_origin": "agnostic",
            "source_ids": ["fixture_group_quotient"],
            "source_unit_ids": ["fixture_group_quotient"],
            "span_lineage": records[0]["span_lineage"],
            "content_sha256": interpretation_hash,
            "content": interpretation,
            "parent_ids": [source_ids[0]],
            "derivation_ids": ["representative-fixture-interpretation-v1"],
            "teacher_provenance": {"kind": "human-authored-fixture", "model": None},
            "quality_state": "accepted",
            "training_eligibility": "eligible",
            "exclusion_reason": None,
            "licensing_boundary": "repository-authored CC0-compatible fixture",
            "representation_dependencies": [],
            "canonical_source_keys": ["fixture:fixture_group_quotient"],
        }
    )
    synthesis = normalize_visible_text(
        "Both constructions move a problem to a representation that forgets selected information. "
        "The quotient identifies vectors or group elements directly; the annihilator records the "
        "same loss contravariantly through functionals. The shared move is controlled forgetting, "
        "but the mechanisms are not interchangeable: normality controls multiplication in the group "
        "case, whereas finite-dimensional duality controls recovery in the linear case."
    )
    synthesis_hash = sha256_text(synthesis)
    records.append(
        {
            "contract_version": CONTRACT_VERSION,
            "corpus_release_id": release,
            "object_id": stable_object_id(
                "synthesis",
                synthesis_hash,
                ["fixture:fixture_group_quotient", "fixture:fixture_linear_duality"],
                source_ids,
            ),
            "object_role": "synthesis",
            "corpus_origin": "agnostic",
            "source_ids": ["fixture_group_quotient", "fixture_linear_duality"],
            "source_unit_ids": ["fixture_group_quotient", "fixture_linear_duality"],
            "span_lineage": records[0]["span_lineage"] + records[1]["span_lineage"],
            "content_sha256": synthesis_hash,
            "content": synthesis,
            "parent_ids": source_ids,
            "derivation_ids": ["representative-fixture-synthesis-v1"],
            "teacher_provenance": {"kind": "human-authored-fixture", "model": None},
            "quality_state": "accepted",
            "training_eligibility": "eligible",
            "exclusion_reason": None,
            "licensing_boundary": "repository-authored CC0-compatible fixture",
            "representation_dependencies": [],
            "canonical_source_keys": [
                "fixture:fixture_group_quotient",
                "fixture:fixture_linear_duality",
            ],
        }
    )
    return records


def write_representative_fixture(path: Path) -> None:
    records = _fixture_records()
    errors = validate_release(records, lambda record: str(record["content"]))
    if errors:
        raise ValueError("invalid representative fixture: " + "; ".join(errors))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(canonical_json(record) + "\n" for record in records), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("build-fixture", "validate-fixture"))
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path(__file__).resolve().parent / "fixtures" / "agnostic_release.jsonl",
    )
    args = parser.parse_args(argv)
    if args.command == "build-fixture":
        write_representative_fixture(args.fixture)
        print(f"wrote {args.fixture}")
        return 0
    records = load_jsonl(args.fixture)
    errors = validate_release(records, lambda record: str(record["content"]))
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1
    print("representative fixture validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
