# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Escape the absolute-value Mellin tariff rather than merely changing source representation

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-054-one-smooth-full-euler-barycenter-already-reaches-the-log-squared-corridor`.

The positive-source program has progressively separated recurrence existence, source resolution, interval occupancy, atomic carrying capacity and integer-carrier discrepancy. NB-202--NB-205 push an `o(1/X_a)` positive Euler return from quadratic shell height through the Vinogradov--Korobov acquisition regime. NB-206 shows why fixed-complexity estimates cannot be used blindly on a moving diagonal, while NB-207 removes an avoidable harmonic-window logarithm.

NB-208--NB-211 then derive an order-one positive-return gap from a phase-pinned harmonic plateau and a prime-supported Halász inequality, ultimately reaching

`log |t| <= kappa X_a^(3/2)/(log X_a)^2`.

NB-212 shows that the harmonic plateau is not what creates this log-squared scale once the full contour estimate is exposed. A **single fixed nonnegative smooth full-von-Mangoldt barycenter** inside the actual Euler shell already gives the same corridor directly: small positive Euler defect forces that barycenter close to its mass, while the Vinogradov--Korobov contour gives a strict nonzero-frequency contraction.

The remaining method boundary is the prefactor in the source-faithful contour estimate. If the normalized error has shape

`L(Q) exp(-c X/(Q^(2/3)(log Q)^(1/3)))`,

then NB-212 proves the phase diagram: every polynomial prefactor `L(Q)=Q^(A+o(1))`, however small `A>0`, forces the same `X^(3/2)/(log X)^2` corridor; a polylogarithmic prefactor would reach `X^(3/2)/(log X)^(1/2+epsilon)` for every fixed `epsilon>0`; a bounded prefactor would permit Ford-scale access `X^(3/2)/sqrt(log X)` in principle.

NB-213 closes the most obvious representation-only repair. Replacing `-zeta'/zeta` by its primitive `log zeta` and then estimating the transferred contour absolutely does not move the prefactor into the subpolynomial class. Integration by parts differentiates the shell carrier `e^(iXv)` and costs a factor `X`; on the coupled diagonal `X=Q^(2/3+o(1))`, even an optimistically subpolynomial bound for `log zeta` therefore becomes a positive-power `Q^(2/3+o(1))` tariff. Any fixed number of ordinary primitive transfers only increases this carrier cost.

The live source-side question is now narrower: can the oscillatory Mellin carrier and the arithmetic primitive/logarithmic derivative be estimated **jointly before absolute values**, producing a genuinely `Q^(o(1))` or bounded final prefactor? Alternatively, can a source-faithful observable include a compensating reciprocal carrier factor before reconstruction? Merely improving the pointwise bound on `zeta'/zeta`, or replacing it by a nicer primitive and then using `L1` control, remains inside the log-squared method class.

A separate destination theorem remains load-bearing. One must still show that a Nyman approximant resolving the target must realize the positive-return condition used by this source analysis, or identify the correct destination-coupled source condition if positivity is too restrictive. Signed/complex synthesis remains a different branch because cancellation can move between phase sectors and destroys the monotone positive-source implication.

## Keep moving-complexity uniformity, source representation, carrier reconstruction and contour prefactor explicit

The relevant currencies now include source mass, requested return tolerance, integer-cell occupancy, moving derivative order, zero-free contour width, the exact prefactor multiplying the contour saving, whether the observable is prime-only or the full von-Mangoldt source, and the reconstruction cost introduced when derivatives are moved between the arithmetic transform and the Mellin carrier.

NB-210 shows that a source-matched theorem can remove a generic support-density loss. NB-211 shows that a fixed-epsilon exponent can disappear when the proof is diagonalized at the natural contour width. NB-212 adds that an apparently essential harmonic/prime-only representation can also be removed: the same corridor is already visible in one smooth full-source scalar. NB-213 adds the converse warning: a formally smoother representation is not cheaper if recovering the original shell observable restores a positive-power carrier factor.

Any continuation should therefore work from the source-faithful barycenter or an equally faithful observable, retain all dependence on `Q=log(10+|t|)` and `X=log x`, and measure progress by the growth class of the **final reconstructed prefactor**. Only after that source theorem is established should its cost be transferred to the Nyman destination.