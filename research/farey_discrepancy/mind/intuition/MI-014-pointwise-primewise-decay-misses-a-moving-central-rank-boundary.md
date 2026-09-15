# MI-014 — Polynomial active-prime mean ancestry still misses a moving central-rank boundary

**Evidence level:** exact construction plus squarefree Erdős--Kac anti-concentration from [FD-132](../../findings/FD-132-pointwise-primewise-ancestry-decay-still-does-not-recover-mobius.md) and [FD-133](../../findings/FD-133-uniform-polynomial-prime-ancestry-decay-still-does-not-recover-mobius.md)

FD-132 first shows that requiring the ancestry defect to vanish separately for every fixed prime does not coerce a source toward Möbius. FD-133 strengthens the same obstruction from fixed coordinates to a polynomially growing active family.

For each fixed anchor depth `K`, the same infinite squarefree sign source `a^(K)=mu b_K` agrees exactly with Möbius on `omega(n)<=K` and differs from Möbius on asymptotic density `1/(2 zeta(2))`. Its sign change occurs across a moving central-rank boundary near `omega(n)=log log n`.

For every fixed `0<alpha<1` and fixed finite `r>=1`, FD-133 proves

`sup_(p<=H^alpha) P_(p,r,H)(a^(K)) -> 0`.

The uniformity is genuine: for `X=H/p>=H^(1-alpha)`, every bad `p`-edge outside a negligible square-root prefix lies in one fixed-width strip `|omega(n)-log log X|<=C_alpha`; unconditioned squarefree Erdős--Kac makes that strip `o(X)` uniformly in the active prime, and an elementary squarefree count keeps the prime-exclusion denominator uniformly comparable to `X`.

The obstruction is therefore stronger than an order-of-quantifiers failure over fixed primes. **Primewise mean normalization can hide a defect even while all prime directions up to every fixed polynomial cutoff are monitored simultaneously**, because the bad edges migrate in multiplicative rank and remain sparse inside each direction.

What FD-133 does not close is equally important. It does not control a simultaneous rank-and-prime norm, edgewise/local `L^infinity` ancestry, a scale-sensitive nonsummable norm that magnifies the central layer, a growing exact anchor, or the regime `alpha=alpha(H)->1`. Nor does it rule out a destination-side Fourier-skeleton coercive inequality that bypasses coefficient recovery.

The reusable boundary is now: **active-prime breadth alone is not active-scale multiplicative coherence when the normalization still averages over rank.** A viable ancestry law must keep the moving rank interface visible as well as the growing prime family, or use a different coercive currency entirely.
