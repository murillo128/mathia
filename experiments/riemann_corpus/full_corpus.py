"""Corpus-scale Riemann → Mathia continuation for issue #42.

The pilot remains immutable calibration evidence. This module inspects every
usable normalized input, materializes exact semantic spans in the external
artifact store, binds isolated multi-pass interpretations, packages the common
Mathia interchange release, and validates the frozen lineage.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping

from experiments.mathia_corpus import interchange
from experiments.riemann_corpus import pipeline


HERE = Path(__file__).resolve().parent
FULL_ROOT = HERE / "full_corpus_v1"
DEFAULT_ARTIFACT_ROOT = pipeline.DEFAULT_ARTIFACT_ROOT
FULL_ARTIFACT_ROOT_NAME = "full_corpus_v1"
SOURCE_INSPECTION_PATH = FULL_ROOT / "source_inspection.jsonl"
SEGMENT_ASSIGNMENT_ROOT = FULL_ROOT / "segmentation_assignments"
SEGMENT_PLAN_ROOT = FULL_ROOT / "segmentation_plans"
SEGMENT_EXPANSION_ASSIGNMENT_ROOT = FULL_ROOT / "segmentation_expansion_assignments"
SEGMENT_EXPANSION_PLAN_ROOT = FULL_ROOT / "segmentation_expansion_plans"
UNITS_PATH = FULL_ROOT / "units.jsonl"
ANALYSIS_ASSIGNMENT_ROOT = FULL_ROOT / "analysis_assignments"
ANALYSIS_ROOT = FULL_ROOT / "analyses"
SYNTHESIS_ROOT = FULL_ROOT / "synthesis"
AUDIT_ROOT = FULL_ROOT / "audit"
AUDIT_RECONCILIATION_PATH = AUDIT_ROOT / "synthesis_reconciliation.jsonl"
OBJECTS_PATH = FULL_ROOT / "objects.jsonl"
TRAINABLE_MANIFEST_PATH = FULL_ROOT / "trainable_manifest.json"
MIXED_MANIFEST_PATH = FULL_ROOT / "mixed_manifest.json"
FREEZE_PATH = FULL_ROOT / "freeze.json"
RELEASE_MANIFEST_PATH = FULL_ROOT / "release_manifest.json"
AGNOSTIC_FIXTURE_PATH = HERE.parent / "mathia_corpus" / "fixtures" / "agnostic_release.jsonl"
RELEASE_ID = "riemann-mathia-full-v1"
INPUT_STATUSES = {
    "acquired-and-normalized",
    "acquired-partial-webtext-and-normalized",
    "acquired-partial-preview-and-normalized",
}
PASS_FILES = {
    "spontaneous": ANALYSIS_ROOT / "pass1_spontaneous.jsonl",
    "directed": ANALYSIS_ROOT / "pass2_directed.jsonl",
    "critic": ANALYSIS_ROOT / "pass3_critic.jsonl",
    "revised": ANALYSIS_ROOT / "pass4_revised.jsonl",
}
PASS_BATCH_ROOT = ANALYSIS_ROOT / "batches"
PROMPT_PATHS = {
    "spontaneous": FULL_ROOT / "prompts" / "pass12_generation.md",
    "directed": FULL_ROOT / "prompts" / "pass12_generation.md",
    "critic": FULL_ROOT / "prompts" / "pass3_critic.md",
    "revised": FULL_ROOT / "prompts" / "pass4_revision.md",
}
PASS_PAYLOAD_FIELDS = {
    "spontaneous": {"unit_id", "spontaneous_reading"},
    "directed": {
        "unit_id",
        "source_grounded_mathematics",
        "conceptual_reading",
        "representation_or_bridge",
        "boundary_or_failure",
        "uncertainty",
    },
    "critic": {
        "unit_id",
        "critic_decision",
        "supported",
        "inference",
        "unsupported_or_imported",
        "paraphrase_or_style_risk",
        "context_or_ocr_risk",
        "missed_mechanism",
        "revision_instructions",
    },
    "revised": {
        "unit_id",
        "decision",
        "interpretation",
        "source_support",
        "nonparaphrase_operation",
        "speculation_status",
        "quality_reason",
    },
}
OCR_MARKER = "OCR fallback used"
PARTIAL_WEB_REASON = (
    "manual inspection found a repository/publisher landing page, access challenge, or abstract-only "
    "record rather than a coherent mathematical source span"
)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_jsonl(path: Path, values: Iterable[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(canonical_json(value) + "\n" for value in values), encoding="utf-8")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def era(year: int | None) -> str:
    if year is None:
        return "unknown"
    if year < 1900:
        return "pre-1900"
    if year < 1950:
        return "1900-1949"
    if year < 2000:
        return "1950-1999"
    return "2000-present"


def viewpoint_tags(record: Mapping[str, Any]) -> list[str]:
    title = pipeline.normalize_title(str(record.get("title") or ""))
    tags: set[str] = set()
    rules = {
        "equivalent-criteria": ("criterion", "equivalent", "nyman", "farey", "nicolas", "superabundant"),
        "spectral-physics": ("spectral", "quantum", "physics", "string", "chaos", "phase space", "bose", "fermi", "vacuum"),
        "zero-statistics-random-matrix": ("random matrix", "pair correlation", "correlations", "mesoscopic", "characteristic polynomials"),
        "mean-values-moments": ("moment", "mean value", "value distribution", "mollifier", "divisor sums"),
        "zero-distribution": ("zero free", "zero density", "critical zeros", "zeros of", "gaps between"),
        "explicit-computation": ("explicit", "compute", "verification", "numerical", "fast methods"),
        "l-functions-families": ("l function", "dirichlet", "elliptic", "automorphic"),
        "debruijn-newman": ("newman", "de bruijn"),
        "historical-foundational": ("number of primes", "prime numbers and the riemann hypothesis"),
        "analytic-continuation-functional-equation": ("analytic continuation", "functional equation", "integral representation"),
    }
    for tag, phrases in rules.items():
        if any(phrase in title for phrase in phrases):
            tags.add(tag)
    if record.get("source_id") in {
        "riemann1859_wilkins",
        "bombieri2000_clay",
        "conrey2003_notices",
        "aim2004_resource",
    }:
        tags.add("survey-or-foundational-overview")
    if not tags:
        tags.add("other-rh-neighborhood-mechanism")
    return sorted(tags)


def _quality_metrics(text: str) -> dict[str, Any]:
    lines = text.splitlines()
    nonempty = [line for line in lines if line.strip()]
    alphabetic = sum(character.isalpha() for character in text)
    printable = sum(character.isprintable() or character in "\n\t" for character in text)
    math_cues = len(
        re.findall(
            r"(?i)\b(theorem|lemma|proposition|corollary|conjecture|proof|formula|criterion|zeros?|primes?|zeta|L-function|equivalent|bound)\b",
            text,
        )
    )
    return {
        "line_count": len(lines),
        "nonempty_line_count": len(nonempty),
        "paragraph_count": len([part for part in re.split(r"\n\s*\n", text) if part.strip()]),
        "source_page_marker_count": len(re.findall(r"<!-- source-page: \d+ -->", text)),
        "replacement_character_count": text.count("�"),
        "alphabetic_ratio": round(alphabetic / max(1, len(text)), 4),
        "printable_ratio": round(printable / max(1, len(text)), 4),
        "math_cue_count": math_cues,
        "figure_reference_count": len(re.findall(r"(?i)\b(fig(?:ure)?\.?\s*\d+)", text)),
    }


def inspect_sources(artifact_root: Path) -> None:
    records = pipeline.load_jsonl(pipeline.INVENTORY_PATH)
    inputs = [
        record
        for record in records
        if record.get("scope_status") == "relevant"
        and record.get("acquisition_status") in INPUT_STATUSES
        and record.get("normalized_relpath")
    ]
    inspections: list[dict[str, Any]] = []
    for record in inputs:
        path = artifact_root / record["normalized_relpath"]
        text = path.read_text(encoding="utf-8", errors="replace")
        metrics = _quality_metrics(text)
        warnings = list(record.get("acquisition_warnings") or [])
        ocr = any(OCR_MARKER in warning for warning in warnings)
        status = str(record["acquisition_status"])
        quality_flags = ["formula-and-reading-order-extraction-risk"]
        if ocr:
            quality_flags.append("ocr-lower-confidence-requires-prose-rich-span")
        if status == "acquired-partial-preview-and-normalized":
            quality_flags.append("partial-preview-only")
        if metrics["figure_reference_count"]:
            quality_flags.append("possible-representation-dependency")
        if metrics["replacement_character_count"]:
            quality_flags.append("replacement-characters-present")
        if int(record.get("normalized_bytes") or 0) < 10_000:
            quality_flags.append("short-normalized-source")

        if status == "acquired-partial-webtext-and-normalized":
            decision = "excluded"
            reason = PARTIAL_WEB_REASON
        elif status == "acquired-partial-preview-and-normalized":
            decision = "usable_with_limits"
            reason = (
                "the three-page preview is coherent mathematical/historical prose, but only that "
                "retained span may be used and no claim about the unseen book is allowed"
            )
        elif metrics["printable_ratio"] < 0.95 or metrics["math_cue_count"] < 3:
            decision = "excluded"
            reason = "normalized full-text response lacks sufficient readable mathematical signal"
        elif ocr:
            decision = "usable_with_limits"
            reason = (
                "OCR prose is sufficiently readable for a checked prose-rich unit; formula-dependent "
                "claims remain quarantined unless verified against the scan"
            )
        else:
            decision = "usable"
            reason = "normalized source has coherent mathematical text suitable for semantic segmentation"
        inspections.append(
            {
                "source_id": record["source_id"],
                "title": record.get("title"),
                "authors": record.get("authors") or [],
                "year": record.get("year"),
                "era": era(record.get("year")),
                "source_type": record.get("source_type"),
                "viewpoint_tags": viewpoint_tags(record),
                "acquisition_status": status,
                "normalized_relpath": record["normalized_relpath"],
                "normalized_sha256": record["normalized_sha256"],
                "normalized_bytes": record.get("normalized_bytes"),
                "normalized_page_count": record.get("normalized_page_count"),
                "ocr": ocr,
                "partial": status != "acquired-and-normalized",
                "quality_metrics": metrics,
                "quality_flags": sorted(set(quality_flags)),
                "inspection_decision": decision,
                "inspection_reason": reason,
            }
        )
    write_jsonl(SOURCE_INSPECTION_PATH, inspections)
    counts = Counter(item["inspection_decision"] for item in inspections)
    print(f"inspected {len(inspections)} normalized relevant inputs: {dict(sorted(counts.items()))}")


def _pilot_source_ids() -> set[str]:
    freeze = load_json(pipeline.PILOT_ROOT / "freeze.json")
    return {source["source_id"] for source in freeze["sources"]}


def prepare_segmentation_assignments(batch_count: int) -> None:
    inspections = load_jsonl(SOURCE_INSPECTION_PATH)
    pilot_ids = _pilot_source_ids()
    candidates = [
        item
        for item in inspections
        if item["inspection_decision"] in {"usable", "usable_with_limits"}
        and item["source_id"] not in pilot_ids
    ]
    candidates.sort(
        key=lambda item: (
            bool(item["ocr"]),
            item["era"],
            item["source_type"],
            item["source_id"],
        )
    )
    batches: list[list[dict[str, Any]]] = [[] for _ in range(batch_count)]
    for index, item in enumerate(candidates):
        batches[index % batch_count].append(item)
    if SEGMENT_ASSIGNMENT_ROOT.exists():
        shutil.rmtree(SEGMENT_ASSIGNMENT_ROOT)
    SEGMENT_ASSIGNMENT_ROOT.mkdir(parents=True)
    for index, batch in enumerate(batches, start=1):
        write_json(
            SEGMENT_ASSIGNMENT_ROOT / f"batch_{index:02d}.json",
            {
                "batch_id": f"segment-{index:02d}",
                "required_output": SEGMENT_PLAN_ROOT.relative_to(HERE).as_posix()
                + f"/batch_{index:02d}.jsonl",
                "source_count": len(batch),
                "sources": batch,
            },
        )
    print(f"assigned {len(candidates)} non-pilot sources across {batch_count} segmentation batches")


def segmentation_prompt(batch_path: Path, artifact_root: Path) -> str:
    output_name = batch_path.name.replace(".json", ".jsonl")
    output_path = SEGMENT_PLAN_ROOT / output_name
    prompt_path = FULL_ROOT / "prompts" / "segmentation.md"
    return (
        prompt_path.read_text(encoding="utf-8")
        + "\n\nRuntime assignment: `"
        + str(batch_path)
        + "`.\nExternal normalized source root: `"
        + str(artifact_root)
        + "`.\nWrite only `"
        + str(output_path)
        + "` using apply_patch."
    )


def prepare_segmentation_expansion_assignments(batch_count: int) -> None:
    """Prepare a non-quota whole-source pass after the one-unit coverage pass."""
    inspections = load_jsonl(SOURCE_INSPECTION_PATH)
    pilot_ids = _pilot_source_ids()
    initial_plans = {
        record["source_id"]: record
        for path in sorted(SEGMENT_PLAN_ROOT.glob("batch_*.jsonl"))
        for record in load_jsonl(path)
    }
    candidates = []
    for item in inspections:
        source_id = item["source_id"]
        if (
            item["inspection_decision"] not in {"usable", "usable_with_limits"}
            or source_id in pilot_ids
        ):
            continue
        initial = initial_plans.get(source_id)
        if initial is None or initial.get("segmentation_decision") != "accepted":
            raise ValueError(f"missing accepted coverage-pass unit for {source_id}")
        candidates.append({**item, "coverage_pass_unit": initial})
    candidates.sort(
        key=lambda item: (
            bool(item["ocr"]),
            item["era"],
            item["source_type"],
            item["source_id"],
        )
    )
    batches: list[list[dict[str, Any]]] = [[] for _ in range(batch_count)]
    for index, item in enumerate(candidates):
        batches[index % batch_count].append(item)
    SEGMENT_EXPANSION_ASSIGNMENT_ROOT.mkdir(parents=True, exist_ok=True)
    for old in SEGMENT_EXPANSION_ASSIGNMENT_ROOT.glob("batch_*.json"):
        old.unlink()
    for index, batch in enumerate(batches, start=1):
        write_json(
            SEGMENT_EXPANSION_ASSIGNMENT_ROOT / f"batch_{index:02d}.json",
            {
                "batch_id": f"segment-expansion-{index:02d}",
                "required_output": SEGMENT_EXPANSION_PLAN_ROOT.relative_to(HERE).as_posix()
                + f"/batch_{index:02d}.jsonl",
                "source_count": len(batch),
                "sources": batch,
            },
        )
    print(
        f"assigned {len(candidates)} non-pilot sources across {batch_count} "
        "non-quota segmentation-expansion batches"
    )


def _selected_pilot_units(artifact_root: Path) -> list[dict[str, Any]]:
    v0_units = pipeline.load_jsonl(pipeline.PILOT_ROOT / "units.jsonl")
    repairs = pipeline.load_jsonl(pipeline.CONTINUATION_ROOT / "unit_repairs.jsonl")
    repairs_by_parent = {repair["parent_unit_id"]: repair for repair in repairs}
    selected: list[dict[str, Any]] = []
    for unit in v0_units:
        active = repairs_by_parent.get(unit["unit_id"], unit)
        transcription = active.get("repair_method") == "careful-transcription-from-frozen-pdf"
        content_path = artifact_root / active["unit_artifact_relpath"]
        if not content_path.is_file() or pipeline.sha256_file(content_path) != active["unit_sha256"]:
            raise ValueError(f"pilot unit artifact missing or drifted: {active['unit_id']}")
        selected.append(
            {
                "unit_id": active["unit_id"],
                "source_id": active["source_id"],
                "unit_type": active.get("unit_type", unit.get("unit_type")),
                "line_start": None if transcription else active.get("line_start", unit.get("line_start")),
                "line_end": None if transcription else active.get("line_end", unit.get("line_end")),
                "source_span_kind": "checked-page-transcription" if transcription else "exact-normalized-line-slice",
                "source_pages": active.get("source_pages") or active.get("source_page_markers_inside_unit") or unit.get("source_page_markers_inside_unit") or [],
                "selection_reason": active.get("repaired_scope") or unit.get("purpose"),
                "context_limit": active.get("repair_reason") if active is not unit else unit.get("boundary_warning"),
                "representation_dependency": "none identified",
                "segmentation_decision": "accepted",
                "segmentation_provenance": (
                    "pilot-v1-repair" if active is not unit else "immutable-pilot-v0-calibration"
                ),
                "source_normalized_sha256": active["source_normalized_sha256"],
                "unit_artifact_relpath": active["unit_artifact_relpath"],
                "unit_sha256": active["unit_sha256"],
                "unit_bytes": active["unit_bytes"],
                "source_page_markers_inside_unit": active.get("source_page_markers_inside_unit") or [],
                "storage": "external-local-not-git",
            }
        )
    return selected


def materialize_units(artifact_root: Path) -> None:
    inspections = load_jsonl(SOURCE_INSPECTION_PATH)
    usable = {
        item["source_id"]: item
        for item in inspections
        if item["inspection_decision"] in {"usable", "usable_with_limits"}
    }
    pilot_ids = _pilot_source_ids()
    expected_nonpilot = set(usable) - pilot_ids
    plans: list[dict[str, Any]] = []
    for path in sorted(SEGMENT_PLAN_ROOT.glob("batch_*.jsonl")):
        plans.extend(load_jsonl(path))
    if {plan.get("source_id") for plan in plans} != expected_nonpilot:
        missing = sorted(expected_nonpilot - {plan.get("source_id") for plan in plans})
        extra = sorted({plan.get("source_id") for plan in plans} - expected_nonpilot)
        raise ValueError(f"segmentation plans do not exactly cover non-pilot sources; missing={missing}, extra={extra}")
    if len(plans) != len(expected_nonpilot):
        raise ValueError("segmentation plans contain duplicate source ids")

    unit_root = artifact_root / FULL_ARTIFACT_ROOT_NAME / "units"
    unit_root.mkdir(parents=True, exist_ok=True)
    units = _selected_pilot_units(artifact_root)
    for plan in sorted(plans, key=lambda item: item["source_id"]):
        source = usable[plan["source_id"]]
        decision = plan.get("segmentation_decision")
        if decision not in {"accepted", "quarantined", "excluded"}:
            raise ValueError(f"invalid segmentation decision for {plan['source_id']}")
        if decision != "accepted":
            continue
        source_path = artifact_root / source["normalized_relpath"]
        if pipeline.sha256_file(source_path) != source["normalized_sha256"]:
            raise ValueError(f"normalized source drifted: {source['source_id']}")
        lines = source_path.read_text(encoding="utf-8").splitlines(keepends=True)
        start, end = int(plan["line_start"]), int(plan["line_end"])
        if start < 1 or end < start or end > len(lines):
            raise ValueError(f"invalid semantic span for {source['source_id']}: {start}-{end}")
        content = "".join(lines[start - 1 : end])
        if not content.endswith("\n"):
            content += "\n"
        unit_id = f"full_{source['source_id']}_u01"
        unit_path = unit_root / f"{unit_id}.txt"
        unit_path.write_text(content, encoding="utf-8")
        units.append(
            {
                "unit_id": unit_id,
                "source_id": source["source_id"],
                "unit_type": plan["unit_type"],
                "line_start": start,
                "line_end": end,
                "source_span_kind": "exact-normalized-line-slice",
                "source_pages": plan.get("source_pages") or [],
                "selection_reason": plan["selection_reason"],
                "context_limit": plan.get("context_limit"),
                "representation_dependency": plan.get("representation_dependency", "none identified"),
                "segmentation_decision": "accepted",
                "segmentation_provenance": plan.get("segmentation_provenance", "isolated-codex-semantic-selection"),
                "source_normalized_sha256": source["normalized_sha256"],
                "unit_artifact_relpath": unit_path.relative_to(artifact_root).as_posix(),
                "unit_sha256": pipeline.sha256_file(unit_path),
                "unit_bytes": unit_path.stat().st_size,
                "source_page_markers_inside_unit": [
                    int(match.group(1))
                    for match in re.finditer(r"<!-- source-page: (\d+) -->", content)
                ],
                "storage": "external-local-not-git",
            }
        )

    expansion_envelopes: list[dict[str, Any]] = []
    for path in sorted(SEGMENT_EXPANSION_PLAN_ROOT.glob("batch_*.jsonl")):
        expansion_envelopes.extend(load_jsonl(path))
    if expansion_envelopes:
        expansion_sources = [record.get("source_id") for record in expansion_envelopes]
        if len(expansion_sources) != len(set(expansion_sources)) or set(expansion_sources) != expected_nonpilot:
            raise ValueError("segmentation expansion must cover every non-pilot usable source exactly once")
        existing_spans = {
            (unit["source_id"], unit.get("line_start"), unit.get("line_end"))
            for unit in units
        }
        for envelope in sorted(expansion_envelopes, key=lambda item: item["source_id"]):
            source = usable[envelope["source_id"]]
            decision = envelope.get("expansion_decision")
            additional = envelope.get("additional_units")
            if decision not in {"expanded", "no_additional_unit", "quarantined"}:
                raise ValueError(f"invalid expansion decision for {source['source_id']}")
            if not isinstance(additional, list) or len(additional) > 4:
                raise ValueError(f"invalid additional-unit list for {source['source_id']}")
            if (decision == "expanded") != bool(additional):
                raise ValueError(f"expansion decision/count mismatch for {source['source_id']}")
            source_path = artifact_root / source["normalized_relpath"]
            if pipeline.sha256_file(source_path) != source["normalized_sha256"]:
                raise ValueError(f"normalized source drifted: {source['source_id']}")
            lines = source_path.read_text(encoding="utf-8").splitlines(keepends=True)
            for offset, item in enumerate(additional, start=2):
                required = {
                    "line_start",
                    "line_end",
                    "source_pages",
                    "unit_type",
                    "selection_reason",
                    "context_limit",
                    "representation_dependency",
                }
                if set(item) != required:
                    raise ValueError(f"additional-unit fields mismatch for {source['source_id']}")
                start, end = int(item["line_start"]), int(item["line_end"])
                if start < 1 or end < start or end > len(lines):
                    raise ValueError(f"invalid expanded semantic span for {source['source_id']}: {start}-{end}")
                span = (source["source_id"], start, end)
                if span in existing_spans:
                    raise ValueError(f"duplicate semantic span in expansion for {source['source_id']}")
                existing_spans.add(span)
                content = "".join(lines[start - 1 : end])
                if not content.endswith("\n"):
                    content += "\n"
                unit_id = f"full_{source['source_id']}_u{offset:02d}"
                unit_path = unit_root / f"{unit_id}.txt"
                unit_path.write_text(content, encoding="utf-8")
                units.append(
                    {
                        "unit_id": unit_id,
                        "source_id": source["source_id"],
                        "unit_type": item["unit_type"],
                        "line_start": start,
                        "line_end": end,
                        "source_span_kind": "exact-normalized-line-slice",
                        "source_pages": item.get("source_pages") or [],
                        "selection_reason": item["selection_reason"],
                        "context_limit": item.get("context_limit"),
                        "representation_dependency": item.get("representation_dependency", "none"),
                        "segmentation_decision": "accepted",
                        "segmentation_provenance": "isolated-codex-nonquota-expansion",
                        "source_normalized_sha256": source["normalized_sha256"],
                        "unit_artifact_relpath": unit_path.relative_to(artifact_root).as_posix(),
                        "unit_sha256": pipeline.sha256_file(unit_path),
                        "unit_bytes": unit_path.stat().st_size,
                        "source_page_markers_inside_unit": [
                            int(match.group(1))
                            for match in re.finditer(r"<!-- source-page: (\d+) -->", content)
                        ],
                        "storage": "external-local-not-git",
                    }
                )
    units.sort(key=lambda item: (item["source_id"], item["unit_id"]))
    write_jsonl(UNITS_PATH, units)
    accepted_sources = {unit["source_id"] for unit in units}
    print(f"materialized {len(units)} accepted units across {len(accepted_sources)} sources")


def prepare_supplemental_analysis_assignments(batch_count: int) -> None:
    units = load_jsonl(UNITS_PATH)
    existing_ids = {
        record["unit_id"] for record in load_jsonl(PASS_FILES["revised"])
    }
    inspections = {item["source_id"]: item for item in load_jsonl(SOURCE_INSPECTION_PATH)}
    pending = []
    for unit in units:
        if unit["unit_id"] in existing_ids:
            continue
        item = dict(unit)
        item["source"] = inspections[unit["source_id"]]
        pending.append(item)
    pending.sort(key=lambda item: (item["source_id"], item["unit_id"]))
    batches: list[list[dict[str, Any]]] = [[] for _ in range(batch_count)]
    for index, item in enumerate(pending):
        batches[index % batch_count].append(item)
    start = 5
    for old in ANALYSIS_ASSIGNMENT_ROOT.glob("batch_*.json"):
        match = re.fullmatch(r"batch_(\d+)\.json", old.name)
        if match and int(match.group(1)) >= start:
            old.unlink()
    for offset, batch in enumerate(batches):
        index = start + offset
        write_json(
            ANALYSIS_ASSIGNMENT_ROOT / f"batch_{index:02d}.json",
            {
                "batch_id": f"analysis-supplemental-{index:02d}",
                "unit_count": len(batch),
                "units": batch,
            },
        )
    print(f"assigned {len(pending)} supplemental units across {batch_count} analysis batches")


def prepare_analysis_assignments(batch_count: int) -> None:
    units = load_jsonl(UNITS_PATH)
    inspections = {item["source_id"]: item for item in load_jsonl(SOURCE_INSPECTION_PATH)}
    enriched = []
    for unit in units:
        item = dict(unit)
        item["source"] = inspections[unit["source_id"]]
        enriched.append(item)
    enriched.sort(
        key=lambda item: (
            bool(item["source"]["ocr"]),
            item["source"]["era"],
            item["source"]["source_type"],
            item["source_id"],
            item["unit_id"],
        )
    )
    batches: list[list[dict[str, Any]]] = [[] for _ in range(batch_count)]
    for index, item in enumerate(enriched):
        batches[index % batch_count].append(item)
    if ANALYSIS_ASSIGNMENT_ROOT.exists():
        shutil.rmtree(ANALYSIS_ASSIGNMENT_ROOT)
    ANALYSIS_ASSIGNMENT_ROOT.mkdir(parents=True)
    for index, batch in enumerate(batches, start=1):
        write_json(
            ANALYSIS_ASSIGNMENT_ROOT / f"batch_{index:02d}.json",
            {
                "batch_id": f"analysis-{index:02d}",
                "unit_count": len(batch),
                "units": batch,
            },
        )
    print(f"assigned {len(units)} units across {batch_count} analysis batches")


def combine_analysis_batches() -> None:
    units = load_jsonl(UNITS_PATH)
    unit_ids = [unit["unit_id"] for unit in units]
    generated_at = utc_now()
    run_specs = {
        "spontaneous": "pass12",
        "directed": "pass12",
        "critic": "pass3",
        "revised": "pass4",
    }
    for pass_name, prefix in run_specs.items():
        raw_records: list[dict[str, Any]] = []
        for path in sorted(PASS_BATCH_ROOT.glob(f"{prefix}_batch_*.jsonl")):
            if prefix == "pass12":
                combined = load_jsonl(path)
                key = "spontaneous" if pass_name == "spontaneous" else "directed"
                raw_records.extend(record[key] for record in combined)
            else:
                raw_records.extend(load_jsonl(path))
        by_id = {record.get("unit_id"): record for record in raw_records}
        if len(raw_records) != len(by_id) or set(by_id) != set(unit_ids):
            raise ValueError(
                f"{pass_name} batch coverage mismatch: records={len(raw_records)}, unique={len(by_id)}, "
                f"missing={sorted(set(unit_ids) - set(by_id))}"
            )
        prompt_path = PROMPT_PATHS[pass_name]
        prompt_hash = pipeline.sha256_file(prompt_path)
        canonical_records = []
        for unit_id in unit_ids:
            payload = by_id[unit_id]
            if set(payload) != PASS_PAYLOAD_FIELDS[pass_name]:
                raise ValueError(f"{pass_name}/{unit_id}: raw output fields mismatch")
            canonical_records.append(
                {
                    "analysis_id": f"riemann_full_{pass_name}_{unit_id}",
                    "unit_id": unit_id,
                    "pass": pass_name,
                    "teacher_provenance": {
                        "provider": "openai",
                        "model": "gpt-5.4",
                        "reasoning_effort": "high",
                        "client": "codex-cli-0.148.0",
                        "execution": (
                            "same isolated pass12 context for spontaneous and directed roles"
                            if pass_name in {"spontaneous", "directed"}
                            else f"fresh isolated {pass_name} context"
                        ),
                    },
                    "prompt_relpath": prompt_path.relative_to(FULL_ROOT).as_posix(),
                    "prompt_sha256": prompt_hash,
                    "generated_at": generated_at,
                    "output": {key: value for key, value in payload.items() if key != "unit_id"},
                }
            )
        write_jsonl(PASS_FILES[pass_name], canonical_records)
    print("combined four analysis passes with exact unit coverage")


def validate_analysis() -> list[str]:
    errors: list[str] = []
    units = load_jsonl(UNITS_PATH)
    unit_ids = [unit["unit_id"] for unit in units]
    for pass_name, path in PASS_FILES.items():
        records = load_jsonl(path)
        if [record.get("unit_id") for record in records] != unit_ids:
            errors.append(f"{pass_name}: pass order/coverage mismatch")
            continue
        expected_output = PASS_PAYLOAD_FIELDS[pass_name] - {"unit_id"}
        for record in records:
            if record.get("pass") != pass_name or set(record.get("output") or {}) != expected_output:
                errors.append(f"{pass_name}/{record.get('unit_id')}: canonical output fields mismatch")
            prompt_path = FULL_ROOT / str(record.get("prompt_relpath"))
            if not prompt_path.is_file() or pipeline.sha256_file(prompt_path) != record.get("prompt_sha256"):
                errors.append(f"{pass_name}/{record.get('unit_id')}: prompt provenance mismatch")
    critic_records = load_jsonl(PASS_FILES["critic"])
    allowed_critic = {"accept_as_is", "revise", "reject", "quarantine"}
    for record in critic_records:
        if (record.get("output") or {}).get("critic_decision") not in allowed_critic:
            errors.append(f"critic/{record.get('unit_id')}: invalid critic decision")
    revised_records = load_jsonl(PASS_FILES["revised"])
    allowed_decisions = {"accepted", "rejected", "quarantined"}
    for record in revised_records:
        output = record.get("output") or {}
        if output.get("decision") not in allowed_decisions:
            errors.append(f"revised/{record.get('unit_id')}: invalid final decision")
        if output.get("decision") == "accepted" and len(str(output.get("interpretation") or "")) < 240:
            errors.append(f"revised/{record.get('unit_id')}: accepted interpretation is too short")
    return errors


def _canonical_source_keys(source: Mapping[str, Any], unit: Mapping[str, Any]) -> list[str]:
    keys = {f"source-id:{source['source_id']}", f"unit-sha256:{unit['unit_sha256']}"}
    for kind, value in (source.get("identifiers") or {}).items():
        if value:
            keys.add(f"{kind}:{str(value).lower()}")
    return sorted(keys)


def _sidecars(unit: Mapping[str, Any]) -> list[dict[str, Any]]:
    relationship = str(unit.get("representation_dependency") or "none").replace("none identified", "none")
    if relationship == "none":
        return []
    return [
        {
            "asset_id": f"representation-for-{unit['unit_id']}",
            "relationship": relationship,
            "availability": "unavailable",
            "content_ref": None,
            "content_sha256": None,
        }
    ]


def _artifact_content_loader(artifact_root: Path):
    def load(record: Mapping[str, Any]) -> str:
        if isinstance(record.get("content"), str):
            return str(record["content"])
        reference = str(record.get("content_ref") or "")
        prefix = "artifact://riemann-corpus-v0/"
        if not reference.startswith(prefix):
            raise ValueError(f"unsupported content reference: {reference}")
        return (artifact_root / reference.removeprefix(prefix)).read_text(encoding="utf-8")

    return load


def build_objects(artifact_root: Path) -> None:
    units = load_jsonl(UNITS_PATH)
    inventory = {record["source_id"]: record for record in pipeline.load_jsonl(pipeline.INVENTORY_PATH)}
    inspections = {item["source_id"]: item for item in load_jsonl(SOURCE_INSPECTION_PATH)}
    revised_by_unit = {
        record["unit_id"]: record for record in load_jsonl(PASS_FILES["revised"])
    }
    analysis_ids_by_unit: dict[str, list[str]] = defaultdict(list)
    for path in PASS_FILES.values():
        for record in load_jsonl(path):
            analysis_ids_by_unit[record["unit_id"]].append(record["analysis_id"])

    objects: list[dict[str, Any]] = []
    source_object_by_unit: dict[str, str] = {}
    for unit in units:
        source = inventory[unit["source_id"]]
        inspection = inspections[unit["source_id"]]
        unit_path = artifact_root / unit["unit_artifact_relpath"]
        content = interchange.normalize_visible_text(unit_path.read_text(encoding="utf-8"))
        content_hash = interchange.sha256_text(content)
        keys = _canonical_source_keys(source, unit)
        object_id = interchange.stable_object_id("source", content_hash, keys, [])
        source_object_by_unit[unit["unit_id"]] = object_id
        span_lineage = [
            {
                "source_id": unit["source_id"],
                "source_unit_id": unit["unit_id"],
                "source_span_kind": unit.get("source_span_kind", "exact-normalized-line-slice"),
                "line_start": unit.get("line_start"),
                "line_end": unit.get("line_end"),
                "source_pages": unit.get("source_pages") or unit.get("source_page_markers_inside_unit") or [],
                "source_normalized_sha256": unit["source_normalized_sha256"],
                "unit_sha256": unit["unit_sha256"],
            }
        ]
        objects.append(
            {
                "contract_version": interchange.CONTRACT_VERSION,
                "corpus_release_id": RELEASE_ID,
                "object_id": object_id,
                "object_role": "source",
                "corpus_origin": "riemann",
                "source_ids": [unit["source_id"]],
                "source_unit_ids": [unit["unit_id"]],
                "span_lineage": span_lineage,
                "content_sha256": content_hash,
                "content_ref": "artifact://riemann-corpus-v0/" + unit["unit_artifact_relpath"],
                "parent_ids": [],
                "derivation_ids": [str(unit["segmentation_provenance"])],
                "teacher_provenance": {
                    "kind": "semantic-unit-extraction",
                    "extractor": unit["segmentation_provenance"],
                    "pilot_lineage": unit["segmentation_provenance"].startswith(("pilot", "immutable")),
                },
                "quality_state": "accepted",
                "training_eligibility": "eligible",
                "exclusion_reason": None,
                "licensing_boundary": (
                    f"source text external-local-not-git; reported license: {source.get('license')}; "
                    "metadata and derived teacher interpretation are repository-retained"
                ),
                "representation_dependencies": _sidecars(unit),
                "canonical_source_keys": keys,
                "corpus_local_audit": {
                    "unit_type": unit.get("unit_type"),
                    "selection_reason": unit.get("selection_reason"),
                    "context_limit": unit.get("context_limit"),
                    "source_inspection_decision": inspection["inspection_decision"],
                    "source_quality_flags": inspection["quality_flags"],
                    "ocr": inspection["ocr"],
                    "partial": inspection["partial"],
                },
            }
        )

    for unit in units:
        revised = revised_by_unit[unit["unit_id"]]
        output = revised["output"]
        decision = output["decision"]
        state = {"accepted": "accepted", "rejected": "rejected", "quarantined": "quarantined"}[decision]
        content = interchange.normalize_visible_text(output["interpretation"])
        content_hash = interchange.sha256_text(content)
        parent_id = source_object_by_unit[unit["unit_id"]]
        source_record = next(record for record in objects if record["object_id"] == parent_id)
        object_id = interchange.stable_object_id(
            "interpretation", content_hash, source_record["canonical_source_keys"], [parent_id]
        )
        objects.append(
            {
                "contract_version": interchange.CONTRACT_VERSION,
                "corpus_release_id": RELEASE_ID,
                "object_id": object_id,
                "object_role": "interpretation",
                "corpus_origin": "riemann",
                "source_ids": list(source_record["source_ids"]),
                "source_unit_ids": [unit["unit_id"]],
                "span_lineage": list(source_record["span_lineage"]),
                "content_sha256": content_hash,
                "content": content,
                "parent_ids": [parent_id],
                "derivation_ids": analysis_ids_by_unit[unit["unit_id"]],
                "teacher_provenance": {
                    "kind": "codex-multi-pass-distillation",
                    "provider": "openai",
                    "model": "gpt-5.4",
                    "reasoning_effort": "high",
                    "client": "codex-cli-0.148.0",
                    "passes": ["spontaneous", "directed", "fresh critic", "fresh revision"],
                },
                "quality_state": state,
                "training_eligibility": "eligible" if state == "accepted" else "ineligible",
                "exclusion_reason": None if state == "accepted" else output["quality_reason"],
                "licensing_boundary": "repository-retained derived teacher interpretation; linked source remains external",
                "representation_dependencies": list(source_record["representation_dependencies"]),
                "canonical_source_keys": list(source_record["canonical_source_keys"]),
                "corpus_local_audit": {
                    "source_support": output["source_support"],
                    "nonparaphrase_operation": output["nonparaphrase_operation"],
                    "speculation_status": output["speculation_status"],
                    "quality_reason": output["quality_reason"],
                },
            }
        )

    synthesis_records = load_jsonl(SYNTHESIS_ROOT / "final.jsonl")
    unit_by_id = {unit["unit_id"]: unit for unit in units}
    for synthesis in synthesis_records:
        unit_ids = synthesis["source_unit_ids"]
        parent_ids = [source_object_by_unit[unit_id] for unit_id in unit_ids]
        parent_records = [next(record for record in objects if record["object_id"] == object_id) for object_id in parent_ids]
        keys = sorted({key for record in parent_records for key in record["canonical_source_keys"]})
        content_parts = [synthesis["synthesis"], "Limits: " + synthesis["limits"]]
        if synthesis.get("historical_change"):
            content_parts.append("Viewpoint change: " + synthesis["historical_change"])
        content = interchange.normalize_visible_text("\n\n".join(content_parts))
        content_hash = interchange.sha256_text(content)
        state = synthesis["decision"]
        object_id = interchange.stable_object_id("synthesis", content_hash, keys, parent_ids)
        objects.append(
            {
                "contract_version": interchange.CONTRACT_VERSION,
                "corpus_release_id": RELEASE_ID,
                "object_id": object_id,
                "object_role": "synthesis",
                "corpus_origin": "riemann",
                "source_ids": list(dict.fromkeys(unit_by_id[unit_id]["source_id"] for unit_id in unit_ids)),
                "source_unit_ids": unit_ids,
                "span_lineage": [lineage for record in parent_records for lineage in record["span_lineage"]],
                "content_sha256": content_hash,
                "content": content,
                "parent_ids": parent_ids,
                "derivation_ids": [synthesis["synthesis_id"]],
                "teacher_provenance": synthesis["teacher_provenance"],
                "quality_state": state,
                "training_eligibility": "eligible" if state == "accepted" else "ineligible",
                "exclusion_reason": None if state == "accepted" else synthesis["quality_reason"],
                "licensing_boundary": "repository-retained derived cross-source synthesis; linked sources remain external",
                "representation_dependencies": [],
                "canonical_source_keys": keys,
                "corpus_local_audit": {
                    "title": synthesis["title"],
                    "limits": synthesis["limits"],
                    "historical_change": synthesis.get("historical_change"),
                    "quality_reason": synthesis["quality_reason"],
                    "audit_reconciliation": synthesis.get("audit_reconciliation"),
                },
            }
        )

    write_jsonl(OBJECTS_PATH, objects)
    eligible = [record for record in objects if record["training_eligibility"] == "eligible"]
    manifest_identity = {
        "contract_version": interchange.CONTRACT_VERSION,
        "corpus_release_id": RELEASE_ID,
        "renderer_sha256": pipeline.sha256_file(HERE.parent / "mathia_corpus" / "interchange.py"),
        "eligible_object_ids": [record["object_id"] for record in eligible],
    }
    write_json(
        TRAINABLE_MANIFEST_PATH,
        {
            **manifest_identity,
            "manifest_id": "riemann_trainable_" + sha256_text(canonical_json(manifest_identity)),
            "object_counts": dict(Counter(record["object_role"] for record in eligible)),
            "excluded_object_counts": dict(
                Counter(record["quality_state"] for record in objects if record["training_eligibility"] == "ineligible")
            ),
            "source_content_storage": "external artifact store; redistribution-restricted text is not committed",
        },
    )

    fixture = interchange.load_jsonl(AGNOSTIC_FIXTURE_PATH)
    mixed = interchange.materialize_mixed_manifest(
        [objects, fixture],
        [_artifact_content_loader(artifact_root), lambda record: str(record["content"])],
        per_release=3,
    )
    write_json(MIXED_MANIFEST_PATH, mixed)
    print(
        f"built {len(objects)} interchange objects; {len(eligible)} eligible; "
        f"mixed dry run {mixed['manifest_id']}"
    )


def validate_objects(artifact_root: Path, require_artifacts: bool) -> list[str]:
    errors = validate_units(artifact_root, require_artifacts) + validate_analysis()
    objects = load_jsonl(OBJECTS_PATH)
    loader = _artifact_content_loader(artifact_root) if require_artifacts else None
    errors.extend(interchange.validate_release(objects, loader))
    eligible_ids = [
        record["object_id"] for record in objects if record.get("training_eligibility") == "eligible"
    ]
    if TRAINABLE_MANIFEST_PATH.is_file():
        manifest = load_json(TRAINABLE_MANIFEST_PATH)
        if manifest.get("eligible_object_ids") != eligible_ids:
            errors.append("trainable manifest does not exactly match accepted eligible objects")
    else:
        errors.append("missing trainable manifest")
    if not MIXED_MANIFEST_PATH.is_file():
        errors.append("missing synthetic mixed compatibility manifest")
    elif len(load_json(MIXED_MANIFEST_PATH).get("selections") or []) < 2:
        errors.append("synthetic mixed manifest does not sample both releases")
    source_objects = [record for record in objects if record.get("object_role") == "source"]
    interpretation_objects = [record for record in objects if record.get("object_role") == "interpretation"]
    unit_count = len(load_jsonl(UNITS_PATH))
    if len(source_objects) != unit_count or len(interpretation_objects) != unit_count:
        errors.append("release must retain one source and one interpretation object per semantic unit")
    return errors


def prepare_synthesis_assignment() -> None:
    revised = {
        record["unit_id"]: record["output"] for record in load_jsonl(PASS_FILES["revised"])
    }
    units = load_jsonl(UNITS_PATH)
    inspections = {item["source_id"]: item for item in load_jsonl(SOURCE_INSPECTION_PATH)}
    accepted = []
    for unit in units:
        output = revised[unit["unit_id"]]
        if output["decision"] != "accepted":
            continue
        source = inspections[unit["source_id"]]
        accepted.append(
            {
                "unit_id": unit["unit_id"],
                "source_id": unit["source_id"],
                "title": source["title"],
                "year": source["year"],
                "era": source["era"],
                "source_type": source["source_type"],
                "viewpoint_tags": source["viewpoint_tags"],
                "unit_type": unit["unit_type"],
                "selection_reason": unit["selection_reason"],
                "context_limit": unit.get("context_limit"),
                "unit_artifact_relpath": unit["unit_artifact_relpath"],
                "interpretation": output["interpretation"],
            }
        )
    write_json(
        SYNTHESIS_ROOT / "assignment.json",
        {
            "accepted_interpretation_count": len(accepted),
            "requested_candidate_count": 12,
            "desired_coverage": [
                "prime/zero transforms and explicit formulas",
                "equivalent criteria that relocate rather than remove difficulty",
                "zero statistics and random-matrix transfer with limits",
                "computation, certification, and finite-evidence boundaries",
                "L-function families and local/global transfer",
                "spectral or physical representations with analogy limits",
                "mean values, mollifiers, and variational choices",
                "zero-free/zero-density partial-result mechanisms",
                "de Bruijn-Newman heat-flow viewpoint",
                "exceptional sets and almost-everywhere conclusions",
                "historical changes in representation",
                "failed analogies or representations that lose decisive information",
            ],
            "units": accepted,
        },
    )
    print(f"prepared synthesis assignment from {len(accepted)} accepted interpretations")


def combine_synthesis() -> None:
    tracks = [(SYNTHESIS_ROOT / "candidates.jsonl", SYNTHESIS_ROOT / "final_raw.jsonl")]
    if (SYNTHESIS_ROOT / "expansion_candidates.jsonl").is_file():
        tracks.append(
            (
                SYNTHESIS_ROOT / "expansion_candidates.jsonl",
                SYNTHESIS_ROOT / "expansion_final_raw.jsonl",
            )
        )
    raw = [record for _candidates, final_raw in tracks for record in load_jsonl(final_raw)]
    candidate_ids = [
        record["synthesis_id"]
        for candidates, _final_raw in tracks
        for record in load_jsonl(candidates)
    ]
    if [record.get("synthesis_id") for record in raw] != candidate_ids:
        raise ValueError("final synthesis revision must cover every candidate in exact order")
    prompt_names = ["synthesis_generation.md", "synthesis_critic.md", "synthesis_revision.md"]
    if len(tracks) > 1:
        prompt_names.extend(
            (
                "synthesis_expansion_generation.md",
                "synthesis_expansion_critic.md",
                "synthesis_expansion_revision.md",
            )
        )
    prompt_hashes = {
        name: pipeline.sha256_file(FULL_ROOT / "prompts" / name) for name in prompt_names
    }
    reconciliations = {
        record["synthesis_id"]: record for record in load_jsonl(AUDIT_RECONCILIATION_PATH)
    }
    output = []
    required = {
        "synthesis_id",
        "decision",
        "title",
        "source_unit_ids",
        "synthesis",
        "limits",
        "historical_change",
        "quality_reason",
    }
    for record in raw:
        if set(record) != required:
            raise ValueError(f"{record.get('synthesis_id')}: final synthesis fields mismatch")
        resolved = dict(record)
        reconciliation = reconciliations.get(record["synthesis_id"])
        if reconciliation:
            if record["decision"] != reconciliation["previous_decision"]:
                raise ValueError(
                    f"{record['synthesis_id']}: audit reconciliation previous decision mismatch"
                )
            resolved["decision"] = reconciliation["final_decision"]
            resolved["quality_reason"] = reconciliation["reason"]
        output.append(
            {
                **resolved,
                "audit_reconciliation": reconciliation,
                "teacher_provenance": {
                    "kind": "codex-cross-source-distillation",
                    "provider": "openai",
                    "model": "gpt-5.4",
                    "reasoning_effort": "high",
                    "client": "codex-cli-0.148.0",
                    "passes": ["candidate", "fresh critic", "fresh revision"],
                    "prompt_sha256": prompt_hashes,
                },
            }
        )
    write_jsonl(SYNTHESIS_ROOT / "final.jsonl", output)
    print(f"combined {len(output)} synthesis records")


def validate_synthesis() -> list[str]:
    errors: list[str] = []
    units = {unit["unit_id"]: unit for unit in load_jsonl(UNITS_PATH)}
    candidates = load_jsonl(SYNTHESIS_ROOT / "candidates.jsonl")
    critics = load_jsonl(SYNTHESIS_ROOT / "critic.jsonl")
    if (SYNTHESIS_ROOT / "expansion_candidates.jsonl").is_file():
        expansion_candidates = load_jsonl(SYNTHESIS_ROOT / "expansion_candidates.jsonl")
        expansion_critics = load_jsonl(SYNTHESIS_ROOT / "expansion_critic.jsonl")
        if len(expansion_candidates) != 8:
            errors.append("synthesis expansion must retain exactly 8 candidates")
        candidates.extend(expansion_candidates)
        critics.extend(expansion_critics)
    final = load_jsonl(SYNTHESIS_ROOT / "final.jsonl")
    reconciliations = load_jsonl(AUDIT_RECONCILIATION_PATH)
    reconciliation_by_id = {
        record.get("synthesis_id"): record for record in reconciliations
    }
    audit_by_id = {
        record.get("object_id"): record
        for record in load_jsonl(AUDIT_ROOT / "independent_review.jsonl")
    }
    raw_by_id = {
        record["synthesis_id"]: record
        for path in (SYNTHESIS_ROOT / "final_raw.jsonl", SYNTHESIS_ROOT / "expansion_final_raw.jsonl")
        for record in load_jsonl(path)
    }
    reconciliation_fields = {
        "synthesis_id",
        "object_id",
        "previous_decision",
        "final_decision",
        "audit_decision",
        "reason",
    }
    if len(reconciliation_by_id) != len(reconciliations):
        errors.append("synthesis audit reconciliation IDs must be unique")
    for synthesis_id, reconciliation in reconciliation_by_id.items():
        if set(reconciliation) != reconciliation_fields:
            errors.append(f"{synthesis_id}: synthesis audit reconciliation fields mismatch")
            continue
        raw_record = raw_by_id.get(synthesis_id)
        audit_record = audit_by_id.get(reconciliation.get("object_id"))
        expected_final = {
            "accept": "accepted",
            "reject": "rejected",
            "quarantine": "quarantined",
        }.get(reconciliation.get("audit_decision"))
        if raw_record is None or raw_record.get("decision") != reconciliation.get("previous_decision"):
            errors.append(f"{synthesis_id}: synthesis audit reconciliation raw decision mismatch")
        if audit_record is None or audit_record.get("decision") != reconciliation.get("audit_decision"):
            errors.append(f"{synthesis_id}: synthesis audit reconciliation evidence mismatch")
        if reconciliation.get("final_decision") != expected_final:
            errors.append(f"{synthesis_id}: synthesis audit reconciliation final decision mismatch")
    ids = [record.get("synthesis_id") for record in candidates]
    if len(candidates) < 12 or len(ids) != len(set(ids)):
        errors.append("synthesis generation must retain at least 12 unique candidates")
    if [record.get("synthesis_id") for record in critics] != ids:
        errors.append("synthesis critic order/coverage mismatch")
    if [record.get("synthesis_id") for record in final] != ids:
        errors.append("final synthesis order/coverage mismatch")
    for record in final:
        unit_ids = record.get("source_unit_ids") or []
        if len(unit_ids) < 2 or any(unit_id not in units for unit_id in unit_ids):
            errors.append(f"{record.get('synthesis_id')}: synthesis parent units do not resolve")
            continue
        source_ids = {units[unit_id]["source_id"] for unit_id in unit_ids}
        if len(source_ids) < 2:
            errors.append(f"{record.get('synthesis_id')}: synthesis needs at least two distinct sources")
        if record.get("decision") not in {"accepted", "rejected", "quarantined"}:
            errors.append(f"{record.get('synthesis_id')}: invalid final synthesis decision")
        if record.get("decision") == "accepted" and len(str(record.get("synthesis") or "")) < 300:
            errors.append(f"{record.get('synthesis_id')}: accepted synthesis is too short")
        reconciliation = reconciliation_by_id.get(record.get("synthesis_id"))
        if record.get("audit_reconciliation") != reconciliation:
            errors.append(f"{record.get('synthesis_id')}: synthesis audit reconciliation not preserved")
        if reconciliation and (
            record.get("decision") != reconciliation["final_decision"]
            or record.get("quality_reason") != reconciliation["reason"]
        ):
            errors.append(f"{record.get('synthesis_id')}: reconciled synthesis decision drift")
    return errors


def prepare_synthesis_expansion_assignment() -> None:
    revised = {
        record["unit_id"]: record["output"] for record in load_jsonl(PASS_FILES["revised"])
    }
    units = load_jsonl(UNITS_PATH)
    inspections = {item["source_id"]: item for item in load_jsonl(SOURCE_INSPECTION_PATH)}
    accepted = []
    for unit in units:
        output = revised[unit["unit_id"]]
        if output["decision"] != "accepted":
            continue
        source = inspections[unit["source_id"]]
        accepted.append(
            {
                "unit_id": unit["unit_id"],
                "source_id": unit["source_id"],
                "title": source["title"],
                "year": source["year"],
                "era": source["era"],
                "source_type": source["source_type"],
                "viewpoint_tags": source["viewpoint_tags"],
                "unit_type": unit["unit_type"],
                "selection_reason": unit["selection_reason"],
                "context_limit": unit.get("context_limit"),
                "unit_artifact_relpath": unit["unit_artifact_relpath"],
                "interpretation": output["interpretation"],
                "is_nonquota_expansion_unit": unit.get("segmentation_provenance")
                == "isolated-codex-nonquota-expansion",
            }
        )
    expansion_count = sum(item["is_nonquota_expansion_unit"] for item in accepted)
    write_json(
        SYNTHESIS_ROOT / "expansion_assignment.json",
        {
            "accepted_interpretation_count": len(accepted),
            "accepted_nonquota_expansion_count": expansion_count,
            "requested_candidate_count": 8,
            "requirement": (
                "each candidate must use at least one non-quota expansion unit and expose a "
                "shared role not already covered by the first synthesis track"
            ),
            "units": accepted,
        },
    )
    print(
        f"prepared synthesis expansion from {len(accepted)} accepted interpretations, "
        f"including {expansion_count} non-quota expansion units"
    )


def prepare_audit_assignment() -> None:
    objects = load_jsonl(OBJECTS_PATH)
    units = {unit["unit_id"]: unit for unit in load_jsonl(UNITS_PATH)}
    inspections = {item["source_id"]: item for item in load_jsonl(SOURCE_INSPECTION_PATH)}
    interpretations = [record for record in objects if record["object_role"] == "interpretation"]
    candidates = []
    for record in interpretations:
        unit_id = record["source_unit_ids"][0]
        unit = units[unit_id]
        source = inspections[unit["source_id"]]
        candidates.append(
            {
                "object_id": record["object_id"],
                "current_quality_state": record["quality_state"],
                "source_id": unit["source_id"],
                "source_unit_id": unit_id,
                "unit_artifact_relpath": unit["unit_artifact_relpath"],
                "interpretation": record["content"],
                "era": source["era"],
                "source_type": source["source_type"],
                "viewpoint_tags": source["viewpoint_tags"],
                "ocr": source["ocr"],
                "partial": source["partial"],
                "unit_type": unit["unit_type"],
                "segmentation_provenance": unit["segmentation_provenance"],
                "context_limit": unit.get("context_limit"),
            }
        )

    selected: list[dict[str, Any]] = []
    selected_ids: set[str] = set()

    def select(item: dict[str, Any]) -> None:
        if item["object_id"] not in selected_ids:
            selected.append(item)
            selected_ids.add(item["object_id"])

    for item in candidates:
        if item["ocr"] or item["partial"] or item["current_quality_state"] != "accepted":
            select(item)
    dimensions = (
        ("era", lambda item: [item["era"]]),
        ("source_type", lambda item: [item["source_type"]]),
        ("viewpoint", lambda item: item["viewpoint_tags"]),
        ("segmentation_provenance", lambda item: [item["segmentation_provenance"]]),
    )
    for _name, values in dimensions:
        seen: set[str] = set()
        for item in candidates:
            for value in values(item):
                if value not in seen:
                    select(item)
                    seen.add(value)
    unit_type_order = sorted(candidates, key=lambda item: (item["unit_type"], item["object_id"]))
    if unit_type_order:
        for index in range(20):
            position = round(index * (len(unit_type_order) - 1) / 19)
            select(unit_type_order[position])
    for item in sorted(candidates, key=lambda value: value["object_id"]):
        if len(selected) >= 64:
            break
        select(item)
    selected = selected[: max(56, min(len(selected), 64))]

    syntheses = []
    for record in objects:
        if record["object_role"] != "synthesis":
            continue
        syntheses.append(
            {
                "object_id": record["object_id"],
                "current_quality_state": record["quality_state"],
                "source_ids": record["source_ids"],
                "source_unit_ids": record["source_unit_ids"],
                "content": record["content"],
                "limits": record["corpus_local_audit"]["limits"],
            }
        )
    blind_interpretations = [
        {key: value for key, value in item.items() if key != "current_quality_state"}
        for item in selected
    ]
    blind_syntheses = [
        {key: value for key, value in item.items() if key != "current_quality_state"}
        for item in syntheses
    ]
    write_json(
        AUDIT_ROOT / "assignment.json",
        {
            "selection_method": (
                "deterministic coverage-first sample: all OCR, partial, and non-accepted interpretations; "
                "then unseen era/source-type/viewpoint/segmentation strata; 20 evenly spaced unit-type "
                "strata; then stable-id fill"
            ),
            "interpretation_population": len(interpretations),
            "interpretation_sample_count": len(selected),
            "synthesis_population_and_sample_count": len(syntheses),
            "label_blinding": (
                "current quality and eligibility states are withheld from the auditor; "
                "comparison occurs only after review output is frozen"
            ),
            "interpretations": blind_interpretations,
            "syntheses": blind_syntheses,
        },
    )
    print(f"prepared independent audit: {len(selected)} interpretations and {len(syntheses)} syntheses")


def validate_audit() -> list[str]:
    errors: list[str] = []
    assignment = load_json(AUDIT_ROOT / "assignment.json")
    expected = [item["object_id"] for item in assignment["interpretations"] + assignment["syntheses"]]
    records = load_jsonl(AUDIT_ROOT / "independent_review.jsonl")
    if [record.get("object_id") for record in records] != expected:
        errors.append("independent audit order/coverage mismatch")
        return errors
    required = {
        "object_id",
        "decision",
        "faithfulness",
        "nonparaphrase",
        "specificity",
        "representation_sensitivity",
        "uncertainty_discipline",
        "context_quality",
        "style_risk",
        "reason",
    }
    objects = {record["object_id"]: record for record in load_jsonl(OBJECTS_PATH)}
    for record in records:
        object_id = record.get("object_id")
        if set(record) != required or record.get("decision") not in {"accept", "reject", "quarantine"}:
            errors.append(f"{object_id}: independent audit fields/decision mismatch")
            continue
        current = objects[object_id]
        if current["quality_state"] == "accepted" and record["decision"] != "accept":
            errors.append(f"{object_id}: independent audit rejects an eligible object")
        if current["quality_state"] in {"rejected", "quarantined"} and record["decision"] == "accept":
            errors.append(f"{object_id}: independent audit disagrees with retained negative state")
    return errors


def freeze_release(final_decision: str) -> None:
    allowed = {
        "RIEMANN_MATHIA_CORPUS_READY",
        "REVISE_EXTRACTION_AT_SCALE",
        "SOURCE_QUALITY_BLOCKER",
        "CORPUS_COVERAGE_BLOCKER",
    }
    if final_decision not in allowed:
        raise ValueError("invalid final issue #42 corpus decision")
    paths = [
        SOURCE_INSPECTION_PATH,
        UNITS_PATH,
        *PASS_FILES.values(),
        SYNTHESIS_ROOT / "final.jsonl",
        AUDIT_ROOT / "independent_review.jsonl",
        AUDIT_RECONCILIATION_PATH,
        OBJECTS_PATH,
        TRAINABLE_MANIFEST_PATH,
        MIXED_MANIFEST_PATH,
    ]
    identity = {
        "contract_version": interchange.CONTRACT_VERSION,
        "corpus_release_id": RELEASE_ID,
        "final_decision": final_decision,
        "files": [
            {
                "path": path.relative_to(FULL_ROOT).as_posix(),
                "sha256": pipeline.sha256_file(path),
                "bytes": path.stat().st_size,
            }
            for path in paths
        ],
    }
    write_json(
        FREEZE_PATH,
        {
            **identity,
            "freeze_id": "riemann_mathia_full_" + sha256_text(canonical_json(identity)),
            "frozen_at": utc_now(),
        },
    )
    print(load_json(FREEZE_PATH)["freeze_id"])


def write_report() -> None:
    freeze = load_json(FREEZE_PATH)
    inspections = load_jsonl(SOURCE_INSPECTION_PATH)
    units = load_jsonl(UNITS_PATH)
    revised = [record["output"] | {"unit_id": record["unit_id"]} for record in load_jsonl(PASS_FILES["revised"])]
    syntheses = load_jsonl(SYNTHESIS_ROOT / "final.jsonl")
    audit = load_jsonl(AUDIT_ROOT / "independent_review.jsonl")
    reconciliations = load_jsonl(AUDIT_RECONCILIATION_PATH)
    objects = load_jsonl(OBJECTS_PATH)
    usable_ids = {
        item["source_id"] for item in inspections if item["inspection_decision"] in {"usable", "usable_with_limits"}
    }
    accepted_unit_ids = {
        record["unit_id"] for record in revised if record["decision"] == "accepted"
    }
    unit_by_id = {unit["unit_id"]: unit for unit in units}
    accepted_source_ids = {unit_by_id[unit_id]["source_id"] for unit_id in accepted_unit_ids}
    source_by_id = {item["source_id"]: item for item in inspections}
    interpretation_counts = Counter(record["decision"] for record in revised)
    synthesis_counts = Counter(record["decision"] for record in syntheses)
    audit_counts = Counter(record["decision"] for record in audit)
    speculation_counts = Counter(record["speculation_status"] for record in revised)
    expansion_records = [
        record
        for path in sorted(SEGMENT_EXPANSION_PLAN_ROOT.glob("batch_*.jsonl"))
        for record in load_jsonl(path)
    ]
    expansion_decisions = Counter(record["expansion_decision"] for record in expansion_records)
    expansion_unit_distribution = Counter(len(record["additional_units"]) for record in expansion_records)
    coverage_era = Counter(source_by_id[source_id]["era"] for source_id in accepted_source_ids)
    coverage_type = Counter(source_by_id[source_id]["source_type"] for source_id in accepted_source_ids)
    coverage_viewpoint = Counter(
        tag for source_id in accepted_source_ids for tag in source_by_id[source_id]["viewpoint_tags"]
    )
    hashes = {
        "objects.jsonl": pipeline.sha256_file(OBJECTS_PATH),
        "trainable_manifest.json": pipeline.sha256_file(TRAINABLE_MANIFEST_PATH),
        "mixed_manifest.json": pipeline.sha256_file(MIXED_MANIFEST_PATH),
    }
    negative_examples = [record for record in revised if record["decision"] != "accepted"][:3]
    accepted_examples = [record for record in revised if record["decision"] == "accepted"][:3]
    report_lines = [
        "# Full Riemann–Mathia corpus report",
        "",
        "## Outcome",
        "",
        f"Final issue #42 corpus decision: `{freeze['final_decision']}`.",
        "",
        "This is a corpus-generation result only. It does not authorize training, choose a mixing ratio, run Qwen or qwen-lean, use the GPU, perform RL, merge weights, or bypass #32.",
        "",
        "## Inputs and source usability",
        "",
        f"The audited ledger contains 393 relevant bibliographic rows. Of those, 94 had full, OCR, preview, or partial-web normalized responses in the source-of-truth acquisition statuses. Per-source inspection classified {len(usable_ids)} as usable for mathematical interpretation and {sum(item['inspection_decision']=='excluded' for item in inspections)} as excluded.",
        "",
        "The usable set is 79 ordinary normalized sources, six OCR sources usable only through checked prose-rich spans, and one coherent three-page book preview usable only within the retained pages. All eight partial web captures were excluded because manual inspection found publisher/repository landing pages, access challenges, or abstract-only metadata rather than coherent mathematical source text. The 18 sub-1KB non-fulltext responses are acquisition failures and were never counted among the 94 candidate inputs.",
        "",
        "## Semantic units and interpretations",
        "",
        f"The release contains {len(units)} accepted exact source units across all {len(usable_ids)} usable sources: 24 calibrated pilot spans (including the three versioned v1 repairs), 74 first coverage-pass spans, and {max(0, len(units)-98)} units from a separate non-quota whole-source expansion. Source text remains a separate trainable object.",
        "",
        f"The non-quota expansion decisions were {dict(sorted(expansion_decisions.items()))}; additional-unit counts per non-pilot source were {dict(sorted(expansion_unit_distribution.items()))}. This variable distribution replaces the initial one-unit coverage artifact and avoids treating papers as equally rich.",
        "",
        f"Multi-pass interpretation decisions: {dict(sorted(interpretation_counts.items()))}. Accepted interpretations cover {len(accepted_source_ids)} of {len(usable_ids)} usable sources. Source units remain eligible even when their derived interpretation is quarantined or rejected.",
        "",
        f"Speculation handling across revised records: {dict(sorted(speculation_counts.items()))}. This count includes explicit marking and downgrades; it is not a truth score.",
        "",
        "## Coverage",
        "",
        f"Accepted-interpretation source coverage by era: `{dict(sorted(coverage_era.items()))}`.",
        "",
        f"Accepted-interpretation source coverage by source type: `{dict(sorted(coverage_type.items()))}`.",
        "",
        f"Accepted-interpretation source coverage by broad discovery viewpoint: `{dict(sorted(coverage_viewpoint.items()))}`. These tags are audit strata, not a Mathia ontology.",
        "",
        "## Cross-source synthesis",
        "",
        f"Twenty source-linked synthesis candidates (twelve initial and eight non-quota-expansion candidates) received separate fresh criticism and revision. Final decisions: {dict(sorted(synthesis_counts.items()))}. Every accepted synthesis resolves at least two distinct source parents and retains limits/mismatches in model-visible content.",
        "",
        "## Layered quality control",
        "",
        "All records receive deterministic hash/span/parent/rendering/exclusion validation. Every interpretation received a source-linked fresh adversarial critique. The pilot's nine RH and six transfer behavioral tasks remain frozen as evaluation-only QA seeds; they are not trainable objects and no artificial task-count target was pursued.",
        "",
        f"The fresh independent stratified audit reviewed {len(audit)} objects, including all OCR/partial/non-accepted interpretation strata, era/source-type/viewpoint/unit-type coverage, and every synthesis. Decisions: {dict(sorted(audit_counts.items()))}. The sample is an audit estimate, not independent mathematical proof.",
        "",
        f"Current release labels were withheld from that auditor. Its frozen output produced {len(reconciliations)} synthesis-label disagreements; both are preserved in `audit/synthesis_reconciliation.jsonl` and applied to the final eligibility state rather than overwritten or forced into agreement.",
        "",
        f"Source-faithful final interpretation acceptance rate: {interpretation_counts.get('accepted',0)}/{len(revised)} ({interpretation_counts.get('accepted',0)/max(1,len(revised)):.1%}). Paraphrase/style rejection is represented by {interpretation_counts.get('rejected',0)} final rejections; context/OCR insufficiency by {interpretation_counts.get('quarantined',0)} quarantines. Speculation/generalization was downgraded or explicitly marked in {speculation_counts.get('downgraded',0)+speculation_counts.get('explicitly_marked',0)} records.",
        "",
        "Recurring critic failures were metaphorical explanation replacing mechanism, imported theorem context, exact claims reconstructed from OCR, and physical/proposed-RH reformulations presented too literally. The revision pass applied these at batch scale; the independent audit is a separate check for remaining systematic defects.",
        "",
        "## Representative evidence",
        "",
        "Strong accepted examples:",
        "",
    ]
    report_lines.extend(
        f"- `{record['unit_id']}` — {record['quality_reason']}" for record in accepted_examples
    )
    report_lines.extend(("", "Rejected or quarantined examples:", ""))
    if negative_examples:
        report_lines.extend(
            f"- `{record['unit_id']}` ({record['decision']}) — {record['quality_reason']}"
            for record in negative_examples
        )
    else:
        report_lines.append("- None; the fresh audit should be consulted for residual uncertainty.")
    report_lines.extend(
        (
            "",
            "Uncertain material is retained through `context_limit`, OCR/partial flags, critic outputs, and non-accepted objects rather than repaired from memory. The six OCR sources never certify damaged exact formulas unless the readable unit supports them.",
            "",
            "## Shared interchange and release integrity",
            "",
            f"The release uses `{interchange.CONTRACT_VERSION}` with a single deterministic renderer shared with the representative #44 agnostic fixture. Eligible source, interpretation, and synthesis roles render without exposing corpus origin, release, quality state, teacher identity, or acceptance metadata. The synthetic mixed manifest materializes records from both releases with no corpus-specific conversion and detects hash/canonical-lineage duplicates.",
            "",
            f"Freeze: `{freeze['freeze_id']}`.",
            "",
            f"Core release hashes: `{hashes}`.",
            "",
            f"Trainable object counts: `{load_json(TRAINABLE_MANIFEST_PATH)['object_counts']}`. QA tasks, raw passes, critiques, rejection records, and audits are not automatically trainable.",
            "",
            "## Storage, licensing, and limitations",
            "",
            "Raw sources, normalized full text, and semantic source-unit text remain under the external local artifact store. Git retains provenance, hashes, small derived teacher outputs, audit evidence, and manifests. Freely accessible text with no redistribution grant is not committed. Each source object records the reported license boundary and an external content reference.",
            "",
            "Teacher prose is distillation, not independent mathematical validation. Famous-source familiarity remains a confound. Some acquired sources contain speculative, physical, or purported-proof programs; accepted interpretations must preserve that epistemic status. The inventory is broad but not literally complete: paywalled/inaccessible works, non-digitized historical material, non-English tails, repository omissions, and the stopped citation frontier remain gaps.",
            "",
            "The release is ready as one native side of a later compatibility-preserving training mix. That later design is a separate issue and remains gated by the repository's training/compute discipline.",
        )
    )
    (FULL_ROOT / "REPORT.md").write_text("\n".join(report_lines) + "\n", encoding="utf-8")
    print("full corpus report written")


def write_release_manifest() -> None:
    entries = []
    for path in sorted(FULL_ROOT.rglob("*")):
        if not path.is_file() or path == RELEASE_MANIFEST_PATH:
            continue
        entry = {
            "path": path.relative_to(FULL_ROOT).as_posix(),
            "sha256": pipeline.sha256_file(path),
            "bytes": path.stat().st_size,
        }
        if path.suffix == ".jsonl":
            entry["record_count"] = len(load_jsonl(path))
        entries.append(entry)
    identity = {"freeze_id": load_json(FREEZE_PATH)["freeze_id"], "files": entries}
    write_json(
        RELEASE_MANIFEST_PATH,
        {
            **identity,
            "manifest_id": "riemann_mathia_manifest_" + sha256_text(canonical_json(identity)),
            "generated_at": utc_now(),
        },
    )
    print(load_json(RELEASE_MANIFEST_PATH)["manifest_id"])


def validate_freeze_and_manifest() -> list[str]:
    errors: list[str] = []
    freeze = load_json(FREEZE_PATH)
    identity = {key: freeze[key] for key in ("contract_version", "corpus_release_id", "final_decision", "files")}
    if freeze.get("freeze_id") != "riemann_mathia_full_" + sha256_text(canonical_json(identity)):
        errors.append("full-corpus freeze id mismatch")
    for entry in freeze.get("files") or []:
        path = FULL_ROOT / entry["path"]
        if not path.is_file() or pipeline.sha256_file(path) != entry["sha256"] or path.stat().st_size != entry["bytes"]:
            errors.append(f"full-corpus freeze drift: {entry['path']}")
    manifest = load_json(RELEASE_MANIFEST_PATH)
    entries = manifest.get("files") or []
    current = [
        path.relative_to(FULL_ROOT).as_posix()
        for path in sorted(FULL_ROOT.rglob("*"))
        if path.is_file() and path != RELEASE_MANIFEST_PATH
    ]
    if [entry.get("path") for entry in entries] != current:
        errors.append("release manifest file set/order mismatch")
    for entry in entries:
        path = FULL_ROOT / str(entry.get("path"))
        if not path.is_file() or pipeline.sha256_file(path) != entry.get("sha256") or path.stat().st_size != entry.get("bytes"):
            errors.append(f"release manifest drift: {entry.get('path')}")
    manifest_identity = {"freeze_id": manifest.get("freeze_id"), "files": entries}
    if manifest.get("manifest_id") != "riemann_mathia_manifest_" + sha256_text(canonical_json(manifest_identity)):
        errors.append("release manifest id mismatch")
    report = (FULL_ROOT / "REPORT.md").read_text(encoding="utf-8")
    allowed = {
        "RIEMANN_MATHIA_CORPUS_READY",
        "REVISE_EXTRACTION_AT_SCALE",
        "SOURCE_QUALITY_BLOCKER",
        "CORPUS_COVERAGE_BLOCKER",
    }
    mentioned = {decision for decision in allowed if decision in report}
    if mentioned != {freeze.get("final_decision")}:
        errors.append("final report must contain exactly the frozen issue #42 decision")
    return errors


def validate_units(artifact_root: Path, require_artifacts: bool) -> list[str]:
    errors: list[str] = []
    inspections = load_jsonl(SOURCE_INSPECTION_PATH)
    input_ids = [item["source_id"] for item in inspections]
    if len(inspections) != 94 or len(input_ids) != len(set(input_ids)):
        errors.append("source inspection must cover exactly 94 unique normalized relevant inputs")
    counts = Counter(item.get("inspection_decision") for item in inspections)
    if counts != Counter({"usable": 79, "usable_with_limits": 7, "excluded": 8}):
        errors.append(f"unexpected source inspection decisions: {dict(counts)}")
    units = load_jsonl(UNITS_PATH)
    unit_ids = [unit.get("unit_id") for unit in units]
    if len(unit_ids) != len(set(unit_ids)):
        errors.append("unit ids are not unique")
    usable_ids = {
        item["source_id"]
        for item in inspections
        if item["inspection_decision"] in {"usable", "usable_with_limits"}
    }
    represented = {unit.get("source_id") for unit in units}
    if represented != usable_ids:
        errors.append(
            f"accepted unit coverage does not equal usable source set: missing={sorted(usable_ids - represented)}"
        )
    if len(units) < 98:
        errors.append(f"expected at least the 98 coverage-pass units, found {len(units)}")
    expansion_records = [
        record
        for path in sorted(SEGMENT_EXPANSION_PLAN_ROOT.glob("batch_*.jsonl"))
        for record in load_jsonl(path)
    ]
    expected_nonpilot = usable_ids - _pilot_source_ids()
    if expansion_records:
        expansion_ids = [record.get("source_id") for record in expansion_records]
        if len(expansion_ids) != len(set(expansion_ids)) or set(expansion_ids) != expected_nonpilot:
            errors.append("segmentation expansion source coverage set mismatch")
        expected_unit_count = 98
        for record in expansion_records:
            additional = record.get("additional_units")
            decision = record.get("expansion_decision")
            if not isinstance(additional, list) or len(additional) > 4:
                errors.append(f"{record.get('source_id')}: invalid expansion unit list")
                continue
            if decision not in {"expanded", "no_additional_unit", "quarantined"}:
                errors.append(f"{record.get('source_id')}: invalid expansion decision")
            if (decision == "expanded") != bool(additional):
                errors.append(f"{record.get('source_id')}: expansion decision/count mismatch")
            expected_unit_count += len(additional)
        if len(units) != expected_unit_count:
            errors.append(
                "semantic unit count does not match coverage plus expansion: "
                f"expected={expected_unit_count}, found={len(units)}"
            )
    nonpilot_counts = Counter(
        unit["source_id"] for unit in units if unit["source_id"] not in _pilot_source_ids()
    )
    if units and len(set(nonpilot_counts.values())) < 2:
        errors.append("non-pilot semantic-unit counts remain artificially uniform")
    inventory = {record["source_id"]: record for record in pipeline.load_jsonl(pipeline.INVENTORY_PATH)}
    for unit in units:
        source = inventory.get(unit.get("source_id"))
        if source is None or unit.get("source_normalized_sha256") != source.get("normalized_sha256"):
            errors.append(f"{unit.get('unit_id')}: source hash lineage mismatch")
        if require_artifacts:
            path = artifact_root / str(unit.get("unit_artifact_relpath"))
            if not path.is_file():
                errors.append(f"{unit.get('unit_id')}: unit artifact missing")
            elif pipeline.sha256_file(path) != unit.get("unit_sha256"):
                errors.append(f"{unit.get('unit_id')}: unit hash mismatch")
            elif path.stat().st_size != unit.get("unit_bytes"):
                errors.append(f"{unit.get('unit_id')}: unit byte count mismatch")
            if source and unit.get("line_start") and unit.get("line_end"):
                source_path = artifact_root / str(source["normalized_relpath"])
                lines = source_path.read_text(encoding="utf-8").splitlines(keepends=True)
                content = "".join(lines[int(unit["line_start"]) - 1 : int(unit["line_end"])])
                if not content.endswith("\n"):
                    content += "\n"
                if path.is_file() and path.read_text(encoding="utf-8") != content:
                    errors.append(f"{unit.get('unit_id')}: exact source line slice mismatch")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--artifact-root", type=Path, default=DEFAULT_ARTIFACT_ROOT)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("inspect")
    segment = subparsers.add_parser("prepare-segmentation")
    segment.add_argument("--batches", type=int, default=4)
    subparsers.add_parser("materialize-units")
    segment_expansion = subparsers.add_parser("prepare-segmentation-expansion")
    segment_expansion.add_argument("--batches", type=int, default=4)
    analysis = subparsers.add_parser("prepare-analysis")
    analysis.add_argument("--batches", type=int, default=4)
    supplemental_analysis = subparsers.add_parser("prepare-supplemental-analysis")
    supplemental_analysis.add_argument("--batches", type=int, default=4)
    subparsers.add_parser("combine-analysis")
    subparsers.add_parser("validate-analysis")
    subparsers.add_parser("build-objects")
    validate_objects_parser = subparsers.add_parser("validate-objects")
    validate_objects_parser.add_argument("--require-artifacts", action="store_true")
    subparsers.add_parser("prepare-synthesis")
    subparsers.add_parser("prepare-synthesis-expansion")
    subparsers.add_parser("combine-synthesis")
    subparsers.add_parser("validate-synthesis")
    subparsers.add_parser("prepare-audit")
    subparsers.add_parser("validate-audit")
    freeze_parser = subparsers.add_parser("freeze-release")
    freeze_parser.add_argument("decision")
    subparsers.add_parser("write-report")
    subparsers.add_parser("release-manifest")
    subparsers.add_parser("validate-release")
    validate = subparsers.add_parser("validate-units")
    validate.add_argument("--require-artifacts", action="store_true")
    args = parser.parse_args(argv)
    if args.command == "inspect":
        inspect_sources(args.artifact_root)
    elif args.command == "prepare-segmentation":
        prepare_segmentation_assignments(args.batches)
    elif args.command == "materialize-units":
        materialize_units(args.artifact_root)
    elif args.command == "prepare-segmentation-expansion":
        prepare_segmentation_expansion_assignments(args.batches)
    elif args.command == "prepare-analysis":
        prepare_analysis_assignments(args.batches)
    elif args.command == "prepare-supplemental-analysis":
        prepare_supplemental_analysis_assignments(args.batches)
    elif args.command == "combine-analysis":
        combine_analysis_batches()
    elif args.command == "validate-analysis":
        errors = validate_analysis()
        if errors:
            print("\n".join(f"ERROR: {error}" for error in errors))
            return 1
        print("full-corpus analysis validation passed")
    elif args.command == "build-objects":
        build_objects(args.artifact_root)
    elif args.command == "validate-objects":
        errors = validate_objects(args.artifact_root, args.require_artifacts)
        if errors:
            print("\n".join(f"ERROR: {error}" for error in errors))
            return 1
        print("full-corpus interchange validation passed")
    elif args.command == "prepare-synthesis":
        prepare_synthesis_assignment()
    elif args.command == "prepare-synthesis-expansion":
        prepare_synthesis_expansion_assignment()
    elif args.command == "combine-synthesis":
        combine_synthesis()
    elif args.command == "validate-synthesis":
        errors = validate_synthesis()
        if errors:
            print("\n".join(f"ERROR: {error}" for error in errors))
            return 1
        print("full-corpus synthesis validation passed")
    elif args.command == "prepare-audit":
        prepare_audit_assignment()
    elif args.command == "validate-audit":
        errors = validate_audit()
        if errors:
            print("\n".join(f"ERROR: {error}" for error in errors))
            return 1
        print("full-corpus independent audit validation passed")
    elif args.command == "freeze-release":
        freeze_release(args.decision)
    elif args.command == "write-report":
        write_report()
    elif args.command == "release-manifest":
        write_release_manifest()
    elif args.command == "validate-release":
        errors = (
            validate_objects(args.artifact_root, True)
            + validate_synthesis()
            + validate_audit()
            + validate_freeze_and_manifest()
        )
        if errors:
            print("\n".join(f"ERROR: {error}" for error in errors))
            return 1
        print("full Riemann-Mathia release validation passed")
    elif args.command == "validate-units":
        errors = validate_units(args.artifact_root, args.require_artifacts)
        if errors:
            print("\n".join(f"ERROR: {error}" for error in errors))
            return 1
        print("full-corpus unit validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
