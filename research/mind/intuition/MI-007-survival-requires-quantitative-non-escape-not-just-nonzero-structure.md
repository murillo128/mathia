# MI-007 — Weak disappearance can be packet drift; uniform Sobolev control rules out a different escape

**Evidence level:** supported; the two mechanisms below are distinguished, not asserted equivalent.

For fixed `N` and `q` in the invertible residue class `r`, choose `1<=a<N` with `ar=1 mod N` and put `k_q=(aq-1)/N`. The original refined coordinate is exactly

\[
Z_q=R_1\otimes S_q^{-k_q},\qquad k_q/q\to a/N.
\]

A fixed degree not divisible by `N` therefore moves a localized packet by order `q` and is weakly invisible in the old packet window. Its norm has not been lost. But following the moving window gives `V_q^(d k_q+h) Z_q^d=U_q^(ad)V_q^h`, back in the already-classified CRT quotient algebra; retaining all `N` residue windows yields an ordinary bilateral-shift model, not a new coordinate ([PC-239](../../prime_circle/findings/PC-239-original-coordinate-bezout-winding-is-ballistic-and-collapses-to-shift-calculus.md)).

For the flute's fixed physical high-pass spaces `V_n`, [PF-292](../../prime_flute/findings/PF-292-fixed-physical-high-pass-forces-diverging-local-frequency-floor.md) instead provides `R_n -> infinity`, `epsilon_n -> 0` with

\[
\|P_{V_n}g_n\|_2\le\varepsilon_n\|g_n\|_2+R_n^{-\sigma}\|K_D^\sigma g_n\|_2.
\]

Uniform positive-Sobolev control forces the high projection to vanish. [PF-296](../../prime_flute/findings/PF-296-weighted-source-row-moment-controls-canonical-fixed-axis-superpositions.md) supplies that control for the canonical source synthesis when `sum_i q_i|a_(n,i)|` is uniformly bounded and `q_i asymp kappa_i`. Persistent normalized mixed-response witnesses therefore require an unbounded weighted source moment along a subsequence or a residual map outside the controlled factorization; growing row count alone is insufficient.

In the first construction the specified recentering locates the escaped mass and classicalizes it. In the second, the norm inequality excludes escape for an explicitly bounded family. A weak limit alone supplies neither conclusion. The flute estimate has no rate for `R_n` and does not establish the missing factorization of the complete physical response.
