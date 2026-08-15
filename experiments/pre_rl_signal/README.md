# Pre-RL conceptual signal experiment

Implement the smallest executable version of `docs/PRE_RL_SIGNAL_STUDY.md` here.

Initial implementation should focus on deterministic finite-arithmetic generation and verification for a small subset of the seed situations in `docs/FIRST_MATHEMATICAL_WORLD.md`.

The first code should make it possible to:

1. generate visible mathematical situations and hidden interventions separately;
2. deterministically compute hidden ground truth;
3. serialize small fixtures for inspection;
4. evaluate externally supplied solver answers without an AI judge;
5. keep conceptual context generation separate from task generation/evaluation.

Do not add RL training or model-specific serving infrastructure in this first implementation.
