"""Write-once execution helpers for issue #32 Checkpoint-B v2.

This runner creates only the 14 amended intuition samples and their blind
leakage reviews.  It deliberately has no formal-worker, Lean, result, or
historical-draw interface.  Existing output paths make every invocation fail
closed so a capture can never be silently retried or replaced.
"""

from __future__ import annotations

import argparse
import json
import uuid
from pathlib import Path
from typing import Any, Sequence

from .canonical import canonical_json, text_sha256
from .checkpoint_a import render_generator_prompt, render_leakage_review_prompt
from .checkpoint_a_v2 import read_checkpoint_a_v2
from .checkpoint_b_runner import (
    GENERATOR_ROLES,
    THEOREM_IDS,
    _run_codex,
    _sha256_bytes,
    _utc_now,
    _write_json_once,
    _write_once,
)
from .panel import Presentation, generator_payload
from .records import deterministic_leakage_flags

BREVITY_INSTRUCTION = "Keep the entire strategy to at most 45 words."
_STRATEGY_SUFFIX = "\n\nStrategy:\n"
_SCHEMA_PATH = Path(__file__).with_name("checkpoint_b_output_schema.json")


def render_generator_prompt_v2(theorem_id: str) -> str:
    """Insert only the prospective common brevity sentence into the v1 prompt."""

    prompt_v1 = render_generator_prompt(theorem_id)
    if not prompt_v1.endswith(_STRATEGY_SUFFIX):
        raise RuntimeError("Checkpoint-B v1 prompt has unexpected structure")
    request_end = prompt_v1[: -len(_STRATEGY_SUFFIX)]
    return f"{request_end}\n{BREVITY_INSTRUCTION}{_STRATEGY_SUFFIX}"


def _codex_generation(output_dir: Path, theorem_id: str) -> None:
    read_checkpoint_a_v2()
    if theorem_id not in THEOREM_IDS:
        raise ValueError(f"unknown theorem id: {theorem_id}")
    record_path = output_dir / f"codex_reference_{theorem_id}.json"
    transcript_path = output_dir / "transcripts" / f"codex_reference_{theorem_id}.jsonl"
    stderr_path = output_dir / "transcripts" / f"codex_reference_{theorem_id}.stderr"
    for path in (record_path, transcript_path, stderr_path):
        if path.exists():
            raise RuntimeError(f"capture already exists; retry forbidden: {path}")

    prompt = render_generator_prompt_v2(theorem_id)
    capture_identity = f"checkpoint_b_v2_codex_reference_{theorem_id}_{uuid.uuid4()}"
    run = _run_codex(prompt)
    transcript_bytes = run.pop("stdout").encode("utf-8")
    stderr_bytes = run.pop("stderr").encode("utf-8")
    _write_once(transcript_path, transcript_bytes)
    _write_once(stderr_path, stderr_bytes)
    record = {
        "schema_version": "checkpoint_b_v2_codex_generation_v1",
        "theorem_id": theorem_id,
        "presentation": Presentation.STANDARD.value,
        "sample_index": 0,
        "capture_identity": capture_identity,
        "prompt_sha256": text_sha256(prompt),
        "transcript_path": str(transcript_path.relative_to(output_dir)),
        "transcript_sha256": _sha256_bytes(transcript_bytes),
        "stderr_path": str(stderr_path.relative_to(output_dir)),
        "stderr_sha256": _sha256_bytes(stderr_bytes),
        **run,
    }
    _write_json_once(record_path, record)


def _qwen_generation(output_dir: Path) -> None:
    freeze = read_checkpoint_a_v2()
    record_path = output_dir / "qwen_base.json"
    if record_path.exists():
        raise RuntimeError(f"capture already exists; retry forbidden: {record_path}")

    try:
        import torch
        import transformers
        import vllm
        from transformers import AutoTokenizer
        from vllm import LLM, SamplingParams
        from vllm.inputs import TokensPrompt
    except ImportError as error:
        raise RuntimeError(
            "frozen Qwen inference environment is unavailable"
        ) from error

    if vllm.__version__ != "0.10.2":
        raise RuntimeError("vLLM version does not match Checkpoint A")
    if not torch.cuda.is_available():
        raise RuntimeError("project-controlled local CUDA is unavailable")
    free_bytes, _ = torch.cuda.mem_get_info()
    if free_bytes < 18_000_000_000:
        raise RuntimeError("shared Ada GPU is not free; no generation was attempted")

    protocol = freeze.base_v1.value["generator_protocol"]["qwen_base"]
    tokenizer = AutoTokenizer.from_pretrained(
        protocol["tokenizer"],
        revision=protocol["tokenizer_revision"],
        local_files_only=True,
        trust_remote_code=False,
    )
    prompts = {
        theorem_id: render_generator_prompt_v2(theorem_id) for theorem_id in THEOREM_IDS
    }
    prompt_token_ids = {
        theorem_id: tokenizer.encode(prompt, add_special_tokens=False)
        for theorem_id, prompt in prompts.items()
    }
    runtime = {
        "max_model_len": 2048,
        "gpu_memory_utilization": 0.95,
        "max_num_seqs": 7,
        "enforce_eager": True,
    }
    started_at = _utc_now()
    model = LLM(
        model=protocol["model"],
        revision=protocol["revision"],
        tokenizer=protocol["tokenizer"],
        tokenizer_revision=protocol["tokenizer_revision"],
        dtype=protocol["dtype"],
        quantization=protocol["quantization"],
        tensor_parallel_size=protocol["tensor_parallel_size"],
        trust_remote_code=False,
        **runtime,
    )
    sampling = SamplingParams(
        n=1,
        best_of=1,
        temperature=protocol["temperature"],
        top_p=protocol["top_p"],
        top_k=protocol["top_k"],
        max_tokens=protocol["max_new_tokens"],
        seed=protocol["seed"],
        stop_token_ids=[tokenizer.eos_token_id],
    )
    requests = [
        TokensPrompt(prompt_token_ids=prompt_token_ids[theorem_id])
        for theorem_id in THEOREM_IDS
    ]
    generated = model.generate(requests, sampling, use_tqdm=False)
    finished_at = _utc_now()
    if len(generated) != len(THEOREM_IDS):
        raise RuntimeError("Qwen returned an incomplete batch; retry forbidden")
    captures: list[dict[str, Any]] = []
    for theorem_id, request_output in zip(THEOREM_IDS, generated, strict=True):
        if len(request_output.outputs) != 1:
            raise RuntimeError("Qwen returned an invalid sample count; retry forbidden")
        output = request_output.outputs[0]
        captures.append(
            {
                "theorem_id": theorem_id,
                "presentation": Presentation.STANDARD.value,
                "sample_index": 0,
                "capture_identity": (
                    f"checkpoint_b_v2_qwen_base_{theorem_id}_{uuid.uuid4()}"
                ),
                "prompt_sha256": text_sha256(prompts[theorem_id]),
                "prompt_token_ids": prompt_token_ids[theorem_id],
                "prompt_token_ids_sha256": text_sha256(
                    canonical_json(prompt_token_ids[theorem_id])
                ),
                "raw_text": output.text,
                "generated_token_ids": list(output.token_ids),
                "finish_reason": output.finish_reason,
                "stop_reason": output.stop_reason,
            }
        )
    record = {
        "schema_version": "checkpoint_b_v2_qwen_generation_v1",
        "started_at_utc": started_at,
        "finished_at_utc": finished_at,
        "generator_config": protocol,
        "runtime": {
            **runtime,
            "inference_execution": "project_controlled_local_cuda",
            "gpu": torch.cuda.get_device_name(0),
            "vllm": vllm.__version__,
            "transformers": transformers.__version__,
            "torch": torch.__version__,
        },
        "captures": captures,
    }
    _write_json_once(record_path, record)


def _load_generation(output_dir: Path, theorem_id: str, role: str) -> dict[str, Any]:
    if role == "codex_reference":
        record = json.loads(
            (output_dir / f"codex_reference_{theorem_id}.json").read_text(
                encoding="utf-8"
            )
        )
        return {
            "raw_text": record["final_message"],
            "valid_capture": record["valid_capture"],
        }
    record = json.loads((output_dir / "qwen_base.json").read_text(encoding="utf-8"))
    capture = next(
        item for item in record["captures"] if item["theorem_id"] == theorem_id
    )
    return {"raw_text": capture["raw_text"], "valid_capture": True}


def _leakage_review(
    output_dir: Path, theorem_id: str, role: str, reviewer_index: int
) -> None:
    read_checkpoint_a_v2()
    if theorem_id not in THEOREM_IDS:
        raise ValueError(f"unknown theorem id: {theorem_id}")
    if role not in GENERATOR_ROLES:
        raise ValueError(f"unknown generator role: {role}")
    if reviewer_index not in (0, 1):
        raise ValueError("reviewer index must be 0 or 1")
    record_path = (
        output_dir / "leakage" / f"{role}_{theorem_id}_reviewer_{reviewer_index}.json"
    )
    transcript_path = (
        output_dir
        / "transcripts"
        / f"leakage_{role}_{theorem_id}_reviewer_{reviewer_index}.jsonl"
    )
    stderr_path = (
        output_dir
        / "transcripts"
        / f"leakage_{role}_{theorem_id}_reviewer_{reviewer_index}.stderr"
    )
    for path in (record_path, transcript_path, stderr_path):
        if path.exists():
            raise RuntimeError(f"review already exists; retry forbidden: {path}")

    generation = _load_generation(output_dir, theorem_id, role)
    if not generation["valid_capture"] or not isinstance(generation["raw_text"], str):
        _write_json_once(
            record_path,
            {
                "schema_version": "checkpoint_b_v2_leakage_review_v1",
                "theorem_id": theorem_id,
                "generator_role": role,
                "reviewer_index": reviewer_index,
                "model_invoked": False,
                "status": "missing_generator_capture",
                "label": "borderline",
                "uncertain": True,
            },
        )
        return

    statement = generator_payload(theorem_id, Presentation.STANDARD)[
        "theorem_statement"
    ]
    prompt = render_leakage_review_prompt(
        theorem_statement=statement,
        candidate_guidance=generation["raw_text"],
    )
    flags = deterministic_leakage_flags(
        {
            "theorem_statement": statement,
            "candidate_guidance": generation["raw_text"],
        }
    )
    if flags:
        _write_json_once(
            record_path,
            {
                "schema_version": "checkpoint_b_v2_leakage_review_v1",
                "theorem_id": theorem_id,
                "generator_role": role,
                "reviewer_index": reviewer_index,
                "model_invoked": False,
                "status": "deterministic_overt_lean_marker",
                "flags": list(flags),
                "prompt_sha256": text_sha256(prompt),
                "label": "proof_like",
                "uncertain": False,
            },
        )
        return

    capture_identity = (
        f"checkpoint_b_v2_leakage_{role}_{theorem_id}_reviewer_"
        f"{reviewer_index}_{uuid.uuid4()}"
    )
    run = _run_codex(prompt, output_schema=_SCHEMA_PATH)
    transcript_bytes = run.pop("stdout").encode("utf-8")
    stderr_bytes = run.pop("stderr").encode("utf-8")
    _write_once(transcript_path, transcript_bytes)
    _write_once(stderr_path, stderr_bytes)
    parsed_output: dict[str, Any] | None = None
    if run["valid_capture"]:
        try:
            candidate = json.loads(run["final_message"])
            if (
                isinstance(candidate, dict)
                and set(candidate) == {"label", "uncertain"}
                and candidate["label"] in {"strategic", "borderline", "proof_like"}
                and isinstance(candidate["uncertain"], bool)
            ):
                parsed_output = candidate
        except (TypeError, json.JSONDecodeError):
            pass
    if parsed_output is None:
        parsed_output = {"label": "borderline", "uncertain": True}
        status = "invalid_or_missing_review"
    else:
        status = "valid_model_review"
    record = {
        "schema_version": "checkpoint_b_v2_leakage_review_v1",
        "theorem_id": theorem_id,
        "generator_role": role,
        "reviewer_index": reviewer_index,
        "capture_identity": capture_identity,
        "model_invoked": True,
        "status": status,
        "prompt_sha256": text_sha256(prompt),
        "transcript_path": str(transcript_path.relative_to(output_dir)),
        "transcript_sha256": _sha256_bytes(transcript_bytes),
        "stderr_path": str(stderr_path.relative_to(output_dir)),
        "stderr_sha256": _sha256_bytes(stderr_bytes),
        "label": parsed_output["label"],
        "uncertain": parsed_output["uncertain"],
        **run,
    }
    _write_json_once(record_path, record)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    codex = subparsers.add_parser("codex-generate")
    codex.add_argument("output_dir", type=Path)
    codex.add_argument("theorem_id", choices=THEOREM_IDS)

    qwen = subparsers.add_parser("qwen-generate")
    qwen.add_argument("output_dir", type=Path)

    leakage = subparsers.add_parser("leakage-review")
    leakage.add_argument("output_dir", type=Path)
    leakage.add_argument("theorem_id", choices=THEOREM_IDS)
    leakage.add_argument("generator_role", choices=GENERATOR_ROLES)
    leakage.add_argument("reviewer_index", type=int, choices=(0, 1))
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "codex-generate":
        _codex_generation(args.output_dir, args.theorem_id)
    elif args.command == "qwen-generate":
        _qwen_generation(args.output_dir)
    else:
        _leakage_review(
            args.output_dir,
            args.theorem_id,
            args.generator_role,
            args.reviewer_index,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
