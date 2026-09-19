# MI-040 — Wang's upper pointwise ceiling follows the first source-specific remainder that survives decomposition and matched controls

**Evidence level:** exact synthesis from [VIS-298](../../findings/VIS-298-wang-gamma-recentering-removes-moving-h-barrier.md) through [VIS-305](../../findings/VIS-305-cramer-parity-control-loglog-spacing-norm.md), using Wang's displayed localization/mean-value identities, the classical weighted Hilbert inequality and the matched Bernoulli spacing control audited there.

The upper pointwise boundary in Wang's short-interval pair statistic has moved repeatedly because generic estimates were applied before the exact structure of their load-bearing terms was exposed.

VIS-298 removes the lower moving-source crossover by exact gamma recentering. VIS-299--VIS-301 decompose the apparent localization ceiling and show that only one inside--outside coherence term is load-bearing; the unconditional Vinogradov--Korobov zero-free region suppresses it enough that the first generic `H`-scale obstruction moves into the interior mean-value estimate.

VIS-302 then specializes the coefficient majorant. For Wang's exact `a_n`, the generic `x log^2 x` cost drops to `x log x`. VIS-303 specializes the support: powers of two carry negligible energy and bounded weighted mass, so at `x log x=O(H)` every odd-additive-shift term is `o(H)`. VIS-304 specializes the frequency geometry as well. Applying the weighted Hilbert inequality on the nonzero prime-power frequencies `log q` gives an absolute spacing cost

`sum_q a_q^2/delta_q << x log log(3x)`,

and hence the pointwise asymptotic throughout `x log log(3x)=o(H)`.

VIS-305 applies the missing matched-control test to that last norm. A parity- and density-matched independent support on the odd lattice already has expected reciprocal-spacing cost of order `x log log x` under the same Wang-scale weights. The logarithm comes from ordinary geometric nearest-gap statistics; no prime-pair arithmetic is needed to create it. Therefore the `log log x` absolute norm cannot by itself be interpreted as a source-specific prime barrier.

The current load-bearing object is the **signed endpoint Hilbert form itself**, or arithmetic spacing information stronger than density/parity-level sparsity. A further improvement must exploit endpoint phase cancellation or correlations of the actual prime-power support that the Bernoulli control lacks. Merely sharpening a nearest-neighbor bound while retaining only density and parity cannot remove the scale uniformly.

The reusable lesson is a layered survivor test. Preserve the exact object until the first inequality that discards structure; restore the discarded deterministic, coefficient, support and spacing information; then run a matched control that preserves the generic features still used by the bound. A nominal critical scale becomes evidence of arithmetic structure only if it survives that matched control or if the remaining signed term itself is shown to attain the scale.

**Boundary.** VIS-305 does not prove a lower bound for the true prime-power spacing sum or for Wang's signed endpoint remainder, and it does not supply a Hardy--Littlewood pair theorem. The fixed-power arithmetic source envelope and the RH-equivalent continuation route remain separate. The `x log log x` layer is still a proof boundary, now known to be reproducible by a non-arithmetic density/parity control at the absolute-spacing level.
