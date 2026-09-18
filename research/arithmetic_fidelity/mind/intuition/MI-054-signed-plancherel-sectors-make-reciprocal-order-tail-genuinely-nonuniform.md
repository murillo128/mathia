# MI-054 — Signed Plancherel sectors make the reciprocal-order left tail genuinely nonuniform

**Evidence level:** exact synthesis from [AF-413](../../findings/AF-413-left-tail-leading-margin-has-reciprocal-order-scale.md) and [AF-414](../../findings/AF-414-fixed-excess-left-tail-sectors-have-signed-plancherel-limit.md). The hook-content, hook-length and Plancherel identities are classical; the Mathia content is their exact appearance in the Euler-log derivative-Hankel diagonal.

AF-413 found the reciprocal-order left-tail scale by examining the root-normalized leading Cauchy--Binet coefficient: for `m=n+3`, the first nontrivial joint regime is `x=e^t=c/n`. AF-414 shows that this scale cannot be treated by substituting `x=c/n` into a fixed-order leading-term asymptotic. Competing exponent families survive at order one on exactly that diagonal.

Inside the double-rank-two sector, exponent sets containing the exceptional exponent `1` are naturally indexed by partitions `lambda`. If `d=|lambda|`, their exact ratio to the leading set satisfies

`T_(n,lambda)(c/n)/T_(n,empty)(c/n) -> (-1)^d (c^2/(4 pi^2))^d/H_lambda^2`.

Thus each fixed excess degree carries a signed Plancherel distribution over partitions. Summing all partitions of fixed size `d` gives

`(-1)^d/d! * (c^2/(4 pi^2))^d`.

In particular the unique first correction tends to `-c^2/(4 pi^2)`. The leading monomial therefore fails to be a relative-error asymptotic for every fixed `c>0` even before leaving its own Cauchy--Binet sector. The reciprocal-order scale is a real alternating competition regime, not merely the point where a normalized leading coefficient happens to become order one.

The fixed-degree coefficients formally match `exp(-c^2/(4 pi^2))`, but this resemblance is not yet a determinant asymptotic. AF-414 gives no uniform control as `d` grows with `n`, and it does not control exponent sets omitting `1` or sectors using fewer than two entries from the logarithmic singular block. Those omitted pieces are precisely where a sign change or a different diagonal scale could still enter.

The useful conceptual shift is from **leading-term scale diagnosis** to **uniform sector summation**. Once every fixed order is eventually positive in the left tail, the escaping obstruction can only live where determinant order and spatial scale move together; AF-414 now proves that on the first such diagonal the internal combinatorics itself becomes nonperturbative. Any all-order positivity argument must therefore control the whole moving partition ensemble and the remaining singular-block sectors, not improve another fixed-order remainder.

**Boundary.** The Plancherel law is exact only after taking `n->infinity` at fixed partition or fixed excess degree. No exchange with the infinite partition sum is proved, no full diagonal determinant limit or sign is known, and no conclusion about the zeta divisor or RH follows from the Euler-log total-positivity hierarchy alone.
