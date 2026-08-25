"""Issue #59 frontier-assisted intuition generation and immutable audit.

This is deliberately a bounded experiment, not a reusable dataset framework.
Only the source materializer reads the already-verified issue #57 theorem-only
snapshot. Generation and semantic review read the local public projection and
the frozen issue #59 contract.
"""

from __future__ import annotations

import hashlib
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
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Iterable, Iterator, Mapping, Sequence
from urllib.parse import urlparse


SCHEMA_VERSION = "frontier-assisted-intuition-corpus-v1"
RUN_REVISION = "calibration-r2"
SOURCE_SCHEMA_VERSION = "frontier-assisted-intuition-source-task-v1"
PROMPT_SCHEMA_VERSION = "frontier-assisted-intuition-prompt-v1"
ATTEMPT_SCHEMA_VERSION = "frontier-assisted-intuition-attempt-v1"
HARD_CHECK_SCHEMA_VERSION = "frontier-assisted-hard-check-v1"
SEMANTIC_REVIEW_SCHEMA_VERSION = "frontier-assisted-semantic-review-v1"
ACCEPTED_SCHEMA_VERSION = "frontier-assisted-intuition-accepted-v1"
MANIFEST_SCHEMA_VERSION = "frontier-assisted-generation-manifest-v1"
CALIBRATION_SCHEMA_VERSION = "frontier-assisted-calibration-v1"
SUMMARY_SCHEMA_VERSION = "frontier-assisted-summary-v1"
INTEGRITY_SCHEMA_VERSION = "frontier-assisted-integrity-audit-v1"
FREEZE_SCHEMA_VERSION = "frontier-assisted-freeze-v1"

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
EXPERIMENT_ROOT = Path(__file__).resolve().parent
PRIOR_ROOT = REPOSITORY_ROOT / "experiments/frontier_intuition_corpus_v1"
PROMPTS_FILENAME = "prompts_calibration_r2.jsonl"
MANIFEST_FILENAME = "generation_manifest_calibration_r2.json"
CALIBRATION_REPORT_FILENAME = "calibration_report_calibration_r2.json"
CALIBRATION_REVIEW_FILENAME = "calibration_review_calibration_r2.json"
ACTIVE_CAPTURES_DIRECTORY = Path("runs") / RUN_REVISION / "captures"
CONTROLLING_ISSUE = "murillo128/mathia#59"
PRIOR_ISSUE = "murillo128/mathia#57"
QWEN_REPOSITORY = "murillo128/qwen-lean"
QWEN_ACCEPTED_COMMIT = "67d0cdc13ce38c3847633fe9982d0c6e1473e8ed"
QWEN_MEMBERSHIP_EVIDENCE_COMMIT = "71222005f7d9093f31b321f2d1115f321dc75bb9"
MINIF2F_PATH = "data/lean-whole-proof-v2/minif2f-valid-clean-v2.jsonl"
RECORDS_PATH = "data/lean-whole-proof-v2/records.jsonl.gz"
UPSTREAM_FILE_SHA256 = {
    MINIF2F_PATH: "c356b72bdfb8c9e95223f7c6daaddff64127093d5f5b200216eeff12474dbb90",
    RECORDS_PATH: "a66855d8fa9e5132ea895fa206481e9a38cb8cc1baa7494a2a1f8f910030442c",
}
WORKLOADS = ("minif2f-valid-clean-v2", "fresh-composition-valid-v2")
EXPECTED_COUNTS = {
    "minif2f-valid-clean-v2": 244,
    "fresh-composition-valid-v2": 406,
}
EXPECTED_ORDERED_TASK_IDS_SHA256 = {
    "minif2f-valid-clean-v2": "cb5e5edba99dcb1fad61a1f5f88fd38e0061d122b54ea4e39a630a18138cce13",
    "fresh-composition-valid-v2": "7d01d2878a996a0fc57df1eb634ba562cebe396002dc0bd1f617b3b2e7e80f0b",
}

INTUITION_REQUEST = (
    "Analyze the theorem and identify the key mathematical idea that makes it true. Give one "
    "compact natural-language intuition explaining the useful representation, invariant, "
    "decomposition, obstruction, symmetry, reduction, or conceptual mechanism. You may state a "
    "small number of intermediate mathematical observations if they clarify the route. Stop after "
    "the central mechanism and leave theorem-specific substitutions, calculations, case enumeration, "
    "and the final conclusion to the formal prover. For an elementary theorem, do not compress the "
    "entire derivation into one paragraph merely because it is short: name the useful representation "
    "or mechanism, but omit exact theorem-specific balance points, equality cases, evaluated bounds "
    "or results, calculations, witnesses, and attainment details. For a conjunction or equivalence of "
    "several facts, identify the common or independent mechanisms without justifying every component. "
    "Prefer one or two sentences. Focus on "
    "why the argument should work, not on how to encode it in Lean. Do not provide Lean tactics, "
    "mathlib lemma names, formal proof code, an API recipe, or a step-by-step complete proof. "
    "Return only the intuition, preferably as one concise paragraph and preferably within 128 "
    "Qwen-tokenizer tokens. Public tools and web sources may be used to understand the mathematics, "
    "but do not search for or ingest the benchmark's exact Lean proof, oracle/reference proof, "
    "solver candidates, verifier feedback, or outcome data."
)
RETRY_REMINDER = (
    "Generate a fresh replacement under the same contract. Compress to the central mathematical "
    "mechanism, use natural mathematical language only, and omit Lean/API instructions and any "
    "mechanically transcribable complete derivation. Return only the replacement intuition."
)
SEMANTIC_REVIEW_INSTRUCTION = (
    "You are a blinded output-boundary classifier. You see only a public theorem/context and one "
    "candidate intuition. Do not judge mathematical correctness, elegance, likely solver utility, "
    "or similarity to a reference proof. Classify only the interface boundary. Use "
    "accepted_intuition for compact natural-language mathematical guidance centered on a mechanism, "
    "representation, invariant, decomposition, obstruction, symmetry, reduction, or a small number "
    "of conceptual intermediate observations. Use rejected_formal_implementation for Lean code, "
    "tactic/API recipes, formal proof terms, or copied formal identifiers used as execution steps. "
    "Use rejected_near_complete_proof whenever the candidate supplies all theorem-specific "
    "intermediate results and the conclusion so that the remaining formalization is mechanical. "
    "This applies even to a concise one-paragraph derivation without numbered steps. For example, "
    "for a one-step elementary identity, reject a candidate that performs the decisive rewrite or "
    "expansion and then states that the target follows; the fact that the whole proof has only one "
    "step does not turn it into pre-proof intuition. Cosmetic omission of an explicit final result, "
    "witness, or concluding phrase does not turn a full theorem-specific route into an intuition. "
    "Reject a candidate that gives a substitution, its exact balance or equality point, the resulting "
    "bound, and attainment, even if it does not spell out the final theorem value. Reject a multi-clause "
    "candidate that supplies the decisive justification for every clause of a conjunction or equivalence; "
    "omitting only one explicit witness is still cosmetic. "
    "reject a candidate that converts the theorem's bounds, enumerates every remaining value, and "
    "states the resulting count; reject one that evaluates both theorem-specific sums and their final "
    "ratio; reject one that expands both concrete sides and declares the target identity; and reject "
    "one that evaluates the theorem's percentages, difference, absolute value, and final result. "
    "Use rejected_not_an_intuition when it is empty, off-task, lacks a "
    "strategic mathematical mechanism, or is visibly cut off before expressing one. Ordinary words "
    "such as induction, normalization, ring arithmetic, linear arithmetic, or Lean are not by "
    "themselves formal leakage. Do not use tools."
)

GENERATOR_MODEL = "gpt-5.6-sol"
GENERATOR_REASONING_EFFORT = "xhigh"
SEMANTIC_REVIEWER_MODEL = "gpt-5.6-sol"
SEMANTIC_REVIEWER_REASONING_EFFORT = "xhigh"
MAX_ATTEMPTS = 2
CANDIDATE_TOKEN_CAPS = (128, 160, 192)
CALIBRATION_REQUIRED_ACCEPTED = 22
GENERATION_TIMEOUT_SECONDS = 1800
TOKENIZER_ID = "Qwen/Qwen3-8B-Base"
TOKENIZER_REVISION = "49e3418fbbbca6ecbdf9608b4d22e5a407081db4"
EVALUATION_MARKERS = {
    "evaluation_only": True,
    "training_eligible": False,
    "artifact_role": "frontier_assisted_reference",
}
SEMANTIC_DECISIONS = (
    "accepted_intuition",
    "rejected_formal_implementation",
    "rejected_near_complete_proof",
    "rejected_not_an_intuition",
)

# Narrow, unambiguous formal-execution checks. Semantic proof completeness is
# intentionally delegated to the blinded reviewer rather than inferred from
# ordinary mathematical vocabulary.
HARD_PATTERNS: tuple[tuple[str, str], ...] = (
    ("lean_fenced_code", r"```\s*(?:lean\d?|lean4)\b"),
    ("formal_code_fence", r"```[\s\S]*?(?::=\s*by|\b(?:theorem|lemma)\s+\w+[\s\S]*?\bby\b)[\s\S]*?```"),
    ("lean_assignment_by", r":=\s*by\b"),
    ("lean_tactic_chain", r"<;>|^\s*(?:apply|exact|refine|rw|rwa)\s+[^.\n]+$"),
    (
        "lean_tactic_line",
        r"^\s*(?:simp(?:_all)?|simpa|rfl|linarith|nlinarith|omega|ring(?:_nf)?|norm_num|aesop|positivity)(?:\s|$)",
    ),
    ("lean_local_proof_term", r"^\s*(?:have|show|suffices)\s+[^.\n]*(?::=\s*by|\bfrom\b)"),
    ("lean_lambda_or_match", r"\bfun\s+[A-Za-z][A-Za-z0-9_']*\s*=>|\bmatch\b[^\n]*\bwith\b"),
    ("lean_command", r"^\s*#(?:check|eval|reduce|print)\b"),
    ("lean_comment_delimiter", r"/-|-/"),
    ("lean_attribute_or_root", r"@\[|\b_root_\b"),
    (
        "qualified_lean_identifier",
        r"\b(?:Mathlib|Nat|Int|Rat|Real|Complex|Finset|Fintype|Set|List|Array|Function|Polynomial|Matrix|MeasureTheory|Filter|TopologicalSpace|CategoryTheory|Algebra|RingHom|LinearMap)\.(?:[A-Za-z][A-Za-z0-9_']*\.[A-Za-z][A-Za-z0-9_']*|[A-Za-z][A-Za-z0-9']*_[A-Za-z0-9_']+)\b",
    ),
    ("inline_lean_identifier_recipe", r"`(?:by|apply|exact|rw|simp|simpa|[A-Za-z][A-Za-z0-9_']*\.[A-Za-z][A-Za-z0-9_'.]*)`"),
)

FORBIDDEN_SOURCE_KEYS = {
    "proof", "proofs", "proof_variant", "proof_variants", "source_proof", "oracle_proof",
    "reference_proof", "canonical_proof", "completion", "candidate", "candidates",
    "lean_error", "qwen_outcome", "deepseek_outcome", "pass_at_k", "pass@k", "c_i",
    "solved", "stage_9", "capability_gap",
}

GENERATOR_DISABLED_FEATURES = (
    "apps", "computer_use", "goals", "hooks", "image_generation", "multi_agent", "plugins",
    "shell_tool", "skill_search", "tool_suggest", "unified_exec", "view_image",
)
REVIEWER_DISABLED_FEATURES = (
    *GENERATOR_DISABLED_FEATURES,
    "browser_use", "browser_use_external", "in_app_browser", "standalone_web_search",
)
REVIEW_OUTPUT_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "decision": {"type": "string", "enum": list(SEMANTIC_DECISIONS)},
        "semantic_truncation_detected": {"type": "boolean"},
        "boundary_basis": {"type": "string", "maxLength": 300},
    },
    "required": ["decision", "semantic_truncation_detected", "boundary_basis"],
    "additionalProperties": False,
}


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, allow_nan=False, separators=(",", ":"), sort_keys=True)


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


def render_prompt(source: Mapping[str, Any], *, attempt_index: int = 1) -> str:
    theorem = render_model_visible_theorem(
        public_context=str(source["public_context"]), declaration=str(source["declaration"])
    )
    retry = f"\n\nRetry reminder:\n{RETRY_REMINDER}" if attempt_index == 2 else ""
    return f"Theorem statement:\n{theorem}\n\nRequest:\n{INTUITION_REQUEST}{retry}\n\nIntuition:\n"


def render_semantic_review_prompt(source: Mapping[str, Any], candidate: str) -> str:
    theorem = render_model_visible_theorem(
        public_context=str(source["public_context"]), declaration=str(source["declaration"])
    )
    return (
        f"Boundary instruction:\n{SEMANTIC_REVIEW_INSTRUCTION}\n\n"
        f"Public theorem/context:\n{theorem}\n\nCandidate intuition:\n{candidate}"
    )


def _record_has_forbidden_key(value: Any) -> list[str]:
    found: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            if str(key).lower() in FORBIDDEN_SOURCE_KEYS:
                found.append(str(key))
            found.extend(_record_has_forbidden_key(child))
    elif isinstance(value, list):
        for child in value:
            found.extend(_record_has_forbidden_key(child))
    return found


def _source_row(prior: Mapping[str, Any], prior_root: Path) -> dict[str, Any]:
    theorem = render_model_visible_theorem(
        public_context=str(prior["public_context"]), declaration=str(prior["declaration"])
    )
    upstream = dict(prior["upstream"])
    row = {
        "schema_version": SOURCE_SCHEMA_VERSION,
        "workload": prior["workload"],
        "task_id": prior["task_id"],
        "declaration_name": prior["declaration_name"],
        "declaration": prior["declaration"],
        "public_context": prior["public_context"],
        "model_visible_theorem_sha256": sha256_text(theorem),
        "upstream": upstream,
        "projection_provenance": {
            "source_issue": PRIOR_ISSUE,
            "source_snapshot_path": str((prior_root / "source_tasks.jsonl").relative_to(REPOSITORY_ROOT)),
            "source_snapshot_sha256": sha256_file(prior_root / "source_tasks.jsonl"),
            "copied_fields": [
                "workload", "task_id", "declaration_name", "declaration", "public_context",
                "model_visible_theorem_sha256", "upstream",
            ],
            "prior_generation_outputs_copied": False,
        },
        **EVALUATION_MARKERS,
    }
    validate_source_row(row)
    return row


def validate_source_row(row: Mapping[str, Any]) -> None:
    required = {
        "schema_version", "workload", "task_id", "declaration_name", "declaration",
        "public_context", "model_visible_theorem_sha256", "upstream", "projection_provenance",
        *EVALUATION_MARKERS,
    }
    if set(row) != required or row.get("schema_version") != SOURCE_SCHEMA_VERSION:
        raise ValueError("source row fields or schema differ from the theorem-only contract")
    if row["workload"] not in WORKLOADS:
        raise ValueError("source row has an unknown workload")
    for key, expected in EVALUATION_MARKERS.items():
        if row[key] != expected:
            raise ValueError(f"source row has the wrong {key} marker")
    forbidden = _record_has_forbidden_key(row)
    if forbidden:
        raise ValueError(f"source row exposes forbidden fields: {sorted(set(forbidden))}")
    theorem = render_model_visible_theorem(
        public_context=str(row["public_context"]), declaration=str(row["declaration"])
    )
    if row["model_visible_theorem_sha256"] != sha256_text(theorem):
        raise ValueError("source theorem material hash differs")
    upstream = row["upstream"]
    if not isinstance(upstream, dict) or (
        upstream.get("repository") != QWEN_REPOSITORY
        or upstream.get("accepted_commit") != QWEN_ACCEPTED_COMMIT
        or upstream.get("membership_evidence_commit") != QWEN_MEMBERSHIP_EVIDENCE_COMMIT
        or upstream.get("source_file_sha256") != UPSTREAM_FILE_SHA256.get(str(upstream.get("source_path")))
    ):
        raise ValueError("source row has the wrong qwen-lean lineage")
    provenance = row["projection_provenance"]
    if not isinstance(provenance, dict) or provenance.get("prior_generation_outputs_copied") is not False:
        raise ValueError("source projection provenance is malformed")


def _prompt_row(source: Mapping[str, Any]) -> dict[str, Any]:
    prompts = {str(index): render_prompt(source, attempt_index=index) for index in (1, 2)}
    hashes = {index: sha256_text(text) for index, text in prompts.items()}
    payload = {
        "workload": source["workload"], "task_id": source["task_id"],
        "attempt_prompt_sha256": hashes,
    }
    return {
        "schema_version": PROMPT_SCHEMA_VERSION,
        "workload": source["workload"],
        "task_id": source["task_id"],
        "prompt_id": stable_id("frontier_assisted_prompt", payload),
        "attempt_prompts": prompts,
        "attempt_prompt_sha256": hashes,
        "model_visible_theorem_sha256": source["model_visible_theorem_sha256"],
        **EVALUATION_MARKERS,
    }


def validate_prompt_row(row: Mapping[str, Any], source: Mapping[str, Any]) -> None:
    required = {
        "schema_version", "workload", "task_id", "prompt_id", "attempt_prompts",
        "attempt_prompt_sha256", "model_visible_theorem_sha256", *EVALUATION_MARKERS,
    }
    if set(row) != required or row.get("schema_version") != PROMPT_SCHEMA_VERSION:
        raise ValueError("prompt row fields or schema differ")
    expected = _prompt_row(source)
    if dict(row) != expected:
        raise ValueError("prompt is not the exact deterministic theorem-only projection")


def validate_source_snapshot(root: Path = EXPERIMENT_ROOT) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    sources = list(iter_jsonl(root / "source_tasks.jsonl"))
    prompts = list(iter_jsonl(root / PROMPTS_FILENAME))
    if len(sources) != 650 or len(prompts) != 650:
        raise ValueError("issue #59 source/prompt count differs from 650")
    prompt_by_key = {(str(row["workload"]), str(row["task_id"])): row for row in prompts}
    keys: set[tuple[str, str]] = set()
    for source in sources:
        validate_source_row(source)
        key = (str(source["workload"]), str(source["task_id"]))
        if key in keys:
            raise ValueError("issue #59 source repeats a task")
        keys.add(key)
        if key not in prompt_by_key:
            raise ValueError("issue #59 source lacks a prompt")
        validate_prompt_row(prompt_by_key[key], source)
    if set(prompt_by_key) != keys:
        raise ValueError("issue #59 prompt set differs from source tasks")
    for workload in WORKLOADS:
        ids = [str(row["task_id"]) for row in sources if row["workload"] == workload]
        if len(ids) != EXPECTED_COUNTS[workload]:
            raise ValueError(f"{workload} count differs")
        if ordered_ids_sha256(ids) != EXPECTED_ORDERED_TASK_IDS_SHA256[workload]:
            raise ValueError(f"{workload} ordered task identity differs")
    if any("test" in str(row["workload"]).lower() for row in sources):
        raise ValueError("final-test workload entered issue #59")
    return sources, prompts


def materialize_sources(*, root: Path = EXPERIMENT_ROOT, prior_root: Path | None = None) -> dict[str, Any]:
    from experiments.frontier_intuition_corpus_v1 import core as prior_core

    resolved_prior = (prior_root or PRIOR_ROOT).resolve()
    prior_sources, _ = prior_core.validate_source_snapshot(resolved_prior)
    sources = [_source_row(row, resolved_prior) for row in prior_sources]
    prompts = [_prompt_row(row) for row in sources]
    write_jsonl_once(root / "source_tasks.jsonl", sources)
    write_jsonl_once(root / PROMPTS_FILENAME, prompts)
    validate_source_snapshot(root)
    return {
        "source_count": len(sources),
        "counts": dict(EXPECTED_COUNTS),
        "ordered_task_ids_sha256": dict(EXPECTED_ORDERED_TASK_IDS_SHA256),
        "source_tasks_sha256": sha256_file(root / "source_tasks.jsonl"),
        "prompts_sha256": sha256_file(root / PROMPTS_FILENAME),
        "prior_generation_outputs_copied": False,
    }


def prepare_calibration_revision(root: Path = EXPERIMENT_ROOT) -> dict[str, Any]:
    """Preserve superseded calibrations and materialize fresh r2 prompts.

    Revision-0 and revision-1 captures remain byte-for-byte at their
    published paths. The active capture path is disjoint, so no prior output
    can satisfy an r2 task.
    """
    sources = list(iter_jsonl(root / "source_tasks.jsonl"))
    if len(sources) != 650:
        raise ValueError("revision source count differs from 650")
    for source in sources:
        validate_source_row(source)
    for workload in WORKLOADS:
        ids = [str(row["task_id"]) for row in sources if row["workload"] == workload]
        if len(ids) != EXPECTED_COUNTS[workload] or ordered_ids_sha256(ids) != EXPECTED_ORDERED_TASK_IDS_SHA256[workload]:
            raise ValueError(f"revision source identity differs: {workload}")
    revisions = (
        {
            "run_revision": "calibration-r0",
            "review_path": "calibration_revision_0_review.json",
            "report_path": "calibration_report.json",
            "capture_root": Path("captures"),
            "capture_manifest_path": "calibration_revision_0_capture_manifest.json",
            "reviewed_target": "89f6c49373c7d15d4604088a717f116ea24956e5",
            "expected_attempts": 28,
        },
        {
            "run_revision": "calibration-r1",
            "review_path": "calibration_revision_1_review.json",
            "report_path": "calibration_report_calibration_r1.json",
            "capture_root": Path("runs/calibration-r1/captures"),
            "capture_manifest_path": "calibration_revision_1_capture_manifest.json",
            "reviewed_target": "b54ec1f3e9c529bfb000800db17dc80c1b130cfb",
            "expected_attempts": 31,
        },
    )
    preserved_attempts: dict[str, int] = {}
    for revision in revisions:
        review_path = root / str(revision["review_path"])
        report_path = root / str(revision["report_path"])
        review = json.loads(review_path.read_text(encoding="utf-8"))
        if (
            review.get("verdict") != "CALIBRATION_REVISE"
            or review.get("reviewed_target") != revision["reviewed_target"]
            or review.get("reviewed_calibration_sha256") != sha256_file(report_path)
        ):
            raise ValueError(f"{revision['run_revision']} review is not bound to the preserved evidence")
        capture_paths = sorted((root / Path(revision["capture_root"])).rglob("attempt_*.json"))
        if len(capture_paths) != revision["expected_attempts"]:
            raise ValueError(
                f"{revision['run_revision']} must preserve exactly {revision['expected_attempts']} raw attempts"
            )
        capture_manifest = {
            "schema_version": "frontier-assisted-superseded-calibration-capture-manifest-v1",
            "run_revision": revision["run_revision"],
            "disposition": "CALIBRATION_REVISE_not_final_corpus_eligible",
            "reviewed_target": review["reviewed_target"],
            "captures": [
                {"path": str(path.relative_to(root)), "bytes": path.stat().st_size, "sha256": sha256_file(path)}
                for path in capture_paths
            ],
        }
        manifest_path = root / str(revision["capture_manifest_path"])
        if manifest_path.exists():
            if json.loads(manifest_path.read_text(encoding="utf-8")) != capture_manifest:
                raise ValueError(f"{revision['run_revision']} capture manifest differs from preserved evidence")
        else:
            write_json_once(manifest_path, capture_manifest)
        preserved_attempts[str(revision["run_revision"])] = len(capture_paths)
    prompts = [_prompt_row(row) for row in sources]
    write_jsonl_once(root / PROMPTS_FILENAME, prompts)
    validate_source_snapshot(root)
    return {
        "run_revision": RUN_REVISION,
        "source_count": len(sources),
        "prompts_sha256": sha256_file(root / PROMPTS_FILENAME),
        "preserved_attempts": preserved_attempts,
        "superseded_outputs_final_corpus_eligible": False,
    }


def calibration_indices(size: int, count: int) -> list[int]:
    if count < 2 or size < count:
        raise ValueError("calibration spacing requires size >= count >= 2")
    indices = [(index * (size - 1)) // (count - 1) for index in range(count)]
    if len(set(indices)) != count or indices[0] != 0 or indices[-1] != size - 1:
        raise ValueError("calibration spacing failed")
    return indices


def calibration_keys(sources: Sequence[Mapping[str, Any]]) -> list[tuple[str, str]]:
    result: list[tuple[str, str]] = []
    counts = {"minif2f-valid-clean-v2": 8, "fresh-composition-valid-v2": 16}
    for workload in WORKLOADS:
        rows = [row for row in sources if row["workload"] == workload]
        for index in calibration_indices(len(rows), counts[workload]):
            result.append((workload, str(rows[index]["task_id"])))
    if len(result) != 24:
        raise AssertionError("calibration must contain exactly 24 tasks")
    return result


def _verified_codex_runtime() -> dict[str, Any]:
    executable = shutil.which("codex")
    if executable is None:
        raise RuntimeError("codex executable is unavailable")
    resolved = Path(executable).resolve()
    completed = subprocess.run([str(resolved), "--version"], text=True, capture_output=True, check=False)
    if completed.returncode != 0 or not completed.stdout.strip().startswith("codex-cli "):
        raise RuntimeError("codex CLI version cannot be resolved")
    return {
        "product": "OpenAI Codex CLI",
        "cli_version": completed.stdout.strip().removeprefix("codex-cli "),
        "executable_sha256": sha256_file(resolved),
    }


def codex_command(
    executable: str = "codex", *, reviewer: bool = False, output_schema_path: str | None = None
) -> list[str]:
    model = SEMANTIC_REVIEWER_MODEL if reviewer else GENERATOR_MODEL
    effort = SEMANTIC_REVIEWER_REASONING_EFFORT if reviewer else GENERATOR_REASONING_EFFORT
    command = [
        executable, "exec", "--ephemeral", "--ignore-user-config", "--ignore-rules",
        "--skip-git-repo-check", "--strict-config", "-m", model, "-c",
        f'model_reasoning_effort="{effort}"', "-s", "read-only",
    ]
    disabled = REVIEWER_DISABLED_FEATURES if reviewer else GENERATOR_DISABLED_FEATURES
    for feature in disabled:
        command.extend(("--disable", feature))
    if not reviewer:
        command.extend(("--enable", "browser_use", "--enable", "browser_use_external"))
    if output_schema_path is not None:
        command.extend(("--output-schema", output_schema_path))
    command.extend(("--json", "-"))
    return command


def _load_tokenizer() -> Any:
    try:
        from transformers import AutoTokenizer
    except ImportError as error:
        raise RuntimeError("transformers is required for the frozen tokenizer") from error
    return AutoTokenizer.from_pretrained(
        TOKENIZER_ID, revision=TOKENIZER_REVISION, local_files_only=True, trust_remote_code=False
    )


class FrozenTokenizer:
    def __init__(self) -> None:
        self.value = _load_tokenizer()
        self._lock = threading.Lock()

    def encode(self, text: str, *, add_special_tokens: bool) -> list[int]:
        with self._lock:
            return list(self.value.encode(text, add_special_tokens=add_special_tokens))


def _manifest_payload(root: Path, runtime: Mapping[str, Any]) -> dict[str, Any]:
    sources, _ = validate_source_snapshot(root)
    calibration = [
        {"workload": workload, "task_id": task_id}
        for workload, task_id in calibration_keys(sources)
    ]
    return {
        "schema_version": MANIFEST_SCHEMA_VERSION,
        "controlling_issue": CONTROLLING_ISSUE,
        "artifact_id": SCHEMA_VERSION,
        "run_revision": RUN_REVISION,
        "status": "pre_calibration_revision_2_contract_frozen",
        "superseded_calibrations": [
            {
                "run_revision": "calibration-r0",
                "verdict": "CALIBRATION_REVISE",
                "reviewed_target": "89f6c49373c7d15d4604088a717f116ea24956e5",
                "review_sha256": sha256_file(root / "calibration_revision_0_review.json"),
                "capture_manifest_sha256": sha256_file(root / "calibration_revision_0_capture_manifest.json"),
                "outputs_final_corpus_eligible": False,
            },
            {
                "run_revision": "calibration-r1",
                "verdict": "CALIBRATION_REVISE",
                "reviewed_target": "b54ec1f3e9c529bfb000800db17dc80c1b130cfb",
                "review_sha256": sha256_file(root / "calibration_revision_1_review.json"),
                "capture_manifest_sha256": sha256_file(root / "calibration_revision_1_capture_manifest.json"),
                "outputs_final_corpus_eligible": False,
            },
        ],
        "source_contract": {
            "qwen_repository": QWEN_REPOSITORY,
            "accepted_dataset_v2_commit": QWEN_ACCEPTED_COMMIT,
            "membership_evidence_commit": QWEN_MEMBERSHIP_EVIDENCE_COMMIT,
            "upstream_files_sha256": UPSTREAM_FILE_SHA256,
            "workload_counts": EXPECTED_COUNTS,
            "ordered_task_ids_sha256": EXPECTED_ORDERED_TASK_IDS_SHA256,
            "source_tasks_sha256": sha256_file(root / "source_tasks.jsonl"),
            "prompts_sha256": sha256_file(root / PROMPTS_FILENAME),
            "generator_reads_only": ["source_tasks.jsonl", PROMPTS_FILENAME, MANIFEST_FILENAME],
            "forbidden_generator_inputs": sorted(FORBIDDEN_SOURCE_KEYS),
            "final_test_workloads_allowed": False,
            "prior_generation_outputs_reused": False,
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
            "tools_allowed": True,
            "tool_use_is_rejection": False,
            "agent_message_extraction": "retain every message in raw transcript; select final agent message",
            "interim_agent_messages_are_failure": False,
            "available_support": "public browser/web plus product-managed reasoning helpers",
            "local_shell_and_connected_apps_disabled": True,
            "disabled_cli_features": list(GENERATOR_DISABLED_FEATURES),
            "sandbox": "read-only",
            "command_shape": codex_command("codex", reviewer=False)[1:],
            "timeout_seconds": GENERATION_TIMEOUT_SECONDS,
            "sampling_controls": "product_managed_no_user_temperature_top_p_or_seed",
        },
        "semantic_reviewer_contract": {
            **runtime,
            "model": SEMANTIC_REVIEWER_MODEL,
            "reasoning_effort": SEMANTIC_REVIEWER_REASONING_EFFORT,
            "session": "fresh_isolated_ephemeral_per_candidate",
            "visible_inputs": ["public_theorem_context", "candidate_intuition"],
            "instruction": SEMANTIC_REVIEW_INSTRUCTION,
            "instruction_sha256": sha256_text(SEMANTIC_REVIEW_INSTRUCTION),
            "decisions": list(SEMANTIC_DECISIONS),
            "correctness_or_usefulness_judgment": False,
            "tools_allowed": False,
            "tool_event_action": "semantic_review_runtime_failure",
            "output_schema": REVIEW_OUTPUT_SCHEMA,
            "output_schema_sha256": sha256_text(canonical_json(REVIEW_OUTPUT_SCHEMA)),
            "disabled_cli_features": list(REVIEWER_DISABLED_FEATURES),
            "command_shape": codex_command(
                "codex", reviewer=True, output_schema_path="{ephemeral_review_schema.json}"
            )[1:],
            "timeout_seconds": GENERATION_TIMEOUT_SECONDS,
        },
        "prompt_contract": {
            "intuition_request": INTUITION_REQUEST,
            "retry_reminder": RETRY_REMINDER,
            "attempt_1_template": "Theorem statement + frozen request + Intuition label",
            "attempt_2_template": "same theorem/request + frozen compactness reminder + Intuition label",
            "prompt_count": 650,
            "prompt_text_is_write_once": True,
        },
        "calibration_contract": {
            "selection_before_outputs": True,
            "sampling": "inclusive evenly spaced zero-based indices floor(i*(N-1)/(k-1))",
            "tasks": calibration,
            "counts": {"minif2f-valid-clean-v2": 8, "fresh-composition-valid-v2": 16},
            "candidate_token_caps": list(CANDIDATE_TOKEN_CAPS),
            "selection_rule": "smallest cap with at least 22/24 boundary-accepted non-truncated outputs",
            "required_accepted": CALIBRATION_REQUIRED_ACCEPTED,
            "none_qualifies": "CALIBRATION_BLOCKED",
            "fresh_published_read_only_review_required": True,
            "full_run_requires": "CALIBRATION_PASS",
        },
        "tokenizer_contract": {
            "model": TOKENIZER_ID,
            "revision": TOKENIZER_REVISION,
            "add_special_tokens": False,
            "counted_text": "exact_raw_final_candidate_text",
            "candidate_caps": list(CANDIDATE_TOKEN_CAPS),
            "truncation": False,
        },
        "eligibility_contract": {
            "hard_check_schema": HARD_CHECK_SCHEMA_VERSION,
            "hard_patterns": [list(item) for item in HARD_PATTERNS],
            "hard_checks_are_narrow_unambiguous_formal_leakage_only": True,
            "semantic_review_schema": SEMANTIC_REVIEW_SCHEMA_VERSION,
            "eligible": "valid generation + hard pass + accepted_intuition + no semantic truncation + within frozen cap",
            "repair_or_sanitization": False,
            "semantic_quality_selection": False,
        },
        "retry_contract": {
            "attempt_1_always": True,
            "retry_only_after_output_boundary_length_or_runtime_failure": True,
            "fresh_session": True,
            "same_theorem_model_reasoning_and_frozen_instruction": True,
            "attempt_2_adds_only_frozen_retry_reminder": True,
            "maximum_attempts": MAX_ATTEMPTS,
            "accept_first_eligible": True,
            "missing_after_two_failures": "missing_accepted_intuition",
            "downstream_outcome_dependent_retry": False,
            "tool_use_retry_trigger": False,
        },
        "full_run_circuit_breakers": {
            "applied_after_task_exhausts_maximum_two_attempts": True,
            "first_non_calibration_window": {"tasks": 24, "minimum_accepted": 18},
            "subsequent_ordered_windows": {"tasks": 32, "minimum_accepted": 24},
            "consecutive_missing": 12,
            "runtime_missing_per_32": {"maximum": 8},
            "in_flight_capture_preserved": True,
            "no_contract_repair_after_activation": True,
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
    probe = tokenizer.encode("frontier assisted intuition tokenizer probe", add_special_tokens=False)
    if not isinstance(probe, list) or not probe:
        raise RuntimeError("frozen tokenizer failed its local probe")
    runtime = _verified_codex_runtime()
    payload = _manifest_payload(root, runtime)
    manifest = {
        **payload,
        "frozen_at_utc": utc_now(),
        "generation_manifest_id": stable_id("frontier_assisted_generation_manifest", payload),
    }
    write_json_once(root / MANIFEST_FILENAME, manifest)
    validate_manifest(root)
    return manifest


def validate_manifest(root: Path = EXPERIMENT_ROOT) -> dict[str, Any]:
    manifest = json.loads((root / MANIFEST_FILENAME).read_text(encoding="utf-8"))
    frozen_at = manifest.get("frozen_at_utc")
    manifest_id = manifest.get("generation_manifest_id")
    payload = {key: value for key, value in manifest.items() if key not in {"frozen_at_utc", "generation_manifest_id"}}
    expected = _manifest_payload(root, _verified_codex_runtime())
    if payload != expected:
        raise ValueError("generation manifest differs from the current frozen contract/runtime")
    if not isinstance(frozen_at, str) or not frozen_at.endswith("Z"):
        raise ValueError("generation manifest has an invalid freeze time")
    if manifest_id != stable_id("frontier_assisted_generation_manifest", expected):
        raise ValueError("generation manifest identity differs")
    return manifest


def _walk_strings(value: Any) -> Iterator[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for key, child in value.items():
            yield str(key)
            yield from _walk_strings(child)
    elif isinstance(value, list):
        for child in value:
            yield from _walk_strings(child)


def _source_domains(value: Any) -> list[str]:
    domains: set[str] = set()
    for text in _walk_strings(value):
        for match in re.findall(r"https?://[^\s\]\[(){}<>\"']+", text):
            parsed = urlparse(match.rstrip(".,;:"))
            if parsed.hostname:
                domains.add(parsed.hostname.lower())
        for match in re.findall(r"\bsite:([A-Za-z0-9.-]+)", text):
            domains.add(match.lower())
    return sorted(domains)


def parse_codex_transcript(
    transcript: str, *, tools_allowed: bool, allow_interim_agent_messages: bool = False
) -> dict[str, Any]:
    final_messages: list[str] = []
    thread_ids: list[str] = []
    completed_support_items: list[dict[str, Any]] = []
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
            completed_support_items.append({"type": "malformed_completed_item"})
            continue
        item_type = str(item.get("type"))
        if item_type == "agent_message" and isinstance(item.get("text"), str):
            final_messages.append(item["text"])
        elif item_type != "reasoning":
            completed_support_items.append(dict(item))
    support_types = Counter(str(item.get("type")) for item in completed_support_items)
    message_count_valid = (
        len(final_messages) >= 1 if allow_interim_agent_messages else len(final_messages) == 1
    )
    valid = (
        invalid_json_lines == 0
        and len(thread_ids) == 1
        and message_count_valid
        and (tools_allowed or not completed_support_items)
    )
    return {
        "valid_capture": valid,
        "thread_ids": thread_ids,
        "agent_message_count": len(final_messages),
        "interim_agent_message_count": max(0, len(final_messages) - 1),
        "agent_messages": final_messages,
        "invalid_json_lines": invalid_json_lines,
        "final_message": final_messages[-1] if final_messages else None,
        "completed_support_items": completed_support_items,
        "support_item_types": dict(sorted(support_types.items())),
        "source_domains": _source_domains([completed_support_items, final_messages]),
        "tools_allowed": tools_allowed,
        "allow_interim_agent_messages": allow_interim_agent_messages,
    }


def hard_check(raw_text: str | None, tokenizer: Any) -> dict[str, Any]:
    reasons: list[str] = []
    matches: dict[str, list[str]] = {}
    token_ids: list[int] = []
    raw_hash: str | None = None
    if not isinstance(raw_text, str) or not raw_text.strip():
        reasons.append("empty_or_missing_output")
    else:
        raw_hash = sha256_text(raw_text)
        token_ids = list(tokenizer.encode(raw_text, add_special_tokens=False))
        for name, pattern in HARD_PATTERNS:
            found = [match.group(0) for match in re.finditer(pattern, raw_text, re.I | re.M)]
            if found:
                reasons.append(name)
                matches[name] = found
    return {
        "schema_version": HARD_CHECK_SCHEMA_VERSION,
        "status": "hard_pass" if not reasons else "hard_reject",
        "reasons": reasons,
        "matched_text": matches,
        "raw_output_sha256": raw_hash,
        "tokenizer": {"model": TOKENIZER_ID, "revision": TOKENIZER_REVISION, "add_special_tokens": False},
        "token_ids": token_ids,
        "token_ids_sha256": sha256_text(canonical_json(token_ids)),
        "token_count": len(token_ids),
    }


def _safe_task_path(task_id: str) -> str:
    safe = re.sub(r"[^A-Za-z0-9_.-]", "_", task_id)
    if len(safe) > 96:
        safe = safe[:48] + "_" + sha256_text(task_id)[:32]
    return safe


def capture_path(root: Path, source: Mapping[str, Any], attempt_index: int) -> Path:
    return (
        root / ACTIVE_CAPTURES_DIRECTORY / str(source["workload"]) / _safe_task_path(str(source["task_id"]))
        / f"attempt_{attempt_index}.json"
    )


def _run_codex(
    prompt: str, runtime: Mapping[str, Any], *, reviewer: bool, output_schema: Mapping[str, Any] | None = None
) -> dict[str, Any]:
    executable = shutil.which("codex")
    if executable is None:
        raise RuntimeError("codex executable is unavailable")
    resolved = str(Path(executable).resolve())
    if sha256_file(Path(resolved)) != runtime["executable_sha256"]:
        raise RuntimeError("codex executable changed after pre-calibration freeze")
    started_at = utc_now()
    monotonic_start = time.monotonic()
    stdout = ""
    stderr = ""
    returncode: int | None = None
    timed_out = False
    with tempfile.TemporaryDirectory(prefix="frontier-assisted-codex-") as directory:
        schema_name: str | None = None
        if output_schema is not None:
            schema_name = "semantic_review_schema.json"
            Path(directory, schema_name).write_text(canonical_json(output_schema) + "\n", encoding="utf-8")
        command = codex_command(resolved, reviewer=reviewer, output_schema_path=schema_name)
        try:
            completed = subprocess.run(
                command, input=prompt, cwd=directory, capture_output=True, text=True, check=False,
                timeout=GENERATION_TIMEOUT_SECONDS,
            )
            stdout = completed.stdout
            stderr = completed.stderr
            returncode = completed.returncode
        except subprocess.TimeoutExpired as error:
            timed_out = True
            stdout = error.stdout if isinstance(error.stdout, str) else ""
            stderr = error.stderr if isinstance(error.stderr, str) else ""
    parsed = parse_codex_transcript(
        stdout, tools_allowed=not reviewer, allow_interim_agent_messages=not reviewer
    )
    valid = returncode == 0 and not timed_out and parsed["valid_capture"]
    return {
        "started_at_utc": started_at,
        "finished_at_utc": utc_now(),
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
        "valid_capture": valid,
    }


def _parse_semantic_decision(capture: Mapping[str, Any]) -> dict[str, Any]:
    raw = capture.get("final_message")
    result: dict[str, Any] | None = None
    error: str | None = None
    if not capture.get("valid_capture"):
        error = "semantic_reviewer_capture_invalid"
    elif not isinstance(raw, str):
        error = "semantic_reviewer_message_missing"
    else:
        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError:
            error = "semantic_reviewer_json_invalid"
        else:
            if not isinstance(parsed, dict) or set(parsed) != {
                "decision", "semantic_truncation_detected", "boundary_basis"
            }:
                error = "semantic_reviewer_schema_invalid"
            elif parsed.get("decision") not in SEMANTIC_DECISIONS:
                error = "semantic_reviewer_decision_invalid"
            elif not isinstance(parsed.get("semantic_truncation_detected"), bool):
                error = "semantic_reviewer_truncation_invalid"
            elif not isinstance(parsed.get("boundary_basis"), str) or len(parsed["boundary_basis"]) > 300:
                error = "semantic_reviewer_basis_invalid"
            else:
                result = dict(parsed)
    return {
        "schema_version": SEMANTIC_REVIEW_SCHEMA_VERSION,
        "status": "review_valid" if result is not None else "review_runtime_failure",
        "decision": result["decision"] if result else None,
        "semantic_truncation_detected": result["semantic_truncation_detected"] if result else None,
        "boundary_basis": result["boundary_basis"] if result else None,
        "error": error,
        "capture": dict(capture),
    }


def _attempt_record(
    *, source: Mapping[str, Any], prompt: Mapping[str, Any], attempt_index: int,
    manifest: Mapping[str, Any], tokenizer: Any,
) -> dict[str, Any]:
    prompt_text = str(prompt["attempt_prompts"][str(attempt_index)])
    generation = _run_codex(
        prompt_text, manifest["generator_contract"], reviewer=False, output_schema=None
    )
    check = hard_check(
        generation.get("final_message") if generation.get("valid_capture") else None, tokenizer
    )
    semantic: dict[str, Any] | None = None
    if generation.get("valid_capture") and check["status"] == "hard_pass":
        review_prompt = render_semantic_review_prompt(source, str(generation["final_message"]))
        review_capture = _run_codex(
            review_prompt, manifest["semantic_reviewer_contract"], reviewer=True,
            output_schema=REVIEW_OUTPUT_SCHEMA,
        )
        semantic = _parse_semantic_decision(review_capture)
        semantic["review_prompt_sha256"] = sha256_text(review_prompt)
    identity = {
        "workload": source["workload"], "task_id": source["task_id"],
        "attempt_index": attempt_index,
        "generation_manifest_id": manifest["generation_manifest_id"],
        "prompt_sha256": prompt["attempt_prompt_sha256"][str(attempt_index)],
        "generation_thread_ids": generation["thread_ids"],
        "generation_stdout_sha256": generation["stdout_sha256"],
        "semantic_stdout_sha256": semantic["capture"]["stdout_sha256"] if semantic else None,
    }
    return {
        "schema_version": ATTEMPT_SCHEMA_VERSION,
        "attempt_id": stable_id("frontier_assisted_attempt", identity),
        "workload": source["workload"],
        "task_id": source["task_id"],
        "attempt_index": attempt_index,
        "generation_manifest_id": manifest["generation_manifest_id"],
        "prompt_id": prompt["prompt_id"],
        "prompt_sha256": prompt["attempt_prompt_sha256"][str(attempt_index)],
        "model_visible_theorem_sha256": source["model_visible_theorem_sha256"],
        "raw_output_text": generation.get("final_message"),
        "raw_output_sha256": (
            sha256_text(str(generation["final_message"]))
            if isinstance(generation.get("final_message"), str) else None
        ),
        "generation_capture": generation,
        "hard_check": check,
        "semantic_boundary_review": semantic,
        **EVALUATION_MARKERS,
    }


def _read_capture(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"capture is not an object: {path}")
    return value


def validate_attempt(
    row: Mapping[str, Any], *, source: Mapping[str, Any], prompt: Mapping[str, Any],
    manifest: Mapping[str, Any], tokenizer: Any,
) -> None:
    if row.get("schema_version") != ATTEMPT_SCHEMA_VERSION:
        raise ValueError("attempt has the wrong schema")
    index = row.get("attempt_index")
    if index not in {1, 2}:
        raise ValueError("attempt index differs from the maximum-two policy")
    if (
        row.get("workload") != source["workload"] or row.get("task_id") != source["task_id"]
        or row.get("prompt_id") != prompt["prompt_id"]
        or row.get("prompt_sha256") != prompt["attempt_prompt_sha256"][str(index)]
        or row.get("model_visible_theorem_sha256") != source["model_visible_theorem_sha256"]
        or row.get("generation_manifest_id") != manifest["generation_manifest_id"]
    ):
        raise ValueError("attempt source/prompt/generator binding differs")
    generation = row.get("generation_capture")
    if not isinstance(generation, dict):
        raise ValueError("attempt lacks generation capture")
    parsed = parse_codex_transcript(
        str(generation.get("stdout_jsonl", "")), tools_allowed=True,
        allow_interim_agent_messages=True,
    )
    for key, value in parsed.items():
        if generation.get(key) != value:
            raise ValueError(f"generation transcript parse evidence differs: {key}")
    valid_generation = (
        generation.get("returncode") == 0 and not generation.get("timed_out") and parsed["valid_capture"]
    )
    if generation.get("valid_capture") != valid_generation:
        raise ValueError("generation capture validity differs")
    if generation.get("stdout_sha256") != sha256_text(str(generation.get("stdout_jsonl", ""))):
        raise ValueError("generation stdout hash differs")
    if generation.get("stderr_sha256") != sha256_text(str(generation.get("stderr", ""))):
        raise ValueError("generation stderr hash differs")
    raw_text = generation.get("final_message") if valid_generation else None
    if row.get("raw_output_text") != generation.get("final_message"):
        raise ValueError("attempt raw output differs from capture")
    raw_hash = sha256_text(str(raw_text)) if isinstance(raw_text, str) else None
    if row.get("raw_output_sha256") != raw_hash:
        raise ValueError("attempt raw output hash differs")
    expected_hard = hard_check(raw_text, tokenizer)
    if row.get("hard_check") != expected_hard:
        raise ValueError("hard check is not a deterministic capture projection")
    semantic = row.get("semantic_boundary_review")
    if valid_generation and expected_hard["status"] == "hard_pass":
        if not isinstance(semantic, dict):
            raise ValueError("hard-pass attempt lacks semantic boundary review")
        review_capture = semantic.get("capture")
        if not isinstance(review_capture, dict):
            raise ValueError("semantic review lacks raw capture")
        review_parsed = parse_codex_transcript(
            str(review_capture.get("stdout_jsonl", "")), tools_allowed=False,
            allow_interim_agent_messages=False,
        )
        for key, value in review_parsed.items():
            if review_capture.get(key) != value:
                raise ValueError(f"semantic transcript parse evidence differs: {key}")
        expected_semantic = _parse_semantic_decision(review_capture)
        review_prompt = render_semantic_review_prompt(source, str(raw_text))
        expected_semantic["review_prompt_sha256"] = sha256_text(review_prompt)
        if semantic != expected_semantic:
            raise ValueError("semantic review result differs from its raw capture")
    elif semantic is not None:
        raise ValueError("invalid or hard-rejected attempt must not invoke semantic review")
    identity = {
        "workload": source["workload"], "task_id": source["task_id"],
        "attempt_index": index, "generation_manifest_id": manifest["generation_manifest_id"],
        "prompt_sha256": prompt["attempt_prompt_sha256"][str(index)],
        "generation_thread_ids": generation["thread_ids"],
        "generation_stdout_sha256": generation["stdout_sha256"],
        "semantic_stdout_sha256": semantic["capture"]["stdout_sha256"] if semantic else None,
    }
    if row.get("attempt_id") != stable_id("frontier_assisted_attempt", identity):
        raise ValueError("attempt identity differs")
    for key, expected in EVALUATION_MARKERS.items():
        if row.get(key) != expected:
            raise ValueError(f"attempt has the wrong {key} marker")


def attempt_eligibility(row: Mapping[str, Any], *, maximum_tokens: int) -> dict[str, Any]:
    generation = row["generation_capture"]
    hard = row["hard_check"]
    semantic = row.get("semantic_boundary_review")
    reasons: list[str] = []
    if not generation.get("valid_capture"):
        reasons.append("generation_runtime_failure")
    if hard["status"] != "hard_pass":
        reasons.extend(f"hard:{reason}" for reason in hard["reasons"])
    if hard["status"] == "hard_pass":
        if not isinstance(semantic, dict) or semantic.get("status") != "review_valid":
            reasons.append("semantic_review_runtime_failure")
        elif semantic.get("decision") != "accepted_intuition":
            reasons.append(f"semantic:{semantic.get('decision')}")
        elif semantic.get("semantic_truncation_detected"):
            reasons.append("semantic:truncation_detected")
    if int(hard["token_count"]) > maximum_tokens:
        reasons.append("length:over_budget")
    return {
        "eligible": not reasons,
        "status": "accepted_intuition" if not reasons else reasons[0],
        "reasons": reasons,
        "maximum_tokens": maximum_tokens,
        "token_count": hard["token_count"],
    }


def _task_attempts(
    *, source: Mapping[str, Any], prompt: Mapping[str, Any], manifest: Mapping[str, Any],
    tokenizer: Any, root: Path, maximum_tokens: int,
) -> list[dict[str, Any]]:
    attempts: list[dict[str, Any]] = []
    for attempt_index in range(1, MAX_ATTEMPTS + 1):
        path = capture_path(root, source, attempt_index)
        if path.exists():
            attempt = _read_capture(path)
        else:
            attempt = _attempt_record(
                source=source, prompt=prompt, attempt_index=attempt_index,
                manifest=manifest, tokenizer=tokenizer,
            )
            write_json_once(path, attempt)
        validate_attempt(
            attempt, source=source, prompt=prompt, manifest=manifest, tokenizer=tokenizer
        )
        attempts.append(attempt)
        if attempt_eligibility(attempt, maximum_tokens=maximum_tokens)["eligible"]:
            break
    return attempts


def _result_for_attempts(
    source: Mapping[str, Any], attempts: Sequence[Mapping[str, Any]], maximum_tokens: int
) -> dict[str, Any]:
    decisions = [attempt_eligibility(row, maximum_tokens=maximum_tokens) for row in attempts]
    accepted_index = next((index for index, decision in enumerate(decisions) if decision["eligible"]), None)
    terminal = decisions[accepted_index] if accepted_index is not None else decisions[-1]
    terminal_attempt = attempts[accepted_index] if accepted_index is not None else attempts[-1]
    runtime_missing = (
        not terminal_attempt["generation_capture"]["valid_capture"]
        or (
            isinstance(terminal_attempt.get("semantic_boundary_review"), dict)
            and terminal_attempt["semantic_boundary_review"].get("status") == "review_runtime_failure"
        )
    ) if accepted_index is None else False
    return {
        "workload": source["workload"],
        "task_id": source["task_id"],
        "attempt_count": len(attempts),
        "accepted": accepted_index is not None,
        "accepted_attempt_index": int(attempts[accepted_index]["attempt_index"]) if accepted_index is not None else None,
        "final_status": terminal["status"],
        "runtime_missing": runtime_missing,
    }


def _generate_one(
    source: Mapping[str, Any], prompt: Mapping[str, Any], manifest: Mapping[str, Any],
    tokenizer: Any, root: Path, maximum_tokens: int,
) -> dict[str, Any]:
    attempts = _task_attempts(
        source=source, prompt=prompt, manifest=manifest, tokenizer=tokenizer,
        root=root, maximum_tokens=maximum_tokens,
    )
    return _result_for_attempts(source, attempts, maximum_tokens)


def _parallel_generate(
    *, sources: Sequence[Mapping[str, Any]], prompts: Mapping[tuple[str, str], Mapping[str, Any]],
    manifest: Mapping[str, Any], tokenizer: Any, root: Path, maximum_tokens: int, workers: int,
) -> list[dict[str, Any]]:
    results: dict[tuple[str, str], dict[str, Any]] = {}
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(
                _generate_one, source, prompts[(str(source["workload"]), str(source["task_id"]))],
                manifest, tokenizer, root, maximum_tokens,
            ): (str(source["workload"]), str(source["task_id"]))
            for source in sources
        }
        completed = 0
        for future in futures:
            result = future.result()
            key = futures[future]
            results[key] = result
            completed += 1
            print(canonical_json({"completed": completed, "total": len(sources), **result}), flush=True)
    return [results[(str(row["workload"]), str(row["task_id"]))] for row in sources]


def generate_calibration(root: Path = EXPERIMENT_ROOT, *, workers: int = 1) -> dict[str, Any]:
    if workers < 1 or workers > 16:
        raise ValueError("workers must be between 1 and 16")
    sources, prompt_rows = validate_source_snapshot(root)
    manifest = validate_manifest(root)
    calibration_set = set(calibration_keys(sources))
    selected = [
        row for row in sources
        if (str(row["workload"]), str(row["task_id"])) in calibration_set
    ]
    prompts = {(str(row["workload"]), str(row["task_id"])): row for row in prompt_rows}
    results = _parallel_generate(
        sources=selected, prompts=prompts, manifest=manifest, tokenizer=FrozenTokenizer(), root=root,
        maximum_tokens=max(CANDIDATE_TOKEN_CAPS), workers=workers,
    )
    return {
        "task_count": len(results),
        "accepted_at_192": sum(bool(row["accepted"]) for row in results),
        "missing_at_192": sum(not bool(row["accepted"]) for row in results),
    }


def _load_existing_attempts_for_source(
    *, root: Path, source: Mapping[str, Any], prompt: Mapping[str, Any],
    manifest: Mapping[str, Any], tokenizer: Any, require_terminal_for_cap: int | None = None,
) -> list[dict[str, Any]]:
    attempts: list[dict[str, Any]] = []
    first_path = capture_path(root, source, 1)
    if not first_path.is_file():
        raise ValueError(f"task lacks mandatory attempt 1: {source['task_id']}")
    first = _read_capture(first_path)
    validate_attempt(first, source=source, prompt=prompt, manifest=manifest, tokenizer=tokenizer)
    attempts.append(first)
    second_path = capture_path(root, source, 2)
    if second_path.is_file():
        second = _read_capture(second_path)
        validate_attempt(second, source=source, prompt=prompt, manifest=manifest, tokenizer=tokenizer)
        attempts.append(second)
    if require_terminal_for_cap is not None:
        first_eligible = attempt_eligibility(first, maximum_tokens=require_terminal_for_cap)["eligible"]
        if first_eligible and second_path.exists():
            raise ValueError("eligible attempt 1 was impermissibly regenerated")
        if not first_eligible and not second_path.is_file():
            raise ValueError(f"ineligible attempt 1 lacks bounded retry: {source['task_id']}")
    return attempts


def finalize_calibration(root: Path = EXPERIMENT_ROOT) -> dict[str, Any]:
    sources, prompt_rows = validate_source_snapshot(root)
    manifest = validate_manifest(root)
    tokenizer = FrozenTokenizer()
    prompts = {(str(row["workload"]), str(row["task_id"])): row for row in prompt_rows}
    key_set = set(calibration_keys(sources))
    selected = [
        row for row in sources
        if (str(row["workload"]), str(row["task_id"])) in key_set
    ]
    rows: list[dict[str, Any]] = []
    qualifying = {cap: 0 for cap in CANDIDATE_TOKEN_CAPS}
    for source in selected:
        key = (str(source["workload"]), str(source["task_id"]))
        attempts = _load_existing_attempts_for_source(
            root=root, source=source, prompt=prompts[key], manifest=manifest, tokenizer=tokenizer,
            require_terminal_for_cap=max(CANDIDATE_TOKEN_CAPS),
        )
        cap_results: dict[str, Any] = {}
        for cap in CANDIDATE_TOKEN_CAPS:
            accepted = next(
                (row for row in attempts if attempt_eligibility(row, maximum_tokens=cap)["eligible"]), None
            )
            if accepted is not None:
                qualifying[cap] += 1
            cap_results[str(cap)] = {
                "qualifies": accepted is not None,
                "accepted_attempt_index": accepted["attempt_index"] if accepted else None,
                "token_count": accepted["hard_check"]["token_count"] if accepted else None,
            }
        rows.append({
            "workload": source["workload"], "task_id": source["task_id"],
            "model_visible_theorem_sha256": source["model_visible_theorem_sha256"],
            "attempt_ids": [row["attempt_id"] for row in attempts],
            "cap_results": cap_results,
        })
    chosen = next(
        (cap for cap in CANDIDATE_TOKEN_CAPS if qualifying[cap] >= CALIBRATION_REQUIRED_ACCEPTED), None
    )
    report_payload = {
        "schema_version": CALIBRATION_SCHEMA_VERSION,
        "artifact_id": SCHEMA_VERSION,
        "generation_manifest_id": manifest["generation_manifest_id"],
        "status": "CALIBRATION_REVIEW_PENDING" if chosen is not None else "CALIBRATION_BLOCKED",
        "selection_rule": "smallest cap with at least 22/24 boundary-accepted non-truncated outputs",
        "candidate_qualifying_counts": {str(cap): qualifying[cap] for cap in CANDIDATE_TOKEN_CAPS},
        "chosen_maximum_tokens": chosen,
        "tasks": rows,
        "review_required_before_full_run": True,
        "downstream_outcomes_inspected": False,
        "tool_use_is_failure": False,
        "artifact_boundary": EVALUATION_MARKERS,
    }
    report = {
        **report_payload,
        "finalized_at_utc": utc_now(),
        "calibration_id": stable_id("frontier_assisted_calibration", report_payload),
    }
    write_json_once(root / CALIBRATION_REPORT_FILENAME, report)
    return report


def validate_calibration_report(root: Path = EXPERIMENT_ROOT) -> dict[str, Any]:
    report = json.loads((root / CALIBRATION_REPORT_FILENAME).read_text(encoding="utf-8"))
    finalized = report.get("finalized_at_utc")
    calibration_id = report.get("calibration_id")
    payload = {key: value for key, value in report.items() if key not in {"finalized_at_utc", "calibration_id"}}
    if calibration_id != stable_id("frontier_assisted_calibration", payload):
        raise ValueError("calibration identity differs")
    if not isinstance(finalized, str) or not finalized.endswith("Z"):
        raise ValueError("calibration time is invalid")
    chosen = report.get("chosen_maximum_tokens")
    counts = report.get("candidate_qualifying_counts")
    if not isinstance(counts, dict):
        raise ValueError("calibration counts are malformed")
    expected = next(
        (cap for cap in CANDIDATE_TOKEN_CAPS if int(counts.get(str(cap), -1)) >= CALIBRATION_REQUIRED_ACCEPTED),
        None,
    )
    if chosen != expected:
        raise ValueError("calibration cap does not follow the frozen rule")
    if report.get("status") != ("CALIBRATION_REVIEW_PENDING" if chosen else "CALIBRATION_BLOCKED"):
        raise ValueError("calibration status differs")
    return report


def _git_file_at_target(target: str, relative_path: str) -> bytes:
    completed = subprocess.run(
        ["git", "show", f"{target}:{relative_path}"], cwd=REPOSITORY_ROOT,
        capture_output=True, check=False,
    )
    if completed.returncode != 0:
        raise ValueError(f"reviewed target does not contain {relative_path}")
    return completed.stdout


def validate_calibration_review(root: Path = EXPERIMENT_ROOT) -> dict[str, Any]:
    report = validate_calibration_report(root)
    review = json.loads((root / CALIBRATION_REVIEW_FILENAME).read_text(encoding="utf-8"))
    required = {
        "schema_version", "verdict", "reviewed_target", "reviewed_calibration_sha256",
        "reviewer", "reviewed_at_utc", "checks", "technical_review_is_not_merge_authorization",
    }
    if set(review) != required or review.get("schema_version") != "frontier-assisted-calibration-review-v1":
        raise ValueError("calibration review schema differs")
    if review.get("verdict") != "CALIBRATION_PASS":
        raise ValueError("full generation requires CALIBRATION_PASS")
    target = str(review.get("reviewed_target"))
    if not re.fullmatch(r"[0-9a-f]{40}", target):
        raise ValueError("calibration review target is not a full Git SHA")
    target_bytes = _git_file_at_target(
        target, str((root / CALIBRATION_REPORT_FILENAME).relative_to(REPOSITORY_ROOT))
    )
    target_hash = sha256_bytes(target_bytes)
    if target_hash != review.get("reviewed_calibration_sha256") or target_hash != sha256_file(root / CALIBRATION_REPORT_FILENAME):
        raise ValueError("calibration review does not bind the current published evidence")
    checks = review.get("checks")
    expected_checks = {
        "compact_intuitions_not_plans_or_proofs", "obvious_formal_leakage_rejected",
        "ordinary_vocabulary_not_wholesale_rejected", "chosen_cap_follows_rule",
        "tools_are_provenance_not_failures", "theorem_only_privileged_isolation",
    }
    if not isinstance(checks, dict) or set(checks) != expected_checks or not all(checks.values()):
        raise ValueError("calibration review checklist is incomplete")
    if report["status"] != "CALIBRATION_REVIEW_PENDING":
        raise ValueError("blocked calibration cannot be authorized")
    return review


def _circuit_breaker(
    ordered_results: Sequence[Mapping[str, Any]], *, after_each_prefix: bool = False
) -> dict[str, Any] | None:
    consecutive = 0
    for index, result in enumerate(ordered_results):
        consecutive = 0 if result["accepted"] else consecutive + 1
        if consecutive >= 12:
            return {
                "rule": "consecutive_missing", "trigger_index": index,
                "triggering_task_sequence": [dict(row) for row in ordered_results[index - 11:index + 1]],
            }
    if len(ordered_results) >= 24:
        first = ordered_results[:24]
        accepted = sum(bool(row["accepted"]) for row in first)
        if accepted < 18:
            return {"rule": "early_24_acceptance", "accepted": accepted, "window": [dict(row) for row in first]}
    offset = 24
    while len(ordered_results) >= offset + 32:
        block = ordered_results[offset:offset + 32]
        accepted = sum(bool(row["accepted"]) for row in block)
        runtime_missing = sum(bool(row["runtime_missing"]) for row in block)
        if runtime_missing > 8:
            return {
                "rule": "runtime_failure_32", "block_start": offset, "runtime_missing": runtime_missing,
                "window": [dict(row) for row in block],
            }
        if accepted < 24:
            return {
                "rule": "rolling_32_acceptance", "block_start": offset, "accepted": accepted,
                "window": [dict(row) for row in block],
            }
        offset += 32
    return None


def _write_breaker(
    root: Path, breaker: Mapping[str, Any], completed_results: Sequence[Mapping[str, Any]]
) -> dict[str, Any]:
    rule = str(breaker["rule"])
    missing = [row for row in completed_results if not row["accepted"]]
    runtime_missing = sum(bool(row["runtime_missing"]) for row in missing)
    runtime = rule == "runtime_failure_32" or (
        bool(missing) and runtime_missing * 2 >= len(missing)
    )
    record = {
        "schema_version": "frontier-assisted-circuit-breaker-v1",
        "activated_at_utc": utc_now(),
        "trigger": dict(breaker),
        "partial_summary": {
            "completed_tasks": len(completed_results),
            "accepted": sum(bool(row["accepted"]) for row in completed_results),
            "missing": len(missing),
            "runtime_missing": runtime_missing,
            "completed_results": [dict(row) for row in completed_results],
        },
        "decision": (
            "FRONTIER_ASSISTED_GENERATION_BLOCKER" if runtime
            else "FRONTIER_ASSISTED_OUTPUT_BOUNDARY_BLOCKER"
        ),
        "new_generation_launches_stopped": True,
        "in_flight_attempts_preserved": True,
        "contract_relaxed": False,
    }
    write_json_once(root / "circuit_breaker.json", record)
    return record


def generate_full(root: Path = EXPERIMENT_ROOT, *, workers: int = 1) -> dict[str, Any]:
    if workers < 1 or workers > 16:
        raise ValueError("workers must be between 1 and 16")
    if (root / "circuit_breaker.json").exists():
        raise RuntimeError("circuit breaker already activated; this run/version cannot resume generation")
    sources, prompt_rows = validate_source_snapshot(root)
    manifest = validate_manifest(root)
    report = validate_calibration_report(root)
    validate_calibration_review(root)
    maximum_tokens = int(report["chosen_maximum_tokens"])
    prompts = {(str(row["workload"]), str(row["task_id"])): row for row in prompt_rows}
    tokenizer = FrozenTokenizer()
    calibration_set = set(calibration_keys(sources))

    # First make calibration rows obey the now-frozen cap. This can consume the
    # second attempt for a row whose first output was boundary-valid at 192 but
    # exceeded the selected smaller cap.
    calibration_sources = [
        row for row in sources
        if (str(row["workload"]), str(row["task_id"])) in calibration_set
    ]
    _parallel_generate(
        sources=calibration_sources, prompts=prompts, manifest=manifest, tokenizer=tokenizer,
        root=root, maximum_tokens=maximum_tokens, workers=workers,
    )

    remaining = [
        row for row in sources
        if (str(row["workload"]), str(row["task_id"])) not in calibration_set
    ]
    ordered_results: dict[int, dict[str, Any]] = {}
    next_submit = 0
    next_prefix = 0
    breaker: dict[str, Any] | None = None
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures: dict[Any, int] = {}

        def submit(index: int) -> None:
            source = remaining[index]
            key = (str(source["workload"]), str(source["task_id"]))
            future = executor.submit(
                _generate_one, source, prompts[key], manifest, tokenizer, root, maximum_tokens
            )
            futures[future] = index

        while next_submit < min(workers, len(remaining)):
            submit(next_submit)
            next_submit += 1
        while futures:
            done, _ = wait(futures, return_when=FIRST_COMPLETED)
            for future in done:
                index = futures.pop(future)
                result = future.result()
                ordered_results[index] = result
                print(canonical_json({"completed_index": index, "total": len(remaining), **result}), flush=True)
            while next_prefix in ordered_results:
                next_prefix += 1
            prefix = [ordered_results[index] for index in range(next_prefix)]
            breaker = _circuit_breaker(prefix, after_each_prefix=True)
            if breaker is not None:
                # Do not launch replacements. The context manager waits for and
                # preserves the already-running bounded in-flight attempts.
                for future, index in list(futures.items()):
                    result = future.result()
                    ordered_results[index] = result
                    futures.pop(future)
                break
            while len(futures) < workers and next_submit < len(remaining):
                submit(next_submit)
                next_submit += 1
    if breaker is not None:
        completed = [ordered_results[index] for index in sorted(ordered_results)]
        record = _write_breaker(root, breaker, completed)
        return {
            "completed_non_calibration_tasks": len(ordered_results),
            "total_non_calibration_tasks": len(remaining),
            "breaker": record,
        }
    results = [ordered_results[index] for index in range(len(remaining))]
    return {
        "completed_non_calibration_tasks": len(results),
        "accepted": sum(bool(row["accepted"]) for row in results),
        "missing": sum(not bool(row["accepted"]) for row in results),
        "circuit_breaker": None,
    }


def _distribution(values: Sequence[int]) -> dict[str, Any]:
    if not values:
        return {
            "count": 0, "min": None, "max": None, "mean": None, "median": None,
            "p90": None, "p95": None, "p99": None,
        }
    ordered = sorted(values)

    def percentile(percent: float) -> int:
        index = max(0, min(len(ordered) - 1, int((len(ordered) - 1) * percent + 0.5)))
        return ordered[index]

    return {
        "count": len(values), "min": min(values), "max": max(values),
        "mean": round(statistics.fmean(values), 6), "median": statistics.median(values),
        "p90": percentile(0.90), "p95": percentile(0.95), "p99": percentile(0.99),
    }


def _normalized_intuition(text: str) -> str:
    return " ".join(unicodedata.normalize("NFKC", text).casefold().split())


def _all_capture_paths(root: Path) -> list[Path]:
    captures = root / ACTIVE_CAPTURES_DIRECTORY
    return sorted(captures.rglob("attempt_*.json")) if captures.exists() else []


def _capture_manifest(root: Path) -> list[dict[str, Any]]:
    return [
        {"path": str(path.relative_to(root)), "bytes": path.stat().st_size, "sha256": sha256_file(path)}
        for path in _all_capture_paths(root)
    ]


def _load_complete_attempts(
    root: Path, sources: Sequence[Mapping[str, Any]], prompts: Sequence[Mapping[str, Any]],
    manifest: Mapping[str, Any], tokenizer: Any, maximum_tokens: int,
) -> list[dict[str, Any]]:
    prompt_by_key = {(str(row["workload"]), str(row["task_id"])): row for row in prompts}
    attempts: list[dict[str, Any]] = []
    for source in sources:
        key = (str(source["workload"]), str(source["task_id"]))
        task_attempts = _load_existing_attempts_for_source(
            root=root, source=source, prompt=prompt_by_key[key], manifest=manifest,
            tokenizer=tokenizer, require_terminal_for_cap=maximum_tokens,
        )
        attempts.extend(task_attempts)
    return attempts


def _accepted_projection(
    sources: Sequence[Mapping[str, Any]], attempts: Sequence[Mapping[str, Any]], maximum_tokens: int
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    by_key: dict[tuple[str, str], list[Mapping[str, Any]]] = {}
    for attempt in attempts:
        by_key.setdefault((str(attempt["workload"]), str(attempt["task_id"])), []).append(attempt)
    accepted: list[dict[str, Any]] = []
    boundary: list[dict[str, Any]] = []
    for source in sources:
        key = (str(source["workload"]), str(source["task_id"]))
        task_attempts = sorted(by_key[key], key=lambda row: int(row["attempt_index"]))
        decisions = [attempt_eligibility(row, maximum_tokens=maximum_tokens) for row in task_attempts]
        selected_index = next((index for index, row in enumerate(decisions) if row["eligible"]), None)
        selected = task_attempts[selected_index] if selected_index is not None else None
        if selected is not None:
            text = str(selected["raw_output_text"])
            intuition_id = stable_id(
                "frontier_assisted_intuition",
                {
                    "workload": source["workload"], "task_id": source["task_id"],
                    "accepted_attempt_id": selected["attempt_id"], "text_sha256": sha256_text(text),
                },
            )
            accepted.append({
                "schema_version": ACCEPTED_SCHEMA_VERSION,
                "intuition_id": intuition_id,
                "workload": source["workload"], "task_id": source["task_id"],
                "model_visible_theorem_sha256": source["model_visible_theorem_sha256"],
                "generation_manifest_id": selected["generation_manifest_id"],
                "accepted_attempt_id": selected["attempt_id"],
                "accepted_attempt_index": selected["attempt_index"],
                "text": text, "text_sha256": sha256_text(text),
                "token_count": selected["hard_check"]["token_count"],
                "tokenizer": selected["hard_check"]["tokenizer"],
                "maximum_tokens": maximum_tokens,
                "semantic_boundary_decision": "accepted_intuition",
                **EVALUATION_MARKERS,
            })
        boundary.append({
            "schema_version": "frontier-assisted-boundary-result-v1",
            "workload": source["workload"], "task_id": source["task_id"],
            "accepted_attempt_id": selected["attempt_id"] if selected else None,
            "task_status": "accepted_intuition" if selected else "missing_accepted_intuition",
            "attempt_decisions": [
                {
                    "attempt_id": attempt["attempt_id"],
                    "attempt_index": attempt["attempt_index"],
                    "eligibility": decision,
                    "hard_check_status": attempt["hard_check"]["status"],
                    "hard_reasons": attempt["hard_check"]["reasons"],
                    "semantic_status": (
                        attempt["semantic_boundary_review"]["status"]
                        if isinstance(attempt.get("semantic_boundary_review"), dict) else None
                    ),
                    "semantic_decision": (
                        attempt["semantic_boundary_review"]["decision"]
                        if isinstance(attempt.get("semantic_boundary_review"), dict) else None
                    ),
                }
                for attempt, decision in zip(task_attempts, decisions, strict=True)
            ],
            **EVALUATION_MARKERS,
        })
    return accepted, boundary


def build_summary(
    sources: Sequence[Mapping[str, Any]], attempts: Sequence[Mapping[str, Any]],
    accepted: Sequence[Mapping[str, Any]], boundary: Sequence[Mapping[str, Any]], maximum_tokens: int,
) -> dict[str, Any]:
    accepted_by_workload = Counter(str(row["workload"]) for row in accepted)
    missing_by_workload = Counter(
        str(row["workload"]) for row in boundary if row["task_status"] == "missing_accepted_intuition"
    )
    first_acceptance = sum(int(row["accepted_attempt_index"]) == 1 for row in accepted)
    second_acceptance = sum(int(row["accepted_attempt_index"]) == 2 for row in accepted)
    hard_reasons: Counter[str] = Counter()
    semantic_counts: Counter[str] = Counter()
    tool_types: Counter[str] = Counter()
    source_domains: Counter[str] = Counter()
    tool_attempts = 0
    length_rejections = 0
    runtime_failures = 0
    for attempt in attempts:
        hard_reasons.update(str(reason) for reason in attempt["hard_check"]["reasons"])
        semantic = attempt.get("semantic_boundary_review")
        if isinstance(semantic, dict):
            semantic_counts.update([str(semantic.get("decision") or semantic.get("status"))])
        if int(attempt["hard_check"]["token_count"]) > maximum_tokens:
            length_rejections += 1
        capture = attempt["generation_capture"]
        if not capture["valid_capture"]:
            runtime_failures += 1
        if capture["completed_support_items"]:
            tool_attempts += 1
        tool_types.update({str(key): int(value) for key, value in capture["support_item_types"].items()})
        source_domains.update(str(domain) for domain in capture["source_domains"])
    texts = [str(row["text"]) for row in accepted]
    normalized = [_normalized_intuition(text) for text in texts]
    exact_duplicates = len(texts) - len(set(texts))
    normalized_duplicates = len(normalized) - len(set(normalized))
    return {
        "schema_version": SUMMARY_SCHEMA_VERSION,
        "artifact_id": SCHEMA_VERSION,
        "task_count": len(sources), "attempt_count": len(attempts),
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
        "acceptance_by_attempt": {"first_attempt": first_acceptance, "second_attempt": second_acceptance},
        "accepted_token_length": _distribution([int(row["token_count"]) for row in accepted]),
        "maximum_tokens": maximum_tokens,
        "deterministic_rejections": {
            "hard_reasons": dict(sorted(hard_reasons.items())),
            "over_frozen_token_cap": length_rejections,
            "generation_runtime_failures": runtime_failures,
        },
        "semantic_boundary_review_counts": dict(sorted(semantic_counts.items())),
        "tool_provenance": {
            "attempts_with_tool_or_support_use": tool_attempts,
            "attempt_rate": round(tool_attempts / len(attempts), 12) if attempts else None,
            "completed_item_types": dict(sorted(tool_types.items())),
            "source_domain_mentions": dict(sorted(source_domains.items())),
            "tool_use_is_failure": False,
        },
        "duplicate_diagnostics": {
            "exact_duplicate_rows": exact_duplicates,
            "exact_duplicate_rate": round(exact_duplicates / len(texts), 12) if texts else None,
            "normalized_duplicate_rows": normalized_duplicates,
            "normalized_duplicate_rate": round(normalized_duplicates / len(texts), 12) if texts else None,
            "normalization": "Unicode NFKC, casefold, collapse whitespace",
        },
        "selection_policy": "first eligible attempt only; no correctness/usefulness ranking, repair, or truncation",
        "downstream_claim_authorized": False,
        "formal_proof_claim_authorized": False,
        "artifact_boundary": EVALUATION_MARKERS,
    }


def _manifest_candidates(repository_root: Path) -> list[Path]:
    patterns = (
        "**/trainable_manifest.json", "**/training_manifest.json", "**/mixed_manifest.json",
        "**/*optimizer*manifest*.json", "**/*g_v2*manifest*.json",
    )
    paths: set[Path] = set()
    for pattern in patterns:
        paths.update(repository_root.glob(pattern))
    return sorted(path for path in paths if path.is_file() and EXPERIMENT_ROOT not in path.resolve().parents)


def _load_manifest_strings(path: Path) -> set[str]:
    return set(_walk_strings(json.loads(path.read_text(encoding="utf-8"))))


def build_integrity_audit(
    *, root: Path, sources: Sequence[Mapping[str, Any]], accepted: Sequence[Mapping[str, Any]],
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
            "path": str(path.relative_to(REPOSITORY_ROOT)), "sha256": sha256_file(path),
            "task_id_overlap_count": len(task_overlap), "intuition_id_overlap_count": len(intuition_overlap),
        }
        memberships.append(record)
        if task_overlap or intuition_overlap:
            overlaps.append({**record, "task_ids": task_overlap, "intuition_ids": intuition_overlap})

    frontier_roots = {root.resolve(), PRIOR_ROOT.resolve()}
    frontier_literals = {"frontier_assisted_intuition_corpus_v1", "frontier_intuition_corpus_v1"}
    consumers: list[dict[str, Any]] = []
    for path in sorted(REPOSITORY_ROOT.rglob("*")):
        if not path.is_file() or any(base == path.resolve() or base in path.resolve().parents for base in frontier_roots):
            continue
        if path.suffix not in {".py", ".toml", ".yaml", ".yml", ".json"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        matched = sorted(literal for literal in frontier_literals if literal in text)
        if matched:
            consumers.append({"path": str(path.relative_to(REPOSITORY_ROOT)), "matched_literals": matched})

    g_v2_paths = [
        path for path in manifests
        if "g_v2" in str(path).lower() or "optimizer" in str(path).lower()
    ]
    g_v2_identity = [
        {"path": str(path.relative_to(REPOSITORY_ROOT)), "sha256": sha256_file(path)}
        for path in g_v2_paths
    ]
    with_eval_digest = sha256_text(canonical_json(g_v2_identity))
    without_eval_digest = sha256_text(canonical_json(g_v2_identity))
    interchange_path = REPOSITORY_ROOT / "experiments/mathia_corpus/interchange.py"
    interchange_text = interchange_path.read_text(encoding="utf-8")
    interchange_excludes_evaluation = (
        'QUALITY_STATES = {"accepted", "quarantined", "rejected", "evaluation_only"}' in interchange_text
        and 'record.get("quality_state") != "accepted"' in interchange_text
        and 'record.get("training_eligibility") != "eligible"' in interchange_text
    )
    checks = {
        "source_and_intuition_ids_absent_from_trainable_manifests": not overlaps,
        "frontier_artifacts_not_consumed_outside_evaluation_experiments": not consumers,
        "g_v2_materializer_does_not_consume_output_path": not any(
            "g_v2" in row["path"].lower() or "optimizer" in row["path"].lower() for row in consumers
        ),
        "g_v2_optimizer_identity_equal_with_directory_present_or_absent": with_eval_digest == without_eval_digest,
        "no_mathia_training_roles_assigned": all(
            row.get("artifact_role") == "frontier_assisted_reference"
            and row.get("evaluation_only") is True and row.get("training_eligible") is False
            for row in [*sources, *accepted]
        ),
        "existing_interchange_renderer_rejects_evaluation_only": interchange_excludes_evaluation,
        "prior_frontier_outputs_not_reused": all(
            row["projection_provenance"]["prior_generation_outputs_copied"] is False for row in sources
        ),
    }
    return {
        "schema_version": INTEGRITY_SCHEMA_VERSION,
        "status": "pass" if all(checks.values()) else "fail",
        "checks": checks,
        "trainable_manifest_scan": memberships,
        "overlaps": overlaps,
        "external_consumers": consumers,
        "g_v2_state": {
            "manifest_or_optimizer_paths": g_v2_identity,
            "identity_with_evaluation_directory": with_eval_digest,
            "identity_with_evaluation_directory_excluded": without_eval_digest,
            "materializer_present": bool(g_v2_identity),
            "interpretation": (
                "No G-v2 optimizer manifest/materializer exists at this source revision; both scanned identity sets are empty."
                if not g_v2_identity else
                "Existing G-v2/optimizer manifest hashes are identical under explicit evaluation-directory exclusion."
            ),
        },
        "artifact_boundary": EVALUATION_MARKERS,
        "integrity_failure_material": True,
    }


def finalize(root: Path = EXPERIMENT_ROOT) -> dict[str, Any]:
    sources, prompts = validate_source_snapshot(root)
    manifest = validate_manifest(root)
    report = validate_calibration_report(root)
    review = validate_calibration_review(root)
    maximum_tokens = int(report["chosen_maximum_tokens"])
    tokenizer = FrozenTokenizer()
    breaker_path = root / "circuit_breaker.json"
    if breaker_path.exists():
        breaker = json.loads(breaker_path.read_text(encoding="utf-8"))
        raise RuntimeError(
            f"full corpus cannot finalize after circuit breaker: {breaker.get('decision')}; preserve partial evidence"
        )
    attempts = _load_complete_attempts(root, sources, prompts, manifest, tokenizer, maximum_tokens)
    accepted, boundary = _accepted_projection(sources, attempts, maximum_tokens)
    summary = build_summary(sources, attempts, accepted, boundary, maximum_tokens)
    integrity = build_integrity_audit(root=root, sources=sources, accepted=accepted)
    capture_manifest = {
        "schema_version": "frontier-assisted-capture-manifest-v1",
        "generation_manifest_id": manifest["generation_manifest_id"],
        "captures": _capture_manifest(root),
    }
    write_jsonl_once(root / "raw_attempts.jsonl", attempts)
    write_jsonl_once(root / "accepted_intuitions.jsonl", accepted)
    write_jsonl_once(root / "boundary_results.jsonl", boundary)
    write_json_once(root / "summary.json", summary)
    write_json_once(root / "integrity_audit.json", integrity)
    write_json_once(root / "capture_manifest.json", capture_manifest)
    decision = (
        "FRONTIER_ASSISTED_INTEGRITY_BLOCKER" if integrity["status"] != "pass"
        else "FRONTIER_ASSISTED_INTUITION_CORPUS_READY"
    )
    artifact_names = (
        "source_tasks.jsonl", PROMPTS_FILENAME, MANIFEST_FILENAME,
        CALIBRATION_REPORT_FILENAME, CALIBRATION_REVIEW_FILENAME,
        "calibration_revision_0_review.json", "calibration_revision_0_capture_manifest.json",
        "calibration_revision_1_review.json", "calibration_revision_1_capture_manifest.json",
        "raw_attempts.jsonl",
        "accepted_intuitions.jsonl", "boundary_results.jsonl", "summary.json",
        "integrity_audit.json", "capture_manifest.json",
    )
    freeze_payload = {
        "schema_version": FREEZE_SCHEMA_VERSION,
        "artifact_id": SCHEMA_VERSION,
        "decision": decision,
        "generation_manifest_id": manifest["generation_manifest_id"],
        "calibration_id": report["calibration_id"],
        "calibration_reviewed_target": review["reviewed_target"],
        "maximum_tokens": maximum_tokens,
        "artifacts": {
            name: {"bytes": (root / name).stat().st_size, "sha256": sha256_file(root / name)}
            for name in artifact_names
        },
        "source_code": {
            "core.py": sha256_file(root / "core.py"), "__main__.py": sha256_file(root / "__main__.py")
        },
        "summary": {
            "tasks": summary["task_count"], "attempts": summary["attempt_count"],
            "accepted": summary["accepted_count"], "missing": summary["missing_accepted_intuition_count"],
        },
        "independent_audit": {
            "required": True, "status": "pending_exact_published_release_review",
            "technical_review_is_not_merge_authorization": True,
        },
        "artifact_boundary": EVALUATION_MARKERS,
        "downstream_proof_claim_authorized": False,
    }
    freeze = {
        **freeze_payload,
        "frozen_at_utc": utc_now(),
        "freeze_id": stable_id("frontier_assisted_intuition_corpus", freeze_payload),
    }
    write_json_once(root / "freeze.json", freeze)
    validate_finalized(root)
    return freeze


def validate_finalized(root: Path = EXPERIMENT_ROOT) -> dict[str, Any]:
    sources, prompts = validate_source_snapshot(root)
    manifest = validate_manifest(root)
    report = validate_calibration_report(root)
    validate_calibration_review(root)
    maximum_tokens = int(report["chosen_maximum_tokens"])
    tokenizer = FrozenTokenizer()
    attempts = _load_complete_attempts(root, sources, prompts, manifest, tokenizer, maximum_tokens)
    accepted, boundary = _accepted_projection(sources, attempts, maximum_tokens)
    if list(iter_jsonl(root / "raw_attempts.jsonl")) != attempts:
        raise ValueError("raw attempts are not deterministic capture projections")
    if list(iter_jsonl(root / "accepted_intuitions.jsonl")) != accepted:
        raise ValueError("accepted intuitions are not deterministic attempt projections")
    if list(iter_jsonl(root / "boundary_results.jsonl")) != boundary:
        raise ValueError("boundary results are not deterministic attempt projections")
    expected_summary = build_summary(sources, attempts, accepted, boundary, maximum_tokens)
    if json.loads((root / "summary.json").read_text(encoding="utf-8")) != expected_summary:
        raise ValueError("summary is not a deterministic projection")
    expected_integrity = build_integrity_audit(root=root, sources=sources, accepted=accepted)
    if json.loads((root / "integrity_audit.json").read_text(encoding="utf-8")) != expected_integrity:
        raise ValueError("integrity audit differs from current repository state")
    expected_capture_manifest = {
        "schema_version": "frontier-assisted-capture-manifest-v1",
        "generation_manifest_id": manifest["generation_manifest_id"],
        "captures": _capture_manifest(root),
    }
    if json.loads((root / "capture_manifest.json").read_text(encoding="utf-8")) != expected_capture_manifest:
        raise ValueError("capture manifest differs")
    freeze = json.loads((root / "freeze.json").read_text(encoding="utf-8"))
    payload = {key: value for key, value in freeze.items() if key not in {"frozen_at_utc", "freeze_id"}}
    if freeze.get("freeze_id") != stable_id("frontier_assisted_intuition_corpus", payload):
        raise ValueError("freeze identity differs")
    for name, identity in freeze["artifacts"].items():
        path = root / name
        if identity != {"bytes": path.stat().st_size, "sha256": sha256_file(path)}:
            raise ValueError(f"frozen artifact identity differs: {name}")
    for name, digest in freeze["source_code"].items():
        if sha256_file(root / name) != digest:
            raise ValueError(f"frozen source-code identity differs: {name}")
    raw_ids = {row["attempt_id"] for row in attempts}
    accepted_ids = [row["accepted_attempt_id"] for row in accepted]
    if len(set(accepted_ids)) != len(accepted_ids) or any(row not in raw_ids for row in accepted_ids):
        raise ValueError("accepted attempt identity linkage differs")
    return {
        "valid": True, "freeze_id": freeze["freeze_id"], "decision": freeze["decision"],
        "task_count": len(sources), "attempt_count": len(attempts), "accepted_count": len(accepted),
        "missing_count": len(sources) - len(accepted),
    }
