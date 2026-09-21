# MI-078 — Unbounded additive factor data buys state capacity only through retained precision

**Evidence level:** exact combinatorial synthesis from [MC-427](../../findings/MC-427-coarse-log-factor-summaries-have-subpolynomial-state-volume.md), extending the bounded-additive collapse MC-425--MC-426. This is a source-state capacity obstruction, not a cancellation theorem.

For a squarefree `n` with `r=omega(n)`, let each factor retain fixed-dimensional nonnegative additive statistics, quantized with meshes `eta_l`. If the total quantized mass in coordinate `l` is `L_l`, then across every ordered active factorization and every depth,

`N(n) <= r prod_l binom(L_l+r,r)`.

Thus unbounded prime weights are not by themselves an escape from the earlier bounded-summary obstruction. For fixed dimension, whenever each `L_l` is at most `(log X/log log X)(log X)^(o(1))`, the total retained state volume is still `X^(o(1))` uniformly for squarefree `n<=X`.

The canonical example is factor log-size. With `w(p)=log p` and `Q_eta(u)=floor(log u/eta)`, the total mass is only `log n<=log X`. Every mesh with `eta^(-1)=(log X)^(o(1))` therefore remains subpolynomial. Conversely, if this scalar size channel alone is claimed to supply at least `X^delta` states, the counting bound forces

`eta^(-1) >= (log X)^(delta-o(1))`.

So **a polynomial factor-state exponent has to be paid for by polynomial-in-`log X` precision, not merely by attaching an unbounded additive quantity**. Exact `log u` lies beyond this coarse regime because it determines `u`; the distinction is retained precision, not just range.

**Boundary.** The argument uses nonnegative additive weights, fixed retained dimension and explicit quantization. Signed weights require variation control, growing dimension can evade the count, and passing the state-capacity threshold is only necessary: it does not show that the extra bits survive shell/closure operations or drive Möbius cancellation.