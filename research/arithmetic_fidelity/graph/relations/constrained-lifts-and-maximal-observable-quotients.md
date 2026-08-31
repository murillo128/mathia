---
id: RGR-AF-LIFTS-001
type: research-graph-relation
scope: arithmetic_fidelity
relation: constrained-lifts-and-maximal-observable-quotients
derived: true
---

# Constrained lifts and maximal observable quotients

[[research/arithmetic_fidelity/findings/AF-001-fiberwise-recoverability-and-unconstrained-lifts|AF-001]] shows that unconstrained minimal lifts are structurally trivial: an arbitrary mark can simply encode the lost discriminator. The subsequent findings make the lift problem meaningful only after the admissible observable class is fixed.

- [[research/arithmetic_fidelity/findings/AF-002-fixed-observable-lifts-are-discernibility-reducts|AF-002]] reduces finite fixed-library recovery to hitting every unresolved conflict pair; minimal lifts are minimal transversals of the discernibility hypergraph.
- [[research/arithmetic_fidelity/findings/AF-003-invariant-observable-quotients-impose-orbit-closure-fidelity-barrier|AF-003]] identifies the maximal quotient carried by an entire admissible invariant-observable algebra; conflicts surviving that quotient cannot be repaired by any subfamily or downstream recombination.
- [[research/arithmetic_fidelity/findings/AF-005-monomial-phase-lifts-annihilator-lattice|AF-005]] gives an exact harmonic instance: monomial phase lifts are complete modulo an allowed subgroup exactly when their exponent lattice equals its annihilator lattice.
- [[research/arithmetic_fidelity/findings/AF-011-zero-error-stochastic-fidelity-is-support-confusability|AF-011]] recovers the same hitting-set structure for fixed observable libraries when deterministic fibers are replaced by stochastic support-overlap conflicts.

The graph consequence is a precise design gate: lift size is meaningful only relative to a mathematically constrained observable class, and the full class should be audited for separability before optimizing a subfamily.