# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push prime-specific harmonic control from the diagonal corridor to the Ford edge

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-053-prime-halasz-turns-the-harmonic-plateau-into-an-order-one-return-gap`.

The positive-source program has progressively separated recurrence existence, source resolution, interval occupancy, atomic carrying capacity and integer-carrier discrepancy. NB-202--NB-205 push an `o(1/X_a)` positive Euler return from quadratic shell height, through every fixed polynomial scale and a quasi-polynomial derivative regime, out to the Vinogradov--Korobov height supplied by Ford's exponential-sum estimate. These are acquisition obstructions, not Nyman distance theorems.

NB-206 shows that a straightforward VMVT replacement does not automatically improve that coupled frontier: a fixed `epsilon` loss becomes fatal when the derivative/degree parameter itself grows. NB-207 removes a different artefact: Fejér/window majorants eliminate the harmonic logarithmic loss caused by naive sharp truncation.

NB-208 changes the geometry of the necessary event. A small positive Euler return forces a whole harmonic plateau of correlated prime Dirichlet-polynomial values. NB-209 showed that generic large-value estimates miss this configuration by one logarithmic dimension because they pay the ambient integer-support tariff.

NB-210 proves that this particular logarithmic deficit is not intrinsic. The Matomäki--Radziwiłł prime-supported Halász inequality carries exactly the prime-density gain the generic estimates lack, and a fixed number of harmonics gives an order-one return gap throughout each fixed subcritical range `|t|<=exp(X_a^(3/2-delta))`.

NB-211 removes the fixed-`delta` quantifier boundary by reopening the same Halász proof at the full Vinogradov--Korobov zero-free width. The resulting off-diagonal factor is epsilon-free, and the order-one positive-return gap now holds uniformly through the moving corridor

`log |t| <= kappa_* X_a^(3/2)/(log X_a)^2`.

This strictly exceeds every fixed `X_a^(3/2-delta)` scale. It still stops before the Ford corridor `X_a^(3/2)/sqrt(log X_a)` by a factor `(log X_a)^(3/2)`. At the Ford scale the zero-free contour supplies only constant exponential saving, so the polynomial prime-correlation prefactor can no longer be absorbed. The remaining boundary is therefore not prime sparsity or a hidden fixed epsilon; it is the actual off-diagonal geometry of the prime correlation kernel.

The live source-side question is now precise: exploit the fact that the forced large values occur on the phase-pinned arithmetic progression `t,2t,...`, or find another prime-specific correlation estimate that removes part of the remaining log-power gap to Ford. Increasing harmonic count inside the same inequality or invoking another generic large-value theorem is not responsive to the boundary isolated by NB-211.

A separate destination theorem is still load-bearing. One must show that a Nyman approximant resolving the target must realize the positive-return condition used by this source analysis, or identify the correct destination-coupled source condition if positivity is too restrictive. Signed/complex synthesis remains a genuinely different branch because cancellation can move between phase sectors and destroys the monotone occupancy argument.

## Keep moving-complexity uniformity, source geometry and destination conditioning explicit

The relevant currencies now include source mass, requested return tolerance, integer-cell occupancy, harmonic-window width, moving derivative order, zero-free contour width, prime-correlation polynomial prefactor, large-value multiplicity and correlation across the prime-harmonic plateau. NB-206 warns that an estimate excellent at each fixed complexity may become useless on a coupled diagonal. NB-207 shows that avoidable window losses should be removed before interpreting a logarithmic deficit as arithmetic. NB-210 shows that generic support-density losses can disappear under a source-matched theorem. NB-211 adds that even a published fixed-epsilon exponent may be only a proof-presentation boundary if the underlying contour admits uniform diagonalization.

Any continuation should therefore state the simultaneous `a_T`--`T`--complexity regime, preserve constants through moving parameters, and compare the forced plateau with a source-matched theorem in the same normalization. The next technical bottleneck is the phase-sensitive prime off-diagonal at heights where Vinogradov--Korobov gives only constant exponential saving. Only after that source theorem is established should its cost be transferred to the Nyman destination.
