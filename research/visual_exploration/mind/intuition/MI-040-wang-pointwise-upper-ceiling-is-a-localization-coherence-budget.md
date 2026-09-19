# MI-040 — Wang's upper pointwise ceiling follows the first source-specific phase channel that survives matched controls

**Evidence level:** exact synthesis from [VIS-298](../../findings/VIS-298-wang-gamma-recentering-removes-moving-h-barrier.md) through [VIS-307](../../findings/VIS-307-prime-power-random-phase-hilbert-cancellation.md), using Wang's displayed localization/mean-value identities, the classical weighted Hilbert inequality and the matched support/phase controls audited there.

The upper pointwise boundary in Wang's short-interval pair statistic has moved repeatedly because generic estimates were applied before the exact structure of their load-bearing terms was exposed.

VIS-298 removes the lower moving-source crossover by exact gamma recentering. VIS-299--VIS-301 decompose the apparent localization ceiling and show that only one inside--outside coherence term is load-bearing; the unconditional Vinogradov--Korobov zero-free region suppresses it enough that the first generic `H`-scale obstruction moves into the interior mean-value estimate.

VIS-302 then specializes the coefficient majorant from `x log^2 x` to `x log x`. VIS-303 specializes the support and deletes the power-of-two/odd-shift sector. VIS-304 specializes the prime-power frequency geometry and obtains the absolute Hilbert-spacing cost `O(x log log x)`.

VIS-305 applies a parity- and density-matched Bernoulli control to that absolute norm. Its expected reciprocal-spacing cost is already `Theta(x log log x)`, so the absolute `log log x` layer is generic under density/parity matching. VIS-306 strengthens the control to the **signed endpoint remainder**: on the Bernoulli-thinned odd lattice the signed form has expectation `O(x)` and variance `O(x log^3 x)`, hence is `o_p(H)` at `H~x log log x`.

VIS-307 then keeps the actual prime-power support instead of thinning it. Every prime and prime power, every spacing relation and every Wang coefficient magnitude is preserved; only the deterministic coefficient phases are replaced by independent Steinhaus phases `epsilon_q`. Phase orthogonality gives

`E R_I^epsilon=0`,

`E |R_I^epsilon|^2 << x log^3 x`,

uniformly in interval position and length. Thus the exact-support random-phase remainder is again `o_p(H)` at `H~x log log x`.

This removes support geometry and coefficient magnitudes as sufficient explanations of the current boundary. The first remaining source-specific candidate is **deterministic phase organization**. The independent phase control deliberately destroys the harmonic relation among powers of one base prime; it assigns unrelated phases to `p,p^2,p^3,...`. Therefore a surviving obstruction must use a coherence relation of that kind, another deterministic endpoint-phase alignment, or a comparable phase-sensitive feature absent from the Steinhaus control.

The reusable lesson is a layered survivor test. Preserve the exact object until the first inequality that discards structure; restore deterministic, coefficient, support and spacing information; match the generic support statistics; then preserve the exact support and randomize only the suspected phase channel. A nominal critical scale becomes evidence of arithmetic structure only after the actual source defeats a control that preserves everything except a clearly identified source-specific coherence.

**Boundary.** VIS-307 is a probabilistic negative control, not a cancellation theorem for the true prime-power phases and not a random-multiplicative theorem. It does not preserve the base-prime harmonic relation `epsilon_(p^k)=epsilon_p^k`. That relation, or another deterministic phase mechanism, is now the natural next discriminator; the fixed-power arithmetic source envelope and RH-equivalent continuation route remain separate.