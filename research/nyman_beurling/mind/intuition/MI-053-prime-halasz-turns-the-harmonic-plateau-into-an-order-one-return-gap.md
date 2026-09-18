# MI-053 — Prime Halasz turns the harmonic plateau into an order-one return gap

**Evidence level:** literature-backed synthesis from [NB-208](../../findings/NB-208-positive-euler-return-forces-a-prime-harmonic-plateau.md), [NB-209](../../findings/NB-209-generic-large-values-miss-the-prime-harmonic-plateau-by-one-logarithm.md), and [NB-210](../../findings/NB-210-prime-halasz-converts-harmonic-plateau-into-constant-gap.md). The prime-supported Halasz inequality is classical; the Mathia content is its use on the deterministic harmonic family forced by positive Euler alignment.

A small positive Euler return is not an isolated large-value event. NB-208 shows that it forces a whole family of prime phase sums at the harmonics `t,2t,...` to remain near maximal. NB-209 found that generic integer-support large-value estimates still lose one logarithmic dimension because they charge the ambient support rather than the density of primes.

NB-210 identifies that loss as methodological rather than intrinsic. The Matomaki--Radziwill prime-supported Halasz inequality includes the missing `1/log P` gain in the coefficient square sum. After normalization, the generic `X_a^2` baseline collapses to order one. A **fixed** number of forced harmonics is then enough to contradict any sufficiently small constant positive Euler defect whenever

`1 <= |t| <= exp(X_a^(3/2-delta))`

for any fixed `delta>0` and sufficiently small `a`. In this whole subcritical regime the source-side obstruction is therefore an order-one gap, stronger than the earlier `Omega(1/X_a)` exclusion.

This changes the interpretation of the prime-harmonic plateau. Its value is not simply that correlation provides “more samples.” The forced family places the large values in exactly the prime-supported geometry for which a source-matched theorem avoids the generic sparsity tariff. The reusable lesson is to test whether an apparent support-density obstruction belongs to the object or only to the comparison theorem.

The result does **not** subsume the outer Ford frontier. Ford's integer exponential-sum estimate still excludes the much smaller `o(1/X_a)` returns up to `exp(kappa X_a^(3/2)/sqrt(log X_a))`. What blocks the prime-Halasz route from matching that height is now the height-dependent off-diagonal/error factor in the prime-specific inequality, not the `1/log x` density of the prime support.

The source frontier has therefore moved from “exploit the correlated plateau” to a sharper endpoint-uniformity question: can the prime-specific harmonic estimate retain an order-one gap as the logarithmic height approaches the Ford scale, or is its off-diagonal term an intrinsic barrier? That question is separate from the destination problem of proving that a target-quality Nyman approximant must realize the positive Euler return condition in the first place.

**Boundary.** This is a positive-source acquisition result. It does not improve the Ford outer height, prove the required Nyman destination implication, apply to arbitrary signed/complex synthesis, or establish RH. The order-one gap is proved only in every fixed `3/2-delta` subcritical exponent regime.
