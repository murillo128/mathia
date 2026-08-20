# Qwen-Mathia v1 (`#47`)

This package executes the one bounded QLoRA run authorized by issue `#47`.
It selects only accepted, training-eligible `interpretation` and `synthesis`
objects from the frozen `agnostic-mathia-full-v1` release, preserves the
canonical `mathia-interchange-v1` visible rendering, and masks prompt tokens
from causal-LM loss.

Normal repository tests and the `audit` command are CPU-only apart from loading
the pinned tokenizer. GPU work is explicit:

```bash
python -m experiments.qwen_mathia_v1 audit \
  --output experiments/qwen_mathia_v1/training_manifest.json

python -m experiments.qwen_mathia_v1 preflight \
  --manifest experiments/qwen_mathia_v1/training_manifest.json \
  --artifact-dir /workspace/mathia-artifacts/qwen-mathia-v1/preflight \
  --output experiments/qwen_mathia_v1/evidence/preflight.json

python -m experiments.qwen_mathia_v1 train \
  --manifest experiments/qwen_mathia_v1/training_manifest.json \
  --output-dir /workspace/mathia-artifacts/qwen-mathia-v1/full-run
```

The external artifact directory retains adapter weights and resumable trainer
state. Git retains only deterministic configuration/manifests, compact evidence,
and the immutable Hugging Face revision. The root publication artifact is the
epoch-4 PEFT adapter; epoch-1 and epoch-2 adapters remain separate. No merged
base-model weights are produced.

The technical sanity and publication checks do not assess mathematical quality.
In particular, this issue does not run qwen-lean fertility validation and does
not support a claim of improved theorem proving, conceptual transfer, or
mathematical reasoning.
