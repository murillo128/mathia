# Experiments

The only active implementation on the `#29` critical path is the deterministic CPU-side
[`intuition_fertility`](intuition_fertility/) harness for issue #31. It
materializes and validates the accepted pre-test mechanics; it does not run a
model experiment.

The [`agnostic_mathia_corpus`](agnostic_mathia_corpus/) work for issue `#44` is
also separate from that critical path. It packages the broad conceptual corpus
under the canonical shared [`mathia_corpus`](mathia_corpus/) interchange owned
with issue `#42`; it does not choose training ratios, train a model, or perform
GPU work.

The exploratory [`riemann_corpus`](riemann_corpus/) work for issue `#42` is
separate from that critical path. It inventories and normalizes an external
source corpus, preserves the pilot calibration evidence, and packages the usable
source corpus into source-linked Riemann–Mathia training objects under a shared
interchange contract with `#44`. It does not train a model, use the GPU, choose a
mixing ratio, or authorize the protected `#32` run.

The [`openalex_discovery`](openalex_discovery/) infrastructure for issue `#46`
streams a declared OpenAlex snapshot into an offline scholarly locator and a
Riemann acquisition handoff on attached storage. OpenAlex metadata remains
discovery evidence rather than trainable mathematical source text; only locally
acquired, hash-bound full text can be handed to `#42` for its separate quality
and Mathia-interpretation gates.

The previous `pre_rl_signal/gold_set_v0` experiment was retired before target-model inference during the semantic-intuition reset. Its full code, fixtures, audits, runner, and tests remain recoverable from Git history and the closed issues/PRs that produced them.

Do not restore or copy that implementation as the default starting point for the new experiment.

The active research hypothesis is documented in `docs/CONCEPTS_DIMENSIONS_INTUITION.md`.

Current sequence:

- `#30` scopes and adversarially audits the provisional concepts, conceptual dimensions, documented-theorem intuition task, and `intuition -> qwen-lean proof-search fertility` measurement contract;
- `#31` may add only the minimal deterministic pre-test/fertility plumbing after that contract is accepted;
- `#32` later freezes and runs the exact Qwen-base + Codex-reference intuition pre-test against matched qwen-lean proof search.

No concept training, dimension training, intuition distillation, or fertility optimization should be implemented here until #32 validates that the proposed downstream measurement channel is informative.

Issue #31 is deliberately limited to transport, leakage screening, frozen
condition construction, prompt parity, result import, and metric mechanics. The
scientific choices and protected model run remain owned by #32.
