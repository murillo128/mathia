# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push prime-specific harmonic control from subcritical height to the Ford edge

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-053-prime-halasz-turns-the-harmonic-plateau-into-an-order-one-return-gap`.

The positive-source program has progressively separated recurrence existence, source resolution, interval occupancy, atomic carrying capacity and integer-carrier discrepancy. NB-202--NB-205 push an `o(1/X_a)` positive Euler return from quadratic shell height, through every fixed polynomial scale and a quasi-polynomial derivative regime, out to the Vinogradov--Korobov height supplied by Ford's exponential-sum estimate. These are acquisition obstructions, not Nyman distance theorems.

NB-206 shows that a straightforward VMVT replacement does not automatically improve that coupled frontier: a fixed `epsilon` loss becomes fatal when the derivative/degree parameter itself grows. Any higher-moment input must retain quantitatively uniform dependence on the moving complexity rather than merely improve a fixed-degree exponent. NB-207 removes a different artefact: Fejér/window majorants eliminate the harmonic logarithmic loss caused by naive sharp truncation.

NB-208 then changes the geometry of the necessary event. A small positive Euler return forces not one anomalously large prime Dirichlet-polynomial value but a whole harmonic plateau of correlated large values. NB-209 showed that generic large-value estimates miss this configuration by one logarithmic dimension because they pay the ambient integer-support tariff.

NB-210 proves that this particular logarithmic deficit is **not intrinsic**. The Matomäki--Radziwiłł prime-supported Halász inequality carries exactly the prime-density gain that the generic estimates lack. Combined with the forced harmonic plateau, a fixed number of harmonics already rules out every sufficiently small constant positive return throughout each fixed subcritical range

`1 <= |t| <= exp(X_a^(3/2-delta))`,  `delta>0`.

Thus the positive-return obstruction in this region is order one, not merely `Omega(1/X_a)`. The remaining gap to the Ford frontier is no longer prime sparsity or failure to exploit the plateau. It is the height-dependent off-diagonal/error term in the prime-specific Halász inequality, together with the uniformity required as one approaches the `X_a^(3/2)` endpoint. Ford still reaches the larger height `exp(kappa X_a^(3/2)/sqrt(log X_a))`, but at the weaker `o(1/X_a)` return tolerance.

The live source-side question is therefore precise: determine whether the prime-specific correlated-harmonic method can be sharpened toward the Ford edge without losing the order-one return gap, or prove an intrinsic barrier in that off-diagonal term. Merely applying another generic large-value theorem is no longer responsive to the obstruction that remains.

A separate destination theorem is still load-bearing. One must show that a Nyman approximant resolving the target must realize the positive-return condition used by this source analysis, or identify the correct destination-coupled source condition if positivity is too restrictive. Signed/complex synthesis remains a genuinely different branch because cancellation can move between phase sectors and destroys the monotone occupancy argument.

## Keep moving-complexity uniformity, source geometry and destination conditioning explicit

The relevant currencies now include source mass, requested return tolerance, integer-cell occupancy, harmonic-window width, moving derivative order, exponential-sum loss, prime-specific off-diagonal error, large-value multiplicity and correlation across the prime-harmonic plateau. NB-206 is the warning that an estimate which is excellent at each fixed complexity may become useless on the diagonal where complexity grows with the source scale. NB-207 is the complementary warning that avoidable window losses should be removed before interpreting a logarithmic deficit as arithmetic. NB-210 adds a third warning: a support-density loss in a generic theorem can disappear completely once the theorem is matched to the actual prime-supported geometry.

Any continuation should therefore state the simultaneous `a_T`--`T`--complexity regime, preserve uniform constants through the moving parameter, and compare the forced plateau with a source-matched theorem in the same normalization. The next technical bottleneck is the height dependence of the prime-specific bound near the endpoint, not the `1/log x` density of primes. Only after that source theorem is established should its cost be transferred to the Nyman destination.
