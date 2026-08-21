"""Issue-42-only pipeline for the agnostic #46 OpenAlex supplement.

The merged issue #44 release is an immutable parent.  This module reads only
the copied agnostic handoff, its compact source-disposition ledger, and
supplement-local derived artifacts.  It never imports Riemann records or
performs acquisition/network work.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from experiments import execution_provenance
from experiments.mathia_corpus import interchange
from experiments.riemann_corpus import full_corpus_v2 as issue42


HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[2]
AGNOSTIC_ROOT = HERE.parent
PARENT_RELEASE_ROOT = AGNOSTIC_ROOT / "release_v1"
DEFAULT_ARTIFACT_ROOT = Path(
    "/workspace/mathia-artifacts/agnostic-mathia-openalex-supplement-v1"
)
RELEASE_ID = "agnostic-mathia-openalex-supplement-v1"
PARENT_RELEASE_ID = "agnostic-mathia-full-v1"
PARENT_FREEZE_ID = "freeze_eeeeb89af3d2ac75d1ff5dad5623b63d1d24dfbddb965beca2f1c4aac9f9867f"
PARENT_MERGE_COMMIT = "f3df94498d83315f79fd6f98a5ec008db6f3ddab"
HANDOFF_ID = "agnostic_mathia_fulltext_v2"
SUPERSEDED_HANDOFF_ID = "agnostic_mathia_fulltext_v1"
HANDOFF_STREAM = "agnostic_mathia"
SOURCE_CONTEXT_MAX_UNITS = 16

SCREENING_FIELDS = {
    "source_id",
    "handoff_source_id",
    "decision",
    "mathematical_scope",
    "usefulness_reason",
    "duplicate_or_version_note",
    "extraction_risk",
    "proposed_lens_ids",
    "proposed_new_family_ids",
    "reviewer_provenance",
}
SCREENING_DECISIONS = {"useful", "reject", "quarantine"}
DEPTH_PLAN_FIELDS = {
    "source_id",
    "normalized_sha256",
    "inspection_summary",
    "coverage_segments",
    "accepted_units",
    "ecosystem_findings",
    "remaining_meaningful_material",
    "stop_reason",
    "reviewer_provenance",
}
COVERAGE_DISPOSITIONS = {
    "unit-bearing",
    "supporting-context",
    "routine-or-repetitive",
    "bibliography-or-front-matter",
    "outside-agnostic-scope",
    "extraction-defective",
}
UNIT_FIELDS = {
    "local_unit_id",
    "unit_type",
    "title",
    "line_start",
    "line_end",
    "why_material",
    "context_note",
    "representation_dependency",
}
FINDING_KINDS = {
    "reinforced_44_lens",
    "materially_extended_44_lens",
    "new_family",
    "saturation_probe_challenged",
    "saturation_probe_strengthened",
    "new_geometry_dependency",
}
GENERATION_FIELDS = {
    "analysis_id",
    "unit_id",
    "interpretation",
    "source_support",
    "nonparaphrase_operation",
    "boundary_or_failure",
    "uncertainty",
    "teacher_provenance",
}
CRITIC_FIELDS = {
    "analysis_id",
    "unit_id",
    "decision",
    "faithfulness",
    "unsupported_or_imported",
    "paraphrase_risk",
    "context_risk",
    "missed_mechanism",
    "revision_instructions",
    "critic_provenance",
}
REVISION_FIELDS = {
    "analysis_id",
    "unit_id",
    "decision",
    "interpretation",
    "source_support",
    "nonparaphrase_operation",
    "boundary_or_failure",
    "uncertainty",
    "quality_reason",
    "teacher_provenance",
}
FINAL_ANALYSIS_FIELDS = {
    "unit_id",
    "decision",
    "interpretation",
    "source_support",
    "nonparaphrase_operation",
    "boundary_or_failure",
    "uncertainty",
    "quality_reason",
    "derivation_ids",
    "teacher_provenance",
}
AUDIT_FIELDS = {
    "unit_id",
    "decision",
    "faithfulness",
    "context_sufficiency",
    "nonparaphrase_value",
    "specificity",
    "representation_sensitivity",
    "uncertainty_discipline",
    "ecosystem_contribution",
    "notes",
    "reviewer_provenance",
}
AUDIT_SAMPLING_POLICY = (
    "all non-accepted analyses plus one deterministic accepted unit per source, one per unit "
    "type, and a stable ten-percent hash sample"
)


@dataclass(frozen=True)
class SupplementLayout:
    root: Path = HERE

    @property
    def parent(self) -> Path:
        return self.root / "parent.json"

    @property
    def intake(self) -> Path:
        return self.root / "source_dispositions.jsonl"

    @property
    def screening_assignments(self) -> Path:
        return self.root / "screening" / "assignments"

    @property
    def screening_batches(self) -> Path:
        return self.root / "screening" / "batches"

    @property
    def screening_final(self) -> Path:
        return self.root / "screening" / "final.jsonl"

    @property
    def depth_assignments(self) -> Path:
        return self.root / "depth" / "assignments"

    @property
    def depth_plans(self) -> Path:
        return self.root / "depth" / "plans"

    @property
    def units(self) -> Path:
        return self.root / "depth" / "units.jsonl"

    def analysis_assignments(self, stage: str) -> Path:
        return self.root / "analysis" / stage / "assignments"

    def analysis_batches(self, stage: str) -> Path:
        return self.root / "analysis" / stage / "batches"

    @property
    def analysis_final(self) -> Path:
        return self.root / "analysis" / "final.jsonl"

    @property
    def audit_assignments(self) -> Path:
        return self.root / "audit" / "assignments"

    @property
    def audit_batches(self) -> Path:
        return self.root / "audit" / "batches"

    @property
    def audit_final(self) -> Path:
        return self.root / "audit" / "independent_review.jsonl"

    @property
    def audit_sample(self) -> Path:
        return self.root / "audit" / "sample.jsonl"

    @property
    def audit_carried(self) -> Path:
        return self.root / "audit" / "carried_prior.jsonl"

    @property
    def objects(self) -> Path:
        return self.root / "objects.jsonl"

    @property
    def trainable_manifest(self) -> Path:
        return self.root / "trainable_manifest.json"

    @property
    def metrics(self) -> Path:
        return self.root / "processing_metrics.json"

    @property
    def report(self) -> Path:
        return self.root / "REPORT.md"

    @property
    def freeze(self) -> Path:
        return self.root / "freeze.json"

    @property
    def isolation_archive(self) -> Path:
        return self.root / "non_authoritative_source_isolation_run"

    @property
    def isolation_manifest(self) -> Path:
        return self.isolation_archive / "manifest.jsonl"

    @property
    def isolation_summary(self) -> Path:
        return self.isolation_archive / "summary.json"


def canonical_json(value: Any) -> str:
    return interchange.canonical_json(value)


def sha256_text(value: str) -> str:
    return interchange.sha256_text(value)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def write_jsonl(path: Path, values: Iterable[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(canonical_json(dict(value)) + "\n" for value in values),
        encoding="utf-8",
    )


def model_visible_packet_sha256(assignment: Mapping[str, Any]) -> str:
    return issue42.model_visible_packet_sha256(assignment)


def _bind_model_visible_packet(assignment: Mapping[str, Any]) -> dict[str, Any]:
    bound = dict(assignment)
    bound["model_visible_packet_sha256"] = model_visible_packet_sha256(bound)
    return bound


def _candidate_payload(row: Mapping[str, Any]) -> dict[str, Any]:
    """Remove execution identity while retaining the candidate shown to the next agent."""
    return {
        str(key): value
        for key, value in row.items()
        if key not in {"teacher_provenance", "critic_provenance", "reviewer_provenance"}
    }


def _row_sha256(row: Mapping[str, Any]) -> str:
    return sha256_text(canonical_json(dict(row)))


def audit_sample_packet_sha256(item: Mapping[str, Any]) -> str:
    return sha256_text(canonical_json(dict(item)))


def exact_audit_carry(
    current_sample: Sequence[Mapping[str, Any]],
    prior_sample: Sequence[Mapping[str, Any]],
    prior_reviews: Sequence[Mapping[str, Any]],
) -> list[dict[str, Any]]:
    prior_packets: dict[str, str] = {}
    for item in prior_sample:
        unit_id = str(item.get("unit_id") or "")
        if not unit_id or unit_id in prior_packets:
            raise ValueError(f"invalid or duplicate prior audit sample unit: {unit_id}")
        prior_packets[unit_id] = audit_sample_packet_sha256(item)
    reviews: dict[str, dict[str, Any]] = {}
    for raw in prior_reviews:
        row = dict(raw)
        unit_id = str(row.get("unit_id") or "")
        if not unit_id or unit_id in reviews:
            raise ValueError(f"invalid or duplicate prior audit review unit: {unit_id}")
        reviews[unit_id] = row
    carried: list[dict[str, Any]] = []
    seen: set[str] = set()
    for item in current_sample:
        unit_id = str(item.get("unit_id") or "")
        if not unit_id or unit_id in seen:
            raise ValueError(f"invalid or duplicate current audit sample unit: {unit_id}")
        seen.add(unit_id)
        if (
            unit_id in reviews
            and prior_packets.get(unit_id) == audit_sample_packet_sha256(item)
        ):
            carried.append(reviews[unit_id])
    return carried


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _valid_analysis_provenance(value: Any) -> bool:
    """Require inspectable model/context provenance for agent-authored analysis."""
    return isinstance(value, dict) and all(
        _nonempty(value.get(field))
        for field in (
            "kind",
            "model_family",
            "exact_service_checkpoint",
            "agent_task_path",
            "review_scope",
        )
    )


def _external_artifact_root(artifact_root: Path) -> Path:
    resolved = artifact_root.resolve()
    if resolved == REPO_ROOT.resolve() or resolved.is_relative_to(REPO_ROOT.resolve()):
        raise ValueError("supplement source/unit artifacts must remain outside Git")
    return resolved


def _ledger_relpath(layout: SupplementLayout, path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except ValueError:
        return path.resolve().relative_to(layout.root.resolve()).as_posix()


def _resolve_ledger_path(layout: SupplementLayout, value: str) -> Path:
    declared = Path(value)
    if declared.is_absolute():
        return declared
    repository_path = REPO_ROOT / declared
    if repository_path.is_file():
        return repository_path
    return layout.root / declared


def discover_reused_generation_contexts(
    layout: SupplementLayout = SupplementLayout(),
) -> list[dict[str, Any]]:
    """Discover reused agent threads from committed assignment/output provenance."""
    if layout.isolation_summary.is_file():
        summary = load_json(layout.isolation_summary)
        if summary.get("status") == "complete":
            errors = issue42.validate_source_isolation_archive(
                layout.root, layout.isolation_archive
            )
            if errors:
                raise ValueError("invalid source-isolation archive: " + "; ".join(errors))
            reused = summary.get("reused_task_paths")
            if not isinstance(reused, list) or not reused:
                raise ValueError(
                    "completed source-isolation summary lacks reused generation contexts"
                )
            return reused
    ledger_path = layout.root / "execution" / "ai_execution_ledger.jsonl"
    if not ledger_path.is_file():
        raise ValueError("agnostic AI execution ledger is required")
    ledger_rows = load_jsonl(ledger_path)
    execution_provenance.validate_execution_rows(ledger_rows)
    owners: dict[str, dict[str, set[str]]] = {}
    generation_rows = [row for row in ledger_rows if row.get("stage") == "generation"]
    for ledger_row in generation_rows:
        assignment_path = _resolve_ledger_path(
            layout, str(ledger_row["assignment_relpath"])
        )
        if not assignment_path.is_file() or not assignment_path.is_relative_to(layout.root):
            raise ValueError("generation ledger assignment is missing or outside the supplement")
        if sha256_file(assignment_path) != ledger_row.get("assignment_sha256"):
            raise ValueError(f"{assignment_path.name}: generation ledger assignment drift")
        assignment = load_json(assignment_path)
        units = assignment.get("units") or [assignment.get("unit") or {}]
        source_ids = {
            str(unit.get("source_id") or "") for unit in units if unit.get("source_id")
        }
        if len(source_ids) != 1:
            raise ValueError(
                f"{assignment_path.name}: generation assignment is not source-local"
            )
        output_path = _resolve_ledger_path(
            layout, str(ledger_row.get("output_relpath") or "")
        )
        if (
            not output_path.is_file()
            or sha256_file(output_path) != ledger_row.get("output_sha256")
        ):
            raise ValueError(
                f"{assignment_path.name}: generation ledger output is missing or drifted"
            )
        task_path = str(ledger_row.get("agent_task_path") or "")
        if not task_path.startswith("/root/"):
            raise ValueError(
                f"{assignment_path.name}: one exact generation agent task path is required"
            )
        owner = owners.setdefault(
            task_path, {"assignments": set(), "source_ids": set(), "unit_ids": set()}
        )
        owner["assignments"].add(assignment_path.relative_to(layout.root).as_posix())
        owner["source_ids"].update(source_ids)
        owner["unit_ids"].update(str(unit["unit_id"]) for unit in units)
    reused: list[dict[str, Any]] = []
    for task_path, owner in sorted(owners.items()):
        if len(owner["assignments"]) < 2:
            continue
        reused.append(
            {
                "agent_task_path": task_path,
                "assignments": sorted(owner["assignments"]),
                "assignment_count": len(owner["assignments"]),
                "source_ids": sorted(owner["source_ids"]),
                "source_count": len(owner["source_ids"]),
                "unit_count": len(owner["unit_ids"]),
            }
        )
    return reused


def prepare_source_isolation_rerun(
    layout: SupplementLayout = SupplementLayout(),
) -> dict[str, Any]:
    """Deactivate reused generation threads and dependent outputs, preserving evidence."""
    if layout.isolation_summary.is_file():
        summary = load_json(layout.isolation_summary)
        if summary.get("status") == "complete":
            errors = issue42.validate_source_isolation_archive(
                layout.root, layout.isolation_archive
            )
            if (
                not layout.isolation_manifest.is_file()
                or summary.get("archive_manifest_sha256")
                != sha256_file(layout.isolation_manifest)
            ):
                errors.append("source-isolation archive manifest hash mismatch")
            if errors:
                raise ValueError("invalid source-isolation archive: " + "; ".join(errors))
            return summary
    else:
        reused = discover_reused_generation_contexts(layout)
        if not reused:
            raise ValueError("no reused agnostic generation contexts were discovered")
        write_json(
            layout.isolation_summary,
            {
                "status": "in_progress",
                "reason": "generation task paths were reused across source assignments",
                "reused_task_paths": reused,
                "affected_source_ids": sorted(
                    {source_id for row in reused for source_id in row["source_ids"]}
                ),
                "authoritative": False,
                "trainable": False,
            },
        )
    in_progress = load_json(layout.isolation_summary)
    reused = list(in_progress["reused_task_paths"])
    affected_assignments = {
        relative for row in reused for relative in row["assignments"]
    }

    def archive_existing(
        path: Path,
        *,
        pool: str,
        category: str,
        reason: str,
        reconciliation_eligible: bool = False,
    ) -> None:
        try:
            relative = path.resolve().relative_to(layout.root.resolve()).as_posix()
        except ValueError:
            raise ValueError(f"supplement isolation artifact is outside release: {path}")
        prior = any(
            row.get("original_relpath") == relative and row.get("pool") == pool
            for row in load_jsonl(layout.isolation_manifest)
        )
        if not path.is_file() and not prior:
            return
        issue42._archive_file_for_isolation(
            layout.root,
            layout.isolation_archive,
            path,
            pool=pool,
            category=category,
            reason=reason,
            reconciliation_eligible=reconciliation_eligible,
        )

    reconciliation_receipts: list[dict[str, Any]] = []

    def archive_assignment(
        assignment_path: Path,
        *,
        pool: str,
        category: str,
        reason: str,
        reconciliation_eligible: bool = False,
    ) -> None:
        assignment = load_json(assignment_path)
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

    for relative in sorted(affected_assignments):
        path = layout.root / relative
        if path.is_file():
            archive_assignment(
                path,
                pool="non_authoritative",
                category="reused-generation-context",
                reason="one generation agent task path executed multiple source assignments",
            )
    for stage in ("critic", "revision"):
        for path in sorted(layout.analysis_assignments(stage).glob("*.json")):
            archive_assignment(
                path,
                pool="reconciliation",
                category=f"dependent-{stage}",
                reason="downstream context depends on deactivated generation",
                reconciliation_eligible=True,
            )
    for path in sorted(layout.audit_assignments.glob("*.json")):
        archive_assignment(
            path,
            pool="reconciliation",
            category="dependent-audit",
            reason="audit packet depends on deactivated generated analysis",
            reconciliation_eligible=True,
        )
    execution_ledger_path = layout.root / "execution" / "ai_execution_ledger.jsonl"
    execution_ledger_snapshot = (
        layout.isolation_archive
        / "non_authoritative"
        / "artifacts"
        / execution_ledger_path.relative_to(layout.root)
    )
    ledger_rows = load_jsonl(
        execution_ledger_snapshot
        if execution_ledger_snapshot.is_file()
        else execution_ledger_path
    )
    if not execution_ledger_snapshot.is_file():
        archive_existing(
            execution_ledger_path,
            pool="non_authoritative",
            category="execution-ledger-snapshot",
            reason="preserve exact pre-rerun execution ledger before status reconciliation",
            reconciliation_eligible=True,
        )
    affected_repo_relpaths = {
        _ledger_relpath(layout, layout.root / relative)
        for relative in affected_assignments
    }
    updated_ledger: list[dict[str, Any]] = []
    for raw in ledger_rows:
        row = dict(raw)
        if row.get("assignment_relpath") in affected_repo_relpaths:
            row.update(
                {
                    "status": "isolation-invalid",
                    "requires_rerun": True,
                    "rerun_reason": "reused-multi-source-context",
                }
            )
        elif row.get("stage") in {"critic", "revision", "audit"}:
            row.update(
                {
                    "status": "reconciliation-pending",
                    "requires_rerun": True,
                    "rerun_reason": "upstream-generation-invalidated",
                }
            )
        updated_ledger.append(row)
    execution_provenance.validate_execution_rows(updated_ledger)
    write_jsonl(execution_ledger_path, updated_ledger)
    for path, pool, category in (
        (layout.analysis_final, "non_authoritative", "analysis-final"),
        (layout.audit_sample, "reconciliation", "audit-sample"),
        (layout.audit_carried, "reconciliation", "audit-carried"),
        (layout.audit_final, "reconciliation", "audit-final"),
        (layout.objects, "non_authoritative", "canonical-objects"),
        (layout.trainable_manifest, "non_authoritative", "trainable-manifest"),
        (layout.metrics, "non_authoritative", "processing-metrics"),
        (layout.report, "non_authoritative", "report"),
        (layout.freeze, "non_authoritative", "candidate-freeze"),
    ):
        archive_existing(
            path,
            pool=pool,
            category=category,
            reason="derived release state depends on reused generation contexts",
            reconciliation_eligible=pool == "reconciliation",
        )
    errors = issue42.validate_source_isolation_archive(
        layout.root, layout.isolation_archive
    )
    if errors:
        raise ValueError("invalid source-isolation archive: " + "; ".join(errors))
    manifest_rows = load_jsonl(layout.isolation_manifest)
    summary = {
        **in_progress,
        "status": "complete",
        "archived_file_count": len(manifest_rows),
        "archived_bytes": sum(int(row["bytes"]) for row in manifest_rows),
        "archive_manifest_sha256": sha256_file(layout.isolation_manifest),
        "reconciliation_receipt_count": 0,
        "retained_live_stages": ["screening", "depth", "materialized-units"],
        "replacement_stages": ["generation", "critic", "revision", "audit", "release"],
    }
    write_json(layout.isolation_summary, summary)
    return summary


def _bundle_root(artifact_root: Path) -> Path:
    return _external_artifact_root(artifact_root) / "openalex_handoffs" / HANDOFF_ID


def _parent_errors(layout: SupplementLayout) -> list[str]:
    errors: list[str] = []
    if not layout.parent.is_file():
        return ["agnostic supplement parent binding is missing"]
    parent = load_json(layout.parent)
    if (
        parent.get("contract_version") != interchange.CONTRACT_VERSION
        or parent.get("supplement_release_id") != RELEASE_ID
        or parent.get("parent_release_id") != PARENT_RELEASE_ID
        or parent.get("parent_freeze_id") != PARENT_FREEZE_ID
        or parent.get("parent_merge_commit") != PARENT_MERGE_COMMIT
    ):
        errors.append("agnostic supplement parent identity mismatch")
    for binding in parent.get("bindings") or []:
        path = REPO_ROOT / str(binding.get("path") or "")
        if (
            not path.is_file()
            or path.stat().st_size != binding.get("bytes")
            or sha256_file(path) != binding.get("sha256")
        ):
            errors.append(f"immutable #44 parent binding drift: {binding.get('path')}")
    return errors


def intake_records(
    layout: SupplementLayout = SupplementLayout(),
    artifact_root: Path = DEFAULT_ARTIFACT_ROOT,
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    parent_errors = _parent_errors(layout)
    if parent_errors:
        raise ValueError("; ".join(parent_errors))
    bundle = issue42._validate_openalex_handoff_bundle(
        _bundle_root(artifact_root), HANDOFF_ID, HANDOFF_STREAM
    )
    records = load_jsonl(layout.intake)
    allowed = {
        "accepted_for_agnostic_supplement_analysis",
        "deduplicated_or_already_represented",
        "quarantined_ambiguous_source_identity",
    }
    if len(records) != len(bundle["rows"]):
        raise ValueError("agnostic source ledger does not cover the handoff manifest")
    by_handoff_id = {row.get("handoff_source_id"): row for row in records}
    if len(by_handoff_id) != len(records) or set(by_handoff_id) != {
        row["source_id"] for row in bundle["rows"]
    }:
        raise ValueError("agnostic source ledger identity/coverage mismatch")
    canonical_ids = [str(row.get("canonical_source_id") or "") for row in records]
    if len(canonical_ids) != len(set(canonical_ids)):
        raise ValueError("agnostic source ledger repeats a canonical source identity")
    manifest = {row["source_id"]: row for row in bundle["rows"]}
    for row in records:
        source_id = str(row.get("canonical_source_id") or "")
        raw = manifest[row["handoff_source_id"]]
        if (
            row.get("stream") != HANDOFF_STREAM
            or row.get("handoff_id") != HANDOFF_ID
            or row.get("disposition") not in allowed
            or not source_id
            or "riemann" in source_id.lower()
            or row.get("normalized_sha256") != raw.get("normalized_sha256")
            or row.get("normalized_bytes") != raw.get("normalized_bytes")
            or row.get("raw_sha256") != raw.get("raw_sha256")
        ):
            raise ValueError(f"invalid or cross-stream agnostic intake row: {source_id}")
    return bundle, records


def validate_intake(
    layout: SupplementLayout = SupplementLayout(),
    artifact_root: Path = DEFAULT_ARTIFACT_ROOT,
) -> list[str]:
    try:
        intake_records(layout, artifact_root)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        return [str(error)]
    return []


def _source_slug(source_id: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "_", source_id.lower()).strip("_")
    return f"{slug[:48]}_{sha256_text(source_id)[:8]}"


def _clear_assignments(root: Path) -> None:
    root.mkdir(parents=True, exist_ok=True)
    for path in root.glob("*.json"):
        path.unlink()


def prepare_source_screening(
    layout: SupplementLayout = SupplementLayout(),
    artifact_root: Path = DEFAULT_ARTIFACT_ROOT,
) -> None:
    bundle, records = intake_records(layout, artifact_root)
    manifest = {row["source_id"]: row for row in bundle["rows"]}
    _clear_assignments(layout.screening_assignments)
    count = 0
    for intake in records:
        if intake["disposition"] != "accepted_for_agnostic_supplement_analysis":
            continue
        raw = manifest[intake["handoff_source_id"]]
        relative = issue42._manifest_handoff_relpath(raw["normalized_path"], HANDOFF_ID)
        normalized_path = Path(bundle["root"]) / relative
        source_id = str(intake["canonical_source_id"])
        slug = _source_slug(source_id)
        write_json(
            layout.screening_assignments / f"{slug}.json",
            {
                "task": "fresh whole-source agnostic supplement screening",
                "isolation_requirement": (
                    "Read only AGENTS.md, this assignment, and the exact bound normalized source. "
                    "OpenAlex relevance metadata is routing evidence, not proof of novelty."
                ),
                "output_path": str(layout.screening_batches / f"{slug}.jsonl"),
                "expected_fields": sorted(SCREENING_FIELDS),
                "decision_vocabulary": sorted(SCREENING_DECISIONS),
                "source": {
                    "source_id": source_id,
                    "handoff_source_id": intake["handoff_source_id"],
                    "title": intake.get("title"),
                    "authors": intake.get("authors") or [],
                    "year": intake.get("year"),
                    "source_type": intake.get("source_type"),
                    "normalized_abspath": str(normalized_path),
                    "normalized_sha256": raw["normalized_sha256"],
                    "normalized_bytes": raw["normalized_bytes"],
                    "normalized_lines": raw.get("normalized_lines"),
                    "routing_lenses": (intake.get("relevance") or {}).get(
                        "ecosystem_lens_ids"
                    )
                    or [],
                    "routing_family_candidates": (intake.get("relevance") or {}).get(
                        "candidate_family_ids"
                    )
                    or [],
                },
            },
        )
        count += 1
    print(f"prepared {count} isolated agnostic source-screening assignments")


def combine_source_screening(layout: SupplementLayout = SupplementLayout()) -> None:
    expected: list[tuple[str, str]] = []
    rows: list[dict[str, Any]] = []
    for assignment_path in sorted(layout.screening_assignments.glob("*.json")):
        assignment = load_json(assignment_path)
        source = assignment["source"]
        expected.append((source["source_id"], source["handoff_source_id"]))
        output_path = Path(assignment["output_path"])
        output = load_jsonl(output_path)
        if len(output) != 1:
            raise ValueError(f"{assignment_path.name}: screening output must contain one row")
        row = output[0]
        if (
            set(row) != SCREENING_FIELDS
            or (row.get("source_id"), row.get("handoff_source_id")) != expected[-1]
            or row.get("decision") not in SCREENING_DECISIONS
            or any(not _nonempty(row.get(field)) for field in (
                "mathematical_scope", "usefulness_reason", "duplicate_or_version_note", "extraction_risk"
            ))
            or not isinstance(row.get("proposed_lens_ids"), list)
            or not isinstance(row.get("proposed_new_family_ids"), list)
            or not isinstance(row.get("reviewer_provenance"), dict)
        ):
            raise ValueError(f"{assignment_path.name}: invalid screening row")
        rows.append(row)
    if len({item[0] for item in expected}) != len(expected):
        raise ValueError("screening assignments repeat a canonical source")
    write_jsonl(layout.screening_final, rows)


def validate_source_screening(
    layout: SupplementLayout = SupplementLayout(), require_complete: bool = True
) -> list[str]:
    errors: list[str] = []
    assignments = sorted(layout.screening_assignments.glob("*.json"))
    expected = [load_json(path)["source"]["source_id"] for path in assignments]
    rows = load_jsonl(layout.screening_final)
    if require_complete and [row.get("source_id") for row in rows] != expected:
        errors.append("source-screening order/coverage differs from assignments")
    for row in rows:
        if set(row) != SCREENING_FIELDS or row.get("decision") not in SCREENING_DECISIONS:
            errors.append(f"{row.get('source_id')}: invalid source-screening schema/decision")
    return errors


def prepare_depth_plans(
    layout: SupplementLayout = SupplementLayout(),
    artifact_root: Path = DEFAULT_ARTIFACT_ROOT,
) -> None:
    if validate_source_screening(layout, True):
        raise ValueError("complete valid source screening is required before depth planning")
    bundle, intake = intake_records(layout, artifact_root)
    intake_by_id = {row["canonical_source_id"]: row for row in intake}
    manifest = {row["source_id"]: row for row in bundle["rows"]}
    _clear_assignments(layout.depth_assignments)
    count = 0
    for screening in load_jsonl(layout.screening_final):
        if screening["decision"] != "useful":
            continue
        source_id = str(screening["source_id"])
        source = intake_by_id[source_id]
        raw = manifest[source["handoff_source_id"]]
        relative = issue42._manifest_handoff_relpath(raw["normalized_path"], HANDOFF_ID)
        slug = _source_slug(source_id)
        write_json(
            layout.depth_assignments / f"{slug}.json",
            {
                "task": "exact whole-source agnostic semantic depth plan",
                "instructions": (
                    "Inspect every logical line and emit a gap-free coverage partition. Candidate "
                    "units must be generic semantic mathematics rather than hidden arithmetic execution. "
                    "The #44 lens map is a retrieval/saturation aid, never a forced label set."
                ),
                "output_path": str(layout.depth_plans / f"{slug}.jsonl"),
                "expected_fields": sorted(DEPTH_PLAN_FIELDS),
                "coverage_dispositions": sorted(COVERAGE_DISPOSITIONS),
                "finding_kinds": sorted(FINDING_KINDS),
                "source": {
                    "source_id": source_id,
                    "handoff_source_id": source["handoff_source_id"],
                    "normalized_abspath": str(Path(bundle["root"]) / relative),
                    "normalized_sha256": raw["normalized_sha256"],
                    "normalized_bytes": raw["normalized_bytes"],
                    "normalized_lines": raw.get("normalized_lines"),
                    "screening": screening,
                },
            },
        )
        count += 1
    print(f"prepared {count} one-source agnostic depth assignments")


def _plan_rows(layout: SupplementLayout) -> list[tuple[dict[str, Any], dict[str, Any]]]:
    result: list[tuple[dict[str, Any], dict[str, Any]]] = []
    for assignment_path in sorted(layout.depth_assignments.glob("*.json")):
        assignment = load_json(assignment_path)
        output = load_jsonl(Path(assignment["output_path"]))
        if len(output) == 1:
            result.append((assignment, output[0]))
    return result


def validate_depth_plans(
    layout: SupplementLayout = SupplementLayout(), require_complete: bool = True
) -> list[str]:
    errors: list[str] = []
    assignments = sorted(layout.depth_assignments.glob("*.json"))
    seen_units: set[str] = set()
    seen_sources: list[str] = []
    for assignment_path in assignments:
        assignment = load_json(assignment_path)
        source = assignment["source"]
        output_path = Path(assignment["output_path"])
        if not output_path.is_file():
            if require_complete:
                errors.append(f"{assignment_path.name}: depth plan is missing")
            continue
        rows = load_jsonl(output_path)
        if len(rows) != 1:
            errors.append(f"{assignment_path.name}: depth plan must contain one row")
            continue
        plan = rows[0]
        source_id = str(source["source_id"])
        seen_sources.append(source_id)
        if (
            set(plan) != DEPTH_PLAN_FIELDS
            or plan.get("source_id") != source_id
            or plan.get("normalized_sha256") != source["normalized_sha256"]
            or not _nonempty(plan.get("inspection_summary"))
            or not _nonempty(plan.get("stop_reason"))
            or not isinstance(plan.get("reviewer_provenance"), dict)
        ):
            errors.append(f"{source_id}: invalid depth-plan schema/binding")
            continue
        source_path = Path(source["normalized_abspath"])
        if (
            not source_path.is_file()
            or sha256_file(source_path) != source["normalized_sha256"]
            or source_path.stat().st_size != source["normalized_bytes"]
        ):
            errors.append(f"{source_id}: normalized source missing or drifted")
            continue
        line_count = len(source_path.read_text(encoding="utf-8", errors="replace").splitlines())
        segments = plan.get("coverage_segments") or []
        expected_start = 1
        unit_segments: set[tuple[int, int]] = set()
        for segment in segments:
            if set(segment) != {"line_start", "line_end", "disposition", "reason"}:
                errors.append(f"{source_id}: invalid coverage segment fields")
                continue
            start, end = int(segment["line_start"]), int(segment["line_end"])
            if (
                start != expected_start
                or end < start
                or end > line_count
                or segment["disposition"] not in COVERAGE_DISPOSITIONS
                or not _nonempty(segment["reason"])
            ):
                errors.append(f"{source_id}: coverage is not exact/gap-free")
            if segment["disposition"] == "unit-bearing":
                unit_segments.add((start, end))
            expected_start = end + 1
        if expected_start != line_count + 1:
            errors.append(f"{source_id}: coverage does not reach the final logical line")
        accepted_spans: set[tuple[int, int]] = set()
        plan_unit_ids: set[str] = set()
        for unit in plan.get("accepted_units") or []:
            unit_id = str(unit.get("local_unit_id") or "")
            if set(unit) != UNIT_FIELDS or not re.fullmatch(r"agnostic_oa_[a-z0-9_]+", unit_id):
                errors.append(f"{source_id}: invalid depth-unit schema/id")
                continue
            if unit_id in seen_units:
                errors.append(f"{unit_id}: duplicate supplement unit ID")
            seen_units.add(unit_id)
            plan_unit_ids.add(unit_id)
            span = (int(unit["line_start"]), int(unit["line_end"]))
            accepted_spans.add(span)
            if span not in unit_segments:
                errors.append(f"{unit_id}: accepted span is not an exact unit-bearing segment")
            for field in (
                "unit_type", "title", "why_material", "context_note", "representation_dependency"
            ):
                if not _nonempty(unit.get(field)):
                    errors.append(f"{unit_id}: empty required depth-unit field {field}")
        if not plan_unit_ids:
            errors.append(f"{source_id}: useful source has no accepted semantic unit")
        if accepted_spans != unit_segments:
            errors.append(f"{source_id}: unit-bearing coverage and accepted units differ")
        for finding in plan.get("ecosystem_findings") or []:
            if (
                set(finding) != {"kind", "identifier", "evidence_unit_ids", "summary"}
                or finding.get("kind") not in FINDING_KINDS
                or not _nonempty(finding.get("identifier"))
                or not _nonempty(finding.get("summary"))
                or not set(finding.get("evidence_unit_ids") or []).issubset(plan_unit_ids)
            ):
                errors.append(f"{source_id}: invalid ecosystem finding")
    if require_complete and len(seen_sources) != len(assignments):
        errors.append("depth-plan source coverage is incomplete")
    return errors


def materialize_units(
    layout: SupplementLayout = SupplementLayout(),
    artifact_root: Path = DEFAULT_ARTIFACT_ROOT,
) -> None:
    errors = validate_depth_plans(layout, True)
    if errors:
        raise ValueError("cannot materialize invalid depth plans: " + "; ".join(errors))
    artifact_root = _external_artifact_root(artifact_root)
    records: list[dict[str, Any]] = []
    for assignment, plan in _plan_rows(layout):
        source = assignment["source"]
        lines = Path(source["normalized_abspath"]).read_text(
            encoding="utf-8", errors="replace"
        ).splitlines()
        findings_by_unit: dict[str, list[dict[str, Any]]] = {}
        for finding in plan["ecosystem_findings"]:
            for unit_id in finding["evidence_unit_ids"]:
                findings_by_unit.setdefault(unit_id, []).append(finding)
        for unit in plan["accepted_units"]:
            start, end = int(unit["line_start"]), int(unit["line_end"])
            content = "\n".join(lines[start - 1 : end]) + "\n"
            relative = Path("depth") / "units" / f"{unit['local_unit_id']}.txt"
            path = artifact_root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            records.append(
                {
                    "unit_id": unit["local_unit_id"],
                    "source_id": source["source_id"],
                    "handoff_source_id": source["handoff_source_id"],
                    "source_normalized_sha256": source["normalized_sha256"],
                    "line_start": start,
                    "line_end": end,
                    "unit_type": unit["unit_type"],
                    "title": unit["title"],
                    "selection_reason": unit["why_material"],
                    "context_note": unit["context_note"],
                    "representation_dependency": unit["representation_dependency"],
                    "ecosystem_findings": findings_by_unit.get(unit["local_unit_id"], []),
                    "artifact_relpath": relative.as_posix(),
                    "artifact_sha256": sha256_file(path),
                    "artifact_bytes": path.stat().st_size,
                    "segmentation_provenance": plan["reviewer_provenance"],
                }
            )
    write_jsonl(layout.units, records)


def validate_units(
    layout: SupplementLayout = SupplementLayout(),
    artifact_root: Path = DEFAULT_ARTIFACT_ROOT,
    require_artifacts: bool = True,
) -> list[str]:
    errors = validate_depth_plans(layout, True)
    units = load_jsonl(layout.units)
    expected = [
        unit["local_unit_id"]
        for _, plan in _plan_rows(layout)
        for unit in plan["accepted_units"]
    ]
    if [row.get("unit_id") for row in units] != expected:
        errors.append("materialized unit order/coverage differs from accepted depth units")
    if not require_artifacts:
        return errors
    artifact_root = _external_artifact_root(artifact_root)
    for unit in units:
        path = artifact_root / str(unit.get("artifact_relpath") or "")
        if (
            not path.is_file()
            or path.stat().st_size != unit.get("artifact_bytes")
            or sha256_file(path) != unit.get("artifact_sha256")
        ):
            errors.append(f"{unit.get('unit_id')}: unit artifact missing or drifted")
    return errors


def _analysis_id(stage: str, unit: Mapping[str, Any]) -> str:
    identity = {
        "release_id": RELEASE_ID,
        "stage": stage,
        "unit_id": unit["unit_id"],
        "unit_sha256": unit["artifact_sha256"],
    }
    return f"agnostic_oa_{stage}_" + sha256_text(canonical_json(identity))


def _analysis_records(layout: SupplementLayout, stage: str) -> dict[str, dict[str, Any]]:
    fields = {
        "generation": GENERATION_FIELDS,
        "critic": CRITIC_FIELDS,
        "revision": REVISION_FIELDS,
    }[stage]
    result: dict[str, dict[str, Any]] = {}
    for assignment_path in sorted(layout.analysis_assignments(stage).glob("*.json")):
        assignment = load_json(assignment_path)
        if assignment.get("model_visible_packet_sha256") != model_visible_packet_sha256(
            assignment
        ):
            raise ValueError(f"{assignment_path.name}: invalid execution packet fingerprint")
        output = load_jsonl(Path(assignment["output_path"]))
        units = assignment.get("units") or [assignment["unit"]]
        expected_ids = assignment.get("expected_analysis_ids") or {
            units[0]["unit_id"]: assignment["expected_analysis_id"]
        }
        if set(expected_ids) != {unit["unit_id"] for unit in units}:
            raise ValueError(f"{assignment_path.name}: invalid expected analysis-id binding")
        if len(output) != len(units):
            raise ValueError(
                f"{assignment_path.name}: {stage} output must contain {len(units)} rows"
            )
        if [row.get("unit_id") for row in output] != [unit["unit_id"] for unit in units]:
            raise ValueError(f"{assignment_path.name}: {stage} output order/coverage mismatch")
        for unit, row in zip(units, output):
            if (
                set(row) != fields
                or row.get("analysis_id") != expected_ids.get(unit["unit_id"])
            ):
                raise ValueError(f"{assignment_path.name}: invalid {stage} schema/binding")
            if stage == "critic" and row.get("decision") not in {
                "accept_as_is", "revise", "reject", "quarantine"
            }:
                raise ValueError(f"{assignment_path.name}: invalid critic decision")
            if stage == "revision" and row.get("decision") not in {
                "accepted", "rejected", "quarantined"
            }:
                raise ValueError(f"{assignment_path.name}: invalid revision decision")
            provenance_key = "critic_provenance" if stage == "critic" else "teacher_provenance"
            if not _valid_analysis_provenance(row.get(provenance_key)):
                raise ValueError(
                    f"{assignment_path.name}: missing structured {stage} provenance"
                )
            nonempty_fields = {
                "generation": {
                    "interpretation", "source_support", "nonparaphrase_operation",
                    "boundary_or_failure", "uncertainty",
                },
                "critic": {
                    "faithfulness", "unsupported_or_imported", "paraphrase_risk",
                    "context_risk", "missed_mechanism", "revision_instructions",
                },
                "revision": {
                    "interpretation", "source_support", "nonparaphrase_operation",
                    "boundary_or_failure", "uncertainty", "quality_reason",
                },
            }[stage]
            if any(not _nonempty(row.get(field)) for field in nonempty_fields):
                raise ValueError(f"{assignment_path.name}: empty required {stage} field")
            if row["unit_id"] in result:
                raise ValueError(f"{assignment_path.name}: duplicate {stage} unit binding")
            result[row["unit_id"]] = row
    return result


def validate_execution_ledger_receipts(
    layout: SupplementLayout = SupplementLayout(),
) -> list[str]:
    """Bind every live agent assignment/output to the recovered execution ledger."""
    errors: list[str] = []
    ledger_path = layout.root / "execution" / "ai_execution_ledger.jsonl"
    if not ledger_path.is_file():
        return ["agnostic AI execution ledger is missing"]
    rows = load_jsonl(ledger_path)
    try:
        execution_provenance.validate_execution_rows(rows)
    except ValueError as error:
        return [str(error)]
    contexts: list[tuple[str, Mapping[str, Any], Mapping[str, Any]]] = []
    assignment_paths = [
        path
        for stage in ("generation", "critic", "revision")
        for path in sorted(layout.analysis_assignments(stage).glob("*.json"))
    ] + sorted(layout.audit_assignments.glob("*.json"))
    for assignment_path in assignment_paths:
        assignment = load_json(assignment_path)
        relative = _ledger_relpath(layout, assignment_path)
        assignment_sha256 = sha256_file(assignment_path)
        output_path = Path(str(assignment.get("output_path") or ""))
        matches = [
            row
            for row in rows
            if row.get("assignment_relpath") == relative
            and row.get("assignment_sha256") == assignment_sha256
            and row.get("requires_rerun") is False
            and row.get("status") == "authoritative"
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
        if assignment.get("model_visible_packet_sha256") != model_visible_packet_sha256(
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
    errors.extend(issue42.validate_execution_receipts(contexts))
    return errors


def prepare_analysis_stage(
    stage: str,
    layout: SupplementLayout = SupplementLayout(),
    artifact_root: Path = DEFAULT_ARTIFACT_ROOT,
) -> None:
    if stage not in {"generation", "critic", "revision"}:
        raise ValueError(f"unknown supplement analysis stage: {stage}")
    stale_outputs = sorted(layout.analysis_batches(stage).glob("*.jsonl"))
    if stale_outputs:
        raise ValueError(
            f"{stage} outputs already exist; archive or reconcile them before preparing replacements"
        )
    unit_errors = validate_units(layout, artifact_root, True)
    if unit_errors:
        raise ValueError("valid materialized units are required: " + "; ".join(unit_errors))
    units = load_jsonl(layout.units)
    generation = _analysis_records(layout, "generation") if stage != "generation" else {}
    critic = _analysis_records(layout, "critic") if stage == "revision" else {}
    expected_ids = {unit["unit_id"] for unit in units}
    if stage != "generation" and set(generation) != expected_ids:
        raise ValueError("generation coverage must be complete before criticism/revision")
    if stage == "revision" and set(critic) != expected_ids:
        raise ValueError("critic coverage must be complete before revision")
    _clear_assignments(layout.analysis_assignments(stage))
    pending = [
        unit
        for unit in units
        if stage != "revision" or critic[unit["unit_id"]]["decision"] == "revise"
    ]
    grouped: dict[str, list[dict[str, Any]]] = {}
    for unit in pending:
        grouped.setdefault(unit["source_id"], []).append(unit)
    context_count = 0
    for source_id in sorted(grouped):
        source_units = grouped[source_id]
        for offset in range(0, len(source_units), SOURCE_CONTEXT_MAX_UNITS):
            chunk = source_units[offset : offset + SOURCE_CONTEXT_MAX_UNITS]
            packet_units: list[dict[str, Any]] = []
            for unit in chunk:
                unit_path = _external_artifact_root(artifact_root) / unit["artifact_relpath"]
                packet_units.append(
                    {
                        **unit,
                        "artifact_abspath": str(unit_path),
                        "content_sha256": sha256_text(
                            interchange.normalize_visible_text(
                                unit_path.read_text(encoding="utf-8")
                            )
                        ),
                    }
                )
            part = offset // SOURCE_CONTEXT_MAX_UNITS + 1
            slug = f"{_source_slug(source_id)}_part_{part:02d}"
            assignment: dict[str, Any] = {
                "stage": stage,
                "source_id": source_id,
                "expected_analysis_ids": {
                    unit["unit_id"]: _analysis_id(stage, unit) for unit in chunk
                },
                "output_path": str(layout.analysis_batches(stage) / f"{slug}.jsonl"),
                "units": packet_units,
                "expected_fields": sorted(
                    {
                        "generation": GENERATION_FIELDS,
                        "critic": CRITIC_FIELDS,
                        "revision": REVISION_FIELDS,
                    }[stage]
                ),
            }
            if stage == "generation":
                assignment["isolation_requirement"] = (
                    "Source-grounded interpretations for nearby units from one source only; keep "
                    "outputs separate and distinguish source fact, inference, representation "
                    "dependence, and uncertainty."
                )
            elif stage == "critic":
                assignment["isolation_requirement"] = (
                    "Fresh critic context for nearby units from one source only; see exact units and "
                    "compact candidates, not teacher reasoning or unrelated analyses."
                )
                assignment["candidate_analyses"] = {
                    unit["unit_id"]: _candidate_payload(generation[unit["unit_id"]])
                    for unit in chunk
                }
                assignment["candidate_bindings"] = {
                    unit["unit_id"]: _row_sha256(generation[unit["unit_id"]])
                    for unit in chunk
                }
            else:
                assignment["isolation_requirement"] = (
                    "Bounded same-source repair context; see exact units, compact candidates, and "
                    "critic findings only."
                )
                assignment["candidate_analyses"] = {
                    unit["unit_id"]: _candidate_payload(generation[unit["unit_id"]])
                    for unit in chunk
                }
                assignment["critic_findings"] = {
                    unit["unit_id"]: _candidate_payload(critic[unit["unit_id"]])
                    for unit in chunk
                }
                assignment["candidate_bindings"] = {
                    unit["unit_id"]: {
                        "generation_sha256": _row_sha256(generation[unit["unit_id"]]),
                        "critic_sha256": _row_sha256(critic[unit["unit_id"]]),
                    }
                    for unit in chunk
                }
            write_json(
                layout.analysis_assignments(stage) / f"{slug}.json",
                _bind_model_visible_packet(assignment),
            )
            context_count += 1
    print(
        f"prepared {context_count} isolated same-source {stage} contexts for "
        f"{len(pending)} units"
    )


def finalize_analysis(layout: SupplementLayout = SupplementLayout()) -> None:
    units = load_jsonl(layout.units)
    expected = [unit["unit_id"] for unit in units]
    generation = _analysis_records(layout, "generation")
    critic = _analysis_records(layout, "critic")
    if set(generation) != set(expected) or set(critic) != set(expected):
        raise ValueError("generation and critic must cover every supplement unit")
    revision = _analysis_records(layout, "revision")
    revise_ids = {unit_id for unit_id, row in critic.items() if row["decision"] == "revise"}
    if set(revision) != revise_ids:
        raise ValueError("revision coverage must exactly match critic revise decisions")
    final: list[dict[str, Any]] = []
    for unit_id in expected:
        candidate = generation[unit_id]
        finding = critic[unit_id]
        if finding["decision"] == "revise":
            repaired = revision[unit_id]
            row = {
                key: repaired[key]
                for key in FINAL_ANALYSIS_FIELDS
                if key not in {"derivation_ids"}
            }
            row["derivation_ids"] = [
                candidate["analysis_id"], finding["analysis_id"], repaired["analysis_id"]
            ]
        else:
            decision = {
                "accept_as_is": "accepted",
                "reject": "rejected",
                "quarantine": "quarantined",
            }[finding["decision"]]
            row = {
                "unit_id": unit_id,
                "decision": decision,
                "interpretation": candidate["interpretation"],
                "source_support": candidate["source_support"],
                "nonparaphrase_operation": candidate["nonparaphrase_operation"],
                "boundary_or_failure": candidate["boundary_or_failure"],
                "uncertainty": candidate["uncertainty"],
                "quality_reason": finding["faithfulness"],
                "derivation_ids": [candidate["analysis_id"], finding["analysis_id"]],
                "teacher_provenance": candidate["teacher_provenance"],
            }
        if set(row) != FINAL_ANALYSIS_FIELDS or any(
            not _nonempty(row.get(field))
            for field in (
                "interpretation", "source_support", "nonparaphrase_operation",
                "boundary_or_failure", "uncertainty", "quality_reason"
            )
        ):
            raise ValueError(f"{unit_id}: invalid final analysis")
        final.append(row)
    write_jsonl(layout.analysis_final, final)


def validate_analysis(layout: SupplementLayout = SupplementLayout()) -> list[str]:
    errors: list[str] = []
    try:
        expected = [row["unit_id"] for row in load_jsonl(layout.units)]
        rows = load_jsonl(layout.analysis_final)
        if [row.get("unit_id") for row in rows] != expected:
            errors.append("final analysis order/coverage differs from units")
        for row in rows:
            if (
                set(row) != FINAL_ANALYSIS_FIELDS
                or row.get("decision") not in {"accepted", "rejected", "quarantined"}
            ):
                errors.append(f"{row.get('unit_id')}: invalid final analysis schema")
    except (OSError, ValueError, json.JSONDecodeError) as error:
        errors.append(str(error))
    return errors


def prepare_independent_audit(
    layout: SupplementLayout = SupplementLayout(),
    artifact_root: Path = DEFAULT_ARTIFACT_ROOT,
) -> None:
    if validate_analysis(layout):
        raise ValueError("valid final analysis is required before independent audit")
    stale_outputs = sorted(layout.audit_batches.glob("*.jsonl"))
    if stale_outputs:
        raise ValueError(
            "audit outputs already exist; archive or reconcile them before preparing replacements"
        )
    units = {row["unit_id"]: row for row in load_jsonl(layout.units)}
    analyses = load_jsonl(layout.analysis_final)
    selected_ids = _independent_audit_sample_ids(list(units.values()), analyses)
    _clear_assignments(layout.audit_assignments)
    sample: list[dict[str, Any]] = []
    for analysis in analyses:
        if analysis["unit_id"] not in selected_ids:
            continue
        unit = units[analysis["unit_id"]]
        path = _external_artifact_root(artifact_root) / unit["artifact_relpath"]
        sample.append(
            {
                "unit_id": analysis["unit_id"],
                "source_id": unit["source_id"],
                "unit": {
                    **unit,
                    "artifact_abspath": str(path),
                    "artifact_sha256": sha256_file(path),
                },
                "candidate_analysis": _candidate_payload(analysis),
                "candidate_analysis_sha256": _row_sha256(analysis),
                "sampling_policy": AUDIT_SAMPLING_POLICY,
            }
        )
    write_jsonl(layout.audit_sample, sample)
    prior_sample_path = (
        layout.isolation_archive
        / "reconciliation"
        / "artifacts"
        / "audit"
        / "sample.jsonl"
    )
    prior_review_path = (
        layout.isolation_archive
        / "reconciliation"
        / "artifacts"
        / "audit"
        / "independent_review.jsonl"
    )
    carried = (
        exact_audit_carry(
            sample, load_jsonl(prior_sample_path), load_jsonl(prior_review_path)
        )
        if prior_sample_path.is_file() and prior_review_path.is_file()
        else []
    )
    write_jsonl(layout.audit_carried, carried)
    carried_ids = {row["unit_id"] for row in carried}
    selected_by_source: dict[str, list[dict[str, Any]]] = {}
    for analysis in analyses:
        if analysis["unit_id"] in selected_ids and analysis["unit_id"] not in carried_ids:
            selected_by_source.setdefault(
                units[analysis["unit_id"]]["source_id"], []
            ).append(analysis)
    for source_id in sorted(selected_by_source):
        source_analyses = selected_by_source[source_id]
        for offset in range(0, len(source_analyses), SOURCE_CONTEXT_MAX_UNITS):
            chunk = source_analyses[offset : offset + SOURCE_CONTEXT_MAX_UNITS]
            packet_units: list[dict[str, Any]] = []
            for analysis in chunk:
                unit = units[analysis["unit_id"]]
                path = _external_artifact_root(artifact_root) / unit["artifact_relpath"]
                packet_units.append(
                    {
                        **unit,
                        "artifact_abspath": str(path),
                        "artifact_sha256": sha256_file(path),
                    }
                )
            part = offset // SOURCE_CONTEXT_MAX_UNITS + 1
            slug = f"{_source_slug(source_id)}_part_{part:02d}"
            write_json(
                layout.audit_assignments / f"{slug}.json",
                _bind_model_visible_packet({
                    "stage": "audit",
                    "task": "fresh independent agnostic supplement audit",
                    "sampling_policy": AUDIT_SAMPLING_POLICY,
                    "isolation_requirement": (
                        "Read only this same-source assignment and exact bound source units; "
                        "independently test faithfulness, non-paraphrase value, representation "
                        "sensitivity, and claimed ecosystem contribution."
                    ),
                    "expected_fields": sorted(AUDIT_FIELDS),
                    "field_contract": {
                        "decision": ["accept", "quarantine", "reject"],
                        "ecosystem_contribution": [
                            "new_mechanism",
                            "refinement_or_relation",
                            "repeats_represented_mechanism",
                            "unresolved",
                        ],
                        "quality_dimensions": (
                            "faithfulness, context_sufficiency, nonparaphrase_value, "
                            "specificity, representation_sensitivity, and "
                            "uncertainty_discipline are concise evidence-specific free text"
                        ),
                        "reviewer_provenance": (
                            "structured kind, model_family, exact_service_checkpoint, "
                            "agent_task_path, and review_scope"
                        ),
                    },
                    "output_path": str(layout.audit_batches / f"{slug}.jsonl"),
                    "units": packet_units,
                    "candidate_analyses": {
                        analysis["unit_id"]: _candidate_payload(analysis)
                        for analysis in chunk
                    },
                    "candidate_bindings": {
                        analysis["unit_id"]: _row_sha256(analysis)
                        for analysis in chunk
                    },
                }),
            )


def _independent_audit_sample_ids(
    units: list[dict[str, Any]], analyses: list[dict[str, Any]]
) -> set[str]:
    """Select a reproducible stratified QA sample without rereading every accepted unit."""
    analysis_by_id = {row["unit_id"]: row for row in analyses}
    selected = {
        unit_id
        for unit_id, analysis in analysis_by_id.items()
        if analysis.get("decision") != "accepted"
    }

    def add_one_per(field: str) -> None:
        grouped: dict[str, list[dict[str, Any]]] = {}
        for unit in units:
            grouped.setdefault(str(unit.get(field) or "unknown"), []).append(unit)
        for rows in grouped.values():
            selected_unit = min(
                rows, key=lambda row: sha256_text(str(row["unit_id"]))
            )
            selected.add(selected_unit["unit_id"])

    add_one_per("source_id")
    add_one_per("unit_type")
    selected.update(
        unit["unit_id"]
        for unit in units
        if int(sha256_text(str(unit["unit_id"]))[:8], 16) % 10 == 0
    )
    return selected


def combine_independent_audit(layout: SupplementLayout = SupplementLayout()) -> None:
    by_id: dict[str, dict[str, Any]] = {}
    for row in load_jsonl(layout.audit_carried):
        if row.get("unit_id") in by_id:
            raise ValueError(f"duplicate carried audit unit: {row.get('unit_id')}")
        by_id[str(row.get("unit_id") or "")] = row
    for assignment_path in sorted(layout.audit_assignments.glob("*.json")):
        assignment = load_json(assignment_path)
        if assignment.get("model_visible_packet_sha256") != model_visible_packet_sha256(
            assignment
        ):
            raise ValueError(f"{assignment_path.name}: invalid execution packet fingerprint")
        output = load_jsonl(Path(assignment["output_path"]))
        units = assignment.get("units") or [assignment["unit"]]
        if len(output) != len(units) or [row.get("unit_id") for row in output] != [
            unit["unit_id"] for unit in units
        ]:
            raise ValueError(f"{assignment_path.name}: audit output order/coverage mismatch")
        for row in output:
            if (
                set(row) != AUDIT_FIELDS
                or row.get("decision") not in {"accept", "quarantine", "reject"}
                or row.get("ecosystem_contribution") not in {
                    "new_mechanism", "refinement_or_relation",
                    "repeats_represented_mechanism", "unresolved"
                }
                or not _valid_analysis_provenance(row.get("reviewer_provenance"))
            ):
                raise ValueError(f"{assignment_path.name}: invalid independent audit row")
            unit_id = str(row["unit_id"])
            if unit_id in by_id:
                raise ValueError(f"duplicate independent audit unit: {unit_id}")
            by_id[unit_id] = row
    expected = [row["unit_id"] for row in load_jsonl(layout.audit_sample)]
    if set(by_id) != set(expected):
        raise ValueError("independent audit does not cover the exact canonical sample")
    write_jsonl(layout.audit_final, [by_id[unit_id] for unit_id in expected])


def validate_audit(layout: SupplementLayout = SupplementLayout()) -> list[str]:
    expected = [row["unit_id"] for row in load_jsonl(layout.audit_sample)]
    rows = load_jsonl(layout.audit_final)
    errors: list[str] = []
    deterministic_sample = _independent_audit_sample_ids(
        load_jsonl(layout.units), load_jsonl(layout.analysis_final)
    )
    if set(expected) != deterministic_sample:
        errors.append("independent-audit assignments differ from deterministic QA sample")
    if [row.get("unit_id") for row in rows] != expected:
        errors.append("independent audit does not cover the exact deterministic QA sample")
    prior_sample_path = (
        layout.isolation_archive / "reconciliation/artifacts/audit/sample.jsonl"
    )
    prior_review_path = (
        layout.isolation_archive
        / "reconciliation/artifacts/audit/independent_review.jsonl"
    )
    try:
        exact_carried = (
            exact_audit_carry(
                load_jsonl(layout.audit_sample),
                load_jsonl(prior_sample_path),
                load_jsonl(prior_review_path),
            )
            if prior_sample_path.is_file() and prior_review_path.is_file()
            else []
        )
        if load_jsonl(layout.audit_carried) != exact_carried:
            errors.append("audit carry differs from exact canonical sample-packet equality")
    except ValueError as error:
        errors.append(str(error))
    for row in rows:
        if (
            set(row) != AUDIT_FIELDS
            or row.get("decision") not in {"accept", "quarantine", "reject"}
            or not _valid_analysis_provenance(row.get("reviewer_provenance"))
        ):
            errors.append(f"{row.get('unit_id')}: invalid audit schema/decision")
    return errors


def _content_loader(artifact_root: Path):
    artifact_root = _external_artifact_root(artifact_root)

    def load(record: Mapping[str, Any]) -> str:
        if isinstance(record.get("content"), str):
            return str(record["content"])
        prefix = f"artifact://{RELEASE_ID}/"
        reference = str(record.get("content_ref") or "")
        if not reference.startswith(prefix):
            raise ValueError(f"unsupported supplement content reference: {reference}")
        relative = Path(reference.removeprefix(prefix))
        if relative.is_absolute() or ".." in relative.parts:
            raise ValueError(f"unsafe supplement content reference: {reference}")
        return (artifact_root / relative).read_text(encoding="utf-8")

    return load


def _representation_dependencies(unit: Mapping[str, Any]) -> list[dict[str, Any]]:
    dependency = str(unit.get("representation_dependency") or "").strip()
    if not dependency or dependency.lower() in {"none", "not required", "none identified"}:
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


def build_objects(
    layout: SupplementLayout = SupplementLayout(),
    artifact_root: Path = DEFAULT_ARTIFACT_ROOT,
) -> None:
    errors = [*validate_units(layout, artifact_root, True), *validate_analysis(layout), *validate_audit(layout)]
    if errors:
        raise ValueError("cannot build invalid supplement: " + "; ".join(errors))
    _, intake = intake_records(layout, artifact_root)
    intake_by_id = {row["canonical_source_id"]: row for row in intake}
    units = load_jsonl(layout.units)
    analyses = {row["unit_id"]: row for row in load_jsonl(layout.analysis_final)}
    audits = {row["unit_id"]: row for row in load_jsonl(layout.audit_final)}
    objects: list[dict[str, Any]] = []
    for unit in units:
        source = intake_by_id[unit["source_id"]]
        path = _external_artifact_root(artifact_root) / unit["artifact_relpath"]
        content = interchange.normalize_visible_text(path.read_text(encoding="utf-8"))
        content_hash = sha256_text(content)
        keys = sorted(
            set(source.get("identity_keys") or [])
            | {f"source-id:{unit['source_id']}", f"source-unit:{unit['unit_id']}"}
        )
        source_id = interchange.stable_object_id("source", content_hash, keys, [])
        source_record = {
            "contract_version": interchange.CONTRACT_VERSION,
            "corpus_release_id": RELEASE_ID,
            "object_id": source_id,
            "object_role": "source",
            "corpus_origin": "agnostic",
            "source_ids": [unit["source_id"]],
            "source_unit_ids": [unit["unit_id"]],
            "span_lineage": [
                {
                    "source_id": unit["source_id"],
                    "source_unit_id": unit["unit_id"],
                    "line_start": unit["line_start"],
                    "line_end": unit["line_end"],
                    "source_normalized_sha256": unit["source_normalized_sha256"],
                    "unit_sha256": unit["artifact_sha256"],
                }
            ],
            "content_sha256": content_hash,
            "content_ref": f"artifact://{RELEASE_ID}/{unit['artifact_relpath']}",
            "parent_ids": [],
            "derivation_ids": ["issue-42-agnostic-openalex-exact-span"],
            "teacher_provenance": unit["segmentation_provenance"],
            "quality_state": "accepted",
            "training_eligibility": "eligible",
            "exclusion_reason": None,
            "licensing_boundary": (
                "source text retained external to Git; public access does not imply redistribution; "
                f"reported license={source.get('license')!r}; access={source.get('access_boundary')!r}"
            ),
            "representation_dependencies": _representation_dependencies(unit),
            "canonical_source_keys": keys,
            "corpus_local_audit": {
                "parent_release_id": PARENT_RELEASE_ID,
                "parent_freeze_id": PARENT_FREEZE_ID,
                "handoff_id": HANDOFF_ID,
                "selection_reason": unit["selection_reason"],
                "ecosystem_findings": unit["ecosystem_findings"],
            },
        }
        objects.append(source_record)
        analysis = analyses[unit["unit_id"]]
        audit = audits.get(unit["unit_id"])
        quality = analysis["decision"]
        if quality == "accepted" and audit and audit["decision"] in {"quarantine", "reject"}:
            quality = "quarantined" if audit["decision"] == "quarantine" else "rejected"
        interpretation = interchange.normalize_visible_text(analysis["interpretation"])
        interpretation_hash = sha256_text(interpretation)
        objects.append(
            {
                "contract_version": interchange.CONTRACT_VERSION,
                "corpus_release_id": RELEASE_ID,
                "object_id": interchange.stable_object_id(
                    "interpretation", interpretation_hash, keys, [source_id]
                ),
                "object_role": "interpretation",
                "corpus_origin": "agnostic",
                "source_ids": [unit["source_id"]],
                "source_unit_ids": [unit["unit_id"]],
                "span_lineage": source_record["span_lineage"],
                "content_sha256": interpretation_hash,
                "content": interpretation,
                "parent_ids": [source_id],
                "derivation_ids": analysis["derivation_ids"],
                "teacher_provenance": analysis["teacher_provenance"],
                "quality_state": quality,
                "training_eligibility": "eligible" if quality == "accepted" else "ineligible",
                "exclusion_reason": None if quality == "accepted" else (
                    "independent supplement audit: " + str(audit["notes"])
                ),
                "licensing_boundary": "source-grounded teacher derivative retained in Git; source remains external",
                "representation_dependencies": [],
                "canonical_source_keys": keys,
                "corpus_local_audit": {
                    "analysis_quality_reason": analysis["quality_reason"],
                    "source_support": analysis["source_support"],
                    "boundary_or_failure": analysis["boundary_or_failure"],
                    "independent_audit": audit or {
                        "decision": "not_sampled",
                        "sampling_policy": AUDIT_SAMPLING_POLICY,
                    },
                },
            }
        )
    write_jsonl(layout.objects, objects)
    release_errors = (
        interchange.validate_release(objects, _content_loader(artifact_root))
        if objects
        else []
    )
    if release_errors:
        raise ValueError("invalid canonical supplement records: " + "; ".join(release_errors))


def write_trainable_manifest(
    layout: SupplementLayout = SupplementLayout(),
    artifact_root: Path = DEFAULT_ARTIFACT_ROOT,
) -> None:
    records = load_jsonl(layout.objects)
    errors = (
        interchange.validate_release(records, _content_loader(artifact_root))
        if records
        else []
    )
    if errors:
        raise ValueError("invalid supplement records: " + "; ".join(errors))
    eligible = [row for row in records if row["training_eligibility"] == "eligible"]
    identity = {
        "contract_version": interchange.CONTRACT_VERSION,
        "corpus_release_id": RELEASE_ID,
        "parent_release_id": PARENT_RELEASE_ID,
        "parent_freeze_id": PARENT_FREEZE_ID,
        "renderer_sha256": sha256_file(Path(interchange.__file__)),
        "eligible_object_ids": [row["object_id"] for row in eligible],
        "object_counts": dict(sorted(Counter(row["object_role"] for row in eligible).items())),
    }
    write_json(
        layout.trainable_manifest,
        {
            **identity,
            "manifest_id": "agnostic_openalex_supplement_" + sha256_text(canonical_json(identity)),
            "purpose": "corpus packaging only; no training or mixing-ratio authorization",
        },
    )


def derived_processing_metrics(layout: SupplementLayout = SupplementLayout()) -> dict[str, Any]:
    intake = load_jsonl(layout.intake)
    screening = load_jsonl(layout.screening_final)
    units = load_jsonl(layout.units)
    objects = load_jsonl(layout.objects)
    findings = [
        finding
        for _, plan in _plan_rows(layout)
        for finding in plan.get("ecosystem_findings") or []
    ]

    def identifiers(kind: str) -> list[str]:
        return sorted({row["identifier"] for row in findings if row["kind"] == kind})

    interpretations = [row for row in objects if row.get("object_role") == "interpretation"]
    audit_rows = load_jsonl(layout.audit_final)
    decisions = Counter(row.get("decision") for row in screening)
    intake_decisions = Counter(row.get("disposition") for row in intake)

    def stage_byte_proxy(stage: str, assignment_root: Path) -> dict[str, int]:
        completed_contexts = analyzed_items = input_bytes = output_bytes = 0
        for assignment_path in sorted(assignment_root.glob("*.json")):
            assignment = load_json(assignment_path)
            output_path = Path(str(assignment.get("output_path") or ""))
            if not output_path.is_file():
                continue
            completed_contexts += 1
            analyzed_items += len(load_jsonl(output_path))
            input_bytes += assignment_path.stat().st_size
            if stage in {"screening", "depth"}:
                input_bytes += int((assignment.get("source") or {}).get("normalized_bytes") or 0)
            else:
                packet_units = assignment.get("units") or [assignment.get("unit") or {}]
                input_bytes += sum(
                    int(unit.get("artifact_bytes") or 0) for unit in packet_units
                )
            output_bytes += output_path.stat().st_size
        return {
            "completed_agent_contexts": completed_contexts,
            "analyzed_items": analyzed_items,
            "observable_input_bytes_proxy": input_bytes,
            "observable_output_bytes": output_bytes,
            "approximate_input_tokens_at_four_bytes_each": input_bytes // 4,
            "approximate_output_tokens_at_four_bytes_each": output_bytes // 4,
        }

    byte_proxies = {
        "screening": stage_byte_proxy("screening", layout.screening_assignments),
        "depth": stage_byte_proxy("depth", layout.depth_assignments),
        **{
            stage: stage_byte_proxy(stage, layout.analysis_assignments(stage))
            for stage in ("generation", "critic", "revision")
        },
        "audit": stage_byte_proxy("audit", layout.audit_assignments),
    }
    metrics = {
        "sources_received": len(intake),
        "sources_deduplicated": intake_decisions["deduplicated_or_already_represented"],
        "sources_useful": decisions["useful"],
        "sources_rejected": decisions["reject"] + decisions["quarantine"]
        + intake_decisions["quarantined_ambiguous_source_identity"],
        "semantic_units": len(units),
        "derivatives_accepted": sum(row.get("quality_state") == "accepted" for row in interpretations),
        "derivatives_quarantined": sum(row.get("quality_state") == "quarantined" for row in interpretations),
        "derivatives_rejected": sum(row.get("quality_state") == "rejected" for row in interpretations),
        "reinforced_44_lenses": identifiers("reinforced_44_lens"),
        "materially_extended_44_lenses": identifiers("materially_extended_44_lens"),
        "new_families": identifiers("new_family"),
        "novelty_status": (
            "unconfirmed: lens extensions and new-family identifiers are source-grounded "
            "working-map gap candidates, not claims of mathematical novelty"
        ),
        "saturation_probes_challenged": identifiers("saturation_probe_challenged"),
        "saturation_probes_strengthened": identifiers("saturation_probe_strengthened"),
        "new_geometry_dependencies": identifiers("new_geometry_dependency"),
        "cross_domain_syntheses": [],
        "independent_audit": {
            "sampling_policy": AUDIT_SAMPLING_POLICY,
            "sampled_units": len(audit_rows),
            "sample_fraction": len(audit_rows) / max(1, len(units)),
            "decisions": dict(sorted(Counter(row.get("decision") for row in audit_rows).items())),
        },
        "agent_efficiency": {
            "exact_token_telemetry_available": False,
            "measurement_note": (
                "Exact collaboration-agent token telemetry is unavailable. Retained assignment, "
                "bound source/unit, and output byte counts are transparent proxies and are not "
                "claimed as exact token usage per accepted source or unit."
            ),
            "observable_byte_proxies_by_stage": byte_proxies,
        },
    }
    return metrics


def write_processing_metrics(layout: SupplementLayout = SupplementLayout()) -> None:
    metrics = derived_processing_metrics(layout)
    identity = {
        "metrics_version": "agnostic-openalex-supplement-processing-v1",
        "handoff_id": HANDOFF_ID,
        "parent_freeze_id": PARENT_FREEZE_ID,
        "processing_metrics": metrics,
    }
    write_json(
        layout.metrics,
        {
            **identity,
            "metrics_id": "agnostic_openalex_metrics_" + sha256_text(canonical_json(identity)),
        },
    )


def validate_release_ready(
    layout: SupplementLayout = SupplementLayout(),
    artifact_root: Path = DEFAULT_ARTIFACT_ROOT,
) -> list[str]:
    errors = [
        *validate_intake(layout, artifact_root),
        *validate_source_screening(layout, True),
        *validate_units(layout, artifact_root, True),
        *validate_analysis(layout),
        *validate_audit(layout),
        *validate_execution_ledger_receipts(layout),
    ]
    records = load_jsonl(layout.objects)
    screening = load_jsonl(layout.screening_final)
    if records:
        errors.extend(interchange.validate_release(records, _content_loader(artifact_root)))
        if any(
            row.get("corpus_release_id") != RELEASE_ID
            or row.get("corpus_origin") != "agnostic"
            or any("riemann" in str(source_id).lower() for source_id in row.get("source_ids") or [])
            for row in records
        ):
            errors.append("supplement records cross the agnostic/Riemann release boundary")
    elif any(row.get("decision") == "useful" for row in screening):
        errors.append("useful screened sources lack canonical supplement records")
    if not layout.trainable_manifest.is_file():
        errors.append("supplement trainable manifest is missing")
    else:
        manifest = load_json(layout.trainable_manifest)
        eligible = [row["object_id"] for row in records if row.get("training_eligibility") == "eligible"]
        if (
            manifest.get("contract_version") != interchange.CONTRACT_VERSION
            or manifest.get("corpus_release_id") != RELEASE_ID
            or manifest.get("parent_freeze_id") != PARENT_FREEZE_ID
            or manifest.get("eligible_object_ids") != eligible
        ):
            errors.append("supplement trainable manifest mismatch")
        manifest_identity = {
            key: manifest[key]
            for key in (
                "contract_version", "corpus_release_id", "parent_release_id",
                "parent_freeze_id", "renderer_sha256", "eligible_object_ids", "object_counts",
            )
        }
        if manifest.get("manifest_id") != "agnostic_openalex_supplement_" + sha256_text(
            canonical_json(manifest_identity)
        ):
            errors.append("supplement trainable manifest identity mismatch")
    if not layout.metrics.is_file():
        errors.append("supplement processing metrics are missing")
    else:
        metrics = load_json(layout.metrics)
        identity = {
            key: metrics[key]
            for key in ("metrics_version", "handoff_id", "parent_freeze_id", "processing_metrics")
        }
        if (
            metrics.get("metrics_id")
            != "agnostic_openalex_metrics_" + sha256_text(canonical_json(identity))
            or metrics.get("processing_metrics") != derived_processing_metrics(layout)
        ):
            errors.append("supplement processing metrics drift")
        processing = metrics.get("processing_metrics") or {}
        if (
            processing.get("sources_deduplicated", 0)
            + processing.get("sources_useful", 0)
            + processing.get("sources_rejected", 0)
            != processing.get("sources_received", 0)
        ):
            errors.append("supplement source dispositions do not account for intake")
    return errors


def write_report(layout: SupplementLayout = SupplementLayout()) -> None:
    metrics = load_json(layout.metrics)["processing_metrics"]
    manifest = load_json(layout.trainable_manifest)
    report = [
        "# Agnostic Mathia OpenAlex supplement v1",
        "",
        f"Parent: `{PARENT_RELEASE_ID}` freeze `{PARENT_FREEZE_ID}` (immutable).",
        (
            f"Authoritative offline handoff: `{HANDOFF_ID}`; immutable "
            f"`{SUPERSEDED_HANDOFF_ID}` is retained as superseded evidence. Release: `{RELEASE_ID}`."
        ),
        "",
        "This is corpus packaging only. It authorizes no training, GPU work, or mixing ratio.",
        "The OpenAlex routing metadata was not treated as proof of conceptual novelty; every useful "
        "source, unit, interpretation, and audit decision is retained separately.",
        "",
        f"Processing metrics: `{metrics}`.",
        f"Eligible canonical objects: {len(manifest['eligible_object_ids'])}.",
        "Riemann records and artifacts are not members of this release lineage.",
    ]
    layout.report.parent.mkdir(parents=True, exist_ok=True)
    layout.report.write_text("\n".join(report) + "\n", encoding="utf-8")


def freeze_release(
    layout: SupplementLayout = SupplementLayout(),
    artifact_root: Path = DEFAULT_ARTIFACT_ROOT,
) -> str:
    errors = validate_release_ready(layout, artifact_root)
    if errors:
        raise ValueError("cannot freeze invalid supplement: " + "; ".join(errors))
    write_report(layout)
    bundle = issue42._validate_openalex_handoff_bundle(
        _bundle_root(artifact_root), HANDOFF_ID, HANDOFF_STREAM
    )
    files = [
        {
            "path": path.relative_to(layout.root).as_posix(),
            "sha256": sha256_file(path),
            "bytes": path.stat().st_size,
        }
        for path in sorted(layout.root.rglob("*"))
        if path.is_file()
        and path != layout.freeze
        and layout.isolation_archive not in path.parents
        and "__pycache__" not in path.parts
    ]
    final_decision = (
        "AGNOSTIC_MATHIA_OPENALEX_SUPPLEMENT_READY"
        if load_jsonl(layout.objects)
        else "NO_USEFUL_AGNOSTIC_OPENALEX_SOURCES"
    )
    identity = {
        "contract_version": interchange.CONTRACT_VERSION,
        "release_id": RELEASE_ID,
        "parent_release_id": PARENT_RELEASE_ID,
        "parent_freeze_id": PARENT_FREEZE_ID,
        "handoff_id": HANDOFF_ID,
        "handoff_freeze_id": bundle["freeze"]["freeze_id"],
        "handoff_freeze_sha256": bundle["freeze_sha256"],
        "final_decision": final_decision,
        "files": files,
    }
    freeze_id = "agnostic_openalex_supplement_" + sha256_text(canonical_json(identity))
    write_json(
        layout.freeze,
        {
            **identity,
            "freeze_id": freeze_id,
            "frozen_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
            "training_or_gpu_work_performed": False,
        },
    )
    return freeze_id


def validate_freeze(
    layout: SupplementLayout = SupplementLayout(),
    artifact_root: Path = DEFAULT_ARTIFACT_ROOT,
) -> list[str]:
    errors = validate_release_ready(layout, artifact_root)
    if not layout.freeze.is_file():
        return [*errors, "supplement freeze is missing"]
    freeze = load_json(layout.freeze)
    identity = {
        key: freeze[key]
        for key in (
            "contract_version", "release_id", "parent_release_id", "parent_freeze_id",
            "handoff_id", "handoff_freeze_id", "handoff_freeze_sha256", "final_decision", "files"
        )
    }
    if freeze.get("freeze_id") != "agnostic_openalex_supplement_" + sha256_text(
        canonical_json(identity)
    ):
        errors.append("supplement freeze identity mismatch")
    try:
        bundle = issue42._validate_openalex_handoff_bundle(
            _bundle_root(artifact_root), HANDOFF_ID, HANDOFF_STREAM
        )
        if (
            freeze.get("handoff_freeze_id") != bundle["freeze"]["freeze_id"]
            or freeze.get("handoff_freeze_sha256") != bundle["freeze_sha256"]
        ):
            errors.append("supplement freeze handoff binding mismatch")
    except (OSError, ValueError, json.JSONDecodeError) as error:
        errors.append(str(error))
    for descriptor in freeze.get("files") or []:
        if str(descriptor.get("path") or "").startswith(
            layout.isolation_archive.name + "/"
        ):
            errors.append("supplement freeze must exclude the non-authoritative archive")
            continue
        path = layout.root / descriptor["path"]
        if (
            not path.is_file()
            or path.stat().st_size != descriptor["bytes"]
            or sha256_file(path) != descriptor["sha256"]
        ):
            errors.append(f"supplement frozen file drift: {descriptor['path']}")
    return errors


def update_handoff_state(
    state_path: Path,
    layout: SupplementLayout = SupplementLayout(),
    artifact_root: Path = DEFAULT_ARTIFACT_ROOT,
) -> None:
    errors = validate_freeze(layout, artifact_root)
    if errors:
        raise ValueError("cannot complete handoff state: " + "; ".join(errors))
    state = load_json(state_path)
    consumed = state["streams"][HANDOFF_STREAM].get("consumed") or []
    row = next((item for item in consumed if item.get("handoff_id") == HANDOFF_ID), None)
    if row is None:
        raise ValueError("agnostic handoff is not registered as consumed")
    freeze = load_json(layout.freeze)
    metrics = load_json(layout.metrics)["processing_metrics"]
    row.update(
        {
            "processing_status": "complete",
            "supplement_release_id": RELEASE_ID,
            "supplement_freeze_id": freeze["freeze_id"],
            "supplement_freeze_path": str(layout.freeze),
            "supplement_freeze_sha256": sha256_file(layout.freeze),
        }
    )
    state["streams"][HANDOFF_STREAM]["processing_metrics"] = metrics
    state["finalization_allowed"] = issue42._openalex_finalization_allowed(state)
    write_json(state_path, state)


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "command",
        choices=(
            "validate-intake", "prepare-screening", "combine-screening",
            "prepare-depth", "validate-depth", "materialize-units", "validate-units",
            "prepare-analysis", "finalize-analysis", "prepare-audit", "combine-audit",
            "prepare-source-isolation-rerun",
            "build-objects", "write-manifest", "write-metrics", "validate-release",
            "freeze", "validate-freeze", "update-handoff-state",
        ),
    )
    parser.add_argument("--artifact-root", type=Path, default=DEFAULT_ARTIFACT_ROOT)
    parser.add_argument("--stage", choices=("generation", "critic", "revision"))
    parser.add_argument("--state-path", type=Path, default=issue42.OPENALEX_HANDOFF_STATE_PATH)
    args = parser.parse_args(list(argv) if argv is not None else None)
    layout = SupplementLayout()
    if args.command == "validate-intake":
        errors = validate_intake(layout, args.artifact_root)
    elif args.command == "prepare-screening":
        prepare_source_screening(layout, args.artifact_root); return 0
    elif args.command == "combine-screening":
        combine_source_screening(layout); return 0
    elif args.command == "prepare-depth":
        prepare_depth_plans(layout, args.artifact_root); return 0
    elif args.command == "validate-depth":
        errors = validate_depth_plans(layout, True)
    elif args.command == "materialize-units":
        materialize_units(layout, args.artifact_root); return 0
    elif args.command == "validate-units":
        errors = validate_units(layout, args.artifact_root, True)
    elif args.command == "prepare-analysis":
        if not args.stage:
            parser.error("--stage is required for prepare-analysis")
        prepare_analysis_stage(args.stage, layout, args.artifact_root); return 0
    elif args.command == "prepare-source-isolation-rerun":
        print(canonical_json(prepare_source_isolation_rerun(layout))); return 0
    elif args.command == "finalize-analysis":
        finalize_analysis(layout); return 0
    elif args.command == "prepare-audit":
        prepare_independent_audit(layout, args.artifact_root); return 0
    elif args.command == "combine-audit":
        combine_independent_audit(layout); return 0
    elif args.command == "build-objects":
        build_objects(layout, args.artifact_root); return 0
    elif args.command == "write-manifest":
        write_trainable_manifest(layout, args.artifact_root); return 0
    elif args.command == "write-metrics":
        write_processing_metrics(layout); return 0
    elif args.command == "validate-release":
        errors = validate_release_ready(layout, args.artifact_root)
    elif args.command == "freeze":
        print(freeze_release(layout, args.artifact_root)); return 0
    elif args.command == "validate-freeze":
        errors = validate_freeze(layout, args.artifact_root)
    else:
        update_handoff_state(args.state_path, layout, args.artifact_root); return 0
    if errors:
        print("\n".join(errors))
        return 1
    print(f"{args.command} passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
