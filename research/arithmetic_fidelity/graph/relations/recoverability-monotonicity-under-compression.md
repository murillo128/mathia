---
id: RGR-AF-RECOVERY-001
type: research-graph-relation
scope: arithmetic_fidelity
relation: recoverability-monotonicity-under-compression
derived: true
---

# Recoverability and monotonicity under compression

Arithmetic Fidelity now has several category-specific versions of the same source-backed boundary: once a discriminator is genuinely lost by a retained representation, downstream processing that receives no new discriminator-side information cannot recreate it.

- [[research/arithmetic_fidelity/findings/AF-001-fiberwise-recoverability-and-unconstrained-lifts|AF-001]] gives the exact set-theoretic fiber criterion and deterministic downstream monotonicity.
- [[research/arithmetic_fidelity/findings/AF-007-vertical-differential-rank-smooth-submersion-fidelity|AF-007]] gives the smooth local version through vertical differential rank and a lift-dimension lower bound.
- [[research/arithmetic_fidelity/findings/AF-009-conditional-variance-is-exact-l2-fidelity-defect|AF-009]] gives the stochastic `L^2` version: deterministic coarsening or Markov garbling can only increase the conditional-variance defect.
- [[research/arithmetic_fidelity/findings/AF-011-zero-error-stochastic-fidelity-is-support-confusability|AF-011]] gives the zero-error stochastic version through support confusability, which can only grow under garbling.
- [[research/arithmetic_fidelity/findings/AF-010-full-jet-projection-fidelity-needs-quasianalyticity-plus-cylindrical-closure|AF-010]] sharpens the smooth boundary by showing that even complete pointwise jet data need not repair lost fiber information outside a suitable quasianalytic/closure class.

These are parallel theorems in different categories, not one theorem inferred from another. Together they justify treating the location and category of a compression as part of any fidelity claim.