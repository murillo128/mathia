# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Price retained information jointly with the admissible source class

**Linked intuitions:** `MI-001-fidelity-is-quotient-relative`, `MI-004-prime-specificity-depends-on-the-retained-analytic-layer`, `MI-018-signed-complexity-only-transfers-through-sign-regular-observations`, `MI-041-one-riesz-order-crosses-conditioning-without-moving-the-zero-discriminator`, `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class`.

AF-365--AF-370 separate exact discriminator survival from finite observation, source freedom, conditioning and source-category rigidity. Small retained data can become complete only after the admissible fibre is restricted enough to be target-pure. Recovering `zeta` inside a rigid category still does not select its nontrivial zeros. The broader question remains to identify source-class/data couplings substantially weaker than full reconstruction but strong enough to preserve the exact downstream discriminator.

## Distinguish relational order, placement generators, support topology, lower-order interiority and multiscale compatibility

**Linked intuitions:** `MI-002-canonical-relational-lifts-can-restore-gauge`, `MI-019-faithful-translation-lifts-are-affine`, `MI-043-support-scale-interaction-components-bound-effective-relational-arity`, `MI-045-shrinking-mesh-solid-pf3-consistency-forces-boundary-flatness`, `MI-046-quasianalytic-flat-jet-uniqueness-closes-multiscale-pf3-recognition`.

AF-371--AF-386 separate target-faithful translation positivity from gauge elimination, sampling density, placement compression and support topology. Dense joint prime-log sampling determines the continuous target, adjacent generators suffice at order two under connected positive support, and one consecutive row stencil generates arbitrary fixed-order Toeplitz placements on shrinking uniform lattices. None of those statements by itself removes lower-order degeneracy at order three.

AF-387 gives the fixed-lattice obstruction: a connected positive `PF_2` sequence can have every solid `3x3` Toeplitz minor nonnegative while a gapped order-three minor is negative. The obstruction is an interior zero-minor stratum, not a support gap.

AF-388--AF-389 classify how much of that boundary alias survives when **one smooth profile** must satisfy the solid `PF_2/PF_3` certificate on meshes `h_n -> 0`. With `q=-(log f)''`, the hierarchy forces `q>=0`, and every zero of `q` is infinitely flat. Cross-scale compatibility therefore recovers the entire finite Taylor-order boundary geometry that one fixed lattice can lose.

AF-390 now closes this recognition problem for every source class with flat-jet unique continuation for `q`. If an infinitely flat zero forces `q≡0`, then either `q>0` everywhere, giving strict sampled order-two minors and allowing AF-385 to upgrade the solid generators to continuum `TN_3`, or `q≡0`, giving the rank-one exponential kernel, which is already totally nonnegative. Real analyticity is only one sufficient case; quasianalytic Denjoy--Carleman regularity of `q` is the broader mechanism. The extra source resource is therefore **uniqueness from the jet that the multiscale certificate has already recovered**, not analyticity as such.

The remaining smooth boundary is sharper. Determine whether a genuinely non-quasianalytic infinitely-flat `q>=0` can satisfy the full shrinking-mesh solid `PF_2/PF_3` hierarchy while some non-solid continuum `3x3` minor is negative, or whether a weaker class-specific exclusion than full quasianalyticity already rules this out. In every case the arithmetic source must still force the required generator signs rather than inherit target positivity as a hypothesis.

## Separate source identification from zero selection

AF-370 identifies `zeta` exactly inside its declared source class, but Hamburger rigidity does not confine nontrivial zeros to `Re s=1/2`. The functional equation can identify the analytic object while leaving RH untouched. Future fidelity arguments must keep source identification and zero selection as orthogonal gates.

## Preserve the remaining exact source-access questions

The RH root-rate endpoint still requires cancellation-coherent access before taking the Li root-rate quotient; ordinary prefix accuracy is the wrong currency. The conditional Schanuel codimension program likewise remains open at the unconditional joint-dependence step: AF-320--AF-336 reduce exact incidence to algebraic relations on the common prime-phase tuple, but no unconditional source theorem yet excludes the required middle-singular fibre.

For every proposed destination theorem state separately the observed data, admissible source/tail class, retained analytic layer, determinant/relation order, intrinsic support-scale interaction complexity, placement-generator family, support topology/zero pattern, lower-order zero-minor/interiority pattern, cross-scale compatibility, normalized pattern closure, coordinate covariance, residual gauge and topology/modulus of inference. AF-390 sharpens the multiscale entry: compatible observations can recover the entire local boundary jet, and a declared source class may then turn that recovered jet into global recognition; without such rigidity an infinitely-flat noncompact stratum can remain.