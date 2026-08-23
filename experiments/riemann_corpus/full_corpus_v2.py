"""Riemann -> Mathia corpus v2 continuation for issue #42.

V2 is an additive release.  The merged ``full_corpus_v1`` tree is treated as an
immutable parent, while this module records renewed full-text searches,
alternate-version provenance, quota-free source-depth work, and the eventual
canonical-interchange release under ``full_corpus_v2``.

The acquisition ledger is intentionally experiment-local.  It is not a second
Mathia interchange schema.  Raw and normalized source text remain in the
external artifact store unless a source's redistribution terms explicitly
permit committing it.
"""

from __future__ import annotations

import argparse
import email.utils
import hashlib
import json
import re
import shutil
import socket
import ssl
import subprocess
import tempfile
import time
import urllib.error
import urllib.parse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from experiments import execution_provenance
from experiments.mathia_corpus import interchange
from experiments.riemann_corpus import pipeline


HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[1]
V1_ROOT = HERE / "full_corpus_v1"
V2_ROOT = HERE / "full_corpus_v2"
AGNOSTIC_V1_ROOT = HERE.parent / "agnostic_mathia_corpus" / "release_v1"
AGNOSTIC_SUPPLEMENT_ROOT = (
    HERE.parent / "agnostic_mathia_corpus" / "openalex_supplement_v1"
)
AGNOSTIC_SUPPLEMENT_PARENT_PATH = AGNOSTIC_SUPPLEMENT_ROOT / "parent.json"
DEFAULT_ARTIFACT_ROOT = Path("/workspace/mathia-artifacts/riemann-corpus-v2")
DEFAULT_OPENALEX_HANDOFF_ROOT = Path("/mnt/openalex/openalex/handoffs")
DEFAULT_AGNOSTIC_SUPPLEMENT_ARTIFACT_ROOT = Path(
    "/workspace/mathia-artifacts/agnostic-mathia-openalex-supplement-v1"
)
PARENT_PATH = V2_ROOT / "parent.json"
ACQUISITION_SEARCH_PATH = V2_ROOT / "acquisition_search.jsonl"
ACQUISITION_SUMMARY_PATH = V2_ROOT / "acquisition_summary.json"
SATURATION_LOG_PATH = V2_ROOT / "saturation_log.jsonl"
ACQUISITION_FRONTIER_PATH = V2_ROOT / "acquisition_frontier.json"
ACQUISITION_RETRY_STATE_PATH = V2_ROOT / "acquisition_retry_state.json"
V2_CURATED_PATH = HERE / "curated_sources_v2.json"
V2_ACQUISITION_QUARANTINE_PATH = HERE / "acquisition_quarantine_v2.json"
DEPTH_ROOT = V2_ROOT / "depth"
DEPTH_INVENTORY_PATH = DEPTH_ROOT / "source_inventory.jsonl"
DEPTH_ASSIGNMENT_ROOT = DEPTH_ROOT / "assignments"
DEPTH_PLAN_ROOT = DEPTH_ROOT / "plans"
DEPTH_REPAIR_ASSIGNMENT_ROOT = DEPTH_ROOT / "repair_assignments"
DEPTH_REPAIR_PLAN_ROOT = DEPTH_ROOT / "repair_plans"
DEPTH_UNITS_PATH = DEPTH_ROOT / "units.jsonl"
DEPTH_SYNTHESIS_REJECTIONS_PATH = DEPTH_ROOT / "synthesis_candidate_rejections.jsonl"
DEPTH_GENERATION_PROVENANCE_PATH = DEPTH_ROOT / "generation_provenance.jsonl"
DEPTH_IDENTITY_QUARANTINE_PATH = DEPTH_ROOT / "identity_quarantine.jsonl"
ANALYSIS_ROOT = V2_ROOT / "analyses"
ANALYSIS_ASSIGNMENT_ROOT = ANALYSIS_ROOT / "assignments"
ANALYSIS_BATCH_ROOT = ANALYSIS_ROOT / "batches"
ANALYSIS_CONTEXT_OVERRIDES_PATH = ANALYSIS_ROOT / "execution_context_overrides.json"
ANALYSIS_GENERATION_PROVENANCE_PATH = ANALYSIS_ROOT / "generation_provenance.jsonl"
ANALYSIS_IDENTITY_QUARANTINE_PATH = ANALYSIS_ROOT / "identity_quarantine.jsonl"
ANALYSIS_CONTEXT_QUARANTINE_PATH = ANALYSIS_ROOT / "context_quarantine.jsonl"
ANALYSIS_CONTEXT_QUARANTINE_ROOT = ANALYSIS_ROOT / "context_quarantine"
ANALYSIS_DETERMINISTIC_PASS4_PATH = ANALYSIS_ROOT / "pass4_deterministic.jsonl"
EXECUTION_ROOT = V2_ROOT / "execution"
SOURCE_DOSSIERS_PATH = EXECUTION_ROOT / "source_dossiers.jsonl"
EXECUTION_BRIEF_PATH = EXECUTION_ROOT / "RUN_BRIEF.md"
EFFICIENCY_METRICS_PATH = EXECUTION_ROOT / "efficiency_metrics.json"
EXECUTION_CONTEXT_MANIFEST_PATH = EXECUTION_ROOT / "manifest.json"
OPENALEX_HANDOFF_STATE_PATH = EXECUTION_ROOT / "openalex_handoff_cutoff.json"
AI_EXECUTION_LEDGER_PATH = EXECUTION_ROOT / "ai_execution_ledger.jsonl"
LEGACY_CONTEXT_LEDGER_PATH = EXECUTION_ROOT / "legacy_context_recovery.jsonl"
RIEMANN_HANDOFF_SOURCE_LEDGER_PATH = (
    EXECUTION_ROOT / "openalex_riemann_source_dispositions.jsonl"
)
AGNOSTIC_HANDOFF_SOURCE_LEDGER_PATH = (
    AGNOSTIC_SUPPLEMENT_ROOT / "source_dispositions.jsonl"
)
SYNTHESIS_ROOT = V2_ROOT / "synthesis"
WITHIN_SYNTHESIS_ROOT = SYNTHESIS_ROOT / "within_source"
CROSS_SYNTHESIS_ROOT = SYNTHESIS_ROOT / "cross_source"
WITHIN_SYNTHESIS_CANDIDATES_PATH = WITHIN_SYNTHESIS_ROOT / "candidates.jsonl"
WITHIN_SYNTHESIS_ASSIGNMENT_ROOT = WITHIN_SYNTHESIS_ROOT / "assignments"
WITHIN_SYNTHESIS_BATCH_ROOT = WITHIN_SYNTHESIS_ROOT / "batches"
WITHIN_SYNTHESIS_FINAL_PATH = WITHIN_SYNTHESIS_ROOT / "final.jsonl"
WITHIN_SYNTHESIS_DETERMINISTIC_PATH = WITHIN_SYNTHESIS_ROOT / "deterministic_rejections.jsonl"
CROSS_SYNTHESIS_CANDIDATES_PATH = CROSS_SYNTHESIS_ROOT / "candidates.jsonl"
CROSS_SYNTHESIS_FINAL_PATH = CROSS_SYNTHESIS_ROOT / "final.jsonl"
CROSS_GENERATION_ASSIGNMENT_ROOT = CROSS_SYNTHESIS_ROOT / "generation_assignments"
CROSS_GENERATION_BATCH_ROOT = CROSS_SYNTHESIS_ROOT / "generation_batches"
CROSS_ADJUDICATION_ASSIGNMENT_ROOT = CROSS_SYNTHESIS_ROOT / "adjudication_assignments"
CROSS_ADJUDICATION_BATCH_ROOT = CROSS_SYNTHESIS_ROOT / "adjudication_batches"
AUDIT_ROOT = V2_ROOT / "audit"
AUDIT_ASSIGNMENT_ROOT = AUDIT_ROOT / "assignments"
AUDIT_BATCH_ROOT = AUDIT_ROOT / "batches"
AUDIT_SAMPLE_PATH = AUDIT_ROOT / "sample.jsonl"
AUDIT_CARRIED_PATH = AUDIT_ROOT / "carried_pre_openalex.jsonl"
AUDIT_FINAL_PATH = AUDIT_ROOT / "independent_review.jsonl"
AUDIT_ISOLATION_QUARANTINE_PATH = AUDIT_ROOT / "isolation_quarantine.jsonl"
AUDIT_DECISION_EXECUTION_MAP_PATH = AUDIT_ROOT / "decision_execution_map.jsonl"
PRE_OPENALEX_AUDIT_ROOT = V2_ROOT / "audit_pre_openalex_handoffs"
PRE_OPENALEX_AUDIT_SAMPLE_PATH = PRE_OPENALEX_AUDIT_ROOT / "sample.jsonl"
PRE_OPENALEX_AUDIT_FINAL_PATH = PRE_OPENALEX_AUDIT_ROOT / "independent_review.jsonl"
OBJECTS_PATH = V2_ROOT / "objects.jsonl"
TRAINABLE_MANIFEST_PATH = V2_ROOT / "trainable_manifest.json"
MIXED_MANIFEST_PATH = V2_ROOT / "mixed_manifest.json"
FREEZE_PATH = V2_ROOT / "freeze.json"
RELEASE_MANIFEST_PATH = V2_ROOT / "release_manifest.json"
COMPATIBILITY_STATUS_PATH = V2_ROOT / "mixed_manifest_status.json"
ISOLATION_ARCHIVE_ROOT = V2_ROOT / "non_authoritative_source_isolation_run"
ISOLATION_ARCHIVE_MANIFEST_PATH = ISOLATION_ARCHIVE_ROOT / "manifest.jsonl"
ISOLATION_ARCHIVE_SUMMARY_PATH = ISOLATION_ARCHIVE_ROOT / "summary.json"
CORRECTIVE_ISOLATION_ARCHIVE_ROOT = (
    V2_ROOT / "non_authoritative_source_isolation_correction_v2"
)
SOURCE_ISOLATION_ARCHIVE_ROOTS = (
    ISOLATION_ARCHIVE_ROOT,
    CORRECTIVE_ISOLATION_ARCHIVE_ROOT,
)
PASS_FILES = {
    "spontaneous": ANALYSIS_ROOT / "pass1_spontaneous.jsonl",
    "directed": ANALYSIS_ROOT / "pass2_directed.jsonl",
    "critic": ANALYSIS_ROOT / "pass3_critic.jsonl",
    "revised": ANALYSIS_ROOT / "pass4_revised.jsonl",
}
ANALYSIS_PROMPTS = {
    "pass12": V2_ROOT / "prompts" / "pass12_generation.md",
    "pass3": V2_ROOT / "prompts" / "pass3_critic.md",
    "pass4": V2_ROOT / "prompts" / "pass4_revision.md",
}
DETERMINISTIC_PASS4_PROMPT = V2_ROOT / "prompts" / "pass4_deterministic_gate.md"
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
V1_RELEASE_ID = "riemann-mathia-full-v1"
V2_RELEASE_ID = "riemann-mathia-full-v2"
V1_FREEZE_ID = "riemann_mathia_full_e9f9f663e6f3a777ab7545f088f39d0662462f5da622364204e52be6fcf42cd6"
AGNOSTIC_V1_RELEASE_ID = "agnostic-mathia-full-v1"
AGNOSTIC_V1_FREEZE_ID = "freeze_eeeeb89af3d2ac75d1ff5dad5623b63d1d24dfbddb965beca2f1c4aac9f9867f"
AGNOSTIC_V1_REVIEW_CONTENT_FREEZE_ID = (
    "review_content_d1d1d7152fa2c2ddd3a4f6d26a4fa4b3f6d64129392b7c79ea72f125b5d95c0b"
)
AGNOSTIC_V1_MERGE_COMMIT = "f3df94498d83315f79fd6f98a5ec008db6f3ddab"
AGNOSTIC_SUPPLEMENT_RELEASE_ID = "agnostic-mathia-openalex-supplement-v1"
ISSUE42_CONCRETE_ARTIFACT_BINDING_COMMENT = (
    "https://github.com/murillo128/mathia/issues/42#issuecomment-5368950640"
)
AGNOSTIC_HANDOFF_V2_MANIFEST_SHA256 = (
    "56282413a704775ddaca0a62090dce03037c8ea55aa2d3be9ce98f542c468942"
)
AGNOSTIC_HANDOFF_V2_SOURCE_COUNT = 25
OPENALEX_HANDOFF_SPECS = {
    "riemann_fulltext_v1": {
        "stream": "riemann",
        "freeze_id": (
            "openalex_handoff_"
            "37e490bf05210c91ef3e9a721b3389373a4fac3182a06554ad9388f80b118b67"
        ),
        "authoritative": False,
        "superseded_by": "riemann_fulltext_v2",
    },
    "riemann_fulltext_v2": {
        "stream": "riemann",
        "freeze_id": (
            "openalex_handoff_"
            "89e50c9a268c116f9ca85d457e4cae8e3efa6f7feed64fbd1f815f0ded9d0dc6"
        ),
        "authoritative": True,
        "supersedes": "riemann_fulltext_v1",
    },
    "agnostic_mathia_fulltext_v1": {
        "stream": "agnostic_mathia",
        "freeze_id": (
            "openalex_handoff_"
            "3d4d9dbc4f55086f956e8c1f3deff54814ecbe3618a24b8b8aa5d2850ab23132"
        ),
        "authoritative": False,
        "superseded_by": "agnostic_mathia_fulltext_v2",
    },
    "agnostic_mathia_fulltext_v2": {
        "stream": "agnostic_mathia",
        "freeze_id": (
            "openalex_handoff_"
            "7a0112075a605e14f20e1de307e73799898ceadc6007837faeb83468bec5691c"
        ),
        "authoritative": True,
        "supersedes": "agnostic_mathia_fulltext_v1",
    },
}
AUTHORITATIVE_OPENALEX_HANDOFF_IDS = {
    str(spec["stream"]): handoff_id
    for handoff_id, spec in OPENALEX_HANDOFF_SPECS.items()
    if spec["authoritative"]
}
OPENALEX_HANDOFF_SUPERSESSION_REASON = (
    "Correct source-version and license provenance so both fields bind to the exact "
    "successful acquisition route."
)
AGNOSTIC_V1_BINDING_PATHS = (
    AGNOSTIC_V1_ROOT / "freeze.json",
    AGNOSTIC_V1_ROOT / "review_content_freeze.json",
    AGNOSTIC_V1_ROOT / "records.jsonl",
    AGNOSTIC_V1_ROOT / "trainable_manifest.json",
    AGNOSTIC_V1_ROOT / "rendered_trainable.jsonl",
    AGNOSTIC_V1_ROOT / "source_inventory.jsonl",
    AGNOSTIC_V1_ROOT / "coverage_map.json",
    AGNOSTIC_V1_ROOT / "coverage_audit.json",
    AGNOSTIC_V1_ROOT / "saturation_log.json",
    AGNOSTIC_V1_ROOT / "quality_reviews.jsonl",
    AGNOSTIC_V1_ROOT / "qa_sample.json",
    AGNOSTIC_V1_ROOT / "baseline_quality_audit.json",
    AGNOSTIC_V1_ROOT / "calibration_audit.json",
    AGNOSTIC_V1_ROOT / "sidecars.jsonl",
    AGNOSTIC_V1_ROOT / "synthetic_mixed_dry_run.json",
    AGNOSTIC_V1_ROOT.parent / "assets" / "fundamental_polygon.svg",
    AGNOSTIC_V1_ROOT.parent / "assets" / "subspace_intersection.svg",
    AGNOSTIC_V1_ROOT.parent / "assets" / "curvature_triangles.svg",
    AGNOSTIC_V1_ROOT.parent / "assets" / "convex_separation.svg",
)
AGNOSTIC_HANDOFF_V2_REPO_EVIDENCE_PATHS = (
    REPO_ROOT / "experiments/openalex_discovery/run_v1/agnostic_handoff_freeze.json",
    REPO_ROOT / "experiments/openalex_discovery/run_v1/agnostic_handoff_manifest.jsonl",
    REPO_ROOT / "experiments/openalex_discovery/run_v1/agnostic_graph_summary.json",
    REPO_ROOT
    / "experiments/openalex_discovery/run_v1/agnostic_discovery_only_unavailable.jsonl",
)
V1_USABLE_DECISIONS = {"usable", "usable_with_limits"}
SUCCESS_RESULTS = {"acquired-and-normalized"}
TEMPORARY_RESULTS = {
    "blocked-http-429",
    "blocked-http-500",
    "blocked-http-502",
    "blocked-http-503",
    "blocked-http-504",
    "blocked-tls-validation",
    "download-timeout",
    "download-failed",
}
TERMINAL_ROUTE_RESULTS = {
    "blocked-http-404",
    "blocked-by-access-policy",
    "blocked-by-robots-policy",
}
DEFAULT_MAX_ROUTE_ATTEMPTS = 5
SOURCE_CONTEXT_MAX_UNITS = 24
NEARBY_CONTEXT_LINES = 8
SYNTHESIS_CONTEXT_MAX_CANDIDATES = 8
ROUTE_ORDER = {
    "issue-46-immutable-offline-handoff": 5,
    "arxiv-preprint": 10,
    "author-hosted-manuscript": 20,
    "institutional-repository": 30,
    "public-fulltext-repository": 35,
    "lawful-mathematical-archive": 40,
    "open-publisher-copy": 50,
    "openalex-indexed-location": 60,
}
LONG_FORM_TYPES = {"book", "monograph", "reference-book", "book-chapter", "report"}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    return pipeline.sha256_file(path)


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return pipeline.load_jsonl(path)


def write_json(path: Path, value: Any) -> None:
    pipeline.write_json(path, value)


def write_jsonl(path: Path, values: Iterable[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(canonical_json(value) + "\n" for value in values), encoding="utf-8")


_PACKET_PATH_KEYS = {
    "artifact_abspath",
    "content_abspath",
    "execution_brief_path",
    "normalized_abspath",
    "output_path",
    "prior_output_paths",
    "prompt_path",
    "unit_artifact_abspath",
}


def _model_visible_packet(value: Any) -> Any:
    """Canonicalize semantic agent input while removing host/path plumbing."""
    if isinstance(value, Mapping):
        return {
            str(key): _model_visible_packet(item)
            for key, item in sorted(value.items())
            if key not in _PACKET_PATH_KEYS
            and key != "model_visible_packet_sha256"
        }
    if isinstance(value, list):
        return [_model_visible_packet(item) for item in value]
    return value


def model_visible_packet_sha256(assignment: Mapping[str, Any]) -> str:
    return sha256_text(canonical_json(_model_visible_packet(assignment)))


def _bind_model_visible_packet(assignment: Mapping[str, Any]) -> dict[str, Any]:
    bound = dict(assignment)
    bound["model_visible_packet_sha256"] = model_visible_packet_sha256(bound)
    return bound


def audit_sample_packet_sha256(item: Mapping[str, Any]) -> str:
    """Bind the complete canonical audit item, not only its stable object ID."""
    return sha256_text(canonical_json(dict(item)))


def _archive_manifest_rows(manifest_path: Path) -> list[dict[str, Any]]:
    return load_jsonl(manifest_path) if manifest_path.is_file() else []


def _is_source_isolation_archive_path(path: Path) -> bool:
    return any(
        root == path or root in path.parents
        for root in SOURCE_ISOLATION_ARCHIVE_ROOTS
    )


def _write_json_atomic(path: Path, value: Mapping[str, Any]) -> None:
    temporary_path = path.with_name(path.name + ".tmp")
    write_json(temporary_path, value)
    temporary_path.replace(path)


def _write_jsonl_atomic(path: Path, values: Iterable[Mapping[str, Any]]) -> None:
    temporary_path = path.with_name(path.name + ".tmp")
    write_jsonl(temporary_path, values)
    temporary_path.replace(path)


def _archive_file_for_isolation(
    release_root: Path,
    archive_root: Path,
    source_path: Path,
    *,
    pool: str,
    category: str,
    reason: str,
    reconciliation_eligible: bool = False,
) -> dict[str, Any]:
    """Hash-verify, copy, and deactivate one live file; safe to repeat."""
    release_root = release_root.resolve()
    archive_root = archive_root.resolve()
    source_path = source_path.resolve()
    if source_path == archive_root or source_path.is_relative_to(archive_root):
        raise ValueError("cannot archive the source-isolation archive into itself")
    try:
        relative = source_path.relative_to(release_root)
    except ValueError as error:
        raise ValueError(f"isolation archive source is outside release root: {source_path}") from error
    archive_path = archive_root / pool / "artifacts" / relative
    manifest_path = archive_root / "manifest.jsonl"
    rows = _archive_manifest_rows(manifest_path)
    prior = next(
        (
            row
            for row in rows
            if row.get("original_relpath") == relative.as_posix()
            and row.get("pool") == pool
        ),
        None,
    )
    if source_path.is_file():
        descriptor = {
            "sha256": sha256_file(source_path),
            "bytes": source_path.stat().st_size,
        }
        if prior is not None and (
            prior.get("sha256") != descriptor["sha256"]
            or prior.get("bytes") != descriptor["bytes"]
        ):
            raise ValueError(f"isolation archive manifest collision: {relative}")
        archive_path.parent.mkdir(parents=True, exist_ok=True)
        if archive_path.is_file() and (
            sha256_file(archive_path) != descriptor["sha256"]
            or archive_path.stat().st_size != descriptor["bytes"]
        ):
            raise ValueError(f"isolation archive file collision: {archive_path}")
        if not archive_path.is_file():
            temporary_path = archive_path.with_name(archive_path.name + ".tmp")
            shutil.copyfile(source_path, temporary_path)
            if (
                sha256_file(temporary_path) != descriptor["sha256"]
                or temporary_path.stat().st_size != descriptor["bytes"]
            ):
                raise ValueError(f"isolation archive verification failed: {relative}")
            temporary_path.replace(archive_path)
        if (
            sha256_file(archive_path) != descriptor["sha256"]
            or archive_path.stat().st_size != descriptor["bytes"]
        ):
            raise ValueError(f"isolation archive verification failed: {relative}")
        if prior is None:
            prior = {
                "archive_relpath": archive_path.relative_to(archive_root).as_posix(),
                "bytes": descriptor["bytes"],
                "category": category,
                "original_relpath": relative.as_posix(),
                "pool": pool,
                "reason": reason,
                "reconciliation_eligible": reconciliation_eligible,
                "replacement_required": True,
                "sha256": descriptor["sha256"],
                "authoritative": False,
                "trainable": False,
            }
            rows.append(prior)
            _write_jsonl_atomic(
                manifest_path,
                sorted(rows, key=lambda row: (row["pool"], row["original_relpath"])),
            )
        source_path.unlink()
    elif prior is None:
        raise ValueError(f"missing live file and isolation archive record: {relative}")
    if not archive_path.is_file() or (
        sha256_file(archive_path) != prior["sha256"]
        or archive_path.stat().st_size != prior["bytes"]
    ):
        raise ValueError(f"archived isolation evidence drift: {relative}")
    return prior


def validate_source_isolation_archive(
    release_root: Path = V2_ROOT,
    archive_root: Path = ISOLATION_ARCHIVE_ROOT,
) -> list[str]:
    errors: list[str] = []
    seen: set[tuple[str, str]] = set()
    for row in _archive_manifest_rows(archive_root / "manifest.jsonl"):
        key = (str(row.get("pool") or ""), str(row.get("original_relpath") or ""))
        if key in seen:
            errors.append(f"duplicate source-isolation manifest entry: {key}")
        seen.add(key)
        archive_path = archive_root / str(row.get("archive_relpath") or "")
        try:
            archive_path.resolve().relative_to(archive_root.resolve())
        except ValueError:
            errors.append(f"unsafe source-isolation archive path: {archive_path}")
            continue
        if (
            row.get("authoritative") is not False
            or row.get("trainable") is not False
            or not archive_path.is_file()
            or archive_path.stat().st_size != row.get("bytes")
            or sha256_file(archive_path) != row.get("sha256")
        ):
            errors.append(
                f"source-isolation archive drift: {row.get('original_relpath')}"
            )
        live_path = release_root / str(row.get("original_relpath") or "")
        if (
            not row.get("reconciliation_eligible")
            and live_path.is_file()
            and sha256_file(live_path) == row.get("sha256")
        ):
            errors.append(
                f"non-authoritative artifact remains live: {row.get('original_relpath')}"
            )
    return errors


def _assignment_source_ids(value: Any) -> set[str]:
    result: set[str] = set()
    if isinstance(value, Mapping):
        source_id = value.get("source_id")
        if isinstance(source_id, str) and source_id:
            result.add(source_id)
        for item in value.values():
            result.update(_assignment_source_ids(item))
    elif isinstance(value, list):
        for item in value:
            result.update(_assignment_source_ids(item))
    return result


def _execution_ledger_relpath(release_root: Path, path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except ValueError:
        return path.resolve().relative_to(release_root.resolve()).as_posix()


def validate_execution_receipts(
    contexts: Iterable[tuple[str, Mapping[str, Any], Mapping[str, Any]]],
    *,
    cross_source_stages: set[str] | None = None,
) -> list[str]:
    """Validate real context bindings; prose isolation claims are insufficient."""
    errors: list[str] = []
    cross_source_stages = cross_source_stages or set()
    path_owners: dict[str, str] = {}
    teacher_paths: set[str] = set()
    critic_paths: set[str] = set()
    for context_id, assignment, receipt in contexts:
        stage = str(receipt.get("stage") or assignment.get("stage") or "")
        source_ids = _assignment_source_ids(assignment.get("units") or assignment)
        if stage not in cross_source_stages and len(source_ids) != 1:
            errors.append(f"{context_id}: expected exactly one source, found {sorted(source_ids)}")
        if stage in cross_source_stages and len(source_ids) < 2:
            errors.append(f"{context_id}: explicit cross-source panel has fewer than two sources")
        packet_sha256 = model_visible_packet_sha256(assignment)
        if receipt.get("model_visible_packet_sha256") != packet_sha256:
            errors.append(f"{context_id}: execution packet fingerprint mismatch")
        task_path = receipt.get("agent_task_path")
        if not isinstance(task_path, str) or not task_path.startswith("/root/"):
            errors.append(f"{context_id}: exact agent task path is missing")
            continue
        prior_owner = path_owners.get(task_path)
        if prior_owner is not None and prior_owner != context_id:
            errors.append(
                f"{context_id}: agent task path reused from {prior_owner}: {task_path}"
            )
        path_owners[task_path] = context_id
        if stage in {"pass12", "generation"}:
            teacher_paths.add(task_path)
        if stage in {
            "pass3", "critic", "audit", "cross-source-audit", "independent-audit"
        }:
            critic_paths.add(task_path)
    for path in sorted(teacher_paths & critic_paths):
        errors.append(f"teacher/critic execution path collision: {path}")
    return errors


def validate_execution_ledger_receipts(
    release_root: Path = V2_ROOT,
    *,
    allow_fresh_pending: bool = False,
) -> list[str]:
    """Bind each live source-local assignment/output to exact recovered execution rows."""
    errors: list[str] = []
    ledger_paths = (
        release_root / "execution/legacy_context_recovery.jsonl",
        release_root / "execution/ai_execution_ledger.jsonl",
    )
    ledger_rows: list[dict[str, Any]] = []
    for ledger_path in ledger_paths:
        if not ledger_path.is_file():
            errors.append(f"required execution ledger is missing: {ledger_path.name}")
            continue
        rows = load_jsonl(ledger_path)
        try:
            execution_provenance.validate_execution_rows(rows)
        except ValueError as error:
            errors.append(str(error))
        ledger_rows.extend(rows)
    if errors:
        return errors
    assignment_paths = [
        *sorted((release_root / "depth/assignments").glob("*.json")),
        *sorted((release_root / "depth/repair_assignments").glob("*.json")),
        *sorted((release_root / "analyses/assignments").glob("*.json")),
        *sorted((release_root / "audit/assignments").glob("*.json")),
    ]
    contexts: list[tuple[str, Mapping[str, Any], Mapping[str, Any]]] = []
    for assignment_path in assignment_paths:
        assignment = load_json(assignment_path)
        relative = _execution_ledger_relpath(release_root, assignment_path)
        assignment_sha256 = sha256_file(assignment_path)
        output_value = assignment.get("output_path")
        output_path = Path(str(output_value or ""))
        if allow_fresh_pending and not output_path.is_file():
            bound_packet = assignment.get("model_visible_packet_sha256")
            completed_exact_receipt = any(
                row.get("assignment_relpath") == relative
                and row.get("assignment_sha256") == assignment_sha256
                and row.get("requires_rerun") is False
                and row.get("status") in {"authoritative", "historical-recovered"}
                for row in ledger_rows
            )
            source_ids = _assignment_source_ids(
                assignment.get("units") or assignment
            )
            try:
                output_path.resolve().relative_to(release_root.resolve())
                output_is_local = isinstance(output_value, str) and bool(output_value)
            except ValueError:
                output_is_local = False
            if (
                not completed_exact_receipt
                and bound_packet == model_visible_packet_sha256(assignment)
                and len(source_ids) == 1
                and output_is_local
            ):
                continue
            errors.append(
                f"{relative}: outputless assignment is not a bound source-local fresh packet"
            )
            continue
        matches = [
            row
            for row in ledger_rows
            if row.get("assignment_relpath") == relative
            and row.get("assignment_sha256") == assignment_sha256
            and row.get("requires_rerun") is False
            and row.get("status") in {"authoritative", "historical-recovered"}
        ]
        if len(matches) != 1:
            errors.append(
                f"{relative}: expected one authoritative exact execution-ledger receipt"
            )
            continue
        receipt = matches[0]
        if (
            not output_path.is_file()
            or receipt.get("output_sha256") != sha256_file(output_path)
            or receipt.get("output_records") != len(load_jsonl(output_path))
        ):
            errors.append(f"{relative}: execution-ledger output binding mismatch")
            continue
        bound_packet = assignment.get("model_visible_packet_sha256")
        if bound_packet is not None and bound_packet != model_visible_packet_sha256(
            assignment
        ):
            errors.append(f"{relative}: execution packet fingerprint mismatch")
            continue
        contexts.append(
            (
                relative,
                assignment,
                {
                    "stage": assignment.get("stage") or receipt.get("stage"),
                    "agent_task_path": receipt.get("agent_task_path"),
                    "model_visible_packet_sha256": model_visible_packet_sha256(assignment),
                },
            )
        )
    errors.extend(
        validate_execution_receipts(
            contexts, cross_source_stages={"cross-source-audit"}
        )
    )
    return errors


def reconcile_archived_assignment(
    assignment_path: Path,
    release_root: Path,
    archive_root: Path,
    receipt: Mapping[str, Any],
    *,
    allow_cross_source: bool = False,
) -> bool:
    """Restore an old output only for an identical packet and verified receipt."""
    relative = assignment_path.resolve().relative_to(release_root.resolve())
    archived_assignment = archive_root / "reconciliation" / "artifacts" / relative
    if not archived_assignment.is_file() or not assignment_path.is_file():
        return False
    old_assignment = load_json(archived_assignment)
    new_assignment = load_json(assignment_path)
    if model_visible_packet_sha256(old_assignment) != model_visible_packet_sha256(new_assignment):
        return False
    source_ids = _assignment_source_ids(new_assignment.get("units") or new_assignment)
    if (not allow_cross_source and len(source_ids) != 1) or (
        allow_cross_source and len(source_ids) < 2
    ):
        return False
    old_output = Path(str(old_assignment.get("output_path") or ""))
    try:
        old_output_relative = old_output.resolve().relative_to(release_root.resolve())
    except ValueError:
        return False
    archived_output = archive_root / "reconciliation" / "artifacts" / old_output_relative
    if not archived_output.is_file():
        return False
    if (
        receipt.get("assignment_sha256") != sha256_file(archived_assignment)
        or receipt.get("raw_output_sha256") != sha256_file(archived_output)
        or receipt.get("model_visible_packet_sha256")
        != model_visible_packet_sha256(old_assignment)
    ):
        return False
    receipt_errors = validate_execution_receipts(
        [(relative.as_posix(), old_assignment, receipt)],
        cross_source_stages={str(receipt.get("stage") or "")} if allow_cross_source else set(),
    )
    if receipt_errors:
        return False
    new_output = Path(str(new_assignment.get("output_path") or ""))
    new_output.parent.mkdir(parents=True, exist_ok=True)
    if new_output.is_file() and sha256_file(new_output) != sha256_file(archived_output):
        raise ValueError(f"stale output collision during reconciliation: {new_output}")
    if not new_output.is_file():
        shutil.copyfile(archived_output, new_output)
    return True


def _v1_relevant_records() -> list[dict[str, Any]]:
    return [
        record
        for record in load_jsonl(pipeline.INVENTORY_PATH)
        if record.get("scope_status") == "relevant"
    ]


def _v1_usable_source_ids() -> set[str]:
    return {
        record["source_id"]
        for record in load_jsonl(V1_ROOT / "source_inspection.jsonl")
        if record.get("inspection_decision") in V1_USABLE_DECISIONS
    }


def _file_descriptor(path: Path, relative_to: Path) -> dict[str, Any]:
    return {
        "path": path.relative_to(relative_to).as_posix(),
        "sha256": sha256_file(path),
        "bytes": path.stat().st_size,
    }


def initialize_lineage() -> None:
    """Bind v2 to the exact merged v1 release and seed one search row per source."""
    freeze = load_json(V1_ROOT / "freeze.json")
    if freeze.get("freeze_id") != V1_FREEZE_ID or freeze.get("corpus_release_id") != V1_RELEASE_ID:
        raise ValueError("the checked-out v1 parent does not match the issue #42 v2 baseline")
    relevant = _v1_relevant_records()
    usable_ids = _v1_usable_source_ids()
    parent = {
        "contract_version": interchange.CONTRACT_VERSION,
        "corpus_release_id": V2_RELEASE_ID,
        "parent_release_id": V1_RELEASE_ID,
        "parent_freeze_id": V1_FREEZE_ID,
        "lineage_policy": (
            "full_corpus_v1 is immutable; carried records retain their v1 content, hashes, "
            "quality labels, and stable object identities"
        ),
        "v1_counts": {
            "relevant_inventory_records": len(relevant),
            "usable_sources": len(usable_ids),
            "sources_needing_usable_full_text": len(relevant) - len(usable_ids),
            "semantic_units": len(load_jsonl(V1_ROOT / "units.jsonl")),
            "objects": len(load_jsonl(V1_ROOT / "objects.jsonl")),
        },
        "bindings": [
            _file_descriptor(pipeline.INVENTORY_PATH, HERE),
            _file_descriptor(V1_ROOT / "freeze.json", HERE),
            _file_descriptor(V1_ROOT / "objects.jsonl", HERE),
            _file_descriptor(V1_ROOT / "units.jsonl", HERE),
        ],
    }
    write_json(PARENT_PATH, parent)

    previous = {record["source_id"]: record for record in load_jsonl(ACQUISITION_SEARCH_PATH)}
    rows: list[dict[str, Any]] = []
    for record in relevant:
        source_id = record["source_id"]
        old = previous.get(source_id) or {}
        attempts = list(old.get("attempts") or [])
        for attempt in attempts:
            attempt.setdefault(
                "artifact_store",
                "riemann-corpus-v0"
                if str(attempt.get("round_id") or "").startswith("v1-")
                else "riemann-corpus-v2",
            )
        if not attempts and record.get("acquisition_status") not in {None, "not-attempted"}:
            attempts.append(_v1_attempt(record))
        selected_artifact = old.get("selected_artifact")
        if selected_artifact and "artifact_store" not in selected_artifact:
            selected_artifact["artifact_store"] = "riemann-corpus-v2"
        rows.append(
            {
                "source_id": source_id,
                "lineage": "v1-relevant",
                "title": record.get("title"),
                "authors": record.get("authors") or [],
                "year": record.get("year"),
                "source_type": record.get("source_type"),
                "identifiers": record.get("identifiers") or {},
                "canonical_url": record.get("canonical_url"),
                "viewpoint_tags": record.get("tags") or [],
                "v1_acquisition_status": record.get("acquisition_status"),
                "v1_usable": source_id in usable_ids,
                "v1_artifact_sha256": record.get("artifact_sha256"),
                "v1_normalized_sha256": record.get("normalized_sha256"),
                "search_priority": "carry-forward" if source_id in usable_ids else "recovery",
                "openalex_refresh_status": old.get("openalex_refresh_status", "not-yet-refreshed"),
                "openalex_refreshed_at": old.get("openalex_refreshed_at"),
                "candidates": list(old.get("candidates") or []),
                "attempts": attempts,
                "final_status": old.get("final_status") or (
                    "usable-carried-from-v1" if source_id in usable_ids else "recovery-search-pending"
                ),
                "selected_candidate_id": old.get("selected_candidate_id"),
                "selected_artifact": selected_artifact,
                "remaining_search_notes": old.get("remaining_search_notes") or [],
            }
        )
    relevant_ids = {record["source_id"] for record in relevant}
    rows.extend(row for source_id, row in previous.items() if source_id not in relevant_ids)
    write_jsonl(ACQUISITION_SEARCH_PATH, rows)
    print(
        f"initialized v2 lineage: {len(relevant)} relevant v1 records; "
        f"{len(usable_ids)} usable carry-forwards; {len(relevant) - len(usable_ids)} recovery targets"
    )


def _v1_attempt(record: Mapping[str, Any]) -> dict[str, Any]:
    url = record.get("acquisition_url")
    identity = {"source_id": record["source_id"], "round": "v1", "url": url}
    return {
        "attempt_id": "v2_attempt_" + sha256_text(canonical_json(identity)),
        "round_id": "v1-parent-preserved",
        "candidate_id": None,
        "route": "v1-canonical-or-discovered-location",
        "requested_url": url,
        "attempted_at": record.get("acquisition_attempted_at"),
        "result": record.get("acquisition_status"),
        "artifact_store": "riemann-corpus-v0",
        "effective_url": record.get("acquisition_final_url"),
        "media_type": record.get("media_type"),
        "artifact_relpath": (
            "riemann-corpus-v0/" + str(record["artifact_relpath"])
            if record.get("artifact_relpath")
            else None
        ),
        "artifact_sha256": record.get("artifact_sha256"),
        "normalized_relpath": (
            "riemann-corpus-v0/" + str(record["normalized_relpath"])
            if record.get("normalized_relpath")
            else None
        ),
        "normalized_sha256": record.get("normalized_sha256"),
        "normalized_bytes": record.get("normalized_bytes"),
        "normalized_page_count": record.get("normalized_page_count"),
        "warnings": record.get("acquisition_warnings") or [],
    }


def add_curated_v2_sources() -> None:
    """Add owner-authorized long-form/ecosystem discoveries to the v2 frontier."""
    rows = load_jsonl(ACQUISITION_SEARCH_PATH)
    by_id = {row["source_id"]: row for row in rows}
    added = augmented = 0
    for source in load_json(V2_CURATED_PATH):
        source_id = source["source_id"]
        row = by_id.get(source_id)
        if row is None:
            row = {
                "source_id": source_id,
                "lineage": "v2-promoted-or-new-discovery",
                "title": source["title"],
                "authors": source["authors"],
                "year": source["year"],
                "source_type": source["source_type"],
                "identifiers": source.get("identifiers") or {},
                "canonical_url": source["canonical_url"],
                "viewpoint_tags": source["viewpoint_tags"],
                "v1_acquisition_status": None,
                "v1_usable": False,
                "v1_artifact_sha256": None,
                "v1_normalized_sha256": None,
                "search_priority": "v2-long-form-and-ecosystem-expansion",
                "openalex_refresh_status": "not-applicable-v2-curated-discovery",
                "openalex_refreshed_at": None,
                "candidates": [],
                "attempts": [],
                "final_status": "v2-new-source-acquisition-pending",
                "selected_candidate_id": None,
                "selected_artifact": None,
                "remaining_search_notes": [],
            }
            rows.append(row)
            by_id[source_id] = row
            added += 1
        else:
            augmented += 1
        row["v2_curated_discovery"] = {
            "rationale": source["rationale"],
            "discovery_route": source["discovery_route"],
            "access_or_license_note": source["access_or_license_note"],
            "long_form": bool(source["long_form"]),
        }
        url = source["acquisition_url"]
        identity = {"source_id": source_id, "url": url}
        candidate_id = "v2_candidate_" + sha256_text(canonical_json(identity))
        route = source["route"]
        candidate = {
            "candidate_id": candidate_id,
            "route": route,
            "route_rank": ROUTE_ORDER[route],
            "url": url,
            "landing_page_url": source["canonical_url"],
            "host": _host(url),
            "source_name": source["discovery_route"],
            "source_type": "repository" if "repository" in route or "author" in route else "source",
            "version": source.get("version") or "specified curated version",
            "license": source["access_or_license_note"],
            "is_oa": True,
            "version_relationship": source.get("version_relationship") or (
                "Curated exact acquisition version; no identity with another edition is assumed"
            ),
            "known_difference": source.get("known_difference") or (
                "The retained artifact is the exact version at this URL and may differ from later "
                "published or revised versions"
            ),
            "storage_boundary": "external local artifact store; no full source text committed to Git",
            "discovery_evidence": source["discovery_route"],
            "force_ocr": bool(source.get("force_ocr")),
        }
        candidates_by_url = {
            item["url"]: item for item in row.get("candidates") or []
        }
        candidates_by_url[url] = candidate
        row["candidates"] = sorted(
            candidates_by_url.values(), key=lambda item: (item["route_rank"], item["url"])
        )
    write_jsonl(ACQUISITION_SEARCH_PATH, rows)
    print(f"added {added} v2 discoveries and augmented {augmented} existing relevant records")


def quarantine_acquisition_identity_mismatches() -> None:
    """Exclude acquired artifacts that fail exact source/full-text identity QA."""
    rows = load_jsonl(ACQUISITION_SEARCH_PATH)
    by_id = {row["source_id"]: row for row in rows}
    quarantined = 0
    for finding in load_json(V2_ACQUISITION_QUARANTINE_PATH):
        row = by_id.get(finding["source_id"])
        if row is None:
            raise ValueError(f"quarantine references unknown source {finding['source_id']}")
        selected_candidate_id = row.get("selected_candidate_id")
        candidate_ids = set(finding.get("candidate_ids") or [selected_candidate_id])
        matched = False
        for attempt in row.get("attempts") or []:
            if attempt.get("candidate_id") in candidate_ids and attempt.get("result") in (
                SUCCESS_RESULTS
                | {
                    "acquired-but-quarantined-source-identity-mismatch",
                    "acquired-but-quarantined-landing-page-only",
                    "acquired-but-quarantined-partial-preview",
                }
            ):
                attempt["result"] = finding["result"]
                attempt["status_class"] = _outcome_status_class(finding["result"])
                attempt["final_reason"] = finding["reason"]
                attempt["identity_audit_reason"] = finding["reason"]
                matched = True
        if not matched:
            raise ValueError(f"{finding['source_id']}: selected successful attempt not found")
        if selected_candidate_id not in candidate_ids:
            continue
        row["final_status"] = "quarantined-acquisition-identity-or-fulltext-mismatch"
        row["identity_audit"] = {
            "status": "quarantined",
            "reason": finding["reason"],
            "audited_at": (row.get("identity_audit") or {}).get("audited_at") or utc_now(),
        }
        retained_note = "The acquired bytes are retained for provenance but are not usable source text."
        row["remaining_search_notes"] = list(
            dict.fromkeys([*(row.get("remaining_search_notes") or []), retained_note])
        )
        quarantined += 1
    write_jsonl(ACQUISITION_SEARCH_PATH, rows)
    print(f"quarantined {quarantined} acquisition identity/full-text mismatches")


def _openalex_work_id(row: Mapping[str, Any]) -> str | None:
    value = (row.get("identifiers") or {}).get("openalex")
    if not value and str(row.get("source_id", "")).startswith("openalex_w"):
        value = "https://openalex.org/" + str(row["source_id"]).split("_", 1)[1].upper()
    if not value:
        return None
    return str(value).rsplit("/", 1)[-1].upper()


def _host(url: str | None) -> str:
    return (urllib.parse.urlparse(url or "").hostname or "").lower()


def _route_for_location(location: Mapping[str, Any]) -> str:
    url = str(location.get("pdf_url") or location.get("landing_page_url") or "")
    host = _host(url)
    source = location.get("source") or {}
    source_name = str(source.get("display_name") or "").lower()
    source_type = str(source.get("type") or "").lower()
    if "arxiv.org" in host or "arxiv" in source_name:
        return "arxiv-preprint"
    if "~" in urllib.parse.urlparse(url).path or any(
        token in host for token in ("people.", "personal.", "faculty.", "homepage.")
    ):
        return "author-hosted-manuscript"
    if any(
        token in host or token in source_name
        for token in (
            ".edu",
            ".ac.uk",
            "repository",
            "eprints",
            "dspace",
            "escholarship",
            "hal.science",
            "hal.archives",
            "inria",
            "research-portal",
            "ora.ox",
            "pure.",
        )
    ) or source_type == "repository":
        return "institutional-repository"
    if any(token in host for token in ("pmc.ncbi.nlm.nih.gov", "europepmc.org")):
        return "public-fulltext-repository"
    if any(
        token in host
        for token in (
            "projecteuclid.org",
            "numdam.org",
            "eudml.org",
            "archive.org",
            "emis.de",
            "ams.org",
        )
    ):
        return "lawful-mathematical-archive"
    if location.get("is_oa") or location.get("license"):
        return "open-publisher-copy"
    return "openalex-indexed-location"


def _download_url(location: Mapping[str, Any]) -> str | None:
    pdf_url = location.get("pdf_url")
    if pdf_url:
        return str(pdf_url)
    landing = str(location.get("landing_page_url") or "")
    match = re.search(r"arxiv\.org/(?:abs|pdf)/([^?#]+)", landing, flags=re.IGNORECASE)
    if match:
        return "https://arxiv.org/pdf/" + match.group(1).removesuffix(".pdf")
    return None


def _candidate(source_id: str, location: Mapping[str, Any]) -> dict[str, Any] | None:
    url = _download_url(location)
    if not url:
        return None
    source = location.get("source") or {}
    route = _route_for_location(location)
    identity = {"source_id": source_id, "url": url}
    version = location.get("version") or "unspecified"
    return {
        "candidate_id": "v2_candidate_" + sha256_text(canonical_json(identity)),
        "route": route,
        "route_rank": ROUTE_ORDER[route],
        "url": url,
        "landing_page_url": location.get("landing_page_url"),
        "host": _host(url),
        "source_name": source.get("display_name"),
        "source_type": source.get("type"),
        "version": version,
        "license": location.get("license"),
        "is_oa": bool(location.get("is_oa")),
        "version_relationship": (
            "location attached to the same OpenAlex work; version label preserved, but byte or "
            "mathematical identity is not assumed"
        ),
        "known_difference": (
            f"OpenAlex labels this {version}; typography, pagination, and revisions may differ "
            "from the canonical citation"
        ),
        "storage_boundary": "external local artifact store; redistribution grant evaluated separately",
        "discovery_evidence": "fresh OpenAlex locations metadata",
    }


def import_v1_alternate_versions() -> None:
    """Reuse lawful v1 preprint artifacts linked to a relevant published record.

    The duplicate row remains distinct bibliographic provenance.  V2 merely
    records that its already-normalized preprint is a usable alternate version
    of the otherwise inaccessible canonical/published row.
    """
    rows = load_jsonl(ACQUISITION_SEARCH_PATH)
    by_id = {row["source_id"]: row for row in rows}
    imported = 0
    for alternate in load_jsonl(pipeline.INVENTORY_PATH):
        canonical_id = alternate.get("duplicate_of")
        if alternate.get("scope_status") != "duplicate" or canonical_id not in by_id:
            continue
        if alternate.get("acquisition_status") != "acquired-and-normalized":
            continue
        canonical = by_id[canonical_id]
        url = alternate.get("acquisition_final_url") or alternate.get("acquisition_url")
        if not url:
            continue
        route = "arxiv-preprint" if "arxiv.org" in str(url) else "openalex-indexed-location"
        identity = {"source_id": canonical_id, "url": url}
        candidate_id = "v2_candidate_" + sha256_text(canonical_json(identity))
        candidate = {
            "candidate_id": candidate_id,
            "route": route,
            "route_rank": ROUTE_ORDER[route],
            "url": url,
            "landing_page_url": alternate.get("canonical_url"),
            "host": _host(str(url)),
            "source_name": "v1 duplicate/version audit",
            "source_type": alternate.get("source_type"),
            "version": "submittedVersion" if route == "arxiv-preprint" else "alternateVersion",
            "license": alternate.get("license"),
            "is_oa": True,
            "version_relationship": alternate.get("version_relationship") or "duplicate/version record",
            "known_difference": (
                "The alternate is linked by the audited v1 same-work relationship. It may differ "
                "in revision, pagination, typography, or publisher copy-editing."
            ),
            "storage_boundary": "existing v1 external artifact; not copied into Git or rewritten",
            "discovery_evidence": f"v1 duplicate row {alternate['source_id']}",
            "alternate_source_id": alternate["source_id"],
        }
        candidates_by_id = {
            item["candidate_id"]: item for item in canonical.get("candidates") or []
        }
        candidates_by_id[candidate_id] = candidate
        canonical["candidates"] = sorted(
            candidates_by_id.values(), key=lambda item: (item["route_rank"], item["url"])
        )
        attempt_identity = {
            "source_id": canonical_id,
            "round": "v1-alternate-version-preserved",
            "candidate_id": candidate_id,
        }
        attempt_id = "v2_attempt_" + sha256_text(canonical_json(attempt_identity))
        attempts_by_id = {
            item["attempt_id"]: item for item in canonical.get("attempts") or []
        }
        attempts_by_id[attempt_id] = {
            "attempt_id": attempt_id,
            "round_id": "v1-alternate-version-preserved",
            "candidate_id": candidate_id,
            "route": route,
            "requested_url": alternate.get("acquisition_url"),
            "attempted_at": alternate.get("acquisition_attempted_at"),
            "result": "acquired-and-normalized",
            "artifact_store": "riemann-corpus-v0",
            "effective_url": alternate.get("acquisition_final_url"),
            "media_type": alternate.get("media_type"),
            "artifact_relpath": alternate.get("artifact_relpath"),
            "artifact_sha256": alternate.get("artifact_sha256"),
            "artifact_bytes": alternate.get("artifact_bytes"),
            "normalized_relpath": alternate.get("normalized_relpath"),
            "normalized_sha256": alternate.get("normalized_sha256"),
            "normalized_bytes": alternate.get("normalized_bytes"),
            "normalized_page_count": alternate.get("normalized_page_count"),
            "warnings": alternate.get("acquisition_warnings") or [],
        }
        canonical["attempts"] = list(attempts_by_id.values())
        if not canonical.get("v1_usable") and canonical.get("final_status") != "recovered-usable-in-v2":
            selected = attempts_by_id[attempt_id]
            canonical["final_status"] = "recovered-usable-in-v2"
            canonical["selected_candidate_id"] = candidate_id
            canonical["selected_artifact"] = {
                key: selected.get(key)
                for key in (
                    "artifact_store",
                    "route",
                    "effective_url",
                    "media_type",
                    "artifact_relpath",
                    "artifact_sha256",
                    "artifact_bytes",
                    "normalized_relpath",
                    "normalized_sha256",
                    "normalized_bytes",
                    "normalized_page_count",
                    "warnings",
                )
            }
            imported += 1
    write_jsonl(ACQUISITION_SEARCH_PATH, rows)
    print(f"imported {imported} formerly unusable sources through audited v1 alternate versions")


def refresh_unpaywall(artifact_root: Path) -> None:
    """Add DOI-indexed repository/publisher locations not exposed by OpenAlex."""
    rows = load_jsonl(ACQUISITION_SEARCH_PATH)
    raw_root = artifact_root / "discovery" / "unpaywall"
    raw_root.mkdir(parents=True, exist_ok=True)
    queried = returned = new_candidates = 0
    for index, row in enumerate(rows, start=1):
        if row.get("v1_usable") or row.get("final_status") == "recovered-usable-in-v2":
            continue
        doi = str((row.get("identifiers") or {}).get("doi") or "")
        doi = doi.lower().removeprefix("https://doi.org/")
        if not doi or doi.startswith("10.48550/arxiv."):
            row["unpaywall_status"] = "not-applicable-no-published-doi"
            continue
        queried += 1
        raw_path = raw_root / f"{row['source_id']}.json"
        try:
            if raw_path.is_file():
                data = load_json(raw_path)
            else:
                encoded = urllib.parse.quote(doi, safe="")
                data = pipeline.fetch_json(
                    f"https://api.unpaywall.org/v2/{encoded}?email=codex@example.invalid"
                )
                write_json(raw_path, data)
                time.sleep(0.08)
            returned += 1
        except (OSError, ValueError, urllib.error.URLError) as error:
            row["unpaywall_status"] = f"lookup-failed: {type(error).__name__}: {error}"
            print(f"[{index}/{len(rows)}] {row['source_id']}: Unpaywall lookup failed", flush=True)
            continue
        before = len(row.get("candidates") or [])
        candidates_by_url = {
            str(candidate["url"]): candidate for candidate in row.get("candidates") or []
        }
        for location in data.get("oa_locations") or []:
            url_for_pdf = location.get("url_for_pdf")
            fallback_url = location.get("url")
            if not url_for_pdf and fallback_url and str(fallback_url).lower().endswith(".pdf"):
                url_for_pdf = fallback_url
            location_like = {
                "pdf_url": url_for_pdf,
                "landing_page_url": location.get("url_for_landing_page") or fallback_url,
                "license": location.get("license"),
                "version": location.get("version"),
                "is_oa": True,
                "source": {
                    "display_name": location.get("repository_institution") or location.get("host_type"),
                    "type": "repository" if location.get("host_type") == "repository" else "journal",
                },
            }
            candidate = _candidate(row["source_id"], location_like)
            if candidate:
                candidate["discovery_evidence"] = f"Unpaywall DOI lookup for {doi}"
                candidate["version_relationship"] = (
                    "Unpaywall location attached to the same DOI; host and version are preserved, "
                    "but byte identity is not assumed"
                )
                candidates_by_url[candidate["url"]] = candidate
        row["candidates"] = sorted(
            candidates_by_url.values(), key=lambda item: (item["route_rank"], item["url"])
        )
        gained = len(row["candidates"]) - before
        new_candidates += gained
        row["unpaywall_status"] = "refreshed"
        row["unpaywall_refreshed_at"] = utc_now()
        if gained:
            print(
                f"[{index}/{len(rows)}] {row['source_id']}: {gained} new Unpaywall location(s)",
                flush=True,
            )
    write_jsonl(ACQUISITION_SEARCH_PATH, rows)
    print(
        f"Unpaywall refresh: {queried} DOI lookups, {returned} responses, "
        f"{new_candidates} new direct full-text candidates"
    )


def _alternate_work_match(row: Mapping[str, Any], work: Mapping[str, Any]) -> dict[str, Any] | None:
    row_title = pipeline.normalize_dedupe_title(str(row.get("title") or ""))
    work_title = pipeline.normalize_dedupe_title(str(work.get("display_name") or ""))
    row_tokens = set(row_title.split())
    work_tokens = set(work_title.split())
    if not row_tokens or not work_tokens:
        return None
    overlap = len(row_tokens & work_tokens) / max(len(row_tokens), len(work_tokens))
    row_authors = pipeline.author_keys({"authors": row.get("authors") or []})
    work_authors = pipeline.author_keys({"authors": pipeline.openalex_authors(dict(work))})
    author_overlap = sorted(row_authors & work_authors)
    row_year, work_year = row.get("year"), work.get("publication_year")
    year_distance = (
        abs(int(row_year) - int(work_year))
        if isinstance(row_year, int) and isinstance(work_year, int)
        else None
    )
    exact_title = row_title == work_title
    if not author_overlap or (not exact_title and (overlap < 0.88 or min(len(row_tokens), len(work_tokens)) < 5)):
        return None
    # A looser title match is useful for TeX/markup variants, but it must not
    # silently turn a later sequel into a preprint/published-version relation.
    if year_distance is not None and year_distance > (6 if exact_title else 2):
        return None
    return {
        "openalex_id": work.get("id"),
        "title": work.get("display_name"),
        "authors": pipeline.openalex_authors(dict(work)),
        "year": work_year,
        "exact_normalized_title": exact_title,
        "title_token_overlap": round(overlap, 4),
        "overlapping_author_keys": author_overlap,
        "year_distance": year_distance,
    }


def search_openalex_alternate_works(
    artifact_root: Path, cached_only: bool = False, limit: int | None = None
) -> None:
    """Search for separately indexed preprints/versions by title and authorship."""
    rows = load_jsonl(ACQUISITION_SEARCH_PATH)
    raw_root = artifact_root / "discovery" / "openalex_alternate_search"
    raw_root.mkdir(parents=True, exist_ok=True)
    host_state_path = raw_root / "_host_state.json"
    if not host_state_path.is_file():
        source_states = [
            load_json(path)
            for path in raw_root.glob("openalex_*.state.json")
            if path.is_file()
        ]
        prior_attempts = [
            attempt
            for state in source_states
            for attempt in state.get("attempts") or []
        ]
        write_json(
            host_state_path,
            {
                "host": "api.openalex.org",
                "attempt_count": len(prior_attempts),
                "latest_attempt_at": max(
                    (str(attempt.get("attempted_at")) for attempt in prior_attempts),
                    default=None,
                ),
                "next_allowed_attempt_at": max(
                    (
                        str(attempt.get("next_allowed_attempt_at"))
                        for attempt in prior_attempts
                        if attempt.get("next_allowed_attempt_at")
                    ),
                    default=None,
                ),
            },
        )
    targets = [
        row
        for row in rows
        if not row.get("v1_usable")
        and row.get("final_status") != "recovered-usable-in-v2"
        and str(row.get("title") or "").strip()
        and (not cached_only or (raw_root / f"{row['source_id']}.json").is_file())
    ]
    query_results: dict[str, tuple[dict[str, Any] | None, str | None]] = {}

    def fetch_target(row: Mapping[str, Any]) -> tuple[str, dict[str, Any] | None, str | None]:
        raw_path = raw_root / f"{row['source_id']}.json"
        if raw_path.is_file():
            return str(row["source_id"]), load_json(raw_path), None
        host_state = load_json(host_state_path)
        host_next_allowed = host_state.get("next_allowed_attempt_at")
        if host_next_allowed and host_next_allowed > utc_now():
            return (
                str(row["source_id"]),
                None,
                f"host-cooling-down-until:{host_next_allowed}",
            )
        state_path = raw_root / f"{row['source_id']}.state.json"
        state = load_json(state_path) if state_path.is_file() else {"attempts": []}
        attempts = list(state.get("attempts") or [])
        if attempts:
            latest = attempts[-1]
            next_allowed = latest.get("next_allowed_attempt_at")
            if next_allowed and next_allowed > utc_now():
                return str(row["source_id"]), None, f"cooling-down-until:{next_allowed}"
            if latest.get("status_class") in {
                "route-specific-failure",
                "terminal-for-route",
            }:
                return (
                    str(row["source_id"]),
                    None,
                    f"openalex-search-route-exhausted:{latest.get('result')}",
                )
            if (
                latest.get("status_class") == "temporary-retryable"
                and len(attempts) >= DEFAULT_MAX_ROUTE_ATTEMPTS
            ):
                return str(row["source_id"]), None, "openalex-search-route-exhausted"
        attempted_at = utc_now()
        attempt_number = len(attempts) + 1
        try:
            params = urllib.parse.urlencode(
                {
                    "search": str(row["title"]),
                    "per-page": 10,
                    "mailto": "codex@example.invalid",
                }
            )
            data = pipeline.fetch_json("https://api.openalex.org/works?" + params)
            write_json(raw_path, data)
            attempts.append(
                {
                    "attempted_at": attempted_at,
                    "attempt_number": attempt_number,
                    "host": "api.openalex.org",
                    "result": "metadata-search-succeeded",
                    "status_class": "success",
                    "retry_after": None,
                    "backoff_seconds": None,
                    "next_allowed_attempt_at": None,
                }
            )
            write_json(state_path, {"source_id": row["source_id"], "attempts": attempts})
            write_json(
                host_state_path,
                {
                    "host": "api.openalex.org",
                    "attempt_count": int(host_state.get("attempt_count") or 0) + 1,
                    "latest_attempt_at": attempted_at,
                    "next_allowed_attempt_at": None,
                },
            )
            return str(row["source_id"]), data, None
        except (OSError, ValueError, urllib.error.URLError) as error:
            result = _failure_result(error)
            status_class = _outcome_status_class(result)
            retry_after, retry_after_seconds = _parse_retry_after_seconds(error, attempted_at)
            backoff = _retry_backoff_seconds(
                str(row["source_id"]),
                "openalex-alternate-search",
                attempt_number,
                result,
                retry_after_seconds,
            )
            next_allowed = (
                (datetime.fromisoformat(attempted_at) + timedelta(seconds=backoff)).isoformat()
                if backoff is not None
                else None
            )
            attempts.append(
                {
                    "attempted_at": attempted_at,
                    "attempt_number": attempt_number,
                    "host": "api.openalex.org",
                    "result": result,
                    "status_class": status_class,
                    "retry_after": retry_after,
                    "retry_after_seconds": retry_after_seconds,
                    "backoff_seconds": backoff,
                    "next_allowed_attempt_at": next_allowed,
                    "warning": f"{type(error).__name__}: {error}",
                }
            )
            write_json(state_path, {"source_id": row["source_id"], "attempts": attempts})
            write_json(
                host_state_path,
                {
                    "host": "api.openalex.org",
                    "attempt_count": int(host_state.get("attempt_count") or 0) + 1,
                    "latest_attempt_at": attempted_at,
                    "next_allowed_attempt_at": next_allowed,
                },
            )
            return str(row["source_id"]), None, f"{type(error).__name__}: {error}"

    network_attempts = 0
    for completed, row in enumerate(targets, start=1):
        raw_path = raw_root / f"{row['source_id']}.json"
        if not raw_path.is_file() and limit is not None and network_attempts >= limit:
            continue
        state_path = raw_root / f"{row['source_id']}.state.json"
        attempts_before = (
            len((load_json(state_path).get("attempts") or [])) if state_path.is_file() else 0
        )
        source_id, data, error = fetch_target(row)
        query_results[source_id] = (data, error)
        attempts_after = (
            len((load_json(state_path).get("attempts") or [])) if state_path.is_file() else 0
        )
        network_attempts += int(attempts_after > attempts_before)
        if completed % 25 == 0 or completed == len(targets):
            print(f"alternate-search metadata [{completed}/{len(targets)}]", flush=True)

    queried = matches = new_candidates = 0
    for index, row in enumerate(rows, start=1):
        if row.get("v1_usable") or row.get("final_status") == "recovered-usable-in-v2":
            continue
        title = str(row.get("title") or "").strip()
        if not title:
            row["alternate_work_search_status"] = "not-applicable-missing-title"
            continue
        queried += 1
        if row["source_id"] not in query_results:
            continue
        data, lookup_error = query_results[row["source_id"]]
        if data is None:
            if str(lookup_error).startswith("openalex-search-route-exhausted:"):
                row["alternate_work_search_status"] = f"search-exhausted: {lookup_error}"
            else:
                row["alternate_work_search_status"] = f"lookup-failed: {lookup_error}"
            print(f"[{index}/{len(rows)}] {row['source_id']}: alternate search failed", flush=True)
            continue
        own_work_id = _openalex_work_id(row)
        match_records: list[dict[str, Any]] = []
        before = len(row.get("candidates") or [])
        candidates_by_url = {
            str(candidate["url"]): candidate for candidate in row.get("candidates") or []
        }
        for work in data.get("results") or []:
            candidate_work_id = str(work.get("id") or "").rsplit("/", 1)[-1].upper()
            if candidate_work_id == own_work_id:
                continue
            match = _alternate_work_match(row, work)
            if match is None:
                continue
            match_records.append(match)
            locations = list(work.get("locations") or [])
            for extra in (work.get("best_oa_location"), work.get("primary_location")):
                if extra:
                    locations.append(extra)
            for location in locations:
                candidate = _candidate(row["source_id"], location)
                if candidate:
                    candidate["discovery_evidence"] = (
                        "fresh OpenAlex title/author search matched separately indexed work "
                        f"{work.get('id')}"
                    )
                    candidate["version_relationship"] = (
                        "probable preprint/published or duplicate version: normalized title and "
                        "author identity match; the records remain bibliographically distinct"
                    )
                    candidate["known_difference"] = (
                        "Separate OpenAlex work record; revision, pagination, copy-editing, or "
                        "substantive version differences have not been ruled out"
                    )
                    candidate["alternate_match"] = match
                    candidates_by_url[candidate["url"]] = candidate
        row["candidates"] = sorted(
            candidates_by_url.values(), key=lambda item: (item["route_rank"], item["url"])
        )
        gained = len(row["candidates"]) - before
        matches += len(match_records)
        new_candidates += gained
        row["alternate_work_search_status"] = "searched"
        row["alternate_work_searched_at"] = utc_now()
        row["alternate_work_matches"] = match_records
        if gained:
            print(
                f"[{index}/{len(rows)}] {row['source_id']}: {len(match_records)} matching work(s), "
                f"{gained} new location(s)",
                flush=True,
            )
    write_jsonl(ACQUISITION_SEARCH_PATH, rows)
    print(
        f"alternate-work search: {queried} title queries, {matches} high-confidence matches, "
        f"{new_candidates} new direct full-text candidates"
    )


def refresh_openalex(artifact_root: Path) -> None:
    """Refresh every OpenAlex-backed relevant row and enumerate all direct full-text locations."""
    if not ACQUISITION_SEARCH_PATH.is_file():
        raise ValueError("run init before refresh-openalex")
    rows = load_jsonl(ACQUISITION_SEARCH_PATH)
    work_to_source: dict[str, str] = {}
    for row in rows:
        if work_id := _openalex_work_id(row):
            work_to_source[work_id] = row["source_id"]
    raw_root = artifact_root / "discovery" / "openalex_refresh"
    raw_root.mkdir(parents=True, exist_ok=True)
    works: dict[str, dict[str, Any]] = {}
    identifiers = sorted(work_to_source)
    for batch_index, offset in enumerate(range(0, len(identifiers), 40), start=1):
        batch = identifiers[offset : offset + 40]
        params = urllib.parse.urlencode(
            {
                "filter": "openalex_id:" + "|".join(batch),
                "per-page": 200,
                "mailto": "codex@example.invalid",
            }
        )
        data = pipeline.fetch_json("https://api.openalex.org/works?" + params)
        write_json(raw_root / f"batch_{batch_index:02d}.json", data)
        for work in data.get("results") or []:
            works[str(work["id"]).rsplit("/", 1)[-1].upper()] = work
        print(f"[{batch_index}/{(len(identifiers) + 39) // 40}] refreshed {len(batch)} OpenAlex works")
        time.sleep(0.1)

    refreshed_at = utc_now()
    for row in rows:
        work_id = _openalex_work_id(row)
        if not work_id:
            row["openalex_refresh_status"] = "not-applicable-no-openalex-id"
            continue
        work = works.get(work_id)
        if work is None:
            row["openalex_refresh_status"] = "openalex-record-not-returned"
            row["openalex_refreshed_at"] = refreshed_at
            continue
        locations = list(work.get("locations") or [])
        for extra in (work.get("best_oa_location"), work.get("primary_location")):
            if extra:
                locations.append(extra)
        candidates_by_url: dict[str, dict[str, Any]] = {
            str(candidate["url"]): candidate for candidate in row.get("candidates") or []
        }
        for location in locations:
            candidate = _candidate(row["source_id"], location)
            if candidate:
                candidates_by_url[candidate["url"]] = candidate
        row["candidates"] = sorted(
            candidates_by_url.values(), key=lambda item: (item["route_rank"], item["url"])
        )
        row["openalex_refresh_status"] = "refreshed"
        row["openalex_refreshed_at"] = refreshed_at
        row["openalex_location_count"] = len(locations)
        row["openalex_cited_by_count_at_refresh"] = int(work.get("cited_by_count") or 0)
    write_jsonl(ACQUISITION_SEARCH_PATH, rows)
    print(
        f"refreshed {len(works)}/{len(identifiers)} OpenAlex works; "
        f"found {sum(len(row['candidates']) for row in rows)} direct full-text candidates"
    )


def _failure_result(error: BaseException) -> str:
    if isinstance(error, urllib.error.HTTPError):
        return f"blocked-http-{error.code}"
    if isinstance(error, urllib.error.URLError):
        reason = error.reason
        if isinstance(reason, ssl.SSLError):
            return "blocked-tls-validation"
        if isinstance(reason, (TimeoutError, socket.timeout)):
            return "download-timeout"
        return "download-failed"
    if isinstance(error, (TimeoutError, socket.timeout)):
        return "download-timeout"
    if isinstance(error, ValueError):
        return "normalization-or-content-validation-failed"
    return "download-failed"


def _outcome_status_class(result: str | None) -> str:
    if result in SUCCESS_RESULTS:
        return "success"
    if result in TEMPORARY_RESULTS or (
        isinstance(result, str)
        and re.fullmatch(r"blocked-http-5\d\d", result) is not None
    ):
        return "temporary-retryable"
    if result in TERMINAL_ROUTE_RESULTS:
        return "terminal-for-route"
    return "route-specific-failure"


def _parse_retry_after_seconds(error: BaseException, attempted_at: str) -> tuple[str | None, int | None]:
    if not isinstance(error, urllib.error.HTTPError) or error.headers is None:
        return None, None
    raw = error.headers.get("Retry-After")
    if raw is None:
        return None, None
    raw = raw.strip()
    if raw.isdigit():
        return raw, max(0, int(raw))
    try:
        retry_at = email.utils.parsedate_to_datetime(raw)
        if retry_at.tzinfo is None:
            retry_at = retry_at.replace(tzinfo=timezone.utc)
        attempted = datetime.fromisoformat(attempted_at)
        return raw, max(0, int((retry_at - attempted).total_seconds()))
    except (TypeError, ValueError, OverflowError):
        return raw, None


def _retry_backoff_seconds(
    source_id: str,
    candidate_id: str,
    attempt_number: int,
    result: str,
    retry_after_seconds: int | None,
) -> int | None:
    if _outcome_status_class(result) != "temporary-retryable":
        return None
    base = 900 if result == "blocked-http-429" else 60
    exponential = min(86_400, base * (2 ** max(0, attempt_number - 1)))
    jitter_seed = int(
        sha256_text(f"{source_id}:{candidate_id}:{attempt_number}")[:8], 16
    )
    jittered = int(exponential * (1.0 + (jitter_seed % 101) / 1000.0))
    return max(jittered, retry_after_seconds or 0)


def _normalize_pdf_v2(
    raw_path: Path, normalized_path: Path, force_ocr: bool = False
) -> tuple[int, list[str]]:
    """Normalize a PDF, parallelizing the issue-mandated last-resort OCR path."""
    with tempfile.TemporaryDirectory(prefix="mathia-riemann-v2-probe-") as temporary:
        probe = Path(temporary) / "probe.txt"
        completed = subprocess.run(
            ["pdftotext", "-enc", "UTF-8", "-layout", str(raw_path), str(probe)],
            capture_output=True,
            text=True,
            check=False,
        )
        if completed.returncode:
            raise ValueError(f"pdftotext failed: {completed.stderr.strip()[:400]}")
        value = probe.read_text(encoding="utf-8", errors="replace")
    if not force_ocr and len(re.sub(r"\s+", "", value)) >= 1_000:
        return pipeline.normalize_pdf(raw_path, normalized_path)
    if not shutil.which("pdftoppm") or not shutil.which("tesseract"):
        raise ValueError("scan requires OCR but pdftoppm/tesseract are unavailable")
    warnings = [
        "PDF extraction may degrade formulas, ligatures, or reading order; original retained",
        (
            "OCR fallback used because the PDF text layer was empty; formulas and symbols are "
            "lower-confidence and must be checked against the scan"
        ),
        "V2 OCR used 160 DPI grayscale rendering and two parallel page workers",
    ]
    with tempfile.TemporaryDirectory(prefix="mathia-riemann-v2-ocr-") as temporary:
        image_prefix = Path(temporary) / "ocr-page"
        rendered = subprocess.run(
            [
                "pdftoppm",
                "-r",
                "160",
                "-gray",
                "-jpeg",
                "-jpegopt",
                "quality=88",
                str(raw_path),
                str(image_prefix),
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        if rendered.returncode:
            raise ValueError(f"pdftoppm OCR rendering failed: {rendered.stderr.strip()[:400]}")
        image_paths = sorted(Path(temporary).glob("ocr-page-*.jpg"))

        def recognize(image_path: Path) -> tuple[Path, str]:
            completed = subprocess.run(
                ["tesseract", str(image_path), "stdout", "-l", "eng", "--dpi", "160"],
                capture_output=True,
                text=True,
                check=False,
            )
            if completed.returncode:
                raise ValueError(
                    f"tesseract failed for {image_path.name}: {completed.stderr.strip()[:400]}"
                )
            return image_path, completed.stdout

        pages_by_path: dict[Path, str] = {}
        # Tesseract itself uses multiple cores. Two page workers avoid the severe
        # oversubscription observed with a wider Python pool on the shared CPU.
        with ThreadPoolExecutor(max_workers=2) as executor:
            futures = [executor.submit(recognize, image_path) for image_path in image_paths]
            for future in as_completed(futures):
                image_path, text = future.result()
                pages_by_path[image_path] = text
        pages = [pages_by_path[image_path] for image_path in image_paths]
    normalized_path.write_text(
        "".join(
            f"\n<!-- source-page: {index} -->\n\n{page.strip()}\n"
            for index, page in enumerate(pages, start=1)
        ).lstrip(),
        encoding="utf-8",
    )
    if "�" in "".join(pages):
        warnings.append("Unicode replacement characters found")
    return len(pages), warnings


def _attempt_candidate(
    row: Mapping[str, Any], candidate: Mapping[str, Any], artifact_root: Path, round_id: str
) -> dict[str, Any]:
    attempted_at = utc_now()
    prior_attempts = [
        attempt
        for attempt in row.get("attempts") or []
        if attempt.get("candidate_id") == candidate.get("candidate_id")
    ]
    attempt_number = len(prior_attempts) + 1
    attempted_candidate_ids = {
        attempt.get("candidate_id") for attempt in row.get("attempts") or []
    }
    another_lawful_route_remaining = any(
        other.get("candidate_id") != candidate.get("candidate_id")
        and other.get("candidate_id") not in attempted_candidate_ids
        for other in row.get("candidates") or []
    )
    identity = {
        "source_id": row["source_id"],
        "round": round_id,
        "candidate_id": candidate["candidate_id"],
        "attempt_number": attempt_number,
    }
    attempt: dict[str, Any] = {
        "attempt_id": "v2_attempt_" + sha256_text(canonical_json(identity)),
        "round_id": round_id,
        "candidate_id": candidate["candidate_id"],
        "route": candidate["route"],
        "host": candidate.get("host") or urllib.parse.urlparse(str(candidate["url"])).hostname,
        "requested_url": candidate["url"],
        "attempted_at": attempted_at,
        "attempt_number": attempt_number,
        "result": None,
        "status_class": None,
        "retry_after": None,
        "retry_after_seconds": None,
        "backoff_seconds": None,
        "next_allowed_attempt_at": None,
        "another_lawful_route_remaining": another_lawful_route_remaining,
        "final_reason": None,
        "artifact_store": "riemann-corpus-v2",
        "effective_url": None,
        "media_type": None,
        "artifact_relpath": None,
        "artifact_sha256": None,
        "artifact_bytes": None,
        "normalized_relpath": None,
        "normalized_sha256": None,
        "normalized_bytes": None,
        "normalized_page_count": None,
        "warnings": [],
    }
    source_id = str(row["source_id"])
    candidate_suffix = str(candidate["candidate_id"])[-12:]
    raw_root = artifact_root / "raw" / source_id
    normalized_root = artifact_root / "normalized"
    raw_root.mkdir(parents=True, exist_ok=True)
    normalized_root.mkdir(parents=True, exist_ok=True)
    try:
        content, media_type, final_url = pipeline.request_bytes(str(candidate["url"]))
        if content.startswith(b"%PDF-"):
            suffix = ".pdf"
            media_type = "application/pdf"
        elif media_type in {"text/html", "application/xhtml+xml"} or b"<html" in content[:1000].lower():
            suffix = ".html"
            media_type = "text/html"
        elif media_type in {"text/plain", "application/x-tex", "text/x-tex"}:
            suffix = ".txt" if media_type == "text/plain" else ".tex"
        else:
            raise ValueError(f"unsupported or suspicious media type {media_type!r}")
        raw_path = raw_root / f"{candidate_suffix}{suffix}"
        raw_path.write_bytes(content)
        # Preserve the fetched bytes even if subsequent normalization or full-text
        # validation fails; the route outcome remains inspectable and resumable.
        attempt.update(
            {
                "effective_url": final_url,
                "media_type": media_type,
                "artifact_relpath": raw_path.relative_to(artifact_root).as_posix(),
                "artifact_sha256": sha256_file(raw_path),
                "artifact_bytes": raw_path.stat().st_size,
            }
        )
        normalized_path = normalized_root / f"{source_id}_{candidate_suffix}.txt"
        if media_type == "application/pdf":
            page_count, warnings = _normalize_pdf_v2(
                raw_path, normalized_path, force_ocr=bool(candidate.get("force_ocr"))
            )
        elif media_type == "text/html":
            page_count, warnings = pipeline.normalize_html(raw_path, normalized_path)
        else:
            normalized_path.write_text(content.decode("utf-8", errors="replace"), encoding="utf-8")
            page_count, warnings = 1, []
        normalized = normalized_path.read_text(encoding="utf-8", errors="replace")
        math_cues = len(
            re.findall(
                r"(?i)\b(theorem|lemma|proposition|corollary|proof|zeta|riemann|zeros?|primes?|formula|criterion)\b",
                normalized,
            )
        )
        if len(normalized.encode("utf-8")) < 1_000:
            raise ValueError("normalized text is shorter than 1,000 bytes")
        if media_type == "text/html" and (len(normalized) < 5_000 or math_cues < 10):
            raise ValueError("HTML response appears to be a landing/abstract page, not mathematical full text")
        attempt.update(
            {
                "result": "acquired-and-normalized",
                "status_class": "success",
                "effective_url": final_url,
                "media_type": media_type,
                "artifact_relpath": raw_path.relative_to(artifact_root).as_posix(),
                "artifact_sha256": sha256_file(raw_path),
                "artifact_bytes": raw_path.stat().st_size,
                "normalized_relpath": normalized_path.relative_to(artifact_root).as_posix(),
                "normalized_sha256": sha256_file(normalized_path),
                "normalized_bytes": normalized_path.stat().st_size,
                "normalized_page_count": page_count,
                "warnings": warnings,
            }
        )
    except (OSError, ValueError, urllib.error.URLError) as error:
        result = _failure_result(error)
        status_class = _outcome_status_class(result)
        retry_after, retry_after_seconds = _parse_retry_after_seconds(error, attempted_at)
        backoff_seconds = _retry_backoff_seconds(
            source_id,
            str(candidate["candidate_id"]),
            attempt_number,
            result,
            retry_after_seconds,
        )
        attempt["result"] = result
        attempt["status_class"] = status_class
        attempt["retry_after"] = retry_after
        attempt["retry_after_seconds"] = retry_after_seconds
        attempt["backoff_seconds"] = backoff_seconds
        if backoff_seconds is not None:
            attempted = datetime.fromisoformat(attempted_at)
            attempt["next_allowed_attempt_at"] = (
                attempted + timedelta(seconds=backoff_seconds)
            ).isoformat()
        if status_class == "terminal-for-route":
            attempt["final_reason"] = result
        elif status_class == "route-specific-failure":
            attempt["final_reason"] = "try-another-lawful-route"
        attempt["warnings"] = [f"{type(error).__name__}: {error}"]
    return attempt


def acquire_alternates(artifact_root: Path, round_id: str, limit: int | None) -> None:
    """Try ranked, as-yet-unattempted locations for every v1 recovery target."""
    rows = load_jsonl(ACQUISITION_SEARCH_PATH)
    attempted = 0
    recovered = 0
    for row_index, row in enumerate(rows, start=1):
        if row.get("v1_usable") or row.get("final_status") == "recovered-usable-in-v2":
            continue
        prior_candidate_ids = {
            attempt.get("candidate_id") for attempt in row.get("attempts") or [] if attempt.get("candidate_id")
        }
        candidates = [
            candidate
            for candidate in row.get("candidates") or []
            if candidate["candidate_id"] not in prior_candidate_ids
        ]
        if not candidates:
            if row.get("openalex_refresh_status") == "refreshed":
                row["final_status"] = "no-untried-openalex-fulltext-location"
            continue
        for candidate in candidates:
            if limit is not None and attempted >= limit:
                write_jsonl(ACQUISITION_SEARCH_PATH, rows)
                print(f"stopped at explicit diagnostic limit after {attempted} attempts")
                return
            attempt = _attempt_candidate(row, candidate, artifact_root, round_id)
            row.setdefault("attempts", []).append(attempt)
            attempted += 1
            print(
                f"[{row_index}/{len(rows)} attempt {attempted}] {row['source_id']} "
                f"{candidate['route']}: {attempt['result']}",
                flush=True,
            )
            if attempt["result"] in SUCCESS_RESULTS:
                row["final_status"] = "recovered-usable-in-v2"
                row["selected_candidate_id"] = candidate["candidate_id"]
                row["selected_artifact"] = {
                    key: attempt[key]
                    for key in (
                        "route",
                        "effective_url",
                        "media_type",
                        "artifact_relpath",
                        "artifact_sha256",
                        "artifact_bytes",
                        "normalized_relpath",
                        "normalized_sha256",
                        "normalized_bytes",
                        "normalized_page_count",
                        "warnings",
                    )
                }
                recovered += 1
                break
        else:
            row["final_status"] = "alternate-locations-attempted-without-usable-text"
        if attempted and attempted % 10 == 0:
            write_jsonl(ACQUISITION_SEARCH_PATH, rows)
    write_jsonl(ACQUISITION_SEARCH_PATH, rows)
    print(f"round {round_id}: {attempted} attempts, {recovered} newly recovered sources")


def retry_transient_failures(artifact_root: Path, round_id: str, delay_seconds: float) -> None:
    """Compatibility entry point for the persistent host-aware retry loop."""
    if delay_seconds:
        print(
            "--delay-seconds is superseded by persisted per-host cooldowns; "
            "the executor will not sleep globally"
        )
    run_persistent_acquisition_loop(
        artifact_root,
        round_id,
        limit=None,
        per_host_limit=1,
        max_route_attempts=DEFAULT_MAX_ROUTE_ATTEMPTS,
    )


def _attempt_effective_status(attempt: Mapping[str, Any]) -> str:
    return str(attempt.get("status_class") or _outcome_status_class(attempt.get("result")))


def _attempt_effective_next_allowed(
    source_id: str, candidate_id: str, attempt: Mapping[str, Any], attempt_count: int
) -> str | None:
    if attempt.get("next_allowed_attempt_at"):
        return str(attempt["next_allowed_attempt_at"])
    result = str(attempt.get("result") or "")
    backoff = _retry_backoff_seconds(
        source_id,
        candidate_id,
        attempt_count,
        result,
        attempt.get("retry_after_seconds") if isinstance(attempt.get("retry_after_seconds"), int) else None,
    )
    if backoff is None or not attempt.get("attempted_at"):
        return None
    try:
        return (
            datetime.fromisoformat(str(attempt["attempted_at"])) + timedelta(seconds=backoff)
        ).isoformat()
    except ValueError:
        return None


def _build_acquisition_retry_state(
    rows: list[dict[str, Any]],
    max_route_attempts: int,
    generated_at: str | None = None,
) -> dict[str, Any]:
    now = utc_now()
    routes: dict[str, dict[str, Any]] = {}
    hosts: dict[str, dict[str, Any]] = {}
    sources: dict[str, dict[str, Any]] = {}
    for row in rows:
        source_id = str(row["source_id"])
        attempts_by_candidate: dict[str, list[dict[str, Any]]] = {}
        for attempt in row.get("attempts") or []:
            if attempt.get("candidate_id"):
                attempts_by_candidate.setdefault(str(attempt["candidate_id"]), []).append(attempt)
        source_dispositions: Counter[str] = Counter()
        for candidate in row.get("candidates") or []:
            candidate_id = str(candidate["candidate_id"])
            attempts = attempts_by_candidate.get(candidate_id, [])
            latest = attempts[-1] if attempts else None
            host = str(
                candidate.get("host")
                or urllib.parse.urlparse(str(candidate.get("url") or "")).hostname
                or "unknown-host"
            )
            if latest is None:
                status_class = "unattempted"
                next_allowed = None
                disposition = "eligible"
            else:
                status_class = _attempt_effective_status(latest)
                next_allowed = _attempt_effective_next_allowed(
                    source_id, candidate_id, latest, len(attempts)
                )
                if status_class == "success":
                    disposition = "succeeded"
                elif status_class == "temporary-retryable" and len(attempts) >= max_route_attempts:
                    disposition = "exhausted-by-conservative-route-policy"
                elif status_class == "temporary-retryable" and next_allowed and next_allowed > now:
                    disposition = "cooling-down"
                elif status_class == "temporary-retryable":
                    disposition = "eligible"
                elif status_class == "terminal-for-route":
                    disposition = "terminal-for-route"
                else:
                    disposition = "search-another-route"
            route_key = f"{source_id}:{candidate_id}"
            backoff_seconds = (
                latest.get("backoff_seconds")
                if latest and latest.get("backoff_seconds") is not None
                else (
                    _retry_backoff_seconds(
                        source_id,
                        candidate_id,
                        len(attempts),
                        str(latest.get("result") or ""),
                        latest.get("retry_after_seconds")
                        if latest and isinstance(latest.get("retry_after_seconds"), int)
                        else None,
                    )
                    if latest
                    else None
                )
            )
            routes[route_key] = {
                "source_id": source_id,
                "candidate_id": candidate_id,
                "route": candidate.get("route"),
                "host": host,
                "attempt_count": len(attempts),
                "latest_attempt_at": latest.get("attempted_at") if latest else None,
                "latest_result": latest.get("result") if latest else None,
                "status_class": status_class,
                "retry_after": latest.get("retry_after") if latest else None,
                "retry_after_seconds": latest.get("retry_after_seconds") if latest else None,
                "backoff_seconds": backoff_seconds,
                "next_allowed_attempt_at": next_allowed,
                "another_lawful_route_remaining": any(
                    other.get("candidate_id") != candidate_id
                    and not attempts_by_candidate.get(str(other.get("candidate_id")))
                    for other in row.get("candidates") or []
                ),
                "final_reason": (
                    latest.get("final_reason")
                    if latest and latest.get("final_reason")
                    else "conservative-retry-policy-exhausted"
                    if disposition == "exhausted-by-conservative-route-policy"
                    else str(latest.get("result") or "")
                    if disposition in {"terminal-for-route", "search-another-route"} and latest
                    else None
                ),
                "disposition": disposition,
            }
            source_dispositions[disposition] += 1
            host_state = hosts.setdefault(
                host,
                {
                    "attempt_count": 0,
                    "temporary_failure_count": 0,
                    "latest_attempt_at": None,
                    "next_allowed_attempt_at": None,
                },
            )
            host_state["attempt_count"] += len(attempts)
            host_state["temporary_failure_count"] += sum(
                _attempt_effective_status(attempt) == "temporary-retryable"
                for attempt in attempts
            )
            for attempt in attempts:
                attempted_at = attempt.get("attempted_at")
                if attempted_at and (
                    host_state["latest_attempt_at"] is None
                    or attempted_at > host_state["latest_attempt_at"]
                ):
                    host_state["latest_attempt_at"] = attempted_at
            if latest and status_class == "temporary-retryable" and next_allowed and (
                host_state["next_allowed_attempt_at"] is None
                or next_allowed > host_state["next_allowed_attempt_at"]
            ):
                host_state["next_allowed_attempt_at"] = next_allowed
        alternate_status = row.get("alternate_work_search_status")
        alternate_search_complete = alternate_status == "searched" or str(
            alternate_status or ""
        ).startswith(("search-exhausted:", "not-applicable-"))
        if row.get("v1_usable") or row.get("final_status") == "recovered-usable-in-v2":
            source_disposition = "usable"
        elif not alternate_search_complete:
            source_disposition = "alternate-version-search-pending"
        elif source_dispositions.get("eligible"):
            source_disposition = "eligible-route-pending"
        elif source_dispositions.get("cooling-down"):
            source_disposition = "retryable-route-cooling"
        else:
            source_disposition = "lawful-routes-exhausted"
        sources[source_id] = {
            "source_id": source_id,
            "disposition": source_disposition,
            "alternate_work_search_status": alternate_status,
            "route_dispositions": dict(sorted(source_dispositions.items())),
            "final_reason": (
                "usable-full-text-selected"
                if source_disposition == "usable"
                else "alternate-version-search-not-complete"
                if source_disposition == "alternate-version-search-pending"
                else "temporary-route-remains"
                if source_disposition in {"eligible-route-pending", "retryable-route-cooling"}
                else "all-known-lawful-routes-exhausted-under-recorded-policy"
            ),
        }
    discovery_host_state_path = (
        DEFAULT_ARTIFACT_ROOT
        / "discovery"
        / "openalex_alternate_search"
        / "_host_state.json"
    )
    discovery_hosts = (
        {"api.openalex.org": load_json(discovery_host_state_path)}
        if discovery_host_state_path.is_file()
        else {}
    )
    return {
        "state_version": "riemann-v2-acquisition-retry-state-v1",
        "generated_at": generated_at or now,
        "policy": {
            "host_concurrency": 1,
            "max_attempts_per_route": max_route_attempts,
            "retry_after_precedence": True,
            "default_backoff": "conservative exponential backoff with deterministic 0-10% jitter",
            "global_sleep": False,
        },
        "hosts": dict(sorted(hosts.items())),
        "discovery_hosts": discovery_hosts,
        "routes": dict(sorted(routes.items())),
        "sources": dict(sorted(sources.items())),
        "source_disposition_counts": dict(
            sorted(Counter(row["disposition"] for row in sources.values()).items())
        ),
    }


def write_acquisition_retry_state(max_route_attempts: int) -> dict[str, Any]:
    rows = load_jsonl(ACQUISITION_SEARCH_PATH)
    state = _build_acquisition_retry_state(rows, max_route_attempts)
    write_json(ACQUISITION_RETRY_STATE_PATH, state)
    return state


def _mark_selected_artifact(row: dict[str, Any], candidate: Mapping[str, Any], attempt: Mapping[str, Any]) -> None:
    row["final_status"] = "recovered-usable-in-v2"
    row["selected_candidate_id"] = candidate["candidate_id"]
    row["selected_artifact"] = {
        key: attempt.get(key)
        for key in (
            "artifact_store",
            "route",
            "effective_url",
            "media_type",
            "artifact_relpath",
            "artifact_sha256",
            "artifact_bytes",
            "normalized_relpath",
            "normalized_sha256",
            "normalized_bytes",
            "normalized_page_count",
            "warnings",
        )
    }


def _refresh_source_retry_statuses(rows: list[dict[str, Any]], state: Mapping[str, Any]) -> None:
    source_states = state.get("sources") or {}
    for row in rows:
        if row.get("v1_usable") or row.get("final_status") == "recovered-usable-in-v2":
            continue
        disposition = (source_states.get(str(row["source_id"])) or {}).get("disposition")
        row["final_status"] = {
            "alternate-version-search-pending": "alternate-version-search-pending",
            "eligible-route-pending": "retryable-or-unattempted-route-pending",
            "retryable-route-cooling": "retryable-route-cooling",
            "lawful-routes-exhausted": "lawful-routes-exhausted-after-persistent-policy",
        }.get(disposition, str(disposition or "acquisition-state-unresolved"))


def run_persistent_acquisition_loop(
    artifact_root: Path,
    round_id: str,
    limit: int | None,
    per_host_limit: int,
    max_route_attempts: int,
) -> None:
    """Run one resumable, host-aware acquisition sweep without global sleeping."""
    if per_host_limit < 1 or max_route_attempts < 1:
        raise ValueError("per-host and per-route limits must be positive")
    rows = load_jsonl(ACQUISITION_SEARCH_PATH)
    state = _build_acquisition_retry_state(rows, max_route_attempts)
    routes = state["routes"]
    hosts = state["hosts"]
    now = utc_now()
    attempted_by_host: Counter[str] = Counter()
    attempts = recovered = 0
    for row in rows:
        if row.get("v1_usable") or row.get("final_status") == "recovered-usable-in-v2":
            continue
        if limit is not None and attempts >= limit:
            break
        for candidate in row.get("candidates") or []:
            if limit is not None and attempts >= limit:
                break
            route_state = routes[f"{row['source_id']}:{candidate['candidate_id']}"]
            if route_state["disposition"] != "eligible":
                continue
            host = str(route_state["host"])
            host_next = (hosts.get(host) or {}).get("next_allowed_attempt_at")
            if host_next and host_next > now:
                continue
            if attempted_by_host[host] >= per_host_limit:
                continue
            attempt = _attempt_candidate(row, candidate, artifact_root, round_id)
            row.setdefault("attempts", []).append(attempt)
            attempts += 1
            attempted_by_host[host] += 1
            print(
                f"[persistent attempt {attempts}] {row['source_id']} {candidate['route']} "
                f"host={host}: "
                f"{attempt['result']}",
                flush=True,
            )
            if attempt["result"] in SUCCESS_RESULTS:
                _mark_selected_artifact(row, candidate, attempt)
                recovered += 1
            # Persist both the attempt ledger and derived queue state after every request.
            write_jsonl(ACQUISITION_SEARCH_PATH, rows)
            state = _build_acquisition_retry_state(rows, max_route_attempts)
            write_json(ACQUISITION_RETRY_STATE_PATH, state)
            routes = state["routes"]
            hosts = state["hosts"]
            if attempt["result"] in SUCCESS_RESULTS:
                break
    state = _build_acquisition_retry_state(rows, max_route_attempts)
    _refresh_source_retry_statuses(rows, state)
    write_jsonl(ACQUISITION_SEARCH_PATH, rows)
    state = _build_acquisition_retry_state(rows, max_route_attempts)
    write_json(ACQUISITION_RETRY_STATE_PATH, state)
    if ACQUISITION_FRONTIER_PATH.is_file():
        ACQUISITION_FRONTIER_PATH.unlink()
    _write_acquisition_saturation_log()
    print(
        f"persistent acquisition {round_id}: {attempts} attempts across "
        f"{len(attempted_by_host)} hosts, {recovered} recoveries; "
        f"state={ACQUISITION_RETRY_STATE_PATH}"
    )


def repair_failed_attempt_artifact_provenance(artifact_root: Path) -> None:
    """Bind already-preserved response bytes from historical normalization failures."""
    rows = load_jsonl(ACQUISITION_SEARCH_PATH)
    repaired = 0
    for row in rows:
        raw_root = artifact_root / "raw" / str(row["source_id"])
        for attempt in row.get("attempts") or []:
            if (
                attempt.get("artifact_store") != "riemann-corpus-v2"
                or attempt.get("artifact_relpath")
                or not attempt.get("candidate_id")
            ):
                continue
            suffix = str(attempt["candidate_id"])[-12:]
            matches = sorted(raw_root.glob(f"{suffix}.*")) if raw_root.is_dir() else []
            if len(matches) != 1:
                continue
            path = matches[0]
            attempt["artifact_relpath"] = path.relative_to(artifact_root).as_posix()
            attempt["artifact_sha256"] = sha256_file(path)
            attempt["artifact_bytes"] = path.stat().st_size
            attempt["media_type"] = {
                ".pdf": "application/pdf",
                ".html": "text/html",
                ".txt": "text/plain",
                ".tex": "application/x-tex",
            }.get(path.suffix.lower(), attempt.get("media_type"))
            attempt.setdefault("warnings", []).append(
                "Response bytes recovered from the deterministic candidate artifact path; "
                "historical redirect/effective-URL metadata was unavailable"
            )
            repaired += 1
    write_jsonl(ACQUISITION_SEARCH_PATH, rows)
    write_acquisition_retry_state(DEFAULT_MAX_ROUTE_ATTEMPTS)
    print(f"repaired raw-artifact provenance for {repaired} failed attempts")


def acquisition_summary() -> dict[str, Any]:
    rows = load_jsonl(ACQUISITION_SEARCH_PATH)
    attempts = [attempt for row in rows for attempt in row.get("attempts") or []]
    network_attempts = [
        attempt
        for attempt in attempts
        if attempt.get("artifact_store") == "riemann-corpus-v2"
        and attempt.get("network_request_performed") is not False
    ]
    imported_attempts = [
        attempt for attempt in attempts if attempt.get("round_id") == "v1-alternate-version-preserved"
    ]
    v1_rows = [row for row in rows if row.get("lineage") == "v1-relevant"]
    new_rows = [row for row in rows if row.get("lineage") != "v1-relevant"]
    recovered = [
        row
        for row in v1_rows
        if not row.get("v1_usable") and row.get("final_status") == "recovered-usable-in-v2"
    ]
    acquired_new = [row for row in new_rows if row.get("final_status") == "recovered-usable-in-v2"]
    recovery_targets = [row for row in v1_rows if not row.get("v1_usable")]
    route_success = Counter(
        attempt["route"] for attempt in network_attempts if attempt.get("result") in SUCCESS_RESULTS
    )
    route_attempts = Counter(attempt["route"] for attempt in network_attempts)
    quarantined_attempts = [
        attempt
        for attempt in network_attempts
        if str(attempt.get("result") or "").startswith("acquired-but-quarantined-")
    ]
    retry_state = (
        load_json(ACQUISITION_RETRY_STATE_PATH)
        if ACQUISITION_RETRY_STATE_PATH.is_file()
        else _build_acquisition_retry_state(rows, DEFAULT_MAX_ROUTE_ATTEMPTS)
    )
    recovered_after_retry = 0
    recovered_by_alternate_route = 0
    for row in recovered:
        selected_id = row.get("selected_candidate_id")
        candidate_attempts = [
            attempt
            for attempt in row.get("attempts") or []
            if attempt.get("candidate_id") == selected_id
        ]
        if len(candidate_attempts) > 1:
            recovered_after_retry += 1
        if selected_id and any(
            attempt.get("candidate_id") != selected_id
            and attempt.get("artifact_store") == "riemann-corpus-v2"
            for attempt in row.get("attempts") or []
        ):
            recovered_by_alternate_route += 1
    source_dispositions = Counter(
        source.get("disposition") for source in (retry_state.get("sources") or {}).values()
    )
    return {
        "contract_version": interchange.CONTRACT_VERSION,
        "corpus_release_id": V2_RELEASE_ID,
        "parent_freeze_id": V1_FREEZE_ID,
        "relevant_v1_records": len(v1_rows),
        "new_v2_inventory_records": len(new_rows),
        "updated_relevant_inventory_records": len(rows),
        "v1_usable_carry_forwards": sum(bool(row.get("v1_usable")) for row in v1_rows),
        "recovery_targets": len(recovery_targets),
        "fresh_openalex_records": sum(row.get("openalex_refresh_status") == "refreshed" for row in rows),
        "direct_fulltext_candidates": sum(len(row.get("candidates") or []) for row in rows),
        "targets_with_candidates": sum(bool(row.get("candidates")) for row in recovery_targets),
        "fresh_network_attempts": len(network_attempts),
        "imported_v1_alternate_versions": len(imported_attempts),
        "fresh_attempt_outcomes": dict(sorted(Counter(attempt.get("result") for attempt in network_attempts).items())),
        "attempts_by_route": dict(sorted(route_attempts.items())),
        "recoveries_by_route": dict(sorted(route_success.items())),
        "quarantined_attempts": len(quarantined_attempts),
        "quarantined_sources": len(
            {
                row["source_id"]
                for row in rows
                if any(attempt in quarantined_attempts for attempt in row.get("attempts") or [])
            }
        ),
        "quarantined_outcomes": dict(
            sorted(Counter(attempt["result"] for attempt in quarantined_attempts).items())
        ),
        "formerly_unusable_recovered": len(recovered),
        "new_v2_sources_acquired": len(acquired_new),
        "total_usable_sources_after_round": (
            sum(bool(row.get("v1_usable")) for row in v1_rows) + len(recovered) + len(acquired_new)
        ),
        "remaining_recovery_targets": len(recovery_targets) - len(recovered),
        "curated_long_form_additions": sum(
            bool((row.get("v2_curated_discovery") or {}).get("long_form")) for row in new_rows
        ),
        "curated_long_form_sources": sum(
            bool((row.get("v2_curated_discovery") or {}).get("long_form")) for row in rows
        ),
        "v1_recovery_funnel": {
            "v1_unavailable_or_retryable_targets": len(recovery_targets),
            "recovered_after_same-route_retry": recovered_after_retry,
            "recovered_after_another_lawful_route": recovered_by_alternate_route,
            "recovered_total": len(recovered),
            "alternate_version_search_pending": source_dispositions.get(
                "alternate-version-search-pending", 0
            ),
            "retryable_or_unattempted_route_pending": source_dispositions.get(
                "eligible-route-pending", 0
            ),
            "retryable_route_cooling": source_dispositions.get("retryable-route-cooling", 0),
            "still_unavailable_after_exhaustive_lawful_search": source_dispositions.get(
                "lawful-routes-exhausted", 0
            ),
        },
        "generated_at": utc_now(),
    }


def _acquisition_saturation_entries() -> list[dict[str, Any]]:
    rows = load_jsonl(ACQUISITION_SEARCH_PATH)
    grouped: dict[str, list[tuple[dict[str, Any], dict[str, Any]]]] = {}
    for row in rows:
        for attempt in row.get("attempts") or []:
            round_id = str(attempt.get("round_id") or "")
            if not round_id or round_id == "v1-parent-preserved":
                continue
            grouped.setdefault(round_id, []).append((row, attempt))

    def sort_key(item: tuple[str, list[tuple[dict[str, Any], dict[str, Any]]]]) -> tuple[str, str]:
        round_id, pairs = item
        timestamps = [str(attempt.get("attempted_at")) for _, attempt in pairs if attempt.get("attempted_at")]
        return (min(timestamps) if timestamps else "9999", round_id)

    entries: list[dict[str, Any]] = []
    for round_id, pairs in sorted(grouped.items(), key=sort_key):
        successful_rows = {
            row["source_id"]: row
            for row, attempt in pairs
            if attempt.get("result") in SUCCESS_RESULTS
        }
        outcomes = Counter(str(attempt.get("result")) for _, attempt in pairs)
        routes = Counter(str(attempt.get("route")) for _, attempt in pairs)
        formerly_unusable = sum(
            row.get("lineage") == "v1-relevant" and not row.get("v1_usable")
            for row in successful_rows.values()
        )
        new_sources = sum(
            row.get("lineage") != "v1-relevant" for row in successful_rows.values()
        )
        attempts = len(pairs)
        recovered = len(successful_rows)
        identity = {
            "axis": "acquisition",
            "round_id": round_id,
            "attempts": attempts,
            "recovered_sources": recovered,
            "outcomes": dict(sorted(outcomes.items())),
        }
        if recovered == 0:
            evidence = (
                "This targeted retry produced no new usable source; its failures and route mix are "
                "preserved as direct diminishing-return evidence."
            )
        elif recovered < attempts // 2:
            evidence = (
                "This expansion round recovered a minority of attempted sources; most candidates "
                "were duplicate, inaccessible, blocked, or not usable full text."
            )
        else:
            evidence = (
                "This expansion round still had material yield and therefore cannot by itself "
                "establish acquisition saturation."
            )
        entries.append(
            {
                **identity,
                "entry_id": "v2_saturation_" + sha256_text(canonical_json(identity)),
                "recorded_at": max(
                    (str(attempt.get("attempted_at")) for _, attempt in pairs if attempt.get("attempted_at")),
                    default=None,
                ),
                "fresh_network_attempts": sum(
                    attempt.get("artifact_store") == "riemann-corpus-v2"
                    and attempt.get("network_request_performed") is not False
                    for _, attempt in pairs
                ),
                "imported_existing_artifact_attempts": sum(
                    attempt.get("artifact_store") == "riemann-corpus-v0" for _, attempt in pairs
                ),
                "formerly_unusable_recovered": formerly_unusable,
                "new_v2_sources_recovered": new_sources,
                "marginal_yield": recovered / attempts if attempts else 0.0,
                "routes": dict(sorted(routes.items())),
                "evidence": evidence,
            }
        )
    if ACQUISITION_FRONTIER_PATH.is_file():
        entries.append(load_json(ACQUISITION_FRONTIER_PATH))
    return entries


def _write_acquisition_saturation_log() -> None:
    preserved = (
        [row for row in load_jsonl(SATURATION_LOG_PATH) if row.get("axis") != "acquisition"]
        if SATURATION_LOG_PATH.is_file()
        else []
    )
    write_jsonl(SATURATION_LOG_PATH, [*_acquisition_saturation_entries(), *preserved])


def record_acquisition_frontier(round_id: str) -> None:
    """Record an exhausted known-candidate frontier without inventing a network attempt."""
    rows = load_jsonl(ACQUISITION_SEARCH_PATH)
    state = _build_acquisition_retry_state(rows, DEFAULT_MAX_ROUTE_ATTEMPTS)
    blocking_sources = [
        source_id
        for source_id, source in state["sources"].items()
        if source["disposition"] not in {"usable", "lawful-routes-exhausted"}
    ]
    if blocking_sources:
        counts = Counter(state["sources"][source_id]["disposition"] for source_id in blocking_sources)
        raise ValueError(
            "persistent lawful acquisition frontier is not exhausted: "
            f"{dict(sorted(counts.items()))}; examples={blocking_sources[:8]}"
        )
    pending = []
    for row in rows:
        if row.get("final_status") in {"usable-carried-from-v1", "recovered-usable-in-v2"}:
            continue
        attempted = {attempt.get("candidate_id") for attempt in row.get("attempts") or []}
        pending.extend(
            (row["source_id"], candidate["candidate_id"])
            for candidate in row.get("candidates") or []
            if candidate.get("candidate_id") not in attempted
        )
    if pending:
        raise ValueError(f"known lawful candidate frontier is not exhausted: {pending[:8]}")
    source_disposition_counts = dict(
        sorted(Counter(source["disposition"] for source in state["sources"].values()).items())
    )
    identity = {
        "axis": "acquisition",
        "round_id": round_id,
        "frontier_status": "terminal-practical-lawful-acquisition-saturation",
        "attempts": 0,
        "recovered_sources": 0,
        "outcomes": {"no-unattempted-lawful-candidates": 1},
        "pending_source_dispositions": {},
        "eligible_route_count": 0,
        "alternate_version_search_pending_count": 0,
        "retry_state_source_disposition_counts": source_disposition_counts,
    }
    write_json(
        ACQUISITION_FRONTIER_PATH,
        {
            **identity,
            "entry_id": "v2_saturation_" + sha256_text(canonical_json(identity)),
            "recorded_at": utc_now(),
            "fresh_network_attempts": 0,
            "imported_existing_artifact_attempts": 0,
            "formerly_unusable_recovered": 0,
            "new_v2_sources_recovered": 0,
            "marginal_yield": 0.0,
            "routes": {},
            "remaining_recovery_targets": sum(
                row.get("lineage") == "v1-relevant"
                and not row.get("v1_usable")
                and row.get("final_status") != "recovered-usable-in-v2"
                for row in rows
            ),
            "evidence": (
                "After persistent alternate-version searches and host-aware retries, every known "
                "lawful candidate either succeeded or reached the recorded conservative per-route "
                "exhaustion policy. The final scheduler sweep produced zero eligible attempts; "
                "remaining records require new external discovery or access changes."
            ),
        },
    )
    write_json(ACQUISITION_RETRY_STATE_PATH, state)
    _write_acquisition_saturation_log()
    print("recorded exhausted known lawful acquisition-candidate frontier")


def write_acquisition_summary(round_id: str, generated_at: str | None = None) -> None:
    rows = load_jsonl(ACQUISITION_SEARCH_PATH)
    reconciled = False
    for row in rows:
        audit = row.get("identity_audit") or {}
        selected_id = row.get("selected_candidate_id")
        selected_attempt = next(
            (
                attempt
                for attempt in reversed(row.get("attempts") or [])
                if attempt.get("candidate_id") == selected_id
            ),
            None,
        )
        if (
            row.get("final_status") == "recovered-usable-in-v2"
            and audit.get("status") == "quarantined"
            and selected_attempt
            and selected_attempt.get("result") in SUCCESS_RESULTS
        ):
            audit["status"] = "resolved-by-identity-verified-replacement"
            audit["replacement_candidate_id"] = selected_id
            audit["replacement_normalized_sha256"] = (
                row.get("selected_artifact") or {}
            ).get("normalized_sha256")
            audit["resolved_at"] = utc_now()
            row["identity_audit"] = audit
            reconciled = True
    if reconciled:
        write_jsonl(ACQUISITION_SEARCH_PATH, rows)
    summary = acquisition_summary()
    if generated_at is not None:
        summary["generated_at"] = generated_at
    write_json(ACQUISITION_SUMMARY_PATH, summary)
    _write_acquisition_saturation_log()
    print(json.dumps(summary, ensure_ascii=False, indent=2))


def _resolved_normalized_source(row: Mapping[str, Any]) -> dict[str, Any] | None:
    if row.get("v1_usable"):
        inspection_by_id = {
            item["source_id"]: item for item in load_jsonl(V1_ROOT / "source_inspection.jsonl")
        }
        inspection = inspection_by_id.get(str(row["source_id"]))
        if not inspection:
            return None
        return {
            "artifact_store": "riemann-corpus-v0",
            "artifact_root": str(pipeline.DEFAULT_ARTIFACT_ROOT),
            "normalized_relpath": inspection["normalized_relpath"],
            "normalized_sha256": inspection["normalized_sha256"],
            "normalized_bytes": inspection["normalized_bytes"],
            "normalized_page_count": inspection["normalized_page_count"],
            "extraction_warnings": inspection.get("acquisition_warnings") or [],
            "ocr": bool(inspection.get("ocr")),
            "inspection_decision": inspection["inspection_decision"],
            "inspection_reason": inspection["inspection_reason"],
        }
    if row.get("final_status") != "recovered-usable-in-v2":
        return None
    selected = row.get("selected_artifact") or {}
    store = selected.get("artifact_store") or "riemann-corpus-v2"
    root = pipeline.DEFAULT_ARTIFACT_ROOT if store == "riemann-corpus-v0" else DEFAULT_ARTIFACT_ROOT
    return {
        "artifact_store": store,
        "artifact_root": str(root),
        "normalized_relpath": selected["normalized_relpath"],
        "normalized_sha256": selected["normalized_sha256"],
        "normalized_bytes": selected["normalized_bytes"],
        "normalized_page_count": selected["normalized_page_count"],
        "extraction_warnings": selected.get("warnings") or [],
        "ocr": any("OCR fallback" in warning for warning in selected.get("warnings") or []),
        "inspection_decision": "pending-whole-source-v2-review",
        "inspection_reason": "lawful alternate normalized successfully; whole-source QA is pending",
    }


def _section_outline(lines: list[str]) -> list[dict[str, Any]]:
    headings: list[dict[str, Any]] = []
    heading_pattern = re.compile(
        r"^\s*(?:(?:chapter|lecture|section|appendix)\s+[A-Z0-9IVXLC]+\b|"
        r"[0-9]+(?:\.[0-9]+){0,3}\.?\s+[A-Z][^\n]{2,100}$|"
        r"(?:abstract|introduction|conclusion|conclusions|references|bibliography|contents)\s*$)",
        flags=re.IGNORECASE,
    )
    for line_number, line in enumerate(lines, start=1):
        text = re.sub(r"\s+", " ", line).strip()
        if not text or len(text) > 120:
            continue
        is_all_caps = len(text) >= 5 and any(char.isalpha() for char in text) and text == text.upper()
        if heading_pattern.match(text) or is_all_caps:
            headings.append({"line": line_number, "text": text})
    return headings


def build_depth_inventory() -> None:
    """Resolve every usable source and seed an auditable whole-source depth record."""
    rows = load_jsonl(ACQUISITION_SEARCH_PATH)
    v1_units_by_source: dict[str, list[dict[str, Any]]] = {}
    for unit in load_jsonl(V1_ROOT / "units.jsonl"):
        v1_units_by_source.setdefault(unit["source_id"], []).append(unit)
    records: list[dict[str, Any]] = []
    for row in rows:
        resolved = _resolved_normalized_source(row)
        if resolved is None:
            continue
        path = Path(resolved["artifact_root"]) / resolved["normalized_relpath"]
        text = path.read_text(encoding="utf-8", errors="replace")
        if sha256_file(path) != resolved["normalized_sha256"]:
            raise ValueError(f"{row['source_id']}: normalized source hash drift")
        lines = text.splitlines()
        prior_units = v1_units_by_source.get(row["source_id"], [])
        warnings = list(resolved["extraction_warnings"])
        ocr = bool(resolved.get("ocr"))
        records.append(
            {
                "source_id": row["source_id"],
                "lineage": row["lineage"],
                "title": row["title"],
                "authors": row["authors"],
                "year": row["year"],
                "source_type": row["source_type"],
                "viewpoint_tags": row.get("viewpoint_tags") or [],
                "acquisition_route": (row.get("selected_artifact") or {}).get("route") or "v1-carry-forward",
                "artifact_store": resolved["artifact_store"],
                "normalized_relpath": resolved["normalized_relpath"],
                "normalized_sha256": resolved["normalized_sha256"],
                "normalized_bytes": resolved["normalized_bytes"],
                "normalized_page_count": resolved["normalized_page_count"],
                "line_count": len(lines),
                "extraction_confidence": "ocr-lower-confidence" if ocr else "text-layer-with-formula-risk",
                "extraction_warnings": warnings,
                "v1_inspection_decision": resolved["inspection_decision"],
                "v1_or_acquisition_reason": resolved["inspection_reason"],
                "prior_v1_units": [
                    {
                        "unit_id": unit["unit_id"],
                        "line_start": unit["line_start"],
                        "line_end": unit["line_end"],
                        "unit_type": unit["unit_type"],
                    }
                    for unit in prior_units
                ],
                "machine_section_outline": _section_outline(lines),
                "whole_source_review_state": "awaiting-fresh-context-depth-plan",
                "stop_rule": (
                    "inspect every usable line; stop only when remaining text is accounted for as "
                    "repetition, routine detail, bibliography, irrelevant, or extraction-defective"
                ),
            }
        )
    write_jsonl(DEPTH_INVENTORY_PATH, records)
    print(
        f"wrote depth inventory for {len(records)} usable sources, including "
        f"{sum(bool(record['prior_v1_units']) for record in records)} with v1 units"
    )


def discover_reused_legacy_analysis_contexts(
    release_root: Path = V2_ROOT,
) -> dict[str, Any]:
    """Discover completed legacy analyses whose exact agent path was not isolated."""
    release_root = release_root.resolve()
    ledger_rows: list[dict[str, Any]] = []
    for relative in (
        "execution/legacy_context_recovery.jsonl",
        "execution/ai_execution_ledger.jsonl",
    ):
        ledger_path = release_root / relative
        if not ledger_path.is_file():
            raise ValueError(f"required execution ledger is missing: {relative}")
        rows = load_jsonl(ledger_path)
        execution_provenance.validate_execution_rows(rows)
        ledger_rows.extend(rows)

    contexts: list[dict[str, Any]] = []
    fresh_pending: list[str] = []
    for assignment_path in sorted(
        (release_root / "analyses/assignments").glob("*.json")
    ):
        assignment = load_json(assignment_path)
        release_relative = assignment_path.relative_to(release_root).as_posix()
        ledger_relative = _execution_ledger_relpath(release_root, assignment_path)
        assignment_sha256 = sha256_file(assignment_path)
        output_value = assignment.get("output_path")
        output_path = Path(str(output_value or ""))
        try:
            output_path.resolve().relative_to(release_root)
            output_is_local = isinstance(output_value, str) and bool(output_value)
        except ValueError:
            output_is_local = False
        if not output_is_local:
            raise ValueError(f"analysis output is outside the release: {release_relative}")
        matches = [
            row
            for row in ledger_rows
            if row.get("assignment_relpath") == ledger_relative
            and row.get("assignment_sha256") == assignment_sha256
            and row.get("requires_rerun") is False
            and row.get("status") in {"authoritative", "historical-recovered"}
        ]
        if not output_path.is_file():
            if (
                not matches
                and assignment.get("model_visible_packet_sha256")
                == model_visible_packet_sha256(assignment)
                and len(_assignment_source_ids(assignment.get("units") or assignment))
                == 1
            ):
                fresh_pending.append(release_relative)
                continue
            raise ValueError(
                f"legacy analysis output is missing without a bound fresh packet: "
                f"{release_relative}"
            )
        if len(matches) != 1:
            raise ValueError(
                f"{release_relative}: expected one exact completed execution receipt"
            )
        receipt = matches[0]
        if (
            receipt.get("output_sha256") != sha256_file(output_path)
            or receipt.get("output_records") != len(load_jsonl(output_path))
        ):
            raise ValueError(f"{release_relative}: execution output binding mismatch")
        task_path = receipt.get("agent_task_path")
        if not isinstance(task_path, str) or not task_path.startswith("/root/"):
            raise ValueError(f"{release_relative}: exact agent task path is missing")
        stage = str(assignment.get("stage") or receipt.get("stage") or "")
        source_ids = _assignment_source_ids(assignment.get("units") or assignment)
        if len(source_ids) != 1:
            raise ValueError(
                f"{release_relative}: expected one source, found {sorted(source_ids)}"
            )
        contexts.append(
            {
                "assignment_relpath": release_relative,
                "assignment_sha256": assignment_sha256,
                "ledger_assignment_relpath": ledger_relative,
                "output_relpath": output_path.resolve().relative_to(release_root).as_posix(),
                "output_sha256": str(receipt["output_sha256"]),
                "agent_task_path": task_path,
                "stage": stage,
            }
        )

    owners: dict[str, list[dict[str, Any]]] = {}
    for context in contexts:
        owners.setdefault(str(context["agent_task_path"]), []).append(context)
    reused_paths = {
        task_path for task_path, owned in owners.items() if len(owned) > 1
    }
    teacher_paths = {
        str(context["agent_task_path"])
        for context in contexts
        if context["stage"] in {"pass12", "generation"}
    }
    critic_paths = {
        str(context["agent_task_path"])
        for context in contexts
        if context["stage"]
        in {"pass3", "critic", "audit", "cross-source-audit", "independent-audit"}
    }
    teacher_critic_collisions = teacher_paths & critic_paths
    compromised_paths = reused_paths | teacher_critic_collisions
    affected = sorted(
        context["assignment_relpath"]
        for context in contexts
        if context["agent_task_path"] in compromised_paths
    )
    if not affected:
        raise ValueError("no reused legacy Riemann analysis contexts were discovered")
    affected_contexts = sorted(
        (
            dict(context)
            for context in contexts
            if context["agent_task_path"] in compromised_paths
        ),
        key=lambda context: str(context["assignment_relpath"]),
    )
    return {
        "affected_assignment_relpaths": affected,
        "affected_contexts": affected_contexts,
        "affected_context_count": len(affected),
        "fresh_pending_assignment_relpaths": sorted(fresh_pending),
        "retained_assignment_relpaths": sorted(
            context["assignment_relpath"]
            for context in contexts
            if context["agent_task_path"] not in compromised_paths
        ),
        "reused_task_paths": [
            {
                "agent_task_path": task_path,
                "assignment_count": len(owners[task_path]),
                "assignment_relpaths": sorted(
                    str(context["assignment_relpath"])
                    for context in owners[task_path]
                ),
                "stages": sorted(
                    {str(context["stage"]) for context in owners[task_path]}
                ),
            }
            for task_path in sorted(reused_paths)
        ],
        "teacher_critic_collision_paths": sorted(teacher_critic_collisions),
    }


def prepare_corrective_source_isolation_rerun(
    release_root: Path | None = None,
) -> dict[str, Any]:
    """Versioned correction for reused legacy analysis execution paths."""
    release_root = (release_root or V2_ROOT).resolve()
    archive_root = release_root / CORRECTIVE_ISOLATION_ARCHIVE_ROOT.name
    summary_path = archive_root / "summary.json"
    manifest_path = archive_root / "manifest.jsonl"
    if summary_path.is_file():
        in_progress = load_json(summary_path)
        if in_progress.get("phase") != "riemann-source-isolation-correction-v2":
            raise ValueError("unexpected corrective source-isolation summary phase")
        if in_progress.get("status") == "complete":
            errors = validate_source_isolation_archive(release_root, archive_root)
            if (
                not manifest_path.is_file()
                or in_progress.get("manifest_sha256") != sha256_file(manifest_path)
            ):
                errors.append("corrective source-isolation manifest hash mismatch")
            errors.extend(
                validate_execution_ledger_receipts(
                    release_root, allow_fresh_pending=True
                )
            )
            if errors:
                raise ValueError(
                    "invalid completed corrective source isolation:\n"
                    + "\n".join(errors)
                )
            return in_progress
    else:
        discovery = discover_reused_legacy_analysis_contexts(release_root)
        in_progress = {
            **discovery,
            "phase": "riemann-source-isolation-correction-v2",
            "status": "in_progress",
            "reason": (
                "legacy analysis task paths were reused across assignments or "
                "teacher/critic roles"
            ),
            "authoritative": False,
            "trainable": False,
        }
        _write_json_atomic(summary_path, in_progress)

    affected_relpaths = in_progress.get("affected_assignment_relpaths")
    affected_contexts = in_progress.get("affected_contexts")
    retained_relpaths = in_progress.get("retained_assignment_relpaths")
    if (
        not isinstance(affected_relpaths, list)
        or not affected_relpaths
        or not all(isinstance(value, str) and value for value in affected_relpaths)
        or not isinstance(affected_contexts, list)
        or not isinstance(retained_relpaths, list)
        or not all(isinstance(value, str) and value for value in retained_relpaths)
    ):
        raise ValueError("corrective source-isolation summary has invalid context sets")
    affected = set(affected_relpaths)
    expected_contexts = {
        str(context.get("assignment_relpath") or ""): context
        for context in affected_contexts
        if isinstance(context, Mapping)
    }
    if set(expected_contexts) != affected or len(expected_contexts) != len(
        affected_contexts
    ):
        raise ValueError("corrective summary lacks exact affected context descriptors")
    if affected & set(retained_relpaths):
        raise ValueError("corrective affected and retained context sets overlap")

    for relative in sorted(affected):
        assignment_path = release_root / relative
        archived_assignment_path = (
            archive_root / "non_authoritative" / "artifacts" / relative
        )
        source = (
            assignment_path
            if assignment_path.is_file()
            else archived_assignment_path
        )
        if not source.is_file():
            raise ValueError(
                f"missing corrective live/archive assignment evidence: {relative}"
            )
        assignment = load_json(source)
        expected = expected_contexts[relative]
        if sha256_file(source) != expected.get("assignment_sha256"):
            raise ValueError(f"corrective assignment evidence drift: {relative}")
        output_path = Path(str(assignment.get("output_path") or ""))
        try:
            output_relative = output_path.resolve().relative_to(release_root).as_posix()
        except ValueError as error:
            raise ValueError(
                f"corrective assignment output is outside release: {relative}"
            ) from error
        if output_relative != expected.get("output_relpath"):
            raise ValueError(f"corrective assignment output binding drift: {relative}")
        archived_output_path = (
            archive_root / "non_authoritative" / "artifacts" / output_relative
        )
        output_source = output_path if output_path.is_file() else archived_output_path
        if (
            not output_source.is_file()
            or sha256_file(output_source) != expected.get("output_sha256")
        ):
            raise ValueError(f"corrective output evidence drift: {relative}")
        _archive_file_for_isolation(
            release_root,
            archive_root,
            output_path,
            pool="non_authoritative",
            category="reused-legacy-analysis-output",
            reason="exact legacy agent task path was reused",
        )
        _archive_file_for_isolation(
            release_root,
            archive_root,
            assignment_path,
            pool="non_authoritative",
            category="reused-legacy-analysis-assignment",
            reason="exact legacy agent task path was reused",
        )

    provenance_path = release_root / "analyses/generation_provenance.jsonl"
    archived_provenance_path = (
        archive_root
        / "non_authoritative"
        / "artifacts"
        / provenance_path.relative_to(release_root)
    )
    provenance_source = (
        archived_provenance_path
        if archived_provenance_path.is_file()
        else provenance_path
    )
    if not provenance_source.is_file():
        raise ValueError("required analysis generation provenance is missing")
    provenance_rows = load_jsonl(provenance_source)
    affected_provenance = Counter(
        str(row.get("assignment_relpath") or "")
        for row in provenance_rows
        if row.get("assignment_relpath") in affected
    )
    if set(affected_provenance) != affected or any(
        count != 1 for count in affected_provenance.values()
    ):
        raise ValueError(
            "corrective analysis provenance does not bind every affected assignment exactly once"
        )
    filtered_provenance = [
        row
        for row in provenance_rows
        if row.get("assignment_relpath") not in affected
    ]
    if not archived_provenance_path.is_file():
        _archive_file_for_isolation(
            release_root,
            archive_root,
            provenance_path,
            pool="non_authoritative",
            category="corrective-analysis-provenance-snapshot",
            reason="preserve provenance before removing reused legacy contexts",
        )
    if provenance_path.is_file() and load_jsonl(provenance_path) != filtered_provenance:
        raise ValueError("corrective filtered analysis provenance drift")
    if not provenance_path.is_file():
        _write_jsonl_atomic(provenance_path, filtered_provenance)

    ledger_path = release_root / "execution/legacy_context_recovery.jsonl"
    archived_ledger_path = (
        archive_root
        / "non_authoritative"
        / "artifacts"
        / ledger_path.relative_to(release_root)
    )
    ledger_source = archived_ledger_path if archived_ledger_path.is_file() else ledger_path
    if not ledger_source.is_file():
        raise ValueError("required legacy execution ledger is missing")
    ledger_rows = load_jsonl(ledger_source)
    execution_provenance.validate_execution_rows(ledger_rows)
    affected_ledger_keys = {
        (
            _execution_ledger_relpath(release_root, release_root / relative),
            sha256_file(
                archive_root / "non_authoritative" / "artifacts" / relative
            ),
        )
        for relative in affected
    }
    bound_counts = Counter(
        (str(row.get("assignment_relpath") or ""), str(row.get("assignment_sha256") or ""))
        for row in ledger_rows
        if (row.get("assignment_relpath"), row.get("assignment_sha256"))
        in affected_ledger_keys
    )
    if set(bound_counts) != affected_ledger_keys or any(
        count != 1 for count in bound_counts.values()
    ):
        raise ValueError(
            "corrective legacy ledger does not bind every affected assignment exactly once"
        )
    updated_ledger = []
    for raw in ledger_rows:
        row = dict(raw)
        if (row.get("assignment_relpath"), row.get("assignment_sha256")) in affected_ledger_keys:
            row.update(
                {
                    "status": "isolation-invalid",
                    "requires_rerun": True,
                    "rerun_reason": "legacy-analysis-context-reuse",
                }
            )
        updated_ledger.append(row)
    execution_provenance.validate_execution_rows(updated_ledger)
    if not archived_ledger_path.is_file():
        _archive_file_for_isolation(
            release_root,
            archive_root,
            ledger_path,
            pool="non_authoritative",
            category="corrective-legacy-execution-ledger-snapshot",
            reason="preserve exact ledger before invalidating reused task paths",
        )
    if ledger_path.is_file() and load_jsonl(ledger_path) != updated_ledger:
        raise ValueError("corrective restated legacy execution ledger drift")
    if not ledger_path.is_file():
        _write_jsonl_atomic(ledger_path, updated_ledger)

    for relative in retained_relpaths:
        assignment_path = release_root / relative
        if not assignment_path.is_file():
            raise ValueError(f"corrective operation removed retained context: {relative}")
        output_path = Path(str(load_json(assignment_path).get("output_path") or ""))
        if not output_path.is_file():
            raise ValueError(f"retained context output is missing: {relative}")
    receipt_errors = validate_execution_ledger_receipts(
        release_root, allow_fresh_pending=True
    )
    if receipt_errors:
        raise ValueError(
            "corrective live execution receipts remain invalid:\n"
            + "\n".join(receipt_errors)
        )
    archive_errors = validate_source_isolation_archive(release_root, archive_root)
    if archive_errors:
        raise ValueError(
            "invalid corrective source-isolation archive:\n"
            + "\n".join(archive_errors)
        )
    manifest_rows = _archive_manifest_rows(manifest_path)
    summary = {
        **in_progress,
        "status": "complete",
        "archived_file_count": len(manifest_rows),
        "archived_bytes": sum(int(row["bytes"]) for row in manifest_rows),
        "manifest_sha256": sha256_file(manifest_path),
        "live_receipt_validation_errors": 0,
    }
    _write_json_atomic(summary_path, summary)
    return summary


def prepare_source_isolation_rerun(release_root: Path | None = None) -> dict[str, Any]:
    """Preserve and deactivate mixed-source work before a fresh source-local rerun."""
    release_root = (release_root or V2_ROOT).resolve()
    archive_root = release_root / ISOLATION_ARCHIVE_ROOT.name
    summary_path = archive_root / "summary.json"
    manifest_path = archive_root / "manifest.jsonl"
    if summary_path.is_file():
        summary = load_json(summary_path)
        if summary.get("status") == "complete":
            errors = validate_source_isolation_archive(release_root, archive_root)
            if (
                not manifest_path.is_file()
                or summary.get("manifest_sha256") != sha256_file(manifest_path)
            ):
                errors.append("source-isolation archive manifest hash mismatch")
            if errors:
                raise ValueError("invalid source-isolation archive:\n" + "\n".join(errors))
            return summary
        affected_source_ids = set(summary.get("affected_source_ids") or [])
        affected_unit_ids = set(summary.get("affected_unit_ids") or [])
    else:
        affected_source_ids: set[str] = set()
        affected_unit_ids: set[str] = set()
        for assignment_path in sorted((release_root / "depth/assignments").glob("batch_*.json")):
            source_ids = {
                str(row["source_id"])
                for row in load_json(assignment_path).get("sources") or []
            }
            if len(source_ids) > 1:
                affected_source_ids.update(source_ids)
        if not affected_source_ids:
            raise ValueError("no mixed-source Riemann depth contexts were discovered")
        write_json(
            summary_path,
            {
                "status": "in_progress",
                "reason": "mixed-source depth contexts invalidate source-isolation claims",
                "affected_source_ids": sorted(affected_source_ids),
                "authoritative": False,
                "trainable": False,
            },
        )

    units_path = release_root / "depth/units.jsonl"
    unit_rows = load_jsonl(units_path) if units_path.is_file() else []
    affected_unit_ids.update({
        str(row["unit_id"])
        for row in unit_rows
        if row.get("source_id") in affected_source_ids
    })

    def archived(relative: str, pool: str) -> bool:
        return any(
            row.get("original_relpath") == relative and row.get("pool") == pool
            for row in _archive_manifest_rows(manifest_path)
        )

    invalidated_assignment_relpaths: set[str] = set()
    reconciliation_assignment_relpaths: set[str] = set()

    def archive_existing(
        path: Path,
        *,
        pool: str,
        category: str,
        reason: str,
        reconciliation_eligible: bool = False,
    ) -> None:
        try:
            relative = path.resolve().relative_to(release_root).as_posix()
        except ValueError:
            return
        if not path.is_file() and not archived(relative, pool):
            return
        _archive_file_for_isolation(
            release_root,
            archive_root,
            path,
            pool=pool,
            category=category,
            reason=reason,
            reconciliation_eligible=reconciliation_eligible,
        )

    def archive_assignment(
        assignment_path: Path,
        *,
        pool: str,
        category: str,
        reason: str,
        reconciliation_eligible: bool = False,
    ) -> None:
        assignment = load_json(assignment_path)
        repo_relative = _execution_ledger_relpath(release_root, assignment_path)
        if pool == "reconciliation":
            reconciliation_assignment_relpaths.add(repo_relative)
        else:
            invalidated_assignment_relpaths.add(repo_relative)
        output_path = Path(str(assignment.get("output_path") or ""))
        archive_existing(
            output_path,
            pool=pool,
            category=category + "-output",
            reason=reason,
            reconciliation_eligible=reconciliation_eligible,
        )
        archive_existing(
            assignment_path,
            pool=pool,
            category=category + "-assignment",
            reason=reason,
            reconciliation_eligible=reconciliation_eligible,
        )

    mixed_depth_stems: set[str] = set()
    for assignment_path in sorted((release_root / "depth/assignments").glob("batch_*.json")):
        assignment = load_json(assignment_path)
        source_ids = {str(row["source_id"]) for row in assignment.get("sources") or []}
        if len(source_ids) > 1:
            mixed_depth_stems.add(assignment_path.stem)
            archive_assignment(
                assignment_path,
                pool="non_authoritative",
                category="mixed-depth",
                reason="one depth execution context contained unrelated sources",
            )
    for assignment_path in sorted((release_root / "depth/repair_assignments").glob("*.json")):
        assignment = load_json(assignment_path)
        base_stem = Path(str(assignment.get("base_assignment_path") or "")).stem
        source_ids = _assignment_source_ids(assignment)
        if base_stem in mixed_depth_stems or source_ids & affected_source_ids:
            archive_assignment(
                assignment_path,
                pool="non_authoritative",
                category="mixed-depth-repair",
                reason="repair output descends from a mixed-source depth context",
            )

    analysis_provenance_path = release_root / "analyses/generation_provenance.jsonl"
    analysis_provenance = (
        load_jsonl(analysis_provenance_path) if analysis_provenance_path.is_file() else []
    )
    legacy_execution_path = release_root / "execution/legacy_context_recovery.jsonl"
    legacy_execution_rows = load_jsonl(legacy_execution_path)
    if not legacy_execution_rows:
        raise ValueError("required legacy execution provenance ledger is missing")
    execution_provenance.validate_execution_rows(legacy_execution_rows)
    retained_analysis_assignments: set[str] = set()
    reconciliation_receipts: list[dict[str, Any]] = []
    for stage in ("pass12", "pass3", "pass4"):
        for assignment_path in sorted((release_root / "analyses/assignments").glob(f"{stage}_*.json")):
            assignment = load_json(assignment_path)
            source_ids = _assignment_source_ids(assignment.get("units") or [])
            if not source_ids & affected_source_ids:
                retained_analysis_assignments.add(
                    assignment_path.relative_to(release_root).as_posix()
                )
                continue
            source_local = len(source_ids) == 1
            if source_local:
                relative = assignment_path.relative_to(release_root).as_posix()
                ledger_relative = _execution_ledger_relpath(
                    release_root, assignment_path
                )
                output_path = Path(str(assignment.get("output_path") or ""))
                receipt = next(
                    (
                        row
                        for row in legacy_execution_rows
                        if row.get("assignment_relpath") == ledger_relative
                        and row.get("assignment_sha256") == sha256_file(assignment_path)
                        and output_path.is_file()
                        and row.get("output_sha256") == sha256_file(output_path)
                    ),
                    None,
                )
                if receipt is not None and receipt.get("agent_task_path"):
                    reconciliation_receipts.append(
                        {
                            **receipt,
                            "raw_output_sha256": receipt.get("output_sha256"),
                            "assignment_relpath": relative,
                            "model_visible_packet_sha256": model_visible_packet_sha256(assignment),
                        }
                    )
            archive_assignment(
                assignment_path,
                pool="reconciliation" if source_local else "non_authoritative",
                category=f"affected-{stage}",
                reason=(
                    "source-local context depends on upstream mixed-source work"
                    if source_local
                    else "analysis execution context contained unrelated sources"
                ),
                reconciliation_eligible=source_local,
            )
    if reconciliation_receipts:
        write_jsonl(
            archive_root / "reconciliation/receipts.jsonl",
            sorted(reconciliation_receipts, key=lambda row: row["assignment_relpath"]),
        )
    if analysis_provenance_path.is_file() and not archived(
        "analyses/generation_provenance.jsonl", "non_authoritative"
    ):
        archive_existing(
            analysis_provenance_path,
            pool="non_authoritative",
            category="analysis-provenance",
            reason="provenance ledger contains deactivated mixed/dependent contexts",
        )
        write_jsonl(
            analysis_provenance_path,
            [
                row
                for row in analysis_provenance
                if row.get("assignment_relpath") in retained_analysis_assignments
            ],
        )

    depth_provenance_path = release_root / "depth/generation_provenance.jsonl"
    if depth_provenance_path.is_file() and not archived(
        "depth/generation_provenance.jsonl", "non_authoritative"
    ):
        depth_provenance = load_jsonl(depth_provenance_path)
        archive_existing(
            depth_provenance_path,
            pool="non_authoritative",
            category="depth-provenance",
            reason="provenance ledger contains mixed-source contexts",
        )
        write_jsonl(
            depth_provenance_path,
            [
                row
                for row in depth_provenance
                if not set(row.get("assigned_source_ids") or []) & affected_source_ids
            ],
        )

    for root_name in (
        "synthesis/within_source/assignments",
        "synthesis/cross_source/generation_assignments",
        "synthesis/cross_source/adjudication_assignments",
        "audit/assignments",
    ):
        for assignment_path in sorted((release_root / root_name).glob("*.json")):
            archive_assignment(
                assignment_path,
                pool="reconciliation",
                category="downstream-source-isolation",
                reason="downstream context requires exact regenerated-input reconciliation",
                reconciliation_eligible=True,
            )

    reconciliation_files = (
        "audit/sample.jsonl",
        "audit/carried_pre_openalex.jsonl",
        "audit/independent_review.jsonl",
    )
    for relative in reconciliation_files:
        archive_existing(
            release_root / relative,
            pool="reconciliation",
            category="audit-reconciliation",
            reason="audit decision may carry only for an exact canonical regenerated packet",
            reconciliation_eligible=True,
        )

    for row in _archive_manifest_rows(manifest_path):
        if not str(row.get("category") or "").endswith("-assignment"):
            continue
        repo_relative = _execution_ledger_relpath(
            release_root, release_root / str(row["original_relpath"])
        )
        if row.get("pool") == "reconciliation":
            reconciliation_assignment_relpaths.add(repo_relative)
        else:
            invalidated_assignment_relpaths.add(repo_relative)

    def preserve_and_restate_execution_ledger(path: Path, category: str) -> list[dict[str, Any]]:
        relative = path.relative_to(release_root)
        archived_path = archive_root / "non_authoritative" / "artifacts" / relative
        rows = load_jsonl(archived_path if archived_path.is_file() else path)
        if not rows:
            raise ValueError(f"required execution provenance ledger is missing: {relative}")
        execution_provenance.validate_execution_rows(rows)
        if not archived_path.is_file():
            archive_existing(
                path,
                pool="non_authoritative",
                category=category,
                reason="preserve exact pre-rerun execution provenance before status reconciliation",
                reconciliation_eligible=True,
            )
        updated: list[dict[str, Any]] = []
        for raw in rows:
            row = dict(raw)
            if row.get("assignment_relpath") in invalidated_assignment_relpaths:
                row.update(
                    {
                        "status": "isolation-invalid",
                        "requires_rerun": True,
                        "rerun_reason": "source-isolation-invalid",
                    }
                )
            elif row.get("assignment_relpath") in reconciliation_assignment_relpaths:
                row.update(
                    {
                        "status": "reconciliation-pending",
                        "requires_rerun": True,
                        "rerun_reason": "upstream-source-isolation-invalidated",
                    }
                )
            updated.append(row)
        execution_provenance.validate_execution_rows(updated)
        write_jsonl(path, updated)
        return updated

    legacy_rows = preserve_and_restate_execution_ledger(
        release_root / "execution/legacy_context_recovery.jsonl",
        "legacy-execution-ledger-snapshot",
    )
    audit_execution_rows = preserve_and_restate_execution_ledger(
        release_root / "execution/ai_execution_ledger.jsonl",
        "audit-execution-ledger-snapshot",
    )
    decision_map_path = release_root / "audit/decision_execution_map.jsonl"
    decision_archive_path = (
        archive_root
        / "non_authoritative"
        / "artifacts"
        / decision_map_path.relative_to(release_root)
    )
    decision_rows = load_jsonl(
        decision_archive_path if decision_archive_path.is_file() else decision_map_path
    )
    if not decision_rows:
        raise ValueError("required audit decision execution map is missing")
    execution_provenance.validate_decision_rows(decision_rows)
    if not decision_archive_path.is_file():
        archive_existing(
            decision_map_path,
            pool="non_authoritative",
            category="audit-decision-map-snapshot",
            reason="preserve exact pre-rerun decision provenance before reconciliation",
        )
    pending_execution_ids = {
        str(row["ledger_id"])
        for row in [*legacy_rows, *audit_execution_rows]
        if row.get("requires_rerun")
    }
    updated_decisions = [
        {
            **row,
            "state": (
                "reconciliation-pending"
                if row.get("execution_ledger_id") in pending_execution_ids
                or str(row.get("state") or "").startswith("active-")
                else row.get("state")
            ),
        }
        for row in decision_rows
    ]
    execution_provenance.validate_decision_rows(updated_decisions)
    write_jsonl(decision_map_path, updated_decisions)

    derived_files = (
        "depth/units.jsonl",
        "analyses/pass1_spontaneous.jsonl",
        "analyses/pass2_directed.jsonl",
        "analyses/pass3_critic.jsonl",
        "analyses/pass4_deterministic.jsonl",
        "analyses/pass4_revised.jsonl",
        "execution/source_dossiers.jsonl",
        "execution/manifest.json",
        "execution/efficiency_metrics.json",
        "synthesis/within_source/candidates.jsonl",
        "synthesis/within_source/deterministic_rejections.jsonl",
        "synthesis/within_source/final.jsonl",
        "synthesis/cross_source/candidates.jsonl",
        "synthesis/cross_source/final.jsonl",
        "objects.jsonl",
        "trainable_manifest.json",
        "mixed_manifest.json",
        "mixed_manifest_status.json",
        "freeze.json",
        "REPORT.md",
        "release_manifest.json",
    )
    for relative in derived_files:
        archive_existing(
            release_root / relative,
            pool="non_authoritative",
            category="invalidated-derived-release",
            reason="artifact descends from source-isolation-compromised model work",
        )

    errors = validate_source_isolation_archive(release_root, archive_root)
    if errors:
        raise ValueError("invalid source-isolation archive:\n" + "\n".join(errors))
    manifest_rows = _archive_manifest_rows(manifest_path)
    summary = {
        "status": "complete",
        "reason": "mixed-source depth contexts invalidate source-isolation claims",
        "affected_source_ids": sorted(affected_source_ids),
        "affected_unit_ids": sorted(affected_unit_ids),
        "archived_file_count": len(manifest_rows),
        "reconciliation_file_count": sum(
            row["pool"] == "reconciliation" for row in manifest_rows
        ),
        "manifest_sha256": sha256_file(manifest_path),
        "prior_candidate_freeze_preserved": any(
            row["original_relpath"] == "freeze.json" for row in manifest_rows
        ),
        "authoritative": False,
        "trainable": False,
    }
    write_json(summary_path, summary)
    return summary


def prepare_depth_assignments(batch_count: int) -> None:
    """Prepare one deep-read context per source under the updated token policy."""
    if batch_count < 1:
        raise ValueError("batch_count must be positive")
    stale_outputs = sorted(DEPTH_PLAN_ROOT.glob("batch_*.jsonl"))
    if stale_outputs:
        raise ValueError(
            "depth outputs already exist; use append-unassigned-depth-assignments "
            "after archive/reconciliation"
        )
    records = load_jsonl(DEPTH_INVENTORY_PATH)
    sources: list[dict[str, Any]] = []
    for record in records:
        artifact_root = (
            pipeline.DEFAULT_ARTIFACT_ROOT
            if record["artifact_store"] == "riemann-corpus-v0"
            else DEFAULT_ARTIFACT_ROOT
        )
        sources.append(
            {
                **record,
                "normalized_abspath": str(artifact_root / record["normalized_relpath"]),
            }
        )
    DEPTH_ASSIGNMENT_ROOT.mkdir(parents=True, exist_ok=True)
    for path in DEPTH_ASSIGNMENT_ROOT.glob("batch_*.json"):
        path.unlink()
    for index, source in enumerate(sources, start=1):
        write_json(
            DEPTH_ASSIGNMENT_ROOT / f"batch_{index:02d}.json",
            _bind_model_visible_packet({
                "stage": "whole-source-depth",
                "task": "whole-source quota-free semantic depth planning",
                "context_policy": "one source deep-read once; no unrelated source batching",
                "execution_brief_path": str(EXECUTION_BRIEF_PATH),
                "prompt_path": str(V2_ROOT / "prompts" / "depth_segmentation.md"),
                "output_path": str(DEPTH_PLAN_ROOT / f"batch_{index:02d}.jsonl"),
                "sources": [source],
            }),
        )
    print(f"prepared {len(sources)} one-source depth contexts")


def append_unassigned_depth_assignments(max_batch_bytes: int = 350_000) -> None:
    """Append new or identity-repaired sources without rebalancing valid batches."""
    inventory_by_id = {
        row["source_id"]: row for row in load_jsonl(DEPTH_INVENTORY_PATH)
    }
    assigned_ids: set[str] = set()
    existing_numbers: list[int] = []
    for path in sorted(DEPTH_ASSIGNMENT_ROOT.glob("batch_*.json")):
        assignment = load_json(path)
        stale_ids = {
            source["source_id"]
            for source in assignment["sources"]
            if source["source_id"] not in inventory_by_id
            or source.get("normalized_sha256")
            != inventory_by_id[source["source_id"]].get("normalized_sha256")
        }
        if stale_ids:
            assignment["sources"] = [
                source
                for source in assignment["sources"]
                if source["source_id"] not in stale_ids
            ]
            plan_path = Path(assignment["output_path"])
            if plan_path.is_file():
                write_jsonl(
                    plan_path,
                    [
                        row
                        for row in load_jsonl(plan_path)
                        if row["source_id"] not in stale_ids
                    ],
                )
            if not assignment["sources"]:
                path.unlink()
                continue
            write_json(path, _bind_model_visible_packet(assignment))
        assigned_ids.update(source["source_id"] for source in assignment["sources"])
        match = re.fullmatch(r"batch_(\d+)", path.stem)
        if match:
            existing_numbers.append(int(match.group(1)))
    pending = [row for row in inventory_by_id.values() if row["source_id"] not in assigned_ids]
    if not pending:
        print("no unassigned usable depth sources")
        return
    batches: list[list[dict[str, Any]]] = []
    for record in sorted(pending, key=lambda item: (-int(item["normalized_bytes"]), item["source_id"])):
        artifact_root = (
            pipeline.DEFAULT_ARTIFACT_ROOT
            if record["artifact_store"] == "riemann-corpus-v0"
            else DEFAULT_ARTIFACT_ROOT
        )
        batches.append(
            [
                {
                    **record,
                    "normalized_abspath": str(artifact_root / record["normalized_relpath"]),
                }
            ]
        )
    next_number = max(existing_numbers, default=0) + 1
    for offset, sources in enumerate(batches):
        number = next_number + offset
        write_json(
            DEPTH_ASSIGNMENT_ROOT / f"batch_{number:02d}.json",
            _bind_model_visible_packet({
                "stage": "whole-source-depth",
                "task": "whole-source quota-free semantic depth planning (late lawful recovery)",
                "context_policy": "one source deep-read once; no unrelated source batching",
                "execution_brief_path": str(EXECUTION_BRIEF_PATH),
                "prompt_path": str(V2_ROOT / "prompts" / "depth_segmentation.md"),
                "output_path": str(DEPTH_PLAN_ROOT / f"batch_{number:02d}.jsonl"),
                "sources": sources,
            }),
        )
    print(f"appended {len(pending)} newly usable sources in {len(batches)} depth batches")


DEPTH_PLAN_FIELDS = {
    "source_id",
    "normalized_sha256",
    "inspection_summary",
    "sections_inspected",
    "accepted_units",
    "coverage_segments",
    "carried_v1_unit_ids",
    "v1_context_repairs",
    "within_source_synthesis_candidates",
    "remaining_meaningful_material",
    "within_source_saturation",
    "stop_reason",
}
DEPTH_UNIT_FIELDS = {
    "local_unit_id",
    "unit_type",
    "title",
    "line_start",
    "line_end",
    "why_material",
    "context_note",
    "representation_dependency",
}
COVERAGE_DISPOSITIONS = {
    "unit-bearing",
    "supporting-context",
    "routine-or-repetitive",
    "bibliography-or-front-matter",
    "outside-rh-scope",
    "extraction-defective",
}


def validate_depth_plans(require_complete: bool) -> list[str]:
    errors: list[str] = []
    inventory = {row["source_id"]: row for row in load_jsonl(DEPTH_INVENTORY_PATH)}
    seen_sources: list[str] = []
    seen_unit_ids: set[str] = set()
    assignment_paths = sorted(DEPTH_ASSIGNMENT_ROOT.glob("batch_*.json"))
    for assignment_path in assignment_paths:
        assignment = load_json(assignment_path)
        expected_sources = assignment.get("sources") or []
        if len(expected_sources) != 1:
            errors.append(
                f"{assignment_path.name}: depth context must bind exactly one source"
            )
        packet_sha256 = assignment.get("model_visible_packet_sha256")
        if packet_sha256 is not None and packet_sha256 != model_visible_packet_sha256(
            assignment
        ):
            errors.append(f"{assignment_path.name}: depth execution packet drift")
        plan_path = Path(str(assignment.get("output_path") or ""))
        if not plan_path.is_file():
            if require_complete:
                errors.append(f"{assignment_path.name}: missing depth plan {plan_path.name}")
            continue
        try:
            plans = load_jsonl(plan_path)
        except (OSError, ValueError, json.JSONDecodeError) as error:
            errors.append(f"{plan_path.name}: invalid JSONL: {error}")
            continue
        expected_ids = [row["source_id"] for row in expected_sources]
        plan_ids = [row.get("source_id") for row in plans]
        if plan_ids != expected_ids:
            errors.append(f"{plan_path.name}: source order differs from assignment")
        if set(plan_ids) != set(expected_ids):
            errors.append(f"{plan_path.name}: source set differs from assignment")
        expected_by_id = {row["source_id"]: row for row in expected_sources}
        for plan in plans:
            source_id = str(plan.get("source_id") or "")
            seen_sources.append(source_id)
            expected = expected_by_id.get(source_id)
            if expected is None:
                errors.append(f"{plan_path.name}: unexpected source {source_id}")
                continue
            if set(plan) != DEPTH_PLAN_FIELDS:
                errors.append(f"{source_id}: depth plan fields differ from the frozen prompt")
            if plan.get("normalized_sha256") != expected.get("normalized_sha256"):
                errors.append(f"{source_id}: normalized_sha256 mismatch")
            line_count = int(expected["line_count"])
            sections = plan.get("sections_inspected")
            units = plan.get("accepted_units")
            segments = plan.get("coverage_segments")
            if not isinstance(sections, list) or not isinstance(units, list) or not isinstance(segments, list):
                errors.append(f"{source_id}: sections, units, and coverage must be lists")
                continue
            for section in sections:
                if not isinstance(section, dict) or not {
                    "label", "line_start", "line_end", "mathematical_role"
                }.issubset(section):
                    errors.append(f"{source_id}: malformed section record")
                    continue
                if not (1 <= int(section["line_start"]) <= int(section["line_end"]) <= line_count):
                    errors.append(f"{source_id}: section outside source range")
            local_ids: set[str] = set()
            for unit in units:
                if not isinstance(unit, dict) or set(unit) != DEPTH_UNIT_FIELDS:
                    errors.append(f"{source_id}: malformed accepted unit")
                    continue
                unit_id = str(unit["local_unit_id"])
                if unit_id in local_ids or unit_id in seen_unit_ids:
                    errors.append(f"{source_id}: duplicate accepted unit id {unit_id}")
                local_ids.add(unit_id)
                seen_unit_ids.add(unit_id)
                if not (1 <= int(unit["line_start"]) <= int(unit["line_end"]) <= line_count):
                    errors.append(f"{source_id}: unit {unit_id} outside source range")
            if not segments:
                errors.append(f"{source_id}: empty coverage partition")
            else:
                next_line = 1
                for segment in segments:
                    if not isinstance(segment, dict) or not {
                        "line_start", "line_end", "disposition", "reason"
                    }.issubset(segment):
                        errors.append(f"{source_id}: malformed coverage segment")
                        continue
                    start, end = int(segment["line_start"]), int(segment["line_end"])
                    if start != next_line or end < start or end > line_count:
                        errors.append(f"{source_id}: coverage is not an exact ordered partition at line {next_line}")
                        break
                    if segment["disposition"] not in COVERAGE_DISPOSITIONS:
                        errors.append(f"{source_id}: invalid coverage disposition {segment['disposition']}")
                    next_line = end + 1
                if next_line != line_count + 1:
                    errors.append(f"{source_id}: coverage does not end at line {line_count}")
            expected_v1 = [unit["unit_id"] for unit in expected.get("prior_v1_units") or []]
            if plan.get("carried_v1_unit_ids") != expected_v1:
                errors.append(f"{source_id}: carried v1 unit ids do not match immutable lineage")
            for repair in plan.get("v1_context_repairs") or []:
                if repair.get("unit_id") not in expected_v1:
                    errors.append(f"{source_id}: context repair references unknown v1 unit")
                if not (1 <= int(repair.get("needed_line_start", 0)) <= int(repair.get("needed_line_end", 0)) <= line_count):
                    errors.append(f"{source_id}: context repair outside source range")
            for synthesis in plan.get("within_source_synthesis_candidates") or []:
                parents = synthesis.get("parent_local_unit_ids") or []
                if len(parents) < 2 or not set(parents).issubset(local_ids):
                    errors.append(f"{source_id}: within-source synthesis has unresolved parents")
            stop_reason = str(plan.get("stop_reason") or "").lower()
            quota_stop_phrases = ("stopped at quota", "unit quota reached", "batch size limit")
            if not stop_reason or any(phrase in stop_reason for phrase in quota_stop_phrases):
                errors.append(f"{source_id}: invalid quota-like or empty stop reason")
    if len(seen_sources) != len(set(seen_sources)):
        errors.append("a source occurs in more than one depth plan")
    if require_complete and set(seen_sources) != set(inventory):
        missing = sorted(set(inventory) - set(seen_sources))
        extra = sorted(set(seen_sources) - set(inventory))
        errors.append(f"depth plan coverage mismatch: missing={missing[:8]} extra={extra[:8]}")
    return errors


def prepare_missing_depth_assignments() -> None:
    DEPTH_REPAIR_ASSIGNMENT_ROOT.mkdir(parents=True, exist_ok=True)
    # Completed repair assignments are immutable generation provenance. Rebuild
    # their small assignment descriptors from the preserved raw repair outputs
    # if a previous orchestration pass removed them.
    for repair_plan_path in sorted(DEPTH_REPAIR_PLAN_ROOT.glob("batch_*_missing.jsonl")):
        base_stem = repair_plan_path.stem.removesuffix("_missing")
        base_assignment_path = DEPTH_ASSIGNMENT_ROOT / f"{base_stem}.json"
        if not base_assignment_path.is_file():
            continue
        base_assignment = load_json(base_assignment_path)
        repaired_ids = {row["source_id"] for row in load_jsonl(repair_plan_path)}
        repaired_sources = [
            source for source in base_assignment["sources"] if source["source_id"] in repaired_ids
        ]
        write_json(
            DEPTH_REPAIR_ASSIGNMENT_ROOT / f"{repair_plan_path.stem}.json",
            _bind_model_visible_packet({
                "stage": "missing-source-depth-repair",
                "task": "whole-source quota-free semantic depth planning (missing-source repair)",
                "prompt_path": base_assignment["prompt_path"],
                "output_path": str(repair_plan_path),
                "base_assignment_path": str(base_assignment_path),
                "base_plan_path": base_assignment["output_path"],
                "sources": repaired_sources,
            }),
        )
    created = missing_sources = 0
    for assignment_path in sorted(DEPTH_ASSIGNMENT_ROOT.glob("batch_*.json")):
        assignment = load_json(assignment_path)
        plan_path = Path(assignment["output_path"])
        if not plan_path.is_file():
            continue
        present = {row["source_id"] for row in load_jsonl(plan_path)}
        missing = [source for source in assignment["sources"] if source["source_id"] not in present]
        if not missing:
            continue
        stem = assignment_path.stem + "_missing"
        write_json(
            DEPTH_REPAIR_ASSIGNMENT_ROOT / f"{stem}.json",
            _bind_model_visible_packet({
                "stage": "missing-source-depth-repair",
                "task": "whole-source quota-free semantic depth planning (missing-source repair)",
                "prompt_path": assignment["prompt_path"],
                "output_path": str(DEPTH_REPAIR_PLAN_ROOT / f"{stem}.jsonl"),
                "base_assignment_path": str(assignment_path),
                "base_plan_path": str(plan_path),
                "sources": missing,
            }),
        )
        created += 1
        missing_sources += len(missing)
    print(f"prepared {created} missing-source repair assignments for {missing_sources} sources")


def prune_quarantined_depth_sources() -> None:
    """Remove newly quarantined sources without rebalancing already-frozen depth batches."""
    usable_ids = {
        row["source_id"]
        for row in load_jsonl(ACQUISITION_SEARCH_PATH)
        if row.get("v1_usable") or row.get("final_status") == "recovered-usable-in-v2"
    }
    inventory = [row for row in load_jsonl(DEPTH_INVENTORY_PATH) if row["source_id"] in usable_ids]
    write_jsonl(DEPTH_INVENTORY_PATH, inventory)
    pruned = 0
    for assignment_path in sorted(DEPTH_ASSIGNMENT_ROOT.glob("batch_*.json")):
        assignment = load_json(assignment_path)
        before = len(assignment["sources"])
        assignment["sources"] = [
            source for source in assignment["sources"] if source["source_id"] in usable_ids
        ]
        pruned += before - len(assignment["sources"])
        if not assignment["sources"]:
            assignment_path.unlink()
            continue
        write_json(assignment_path, assignment)
        plan_path = Path(assignment["output_path"])
        if plan_path.is_file():
            write_jsonl(
                plan_path,
                [row for row in load_jsonl(plan_path) if row["source_id"] in usable_ids],
            )
    print(f"pruned {pruned} quarantined sources from depth assignments without rebalancing")


def merge_depth_repair_plans() -> None:
    merged = 0
    for repair_assignment_path in sorted(DEPTH_REPAIR_ASSIGNMENT_ROOT.glob("batch_*_missing.json")):
        repair = load_json(repair_assignment_path)
        repair_plan_path = Path(repair["output_path"])
        if not repair_plan_path.is_file():
            raise ValueError(f"missing repair plan {repair_plan_path}")
        base_assignment = load_json(Path(repair["base_assignment_path"]))
        base_plan_path = Path(repair["base_plan_path"])
        expected_ids = [source["source_id"] for source in base_assignment["sources"]]
        by_source = {row["source_id"]: row for row in load_jsonl(base_plan_path)}
        for row in load_jsonl(repair_plan_path):
            source_id = row["source_id"]
            if source_id not in expected_ids:
                # A later acquisition identity audit may have pruned this source
                # from the live batch while retaining the repair as provenance.
                continue
            existing = by_source.get(source_id)
            if existing is None:
                by_source[source_id] = row
        if set(by_source) != set(expected_ids):
            raise ValueError(f"{base_plan_path.name}: repair does not resolve exact source set")
        write_jsonl(base_plan_path, [by_source[source_id] for source_id in expected_ids])
        merged += 1
    print(f"merged {merged} missing-source repair plans into deterministic base plans")


def normalize_depth_plan_order() -> None:
    """Rewrite completed batch plans into deterministic assignment order."""
    rewritten = 0
    for assignment_path in sorted(DEPTH_ASSIGNMENT_ROOT.glob("batch_*.json")):
        assignment = load_json(assignment_path)
        plan_path = Path(assignment["output_path"])
        if not plan_path.is_file():
            continue
        by_source = {row["source_id"]: row for row in load_jsonl(plan_path)}
        expected_ids = [source["source_id"] for source in assignment["sources"]]
        if set(by_source) != set(expected_ids):
            raise ValueError(f"{plan_path.name}: cannot normalize mismatched source set")
        ordered = [by_source[source_id] for source_id in expected_ids]
        write_jsonl(plan_path, ordered)
        rewritten += 1
    print(f"normalized deterministic source order in {rewritten} completed depth plans")


def sanitize_depth_synthesis_candidates() -> None:
    """Preserve but exclude malformed one-parent or unresolved synthesis candidates."""
    rejected_by_id = {
        row["rejection_id"]: row for row in load_jsonl(DEPTH_SYNTHESIS_REJECTIONS_PATH)
    }
    rewritten = 0
    for assignment_path in sorted(DEPTH_ASSIGNMENT_ROOT.glob("batch_*.json")):
        plan_path = Path(load_json(assignment_path)["output_path"])
        if not plan_path.is_file():
            continue
        rows = load_jsonl(plan_path)
        for row in rows:
            local_ids = {unit["local_unit_id"] for unit in row["accepted_units"]}
            retained = []
            for candidate in row["within_source_synthesis_candidates"]:
                parents = candidate.get("parent_local_unit_ids") or []
                if len(parents) >= 2 and set(parents).issubset(local_ids):
                    retained.append(candidate)
                    continue
                identity = {
                    "source_id": row["source_id"],
                    "title": candidate.get("title"),
                    "parents": parents,
                }
                rejection = {
                    **identity,
                    "rejection_id": "v2_synthesis_rejection_" + sha256_text(canonical_json(identity)),
                    "candidate": candidate,
                    "reason": (
                        "within-source synthesis requires at least two resolved accepted parent "
                        "units; the claim is retained as audit evidence but is not synthesized"
                    ),
                }
                rejected_by_id[rejection["rejection_id"]] = rejection
            row["within_source_synthesis_candidates"] = retained
        write_jsonl(plan_path, rows)
        rewritten += 1
    for repair_plan_path in sorted(DEPTH_REPAIR_PLAN_ROOT.glob("batch_*_missing.jsonl")):
        for row in load_jsonl(repair_plan_path):
            local_ids = {unit["local_unit_id"] for unit in row["accepted_units"]}
            for candidate in row["within_source_synthesis_candidates"]:
                parents = candidate.get("parent_local_unit_ids") or []
                if len(parents) >= 2 and set(parents).issubset(local_ids):
                    continue
                identity = {
                    "source_id": row["source_id"],
                    "title": candidate.get("title"),
                    "parents": parents,
                }
                rejection = {
                    **identity,
                    "rejection_id": "v2_synthesis_rejection_" + sha256_text(canonical_json(identity)),
                    "candidate": candidate,
                    "reason": (
                        "within-source synthesis requires at least two resolved accepted parent "
                        "units; the claim is retained as audit evidence but is not synthesized"
                    ),
                }
                rejected_by_id[rejection["rejection_id"]] = rejection
    write_jsonl(DEPTH_SYNTHESIS_REJECTIONS_PATH, rejected_by_id.values())
    print(
        f"sanitized synthesis candidates in {rewritten} plans; preserved {len(rejected_by_id)} rejections"
    )


def write_depth_generation_provenance(artifact_root: Path) -> None:
    """Bind each fresh Codex context, assignment, raw event log, and emitted plan."""
    records: list[dict[str, Any]] = []
    groups = (
        (
            "whole-source-depth",
            DEPTH_ASSIGNMENT_ROOT,
            DEPTH_PLAN_ROOT,
            artifact_root / "generation" / "depth",
            "batch_*.json",
        ),
        (
            "missing-source-depth-repair",
            DEPTH_REPAIR_ASSIGNMENT_ROOT,
            DEPTH_REPAIR_PLAN_ROOT,
            artifact_root / "generation" / "depth_repairs",
            "batch_*_missing.json",
        ),
    )
    prompt_path = V2_ROOT / "prompts" / "depth_segmentation.md"
    for stage, assignment_root, _, log_root, pattern in groups:
        for assignment_path in sorted(assignment_root.glob(pattern)):
            assignment = load_json(assignment_path)
            if assignment.get("model_visible_packet_sha256") is not None and len(
                assignment.get("sources") or []
            ) != 1:
                raise ValueError(
                    f"{assignment_path.name}: rerun depth receipt requires one source"
                )
            output_path = Path(assignment["output_path"])
            log_path = log_root / (assignment_path.stem + ".jsonl")
            if not output_path.is_file():
                continue
            thread_id = None
            completion_usage = None
            completion_event_present = False
            if log_path.is_file():
                for line in log_path.read_text(encoding="utf-8", errors="replace").splitlines():
                    try:
                        event = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if event.get("type") == "thread.started":
                        thread_id = event.get("thread_id")
                    if event.get("type") == "turn.completed":
                        completion_event_present = True
                        completion_usage = event.get("usage")
            context_name = assignment_path.stem.removesuffix("_missing")
            collaboration_task = (
                f"/root/depth_{context_name}_repair"
                if stage == "missing-source-depth-repair"
                else f"/root/depth_{context_name}"
            )
            identity = {
                "stage": stage,
                "assignment_sha256": sha256_file(assignment_path),
                "execution_context": thread_id or collaboration_task,
            }
            records.append(
                {
                    **identity,
                    "generation_id": "v2_generation_" + sha256_text(canonical_json(identity)),
                    "corpus_release_id": V2_RELEASE_ID,
                    "teacher": "OpenAI Codex",
                    "model": "gpt-5.6-sol",
                    "reasoning_effort": "xhigh",
                    "client": "codex-cli 0.148.0" if log_path.is_file() else "codex-collaboration-agent",
                    "fresh_isolated_context": True,
                    "invocation_mode": (
                        "codex exec --ephemeral --sandbox workspace-write"
                        if log_path.is_file()
                        else "fresh no-history collaboration task"
                    ),
                    "agent_task_path": None if log_path.is_file() else collaboration_task,
                    "working_directory": "/workspace/mathia-issue42",
                    "prompt_path": prompt_path.relative_to(HERE).as_posix(),
                    "prompt_sha256": sha256_file(prompt_path),
                    "assignment_path": assignment_path.relative_to(HERE).as_posix(),
                    "model_visible_packet_sha256": model_visible_packet_sha256(assignment),
                    "assigned_source_ids": [source["source_id"] for source in assignment["sources"]],
                    "output_path": output_path.relative_to(HERE).as_posix(),
                    "output_sha256": sha256_file(output_path),
                    "output_records": len(load_jsonl(output_path)),
                    "external_event_log_relpath": (
                        log_path.relative_to(artifact_root).as_posix() if log_path.is_file() else None
                    ),
                    "external_event_log_sha256": sha256_file(log_path) if log_path.is_file() else None,
                    "completion_event_present": completion_event_present,
                    "usage": completion_usage,
                    "postprocessing": (
                        "base plans may be deterministically reordered, receive separately logged "
                        "missing-source repair records, exclude quarantined acquisition mismatches, "
                        "and move malformed synthesis candidates to the rejection ledger"
                    ),
                }
            )
    write_jsonl(DEPTH_GENERATION_PROVENANCE_PATH, records)
    print(f"wrote exact generation provenance for {len(records)} fresh depth contexts")


def _archive_orphaned_depth_lineage() -> None:
    """Preserve surviving bindings from depth work over a misidentified source."""
    inventory = {
        row["source_id"]: row for row in load_jsonl(DEPTH_INVENTORY_PATH)
    }
    old_units = load_jsonl(DEPTH_UNITS_PATH) if DEPTH_UNITS_PATH.is_file() else []
    stale_by_source: dict[str, list[dict[str, Any]]] = {}
    for unit in old_units:
        source = inventory.get(str(unit.get("source_id") or ""))
        if source is None or unit.get("source_normalized_sha256") != source.get(
            "normalized_sha256"
        ):
            stale_by_source.setdefault(str(unit.get("source_id") or ""), []).append(unit)
    if not stale_by_source:
        return
    acquisition = {
        row["source_id"]: row for row in load_jsonl(ACQUISITION_SEARCH_PATH)
    }
    generation = (
        load_jsonl(DEPTH_GENERATION_PROVENANCE_PATH)
        if DEPTH_GENERATION_PROVENANCE_PATH.is_file()
        else []
    )
    candidates = (
        load_jsonl(WITHIN_SYNTHESIS_CANDIDATES_PATH)
        if WITHIN_SYNTHESIS_CANDIDATES_PATH.is_file()
        else []
    )
    preserved = (
        load_jsonl(DEPTH_IDENTITY_QUARANTINE_PATH)
        if DEPTH_IDENTITY_QUARANTINE_PATH.is_file()
        else []
    )
    existing = {
        (row.get("source_id"), row.get("quarantined_normalized_sha256"))
        for row in preserved
    }
    for source_id, units in sorted(stale_by_source.items()):
        stale_hashes = {str(unit.get("source_normalized_sha256") or "") for unit in units}
        if len(stale_hashes) != 1:
            raise ValueError(f"{source_id}: stale depth units span multiple source hashes")
        stale_hash = next(iter(stale_hashes))
        if (source_id, stale_hash) in existing:
            continue
        source = inventory.get(source_id) or {}
        row = acquisition.get(source_id) or {}
        preserved.append(
            {
                "source_id": source_id,
                "quarantined_normalized_sha256": stale_hash,
                "replacement_normalized_sha256": source.get("normalized_sha256"),
                "reason": (row.get("identity_audit") or {}).get("reason")
                or "normalized source identity changed after acquisition audit",
                "original_depth_generation_bindings": [
                    record
                    for record in generation
                    if source_id in (record.get("assigned_source_ids") or [])
                ],
                "surviving_materialized_unit_records": units,
                "surviving_within_source_candidate_records": [
                    candidate
                    for candidate in candidates
                    if candidate.get("source_id") == source_id
                ],
                "recovery_note": (
                    "The original batch plan row was deterministically removed when the source "
                    "was requeued. Its recorded batch hash, accepted unit metadata/artifact "
                    "hashes, synthesis candidates, and downstream raw analyses remain preserved; "
                    "the removed plan prose and coverage reasons are not reconstructed."
                ),
            }
        )
    write_jsonl(DEPTH_IDENTITY_QUARANTINE_PATH, preserved)
    print(
        f"preserved stale depth lineage for {len(stale_by_source)} identity-repaired sources"
    )


def _restore_archived_audit_parent_units(
    artifact_root: Path,
    assignments: Mapping[str, Mapping[str, Any]],
) -> int:
    """Keep archived audit packets bound to their original external unit bytes."""
    archived_units_path = (
        ISOLATION_ARCHIVE_ROOT
        / "non_authoritative/artifacts/depth/units.jsonl"
    )
    archived_assignment_root = (
        ISOLATION_ARCHIVE_ROOT
        / "reconciliation/artifacts/audit/assignments"
    )
    if not archived_units_path.is_file() or not archived_assignment_root.is_dir():
        return 0
    archived_units = {
        str(row["unit_artifact_relpath"]): row
        for row in load_jsonl(archived_units_path)
    }
    required: dict[str, tuple[str, int]] = {}
    for assignment_path in sorted(archived_assignment_root.glob("*.json")):
        for item in load_json(assignment_path).get("items") or []:
            for parent in item.get("parent_sources") or []:
                parent_path = Path(str(parent.get("content_abspath") or ""))
                try:
                    relpath = parent_path.resolve().relative_to(
                        artifact_root.resolve()
                    ).as_posix()
                except ValueError:
                    continue
                expected = (
                    str(parent.get("artifact_sha256") or ""),
                    int(parent.get("artifact_bytes") or 0),
                )
                prior = required.get(relpath)
                if prior is not None and prior != expected:
                    raise ValueError(
                        f"archived audit parents disagree about external artifact: {relpath}"
                    )
                required[relpath] = expected
    restored = 0
    for relpath, (expected_sha256, expected_bytes) in sorted(required.items()):
        path = artifact_root / relpath
        if (
            path.is_file()
            and sha256_file(path) == expected_sha256
            and path.stat().st_size == expected_bytes
        ):
            continue
        archived_unit = archived_units.get(relpath)
        if archived_unit is None:
            raise ValueError(f"archived audit parent lacks depth-unit lineage: {relpath}")
        source_id = str(archived_unit["source_id"])
        source = assignments.get(source_id)
        if source is None or source.get("normalized_sha256") != archived_unit.get(
            "source_normalized_sha256"
        ):
            raise ValueError(
                f"cannot reconstruct archived audit parent from exact source: {relpath}"
            )
        source_path = Path(str(source["normalized_abspath"]))
        if sha256_file(source_path) != source["normalized_sha256"]:
            raise ValueError(f"normalized source drift while restoring {relpath}")
        lines = source_path.read_text(
            encoding="utf-8", errors="replace"
        ).splitlines()
        start, end = int(archived_unit["line_start"]), int(archived_unit["line_end"])
        content = "\n".join(lines[start - 1 : end]) + "\n"
        encoded = content.encode("utf-8")
        if hashlib.sha256(encoded).hexdigest() != expected_sha256 or len(
            encoded
        ) != expected_bytes:
            raise ValueError(f"reconstructed archived audit parent differs: {relpath}")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        restored += 1
    return restored


def materialize_depth_units(artifact_root: Path) -> None:
    errors = validate_depth_plans(require_complete=True)
    if errors:
        raise ValueError("cannot materialize invalid depth plans:\n" + "\n".join(errors))
    _archive_orphaned_depth_lineage()
    assignments: dict[str, dict[str, Any]] = {}
    plan_by_source: dict[str, dict[str, Any]] = {}
    for assignment_path in sorted(DEPTH_ASSIGNMENT_ROOT.glob("batch_*.json")):
        assignment = load_json(assignment_path)
        for source in assignment["sources"]:
            assignments[source["source_id"]] = source
        for plan in load_jsonl(Path(assignment["output_path"])):
            plan_by_source[plan["source_id"]] = plan
    restored = _restore_archived_audit_parent_units(artifact_root, assignments)
    v1_unit_ids = {unit["unit_id"] for unit in load_jsonl(V1_ROOT / "units.jsonl")}
    unit_root = artifact_root / "depth" / "units"
    unit_root.mkdir(parents=True, exist_ok=True)
    records: list[dict[str, Any]] = []
    for source_id in [row["source_id"] for row in load_jsonl(DEPTH_INVENTORY_PATH)]:
        source = assignments[source_id]
        lines = Path(source["normalized_abspath"]).read_text(
            encoding="utf-8", errors="replace"
        ).splitlines()
        for unit in plan_by_source[source_id]["accepted_units"]:
            unit_id = unit["local_unit_id"]
            if unit_id in v1_unit_ids:
                continue
            start, end = int(unit["line_start"]), int(unit["line_end"])
            content = "\n".join(lines[start - 1 : end]) + "\n"
            encoded = content.encode("utf-8")
            unit_sha256 = hashlib.sha256(encoded).hexdigest()
            relpath = Path("depth") / "units" / f"{unit_id}.txt"
            path = artifact_root / relpath
            if path.is_file() and sha256_file(path) != unit_sha256:
                relpath = (
                    Path("depth")
                    / "units"
                    / f"{unit_id}_{unit_sha256[:12]}.txt"
                )
                path = artifact_root / relpath
            if path.is_file() and sha256_file(path) != unit_sha256:
                raise ValueError(f"depth-unit artifact collision: {relpath}")
            if not path.is_file():
                path.write_text(content, encoding="utf-8")
            pages = [int(value) for value in re.findall(r"<!-- source-page: (\d+) -->", content)]
            records.append(
                {
                    "unit_id": unit_id,
                    "source_id": source_id,
                    "parent_release_id": V1_RELEASE_ID,
                    "lineage": "v2-new-or-deeper-source-unit",
                    "source_normalized_sha256": source["normalized_sha256"],
                    "source_span_kind": "exact-normalized-line-slice",
                    "line_start": start,
                    "line_end": end,
                    "unit_type": unit["unit_type"],
                    "title": unit["title"],
                    "selection_reason": unit["why_material"],
                    "context_note": unit["context_note"],
                    "representation_dependency": unit["representation_dependency"],
                    "segmentation_decision": "accepted",
                    "segmentation_provenance": "v2-fresh-context-whole-source-depth-review",
                    "storage": "external-local-not-git",
                    "artifact_store": "riemann-corpus-v2",
                    "unit_artifact_relpath": relpath.as_posix(),
                    "unit_sha256": unit_sha256,
                    "unit_bytes": len(encoded),
                    "source_page_markers_inside_unit": pages,
                }
            )
    write_jsonl(DEPTH_UNITS_PATH, records)
    print(
        f"materialized {len(records)} new/deeper unit spans from {len(plan_by_source)} "
        f"sources; restored {restored} archived audit parent artifacts"
    )


def validate_depth_units(artifact_root: Path, require_artifacts: bool) -> list[str]:
    errors: list[str] = []
    inventory = {row["source_id"]: row for row in load_jsonl(DEPTH_INVENTORY_PATH)}
    v1_ids = {row["unit_id"] for row in load_jsonl(V1_ROOT / "units.jsonl")}
    plan_by_source = {
        row["source_id"]: row
        for path in sorted(DEPTH_PLAN_ROOT.glob("batch_*.jsonl"))
        for row in load_jsonl(path)
    }
    expected: list[str] = []
    for source in load_jsonl(DEPTH_INVENTORY_PATH):
        source_id = source["source_id"]
        plan = plan_by_source.get(source_id)
        if plan is not None:
            expected.extend(
                row["local_unit_id"] for row in plan["accepted_units"] if row["local_unit_id"] not in v1_ids
            )
    units = load_jsonl(DEPTH_UNITS_PATH)
    actual = [row.get("unit_id") for row in units]
    if actual != expected:
        errors.append("materialized depth-unit order/coverage differs from accepted depth plans")
    if len(actual) != len(set(actual)):
        errors.append("materialized depth-unit IDs are not unique")
    for unit in units:
        source = inventory.get(unit.get("source_id"))
        if source is None or unit.get("source_normalized_sha256") != source.get("normalized_sha256"):
            errors.append(f"{unit.get('unit_id')}: normalized source lineage mismatch")
            continue
        if not require_artifacts:
            continue
        path = artifact_root / str(unit.get("unit_artifact_relpath") or "")
        if not path.is_file():
            errors.append(f"{unit.get('unit_id')}: external unit artifact missing")
            continue
        content = path.read_text(encoding="utf-8")
        if sha256_file(path) != unit.get("unit_sha256"):
            errors.append(f"{unit.get('unit_id')}: external unit hash mismatch")
        if len(content.encode("utf-8")) != unit.get("unit_bytes"):
            errors.append(f"{unit.get('unit_id')}: external unit byte count mismatch")
        source_root = (
            pipeline.DEFAULT_ARTIFACT_ROOT
            if source["artifact_store"] == "riemann-corpus-v0"
            else artifact_root
        )
        source_path = source_root / source["normalized_relpath"]
        lines = source_path.read_text(encoding="utf-8", errors="replace").splitlines()
        expected_content = "\n".join(
            lines[int(unit["line_start"]) - 1 : int(unit["line_end"])]
        ) + "\n"
        if content != expected_content:
            errors.append(f"{unit.get('unit_id')}: external unit is not the exact logical-line slice")
    return errors


def _depth_batch_by_source() -> dict[str, str]:
    result: dict[str, str] = {}
    for path in sorted(DEPTH_ASSIGNMENT_ROOT.glob("batch_*.json")):
        for source in load_json(path)["sources"]:
            source_id = str(source["source_id"])
            if source_id in result:
                raise ValueError(f"{source_id}: assigned to more than one depth batch")
            result[source_id] = path.stem
    return result


def _depth_plan_by_source() -> dict[str, dict[str, Any]]:
    plans: dict[str, dict[str, Any]] = {}
    for path in sorted(DEPTH_PLAN_ROOT.glob("batch_*.jsonl")):
        for plan in load_jsonl(path):
            source_id = str(plan["source_id"])
            if source_id in plans:
                raise ValueError(f"{source_id}: occurs in more than one depth plan")
            plans[source_id] = plan
    return plans


def _normalized_source_path(source: Mapping[str, Any], artifact_root: Path) -> Path:
    root = (
        pipeline.DEFAULT_ARTIFACT_ROOT
        if source.get("artifact_store") == "riemann-corpus-v0"
        else artifact_root
    )
    return root / str(source["normalized_relpath"])


def _dossier_payload(
    source: Mapping[str, Any], plan: Mapping[str, Any]
) -> dict[str, Any]:
    units = list(plan.get("accepted_units") or [])
    extraction_risks = [
        segment
        for segment in plan.get("coverage_segments") or []
        if segment.get("disposition") in {"extraction-defective", "supporting-context"}
    ]
    return {
        "dossier_version": "riemann-v2-source-dossier-v1",
        "cache_role": "non-authoritative-execution-cache",
        "authority_note": (
            "This compact dossier routes work but is neither a trainable object nor mathematical "
            "authority; every claim must resolve to the exact normalized source/unit span."
        ),
        "source_id": source["source_id"],
        "source_identity": {
            key: source.get(key)
            for key in (
                "title",
                "authors",
                "year",
                "source_type",
                "viewpoint_tags",
                "artifact_store",
                "normalized_relpath",
                "normalized_sha256",
                "normalized_bytes",
                "line_count",
                "normalized_page_count",
            )
        },
        "section_argument_map": list(plan.get("sections_inspected") or []),
        "notation_and_main_objects_policy": (
            "Notation is intentionally not reconstructed mechanically; use the exact unit and "
            "nearby source context. Unit titles/types provide routing hints only."
        ),
        "result_and_mechanism_map": [
            {
                "unit_id": unit["local_unit_id"],
                "unit_type": unit["unit_type"],
                "title": unit["title"],
                "line_start": unit["line_start"],
                "line_end": unit["line_end"],
                "why_material": unit["why_material"],
            }
            for unit in units
        ],
        "dependency_context_and_representation_map": [
            {
                "unit_id": unit["local_unit_id"],
                "context_note": unit["context_note"],
                "representation_dependency": unit["representation_dependency"],
            }
            for unit in units
        ],
        "within_source_synthesis_map": list(
            plan.get("within_source_synthesis_candidates") or []
        ),
        "extraction_quality": {
            "confidence": source.get("extraction_confidence"),
            "warnings": list(source.get("extraction_warnings") or []),
            "risk_spans": extraction_risks,
        },
        "limitations_and_stop": {
            "remaining_meaningful_material": list(
                plan.get("remaining_meaningful_material") or []
            ),
            "within_source_saturation": plan.get("within_source_saturation"),
            "stop_reason": plan.get("stop_reason"),
        },
    }


def write_source_dossiers() -> None:
    """Materialize one deterministic routing dossier from each validated depth plan."""
    depth_errors = validate_depth_plans(require_complete=True)
    if depth_errors:
        raise ValueError("cannot write dossiers from invalid depth plans:\n" + "\n".join(depth_errors))
    inventory = load_jsonl(DEPTH_INVENTORY_PATH)
    plans = _depth_plan_by_source()
    records: list[dict[str, Any]] = []
    for source in inventory:
        payload = _dossier_payload(source, plans[source["source_id"]])
        identity = {
            "source_id": source["source_id"],
            "normalized_sha256": source["normalized_sha256"],
            "payload": payload,
        }
        records.append(
            {
                "dossier_id": "riemann_v2_dossier_" + sha256_text(canonical_json(identity)),
                "dossier_sha256": sha256_text(canonical_json(payload)),
                **payload,
            }
        )
    write_jsonl(SOURCE_DOSSIERS_PATH, records)
    print(f"wrote {len(records)} deterministic non-authoritative source dossiers")


def _safe_handoff_relpath(value: Any) -> Path:
    text = str(value or "")
    path = Path(text)
    if not text or path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        raise ValueError(f"unsafe handoff-relative path: {text!r}")
    return path


def _manifest_handoff_relpath(value: Any, handoff_id: str) -> Path:
    """Resolve a producer path without trusting its detachable absolute root."""
    path = Path(str(value or ""))
    if path.is_absolute():
        matching = [index for index, part in enumerate(path.parts) if part == handoff_id]
        if len(matching) != 1 or matching[0] + 1 >= len(path.parts):
            raise ValueError(f"manifest path is not rooted in {handoff_id}: {path}")
        path = Path(*path.parts[matching[0] + 1 :])
    return _safe_handoff_relpath(path.as_posix())


def _validate_openalex_handoff_bundle(
    bundle_root: Path,
    handoff_id: str,
    expected_stream: str,
) -> dict[str, Any]:
    """Validate one immutable producer bundle without opening mathematical text."""
    spec = OPENALEX_HANDOFF_SPECS.get(handoff_id)
    if spec is None or spec["stream"] != expected_stream:
        raise ValueError(f"unsupported #46 handoff/stream: {handoff_id}/{expected_stream}")
    if not bundle_root.is_dir() or bundle_root.is_symlink():
        raise ValueError(f"handoff root is missing or symlinked: {bundle_root}")
    for path in bundle_root.rglob("*"):
        if path.is_symlink():
            raise ValueError(f"handoff contains a symlink: {path}")
    freeze_path = bundle_root / "freeze.json"
    manifest_path = bundle_root / "manifest.jsonl"
    if not freeze_path.is_file() or not manifest_path.is_file():
        raise ValueError(f"{handoff_id}: freeze.json or manifest.jsonl is missing")
    freeze = load_json(freeze_path)
    required_freeze = {
        "consumer_contract",
        "files",
        "freeze_id",
        "frozen_at",
        "handoff_version",
        "immutable",
        "manifest_sha256",
        "pipeline_version",
        "source_count",
        "stream",
    }
    if not required_freeze.issubset(freeze):
        raise ValueError(f"{handoff_id}: incomplete freeze schema")
    if (
        freeze.get("immutable") is not True
        or freeze.get("handoff_version") != handoff_id
        or freeze.get("stream") != expected_stream
        or freeze.get("freeze_id") != spec["freeze_id"]
    ):
        raise ValueError(f"{handoff_id}: immutable identity/stream mismatch")
    if not isinstance(freeze.get("source_count"), int) or freeze["source_count"] < 1:
        raise ValueError(f"{handoff_id}: invalid source count")
    descriptors: dict[str, dict[str, Any]] = {}
    for descriptor in freeze.get("files") or []:
        if not isinstance(descriptor, dict) or not {"path", "sha256", "bytes"}.issubset(
            descriptor
        ):
            raise ValueError(f"{handoff_id}: malformed file descriptor")
        relative = _safe_handoff_relpath(descriptor["path"]).as_posix()
        if relative == "freeze.json" or relative in descriptors:
            raise ValueError(f"{handoff_id}: duplicate or recursive freeze descriptor: {relative}")
        if not re.fullmatch(r"[0-9a-f]{64}", str(descriptor.get("sha256") or "")):
            raise ValueError(f"{handoff_id}: invalid descriptor SHA-256: {relative}")
        if not isinstance(descriptor.get("bytes"), int) or descriptor["bytes"] < 0:
            raise ValueError(f"{handoff_id}: invalid descriptor byte count: {relative}")
        descriptors[relative] = dict(descriptor)
    actual_files = {
        path.relative_to(bundle_root).as_posix()
        for path in bundle_root.rglob("*")
        if path.is_file()
    }
    if actual_files != {"freeze.json", *descriptors}:
        raise ValueError(f"{handoff_id}: frozen descriptor coverage differs from bundle files")
    for relative, descriptor in descriptors.items():
        path = bundle_root / relative
        if path.stat().st_size != descriptor["bytes"] or sha256_file(path) != descriptor["sha256"]:
            raise ValueError(f"{handoff_id}: frozen file drift: {relative}")
    manifest_descriptor = descriptors.get("manifest.jsonl")
    if (
        manifest_descriptor is None
        or freeze.get("manifest_sha256") != manifest_descriptor["sha256"]
        or sha256_file(manifest_path) != freeze.get("manifest_sha256")
    ):
        raise ValueError(f"{handoff_id}: manifest binding mismatch")
    rows = load_jsonl(manifest_path)
    if len(rows) != freeze["source_count"]:
        raise ValueError(f"{handoff_id}: manifest/source-count mismatch")
    required_row = {
        "source_id",
        "handoff_version",
        "openalex_id",
        "raw_path",
        "raw_sha256",
        "raw_bytes",
        "normalized_path",
        "normalized_sha256",
        "normalized_bytes",
    }
    source_ids: list[str] = []
    work_ids: list[str] = []
    declared_artifacts: set[str] = set()
    for row in rows:
        if not required_row.issubset(row) or row.get("handoff_version") != handoff_id:
            raise ValueError(f"{handoff_id}: malformed manifest row")
        source_id = str(row.get("source_id") or "")
        work_id = _canonical_openalex_work_id(row)
        if not source_id or not work_id:
            raise ValueError(f"{handoff_id}: source/OpenAlex identity is missing")
        source_ids.append(source_id)
        work_ids.append(work_id)
        for prefix in ("raw", "normalized"):
            relative = _manifest_handoff_relpath(row[f"{prefix}_path"], handoff_id)
            if relative.parts[0] != prefix:
                raise ValueError(f"{handoff_id}/{source_id}: misplaced {prefix} artifact")
            relative_text = relative.as_posix()
            descriptor = descriptors.get(relative_text)
            if descriptor is None:
                raise ValueError(f"{handoff_id}/{source_id}: undeclared {prefix} artifact")
            if (
                descriptor["sha256"] != row[f"{prefix}_sha256"]
                or descriptor["bytes"] != row[f"{prefix}_bytes"]
            ):
                raise ValueError(f"{handoff_id}/{source_id}: {prefix} manifest drift")
            declared_artifacts.add(relative_text)
    if len(source_ids) != len(set(source_ids)) or len(work_ids) != len(set(work_ids)):
        raise ValueError(f"{handoff_id}: duplicate source/OpenAlex identity")
    if declared_artifacts != set(descriptors) - {"manifest.jsonl"}:
        raise ValueError(f"{handoff_id}: manifest does not bind every frozen source artifact")
    return {
        "handoff_id": handoff_id,
        "stream": expected_stream,
        "root": bundle_root,
        "freeze": freeze,
        "freeze_path": freeze_path,
        "freeze_sha256": sha256_file(freeze_path),
        "manifest_path": manifest_path,
        "manifest_sha256": sha256_file(manifest_path),
        "rows": rows,
        "descriptors": descriptors,
    }


def _copy_verified_handoff(
    source_root: Path,
    destination_parent: Path,
    handoff_id: str,
    expected_stream: str,
) -> dict[str, Any]:
    """Copy through a validated staging directory, never overwriting drift."""
    source = _validate_openalex_handoff_bundle(source_root, handoff_id, expected_stream)
    destination_parent.mkdir(parents=True, exist_ok=True)
    destination = destination_parent / handoff_id
    if destination.exists():
        existing = _validate_openalex_handoff_bundle(destination, handoff_id, expected_stream)
        if existing["freeze_sha256"] != source["freeze_sha256"]:
            raise ValueError(f"{handoff_id}: retained copy conflicts with published freeze")
        return existing
    staging = Path(
        tempfile.mkdtemp(prefix=f".{handoff_id}.staging-", dir=str(destination_parent))
    )
    try:
        for relative in ["freeze.json", *sorted(source["descriptors"])]:
            target = staging / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_root / relative, target)
        staged = _validate_openalex_handoff_bundle(staging, handoff_id, expected_stream)
        if staged["freeze_sha256"] != source["freeze_sha256"]:
            raise ValueError(f"{handoff_id}: staged handoff differs from source")
        try:
            staging.rename(destination)
        except FileExistsError:
            existing = _validate_openalex_handoff_bundle(
                destination, handoff_id, expected_stream
            )
            if existing["freeze_sha256"] != source["freeze_sha256"]:
                raise ValueError(f"{handoff_id}: concurrent retained copy conflicts")
            shutil.rmtree(staging)
        return _validate_openalex_handoff_bundle(destination, handoff_id, expected_stream)
    except BaseException:
        if staging.exists():
            shutil.rmtree(staging)
        raise


def _canonical_openalex_work_id(row: Mapping[str, Any]) -> str | None:
    candidates = [
        row.get("openalex_id"),
        (row.get("ids") or {}).get("openalex"),
        row.get("source_id"),
    ]
    for value in candidates:
        match = re.search(
            r"(?<![A-Za-z0-9])W(\d+)(?!\d)",
            str(value or ""),
            flags=re.IGNORECASE,
        )
        if match:
            return "openalex_w" + match.group(1)
    return None


def _canonical_doi(value: Any) -> str | None:
    text = str(value or "").strip().lower()
    for prefix in ("https://doi.org/", "http://doi.org/", "doi:"):
        if text.startswith(prefix):
            text = text[len(prefix) :]
    return text or None


def _canonical_url(value: Any) -> str | None:
    text = str(value or "").strip()
    if not text:
        return None
    parsed = urllib.parse.urlsplit(text)
    if not parsed.scheme or not parsed.netloc:
        return None
    path = re.sub(r"/+", "/", parsed.path).rstrip("/")
    return urllib.parse.urlunsplit(
        (parsed.scheme.lower(), parsed.netloc.lower(), path, parsed.query, "")
    )


def _handoff_source_identity_keys(row: Mapping[str, Any]) -> set[str]:
    keys: set[str] = set()
    work_id = _canonical_openalex_work_id(row)
    doi = _canonical_doi(row.get("doi") or (row.get("ids") or {}).get("doi"))
    if work_id:
        keys.add("openalex:" + work_id)
    if doi:
        keys.add("doi:" + doi)
    if row.get("normalized_sha256"):
        keys.add("normalized-sha256:" + str(row["normalized_sha256"]))
    if row.get("raw_sha256"):
        keys.add("artifact-sha256:" + str(row["raw_sha256"]))
    for field in ("canonical_url", "acquisition_url", "effective_url"):
        url = _canonical_url(row.get(field))
        if url:
            keys.add("url:" + url)
    for value in row.get("candidate_public_locations") or []:
        url = _canonical_url(value)
        if url:
            keys.add("url:" + url)
    return keys


def _existing_source_identity_keys(row: Mapping[str, Any]) -> set[str]:
    selected = row.get("selected_artifact") or {}
    keys = _handoff_source_identity_keys(
        {
            "source_id": row.get("source_id"),
            "openalex_id": (row.get("identifiers") or {}).get("openalex"),
            "doi": (row.get("identifiers") or {}).get("doi"),
            "normalized_sha256": selected.get("normalized_sha256")
            or row.get("normalized_sha256"),
            "raw_sha256": selected.get("artifact_sha256")
            or row.get("v1_artifact_sha256")
            or row.get("artifact_sha256"),
            "canonical_url": row.get("canonical_url"),
            "acquisition_url": row.get("acquisition_url"),
        }
    )
    return keys


def _classify_handoff_source(
    row: Mapping[str, Any],
    existing_rows: Iterable[Mapping[str, Any]],
    represented_source_ids: set[str],
    accepted_disposition: str,
) -> dict[str, Any]:
    keys = _handoff_source_identity_keys(row)
    matches = [
        str(existing["source_id"])
        for existing in existing_rows
        if keys & _existing_source_identity_keys(existing)
    ]
    matches = sorted(set(matches))
    if len(matches) > 1:
        disposition = "quarantined_ambiguous_source_identity"
        reason = "multiple existing source identities share a strong identifier"
    elif matches and matches[0] in represented_source_ids:
        disposition = "deduplicated_or_already_represented"
        reason = "the canonical work is already represented by a completed source-depth record"
    else:
        disposition = accepted_disposition
        reason = (
            "known source lacked represented usable depth and is recovered by the handoff"
            if matches
            else "no exact OpenAlex, DOI, normalized-hash, or canonical-URL identity match"
        )
    canonical_source_id = _canonical_openalex_work_id(row) or str(row["source_id"])
    return {
        "canonical_source_id": matches[0] if len(matches) == 1 else canonical_source_id,
        "handoff_source_id": str(row["source_id"]),
        "disposition": disposition,
        "reason": reason,
        "identity_keys": sorted(keys),
        "matched_source_ids": matches,
    }


def _handoff_source_ledger_record(
    bundle: Mapping[str, Any],
    row: Mapping[str, Any],
    classification: Mapping[str, Any],
) -> dict[str, Any]:
    handoff_id = str(bundle["handoff_id"])
    raw_relpath = _manifest_handoff_relpath(row["raw_path"], handoff_id).as_posix()
    normalized_relpath = _manifest_handoff_relpath(
        row["normalized_path"], handoff_id
    ).as_posix()
    payload = {
        "handoff_id": handoff_id,
        "stream": bundle["stream"],
        **dict(classification),
        "openalex_id": row.get("openalex_id"),
        "doi": row.get("doi"),
        "title": row.get("title"),
        "authors": row.get("authors") or [],
        "year": row.get("year"),
        "source_type": row.get("type"),
        "source_version": row.get("source_version"),
        "license": row.get("license"),
        "access_boundary": row.get("access_boundary"),
        "relevance": row.get("relevance") or {},
        "raw_relpath": raw_relpath,
        "raw_sha256": row["raw_sha256"],
        "raw_bytes": row["raw_bytes"],
        "normalized_relpath": normalized_relpath,
        "normalized_sha256": row["normalized_sha256"],
        "normalized_bytes": row["normalized_bytes"],
        "normalized_lines": row.get("normalized_lines"),
        "normalization": row.get("normalization") or {},
    }
    return {
        "source_disposition_id": "openalex_handoff_source_"
        + sha256_text(canonical_json(payload)),
        **payload,
    }


def _superseding_handoff_classifications(
    prior_bundle: Mapping[str, Any],
    authoritative_bundle: Mapping[str, Any],
    prior_ledger: Iterable[Mapping[str, Any]],
) -> dict[str, dict[str, Any]]:
    """Carry decisions only when a superseding row has the exact same source bytes."""
    prior_manifest = {str(row["source_id"]): row for row in prior_bundle["rows"]}
    authoritative_manifest = {
        str(row["source_id"]): row for row in authoritative_bundle["rows"]
    }
    prior_by_source = {
        str(row.get("handoff_source_id") or ""): row for row in prior_ledger
    }
    if (
        set(prior_manifest) != set(authoritative_manifest)
        or set(prior_by_source) != set(prior_manifest)
    ):
        raise ValueError("superseding handoff source/ledger coverage differs from v1")
    result: dict[str, dict[str, Any]] = {}
    for source_id, row in authoritative_manifest.items():
        prior_row = prior_manifest[source_id]
        ledger_row = prior_by_source[source_id]
        for field in ("raw_sha256", "raw_bytes", "normalized_sha256", "normalized_bytes"):
            if row.get(field) != prior_row.get(field) or row.get(field) != ledger_row.get(field):
                raise ValueError(
                    f"{source_id}: superseding handoff changed source bytes; "
                    "historical disposition cannot be rebound"
                )
        result[source_id] = {
            key: ledger_row[key]
            for key in (
                "canonical_source_id",
                "handoff_source_id",
                "disposition",
                "reason",
                "identity_keys",
                "matched_source_ids",
            )
        }
    return result


def _adapt_riemann_handoff_acquisition(
    bundle: Mapping[str, Any],
    artifact_root: Path,
    acquisition_path: Path | None = None,
    depth_inventory_path: Path | None = None,
    carried_classifications: Mapping[str, Mapping[str, Any]] | None = None,
) -> list[dict[str, Any]]:
    """Route unrepresented Riemann sources into the existing v2 depth path."""
    acquisition_path = acquisition_path or ACQUISITION_SEARCH_PATH
    depth_inventory_path = depth_inventory_path or DEPTH_INVENTORY_PATH
    existing = load_jsonl(acquisition_path) if acquisition_path.is_file() else []
    handoff_id = str(bundle["handoff_id"])
    # Recompute generated intake rows from the immutable bundle on every run.
    # This makes a later stronger exact-identity rule (for example a matching
    # retained raw artifact) remove a formerly accepted duplicate cleanly while
    # preserving pre-existing ledger sources recovered by the handoff.
    existing = [
        row
        for row in existing
        if not (
            row.get("lineage") == "issue-46-offline-handoff"
            and (row.get("issue_46_handoff_provenance") or {}).get("handoff_id")
            in OPENALEX_HANDOFF_SPECS
        )
    ]
    for row in existing:
        superseded_candidate_ids = {
            str(candidate.get("candidate_id") or "")
            for candidate in row.get("candidates") or []
            if candidate.get("route") == "issue-46-immutable-offline-handoff"
        }
        if superseded_candidate_ids:
            row["candidates"] = [
                candidate
                for candidate in row.get("candidates") or []
                if str(candidate.get("candidate_id") or "")
                not in superseded_candidate_ids
            ]
            row["attempts"] = [
                attempt
                for attempt in row.get("attempts") or []
                if str(attempt.get("candidate_id") or "")
                not in superseded_candidate_ids
            ]
            if row.get("selected_candidate_id") in superseded_candidate_ids:
                row["selected_candidate_id"] = None
                row["selected_artifact"] = None
        if (row.get("issue_46_handoff_provenance") or {}).get(
            "handoff_id"
        ) in OPENALEX_HANDOFF_SPECS:
            row.pop("issue_46_handoff_provenance", None)
    represented = (
        {row["source_id"] for row in load_jsonl(depth_inventory_path)}
        if depth_inventory_path.is_file()
        else set()
    )
    by_id = {str(row["source_id"]): row for row in existing}
    ledger: list[dict[str, Any]] = []
    bundle_root = Path(bundle["root"])
    try:
        bundle_relroot = bundle_root.relative_to(artifact_root)
    except ValueError as error:
        raise ValueError("retained Riemann handoff is outside its artifact root") from error
    for manifest_row in bundle["rows"]:
        classification = (
            dict(carried_classifications[str(manifest_row["source_id"])])
            if carried_classifications is not None
            else _classify_handoff_source(
                manifest_row,
                existing,
                represented,
                "accepted_for_riemann_v2_processing",
            )
        )
        ledger_row = _handoff_source_ledger_record(
            bundle, manifest_row, classification
        )
        ledger.append(ledger_row)
        if classification["disposition"] != "accepted_for_riemann_v2_processing":
            continue
        source_id = str(classification["canonical_source_id"])
        row = by_id.get(source_id)
        if row is None:
            row = {
                "source_id": source_id,
                "lineage": "issue-46-offline-handoff",
                "title": manifest_row.get("title"),
                "authors": manifest_row.get("authors") or [],
                "year": manifest_row.get("year"),
                "source_type": manifest_row.get("type"),
                "identifiers": {
                    key: value
                    for key, value in {
                        "openalex": manifest_row.get("openalex_id"),
                        "doi": manifest_row.get("doi"),
                    }.items()
                    if value
                },
                "canonical_url": manifest_row.get("openalex_id"),
                "viewpoint_tags": list(
                    (manifest_row.get("relevance") or {}).get("mechanism_tags") or []
                ),
                "v1_acquisition_status": None,
                "v1_usable": False,
                "v1_artifact_sha256": None,
                "v1_normalized_sha256": None,
                "search_priority": "issue-46-offline-handoff",
                "openalex_refresh_status": "issue-46-offline-handoff",
                "openalex_refreshed_at": bundle["freeze"].get("frozen_at"),
                "candidates": [],
                "attempts": [],
                "final_status": "v2-new-source-acquisition-pending",
                "selected_candidate_id": None,
                "selected_artifact": None,
                "remaining_search_notes": [],
            }
            existing.append(row)
            by_id[source_id] = row
        manifest_raw_relpath = _manifest_handoff_relpath(
            manifest_row["raw_path"], handoff_id
        )
        manifest_normalized_relpath = _manifest_handoff_relpath(
            manifest_row["normalized_path"], handoff_id
        )
        raw_relpath = (bundle_relroot / manifest_raw_relpath).as_posix()
        normalized_relpath = (bundle_relroot / manifest_normalized_relpath).as_posix()
        candidate_identity = {
            "source_id": source_id,
            "handoff_id": handoff_id,
            "normalized_sha256": manifest_row["normalized_sha256"],
        }
        candidate_id = "v2_candidate_" + sha256_text(canonical_json(candidate_identity))
        handoff_url = f"handoff://{handoff_id}/{manifest_normalized_relpath.as_posix()}"
        candidate = {
            "candidate_id": candidate_id,
            "route": "issue-46-immutable-offline-handoff",
            "route_rank": ROUTE_ORDER["issue-46-immutable-offline-handoff"],
            "url": handoff_url,
            "landing_page_url": manifest_row.get("openalex_id"),
            "host": None,
            "source_name": handoff_id,
            "source_type": "immutable-offline-handoff",
            "version": manifest_row.get("source_version"),
            "reported_license": manifest_row.get("license"),
            "access_boundary": manifest_row.get("access_boundary"),
            "license": manifest_row.get("license")
            or manifest_row.get("access_boundary")
            or "no redistribution grant inferred",
            "is_oa": bool((manifest_row.get("open_access") or {}).get("is_oa")),
            "version_relationship": (
                "Exact producer-frozen source version; identity with another edition is not assumed"
            ),
            "known_difference": (
                "A matching work may use a different normalized artifact; represented works are not reprocessed"
            ),
            "storage_boundary": "external retained artifact store; no source text committed to Git",
            "discovery_evidence": "immutable issue #46 offline handoff",
            "force_ocr": False,
        }
        candidates = {item["candidate_id"]: item for item in row.get("candidates") or []}
        candidates[candidate_id] = candidate
        row["candidates"] = sorted(
            candidates.values(), key=lambda item: (item["route_rank"], item["url"])
        )
        attempt_identity = {**candidate_identity, "candidate_id": candidate_id}
        attempt_id = "v2_attempt_" + sha256_text(canonical_json(attempt_identity))
        attempt = {
            "attempt_id": attempt_id,
            "round_id": "issue-46-offline-handoff",
            "candidate_id": candidate_id,
            "route": candidate["route"],
            "requested_url": handoff_url,
            "attempted_at": bundle["freeze"].get("frozen_at"),
            "result": "acquired-and-normalized",
            "status_class": "success",
            "network_request_performed": False,
            "artifact_store": "riemann-corpus-v2",
            "effective_url": manifest_row.get("effective_url"),
            "media_type": (manifest_row.get("normalization") or {}).get("media_type"),
            "artifact_relpath": raw_relpath,
            "artifact_sha256": manifest_row["raw_sha256"],
            "artifact_bytes": manifest_row["raw_bytes"],
            "normalized_relpath": normalized_relpath,
            "normalized_sha256": manifest_row["normalized_sha256"],
            "normalized_bytes": manifest_row["normalized_bytes"],
            "normalized_page_count": None,
            "warnings": list(
                (manifest_row.get("normalization") or {}).get("warnings") or []
            ),
        }
        attempts = {item["attempt_id"]: item for item in row.get("attempts") or []}
        attempts[attempt_id] = attempt
        row["attempts"] = list(attempts.values())
        row["issue_46_handoff_provenance"] = {
            "handoff_id": handoff_id,
            "freeze_id": bundle["freeze"]["freeze_id"],
            "handoff_source_id": manifest_row["source_id"],
        }
        _mark_selected_artifact(row, candidate, attempt)
    write_jsonl(acquisition_path, existing)
    return ledger


def _agnostic_handoff_source_ledger(
    bundle: Mapping[str, Any],
    carried_classifications: Mapping[str, Mapping[str, Any]] | None = None,
) -> list[dict[str, Any]]:
    existing = load_jsonl(AGNOSTIC_V1_ROOT / "source_inventory.jsonl")
    represented = {str(row["source_id"]) for row in existing}
    records_path = AGNOSTIC_V1_ROOT / "records.jsonl"
    if records_path.is_file():
        existing.extend(
            {
                "source_id": str(record["source_ids"][0]),
                "normalized_sha256": record.get("content_sha256"),
            }
            for record in load_jsonl(records_path)
            if record.get("object_role") == "source" and record.get("source_ids")
        )
    return [
        _handoff_source_ledger_record(
            bundle,
            row,
            (
                dict(carried_classifications[str(row["source_id"])])
                if carried_classifications is not None
                else _classify_handoff_source(
                    row,
                    existing,
                    represented,
                    "accepted_for_agnostic_supplement_analysis",
                )
            ),
        )
        for row in bundle["rows"]
    ]


def _bound_source_ledger(path: Path, records: list[dict[str, Any]]) -> dict[str, Any]:
    write_jsonl(path, records)
    return {
        "source_disposition_path": str(path),
        "source_disposition_sha256": sha256_file(path),
        "source_disposition_count": len(records),
        "source_disposition_counts": dict(
            sorted(Counter(row["disposition"] for row in records).items())
        ),
    }


def _replace_handoff_record(rows: list[dict[str, Any]], record: dict[str, Any]) -> None:
    rows[:] = [row for row in rows if row.get("handoff_id") != record["handoff_id"]]
    rows.append(record)
    rows.sort(key=lambda row: str(row.get("handoff_id") or ""))


def _openalex_handoff_disposition_ids(state: Mapping[str, Any]) -> list[str]:
    result: list[str] = []
    for stream in (state.get("streams") or {}).values():
        for key in (
            "consumed",
            "superseded",
            "deduplicated_or_already_represented",
            "rejected_or_quarantined",
            "deferred_with_blocker",
        ):
            result.extend(str(row.get("handoff_id")) for row in stream.get(key) or [])
    return result


def _openalex_finalization_allowed(state: Mapping[str, Any]) -> bool:
    cutoff = state.get("processing_cutoff") or {}
    published = [str(value) for value in cutoff.get("published_handoff_ids_through_cutoff") or []]
    if (
        cutoff.get("status") != "frozen"
        or not str(cutoff.get("cutoff_id") or "").strip()
        or Counter(published) != Counter(_openalex_handoff_disposition_ids(state))
    ):
        return False
    streams = state.get("streams") or {}
    if any(stream.get("deferred_with_blocker") for stream in streams.values()):
        return False
    return all(
        row.get("processing_status") == "complete"
        for stream in streams.values()
        for row in stream.get("consumed") or []
    )


def consume_openalex_handoffs(
    handoff_root: Path,
    riemann_artifact_root: Path,
    agnostic_artifact_root: Path,
) -> None:
    """Retain all four #46 bundles and consume only the route-corrected v2 streams."""
    if not OPENALEX_HANDOFF_STATE_PATH.is_file():
        write_openalex_handoff_state()
    state = load_json(OPENALEX_HANDOFF_STATE_PATH)
    retained: dict[str, dict[str, Any]] = {}
    for handoff_id, spec in OPENALEX_HANDOFF_SPECS.items():
        destination_root = (
            riemann_artifact_root
            if spec["stream"] == "riemann"
            else agnostic_artifact_root
        ) / "openalex_handoffs"
        retained[handoff_id] = _copy_verified_handoff(
            handoff_root / handoff_id,
            destination_root,
            handoff_id,
            str(spec["stream"]),
        )
    prior_ledgers = {
        "riemann": load_jsonl(RIEMANN_HANDOFF_SOURCE_LEDGER_PATH),
        "agnostic_mathia": load_jsonl(AGNOSTIC_HANDOFF_SOURCE_LEDGER_PATH),
    }
    carried_classifications: dict[str, dict[str, dict[str, Any]]] = {}
    for stream_name, authoritative_id in AUTHORITATIVE_OPENALEX_HANDOFF_IDS.items():
        authoritative_bundle = retained[authoritative_id]
        superseded_id = str(OPENALEX_HANDOFF_SPECS[authoritative_id]["supersedes"])
        superseded_bundle = retained[superseded_id]
        lineage = authoritative_bundle["freeze"].get("lineage") or {}
        if (
            lineage.get("supersedes") != superseded_id
            or lineage.get("reuses_verified_source_bytes") is not True
            or lineage.get("reason") != OPENALEX_HANDOFF_SUPERSESSION_REASON
        ):
            raise ValueError(f"{authoritative_id}: invalid v1-to-v2 supersession lineage")
        carried_classifications[stream_name] = _superseding_handoff_classifications(
            superseded_bundle,
            authoritative_bundle,
            prior_ledgers[stream_name],
        )
    riemann_bundle = retained[AUTHORITATIVE_OPENALEX_HANDOFF_IDS["riemann"]]
    riemann_ledger = _adapt_riemann_handoff_acquisition(
        riemann_bundle,
        riemann_artifact_root,
        carried_classifications=carried_classifications["riemann"],
    )
    agnostic_bundle = retained[AUTHORITATIVE_OPENALEX_HANDOFF_IDS["agnostic_mathia"]]
    agnostic_ledger = _agnostic_handoff_source_ledger(
        agnostic_bundle,
        carried_classifications=carried_classifications["agnostic_mathia"],
    )
    ledger_bindings = {
        "riemann": _bound_source_ledger(
            RIEMANN_HANDOFF_SOURCE_LEDGER_PATH, riemann_ledger
        ),
        "agnostic_mathia": _bound_source_ledger(
            AGNOSTIC_HANDOFF_SOURCE_LEDGER_PATH, agnostic_ledger
        ),
    }
    for handoff_id, bundle in retained.items():
        stream_name = str(bundle["stream"])
        stream = state["streams"][stream_name]
        spec = OPENALEX_HANDOFF_SPECS[handoff_id]
        record: dict[str, Any] = {
            "handoff_id": handoff_id,
            "handoff_version": bundle["freeze"]["handoff_version"],
            "stream": stream_name,
            "freeze_id": bundle["freeze"]["freeze_id"],
            "freeze_path": str(bundle["freeze_path"]),
            "freeze_sha256": bundle["freeze_sha256"],
            "manifest_path": str(bundle["manifest_path"]),
            "manifest_sha256": bundle["manifest_sha256"],
            "local_artifact_root": str(bundle["root"]),
            "processing_cutoff": (state.get("processing_cutoff") or {}).get("cutoff_id"),
        }
        for key in (
            "consumed",
            "superseded",
            "deduplicated_or_already_represented",
            "rejected_or_quarantined",
            "deferred_with_blocker",
        ):
            stream[key] = [
                row for row in stream.get(key) or [] if row.get("handoff_id") != handoff_id
            ]
        if spec["authoritative"]:
            record.update(
                {
                    "authority": "authoritative-consumed-stream",
                    "supersedes": spec["supersedes"],
                    "reuses_verified_source_bytes": True,
                    "processing_status": "copied_pending_analysis",
                    **ledger_bindings[stream_name],
                }
            )
            _replace_handoff_record(stream.setdefault("consumed", []), record)
            counts = record["source_disposition_counts"]
            metrics = stream["processing_metrics"]
            metrics["sources_received"] = record["source_disposition_count"]
            metrics["sources_deduplicated"] = counts.get(
                "deduplicated_or_already_represented", 0
            )
        else:
            record.update(
                {
                    "authority": "immutable-superseded-evidence",
                    "superseded_by": spec["superseded_by"],
                    "supersession_reason": OPENALEX_HANDOFF_SUPERSESSION_REASON,
                    "source_count": len(bundle["rows"]),
                    "source_bytes_verified_equal_to_successor": True,
                }
            )
            _replace_handoff_record(stream.setdefault("superseded", []), record)
    state["handoff_root_currently_nonempty"] = True
    state["finalization_allowed"] = _openalex_finalization_allowed(state)
    write_json(OPENALEX_HANDOFF_STATE_PATH, state)
    handoff_generated_at = max(
        str(bundle["freeze"].get("frozen_at") or "") for bundle in retained.values()
    )
    write_json(
        ACQUISITION_RETRY_STATE_PATH,
        _build_acquisition_retry_state(
            load_jsonl(ACQUISITION_SEARCH_PATH),
            DEFAULT_MAX_ROUTE_ATTEMPTS,
            generated_at=handoff_generated_at,
        ),
    )
    write_acquisition_summary(
        "issue-46-offline-handoff", generated_at=handoff_generated_at
    )
    print("verified and retained four offline #46 handoffs; v2 streams are authoritative")


def freeze_openalex_handoff_cutoff(
    handoff_ids: Iterable[str], observed_issue_url: str
) -> str:
    """Freeze the finite authorized set without discovering later directories."""
    requested = [str(value) for value in handoff_ids]
    expected = sorted(OPENALEX_HANDOFF_SPECS)
    if len(requested) != len(set(requested)) or sorted(requested) != expected:
        raise ValueError(f"#46 cutoff must contain exactly the authorized IDs: {expected}")
    if not str(observed_issue_url or "").strip():
        raise ValueError("#46 cutoff requires the authoritative observed issue URL")
    state = load_json(OPENALEX_HANDOFF_STATE_PATH)
    dispositioned = {
        row["handoff_id"]: row
        for stream in state["streams"].values()
        for key in (
            "consumed",
            "superseded",
            "deduplicated_or_already_represented",
            "rejected_or_quarantined",
            "deferred_with_blocker",
        )
        for row in stream.get(key) or []
    }
    if set(dispositioned) != set(expected):
        raise ValueError("all authorized handoffs must be retained before freezing the cutoff")
    bindings = [
        {
            "handoff_id": handoff_id,
            "stream": dispositioned[handoff_id]["stream"],
            "disposition": (
                "consumed"
                if OPENALEX_HANDOFF_SPECS[handoff_id]["authoritative"]
                else "superseded"
            ),
            "freeze_id": dispositioned[handoff_id]["freeze_id"],
            "freeze_sha256": dispositioned[handoff_id]["freeze_sha256"],
            "manifest_sha256": dispositioned[handoff_id]["manifest_sha256"],
        }
        for handoff_id in expected
    ]
    identity = {
        "scope_amendment": state["scope_amendment"],
        "observed_issue_46_through": observed_issue_url,
        "published_handoffs": bindings,
    }
    cutoff_id = "issue46_cutoff_" + sha256_text(canonical_json(identity))
    state["processing_cutoff"] = {
        "status": "frozen",
        "cutoff_id": cutoff_id,
        "published_handoff_ids_through_cutoff": expected,
        "published_handoff_bindings": bindings,
        "observed_issue_46_through": observed_issue_url,
    }
    for stream in state["streams"].values():
        for key in ("consumed", "superseded"):
            for row in stream.get(key) or []:
                row["processing_cutoff"] = cutoff_id
    state["finalization_allowed"] = _openalex_finalization_allowed(state)
    write_json(OPENALEX_HANDOFF_STATE_PATH, state)
    return cutoff_id


def _agnostic_parent_record() -> dict[str, Any]:
    """Return the exact #44 baseline and merged-#46 handoff binding for #42."""
    agnostic_freeze = load_json(AGNOSTIC_V1_ROOT / "freeze.json")
    if (
        agnostic_freeze.get("release_id") != AGNOSTIC_V1_RELEASE_ID
        or agnostic_freeze.get("freeze_id") != AGNOSTIC_V1_FREEZE_ID
    ):
        raise ValueError("merged #44/#45 agnostic baseline identity mismatch")
    review_freeze = load_json(AGNOSTIC_V1_ROOT / "review_content_freeze.json")
    if (
        review_freeze.get("release_id") != AGNOSTIC_V1_RELEASE_ID
        or review_freeze.get("review_content_freeze_id")
        != AGNOSTIC_V1_REVIEW_CONTENT_FREEZE_ID
    ):
        raise ValueError("merged #44/#45 reviewed-content freeze identity mismatch")
    handoff_freeze_path, handoff_manifest_path, *_ = (
        AGNOSTIC_HANDOFF_V2_REPO_EVIDENCE_PATHS
    )
    handoff_freeze = load_json(handoff_freeze_path)
    expected_handoff_freeze_id = OPENALEX_HANDOFF_SPECS[
        "agnostic_mathia_fulltext_v2"
    ]["freeze_id"]
    if (
        handoff_freeze.get("handoff_version") != "agnostic_mathia_fulltext_v2"
        or handoff_freeze.get("stream") != "agnostic_mathia"
        or handoff_freeze.get("freeze_id") != expected_handoff_freeze_id
        or handoff_freeze.get("manifest_sha256")
        != AGNOSTIC_HANDOFF_V2_MANIFEST_SHA256
        or handoff_freeze.get("source_count") != AGNOSTIC_HANDOFF_V2_SOURCE_COUNT
        or sha256_file(handoff_manifest_path) != AGNOSTIC_HANDOFF_V2_MANIFEST_SHA256
    ):
        raise ValueError("merged #46 agnostic handoff evidence identity mismatch")
    concrete_binding = {
        "controlling_comment": ISSUE42_CONCRETE_ARTIFACT_BINDING_COMMENT,
        "handoff_id": "agnostic_mathia_fulltext_v2",
        "handoff_freeze_id": expected_handoff_freeze_id,
        "handoff_manifest_sha256": AGNOSTIC_HANDOFF_V2_MANIFEST_SHA256,
        "source_pair_count": AGNOSTIC_HANDOFF_V2_SOURCE_COUNT,
        "frozen_local_artifact_root": (
            "/mnt/openalex/openalex/handoffs/agnostic_mathia_fulltext_v2"
        ),
        "preserved_artifact_root": str(
            DEFAULT_AGNOSTIC_SUPPLEMENT_ARTIFACT_ROOT
            / "openalex_handoffs/agnostic_mathia_fulltext_v2"
        ),
        "repo_evidence": [
            _file_descriptor(path, REPO_ROOT)
            for path in AGNOSTIC_HANDOFF_V2_REPO_EVIDENCE_PATHS
        ],
    }
    return {
        "contract_version": interchange.CONTRACT_VERSION,
        "supplement_release_id": AGNOSTIC_SUPPLEMENT_RELEASE_ID,
        "parent_release_id": AGNOSTIC_V1_RELEASE_ID,
        "parent_freeze_id": AGNOSTIC_V1_FREEZE_ID,
        "parent_review_content_freeze_id": AGNOSTIC_V1_REVIEW_CONTENT_FREEZE_ID,
        "parent_merge_commit": AGNOSTIC_V1_MERGE_COMMIT,
        "concrete_artifact_binding": concrete_binding,
        "lineage_policy": (
            "The merged #44 release is immutable. OpenAlex-derived agnostic records form a "
            "separate supplement and never enter the Riemann release namespace."
        ),
        "bindings": [
            _file_descriptor(path, REPO_ROOT) for path in AGNOSTIC_V1_BINDING_PATHS
        ],
    }


def write_openalex_handoff_state() -> None:
    """Bind the two immutable baselines and the currently finite #46 intake state."""
    parent = _agnostic_parent_record()
    write_json(AGNOSTIC_SUPPLEMENT_PARENT_PATH, parent)
    existing = (
        load_json(OPENALEX_HANDOFF_STATE_PATH)
        if OPENALEX_HANDOFF_STATE_PATH.is_file()
        else {}
    )
    streams = existing.get("streams") or {
        "riemann": {
            "parent_release_id": V1_RELEASE_ID,
            "consumed": [],
            "superseded": [],
            "deduplicated_or_already_represented": [],
            "rejected_or_quarantined": [],
            "deferred_with_blocker": [],
            "processing_metrics": {
                "sources_received": 0,
                "sources_deduplicated": 0,
                "sources_processed": 0,
                "semantic_units": 0,
                "derivatives_accepted": 0,
                "derivatives_quarantined": 0,
                "derivatives_rejected": 0,
            },
        },
        "agnostic_mathia": {
            "parent_release_id": AGNOSTIC_V1_RELEASE_ID,
            "supplement_release_id": AGNOSTIC_SUPPLEMENT_RELEASE_ID,
            "consumed": [],
            "superseded": [],
            "deduplicated_or_already_represented": [],
            "rejected_or_quarantined": [],
            "deferred_with_blocker": [],
            "processing_metrics": {
                "sources_received": 0,
                "sources_deduplicated": 0,
                "sources_useful": 0,
                "sources_rejected": 0,
                "semantic_units": 0,
                "derivatives_accepted": 0,
                "derivatives_quarantined": 0,
                "derivatives_rejected": 0,
                "reinforced_44_lenses": [],
                "materially_extended_44_lenses": [],
                "new_families": [],
                "saturation_probes_challenged": [],
                "saturation_probes_strengthened": [],
                "new_geometry_dependencies": [],
                "cross_domain_syntheses": [],
            },
        },
    }
    for stream in streams.values():
        stream.setdefault("superseded", [])
    cutoff = existing.get("processing_cutoff") or {
        "status": "open-awaiting-frozen-handoffs",
        "cutoff_id": None,
        "published_handoff_ids_through_cutoff": [],
        "observed_issue_46_through": (
            "https://github.com/murillo128/mathia/issues/46#issuecomment-5354357739"
        ),
    }
    handoff_root_nonempty = (
        DEFAULT_OPENALEX_HANDOFF_ROOT.is_dir()
        and next(DEFAULT_OPENALEX_HANDOFF_ROOT.iterdir(), None) is not None
    )
    state = {
        "state_version": "riemann-v2-dual-openalex-handoff-state-v2",
        "scope_amendment": (
            "https://github.com/murillo128/mathia/issues/42#issuecomment-5354363863"
        ),
        "concrete_artifact_binding": parent["concrete_artifact_binding"],
        "expected_local_handoff_root": str(DEFAULT_OPENALEX_HANDOFF_ROOT),
        "offline_only": True,
        "network_requests_performed_by_42_for_handoffs": 0,
        "handoff_root_currently_nonempty": handoff_root_nonempty,
        "processing_cutoff": cutoff,
        "immutable_baselines": {
            "riemann": {
                "release_id": V1_RELEASE_ID,
                "freeze_id": V1_FREEZE_ID,
            },
            "agnostic_mathia": {
                "release_id": AGNOSTIC_V1_RELEASE_ID,
                "freeze_id": AGNOSTIC_V1_FREEZE_ID,
                "review_content_freeze_id": AGNOSTIC_V1_REVIEW_CONTENT_FREEZE_ID,
                "merge_commit": AGNOSTIC_V1_MERGE_COMMIT,
            },
        },
        "streams": streams,
        "finalization_allowed": False,
    }
    state["finalization_allowed"] = _openalex_finalization_allowed(state)
    write_json(OPENALEX_HANDOFF_STATE_PATH, state)
    print("recorded separate offline #46 handoff streams and open finite cutoff")


def validate_openalex_handoff_state(require_frozen_cutoff: bool = False) -> list[str]:
    errors: list[str] = []
    if not OPENALEX_HANDOFF_STATE_PATH.is_file() or not AGNOSTIC_SUPPLEMENT_PARENT_PATH.is_file():
        return ["dual-stream #46 handoff state or agnostic supplement parent is missing"]
    try:
        expected_parent = _agnostic_parent_record()
    except ValueError as error:
        errors.append(str(error))
        expected_parent = None
    parent = load_json(AGNOSTIC_SUPPLEMENT_PARENT_PATH)
    if expected_parent is None or parent != expected_parent:
        errors.append("agnostic OpenAlex supplement parent binding mismatch")
    state = load_json(OPENALEX_HANDOFF_STATE_PATH)
    if state.get("state_version") != "riemann-v2-dual-openalex-handoff-state-v2":
        errors.append("unknown dual-stream handoff-state version")
    if state.get("scope_amendment") != (
        "https://github.com/murillo128/mathia/issues/42#issuecomment-5354363863"
    ):
        errors.append("dual-stream handoff state does not bind the controlling amendment")
    expected_concrete_binding = (
        expected_parent.get("concrete_artifact_binding") if expected_parent else None
    )
    if state.get("concrete_artifact_binding") != expected_concrete_binding:
        errors.append("dual-stream handoff state omits the concrete #44/#46 binding")
    if state.get("offline_only") is not True:
        errors.append("#42 handoff consumption is not marked offline-only")
    if state.get("network_requests_performed_by_42_for_handoffs") != 0:
        errors.append("#42 handoff consumption must remain offline")
    if set(state.get("streams") or {}) != {"riemann", "agnostic_mathia"}:
        errors.append("#46 handoff state must keep exactly two distinct streams")
    expected_baselines = {
        "riemann": {"release_id": V1_RELEASE_ID, "freeze_id": V1_FREEZE_ID},
        "agnostic_mathia": {
            "release_id": AGNOSTIC_V1_RELEASE_ID,
            "freeze_id": AGNOSTIC_V1_FREEZE_ID,
            "review_content_freeze_id": AGNOSTIC_V1_REVIEW_CONTENT_FREEZE_ID,
            "merge_commit": AGNOSTIC_V1_MERGE_COMMIT,
        },
    }
    if state.get("immutable_baselines") != expected_baselines:
        errors.append("dual-stream immutable baseline bindings mismatch")
    cutoff = state.get("processing_cutoff") or {}
    if require_frozen_cutoff and cutoff.get("status") != "frozen":
        errors.append("#46 finite consumption cutoff is not frozen")
    published_rows = [
        str(value) for value in cutoff.get("published_handoff_ids_through_cutoff") or []
    ]
    if len(published_rows) != len(set(published_rows)):
        errors.append("#46 cutoff publishes a handoff ID more than once")
    if cutoff.get("status") == "frozen" and sorted(published_rows) != sorted(
        OPENALEX_HANDOFF_SPECS
    ):
        errors.append("#46 frozen cutoff does not contain the exact authorized handoff IDs")
    if require_frozen_cutoff and not str(cutoff.get("cutoff_id") or "").strip():
        errors.append("#46 frozen consumption cutoff has no immutable cutoff ID")
    dispositions: list[str] = []
    required_consumed = {
        "handoff_id",
        "handoff_version",
        "stream",
        "freeze_id",
        "freeze_path",
        "freeze_sha256",
        "manifest_path",
        "manifest_sha256",
        "local_artifact_root",
        "processing_cutoff",
        "processing_status",
        "source_disposition_path",
        "source_disposition_sha256",
        "source_disposition_count",
        "source_disposition_counts",
        "authority",
        "supersedes",
        "reuses_verified_source_bytes",
    }
    required_superseded = {
        "handoff_id",
        "handoff_version",
        "stream",
        "freeze_id",
        "freeze_path",
        "freeze_sha256",
        "manifest_path",
        "manifest_sha256",
        "local_artifact_root",
        "processing_cutoff",
        "authority",
        "superseded_by",
        "supersession_reason",
        "source_count",
        "source_bytes_verified_equal_to_successor",
    }
    required_metrics = {
        "riemann": {
            "sources_received",
            "sources_deduplicated",
            "sources_processed",
            "semantic_units",
            "derivatives_accepted",
            "derivatives_quarantined",
            "derivatives_rejected",
        },
        "agnostic_mathia": {
            "sources_received",
            "sources_deduplicated",
            "sources_useful",
            "sources_rejected",
            "semantic_units",
            "derivatives_accepted",
            "derivatives_quarantined",
            "derivatives_rejected",
            "reinforced_44_lenses",
            "materially_extended_44_lenses",
            "new_families",
            "saturation_probes_challenged",
            "saturation_probes_strengthened",
            "new_geometry_dependencies",
            "cross_domain_syntheses",
        },
    }
    for stream_name, stream in (state.get("streams") or {}).items():
        if not required_metrics.get(stream_name, set()).issubset(
            (stream.get("processing_metrics") or {}).keys()
        ):
            errors.append(f"{stream_name}: required separate processing metrics are incomplete")
        for row in stream.get("consumed") or []:
            dispositions.append(str(row.get("handoff_id")))
            if not required_consumed.issubset(row):
                errors.append(f"{stream_name}: consumed handoff record is incomplete")
                continue
            if row.get("stream") != stream_name:
                errors.append(f"{stream_name}/{row['handoff_id']}: stream binding mismatch")
            if (
                row.get("handoff_id") != AUTHORITATIVE_OPENALEX_HANDOFF_IDS.get(stream_name)
                or row.get("authority") != "authoritative-consumed-stream"
                or row.get("supersedes")
                != OPENALEX_HANDOFF_SPECS.get(str(row.get("handoff_id")), {}).get(
                    "supersedes"
                )
                or row.get("reuses_verified_source_bytes") is not True
            ):
                errors.append(f"{stream_name}: consumed handoff is not the authoritative v2 stream")
            if row.get("processing_status") not in {"copied_pending_analysis", "complete"}:
                errors.append(
                    f"{stream_name}/{row['handoff_id']}: invalid processing status"
                )
            freeze_path = Path(str(row["freeze_path"]))
            manifest_path = Path(str(row["manifest_path"]))
            artifact_root = Path(str(row["local_artifact_root"]))
            ledger_path = Path(str(row["source_disposition_path"]))
            if freeze_path != artifact_root / "freeze.json":
                errors.append(f"{stream_name}/{row['handoff_id']}: freeze path is not retained-root local")
            if manifest_path != artifact_root / "manifest.jsonl":
                errors.append(f"{stream_name}/{row['handoff_id']}: manifest path is not retained-root local")
            if row.get("processing_cutoff") != cutoff.get("cutoff_id"):
                errors.append(f"{stream_name}/{row['handoff_id']}: processing-cutoff binding mismatch")
            if not freeze_path.is_file() or sha256_file(freeze_path) != row["freeze_sha256"]:
                errors.append(f"{stream_name}/{row['handoff_id']}: freeze missing or drifted")
            if not manifest_path.is_file() or sha256_file(manifest_path) != row["manifest_sha256"]:
                errors.append(f"{stream_name}/{row['handoff_id']}: manifest missing or drifted")
            if not artifact_root.is_dir():
                errors.append(f"{stream_name}/{row['handoff_id']}: preserved local artifact root missing")
                bundle = None
            else:
                try:
                    bundle = _validate_openalex_handoff_bundle(
                        artifact_root, str(row["handoff_id"]), stream_name
                    )
                    lineage = bundle["freeze"].get("lineage") or {}
                    if (
                        row.get("freeze_id") != bundle["freeze"].get("freeze_id")
                        or row.get("freeze_sha256") != bundle.get("freeze_sha256")
                        or row.get("manifest_sha256") != bundle.get("manifest_sha256")
                        or lineage.get("supersedes") != row.get("supersedes")
                        or lineage.get("reuses_verified_source_bytes") is not True
                        or lineage.get("reason") != OPENALEX_HANDOFF_SUPERSESSION_REASON
                    ):
                        errors.append(
                            f"{stream_name}/{row['handoff_id']}: authoritative freeze/state lineage mismatch"
                        )
                except ValueError as error:
                    bundle = None
                    errors.append(
                        f"{stream_name}/{row['handoff_id']}: retained bundle invalid: {error}"
                    )
            if (
                not ledger_path.is_file()
                or sha256_file(ledger_path) != row["source_disposition_sha256"]
            ):
                errors.append(
                    f"{stream_name}/{row['handoff_id']}: source-disposition ledger missing or drifted"
                )
                ledger = []
            else:
                ledger = load_jsonl(ledger_path)
                if len(ledger) != row["source_disposition_count"]:
                    errors.append(
                        f"{stream_name}/{row['handoff_id']}: source-disposition count mismatch"
                    )
                actual_counts = dict(
                    sorted(Counter(item.get("disposition") for item in ledger).items())
                )
                if actual_counts != row["source_disposition_counts"]:
                    errors.append(
                        f"{stream_name}/{row['handoff_id']}: source-disposition metrics mismatch"
                    )
                handoff_source_ids = [item.get("handoff_source_id") for item in ledger]
                if len(handoff_source_ids) != len(set(handoff_source_ids)):
                    errors.append(
                        f"{stream_name}/{row['handoff_id']}: duplicate source disposition"
                    )
                if bundle is not None and set(handoff_source_ids) != {
                    item["source_id"] for item in bundle["rows"]
                }:
                    errors.append(
                        f"{stream_name}/{row['handoff_id']}: source ledger does not cover manifest"
                    )
                if bundle is not None:
                    manifest_by_id = {
                        item["source_id"]: item for item in bundle["rows"]
                    }
                    for ledger_row in ledger:
                        manifest_row = manifest_by_id.get(
                            str(ledger_row.get("handoff_source_id") or "")
                        )
                        if manifest_row is None or any(
                            ledger_row.get(field) != manifest_row.get(field)
                            for field in (
                                "source_version",
                                "license",
                                "raw_sha256",
                                "normalized_sha256",
                            )
                        ) or ledger_row.get("handoff_id") != row.get("handoff_id"):
                            errors.append(
                                f"{stream_name}/{row['handoff_id']}: source ledger provenance differs from authoritative manifest"
                            )
                            break
            metrics = stream.get("processing_metrics") or {}
            if metrics.get("sources_received") != row["source_disposition_count"]:
                errors.append(f"{stream_name}: received-source metric differs from intake")
            if metrics.get("sources_deduplicated") != row[
                "source_disposition_counts"
            ].get("deduplicated_or_already_represented", 0):
                errors.append(f"{stream_name}: deduplicated-source metric differs from intake")
            if row.get("processing_status") == "complete":
                if stream_name == "riemann" and (
                    metrics.get("sources_processed", 0)
                    + metrics.get("sources_deduplicated", 0)
                    != metrics.get("sources_received", 0)
                ):
                    errors.append(
                        "riemann: complete handoff does not account for every source"
                    )
                if stream_name == "agnostic_mathia" and (
                    metrics.get("sources_useful", 0)
                    + metrics.get("sources_rejected", 0)
                    + metrics.get("sources_deduplicated", 0)
                    != metrics.get("sources_received", 0)
                ):
                    errors.append(
                        "agnostic_mathia: complete handoff does not account for every source"
                    )
        if len(stream.get("consumed") or []) != 1:
            errors.append(f"{stream_name}: exactly one authoritative v2 handoff must be consumed")
        superseded_rows = stream.get("superseded") or []
        for row in superseded_rows:
            dispositions.append(str(row.get("handoff_id")))
            if not required_superseded.issubset(row):
                errors.append(f"{stream_name}: superseded handoff record is incomplete")
                continue
            handoff_id = str(row.get("handoff_id") or "")
            spec = OPENALEX_HANDOFF_SPECS.get(handoff_id) or {}
            successor_id = str(row.get("superseded_by") or "")
            successor = next(
                (
                    item
                    for item in stream.get("consumed") or []
                    if item.get("handoff_id") == successor_id
                ),
                None,
            )
            if (
                row.get("stream") != stream_name
                or spec.get("authoritative") is not False
                or spec.get("superseded_by") != successor_id
                or row.get("authority") != "immutable-superseded-evidence"
                or row.get("supersession_reason") != OPENALEX_HANDOFF_SUPERSESSION_REASON
                or row.get("source_bytes_verified_equal_to_successor") is not True
                or successor is None
            ):
                errors.append(f"{stream_name}/{handoff_id}: invalid supersession authority/lineage")
                continue
            try:
                prior_bundle = _validate_openalex_handoff_bundle(
                    Path(str(row["local_artifact_root"])), handoff_id, stream_name
                )
                successor_bundle = _validate_openalex_handoff_bundle(
                    Path(str(successor["local_artifact_root"])), successor_id, stream_name
                )
                prior_rows = {item["source_id"]: item for item in prior_bundle["rows"]}
                successor_rows = {
                    item["source_id"]: item for item in successor_bundle["rows"]
                }
                if (
                    row.get("freeze_id") != prior_bundle["freeze"].get("freeze_id")
                    or row.get("freeze_sha256") != prior_bundle.get("freeze_sha256")
                    or row.get("manifest_sha256") != prior_bundle.get("manifest_sha256")
                    or row.get("processing_cutoff") != cutoff.get("cutoff_id")
                    or set(prior_rows) != set(successor_rows)
                    or row.get("source_count") != len(prior_rows)
                    or any(
                        prior_rows[source_id].get(field)
                        != successor_rows[source_id].get(field)
                        for source_id in prior_rows
                        for field in (
                            "raw_sha256",
                            "raw_bytes",
                            "normalized_sha256",
                            "normalized_bytes",
                        )
                    )
                ):
                    errors.append(f"{stream_name}/{handoff_id}: v1/v2 source-byte equivalence mismatch")
            except (OSError, ValueError, json.JSONDecodeError) as error:
                errors.append(f"{stream_name}/{handoff_id}: retained superseded bundle invalid: {error}")
        if len(superseded_rows) != 1:
            errors.append(f"{stream_name}: exactly one immutable v1 handoff must be superseded")
        for key in (
            "deduplicated_or_already_represented",
            "rejected_or_quarantined",
            "deferred_with_blocker",
        ):
            dispositions.extend(
                str(row.get("handoff_id")) for row in stream.get(key) or []
            )
    if require_frozen_cutoff and Counter(published_rows) != Counter(dispositions):
        errors.append("not every #46 handoff through the cutoff has exactly one disposition")
    if cutoff.get("status") == "frozen":
        dispositioned_by_id = {
            row.get("handoff_id"): (stream_name, key, row)
            for stream_name, stream in (state.get("streams") or {}).items()
            for key in ("consumed", "superseded")
            for row in stream.get(key) or []
        }
        if set(dispositioned_by_id) == set(published_rows):
            expected_bindings = [
                {
                    "handoff_id": handoff_id,
                    "stream": dispositioned_by_id[handoff_id][0],
                    "disposition": dispositioned_by_id[handoff_id][1],
                    "freeze_id": dispositioned_by_id[handoff_id][2].get("freeze_id"),
                    "freeze_sha256": dispositioned_by_id[handoff_id][2].get("freeze_sha256"),
                    "manifest_sha256": dispositioned_by_id[handoff_id][2].get(
                        "manifest_sha256"
                    ),
                }
                for handoff_id in sorted(published_rows)
            ]
            if cutoff.get("published_handoff_bindings") != expected_bindings:
                errors.append("#46 cutoff handoff bindings differ from retained bundles")
            cutoff_identity = {
                "scope_amendment": state.get("scope_amendment"),
                "observed_issue_46_through": cutoff.get("observed_issue_46_through"),
                "published_handoffs": expected_bindings,
            }
            expected_cutoff_id = "issue46_cutoff_" + sha256_text(
                canonical_json(cutoff_identity)
            )
            if cutoff.get("cutoff_id") != expected_cutoff_id:
                errors.append("#46 frozen cutoff identity mismatch")
    expected_finalization = _openalex_finalization_allowed(state)
    if state.get("finalization_allowed") != expected_finalization:
        errors.append("handoff finalization gate disagrees with cutoff state")
    if require_frozen_cutoff and not expected_finalization:
        errors.append("#46 handoff processing is incomplete despite the frozen cutoff")
    return errors


def write_execution_brief() -> None:
    """Write the compact stable context that replaces repeated issue-history reads."""
    parent = load_json(PARENT_PATH)
    handoff_state = load_json(OPENALEX_HANDOFF_STATE_PATH)
    riemann_handoff_ids = [
        row["handoff_id"] for row in handoff_state["streams"]["riemann"]["consumed"]
    ]
    agnostic_handoff_ids = [
        row["handoff_id"]
        for row in handoff_state["streams"]["agnostic_mathia"]["consumed"]
    ]
    riemann_handoff_text = ", ".join(riemann_handoff_ids) if riemann_handoff_ids else "none"
    agnostic_handoff_text = ", ".join(agnostic_handoff_ids) if agnostic_handoff_ids else "none"
    cutoff_status = handoff_state["processing_cutoff"]["status"]
    brief = f"""# Riemann–Mathia v2 execution brief

This is the compact run context for GitHub issue #42 v2. It implements the token/agent-compute policy at https://github.com/murillo128/mathia/issues/42#issuecomment-5354075669 and the dual-stream #46 amendment at https://github.com/murillo128/mathia/issues/42#issuecomment-5354363863.

## Fixed scope and lineage

- Corpus only: no training, Qwen/qwen-lean inference, GPU use, RL, weight merging, Lean work, or RH proof attempt.
- Parent: `{parent['parent_release_id']}` at freeze `{parent['parent_freeze_id']}`; PR #43/v1 is immutable.
- Second immutable baseline: `{AGNOSTIC_V1_RELEASE_ID}` at freeze `{AGNOSTIC_V1_FREEZE_ID}` from merged PR #45. It is a comparison parent for a separate agnostic OpenAlex supplement, never Riemann content.
- Reuse the unchanged `{interchange.CONTRACT_VERSION}` canonical interchange. V2 is additive and source linked.
- Consumed issue #46 Riemann handoff IDs: **{riemann_handoff_text}**.
- Consumed issue #46 agnostic Mathia handoff IDs: **{agnostic_handoff_text}**.
- The #46 processing cutoff is **{cutoff_status}**. #42 consumes only hash-bound local artifacts and performs no repeated acquisition or OpenAlex/API request.
- Future `riemann_fulltext_vN` batches continue Riemann v2. Future `agnostic_mathia_fulltext_vN` batches are deterministically deduplicated against #44 and can only enter `{AGNOSTIC_SUPPLEMENT_RELEASE_ID}`.

## Evidence and context protocol

- Deterministic code owns acquisition state, hashes, dedup/version checks, normalization diagnostics, exact spans, manifests, dossiers, batching, and validation.
- The source dossier is a routing cache, not mathematical authority or automatically trainable content.
- For unit analysis read only this brief, the frozen stage prompt, the exact unit span, its bounded nearby context, the assigned dossier fragment, and the explicitly named prior-stage record.
- Do not read the full issue history, whole source, unrelated batches, v1 teacher/critic outputs, or other agents' reasoning unless an explicit evidence correction requires it.
- Exact source text wins over dossier summaries. Keep spontaneous/directed outputs distinct. A critic must be fresh and isolated from teacher reasoning.

## Quality states and gates

- `candidate`: exact accepted depth unit awaiting interpretation.
- `accept_as_is`: source-grounded candidate requiring no model revision; deterministic finalization is allowed.
- `revise`: critic identified a bounded repair; revision sees exact span, compact candidate, and findings only.
- `reject`: unsupported/shallow candidate excluded from training; sampled rejects may enter QA.
- `quarantine`: corrupt, OCR/formula-unsafe, identity/context-defective, or isolation-compromised evidence; inspect at 100% where applicable.
- Synthesis begins from accepted linked interpretations/dossier relations and reopens only the exact supporting spans required to verify a proposed relation.
- The 28 #44 ecosystem families are retrieval and saturation lenses, not target labels or a permanent ontology. Source evidence may reinforce, challenge, or extend that map.

## Stop conditions

- Never stop a source because of an arbitrary unit quota; depth ends only after an exact whole-source partition and source-specific saturation account.
- Do not repeat frozen v1/v2 work unless evidence or execution context materially changed, and preserve the superseded artifact when it did.
- Stop network/OpenAlex work in this session; preserve the offline #46 boundary.
- Do not freeze the final release until a finite #46 cutoff records a disposition for every published Riemann and agnostic handoff through that cutoff.
- Stop an agent task on any source/hash/span mismatch, missing exact evidence, cross-batch context exposure, or schema/order failure.
- Optimize mathematical information per agent token, not minimum tokens; expand context only when the exact unit cannot be judged safely from the bounded packet.
"""
    EXECUTION_BRIEF_PATH.parent.mkdir(parents=True, exist_ok=True)
    EXECUTION_BRIEF_PATH.write_text(brief, encoding="utf-8")
    print("wrote compact issue #42 v2 execution brief")


def _stage_assignment_paths(stage: str) -> list[Path]:
    return sorted(ANALYSIS_ASSIGNMENT_ROOT.glob(f"{stage}_*.json"))


def _stage_batch_paths(stage: str) -> list[Path]:
    return sorted(ANALYSIS_BATCH_ROOT.glob(f"{stage}_*.jsonl"))


def _verified_analysis_output(
    stage: str, assignment_path: Path, assignment: Mapping[str, Any]
) -> bool:
    """Accept completion when canonical or incremental provenance binds exact bytes."""
    output_path = Path(str(assignment.get("output_path") or ""))
    if not output_path.is_file():
        return False
    relative = assignment_path.relative_to(V2_ROOT).as_posix()
    expected_packet = assignment.get("model_visible_packet_sha256")
    if expected_packet is not None and (
        expected_packet != model_visible_packet_sha256(assignment)
    ):
        return False
    if ANALYSIS_GENERATION_PROVENANCE_PATH.is_file():
        receipt = next(
            (
                row
                for row in load_jsonl(ANALYSIS_GENERATION_PROVENANCE_PATH)
                if row.get("stage") == stage
                and row.get("assignment_relpath") == relative
            ),
            None,
        )
        if receipt is not None and (
            receipt.get("assignment_sha256") == sha256_file(assignment_path)
            and receipt.get("raw_output_sha256") == sha256_file(output_path)
            and (
                expected_packet is None
                or receipt.get("model_visible_packet_sha256") == expected_packet
            )
        ):
            return True
    if not LEGACY_CONTEXT_LEDGER_PATH.is_file():
        return False
    repo_relative = assignment_path.relative_to(REPO_ROOT).as_posix()
    matches = [
        row
        for row in load_jsonl(LEGACY_CONTEXT_LEDGER_PATH)
        if row.get("stage") == stage
        and row.get("assignment_relpath") == repo_relative
        and row.get("assignment_sha256") == sha256_file(assignment_path)
        and row.get("output_sha256") == sha256_file(output_path)
        and row.get("output_records") == len(load_jsonl(output_path))
        and row.get("requires_rerun") is False
        and row.get("status") in {"authoritative", "historical-recovered"}
    ]
    return len(matches) == 1


def write_efficiency_metrics() -> None:
    inventory = load_jsonl(DEPTH_INVENTORY_PATH)
    units = load_jsonl(DEPTH_UNITS_PATH)
    plans = _depth_plan_by_source()
    dossiers = load_jsonl(SOURCE_DOSSIERS_PATH)
    handoff_state = load_json(OPENALEX_HANDOFF_STATE_PATH)
    context_counts: dict[str, Any] = {}
    proxy_stages: dict[str, dict[str, int]] = {}
    depth_context_sizes: list[int] = []
    depth_source_ids: set[str] = set()
    depth_input_bytes = depth_output_bytes = 0
    for assignment_root, pattern in (
        (DEPTH_ASSIGNMENT_ROOT, "batch_*.json"),
        (DEPTH_REPAIR_ASSIGNMENT_ROOT, "batch_*_missing.json"),
    ):
        for assignment_path in sorted(assignment_root.glob(pattern)):
            assignment = load_json(assignment_path)
            output_path = Path(str(assignment.get("output_path") or ""))
            if not output_path.is_file():
                continue
            sources = assignment.get("sources") or []
            if not sources:
                continue
            depth_context_sizes.append(len(sources))
            depth_source_ids.update(str(source["source_id"]) for source in sources)
            depth_input_bytes += assignment_path.stat().st_size
            prompt_path = Path(assignment["prompt_path"])
            depth_input_bytes += prompt_path.stat().st_size
            depth_input_bytes += sum(int(source.get("normalized_bytes") or 0) for source in sources)
            depth_output_bytes += output_path.stat().st_size
    context_counts["depth"] = {
        "completed_agent_contexts": len(depth_context_sizes),
        "analyzed_source_visits": sum(depth_context_sizes),
        "unique_analyzed_sources": len(depth_source_ids),
        "sources_per_context_min": min(depth_context_sizes) if depth_context_sizes else 0,
        "sources_per_context_median": (
            sorted(depth_context_sizes)[len(depth_context_sizes) // 2]
            if depth_context_sizes
            else 0
        ),
        "sources_per_context_max": max(depth_context_sizes) if depth_context_sizes else 0,
    }
    proxy_stages["depth"] = {
        "observable_input_bytes_proxy": depth_input_bytes,
        "observable_output_bytes": depth_output_bytes,
        "approximate_input_tokens_at_four_bytes_each": depth_input_bytes // 4,
        "approximate_output_tokens_at_four_bytes_each": depth_output_bytes // 4,
    }
    for stage in ("pass12", "pass3", "pass4"):
        completed = []
        input_bytes = output_bytes = 0
        for assignment_path in _stage_assignment_paths(stage):
            assignment = load_json(assignment_path)
            output_path = Path(str(assignment.get("output_path") or ""))
            if not output_path.is_file():
                continue
            count = len(load_jsonl(output_path))
            completed.append(count)
            input_bytes += assignment_path.stat().st_size
            prompt_path = Path(assignment["prompt_path"])
            input_bytes += prompt_path.stat().st_size
            input_bytes += sum(int(unit.get("unit_bytes") or 0) for unit in assignment["units"])
            for prior_path in (assignment.get("prior_output_paths") or {}).values():
                prior = Path(prior_path)
                if prior.is_file():
                    input_bytes += prior.stat().st_size
            output_bytes += output_path.stat().st_size
        context_counts[stage] = {
            "completed_agent_contexts": len(completed),
            "analyzed_units": sum(completed),
            "units_per_context_min": min(completed) if completed else 0,
            "units_per_context_median": sorted(completed)[len(completed) // 2] if completed else 0,
            "units_per_context_max": max(completed) if completed else 0,
        }
        proxy_stages[stage] = {
            "observable_input_bytes_proxy": input_bytes,
            "observable_output_bytes": output_bytes,
            "approximate_input_tokens_at_four_bytes_each": input_bytes // 4,
            "approximate_output_tokens_at_four_bytes_each": output_bytes // 4,
        }
    audit_sizes: list[int] = []
    audit_input_bytes = audit_output_bytes = 0
    for assignment_path in sorted(AUDIT_ASSIGNMENT_ROOT.glob("*.json")):
        assignment = load_json(assignment_path)
        output_path = Path(str(assignment.get("output_path") or ""))
        if not output_path.is_file():
            continue
        rows = load_jsonl(output_path)
        audit_sizes.append(len(rows))
        audit_input_bytes += assignment_path.stat().st_size
        for key in ("prompt_path", "execution_brief_path"):
            path = Path(str(assignment.get(key) or ""))
            if path.is_file():
                audit_input_bytes += path.stat().st_size
        audit_input_bytes += sum(
            int(parent.get("artifact_bytes") or 0)
            for item in assignment.get("items") or []
            for parent in item.get("parent_sources") or []
        )
        audit_output_bytes += output_path.stat().st_size
    context_counts["independent_audit"] = {
        "completed_agent_contexts": len(audit_sizes),
        "analyzed_objects": sum(audit_sizes),
        "objects_per_context_min": min(audit_sizes) if audit_sizes else 0,
        "objects_per_context_median": (
            sorted(audit_sizes)[len(audit_sizes) // 2] if audit_sizes else 0
        ),
        "objects_per_context_max": max(audit_sizes) if audit_sizes else 0,
    }
    proxy_stages["independent_audit"] = {
        "observable_input_bytes_proxy": audit_input_bytes,
        "observable_output_bytes": audit_output_bytes,
        "approximate_input_tokens_at_four_bytes_each": audit_input_bytes // 4,
        "approximate_output_tokens_at_four_bytes_each": audit_output_bytes // 4,
    }
    critic_records = [
        row for path in _stage_batch_paths("pass3") for row in load_jsonl(path)
    ]
    critic_counts = Counter(row["critic_decision"] for row in critic_records)
    coverage = Counter(
        segment["disposition"]
        for plan in plans.values()
        for segment in plan["coverage_segments"]
    )
    coverage_lines = Counter()
    for plan in plans.values():
        for segment in plan["coverage_segments"]:
            coverage_lines[segment["disposition"]] += (
                int(segment["line_end"]) - int(segment["line_start"]) + 1
            )
    excluded_coverage = {
        key: value for key, value in coverage.items() if key != "unit-bearing"
    }
    excluded_lines = {
        key: value for key, value in coverage_lines.items() if key != "unit-bearing"
    }
    audit_sample_count = (
        len(load_jsonl(AUDIT_SAMPLE_PATH)) if AUDIT_SAMPLE_PATH.is_file() else 0
    )
    carried_audit_count = (
        len(load_jsonl(AUDIT_CARRIED_PATH)) if AUDIT_CARRIED_PATH.is_file() else 0
    )
    materialized_objects = load_jsonl(OBJECTS_PATH) if OBJECTS_PATH.is_file() else []
    metrics = {
        "metrics_version": "riemann-v2-efficiency-v1",
        "measurement_note": (
            "Codex token telemetry is unavailable for collaboration contexts; byte counts are "
            "transparent upper-bound proxies and are not claimed as exact tokens."
        ),
        "source_count": len(inventory),
        "semantic_unit_count_v2_new_or_deeper": len(units),
        "source_dossier_count": len(dossiers),
        "openalex_handoff_streams": {
            stream_name: {
                "consumed_handoff_ids": [
                    row["handoff_id"] for row in stream["consumed"]
                ],
                "processing_metrics": stream["processing_metrics"],
            }
            for stream_name, stream in handoff_state["streams"].items()
        },
        "openalex_processing_cutoff": handoff_state["processing_cutoff"],
        "pre_llm_filtering": {
            "enumerated_candidate_units_rejected": None,
            "reason_unavailable": (
                "The depth format records an exact whole-source coverage partition rather than "
                "assigning IDs to every mechanically possible candidate span."
            ),
            "coverage_segments_by_disposition": dict(sorted(coverage.items())),
            "coverage_lines_by_disposition": dict(sorted(coverage_lines.items())),
            "pre_llm_excluded_segments": dict(sorted(excluded_coverage.items())),
            "pre_llm_excluded_lines": dict(sorted(excluded_lines.items())),
        },
        "analysis_contexts": context_counts,
        "independent_audit_reuse": {
            "sampled_objects": audit_sample_count,
            "exact_pre_openalex_decisions_carried": carried_audit_count,
            "fresh_review_objects": audit_sample_count - carried_audit_count,
            "carried_fraction": carried_audit_count / max(1, audit_sample_count),
            "reuse_gate": "exact canonical object_id match only",
        },
        "critic_decisions_observed": dict(sorted(critic_counts.items())),
        "fresh_critic_fraction_of_v2_units": len(critic_records) / max(1, len(units)),
        "critic_revision_fraction": critic_counts["revise"] / max(1, len(critic_records)),
        "v1_reuse": load_json(PARENT_PATH)["v1_counts"],
        "materialized_v2_object_count": len(materialized_objects),
        "new_v2_object_count": sum(
            not any(
                str(value).startswith("carried-unchanged-from:")
                for value in row.get("derivation_ids") or []
            )
            for row in materialized_objects
        ),
        "token_or_byte_proxies_by_stage": proxy_stages,
        "largest_observable_agent_input_stages": [
            stage
            for stage, _ in sorted(
                proxy_stages.items(),
                key=lambda item: (-item[1]["observable_input_bytes_proxy"], item[0]),
            )
        ],
        "quality_tradeoff": (
            "The compact dossier/nearby-context packet is used by default, while exact source "
            "spans remain mandatory and wider context is allowed when a unit cannot be judged safely."
        ),
    }
    write_json(EFFICIENCY_METRICS_PATH, metrics)
    print("wrote observable issue #42 v2 efficiency metrics")


def write_execution_context() -> None:
    write_openalex_handoff_state()
    write_source_dossiers()
    write_execution_brief()
    write_efficiency_metrics()
    rebind_execution_context_manifest()
    print("bound deterministic v2 execution context")


def rebind_execution_context_manifest() -> None:
    """Rebind deterministic context files without rewriting historical agent packets."""
    identity = {
        "policy_comment": (
            "https://github.com/murillo128/mathia/issues/42#issuecomment-5354075669"
        ),
        "dual_stream_scope_amendment": (
            "https://github.com/murillo128/mathia/issues/42#issuecomment-5354363863"
        ),
        "concrete_artifact_binding_comment": (
            ISSUE42_CONCRETE_ARTIFACT_BINDING_COMMENT
        ),
        "openalex_handoff_state": _file_descriptor(OPENALEX_HANDOFF_STATE_PATH, V2_ROOT),
        "agnostic_supplement_parent": _file_descriptor(
            AGNOSTIC_SUPPLEMENT_PARENT_PATH, REPO_ROOT
        ),
        "source_dossiers": _file_descriptor(SOURCE_DOSSIERS_PATH, V2_ROOT),
        "run_brief": _file_descriptor(EXECUTION_BRIEF_PATH, V2_ROOT),
        "efficiency_metrics": _file_descriptor(EFFICIENCY_METRICS_PATH, V2_ROOT),
    }
    write_json(
        EXECUTION_CONTEXT_MANIFEST_PATH,
        {
            **identity,
            "manifest_id": "riemann_v2_execution_" + sha256_text(canonical_json(identity)),
        },
    )


def validate_execution_context() -> list[str]:
    errors: list[str] = []
    required = (
        SOURCE_DOSSIERS_PATH,
        EXECUTION_BRIEF_PATH,
        EFFICIENCY_METRICS_PATH,
        EXECUTION_CONTEXT_MANIFEST_PATH,
        OPENALEX_HANDOFF_STATE_PATH,
        AGNOSTIC_SUPPLEMENT_PARENT_PATH,
    )
    if any(not path.is_file() for path in required):
        return ["deterministic execution context is incomplete"]
    inventory = load_jsonl(DEPTH_INVENTORY_PATH)
    plans = _depth_plan_by_source()
    dossiers = load_jsonl(SOURCE_DOSSIERS_PATH)
    if [row.get("source_id") for row in dossiers] != [row["source_id"] for row in inventory]:
        errors.append("source dossier order/coverage differs from the depth inventory")
    source_by_id = {row["source_id"]: row for row in inventory}
    for dossier in dossiers:
        source_id = str(dossier.get("source_id") or "")
        source = source_by_id.get(source_id)
        if source is None:
            continue
        payload = {key: value for key, value in dossier.items() if key not in {"dossier_id", "dossier_sha256"}}
        expected_identity = {
            "source_id": source_id,
            "normalized_sha256": source["normalized_sha256"],
            "payload": payload,
        }
        if dossier.get("dossier_id") != "riemann_v2_dossier_" + sha256_text(canonical_json(expected_identity)):
            errors.append(f"{source_id}: dossier identity mismatch")
        if dossier.get("dossier_sha256") != sha256_text(canonical_json(payload)):
            errors.append(f"{source_id}: dossier payload hash mismatch")
        expected_units = [
            (row["local_unit_id"], row["line_start"], row["line_end"])
            for row in plans[source_id]["accepted_units"]
        ]
        actual_units = [
            (row.get("unit_id"), row.get("line_start"), row.get("line_end"))
            for row in dossier.get("result_and_mechanism_map") or []
        ]
        if actual_units != expected_units:
            errors.append(f"{source_id}: dossier exact-span index differs from depth plan")
        if dossier.get("cache_role") != "non-authoritative-execution-cache":
            errors.append(f"{source_id}: dossier is not explicitly non-authoritative")
    manifest = load_json(EXECUTION_CONTEXT_MANIFEST_PATH)
    identity = {
        key: manifest[key]
        for key in (
            "policy_comment",
            "dual_stream_scope_amendment",
            "concrete_artifact_binding_comment",
            "openalex_handoff_state",
            "agnostic_supplement_parent",
            "source_dossiers",
            "run_brief",
            "efficiency_metrics",
        )
    }
    if manifest.get("manifest_id") != "riemann_v2_execution_" + sha256_text(canonical_json(identity)):
        errors.append("execution-context manifest identity mismatch")
    if (
        manifest.get("concrete_artifact_binding_comment")
        != ISSUE42_CONCRETE_ARTIFACT_BINDING_COMMENT
    ):
        errors.append("execution-context manifest omits the concrete artifact binding")
    for key in ("source_dossiers", "run_brief", "efficiency_metrics", "openalex_handoff_state"):
        item = manifest[key]
        path = V2_ROOT / item["path"]
        if not path.is_file() or sha256_file(path) != item["sha256"] or path.stat().st_size != item["bytes"]:
            errors.append(f"execution-context manifest drift: {key}")
    agnostic_parent = manifest["agnostic_supplement_parent"]
    agnostic_parent_path = REPO_ROOT / agnostic_parent["path"]
    if (
        not agnostic_parent_path.is_file()
        or sha256_file(agnostic_parent_path) != agnostic_parent["sha256"]
        or agnostic_parent_path.stat().st_size != agnostic_parent["bytes"]
    ):
        errors.append("execution-context manifest drift: agnostic_supplement_parent")
    errors.extend(validate_openalex_handoff_state(require_frozen_cutoff=False))
    brief = EXECUTION_BRIEF_PATH.read_text(encoding="utf-8")
    handoff_state = load_json(OPENALEX_HANDOFF_STATE_PATH)
    for stream_name, label in (
        ("riemann", "Riemann"),
        ("agnostic_mathia", "agnostic Mathia"),
    ):
        stream = handoff_state["streams"][stream_name]
        authoritative_ids = [row["handoff_id"] for row in stream["consumed"]]
        authoritative_phrase = (
            f"Consumed issue #46 {label} handoff IDs: **"
            + (", ".join(authoritative_ids) if authoritative_ids else "none")
            + "**"
        )
        if authoritative_phrase in brief:
            continue
        superseded_ids = [row["handoff_id"] for row in stream.get("superseded") or []]
        historical_phrase = (
            f"Consumed issue #46 {label} handoff IDs: **"
            + (", ".join(superseded_ids) if superseded_ids else "none")
            + "**"
        )
        if not (
            historical_phrase in brief
            and superseded_ids
            and all(
                row.get("source_bytes_verified_equal_to_successor") is True
                and row.get("superseded_by") in authoritative_ids
                for row in stream.get("superseded") or []
            )
        ):
            errors.append(
                f"execution brief omits authoritative or verified historical alias: {authoritative_phrase}"
            )
    for required_phrase in (
        "The #46 processing cutoff is **"
        + handoff_state["processing_cutoff"]["status"]
        + "**",
        AGNOSTIC_V1_FREEZE_ID,
        "source dossier is a routing cache",
        "Do not read the full issue history",
        "Exact source text wins",
    ):
        if required_phrase not in brief:
            errors.append(f"execution brief omits required policy: {required_phrase}")
    metrics = load_json(EFFICIENCY_METRICS_PATH)
    if metrics.get("source_dossier_count") != len(inventory):
        errors.append("efficiency dossier count mismatch")
    dossier_by_source = {row["source_id"]: row for row in dossiers}
    for assignment_path in sorted(ANALYSIS_ASSIGNMENT_ROOT.glob("pass*_source_*.json")):
        assignment = load_json(assignment_path)
        source_id = assignment.get("source_id")
        units = assignment.get("units") or []
        if not source_id or any(unit.get("source_id") != source_id for unit in units):
            errors.append(f"{assignment_path.name}: context mixes unrelated sources")
        if not (1 <= len(units) <= SOURCE_CONTEXT_MAX_UNITS):
            errors.append(f"{assignment_path.name}: source context exceeds bounded unit count")
        assignment_brief_path = Path(str(assignment.get("execution_brief_path") or ""))
        if (
            not assignment_brief_path.is_file()
            or assignment.get("execution_brief_sha256") != sha256_file(assignment_brief_path)
        ):
            errors.append(f"{assignment_path.name}: execution brief binding mismatch")
        output_path = Path(str(assignment.get("output_path") or ""))
        if not output_path.is_file() and assignment_brief_path != EXECUTION_BRIEF_PATH:
            errors.append(f"{assignment_path.name}: pending context does not use current brief")
        dossier = dossier_by_source.get(str(source_id))
        for unit in units:
            fragment = unit.get("source_dossier_fragment") or {}
            if dossier is None or fragment.get("dossier_id") != dossier.get("dossier_id"):
                errors.append(f"{assignment_path.name}/{unit.get('unit_id')}: dossier mismatch")
            nearby = unit.get("nearby_context") or {}
            for side in ("before", "after"):
                packet = nearby.get(side) or {}
                text = str(packet.get("text") or "")
                if packet.get("sha256") != sha256_text(text):
                    errors.append(
                        f"{assignment_path.name}/{unit.get('unit_id')}: nearby {side} hash mismatch"
                    )
    if ANALYSIS_CONTEXT_QUARANTINE_PATH.is_file():
        for finding in load_jsonl(ANALYSIS_CONTEXT_QUARANTINE_PATH):
            archive = V2_ROOT / str(finding.get("archived_output_relpath") or "")
            if (
                not archive.is_file()
                or sha256_file(archive) != finding.get("original_output_sha256")
                or archive.stat().st_size != finding.get("original_output_bytes")
            ):
                errors.append(
                    f"{finding.get('quarantine_key')}: context-quarantine archive drift"
                )
            if finding.get("trainable") is not False:
                errors.append(
                    f"{finding.get('quarantine_key')}: context-quarantine must be non-trainable"
                )
    return errors


def _analysis_batch_path(stage: str, batch_stem: str) -> Path:
    return ANALYSIS_BATCH_ROOT / f"{stage}_{batch_stem}.jsonl"


def _analysis_assignment_path(stage: str, batch_stem: str) -> Path:
    return ANALYSIS_ASSIGNMENT_ROOT / f"{stage}_{batch_stem}.json"


def _raw_analysis_by_unit(stage: str) -> dict[str, dict[str, Any]]:
    records: list[dict[str, Any]] = []
    if stage == "pass4" and ANALYSIS_DETERMINISTIC_PASS4_PATH.is_file():
        records.extend(load_jsonl(ANALYSIS_DETERMINISTIC_PASS4_PATH))
    for path in _stage_batch_paths(stage):
        records.extend(load_jsonl(path))
    by_unit = {str(record.get("unit_id")): record for record in records}
    if len(records) != len(by_unit):
        raise ValueError(f"{stage}: duplicate raw unit records")
    return by_unit


def quarantine_analysis_context(stage: str, batch_stem: str, reason_code: str) -> None:
    """Preserve an isolation-compromised output byte-for-byte before a bounded rerun."""
    if stage not in {"pass12", "pass3", "pass4"}:
        raise ValueError(f"unknown analysis stage: {stage}")
    assignment_path = _analysis_assignment_path(stage, batch_stem)
    if not assignment_path.is_file():
        raise ValueError(f"missing assignment: {assignment_path}")
    assignment = load_json(assignment_path)
    output_path = Path(assignment["output_path"])
    existing = (
        load_jsonl(ANALYSIS_CONTEXT_QUARANTINE_PATH)
        if ANALYSIS_CONTEXT_QUARANTINE_PATH.is_file()
        else []
    )
    key = f"{stage}:{batch_stem}:{reason_code}"
    prior = next((row for row in existing if row.get("quarantine_key") == key), None)
    if not output_path.is_file():
        if prior is not None:
            print(f"analysis context already quarantined: {key}")
            return
        raise ValueError(f"missing raw output to quarantine: {output_path}")
    original_sha256 = sha256_file(output_path)
    archive_path = ANALYSIS_CONTEXT_QUARANTINE_ROOT / output_path.name
    archive_path.parent.mkdir(parents=True, exist_ok=True)
    if archive_path.is_file() and sha256_file(archive_path) != original_sha256:
        raise ValueError(f"context-quarantine archive collision: {archive_path}")
    if not archive_path.is_file():
        shutil.copyfile(output_path, archive_path)
    if sha256_file(archive_path) != original_sha256:
        raise ValueError("context-quarantine copy failed hash verification")
    if prior is None:
        existing.append(
            {
                "quarantine_key": key,
                "stage": stage,
                "batch_stem": batch_stem,
                "reason_code": reason_code,
                "reason": (
                    "The generating critic disclosed accidental exposure to unrelated v1 critic "
                    "excerpts. The exact output is preserved as non-trainable provenance; changed "
                    "execution context authorizes one fresh source-bounded replacement."
                ),
                "original_output_relpath": output_path.relative_to(V2_ROOT).as_posix(),
                "archived_output_relpath": archive_path.relative_to(V2_ROOT).as_posix(),
                "original_output_sha256": original_sha256,
                "original_output_bytes": output_path.stat().st_size,
                "assignment_relpath": assignment_path.relative_to(V2_ROOT).as_posix(),
                "assignment_sha256": sha256_file(assignment_path),
                "replacement_required": True,
                "trainable": False,
            }
        )
        write_jsonl(ANALYSIS_CONTEXT_QUARANTINE_PATH, existing)
    output_path.unlink()
    print(f"preserved and deactivated isolation-compromised analysis: {key}")


def _deterministic_final_record(
    unit_id: str,
    candidate: Mapping[str, Any],
    critic: Mapping[str, Any],
) -> dict[str, Any]:
    decision = str(critic["critic_decision"])
    final_decision = {
        "accept_as_is": "accepted",
        "reject": "rejected",
        "quarantine": "quarantined",
    }[decision]
    directed = candidate["directed"]
    risk_parts = [
        str(directed.get("boundary_or_failure") or "").strip(),
        str(directed.get("uncertainty") or "").strip(),
        *[str(value).strip() for value in critic.get("inference") or []],
        *[str(value).strip() for value in critic.get("context_or_ocr_risk") or []],
    ]
    quality_parts = [
        *[str(value).strip() for value in critic.get("supported") or []],
        *[str(value).strip() for value in critic.get("unsupported_or_imported") or []],
        *[str(value).strip() for value in critic.get("paraphrase_or_style_risk") or []],
    ]
    return {
        "unit_id": unit_id,
        "decision": final_decision,
        "interpretation": str(directed["conceptual_reading"]),
        "source_support": str(directed["source_grounded_mathematics"]),
        "nonparaphrase_operation": str(directed["representation_or_bridge"]),
        "speculation_status": " ".join(part for part in risk_parts if part),
        "quality_reason": " ".join(part for part in quality_parts if part),
    }


def materialize_deterministic_pass4() -> None:
    """Finalize non-revision critic decisions without another model context."""
    units = [row["unit_id"] for row in load_jsonl(DEPTH_UNITS_PATH)]
    candidates = _raw_analysis_by_unit("pass12")
    critics = _raw_analysis_by_unit("pass3")
    agent_final: set[str] = set()
    for assignment_path in _stage_assignment_paths("pass4"):
        assignment = load_json(assignment_path)
        output_path = Path(str(assignment.get("output_path") or ""))
        if output_path.is_file():
            agent_final.update(row["unit_id"] for row in load_jsonl(output_path))
    records = []
    for unit_id in units:
        if unit_id in agent_final or critics[unit_id]["critic_decision"] == "revise":
            continue
        record = _deterministic_final_record(unit_id, candidates[unit_id], critics[unit_id])
        if not record["speculation_status"]:
            record["speculation_status"] = "No additional uncertainty beyond the bounded source span."
        if not record["quality_reason"]:
            record["quality_reason"] = f"Fresh critic decision: {critics[unit_id]['critic_decision']}."
        records.append(record)
    write_jsonl(ANALYSIS_DETERMINISTIC_PASS4_PATH, records)
    print(f"deterministically finalized {len(records)} non-revision critic decisions")


def _quarantine_orphaned_raw_analysis(valid_unit_ids: set[str]) -> None:
    """Preserve, then deactivate raw records whose source identity left the live corpus."""
    preserved = (
        load_jsonl(ANALYSIS_IDENTITY_QUARANTINE_PATH)
        if ANALYSIS_IDENTITY_QUARANTINE_PATH.is_file()
        else []
    )
    preserved_keys = {
        (row.get("stage"), row.get("unit_id")) for row in preserved
    }
    removed = 0
    for stage in ("pass12", "pass3", "pass4"):
        for path in sorted(ANALYSIS_BATCH_ROOT.glob(f"{stage}_batch_*.jsonl")):
            records = load_jsonl(path)
            orphaned = [
                (index, record)
                for index, record in enumerate(records)
                if str(record.get("unit_id") or "") not in valid_unit_ids
            ]
            if not orphaned:
                continue
            original_sha256 = sha256_file(path)
            for original_record_index, record in orphaned:
                unit_id = str(record.get("unit_id") or "")
                key = (stage, unit_id)
                if key in preserved_keys:
                    continue
                preserved.append(
                    {
                        "stage": stage,
                        "unit_id": unit_id,
                        "original_batch_relpath": path.relative_to(HERE).as_posix(),
                        "original_batch_sha256": original_sha256,
                        "original_record_index": original_record_index,
                        "reason": (
                            "The unit belonged to a normalized artifact later quarantined for "
                            "source-identity mismatch; the raw teacher record is preserved as "
                            "non-trainable provenance and removed from live coverage."
                        ),
                        "record": record,
                    }
                )
                preserved_keys.add(key)
                removed += 1
            write_jsonl(
                path,
                [
                    record
                    for record in records
                    if str(record.get("unit_id") or "") in valid_unit_ids
                ],
            )
    if preserved:
        write_jsonl(ANALYSIS_IDENTITY_QUARANTINE_PATH, preserved)
    if removed:
        print(f"preserved and deactivated {removed} identity-orphaned raw analysis records")


def prepare_analysis_assignments(stage: str, artifact_root: Path) -> None:
    """Prepare bounded same-source contexts, preserving completed historical work."""
    if stage not in {"pass12", "pass3", "pass4"}:
        raise ValueError(f"unknown analysis stage: {stage}")
    context_errors = validate_execution_context()
    if context_errors:
        raise ValueError(
            "deterministic execution context must validate before agent work:\n"
            + "\n".join(context_errors)
        )
    units = load_jsonl(DEPTH_UNITS_PATH)
    if not units:
        raise ValueError("materialized v2 depth units are required")
    if stage == "pass12":
        _quarantine_orphaned_raw_analysis({unit["unit_id"] for unit in units})
    inventory = {row["source_id"]: row for row in load_jsonl(DEPTH_INVENTORY_PATH)}
    pass12 = _raw_analysis_by_unit("pass12") if stage in {"pass3", "pass4"} else {}
    critics = _raw_analysis_by_unit("pass3") if stage == "pass4" else {}
    expected_ids = {unit["unit_id"] for unit in units}
    if stage in {"pass3", "pass4"} and set(pass12) != expected_ids:
        raise ValueError(f"pass12 coverage must be complete before {stage}")
    if stage == "pass4" and set(critics) != expected_ids:
        raise ValueError("pass3 coverage must be complete before pass4")
    ANALYSIS_ASSIGNMENT_ROOT.mkdir(parents=True, exist_ok=True)
    completed_ids: set[str] = set()
    for path in _stage_assignment_paths(stage):
        assignment = load_json(path)
        output_path = Path(str(assignment.get("output_path") or ""))
        if output_path.is_file():
            if not _verified_analysis_output(stage, path, assignment):
                raise ValueError(
                    f"{path.name}: stale or unbound output must be archived before reuse"
                )
            completed_ids.update(str(row["unit_id"]) for row in load_jsonl(output_path))
        else:
            path.unlink()
    if stage == "pass4":
        materialize_deterministic_pass4()
        completed_ids.update(
            row["unit_id"] for row in load_jsonl(ANALYSIS_DETERMINISTIC_PASS4_PATH)
        )
    pending_units = [
        unit
        for unit in units
        if unit["unit_id"] not in completed_ids
        and (stage != "pass4" or critics[unit["unit_id"]]["critic_decision"] == "revise")
    ]
    dossiers = {row["source_id"]: row for row in load_jsonl(SOURCE_DOSSIERS_PATH)}
    plans = _depth_plan_by_source()
    source_lines: dict[str, list[str]] = {}
    grouped: dict[str, list[dict[str, Any]]] = {}
    for unit in pending_units:
        source_id = unit["source_id"]
        source = inventory[source_id]
        dossier = dossiers[source_id]
        plan_units = plans[source_id]["accepted_units"]
        plan_index = next(
            index
            for index, candidate in enumerate(plan_units)
            if candidate["local_unit_id"] == unit["unit_id"]
        )
        if source_id not in source_lines:
            source_path = _normalized_source_path(source, artifact_root)
            if sha256_file(source_path) != source["normalized_sha256"]:
                raise ValueError(f"{source_id}: normalized source drift before assignment")
            source_lines[source_id] = source_path.read_text(
                encoding="utf-8", errors="replace"
            ).splitlines()
        lines = source_lines[source_id]
        start, end = int(unit["line_start"]), int(unit["line_end"])
        before_start = max(1, start - NEARBY_CONTEXT_LINES)
        before_text = "\n".join(lines[before_start - 1 : start - 1])
        if before_text:
            before_text += "\n"
        after_end = min(len(lines), end + NEARBY_CONTEXT_LINES)
        after_text = "\n".join(lines[end:after_end])
        if after_text:
            after_text += "\n"
        result_entry = dossier["result_and_mechanism_map"][plan_index]
        dependency_entry = dossier["dependency_context_and_representation_map"][plan_index]
        neighboring_entries = [
            dossier["result_and_mechanism_map"][index]
            for index in (plan_index - 1, plan_index + 1)
            if 0 <= index < len(plan_units)
        ]
        item: dict[str, Any] = {
            **unit,
            "unit_artifact_abspath": str(artifact_root / unit["unit_artifact_relpath"]),
            "source": {
                key: source.get(key)
                for key in (
                    "source_id",
                    "title",
                    "authors",
                    "year",
                    "source_type",
                    "viewpoint_tags",
                    "artifact_store",
                    "extraction_confidence",
                    "extraction_warnings",
                )
            },
            "nearby_context": {
                "before": {
                    "line_start": before_start if before_text else None,
                    "line_end": start - 1 if before_text else None,
                    "text": before_text,
                    "sha256": sha256_text(before_text),
                },
                "after": {
                    "line_start": end + 1 if after_text else None,
                    "line_end": after_end if after_text else None,
                    "text": after_text,
                    "sha256": sha256_text(after_text),
                },
            },
            "source_dossier_fragment": {
                "dossier_id": dossier["dossier_id"],
                "dossier_sha256": dossier["dossier_sha256"],
                "dossier_relpath": SOURCE_DOSSIERS_PATH.relative_to(V2_ROOT).as_posix(),
                "section_entries": [
                    section
                    for section in dossier["section_argument_map"]
                    if int(section["line_start"]) <= end
                    and int(section["line_end"]) >= start
                ],
                "unit_result_entry": result_entry,
                "unit_dependency_entry": dependency_entry,
                "neighboring_unit_entries": neighboring_entries,
                "related_synthesis_entries": [
                    synthesis
                    for synthesis in dossier["within_source_synthesis_map"]
                    if unit["unit_id"] in synthesis.get("parent_local_unit_ids", [])
                ],
                "extraction_quality": {
                    "confidence": dossier["extraction_quality"]["confidence"],
                    "warnings": dossier["extraction_quality"]["warnings"],
                    "risk_spans": [
                        risk
                        for risk in dossier["extraction_quality"]["risk_spans"]
                        if int(risk["line_start"]) <= after_end
                        and int(risk["line_end"]) >= before_start
                    ],
                },
            },
        }
        if stage in {"pass3", "pass4"}:
            item["candidate_analysis"] = pass12[unit["unit_id"]]
        if stage == "pass4":
            item["critic_findings"] = critics[unit["unit_id"]]
        grouped.setdefault(source_id, []).append(item)
    prompt_path = ANALYSIS_PROMPTS[stage]
    created = 0
    for source_id in sorted(grouped):
        source_items = grouped[source_id]
        slug = re.sub(r"[^a-z0-9]+", "_", source_id.lower()).strip("_")[:48]
        source_key = f"{slug}_{sha256_text(source_id)[:8]}"
        for offset in range(0, len(source_items), SOURCE_CONTEXT_MAX_UNITS):
            items = source_items[offset : offset + SOURCE_CONTEXT_MAX_UNITS]
            part = offset // SOURCE_CONTEXT_MAX_UNITS + 1
            context_stem = f"source_{source_key}_part_{part:02d}"
            write_json(
                _analysis_assignment_path(stage, context_stem),
                _bind_model_visible_packet({
                    "stage": stage,
                    "isolation_requirement": (
                        "fresh isolated critic context; no teacher reasoning, unrelated batch, or v1 critic output"
                        if stage == "pass3"
                        else "isolated same-source generation context"
                    ),
                    "context_packet_policy": (
                        "Read AGENTS.md, the compact run brief, frozen prompt, exact unit artifacts, "
                        "bounded nearby context, dossier fragments, and embedded named prior records only."
                    ),
                    "execution_brief_path": str(EXECUTION_BRIEF_PATH),
                    "execution_brief_sha256": sha256_file(EXECUTION_BRIEF_PATH),
                    "prompt_path": str(prompt_path),
                    "prompt_sha256": sha256_file(prompt_path),
                    "output_path": str(_analysis_batch_path(stage, context_stem)),
                    "prior_output_paths": {},
                    "source_id": source_id,
                    "unit_count": len(items),
                    "units": items,
                }),
            )
            created += 1
    print(
        f"preserved {len(completed_ids)} completed {stage} units; prepared {created} "
        f"bounded same-source contexts for {len(pending_units)} pending units"
    )


def validate_raw_analysis_stage(stage: str, require_complete: bool = True) -> list[str]:
    errors: list[str] = []
    assignment_paths = _stage_assignment_paths(stage)
    seen: list[str] = []
    record_groups: list[tuple[str, list[dict[str, Any]], list[str] | None]] = []
    if stage == "pass4" and ANALYSIS_DETERMINISTIC_PASS4_PATH.is_file():
        record_groups.append(
            (
                ANALYSIS_DETERMINISTIC_PASS4_PATH.name,
                load_jsonl(ANALYSIS_DETERMINISTIC_PASS4_PATH),
                None,
            )
        )
    for assignment_path in assignment_paths:
        assignment = load_json(assignment_path)
        source_ids = _assignment_source_ids(assignment.get("units") or [])
        if len(source_ids) != 1:
            errors.append(
                f"{assignment_path.name}: analysis context must bind exactly one source"
            )
        packet_sha256 = assignment.get("model_visible_packet_sha256")
        if packet_sha256 is not None and packet_sha256 != model_visible_packet_sha256(
            assignment
        ):
            errors.append(f"{assignment_path.name}: analysis execution packet drift")
        expected = [row["unit_id"] for row in assignment.get("units") or []]
        output_path = Path(str(assignment.get("output_path") or ""))
        if not output_path.is_file():
            if require_complete:
                errors.append(f"{assignment_path.name}: missing raw output")
            continue
        try:
            records = load_jsonl(output_path)
        except (OSError, ValueError, json.JSONDecodeError) as error:
            errors.append(f"{output_path.name}: invalid JSONL: {error}")
            continue
        record_groups.append((output_path.name, records, expected))
    for output_name, records, expected in record_groups:
        actual = [str(record.get("unit_id") or "") for record in records]
        if expected is not None and actual != expected:
            errors.append(f"{output_name}: unit order/coverage mismatch")
        seen.extend(actual)
        for record in records:
            unit_id = str(record.get("unit_id") or "")
            if stage == "pass12":
                if set(record) != {"unit_id", "spontaneous", "directed"}:
                    errors.append(f"{stage}/{unit_id}: raw top-level fields mismatch")
                    continue
                spontaneous = record.get("spontaneous") or {}
                directed = record.get("directed") or {}
                if set(spontaneous) != PASS_PAYLOAD_FIELDS["spontaneous"]:
                    errors.append(f"{stage}/{unit_id}: spontaneous fields mismatch")
                if set(directed) != PASS_PAYLOAD_FIELDS["directed"]:
                    errors.append(f"{stage}/{unit_id}: directed fields mismatch")
            else:
                pass_name = "critic" if stage == "pass3" else "revised"
                if set(record) != PASS_PAYLOAD_FIELDS[pass_name]:
                    errors.append(f"{stage}/{unit_id}: raw fields mismatch")
            if stage == "pass3" and record.get("critic_decision") not in {
                "accept_as_is", "revise", "reject", "quarantine"
            }:
                errors.append(f"{stage}/{unit_id}: invalid critic decision")
            if stage == "pass4":
                if record.get("decision") not in {"accepted", "rejected", "quarantined"}:
                    errors.append(f"{stage}/{unit_id}: invalid final decision")
                if not str(record.get("interpretation") or "").strip():
                    errors.append(f"{stage}/{unit_id}: empty interpretation")
    if len(seen) != len(set(seen)):
        errors.append(f"{stage}: a unit occurs in more than one output batch")
    if require_complete:
        expected_all = [row["unit_id"] for row in load_jsonl(DEPTH_UNITS_PATH)]
        if set(seen) != set(expected_all):
            errors.append(f"{stage}: raw output does not cover the exact v2 depth unit set")
    return errors


def _exact_analysis_execution_receipt(
    stage: str,
    assignment_path: Path,
    output_path: Path,
    execution_rows: Sequence[Mapping[str, Any]],
    *,
    release_root: Path = V2_ROOT,
) -> Mapping[str, Any]:
    context_key = f"{stage}:{assignment_path.stem.removeprefix(stage + '_')}"
    assignment_relpath = _execution_ledger_relpath(release_root, assignment_path)
    assignment_sha256 = sha256_file(assignment_path)
    receipts = [
        row
        for row in execution_rows
        if row.get("assignment_relpath") == assignment_relpath
        and row.get("assignment_sha256") == assignment_sha256
        and row.get("requires_rerun") is False
        and row.get("status") in {"authoritative", "historical-recovered"}
    ]
    if len(receipts) != 1:
        raise ValueError(
            f"{context_key}: expected one authoritative exact execution receipt"
        )
    receipt = receipts[0]
    if (
        receipt.get("stage") != stage
        or receipt.get("output_relpath")
        != _execution_ledger_relpath(release_root, output_path)
        or receipt.get("output_sha256") != sha256_file(output_path)
        or receipt.get("output_records") != len(load_jsonl(output_path))
    ):
        raise ValueError(f"{context_key}: execution receipt binding mismatch")
    return receipt


def write_analysis_generation_provenance() -> None:
    """Bind each isolated generation context to its prompt, assignment, and raw output."""
    if not LEGACY_CONTEXT_LEDGER_PATH.is_file():
        raise ValueError("analysis execution provenance ledger is missing")
    execution_rows = load_jsonl(LEGACY_CONTEXT_LEDGER_PATH)
    execution_provenance.validate_execution_rows(execution_rows)
    records: list[dict[str, Any]] = []
    agent_candidates_by_stage_and_unit: dict[tuple[str, str], frozenset[str]] = {}
    task_path_owners: dict[str, str] = {}
    teacher_task_paths: set[str] = set()
    critic_task_paths: set[str] = set()
    for stage in ("pass12", "pass3", "pass4"):
        errors = validate_raw_analysis_stage(stage, require_complete=True)
        if errors:
            raise ValueError(f"cannot bind {stage} provenance:\n" + "\n".join(errors))
        for assignment_path in _stage_assignment_paths(stage):
            assignment = load_json(assignment_path)
            output_path = Path(assignment["output_path"])
            context_stem = assignment_path.stem.removeprefix(stage + "_")
            context_key = f"{stage}:{context_stem}"
            assignment_sha256 = sha256_file(assignment_path)
            receipt = _exact_analysis_execution_receipt(
                stage, assignment_path, output_path, execution_rows
            )
            required_execution_fields = (
                "agent_task_path",
                "provider",
                "model_selector",
                "reasoning_effort",
                "client",
                "ledger_id",
            )
            missing_execution_fields = [
                field for field in required_execution_fields if not receipt.get(field)
            ]
            if missing_execution_fields:
                raise ValueError(
                    f"{context_key}: execution receipt is missing "
                    + ", ".join(missing_execution_fields)
                )
            agent_task_path = str(receipt["agent_task_path"])
            if not agent_task_path.startswith("/root/"):
                raise ValueError(f"{context_key}: invalid exact agent task path")
            prior_owner = task_path_owners.get(agent_task_path)
            if prior_owner is not None and prior_owner != context_key:
                raise ValueError(
                    f"{context_key}: agent task path reused from {prior_owner}: "
                    f"{agent_task_path}"
                )
            task_path_owners[agent_task_path] = context_key
            if stage == "pass12":
                teacher_task_paths.add(agent_task_path)
            elif stage == "pass3":
                critic_task_paths.add(agent_task_path)
            agent_task_path_candidates = [agent_task_path]
            for unit in assignment.get("units") or []:
                agent_candidates_by_stage_and_unit[(stage, str(unit["unit_id"]))] = (
                    frozenset(agent_task_path_candidates)
                )
            records.append(
                {
                    "context_id": f"collaboration-agent:{stage}:{context_stem}",
                    "stage": stage,
                    "batch": context_stem,
                    "agent_task_path": agent_task_path,
                    "agent_task_path_candidates": agent_task_path_candidates,
                    "agent_task_path_status": "exact",
                    "execution_ledger_id": receipt["ledger_id"],
                    "provider": receipt["provider"],
                    "model": receipt["model_selector"],
                    "reasoning_effort": receipt["reasoning_effort"],
                    "client": receipt["client"],
                    "isolation": assignment["isolation_requirement"],
                    "unit_count": assignment["unit_count"],
                    "prompt_relpath": Path(assignment["prompt_path"]).relative_to(V2_ROOT).as_posix(),
                    "prompt_sha256": assignment["prompt_sha256"],
                    "assignment_relpath": assignment_path.relative_to(V2_ROOT).as_posix(),
                    "assignment_sha256": sha256_file(assignment_path),
                    "model_visible_packet_sha256": model_visible_packet_sha256(assignment),
                    "raw_output_relpath": output_path.relative_to(V2_ROOT).as_posix(),
                    "raw_output_sha256": sha256_file(output_path),
                }
            )
    critic_collisions = sorted(
        unit_id
        for stage, unit_id in agent_candidates_by_stage_and_unit
        if stage == "pass3"
        and agent_candidates_by_stage_and_unit.get(("pass12", unit_id), frozenset())
        & agent_candidates_by_stage_and_unit[("pass3", unit_id)]
    )
    if critic_collisions:
        raise ValueError(
            "fresh-critic isolation violated or not demonstrable because pass12/pass3 "
            "agent task-path candidates overlap: "
            + ", ".join(critic_collisions)
        )
    if teacher_task_paths & critic_task_paths:
        raise ValueError(
            "teacher/critic execution task paths overlap: "
            + ", ".join(sorted(teacher_task_paths & critic_task_paths))
        )
    write_jsonl(ANALYSIS_GENERATION_PROVENANCE_PATH, records)
    print(f"wrote exact provenance for {len(records)} isolated analysis contexts")


def _analysis_context_by_unit(stage: str) -> dict[str, str]:
    contexts: dict[str, str] = {}
    for assignment_path in _stage_assignment_paths(stage):
        assignment = load_json(assignment_path)
        output_path = Path(str(assignment.get("output_path") or ""))
        if not output_path.is_file():
            continue
        context_stem = assignment_path.stem.removeprefix(stage + "_")
        for record in load_jsonl(output_path):
            unit_id = str(record["unit_id"])
            if unit_id in contexts:
                raise ValueError(f"{stage}/{unit_id}: duplicate execution context")
            contexts[unit_id] = f"collaboration-agent:{stage}:{context_stem}"
    if stage == "pass4" and ANALYSIS_DETERMINISTIC_PASS4_PATH.is_file():
        for record in load_jsonl(ANALYSIS_DETERMINISTIC_PASS4_PATH):
            unit_id = str(record["unit_id"])
            if unit_id in contexts:
                raise ValueError(f"{stage}/{unit_id}: duplicate deterministic/agent context")
            contexts[unit_id] = "deterministic-gate:pass4-non-revision"
    return contexts


def combine_analysis_batches() -> None:
    unit_ids = [row["unit_id"] for row in load_jsonl(DEPTH_UNITS_PATH)]
    for stage in ("pass12", "pass3", "pass4"):
        errors = validate_raw_analysis_stage(stage, require_complete=True)
        if errors:
            raise ValueError(f"cannot combine {stage}:\n" + "\n".join(errors))
    raw12 = _raw_analysis_by_unit("pass12")
    raw3 = _raw_analysis_by_unit("pass3")
    raw4 = _raw_analysis_by_unit("pass4")
    stage_records = {
        "spontaneous": {unit_id: raw12[unit_id]["spontaneous"] for unit_id in unit_ids},
        "directed": {unit_id: raw12[unit_id]["directed"] for unit_id in unit_ids},
        "critic": raw3,
        "revised": raw4,
    }
    stage_prompt = {
        "spontaneous": "pass12",
        "directed": "pass12",
        "critic": "pass3",
        "revised": "pass4",
    }
    context_by_stage = {
        stage: _analysis_context_by_unit(stage) for stage in ("pass12", "pass3", "pass4")
    }
    generated_at = utc_now()
    for pass_name, by_unit in stage_records.items():
        prompt_key = stage_prompt[pass_name]
        prompt_path = ANALYSIS_PROMPTS[prompt_key]
        canonical: list[dict[str, Any]] = []
        for unit_id in unit_ids:
            payload = by_unit[unit_id]
            if set(payload) != PASS_PAYLOAD_FIELDS[pass_name]:
                raise ValueError(f"{pass_name}/{unit_id}: raw fields differ at combination")
            context_id = context_by_stage[prompt_key][unit_id]
            deterministic = context_id.startswith("deterministic-gate:")
            record_prompt_path = (
                DETERMINISTIC_PASS4_PROMPT if deterministic else prompt_path
            )
            canonical.append(
                {
                    "analysis_id": f"riemann_v2_{pass_name}_{unit_id}",
                    "unit_id": unit_id,
                    "pass": pass_name,
                    "teacher_provenance": {
                        "provider": "deterministic" if deterministic else "openai",
                        "model": "none" if deterministic else "gpt-5.6-sol",
                        "reasoning_effort": "none" if deterministic else "xhigh",
                        "client": "ordinary-code" if deterministic else "codex-collaboration-agent",
                        "execution_context_id": context_id,
                        "execution": (
                            "same isolated pass12 context for spontaneous and directed roles"
                            if prompt_key == "pass12"
                            else "deterministic finalization of a non-revision fresh-critic decision"
                            if deterministic
                            else f"fresh isolated {pass_name} context"
                        ),
                    },
                    "prompt_relpath": record_prompt_path.relative_to(V2_ROOT).as_posix(),
                    "prompt_sha256": sha256_file(record_prompt_path),
                    "generated_at": generated_at,
                    "output": {key: value for key, value in payload.items() if key != "unit_id"},
                }
            )
        write_jsonl(PASS_FILES[pass_name], canonical)
    print(f"combined gated analysis records for {len(unit_ids)} v2 depth units")


def validate_analysis() -> list[str]:
    errors: list[str] = []
    unit_ids = [row["unit_id"] for row in load_jsonl(DEPTH_UNITS_PATH)]
    for pass_name, path in PASS_FILES.items():
        records = load_jsonl(path)
        if [record.get("unit_id") for record in records] != unit_ids:
            errors.append(f"{pass_name}: canonical pass order/coverage mismatch")
            continue
        expected_output = PASS_PAYLOAD_FIELDS[pass_name] - {"unit_id"}
        for record in records:
            if record.get("pass") != pass_name or set(record.get("output") or {}) != expected_output:
                errors.append(f"{pass_name}/{record.get('unit_id')}: canonical fields mismatch")
            prompt_path = V2_ROOT / str(record.get("prompt_relpath") or "")
            if not prompt_path.is_file() or sha256_file(prompt_path) != record.get("prompt_sha256"):
                errors.append(f"{pass_name}/{record.get('unit_id')}: prompt provenance mismatch")
    return errors


SYNTHESIS_FINAL_FIELDS = {
    "synthesis_id",
    "decision",
    "synthesis",
    "source_support",
    "nonparaphrase_operation",
    "limits",
    "quality_reason",
}


def _all_unit_descriptors(v2_artifact_root: Path) -> dict[str, dict[str, Any]]:
    descriptors: dict[str, dict[str, Any]] = {}
    for unit in load_jsonl(V1_ROOT / "units.jsonl"):
        descriptors[unit["unit_id"]] = {
            **unit,
            "unit_artifact_abspath": str(pipeline.DEFAULT_ARTIFACT_ROOT / unit["unit_artifact_relpath"]),
            "release_id": V1_RELEASE_ID,
        }
    for unit in load_jsonl(DEPTH_UNITS_PATH):
        descriptors[unit["unit_id"]] = {
            **unit,
            "unit_artifact_abspath": str(v2_artifact_root / unit["unit_artifact_relpath"]),
            "release_id": V2_RELEASE_ID,
        }
    return descriptors


def materialize_within_source_synthesis_candidates() -> None:
    unit_ids = set(_all_unit_descriptors(DEFAULT_ARTIFACT_ROOT))
    records: list[dict[str, Any]] = []
    seen: set[str] = set()
    for plan_path in sorted(DEPTH_PLAN_ROOT.glob("batch_*.jsonl")):
        for plan in load_jsonl(plan_path):
            for candidate in plan.get("within_source_synthesis_candidates") or []:
                parents = list(candidate["parent_local_unit_ids"])
                identity = {
                    "source_id": plan["source_id"],
                    "title": candidate["title"],
                    "parent_unit_ids": parents,
                    "claim": candidate["claim"],
                }
                synthesis_id = "riemann_v2_within_" + sha256_text(canonical_json(identity))[:24]
                if synthesis_id in seen:
                    continue
                seen.add(synthesis_id)
                records.append(
                    {
                        "synthesis_id": synthesis_id,
                        "source_id": plan["source_id"],
                        "title": candidate["title"],
                        "parent_unit_ids": parents,
                        "claim": candidate["claim"],
                        "proposed_limit": candidate["limit"],
                        "candidate_provenance": "v2-fresh-context-whole-source-depth-review",
                        "parent_resolution": "resolved" if set(parents).issubset(unit_ids) else "unresolved",
                    }
                )
    unresolved = [row["synthesis_id"] for row in records if row["parent_resolution"] != "resolved"]
    if unresolved:
        raise ValueError(f"within-source candidates have unresolved units: {unresolved[:8]}")
    write_jsonl(WITHIN_SYNTHESIS_CANDIDATES_PATH, records)
    print(f"materialized {len(records)} source-linked within-source synthesis candidates")


def prepare_within_source_synthesis_assignments(v2_artifact_root: Path) -> None:
    candidates = load_jsonl(WITHIN_SYNTHESIS_CANDIDATES_PATH)
    units = _all_unit_descriptors(v2_artifact_root)
    accepted = {
        row["unit_id"]: row["output"]
        for row in load_jsonl(PASS_FILES["revised"])
        if row["output"]["decision"] == "accepted"
    }
    dossiers = {row["source_id"]: row for row in load_jsonl(SOURCE_DOSSIERS_PATH)}
    grouped: dict[str, list[dict[str, Any]]] = {}
    deterministic_rejections: list[dict[str, Any]] = []
    for candidate in candidates:
        parent_units = [units[unit_id] for unit_id in candidate["parent_unit_ids"]]
        if not all(unit_id in accepted for unit_id in candidate["parent_unit_ids"]):
            failed = [
                unit_id for unit_id in candidate["parent_unit_ids"] if unit_id not in accepted
            ]
            deterministic_rejections.append(
                {
                    "synthesis_id": candidate["synthesis_id"],
                    "decision": "rejected",
                    "synthesis": "No trainable synthesis is materialized from non-accepted parents.",
                    "source_support": "Parent acceptance gate failed for: " + ", ".join(failed),
                    "nonparaphrase_operation": "No cross-unit operation is licensed by the gate.",
                    "limits": "This is a deterministic eligibility rejection, not a mathematical refutation.",
                    "quality_reason": "At least one required source-linked interpretation is not accepted.",
                }
            )
            continue
        item = {
            "candidate": candidate,
            "parents": [
                {
                    **unit,
                    "accepted_interpretation": accepted[unit["unit_id"]],
                }
                for unit in parent_units
            ],
            "source_dossier_binding": {
                "dossier_id": dossiers[candidate["source_id"]]["dossier_id"],
                "dossier_sha256": dossiers[candidate["source_id"]]["dossier_sha256"],
            },
        }
        grouped.setdefault(candidate["source_id"], []).append(item)
    write_jsonl(WITHIN_SYNTHESIS_DETERMINISTIC_PATH, deterministic_rejections)
    prompt_path = V2_ROOT / "prompts" / "within_source_synthesis_adjudication.md"
    WITHIN_SYNTHESIS_ASSIGNMENT_ROOT.mkdir(parents=True, exist_ok=True)
    for path in WITHIN_SYNTHESIS_ASSIGNMENT_ROOT.glob("*.json"):
        path.unlink()
    context_count = included = 0
    for source_id in sorted(grouped):
        source_items = grouped[source_id]
        slug = re.sub(r"[^a-z0-9]+", "_", source_id.lower()).strip("_")[:48]
        source_key = f"{slug}_{sha256_text(source_id)[:8]}"
        for offset in range(0, len(source_items), SYNTHESIS_CONTEXT_MAX_CANDIDATES):
            items = source_items[offset : offset + SYNTHESIS_CONTEXT_MAX_CANDIDATES]
            part = offset // SYNTHESIS_CONTEXT_MAX_CANDIDATES + 1
            stem = f"source_{source_key}_part_{part:02d}"
            output_path = WITHIN_SYNTHESIS_BATCH_ROOT / f"adjudication_{stem}.jsonl"
            if output_path.is_file():
                raise ValueError(
                    f"{output_path.name}: stale synthesis output must be archived or reconciled"
                )
            write_json(
                WITHIN_SYNTHESIS_ASSIGNMENT_ROOT / f"{stem}.json",
                _bind_model_visible_packet({
                    "task": "source-grounded within-source synthesis adjudication",
                    "source_id": source_id,
                    "execution_brief_path": str(EXECUTION_BRIEF_PATH),
                    "execution_brief_sha256": sha256_file(EXECUTION_BRIEF_PATH),
                    "prompt_path": str(prompt_path),
                    "prompt_sha256": sha256_file(prompt_path),
                    "output_path": str(output_path),
                    "candidate_count": len(items),
                    "candidates": items,
                }),
            )
            context_count += 1
            included += len(items)
    print(
        f"prepared {included} accepted-parent within-source candidates across "
        f"{context_count} bounded same-source adjudication contexts"
    )


def validate_within_source_synthesis(require_complete: bool = True) -> list[str]:
    errors: list[str] = []
    candidates = {row["synthesis_id"]: row for row in load_jsonl(WITHIN_SYNTHESIS_CANDIDATES_PATH)}
    seen: list[str] = []
    if WITHIN_SYNTHESIS_DETERMINISTIC_PATH.is_file():
        for row in load_jsonl(WITHIN_SYNTHESIS_DETERMINISTIC_PATH):
            seen.append(str(row.get("synthesis_id") or ""))
            if set(row) != SYNTHESIS_FINAL_FIELDS or row.get("decision") != "rejected":
                errors.append(
                    f"{row.get('synthesis_id')}: malformed deterministic synthesis rejection"
                )
    for assignment_path in sorted(WITHIN_SYNTHESIS_ASSIGNMENT_ROOT.glob("*.json")):
        assignment = load_json(assignment_path)
        expected = [row["candidate"]["synthesis_id"] for row in assignment["candidates"]]
        output_path = Path(assignment["output_path"])
        if not output_path.is_file():
            if require_complete:
                errors.append(f"{assignment_path.name}: missing synthesis adjudication")
            continue
        records = load_jsonl(output_path)
        actual = [row.get("synthesis_id") for row in records]
        if actual != expected:
            errors.append(f"{output_path.name}: synthesis order/coverage mismatch")
        seen.extend(str(value) for value in actual)
        for row in records:
            if set(row) != SYNTHESIS_FINAL_FIELDS:
                errors.append(f"{row.get('synthesis_id')}: final synthesis fields mismatch")
            if row.get("decision") not in {"accepted", "quarantined", "rejected"}:
                errors.append(f"{row.get('synthesis_id')}: invalid synthesis decision")
    if len(seen) != len(set(seen)):
        errors.append("within-source synthesis appears in multiple outputs")
    if require_complete and set(seen) != set(candidates):
        errors.append("within-source synthesis adjudication does not cover the exact candidate set")
    return errors


def combine_within_source_synthesis() -> None:
    errors = validate_within_source_synthesis(require_complete=True)
    if errors:
        raise ValueError("cannot combine within-source synthesis:\n" + "\n".join(errors))
    candidates = load_jsonl(WITHIN_SYNTHESIS_CANDIDATES_PATH)
    raw: dict[str, dict[str, Any]] = {}
    context_by_id: dict[str, str] = {}
    prompt_path = V2_ROOT / "prompts" / "within_source_synthesis_adjudication.md"
    if WITHIN_SYNTHESIS_DETERMINISTIC_PATH.is_file():
        for row in load_jsonl(WITHIN_SYNTHESIS_DETERMINISTIC_PATH):
            raw[row["synthesis_id"]] = row
            context_by_id[row["synthesis_id"]] = "deterministic-gate:within-synthesis-parent-eligibility"
    for assignment_path in sorted(WITHIN_SYNTHESIS_ASSIGNMENT_ROOT.glob("*.json")):
        assignment = load_json(assignment_path)
        batch_stem = assignment_path.stem
        for row in load_jsonl(Path(assignment["output_path"])):
            raw[row["synthesis_id"]] = row
            context_by_id[row["synthesis_id"]] = f"collaboration-agent:within-synthesis:{batch_stem}"
    records = []
    for candidate in candidates:
        final = raw[candidate["synthesis_id"]]
        records.append(
            {
                **candidate,
                **{key: final[key] for key in SYNTHESIS_FINAL_FIELDS if key != "synthesis_id"},
                "teacher_provenance": {
                    "provider": "deterministic" if context_by_id[candidate["synthesis_id"]].startswith("deterministic-gate:") else "openai",
                    "model": "none" if context_by_id[candidate["synthesis_id"]].startswith("deterministic-gate:") else "gpt-5.6-sol",
                    "reasoning_effort": "none" if context_by_id[candidate["synthesis_id"]].startswith("deterministic-gate:") else "xhigh",
                    "client": "ordinary-code" if context_by_id[candidate["synthesis_id"]].startswith("deterministic-gate:") else "codex-collaboration-agent",
                    "execution_context_id": context_by_id[candidate["synthesis_id"]],
                    "prompt_relpath": prompt_path.relative_to(V2_ROOT).as_posix(),
                    "prompt_sha256": sha256_file(prompt_path),
                },
            }
        )
    write_jsonl(WITHIN_SYNTHESIS_FINAL_PATH, records)
    print(f"combined final decisions for {len(records)} within-source syntheses")


def record_within_source_saturation() -> None:
    errors = validate_depth_plans(require_complete=True)
    if errors:
        raise ValueError("cannot record within-source saturation:\n" + "\n".join(errors))
    plans = [
        row
        for path in sorted(DEPTH_PLAN_ROOT.glob("batch_*.jsonl"))
        for row in load_jsonl(path)
    ]
    inventory = {row["source_id"]: row for row in load_jsonl(DEPTH_INVENTORY_PATH)}
    disposition_lines: Counter[str] = Counter()
    for plan in plans:
        for segment in plan["coverage_segments"]:
            disposition_lines[segment["disposition"]] += (
                int(segment["line_end"]) - int(segment["line_start"]) + 1
            )
    unit_counts = sorted(len(plan["accepted_units"]) for plan in plans)
    remaining = {
        plan["source_id"]: plan["remaining_meaningful_material"]
        for plan in plans
        if plan["remaining_meaningful_material"]
    }
    long_form_ids = {
        source_id
        for source_id, row in inventory.items()
        if int(row.get("normalized_page_count") or 0) >= 30
        or row.get("source_type") in {
            "book",
            "monograph-lecture-series",
            "advanced-lecture-notes",
            "masters-thesis",
        }
    }
    long_form_plans = [plan for plan in plans if plan["source_id"] in long_form_ids]
    identity = {
        "axis": "within-source",
        "source_count": len(plans),
        "unit_count": sum(unit_counts),
        "remaining_meaningful_source_count": len(remaining),
        "disposition_lines": dict(sorted(disposition_lines.items())),
    }
    entry = {
        **identity,
        "entry_id": "v2_saturation_" + sha256_text(canonical_json(identity)),
        "recorded_at": utc_now(),
        "whole_source_exact_partition_count": len(plans),
        "total_logical_lines": sum(int(row["line_count"]) for row in inventory.values()),
        "unit_distribution": {
            "min": min(unit_counts),
            "median": unit_counts[len(unit_counts) // 2],
            "p90": unit_counts[min(len(unit_counts) - 1, int(len(unit_counts) * 0.9))],
            "max": max(unit_counts),
        },
        "long_form_source_count": len(long_form_plans),
        "long_form_unit_count": sum(len(plan["accepted_units"]) for plan in long_form_plans),
        "v1_context_repair_count": sum(len(plan["v1_context_repairs"]) for plan in plans),
        "remaining_meaningful_material": remaining,
        "status": "established" if not remaining else "gaps-recorded",
        "evidence": (
            "Every usable source has a fresh-context, first-to-last logical-line inspection, an "
            "exact gap-free coverage partition, source-specific stop reason, and quota-free unit "
            "selection. Remaining meaningful material is preserved explicitly rather than hidden."
        ),
    }
    entries = [row for row in load_jsonl(SATURATION_LOG_PATH) if row.get("axis") != "within-source"]
    entries.append(entry)
    write_jsonl(SATURATION_LOG_PATH, entries)
    print(f"recorded within-source saturation for {len(plans)} sources")


CROSS_CANDIDATE_FIELDS = {
    "synthesis_id",
    "title",
    "parent_unit_ids",
    "claim",
    "historical_or_program_relation",
    "limits",
}

CROSS_PANELS = {
    "analytic_prime_zero": {
        "analytic-foundations", "explicit-formula", "primes-zeros", "prime-number-theorem",
        "analytic-continuation", "functional-equation", "prime-counting",
    },
    "zero_distribution": {
        "zero-density", "zero-free-region", "zero-free-regions", "critical-line",
        "critical-line-zeros", "partial-results", "zeros", "exponential-sums",
    },
    "moments_statistics": {
        "mean-values", "mean-values-moments", "moments", "mollifier", "pair-correlation",
        "random-matrix", "zero-statistics", "zero-statistics-random-matrix", "value-distribution",
    },
    "spectral_programs": {
        "spectral", "spectral-physics", "hilbert-polya", "trace-formula",
        "noncommutative-geometry", "arithmetic-quantum-chaos",
    },
    "equivalent_criteria": {
        "equivalent-criteria", "nyman-beurling", "approximation", "arithmetic-functions",
        "reformulation", "weil-positivity",
    },
    "l_functions_geometry": {
        "l-functions", "l-functions-families", "grh", "finite-fields",
        "finite-field-analogues", "weil-conjectures", "cohomology", "symmetry-types",
    },
    "computation_dynamics": {
        "computation", "explicit-computation", "numerical-evidence", "interval-arithmetic",
        "debruijn-newman", "heat-flow", "zero-dynamics", "riemann-siegel",
    },
    "history_obstructions": {
        "history", "historical-foundational", "failed-approaches", "failed-or-limited-approaches",
        "obstruction", "obstructions", "limitations", "epistemic-limits", "speculative-program",
    },
}

# The issue-46 handoff exposed only generic ``riemann_zeta`` / ``riemann_hypothesis``
# mechanism tags for most sources.  Route those sources once, by their inspected
# mathematics, so weak discovery metadata cannot silently exclude them from the
# bounded cross-source panels.  This is an execution aid, not a corpus ontology.
CROSS_PANEL_SOURCE_OVERRIDES = {
    "analytic_prime_zero": {
        "openalex_w1515754334",
        "openalex_w1966384992",
        "openalex_w1987559074",
        "openalex_w2150541646",
    },
    "zero_distribution": {
        "openalex_w2031421669",
    },
    "moments_statistics": {
        "openalex_w2055983684",
        "openalex_w2278237719",
        "openalex_w2609909332",
        "openalex_w2949840527",
        "openalex_w986718947",
    },
    "spectral_programs": {
        "openalex_w1966546572",
        "openalex_w2141932395",
    },
    "l_functions_geometry": {
        "openalex_w1602172244",
        "openalex_w1981597330",
        "openalex_w2237579816",
    },
}


def _evenly_select(values: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    if len(values) <= limit:
        return values
    if limit == 1:
        return [values[len(values) // 2]]
    indices = sorted({round(index * (len(values) - 1) / (limit - 1)) for index in range(limit)})
    return [values[index] for index in indices]


def prepare_cross_source_generation_assignments(v2_artifact_root: Path) -> None:
    units = {row["unit_id"]: row for row in load_jsonl(DEPTH_UNITS_PATH)}
    revised = {
        row["unit_id"]: row["output"]
        for row in load_jsonl(PASS_FILES["revised"])
        if row["output"]["decision"] == "accepted"
    }
    inventory = {row["source_id"]: row for row in load_jsonl(DEPTH_INVENTORY_PATH)}
    dossiers = {row["source_id"]: row for row in load_jsonl(SOURCE_DOSSIERS_PATH)}
    by_source: dict[str, list[dict[str, Any]]] = {}
    for unit_id, output in revised.items():
        unit = units[unit_id]
        by_source.setdefault(unit["source_id"], []).append(
            {
                "unit_id": unit_id,
                "source_id": unit["source_id"],
                "source_title": inventory[unit["source_id"]]["title"],
                "source_year": inventory[unit["source_id"]]["year"],
                "source_viewpoint_tags": inventory[unit["source_id"]].get("viewpoint_tags") or [],
                "unit_title": unit["title"],
                "unit_type": unit["unit_type"],
                "nonparaphrase_operation": output["nonparaphrase_operation"],
                "interpretation": output["interpretation"],
                "unit_artifact_abspath": str(v2_artifact_root / unit["unit_artifact_relpath"]),
                "source_dossier_binding": {
                    "dossier_id": dossiers[unit["source_id"]]["dossier_id"],
                    "dossier_sha256": dossiers[unit["source_id"]]["dossier_sha256"],
                },
            }
        )
    representatives = {
        source_id: _evenly_select(sorted(rows, key=lambda row: row["unit_id"]), 6)
        for source_id, rows in by_source.items()
    }
    CROSS_GENERATION_ASSIGNMENT_ROOT.mkdir(parents=True, exist_ok=True)
    for path in CROSS_GENERATION_ASSIGNMENT_ROOT.glob("*.json"):
        path.unlink()
    prompt_path = V2_ROOT / "prompts" / "cross_source_synthesis_generation.md"
    for panel_id, tags in CROSS_PANELS.items():
        source_overrides = CROSS_PANEL_SOURCE_OVERRIDES.get(panel_id, set())
        panel_sources = [
            source_id
            for source_id, source in inventory.items()
            if source_id in representatives
            and (
                tags.intersection(source.get("viewpoint_tags") or [])
                or source_id in source_overrides
            )
        ]
        items = [row for source_id in sorted(panel_sources) for row in representatives[source_id]]
        output_path = CROSS_GENERATION_BATCH_ROOT / f"{panel_id}.jsonl"
        if output_path.is_file():
            raise ValueError(
                f"{output_path.name}: stale cross-generation output must be archived or reconciled"
            )
        write_json(
            CROSS_GENERATION_ASSIGNMENT_ROOT / f"{panel_id}.json",
            _bind_model_visible_packet({
                "task": "cross-source mechanism synthesis generation",
                "panel_id": panel_id,
                "required_synthesis_id_prefix": f"riemann_v2_cross_{panel_id}_",
                "execution_brief_path": str(EXECUTION_BRIEF_PATH),
                "execution_brief_sha256": sha256_file(EXECUTION_BRIEF_PATH),
                "prompt_path": str(prompt_path),
                "prompt_sha256": sha256_file(prompt_path),
                "output_path": str(output_path),
                "source_count": len(panel_sources),
                "unit_index_count": len(items),
                "unit_index": items,
            }),
        )
    print(f"prepared {len(CROSS_PANELS)} cross-source conceptual panels")


def combine_cross_source_candidates() -> None:
    units = {row["unit_id"]: row for row in load_jsonl(DEPTH_UNITS_PATH)}
    accepted = {
        row["unit_id"]
        for row in load_jsonl(PASS_FILES["revised"])
        if row["output"]["decision"] == "accepted"
    }
    combined: list[dict[str, Any]] = []
    seen: set[str] = set()
    for assignment_path in sorted(CROSS_GENERATION_ASSIGNMENT_ROOT.glob("*.json")):
        assignment = load_json(assignment_path)
        output_path = Path(assignment["output_path"])
        if not output_path.is_file():
            raise ValueError(f"{assignment_path.name}: missing cross-source generation output")
        for row in load_jsonl(output_path):
            if set(row) != CROSS_CANDIDATE_FIELDS:
                raise ValueError(f"{row.get('synthesis_id')}: cross candidate fields mismatch")
            synthesis_id = str(row["synthesis_id"])
            if not synthesis_id.startswith(assignment["required_synthesis_id_prefix"]):
                raise ValueError(f"{synthesis_id}: wrong panel-specific id prefix")
            if synthesis_id in seen:
                raise ValueError(f"duplicate cross synthesis id: {synthesis_id}")
            seen.add(synthesis_id)
            parents = row["parent_unit_ids"]
            if len(parents) < 2 or len(parents) != len(set(parents)) or not set(parents).issubset(accepted):
                raise ValueError(f"{synthesis_id}: unresolved/non-accepted parent units")
            if len({units[unit_id]["source_id"] for unit_id in parents}) < 2:
                raise ValueError(f"{synthesis_id}: cross synthesis needs distinct sources")
            combined.append({**row, "generation_panel": assignment["panel_id"]})
    write_jsonl(CROSS_SYNTHESIS_CANDIDATES_PATH, combined)
    print(f"combined {len(combined)} cross-source synthesis candidates")


def prepare_cross_source_adjudication_assignments(v2_artifact_root: Path) -> None:
    candidates = load_jsonl(CROSS_SYNTHESIS_CANDIDATES_PATH)
    units = {row["unit_id"]: row for row in load_jsonl(DEPTH_UNITS_PATH)}
    revised = {row["unit_id"]: row["output"] for row in load_jsonl(PASS_FILES["revised"])}
    inventory = {row["source_id"]: row for row in load_jsonl(DEPTH_INVENTORY_PATH)}
    dossiers = {row["source_id"]: row for row in load_jsonl(SOURCE_DOSSIERS_PATH)}
    by_panel: dict[str, list[dict[str, Any]]] = {}
    for candidate in candidates:
        parents = []
        for unit_id in candidate["parent_unit_ids"]:
            unit = units[unit_id]
            parents.append(
                {
                    **unit,
                    "unit_artifact_abspath": str(v2_artifact_root / unit["unit_artifact_relpath"]),
                    "source_title": inventory[unit["source_id"]]["title"],
                    "accepted_interpretation": revised[unit_id],
                    "source_dossier_binding": {
                        "dossier_id": dossiers[unit["source_id"]]["dossier_id"],
                        "dossier_sha256": dossiers[unit["source_id"]]["dossier_sha256"],
                    },
                }
            )
        by_panel.setdefault(candidate["generation_panel"], []).append(
            {"candidate": candidate, "parents": parents}
        )
    prompt_path = V2_ROOT / "prompts" / "cross_source_synthesis_adjudication.md"
    CROSS_ADJUDICATION_ASSIGNMENT_ROOT.mkdir(parents=True, exist_ok=True)
    for path in CROSS_ADJUDICATION_ASSIGNMENT_ROOT.glob("*.json"):
        path.unlink()
    for panel_id, items in sorted(by_panel.items()):
        output_path = CROSS_ADJUDICATION_BATCH_ROOT / f"{panel_id}.jsonl"
        if output_path.is_file():
            raise ValueError(
                f"{output_path.name}: stale cross-adjudication output must be archived or reconciled"
            )
        write_json(
            CROSS_ADJUDICATION_ASSIGNMENT_ROOT / f"{panel_id}.json",
            _bind_model_visible_packet({
                "task": "fresh cross-source synthesis adjudication",
                "panel_id": panel_id,
                "execution_brief_path": str(EXECUTION_BRIEF_PATH),
                "execution_brief_sha256": sha256_file(EXECUTION_BRIEF_PATH),
                "prompt_path": str(prompt_path),
                "prompt_sha256": sha256_file(prompt_path),
                "output_path": str(output_path),
                "candidate_count": len(items),
                "candidates": items,
            }),
        )
    print(f"prepared cross-source adjudication for {len(candidates)} candidates")


def combine_cross_source_synthesis() -> None:
    candidates = load_jsonl(CROSS_SYNTHESIS_CANDIDATES_PATH)
    by_id = {row["synthesis_id"]: row for row in candidates}
    finals: dict[str, dict[str, Any]] = {}
    contexts: dict[str, str] = {}
    for assignment_path in sorted(CROSS_ADJUDICATION_ASSIGNMENT_ROOT.glob("*.json")):
        assignment = load_json(assignment_path)
        expected = [row["candidate"]["synthesis_id"] for row in assignment["candidates"]]
        output_path = Path(assignment["output_path"])
        if not output_path.is_file():
            raise ValueError(f"{assignment_path.name}: missing cross-source adjudication")
        records = load_jsonl(output_path)
        if [row.get("synthesis_id") for row in records] != expected:
            raise ValueError(f"{output_path.name}: cross-source adjudication order mismatch")
        for row in records:
            if set(row) != SYNTHESIS_FINAL_FIELDS:
                raise ValueError(f"{row.get('synthesis_id')}: cross final fields mismatch")
            if row.get("decision") not in {"accepted", "quarantined", "rejected"}:
                raise ValueError(f"{row.get('synthesis_id')}: invalid cross decision")
            finals[row["synthesis_id"]] = row
            contexts[row["synthesis_id"]] = f"collaboration-agent:cross-adjudication:{assignment['panel_id']}"
    if set(finals) != set(by_id):
        raise ValueError("cross-source adjudication does not cover the exact candidate set")
    prompt_path = V2_ROOT / "prompts" / "cross_source_synthesis_adjudication.md"
    records = []
    for candidate in candidates:
        final = finals[candidate["synthesis_id"]]
        records.append(
            {
                **candidate,
                **{key: final[key] for key in SYNTHESIS_FINAL_FIELDS if key != "synthesis_id"},
                "teacher_provenance": {
                    "provider": "openai",
                    "model": "gpt-5.6-sol",
                    "reasoning_effort": "xhigh",
                    "client": "codex-collaboration-agent",
                    "execution_context_id": contexts[candidate["synthesis_id"]],
                    "prompt_relpath": prompt_path.relative_to(V2_ROOT).as_posix(),
                    "prompt_sha256": sha256_file(prompt_path),
                },
            }
        )
    write_jsonl(CROSS_SYNTHESIS_FINAL_PATH, records)
    print(f"combined final decisions for {len(records)} cross-source syntheses")


def _artifact_content_loader(v2_artifact_root: Path):
    def load(record: Mapping[str, Any]) -> str:
        if isinstance(record.get("content"), str):
            return str(record["content"])
        reference = str(record.get("content_ref") or "")
        roots = {
            "artifact://riemann-corpus-v0/": pipeline.DEFAULT_ARTIFACT_ROOT,
            "artifact://riemann-corpus-v2/": v2_artifact_root,
        }
        for prefix, root in roots.items():
            if reference.startswith(prefix):
                return (root / reference.removeprefix(prefix)).read_text(encoding="utf-8")
        raise ValueError(f"unsupported content reference: {reference}")

    return load


def _v2_source_keys(source: Mapping[str, Any], unit: Mapping[str, Any]) -> list[str]:
    keys = {
        f"source-id:{source['source_id']}",
        f"source-unit-id:{unit['unit_id']}",
        f"unit-sha256:{unit['unit_sha256']}",
    }
    for kind, value in (source.get("identifiers") or {}).items():
        if value:
            keys.add(f"{kind}:{str(value).lower()}")
    return sorted(keys)


def _v2_source_license(source: Mapping[str, Any]) -> str:
    selected_id = source.get("selected_candidate_id")
    candidate = next(
        (row for row in source.get("candidates") or [] if row.get("candidate_id") == selected_id),
        None,
    )
    if candidate is None or "reported_license" not in candidate:
        license_note = (candidate or {}).get("license") or "no redistribution grant located"
        return (
            "source text external-local-not-git; reported access boundary: "
            f"{license_note}; metadata and derived teacher interpretation are repository-retained"
        )
    reported_license = candidate.get("reported_license")
    access_boundary = (candidate or {}).get("access_boundary") or (
        "no redistribution grant located"
    )
    return (
        "source text external-local-not-git; "
        f"route-bound reported license={reported_license!r}; "
        f"access boundary={access_boundary}; metadata and derived teacher interpretation "
        "are repository-retained"
    )


def _selected_artifact_warnings(source: Mapping[str, Any]) -> list[Any]:
    return list((source.get("selected_artifact") or {}).get("warnings") or [])


def _v2_sidecars(unit: Mapping[str, Any]) -> list[dict[str, Any]]:
    dependency = str(unit.get("representation_dependency") or "").strip()
    if not dependency or dependency.lower() in {"none", "none identified", "not required"}:
        return []
    return [
        {
            "asset_id": f"representation-for-{unit['unit_id']}",
            "relationship": "provenance_only",
            "availability": "unavailable",
            "content_ref": None,
            "content_sha256": None,
        }
    ]


def build_objects(v2_artifact_root: Path) -> None:
    """Build one canonical v2 release while preserving every v1 object as parent lineage."""
    acquisition = {row["source_id"]: row for row in load_jsonl(ACQUISITION_SEARCH_PATH)}
    units = load_jsonl(DEPTH_UNITS_PATH)
    revised = {row["unit_id"]: row for row in load_jsonl(PASS_FILES["revised"])}
    analyses_by_unit: dict[str, list[str]] = {}
    for path in PASS_FILES.values():
        for row in load_jsonl(path):
            analyses_by_unit.setdefault(row["unit_id"], []).append(row["analysis_id"])

    objects: list[dict[str, Any]] = []
    object_ids: set[str] = set()

    def add(record: dict[str, Any]) -> None:
        object_id = str(record["object_id"])
        if object_id in object_ids:
            raise ValueError(f"duplicate v2 object id: {object_id}")
        object_ids.add(object_id)
        objects.append(record)

    unit_to_source_object: dict[str, str] = {}
    for parent_record in load_jsonl(V1_ROOT / "objects.jsonl"):
        carried = json.loads(json.dumps(parent_record))
        carried["corpus_release_id"] = V2_RELEASE_ID
        carried["derivation_ids"] = list(carried.get("derivation_ids") or []) + [
            f"carried-unchanged-from:{V1_FREEZE_ID}"
        ]
        audit = dict(carried.get("corpus_local_audit") or {})
        audit["parent_release_id"] = V1_RELEASE_ID
        audit["parent_freeze_id"] = V1_FREEZE_ID
        carried["corpus_local_audit"] = audit
        add(carried)
        if carried["object_role"] == "source":
            for unit_id in carried.get("source_unit_ids") or []:
                unit_to_source_object[unit_id] = carried["object_id"]

    source_record_by_object = {
        row["object_id"]: row for row in objects if row["object_role"] == "source"
    }
    for unit in units:
        source = acquisition[unit["source_id"]]
        content_path = v2_artifact_root / unit["unit_artifact_relpath"]
        content = interchange.normalize_visible_text(content_path.read_text(encoding="utf-8"))
        content_hash = interchange.sha256_text(content)
        keys = _v2_source_keys(source, unit)
        object_id = interchange.stable_object_id("source", content_hash, keys, [])
        record = {
            "contract_version": interchange.CONTRACT_VERSION,
            "corpus_release_id": V2_RELEASE_ID,
            "object_id": object_id,
            "object_role": "source",
            "corpus_origin": "riemann",
            "source_ids": [unit["source_id"]],
            "source_unit_ids": [unit["unit_id"]],
            "span_lineage": [
                {
                    "source_id": unit["source_id"],
                    "source_unit_id": unit["unit_id"],
                    "source_span_kind": unit["source_span_kind"],
                    "line_start": unit["line_start"],
                    "line_end": unit["line_end"],
                    "source_pages": unit.get("source_page_markers_inside_unit") or [],
                    "source_normalized_sha256": unit["source_normalized_sha256"],
                    "unit_sha256": unit["unit_sha256"],
                }
            ],
            "content_sha256": content_hash,
            "content_ref": "artifact://riemann-corpus-v2/" + unit["unit_artifact_relpath"],
            "parent_ids": [],
            "derivation_ids": [unit["segmentation_provenance"]],
            "teacher_provenance": {
                "kind": "semantic-unit-extraction",
                "model": "gpt-5.6-sol",
                "source_release_parent": V1_RELEASE_ID,
            },
            "quality_state": "accepted",
            "training_eligibility": "eligible",
            "exclusion_reason": None,
            "licensing_boundary": _v2_source_license(source),
            "representation_dependencies": _v2_sidecars(unit),
            "canonical_source_keys": keys,
            "corpus_local_audit": {
                "unit_type": unit["unit_type"],
                "title": unit["title"],
                "selection_reason": unit["selection_reason"],
                "context_note": unit["context_note"],
                "representation_dependency": unit["representation_dependency"],
                "parent_release_id": V1_RELEASE_ID,
                "extraction_warnings": _selected_artifact_warnings(source),
                **(
                    {
                        "issue_46_handoff_provenance": source[
                            "issue_46_handoff_provenance"
                        ]
                    }
                    if source.get("issue_46_handoff_provenance")
                    else {}
                ),
            },
        }
        add(record)
        unit_to_source_object[unit["unit_id"]] = object_id
        source_record_by_object[object_id] = record

    for unit in units:
        analysis = revised[unit["unit_id"]]
        output = analysis["output"]
        content = interchange.normalize_visible_text(output["interpretation"])
        content_hash = interchange.sha256_text(content)
        parent_id = unit_to_source_object[unit["unit_id"]]
        parent = source_record_by_object[parent_id]
        quality_state = output["decision"]
        if quality_state == "accepted":
            exclusion = None
            eligibility = "eligible"
        else:
            exclusion = output["quality_reason"]
            eligibility = "ineligible"
        add(
            {
                "contract_version": interchange.CONTRACT_VERSION,
                "corpus_release_id": V2_RELEASE_ID,
                "object_id": interchange.stable_object_id(
                    "interpretation", content_hash, parent["canonical_source_keys"], [parent_id]
                ),
                "object_role": "interpretation",
                "corpus_origin": "riemann",
                "source_ids": parent["source_ids"],
                "source_unit_ids": [unit["unit_id"]],
                "span_lineage": parent["span_lineage"],
                "content_sha256": content_hash,
                "content": content,
                "parent_ids": [parent_id],
                "derivation_ids": analyses_by_unit[unit["unit_id"]],
                "teacher_provenance": analysis["teacher_provenance"],
                "quality_state": quality_state,
                "training_eligibility": eligibility,
                "exclusion_reason": exclusion,
                "licensing_boundary": "derived teacher interpretation retained in Git; source remains external",
                "representation_dependencies": [],
                "canonical_source_keys": parent["canonical_source_keys"],
                "corpus_local_audit": {
                    "source_support": output["source_support"],
                    "nonparaphrase_operation": output["nonparaphrase_operation"],
                    "speculation_status": output["speculation_status"],
                    "quality_reason": output["quality_reason"],
                    "parent_release_id": V1_RELEASE_ID,
                },
            }
        )

    def add_synthesis(row: Mapping[str, Any], kind: str) -> None:
        parent_unit_ids = list(row["parent_unit_ids"])
        parent_ids = [unit_to_source_object[unit_id] for unit_id in parent_unit_ids]
        parent_records = [source_record_by_object[parent_id] for parent_id in parent_ids]
        content = interchange.normalize_visible_text(str(row["synthesis"]))
        content_hash = interchange.sha256_text(content)
        keys = sorted({key for parent in parent_records for key in parent["canonical_source_keys"]})
        quality_state = str(row["decision"])
        add(
            {
                "contract_version": interchange.CONTRACT_VERSION,
                "corpus_release_id": V2_RELEASE_ID,
                "object_id": interchange.stable_object_id("synthesis", content_hash, keys, parent_ids),
                "object_role": "synthesis",
                "corpus_origin": "riemann",
                "source_ids": sorted({value for parent in parent_records for value in parent["source_ids"]}),
                "source_unit_ids": parent_unit_ids,
                "span_lineage": [span for parent in parent_records for span in parent["span_lineage"]],
                "content_sha256": content_hash,
                "content": content,
                "parent_ids": parent_ids,
                "derivation_ids": [str(row["synthesis_id"])],
                "teacher_provenance": row["teacher_provenance"],
                "quality_state": quality_state,
                "training_eligibility": "eligible" if quality_state == "accepted" else "ineligible",
                "exclusion_reason": None if quality_state == "accepted" else row["quality_reason"],
                "licensing_boundary": "derived teacher synthesis retained in Git; source texts remain external",
                "representation_dependencies": [],
                "canonical_source_keys": keys,
                "corpus_local_audit": {
                    "synthesis_kind": kind,
                    "source_support": row["source_support"],
                    "nonparaphrase_operation": row["nonparaphrase_operation"],
                    "limits": row["limits"],
                    "quality_reason": row["quality_reason"],
                },
            }
        )

    for row in load_jsonl(WITHIN_SYNTHESIS_FINAL_PATH):
        add_synthesis(row, "within-source")
    for row in load_jsonl(CROSS_SYNTHESIS_FINAL_PATH):
        add_synthesis(row, "cross-source")
    write_jsonl(OBJECTS_PATH, objects)
    print(f"built {len(objects)} canonical v2 objects, including {len(load_jsonl(V1_ROOT / 'objects.jsonl'))} carried v1 objects")


def write_trainable_manifest(v2_artifact_root: Path) -> None:
    records = load_jsonl(OBJECTS_PATH)
    errors = interchange.validate_release(records, _artifact_content_loader(v2_artifact_root))
    if errors:
        raise ValueError("invalid v2 interchange release:\n" + "\n".join(errors))
    eligible = [row for row in records if row["training_eligibility"] == "eligible"]
    identity = {
        "contract_version": interchange.CONTRACT_VERSION,
        "corpus_release_id": V2_RELEASE_ID,
        "parent_release_id": V1_RELEASE_ID,
        "parent_freeze_id": V1_FREEZE_ID,
        "renderer_sha256": sha256_file(Path(interchange.__file__)),
        "eligible_object_ids": [row["object_id"] for row in eligible],
        "object_counts": dict(sorted(Counter(row["object_role"] for row in eligible).items())),
    }
    write_json(
        TRAINABLE_MANIFEST_PATH,
        {
            **identity,
            "manifest_id": "riemann_v2_trainable_" + sha256_text(canonical_json(identity)),
            "purpose": "corpus packaging only; no training or mixing-ratio authorization",
        },
    )
    print(f"wrote v2 trainable manifest with {len(eligible)} eligible objects")


AUDIT_FIELDS = {
    "object_id",
    "decision",
    "faithfulness",
    "context_sufficiency",
    "nonparaphrase_value",
    "specificity",
    "representation_sensitivity",
    "uncertainty_discipline",
    "duplicate_or_version_risk",
    "conceptual_ecosystem_contribution",
    "notes",
}


def _validate_independent_audit_row(row: Mapping[str, Any], context: str) -> None:
    if set(row) != AUDIT_FIELDS:
        raise ValueError(f"{context}: independent audit fields mismatch")
    if row.get("decision") not in {"accept", "quarantine", "reject"}:
        raise ValueError(f"{context}: invalid audit decision")
    if row.get("conceptual_ecosystem_contribution") not in {
        "new_mechanism",
        "refinement_or_relation",
        "repeats_represented_mechanism",
        "unresolved",
    }:
        raise ValueError(f"{context}: invalid ecosystem contribution")


def exact_audit_carry(
    current_sample: Sequence[Mapping[str, Any]],
    prior_sample: Sequence[Mapping[str, Any]],
    prior_reviews: Sequence[Mapping[str, Any]],
) -> list[dict[str, Any]]:
    """Carry an audit decision only when the exact model-visible sample is unchanged."""
    prior_packets: dict[str, str] = {}
    for item in prior_sample:
        object_id = str(item.get("object_id") or "")
        if not object_id or object_id in prior_packets:
            raise ValueError(f"invalid or duplicate prior audit sample object: {object_id}")
        prior_packets[object_id] = audit_sample_packet_sha256(item)
    reviews: dict[str, dict[str, Any]] = {}
    for raw in prior_reviews:
        row = dict(raw)
        object_id = str(row.get("object_id") or "")
        _validate_independent_audit_row(row, object_id or "prior audit row")
        if object_id in reviews:
            raise ValueError(f"duplicate prior audit review object: {object_id}")
        reviews[object_id] = row
    carried: list[dict[str, Any]] = []
    seen: set[str] = set()
    for item in current_sample:
        object_id = str(item.get("object_id") or "")
        if not object_id or object_id in seen:
            raise ValueError(f"invalid or duplicate current audit sample object: {object_id}")
        seen.add(object_id)
        if (
            object_id in reviews
            and prior_packets.get(object_id) == audit_sample_packet_sha256(item)
        ):
            carried.append(reviews[object_id])
    return carried


def validate_exact_audit_carry() -> list[str]:
    if not AUDIT_SAMPLE_PATH.is_file() or not AUDIT_CARRIED_PATH.is_file():
        return ["canonical audit sample/carry ledger is missing"]
    sample = load_jsonl(AUDIT_SAMPLE_PATH)
    expected_by_id: dict[str, dict[str, Any]] = {}
    carry_ledgers = [
        (PRE_OPENALEX_AUDIT_SAMPLE_PATH, PRE_OPENALEX_AUDIT_FINAL_PATH),
        (
            ISOLATION_ARCHIVE_ROOT / "reconciliation/artifacts/audit/sample.jsonl",
            ISOLATION_ARCHIVE_ROOT
            / "reconciliation/artifacts/audit/independent_review.jsonl",
        ),
    ]
    try:
        for prior_sample_path, prior_review_path in carry_ledgers:
            if not prior_sample_path.is_file() or not prior_review_path.is_file():
                continue
            for row in exact_audit_carry(
                sample, load_jsonl(prior_sample_path), load_jsonl(prior_review_path)
            ):
                object_id = str(row["object_id"])
                prior = expected_by_id.get(object_id)
                if prior is not None and prior != row:
                    return [f"conflicting exact audit carry decisions: {object_id}"]
                expected_by_id[object_id] = row
    except ValueError as error:
        return [str(error)]
    expected = [
        expected_by_id[row["object_id"]]
        for row in sample
        if row["object_id"] in expected_by_id
    ]
    if load_jsonl(AUDIT_CARRIED_PATH) != expected:
        return ["audit carry differs from exact canonical sample-packet equality"]
    return []


def prepare_independent_audit(v2_artifact_root: Path, batch_count: int) -> None:
    if batch_count < 1:
        raise ValueError("audit batch_count must be positive")
    stale_outputs = sorted(AUDIT_BATCH_ROOT.glob("*.jsonl"))
    if stale_outputs:
        raise ValueError(
            "audit outputs already exist; archive or reconcile them before preparing replacements"
        )
    records = load_jsonl(OBJECTS_PATH)
    by_id = {row["object_id"]: row for row in records}
    depth_units = {row["unit_id"]: row for row in load_jsonl(DEPTH_UNITS_PATH)}
    inventory = {row["source_id"]: row for row in load_jsonl(DEPTH_INVENTORY_PATH)}
    depth_counts = Counter(row["source_id"] for row in depth_units.values())
    candidates = [
        row
        for row in records
        if row["object_role"] in {"interpretation", "synthesis"}
        and not any(str(value).startswith("carried-unchanged-from:") for value in row["derivation_ids"])
    ]
    selected_ids: set[str] = {
        row["object_id"] for row in candidates if row["quality_state"] != "accepted"
    }
    syntheses = sorted(
        (row for row in candidates if row["object_role"] == "synthesis"),
        key=lambda row: row["object_id"],
    )
    # Updated #42 policy: audit 100% of synthesis and negative/high-risk OCR
    # objects, then stratify the lower-risk accepted remainder.
    selected_ids.update(row["object_id"] for row in syntheses)
    interpretations_by_source: dict[str, list[dict[str, Any]]] = {}
    for row in candidates:
        if row["object_role"] == "interpretation":
            interpretations_by_source.setdefault(row["source_ids"][0], []).append(row)
    for source_id, source_rows in interpretations_by_source.items():
        source = inventory[source_id]
        if source["extraction_confidence"] == "ocr-lower-confidence":
            selected_ids.update(row["object_id"] for row in source_rows)
            continue
        sample_size = 1
        if source["extraction_confidence"] == "ocr-lower-confidence":
            sample_size = 3
        if int(source.get("normalized_page_count") or 0) >= 30:
            sample_size = max(sample_size, 2)
        if depth_counts[source_id] >= 20:
            sample_size = max(sample_size, 3)
        chosen = _evenly_select(sorted(source_rows, key=lambda row: row["object_id"]), sample_size)
        selected_ids.update(row["object_id"] for row in chosen)
    selected = [row for row in candidates if row["object_id"] in selected_ids]
    selected.sort(key=lambda row: (row["object_role"], row["source_ids"], row["object_id"]))

    def parent_sources(record: Mapping[str, Any]) -> list[dict[str, Any]]:
        parents = []
        for parent_id in record["parent_ids"]:
            parent = by_id[parent_id]
            source_id = parent["source_ids"][0]
            item = {
                "source_object_id": parent_id,
                "source_id": source_id,
                "source_unit_ids": parent["source_unit_ids"],
                "content_ref": parent.get("content_ref"),
                "source_title": inventory.get(source_id, {}).get("title"),
                "source_year": inventory.get(source_id, {}).get("year"),
                "source_type": inventory.get(source_id, {}).get("source_type"),
                "viewpoint_tags": inventory.get(source_id, {}).get("viewpoint_tags") or [],
                "ocr": inventory.get(source_id, {}).get("extraction_confidence") == "ocr-lower-confidence",
                "long_form": int(inventory.get(source_id, {}).get("normalized_page_count") or 0) >= 30,
            }
            reference = str(parent.get("content_ref") or "")
            if reference.startswith("artifact://riemann-corpus-v2/"):
                content_path = (
                    v2_artifact_root / reference.removeprefix("artifact://riemann-corpus-v2/")
                )
            elif reference.startswith("artifact://riemann-corpus-v0/"):
                content_path = (
                    pipeline.DEFAULT_ARTIFACT_ROOT
                    / reference.removeprefix("artifact://riemann-corpus-v0/")
                )
            else:
                raise ValueError(f"unsupported audit parent content reference: {reference}")
            item["content_abspath"] = str(content_path)
            item["content_sha256"] = parent["content_sha256"]
            item["artifact_sha256"] = sha256_file(content_path)
            item["artifact_bytes"] = content_path.stat().st_size
            parents.append(item)
        return parents

    sample = []
    for row in selected:
        source_ids = sorted(set(row["source_ids"]))
        if len(source_ids) == 1:
            context_group = "source:" + source_ids[0]
        else:
            derivation = " ".join(str(value) for value in row.get("derivation_ids") or [])
            panel = next(
                (panel_id for panel_id in CROSS_PANELS if f"cross_{panel_id}_" in derivation),
                "cross-source-mixed",
            )
            context_group = "synthesis-panel:" + panel
        sample.append(
            {
                "object_id": row["object_id"],
                "object_role": row["object_role"],
                "proposed_content": row["content"],
                "parent_sources": parent_sources(row),
                "audit_context_group": context_group,
                "audit_strata": {
                    "source_count": len(set(row["source_ids"])),
                    "source_types": sorted({inventory.get(sid, {}).get("source_type") for sid in row["source_ids"]}),
                    "viewpoint_tags": sorted({tag for sid in row["source_ids"] for tag in inventory.get(sid, {}).get("viewpoint_tags") or []}),
                    "ocr": any(inventory.get(sid, {}).get("extraction_confidence") == "ocr-lower-confidence" for sid in row["source_ids"]),
                    "long_form": any(int(inventory.get(sid, {}).get("normalized_page_count") or 0) >= 30 for sid in row["source_ids"]),
                    "depth": max((depth_counts[sid] for sid in row["source_ids"]), default=0),
                },
            }
        )
    write_jsonl(AUDIT_SAMPLE_PATH, sample)
    carry_ledgers = [
        (PRE_OPENALEX_AUDIT_SAMPLE_PATH, PRE_OPENALEX_AUDIT_FINAL_PATH),
        (
            ISOLATION_ARCHIVE_ROOT / "reconciliation" / "artifacts" / "audit" / "sample.jsonl",
            ISOLATION_ARCHIVE_ROOT
            / "reconciliation"
            / "artifacts"
            / "audit"
            / "independent_review.jsonl",
        ),
    ]
    carried_by_id: dict[str, dict[str, Any]] = {}
    for prior_sample_path, prior_review_path in carry_ledgers:
        if not prior_sample_path.is_file() or not prior_review_path.is_file():
            continue
        for row in exact_audit_carry(
            sample, load_jsonl(prior_sample_path), load_jsonl(prior_review_path)
        ):
            object_id = str(row["object_id"])
            prior = carried_by_id.get(object_id)
            if prior is not None and prior != row:
                raise ValueError(f"conflicting exact audit carry decisions: {object_id}")
            carried_by_id[object_id] = row
    carried = [carried_by_id[row["object_id"]] for row in sample if row["object_id"] in carried_by_id]
    carried_ids = set(carried_by_id)
    write_jsonl(AUDIT_CARRIED_PATH, carried)
    grouped: dict[str, list[dict[str, Any]]] = {}
    for item in sample:
        if item["object_id"] in carried_ids:
            continue
        grouped.setdefault(item["audit_context_group"], []).append(item)
    prompt_path = V2_ROOT / "prompts" / "independent_stratified_audit.md"
    AUDIT_ASSIGNMENT_ROOT.mkdir(parents=True, exist_ok=True)
    for path in AUDIT_ASSIGNMENT_ROOT.glob("*.json"):
        path.unlink()
    AUDIT_BATCH_ROOT.mkdir(parents=True, exist_ok=True)
    context_count = 0
    for group_key in sorted(grouped):
        items = sorted(grouped[group_key], key=lambda row: row["object_id"])
        limit = (
            SYNTHESIS_CONTEXT_MAX_CANDIDATES
            if group_key.startswith("synthesis-panel:")
            else SOURCE_CONTEXT_MAX_UNITS
        )
        slug = re.sub(r"[^a-z0-9]+", "_", group_key.lower()).strip("_")[:56]
        group_id = f"{slug}_{sha256_text(group_key)[:8]}"
        for offset in range(0, len(items), limit):
            bucket = items[offset : offset + limit]
            part = offset // limit + 1
            stem = f"{group_id}_part_{part:02d}"
            output_path = AUDIT_BATCH_ROOT / f"{stem}.jsonl"
            write_json(
                AUDIT_ASSIGNMENT_ROOT / f"{stem}.json",
                _bind_model_visible_packet({
                    "stage": (
                        "cross-source-audit"
                        if group_key.startswith("synthesis-panel:")
                        else "audit"
                    ),
                    "task": "fresh-context stratified capability-vs-style and ecosystem audit",
                    "audit_context_group": group_key,
                    "execution_brief_path": str(EXECUTION_BRIEF_PATH),
                    "execution_brief_sha256": sha256_file(EXECUTION_BRIEF_PATH),
                    "prompt_path": str(prompt_path),
                    "prompt_sha256": sha256_file(prompt_path),
                    "output_path": str(output_path),
                    "item_count": len(bucket),
                    "items": bucket,
                }),
            )
            context_count += 1
    print(
        f"prepared 100%-high-risk plus stratified audit sample of {len(sample)} objects "
        f"with {len(carried)} exact pre-OpenAlex decisions carried and "
        f"{len(sample) - len(carried)} new objects across {context_count} "
        "source/panel-coherent contexts"
    )


def combine_independent_audit() -> None:
    sample_ids = [row["object_id"] for row in load_jsonl(AUDIT_SAMPLE_PATH)]
    raw: dict[str, dict[str, Any]] = {}
    if AUDIT_CARRIED_PATH.is_file():
        for row in load_jsonl(AUDIT_CARRIED_PATH):
            object_id = str(row.get("object_id") or "")
            _validate_independent_audit_row(row, object_id or AUDIT_CARRIED_PATH.name)
            if object_id in raw:
                raise ValueError(f"duplicate carried independent audit object: {object_id}")
            raw[object_id] = row
    for assignment_path in sorted(AUDIT_ASSIGNMENT_ROOT.glob("*.json")):
        assignment = load_json(assignment_path)
        expected = [row["object_id"] for row in assignment["items"]]
        output_path = Path(assignment["output_path"])
        if not output_path.is_file():
            raise ValueError(f"{assignment_path.name}: missing independent audit output")
        rows = load_jsonl(output_path)
        if [row.get("object_id") for row in rows] != expected:
            raise ValueError(f"{output_path.name}: audit order/coverage mismatch")
        for row in rows:
            object_id = str(row.get("object_id") or "")
            _validate_independent_audit_row(row, object_id or output_path.name)
            if object_id in raw:
                raise ValueError(f"duplicate independent audit object: {object_id}")
            raw[object_id] = row
    if set(raw) != set(sample_ids):
        raise ValueError("independent audit does not cover the frozen sample")
    write_jsonl(AUDIT_FINAL_PATH, [raw[object_id] for object_id in sample_ids])
    print(f"combined {len(sample_ids)} independent audit decisions")


def apply_independent_audit() -> None:
    audit = {row["object_id"]: row for row in load_jsonl(AUDIT_FINAL_PATH)}
    records = load_jsonl(OBJECTS_PATH)
    for record in records:
        finding = audit.get(record["object_id"])
        if finding is None:
            continue
        prior = record["quality_state"]
        if prior == "accepted" and finding["decision"] in {"quarantine", "reject"}:
            record["quality_state"] = "quarantined" if finding["decision"] == "quarantine" else "rejected"
            record["training_eligibility"] = "ineligible"
            record["exclusion_reason"] = (
                "independent stratified audit: " + str(finding["notes"])
            )
        audit_data = dict(record.get("corpus_local_audit") or {})
        audit_data["independent_v2_audit"] = finding
        audit_data["pre_audit_quality_state"] = prior
        record["corpus_local_audit"] = audit_data
    write_jsonl(OBJECTS_PATH, records)
    print("applied independent audit downgrades without upgrading prior negative labels")


def update_riemann_handoff_state() -> None:
    """Close the Riemann #46 stream from audited, source-linked release evidence."""
    state = load_json(OPENALEX_HANDOFF_STATE_PATH)
    stream = state["streams"]["riemann"]
    consumed = stream.get("consumed") or []
    row = next(
        (
            item
            for item in consumed
            if item.get("handoff_id")
            == AUTHORITATIVE_OPENALEX_HANDOFF_IDS["riemann"]
        ),
        None,
    )
    if row is None:
        raise ValueError("Riemann handoff is not registered as consumed")
    ledger_path = Path(str(row.get("source_disposition_path") or ""))
    if (
        not ledger_path.is_file()
        or sha256_file(ledger_path) != row.get("source_disposition_sha256")
    ):
        raise ValueError("Riemann handoff source-disposition ledger is missing or drifted")
    ledger = load_jsonl(ledger_path)
    processed_source_ids = {
        item["canonical_source_id"]
        for item in ledger
        if item.get("disposition") == "accepted_for_riemann_v2_processing"
    }
    units = [
        item for item in load_jsonl(DEPTH_UNITS_PATH)
        if item["source_id"] in processed_source_ids
    ]
    if {item["source_id"] for item in units} != processed_source_ids:
        raise ValueError("not every accepted Riemann handoff source has semantic units")

    sample_ids = [item["object_id"] for item in load_jsonl(AUDIT_SAMPLE_PATH)]
    audit_rows = load_jsonl(AUDIT_FINAL_PATH)
    if [item.get("object_id") for item in audit_rows] != sample_ids:
        raise ValueError("current independent audit is not complete for the frozen sample")
    audit_by_id = {item["object_id"]: item for item in audit_rows}
    objects = load_jsonl(OBJECTS_PATH)
    for item in objects:
        finding = audit_by_id.get(item["object_id"])
        if finding is not None and (
            (item.get("corpus_local_audit") or {}).get("independent_v2_audit")
            != finding
        ):
            raise ValueError("current independent audit has not been applied to all objects")
    interpretations = [
        item
        for item in objects
        if item.get("object_role") == "interpretation"
        and bool(set(item.get("source_ids") or []) & processed_source_ids)
        and not any(
            str(value).startswith("carried-unchanged-from:")
            for value in item.get("derivation_ids") or []
        )
    ]
    if len(interpretations) != len(units):
        raise ValueError("Riemann handoff unit/interpretation coverage mismatch")
    quality_counts = Counter(item.get("quality_state") for item in interpretations)
    metrics = stream["processing_metrics"]
    metrics.update(
        {
            "sources_processed": len(processed_source_ids),
            "semantic_units": len(units),
            "derivatives_accepted": quality_counts["accepted"],
            "derivatives_quarantined": quality_counts["quarantined"],
            "derivatives_rejected": quality_counts["rejected"],
        }
    )
    row["processing_status"] = "complete"
    state["finalization_allowed"] = _openalex_finalization_allowed(state)
    write_json(OPENALEX_HANDOFF_STATE_PATH, state)
    print("completed the audited Riemann #46 handoff state")


def record_conceptual_saturation() -> None:
    findings = load_jsonl(AUDIT_FINAL_PATH)
    carried_count = (
        len(load_jsonl(AUDIT_CARRIED_PATH)) if AUDIT_CARRIED_PATH.is_file() else 0
    )
    fresh_count = len(findings) - carried_count
    counts = Counter(row["conceptual_ecosystem_contribution"] for row in findings)
    decisions = Counter(row["decision"] for row in findings)
    total_resolved = len(findings) - counts["unresolved"]
    new_fraction = counts["new_mechanism"] / max(1, total_resolved)
    identity = {
        "axis": "conceptual-ecosystem",
        "audit_sample_count": len(findings),
        "contribution_counts": dict(sorted(counts.items())),
        "decision_counts": dict(sorted(decisions.items())),
    }
    entry = {
        **identity,
        "entry_id": "v2_saturation_" + sha256_text(canonical_json(identity)),
        "recorded_at": utc_now(),
        "cross_panel_count": len(CROSS_PANELS),
        "cross_candidate_count": len(load_jsonl(CROSS_SYNTHESIS_CANDIDATES_PATH)),
        "new_mechanism_fraction_among_resolved_sample": new_fraction,
        "status": "established" if new_fraction <= 0.15 else "gaps-recorded",
        "evidence": (
            f"The sample carries {carried_count} decisions only for exact unchanged canonical "
            f"object IDs from the preserved pre-handoff audit; fresh isolated reviewers audited "
            f"the remaining {fresh_count} handoff-affected objects across all major viewpoint "
            "panels. Contributions distinguish candidate new mechanisms from refinements, "
            "relations, repetitions, and unresolved cases. This is teacher audit evidence, not "
            "mathematical truth."
        ),
    }
    entries = [row for row in load_jsonl(SATURATION_LOG_PATH) if row.get("axis") != "conceptual-ecosystem"]
    entries.append(entry)
    write_jsonl(SATURATION_LOG_PATH, entries)
    print("recorded conceptual/ecosystem saturation evidence")


V2_EXIT_DECISIONS = {
    "RIEMANN_MATHIA_CORPUS_V2_READY",
    "MORE_ACQUISITION_NEEDED",
    "MORE_SOURCE_DEPTH_NEEDED",
    "CONCEPTUAL_COVERAGE_GAPS",
    "QUALITY_REGRESSION",
    "INTERCHANGE_BLOCKER",
}


def _ready_acquisition_frontier_errors(final_decision: str) -> list[str]:
    if final_decision != "RIEMANN_MATHIA_CORPUS_V2_READY":
        return []

    errors: list[str] = []
    if not ACQUISITION_RETRY_STATE_PATH.is_file():
        return ["READY requires the persistent acquisition retry state"]
    if not ACQUISITION_SEARCH_PATH.is_file():
        return ["READY requires the acquisition search ledger"]

    recorded_state = load_json(ACQUISITION_RETRY_STATE_PATH)
    max_route_attempts = (recorded_state.get("policy") or {}).get(
        "max_attempts_per_route"
    )
    if not isinstance(max_route_attempts, int) or max_route_attempts < 1:
        errors.append("READY acquisition retry state lacks a positive per-route exhaustion policy")
        max_route_attempts = DEFAULT_MAX_ROUTE_ATTEMPTS
    live_state = _build_acquisition_retry_state(
        load_jsonl(ACQUISITION_SEARCH_PATH), max_route_attempts
    )
    for field in ("routes", "sources", "source_disposition_counts"):
        if recorded_state.get(field) != live_state.get(field):
            errors.append(f"READY acquisition retry state is stale for {field}")

    terminal_dispositions = {"usable", "lawful-routes-exhausted"}
    pending_dispositions = dict(
        sorted(
            Counter(
                source["disposition"]
                for source in live_state["sources"].values()
                if source["disposition"] not in terminal_dispositions
            ).items()
        )
    )
    eligible_routes = [
        route_key
        for route_key, route in live_state["routes"].items()
        if route["disposition"] == "eligible"
        and live_state["sources"][route["source_id"]]["disposition"] != "usable"
    ]
    alternate_searches_pending = sum(
        source["disposition"] == "alternate-version-search-pending"
        for source in live_state["sources"].values()
    )
    if pending_dispositions:
        errors.append(
            "READY acquisition frontier has unresolved source dispositions: "
            f"{pending_dispositions}"
        )
    if eligible_routes:
        errors.append(
            "READY acquisition frontier has eligible lawful routes: "
            f"{eligible_routes[:8]}"
        )
    if alternate_searches_pending:
        errors.append(
            "READY acquisition frontier has pending alternate-version searches: "
            f"{alternate_searches_pending}"
        )

    if not ACQUISITION_FRONTIER_PATH.is_file():
        errors.append("READY requires a terminal acquisition_frontier.json record")
        return errors

    frontier = load_json(ACQUISITION_FRONTIER_PATH)
    live_disposition_counts = dict(
        sorted(
            Counter(
                source["disposition"] for source in live_state["sources"].values()
            ).items()
        )
    )
    proof = {
        "frontier_status": "terminal-practical-lawful-acquisition-saturation",
        "pending_source_dispositions": {},
        "eligible_route_count": 0,
        "alternate_version_search_pending_count": 0,
        "retry_state_source_disposition_counts": live_disposition_counts,
    }
    if any(frontier.get(field) != value for field, value in proof.items()):
        errors.append("READY acquisition frontier lacks a terminal zero-pending proof")

    sentinel = {
        "axis": "acquisition",
        "attempts": 0,
        "recovered_sources": 0,
        "fresh_network_attempts": 0,
        "imported_existing_artifact_attempts": 0,
        "marginal_yield": 0.0,
        "routes": {},
        "outcomes": {"no-unattempted-lawful-candidates": 1},
    }
    if any(frontier.get(field) != value for field, value in sentinel.items()):
        errors.append("READY acquisition frontier lacks the final zero-attempt/zero-yield sentinel")

    frontier_identity_fields = (
        "axis",
        "round_id",
        "frontier_status",
        "attempts",
        "recovered_sources",
        "outcomes",
        "pending_source_dispositions",
        "eligible_route_count",
        "alternate_version_search_pending_count",
        "retry_state_source_disposition_counts",
    )
    frontier_identity = {field: frontier.get(field) for field in frontier_identity_fields}
    if frontier.get("entry_id") != "v2_saturation_" + sha256_text(
        canonical_json(frontier_identity)
    ):
        errors.append("READY acquisition frontier entry identity mismatch")

    if not SATURATION_LOG_PATH.is_file():
        errors.append("READY requires the acquisition saturation log")
    else:
        acquisition_entries = [
            row
            for row in load_jsonl(SATURATION_LOG_PATH)
            if row.get("axis") == "acquisition"
        ]
        if not acquisition_entries or acquisition_entries[-1] != frontier:
            errors.append("READY terminal acquisition frontier is not the final saturation sentinel")
    return errors


def write_mixed_manifest_status() -> None:
    if not OBJECTS_PATH.is_file():
        raise ValueError("Riemann v2 objects are required for the real #42/#44 mixed run")
    riemann_records = load_jsonl(OBJECTS_PATH)
    agnostic_records = load_jsonl(AGNOSTIC_V1_ROOT / "records.jsonl")
    riemann_loader = _artifact_content_loader(DEFAULT_ARTIFACT_ROOT)
    agnostic_loader = lambda record: str(record.get("content") or "")
    riemann_errors = interchange.validate_release(riemann_records, riemann_loader)
    agnostic_errors = interchange.validate_release(agnostic_records, agnostic_loader)
    if riemann_errors or agnostic_errors:
        raise ValueError(
            "real #42/#44 releases failed canonical validation before mixing:\n"
            + "\n".join([*riemann_errors, *agnostic_errors])
        )
    eligible_counts = [
        sum(row.get("training_eligibility") == "eligible" for row in records)
        for records in (riemann_records, agnostic_records)
    ]
    mixed = interchange.materialize_mixed_manifest(
        [riemann_records, agnostic_records],
        [riemann_loader, agnostic_loader],
        per_release=max(eligible_counts),
    )
    write_json(MIXED_MANIFEST_PATH, mixed)
    write_json(
        COMPATIBILITY_STATUS_PATH,
        {
            "contract_version": interchange.CONTRACT_VERSION,
            "riemann_release_id": V2_RELEASE_ID,
            "agnostic_release_id": AGNOSTIC_V1_RELEASE_ID,
            "agnostic_freeze_id": AGNOSTIC_V1_FREEZE_ID,
            "agnostic_merge_commit": AGNOSTIC_V1_MERGE_COMMIT,
            "status": "real-merged-releases-compatible",
            "mixed_manifest_executed": True,
            "mixed_manifest_id": mixed["manifest_id"],
            "eligible_counts": {
                V2_RELEASE_ID: eligible_counts[0],
                AGNOSTIC_V1_RELEASE_ID: eligible_counts[1],
            },
            "selection_counts": dict(
                sorted(Counter(row["corpus_release_id"] for row in mixed["selections"]).items())
            ),
            "reason": (
                "The actual frozen merged #44 release and the actual Riemann v2 objects validate "
                "under the unchanged interchange and were exhaustively passed through the "
                "origin-blind mixed-manifest compatibility path. This selects no training ratio."
            ),
        },
    )
    print("wrote real merged #42/#44 mixed-manifest compatibility evidence")


def validate_mixed_manifest_status() -> list[str]:
    errors: list[str] = []
    if not MIXED_MANIFEST_PATH.is_file() or not COMPATIBILITY_STATUS_PATH.is_file():
        return ["real merged #42/#44 mixed-manifest evidence is missing"]
    status = load_json(COMPATIBILITY_STATUS_PATH)
    mixed = load_json(MIXED_MANIFEST_PATH)
    if (
        status.get("status") != "real-merged-releases-compatible"
        or status.get("mixed_manifest_executed") is not True
        or status.get("agnostic_release_id") != AGNOSTIC_V1_RELEASE_ID
        or status.get("agnostic_freeze_id") != AGNOSTIC_V1_FREEZE_ID
        or status.get("mixed_manifest_id") != mixed.get("manifest_id")
    ):
        errors.append("mixed-manifest status does not bind the merged agnostic release")
    identity = {
        "contract_version": mixed.get("contract_version"),
        "selections": mixed.get("selections") or [],
        "duplicate_groups": mixed.get("duplicate_groups") or [],
    }
    if mixed.get("manifest_id") != "mathia_mixed_" + sha256_text(canonical_json(identity)):
        errors.append("mixed-manifest identity mismatch")
    release_ids = {row.get("corpus_release_id") for row in mixed.get("selections") or []}
    if release_ids != {V2_RELEASE_ID, AGNOSTIC_V1_RELEASE_ID}:
        errors.append("mixed manifest does not select both actual release identities")
    return errors


def freeze_release(final_decision: str) -> None:
    if final_decision not in V2_EXIT_DECISIONS:
        raise ValueError(f"invalid v2 exit decision: {final_decision}")
    receipt_errors = [
        *validate_execution_ledger_receipts(V2_ROOT),
        *validate_exact_audit_carry(),
    ]
    if receipt_errors:
        raise ValueError(
            "cannot freeze without exact execution-ledger receipts:\n"
            + "\n".join(receipt_errors)
        )
    acquisition_errors = _ready_acquisition_frontier_errors(final_decision)
    if acquisition_errors:
        raise ValueError(
            "cannot freeze READY with unresolved acquisition state:\n"
            + "\n".join(acquisition_errors)
        )
    handoff_errors = validate_openalex_handoff_state(
        require_frozen_cutoff=final_decision == "RIEMANN_MATHIA_CORPUS_V2_READY"
    )
    handoff_state = load_json(OPENALEX_HANDOFF_STATE_PATH)
    if (handoff_state.get("processing_cutoff") or {}).get("status") != "frozen":
        handoff_errors.append("#46 finite consumption cutoff is not frozen")
    if handoff_errors:
        raise ValueError(
            "cannot freeze before the finite dual-stream #46 cutoff:\n"
            + "\n".join(handoff_errors)
        )
    paths = [
        path
        for path in sorted(V2_ROOT.rglob("*"))
        if path.is_file()
        and path not in {FREEZE_PATH, RELEASE_MANIFEST_PATH, V2_ROOT / "REPORT.md"}
        and not _is_source_isolation_archive_path(path)
        and "__pycache__" not in path.parts
    ]
    files = [
        {
            "path": path.relative_to(V2_ROOT).as_posix(),
            "sha256": sha256_file(path),
            "bytes": path.stat().st_size,
        }
        for path in paths
    ]
    identity = {
        "contract_version": interchange.CONTRACT_VERSION,
        "corpus_release_id": V2_RELEASE_ID,
        "parent_release_id": V1_RELEASE_ID,
        "parent_freeze_id": V1_FREEZE_ID,
        "final_decision": final_decision,
        "files": files,
    }
    write_json(
        FREEZE_PATH,
        {
            **identity,
            "freeze_id": "riemann_mathia_v2_" + sha256_text(canonical_json(identity)),
            "frozen_at": utc_now(),
        },
    )
    print(load_json(FREEZE_PATH)["freeze_id"])


def _era(year: int | None) -> str:
    if year is None:
        return "unknown"
    if year < 1900:
        return "pre-1900"
    if year < 1950:
        return "1900-1949"
    if year < 2000:
        return "1950-1999"
    return "2000-present"


def write_report() -> None:
    freeze = load_json(FREEZE_PATH)
    acquisition = load_json(ACQUISITION_SUMMARY_PATH)
    inventory = load_jsonl(DEPTH_INVENTORY_PATH)
    plans = [row for path in sorted(DEPTH_PLAN_ROOT.glob("batch_*.jsonl")) for row in load_jsonl(path)]
    units = load_jsonl(DEPTH_UNITS_PATH)
    revised = [row["output"] for row in load_jsonl(PASS_FILES["revised"])]
    within = load_jsonl(WITHIN_SYNTHESIS_FINAL_PATH)
    cross = load_jsonl(CROSS_SYNTHESIS_FINAL_PATH)
    audit = load_jsonl(AUDIT_FINAL_PATH)
    objects = load_jsonl(OBJECTS_PATH)
    efficiency = load_json(EFFICIENCY_METRICS_PATH)
    context_quarantine = (
        load_jsonl(ANALYSIS_CONTEXT_QUARANTINE_PATH)
        if ANALYSIS_CONTEXT_QUARANTINE_PATH.is_file()
        else []
    )
    audit_isolation_quarantine = (
        load_jsonl(AUDIT_ISOLATION_QUARANTINE_PATH)
        if AUDIT_ISOLATION_QUARANTINE_PATH.is_file()
        else []
    )
    handoff_state = load_json(OPENALEX_HANDOFF_STATE_PATH)
    agnostic_baseline_report = load_json(AGNOSTIC_V1_ROOT / "corpus_report.json")
    unit_counts = sorted(Counter(row["source_id"] for row in units).values())
    source_by_id = {row["source_id"]: row for row in inventory}
    interpretation_counts = Counter(row["decision"] for row in revised)
    within_counts = Counter(row["decision"] for row in within)
    cross_counts = Counter(row["decision"] for row in cross)
    audit_counts = Counter(row["decision"] for row in audit)
    coverage_type = Counter(row["source_type"] for row in inventory)
    coverage_era = Counter(_era(row.get("year")) for row in inventory)
    coverage_viewpoint = Counter(tag for row in inventory for tag in row.get("viewpoint_tags") or [])
    ocr_sources = [row for row in inventory if row["extraction_confidence"] == "ocr-lower-confidence"]
    long_sources = [
        row for row in inventory
        if int(row.get("normalized_page_count") or 0) >= 30
        or row["source_type"] in {"book", "monograph-lecture-series", "advanced-lecture-notes", "masters-thesis"}
    ]
    remaining = {plan["source_id"]: plan["remaining_meaningful_material"] for plan in plans if plan["remaining_meaningful_material"]}
    saturation = {row["axis"]: row for row in load_jsonl(SATURATION_LOG_PATH) if row["axis"] != "acquisition"}
    acquisition_rounds = [row for row in load_jsonl(SATURATION_LOG_PATH) if row["axis"] == "acquisition"]
    acquisition_state = load_json(ACQUISITION_RETRY_STATE_PATH)
    acquisition_frontier_status = (
        "an exhausted persistent lawful-candidate frontier with a zero-attempt final sweep"
        if ACQUISITION_FRONTIER_PATH.is_file()
        else "an open persistent recovery frontier with dispositions "
        f"{acquisition_state['source_disposition_counts']}"
    )
    eligible_counts = Counter(row["object_role"] for row in objects if row["training_eligibility"] == "eligible")
    negative_examples = [row for row in revised if row["decision"] != "accepted"][:5]
    accepted_examples = [row for row in revised if row["decision"] == "accepted"][:5]
    report = [
        "# Riemann–Mathia full corpus v2 report",
        "",
        "## Outcome",
        "",
        f"Final issue #42 v2 corpus decision: `{freeze['final_decision']}`.",
        "",
        "This is a corpus-only result. It does not authorize training, a mixing ratio, Qwen/qwen-lean inference, GPU use, RL, weight merging, Lean work, or an attempt to solve RH.",
        "",
        "## Immutable parent and acquisition breadth",
        "",
        f"V2 is explicitly parented to `{V1_RELEASE_ID}` freeze `{V1_FREEZE_ID}`. The v1 release tree and its 393 relevant records, 86 usable sources, 274 units, and 568 objects remain immutable.",
        "",
        f"The updated inventory contains {acquisition['updated_relevant_inventory_records']} relevant records. V2 recovered lawful usable text for {acquisition['formerly_unusable_recovered']} formerly unusable v1 records and acquired {acquisition['new_v2_sources_acquired']} newly inventoried sources, producing {acquisition['total_usable_sources_after_round']} usable sources total.",
        "",
        f"Fresh acquisition attempts by route: `{acquisition['attempts_by_route']}`; successful recoveries by route: `{acquisition['recoveries_by_route']}`. Provenance-preserved quarantine covers {acquisition['quarantined_attempts']} attempts across {acquisition['quarantined_sources']} sources with outcomes `{acquisition['quarantined_outcomes']}`.",
        "",
        f"The v1 recovery funnel is `{acquisition['v1_recovery_funnel']}`. Requests use the persistent source/route/host queue documented in `docs/RIEMANN_CORPUS_V2_ACQUISITION.md`; host cooldowns do not block work on unrelated hosts or local corpus processing.",
        "",
        "Further OpenAlex discovery/acquisition belongs to issue #46's independent offline worker. #42 consumes only immutable local full-text handoffs and makes zero repeated OpenAlex or source-download requests. Pending #46 work is not counted as an exhausted or saturated acquisition frontier.",
        "",
        f"The usable set includes {len(long_sources)} deliberately identified long-form sources and {len(ocr_sources)} flagged OCR sources. Raw and normalized copyrighted text remains in external artifact stores; Git retains hashes, provenance, derived outputs, and compact audit evidence.",
        "",
        f"Coverage by era: `{dict(sorted(coverage_era.items()))}`. Coverage by source type: `{dict(sorted(coverage_type.items()))}`. Broad discovery viewpoint counts: `{dict(sorted(coverage_viewpoint.items()))}`. These tags are search/audit strata, not a Mathia ontology.",
        "",
        f"Known gaps remain: inaccessible/paywalled works, non-digitized historical and non-English tails, repository access changes, and {acquisition['remaining_recovery_targets']} relevant v1 recovery targets without usable text. Any saturation claim is practical and lawful, not literal bibliography completeness.",
        "",
        "## Offline #46 dual-stream cutoff",
        "",
        f"Processing cutoff status: `{handoff_state['processing_cutoff']['status']}`. Riemann handoffs consumed: `{[row['handoff_id'] for row in handoff_state['streams']['riemann']['consumed']]}`; superseded evidence: `{[row['handoff_id'] for row in handoff_state['streams']['riemann']['superseded']]}`. Agnostic Mathia handoffs consumed: `{[row['handoff_id'] for row in handoff_state['streams']['agnostic_mathia']['consumed']]}`; superseded evidence: `{[row['handoff_id'] for row in handoff_state['streams']['agnostic_mathia']['superseded']]}`. Every row binds its immutable manifest, local artifact root, and processing cutoff. Finalization allowed: `{handoff_state['finalization_allowed']}`; the Riemann authoritative stream completed its separate isolation, provenance, and independent-audit reruns.",
        "",
        f"The separate agnostic supplement is parented to `{AGNOSTIC_V1_RELEASE_ID}` freeze `{AGNOSTIC_V1_FREEZE_ID}` (merged PR #45), whose baseline contains {agnostic_baseline_report['counts']['seed_source_inventory']} source inventory rows, {agnostic_baseline_report['counts']['semantic_source_units']} semantic units, and {agnostic_baseline_report['counts']['trainable_objects']} trainable objects. Current agnostic-stream processing metrics: `{handoff_state['streams']['agnostic_mathia']['processing_metrics']}`. The 28-family map is a retrieval/saturation lens, not a target schema.",
        "",
        "## Whole-source depth",
        "",
        f"All {len(plans)} usable sources received first-to-last logical-line inspection with exact gap-free coverage partitions and source-specific stop reasons. V2 materialized {len(units)} new/deeper exact source units; carried v1 objects remain present separately through immutable parent lineage.",
        "",
        f"New/deeper units per represented source: minimum {min(unit_counts)}, median {unit_counts[len(unit_counts)//2]}, 90th percentile {unit_counts[min(len(unit_counts)-1,int(len(unit_counts)*0.9))]}, maximum {max(unit_counts)}. Long-form sources account for {sum(len(plan['accepted_units']) for plan in plans if plan['source_id'] in {row['source_id'] for row in long_sources})} planned units. No max-units-per-source stop rule exists.",
        "",
        f"V1 context repairs identified: {sum(len(plan['v1_context_repairs']) for plan in plans)}. Sources with explicitly retained remaining meaningful material: {len(remaining)}; details stay in the source plans and within-source saturation record.",
        "",
        "## Token-aware gated Mathia extraction and synthesis",
        "",
        f"All {len(inventory)} sources have deterministic non-authoritative dossiers, and all {len(units)} v2 depth units retain exact source spans. Spontaneous and directed roles share a source context while remaining separately identifiable. Fresh adversarial criticism is isolated; only `revise` findings require another model context, while other critic decisions are finalized deterministically. Final interpretation decisions: `{dict(sorted(interpretation_counts.items()))}`.",
        "",
        f"Observable efficiency metrics: {efficiency['source_dossier_count']} dossiers; critic coverage fraction {efficiency['fresh_critic_fraction_of_v2_units']:.3f}; critic revision fraction {efficiency['critic_revision_fraction']:.3f}; completed context counts `{ {stage: row['completed_agent_contexts'] for stage, row in efficiency['analysis_contexts'].items()} }`. The independent-audit reuse gate carried {efficiency['independent_audit_reuse']['exact_pre_openalex_decisions_carried']} of {efficiency['independent_audit_reuse']['sampled_objects']} decisions only by exact canonical object-ID match, leaving {efficiency['independent_audit_reuse']['fresh_review_objects']} objects for fresh review. Exact collaboration-token telemetry was unavailable, so the retained stage input/output byte counts are explicit proxies rather than claimed token totals. Largest proxy stages: `{efficiency['largest_observable_agent_input_stages']}`.",
        "",
        f"Pre-LLM filtering is recorded as an exact whole-source coverage partition rather than invented rejected-candidate IDs: excluded segment counts `{efficiency['pre_llm_filtering']['pre_llm_excluded_segments']}`. Disclosed isolation-compromised contexts were excluded and rerun fresh rather than represented as independent evidence: analysis-context quarantine records {len(context_quarantine)}, audit-context quarantine records {len(audit_isolation_quarantine)}.",
        "",
        f"Within-source synthesis decisions: `{dict(sorted(within_counts.items()))}`. Cross-source synthesis decisions across {len(CROSS_PANELS)} mechanism panels: `{dict(sorted(cross_counts.items()))}`. All synthesis parents resolve to concrete source units and retain explicit limits.",
        "",
        "Representative accepted interpretations:",
        "",
    ]
    report.extend(f"- {row['quality_reason']}" for row in accepted_examples)
    report.extend(("", "Representative rejected/quarantined interpretations:", ""))
    report.extend(f"- `{row['decision']}` — {row['quality_reason']}" for row in negative_examples)
    report.extend(
        (
            "",
            "## Saturation and independent QA",
            "",
            f"Acquisition expansion preserved {len(acquisition_rounds)} marginal-yield rounds and currently records {acquisition_frontier_status}. Within-source saturation status: `{saturation.get('within-source',{}).get('status')}`. Conceptual/ecosystem saturation status: `{saturation.get('conceptual-ecosystem',{}).get('status')}`.",
            "",
            f"Independent stratified QA covers {len(audit)} interpretations/syntheses across era, source type, long/short form, OCR/alternate acquisition, viewpoint, source-depth, synthesis kind, and negative states. Of these, {efficiency['independent_audit_reuse']['exact_pre_openalex_decisions_carried']} exact unchanged object decisions were carried from the preserved pre-handoff audit and {efficiency['independent_audit_reuse']['fresh_review_objects']} handoff-affected objects received fresh isolated review. Decisions: `{dict(sorted(audit_counts.items()))}`. Audit downgrades were applied; prior negative labels were never upgraded automatically.",
            "",
            "Teacher interpretations, criticism, revision, synthesis, and audit are distillation evidence rather than independent mathematical proof. Famous-source familiarity and solver-specific prose remain live confounds; source text is retained as a separate trainable object.",
            "",
            "## Canonical interchange and compatibility",
            "",
            f"The release validates with the unchanged main-branch `{interchange.CONTRACT_VERSION}` renderer. Eligible object counts are `{dict(sorted(eligible_counts.items()))}`. V1 objects are carried under the v2 release with exact stable IDs and explicit parent freeze lineage; new v2 objects use source-linked stable IDs and external content references.",
            "",
            f"Merged `{AGNOSTIC_V1_RELEASE_ID}` is the immutable second baseline. Riemann v2 and any future `{AGNOSTIC_SUPPLEMENT_RELEASE_ID}` remain distinct release lineages under the same interchange; compatibility evidence must use their real frozen records rather than the old representative fixture.",
            "",
            f"Freeze: `{freeze['freeze_id']}`.",
        )
    )
    (V2_ROOT / "REPORT.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print("v2 report written")


def write_release_manifest() -> None:
    entries = []
    for path in sorted(V2_ROOT.rglob("*")):
        if (
            not path.is_file()
            or path == RELEASE_MANIFEST_PATH
            or _is_source_isolation_archive_path(path)
            or "__pycache__" in path.parts
        ):
            continue
        item = {
            "path": path.relative_to(V2_ROOT).as_posix(),
            "sha256": sha256_file(path),
            "bytes": path.stat().st_size,
        }
        if path.suffix == ".jsonl":
            item["record_count"] = len(load_jsonl(path))
        entries.append(item)
    identity = {"freeze_id": load_json(FREEZE_PATH)["freeze_id"], "files": entries}
    write_json(
        RELEASE_MANIFEST_PATH,
        {
            **identity,
            "manifest_id": "riemann_mathia_v2_manifest_" + sha256_text(canonical_json(identity)),
            "generated_at": utc_now(),
        },
    )
    print(load_json(RELEASE_MANIFEST_PATH)["manifest_id"])


def validate_frozen_release(v2_artifact_root: Path) -> list[str]:
    errors: list[str] = []
    errors.extend(validate_acquisition(v2_artifact_root, require_artifacts=True))
    errors.extend(validate_depth_plans(require_complete=True))
    errors.extend(validate_depth_units(v2_artifact_root, require_artifacts=True))
    errors.extend(validate_execution_context())
    errors.extend(validate_execution_ledger_receipts(V2_ROOT))
    errors.extend(validate_exact_audit_carry())
    freeze = load_json(FREEZE_PATH)
    errors.extend(
        validate_openalex_handoff_state(
            require_frozen_cutoff=(
                freeze.get("final_decision") == "RIEMANN_MATHIA_CORPUS_V2_READY"
            )
        )
    )
    if (
        (load_json(OPENALEX_HANDOFF_STATE_PATH).get("processing_cutoff") or {}).get(
            "status"
        )
        != "frozen"
    ):
        errors.append("#46 finite consumption cutoff is not frozen")
    errors.extend(validate_analysis())
    errors.extend(validate_within_source_synthesis(require_complete=True))
    errors.extend(validate_mixed_manifest_status())
    records = load_jsonl(OBJECTS_PATH)
    errors.extend(interchange.validate_release(records, _artifact_content_loader(v2_artifact_root)))
    errors.extend(_ready_acquisition_frontier_errors(str(freeze.get("final_decision") or "")))
    identity = {
        key: freeze[key]
        for key in (
            "contract_version", "corpus_release_id", "parent_release_id", "parent_freeze_id",
            "final_decision", "files",
        )
    }
    if freeze.get("freeze_id") != "riemann_mathia_v2_" + sha256_text(canonical_json(identity)):
        errors.append("v2 freeze id mismatch")
    if freeze.get("final_decision") not in V2_EXIT_DECISIONS:
        errors.append("invalid frozen v2 decision")
    for item in freeze.get("files") or []:
        if _is_source_isolation_archive_path(
            V2_ROOT / str(item.get("path") or "")
        ):
            errors.append("v2 freeze must exclude the non-authoritative isolation archive")
            continue
        path = V2_ROOT / item["path"]
        if not path.is_file() or sha256_file(path) != item["sha256"] or path.stat().st_size != item["bytes"]:
            errors.append(f"v2 frozen file drift: {item['path']}")
    report = (V2_ROOT / "REPORT.md").read_text(encoding="utf-8")
    mentioned = {decision for decision in V2_EXIT_DECISIONS if decision in report}
    if mentioned != {freeze.get("final_decision")}:
        errors.append("report must mention exactly the sole frozen v2 exit decision")
    manifest = load_json(RELEASE_MANIFEST_PATH)
    manifest_identity = {"freeze_id": manifest.get("freeze_id"), "files": manifest.get("files") or []}
    if manifest.get("manifest_id") != "riemann_mathia_v2_manifest_" + sha256_text(canonical_json(manifest_identity)):
        errors.append("v2 release manifest id mismatch")
    for item in manifest.get("files") or []:
        if _is_source_isolation_archive_path(
            V2_ROOT / str(item.get("path") or "")
        ):
            errors.append("v2 release manifest must exclude the non-authoritative isolation archive")
            continue
        path = V2_ROOT / item["path"]
        if not path.is_file() or sha256_file(path) != item["sha256"] or path.stat().st_size != item["bytes"]:
            errors.append(f"v2 manifest file drift: {item['path']}")
    return errors


def validate_acquisition(artifact_root: Path, require_artifacts: bool) -> list[str]:
    errors: list[str] = []
    if not PARENT_PATH.is_file() or not ACQUISITION_SEARCH_PATH.is_file():
        return ["v2 lineage is not initialized"]
    parent = load_json(PARENT_PATH)
    if parent.get("contract_version") != interchange.CONTRACT_VERSION:
        errors.append("parent contract_version mismatch")
    if parent.get("parent_freeze_id") != V1_FREEZE_ID:
        errors.append("parent freeze mismatch")
    v1_freeze = load_json(V1_ROOT / "freeze.json")
    if v1_freeze.get("freeze_id") != V1_FREEZE_ID:
        errors.append("v1 freeze changed")
    relevant = _v1_relevant_records()
    rows = load_jsonl(ACQUISITION_SEARCH_PATH)
    ids = [row.get("source_id") for row in rows]
    expected_ids = [record["source_id"] for record in relevant]
    if ids[: len(expected_ids)] != expected_ids:
        errors.append("acquisition search rows do not preserve exact v1 relevant-source prefix order")
    if any(row.get("lineage") != "v1-relevant" for row in rows[: len(expected_ids)]):
        errors.append("v1 relevant prefix has incorrect lineage")
    if len(ids) != len(set(ids)):
        errors.append("duplicate source_id in acquisition search")
    retry_state = None
    if not ACQUISITION_RETRY_STATE_PATH.is_file():
        errors.append("persistent acquisition retry state is missing")
    else:
        retry_state = load_json(ACQUISITION_RETRY_STATE_PATH)
        if retry_state.get("state_version") != "riemann-v2-acquisition-retry-state-v1":
            errors.append("persistent acquisition retry-state version mismatch")
        policy = retry_state.get("policy") or {}
        if policy.get("host_concurrency") != 1 or policy.get("global_sleep") is not False:
            errors.append("persistent acquisition host policy is not conservative/nonblocking")
        if any(
            "host-cooling-down-until:" in str(row.get("alternate_work_search_status") or "")
            for row in rows
        ):
            openalex_host = (retry_state.get("discovery_hosts") or {}).get(
                "api.openalex.org"
            ) or {}
            if not openalex_host.get("next_allowed_attempt_at"):
                errors.append("OpenAlex discovery cooldown is not persisted at host scope")
    for row in rows:
        source_id = row.get("source_id")
        candidates = row.get("candidates")
        attempts = row.get("attempts")
        if not isinstance(candidates, list) or not isinstance(attempts, list):
            errors.append(f"{source_id}: candidates and attempts must be lists")
            continue
        candidate_ids = [candidate.get("candidate_id") for candidate in candidates]
        if len(candidate_ids) != len(set(candidate_ids)):
            errors.append(f"{source_id}: duplicate candidate_id")
        if candidates != sorted(candidates, key=lambda item: (item["route_rank"], item["url"])):
            errors.append(f"{source_id}: candidates are not in provenance route order")
        known_candidates = set(candidate_ids)
        attempt_ids = [attempt.get("attempt_id") for attempt in attempts]
        if len(attempt_ids) != len(set(attempt_ids)):
            errors.append(f"{source_id}: duplicate attempt_id")
        for attempt in attempts:
            candidate_id = attempt.get("candidate_id")
            if candidate_id is not None and candidate_id not in known_candidates:
                errors.append(f"{source_id}: attempt references unknown candidate {candidate_id}")
            if (
                require_artifacts
                and attempt.get("artifact_store") == "riemann-corpus-v2"
                and attempt.get("artifact_relpath")
            ):
                artifact_path = artifact_root / str(attempt["artifact_relpath"])
                if not artifact_path.is_file():
                    errors.append(
                        f"{source_id}: missing attempted artifact {attempt['artifact_relpath']}"
                    )
                elif sha256_file(artifact_path) != attempt.get("artifact_sha256"):
                    errors.append(
                        f"{source_id}: attempted artifact hash drift {attempt['artifact_relpath']}"
                    )
            if attempt.get("result") in SUCCESS_RESULTS:
                for field in ("artifact_sha256", "normalized_sha256"):
                    if not re.fullmatch(r"[0-9a-f]{64}", str(attempt.get(field) or "")):
                        errors.append(f"{source_id}: successful attempt has invalid {field}")
                if require_artifacts and attempt.get("artifact_store") == "riemann-corpus-v2":
                    for relpath, digest in ((attempt.get("normalized_relpath"), attempt.get("normalized_sha256")),):
                        path = artifact_root / str(relpath)
                        if not path.is_file():
                            errors.append(f"{source_id}: missing external artifact {relpath}")
                        elif sha256_file(path) != digest:
                            errors.append(f"{source_id}: external artifact hash drift {relpath}")
            if attempt.get("status_class") is not None and attempt.get("status_class") != _outcome_status_class(
                attempt.get("result")
            ):
                errors.append(f"{source_id}: attempt status class disagrees with result")
            if attempt.get("host") is not None:
                expected_host = urllib.parse.urlparse(str(attempt.get("requested_url") or "")).hostname
                if attempt.get("host") != expected_host:
                    errors.append(f"{source_id}: attempt host disagrees with requested URL")
        if row.get("final_status") == "recovered-usable-in-v2":
            selected = row.get("selected_artifact") or {}
            if row.get("selected_candidate_id") not in known_candidates:
                errors.append(f"{source_id}: recovered source lacks a known selected candidate")
            if not selected.get("normalized_relpath"):
                errors.append(f"{source_id}: recovered source lacks selected normalized text")
    if retry_state is not None:
        expected_route_keys = {
            f"{row['source_id']}:{candidate['candidate_id']}"
            for row in rows
            for candidate in row.get("candidates") or []
        }
        if set(retry_state.get("routes") or {}) != expected_route_keys:
            errors.append("persistent retry state does not cover the exact candidate-route set")
        if set(retry_state.get("sources") or {}) != set(ids):
            errors.append("persistent retry state does not cover the exact source set")
    if ACQUISITION_FRONTIER_PATH.is_file() and retry_state is not None:
        unresolved = [
            source_id
            for source_id, source in retry_state["sources"].items()
            if source["disposition"] not in {"usable", "lawful-routes-exhausted"}
        ]
        if unresolved:
            errors.append("acquisition frontier is recorded while retry/discovery work remains")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "command",
        choices=(
            "init",
            "add-curated-v2-sources",
            "quarantine-acquisition-mismatches",
            "import-v1-alternates",
            "refresh-openalex",
            "search-openalex-alternates",
            "refresh-unpaywall",
            "acquire-alternates",
            "retry-transient",
            "write-acquisition-retry-state",
            "run-acquisition-loop",
            "repair-failed-attempt-artifacts",
            "summarize-acquisition",
            "record-acquisition-frontier",
            "validate-acquisition",
            "build-depth-inventory",
            "prepare-source-isolation-rerun",
            "prepare-source-isolation-correction-v2",
            "prepare-depth-assignments",
            "append-unassigned-depth-assignments",
            "prepare-missing-depth-assignments",
            "prune-quarantined-depth-sources",
            "merge-depth-repair-plans",
            "normalize-depth-plan-order",
            "sanitize-depth-synthesis-candidates",
            "write-depth-generation-provenance",
            "validate-depth-plans",
            "materialize-depth-units",
            "validate-depth-units",
            "write-openalex-handoff-state",
            "consume-openalex-handoffs",
            "freeze-openalex-handoff-cutoff",
            "validate-openalex-handoff-state",
            "write-execution-context",
            "validate-execution-context",
            "prepare-analysis-assignments",
            "quarantine-analysis-context",
            "materialize-deterministic-pass4",
            "validate-raw-analysis",
            "write-analysis-generation-provenance",
            "combine-analysis",
            "validate-analysis",
            "materialize-within-source-synthesis",
            "prepare-within-source-synthesis",
            "validate-within-source-synthesis",
            "combine-within-source-synthesis",
            "record-within-source-saturation",
            "prepare-cross-source-generation",
            "combine-cross-source-candidates",
            "prepare-cross-source-adjudication",
            "combine-cross-source-synthesis",
            "build-objects",
            "write-trainable-manifest",
            "prepare-independent-audit",
            "combine-independent-audit",
            "apply-independent-audit",
            "update-riemann-handoff-state",
            "record-conceptual-saturation",
            "write-mixed-manifest-status",
            "freeze-release",
            "write-report",
            "write-release-manifest",
            "validate-frozen-release",
        ),
    )
    parser.add_argument("--artifact-root", type=Path, default=DEFAULT_ARTIFACT_ROOT)
    parser.add_argument(
        "--agnostic-artifact-root",
        type=Path,
        default=DEFAULT_AGNOSTIC_SUPPLEMENT_ARTIFACT_ROOT,
    )
    parser.add_argument(
        "--handoff-root", type=Path, default=DEFAULT_OPENALEX_HANDOFF_ROOT
    )
    parser.add_argument("--handoff-id", action="append", default=[])
    parser.add_argument("--observed-issue-url")
    parser.add_argument("--round-id", default="openalex-refresh-round-1")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--require-artifacts", action="store_true")
    parser.add_argument("--batch-count", type=int, default=36)
    parser.add_argument("--delay-seconds", type=float, default=2.0)
    parser.add_argument("--per-host-limit", type=int, default=1)
    parser.add_argument("--max-route-attempts", type=int, default=DEFAULT_MAX_ROUTE_ATTEMPTS)
    parser.add_argument("--cached-only", action="store_true")
    parser.add_argument("--stage", choices=("pass12", "pass3", "pass4"))
    parser.add_argument("--batch-stem")
    parser.add_argument("--reason-code")
    parser.add_argument("--require-frozen-cutoff", action="store_true")
    parser.add_argument("--decision", choices=sorted(V2_EXIT_DECISIONS))
    args = parser.parse_args(argv)
    if args.command == "init":
        initialize_lineage()
        return 0
    if args.command == "add-curated-v2-sources":
        add_curated_v2_sources()
        return 0
    if args.command == "quarantine-acquisition-mismatches":
        quarantine_acquisition_identity_mismatches()
        return 0
    if args.command == "import-v1-alternates":
        import_v1_alternate_versions()
        return 0
    if args.command == "refresh-openalex":
        refresh_openalex(args.artifact_root)
        return 0
    if args.command == "search-openalex-alternates":
        search_openalex_alternate_works(args.artifact_root, args.cached_only, args.limit)
        return 0
    if args.command == "refresh-unpaywall":
        refresh_unpaywall(args.artifact_root)
        return 0
    if args.command == "acquire-alternates":
        acquire_alternates(args.artifact_root, args.round_id, args.limit)
        return 0
    if args.command == "retry-transient":
        retry_transient_failures(args.artifact_root, args.round_id, args.delay_seconds)
        return 0
    if args.command == "write-acquisition-retry-state":
        state = write_acquisition_retry_state(args.max_route_attempts)
        print(json.dumps(state["source_disposition_counts"], sort_keys=True))
        return 0
    if args.command == "run-acquisition-loop":
        run_persistent_acquisition_loop(
            args.artifact_root,
            args.round_id,
            args.limit,
            args.per_host_limit,
            args.max_route_attempts,
        )
        return 0
    if args.command == "repair-failed-attempt-artifacts":
        repair_failed_attempt_artifact_provenance(args.artifact_root)
        return 0
    if args.command == "summarize-acquisition":
        write_acquisition_summary(args.round_id)
        return 0
    if args.command == "record-acquisition-frontier":
        record_acquisition_frontier(args.round_id)
        return 0
    if args.command == "build-depth-inventory":
        build_depth_inventory()
        return 0
    if args.command == "prepare-source-isolation-rerun":
        print(json.dumps(prepare_source_isolation_rerun(), sort_keys=True))
        return 0
    if args.command == "prepare-source-isolation-correction-v2":
        print(json.dumps(prepare_corrective_source_isolation_rerun(), sort_keys=True))
        return 0
    if args.command == "prepare-depth-assignments":
        prepare_depth_assignments(args.batch_count)
        return 0
    if args.command == "append-unassigned-depth-assignments":
        append_unassigned_depth_assignments()
        return 0
    if args.command == "prepare-missing-depth-assignments":
        prepare_missing_depth_assignments()
        return 0
    if args.command == "prune-quarantined-depth-sources":
        prune_quarantined_depth_sources()
        return 0
    if args.command == "merge-depth-repair-plans":
        merge_depth_repair_plans()
        return 0
    if args.command == "normalize-depth-plan-order":
        normalize_depth_plan_order()
        return 0
    if args.command == "sanitize-depth-synthesis-candidates":
        sanitize_depth_synthesis_candidates()
        return 0
    if args.command == "write-depth-generation-provenance":
        write_depth_generation_provenance(args.artifact_root)
        return 0
    if args.command == "validate-depth-plans":
        errors = validate_depth_plans(require_complete=args.require_artifacts)
        if errors:
            print("\n".join(errors))
            return 1
        print("v2 depth-plan validation passed")
        return 0
    if args.command == "materialize-depth-units":
        materialize_depth_units(args.artifact_root)
        return 0
    if args.command == "validate-depth-units":
        errors = validate_depth_units(args.artifact_root, args.require_artifacts)
        if errors:
            print("\n".join(errors))
            return 1
        print("v2 materialized depth-unit validation passed")
        return 0
    if args.command == "write-openalex-handoff-state":
        write_openalex_handoff_state()
        return 0
    if args.command == "consume-openalex-handoffs":
        consume_openalex_handoffs(
            args.handoff_root, args.artifact_root, args.agnostic_artifact_root
        )
        return 0
    if args.command == "freeze-openalex-handoff-cutoff":
        if not args.observed_issue_url or not args.handoff_id:
            parser.error(
                "--observed-issue-url and two explicit --handoff-id values are required "
                "for freeze-openalex-handoff-cutoff"
            )
        print(
            freeze_openalex_handoff_cutoff(
                args.handoff_id, args.observed_issue_url
            )
        )
        return 0
    if args.command == "validate-openalex-handoff-state":
        errors = validate_openalex_handoff_state(args.require_frozen_cutoff)
        if errors:
            print("\n".join(errors))
            return 1
        print("v2 dual-stream offline #46 handoff-state validation passed")
        return 0
    if args.command == "write-execution-context":
        write_execution_context()
        return 0
    if args.command == "validate-execution-context":
        errors = validate_execution_context()
        if errors:
            print("\n".join(errors))
            return 1
        print("v2 deterministic execution-context validation passed")
        return 0
    if args.command == "prepare-analysis-assignments":
        if not args.stage:
            parser.error("--stage is required for prepare-analysis-assignments")
        prepare_analysis_assignments(args.stage, args.artifact_root)
        return 0
    if args.command == "quarantine-analysis-context":
        if not args.stage or not args.batch_stem or not args.reason_code:
            parser.error(
                "--stage, --batch-stem, and --reason-code are required for quarantine-analysis-context"
            )
        quarantine_analysis_context(args.stage, args.batch_stem, args.reason_code)
        return 0
    if args.command == "materialize-deterministic-pass4":
        materialize_deterministic_pass4()
        return 0
    if args.command == "validate-raw-analysis":
        if not args.stage:
            parser.error("--stage is required for validate-raw-analysis")
        errors = validate_raw_analysis_stage(args.stage, require_complete=args.require_artifacts)
        if errors:
            print("\n".join(errors))
            return 1
        print(f"v2 {args.stage} raw-analysis validation passed")
        return 0
    if args.command == "write-analysis-generation-provenance":
        write_analysis_generation_provenance()
        return 0
    if args.command == "combine-analysis":
        combine_analysis_batches()
        return 0
    if args.command == "validate-analysis":
        errors = validate_analysis()
        if errors:
            print("\n".join(errors))
            return 1
        print("v2 canonical four-pass analysis validation passed")
        return 0
    if args.command == "materialize-within-source-synthesis":
        materialize_within_source_synthesis_candidates()
        return 0
    if args.command == "prepare-within-source-synthesis":
        prepare_within_source_synthesis_assignments(args.artifact_root)
        return 0
    if args.command == "validate-within-source-synthesis":
        errors = validate_within_source_synthesis(require_complete=args.require_artifacts)
        if errors:
            print("\n".join(errors))
            return 1
        print("v2 within-source synthesis validation passed")
        return 0
    if args.command == "combine-within-source-synthesis":
        combine_within_source_synthesis()
        return 0
    if args.command == "record-within-source-saturation":
        record_within_source_saturation()
        return 0
    if args.command == "prepare-cross-source-generation":
        prepare_cross_source_generation_assignments(args.artifact_root)
        return 0
    if args.command == "combine-cross-source-candidates":
        combine_cross_source_candidates()
        return 0
    if args.command == "prepare-cross-source-adjudication":
        prepare_cross_source_adjudication_assignments(args.artifact_root)
        return 0
    if args.command == "combine-cross-source-synthesis":
        combine_cross_source_synthesis()
        return 0
    if args.command == "build-objects":
        build_objects(args.artifact_root)
        return 0
    if args.command == "write-trainable-manifest":
        write_trainable_manifest(args.artifact_root)
        return 0
    if args.command == "prepare-independent-audit":
        prepare_independent_audit(args.artifact_root, args.batch_count)
        return 0
    if args.command == "combine-independent-audit":
        combine_independent_audit()
        return 0
    if args.command == "apply-independent-audit":
        apply_independent_audit()
        return 0
    if args.command == "update-riemann-handoff-state":
        update_riemann_handoff_state()
        return 0
    if args.command == "record-conceptual-saturation":
        record_conceptual_saturation()
        return 0
    if args.command == "write-mixed-manifest-status":
        write_mixed_manifest_status()
        return 0
    if args.command == "freeze-release":
        if not args.decision:
            parser.error("--decision is required for freeze-release")
        freeze_release(args.decision)
        return 0
    if args.command == "write-report":
        write_report()
        return 0
    if args.command == "write-release-manifest":
        write_release_manifest()
        return 0
    if args.command == "validate-frozen-release":
        errors = validate_frozen_release(args.artifact_root)
        if errors:
            print("\n".join(errors))
            return 1
        print("v2 frozen release validation passed")
        return 0
    errors = validate_acquisition(args.artifact_root, args.require_artifacts)
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1
    print("v2 acquisition validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
