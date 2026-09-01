---
id: RGR-AF-STABLE-DISTANCE-001
type: research-graph-relation
scope: arithmetic_fidelity
relation: stable-fidelity-distance-to-collision
derived: true
---

# Stable fidelity is measured by distance from collision

The newest Arithmetic Fidelity results give exact robustness moduli in several categories rather than merely binary injectivity tests.

- [[research/arithmetic_fidelity/findings/AF-041-stable-composition-is-range-kernel-transversality|AF-041]] expresses stable composition through a quantitative range--kernel transversality modulus.
- [[research/arithmetic_fidelity/findings/AF-042-compact-smooth-fidelity-is-injective-immersion|AF-042]] identifies compact smooth fidelity with the injective-immersion gate in its stated category.
- [[research/arithmetic_fidelity/findings/AF-043-closed-secant-transversality-classifies-linear-compression-fidelity|AF-043]] and [[research/arithmetic_fidelity/findings/AF-044-closed-secant-modulus-is-distance-to-fidelity-loss|AF-044]] turn linear compression robustness into closed-secant transversality and an exact distance to the loss set.
- [[research/arithmetic_fidelity/findings/AF-045-lower-lipschitz-modulus-is-exact-nonlinear-collision-distance|AF-045]] gives the nonlinear metric analogue: the lower Lipschitz modulus is exactly the distance to a collision map in the Lipschitz norm.

Across these source-backed categories, exact recovery and robust recovery are distinct. A map may be injective while arbitrarily close to fidelity loss; a downstream arithmetic claim that needs stable realization must therefore specify the perturbation topology and retain a positive distance-to-collision margin there.

The relation is a transversal fidelity principle only. Applying it to a concrete RH-facing construction requires that construction's own source space, controls and destination norm to satisfy the corresponding hypotheses.
