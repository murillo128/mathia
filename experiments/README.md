# Experiments

There is currently **no active Mathia experiment implementation in this directory**.

The previous `pre_rl_signal/gold_set_v0` experiment was retired before target-model inference during the semantic-intuition reset. Its full code, fixtures, audits, runner, and tests remain recoverable from Git history and the closed issues/PRs that produced them.

Do not restore or copy that implementation as the default starting point for the new experiment.

The active research hypothesis is documented in `docs/CONCEPTS_DIMENSIONS_INTUITION.md`.

Current sequence:

- `#30` scopes and adversarially audits the provisional concepts, conceptual dimensions, documented-theorem intuition task, and `intuition -> qwen-lean proof-search fertility` measurement contract;
- `#31` may add only the minimal deterministic pre-test/fertility plumbing after that contract is accepted;
- `#32` later freezes and runs the exact Qwen-base + Codex-reference intuition pre-test against matched qwen-lean proof search.

No concept training, dimension training, intuition distillation, or fertility optimization should be implemented here until #32 validates that the proposed downstream measurement channel is informative.

The directory is intentionally quiet until the scientific contract justifies new code.
