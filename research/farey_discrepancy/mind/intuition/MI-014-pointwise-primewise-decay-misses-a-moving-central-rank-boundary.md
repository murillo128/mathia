# MI-014 — Pointwise primewise ancestry decay misses a moving central-rank boundary

**Evidence level:** exact construction plus squarefree Erdős--Kac anti-concentration from [FD-132](../../findings/FD-132-pointwise-primewise-ancestry-decay-still-does-not-recover-mobius.md)

FD-131 shows that rankwise normalization can still dilute defects across prime directions. FD-132 closes the next obvious repair: even requiring the ancestry defect to vanish separately for **every fixed prime** does not coerce a source toward Möbius.

For each fixed anchor depth `K`, FD-132 constructs one infinite squarefree sign source `a^(K)=mu b_K` which agrees exactly with Möbius whenever `omega(n)<=K` but flips sign above a moving central-rank boundary near `omega(n)=log log n`. The changed coefficients have asymptotic density `1/(2 zeta(2))`, so the source stays macroscopically separated from Möbius.

Nevertheless, for every fixed prime `p`, multiplication by `p` crosses the gauge boundary only when `omega(n)` lies in a bounded-width strip around its normal order. Squarefree Erdős--Kac anti-concentration makes that strip negligible, giving

`P_(p,r,H)(a^(K)) -> 0`

for each fixed `p`. The same conclusion holds uniformly over every fixed finite set of primes and after any fixed summable weighting of the primewise defects.

The obstruction is therefore an **order-of-quantifiers failure**. Pointwise convergence in the prime coordinate does not control a defect whose active coordinate set drifts outward with the scale. A viable ancestry law must keep a scale-growing family of prime directions simultaneously visible, for example through a genuinely uniform bound such as `sup_(p<=P(H)) P_(p,r,H)`, a scale-dependent/nonsummable directional norm, local `L^infinity` control, a growing exact anchor, or a destination-side coercive inequality that bypasses coefficient recovery.

FD-132 does not prove that any of those stronger currencies suffice. In particular, its Erdős--Kac input keeps `p` fixed and gives no counterexample to a suitable growing-prime uniformity theorem. The reusable boundary is precise: **“for every fixed prime, defect tends to zero” is still weaker than active-scale multiplicative coherence.**
