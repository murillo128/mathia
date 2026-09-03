# MI-001 — Collision-safe coordinates separate a branch singularity from the first source-dependent interaction

**Evidence level:** exact for simple double collisions under the backward heat equation, supported by XF-001--XF-003

## Core intuition

The divergent velocity of an individual zero at a simple collision is a coordinate singularity, not evidence of singular dynamics of the entire zero set. Passing from labeled roots to the local quadratic discriminant or squared gap removes the square-root branch and gives an analytic collision coordinate.

But the first derivative of that coordinate is universal. Arithmetic information can enter only in later interaction terms involving the exterior zeros.

## Strongest justified principle

XF-001 shows the generic local normal form: two roots split as `+-sqrt(2 tau)`, so root speed diverges like `tau^{-1/2}`. Any argument assuming analytic labeled roots or uniformly bounded root velocity through collision is structurally invalid.

XF-002 replaces the bad coordinate by the local discriminant `D`; at a simple double collision it is analytic with the universal slope `D'(t*)=8`. XF-003 gives the adjacent real-pair equation `q'=8-4qS`, where `S` is the exterior inverse-square field. The universal `8` is the collision normal form, while `S` is the first place the surrounding zero configuration affects gap evolution.

## Evidence synthesis and boundaries

The result is local and does not control multiple collisions, complex departures, or a whole high-zero window. The exterior field is also not automatically Xi-specific; matched real-zero heat flows can reproduce the same formula.

Thus “regularize the collision” is a coordinate repair, not an RH mechanism. The next theorem must control the exterior term from independently known Xi structure.

## Status / novelty

Weierstrass preparation and square-root collision normal forms are classical. The synthesis is the source-information boundary inside the exact heat-flow gap equation.

## Falsification criterion

Find an Xi-specific invariant already present in the universal first collision slope, or show that the proposed symmetric coordinate still develops a branch singularity at a generic simple double collision.

## Lean-formalizable core

- Square-root root splitting.
- Analytic quadratic discriminant.
- Universal slope `8`.
- Exact exterior-field correction to squared-gap dynamics.
