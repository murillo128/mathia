# MI-043 — Finite scalar Wang dilation banks have a Vandermonde cancellation ceiling

**Evidence level:** exact transform synthesis from [VIS-341](../../findings/VIS-341-fixed-polynomial-smoothing-preserves-korobov-vinogradov-power.md), [VIS-342](../../findings/VIS-342-variable-scalar-smoothing-needs-polynomial-order-for-fixed-power-gain.md), and [VIS-343](../../findings/VIS-343-wang-dilate-mixture-cancellation-order.md). This concerns frequency-independent scalar combinations of finitely many distinct pure dilates of the Wang multiplier; translations, source-dependent/frequency-dependent coefficients and nonlinear constructions are outside the theorem.

The Wang multiplier is `m(xi)=4(1+i xi)/(4+xi^2)`. For distinct positive dilations `a_1,...,a_N`, a scalar bank `M(xi)=sum_j c_j m(a_j xi)` can improve its high-frequency tail only by cancelling successive inverse-power moments `sum_j c_j a_j^(-k)`.

These conditions form a Vandermonde system. A nonzero `N`-dilate bank can cancel at most `N-1` leading tail terms, so its decay order is at most `N`; that ceiling is sharp. The apparent freedom of choosing dilation scales does not create more scalar smoothing order than the number of independent coefficients.

Combining this with VIS-342 converts order into source complexity. Inside the same scalar envelope model, a fixed power-class improvement by `delta>0` requires effective order `r(u)=u^(5 delta/2+o(1))`. Therefore any pure-dilation scalar bank achieving that mechanism must have

`N(u) >= u^(5 delta/2+o(1))`.

Finite, logarithmic, polylogarithmic or more generally subpolynomial dilation banks cannot change the `3/5` Korobov--Vinogradov power class by scalar tail-order cancellation alone. “Many scales” becomes a quantitative polynomial complexity requirement rather than an informal source of extra cancellation.

**Boundary.** This does not exclude translations, frequency-dependent weights, signed arithmetic coefficients tied to the source, nonlinear interactions, or a mechanism that improves the theta remainder without scalarizing to tail-order cancellation. Any such proposal must identify the exact estimate that escapes the Vandermonde reduction and still survive the downstream derivative ledger.