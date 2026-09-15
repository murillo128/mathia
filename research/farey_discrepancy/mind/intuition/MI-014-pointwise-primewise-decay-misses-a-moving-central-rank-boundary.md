# MI-014 — Almost-full active-prime mean ancestry still misses a moving central-rank boundary

**Evidence level:** exact construction plus squarefree Erdős--Kac anti-concentration from [FD-132](../../findings/FD-132-pointwise-primewise-ancestry-decay-still-does-not-recover-mobius.md), [FD-133](../../findings/FD-133-uniform-polynomial-prime-ancestry-decay-still-does-not-recover-mobius.md), and [FD-134](../../findings/FD-134-almost-full-prime-family-mean-ancestry-decay-still-does-not-recover-mobius.md)

FD-132 first shows that requiring the ancestry defect to vanish separately for every fixed prime does not coerce a source toward Möbius. FD-133 strengthens the same obstruction to every fixed polynomial active-prime family. FD-134 shows that the fixed-power boundary was not the real limit: the same one infinite source survives a large explicit `H^(1-o(1))` family.

For each fixed anchor depth `K`, the squarefree sign source `a^(K)=mu b_K` agrees exactly with Möbius on `omega(n)<=K` and differs from Möbius on asymptotic density `1/(2 zeta(2))`. Its sign change occurs across a moving central-rank boundary near `omega(n)=log log n`.

Let `P(H)<H`, `Y(H)=H/P(H)`, and assume `Y(H)->infinity` together with

`1 + log(log H/log Y(H)) = o(sqrt(log log Y(H)))`.

Then for every fixed finite `r>=1`, FD-134 proves

`sup_(p<=P(H)) P_(p,r,H)(a^(K)) -> 0`.

The bad edges lie in a rank strip whose width is `O(1+log(log H/log Y))`. The displayed condition makes that width negligible relative to the squarefree Erdős--Kac fluctuation scale at the smallest parent horizon, so one unconditioned anti-concentration estimate controls every active prime simultaneously.

Writing `P(H)=H^(1-delta(H))`, the construction therefore survives many cutoffs with `delta(H)->0`; for example `delta(H)=exp(-(log log H)^(1/3))`. The present proof mechanism stops only when `log(1/delta(H))` reaches the order of `sqrt(log log H)`, where the displaced rank strip is no longer negligible on the Gaussian scale. That is a boundary of this witness/proof, not a coercivity theorem.

The obstruction is therefore stronger than either fixed-coordinate or fixed-power quantifier failure. **Primewise mean normalization can monitor an almost-full active-prime family and still miss a positive-density source defect because the defect migrates through multiplicative rank.** Increasing directional breadth is not enough while each direction averages over the moving rank interface.

What remains genuinely different is simultaneous rank-and-prime localization, edgewise/local `L^infinity` ancestry, a weighting that gives nonvanishing mass to an `o(sqrt(log log X))` central strip, a growing exact anchor, cutoffs beyond the FD-134 condition, or destination-side Fourier-skeleton coercivity that avoids coefficient recovery.

The reusable boundary is: **active-prime breadth alone is not active-scale multiplicative coherence when normalization still averages over rank.** A viable source law must keep the moving rank interface visible as the prime family grows, rather than merely push the prime cutoff closer to `H`.