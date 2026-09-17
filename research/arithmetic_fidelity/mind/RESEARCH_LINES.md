# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Price retained information jointly with the admissible source class

**Linked intuitions:** `MI-001-fidelity-is-quotient-relative`, `MI-004-prime-specificity-depends-on-the-retained-analytic-layer`, `MI-018-signed-complexity-only-transfers-through-sign-regular-observations`, `MI-041-one-riesz-order-crosses-conditioning-without-moving-the-zero-discriminator`, `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class`.

AF-365--AF-370 separate exact discriminator survival from finite observation, source freedom, conditioning and source-category rigidity. Small retained data can become complete only after the admissible fibre is restricted enough to be target-pure. Recovering `zeta` inside a rigid category still does not select its nontrivial zeros. The broader question remains to identify source-class/data couplings substantially weaker than full reconstruction but strong enough to preserve the exact downstream discriminator.

## Distinguish relational order, placement generators, local analytic recovery and component topology

**Linked intuitions:** `MI-002-canonical-relational-lifts-can-restore-gauge`, `MI-019-faithful-translation-lifts-are-affine`, `MI-043-support-scale-interaction-components-bound-effective-relational-arity`, `MI-045-shrinking-mesh-solid-pf3-consistency-forces-boundary-flatness`, `MI-046-quasianalytic-flat-jet-uniqueness-closes-multiscale-pf3-recognition`, `MI-047-log-concave-curvature-closes-pf3-without-quasianalyticity`.

AF-371--AF-386 separate target-faithful translation positivity from gauge elimination, sampling density, placement compression and support topology. Dense joint prime-log sampling determines the continuous target, adjacent generators suffice at order two under connected positive support, and one consecutive row stencil generates arbitrary fixed-order Toeplitz placements on shrinking uniform lattices. None of those statements by itself removes lower-order degeneracy at order three.

AF-387 gives the fixed-lattice obstruction: a connected positive `PF_2` sequence can have every solid `3x3` Toeplitz minor nonnegative while a gapped order-three minor is negative. The obstruction is an interior zero-minor stratum, not a support gap.

AF-388--AF-389 classify how much of that boundary alias survives when **one smooth profile** must satisfy the solid `PF_2/PF_3` certificate on meshes `h_n -> 0`. With `q=-(log f)''`, the hierarchy forces `q>=0`, and every zero of `q` is infinitely flat. Cross-scale compatibility therefore recovers the complete finite Taylor-order boundary geometry that one fixed lattice can lose.

AF-390 and AF-391 give two sufficient ways to close this boundary: flat-jet unique continuation and log-concavity of `q`. AF-392 identifies the exact finite-window criterion when `q>0`, and AF-393 closes the apparent local-versus-finite-window gap: for a positive `C^4` profile, the positive-curvature order-three condition is exactly

`(log q)'' <= 2q`.

Equivalently, in the curvature-mass coordinate `Q` with `dQ=q dt` and `r=(log q)'`, the condition is `dr/dQ<=2`. Integrating this local slope bound over adjacent mass windows gives precisely the AF-392 finite-window inequalities, and differentiating the finite-window family recovers the same local condition.

AF-394 now closes the smooth zero-curvature boundary as well. For positive `C^4` `f`, the translation kernel `K_f(x,y)=f(x-y)` is `TN_3` iff `q>=0`, the positive-curvature set `{q>0}` is an interval, and `(log q)''<=2q` on that interval. Under the AF-388 shrinking solid hierarchy the first and third conditions are already forced, so **connectedness of `{q>0}` is the exact remaining global resource**. Infinitely-flat boundary zeros are allowed; a zero separating two positive regions is not.

The smooth `PF_3` recognition question is therefore no longer missing an analytic boundary criterion. The live arithmetic question is whether genuine source information can force the required sampled solid signs and the connected positive-curvature topology without assuming target positivity. A separate structural frontier is whether higher determinant orders admit any comparably sharp split between local analytic conditions and a finite topological residue.

## Separate source identification from zero selection

AF-370 identifies `zeta` exactly inside its declared source class, but Hamburger rigidity does not confine nontrivial zeros to `Re s=1/2`. The functional equation can identify the analytic object while leaving RH untouched. Future fidelity arguments must keep source identification and zero selection as orthogonal gates.

## Preserve the remaining exact source-access questions

The RH root-rate endpoint still requires cancellation-coherent access before taking the Li root-rate quotient; ordinary prefix accuracy is the wrong currency. The conditional Schanuel codimension program likewise remains open at the unconditional joint-dependence step: AF-320--AF-336 reduce exact incidence to algebraic relations on the common prime-phase tuple, but no unconditional source theorem yet excludes the required middle-singular fibre.

For every proposed destination theorem state separately the observed data, admissible source/tail class, retained analytic layer, determinant/relation order, intrinsic support-scale interaction complexity, placement-generator family, support topology/zero pattern, lower-order zero-minor/interiority pattern, cross-scale compatibility, intrinsic curvature coordinate, normalized pattern closure, coordinate covariance, residual gauge and topology/modulus of inference. AF-390--AF-394 sharpen the multiscale entry: the local analytic order-three cone is completely recognized, while connectedness of positive logarithmic curvature is the exact residual global datum. Any arithmetic application must still derive both pieces from genuine source information rather than assume target positivity.