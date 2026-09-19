# MI-040 — Wang's upper pointwise ceiling follows the first source-specific remainder that survives decomposition

**Evidence level:** exact synthesis from [VIS-298](../../findings/VIS-298-wang-gamma-recentering-removes-moving-h-barrier.md) through [VIS-304](../../findings/VIS-304-wang-prime-power-spacing-loglog-boundary.md), using Wang's displayed localization and mean-value identities plus the classical Montgomery--Vaughan weighted Hilbert inequality and prime-pair upper-bound sieve as audited there.

The upper pointwise boundary in Wang's short-interval pair statistic has moved repeatedly because each generic estimate was applied before the exact structure of its load-bearing term was exposed.

VIS-298 removes the lower moving-source crossover by exact gamma recentering. VIS-299--VIS-301 then decompose the apparent localization ceiling. The pure leakage terms are already cheaper; the only load-bearing localization contribution is an inside--outside coherence term, and the unconditional Vinogradov--Korobov zero-free region suppresses it sufficiently that the first generic `H`-scale obstruction moves into the interior mean-value estimate.

VIS-302 shows that Wang's displayed Montgomery--Vaughan coefficient majorant is itself loose after source specialization. For

`a_n=(Lambda(n)/sqrt(n)) min(n/x,x/n)`,

one has

`sum_n n a_n^2=(4/3)x log x+(8/9)x+O(x exp(-cV(log x)))`,

so the complete pointwise asymptotic survives throughout `x log x=o(H)`.

VIS-303 then decomposes the actual off-diagonal source support at that scale. Powers of two have negligible energy and bounded weighted mass, which makes every odd-additive-shift contribution `o(H)` throughout `x log x=O(H)`. The first unresolved part at that layer is therefore the odd-prime-power/even-shift sector.

VIS-304 goes one step deeper and changes the relevant notion of spacing. Since `Lambda(n)` vanishes off prime powers, the nonzero frequencies are `lambda_q=log q` for prime powers `q`. Applying the weighted Montgomery--Vaughan inequality with the **nearest-neighbor spacing inside this sparse frequency set**, rather than with ambient integer spacing, yields

`|int_I |D_x(t)|^2 dt-H sum_q a_q^2| << sum_q a_q^2/delta_q`.

A dyadic reciprocal-spacing estimate based on a Brun--Selberg upper-bound sieve gives

`sum_q a_q^2/delta_q << x log log(3x)`.

Thus the same pointwise asymptotic persists whenever `x log log(3x)=o(H)`. The previous `x log x` boundary was not an intrinsic even-shift transition; it was another cost of forgetting the exact sparse frequency support before applying a classical inequality.

The current load-bearing object is now the **signed endpoint Hilbert form itself** on the prime-power logarithmic frequencies near `x log log x asymp H`. The `log log x` factor is the cost of an absolute weighted norm and an upper-bound sieve. It is not a proven term of the pair-correlation statistic and may still disappear if the endpoint phases cancel.

The reusable lesson is stronger than “specialize coefficients before estimating.” At each stage, preserve the exact object until the first inequality that loses its structure, then ask which structure that inequality discarded: deterministic recombination, source-specific coefficients, support parity, sparse frequency spacing, or finally oscillatory phase. A nominal theorem boundary is structural only after all earlier discarded structure has been restored and the surviving term itself can be matched by a lower/control construction or an exact asymptotic.

**Boundary.** VIS-304 does not prove an `x log log x` lower obstruction, a Hardy--Littlewood prime-pair asymptotic, or further cancellation in the signed Hilbert form. Its prime-spacing input is an upper-bound sieve, and the local-spacing norm may be far from sharp for the actual endpoint phases. The fixed-power arithmetic source envelope and the RH-equivalent continuation route remain separate questions.
