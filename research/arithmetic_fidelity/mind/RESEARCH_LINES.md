# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Price retained information jointly with the admissible source class

**Linked intuitions:** `MI-001-fidelity-is-quotient-relative`, `MI-004-prime-specificity-depends-on-the-retained-analytic-layer`, `MI-018-signed-complexity-only-transfers-through-sign-regular-observations`, `MI-041-one-riesz-order-crosses-conditioning-without-moving-the-zero-discriminator`, `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class`.

AF-365--AF-370 separate exact discriminator survival from finite observation, source freedom, conditioning and source-category rigidity. Small retained data can become complete only after the admissible fibre is restricted enough to be target-pure. Recovering `zeta` inside a rigid category still does not select its nontrivial zeros. The broader question remains to identify source-class/data couplings substantially weaker than full reconstruction but strong enough to preserve the exact downstream discriminator.

## Distinguish relational order from placement-generator complexity

**Linked intuitions:** `MI-002-canonical-relational-lifts-can-restore-gauge`, `MI-019-faithful-translation-lifts-are-affine`, `MI-043-support-scale-interaction-components-bound-effective-relational-arity`.

AF-371--AF-378 separate target-faithful translation positivity from gauge elimination, sampling density and coordinate display. Uniformly discrete rows admit compact-support false positives; even `inf gap=0` can leave every support-interaction component uniformly bounded; faithful nonlinear coordinate transport preserves the sampled fibre rather than creating new information.

AF-379 and AF-381 give the complementary determining regime. Dense normalized finite row patterns determine one-sided continuous translation minors, while dense joint row/column patterns determine the fully sampled target. Vanishing tail mesh forces both closures. Since `log p_(n+1)-log p_n -> 0`, the fully prime-indexed matrices `f(log(p_i/q_j))` are target-complete for continuous translation total nonnegativity.

AF-382 compresses determinant order two further. For strictly positive continuous `f`, adjacent successor-prime rectangles generate every sampled `2x2` inequality by logarithmic mixed-difference telescoping, and the vanishing prime-log mesh then closes to global `TN_2`/log-concavity.

AF-383 shows that a different exact placement compression survives at **every fixed determinant order**. On any shrinking uniform lattice, arbitrary Toeplitz order-`k` minors are nonnegative combinations of minors with one consecutive `k`-row stencil and arbitrary column tuple; continuity then passes the lattice result to the continuum. Thus one spatial tuple is redundant at every fixed order even in the general nonnegative class.

AF-384 identifies a sufficient condition for collapsing the remaining placement axis: continuum strict total positivity through orders `<k` plus nonnegative solid order-`k` minors on shrinking lattices yields continuum `TN_k`.

AF-385 localizes that strictness burden to the same sampled generator hierarchy. It is enough that, on one sequence `h_m -> 0`, every solid Toeplitz generator `C_(j,h_m)(d)` is **strictly positive for `j<k`** and the top-order solid generators are nonnegative. Finite `k`-positivity recognition reconstructs all lattice placements, and continuity closes them to continuum `TN_k`. No independent continuum strict-positivity theorem below order `k` is required; the sampled strict margins may even collapse to zero in the continuum limit.

The fixed-order placement certificate is therefore a triangular one-parameter hierarchy over determinant order and relative offset, not the full row/column placement family. But the compression does not remove the other resources: unrestricted `PF_infinity` still needs unbounded determinant order by AF-372, every mesh retains infinitely many offsets, a vanishing mesh sequence is still needed for an unrestricted continuous profile, and the arithmetic source must still force the strict/nonnegative signs of the solid generators. The live source question is whether the RH-facing object supplies this sampled all-order sign hierarchy without importing the desired positivity as a hypothesis.

## Separate source identification from zero selection

AF-370 identifies `zeta` exactly inside its declared source class, but Hamburger rigidity does not confine nontrivial zeros to `Re s=1/2`. The functional equation can identify the analytic object while leaving RH untouched. Future fidelity arguments must keep source identification and zero selection as orthogonal gates.

## Preserve the remaining exact source-access questions

The RH root-rate endpoint still requires cancellation-coherent access before taking the Li root-rate quotient; ordinary prefix accuracy is the wrong currency. The conditional Schanuel codimension program likewise remains open at the unconditional joint-dependence step: AF-320--AF-336 reduce exact incidence to algebraic relations on the common prime-phase tuple, but no unconditional source theorem yet excludes the required middle-singular fibre.

For every proposed destination theorem state separately the observed data, admissible source/tail class, retained analytic layer, determinant/relation order, intrinsic support-scale interaction complexity, **placement-generator family**, sampled lower-order interiority, normalized pattern closure, coordinate covariance, residual gauge and topology/modulus of inference. AF-385 makes the accounting especially concrete: a tiny target-complete placement family can still require strict side information at all lower orders plus infinitely many offsets and shrinking spatial scales.
