# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Reduce the full-Euler Vinogradov--Korobov prefactor from the log-squared corridor toward the Ford edge

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-054-one-smooth-full-euler-barycenter-already-reaches-the-log-squared-corridor`.

The positive-source program has progressively separated recurrence existence, source resolution, interval occupancy, atomic carrying capacity and integer-carrier discrepancy. NB-202--NB-205 push an `o(1/X_a)` positive Euler return from quadratic shell height through the Vinogradov--Korobov acquisition regime. NB-206 shows why fixed-complexity estimates cannot be used blindly on a moving diagonal, while NB-207 removes an avoidable harmonic-window logarithm.

NB-208--NB-211 then derive an order-one positive-return gap from a phase-pinned harmonic plateau and a prime-supported Halász inequality, ultimately reaching

`log |t| <= kappa X_a^(3/2)/(log X_a)^2`.

NB-212 shows that the harmonic plateau is not what creates this log-squared scale once the full contour estimate is exposed. A **single fixed nonnegative smooth full-von-Mangoldt barycenter** inside the actual Euler shell already gives the same corridor directly: small positive Euler defect forces that barycenter close to its mass, while the Vinogradov--Korobov contour gives a strict nonzero-frequency contraction.

The remaining method boundary is now the prefactor in the source-faithful contour estimate. If the normalized error has shape

`L(Q) exp(-c X/(Q^(2/3)(log Q)^(1/3)))`,

then NB-212 proves the phase diagram: every polynomial prefactor `L(Q)=Q^(A+o(1))`, however small `A>0`, forces the same `X^(3/2)/(log X)^2` corridor; a polylogarithmic prefactor would reach `X^(3/2)/(log X)^(1/2+epsilon)` for every fixed `epsilon>0`; a bounded prefactor would permit Ford-scale access `X^(3/2)/sqrt(log X)` in principle. This is a method theorem, not a claim that the stronger source estimate exists.

The live source-side question is therefore more precise than “use more harmonics” or “improve the prime large-value theorem”: can the full smoothed von-Mangoldt correlation be proved with a genuinely subpolynomial, ideally bounded, `Q`-prefactor at the needed Vinogradov--Korobov displacement? Any proposed improvement should state exactly which contour/logarithmic-derivative factor is removed and how uniformity in the coupled `X,Q` regime is preserved.

A separate destination theorem remains load-bearing. One must still show that a Nyman approximant resolving the target must realize the positive-return condition used by this source analysis, or identify the correct destination-coupled source condition if positivity is too restrictive. Signed/complex synthesis remains a different branch because cancellation can move between phase sectors and destroys the monotone positive-source implication.

## Keep moving-complexity uniformity, source representation and contour prefactor explicit

The relevant currencies now include source mass, requested return tolerance, integer-cell occupancy, moving derivative order, zero-free contour width, the exact prefactor multiplying the contour saving, and whether the observable is prime-only or the full von-Mangoldt source. NB-210 shows that a source-matched theorem can remove a generic support-density loss. NB-211 shows that a fixed-epsilon exponent can disappear when the proof is diagonalized at the natural contour width. NB-212 adds that an apparently essential harmonic/prime-only representation can also be removed: the same corridor is already visible in one smooth full-source scalar.

Any continuation should therefore work from the source-faithful barycenter or an equally faithful observable, retain all dependence on `Q=log(10+|t|)`, and measure progress by the growth class of the prefactor rather than by a small change in a polynomial exponent. Only after that source theorem is established should its cost be transferred to the Nyman destination.