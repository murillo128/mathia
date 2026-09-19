# MI-071 — Exceptional sets must be measured on the source-difference frame, not only in the ambient modulus space

**Evidence level:** exact synthesis from [MC-385](../../findings/MC-385-fixed-power-exceptional-moduli-cannot-feed-rank-linear-source-frame.md), interpreted against the endpoint source-frame bounds of MC-374 and MC-381 and the analytic ceilings MC-382--MC-384.

The endpoint frame does not require uniform cancellation for every source character. Let `W` be a surviving endpoint-mode subspace, `H=|W|`, and let `G` be the Gram matrix of its normalized source rows. Exact endpoint constancy puts all rows in an `R`-dimensional space, so

`lambda_max(G) >= H/R`.

Because source rows are indexed by the additive group `W`, pair correlations depend on the difference mode `I+J`. If only `E` nonzero difference modes are exceptional and all others have correlation at most `epsilon`, every row has exactly `E` exceptional neighbors. The row-sum bound gives

`lambda_max(G) <= 1+E+H epsilon`.

Hence the frame contradiction survives whenever

`E=o(H/R)` and `epsilon=o(1/R)`.

This is substantially weaker than uniform character control: an exponentially large endpoint family can tolerate many bad modes. The important quantity is not the ambient exceptional population but the **degree induced by those exceptions on the source-difference Cayley frame**.

MC-385 shows why standard fixed-power exceptional-modulus counts still miss this target. Under a trial source bound `P<=y^A`, the fixed-power source cutoff leaves `H>=2^(R-A/beta)`. An ambient theorem with at most `P^theta` exceptional conductors, for any fixed `theta>0`, certifies `E=o(H/R)` only while `A=O(R/log y)`. Even perfect cancellation outside the exceptional set does not change that bookkeeping. The ambient count simply does not say whether the thin structured source-conductor image concentrates inside the exceptional set.

The reusable lesson is that **almost-all information must be pulled back through the exact source map before it is priced**. A small exceptional fraction in a huge ambient conductor interval can still cover all source points relevant to the destination, while a much larger ambient exceptional set can be harmless if it has low degree on the source frame. The theorem surface that matters is source-conditioned incidence, not ambient cardinality by itself.

**Boundary.** This is a certificate obstruction, not a claim that the actual exceptional set meets the source family heavily. A source-adapted theorem could prove sparse intersection despite the same ambient count, or signed/operator cancellation could make a larger bad set harmless. The result does not improve the source-cost lower bound and implies no estimate for `M(x)` or RH.
