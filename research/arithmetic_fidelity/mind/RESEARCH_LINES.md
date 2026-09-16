# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Price retained information jointly with the admissible source class

**Linked intuitions:** `MI-001-fidelity-is-quotient-relative`, `MI-004-prime-specificity-depends-on-the-retained-analytic-layer`, `MI-018-signed-complexity-only-transfers-through-sign-regular-observations`, `MI-041-one-riesz-order-crosses-conditioning-without-moving-the-zero-discriminator`, `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class`.

AF-365--AF-370 separate exact discriminator survival from finite observation, source freedom, conditioning and source-category rigidity. Small retained data can become complete only after the admissible fibre is restricted enough to be target-pure. Recovering `zeta` inside a rigid category still does not select its nontrivial zeros. The broader question remains to identify source-class/data couplings substantially weaker than full reconstruction but strong enough to preserve the exact downstream discriminator.

## Distinguish relational order, placement generators, support topology, lower-order interiority and multiscale compatibility

**Linked intuitions:** `MI-002-canonical-relational-lifts-can-restore-gauge`, `MI-019-faithful-translation-lifts-are-affine`, `MI-043-support-scale-interaction-components-bound-effective-relational-arity`, `MI-045-shrinking-mesh-solid-pf3-consistency-forces-boundary-flatness`.

AF-371--AF-386 separate target-faithful translation positivity from gauge elimination, sampling density, placement compression and support topology. Dense joint prime-log sampling determines the continuous target, adjacent generators suffice at order two under connected positive support, and one consecutive row stencil generates arbitrary fixed-order Toeplitz placements on shrinking uniform lattices. None of those statements by itself removes lower-order degeneracy at order three.

AF-387 gives the fixed-lattice obstruction: a connected positive `PF_2` sequence can have every solid `3x3` Toeplitz minor nonnegative while a gapped order-three minor is negative. The obstruction is an interior zero-minor stratum, not a support gap.

AF-388--AF-389 now classify how much of that boundary alias survives when **one smooth profile** must satisfy the solid `PF_2/PF_3` certificate on meshes `h_n -> 0`. With `q=-(log f)''`, the hierarchy forces `q>=0`, and AF-389 proves that every zero of `q` is infinitely flat. Every finite-order contact `q(x_0+y)=c y^(2m)+o(y^(2m))` is incompatible with the shrinking solid order-three determinants. Cross-scale compatibility therefore recovers the entire finite Taylor-order boundary geometry that one fixed lattice can lose.

The analytic category is correspondingly rigid. For positive real-analytic `f`, either `q>0` everywhere or `q≡0`, hence `f=e^(ax+b)`; a positive integrable analytic profile cannot take the affine-log alternative. This still does **not** prove continuum `TN_3`: in the smooth category an infinitely-flat zero of `q` remains possible, and even elimination of that stratum must still be connected to arbitrary-placement order-three positivity.

The sharp remaining recognition question is now whether an infinitely-flat `PF_2` boundary contact can coexist with the full shrinking-mesh solid `PF_2/PF_3` hierarchy while some non-solid continuum `3x3` minor is negative. If not, identify the minimal regularity/unique-continuation hypothesis that closes the last boundary stratum without simply assuming strict lower-order positivity. In every case the arithmetic source must still force the required generator signs rather than inherit target positivity as a hypothesis.

## Separate source identification from zero selection

AF-370 identifies `zeta` exactly inside its declared source class, but Hamburger rigidity does not confine nontrivial zeros to `Re s=1/2`. The functional equation can identify the analytic object while leaving RH untouched. Future fidelity arguments must keep source identification and zero selection as orthogonal gates.

## Preserve the remaining exact source-access questions

The RH root-rate endpoint still requires cancellation-coherent access before taking the Li root-rate quotient; ordinary prefix accuracy is the wrong currency. The conditional Schanuel codimension program likewise remains open at the unconditional joint-dependence step: AF-320--AF-336 reduce exact incidence to algebraic relations on the common prime-phase tuple, but no unconditional source theorem yet excludes the required middle-singular fibre.

For every proposed destination theorem state separately the observed data, admissible source/tail class, retained analytic layer, determinant/relation order, intrinsic support-scale interaction complexity, placement-generator family, support topology/zero pattern, lower-order zero-minor/interiority pattern, cross-scale compatibility, normalized pattern closure, coordinate covariance, residual gauge and topology/modulus of inference. AF-389 sharpens the multiscale entry: compatible observations can eliminate every finite-order boundary alias while leaving an infinitely-flat noncompact stratum and the separate destination-selection problem untouched.