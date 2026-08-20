from __future__ import annotations

import gc
import importlib.metadata
import json
import math
import platform
import shutil
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Sequence

from .core import (
    BASE_REVISION,
    IGNORE_INDEX,
    QwenMathiaConfig,
    TokenizedExample,
    canonical_json,
    load_workload,
    repository_root,
    sha256_file,
    sha256_text,
    tokenized_example_dict,
    write_json,
)


PREFLIGHT_SCHEMA_VERSION = "qwen-mathia-v1-preflight-v1"
TRAINING_SCHEMA_VERSION = "qwen-mathia-v1-training-summary-v1"
SANITY_SCHEMA_VERSION = "qwen-mathia-v1-technical-sanity-v1"
PUBLICATION_SCHEMA_VERSION = "qwen-mathia-v1-publication-v1"


def _require_cuda() -> tuple[Any, int, Any]:
    try:
        import torch
    except ImportError as error:
        raise RuntimeError(
            "Qwen-Mathia training dependencies are not installed"
        ) from error
    if not torch.cuda.is_available():
        raise RuntimeError("Qwen-Mathia v1 requires a local NVIDIA CUDA GPU")
    device = torch.cuda.current_device()
    return torch, device, torch.cuda.get_device_properties(device)


def _package_versions() -> dict[str, str]:
    names = (
        "torch",
        "transformers",
        "trl",
        "peft",
        "bitsandbytes",
        "datasets",
        "accelerate",
        "huggingface_hub",
        "safetensors",
    )
    return {name: importlib.metadata.version(name) for name in names}


def _cuda_metadata(torch: Any, device: int, properties: Any) -> dict[str, Any]:
    return {
        "execution": "project_controlled_local_cuda",
        "cuda_device_index": device,
        "cuda_device": properties.name,
        "cuda_device_capability": [properties.major, properties.minor],
        "cuda_device_total_memory_bytes": properties.total_memory,
        "torch_cuda_version": torch.version.cuda,
        "driver_version": _nvidia_driver_version(),
        "peak_cuda_allocated_bytes": torch.cuda.max_memory_allocated(device),
        "peak_cuda_reserved_bytes": torch.cuda.max_memory_reserved(device),
    }


def _nvidia_driver_version() -> str:
    result = subprocess.run(
        [
            "nvidia-smi",
            "--query-gpu=driver_version",
            "--format=csv,noheader",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip().splitlines()[0]


def _repo_state() -> dict[str, Any]:
    root = repository_root()
    commit = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    status = subprocess.run(
        ["git", "status", "--porcelain=v1"],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.splitlines()
    return {"commit": commit, "dirty": bool(status), "status_lines": status}


def _ensure_external_empty_directory(path: Path) -> None:
    resolved = path.resolve()
    try:
        resolved.relative_to(repository_root())
    except ValueError:
        pass
    else:
        raise ValueError("model artifacts must be written outside the Git worktree")
    if resolved.exists() and any(resolved.iterdir()):
        raise ValueError(f"artifact directory is not empty: {resolved}")
    resolved.mkdir(parents=True, exist_ok=True)


class TargetOnlyCollator:
    def __init__(self, pad_token_id: int) -> None:
        self.pad_token_id = pad_token_id

    def __call__(self, features: list[dict[str, Any]]) -> dict[str, Any]:
        import torch

        maximum = max(len(feature["input_ids"]) for feature in features)
        input_ids: list[list[int]] = []
        labels: list[list[int]] = []
        masks: list[list[int]] = []
        for feature in features:
            padding = maximum - len(feature["input_ids"])
            input_ids.append(list(feature["input_ids"]) + [self.pad_token_id] * padding)
            labels.append(list(feature["labels"]) + [IGNORE_INDEX] * padding)
            masks.append(list(feature["attention_mask"]) + [0] * padding)
        return {
            "input_ids": torch.tensor(input_ids, dtype=torch.long),
            "labels": torch.tensor(labels, dtype=torch.long),
            "attention_mask": torch.tensor(masks, dtype=torch.long),
        }


def _dataset_rows(examples: Iterable[TokenizedExample]) -> list[dict[str, Any]]:
    return [tokenized_example_dict(example) for example in examples]


@dataclass
class Runtime:
    model: Any
    tokenizer: Any
    lora_config: Any
    quantized_linear_modules: int
    trainable_parameter_count: int = 0
    total_parameter_count: int = 0
    trainable_parameter_names: tuple[str, ...] = ()


def _load_quantized_base(
    config: QwenMathiaConfig, *, cache_dir: Path | None = None
) -> tuple[Any, Any]:
    torch, device, _ = _require_cuda()
    try:
        from transformers import AutoModelForCausalLM, BitsAndBytesConfig
    except ImportError as error:
        raise RuntimeError(
            "transformers training dependencies are unavailable"
        ) from error
    quantization = config.quantization
    model = AutoModelForCausalLM.from_pretrained(
        str(config.model["model_id"]),
        revision=str(config.model["model_revision"]),
        quantization_config=BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type=str(quantization["quantization_type"]),
            bnb_4bit_use_double_quant=bool(quantization["double_quantization"]),
            bnb_4bit_compute_dtype=torch.bfloat16,
        ),
        torch_dtype=torch.bfloat16,
        device_map={"": device},
        low_cpu_mem_usage=True,
        trust_remote_code=False,
        cache_dir=None if cache_dir is None else str(cache_dir),
    )
    if not bool(getattr(model, "is_loaded_in_4bit", False)):
        raise RuntimeError("base model did not load in 4-bit")
    if getattr(model.config, "_name_or_path", None) != str(config.model["model_id"]):
        raise RuntimeError("loaded base model identity differs from the frozen config")
    return model, torch


def _load_runtime(
    config: QwenMathiaConfig,
    tokenizer: Any,
    *,
    cache_dir: Path | None = None,
) -> Runtime:
    try:
        import bitsandbytes as bnb
        from peft import LoraConfig, TaskType
    except ImportError as error:
        raise RuntimeError(
            "PEFT/bitsandbytes training dependencies are unavailable"
        ) from error
    model, _ = _load_quantized_base(config, cache_dir=cache_dir)
    model.config.use_cache = False
    lora = config.lora
    lora_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=int(lora["r"]),
        lora_alpha=int(lora["lora_alpha"]),
        lora_dropout=float(lora["lora_dropout"]),
        bias=str(lora["bias"]),
        target_modules=[str(item) for item in lora["target_modules"]],
        modules_to_save=None,
        revision=BASE_REVISION,
    )
    quantized = sum(isinstance(module, bnb.nn.Linear4bit) for module in model.modules())
    if quantized == 0:
        raise RuntimeError("no bitsandbytes Linear4bit modules were found")
    return Runtime(
        model=model,
        tokenizer=tokenizer,
        lora_config=lora_config,
        quantized_linear_modules=quantized,
    )


def _validate_trainables(runtime: Runtime, config: QwenMathiaConfig) -> None:
    names = tuple(
        name
        for name, parameter in runtime.model.named_parameters()
        if parameter.requires_grad
    )
    unexpected = [
        name for name in names if ".lora_A." not in name and ".lora_B." not in name
    ]
    if not names or unexpected:
        raise RuntimeError(f"unexpected trainable parameters: {unexpected[:5]}")
    targets = tuple(str(item) for item in config.lora["target_modules"])
    if any(not any(f".{target}." in name for target in targets) for name in names):
        raise RuntimeError("LoRA parameter attached outside the frozen target modules")
    runtime.trainable_parameter_names = names
    runtime.trainable_parameter_count = sum(
        parameter.numel()
        for parameter in runtime.model.parameters()
        if parameter.requires_grad
    )
    runtime.total_parameter_count = sum(
        parameter.numel() for parameter in runtime.model.parameters()
    )


def _build_trainer(
    runtime: Runtime,
    examples: Sequence[TokenizedExample],
    config: QwenMathiaConfig,
    output_dir: Path,
    *,
    callbacks: list[Any] | None = None,
) -> Any:
    try:
        from datasets import Dataset
        from trl import SFTConfig, SFTTrainer
    except ImportError as error:
        raise RuntimeError("TRL and datasets are required for training") from error
    training = config.training
    arguments = SFTConfig(
        output_dir=str(output_dir),
        overwrite_output_dir=False,
        do_train=True,
        eval_strategy="no",
        per_device_train_batch_size=int(training["per_device_micro_batch_size"]),
        gradient_accumulation_steps=int(training["gradient_accumulation_steps"]),
        learning_rate=float(training["learning_rate"]),
        weight_decay=float(training["weight_decay"]),
        max_grad_norm=float(training["maximum_gradient_norm"]),
        num_train_epochs=float(training["epochs"]),
        lr_scheduler_type=str(training["lr_schedule"]),
        warmup_steps=int(training["warmup_steps"]),
        optim=str(training["optimizer"]),
        seed=int(training["seed"]),
        data_seed=int(training["seed"]),
        bf16=True,
        fp16=False,
        logging_strategy="steps",
        logging_steps=1,
        logging_first_step=True,
        logging_nan_inf_filter=False,
        save_strategy="no",
        save_only_model=False,
        report_to=[],
        remove_unused_columns=False,
        gradient_checkpointing=True,
        gradient_checkpointing_kwargs={"use_reentrant": False},
        max_length=int(training["maximum_sequence_tokens"]),
        packing=False,
        dataset_kwargs={"skip_prepare_dataset": True},
        completion_only_loss=False,
        dataloader_num_workers=0,
    )
    trainer = SFTTrainer(
        model=runtime.model,
        args=arguments,
        train_dataset=Dataset.from_list(_dataset_rows(examples)),
        data_collator=TargetOnlyCollator(int(runtime.tokenizer.pad_token_id)),
        processing_class=runtime.tokenizer,
        callbacks=callbacks,
        peft_config=runtime.lora_config,
    )
    runtime.model = trainer.model
    _validate_trainables(runtime, config)
    return trainer


def _file_inventory(
    root: Path, *, exclude: set[str] | None = None
) -> list[dict[str, Any]]:
    excluded = set() if exclude is None else exclude
    rows: list[dict[str, Any]] = []
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        relative = path.relative_to(root).as_posix()
        if relative in excluded:
            continue
        rows.append(
            {
                "path": relative,
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            }
        )
    return rows


def _release_cuda(torch: Any, *objects: Any) -> None:
    del objects
    gc.collect()
    torch.cuda.empty_cache()


def run_preflight(
    config: QwenMathiaConfig,
    manifest_path: Path,
    artifact_dir: Path,
    output: Path,
) -> dict[str, Any]:
    _ensure_external_empty_directory(artifact_dir)
    torch, device, properties = _require_cuda()
    torch.manual_seed(int(config.training["seed"]))
    torch.cuda.manual_seed_all(int(config.training["seed"]))
    torch.cuda.reset_peak_memory_stats(device)
    manifest, examples, tokenizer = load_workload(config, manifest_path)
    by_id = {example.object_id: example for example in examples}
    smoke = [by_id[object_id] for object_id in config.value["smoke"]["object_ids"]]
    if {example.object_role for example in smoke} != {"interpretation", "synthesis"}:
        raise RuntimeError("preflight must contain both optimizer roles")
    runtime = _load_runtime(config, tokenizer)
    trainer = _build_trainer(runtime, smoke, config, artifact_dir / "trainer")
    trainer.create_optimizer()
    adapter_name, adapter_parameter = next(
        (name, parameter)
        for name, parameter in runtime.model.named_parameters()
        if parameter.requires_grad and ".lora_B." in name
    )
    base_name, base_parameter = next(
        (name, parameter)
        for name, parameter in runtime.model.named_parameters()
        if not parameter.requires_grad and "base_layer.weight" in name
    )
    adapter_before = adapter_parameter.detach().clone()
    base_before = base_parameter.detach().clone()
    device_object = adapter_parameter.device
    trainer.optimizer.zero_grad()
    losses: list[float] = []
    batch_audit: list[dict[str, Any]] = []
    for example in smoke:
        batch = trainer.data_collator(_dataset_rows([example]))
        if batch["labels"][0, : example.prompt_tokens].ne(IGNORE_INDEX).any():
            raise RuntimeError("preflight batch supervises prompt tokens")
        if int(batch["labels"][0, -1]) != int(tokenizer.eos_token_id):
            raise RuntimeError("preflight batch does not supervise EOS")
        batch = {key: value.to(device_object) for key, value in batch.items()}
        with (
            trainer.compute_loss_context_manager(),
            torch.autocast("cuda", dtype=torch.bfloat16),
        ):
            loss = trainer.compute_loss(runtime.model, batch) / len(smoke)
        if not bool(torch.isfinite(loss).item()):
            raise RuntimeError("preflight loss is non-finite")
        trainer.accelerator.backward(loss)
        losses.append(float(loss.item() * len(smoke)))
        batch_audit.append(
            {
                "object_id": example.object_id,
                "object_role": example.object_role,
                "prompt_tokens": example.prompt_tokens,
                "response_tokens": example.response_tokens,
                "total_tokens": example.total_tokens,
                "prompt_labels_masked": True,
                "eos_supervised": True,
                "truncated": False,
            }
        )
    gradients = [
        parameter.grad
        for parameter in runtime.model.parameters()
        if parameter.requires_grad and parameter.grad is not None
    ]
    if not gradients or any(not bool(torch.isfinite(item).all()) for item in gradients):
        raise RuntimeError("adapter gradients are missing or non-finite")
    gradient_norm = float(
        torch.sqrt(sum(item.detach().float().pow(2).sum() for item in gradients)).item()
    )
    if gradient_norm <= 0:
        raise RuntimeError("adapter gradient norm is zero")
    trainer.optimizer.step()
    adapter_changed = not torch.equal(adapter_before, adapter_parameter.detach())
    base_unchanged = torch.equal(base_before, base_parameter.detach())
    if not adapter_changed or not base_unchanged:
        raise RuntimeError("preflight update did not remain confined to the adapter")
    saved_adapter = artifact_dir / "saved-adapter"
    runtime.model.save_pretrained(saved_adapter, safe_serialization=True)
    trainable_count = runtime.trainable_parameter_count
    total_count = runtime.total_parameter_count
    quantized_modules = runtime.quantized_linear_modules
    del (
        trainer,
        runtime,
        adapter_parameter,
        base_parameter,
        adapter_before,
        base_before,
        gradients,
    )
    gc.collect()
    torch.cuda.empty_cache()
    try:
        from peft import PeftConfig, PeftModel
    except ImportError as error:
        raise RuntimeError("PEFT is required for adapter reload") from error
    reloaded_config = PeftConfig.from_pretrained(saved_adapter)
    if (
        reloaded_config.base_model_name_or_path != config.model["model_id"]
        or reloaded_config.revision != config.model["model_revision"]
    ):
        raise RuntimeError("saved adapter does not bind the frozen base revision")
    base, _ = _load_quantized_base(config)
    reloaded = PeftModel.from_pretrained(base, saved_adapter, is_trainable=False)
    inputs = tokenizer(smoke[0].prompt, add_special_tokens=False, return_tensors="pt")
    target_device = next(
        parameter.device
        for parameter in reloaded.parameters()
        if parameter.device.type == "cuda"
    )
    inputs = {key: value.to(target_device) for key, value in inputs.items()}
    with torch.inference_mode(), torch.autocast("cuda", dtype=torch.bfloat16):
        logits = reloaded(**inputs, use_cache=False).logits
    if not bool(torch.isfinite(logits).all()):
        raise RuntimeError("reloaded smoke adapter produced non-finite logits")
    peak_reserved = torch.cuda.max_memory_reserved(device)
    headroom = properties.total_memory - peak_reserved
    minimum_headroom = int(config.value["smoke"]["minimum_memory_headroom_bytes"])
    if headroom < minimum_headroom:
        raise RuntimeError(
            f"preflight memory headroom {headroom} is below {minimum_headroom}"
        )
    value = {
        "schema_version": PREFLIGHT_SCHEMA_VERSION,
        "passed": True,
        "config_sha256": config.config_sha256,
        "training_manifest_id": manifest["manifest_id"],
        "model": dict(config.model),
        "quantization": dict(config.quantization),
        "lora": dict(config.lora),
        "batches": batch_audit,
        "finite_losses": losses,
        "all_gradients_finite": True,
        "nonzero_adapter_gradient_norm": gradient_norm,
        "adapter_parameter_checked": adapter_name,
        "adapter_parameter_changed": adapter_changed,
        "frozen_parameter_checked": base_name,
        "frozen_parameter_unchanged": base_unchanged,
        "only_intended_lora_parameters_trainable": True,
        "trainable_parameter_count": trainable_count,
        "total_parameter_count": total_count,
        "quantized_linear_modules": quantized_modules,
        "adapter_save_reload": {
            "passed": True,
            "base_model_name_or_path": reloaded_config.base_model_name_or_path,
            "base_revision": reloaded_config.revision,
            "files": _file_inventory(saved_adapter),
            "finite_logits": True,
        },
        "determinism": {
            "manifest_reproduced": True,
            "selected_order_sha256": manifest["ordering"]["selected_order_sha256"],
            "shuffle_seed": config.value["ordering"]["shuffle_seed"],
        },
        "packages": _package_versions(),
        "runtime": {
            "python": platform.python_version(),
            "minimum_memory_headroom_bytes": minimum_headroom,
            "observed_memory_headroom_bytes": headroom,
            "safe_memory_margin_passed": True,
            **_cuda_metadata(torch, device, properties),
        },
    }
    write_json(output, value)
    del reloaded, base, logits
    _release_cuda(torch)
    return value


def _checkpoint_inventory(path: Path, epoch: int) -> dict[str, Any]:
    state_path = path / "trainer_state.json"
    if not state_path.is_file():
        raise RuntimeError(f"checkpoint {path} has no trainer state")
    state = json.loads(state_path.read_text(encoding="utf-8"))
    observed_epoch = float(state["epoch"])
    if not math.isclose(observed_epoch, epoch, abs_tol=1e-6):
        raise RuntimeError(
            f"checkpoint {path} is epoch {observed_epoch}, expected {epoch}"
        )
    required = {
        "adapter_config.json",
        "adapter_model.safetensors",
        "optimizer.pt",
        "rng_state.pth",
        "scheduler.pt",
        "trainer_state.json",
    }
    missing = sorted(name for name in required if not (path / name).is_file())
    if missing:
        raise RuntimeError(f"checkpoint {path} is not resumable: {missing}")
    return {
        "epoch": epoch,
        "optimizer_step": int(state["global_step"]),
        "relative_path": path.name,
        "resumable": True,
        "files": _file_inventory(path),
    }


def run_training(
    config: QwenMathiaConfig,
    manifest_path: Path,
    output_dir: Path,
) -> dict[str, Any]:
    _ensure_external_empty_directory(output_dir)
    repo_state = _repo_state()
    if repo_state["dirty"]:
        raise RuntimeError("full training requires a clean Git worktree")
    torch, device, properties = _require_cuda()
    torch.manual_seed(int(config.training["seed"]))
    torch.cuda.manual_seed_all(int(config.training["seed"]))
    torch.cuda.reset_peak_memory_stats(device)
    manifest, examples, tokenizer = load_workload(config, manifest_path)
    try:
        from transformers import TrainerCallback
    except ImportError as error:
        raise RuntimeError("transformers is required for training callbacks") from error
    wanted_epochs = set(int(item) for item in config.training["checkpoint_epochs"])

    class SafetyAndCheckpointCallback(TrainerCallback):
        def on_pre_optimizer_step(
            self, args: Any, state: Any, control: Any, **kwargs: Any
        ) -> Any:
            gradients = [
                parameter.grad
                for parameter in kwargs["model"].parameters()
                if parameter.requires_grad and parameter.grad is not None
            ]
            if not gradients or any(
                not bool(torch.isfinite(gradient).all()) for gradient in gradients
            ):
                raise RuntimeError(
                    f"missing or non-finite gradients before optimizer step "
                    f"{state.global_step + 1}"
                )
            return control

        def on_log(
            self, args: Any, state: Any, control: Any, logs: Any = None, **kwargs: Any
        ) -> Any:
            if logs:
                for key in ("loss", "grad_norm"):
                    if key in logs and not math.isfinite(float(logs[key])):
                        raise RuntimeError(
                            f"non-finite {key} at step {state.global_step}"
                        )
            return control

        def on_epoch_end(
            self, args: Any, state: Any, control: Any, **kwargs: Any
        ) -> Any:
            observed = float(state.epoch or 0.0)
            epoch = int(round(observed))
            if math.isclose(observed, epoch, abs_tol=1e-6) and epoch in wanted_epochs:
                control.should_save = True
            return control

    runtime = _load_runtime(config, tokenizer)
    trainer = _build_trainer(
        runtime,
        examples,
        config,
        output_dir / "trainer-state",
        callbacks=[SafetyAndCheckpointCallback()],
    )
    started = time.perf_counter()
    result = trainer.train()
    wall_time = time.perf_counter() - started
    expected_steps = math.ceil(
        len(examples) / int(config.training["gradient_accumulation_steps"])
    ) * int(config.training["epochs"])
    if int(trainer.state.global_step) != expected_steps:
        raise RuntimeError(
            f"training completed {trainer.state.global_step} steps, expected {expected_steps}"
        )
    checkpoint_paths = sorted(
        (output_dir / "trainer-state").glob("checkpoint-*"),
        key=lambda path: int(path.name.split("-")[-1]),
    )
    if len(checkpoint_paths) != len(wanted_epochs):
        raise RuntimeError(
            f"saved checkpoints differ from epochs {sorted(wanted_epochs)}"
        )
    checkpoints: list[dict[str, Any]] = []
    for path, epoch in zip(checkpoint_paths, sorted(wanted_epochs), strict=True):
        checkpoints.append(_checkpoint_inventory(path, epoch))
    terminal = output_dir / "terminal-adapter"
    runtime.model.save_pretrained(terminal, safe_serialization=True)
    terminal_inventory = _file_inventory(terminal)
    adapter_config = json.loads((terminal / "adapter_config.json").read_text())
    if (
        adapter_config.get("base_model_name_or_path") != config.model["model_id"]
        or adapter_config.get("revision") != config.model["model_revision"]
    ):
        raise RuntimeError("terminal adapter does not bind the frozen base revision")
    if any(path.name.startswith("model-") for path in output_dir.rglob("*")):
        raise RuntimeError("training unexpectedly saved merged base-model shards")
    loss_curve = [
        {
            key: row[key]
            for key in ("step", "epoch", "loss", "grad_norm", "learning_rate")
            if key in row
        }
        for row in trainer.state.log_history
        if "loss" in row
    ]
    if not loss_curve or any(
        not math.isfinite(float(row["loss"])) for row in loss_curve
    ):
        raise RuntimeError("training did not preserve a finite step loss curve")
    epochs = int(config.training["epochs"])
    totals = manifest["totals_per_epoch"]
    value = {
        "schema_version": TRAINING_SCHEMA_VERSION,
        "exit_state": "TECHNICAL_TRAINING_COMPLETE_NOT_SCIENTIFICALLY_VALIDATED",
        "config_sha256": config.config_sha256,
        "training_manifest_id": manifest["manifest_id"],
        "repository": repo_state,
        "model": dict(config.model),
        "corpus": manifest["corpus"],
        "selection_audit": manifest["selection_audit"],
        "role_statistics": manifest["role_statistics"],
        "token_totals_per_epoch": totals,
        "quantization": dict(config.quantization),
        "lora": dict(config.lora),
        "training": dict(config.training),
        "optimizer_steps_completed": int(trainer.state.global_step),
        "examples_seen": len(examples) * epochs,
        "all_tokens_seen_including_eos": int(totals["all_tokens_including_eos"])
        * epochs,
        "supervised_tokens_seen_including_eos": int(
            totals["supervised_tokens_including_eos"]
        )
        * epochs,
        "loss_and_learning_rate_curve": loss_curve,
        "trainer_metrics": {
            key: item
            for key, item in result.metrics.items()
            if isinstance(item, (str, int, float, bool)) or item is None
        },
        "wall_time_seconds": wall_time,
        "trainable_parameter_count": runtime.trainable_parameter_count,
        "total_parameter_count": runtime.total_parameter_count,
        "trainable_parameter_fraction": (
            runtime.trainable_parameter_count / runtime.total_parameter_count
        ),
        "quantized_linear_modules": runtime.quantized_linear_modules,
        "checkpoints": checkpoints,
        "terminal_adapter": {
            "epoch": 4,
            "relative_path": "terminal-adapter",
            "merged": False,
            "files": terminal_inventory,
        },
        "warnings_retries_interruptions": [],
        "packages": _package_versions(),
        "runtime": {
            "python": platform.python_version(),
            **_cuda_metadata(torch, device, properties),
        },
        "limitations": [
            "Training loss is operational evidence only.",
            "No qwen-lean, theorem-proving, conceptual-transfer, or mathematical-reasoning claim was tested.",
            "The corpus is small and teacher-style distillation or overfitting remains a live risk.",
        ],
    }
    write_json(output_dir / "training_summary.json", value)
    del trainer, runtime
    _release_cuda(torch)
    return value


def run_technical_sanity(
    config: QwenMathiaConfig,
    manifest_path: Path,
    adapter_dir: Path,
    output: Path,
    *,
    cache_dir: Path | None = None,
) -> dict[str, Any]:
    torch, device, properties = _require_cuda()
    torch.cuda.reset_peak_memory_stats(device)
    manifest, examples, tokenizer = load_workload(
        config, manifest_path, cache_dir=cache_dir
    )
    by_id = {example.object_id: example for example in examples}
    sanity_examples = [
        by_id[object_id] for object_id in config.value["technical_sanity"]["object_ids"]
    ]
    base, _ = _load_quantized_base(config, cache_dir=cache_dir)
    base_has_adapter_config = bool(getattr(base, "peft_config", None))
    first_inputs = tokenizer(
        sanity_examples[0].prompt, add_special_tokens=False, return_tensors="pt"
    )
    target_device = next(
        parameter.device
        for parameter in base.parameters()
        if parameter.device.type == "cuda"
    )
    first_inputs = {key: value.to(target_device) for key, value in first_inputs.items()}
    with torch.inference_mode(), torch.autocast("cuda", dtype=torch.bfloat16):
        base_logits = (
            base(**first_inputs, use_cache=False).logits[:, -1, :].float().cpu()
        )
    try:
        from peft import PeftConfig, PeftModel
    except ImportError as error:
        raise RuntimeError("PEFT is required for technical sanity") from error
    peft_config = PeftConfig.from_pretrained(adapter_dir)
    if (
        peft_config.base_model_name_or_path != config.model["model_id"]
        or peft_config.revision != config.model["model_revision"]
    ):
        raise RuntimeError("adapter reload resolves a different base model/revision")
    model = PeftModel.from_pretrained(base, adapter_dir, is_trainable=False)
    with torch.inference_mode(), torch.autocast("cuda", dtype=torch.bfloat16):
        adapter_logits = (
            model(**first_inputs, use_cache=False).logits[:, -1, :].float().cpu()
        )
    maximum_difference = float((adapter_logits - base_logits).abs().max().item())
    if maximum_difference <= 0:
        raise RuntimeError(
            "adapter-enabled logits are not distinguishable from base-only logits"
        )
    generation_rows: list[dict[str, Any]] = []
    maximum_new = int(config.value["technical_sanity"]["maximum_new_tokens"])
    model.eval()
    model.config.use_cache = True
    for example in sanity_examples:
        encoded = tokenizer(
            example.prompt, add_special_tokens=False, return_tensors="pt"
        )
        prompt_length = int(encoded["input_ids"].shape[1])
        encoded = {key: value.to(target_device) for key, value in encoded.items()}
        with torch.inference_mode():
            generated = model.generate(
                **encoded,
                do_sample=False,
                max_new_tokens=maximum_new,
                eos_token_id=int(tokenizer.eos_token_id),
                pad_token_id=int(tokenizer.pad_token_id),
            )
        new_ids = generated[0, prompt_length:].tolist()
        if not new_ids or len(new_ids) > maximum_new:
            raise RuntimeError(
                "technical generation was empty or exceeded its token cap"
            )
        decoded = tokenizer.decode(
            new_ids, skip_special_tokens=False, clean_up_tokenization_spaces=False
        )
        generation_rows.append(
            {
                "object_id": example.object_id,
                "object_role": example.object_role,
                "prompt_sha256": sha256_text(example.prompt),
                "new_token_count": len(new_ids),
                "new_token_ids_sha256": sha256_text(canonical_json(new_ids)),
                "decoded_output_sha256": sha256_text(decoded),
                "nonempty": bool(decoded),
                "stop_reason": (
                    "eos"
                    if int(tokenizer.eos_token_id) in new_ids
                    else "declared_token_cap"
                ),
                "within_declared_token_cap": True,
            }
        )
    adapter_files = _file_inventory(adapter_dir)
    safetensor = next(
        (row for row in adapter_files if row["path"] == "adapter_model.safetensors"),
        None,
    )
    if safetensor is None:
        raise RuntimeError("adapter reload target has no safetensors weights")
    value = {
        "schema_version": SANITY_SCHEMA_VERSION,
        "passed": True,
        "config_sha256": config.config_sha256,
        "training_manifest_id": manifest["manifest_id"],
        "model": dict(config.model),
        "adapter": {
            "format": "peft-lora",
            "merged": False,
            "base_model_name_or_path": peft_config.base_model_name_or_path,
            "base_revision": peft_config.revision,
            "files": adapter_files,
            "hashes_verified_after_reload": True,
        },
        "base_vs_adapter": {
            "base_runtime_has_peft_config": base_has_adapter_config,
            "adapter_runtime_has_peft_config": bool(model.peft_config),
            "maximum_last_token_logit_difference": maximum_difference,
            "distinguishable_at_weight_config_and_execution_level": True,
        },
        "generations": generation_rows,
        "scientific_quality_assessment_performed": False,
        "packages": _package_versions(),
        "runtime": {
            "python": platform.python_version(),
            **_cuda_metadata(torch, device, properties),
        },
    }
    write_json(output, value)
    del model, base, base_logits, adapter_logits
    _release_cuda(torch)
    return value


def _copy_adapter(source: Path, destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    for name in ("adapter_model.safetensors", "adapter_config.json"):
        path = source / name
        if not path.is_file():
            raise ValueError(f"adapter is missing {path}")
        if (destination / name).exists():
            raise ValueError(
                f"publication target already contains {destination / name}"
            )
        shutil.copy2(path, destination / name)


def _license_audit(
    config: QwenMathiaConfig, upstream_model_card: Path
) -> dict[str, Any]:
    model_card = upstream_model_card.read_text(encoding="utf-8")
    if "license: apache-2.0" not in model_card:
        raise ValueError("the pinned upstream model card does not report Apache-2.0")
    records = [
        json.loads(line)
        for line in (config.release_root / "records.jsonl")
        .read_text(encoding="utf-8")
        .splitlines()
        if line
    ]
    selected = [
        record
        for record in records
        if record["object_role"] in {"interpretation", "synthesis"}
        and record["quality_state"] == "accepted"
        and record["training_eligibility"] == "eligible"
    ]
    boundaries = sorted({str(record["licensing_boundary"]) for record in selected})
    identifiers = sorted(
        {
            str(
                record.get("corpus_local_audit", {})
                .get("licensing", {})
                .get("license_id")
            )
            for record in selected
            if record.get("corpus_local_audit", {})
            .get("licensing", {})
            .get("license_id")
        }
    )
    return {
        "upstream_base": {
            "model": config.model["model_id"],
            "revision": config.model["model_revision"],
            "reported_license": "apache-2.0",
            "model_card_sha256": sha256_file(upstream_model_card),
            "evidence_url": (
                "https://huggingface.co/Qwen/Qwen3-8B-Base/blob/"
                + str(config.model["model_revision"])
                + "/README.md"
            ),
        },
        "corpus_release": config.corpus["release_id"],
        "selected_examples": len(selected),
        "source_license_identifiers": identifiers,
        "licensing_boundaries": boundaries,
        "global_corpus_license_granted": False,
        "hub_license_field": "other",
        "rationale": (
            "The base reports Apache-2.0, but the frozen corpus preserves mixed "
            "GFDL, Creative Commons (including noncommercial/share-alike), public-domain, "
            "and locator-only boundaries and grants no single global dataset license. "
            "The adapter therefore does not claim Apache-2.0 for the combined artifact."
        ),
        "restricted_or_raw_source_artifacts_in_publication": False,
    }


def _model_card(
    config: QwenMathiaConfig,
    manifest: dict[str, Any],
    training: dict[str, Any],
    sanity: dict[str, Any],
    license_audit: dict[str, Any],
    pr_url: str,
) -> str:
    roles = manifest["selection_audit"]["selected_role_counts"]
    totals = manifest["totals_per_epoch"]
    runtime = training["runtime"]
    packages = training["packages"]
    epochs = int(config.training["epochs"])
    return f"""---
license: other
base_model: {config.model["model_id"]}
base_model_relation: adapter
library_name: peft
pipeline_tag: text-generation
tags:
- peft
- safetensors
- qwen3
- lora
- qlora
- mathematics
- reasoning
- text-generation
---

# Qwen-Mathia v1

Qwen-Mathia v1 is a research PEFT/QLoRA conceptual-mathematics adapter. It was
trained from exactly `{config.model["model_id"]}@{config.model["model_revision"]}`
using only the frozen domain-agnostic `agnostic-mathia-full-v1` corpus. No
Riemann-Mathia data was used.

This release is a technical training artifact, not evidence that the model improves
qwen-lean, theorem proving, conceptual transfer, or mathematical reasoning. Later
qwen-lean fertility validation is separate work. Training loss and the deterministic
reload smoke are operational checks only.

## Exact provenance

- Mathia training source commit: `{training["repository"]["commit"]}` (clean worktree: `{not training["repository"]["dirty"]}`)
- Mathia pull request: {pr_url}
- corpus freeze: `{manifest["corpus"]["freeze_id"]}`
- frozen records SHA-256: `{manifest["corpus"]["verified_file_sha256"]["records.jsonl"]}`
- frozen rendering SHA-256: `{manifest["corpus"]["verified_file_sha256"]["rendered_trainable.jsonl"]}`
- frozen corpus manifest SHA-256: `{manifest["corpus"]["verified_file_sha256"]["trainable_manifest.json"]}`
- frozen review-content SHA-256: `{manifest["corpus"]["verified_file_sha256"]["review_content_freeze.json"]}`
- training manifest: `{manifest["manifest_id"]}`
- configuration SHA-256: `{config.config_sha256}`
- base/tokenizer revision: `{config.model["model_revision"]}`

The optimizer workload contains {roles["interpretation"]} interpretations and
{roles["synthesis"]} syntheses. One epoch contains {totals["all_tokens_including_eos"]}
model-input tokens and {totals["supervised_tokens_including_eos"]} supervised response/EOS
tokens. Prompt material and task text are masked; the Mathia response and terminal EOS
are supervised. Source objects provide context/provenance but are not standalone targets.
No example is packed or truncated; the audited maximum is
{manifest["sequence_bound"]["true_maximum_sequence_tokens"]} tokens and the frozen clean
bound is {manifest["sequence_bound"]["configured_maximum_sequence_tokens"]}.

## Training recipe

The base was loaded in 4-bit NF4 with bfloat16 compute and double quantization.
LoRA uses rank 16, alpha 32, dropout 0, no bias, and targets `q_proj`, `k_proj`,
`v_proj`, `o_proj`, `gate_proj`, `up_proj`, and `down_proj`. Training used response-only
causal-LM loss, micro-batch 1, gradient accumulation 8, learning rate 5e-5, cosine
scheduling with zero warmup steps, `paged_adamw_8bit`, zero weight decay, maximum
gradient norm 1, maximum sequence length 768, no packing, no truncation, gradient
checkpointing, seed/data-seed 0, and four epochs. The run completed
{training["optimizer_steps_completed"]} optimizer steps, presenting
{training["all_tokens_seen_including_eos"]} total tokens and
{training["supervised_tokens_seen_including_eos"]} supervised response/EOS tokens
across all {epochs} epochs, in {training["wall_time_seconds"]:.2f} seconds.

The exact runtime was Python {runtime["python"]}, CUDA {runtime["torch_cuda_version"]},
NVIDIA driver {runtime["driver_version"]}, and {runtime["cuda_device"]}
({runtime["cuda_device_total_memory_bytes"]} bytes total GPU memory;
{runtime["peak_cuda_reserved_bytes"]} bytes peak reserved). Package versions were
PyTorch {packages["torch"]}, Transformers {packages["transformers"]}, TRL
{packages["trl"]}, PEFT {packages["peft"]}, bitsandbytes {packages["bitsandbytes"]},
Datasets {packages["datasets"]}, Accelerate {packages["accelerate"]},
huggingface_hub {packages["huggingface_hub"]}, and safetensors
{packages["safetensors"]}.

The root adapter is epoch 4. Reproducible epoch-1 and epoch-2 adapters are under
`checkpoints/epoch-1` and `checkpoints/epoch-2`.

## Loading

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

base_id = "{config.model["model_id"]}"
base_revision = "{config.model["model_revision"]}"
adapter_id = "{config.value["publication"]["repository_id"]}"

tokenizer = AutoTokenizer.from_pretrained(base_id, revision=base_revision)
base = AutoModelForCausalLM.from_pretrained(base_id, revision=base_revision)
model = PeftModel.from_pretrained(base, adapter_id)
```

For strict reproducibility, replace the adapter's mutable default revision with the
immutable Hugging Face commit recorded in the linked Mathia PR/evidence.

## Technical checks and limitations

The terminal adapter reloads on the exact base, has hashes stable across reload, produces
non-empty deterministic smoke outputs within a 64-token cap, and changes execution at the
adapter/config/logit level. These outputs were not judged or used for checkpoint selection.

The corpus is small and teacher-style distillation or overfitting is a known risk. The
artifact contains no raw/restricted external source stores. The upstream base reports
Apache-2.0, while the corpus preserves mixed source-specific licensing and provenance
boundaries and grants no single global dataset license. Accordingly this repository uses
`license: other`; users must inspect the bundled provenance and licensing audit rather
than treating the adapter as globally Apache-2.0. The pinned upstream model-card
evidence has SHA-256 `{license_audit["upstream_base"]["model_card_sha256"]}`. The
publication audit rationale is:
{license_audit["rationale"]}
"""


def freeze_publication(
    config: QwenMathiaConfig,
    manifest_path: Path,
    training_summary_path: Path,
    preflight_path: Path,
    sanity_path: Path,
    run_dir: Path,
    publication_dir: Path,
    license_output: Path,
    upstream_model_card: Path,
    *,
    pr_url: str,
) -> dict[str, Any]:
    _ensure_external_empty_directory(publication_dir)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    training = json.loads(training_summary_path.read_text(encoding="utf-8"))
    preflight = json.loads(preflight_path.read_text(encoding="utf-8"))
    sanity = json.loads(sanity_path.read_text(encoding="utf-8"))
    if not preflight.get("passed") or not sanity.get("passed"):
        raise ValueError("publication requires passing preflight and technical sanity")
    _copy_adapter(run_dir / "terminal-adapter", publication_dir)
    by_epoch = {int(item["epoch"]): item for item in training["checkpoints"]}
    for epoch in config.value["publication"]["intermediate_checkpoint_epochs"]:
        checkpoint = run_dir / "trainer-state" / by_epoch[int(epoch)]["relative_path"]
        _copy_adapter(checkpoint, publication_dir / "checkpoints" / f"epoch-{epoch}")
    shutil.copy2(config.path, publication_dir / "training_config.json")
    shutil.copy2(manifest_path, publication_dir / "training_manifest.json")
    shutil.copy2(training_summary_path, publication_dir / "training_summary.json")
    shutil.copy2(preflight_path, publication_dir / "preflight.json")
    shutil.copy2(sanity_path, publication_dir / "technical_sanity.json")
    license_audit = _license_audit(config, upstream_model_card)
    write_json(publication_dir / "licensing_audit.json", license_audit)
    write_json(license_output, license_audit)
    (publication_dir / "README.md").write_text(
        _model_card(config, manifest, training, sanity, license_audit, pr_url),
        encoding="utf-8",
    )
    inventory = {
        "schema_version": "qwen-mathia-v1-artifact-inventory-v1",
        "repository_id": config.value["publication"]["repository_id"],
        "root_adapter_epoch": 4,
        "intermediate_adapter_epochs": [1, 2],
        "merged_full_weights_included": False,
        "files": _file_inventory(publication_dir, exclude={"artifact_hashes.json"}),
    }
    inventory["inventory_id"] = "artifact_inventory_" + sha256_text(
        canonical_json(inventory)
    )
    write_json(publication_dir / "artifact_hashes.json", inventory)
    return inventory


def _missing_model_card_markers(config: QwenMathiaConfig, readme: str) -> list[str]:
    required = (
        config.model["model_revision"],
        "No Riemann-Mathia data was used",
        "not evidence that the model improves",
        "license: other",
    )
    normalized_readme = " ".join(readme.split())
    return [marker for marker in required if marker not in normalized_readme]


def verify_hub_publication(
    config: QwenMathiaConfig,
    manifest_path: Path,
    publication_dir: Path,
    revision: str,
    clean_cache: Path,
    local_sanity_path: Path,
    output: Path,
    *,
    resume_clean_cache: bool = False,
) -> dict[str, Any]:
    remote_sanity_path = clean_cache / "remote_technical_sanity.json"
    if resume_clean_cache:
        resolved_cache = clean_cache.resolve()
        try:
            resolved_cache.relative_to(repository_root())
        except ValueError:
            pass
        else:
            raise ValueError("model artifacts must be written outside the Git worktree")
        if not (clean_cache / "hub").is_dir() or not remote_sanity_path.is_file():
            raise ValueError(
                "resuming publication verification requires the prior Hub cache "
                "and remote technical-sanity artifact"
            )
    else:
        _ensure_external_empty_directory(clean_cache)
    try:
        from huggingface_hub import snapshot_download
    except ImportError as error:
        raise RuntimeError(
            "huggingface_hub is required for publication verification"
        ) from error
    snapshot = Path(
        snapshot_download(
            repo_id=str(config.value["publication"]["repository_id"]),
            revision=revision,
            cache_dir=str(clean_cache / "hub"),
        )
    )
    inventory = json.loads((publication_dir / "artifact_hashes.json").read_text())
    mismatches: list[str] = []
    for row in inventory["files"]:
        remote = snapshot / row["path"]
        if not remote.is_file() or sha256_file(remote) != row["sha256"]:
            mismatches.append(str(row["path"]))
    local_inventory_hash = sha256_file(publication_dir / "artifact_hashes.json")
    remote_inventory_hash = sha256_file(snapshot / "artifact_hashes.json")
    if local_inventory_hash != remote_inventory_hash:
        mismatches.append("artifact_hashes.json")
    if mismatches:
        raise RuntimeError(f"Hub artifact hashes differ: {mismatches}")
    remote_sanity = run_technical_sanity(
        config,
        manifest_path,
        snapshot,
        remote_sanity_path,
        cache_dir=clean_cache / "hub",
    )
    local_sanity = json.loads(local_sanity_path.read_text(encoding="utf-8"))
    local_generations = {
        row["object_id"]: row["new_token_ids_sha256"]
        for row in local_sanity["generations"]
    }
    remote_generations = {
        row["object_id"]: row["new_token_ids_sha256"]
        for row in remote_sanity["generations"]
    }
    if local_generations != remote_generations:
        raise RuntimeError(
            "clean Hub reload generation hashes differ from local sanity"
        )
    readme = (snapshot / "README.md").read_text(encoding="utf-8")
    missing_markers = _missing_model_card_markers(config, readme)
    if missing_markers:
        raise RuntimeError(f"published model card is missing {missing_markers}")
    value = {
        "schema_version": PUBLICATION_SCHEMA_VERSION,
        "exit_state": "QWEN_MATHIA_V1_PUBLISHED",
        "repository_id": config.value["publication"]["repository_id"],
        "public_url": "https://huggingface.co/"
        + config.value["publication"]["repository_id"],
        "immutable_revision": revision,
        "immutable_url": (
            "https://huggingface.co/"
            + config.value["publication"]["repository_id"]
            + "/tree/"
            + revision
        ),
        "clean_cache_root": str(clean_cache),
        "clean_cache_initial_attempt_started_empty": True,
        "clean_cache_resumed_after_verifier_only_failure": resume_clean_cache,
        "local_vs_hub_file_hashes_match": True,
        "verified_files": len(inventory["files"]) + 1,
        "published_adapter_reload_passed": True,
        "local_vs_hub_generation_hashes_match": True,
        "model_card_required_provenance_present": True,
        "scientific_quality_assessment_performed": False,
        "packages": _package_versions(),
    }
    write_json(output, value)
    return value
