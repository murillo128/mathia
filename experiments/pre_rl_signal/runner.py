from __future__ import annotations

"""Model-agnostic prompt and result plumbing for ``gold-set-v0``.

The public prompt path deliberately imports only the audited public fixture.
Private truth and the exact scorer are imported lazily by the scoring/oracle
paths so prompt materialization cannot accidentally depend on private data.
"""

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from typing import Any, Iterable, Mapping, Sequence


ROOT = Path(__file__).resolve().parents[2]
GOLD_SET_DIR = Path(__file__).resolve().parent / "gold_set_v0"

# gold_set_v0 is intentionally an executable fixture directory whose modules
# use local imports. Make that existing seam available without changing the
# audited fixture/scoring files in this issue.
if str(GOLD_SET_DIR) not in sys.path:
    sys.path.insert(0, str(GOLD_SET_DIR))

from public_fixtures import build_public  # noqa: E402


CONDITIONS = (
    "none",
    "factual",
    "procedural",
    "structural",
    "sterile",
    "wrong",
    "shuffled",
)
PAIR_ANSWER_KINDS = {"int_pair", "mul_collision_pair", "crt_collision_pair"}
SUPPORTED_ANSWER_KINDS = {"bool", "int", "mod_int", *PAIR_ANSWER_KINDS}
PRIVATE_MANIFEST_KEYS = {
    "answer",
    "canonical_answer",
    "expected_answer",
    "ground_truth",
    "correct_answer",
    "truth",
    "private",
    "private_truth",
    "scorer_params",
    "scoring_params",
    "params",
}
RESULT_PUBLIC_FIELDS = (
    "gold_set_version",
    "situation_id",
    "task_id",
    "cluster",
    "task_type",
    "distance",
    "condition",
    "answer_kind",
)
RESPONSE_CONTROL_FIELDS = {
    "prompt_id",
    "raw_response",
    "prompt_sha256",
    "manifest_sha256",
}


class RunnerError(ValueError):
    """Base class for deterministic runner contract failures."""


class ManifestMismatchError(RunnerError):
    """The supplied manifest does not match the current audited public set."""


class ResponseImportError(RunnerError):
    """A response file violates the provider-neutral import contract."""

    def __init__(self, message: str, summary: Mapping[str, Any]):
        super().__init__(message)
        self.summary = dict(summary)


def canonical_json(value: Any) -> str:
    """Return the compact deterministic JSON representation used by prompts."""

    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def render_prompt(
    visible: Mapping[str, Any],
    task_prompt: str,
    context: str | None = None,
) -> str:
    """Render one provider-independent plain-text solver prompt."""

    sections = [
        "Mathematical situation:\n" + canonical_json(visible),
    ]
    if context is not None:
        sections.append("Additional context:\n" + context)
    sections.extend(
        [
            "Task:\n" + task_prompt,
            (
                "Return only the final answer as one valid JSON value. "
                "Do not include reasoning or prose.\nAnswer:"
            ),
        ]
    )
    return "\n\n".join(sections) + "\n"


def _selected_context(
    public: Mapping[str, Any],
    situation: Mapping[str, Any],
    condition: str,
) -> str | None:
    if condition == "none":
        return None
    if condition == "shuffled":
        return public["shuffled_pool"][situation["shuffled_context_id"]]
    return situation["contexts"][condition]


def build_prompt_records() -> list[dict[str, Any]]:
    """Build the canonical 560 public prompt records without private access."""

    public = build_public()
    version = public["version"]
    records: list[dict[str, Any]] = []
    for situation in public["situations"]:
        for task in situation["hidden_tasks"]:
            for condition in CONDITIONS:
                prompt_text = render_prompt(
                    situation["visible"],
                    task["prompt"],
                    _selected_context(public, situation, condition),
                )
                records.append(
                    {
                        "prompt_id": (
                            f"{version}/{situation['id']}/{task['id']}/{condition}"
                        ),
                        "gold_set_version": version,
                        "situation_id": situation["id"],
                        "task_id": task["id"],
                        "cluster": situation["cluster"],
                        "task_type": task["type"],
                        "distance": task["distance"],
                        "condition": condition,
                        "answer_kind": task["answer_kind"],
                        "prompt_text": prompt_text,
                        "prompt_sha256": hashlib.sha256(
                            prompt_text.encode("utf-8")
                        ).hexdigest(),
                    }
                )
    return records


def serialize_jsonl(records: Iterable[Mapping[str, Any]]) -> bytes:
    """Serialize JSONL deterministically, including one trailing newline/record."""

    return b"".join(
        (
            json.dumps(
                record,
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            )
            + "\n"
        ).encode("utf-8")
        for record in records
    )


def manifest_sha256(records: Sequence[Mapping[str, Any]]) -> str:
    """Hash the exact deterministic JSONL bytes, including record order."""

    return hashlib.sha256(serialize_jsonl(records)).hexdigest()


def repository_commit() -> str | None:
    """Resolve the local repository commit when the runner is inside Git."""

    try:
        completed = subprocess.run(
            ["git", "-C", str(ROOT), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
            timeout=5,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    commit = completed.stdout.strip()
    return commit or None


def _metadata_path(path: Path) -> Path:
    return path.with_name(path.name + ".meta.json")


def _write_json(path: Path, value: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )


def write_prompt_manifest(
    path: str | Path,
    records: Sequence[Mapping[str, Any]] | None = None,
) -> dict[str, Any]:
    """Write canonical prompts plus a non-model-visible provenance sidecar."""

    output_path = Path(path)
    prompt_records = list(records) if records is not None else build_prompt_records()
    validate_manifest_records(prompt_records)
    data = serialize_jsonl(prompt_records)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(data)
    metadata = {
        "artifact_kind": "prompt_manifest",
        "gold_set_version": prompt_records[0]["gold_set_version"],
        "manifest_sha256": hashlib.sha256(data).hexdigest(),
        "prompt_count": len(prompt_records),
        "repository_commit": repository_commit(),
    }
    _write_json(_metadata_path(output_path), metadata)
    return metadata


def read_jsonl(path: str | Path) -> list[dict[str, Any]]:
    """Read an object-per-line JSONL file with useful structural errors."""

    records: list[dict[str, Any]] = []
    for line_number, line in enumerate(
        Path(path).read_text(encoding="utf-8").splitlines(), start=1
    ):
        if not line.strip():
            continue
        try:
            record = json.loads(
                line,
                parse_constant=_reject_nonstandard_json_constant,
            )
        except (json.JSONDecodeError, ValueError) as exc:
            raise RunnerError(f"invalid JSONL at line {line_number}: {exc}") from exc
        if not isinstance(record, dict):
            raise RunnerError(f"JSONL line {line_number} must be an object")
        records.append(record)
    return records


def _contains_private_key(value: Any) -> bool:
    if isinstance(value, Mapping):
        if any(key in PRIVATE_MANIFEST_KEYS for key in value):
            return True
        return any(_contains_private_key(item) for item in value.values())
    if isinstance(value, (list, tuple)):
        return any(_contains_private_key(item) for item in value)
    return False


def validate_manifest_records(records: Sequence[Mapping[str, Any]]) -> None:
    """Validate public identity/text while permitting a later reordered manifest."""

    expected_records = build_prompt_records()
    expected_by_id = {record["prompt_id"]: record for record in expected_records}
    if len(records) != len(expected_records):
        raise ManifestMismatchError(
            f"manifest has {len(records)} records; expected {len(expected_records)}"
        )

    seen: set[str] = set()
    for position, record in enumerate(records, start=1):
        if not isinstance(record, Mapping):
            raise ManifestMismatchError(f"manifest record {position} is not an object")
        if _contains_private_key(record):
            raise ManifestMismatchError(
                f"manifest record {position} contains private scoring material"
            )
        prompt_id = record.get("prompt_id")
        if not isinstance(prompt_id, str) or prompt_id not in expected_by_id:
            raise ManifestMismatchError(
                f"manifest record {position} has an unknown prompt_id"
            )
        if prompt_id in seen:
            raise ManifestMismatchError(f"duplicate manifest prompt_id: {prompt_id}")
        seen.add(prompt_id)

        expected = expected_by_id[prompt_id]
        for key, expected_value in expected.items():
            if record.get(key) != expected_value:
                raise ManifestMismatchError(
                    f"manifest mismatch for {prompt_id} field {key}"
                )

    missing = set(expected_by_id) - seen
    if missing:
        raise ManifestMismatchError(
            f"manifest is missing {len(missing)} expected prompt IDs"
        )


def _reject_nonstandard_json_constant(value: str) -> None:
    raise ValueError(f"non-standard JSON constant: {value}")


def parse_response(raw_response: str, answer_kind: str) -> tuple[str, Any | None]:
    """Strictly parse one complete response and enforce its public shape."""

    if answer_kind not in SUPPORTED_ANSWER_KINDS:
        raise RunnerError(f"unsupported answer kind: {answer_kind}")
    try:
        answer = json.loads(
            raw_response.strip(),
            parse_constant=_reject_nonstandard_json_constant,
        )
    except (json.JSONDecodeError, UnicodeError, ValueError, TypeError):
        return "invalid_json", None

    if answer_kind == "bool":
        valid_shape = isinstance(answer, bool)
    elif answer_kind in {"int", "mod_int"}:
        valid_shape = isinstance(answer, int) and not isinstance(answer, bool)
    else:
        valid_shape = (
            isinstance(answer, list)
            and len(answer) == 2
            and all(
                isinstance(item, int) and not isinstance(item, bool)
                for item in answer
            )
        )
    if not valid_shape:
        return "wrong_shape", None
    return "ok", answer


def _base_import_summary(expected: int) -> dict[str, Any]:
    return {
        "total_expected_prompts": expected,
        "imported_responses": 0,
        "parsed_successfully": 0,
        "parse_failures": 0,
        "invalid_json": 0,
        "wrong_shape": 0,
        "correct_answers": 0,
        "incorrect_answers": 0,
        "missing_responses": expected,
        "duplicate_prompt_ids": 0,
        "unknown_prompt_ids": 0,
        "manifest_mismatches": 0,
        "invalid_response_records": 0,
        "complete": False,
    }


def _index_responses(
    response_records: Sequence[Mapping[str, Any]],
    manifest_records: Sequence[Mapping[str, Any]],
    current_manifest_hash: str,
    allow_partial: bool,
) -> tuple[dict[str, Mapping[str, Any]], dict[str, Any]]:
    manifest_by_id = {record["prompt_id"]: record for record in manifest_records}
    indexed: dict[str, Mapping[str, Any]] = {}
    seen_prompt_ids: set[str] = set()
    summary = _base_import_summary(len(manifest_records))

    for response in response_records:
        if not isinstance(response, Mapping):
            summary["invalid_response_records"] += 1
            continue
        prompt_id = response.get("prompt_id")
        if not isinstance(prompt_id, str) or prompt_id not in manifest_by_id:
            summary["unknown_prompt_ids"] += 1
            continue
        if prompt_id in seen_prompt_ids:
            summary["duplicate_prompt_ids"] += 1
            continue
        seen_prompt_ids.add(prompt_id)
        raw_response = response.get("raw_response")
        if "raw_response" not in response or not isinstance(raw_response, str):
            summary["invalid_response_records"] += 1
            continue

        manifest_record = manifest_by_id[prompt_id]
        if (
            "prompt_sha256" in response
            and response["prompt_sha256"] != manifest_record["prompt_sha256"]
        ):
            summary["manifest_mismatches"] += 1
            continue
        if (
            "manifest_sha256" in response
            and response["manifest_sha256"] != current_manifest_hash
        ):
            summary["manifest_mismatches"] += 1
            continue
        indexed[prompt_id] = response

    summary["imported_responses"] = len(indexed)
    summary["missing_responses"] = len(manifest_by_id.keys() - indexed.keys())
    structural_failures = (
        summary["unknown_prompt_ids"]
        + summary["duplicate_prompt_ids"]
        + summary["manifest_mismatches"]
        + summary["invalid_response_records"]
    )
    if structural_failures:
        raise ResponseImportError(
            "response import contains structural errors",
            summary,
        )
    if summary["missing_responses"] and not allow_partial:
        raise ResponseImportError(
            "response import is incomplete; use explicit partial mode for plumbing",
            summary,
        )
    return indexed, summary


def _load_exact_scorer():
    from scoring import score_answer

    return score_answer


def score_imported_responses(
    manifest_records: Sequence[Mapping[str, Any]],
    response_records: Sequence[Mapping[str, Any]],
    *,
    model_id: str,
    generation_settings: Mapping[str, Any],
    model_revision: str | None = None,
    allow_partial: bool = False,
    commit: str | None = None,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Import, strictly parse, and exactly score provider-neutral responses."""

    if not isinstance(model_id, str) or not model_id:
        raise RunnerError("model_id must be a non-empty string")
    if not isinstance(generation_settings, Mapping):
        raise RunnerError("generation_settings must be a JSON object")
    # Ensure caller-supplied settings can be retained without interpretation.
    try:
        json.dumps(generation_settings, ensure_ascii=False)
    except (TypeError, ValueError) as exc:
        raise RunnerError("generation_settings must be JSON-serializable") from exc

    validate_manifest_records(manifest_records)
    current_manifest_hash = manifest_sha256(manifest_records)
    indexed, summary = _index_responses(
        response_records,
        manifest_records,
        current_manifest_hash,
        allow_partial,
    )

    exact_scorer = None
    source_commit = commit if commit is not None else repository_commit()
    results: list[dict[str, Any]] = []
    for manifest_record in manifest_records:
        prompt_id = manifest_record["prompt_id"]
        response = indexed.get(prompt_id)
        if response is None:
            continue
        parse_status, parsed_answer = parse_response(
            response["raw_response"], manifest_record["answer_kind"]
        )
        correct = False
        if parse_status == "ok":
            summary["parsed_successfully"] += 1
            if exact_scorer is None:
                exact_scorer = _load_exact_scorer()
            correct = exact_scorer(
                manifest_record["situation_id"],
                manifest_record["task_id"],
                parsed_answer,
            )
        else:
            summary["parse_failures"] += 1
            summary[parse_status] += 1

        if correct:
            summary["correct_answers"] += 1
        else:
            summary["incorrect_answers"] += 1

        result = {
            "prompt_id": prompt_id,
            "prompt_sha256": manifest_record["prompt_sha256"],
            **{
                key: manifest_record[key]
                for key in RESULT_PUBLIC_FIELDS
            },
            "repository_commit": source_commit,
            "manifest_sha256": current_manifest_hash,
            "model_id": model_id,
            "model_revision": model_revision,
            "generation_settings": dict(generation_settings),
            "raw_response": response["raw_response"],
            "parse_status": parse_status,
            "correct": bool(correct),
        }
        if parse_status == "ok":
            result["parsed_answer"] = parsed_answer
        import_metadata = {
            key: value
            for key, value in response.items()
            if key not in RESPONSE_CONTROL_FIELDS
        }
        if import_metadata:
            result["import_metadata"] = import_metadata
        results.append(result)

    summary["complete"] = (
        summary["missing_responses"] == 0
        and summary["imported_responses"] == summary["total_expected_prompts"]
    )
    return results, summary


def build_oracle_responses(
    manifest_records: Sequence[Mapping[str, Any]],
) -> list[dict[str, str]]:
    """Create explicitly synthetic responses from canonical private answers."""

    validate_manifest_records(manifest_records)
    from private_truth import build_private

    answers = build_private()["answers"]
    return [
        {
            "prompt_id": record["prompt_id"],
            "raw_response": json.dumps(
                answers[record["situation_id"]][record["task_id"]]["value"],
                ensure_ascii=False,
                separators=(",", ":"),
            ),
        }
        for record in manifest_records
    ]


def run_oracle(
    manifest_records: Sequence[Mapping[str, Any]] | None = None,
    *,
    commit: str | None = None,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Run the complete synthetic/oracle plumbing check through normal scoring."""

    prompts = (
        list(manifest_records)
        if manifest_records is not None
        else build_prompt_records()
    )
    responses = build_oracle_responses(prompts)
    results, summary = score_imported_responses(
        prompts,
        responses,
        model_id="synthetic/oracle",
        model_revision=None,
        generation_settings={"mode": "synthetic_oracle"},
        commit=commit,
    )
    summary["synthetic_oracle"] = True
    return results, summary


def write_results(
    path: str | Path,
    results: Sequence[Mapping[str, Any]],
    summary: Mapping[str, Any],
) -> dict[str, Any]:
    """Write scored result records and a compact provenance/summary sidecar."""

    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(serialize_jsonl(results))
    metadata = {
        "artifact_kind": "scored_results",
        "summary": dict(summary),
    }
    if results:
        first = results[0]
        metadata.update(
            {
                "gold_set_version": first["gold_set_version"],
                "repository_commit": first["repository_commit"],
                "manifest_sha256": first["manifest_sha256"],
                "model_id": first["model_id"],
                "model_revision": first["model_revision"],
                "generation_settings": first["generation_settings"],
            }
        )
    _write_json(_metadata_path(output_path), metadata)
    return metadata


def _parse_settings(raw: str) -> dict[str, Any]:
    try:
        settings = json.loads(
            raw,
            parse_constant=_reject_nonstandard_json_constant,
        )
    except (json.JSONDecodeError, ValueError) as exc:
        raise RunnerError(f"generation settings are not valid JSON: {exc}") from exc
    if not isinstance(settings, dict):
        raise RunnerError("generation settings must be a JSON object")
    return settings


def _build_cli() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    materialize = subparsers.add_parser(
        "materialize", help="write the canonical 560-prompt public JSONL manifest"
    )
    materialize.add_argument("--output", required=True, type=Path)

    score = subparsers.add_parser(
        "score", help="strictly import and score an external response JSONL file"
    )
    score.add_argument("--manifest", required=True, type=Path)
    score.add_argument("--responses", required=True, type=Path)
    score.add_argument("--output", required=True, type=Path)
    score.add_argument("--model-id", required=True)
    score.add_argument("--model-revision")
    score.add_argument("--generation-settings", required=True)
    score.add_argument("--allow-partial", action="store_true")

    oracle = subparsers.add_parser(
        "oracle", help="run the explicitly synthetic 560/560 plumbing check"
    )
    oracle.add_argument("--manifest", type=Path)
    oracle.add_argument("--output", required=True, type=Path)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = _build_cli()
    args = parser.parse_args(argv)
    try:
        if args.command == "materialize":
            metadata = write_prompt_manifest(args.output)
            print(canonical_json(metadata))
            return 0

        manifest_records = read_jsonl(args.manifest) if args.manifest else None
        if args.command == "score":
            results, summary = score_imported_responses(
                manifest_records,
                read_jsonl(args.responses),
                model_id=args.model_id,
                model_revision=args.model_revision,
                generation_settings=_parse_settings(args.generation_settings),
                allow_partial=args.allow_partial,
            )
        else:
            results, summary = run_oracle(manifest_records)
        write_results(args.output, results, summary)
        print(canonical_json(summary))
        return 0
    except ResponseImportError as exc:
        print(canonical_json({"error": str(exc), **exc.summary}), file=sys.stderr)
        return 2
    except (RunnerError, OSError) as exc:
        print(canonical_json({"error": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
