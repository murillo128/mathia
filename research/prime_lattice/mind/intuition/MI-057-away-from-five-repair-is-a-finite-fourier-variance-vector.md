# MI-057 — Away-from-five repair is a finite Fourier variance vector

**Evidence level:** exact source/representation synthesis from [PL-414](../../findings/PL-414-away-from-5-residue-variance-projection.md), refining the actual-prime transfer boundary left by MI-056.

The source-realized `p=5` de-aliasing does not create a new infinite-dimensional prime bridge. Its multiplier on pair lags is the fixed finite Fourier projector

`g_5(h)=76/75-(4/75) sum_{j=1}^4 e(jh/5)`.

Equivalently, multiplying the prime-pair correlation by `g_5` is, up to the explicit power-of-5 exceptional terms, a normalized average over the admissible residue classes modulo `5`. For the cubic source-replacement functional this gives an exact decomposition into five ordinary quadratic variance sectors at rational frequencies `j/5`, `j=0,...,4`.

The quantitative consequence is sharp at the level already isolated by PL-407. If all five triangular source-subtracted remainders satisfy

`|Delta T_{X,j}(L)| << X L (L/X)^mu (log X)^B`,

uniformly on the effective kernel support, then the away-from-five cubic error has the same power-saving curve as before: for `H=X^theta`, it is sufficient that

`mu > 3 theta / (4(1-theta))`.

Thus the square-root calibration boundary `theta=2/5` is unchanged. The untwisted sector `j=0` alone is not enough; the repair replaces one scalar variance target by a five-component fixed-modulus vector without changing the exponent requirement.

This localizes the remaining actual-prime problem much more tightly. Model-side Euler continuation and the provenance of the `p=5` deletion are no longer the missing steps. What remains is a power-small signed estimate for a finite family of mod-5 twisted short-interval prime variances. Fixed-modulus periodicity itself is not the obstruction; the required power precision is.

**Boundary.** PL-414 supplies exact residue/Fourier identities and a conditional transfer of the PL-407 threshold, not the needed variance estimate. Existing fixed-modulus almost-all correlation technology does not by itself provide the stated power-saving signed remainder at this scale, so this intuition must not be read as an actual-prime bridge theorem.