---
id: RGR-AF-STABLE-DISTANCE-001
type: research-graph-relation
scope: arithmetic_fidelity
relation: stable-fidelity-distance-to-collision
derived: true
---

# Stable fidelity is measured by distance from collision or repair geometry

[[research/arithmetic_fidelity/findings/AF-041-stable-composition-is-range-kernel-transversality|AF-041]]--[[research/arithmetic_fidelity/findings/AF-045-lower-lipschitz-modulus-is-exact-nonlinear-collision-distance|AF-045]] turn robust deterministic fidelity into exact transversality and distance-to-collision moduli in operator, smooth, linear-secant and nonlinear Lipschitz categories.

The stochastic zero-error results add a complementary boundary rather than a universal extension of that theorem. [[research/arithmetic_fidelity/findings/AF-046-zero-error-fidelity-has-zero-tv-robustness|AF-046]] shows that exact support-disjoint recovery can have zero robustness even where output laws remain separated by a positive TV margin. [[research/arithmetic_fidelity/findings/AF-047-zero-error-tv-repair-is-bayes-error-plus-hall-coverage|AF-047]]--[[research/arithmetic_fidelity/findings/AF-050-f-divergence-zero-error-repair-reduces-to-binary-penalties|AF-050]] give exact projection distances to the zero-error set in several row-separable geometries, while [[research/arithmetic_fidelity/findings/AF-051-quadratic-zero-error-repair-is-clone-granularity-sensitive|AF-051]] shows that changing to quadratic geometry introduces representation-sensitive concentration/cardinality data.

Across these source-backed categories, exact recovery, robust recovery and minimum repair are distinct questions. A downstream arithmetic claim that needs stability must specify the perturbation geometry in which a positive margin is required; a margin proved in one metric or representation cannot be silently transferred to another.
