from __future__ import annotations

import hashlib
import importlib.metadata
import json
import math
import platform
import re
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Callable, Mapping, Protocol, Sequence

from experiments.mathia_corpus import interchange


CONFIG_SCHEMA_VERSION = "qwen-mathia-v2-general-design-config-v1"
MANIFEST_SCHEMA_VERSION = "qwen-mathia-v2-general-manifest-v1"
DEDUPE_SCHEMA_VERSION = "qwen-mathia-v2-general-dedupe-v1"
ARCHITECTURE_SCHEMA_VERSION = "qwen-mathia-v2-general-architecture-v1"
BASE_MODEL_ID = "Qwen/Qwen3.5-4B-Base"
BASE_REVISION = "1001bb4d826a52d1f399e183466143f4da7b741b"
OPTIMIZER_ROLES = ("interpretation", "synthesis")
IGNORE_INDEX = -100
ASSISTANT_END_TEXT = "<|im_end|>\n"
LORA_TARGET_SUFFIXES = (
    "q_proj",
    "k_proj",
    "v_proj",
    "o_proj",
    "in_proj_qkv",
    "in_proj_z",
    "in_proj_a",
    "in_proj_b",
    "out_proj",
    "gate_proj",
    "up_proj",
    "down_proj",
)
LORA_TARGET_REGEX = (
    r"^model\.layers\.\d+\."
    r"(?:self_attn\.(?:q_proj|k_proj|v_proj|o_proj)|"
    r"linear_attn\.(?:in_proj_qkv|in_proj_z|in_proj_a|in_proj_b|out_proj)|"
    r"mlp\.(?:gate_proj|up_proj|down_proj))$"
)
EXPECTED_LORA_MODULE_COUNTS = {
    "q_proj": 8,
    "k_proj": 8,
    "v_proj": 8,
    "o_proj": 8,
    "in_proj_qkv": 24,
    "in_proj_z": 24,
    "in_proj_a": 24,
    "in_proj_b": 24,
    "out_proj": 24,
    "gate_proj": 32,
    "up_proj": 32,
    "down_proj": 32,
}


class Tokenizer(Protocol):
    eos_token_id: int | None
    pad_token_id: int | None
    chat_template: str | None

    def encode(self, text: str, *, add_special_tokens: bool) -> Sequence[int]: ...

    def decode(
        self,
        ids: Sequence[int],
        *,
        skip_special_tokens: bool,
        clean_up_tokenization_spaces: bool,
    ) -> str: ...

    def apply_chat_template(self, messages: Sequence[Mapping[str, str]], **kwargs: Any) -> Any: ...

    def convert_tokens_to_ids(self, token: str) -> int: ...


ContentLoader = Callable[[Mapping[str, Any]], str]


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
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


@dataclass(frozen=True)
class DesignConfig:
    path: Path
    value: dict[str, Any]

    @classmethod
    def load(cls, path: Path) -> DesignConfig:
        value = _read_json(path)
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
    def training(self) -> dict[str, Any]:
        return self.value["training"]

    @property
    def lora(self) -> dict[str, Any]:
        return self.value["lora"]

    @property
    def config_sha256(self) -> str:
        return sha256_text(canonical_json(self.value))

    def validate(self) -> None:
        if self.value.get("schema_version") != CONFIG_SCHEMA_VERSION:
            raise ValueError("unknown Qwen-Mathia v2 general configuration schema")
        required = (
            (("exit_decision",), "QWEN_MATHIA_V2_GENERAL_DESIGN_READY"),
            (("model", "model_id"), BASE_MODEL_ID),
            (("model", "model_revision"), BASE_REVISION),
            (("model", "tokenizer_id"), BASE_MODEL_ID),
            (("model", "tokenizer_revision"), BASE_REVISION),
            (("model", "architecture_class"), "Qwen3_5ForCausalLM"),
            (("model", "text_only"), True),
            (("corpus", "contract_version"), interchange.CONTRACT_VERSION),
            (("corpus", "optimizer_roles"), list(OPTIMIZER_ROLES)),
            (("serialization", "chat_template"), "official-pinned-tokenizer"),
            (("serialization", "enable_thinking"), False),
            (("serialization", "add_generation_prompt"), True),
            (("serialization", "prompt_loss_masked"), True),
            (("serialization", "assistant_content_supervised"), True),
            (("serialization", "assistant_end_supervised"), True),
            (("serialization", "assistant_end_text"), ASSISTANT_END_TEXT),
            (("serialization", "system_message"), None),
            (("ordering", "selection_order"), "object_id_utf8_ascending"),
            (("ordering", "training_order"), "sha256(seed_newline_object_id)_ascending"),
            (("ordering", "seed"), 0),
            (("dedupe", "near_duplicate_threshold"), 0.8),
            (("dedupe", "near_duplicates_are_automatically_deleted"), False),
            (("quantization", "load_in_4bit"), True),
            (("quantization", "quantization_type"), "nf4"),
            (("quantization", "double_quantization"), True),
            (("quantization", "compute_dtype"), "bfloat16"),
            (("lora", "target_regex"), LORA_TARGET_REGEX),
            (("lora", "target_suffixes"), list(LORA_TARGET_SUFFIXES)),
            (("lora", "expected_module_counts"), EXPECTED_LORA_MODULE_COUNTS),
            (("lora", "r"), 16),
            (("lora", "lora_alpha"), 32),
            (("lora", "lora_dropout"), 0.0),
            (("lora", "bias"), "none"),
            (("lora", "modules_to_save"), None),
            (("training", "per_device_micro_batch_size"), 1),
            (("training", "gradient_accumulation_steps"), 8),
            (("training", "epochs"), 1.0),
            (("training", "maximum_sequence_tokens"), 9472),
            (("training", "clean_sequence_multiple"), 128),
            (("training", "packing"), False),
            (("training", "truncation"), False),
            (("training", "gradient_checkpointing"), True),
            (("training", "optimizer"), "paged_adamw_8bit"),
            (("training", "learning_rate"), 5e-5),
            (("training", "weight_decay"), 0.0),
            (("training", "maximum_gradient_norm"), 1.0),
            (("training", "lr_schedule"), "cosine"),
            (("training", "seed"), 0),
            (("training", "checkpoint_fractions"), [0.25, 0.5, 1.0]),
            (("publication", "repository_id"), "murillo2000/qwen3.5-4b-base-mathia-v2"),
            (("publication", "artifact_format"), "peft-lora"),
            (("publication", "hub_license"), "other"),
        )
        for path, wanted in required:
            observed: Any = self.value
            for key in path:
                observed = observed[key]
            if observed != wanted:
                raise ValueError(f"{'.'.join(path)} must be {wanted!r}, got {observed!r}")
        if len(self.corpus.get("parents", [])) != 2:
            raise ValueError("G-v2 must bind exactly the #44 and OpenAlex parents")


@dataclass(frozen=True)
class ParentRelease:
    release_id: str
    root: Path
    records_path: Path
    records: tuple[dict[str, Any], ...]
    by_id: dict[str, dict[str, Any]]
    loader: ContentLoader
    rank: int


@dataclass(frozen=True)
class Candidate:
    parent: ParentRelease
    record: dict[str, Any]
    lineage_sha256: str

    @property
    def object_id(self) -> str:
        return str(self.record["object_id"])


@dataclass(frozen=True)
class TokenizedTarget:
    object_id: str
    object_role: str
    parent_release_id: str
    user_content: str
    assistant_content: str
    prompt_text: str
    supervised_text: str
    rendered_text: str
    input_ids: tuple[int, ...]
    labels: tuple[int, ...]
    attention_mask: tuple[int, ...]
    prompt_tokens: int
    assistant_content_tokens: int
    assistant_end_tokens: int

    @property
    def supervised_tokens(self) -> int:
        return self.assistant_content_tokens + self.assistant_end_tokens

    @property
    def total_tokens(self) -> int:
        return len(self.input_ids)

    def validate(self, maximum_sequence_tokens: int) -> None:
        if self.rendered_text != self.prompt_text + self.supervised_text:
            raise ValueError(f"{self.object_id}: visible prompt/target boundary changed")
        if self.supervised_text != self.assistant_content + ASSISTANT_END_TEXT:
            raise ValueError(f"{self.object_id}: assistant target differs from frozen content")
        if len(self.input_ids) != len(self.labels) or len(self.input_ids) != len(self.attention_mask):
            raise ValueError(f"{self.object_id}: token vector lengths disagree")
        if self.total_tokens != self.prompt_tokens + self.supervised_tokens:
            raise ValueError(f"{self.object_id}: token boundary lengths disagree")
        if self.total_tokens > maximum_sequence_tokens:
            raise ValueError(
                f"{self.object_id}: {self.total_tokens} tokens exceeds {maximum_sequence_tokens}; "
                "truncation is forbidden"
            )
        if self.labels[: self.prompt_tokens] != (IGNORE_INDEX,) * self.prompt_tokens:
            raise ValueError(f"{self.object_id}: prompt or assistant prefix supervision leaked")
        if any(label == IGNORE_INDEX for label in self.labels[self.prompt_tokens :]):
            raise ValueError(f"{self.object_id}: assistant response/end supervision was masked")
        if self.attention_mask != (1,) * self.total_tokens:
            raise ValueError(f"{self.object_id}: unpadded attention mask is invalid")


def _verify_files(root: Path, files: Mapping[str, str]) -> dict[str, str]:
    observed: dict[str, str] = {}
    for relative, wanted in files.items():
        path = root / relative
        if not path.is_file():
            raise FileNotFoundError(f"required frozen file is missing: {path}")
        got = sha256_file(path)
        if got != wanted:
            raise ValueError(f"frozen file hash mismatch for {relative}: {got}")
        observed[relative] = got
    return observed


def _supplement_loader(artifact_root: Path, release_id: str) -> ContentLoader:
    resolved = artifact_root.resolve()
    prefix = f"artifact://{release_id}/"

    def load(record: Mapping[str, Any]) -> str:
        if isinstance(record.get("content"), str):
            return str(record["content"])
        reference = str(record.get("content_ref") or "")
        if not reference.startswith(prefix):
            raise ValueError(f"unsupported supplement content reference: {reference}")
        relative = Path(reference.removeprefix(prefix))
        if relative.is_absolute() or ".." in relative.parts:
            raise ValueError(f"unsafe supplement content reference: {reference}")
        return (resolved / relative).read_text(encoding="utf-8")

    return load


def load_parent_releases(config: DesignConfig, supplement_artifact_root: Path) -> tuple[ParentRelease, ...]:
    parents: list[ParentRelease] = []
    for rank, binding in enumerate(config.corpus["parents"]):
        root = repository_root() / str(binding["root"])
        _verify_files(root, binding["frozen_files"])
        release_id = str(binding["release_id"])
        freeze = _read_json(root / str(binding["freeze_file"]))
        if freeze.get("freeze_id") != binding["freeze_id"]:
            raise ValueError(f"{release_id}: freeze identity mismatch")
        if freeze.get("release_id") != release_id:
            raise ValueError(f"{release_id}: release identity mismatch")
        records_path = root / str(binding["records_file"])
        records = _load_jsonl(records_path)
        by_id = {str(record["object_id"]): record for record in records}
        if len(by_id) != len(records):
            raise ValueError(f"{release_id}: duplicate object IDs")
        if binding["kind"] == "inline":
            loader: ContentLoader = lambda record: str(record["content"])
        elif binding["kind"] == "external-content-ref":
            loader = _supplement_loader(supplement_artifact_root, release_id)
            parent = _read_json(root / "parent.json")
            handoff_root = supplement_artifact_root / "openalex_handoffs" / str(parent["concrete_artifact_binding"]["handoff_id"])
            handoff_freeze = _read_json(handoff_root / "freeze.json")
            expected = parent["concrete_artifact_binding"]
            if handoff_freeze.get("freeze_id") != expected["handoff_freeze_id"]:
                raise ValueError("supplement external handoff freeze identity mismatch")
            if handoff_freeze.get("manifest_sha256") != expected["handoff_manifest_sha256"]:
                raise ValueError("supplement external handoff manifest hash mismatch")
        else:
            raise ValueError(f"unknown parent content kind: {binding['kind']}")
        errors = interchange.validate_release(records, loader)
        if errors:
            raise ValueError(f"{release_id} no longer validates: " + "; ".join(errors[:5]))
        manifest = _read_json(root / str(binding["trainable_manifest_file"]))
        eligible_ids = set(manifest["eligible_object_ids"])
        accepted_ids = {
            str(record["object_id"])
            for record in records
            if record["quality_state"] == "accepted" and record["training_eligibility"] == "eligible"
        }
        if eligible_ids != accepted_ids:
            raise ValueError(f"{release_id}: eligible manifest differs from frozen records")
        parents.append(
            ParentRelease(
                release_id=release_id,
                root=root,
                records_path=records_path,
                records=tuple(records),
                by_id=by_id,
                loader=loader,
                rank=rank,
            )
        )
    return tuple(parents)


def _lineage_sha256(record: Mapping[str, Any]) -> str:
    lineage = {
        "canonical_source_keys": sorted(str(item) for item in record.get("canonical_source_keys", [])),
        "source_ids": sorted(str(item) for item in record.get("source_ids", [])),
        "source_unit_ids": sorted(str(item) for item in record.get("source_unit_ids", [])),
        "span_lineage": record.get("span_lineage", []),
        "parent_ids": record.get("parent_ids", []),
    }
    return sha256_text(canonical_json(lineage))


def select_and_dedupe(parents: Sequence[ParentRelease]) -> tuple[list[Candidate], dict[str, Any]]:
    inputs: list[Candidate] = []
    input_counts: Counter[tuple[str, str]] = Counter()
    excluded: Counter[tuple[str, str]] = Counter()
    eligible_release_objects: Counter[str] = Counter()
    for parent in parents:
        for record in parent.records:
            if record.get("training_eligibility") == "eligible":
                eligible_release_objects[parent.release_id] += 1
            if (
                record.get("quality_state") == "accepted"
                and record.get("training_eligibility") == "eligible"
                and record.get("object_role") in OPTIMIZER_ROLES
            ):
                candidate = Candidate(parent, record, _lineage_sha256(record))
                inputs.append(candidate)
                input_counts[(parent.release_id, str(record["object_role"]))] += 1
            elif record.get("quality_state") != "accepted":
                excluded[(parent.release_id, str(record.get("quality_state")))] += 1

    identity_groups: dict[str, list[Candidate]] = defaultdict(list)
    for candidate in inputs:
        identity_groups[candidate.object_id].append(candidate)
    after_identity: list[Candidate] = []
    duplicate_identity_groups: list[dict[str, Any]] = []
    dropped: list[dict[str, Any]] = []
    for object_id, members in sorted(identity_groups.items()):
        ordered = sorted(members, key=lambda item: (item.parent.rank, item.object_id))
        kept = ordered[0]
        if len(ordered) > 1:
            baseline = canonical_json(kept.record)
            if any(canonical_json(item.record) != baseline for item in ordered[1:]):
                raise ValueError(f"conflicting records share object identity {object_id}")
            duplicate_identity_groups.append(
                {"object_id": object_id, "members": [item.parent.release_id for item in ordered]}
            )
            dropped.extend(
                {
                    "object_id": item.object_id,
                    "parent_release_id": item.parent.release_id,
                    "reason": "duplicate_object_identity",
                    "kept_object_id": kept.object_id,
                }
                for item in ordered[1:]
            )
        after_identity.append(kept)

    content_lineage_groups: dict[tuple[str, str], list[Candidate]] = defaultdict(list)
    content_groups: dict[str, list[Candidate]] = defaultdict(list)
    for candidate in after_identity:
        content_hash = str(candidate.record["content_sha256"])
        content_lineage_groups[(content_hash, candidate.lineage_sha256)].append(candidate)
        content_groups[content_hash].append(candidate)

    retained: list[Candidate] = []
    duplicate_content_lineage_groups: list[dict[str, Any]] = []
    for (content_hash, lineage_hash), members in sorted(content_lineage_groups.items()):
        ordered = sorted(members, key=lambda item: (item.parent.rank, item.object_id))
        kept = ordered[0]
        retained.append(kept)
        if len(ordered) > 1:
            duplicate_content_lineage_groups.append(
                {
                    "content_sha256": content_hash,
                    "lineage_sha256": lineage_hash,
                    "members": [
                        {"object_id": item.object_id, "parent_release_id": item.parent.release_id}
                        for item in ordered
                    ],
                }
            )
            dropped.extend(
                {
                    "object_id": item.object_id,
                    "parent_release_id": item.parent.release_id,
                    "reason": "duplicate_content_and_lineage",
                    "kept_object_id": kept.object_id,
                }
                for item in ordered[1:]
            )

    distinct_lineage_collisions = []
    for content_hash, members in sorted(content_groups.items()):
        lineage_hashes = {item.lineage_sha256 for item in members}
        if len(members) > 1 and len(lineage_hashes) > 1:
            distinct_lineage_collisions.append(
                {
                    "content_sha256": content_hash,
                    "decision": "retain_distinct_lineage",
                    "members": [
                        {
                            "object_id": item.object_id,
                            "parent_release_id": item.parent.release_id,
                            "lineage_sha256": item.lineage_sha256,
                        }
                        for item in sorted(members, key=lambda value: value.object_id)
                    ],
                }
            )

    retained.sort(key=lambda item: item.object_id)
    audit = {
        "schema_version": DEDUPE_SCHEMA_VERSION,
        "policy": {
            "identity": "identical object_id requires byte-identical canonical record; keep parent precedence",
            "content_and_lineage": "identical content_sha256 and lineage_sha256; keep parent precedence",
            "same_content_distinct_lineage": "retain and report",
            "near_duplicate": "diagnostic only; never deletes automatically",
            "parent_precedence": [parent.release_id for parent in parents],
        },
        "input_candidate_count": len(inputs),
        "input_counts_by_parent_and_role": {
            f"{parent}|{role}": count for (parent, role), count in sorted(input_counts.items())
        },
        "eligible_release_objects_by_parent": dict(sorted(eligible_release_objects.items())),
        "excluded_quality_counts_by_parent": {
            f"{parent}|{state}": count for (parent, state), count in sorted(excluded.items())
        },
        "duplicate_identity_groups": duplicate_identity_groups,
        "duplicate_content_and_lineage_groups": duplicate_content_lineage_groups,
        "same_content_distinct_lineage_groups": distinct_lineage_collisions,
        "dropped": sorted(dropped, key=lambda item: (item["object_id"], item["parent_release_id"])),
        "retained_count": len(retained),
    }
    return retained, audit


def _chat_ids(tokenizer: Tokenizer, messages: Sequence[Mapping[str, str]], **kwargs: Any) -> tuple[int, ...]:
    result = tokenizer.apply_chat_template(messages, tokenize=True, return_dict=True, **kwargs)
    if isinstance(result, Mapping):
        result = result["input_ids"]
    if result and isinstance(result[0], Sequence) and not isinstance(result[0], (str, bytes, int)):
        if len(result) != 1:
            raise ValueError("chat template unexpectedly returned a batch")
        result = result[0]
    return tuple(int(item) for item in result)


def _split_canonical_example(candidate: Candidate) -> tuple[str, str, str]:
    record = candidate.record
    rendered = interchange.render_training_example(record, candidate.parent.by_id, candidate.parent.loader)
    response = interchange.record_content(record, candidate.parent.loader)
    marker = "## Response\n\n" + response + "\n"
    if not rendered.endswith(marker) or len(rendered) == len(marker):
        raise ValueError(f"{candidate.object_id}: canonical response boundary is ambiguous")
    user_content = rendered[: -len(marker)].rstrip()
    if not user_content.endswith(interchange.INTERPRETATION_REQUEST) and not user_content.endswith(
        interchange.SYNTHESIS_REQUEST
    ):
        raise ValueError(f"{candidate.object_id}: canonical task boundary changed")
    return user_content, response, rendered


def tokenize_candidate(
    candidate: Candidate, tokenizer: Tokenizer, maximum_sequence_tokens: int
) -> TokenizedTarget:
    if not tokenizer.chat_template:
        raise ValueError("pinned tokenizer has no official chat template")
    user_content, assistant_content, _canonical_rendered = _split_canonical_example(candidate)
    user_messages = ({"role": "user", "content": user_content},)
    full_messages = user_messages + ({"role": "assistant", "content": assistant_content},)
    prompt_text = str(
        tokenizer.apply_chat_template(
            user_messages,
            tokenize=False,
            add_generation_prompt=True,
            enable_thinking=False,
        )
    )
    rendered_text = str(
        tokenizer.apply_chat_template(
            full_messages,
            tokenize=False,
            add_generation_prompt=False,
            enable_thinking=False,
        )
    )
    if not rendered_text.startswith(prompt_text):
        raise ValueError(f"{candidate.object_id}: official chat prompt is not a full-render prefix")
    supervised_text = rendered_text[len(prompt_text) :]
    if supervised_text != assistant_content + ASSISTANT_END_TEXT:
        raise ValueError(f"{candidate.object_id}: official assistant target boundary changed")

    prompt_ids = _chat_ids(
        tokenizer,
        user_messages,
        add_generation_prompt=True,
        enable_thinking=False,
    )
    full_ids = _chat_ids(
        tokenizer,
        full_messages,
        add_generation_prompt=False,
        enable_thinking=False,
    )
    if full_ids[: len(prompt_ids)] != prompt_ids:
        raise ValueError(f"{candidate.object_id}: tokenizer crosses prompt/assistant boundary")
    supervised_ids = full_ids[len(prompt_ids) :]
    end_ids = tuple(tokenizer.encode(ASSISTANT_END_TEXT, add_special_tokens=False))
    content_ids = tuple(tokenizer.encode(assistant_content, add_special_tokens=False))
    if supervised_ids != content_ids + end_ids:
        raise ValueError(f"{candidate.object_id}: tokenizer crosses content/end boundary")
    if tokenizer.decode(
        full_ids,
        skip_special_tokens=False,
        clean_up_tokenization_spaces=False,
    ) != rendered_text:
        raise ValueError(f"{candidate.object_id}: tokenization changes visible bytes")

    target = TokenizedTarget(
        object_id=candidate.object_id,
        object_role=str(candidate.record["object_role"]),
        parent_release_id=candidate.parent.release_id,
        user_content=user_content,
        assistant_content=assistant_content,
        prompt_text=prompt_text,
        supervised_text=supervised_text,
        rendered_text=rendered_text,
        input_ids=full_ids,
        labels=(IGNORE_INDEX,) * len(prompt_ids) + supervised_ids,
        attention_mask=(1,) * len(full_ids),
        prompt_tokens=len(prompt_ids),
        assistant_content_tokens=len(content_ids),
        assistant_end_tokens=len(end_ids),
    )
    target.validate(maximum_sequence_tokens)
    return target


def _distribution(values: Sequence[int]) -> dict[str, int]:
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


def _target_statistics(targets: Sequence[TokenizedTarget]) -> dict[str, Any]:
    metrics: dict[str, Callable[[TokenizedTarget], int]] = {
        "prompt_tokens": lambda item: item.prompt_tokens,
        "assistant_content_tokens": lambda item: item.assistant_content_tokens,
        "assistant_end_tokens": lambda item: item.assistant_end_tokens,
        "supervised_tokens": lambda item: item.supervised_tokens,
        "total_tokens": lambda item: item.total_tokens,
    }
    value: dict[str, Any] = {"examples": len(targets)}
    for name, getter in metrics.items():
        values = [getter(item) for item in targets]
        summary = _distribution(values)
        maximum = summary["maximum"]
        if name in {"prompt_tokens", "supervised_tokens", "total_tokens"}:
            summary["longest_object_ids"] = sorted(
                item.object_id for item in targets if getter(item) == maximum
            )
        value[name] = summary
    return value


def _normalized_target(value: str) -> str:
    return re.sub(r"\s+", " ", value.casefold()).strip()


def _token_trigrams(value: str) -> frozenset[tuple[str, ...]]:
    tokens = re.findall(r"\w+|[^\w\s]", value, flags=re.UNICODE)
    width = min(3, len(tokens))
    if width == 0:
        return frozenset()
    return frozenset(tuple(tokens[index : index + width]) for index in range(len(tokens) - width + 1))


def add_near_duplicate_diagnostic(
    audit: dict[str, Any],
    targets: Sequence[TokenizedTarget],
    threshold: float,
) -> dict[str, Any]:
    normalized = {item.object_id: _normalized_target(item.assistant_content) for item in targets}
    shingles = {object_id: _token_trigrams(value) for object_id, value in normalized.items()}
    pairs: list[dict[str, Any]] = []
    for index, left in enumerate(targets):
        for right in targets[index + 1 :]:
            left_shingles = shingles[left.object_id]
            right_shingles = shingles[right.object_id]
            union = left_shingles | right_shingles
            ratio = len(left_shingles & right_shingles) / len(union) if union else 1.0
            if ratio >= threshold:
                pairs.append(
                    {
                        "left_object_id": left.object_id,
                        "left_parent_release_id": left.parent_release_id,
                        "right_object_id": right.object_id,
                        "right_parent_release_id": right.parent_release_id,
                        "token_trigram_jaccard": round(ratio, 6),
                        "decision": "retain_for_manual_mathematical_review",
                    }
                )
    audit = json.loads(json.dumps(audit))
    audit["near_duplicate_diagnostic"] = {
        "scope": "normalized rendered supervised assistant content excluding assistant end control",
        "normalization": "Unicode-preserving casefold plus whitespace collapse",
        "algorithm": "Jaccard similarity over normalized lexical token trigrams",
        "threshold": threshold,
        "automatic_deletion": False,
        "pair_count": len(pairs),
        "pairs": sorted(
            pairs,
            key=lambda item: (
                -item["token_trigram_jaccard"],
                item["left_object_id"],
                item["right_object_id"],
            ),
        ),
    }
    audit["dedupe_report_id"] = "g_v2_dedupe_" + sha256_text(canonical_json(audit))
    return audit


def _source_ancestor_rows(candidate: Candidate) -> list[dict[str, str]]:
    result: list[dict[str, str]] = []
    seen: set[str] = set()

    def visit(record: Mapping[str, Any]) -> None:
        object_id = str(record["object_id"])
        if object_id in seen:
            return
        seen.add(object_id)
        if record["object_role"] == "source":
            result.append(
                {
                    "object_id": object_id,
                    "content_sha256": str(record["content_sha256"]),
                }
            )
            return
        for parent_id in record.get("parent_ids", []):
            visit(candidate.parent.by_id[str(parent_id)])

    visit(candidate.record)
    return sorted(result, key=lambda item: item["object_id"])


def _training_order(targets: Sequence[TokenizedTarget], seed: int) -> list[TokenizedTarget]:
    return sorted(
        targets,
        key=lambda item: (sha256_text(f"{seed}\n{item.object_id}"), item.object_id),
    )


def _exposure_plan(config: DesignConfig, targets: Sequence[TokenizedTarget]) -> dict[str, Any]:
    accumulation = int(config.training["gradient_accumulation_steps"])
    ordered = _training_order(targets, int(config.training["seed"]))
    total_steps = math.ceil(len(ordered) / accumulation)
    checkpoints = []
    for fraction in config.training["checkpoint_fractions"]:
        step = math.ceil(total_steps * float(fraction))
        examples = min(step * accumulation, len(ordered))
        prefix = ordered[:examples]
        checkpoints.append(
            {
                "requested_epoch_fraction": fraction,
                "optimizer_step": step,
                "microbatches_consumed": examples,
                "examples_consumed": examples,
                "actual_example_fraction": examples / len(ordered),
                "token_presentations": {
                    "prompt_tokens": sum(item.prompt_tokens for item in prefix),
                    "assistant_content_tokens": sum(item.assistant_content_tokens for item in prefix),
                    "assistant_end_tokens": sum(item.assistant_end_tokens for item in prefix),
                    "supervised_tokens": sum(item.supervised_tokens for item in prefix),
                    "all_tokens": sum(item.total_tokens for item in prefix),
                },
            }
        )
    return {
        "terminal_epochs": 1.0,
        "effective_batch_size": int(config.training["per_device_micro_batch_size"]) * accumulation,
        "drop_last": False,
        "optimizer_steps": total_steps,
        "final_partial_accumulation_microbatches": len(ordered) % accumulation,
        "training_order_object_ids": [item.object_id for item in ordered],
        "training_order_sha256": sha256_text("\n".join(item.object_id for item in ordered) + "\n"),
        "checkpoints": checkpoints,
    }


def build_materialization(
    config: DesignConfig,
    tokenizer: Tokenizer,
    supplement_artifact_root: Path,
) -> tuple[dict[str, Any], dict[str, Any], list[TokenizedTarget]]:
    parents = load_parent_releases(config, supplement_artifact_root)
    candidates, dedupe = select_and_dedupe(parents)
    maximum = int(config.training["maximum_sequence_tokens"])
    targets = [tokenize_candidate(candidate, tokenizer, maximum) for candidate in candidates]
    if [item.object_id for item in targets] != sorted(item.object_id for item in targets):
        raise ValueError("selection order is not object_id UTF-8 ascending")
    true_maximum = max(item.total_tokens for item in targets)
    multiple = int(config.training["clean_sequence_multiple"])
    smallest_bound = math.ceil(true_maximum / multiple) * multiple
    if smallest_bound != maximum:
        raise ValueError(
            f"configured sequence bound {maximum} is not the smallest {multiple}-token bound "
            f"for observed maximum {true_maximum}"
        )
    dedupe = add_near_duplicate_diagnostic(
        dedupe,
        targets,
        float(config.value["dedupe"]["near_duplicate_threshold"]),
    )
    by_candidate = {candidate.object_id: candidate for candidate in candidates}
    rows = []
    counts_by_source: Counter[str] = Counter()
    for selection_index, target in enumerate(targets):
        candidate = by_candidate[target.object_id]
        record = candidate.record
        for source_id in record.get("source_ids", []):
            counts_by_source[str(source_id)] += 1
        rows.append(
            {
                "selection_index": selection_index,
                "object_id": target.object_id,
                "object_role": target.object_role,
                "parent_release_id": target.parent_release_id,
                "quality_state": record["quality_state"],
                "training_eligibility": record["training_eligibility"],
                "content_sha256": record["content_sha256"],
                "original_record_sha256": sha256_text(canonical_json(record)),
                "lineage_sha256": candidate.lineage_sha256,
                "parent_ids": list(record["parent_ids"]),
                "source_ids": list(record["source_ids"]),
                "source_unit_ids": list(record["source_unit_ids"]),
                "source_ancestors": _source_ancestor_rows(candidate),
                "canonical_user_content_sha256": sha256_text(target.user_content),
                "prompt_sha256": sha256_text(target.prompt_text),
                "assistant_content_sha256": sha256_text(target.assistant_content),
                "supervised_text_sha256": sha256_text(target.supervised_text),
                "rendered_sha256": sha256_text(target.rendered_text),
                "rendered_bytes": len(target.rendered_text.encode("utf-8")),
                "prompt_tokens": target.prompt_tokens,
                "assistant_content_tokens": target.assistant_content_tokens,
                "assistant_end_tokens": target.assistant_end_tokens,
                "supervised_tokens": target.supervised_tokens,
                "total_tokens": target.total_tokens,
                "loss_mask": {
                    "masked_prompt_range": [0, target.prompt_tokens],
                    "supervised_assistant_content_range": [
                        target.prompt_tokens,
                        target.prompt_tokens + target.assistant_content_tokens,
                    ],
                    "supervised_assistant_end_range": [
                        target.prompt_tokens + target.assistant_content_tokens,
                        target.total_tokens,
                    ],
                },
            }
        )

    statistics = {"all": _target_statistics(targets), "by_parent": {}, "by_role": {}, "by_parent_and_role": {}}
    for parent in parents:
        subset = [item for item in targets if item.parent_release_id == parent.release_id]
        statistics["by_parent"][parent.release_id] = _target_statistics(subset)
    for role in OPTIMIZER_ROLES:
        subset = [item for item in targets if item.object_role == role]
        if subset:
            statistics["by_role"][role] = _target_statistics(subset)
    for parent in parents:
        for role in OPTIMIZER_ROLES:
            subset = [
                item
                for item in targets
                if item.parent_release_id == parent.release_id and item.object_role == role
            ]
            if subset:
                statistics["by_parent_and_role"][f"{parent.release_id}|{role}"] = _target_statistics(subset)

    end_ids = tuple(tokenizer.encode(ASSISTANT_END_TEXT, add_special_tokens=False))
    selection_counts = Counter((item.parent_release_id, item.object_role) for item in targets)
    body: dict[str, Any] = {
        "schema_version": MANIFEST_SCHEMA_VERSION,
        "config_sha256": config.config_sha256,
        "implementation": {
            "qwen_mathia_v2_general_core_sha256": sha256_file(Path(__file__)),
            "mathia_interchange_sha256": sha256_file(Path(interchange.__file__)),
        },
        "exit_decision": config.value["exit_decision"],
        "model": dict(config.model),
        "tokenizer": {
            "tokenizer_id": config.model["tokenizer_id"],
            "tokenizer_revision": config.model["tokenizer_revision"],
            "tokenizer_class": type(tokenizer).__name__,
            "chat_template_sha256": sha256_text(str(tokenizer.chat_template)),
            "eos_token_id": tokenizer.eos_token_id,
            "pad_token_id": tokenizer.pad_token_id,
            "assistant_end_token_id": tokenizer.convert_tokens_to_ids("<|im_end|>"),
            "assistant_end_sequence_ids": list(end_ids),
        },
        "parent_bindings": [
            {
                "release_id": binding["release_id"],
                "freeze_id": binding["freeze_id"],
                "review_content_freeze_id": binding.get("review_content_freeze_id"),
                "verified_files": dict(binding["frozen_files"]),
            }
            for binding in config.corpus["parents"]
        ],
        "dedupe_report_id": dedupe["dedupe_report_id"],
        "selection_audit": {
            "input_candidates": dedupe["input_candidate_count"],
            "selected_optimizer_targets": len(targets),
            "selected_counts_by_parent_and_role": {
                f"{parent}|{role}": count
                for (parent, role), count in sorted(selection_counts.items())
            },
            "selected_counts_by_source_id": dict(sorted(counts_by_source.items())),
            "dedupe_dropped": len(dedupe["dropped"]),
            "source_objects_selected_as_standalone_targets": 0,
            "rejected_quarantined_or_evaluation_only_selected": 0,
            "riemann_release_or_origin_objects_selected": 0,
            "selected_are_all_accepted_and_eligible": True,
        },
        "serialization": dict(config.value["serialization"]),
        "ordering": {
            **config.value["ordering"],
            "selection_object_ids": [item.object_id for item in targets],
            "selection_order_sha256": sha256_text("\n".join(item.object_id for item in targets) + "\n"),
        },
        "sequence_bound": {
            "true_maximum_sequence_tokens": true_maximum,
            "configured_maximum_sequence_tokens": maximum,
            "clean_sequence_multiple": multiple,
            "smallest_clean_bound": smallest_bound,
            "truncated_examples": 0,
        },
        "token_statistics": statistics,
        "one_unique_corpus_pass": {
            "examples": len(targets),
            "prompt_tokens": sum(item.prompt_tokens for item in targets),
            "assistant_content_tokens": sum(item.assistant_content_tokens for item in targets),
            "assistant_end_tokens": sum(item.assistant_end_tokens for item in targets),
            "supervised_tokens": sum(item.supervised_tokens for item in targets),
            "all_tokens": sum(item.total_tokens for item in targets),
        },
        "exposure_plan": _exposure_plan(config, targets),
        "examples": rows,
    }
    body["g_v2_freeze_id"] = "g_v2_" + sha256_text(canonical_json(body))
    return body, dedupe, targets


@dataclass(frozen=True)
class LoraTargetMatch:
    path: str
    suffix: str
    family: str
    module_class: str
    input_features: int
    output_features: int
    lora_parameter_count: int


def inspect_lora_targets(model: Any, rank: int, target_regex: str) -> tuple[LoraTargetMatch, ...]:
    pattern = re.compile(target_regex)
    matches: list[LoraTargetMatch] = []
    lookalikes: list[str] = []
    for path, module in model.named_modules():
        suffix = path.rsplit(".", 1)[-1]
        if suffix not in LORA_TARGET_SUFFIXES:
            continue
        if not pattern.fullmatch(path):
            lookalikes.append(path)
            continue
        input_features = getattr(module, "in_features", None)
        output_features = getattr(module, "out_features", None)
        if not isinstance(input_features, int) or not isinstance(output_features, int):
            raise TypeError(f"LoRA target is not a linear projection: {path}")
        if ".self_attn." in path:
            family = "full_attention"
        elif ".linear_attn." in path:
            family = "gated_deltanet"
        elif ".mlp." in path:
            family = "mlp"
        else:
            raise ValueError(f"unknown LoRA target family: {path}")
        matches.append(
            LoraTargetMatch(
                path=path,
                suffix=suffix,
                family=family,
                module_class=type(module).__name__,
                input_features=input_features,
                output_features=output_features,
                lora_parameter_count=rank * (input_features + output_features),
            )
        )
    if lookalikes:
        raise RuntimeError("target-like modules exist outside the text-only regex: " + ", ".join(lookalikes[:5]))
    counts = Counter(item.suffix for item in matches)
    if dict(counts) != EXPECTED_LORA_MODULE_COUNTS:
        raise RuntimeError(f"Qwen3.5 target counts differ: {dict(counts)}")
    if {item.family for item in matches} != {"full_attention", "gated_deltanet", "mlp"}:
        raise RuntimeError("Qwen3.5 target families are incomplete")
    forbidden = ("vision", "visual", "embed", "norm", "lm_head")
    if any(any(token in item.path for token in forbidden) for item in matches):
        raise RuntimeError("forbidden vision/embedding/norm/head module matched")
    return tuple(sorted(matches, key=lambda item: item.path))


def _package_versions(names: Sequence[str]) -> dict[str, str]:
    versions: dict[str, str] = {}
    for name in names:
        versions[name] = importlib.metadata.version(name)
    return versions


def build_architecture_audit(config: DesignConfig, model_source: Path) -> dict[str, Any]:
    source = model_source.resolve()
    observed_files = _verify_files(source, config.model["source_files"])
    try:
        import torch
        from accelerate import init_empty_weights
        from peft import LoraConfig, TaskType, get_peft_model
        from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
    except ImportError as error:
        raise RuntimeError("architecture audit requires the pinned Qwen3.5 design runtime") from error

    loaded = AutoConfig.from_pretrained(str(source), local_files_only=True, trust_remote_code=False)
    tokenizer = AutoTokenizer.from_pretrained(str(source), local_files_only=True, trust_remote_code=False)
    if type(loaded).__name__ != "Qwen3_5Config" or type(loaded.text_config).__name__ != "Qwen3_5TextConfig":
        raise RuntimeError("pinned source did not load the Qwen3.5 multimodal/text configs")
    if sha256_text(str(tokenizer.chat_template)) != config.model["chat_template_sha256"]:
        raise RuntimeError("pinned tokenizer chat template hash differs")
    with init_empty_weights():
        model = AutoModelForCausalLM.from_config(loaded.text_config, trust_remote_code=False)
        if type(model).__name__ != config.model["architecture_class"]:
            raise RuntimeError("text-only Qwen3.5 causal LM class differs")
        if any("vision" in path or "visual" in path for path, _ in model.named_modules()):
            raise RuntimeError("text-only causal LM unexpectedly contains vision modules")
        base_parameter_count = sum(parameter.numel() for parameter in model.parameters())
        matches = inspect_lora_targets(model, int(config.lora["r"]), str(config.lora["target_regex"]))
        lora_config = LoraConfig(
            task_type=TaskType.CAUSAL_LM,
            r=int(config.lora["r"]),
            lora_alpha=int(config.lora["lora_alpha"]),
            lora_dropout=float(config.lora["lora_dropout"]),
            bias=str(config.lora["bias"]),
            target_modules=str(config.lora["target_regex"]),
            modules_to_save=None,
            revision=BASE_REVISION,
        )
        peft_model = get_peft_model(model, lora_config)
        trainable = [
            (name, parameter.numel())
            for name, parameter in peft_model.named_parameters()
            if parameter.requires_grad
        ]
        total_parameter_count = sum(parameter.numel() for parameter in peft_model.parameters())

    analytic_trainable = sum(item.lora_parameter_count for item in matches)
    observed_trainable = sum(count for _name, count in trainable)
    invalid_trainables = [
        name for name, _count in trainable if ".lora_A." not in name and ".lora_B." not in name
    ]
    if observed_trainable != analytic_trainable or invalid_trainables:
        raise RuntimeError("PEFT trainable parameter ownership differs from analytic LoRA target audit")
    quantization = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_use_double_quant=True,
        bnb_4bit_compute_dtype=torch.bfloat16,
    )
    suffix_shapes: dict[str, set[tuple[int, int]]] = defaultdict(set)
    for item in matches:
        suffix_shapes[item.suffix].add((item.input_features, item.output_features))
    body: dict[str, Any] = {
        "schema_version": ARCHITECTURE_SCHEMA_VERSION,
        "config_sha256": config.config_sha256,
        "implementation_core_sha256": sha256_file(Path(__file__)),
        "status": "passed_cpu_design_audit",
        "model": {
            "model_id": BASE_MODEL_ID,
            "model_revision": BASE_REVISION,
            "tokenizer_id": BASE_MODEL_ID,
            "tokenizer_revision": BASE_REVISION,
            "upstream_architecture_class": loaded.architectures[0],
            "text_architecture_class": type(peft_model.base_model.model).__name__,
            "text_config_class": type(loaded.text_config).__name__,
            "text_model_type": loaded.text_config.model_type,
            "text_only_training_path": True,
            "upstream_has_vision_config": hasattr(loaded, "vision_config"),
            "vision_modules_present_in_training_model": 0,
            "base_parameter_count": base_parameter_count,
            "peft_wrapped_total_parameter_count": total_parameter_count,
        },
        "tokenizer": {
            "class": type(tokenizer).__name__,
            "eos_token_id": tokenizer.eos_token_id,
            "pad_token_id": tokenizer.pad_token_id,
            "assistant_end_token_id": tokenizer.convert_tokens_to_ids("<|im_end|>"),
            "chat_template_sha256": sha256_text(str(tokenizer.chat_template)),
        },
        "source_files": observed_files,
        "upstream_evidence": dict(config.model["upstream_evidence"]),
        "lora": {
            "target_regex": config.lora["target_regex"],
            "target_suffixes": list(LORA_TARGET_SUFFIXES),
            "matched_module_count": len(matches),
            "module_counts_by_suffix": dict(sorted(Counter(item.suffix for item in matches).items())),
            "module_counts_by_family": dict(sorted(Counter(item.family for item in matches).items())),
            "projection_shapes_by_suffix": {
                suffix: [list(shape) for shape in sorted(shapes)]
                for suffix, shapes in sorted(suffix_shapes.items())
            },
            "matched_modules": [asdict(item) for item in matches],
            "adapter_trainable_parameter_count": observed_trainable,
            "adapter_parameter_tensor_count": len(trainable),
            "vision_modules_matched": 0,
            "embedding_modules_matched": 0,
            "normalization_modules_matched": 0,
            "lm_head_modules_matched": 0,
        },
        "compatibility": {
            "python": platform.python_version(),
            "packages": _package_versions(
                (
                    "torch",
                    "transformers",
                    "peft",
                    "bitsandbytes",
                    "accelerate",
                    "huggingface-hub",
                    "tokenizers",
                )
            ),
            "auto_config_loaded": True,
            "text_only_meta_model_instantiated": True,
            "peft_adapter_attached": True,
            "only_lora_parameters_trainable": True,
            "bitsandbytes_nf4_config_constructed": bool(quantization.load_in_4bit),
            "gpu_forward_backward_or_memory_claimed": False,
        },
    }
    body["architecture_audit_id"] = "qwen35_4b_architecture_" + sha256_text(canonical_json(body))
    return body


def load_pinned_tokenizer(config: DesignConfig, model_source: Path) -> Any:
    try:
        from transformers import AutoTokenizer
    except ImportError as error:
        raise RuntimeError("token audit requires the pinned Transformers runtime") from error
    source = model_source.resolve()
    _verify_files(source, config.model["source_files"])
    tokenizer = AutoTokenizer.from_pretrained(str(source), local_files_only=True, trust_remote_code=False)
    if tokenizer.eos_token_id is None or tokenizer.pad_token_id is None:
        raise RuntimeError("pinned tokenizer must define EOS and pad tokens")
    if sha256_text(str(tokenizer.chat_template)) != config.model["chat_template_sha256"]:
        raise RuntimeError("pinned tokenizer chat template hash differs")
    return tokenizer


def verify_committed_materialization(
    config: DesignConfig,
    tokenizer: Tokenizer,
    supplement_artifact_root: Path,
    manifest_path: Path,
    dedupe_path: Path,
) -> tuple[dict[str, Any], dict[str, Any]]:
    manifest, dedupe, _targets = build_materialization(config, tokenizer, supplement_artifact_root)
    if canonical_json(manifest) != canonical_json(_read_json(manifest_path)):
        raise ValueError("G-v2 manifest does not reproduce from frozen inputs")
    if canonical_json(dedupe) != canonical_json(_read_json(dedupe_path)):
        raise ValueError("G-v2 dedupe report does not reproduce from frozen inputs")
    return manifest, dedupe
