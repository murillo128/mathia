# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Price retained information jointly with the admissible source class

**Linked intuitions:** `MI-001-fidelity-is-quotient-relative`, `MI-004-prime-specificity-depends-on-the-retained-analytic-layer`, `MI-018-signed-complexity-only-transfers-through-sign-regular-observations`, `MI-041-one-riesz-order-crosses-conditioning-without-moving-the-zero-discriminator`, `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class`.

AF-365--AF-370 separate exact discriminator survival from finite observation, source freedom, conditioning and source-category rigidity. Small retained data can become complete only after the admissible fibre is restricted enough to be target-pure. Recovering `zeta` inside a rigid category still does not select its nontrivial zeros. The broader question remains to identify source-class/data couplings substantially weaker than full reconstruction but strong enough to preserve the exact downstream discriminator.

## Distinguish relational order, placement generators, support topology and curvature-boundary degeneracy

**Linked intuitions:** `MI-002-canonical-relational-lifts-can-restore-gauge`, `MI-019-faithful-translation-lifts-are-affine`, `MI-043-support-scale-interaction-components-bound-effective-relational-arity`, `MI-045-shrinking-mesh-solid-pf3-consistency-forces-boundary-flatness`, `MI-046-quasianalytic-flat-jet-uniqueness-closes-multiscale-pf3-recognition`, `MI-047-log-concave-curvature-closes-pf3-without-quasianalyticity`.

AF-371--AF-386 separate target-faithful translation positivity from gauge elimination, sampling density, placement compression and support topology. Dense joint prime-log sampling determines the continuous target, adjacent generators suffice at order two under connected positive support, and one consecutive row stencil generates arbitrary fixed-order Toeplitz placements on shrinking uniform lattices. None of those statements by itself removes lower-order degeneracy at order three.

AF-387 gives the fixed-lattice obstruction: a connected positive `PF_2` sequence can have every solid `3x3` Toeplitz minor nonnegative while a gapped order-three minor is negative. The obstruction is an interior zero-minor stratum, not a support gap.

AF-388--AF-389 classify how much of that boundary alias survives when **one smooth profile** must satisfy the solid `PF_2/PF_3` certificate on meshes `h_n -> 0`. With `q=-(log f)''`, the hierarchy forces `q>=0`, and every zero of `q` is infinitely flat. Cross-scale compatibility therefore recovers the complete finite Taylor-order boundary geometry that one fixed lattice can lose.

AF-390 closes the boundary for source classes with flat-jet unique continuation: an infinitely flat zero either cannot occur nontrivially or collapses the profile to the rank-one exponential case. AF-391 gives an independent shape closure: extended log-concavity of `q` forces continuum `TN_3`, including nonquasianalytic infinitely-flat examples.

AF-392 identifies the exact finite-window criterion when `q>0` in terms of adjacent curvature masses. AF-393 closes the apparent local-versus-finite-window gap: for a positive `C^4` profile, continuum `TN_3` is equivalent to the local differential inequality

`(log q)'' <= 2q`.

Equivalently, in the curvature-mass coordinate `Q` with `dQ=q dt` and `r=(log q)'`, the exact condition is `dr/dQ<=2`. Integrating this local slope bound over adjacent mass windows gives precisely the AF-392 finite-window inequalities, and differentiating the finite-window family recovers the same local condition. The positive-curvature recognition problem is therefore local after using the correct intrinsic coordinate; finite windows contain no additional independent constraint there.

The live smooth recognition boundary is now concentrated at zeros of `q`, where the curvature-mass coordinate degenerates. Shrinking solid consistency forces those zeros to be infinitely flat, while quasianalytic continuation and log-concavity are two sufficient ways to close the boundary. The remaining question is whether there is an exact limiting/stratified criterion across nontrivial infinitely-flat zero sets, or a weaker source/category hypothesis that excludes the residual boundary fibre. Any arithmetic application must still derive the relevant solid signs or curvature condition from genuine source information rather than assume target positivity.

## Separate source identification from zero selection

AF-370 identifies `zeta` exactly inside its declared source class, but Hamburger rigidity does not confine nontrivial zeros to `Re s=1/2`. The functional equation can identify the analytic object while leaving RH untouched. Future fidelity arguments must keep source identification and zero selection as orthogonal gates.

## Preserve the remaining exact source-access questions

The RH root-rate endpoint still requires cancellation-coherent access before taking the Li root-rate quotient; ordinary prefix accuracy is the wrong currency. The conditional Schanuel codimension program likewise remains open at the unconditional joint-dependence step: AF-320--AF-336 reduce exact incidence to algebraic relations on the common prime-phase tuple, but no unconditional source theorem yet excludes the required middle-singular fibre.

For every proposed destination theorem state separately the observed data, admissible source/tail class, retained analytic layer, determinant/relation order, intrinsic support-scale interaction complexity, placement-generator family, support topology/zero pattern, lower-order zero-minor/interiority pattern, cross-scale compatibility, intrinsic curvature coordinate, normalized pattern closure, coordinate covariance, residual gauge and topology/modulus of inference. AF-390--AF-393 sharpen the multiscale entry: in the strictly positive curvature stratum the exact global order-three condition is equivalent to one local differential slope bound in curvature mass. The unresolved recognition geometry lies at the degenerate zero-curvature boundary, not in an additional positive-interior finite-window constraint.