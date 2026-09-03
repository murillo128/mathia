# Xi Flow

## Scope

`xi_flow` studies the Riemann hypothesis through the de Bruijn–Newman heat-flow deformation of the completed zeta function. Its core viewpoint is dynamical: instead of treating zero location as a static condition, study how the zero configuration evolves under the heat parameter and whether `t = 0` can be characterized as the exact transition boundary for real-rootedness.

The line should use the de Bruijn–Newman constant, zero dynamics, collision/repulsion structure, Lehmer-pair phenomena, monotone or nearly monotone energies, barrier arguments, local-versus-global gap statistics, and faithful finite-dimensional models when they illuminate the infinite system.

## Research objective

Seek a source-faithful mechanism that would force or constrain

`Lambda = 0`,

or, more realistically, produce a new unconditional upper bound or structural obstruction on positive-time first collision.

Prefer concrete intermediate statements such as:

- a monotone quantity along the zero flow that has the correct sign at `t = 0`;
- a collision barrier derived from global zero statistics or arithmetic input;
- a rigidity theorem showing that a positive `Lambda` would force an impossible local/global gap configuration;
- a finite-dimensional or truncated model whose invariant survives a controlled limit to the actual xi flow;
- a quantitative relation between Lehmer-type near-collisions and global density/correlation information that improves known bounds on `Lambda`.

## Boundaries

Do not count the equivalence `RH <=> Lambda <= 0` or the known lower bound `Lambda >= 0` as new progress. Do not infer infinite-system behavior from a visually compelling finite simulation without a topology-matched stability argument.

Avoid silently assuming RH in zero-labeling, pair-correlation, or real-root dynamics. When a formula for moving zeros is valid only inside a real-rooted regime, state that domain explicitly and do not extrapolate it through a collision.

Do not duplicate `weil_inertia` merely because both lines use zero statistics. `xi_flow` owns the heat deformation, zero motion, collision geometry, and `Lambda`; if the central object becomes the compressed Weil form or a rank/inertia certificate, hand the question to `weil_inertia` as a clue.

## Starting directions

1. Reconstruct the exact zero-motion equations in the real-rooted regime and identify quantities with monotonicity, convexity, or conservation properties that could survive toward `t = 0`.
2. Study whether known pair-correlation or higher-correlation information imposes a quantitative obstruction to a positive-time first collision.
3. Audit Lehmer-pair mechanisms as possible local witnesses of near-criticality while separating numerical evidence from a global theorem.
4. Search for energy/entropy/Lyapunov formulations whose sign or growth changes at the de Bruijn–Newman transition and test them against matched synthetic zero configurations.
5. Use visualization as clue-generation only when it leads to an explicit invariant, inequality, counterexample, or falsifiable dynamical hypothesis.

## Persistence

Use the standard Mathia Research Watch workflow and repository conventions. Durable results belong under `findings/`; speculative but falsifiable handoffs belong under `clues/`; granular research attempts belong wherever the Research Watch skill currently requires. Do not create artifacts merely to record activity.
