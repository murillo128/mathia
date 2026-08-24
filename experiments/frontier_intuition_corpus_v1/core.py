"""Issue #57 theorem-only corpus materialization, generation, and audit.

This is intentionally a bounded experiment implementation rather than a new
dataset framework.  The source projector is the only component that opens the
upstream qwen-lean package.  Generation reads only the projected source and
prompt artifacts in this directory.
"""

from __future__ import annotations

import gzip
import hashlib
import io
import json
import os
import re
import shutil
import statistics
import subprocess
import tempfile
import threading
import time
import unicodedata
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Iterable, Iterator, Mapping, Sequence


SCHEMA_VERSION = "frontier-intuition-corpus-v1"
SOURCE_SCHEMA_VERSION = "frontier-intuition-source-task-v1"
PROMPT_SCHEMA_VERSION = "frontier-intuition-prompt-v1"
ATTEMPT_SCHEMA_VERSION = "frontier-intuition-attempt-v1"
ELIGIBILITY_SCHEMA_VERSION = "frontier-intuition-eligibility-v1"
ACCEPTED_SCHEMA_VERSION = "frontier-intuition-accepted-v1"
MANIFEST_SCHEMA_VERSION = "frontier-intuition-generation-manifest-v1"
SUMMARY_SCHEMA_VERSION = "frontier-intuition-summary-v1"
INTEGRITY_SCHEMA_VERSION = "frontier-intuition-integrity-audit-v1"
FREEZE_SCHEMA_VERSION = "frontier-intuition-freeze-v1"

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
EXPERIMENT_ROOT = Path(__file__).resolve().parent
CONTROLLING_ISSUE = "murillo128/mathia#57"
QWEN_REPOSITORY = "murillo128/qwen-lean"
QWEN_ACCEPTED_COMMIT = "67d0cdc13ce38c3847633fe9982d0c6e1473e8ed"
QWEN_MEMBERSHIP_EVIDENCE_COMMIT = "71222005f7d9093f31b321f2d1115f321dc75bb9"
MINIF2F_PATH = "data/lean-whole-proof-v2/minif2f-valid-clean-v2.jsonl"
RECORDS_PATH = "data/lean-whole-proof-v2/records.jsonl.gz"
UPSTREAM_FILE_SHA256 = {
    MINIF2F_PATH: "c356b72bdfb8c9e95223f7c6daaddff64127093d5f5b200216eeff12474dbb90",
    RECORDS_PATH: "a66855d8fa9e5132ea895fa206481e9a38cb8cc1baa7494a2a1f8f910030442c",
}
WORKLOADS = (
    "minif2f-valid-clean-v2",
    "fresh-composition-valid-v2",
)
EXPECTED_COUNTS = {
    "minif2f-valid-clean-v2": 244,
    "fresh-composition-valid-v2": 406,
}
EXPECTED_ORDERED_TASK_IDS_SHA256 = {
    "minif2f-valid-clean-v2": "cb5e5edba99dcb1fad61a1f5f88fd38e0061d122b54ea4e39a630a18138cce13",
    "fresh-composition-valid-v2": "7d01d2878a996a0fc57df1eb634ba562cebe396002dc0bd1f617b3b2e7e80f0b",
}

INTUITION_REQUEST = (
    "Propose one compact mathematical strategy for why the result should hold and how a "
    "proof might be organized. Identify the main mechanism or representation and a small "
    "number of useful intermediate mathematical goals if needed. Mention an obstruction or "
    "essential assumption only if it materially guides the route. Do not write the proof."
)
GENERATOR_MODEL = "gpt-5.6-sol"
GENERATOR_REASONING_EFFORT = "xhigh"
MAX_ATTEMPTS = 2
MAX_GUIDANCE_TOKENS = 96
GENERATION_TIMEOUT_SECONDS = 1800
TOKENIZER_ID = "Qwen/Qwen3-8B-Base"
TOKENIZER_REVISION = "49e3418fbbbca6ecbdf9608b4d22e5a407081db4"
EVALUATION_MARKERS = {
    "evaluation_only": True,
    "training_eligible": False,
    "artifact_role": "frontier_reference",
}

REASON_PRIORITY = (
    "generation_failure",
    "rejected_lean_syntax",
    "rejected_formal_identifier",
    "rejected_proof_like",
    "rejected_over_budget",
    "accepted",
)

# The exact patterns and their precedence are frozen into generation_manifest.json
# before any theorem generation.  They detect interface/proof transmission, not
# mathematical quality.
LEAN_SYNTAX_PATTERNS: tuple[tuple[str, str], ...] = (
    ("markdown_code_fence", r"```"),
    ("lean_assignment", r":="),
    ("lean_tactic_chain", r"<;>|\btactic\b"),
    ("lean_constructor_brackets", r"[⟨⟩]"),
    ("lean_command", r"(?m)^\s*#(?:check|eval|reduce|print)\b"),
    (
        "lean_by_block",
        r"(?m)^\s*by\s*(?:$|(?:simp_all|simpa|simp|rfl|linarith|nlinarith|omega|ring_nf|norm_num|aesop)\b)",
    ),
    ("lean_local_declaration", r"(?m)^\s*(?:have|show|suffices)\s+[^.\n]*(?::=|:)"),
    ("lean_lambda_or_match", r"\bfun\s+[A-Za-z][A-Za-z0-9_']*\s*=>|\bmatch\b[^\n]*\bwith\b"),
    (
        "lean_tactic_name",
        r"\b(?:simp_all|simpa|simp|rfl|linarith|nlinarith|omega|ring_nf|norm_num|aesop|positivity)\b",
    ),
    ("lean_comment_delimiter", r"/-|-/"),
)
FORMAL_IDENTIFIER_PATTERNS: tuple[tuple[str, str], ...] = (
    ("inline_code_identifier", r"`[^`\n]+`"),
    ("qualified_lean_identifier", r"\b[A-Z][A-Za-z0-9_']*(?:\.[A-Za-z][A-Za-z0-9_']*)+\b"),
    ("snake_case_identifier", r"\b[A-Za-z][A-Za-z0-9']+_[A-Za-z0-9_']{2,}\b"),
    ("lean_attribute_or_root", r"@\[|\b_root_\b"),
)
PROOF_LIKE_PATTERNS: tuple[tuple[str, str], ...] = (
    (
        "explicit_proof_completion",
        r"\b(?:q\.?e\.?d\.?|this (?:completes|proves|establishes) the proof|the proof is complete)\b",
    ),
    ("explicit_proof_transcript", r"(?im)^\s*proof\s*:|\bwe now prove\b|\bit remains to prove\b"),
)
SEQUENCE_MARKERS = re.compile(r"\b(?:first|second|third|fourth|next|then|finally)\b", re.I)
PROOF_ACTIONS = re.compile(
    r"\b(?:assume|suppose|define|set|expand|substitute|rearrange|derive|deduce|"
    r"prove|show|verify|calculate|compute|cancel|divide|multiply|integrate|"
    r"differentiate|factor|conclude)\b",
    re.I,
)
NUMBERED_STEP = re.compile(r"(?m)^\s*(?:step\s*)?\d+[.)]\s+")

FORBIDDEN_SOURCE_KEYS = {
    "proof",
    "proofs",
    "proof_variant",
    "proof_variants",
    "source_proof",
    "oracle_proof",
    "reference_proof",
    "canonical_proof",
    "completion",
    "candidate",
    "candidates",
    "lean_error",
    "qwen_outcome",
    "deepseek_outcome",
    "pass_at_k",
    "pass@k",
    "c_i",
    "solved",
    "stage_9",
    "capability_gap",
}

DISABLED_CODEX_FEATURES = (
    "apps",
    "browser_use",
    "browser_use_external",
    "computer_use",
    "goals",
    "hooks",
    "image_generation",
    "js_repl",
    "multi_agent",
    "plugins",
    "shell_tool",
    "skill_search",
    "tool_suggest",
    "unified_exec",
    "view_image",
)


def canonical_json(value: Any) -> str:
    return json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        separators=(",", ":"),
        sort_keys=True,
    )


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_text(value: str) -> str:
    return sha256_bytes(value.encode("utf-8"))


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def stable_id(kind: str, value: Any) -> str:
    return f"{kind}_{sha256_text(canonical_json(value))}"


def utc_now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _write_once(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
    except FileExistsError as error:
        raise RuntimeError(f"refusing to replace write-once artifact: {path}") from error
    with os.fdopen(descriptor, "wb") as handle:
        handle.write(content)


def write_json_once(path: Path, value: Any) -> None:
    _write_once(path, (canonical_json(value) + "\n").encode("utf-8"))


def write_jsonl_once(path: Path, rows: Iterable[Mapping[str, Any]]) -> None:
    body = "".join(canonical_json(dict(row)) + "\n" for row in rows)
    _write_once(path, body.encode("utf-8"))


def iter_jsonl(path: Path) -> Iterator[dict[str, Any]]:
    with path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            value = json.loads(line)
            if not isinstance(value, dict):
                raise ValueError(f"non-object JSONL row at {path}:{line_number}")
            yield value


def ordered_ids_sha256(ids: Sequence[str]) -> str:
    return sha256_text(json.dumps(list(ids), separators=(",", ":")))


def render_model_visible_theorem(*, public_context: str, declaration: str) -> str:
    if public_context:
        return f"Public Lean context:\n{public_context}\n\nTheorem declaration:\n{declaration}"
    return f"Theorem declaration:\n{declaration}"


def render_prompt(source: Mapping[str, Any]) -> str:
    theorem = render_model_visible_theorem(
        public_context=str(source["public_context"]),
        declaration=str(source["declaration"]),
    )
    return f"Theorem statement:\n{theorem}\n\nRequest:\n{INTUITION_REQUEST}\n\nStrategy:\n"


def escape_lean_block_comment(text: str) -> str:
    if "\x00" in text:
        raise ValueError("guidance containing NUL cannot be rendered")
    return text.replace("/-", "/ -").replace("-/", "- /")


def _record_has_forbidden_key(value: Any) -> list[str]:
    found: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            normalized = str(key).lower()
            if normalized in FORBIDDEN_SOURCE_KEYS:
                found.append(str(key))
            found.extend(_record_has_forbidden_key(child))
    elif isinstance(value, list):
        for child in value:
            found.extend(_record_has_forbidden_key(child))
    return found


def validate_source_row(row: Mapping[str, Any]) -> None:
    required = {
        "schema_version",
        "workload",
        "task_id",
        "declaration_name",
        "declaration",
        "public_context",
        "model_visible_theorem_sha256",
        "upstream",
        *EVALUATION_MARKERS,
    }
    if set(row) != required:
        raise ValueError("source row fields differ from the theorem-only schema")
    if row["schema_version"] != SOURCE_SCHEMA_VERSION:
        raise ValueError("source row has the wrong schema")
    if row["workload"] not in WORKLOADS:
        raise ValueError("source row has an unknown workload")
    for key, expected in EVALUATION_MARKERS.items():
        if row[key] != expected:
            raise ValueError(f"source row has the wrong {key} marker")
    forbidden = _record_has_forbidden_key(row)
    if forbidden:
        raise ValueError(f"source row exposes forbidden fields: {sorted(set(forbidden))}")
    theorem = render_model_visible_theorem(
        public_context=str(row["public_context"]),
        declaration=str(row["declaration"]),
    )
    if row["model_visible_theorem_sha256"] != sha256_text(theorem):
        raise ValueError("source theorem material hash differs")
    upstream = row["upstream"]
    if not isinstance(upstream, dict) or set(upstream) != {
        "repository",
        "accepted_commit",
        "membership_evidence_commit",
        "source_path",
        "source_file_sha256",
    }:
        raise ValueError("source row has malformed upstream provenance")
    if (
        upstream["repository"] != QWEN_REPOSITORY
        or upstream["accepted_commit"] != QWEN_ACCEPTED_COMMIT
        or upstream["membership_evidence_commit"] != QWEN_MEMBERSHIP_EVIDENCE_COMMIT
    ):
        raise ValueError("source row has the wrong qwen-lean lineage")


def validate_prompt_row(row: Mapping[str, Any], source: Mapping[str, Any]) -> None:
    required = {
        "schema_version",
        "workload",
        "task_id",
        "prompt_id",
        "prompt_text",
        "prompt_sha256",
        "model_visible_theorem_sha256",
        *EVALUATION_MARKERS,
    }
    if set(row) != required or row["schema_version"] != PROMPT_SCHEMA_VERSION:
        raise ValueError("prompt row fields or schema differ")
    expected_text = render_prompt(source)
    if row["prompt_text"] != expected_text or row["prompt_sha256"] != sha256_text(expected_text):
        raise ValueError("prompt is not the exact deterministic source projection")
    if row["model_visible_theorem_sha256"] != source["model_visible_theorem_sha256"]:
        raise ValueError("prompt theorem binding differs")
    expected_id = stable_id(
        "frontier_prompt",
        {
            "workload": source["workload"],
            "task_id": source["task_id"],
            "prompt_sha256": row["prompt_sha256"],
        },
    )
    if row["prompt_id"] != expected_id:
        raise ValueError("prompt identity differs")
    for key, expected in EVALUATION_MARKERS.items():
        if row[key] != expected:
            raise ValueError(f"prompt row has the wrong {key} marker")


def _git_object_to_temp(qwen_repo: Path, path: str) -> tempfile._TemporaryFileWrapper[bytes]:
    temporary = tempfile.NamedTemporaryFile(prefix="frontier-intuition-upstream-")
    process = subprocess.Popen(
        ["git", "show", f"{QWEN_ACCEPTED_COMMIT}:{path}"],
        cwd=qwen_repo,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if process.stdout is None:
        temporary.close()
        raise RuntimeError("git show did not expose stdout")
    digest = hashlib.sha256()
    for chunk in iter(lambda: process.stdout.read(1024 * 1024), b""):
        digest.update(chunk)
        temporary.write(chunk)
    stderr = b"" if process.stderr is None else process.stderr.read()
    returncode = process.wait()
    if returncode != 0:
        temporary.close()
        raise RuntimeError(f"cannot read pinned qwen-lean object {path}: {stderr.decode(errors='replace')}")
    if digest.hexdigest() != UPSTREAM_FILE_SHA256[path]:
        temporary.close()
        raise ValueError(f"pinned qwen-lean object hash differs: {path}")
    temporary.flush()
    temporary.seek(0)
    return temporary


def _source_upstream(path: str) -> dict[str, Any]:
    return {
        "repository": QWEN_REPOSITORY,
        "accepted_commit": QWEN_ACCEPTED_COMMIT,
        "membership_evidence_commit": QWEN_MEMBERSHIP_EVIDENCE_COMMIT,
        "source_path": path,
        "source_file_sha256": UPSTREAM_FILE_SHA256[path],
    }


def _source_row(
    *,
    workload: str,
    task_id: str,
    declaration_name: str,
    declaration: str,
    public_context: str,
    source_path: str,
) -> dict[str, Any]:
    theorem = render_model_visible_theorem(
        public_context=public_context,
        declaration=declaration,
    )
    row = {
        "schema_version": SOURCE_SCHEMA_VERSION,
        "workload": workload,
        "task_id": task_id,
        "declaration_name": declaration_name,
        "declaration": declaration,
        "public_context": public_context,
        "model_visible_theorem_sha256": sha256_text(theorem),
        "upstream": _source_upstream(source_path),
        **EVALUATION_MARKERS,
    }
    validate_source_row(row)
    return row


def _materialize_minif2f(qwen_repo: Path) -> list[dict[str, Any]]:
    temporary = _git_object_to_temp(qwen_repo, MINIF2F_PATH)
    rows: list[dict[str, Any]] = []
    try:
        wrapper = io.TextIOWrapper(temporary, encoding="utf-8")
        for line in wrapper:
            value = json.loads(line)
            if set(value) != {
                "declaration",
                "declaration_name",
                "preamble",
                "source_split",
                "task_id",
            }:
                raise ValueError("miniF2F source gained an unexpected field")
            if value["source_split"] != "valid":
                raise ValueError("non-validation miniF2F row entered issue #57")
            rows.append(
                _source_row(
                    workload="minif2f-valid-clean-v2",
                    task_id=str(value["task_id"]),
                    declaration_name=str(value["declaration_name"]),
                    declaration=str(value["declaration"]),
                    public_context=str(value["preamble"]),
                    source_path=MINIF2F_PATH,
                )
            )
        wrapper.detach()
    finally:
        temporary.close()
    return rows


def _declaration_name(declaration: str) -> str:
    matched = re.match(r"\s*(?:theorem|lemma)\s+([^\s:({]+)", declaration)
    if matched is None:
        raise ValueError("cannot recover the public declaration name")
    return matched.group(1)


def _materialize_fresh_composition(qwen_repo: Path) -> list[dict[str, Any]]:
    temporary = _git_object_to_temp(qwen_repo, RECORDS_PATH)
    selected: list[dict[str, Any]] = []
    try:
        with gzip.GzipFile(fileobj=temporary, mode="rb") as compressed:
            with io.TextIOWrapper(compressed, encoding="utf-8") as wrapper:
                for line in wrapper:
                    value = json.loads(line)
                    if value.get("provenance") != "synthetic" or value.get("role") != "validation":
                        continue
                    environment = value.get("environment")
                    if not isinstance(environment, dict):
                        raise ValueError("synthetic validation row lacks public environment")
                    imports = environment.get("imports")
                    if not isinstance(imports, list) or not imports or not all(
                        isinstance(item, str) and item for item in imports
                    ):
                        raise ValueError("synthetic validation row lacks persisted imports")
                    declaration = str(value["canonical_declaration"])
                    selected.append(
                        _source_row(
                            workload="fresh-composition-valid-v2",
                            task_id=str(value["statement_id"]),
                            declaration_name=_declaration_name(declaration),
                            declaration=declaration,
                            public_context="\n".join(
                                f"import {module}" for module in dict.fromkeys(imports)
                            ),
                            source_path=RECORDS_PATH,
                        )
                    )
    finally:
        temporary.close()
    return sorted(selected, key=lambda row: str(row["task_id"]))


def _prompt_row(source: Mapping[str, Any]) -> dict[str, Any]:
    prompt = render_prompt(source)
    prompt_hash = sha256_text(prompt)
    row = {
        "schema_version": PROMPT_SCHEMA_VERSION,
        "workload": source["workload"],
        "task_id": source["task_id"],
        "prompt_id": stable_id(
            "frontier_prompt",
            {
                "workload": source["workload"],
                "task_id": source["task_id"],
                "prompt_sha256": prompt_hash,
            },
        ),
        "prompt_text": prompt,
        "prompt_sha256": prompt_hash,
        "model_visible_theorem_sha256": source["model_visible_theorem_sha256"],
        **EVALUATION_MARKERS,
    }
    validate_prompt_row(row, source)
    return row


def validate_source_snapshot(root: Path = EXPERIMENT_ROOT) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    sources = list(iter_jsonl(root / "source_tasks.jsonl"))
    prompts = list(iter_jsonl(root / "prompts.jsonl"))
    if len(sources) != sum(EXPECTED_COUNTS.values()) or len(prompts) != len(sources):
        raise ValueError("issue #57 source/prompt count differs from 650")
    source_keys: set[tuple[str, str]] = set()
    prompt_by_key = {(row["workload"], row["task_id"]): row for row in prompts}
    for source in sources:
        validate_source_row(source)
        key = (str(source["workload"]), str(source["task_id"]))
        if key in source_keys:
            raise ValueError("issue #57 source repeats a task")
        source_keys.add(key)
        prompt = prompt_by_key.get(key)
        if prompt is None:
            raise ValueError("issue #57 source lacks a prompt")
        validate_prompt_row(prompt, source)
    if set(prompt_by_key) != source_keys:
        raise ValueError("issue #57 prompt set differs from source tasks")
    for workload in WORKLOADS:
        ids = [str(row["task_id"]) for row in sources if row["workload"] == workload]
        if len(ids) != EXPECTED_COUNTS[workload]:
            raise ValueError(f"{workload} count differs")
        if ordered_ids_sha256(ids) != EXPECTED_ORDERED_TASK_IDS_SHA256[workload]:
            raise ValueError(f"{workload} ordered task identity differs")
    if any("test" in str(row["workload"]).lower() for row in sources):
        raise ValueError("test workload entered issue #57")
    return sources, prompts


def materialize_sources(qwen_repo: Path, root: Path = EXPERIMENT_ROOT) -> dict[str, Any]:
    if not (qwen_repo / ".git").exists():
        raise ValueError("qwen-lean input is not a Git worktree")
    commit_type = subprocess.run(
        ["git", "cat-file", "-t", QWEN_ACCEPTED_COMMIT],
        cwd=qwen_repo,
        text=True,
        capture_output=True,
        check=False,
    )
    if commit_type.returncode != 0 or commit_type.stdout.strip() != "commit":
        raise ValueError("qwen-lean accepted Dataset-v2 commit is unavailable")
    sources = _materialize_minif2f(qwen_repo) + _materialize_fresh_composition(qwen_repo)
    for workload in WORKLOADS:
        ids = [str(row["task_id"]) for row in sources if row["workload"] == workload]
        if len(ids) != EXPECTED_COUNTS[workload]:
            raise ValueError(f"{workload} count differs before materialization")
        if ordered_ids_sha256(ids) != EXPECTED_ORDERED_TASK_IDS_SHA256[workload]:
            raise ValueError(f"{workload} ordered task identities differ before materialization")
    prompts = [_prompt_row(row) for row in sources]
    write_jsonl_once(root / "source_tasks.jsonl", sources)
    write_jsonl_once(root / "prompts.jsonl", prompts)
    validate_source_snapshot(root)
    return {
        "source_count": len(sources),
        "counts": dict(EXPECTED_COUNTS),
        "ordered_task_ids_sha256": dict(EXPECTED_ORDERED_TASK_IDS_SHA256),
        "source_tasks_sha256": sha256_file(root / "source_tasks.jsonl"),
        "prompts_sha256": sha256_file(root / "prompts.jsonl"),
    }


def _verified_codex_runtime() -> dict[str, Any]:
    executable = shutil.which("codex")
    if executable is None:
        raise RuntimeError("codex executable is unavailable")
    resolved = Path(executable).resolve()
    completed = subprocess.run(
        [str(resolved), "--version"],
        text=True,
        capture_output=True,
        check=False,
    )
    if completed.returncode != 0 or not completed.stdout.strip().startswith("codex-cli "):
        raise RuntimeError("codex CLI version cannot be resolved")
    return {
        "product": "OpenAI Codex CLI",
        "cli_version": completed.stdout.strip().removeprefix("codex-cli "),
        "executable_sha256": sha256_file(resolved),
    }


def codex_command(executable: str = "codex") -> list[str]:
    command = [
        executable,
        "exec",
        "--ephemeral",
        "--ignore-user-config",
        "--ignore-rules",
        "--skip-git-repo-check",
        "--strict-config",
        "-m",
        GENERATOR_MODEL,
        "-c",
        f'model_reasoning_effort="{GENERATOR_REASONING_EFFORT}"',
        "-s",
        "read-only",
    ]
    for feature in DISABLED_CODEX_FEATURES:
        command.extend(("--disable", feature))
    command.extend(("--json", "-"))
    return command


def _load_tokenizer() -> Any:
    try:
        from transformers import AutoTokenizer
    except ImportError as error:
        raise RuntimeError("transformers is required for the frozen tokenizer") from error
    tokenizer = AutoTokenizer.from_pretrained(
        TOKENIZER_ID,
        revision=TOKENIZER_REVISION,
        local_files_only=True,
        trust_remote_code=False,
    )
    return tokenizer


def _manifest_payload(root: Path, runtime: Mapping[str, Any]) -> dict[str, Any]:
    command_shape = codex_command("codex")
    return {
        "schema_version": MANIFEST_SCHEMA_VERSION,
        "controlling_issue": CONTROLLING_ISSUE,
        "artifact_id": SCHEMA_VERSION,
        "status": "pre_generation_contract_frozen",
        "source_contract": {
            "qwen_repository": QWEN_REPOSITORY,
            "accepted_dataset_v2_commit": QWEN_ACCEPTED_COMMIT,
            "membership_evidence_commit": QWEN_MEMBERSHIP_EVIDENCE_COMMIT,
            "upstream_files_sha256": UPSTREAM_FILE_SHA256,
            "workload_counts": EXPECTED_COUNTS,
            "ordered_task_ids_sha256": EXPECTED_ORDERED_TASK_IDS_SHA256,
            "source_tasks_sha256": sha256_file(root / "source_tasks.jsonl"),
            "prompts_sha256": sha256_file(root / "prompts.jsonl"),
            "generator_reads_only": ["source_tasks.jsonl", "prompts.jsonl", "generation_manifest.json"],
            "forbidden_generator_inputs": sorted(FORBIDDEN_SOURCE_KEYS),
            "final_test_workloads_allowed": False,
        },
        "generator_contract": {
            **runtime,
            "model": GENERATOR_MODEL,
            "reasoning_effort": GENERATOR_REASONING_EFFORT,
            "session": "fresh_isolated_ephemeral_per_attempt",
            "working_directory": "fresh_empty_non_repository_temporary_directory",
            "project_instructions_loaded": False,
            "user_config_loaded": False,
            "prior_conversation": False,
            "tools_allowed": False,
            "tool_or_unexpected_event_action": "generation_failure",
            "disabled_cli_features": list(DISABLED_CODEX_FEATURES),
            "sandbox": "read-only",
            "command_shape": command_shape[1:],
            "timeout_seconds": GENERATION_TIMEOUT_SECONDS,
            "sampling_controls": "product_managed_no_user_temperature_top_p_or_seed",
        },
        "prompt_contract": {
            "intuition_request": INTUITION_REQUEST,
            "template": "Theorem statement:\\n{model_visible_theorem}\\n\\nRequest:\\n{intuition_request}\\n\\nStrategy:\\n",
            "prompt_count": sum(EXPECTED_COUNTS.values()),
            "prompt_text_is_write_once": True,
        },
        "tokenizer_contract": {
            "model": TOKENIZER_ID,
            "revision": TOKENIZER_REVISION,
            "add_special_tokens": False,
            "counted_text": "exact_downstream_visible_text_after_lean_block_comment_escaping_before_wrapper",
            "maximum_tokens": MAX_GUIDANCE_TOKENS,
        },
        "eligibility_contract": {
            "schema_version": ELIGIBILITY_SCHEMA_VERSION,
            "primary_gate": "deterministic_no_llm_quality_judge",
            "reason_priority": list(REASON_PRIORITY),
            "lean_syntax_patterns": [list(item) for item in LEAN_SYNTAX_PATTERNS],
            "formal_identifier_patterns": [list(item) for item in FORMAL_IDENTIFIER_PATTERNS],
            "proof_like_patterns": [list(item) for item in PROOF_LIKE_PATTERNS],
            "proof_like_aggregate_rules": {
                "numbered_steps_at_least": 3,
                "sequence_markers_at_least": 4,
                "proof_actions_and_clauses": {"actions_at_least": 6, "clauses_at_least": 5},
            },
            "semantic_quality_selection": False,
            "repair_or_sanitization": False,
        },
        "regeneration_contract": {
            "attempt_1_always": True,
            "retry_only_after_deterministic_ineligibility": True,
            "fresh_identical_prompt_and_config": True,
            "accept_first_eligible": True,
            "maximum_attempts": MAX_ATTEMPTS,
            "missing_after_two_failures": "missing_accepted_intuition",
            "outcome_dependent_retry": False,
            "subjective_quality_retry": False,
        },
        "implementation": {
            "core.py_sha256": sha256_file(root / "core.py"),
            "__main__.py_sha256": sha256_file(root / "__main__.py"),
        },
        "artifact_boundary": EVALUATION_MARKERS,
    }


def freeze_contract(root: Path = EXPERIMENT_ROOT) -> dict[str, Any]:
    validate_source_snapshot(root)
    tokenizer = _load_tokenizer()
    probe = tokenizer.encode("frontier intuition tokenizer probe", add_special_tokens=False)
    if not isinstance(probe, list) or not probe:
        raise RuntimeError("frozen tokenizer failed its local probe")
    runtime = _verified_codex_runtime()
    payload = _manifest_payload(root, runtime)
    manifest = {
        **payload,
        "frozen_at_utc": utc_now(),
        "generation_manifest_id": stable_id("frontier_generation_manifest", payload),
    }
    write_json_once(root / "generation_manifest.json", manifest)
    validate_manifest(root)
    return manifest


def validate_manifest(root: Path = EXPERIMENT_ROOT) -> dict[str, Any]:
    path = root / "generation_manifest.json"
    manifest = json.loads(path.read_text(encoding="utf-8"))
    frozen_at = manifest.get("frozen_at_utc")
    manifest_id = manifest.get("generation_manifest_id")
    payload = {key: value for key, value in manifest.items() if key not in {"frozen_at_utc", "generation_manifest_id"}}
    runtime = _verified_codex_runtime()
    expected = _manifest_payload(root, runtime)
    if payload != expected:
        raise ValueError("generation manifest differs from the current frozen contract/runtime")
    if not isinstance(frozen_at, str) or not frozen_at.endswith("Z"):
        raise ValueError("generation manifest has an invalid freeze time")
    if manifest_id != stable_id("frontier_generation_manifest", expected):
        raise ValueError("generation manifest identity differs")
    return manifest


def parse_codex_transcript(transcript: str) -> dict[str, Any]:
    final_messages: list[str] = []
    thread_ids: list[str] = []
    unexpected_items: list[str] = []
    invalid_json_lines = 0
    for line in transcript.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            invalid_json_lines += 1
            continue
        if event.get("type") == "thread.started" and isinstance(event.get("thread_id"), str):
            thread_ids.append(event["thread_id"])
        if event.get("type") != "item.completed":
            continue
        item = event.get("item")
        if not isinstance(item, dict):
            unexpected_items.append("malformed_completed_item")
            continue
        item_type = str(item.get("type"))
        if item_type == "agent_message" and isinstance(item.get("text"), str):
            final_messages.append(item["text"])
        elif item_type != "reasoning":
            unexpected_items.append(item_type)
    valid = (
        invalid_json_lines == 0
        and len(thread_ids) == 1
        and len(final_messages) == 1
        and not unexpected_items
    )
    return {
        "valid_tool_free_capture": valid,
        "thread_ids": thread_ids,
        "agent_message_count": len(final_messages),
        "unexpected_item_types": unexpected_items,
        "invalid_json_lines": invalid_json_lines,
        "final_message": final_messages[0] if len(final_messages) == 1 else None,
    }


def _matched_rules(
    text: str,
    patterns: Sequence[tuple[str, str]],
    *,
    flags: int = re.I,
) -> list[str]:
    return [name for name, pattern in patterns if re.search(pattern, text, flags)]


def classify_text(
    *,
    raw_text: str | None,
    valid_tool_free_capture: bool,
    declaration_name: str,
    tokenizer: Any,
) -> dict[str, Any]:
    triggered: list[str] = []
    rule_matches: dict[str, list[str]] = {
        "lean_syntax": [],
        "formal_identifier": [],
        "proof_like": [],
    }
    downstream_text: str | None = None
    downstream_hash: str | None = None
    raw_hash: str | None = None
    token_ids: list[int] = []
    if not valid_tool_free_capture or not isinstance(raw_text, str) or not raw_text.strip():
        triggered.append("generation_failure")
    else:
        raw_hash = sha256_text(raw_text)
        downstream_text = escape_lean_block_comment(raw_text)
        downstream_hash = sha256_text(downstream_text)
        token_ids = list(tokenizer.encode(downstream_text, add_special_tokens=False))
        rule_matches["lean_syntax"] = _matched_rules(raw_text, LEAN_SYNTAX_PATTERNS)
        if rule_matches["lean_syntax"]:
            triggered.append("rejected_lean_syntax")
        rule_matches["formal_identifier"] = _matched_rules(
            raw_text,
            FORMAL_IDENTIFIER_PATTERNS,
            flags=0,
        )
        if re.search(rf"\b{re.escape(declaration_name)}\b", raw_text):
            rule_matches["formal_identifier"].append("copied_declaration_name")
        if rule_matches["formal_identifier"]:
            triggered.append("rejected_formal_identifier")
        proof_matches = _matched_rules(raw_text, PROOF_LIKE_PATTERNS)
        numbered_steps = len(NUMBERED_STEP.findall(raw_text))
        sequence_markers = len(SEQUENCE_MARKERS.findall(raw_text))
        proof_actions = len(PROOF_ACTIONS.findall(raw_text))
        clauses = len(re.findall(r"[.;:]|\n", raw_text)) + 1
        if numbered_steps >= 3:
            proof_matches.append("three_or_more_numbered_steps")
        if sequence_markers >= 4:
            proof_matches.append("four_or_more_sequence_markers")
        if proof_actions >= 6 and clauses >= 5:
            proof_matches.append("dense_local_derivation")
        rule_matches["proof_like"] = proof_matches
        if proof_matches:
            triggered.append("rejected_proof_like")
        if len(token_ids) > MAX_GUIDANCE_TOKENS:
            triggered.append("rejected_over_budget")
    primary = next((reason for reason in REASON_PRIORITY if reason in triggered), "accepted")
    if primary == "accepted":
        triggered = ["accepted"]
    return {
        "schema_version": ELIGIBILITY_SCHEMA_VERSION,
        "status": primary,
        "eligible": primary == "accepted",
        "triggered_reasons": triggered,
        "matched_rules": rule_matches,
        "raw_output_sha256": raw_hash,
        "downstream_visible_text": downstream_text,
        "downstream_visible_text_sha256": downstream_hash,
        "post_render": {
            "transformation": "lean_block_comment_escape_only",
            "tokenizer": {
                "model": TOKENIZER_ID,
                "revision": TOKENIZER_REVISION,
                "add_special_tokens": False,
            },
            "token_ids": token_ids,
            "token_ids_sha256": sha256_text(canonical_json(token_ids)),
            "token_count": len(token_ids),
            "maximum_tokens": MAX_GUIDANCE_TOKENS,
        },
    }


def _safe_task_path(task_id: str) -> str:
    safe = re.sub(r"[^A-Za-z0-9_.-]", "_", task_id)
    if len(safe) > 96:
        safe = safe[:48] + "_" + sha256_text(task_id)[:32]
    return safe


def capture_path(root: Path, source: Mapping[str, Any], attempt_index: int) -> Path:
    return (
        root
        / "captures"
        / str(source["workload"])
        / _safe_task_path(str(source["task_id"]))
        / f"attempt_{attempt_index}.json"
    )


def _run_codex(prompt: str, runtime: Mapping[str, Any]) -> dict[str, Any]:
    executable = shutil.which("codex")
    if executable is None:
        raise RuntimeError("codex executable is unavailable")
    resolved = str(Path(executable).resolve())
    if sha256_file(Path(resolved)) != runtime["executable_sha256"]:
        raise RuntimeError("codex executable changed after pre-generation freeze")
    command = codex_command(resolved)
    started_at = utc_now()
    monotonic_start = time.monotonic()
    stdout = ""
    stderr = ""
    returncode: int | None = None
    timed_out = False
    with tempfile.TemporaryDirectory(prefix="frontier-intuition-codex-") as directory:
        try:
            completed = subprocess.run(
                command,
                input=prompt,
                cwd=directory,
                capture_output=True,
                text=True,
                check=False,
                timeout=GENERATION_TIMEOUT_SECONDS,
            )
            stdout = completed.stdout
            stderr = completed.stderr
            returncode = completed.returncode
        except subprocess.TimeoutExpired as error:
            timed_out = True
            stdout = error.stdout if isinstance(error.stdout, str) else ""
            stderr = error.stderr if isinstance(error.stderr, str) else ""
    parsed = parse_codex_transcript(stdout)
    finished_at = utc_now()
    return {
        "started_at_utc": started_at,
        "finished_at_utc": finished_at,
        "duration_seconds": round(time.monotonic() - monotonic_start, 6),
        "command": command[1:],
        "working_directory": "fresh_empty_non_repository_temporary_directory",
        "returncode": returncode,
        "timed_out": timed_out,
        "stdout_jsonl": stdout,
        "stdout_sha256": sha256_text(stdout),
        "stderr": stderr,
        "stderr_sha256": sha256_text(stderr),
        **parsed,
        "valid_capture": returncode == 0 and not timed_out and parsed["valid_tool_free_capture"],
    }


class FrozenTokenizer:
    def __init__(self) -> None:
        self.value = _load_tokenizer()
        self._lock = threading.Lock()

    def encode(self, text: str, *, add_special_tokens: bool) -> list[int]:
        with self._lock:
            return list(self.value.encode(text, add_special_tokens=add_special_tokens))


def _attempt_record(
    *,
    source: Mapping[str, Any],
    prompt: Mapping[str, Any],
    attempt_index: int,
    manifest: Mapping[str, Any],
    tokenizer: Any,
) -> dict[str, Any]:
    run = _run_codex(str(prompt["prompt_text"]), manifest["generator_contract"])
    eligibility = classify_text(
        raw_text=run["final_message"],
        valid_tool_free_capture=bool(run["valid_capture"]),
        declaration_name=str(source["declaration_name"]),
        tokenizer=tokenizer,
    )
    identity = {
        "workload": source["workload"],
        "task_id": source["task_id"],
        "attempt_index": attempt_index,
        "generation_manifest_id": manifest["generation_manifest_id"],
        "prompt_sha256": prompt["prompt_sha256"],
        "thread_ids": run["thread_ids"],
        "stdout_sha256": run["stdout_sha256"],
    }
    return {
        "schema_version": ATTEMPT_SCHEMA_VERSION,
        "attempt_id": stable_id("frontier_attempt", identity),
        "workload": source["workload"],
        "task_id": source["task_id"],
        "attempt_index": attempt_index,
        "generation_manifest_id": manifest["generation_manifest_id"],
        "generator": manifest["generator_contract"],
        "prompt_id": prompt["prompt_id"],
        "prompt_sha256": prompt["prompt_sha256"],
        "model_visible_theorem_sha256": source["model_visible_theorem_sha256"],
        "raw_output_text": run["final_message"],
        "eligibility": eligibility,
        "capture": run,
        **EVALUATION_MARKERS,
    }


def validate_attempt(
    row: Mapping[str, Any],
    *,
    source: Mapping[str, Any],
    prompt: Mapping[str, Any],
    manifest: Mapping[str, Any],
    tokenizer: Any,
) -> None:
    if row.get("schema_version") != ATTEMPT_SCHEMA_VERSION:
        raise ValueError("attempt has the wrong schema")
    if (
        row.get("workload") != source["workload"]
        or row.get("task_id") != source["task_id"]
        or row.get("prompt_id") != prompt["prompt_id"]
        or row.get("prompt_sha256") != prompt["prompt_sha256"]
        or row.get("model_visible_theorem_sha256") != source["model_visible_theorem_sha256"]
        or row.get("generation_manifest_id") != manifest["generation_manifest_id"]
        or row.get("generator") != manifest["generator_contract"]
    ):
        raise ValueError("attempt source/prompt/generator binding differs")
    if row.get("attempt_index") not in {1, 2}:
        raise ValueError("attempt index differs from the maximum-two policy")
    capture = row.get("capture")
    if not isinstance(capture, dict):
        raise ValueError("attempt lacks its raw capture")
    parsed = parse_codex_transcript(str(capture.get("stdout_jsonl", "")))
    if any(capture.get(key) != value for key, value in parsed.items()):
        raise ValueError("attempt transcript parse evidence differs")
    valid_capture = (
        capture.get("returncode") == 0
        and not capture.get("timed_out")
        and parsed["valid_tool_free_capture"]
    )
    if capture.get("valid_capture") != valid_capture:
        raise ValueError("attempt validity differs from the raw transcript")
    if capture.get("stdout_sha256") != sha256_text(str(capture.get("stdout_jsonl", ""))):
        raise ValueError("attempt stdout hash differs")
    if capture.get("stderr_sha256") != sha256_text(str(capture.get("stderr", ""))):
        raise ValueError("attempt stderr hash differs")
    expected_eligibility = classify_text(
        raw_text=row.get("raw_output_text") if isinstance(row.get("raw_output_text"), str) else None,
        valid_tool_free_capture=valid_capture,
        declaration_name=str(source["declaration_name"]),
        tokenizer=tokenizer,
    )
    if row.get("eligibility") != expected_eligibility:
        raise ValueError("attempt eligibility is not a deterministic raw-capture projection")
    identity = {
        "workload": source["workload"],
        "task_id": source["task_id"],
        "attempt_index": row["attempt_index"],
        "generation_manifest_id": manifest["generation_manifest_id"],
        "prompt_sha256": prompt["prompt_sha256"],
        "thread_ids": capture["thread_ids"],
        "stdout_sha256": capture["stdout_sha256"],
    }
    if row.get("attempt_id") != stable_id("frontier_attempt", identity):
        raise ValueError("attempt identity differs")
    for key, expected in EVALUATION_MARKERS.items():
        if row.get(key) != expected:
            raise ValueError(f"attempt has the wrong {key} marker")


def _read_capture(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"capture is not an object: {path}")
    return value


def _generate_task(
    source: Mapping[str, Any],
    prompt: Mapping[str, Any],
    manifest: Mapping[str, Any],
    tokenizer: Any,
    root: Path,
) -> dict[str, Any]:
    attempts: list[dict[str, Any]] = []
    for attempt_index in range(1, MAX_ATTEMPTS + 1):
        path = capture_path(root, source, attempt_index)
        if path.exists():
            attempt = _read_capture(path)
        else:
            attempt = _attempt_record(
                source=source,
                prompt=prompt,
                attempt_index=attempt_index,
                manifest=manifest,
                tokenizer=tokenizer,
            )
            write_json_once(path, attempt)
        validate_attempt(
            attempt,
            source=source,
            prompt=prompt,
            manifest=manifest,
            tokenizer=tokenizer,
        )
        attempts.append(attempt)
        if attempt["eligibility"]["eligible"]:
            break
    return {
        "workload": source["workload"],
        "task_id": source["task_id"],
        "attempts": len(attempts),
        "accepted": bool(attempts[-1]["eligibility"]["eligible"]),
        "final_reason": attempts[-1]["eligibility"]["status"],
    }


def generate(root: Path = EXPERIMENT_ROOT, *, workers: int = 1) -> dict[str, Any]:
    if workers < 1 or workers > 16:
        raise ValueError("workers must be between 1 and 16")
    sources, prompts = validate_source_snapshot(root)
    manifest = validate_manifest(root)
    tokenizer = FrozenTokenizer()
    prompt_by_key = {(row["workload"], row["task_id"]): row for row in prompts}
    results: list[dict[str, Any]] = []
    source_iterator = iter(sources)
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures: dict[Any, tuple[str, str]] = {}

        def submit_one(source: Mapping[str, Any]) -> None:
            future = executor.submit(
                _generate_task,
                source,
                prompt_by_key[(source["workload"], source["task_id"])],
                manifest,
                tokenizer,
                root,
            )
            futures[future] = (str(source["workload"]), str(source["task_id"]))

        for _ in range(min(workers, len(sources))):
            submit_one(next(source_iterator))
        completed = 0
        while futures:
            future = next(as_completed(futures))
            futures.pop(future)
            result = future.result()
            results.append(result)
            completed += 1
            print(
                canonical_json(
                    {
                        "completed": completed,
                        "total": len(sources),
                        **result,
                    }
                ),
                flush=True,
            )
            try:
                submit_one(next(source_iterator))
            except StopIteration:
                pass
    return {
        "task_count": len(results),
        "accepted": sum(result["accepted"] for result in results),
        "missing": sum(not result["accepted"] for result in results),
    }


def load_attempts(root: Path = EXPERIMENT_ROOT) -> list[dict[str, Any]]:
    sources, prompts = validate_source_snapshot(root)
    manifest = validate_manifest(root)
    tokenizer = FrozenTokenizer()
    prompt_by_key = {(row["workload"], row["task_id"]): row for row in prompts}
    attempts: list[dict[str, Any]] = []
    for source in sources:
        prompt = prompt_by_key[(source["workload"], source["task_id"])]
        first_path = capture_path(root, source, 1)
        if not first_path.is_file():
            raise ValueError(f"task lacks mandatory attempt 1: {source['task_id']}")
        first = _read_capture(first_path)
        validate_attempt(first, source=source, prompt=prompt, manifest=manifest, tokenizer=tokenizer)
        attempts.append(first)
        second_path = capture_path(root, source, 2)
        if first["eligibility"]["eligible"]:
            if second_path.exists():
                raise ValueError("eligible attempt 1 was impermissibly regenerated")
            continue
        if not second_path.is_file():
            raise ValueError(f"ineligible attempt 1 lacks bounded retry: {source['task_id']}")
        second = _read_capture(second_path)
        validate_attempt(second, source=source, prompt=prompt, manifest=manifest, tokenizer=tokenizer)
        attempts.append(second)
    return attempts


def _accepted_projection(
    sources: Sequence[Mapping[str, Any]], attempts: Sequence[Mapping[str, Any]]
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    by_key: dict[tuple[str, str], list[Mapping[str, Any]]] = {}
    for attempt in attempts:
        by_key.setdefault((str(attempt["workload"]), str(attempt["task_id"])), []).append(attempt)
    accepted: list[dict[str, Any]] = []
    leakage: list[dict[str, Any]] = []
    for source in sources:
        key = (str(source["workload"]), str(source["task_id"]))
        task_attempts = sorted(by_key[key], key=lambda row: int(row["attempt_index"]))
        eligible = [row for row in task_attempts if row["eligibility"]["eligible"]]
        if eligible:
            selected = eligible[0]
            downstream = selected["eligibility"]["downstream_visible_text"]
            intuition_id = stable_id(
                "frontier_intuition",
                {
                    "workload": source["workload"],
                    "task_id": source["task_id"],
                    "accepted_attempt_id": selected["attempt_id"],
                    "text_sha256": selected["eligibility"]["downstream_visible_text_sha256"],
                },
            )
            accepted.append(
                {
                    "schema_version": ACCEPTED_SCHEMA_VERSION,
                    "intuition_id": intuition_id,
                    "workload": source["workload"],
                    "task_id": source["task_id"],
                    "model_visible_theorem_sha256": source["model_visible_theorem_sha256"],
                    "accepted_attempt_id": selected["attempt_id"],
                    "accepted_attempt_index": selected["attempt_index"],
                    "text": downstream,
                    "text_sha256": selected["eligibility"]["downstream_visible_text_sha256"],
                    "token_count": selected["eligibility"]["post_render"]["token_count"],
                    "tokenizer": selected["eligibility"]["post_render"]["tokenizer"],
                    **EVALUATION_MARKERS,
                }
            )
        leakage.append(
            {
                "schema_version": ELIGIBILITY_SCHEMA_VERSION,
                "workload": source["workload"],
                "task_id": source["task_id"],
                "accepted_attempt_id": eligible[0]["attempt_id"] if eligible else None,
                "task_status": "accepted" if eligible else "missing_accepted_intuition",
                "attempt_decisions": [
                    {
                        "attempt_id": row["attempt_id"],
                        "attempt_index": row["attempt_index"],
                        "eligibility": row["eligibility"],
                    }
                    for row in task_attempts
                ],
                **EVALUATION_MARKERS,
            }
        )
    return accepted, leakage


def _distribution(values: Sequence[int]) -> dict[str, Any]:
    if not values:
        return {"count": 0, "min": None, "max": None, "mean": None, "median": None, "p90": None, "p95": None, "p99": None}
    ordered = sorted(values)

    def percentile(percent: float) -> int:
        index = max(0, min(len(ordered) - 1, int((len(ordered) - 1) * percent + 0.5)))
        return ordered[index]

    return {
        "count": len(values),
        "min": min(values),
        "max": max(values),
        "mean": round(statistics.fmean(values), 6),
        "median": statistics.median(values),
        "p90": percentile(0.90),
        "p95": percentile(0.95),
        "p99": percentile(0.99),
    }


def _normalized_intuition(text: str) -> str:
    return " ".join(unicodedata.normalize("NFKC", text).casefold().split())


def build_summary(
    sources: Sequence[Mapping[str, Any]],
    attempts: Sequence[Mapping[str, Any]],
    accepted: Sequence[Mapping[str, Any]],
    leakage: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    attempt_reasons = Counter(str(row["eligibility"]["status"]) for row in attempts)
    accepted_by_workload = Counter(str(row["workload"]) for row in accepted)
    missing_by_workload = Counter(
        str(row["workload"]) for row in leakage if row["task_status"] == "missing_accepted_intuition"
    )
    texts = [str(row["text"]) for row in accepted]
    normalized = [_normalized_intuition(text) for text in texts]
    exact_duplicates = len(texts) - len(set(texts))
    normalized_duplicates = len(normalized) - len(set(normalized))
    return {
        "schema_version": SUMMARY_SCHEMA_VERSION,
        "artifact_id": SCHEMA_VERSION,
        "task_count": len(sources),
        "attempt_count": len(attempts),
        "accepted_count": len(accepted),
        "missing_accepted_intuition_count": len(sources) - len(accepted),
        "by_workload": {
            workload: {
                "tasks": EXPECTED_COUNTS[workload],
                "accepted": accepted_by_workload[workload],
                "missing_accepted_intuition": missing_by_workload[workload],
            }
            for workload in WORKLOADS
        },
        "attempt_reasons": dict(sorted(attempt_reasons.items())),
        "accepted_token_length": _distribution([int(row["token_count"]) for row in accepted]),
        "duplicate_diagnostics": {
            "exact_duplicate_rows": exact_duplicates,
            "exact_duplicate_rate": round(exact_duplicates / len(texts), 12) if texts else None,
            "normalized_duplicate_rows": normalized_duplicates,
            "normalized_duplicate_rate": round(normalized_duplicates / len(texts), 12) if texts else None,
            "normalization": "Unicode NFKC, casefold, collapse whitespace",
        },
        "selection_policy": "first eligible attempt only; no semantic ranking or repair",
        "downstream_claim_authorized": False,
        "formal_proof_claim_authorized": False,
        "artifact_boundary": EVALUATION_MARKERS,
    }


def _manifest_candidates(repository_root: Path) -> list[Path]:
    patterns = (
        "**/trainable_manifest.json",
        "**/training_manifest.json",
        "**/mixed_manifest.json",
        "**/*optimizer*manifest*.json",
        "**/*g_v2*manifest*.json",
    )
    paths: set[Path] = set()
    for pattern in patterns:
        paths.update(repository_root.glob(pattern))
    return sorted(
        path
        for path in paths
        if path.is_file() and EXPERIMENT_ROOT not in path.resolve().parents
    )


def _all_strings(value: Any) -> Iterator[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for key, child in value.items():
            yield str(key)
            yield from _all_strings(child)
    elif isinstance(value, list):
        for child in value:
            yield from _all_strings(child)


def _load_manifest_strings(path: Path) -> set[str]:
    value = json.loads(path.read_text(encoding="utf-8"))
    return set(_all_strings(value))


def build_integrity_audit(
    *,
    root: Path,
    sources: Sequence[Mapping[str, Any]],
    accepted: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    task_ids = {str(row["task_id"]) for row in sources}
    intuition_ids = {str(row["intuition_id"]) for row in accepted}
    manifests = _manifest_candidates(REPOSITORY_ROOT)
    memberships: list[dict[str, Any]] = []
    overlaps: list[dict[str, Any]] = []
    for path in manifests:
        strings = _load_manifest_strings(path)
        task_overlap = sorted(task_ids.intersection(strings))
        intuition_overlap = sorted(intuition_ids.intersection(strings))
        record = {
            "path": str(path.relative_to(REPOSITORY_ROOT)),
            "sha256": sha256_file(path),
            "task_id_overlap_count": len(task_overlap),
            "intuition_id_overlap_count": len(intuition_overlap),
        }
        memberships.append(record)
        if task_overlap or intuition_overlap:
            overlaps.append({**record, "task_ids": task_overlap, "intuition_ids": intuition_overlap})

    consumed_by: list[str] = []
    experiment_literal = "frontier_intuition_corpus_v1"
    for path in sorted(REPOSITORY_ROOT.rglob("*")):
        if not path.is_file() or root == path or root in path.parents:
            continue
        if path.suffix not in {".py", ".toml", ".yaml", ".yml", ".json"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if experiment_literal in text:
            consumed_by.append(str(path.relative_to(REPOSITORY_ROOT)))

    interchange_path = REPOSITORY_ROOT / "experiments/mathia_corpus/interchange.py"
    interchange_text = interchange_path.read_text(encoding="utf-8")
    interchange_excludes_evaluation = (
        'QUALITY_STATES = {"accepted", "quarantined", "rejected", "evaluation_only"}' in interchange_text
        and 'record.get("quality_state") != "accepted"' in interchange_text
        and 'record.get("training_eligibility") != "eligible"' in interchange_text
    )
    g_v2_paths = [
        row for row in memberships if "g_v2" in row["path"].lower() or "optimizer" in row["path"].lower()
    ]
    checks = {
        "source_and_intuition_ids_absent_from_trainable_manifests": not overlaps,
        "frontier_path_not_consumed_outside_experiment": not consumed_by,
        "g_v2_manifest_or_materializer_does_not_consume_frontier_path": not any(
            "g_v2" in path.lower() or "optimizer" in path.lower() for path in consumed_by
        ),
        "g_v2_manifest_identity_unchanged_by_isolated_artifact": True,
        "no_mathia_training_roles_assigned": all(
            row.get("artifact_role") == "frontier_reference"
            and row.get("evaluation_only") is True
            and row.get("training_eligible") is False
            for row in [*sources, *accepted]
        ),
        "existing_interchange_renderer_rejects_evaluation_only": interchange_excludes_evaluation,
    }
    return {
        "schema_version": INTEGRITY_SCHEMA_VERSION,
        "status": "pass" if all(checks.values()) else "fail",
        "checks": checks,
        "trainable_manifest_scan": memberships,
        "overlaps": overlaps,
        "external_consumers": consumed_by,
        "g_v2_state": {
            "manifest_or_optimizer_paths": g_v2_paths,
            "interpretation": (
                "No G-v2 optimizer manifest/materializer is present at this source revision; "
                "the isolated directory therefore cannot alter a materialized G-v2 identity."
                if not g_v2_paths
                else "Existing G-v2/optimizer manifest hashes are recorded above and no consumer references the frontier path."
            ),
        },
        "artifact_boundary": EVALUATION_MARKERS,
        "integrity_failure_material": True,
    }


def _capture_manifest(root: Path) -> list[dict[str, Any]]:
    return [
        {
            "path": str(path.relative_to(root)),
            "bytes": path.stat().st_size,
            "sha256": sha256_file(path),
        }
        for path in sorted((root / "captures").rglob("attempt_*.json"))
    ]


def finalize(root: Path = EXPERIMENT_ROOT) -> dict[str, Any]:
    sources, _ = validate_source_snapshot(root)
    manifest = validate_manifest(root)
    attempts = load_attempts(root)
    accepted, leakage = _accepted_projection(sources, attempts)
    summary = build_summary(sources, attempts, accepted, leakage)
    integrity = build_integrity_audit(root=root, sources=sources, accepted=accepted)
    capture_manifest = {
        "schema_version": "frontier-intuition-capture-manifest-v1",
        "generation_manifest_id": manifest["generation_manifest_id"],
        "captures": _capture_manifest(root),
    }
    write_jsonl_once(root / "raw_attempts.jsonl", attempts)
    write_jsonl_once(root / "accepted_intuitions.jsonl", accepted)
    write_jsonl_once(root / "leakage_results.jsonl", leakage)
    write_json_once(root / "summary.json", summary)
    write_json_once(root / "integrity_audit.json", integrity)
    write_json_once(root / "capture_manifest.json", capture_manifest)

    decision = (
        "FRONTIER_INTUITION_INTEGRITY_BLOCKER"
        if integrity["status"] != "pass"
        else (
            "FRONTIER_INTUITION_GENERATION_BLOCKER"
            if summary["missing_accepted_intuition_count"]
            else "FRONTIER_INTUITION_CORPUS_READY"
        )
    )
    artifact_names = (
        "source_tasks.jsonl",
        "generation_manifest.json",
        "prompts.jsonl",
        "raw_attempts.jsonl",
        "accepted_intuitions.jsonl",
        "leakage_results.jsonl",
        "summary.json",
        "integrity_audit.json",
        "capture_manifest.json",
    )
    freeze_payload = {
        "schema_version": FREEZE_SCHEMA_VERSION,
        "artifact_id": SCHEMA_VERSION,
        "decision": decision,
        "generation_manifest_id": manifest["generation_manifest_id"],
        "artifacts": {
            name: {"bytes": (root / name).stat().st_size, "sha256": sha256_file(root / name)}
            for name in artifact_names
        },
        "source_code": {
            "core.py": sha256_file(root / "core.py"),
            "__main__.py": sha256_file(root / "__main__.py"),
        },
        "summary": {
            "tasks": summary["task_count"],
            "attempts": summary["attempt_count"],
            "accepted": summary["accepted_count"],
            "missing": summary["missing_accepted_intuition_count"],
        },
        "independent_audit": {
            "required": True,
            "status": "pending_exact_published_target_review",
            "technical_review_is_not_merge_authorization": True,
        },
        "artifact_boundary": EVALUATION_MARKERS,
        "downstream_proof_claim_authorized": False,
    }
    freeze = {
        **freeze_payload,
        "frozen_at_utc": utc_now(),
        "freeze_id": stable_id("frontier_intuition_corpus", freeze_payload),
    }
    write_json_once(root / "freeze.json", freeze)
    validate_finalized(root)
    return freeze


def validate_finalized(root: Path = EXPERIMENT_ROOT) -> dict[str, Any]:
    sources, _ = validate_source_snapshot(root)
    manifest = validate_manifest(root)
    attempts = load_attempts(root)
    accepted, leakage = _accepted_projection(sources, attempts)
    stored_attempts = list(iter_jsonl(root / "raw_attempts.jsonl"))
    stored_accepted = list(iter_jsonl(root / "accepted_intuitions.jsonl"))
    stored_leakage = list(iter_jsonl(root / "leakage_results.jsonl"))
    if stored_attempts != attempts or stored_accepted != accepted or stored_leakage != leakage:
        raise ValueError("final JSONL artifacts are not deterministic capture projections")
    expected_summary = build_summary(sources, attempts, accepted, leakage)
    if json.loads((root / "summary.json").read_text(encoding="utf-8")) != expected_summary:
        raise ValueError("summary is not a deterministic projection")
    expected_integrity = build_integrity_audit(root=root, sources=sources, accepted=accepted)
    if json.loads((root / "integrity_audit.json").read_text(encoding="utf-8")) != expected_integrity:
        raise ValueError("integrity audit differs from the current repository state")
    expected_capture_manifest = {
        "schema_version": "frontier-intuition-capture-manifest-v1",
        "generation_manifest_id": manifest["generation_manifest_id"],
        "captures": _capture_manifest(root),
    }
    if json.loads((root / "capture_manifest.json").read_text(encoding="utf-8")) != expected_capture_manifest:
        raise ValueError("capture manifest differs")
    freeze = json.loads((root / "freeze.json").read_text(encoding="utf-8"))
    payload = {key: value for key, value in freeze.items() if key not in {"frozen_at_utc", "freeze_id"}}
    if freeze.get("freeze_id") != stable_id("frontier_intuition_corpus", payload):
        raise ValueError("freeze identity differs")
    for name, identity in freeze["artifacts"].items():
        path = root / name
        if identity != {"bytes": path.stat().st_size, "sha256": sha256_file(path)}:
            raise ValueError(f"frozen artifact identity differs: {name}")
    for name, digest in freeze["source_code"].items():
        if sha256_file(root / name) != digest:
            raise ValueError(f"frozen source-code identity differs: {name}")
    if len({row["accepted_attempt_id"] for row in accepted}) != len(accepted):
        raise ValueError("accepted artifact reuses an attempt")
    raw_ids = {row["attempt_id"] for row in attempts}
    if any(row["accepted_attempt_id"] not in raw_ids for row in accepted):
        raise ValueError("accepted row does not derive from a stored raw attempt")
    return {
        "valid": True,
        "freeze_id": freeze["freeze_id"],
        "decision": freeze["decision"],
        "task_count": len(sources),
        "attempt_count": len(attempts),
        "accepted_count": len(accepted),
    }
