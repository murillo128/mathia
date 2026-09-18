# MI-064 — Exact-real prime-shell bias is a subset-sum side channel

**Evidence level:** exact synthesis from [MC-296](../../findings/MC-296-prime-shell-character-bias-is-an-arithmetic-observable.md), [MC-338](../../findings/MC-338-posterior-predictability-prices-endpoint-dephasing.md), and [MC-368](../../findings/MC-368-prime-shell-bias-subset-sum-side-channel.md).

On the even-rank punctured-cube endpoint source, let `X_i` be the source signs and `d_i` the normalized masses of the prime-shell cells. The scalar shell bias is

`T=sum_i d_i X_i = 1-2 d(J)`,

where `J` is the subset of negative coordinates. Thus an apparently one-dimensional arithmetic observable is exactly a subset-sum code for the sign pattern.

Its information content is discontinuous in the coefficient geometry. At exact balance `d_i=1/R`, the scalar sees essentially only Hamming weight and the squared own-phase predictability is

`rho_i^2=(2^R-R)/(R(2^R-1)) ~ 1/R`,

so exact dephasing still costs energy of order `R`. But if the cell multiplicities are perturbed to distinct binary-weighted integers, all subset sums become distinct and `T` recovers the complete source, giving `rho_i=1` for every coordinate. These injective multiplicity vectors can be normalized arbitrarily close to balance.

Therefore approximate equidistribution of shell masses does not by itself imply low leakage under exact-real observation. A scalar can carry exponentially many discrete states when its coefficients provide enough resolving precision. The relevant acquisition currency must include a canonical resolution/noise/coarsening scale, an arithmetic theorem forcing additive collisions, or an inverse-conditioning modulus for the subset-sum map—not merely coefficient closeness or transcript dimension.

This complements the coordinate/parity-query tariffs of MC-366--MC-367. Those results price source access once an acquisition architecture is fixed. MC-368 shows that the actual arithmetic shell statistic may belong to a richer nonlinear side-channel class in which one exact real number can already encode the whole source. Any endpoint contradiction must therefore audit the physical precision and conditioning of that scalar before treating it as low-dimensional information.

**Boundary.** The theorem is for the exact endpoint partition and exact-real access. The injective near-balanced family is a matched-control construction, not a theorem that the actual prime multiplicities realize binary subset-sum coding. It does not estimate `M(x)` or prove an RH-scale Möbius bound.