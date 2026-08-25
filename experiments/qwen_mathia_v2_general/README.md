# Qwen-Mathia v2 general CPU materialization

This package implements the design-only boundary of issue #55. It verifies the
two frozen general parents, preserves external supplement content outside Git,
applies the exact Qwen3.5-4B official template, produces the G-v2 optimizer
manifest and dedupe report, and audits the text-only LoRA architecture on CPU.
It does not load model weights or run SFT.

The materializer needs:

- the exact-revision small Qwen files listed in `config.json`, downloaded to an
  external directory without model safetensors;
- the preserved `agnostic-mathia-openalex-supplement-v1` external artifact root;
- the audited runtime versions recorded in `evidence/architecture_audit.json`.

Run from the repository root with an interpreter containing the pinned runtime:

```bash
python -m experiments.qwen_mathia_v2_general \
  --model-source /external/qwen3.5-4b-base-source \
  --supplement-artifact-root /external/agnostic-mathia-openalex-supplement-v1 \
  materialize

python -m experiments.qwen_mathia_v2_general \
  --model-source /external/qwen3.5-4b-base-source \
  --supplement-artifact-root /external/agnostic-mathia-openalex-supplement-v1 \
  verify
```

Missing external source units are a hard failure. The committed manifest does
not make unavailable or restricted source bytes redistributable.

Repository tests validate the committed hashes, selection, loss ranges, token
audit, exposure, architecture boundary, and scope without requiring those
external source bytes.
