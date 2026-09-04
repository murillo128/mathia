---
id: CLUE-xi-flow-overlap-discriminant-taper-summation-by-parts
type: research-clue
status: accepted
origin: research-watch
target_line: xi_flow
based_on:
  - research/xi_flow/findings/XF-027-normalized-block-discriminant-has-square-production-and-affine-exterior-cancellation.md
  - research/xi_flow/findings/XF-028-overlapping-normalized-discriminants-make-covered-collisions-positive.md
---

# Can overlapped discriminant flux be localized by discrete taper derivatives?

## Observation

`XF-027` gives each normalized block discriminant an exact internal square production and removes the affine part of the exterior field, but a hard block still has a near-boundary flux defect. `XF-028` shows that positive overlap repairs the leading collision-wall sign: for block-start weights `a_j`, an adjacent pair has coverage

`W_k = sum_{j=k-n+2}^k a_j`

and a covered collision contributes `8 W_k / epsilon^2 + O(1/epsilon)`.

There is an additional exact piece of the overlap geometry. With `m=n-1`,

`W_k-W_{k-1}=a_k-a_{k-m}`.

Hence pair coverage is a box convolution of the taper, while variation of that coverage is exactly a shifted taper difference. A slowly varying nonnegative taper can therefore maintain a broad positive-coverage core while moving all coverage variation into a buffer-shaped boundary layer. This identity is deterministic; it does not imply that the full Xi-flow derivative localizes in the same way.

## Research question

For the finite-gap derivative of

`K_{n,a} = sum_j a_j J_j`,

can the exterior/non-affine and block-interface terms be reorganized by discrete summation by parts so that the localization loss depends on one or more discrete differences of `a_j` (or equivalently controlled differences of the pair-coverage weights), rather than on the full mass of the taper?

A useful positive theorem would combine the exact square production of `XF-027` with the pair-coverage mechanism of `XF-028`: retain `W_k >= w_* > 0` on a target core while choosing a super-mesoscopic buffer over which the taper differences are small enough that the remaining finite-gap flux is lower order.

## Why it may matter

`XF-028` explicitly leaves finite-gap sign and support-edge flux as the next obstruction after collision-wall coverage is repaired. If overlap admits a genuine summation-by-parts localization, taper width becomes a quantitative resource that can be matched to the super-mesoscopic buffer already available in the Xi-flow program. That would turn a hard membership defect into a scale-budget question.

If no such decomposition or bound is possible, an explicit finite configuration with positive core coverage but negative aggregate derivative would provide a clean obstruction and prevent further effort on taper engineering.

## Decisive test

Starting from the exact identity for each block,

`J_j' = 4 ||q^(j)||^2 + 4 <q^(j), e^(j)>`,

derive the derivative of `K_{n,a}` without discarding finite-gap terms. Express the aggregate in pair/block coordinates and attempt a discrete summation-by-parts decomposition separating a nonnegative core production term weighted by pair coverage, the far-field terms already controlled by the affine cancellation/cubic leakage of `XF-027`, and localization terms whose coefficients contain explicit discrete differences of `a`.

Then either prove a bound in which the localization terms are lower order or strictly dominated by production for a nonnegative taper varying across the available Xi buffer, uniformly at the source-relevant scale, or construct a finite real-rooted logarithmic-particle configuration showing that the aggregate can remain negative by an order-one amount even as the taper differences tend to zero at fixed positive core coverage.

The counterexample test should increase the buffer width rather than use only one hard edge, so it distinguishes a genuinely nonlocal obstruction from the already-known single-block boundary spike.

## Evidence boundary

The convolution identity for `W_k` is elementary and exact, and `XF-027`/`XF-028` establish the blockwise production, affine cancellation, and near-collision pair-coverage asymptotic.

No summation-by-parts formula for the full aggregate derivative has been established, no uniform Xi-flow flux bound is known here, and slow taper variation is not evidence of monotonicity. This clue proposes the missing derivation or falsifying counterexample; it does not assert that tapering closes the Xi-flow argument.

## Research disposition

Accepted for continued investigation. `XF-029` proves the desired localization mechanism at quadratic order around the arithmetic lattice for overlapping three-root discriminants: the weighted derivative splits into positive Cauchy production plus a commutator potential whose coefficient is `La`, and a width-`M` smooth taper has `||La||_infinity=O(1/M)`. Combined with the existing Xi memory and buffer scales, that perturbative loss is smaller than memory-scale Cauchy production by `O(1/R(T))` when the physical buffer is `R(T) log T`.

This does **not** resolve the clue's finite-gap question. The remaining decisive test is an exact nonlinear analogue of the Cauchy commutator estimate, preserving the collision positivity of `XF-028` and the affine/cubic far-field cancellation of `XF-027`, or a growing-buffer counterexample showing that an order-one nonlinear defect survives even when taper variation tends to zero.