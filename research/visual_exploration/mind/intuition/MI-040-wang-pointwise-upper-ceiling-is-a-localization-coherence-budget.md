# MI-040 — Wang's upper pointwise ceiling follows the first source-specific remainder that survives decomposition and matched controls

**Evidence level:** exact synthesis from [VIS-298](../../findings/VIS-298-wang-gamma-recentering-removes-moving-h-barrier.md) through [VIS-306](../../findings/VIS-306-bernoulli-signed-shell-hilbert-cancellation.md), using Wang's displayed localization/mean-value identities, the classical weighted Hilbert inequality and the matched Bernoulli controls audited there.

The upper pointwise boundary in Wang's short-interval pair statistic has moved repeatedly because generic estimates were applied before the exact structure of their load-bearing terms was exposed.

VIS-298 removes the lower moving-source crossover by exact gamma recentering. VIS-299--VIS-301 decompose the apparent localization ceiling and show that only one inside--outside coherence term is load-bearing; the unconditional Vinogradov--Korobov zero-free region suppresses it enough that the first generic `H`-scale obstruction moves into the interior mean-value estimate.

VIS-302 then specializes the coefficient majorant from `x log^2 x` to `x log x`. VIS-303 specializes the support and deletes the power-of-two/odd-shift sector. VIS-304 specializes the prime-power frequency geometry and obtains the absolute Hilbert-spacing cost `O(x log log x)`.

VIS-305 applies a parity- and density-matched Bernoulli control to that absolute norm. Its expected reciprocal-spacing cost is already `Theta(x log log x)`, so the absolute `log log x` layer is generic under density/parity matching and cannot by itself certify prime arithmetic.

VIS-306 strengthens the control at the exact place where VIS-305 left uncertainty: the **signed endpoint Hilbert remainder**. On the same Bernoulli-thinned odd lattice, the signed off-diagonal Dirichlet form has expectation `O(x)` and variance `O(x log^3 x)`, hence is `O_p(x)`. At the comparison scale `H~x log log x` this is `o_p(H)`. The matched support can therefore have a critical absolute spacing norm while its signed endpoint contribution cancels below the destination scale.

The current load-bearing object is no longer “signedness” in the abstract. It is whatever **source-specific phase/coherence or spacing correlation of the actual prime-power frequencies defeats the signed Bernoulli cancellation**. Any claimed `H`-scale obstruction should identify that extra arithmetic mechanism explicitly rather than inherit it from the absolute Hilbert majorant.

The reusable lesson is a layered survivor test. Preserve the exact object until the first inequality that discards structure; restore deterministic, coefficient, support and spacing information; match the generic support statistics; and then match the sign-sensitive observable itself. A nominal critical scale becomes evidence of arithmetic structure only if the actual source survives a control that cancels the same signed channel.

**Boundary.** VIS-306 is a matched negative control, not a cancellation theorem for prime powers and not a Hardy--Littlewood pair theorem. Arithmetic correlations absent from independent thinning may still produce an `H`-scale signed contribution. The fixed-power arithmetic source envelope and the RH-equivalent continuation route remain separate.