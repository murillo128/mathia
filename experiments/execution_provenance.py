"""Recover compact, non-sensitive AI execution provenance from local Codex logs.

This utility is deliberately offline and environment-local.  It reads rollout
JSONL files, but retains only a strict allowlist of execution identifiers,
configuration values, repository paths, counts, and SHA-256 digests.  It never
emits prompts, instructions, reasoning, encrypted payloads, tool output bodies,
environment variables, credentials, or local Codex storage paths.

The checked-in ledgers are current recovery evidence, not a portable promise
that CI has access to the original local rollout archive.  Use ``--write`` only
in the original execution environment; use ``--validate`` anywhere.
"""

from __future__ import annotations

import argparse
import dataclasses
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


REPO_ROOT = Path(__file__).resolve().parents[1]
RIEMANN_ROOT = REPO_ROOT / "experiments" / "riemann_corpus" / "full_corpus_v2"
AGNOSTIC_ROOT = (
    REPO_ROOT
    / "experiments"
    / "agnostic_mathia_corpus"
    / "openalex_supplement_v1"
)
ISOLATION_ARCHIVE_NAME = "non_authoritative_source_isolation_run"
ISOLATION_ARCHIVE_NAMES = (
    ISOLATION_ARCHIVE_NAME,
    "non_authoritative_source_isolation_correction_v2",
)
RIEMANN_ISOLATION_ARCHIVE = RIEMANN_ROOT / ISOLATION_ARCHIVE_NAME
AGNOSTIC_ISOLATION_ARCHIVE = AGNOSTIC_ROOT / ISOLATION_ARCHIVE_NAME
DEFAULT_ARCHIVE_ROOTS = (RIEMANN_ROOT, AGNOSTIC_ROOT)

RIEMANN_AUDIT_LEDGER = RIEMANN_ROOT / "execution" / "ai_execution_ledger.jsonl"
RIEMANN_DECISION_MAP = RIEMANN_ROOT / "audit" / "decision_execution_map.jsonl"
LEGACY_CONTEXT_LEDGER = RIEMANN_ROOT / "execution" / "legacy_context_recovery.jsonl"
AGNOSTIC_EXECUTION_LEDGER = AGNOSTIC_ROOT / "execution" / "ai_execution_ledger.jsonl"

SCHEMA_VERSION = 1
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
UUID_RE = re.compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
)
SENSITIVE_PATTERNS = (
    "encrypted_content",
    "gAAAA",
    "sk-",
    "bearer ",
    "authorization",
    "api_key",
    "openai_api_key",
    "/root/.codex",
)

EXECUTION_FIELDS = frozenset(
    {
        "schema_version",
        "ledger_kind",
        "ledger_id",
        "release_id",
        "stage",
        "status",
        "requires_rerun",
        "rerun_reason",
        "assignment_relpath",
        "assignment_sha256",
        "prompt_relpath",
        "prompt_sha256",
        "prompt_recovery_status",
        "execution_brief_relpath",
        "execution_brief_sha256",
        "agent_task_path",
        "thread_id",
        "turn_id",
        "parent_thread_id",
        "timestamp",
        "client",
        "cli_version",
        "originator",
        "provider",
        "model_selector",
        "service_checkpoint_id",
        "reasoning_effort",
        "comp_hash",
        "sandbox_type",
        "approval_policy",
        "session_cwd",
        "tool_workdir",
        "task_envelope_ciphertext_sha256",
        "output_relpath",
        "output_sha256",
        "output_records",
        "recovery_quality",
        "source_provenance_relpath",
        "superseded_by_thread_id",
    }
)

DECISION_FIELDS = frozenset(
    {
        "schema_version",
        "ledger_kind",
        "release_id",
        "object_id",
        "state",
        "execution_ledger_id",
        "assignment_sha256",
        "output_sha256",
        "decision_canonical_sha256",
    }
)

ARCHIVE_MANIFEST_FIELDS = frozenset(
    {
        "archive_relpath",
        "authoritative",
        "bytes",
        "category",
        "original_relpath",
        "pool",
        "reason",
        "reconciliation_eligible",
        "replacement_required",
        "sha256",
        "trainable",
    }
)


@dataclasses.dataclass(frozen=True)
class Envelope:
    index: int
    turn_id: str | None
    ciphertext_sha256: str


@dataclasses.dataclass(frozen=True)
class ToolCall:
    index: int
    call_id: str | None
    turn_id: str | None
    timestamp: str | None
    input_text: str


@dataclasses.dataclass
class Session:
    thread_id: str
    parent_thread_id: str | None
    agent_task_path: str | None
    timestamp: str | None
    cli_version: str | None
    originator: str | None
    provider: str | None
    session_cwd: str | None
    turn_contexts: dict[str, dict[str, Any]]
    first_turn_context: dict[str, Any]
    envelopes: list[Envelope]
    calls: list[ToolCall]

    def context_for(self, turn_id: str | None) -> Mapping[str, Any]:
        if turn_id and turn_id in self.turn_contexts:
            return self.turn_contexts[turn_id]
        return self.first_turn_context

    def envelope_for(self, call: ToolCall) -> Envelope | None:
        same_turn = [
            item
            for item in self.envelopes
            if item.index < call.index and item.turn_id == call.turn_id
        ]
        if same_turn:
            return same_turn[-1]
        prior = [item for item in self.envelopes if item.index < call.index]
        return prior[-1] if prior else None


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def canonical_sha256(value: Mapping[str, Any]) -> str:
    payload = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return sha256_bytes(payload)


def jsonl_rows(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


def count_jsonl(path: Path) -> int:
    with path.open(encoding="utf-8") as handle:
        return sum(1 for line in handle if line.strip())


def contained_path(root: Path, relpath: str) -> Path:
    """Resolve a repository-relative path without permitting directory escape."""

    if not isinstance(relpath, str) or not relpath or Path(relpath).is_absolute():
        raise ValueError(f"unsafe relative artifact path: {relpath!r}")
    root = root.resolve()
    candidate = (root / relpath).resolve()
    try:
        candidate.relative_to(root)
    except ValueError as error:
        raise ValueError(f"artifact path escapes its root: {relpath!r}") from error
    return candidate


def resolve_ledger_artifact(
    relpath: str,
    expected_sha256: str,
    *,
    repo_root: Path = REPO_ROOT,
    archive_roots: Sequence[Path] | None = None,
) -> tuple[Path, str]:
    """Resolve a live or isolation-archived artifact by its exact digest.

    Ledgers intentionally retain the original repository path after archival.
    The archive manifest is the only accepted redirection: a basename search
    would be ambiguous and could silently bind the wrong historical packet.
    """

    if not isinstance(expected_sha256, str) or not SHA256_RE.fullmatch(
        expected_sha256
    ):
        raise ValueError(f"invalid artifact SHA-256: {expected_sha256!r}")
    repo_root = repo_root.resolve()
    live_path = contained_path(repo_root, relpath)
    if live_path.is_file() and sha256_file(live_path) == expected_sha256:
        return live_path, "live"

    roots = tuple(archive_roots or DEFAULT_ARCHIVE_ROOTS)
    matches: list[Path] = []
    for raw_artifact_root in roots:
        artifact_root = raw_artifact_root.resolve()
        try:
            original_relpath = live_path.relative_to(artifact_root).as_posix()
        except ValueError:
            continue
        for archive_name in ISOLATION_ARCHIVE_NAMES:
            archive_root = artifact_root / archive_name
            manifest_path = archive_root / "manifest.jsonl"
            if not manifest_path.is_file():
                continue
            for manifest_row in jsonl_rows(manifest_path):
                if set(manifest_row) != ARCHIVE_MANIFEST_FIELDS:
                    raise ValueError(
                        f"isolation archive manifest fields differ: "
                        f"{sorted(set(manifest_row) ^ ARCHIVE_MANIFEST_FIELDS)}"
                    )
                if (
                    manifest_row["original_relpath"] != original_relpath
                    or manifest_row["sha256"] != expected_sha256
                ):
                    continue
                archived_path = contained_path(
                    archive_root, str(manifest_row["archive_relpath"])
                )
                if (
                    not archived_path.is_file()
                    or archived_path.stat().st_size != manifest_row["bytes"]
                    or sha256_file(archived_path) != expected_sha256
                ):
                    raise ValueError(
                        f"isolation archive artifact drift: {original_relpath}"
                    )
                matches.append(archived_path)
    if len(matches) != 1:
        raise ValueError(
            f"expected exactly one exact artifact for {relpath}, found {len(matches)}"
        )
    return matches[0], "archive"


def repo_relpath(path: Path) -> str:
    return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()


def normalize_riemann_relpath(value: str | None) -> str | None:
    if not value:
        return None
    path = Path(value)
    if path.is_absolute():
        try:
            return repo_relpath(path)
        except ValueError:
            return None
    text = path.as_posix()
    if text.startswith("full_corpus_v2/"):
        return f"experiments/riemann_corpus/{text}"
    if text.startswith(("analyses/", "depth/", "prompts/", "execution/")):
        return f"experiments/riemann_corpus/full_corpus_v2/{text}"
    if text.startswith("experiments/"):
        return text
    return None


def resolve_hash_bound_path(
    declared_path: str | None, expected_sha256: str | None
) -> str | None:
    """Resolve a declared repository file, including a preserved renamed copy."""

    relpath = normalize_riemann_relpath(declared_path)
    if relpath:
        candidate = REPO_ROOT / relpath
        if candidate.is_file() and (
            expected_sha256 is None or sha256_file(candidate) == expected_sha256
        ):
            return relpath
        if candidate.parent.is_dir() and expected_sha256:
            for sibling in sorted(candidate.parent.iterdir()):
                if sibling.is_file() and sha256_file(sibling) == expected_sha256:
                    return repo_relpath(sibling)
    return relpath


def _safe_meta_value(value: Any) -> str | None:
    return value if isinstance(value, str) else None


def load_sessions(session_roots: Sequence[Path]) -> list[Session]:
    sessions: list[Session] = []
    rollout_paths: list[Path] = []
    for root in session_roots:
        if root.is_dir():
            rollout_paths.extend(root.rglob("*.jsonl"))

    for path in sorted(set(rollout_paths)):
        session: Session | None = None
        turn_contexts: dict[str, dict[str, Any]] = {}
        first_turn_context: dict[str, Any] = {}
        envelopes: list[Envelope] = []
        calls: list[ToolCall] = []
        try:
            handle = path.open(encoding="utf-8", errors="replace")
        except OSError:
            continue
        with handle:
            for index, line in enumerate(handle):
                try:
                    event = json.loads(line)
                except json.JSONDecodeError:
                    continue
                event_type = event.get("type")
                payload = event.get("payload")
                if not isinstance(payload, dict):
                    continue
                if event_type == "session_meta" and session is None:
                    thread_id = _safe_meta_value(payload.get("id"))
                    if not thread_id or not UUID_RE.fullmatch(thread_id):
                        break
                    session = Session(
                        thread_id=thread_id,
                        parent_thread_id=_safe_meta_value(
                            payload.get("parent_thread_id")
                        ),
                        agent_task_path=_safe_meta_value(payload.get("agent_path")),
                        timestamp=_safe_meta_value(payload.get("timestamp")),
                        cli_version=_safe_meta_value(payload.get("cli_version")),
                        originator=_safe_meta_value(payload.get("originator")),
                        provider=_safe_meta_value(payload.get("model_provider")),
                        session_cwd=_safe_meta_value(payload.get("cwd")),
                        turn_contexts=turn_contexts,
                        first_turn_context=first_turn_context,
                        envelopes=envelopes,
                        calls=calls,
                    )
                    continue
                if session is None:
                    continue
                if event_type == "turn_context":
                    turn_id = _safe_meta_value(payload.get("turn_id"))
                    allowed_context = {
                        "model": _safe_meta_value(payload.get("model")),
                        "effort": _safe_meta_value(payload.get("effort")),
                        "comp_hash": _safe_meta_value(payload.get("comp_hash")),
                        "approval_policy": _safe_meta_value(
                            payload.get("approval_policy")
                        ),
                        "sandbox_type": _safe_meta_value(
                            (payload.get("sandbox_policy") or {}).get("type")
                            if isinstance(payload.get("sandbox_policy"), dict)
                            else None
                        ),
                        "cwd": _safe_meta_value(payload.get("cwd")),
                    }
                    if turn_id:
                        turn_contexts[turn_id] = allowed_context
                    if not first_turn_context:
                        first_turn_context.update(allowed_context)
                    continue
                inner_type = payload.get("type")
                metadata = payload.get("internal_chat_message_metadata_passthrough")
                turn_id = (
                    _safe_meta_value(metadata.get("turn_id"))
                    if isinstance(metadata, dict)
                    else None
                )
                if (
                    inner_type == "agent_message"
                    and payload.get("recipient") == session.agent_task_path
                ):
                    content = payload.get("content")
                    if not isinstance(content, list):
                        continue
                    encrypted = next(
                        (
                            item.get("encrypted_content")
                            for item in content
                            if isinstance(item, dict)
                            and item.get("type") == "encrypted_content"
                            and isinstance(item.get("encrypted_content"), str)
                        ),
                        None,
                    )
                    if encrypted:
                        envelopes.append(
                            Envelope(index, turn_id, sha256_bytes(encrypted.encode()))
                        )
                    continue
                if inner_type == "custom_tool_call":
                    input_text = payload.get("input")
                    if isinstance(input_text, str):
                        calls.append(
                            ToolCall(
                                index=index,
                                call_id=_safe_meta_value(payload.get("call_id")),
                                turn_id=turn_id,
                                timestamp=_safe_meta_value(event.get("timestamp")),
                                input_text=input_text,
                            )
                        )
        if session is not None:
            sessions.append(session)
    return sessions


def is_output_mutation(call: ToolCall, output_name: str) -> bool:
    text = call.input_text
    if output_name not in text:
        return False
    markers = (
        "*** Add File:",
        "*** Update File:",
        "*** Delete File:",
        "tools.apply_patch",
        "write_text",
        "write_bytes",
    )
    return any(marker in text for marker in markers)


def tool_workdir(call: ToolCall) -> str | None:
    patterns = (
        r'"workdir"\s*:\s*"([^"]+)"',
        r'workdir\s*:\s*"([^"]+)"',
    )
    for pattern in patterns:
        match = re.search(pattern, call.input_text)
        if match and match.group(1).startswith("/workspace/"):
            return match.group(1)
    if "/workspace/mathia-issue42/" in call.input_text:
        return "/workspace/mathia-issue42"
    return None


def writer_candidates(
    sessions: Sequence[Session],
    output_name: str,
    prefixes: Sequence[str] | None = None,
) -> list[tuple[Session, ToolCall]]:
    results: list[tuple[Session, ToolCall]] = []
    for session in sessions:
        if prefixes and not any(
            (session.agent_task_path or "").startswith(prefix) for prefix in prefixes
        ):
            continue
        mutations = [
            call for call in session.calls if is_output_mutation(call, output_name)
        ]
        if mutations:
            # Attribute creation to the first mutation.  Later turns commonly run
            # aggregate verification commands that enumerate many existing batch
            # names; treating those as writers collapses independently assigned
            # generation turns onto the verifier turn.
            results.append((session, mutations[0]))
    return results


def choose_writer(
    candidates: Sequence[tuple[Session, ToolCall]],
    claimed_path: str | None = None,
    excluded_paths: Iterable[str] = (),
) -> tuple[Session, ToolCall]:
    excluded = set(excluded_paths)
    eligible = [
        item for item in candidates if item[0].agent_task_path not in excluded
    ]
    claimed = [
        item for item in eligible if claimed_path and item[0].agent_task_path == claimed_path
    ]
    if claimed:
        return sorted(claimed, key=lambda item: item[0].timestamp or "")[-1]
    if not eligible:
        raise ValueError("no eligible output-writer context")
    return sorted(eligible, key=lambda item: item[0].timestamp or "")[-1]


def session_execution_fields(
    session: Session, call: ToolCall
) -> dict[str, Any]:
    context = session.context_for(call.turn_id)
    envelope = session.envelope_for(call)
    return {
        "agent_task_path": session.agent_task_path,
        "thread_id": session.thread_id,
        "turn_id": call.turn_id,
        "parent_thread_id": session.parent_thread_id,
        "timestamp": call.timestamp or session.timestamp,
        "cli_version": session.cli_version,
        "originator": session.originator,
        "provider": session.provider,
        "model_selector": context.get("model"),
        "service_checkpoint_id": None,
        "reasoning_effort": context.get("effort"),
        "comp_hash": context.get("comp_hash"),
        "sandbox_type": context.get("sandbox_type"),
        "approval_policy": context.get("approval_policy"),
        "session_cwd": session.session_cwd or context.get("cwd"),
        "tool_workdir": (
            tool_workdir(call) or context.get("cwd") or session.session_cwd
        ),
        "task_envelope_ciphertext_sha256": (
            envelope.ciphertext_sha256 if envelope else None
        ),
    }


def ledger_id(kind: str, stage: str, assignment_relpath: str, thread_id: str | None) -> str:
    digest = sha256_bytes(
        f"{kind}\0{stage}\0{assignment_relpath}\0{thread_id or 'missing'}".encode()
    )[:20]
    return f"{kind}_{digest}"


def base_execution_row() -> dict[str, Any]:
    return {field: None for field in sorted(EXECUTION_FIELDS)}


def _audit_assignment_rows(
    sessions: Sequence[Session],
    *,
    stage: str,
    assignment_dir: Path,
    output_dir: Path,
    prefixes: Sequence[str],
    excluded_paths: Sequence[str],
) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    rows: list[dict[str, Any]] = []
    by_output_name: dict[str, dict[str, Any]] = {}
    for assignment_path in sorted(assignment_dir.glob("*.json")):
        assignment = json.loads(assignment_path.read_text(encoding="utf-8"))
        output_path = output_dir / f"{assignment_path.stem}.jsonl"
        candidates = writer_candidates(sessions, output_path.name, prefixes)
        session, call = choose_writer(candidates, excluded_paths=excluded_paths)
        assignment_relpath = repo_relpath(assignment_path)
        assignment_sha = sha256_file(assignment_path)
        output_relpath = repo_relpath(output_path)
        output_sha = sha256_file(output_path)
        prompt_sha = assignment.get("prompt_sha256")
        brief_sha = assignment.get("execution_brief_sha256")
        row = base_execution_row()
        row.update(
            {
                "schema_version": SCHEMA_VERSION,
                "ledger_kind": "riemann-audit-execution",
                "release_id": "riemann-mathia-full-v2",
                "stage": stage,
                "status": "authoritative",
                "requires_rerun": False,
                "rerun_reason": None,
                "assignment_relpath": assignment_relpath,
                "assignment_sha256": assignment_sha,
                "prompt_relpath": resolve_hash_bound_path(
                    assignment.get("prompt_path"), prompt_sha
                ),
                "prompt_sha256": prompt_sha,
                "prompt_recovery_status": "verified-file",
                "execution_brief_relpath": resolve_hash_bound_path(
                    assignment.get("execution_brief_path"), brief_sha
                ),
                "execution_brief_sha256": brief_sha,
                "client": "codex-collaboration-agent",
                "output_relpath": output_relpath,
                "output_sha256": output_sha,
                "output_records": count_jsonl(output_path),
                "recovery_quality": "session-and-hashes-exact",
                "source_provenance_relpath": None,
                "superseded_by_thread_id": None,
            }
        )
        row.update(session_execution_fields(session, call))
        row["ledger_id"] = ledger_id(
            "riemann_audit", stage, assignment_relpath, session.thread_id
        )
        rows.append(row)
        by_output_name[output_path.name] = row
    return rows, by_output_name


SUPERSEDED_AUDIT_PATHS = {
    "/root/audit_lane2_002": "/root/audit_lane2_002_retry",
    "/root/audit_024": "/root/audit_024_retry",
    "/root/riemann_audit_computation_p2": (
        "/root/riemann_audit_computation_p2_retry"
    ),
}


def build_riemann_audit_ledger(
    sessions: Sequence[Session],
) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    predecessor_rows, predecessor_map = _audit_assignment_rows(
        sessions,
        stage="predecessor-audit",
        assignment_dir=RIEMANN_ROOT / "audit_pre_openalex_handoffs" / "assignments",
        output_dir=RIEMANN_ROOT / "audit_pre_openalex_handoffs" / "batches",
        prefixes=("/root/audit",),
        excluded_paths=tuple(SUPERSEDED_AUDIT_PATHS),
    )
    active_rows, active_map = _audit_assignment_rows(
        sessions,
        stage="active-fresh-audit",
        assignment_dir=RIEMANN_ROOT / "audit" / "assignments",
        output_dir=RIEMANN_ROOT / "audit" / "batches",
        prefixes=("/root/riemann_audit",),
        excluded_paths=tuple(SUPERSEDED_AUDIT_PATHS),
    )
    rows = predecessor_rows + active_rows
    authoritative_by_task = {
        row["agent_task_path"]: row for row in rows if row["agent_task_path"]
    }
    sessions_by_path = {
        session.agent_task_path: session
        for session in sessions
        if session.agent_task_path in SUPERSEDED_AUDIT_PATHS
    }
    for bad_path, retry_path in SUPERSEDED_AUDIT_PATHS.items():
        bad_session = sessions_by_path[bad_path]
        authoritative = authoritative_by_task[retry_path]
        calls = bad_session.calls
        call = calls[-1] if calls else ToolCall(0, None, None, None, "")
        row = dict(authoritative)
        row.update(session_execution_fields(bad_session, call))
        row.update(
            {
                "ledger_id": ledger_id(
                    "riemann_audit_superseded",
                    authoritative["stage"],
                    authoritative["assignment_relpath"],
                    bad_session.thread_id,
                ),
                "status": "superseded",
                "requires_rerun": False,
                "rerun_reason": "superseded-attempt",
                "output_sha256": None,
                "output_records": None,
                "recovery_quality": "superseded-attempt-metadata",
                "superseded_by_thread_id": authoritative["thread_id"],
            }
        )
        rows.append(row)
    output_map = {**predecessor_map, **active_map}
    return sorted(rows, key=lambda row: row["ledger_id"]), output_map


def build_riemann_decision_map(
    audit_rows: Sequence[dict[str, Any]],
) -> list[dict[str, Any]]:
    authoritative = {
        Path(row["output_relpath"]).name: row
        for row in audit_rows
        if row["status"] == "authoritative"
    }
    predecessor_by_id: dict[str, tuple[dict[str, Any], dict[str, Any]]] = {}
    for batch_path in sorted(
        (RIEMANN_ROOT / "audit_pre_openalex_handoffs" / "batches").glob("*.jsonl")
    ):
        execution = authoritative[batch_path.name]
        for decision in jsonl_rows(batch_path):
            predecessor_by_id[decision["object_id"]] = (decision, execution)

    fresh_by_id: dict[str, tuple[dict[str, Any], dict[str, Any]]] = {}
    for batch_path in sorted((RIEMANN_ROOT / "audit" / "batches").glob("*.jsonl")):
        execution = authoritative[batch_path.name]
        for decision in jsonl_rows(batch_path):
            fresh_by_id[decision["object_id"]] = (decision, execution)

    rows: list[dict[str, Any]] = []

    def append_row(
        decision: Mapping[str, Any], execution: Mapping[str, Any], state: str
    ) -> None:
        rows.append(
            {
                "schema_version": SCHEMA_VERSION,
                "ledger_kind": "riemann-audit-decision-map",
                "release_id": "riemann-mathia-full-v2",
                "object_id": decision["object_id"],
                "state": state,
                "execution_ledger_id": execution["ledger_id"],
                "assignment_sha256": execution["assignment_sha256"],
                "output_sha256": execution["output_sha256"],
                "decision_canonical_sha256": canonical_sha256(decision),
            }
        )

    for object_id in sorted(predecessor_by_id):
        decision, execution = predecessor_by_id[object_id]
        append_row(decision, execution, "predecessor")

    carried_ids = {
        row["object_id"]
        for row in jsonl_rows(RIEMANN_ROOT / "audit" / "carried_pre_openalex.jsonl")
    }
    for decision in jsonl_rows(RIEMANN_ROOT / "audit" / "independent_review.jsonl"):
        object_id = decision["object_id"]
        if object_id in carried_ids:
            predecessor, execution = predecessor_by_id[object_id]
            if predecessor != decision:
                raise ValueError(f"carried decision changed semantically: {object_id}")
            append_row(decision, execution, "active-carried")
        else:
            fresh, execution = fresh_by_id[object_id]
            if fresh != decision:
                raise ValueError(f"fresh decision changed semantically: {object_id}")
            append_row(decision, execution, "active-fresh")
    return rows


def _assignment_source_count(assignment_path: Path) -> int:
    assignment = json.loads(assignment_path.read_text(encoding="utf-8"))
    if isinstance(assignment.get("source_id"), str):
        return 1
    units = assignment.get("units")
    if isinstance(units, list):
        return len(
            {
                item.get("source_id")
                for item in units
                if isinstance(item, dict) and isinstance(item.get("source_id"), str)
            }
        )
    sources = assignment.get("sources")
    if isinstance(sources, list):
        return len(sources)
    return 0


def _legacy_path(value: str) -> Path:
    relpath = normalize_riemann_relpath(value)
    if not relpath:
        raise ValueError(f"unresolved legacy path: {value}")
    return REPO_ROOT / relpath


def _legacy_session_row(
    provenance: Mapping[str, Any],
    assignment_path: Path,
    output_path: Path,
    session: Session | None,
    call: ToolCall | None,
    *,
    mixed: bool,
    source_provenance_relpath: str,
) -> dict[str, Any]:
    stage = str(provenance["stage"])
    assignment_relpath = repo_relpath(assignment_path)
    row = base_execution_row()
    row.update(
        {
            "schema_version": SCHEMA_VERSION,
            "ledger_kind": "riemann-legacy-context-recovery",
            "release_id": "riemann-mathia-full-v2",
            "stage": stage,
            "status": "isolation-invalid" if mixed else "historical-recovered",
            "requires_rerun": mixed,
            "rerun_reason": "multi-source-context" if mixed else None,
            "assignment_relpath": assignment_relpath,
            "assignment_sha256": sha256_file(assignment_path),
            "prompt_relpath": resolve_hash_bound_path(
                provenance.get("prompt_path") or provenance.get("prompt_relpath"),
                provenance.get("prompt_sha256"),
            ),
            "prompt_sha256": provenance.get("prompt_sha256"),
            "prompt_recovery_status": "verified-file",
            "execution_brief_relpath": None,
            "execution_brief_sha256": None,
            "client": provenance.get("client"),
            "provider": provenance.get("provider") or "openai",
            "model_selector": provenance.get("model"),
            "service_checkpoint_id": None,
            "reasoning_effort": provenance.get("reasoning_effort"),
            "output_relpath": repo_relpath(output_path),
            "output_sha256": sha256_file(output_path),
            "output_records": count_jsonl(output_path),
            "source_provenance_relpath": source_provenance_relpath,
            "superseded_by_thread_id": None,
        }
    )
    if session is not None and call is not None:
        row.update(session_execution_fields(session, call))
        row["recovery_quality"] = "session-and-hashes-exact"
    else:
        execution_context = provenance.get("execution_context")
        exact_uuid = (
            execution_context
            if isinstance(execution_context, str)
            and UUID_RE.fullmatch(execution_context)
            else None
        )
        client = str(provenance.get("client") or "")
        cli_match = re.search(r"(\d+\.\d+\.\d+)", client)
        row.update(
            {
                "agent_task_path": provenance.get("agent_task_path"),
                "thread_id": exact_uuid,
                "turn_id": None,
                "parent_thread_id": None,
                "timestamp": None,
                "cli_version": cli_match.group(1) if cli_match else None,
                "originator": "codex-exec" if exact_uuid else None,
                "comp_hash": None,
                "sandbox_type": (
                    "workspace-write"
                    if "workspace-write" in str(provenance.get("invocation_mode"))
                    else None
                ),
                "approval_policy": None,
                "session_cwd": provenance.get("working_directory"),
                "tool_workdir": provenance.get("working_directory"),
                "task_envelope_ciphertext_sha256": None,
                "recovery_quality": (
                    "external-event-log-and-hashes-exact"
                    if exact_uuid
                    else "path-and-hashes-only"
                ),
            }
        )
    row["ledger_id"] = ledger_id(
        "riemann_legacy", stage, assignment_relpath, row["thread_id"]
    )
    return row


def build_legacy_context_ledger(
    sessions: Sequence[Session],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    depth_provenance_path = RIEMANN_ROOT / "depth" / "generation_provenance.jsonl"
    for provenance in jsonl_rows(depth_provenance_path):
        assignment_path = _legacy_path(provenance["assignment_path"])
        output_path = _legacy_path(provenance["output_path"])
        claimed_path = provenance.get("agent_task_path")
        candidates = writer_candidates(sessions, output_path.name, ("/root/depth",))
        selected: tuple[Session, ToolCall] | None = None
        if candidates:
            try:
                selected = choose_writer(candidates, claimed_path=claimed_path)
            except ValueError:
                selected = None
        mixed = (
            provenance.get("stage") == "whole-source-depth"
            and len(provenance.get("assigned_source_ids") or []) > 1
        )
        rows.append(
            _legacy_session_row(
                provenance,
                assignment_path,
                output_path,
                selected[0] if selected else None,
                selected[1] if selected else None,
                mixed=mixed,
                source_provenance_relpath=repo_relpath(depth_provenance_path),
            )
        )

    analysis_provenance_path = RIEMANN_ROOT / "analyses" / "generation_provenance.jsonl"
    for provenance in jsonl_rows(analysis_provenance_path):
        assignment_path = RIEMANN_ROOT / provenance["assignment_relpath"]
        output_path = RIEMANN_ROOT / provenance["raw_output_relpath"]
        candidates = writer_candidates(sessions, output_path.name)
        selected = choose_writer(
            candidates, claimed_path=provenance.get("agent_task_path")
        )
        mixed = _assignment_source_count(assignment_path) > 1
        normalized = dict(provenance)
        normalized["prompt_path"] = provenance.get("prompt_relpath")
        rows.append(
            _legacy_session_row(
                normalized,
                assignment_path,
                output_path,
                selected[0],
                selected[1],
                mixed=mixed,
                source_provenance_relpath=repo_relpath(analysis_provenance_path),
            )
        )
    return sorted(rows, key=lambda row: row["ledger_id"])


AGNOSTIC_STAGES = (
    (
        "generation",
        AGNOSTIC_ROOT / "analysis" / "generation",
        ("/root/handoff_ingest_design", "/root/riemann_critic_w2055983684"),
    ),
    (
        "critic",
        AGNOSTIC_ROOT / "analysis" / "critic",
        ("/root/agnostic_critic_",),
    ),
    (
        "revision",
        AGNOSTIC_ROOT / "analysis" / "revision",
        ("/root/agnostic_revision_",),
    ),
    ("audit", AGNOSTIC_ROOT / "audit", ("/root/agnostic_audit_",)),
)


def build_agnostic_execution_ledger(
    sessions: Sequence[Session],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for stage, stage_root, prefixes in AGNOSTIC_STAGES:
        for assignment_path in sorted((stage_root / "assignments").glob("*.json")):
            assignment = json.loads(assignment_path.read_text(encoding="utf-8"))
            output_path = stage_root / "batches" / f"{assignment_path.stem}.jsonl"
            session, call = choose_writer(
                writer_candidates(sessions, output_path.name, prefixes)
            )
            assignment_relpath = repo_relpath(assignment_path)
            invalid = stage == "generation"
            row = base_execution_row()
            row.update(
                {
                    "schema_version": SCHEMA_VERSION,
                    "ledger_kind": "agnostic-execution",
                    "release_id": "agnostic-mathia-openalex-supplement-v1",
                    "stage": stage,
                    "status": "isolation-invalid" if invalid else "authoritative",
                    "requires_rerun": invalid,
                    "rerun_reason": "reused-multi-source-context" if invalid else None,
                    "assignment_relpath": assignment_relpath,
                    "assignment_sha256": sha256_file(assignment_path),
                    "prompt_relpath": None,
                    "prompt_sha256": None,
                    "prompt_recovery_status": "encrypted-local-only",
                    "execution_brief_relpath": None,
                    "execution_brief_sha256": None,
                    "client": "codex-collaboration-agent",
                    "output_relpath": repo_relpath(output_path),
                    "output_sha256": sha256_file(output_path),
                    "output_records": count_jsonl(output_path),
                    "recovery_quality": "session-and-hashes-except-plaintext-prompt",
                    "source_provenance_relpath": None,
                    "superseded_by_thread_id": None,
                }
            )
            row.update(session_execution_fields(session, call))
            row["ledger_id"] = ledger_id(
                "agnostic", stage, assignment_relpath, session.thread_id
            )
            rows.append(row)
    return sorted(rows, key=lambda row: row["ledger_id"])


def _assert_sha(value: Any, field: str, allow_null: bool = False) -> None:
    if value is None and allow_null:
        return
    if not isinstance(value, str) or not SHA256_RE.fullmatch(value):
        raise ValueError(f"invalid SHA-256 in {field}: {value!r}")


def validate_execution_rows(rows: Sequence[Mapping[str, Any]]) -> None:
    seen: set[str] = set()
    for row in rows:
        if set(row) != EXECUTION_FIELDS:
            raise ValueError(
                f"execution ledger fields differ: {sorted(set(row) ^ EXECUTION_FIELDS)}"
            )
        ledger = row["ledger_id"]
        if not isinstance(ledger, str) or ledger in seen:
            raise ValueError(f"duplicate or invalid ledger_id: {ledger!r}")
        seen.add(ledger)
        _assert_sha(row["assignment_sha256"], "assignment_sha256")
        _assert_sha(row["prompt_sha256"], "prompt_sha256", allow_null=True)
        _assert_sha(
            row["execution_brief_sha256"],
            "execution_brief_sha256",
            allow_null=True,
        )
        _assert_sha(row["output_sha256"], "output_sha256", allow_null=True)
        _assert_sha(
            row["task_envelope_ciphertext_sha256"],
            "task_envelope_ciphertext_sha256",
            allow_null=True,
        )
        if row["service_checkpoint_id"] is not None:
            raise ValueError("service_checkpoint_id must remain transparently null")
        if row["prompt_recovery_status"] == "encrypted-local-only" and (
            row["prompt_relpath"] is not None or row["prompt_sha256"] is not None
        ):
            raise ValueError("encrypted-local-only prompt cannot claim plaintext binding")
    reject_sensitive_content(rows)


def validate_decision_rows(rows: Sequence[Mapping[str, Any]]) -> None:
    for row in rows:
        if set(row) != DECISION_FIELDS:
            raise ValueError(
                f"decision map fields differ: {sorted(set(row) ^ DECISION_FIELDS)}"
            )
        _assert_sha(row["assignment_sha256"], "assignment_sha256")
        _assert_sha(row["output_sha256"], "output_sha256")
        _assert_sha(row["decision_canonical_sha256"], "decision_canonical_sha256")
    reject_sensitive_content(rows)


def reject_sensitive_content(rows: Sequence[Mapping[str, Any]]) -> None:
    serialized = "\n".join(
        json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        for row in rows
    ).lower()
    for pattern in SENSITIVE_PATTERNS:
        if pattern.lower() in serialized:
            raise ValueError(f"sensitive pattern rejected: {pattern}")


def validate_artifact_bindings(
    rows: Sequence[Mapping[str, Any]],
    *,
    repo_root: Path = REPO_ROOT,
    archive_roots: Sequence[Path] | None = None,
) -> Counter[str]:
    """Verify every claimed digest against its live or archived exact bytes."""

    locations: Counter[str] = Counter()
    bindings = (
        ("assignment_relpath", "assignment_sha256"),
        ("prompt_relpath", "prompt_sha256"),
        ("execution_brief_relpath", "execution_brief_sha256"),
        ("output_relpath", "output_sha256"),
    )
    for row in rows:
        for path_field, hash_field in bindings:
            digest = row[hash_field]
            if digest is None:
                continue
            artifact_path, location = resolve_ledger_artifact(
                row[path_field],
                digest,
                repo_root=repo_root,
                archive_roots=archive_roots,
            )
            if sha256_file(artifact_path) != digest:
                raise ValueError(f"artifact hash drift: {row[path_field]}")
            locations[location] += 1
    return locations


def validate_coverage(
    audit_rows: Sequence[Mapping[str, Any]],
    decision_rows: Sequence[Mapping[str, Any]],
    legacy_rows: Sequence[Mapping[str, Any]],
    agnostic_rows: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    audit_fresh = [
        row
        for row in audit_rows
        if row["stage"] == "active-fresh-audit"
        and row["status"] == "authoritative"
        and row["requires_rerun"] is False
    ]
    audit_states = Counter(
        (row["stage"], row["status"], row["requires_rerun"])
        for row in audit_rows
        if row not in audit_fresh
    )
    if audit_states != Counter(
        {
            ("predecessor-audit", "authoritative", False): 165,
            ("predecessor-audit", "superseded", False): 2,
            ("active-fresh-audit", "reconciliation-pending", True): 32,
        }
    ):
        raise ValueError(f"unexpected Riemann audit states: {audit_states}")

    decisions = Counter(row["state"] for row in decision_rows)
    if decisions != Counter({"predecessor": 860, "reconciliation-pending": 1004}):
        raise ValueError(f"unexpected decision coverage: {decisions}")

    legacy_fresh = [
        row
        for row in legacy_rows
        if row["status"] == "authoritative" and row["requires_rerun"] is False
    ]
    legacy_stages = Counter(
        row["stage"] for row in legacy_rows if row not in legacy_fresh
    )
    if legacy_stages != Counter(
        {
            "whole-source-depth": 55,
            "missing-source-depth-repair": 3,
            "pass12": 59,
            "pass3": 61,
            "pass4": 112,
        }
    ):
        raise ValueError(f"unexpected legacy stage coverage: {legacy_stages}")
    legacy_invalid = Counter(row["stage"] for row in legacy_rows if row["requires_rerun"])
    if legacy_invalid != Counter(
        {
            "whole-source-depth": 37,
            "missing-source-depth-repair": 3,
            "pass12": 56,
            "pass3": 58,
            "pass4": 109,
        }
    ):
        raise ValueError(f"unexpected legacy rerun coverage: {legacy_invalid}")
    legacy_status = Counter(row["status"] for row in legacy_rows if row not in legacy_fresh)
    if legacy_status != Counter(
        {
            "historical-recovered": 27,
            "isolation-invalid": 179,
            "reconciliation-pending": 84,
        }
    ):
        raise ValueError(f"unexpected legacy status coverage: {legacy_status}")
    legacy_quality = Counter(row["recovery_quality"] for row in legacy_rows)
    if legacy_quality["path-and-hashes-only"] != 16:
        raise ValueError(f"unexpected partial legacy contexts: {legacy_quality}")

    agnostic_fresh = [
        row
        for row in agnostic_rows
        if row["status"] == "authoritative" and row["requires_rerun"] is False
    ]
    agnostic_stages = Counter(
        row["stage"] for row in agnostic_rows if row not in agnostic_fresh
    )
    if agnostic_stages != Counter(
        {"generation": 27, "critic": 27, "revision": 22, "audit": 26}
    ):
        raise ValueError(f"unexpected agnostic stage coverage: {agnostic_stages}")
    agnostic_invalid = [row for row in agnostic_rows if row["requires_rerun"]]
    agnostic_status = Counter(
        row["status"] for row in agnostic_rows if row not in agnostic_fresh
    )
    if len(agnostic_invalid) != 102 or agnostic_status != Counter(
        {"isolation-invalid": 27, "reconciliation-pending": 75}
    ):
        raise ValueError(
            f"unexpected agnostic post-isolation coverage: {agnostic_status}"
        )
    generation_threads = {
        row["thread_id"]
        for row in agnostic_rows
        if row["stage"] == "generation" and row["status"] == "isolation-invalid"
    }
    generation_turns = {
        row["turn_id"]
        for row in agnostic_rows
        if row["stage"] == "generation" and row["status"] == "isolation-invalid"
    }
    if len(generation_threads) != 2 or len(generation_turns) != 27:
        raise ValueError(
            "agnostic generation must expose 27 turns in exactly two reused threads"
        )
    return {
        "riemann_audit_rows": len(audit_rows),
        "riemann_audit_requires_rerun": sum(
            bool(row["requires_rerun"]) for row in audit_rows
        ),
        "riemann_fresh_authoritative_rows": len(audit_fresh),
        "riemann_decision_rows": len(decision_rows),
        "riemann_decisions_reconciliation_pending": decisions[
            "reconciliation-pending"
        ],
        "legacy_context_rows": len(legacy_rows),
        "legacy_requires_rerun": sum(
            bool(row["requires_rerun"]) for row in legacy_rows
        ),
        "legacy_fresh_authoritative_rows": len(legacy_fresh),
        "agnostic_rows": len(agnostic_rows),
        "agnostic_requires_rerun": len(agnostic_invalid),
        "agnostic_fresh_authoritative_rows": len(agnostic_fresh),
    }


def write_jsonl(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = "".join(
        json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        + "\n"
        for row in rows
    )
    path.write_text(payload, encoding="utf-8")


def resolve_declared_live_artifact(
    declared: str,
    *,
    assignment_path: Path,
    repo_root: Path = REPO_ROOT,
) -> Path:
    """Resolve one declared live path without searching by basename."""

    repo_root = repo_root.resolve()
    raw = Path(declared)
    candidates = [raw] if raw.is_absolute() else [
        repo_root / raw,
        assignment_path.parent / raw,
    ]
    resolved: list[Path] = []
    for candidate in candidates:
        candidate = candidate.resolve()
        try:
            candidate.relative_to(repo_root)
        except ValueError:
            continue
        if candidate.is_file() and candidate not in resolved:
            resolved.append(candidate)
    if len(resolved) != 1:
        raise ValueError(
            f"expected one live declared artifact for {declared!r}, found {len(resolved)}"
        )
    return resolved[0]


def assignment_artifact_binding(
    assignment: Mapping[str, Any],
    assignment_path: Path,
    *,
    path_fields: Sequence[str],
    hash_fields: Sequence[str],
    repo_root: Path = REPO_ROOT,
) -> tuple[str | None, str | None]:
    """Return an exact optional prompt/brief binding without reading its body."""

    declared_values = {
        str(assignment[field])
        for field in path_fields
        if isinstance(assignment.get(field), str) and assignment.get(field)
    }
    declared_hashes = {
        str(assignment[field])
        for field in hash_fields
        if isinstance(assignment.get(field), str) and assignment.get(field)
    }
    if not declared_values:
        if declared_hashes:
            raise ValueError("artifact hash is declared without its path")
        return None, None
    if len(declared_values) != 1 or len(declared_hashes) > 1:
        raise ValueError("assignment contains ambiguous artifact bindings")
    artifact_path = resolve_declared_live_artifact(
        next(iter(declared_values)),
        assignment_path=assignment_path,
        repo_root=repo_root,
    )
    digest = sha256_file(artifact_path)
    if declared_hashes and declared_hashes != {digest}:
        raise ValueError("assignment artifact hash mismatch")
    return artifact_path.relative_to(repo_root.resolve()).as_posix(), digest


def recover_authoritative_execution_row(
    assignment_path: Path,
    ledger_path: Path,
    *,
    expected_stage: str,
    release_id: str,
    agent_task_path: str,
    session_roots: Sequence[Path],
    repo_root: Path = REPO_ROOT,
) -> dict[str, Any]:
    """Recover one exact local write context and construct a safe ledger row."""

    repo_root = repo_root.resolve()
    assignment_path = assignment_path.resolve()
    ledger_path = ledger_path.resolve()
    for label, path in (("assignment", assignment_path), ("ledger", ledger_path)):
        try:
            path.relative_to(repo_root)
        except ValueError as error:
            raise ValueError(f"{label} path must remain inside the repository") from error
    if not assignment_path.is_file() or not ledger_path.is_file():
        raise ValueError("live assignment and target execution ledger are required")
    assignment = json.loads(assignment_path.read_text(encoding="utf-8"))
    if not isinstance(assignment, dict):
        raise ValueError("assignment must contain one JSON object")
    if assignment.get("stage") != expected_stage:
        raise ValueError(
            f"assignment stage mismatch: expected {expected_stage!r}, "
            f"found {assignment.get('stage')!r}"
        )
    if not agent_task_path.startswith("/root/"):
        raise ValueError("an exact /root agent task path is required")

    prior_rows = jsonl_rows(ledger_path)
    validate_execution_rows(prior_rows)
    ledger_kinds = {row["ledger_kind"] for row in prior_rows}
    release_ids = {row["release_id"] for row in prior_rows}
    if len(ledger_kinds) != 1 or release_ids != {release_id}:
        raise ValueError("target ledger kind or release_id mismatch")
    declared_output = assignment.get("output_path")
    if not isinstance(declared_output, str) or not declared_output:
        raise ValueError("assignment must declare one output_path")
    output_path = resolve_declared_live_artifact(
        declared_output,
        assignment_path=assignment_path,
        repo_root=repo_root,
    )
    output_relpath = output_path.relative_to(repo_root).as_posix()

    matching_writes: list[tuple[Session, ToolCall]] = []
    for session in load_sessions(session_roots):
        if session.agent_task_path != agent_task_path:
            continue
        for call in session.calls:
            if not is_output_mutation(call, output_path.name):
                continue
            declared_forms = {
                str(output_path),
                output_relpath,
                declared_output,
            }
            workdir = tool_workdir(call)
            if workdir:
                try:
                    declared_forms.add(output_path.relative_to(workdir).as_posix())
                except ValueError:
                    pass
            if any(form and form in call.input_text for form in declared_forms):
                matching_writes.append((session, call))
    if len(matching_writes) != 1:
        raise ValueError(
            f"expected one local session/tool write for {agent_task_path}, "
            f"found {len(matching_writes)}"
        )
    session, call = matching_writes[0]

    prompt_relpath, prompt_sha256 = assignment_artifact_binding(
        assignment,
        assignment_path,
        path_fields=("prompt_path", "prompt_relpath"),
        hash_fields=("prompt_sha256",),
        repo_root=repo_root,
    )
    brief_relpath, brief_sha256 = assignment_artifact_binding(
        assignment,
        assignment_path,
        path_fields=("execution_brief_path", "execution_brief_relpath"),
        hash_fields=("execution_brief_sha256",),
        repo_root=repo_root,
    )
    assignment_relpath = assignment_path.relative_to(repo_root).as_posix()
    row = base_execution_row()
    row.update(
        {
            "schema_version": SCHEMA_VERSION,
            "ledger_kind": next(iter(ledger_kinds)),
            "release_id": release_id,
            "stage": expected_stage,
            "status": "authoritative",
            "requires_rerun": False,
            "rerun_reason": None,
            "assignment_relpath": assignment_relpath,
            "assignment_sha256": sha256_file(assignment_path),
            "prompt_relpath": prompt_relpath,
            "prompt_sha256": prompt_sha256,
            "prompt_recovery_status": (
                "verified-file" if prompt_sha256 else "encrypted-local-only"
            ),
            "execution_brief_relpath": brief_relpath,
            "execution_brief_sha256": brief_sha256,
            "client": "codex-collaboration-agent",
            "output_relpath": output_relpath,
            "output_sha256": sha256_file(output_path),
            "output_records": count_jsonl(output_path),
            "recovery_quality": (
                "session-and-hashes-exact"
                if prompt_sha256
                else "session-and-hashes-except-plaintext-prompt"
            ),
            "source_provenance_relpath": None,
            "superseded_by_thread_id": None,
        }
    )
    row.update(session_execution_fields(session, call))
    if row["agent_task_path"] != agent_task_path:
        raise ValueError("recovered session task path mismatch")
    row["ledger_id"] = ledger_id(
        "authoritative_recovery",
        expected_stage,
        assignment_relpath,
        session.thread_id,
    )
    validate_fresh_authoritative_row(row, prior_rows, repo_root=repo_root)
    return row


def recover_and_append_authoritative_assignment(
    assignment_path: Path,
    ledger_path: Path,
    *,
    expected_stage: str,
    release_id: str,
    agent_task_path: str,
    session_roots: Sequence[Path],
    repo_root: Path = REPO_ROOT,
) -> dict[str, Any]:
    """Recover, validate, and append one exact authoritative receipt."""

    row = recover_authoritative_execution_row(
        assignment_path,
        ledger_path,
        expected_stage=expected_stage,
        release_id=release_id,
        agent_task_path=agent_task_path,
        session_roots=session_roots,
        repo_root=repo_root,
    )
    append_authoritative_execution_row(
        ledger_path, row, repo_root=repo_root
    )
    return row


def validate_fresh_authoritative_row(
    row: Mapping[str, Any],
    existing_rows: Sequence[Mapping[str, Any]],
    *,
    repo_root: Path = REPO_ROOT,
) -> None:
    """Validate one fresh, live, isolated context before ledger append."""

    validate_execution_rows([row])
    if (
        row["status"] != "authoritative"
        or row["requires_rerun"] is not False
        or row["rerun_reason"] is not None
    ):
        raise ValueError("fresh execution receipt must be authoritative")
    required_strings = (
        "ledger_id",
        "stage",
        "assignment_relpath",
        "agent_task_path",
        "thread_id",
        "turn_id",
        "parent_thread_id",
        "timestamp",
        "client",
        "cli_version",
        "originator",
        "provider",
        "model_selector",
        "reasoning_effort",
        "comp_hash",
        "sandbox_type",
        "approval_policy",
        "session_cwd",
        "tool_workdir",
        "task_envelope_ciphertext_sha256",
        "output_relpath",
    )
    missing = [
        field
        for field in required_strings
        if not isinstance(row[field], str) or not row[field]
    ]
    if missing:
        raise ValueError(f"fresh execution receipt fields are missing: {missing}")
    if not str(row["agent_task_path"]).startswith("/root/"):
        raise ValueError("fresh execution receipt requires an exact agent task path")
    for identifier in ("thread_id", "turn_id", "parent_thread_id"):
        if not UUID_RE.fullmatch(str(row[identifier])):
            raise ValueError(f"fresh execution receipt has invalid {identifier}")

    repo_root = repo_root.resolve()
    for path_field, hash_field in (
        ("assignment_relpath", "assignment_sha256"),
        ("output_relpath", "output_sha256"),
    ):
        artifact_path = contained_path(repo_root, row[path_field])
        if not artifact_path.is_file() or sha256_file(artifact_path) != row[hash_field]:
            raise ValueError(f"fresh live artifact binding mismatch: {row[path_field]}")
    if count_jsonl(contained_path(repo_root, row["output_relpath"])) != row[
        "output_records"
    ]:
        raise ValueError("fresh execution receipt output-record count mismatch")
    for path_field, hash_field in (
        ("prompt_relpath", "prompt_sha256"),
        ("execution_brief_relpath", "execution_brief_sha256"),
    ):
        if row[hash_field] is None:
            continue
        artifact_path = contained_path(repo_root, row[path_field])
        if not artifact_path.is_file() or sha256_file(artifact_path) != row[hash_field]:
            raise ValueError(f"fresh live artifact binding mismatch: {row[path_field]}")

    for prior in existing_rows:
        if prior["ledger_id"] == row["ledger_id"]:
            raise ValueError(f"duplicate ledger_id: {row['ledger_id']}")
        if prior.get("agent_task_path") == row["agent_task_path"]:
            raise ValueError("fresh agent task path was already used")
        if prior.get("thread_id") == row["thread_id"]:
            raise ValueError("fresh execution thread was already used")
        if (
            prior.get("assignment_relpath") == row["assignment_relpath"]
            and prior.get("assignment_sha256") == row["assignment_sha256"]
            and prior.get("requires_rerun") is False
            and prior.get("status") in {"authoritative", "historical-recovered"}
        ):
            raise ValueError("assignment already has an authoritative exact receipt")


def append_authoritative_execution_row(
    ledger_path: Path,
    row: Mapping[str, Any],
    *,
    repo_root: Path = REPO_ROOT,
) -> None:
    """Append one verified receipt without rewriting historical status evidence."""

    repo_root = repo_root.resolve()
    ledger_path = ledger_path.resolve()
    try:
        ledger_path.relative_to(repo_root)
    except ValueError as error:
        raise ValueError("execution ledger must remain inside the repository") from error
    existing_rows = jsonl_rows(ledger_path) if ledger_path.is_file() else []
    validate_execution_rows(existing_rows)
    validate_fresh_authoritative_row(row, existing_rows, repo_root=repo_root)
    write_jsonl(ledger_path, [*existing_rows, dict(row)])


def build_all(session_roots: Sequence[Path]) -> tuple[
    list[dict[str, Any]],
    list[dict[str, Any]],
    list[dict[str, Any]],
    list[dict[str, Any]],
]:
    sessions = load_sessions(session_roots)
    audit_rows, _ = build_riemann_audit_ledger(sessions)
    decision_rows = build_riemann_decision_map(audit_rows)
    legacy_rows = build_legacy_context_ledger(sessions)
    agnostic_rows = build_agnostic_execution_ledger(sessions)
    validate_execution_rows(audit_rows)
    validate_decision_rows(decision_rows)
    validate_execution_rows(legacy_rows)
    validate_execution_rows(agnostic_rows)
    validate_coverage(audit_rows, decision_rows, legacy_rows, agnostic_rows)
    return audit_rows, decision_rows, legacy_rows, agnostic_rows


def load_and_validate_existing() -> dict[str, Any]:
    audit_rows = jsonl_rows(RIEMANN_AUDIT_LEDGER)
    decision_rows = jsonl_rows(RIEMANN_DECISION_MAP)
    legacy_rows = jsonl_rows(LEGACY_CONTEXT_LEDGER)
    agnostic_rows = jsonl_rows(AGNOSTIC_EXECUTION_LEDGER)
    validate_execution_rows(audit_rows)
    validate_decision_rows(decision_rows)
    validate_execution_rows(legacy_rows)
    validate_execution_rows(agnostic_rows)
    artifact_locations = validate_artifact_bindings(
        [*audit_rows, *legacy_rows, *agnostic_rows]
    )
    summary = validate_coverage(
        audit_rows, decision_rows, legacy_rows, agnostic_rows
    )
    summary.update(
        {
            "archived_artifact_bindings": artifact_locations["archive"],
            "live_artifact_bindings": artifact_locations["live"],
        }
    )
    return summary


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--validate", action="store_true")
    mode.add_argument(
        "--append-authoritative-row",
        type=Path,
        metavar="ROW_JSON",
        help="Append one strict-allowlist row after verifying its live artifacts.",
    )
    mode.add_argument(
        "--recover-authoritative-assignment",
        type=Path,
        metavar="ASSIGNMENT_JSON",
        help="Recover and append the unique local write for one live assignment.",
    )
    parser.add_argument(
        "--ledger",
        type=Path,
        help="Repository-local execution ledger used with --append-authoritative-row.",
    )
    parser.add_argument("--expected-stage")
    parser.add_argument("--release-id")
    parser.add_argument("--agent-task-path")
    parser.add_argument(
        "--session-root",
        action="append",
        type=Path,
        default=[],
        help="Local rollout directory; may be repeated and is never written to a ledger.",
    )
    args = parser.parse_args(argv)
    if args.validate:
        summary = load_and_validate_existing()
    elif args.recover_authoritative_assignment:
        required = {
            "--ledger": args.ledger,
            "--expected-stage": args.expected_stage,
            "--release-id": args.release_id,
            "--agent-task-path": args.agent_task_path,
        }
        missing = [name for name, value in required.items() if not value]
        if missing:
            parser.error(
                "required with --recover-authoritative-assignment: "
                + ", ".join(missing)
            )
        ledger_path = args.ledger
        if not ledger_path.is_absolute():
            ledger_path = REPO_ROOT / ledger_path
        assignment_path = args.recover_authoritative_assignment
        if not assignment_path.is_absolute():
            assignment_path = REPO_ROOT / assignment_path
        roots = args.session_root or [
            Path("/root/.codex/sessions"),
            Path("/root/.codex/archived_sessions"),
        ]
        row = recover_and_append_authoritative_assignment(
            assignment_path,
            ledger_path,
            expected_stage=args.expected_stage,
            release_id=args.release_id,
            agent_task_path=args.agent_task_path,
            session_roots=roots,
        )
        summary = {
            "appended_ledger_id": row["ledger_id"],
            "output_records": row["output_records"],
            "output_sha256": row["output_sha256"],
            "thread_id": row["thread_id"],
            "turn_id": row["turn_id"],
        }
    elif args.append_authoritative_row:
        if args.ledger is None:
            parser.error("--ledger is required with --append-authoritative-row")
        row = json.loads(args.append_authoritative_row.read_text(encoding="utf-8"))
        if not isinstance(row, dict):
            parser.error("--append-authoritative-row must contain one JSON object")
        ledger_path = args.ledger
        if not ledger_path.is_absolute():
            ledger_path = REPO_ROOT / ledger_path
        append_authoritative_execution_row(ledger_path, row)
        summary = {
            "appended_ledger_id": row["ledger_id"],
            "ledger_relpath": ledger_path.resolve()
            .relative_to(REPO_ROOT.resolve())
            .as_posix(),
        }
    else:
        roots = args.session_root or [
            Path("/root/.codex/sessions"),
            Path("/root/.codex/archived_sessions"),
        ]
        audit, decisions, legacy, agnostic = build_all(roots)
        write_jsonl(RIEMANN_AUDIT_LEDGER, audit)
        write_jsonl(RIEMANN_DECISION_MAP, decisions)
        write_jsonl(LEGACY_CONTEXT_LEDGER, legacy)
        write_jsonl(AGNOSTIC_EXECUTION_LEDGER, agnostic)
        summary = validate_coverage(audit, decisions, legacy, agnostic)
    print(json.dumps(summary, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
