# Implementation constraints

The first implementation exists to test the research signal, not to establish permanent infrastructure.

Prefer simple standard-library or lightweight Python code and transparent finite enumeration.

Preserve these boundaries:

- visible situation generation must be separable from hidden intervention generation;
- objective ground truth must be deterministic and inspectable;
- context candidates must be supplied independently of the exact hidden instances used for scoring;
- scoring must not require an AI judge for the mechanically verifiable task families;
- fixtures should be small enough for human inspection;
- do not introduce a durable dataset schema until examples force one;
- do not add RL, Lean, distributed serving, or large-data infrastructure yet.
