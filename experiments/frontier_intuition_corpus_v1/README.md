# Frontier intuition corpus v1

This directory is the bounded, evaluation-only artifact for
[`murillo128/mathia#57`](https://github.com/murillo128/mathia/issues/57).
It freezes theorem-only GPT-5.6 Sol / xhigh Mathia-style intuitions for the
complete qwen-lean Dataset-v2 validation population: 244 clean miniF2F
validation tasks and 406 fresh synthetic-composition validation tasks.

Every record is `evaluation_only: true`, `training_eligible: false`, and
`artifact_role: frontier_reference`. Nothing here is a Mathia or qwen-lean
training object. The directory is deliberately outside all canonical Mathia
corpus and training-manifest paths.

The source projector reads only pinned qwen-lean Git objects while building
`source_tasks.jsonl`. Generation reads only the projected source, prompt, and
generation-manifest artifacts in this directory; it has no qwen-lean result,
proof, candidate, Lean-error, DeepSeek, or final-test interface. Each attempt
runs in a fresh empty non-repository directory with an ephemeral ignored-config
Codex session. Captures containing a tool or unexpected item are mechanically
classified as `generation_failure`.

The deterministic eligibility gate detects Lean syntax, formal identifiers,
proof-like transmission, and the frozen 96-token Qwen3-8B-Base budget. It does
not judge correctness, usefulness, style, or expected proof success. Attempt 2
exists only when attempt 1 fails that gate; raw outputs are never repaired,
rewritten, or overwritten.

## Reproduction and validation

Run with the local environment that contains the pinned tokenizer:

```text
PYTHONPATH=. /workspace/.venvs/qwen45/bin/python -m experiments.frontier_intuition_corpus_v1 materialize-sources --qwen-repo /workspace/qwen-lean-issue-78
PYTHONPATH=. /workspace/.venvs/qwen45/bin/python -m experiments.frontier_intuition_corpus_v1 validate-sources
PYTHONPATH=. /workspace/.venvs/qwen45/bin/python -m experiments.frontier_intuition_corpus_v1 freeze-contract
PYTHONPATH=. /workspace/.venvs/qwen45/bin/python -m experiments.frontier_intuition_corpus_v1 generate --workers 4
PYTHONPATH=. /workspace/.venvs/qwen45/bin/python -m experiments.frontier_intuition_corpus_v1 finalize
PYTHONPATH=. /workspace/.venvs/qwen45/bin/python -m experiments.frontier_intuition_corpus_v1 validate-finalized
```

`generation_manifest.json` is frozen before the first theorem attempt.
`summary.json`, `integrity_audit.json`, and `freeze.json` contain the final
counts, anti-contamination evidence, artifact hashes, and sole exit decision.
Completing this corpus makes no qwen-lean, Lean-proof, Mathia, or downstream
fertility claim.
