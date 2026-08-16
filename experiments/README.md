# Experiments

There is currently **no active Mathia experiment implementation in this directory**.

The previous `pre_rl_signal/gold_set_v0` experiment was retired before target-model inference during the semantic-intuition reset. Its full code, fixtures, audits, runner, and tests remain recoverable from Git history and the closed issues/PRs that produced them.

Do not restore or copy that implementation as the default starting point for the new experiment.

Active sequence:

- `#30` designs and audits the new computation-free semantic-intuition benchmark first;
- `#31` may add minimal benchmark-specific code only after that semantic contract is accepted;
- `#32` later freezes and runs the first local base-model diagnostic.

The directory is intentionally quiet until the mathematics justifies new code.
