from __future__ import annotations

import hashlib
import json
import math
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Mapping, Protocol, Sequence

from experiments.mathia_corpus import interchange


CONFIG_SCHEMA_VERSION = "qwen-mathia-v1-config-v1"
MANIFEST_SCHEMA_VERSION = "qwen-mathia-v1-training-manifest-v1"
BASE_MODEL_ID = "Qwen/Qwen3-8B-Base"
BASE_REVISION = "49e3418fbbbca6ecbdf9608b4d22e5a407081db4"
RELEASE_ID = "agnostic-mathia-full-v1"
FREEZE_ID = "freeze_eeeeb89af3d2ac75d1ff5dad5623b63d1d24dfbddb965beca2f1c4aac9f9867f"
IGNORE_INDEX = -100
OPTIMIZER_ROLES = ("interpretation", "synthesis")
TARGET_MODULES = (
    "q_proj",
    "k_proj",
    "v_proj",
    "o_proj",
    "gate_proj",
    "up_proj",
    "down_proj",
)


class Tokenizer(Protocol):
    eos_token_id: int | None
    pad_token_id: int | None
    name_or_path: str

    def encode(self, text: str, *, add_special_tokens: bool) -> Sequence[int]: ...


def repository_root() -> Path:
    return Path(__file__).resolve().parents[2]


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


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


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


@dataclass(frozen=True)
class QwenMathiaConfig:
    path: Path
    value: dict[str, Any]

    @classmethod
    def load(cls, path: Path) -> QwenMathiaConfig:
        value = json.loads(path.read_text(encoding="utf-8"))
        config = cls(path=path.resolve(), value=value)
        config.validate()
        return config

    @property
    def model(self) -> dict[str, Any]:
        return self.value["model"]

    @property
    def corpus(self) -> dict[str, Any]:
        return self.value["corpus"]

    @property
    def quantization(self) -> dict[str, Any]:
        return self.value["quantization"]

    @property
    def lora(self) -> dict[str, Any]:
        return self.value["lora"]

    @property
    def training(self) -> dict[str, Any]:
        return self.value["training"]

    @property
    def config_sha256(self) -> str:
        return sha256_text(canonical_json(self.value))

    @property
    def release_root(self) -> Path:
        return repository_root() / str(self.corpus["release_root"])

    def validate(self) -> None:
        if self.value.get("schema_version") != CONFIG_SCHEMA_VERSION:
            raise ValueError("unknown Qwen-Mathia v1 configuration schema")
        required = (
            (("model", "model_id"), BASE_MODEL_ID),
            (("model", "model_revision"), BASE_REVISION),
            (("model", "tokenizer_id"), BASE_MODEL_ID),
            (("model", "tokenizer_revision"), BASE_REVISION),
            (("model", "add_special_tokens"), False),
            (("model", "chat_template"), None),
            (("corpus", "release_id"), RELEASE_ID),
            (("corpus", "freeze_id"), FREEZE_ID),
            (("corpus", "contract_version"), interchange.CONTRACT_VERSION),
            (("corpus", "optimizer_roles"), list(OPTIMIZER_ROLES)),
            (("serialization", "prompt_loss_masked"), True),
            (("serialization", "response_supervised"), True),
            (("serialization", "eos_supervised"), True),
            (("ordering", "selected_order"), "object_id_utf8_ascending"),
            (("ordering", "shuffle_seed"), 0),
            (("quantization", "load_in_4bit"), True),
            (("quantization", "quantization_type"), "nf4"),
            (("quantization", "double_quantization"), True),
            (("quantization", "compute_dtype"), "bfloat16"),
            (("lora", "task_type"), "CAUSAL_LM"),
            (("lora", "r"), 16),
            (("lora", "lora_alpha"), 32),
            (("lora", "lora_dropout"), 0.0),
            (("lora", "bias"), "none"),
            (("lora", "modules_to_save"), None),
            (("training", "per_device_micro_batch_size"), 1),
            (("training", "gradient_accumulation_steps"), 8),
            (("training", "epochs"), 4),
            (("training", "learning_rate"), 5e-5),
            (("training", "weight_decay"), 0.0),
            (("training", "maximum_gradient_norm"), 1.0),
            (("training", "lr_schedule"), "cosine"),
            (("training", "optimizer"), "paged_adamw_8bit"),
            (("training", "maximum_sequence_tokens"), 768),
            (("training", "packing"), False),
            (("training", "truncation"), False),
            (("training", "gradient_checkpointing"), True),
            (("training", "seed"), 0),
            (("training", "checkpoint_epochs"), [1, 2, 4]),
            (("publication", "repository_id"), "murillo2000/qwen3-8b-base-mathia-v1"),
            (("publication", "artifact_format"), "peft-lora"),
            (("publication", "hub_license"), "other"),
        )
        for path, wanted in required:
            observed: Any = self.value
            for key in path:
                observed = observed[key]
            if observed != wanted:
                raise ValueError(
                    f"{'.'.join(path)} must be {wanted!r}, got {observed!r}"
                )
        if tuple(self.lora["target_modules"]) != TARGET_MODULES:
            raise ValueError("LoRA target module order differs from issue #47")
        smoke_ids = self.value["smoke"]["object_ids"]
        sanity_ids = self.value["technical_sanity"]["object_ids"]
        if len(smoke_ids) != 2 or len(set(smoke_ids)) != 2 or smoke_ids != sanity_ids:
            raise ValueError("smoke and sanity must pin the same two distinct examples")


@dataclass(frozen=True)
class TokenizedExample:
    object_id: str
    object_role: str
    prompt: str
    response: str
    rendered_text: str
    input_ids: tuple[int, ...]
    labels: tuple[int, ...]
    attention_mask: tuple[int, ...]
    prompt_tokens: int
    response_tokens: int

    @property
    def total_tokens(self) -> int:
        return len(self.input_ids)

    def validate(self, eos_token_id: int, maximum_sequence_tokens: int) -> None:
        if self.rendered_text != self.prompt + self.response:
            raise ValueError(
                f"{self.object_id}: prompt/response boundary changed visible bytes"
            )
        if not (
            len(self.input_ids) == len(self.labels) == len(self.attention_mask)
            and len(self.input_ids) == self.prompt_tokens + self.response_tokens + 1
        ):
            raise ValueError(f"{self.object_id}: tokenized lengths disagree")
        if self.total_tokens > maximum_sequence_tokens:
            raise ValueError(
                f"{self.object_id}: {self.total_tokens} tokens exceeds "
                f"{maximum_sequence_tokens}; truncation is forbidden"
            )
        if self.input_ids[-1] != eos_token_id or self.labels[-1] != eos_token_id:
            raise ValueError(f"{self.object_id}: terminal EOS is not supervised")
        if self.labels[: self.prompt_tokens] != (IGNORE_INDEX,) * self.prompt_tokens:
            raise ValueError(f"{self.object_id}: prompt token supervision leaked")
        if any(label == IGNORE_INDEX for label in self.labels[self.prompt_tokens :]):
            raise ValueError(f"{self.object_id}: response or EOS token was masked")
        if self.attention_mask != (1,) * self.total_tokens:
            raise ValueError(f"{self.object_id}: unpadded attention mask is invalid")

    def manifest_row(self, record: Mapping[str, Any]) -> dict[str, Any]:
        return {
            "object_id": self.object_id,
            "object_role": self.object_role,
            "content_sha256": record["content_sha256"],
            "parent_ids": list(record["parent_ids"]),
            "rendered_sha256": sha256_text(self.rendered_text),
            "prompt_sha256": sha256_text(self.prompt),
            "response_sha256": sha256_text(self.response),
            "rendered_bytes": len(self.rendered_text.encode("utf-8")),
            "prompt_tokens": self.prompt_tokens,
            "response_tokens": self.response_tokens,
            "eos_tokens": 1,
            "total_tokens": self.total_tokens,
            "loss_mask": {
                "masked_token_range": [0, self.prompt_tokens],
                "supervised_token_range": [self.prompt_tokens, self.total_tokens],
                "eos_token_index": self.total_tokens - 1,
            },
        }


def load_pinned_tokenizer(
    config: QwenMathiaConfig, *, cache_dir: Path | None = None
) -> Any:
    try:
        from transformers import AutoTokenizer
    except ImportError as error:
        raise RuntimeError("tokenizer audit requires transformers") from error
    tokenizer = AutoTokenizer.from_pretrained(
        str(config.model["tokenizer_id"]),
        revision=str(config.model["tokenizer_revision"]),
        trust_remote_code=False,
        cache_dir=None if cache_dir is None else str(cache_dir),
    )
    if tokenizer.eos_token_id is None:
        raise RuntimeError("the frozen tokenizer has no EOS token")
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"
    return tokenizer


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def verify_frozen_release(config: QwenMathiaConfig) -> dict[str, Any]:
    root = config.release_root
    observed: dict[str, str] = {}
    for relative, wanted in config.corpus["frozen_files"].items():
        path = root / str(relative)
        got = sha256_file(path)
        if got != wanted:
            raise ValueError(f"frozen corpus hash mismatch for {relative}: {got}")
        observed[str(relative)] = got
    freeze = _read_json(root / "freeze.json")
    if freeze.get("freeze_id") != FREEZE_ID or freeze.get("release_id") != RELEASE_ID:
        raise ValueError("frozen corpus identity differs from issue #47")
    return {
        "release_id": RELEASE_ID,
        "freeze_id": FREEZE_ID,
        "contract_version": interchange.CONTRACT_VERSION,
        "verified_file_sha256": observed,
    }


def load_selected_records(
    config: QwenMathiaConfig,
) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]], dict[str, Any]]:
    verify_frozen_release(config)
    records = interchange.load_jsonl(config.release_root / "records.jsonl")
    by_id = {str(record["object_id"]): record for record in records}
    errors = interchange.validate_release(
        records, lambda record: str(record["content"])
    )
    if errors:
        raise ValueError("frozen release no longer validates: " + "; ".join(errors[:5]))
    release_manifest = _read_json(config.release_root / "trainable_manifest.json")
    eligible_ids = set(release_manifest["eligible_object_ids"])
    accepted_ids = {
        str(record["object_id"])
        for record in records
        if record.get("quality_state") == "accepted"
        and record.get("training_eligibility") == "eligible"
    }
    if eligible_ids != accepted_ids:
        raise ValueError("release manifest eligibility differs from frozen records")
    selected = sorted(
        (
            record
            for record in records
            if record["object_id"] in eligible_ids
            and record["object_role"] in OPTIMIZER_ROLES
        ),
        key=lambda record: str(record["object_id"]),
    )
    counts = Counter(str(record["object_role"]) for record in selected)
    if counts != Counter({"interpretation": 98, "synthesis": 18}):
        raise ValueError(f"optimizer role counts differ from frozen contract: {counts}")
    for record in selected:
        if (
            record["corpus_release_id"] != RELEASE_ID
            or record["corpus_origin"] != "agnostic"
            or record["quality_state"] != "accepted"
            or record["training_eligibility"] != "eligible"
        ):
            raise ValueError(
                f"{record['object_id']}: excluded or foreign object selected"
            )
    exclusion_counts = Counter(
        str(record["quality_state"])
        for record in records
        if record["quality_state"] != "accepted"
    )
    return (
        selected,
        by_id,
        {
            "eligible_release_objects": len(eligible_ids),
            "selected_optimizer_objects": len(selected),
            "selected_role_counts": dict(sorted(counts.items())),
            "excluded_object_counts": dict(sorted(exclusion_counts.items())),
            "selected_are_all_accepted_and_eligible": True,
            "excluded_or_evaluation_objects_selected": 0,
            "source_objects_selected_as_standalone_targets": 0,
            "riemann_objects_selected": 0,
        },
    )


def split_canonical_rendering(
    record: Mapping[str, Any], records_by_id: Mapping[str, Mapping[str, Any]]
) -> tuple[str, str, str]:
    def loader(item: Mapping[str, Any]) -> str:
        return str(item["content"])

    rendered = interchange.render_training_example(record, records_by_id, loader)
    response = interchange.record_content(record, loader) + "\n"
    if not rendered.endswith(response) or len(rendered) == len(response):
        raise ValueError(
            f"{record['object_id']}: canonical response boundary is ambiguous"
        )
    prompt = rendered[: -len(response)]
    if not prompt.endswith("## Response\n\n"):
        raise ValueError(f"{record['object_id']}: canonical response heading changed")
    return prompt, response, rendered


def tokenize_record(
    record: Mapping[str, Any],
    records_by_id: Mapping[str, Mapping[str, Any]],
    tokenizer: Tokenizer,
    maximum_sequence_tokens: int,
) -> TokenizedExample:
    if tokenizer.eos_token_id is None:
        raise ValueError("tokenizer has no EOS token")
    prompt, response, rendered = split_canonical_rendering(record, records_by_id)
    prompt_ids = tuple(tokenizer.encode(prompt, add_special_tokens=False))
    response_ids = tuple(tokenizer.encode(response, add_special_tokens=False))
    input_ids = prompt_ids + response_ids + (int(tokenizer.eos_token_id),)
    example = TokenizedExample(
        object_id=str(record["object_id"]),
        object_role=str(record["object_role"]),
        prompt=prompt,
        response=response,
        rendered_text=rendered,
        input_ids=input_ids,
        labels=(IGNORE_INDEX,) * len(prompt_ids)
        + response_ids
        + (int(tokenizer.eos_token_id),),
        attention_mask=(1,) * len(input_ids),
        prompt_tokens=len(prompt_ids),
        response_tokens=len(response_ids),
    )
    example.validate(int(tokenizer.eos_token_id), maximum_sequence_tokens)
    full_ids = tuple(tokenizer.encode(rendered, add_special_tokens=False))
    if full_ids != prompt_ids + response_ids:
        raise ValueError(f"{record['object_id']}: tokenizer crosses the loss boundary")
    decoder = getattr(tokenizer, "decode", None)
    if callable(decoder):
        decoded = decoder(
            list(full_ids),
            skip_special_tokens=False,
            clean_up_tokenization_spaces=False,
        )
        if decoded != rendered:
            raise ValueError(
                f"{record['object_id']}: tokenization changes visible bytes"
            )
    return example


def _distribution(values: list[int]) -> dict[str, int]:
    ordered = sorted(values)
    if not ordered:
        raise ValueError("cannot summarize an empty distribution")

    def percentile(fraction: float) -> int:
        return ordered[math.ceil(len(ordered) * fraction) - 1]

    return {
        "minimum": ordered[0],
        "p50": percentile(0.50),
        "p90": percentile(0.90),
        "p95": percentile(0.95),
        "p99": percentile(0.99),
        "maximum": ordered[-1],
        "sum": sum(ordered),
    }


def build_training_manifest(
    config: QwenMathiaConfig, tokenizer: Tokenizer
) -> tuple[dict[str, Any], list[TokenizedExample]]:
    release_identity = verify_frozen_release(config)
    records, by_id, selection_audit = load_selected_records(config)
    maximum = int(config.training["maximum_sequence_tokens"])
    examples = [
        tokenize_record(record, by_id, tokenizer, maximum) for record in records
    ]
    rows = [example.manifest_row(by_id[example.object_id]) for example in examples]
    true_maximum = max(example.total_tokens for example in examples)
    multiple = int(config.training["clean_sequence_multiple"])
    clean_bound = math.ceil(true_maximum / multiple) * multiple
    if clean_bound != maximum:
        raise ValueError(
            f"configured maximum {maximum} is not the smallest {multiple}-token "
            f"bound for observed maximum {true_maximum}"
        )
    role_statistics: dict[str, Any] = {}
    for role in OPTIMIZER_ROLES:
        role_examples = [item for item in examples if item.object_role == role]
        role_statistics[role] = {
            "examples": len(role_examples),
            "prompt_tokens": _distribution(
                [item.prompt_tokens for item in role_examples]
            ),
            "response_tokens": _distribution(
                [item.response_tokens for item in role_examples]
            ),
            "total_tokens_including_eos": _distribution(
                [item.total_tokens for item in role_examples]
            ),
        }
    selected_ids = [example.object_id for example in examples]
    body = {
        "schema_version": MANIFEST_SCHEMA_VERSION,
        "config_sha256": config.config_sha256,
        "model": dict(config.model),
        "tokenizer": {
            "tokenizer_id": config.model["tokenizer_id"],
            "tokenizer_revision": config.model["tokenizer_revision"],
            "tokenizer_class": type(tokenizer).__name__,
            "eos_token_id": int(tokenizer.eos_token_id),
            "pad_token_id": int(tokenizer.pad_token_id)
            if tokenizer.pad_token_id is not None
            else None,
        },
        "corpus": release_identity,
        "selection_audit": selection_audit,
        "serialization": dict(config.value["serialization"]),
        "ordering": {
            **config.value["ordering"],
            "selected_object_ids": selected_ids,
            "selected_order_sha256": sha256_text("\n".join(selected_ids) + "\n"),
        },
        "sequence_bound": {
            "true_maximum_sequence_tokens": true_maximum,
            "configured_maximum_sequence_tokens": maximum,
            "clean_sequence_multiple": multiple,
            "smallest_clean_bound": clean_bound,
            "truncated_examples": 0,
        },
        "role_statistics": role_statistics,
        "totals_per_epoch": {
            "examples": len(examples),
            "prompt_tokens": sum(item.prompt_tokens for item in examples),
            "response_tokens": sum(item.response_tokens for item in examples),
            "supervised_tokens_including_eos": sum(
                item.response_tokens + 1 for item in examples
            ),
            "all_tokens_including_eos": sum(item.total_tokens for item in examples),
        },
        "examples": rows,
    }
    body["manifest_id"] = "training_manifest_" + sha256_text(canonical_json(body))
    return body, examples


def load_workload(
    config: QwenMathiaConfig,
    manifest_path: Path,
    *,
    tokenizer: Tokenizer | None = None,
    cache_dir: Path | None = None,
) -> tuple[dict[str, Any], list[TokenizedExample], Any]:
    if tokenizer is None:
        tokenizer = load_pinned_tokenizer(config, cache_dir=cache_dir)
    observed, examples = build_training_manifest(config, tokenizer)
    committed = _read_json(manifest_path)
    if canonical_json(observed) != canonical_json(committed):
        raise ValueError("training manifest does not reproduce from frozen inputs")
    return committed, examples, tokenizer


def tokenized_example_dict(example: TokenizedExample) -> dict[str, Any]:
    value = asdict(example)
    for key in ("input_ids", "labels", "attention_mask"):
        value[key] = list(value[key])
    return value
