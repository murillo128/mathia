# MI-054 — Signed Plancherel sectors make the reciprocal-order left tail genuinely nonuniform

**Evidence level:** exact synthesis from [AF-413](../../findings/AF-413-left-tail-leading-margin-has-reciprocal-order-scale.md), [AF-414](../../findings/AF-414-fixed-excess-left-tail-sectors-have-signed-plancherel-limit.md), [AF-415](../../findings/AF-415-exceptional-1-double-block-tail-resums-to-positive-cauchy-exponential.md), and [AF-416](../../findings/AF-416-full-left-tail-diagonal-has-positive-cauchy-limit.md). The hook-content, hook-length, Plancherel and Schur-Cauchy identities are classical; the Mathia content is their exact appearance and full fixed-shift resummation in the Euler-log derivative-Hankel diagonal.

AF-413 finds the reciprocal-order scale `x=e^t=c/n` for `m=n+3`. AF-414 shows why a fixed-order leading monomial cannot simply be evaluated on that diagonal: every fixed excess degree survives at order one, with partition `lambda` of size `d` contributing asymptotically

`(-1)^d (c^2/(4 pi^2))^d/H_lambda^2`.

Summing partitions of fixed size gives the alternating coefficient `(-1)^d/d! * (c^2/(4 pi^2))^d`. The first correction is therefore negative and order one. The diagonal is genuinely nonuniform at the level of individual Cauchy--Binet sectors.

AF-415 proves that the complete exceptional-`1` double-rank-two partition ensemble nevertheless resums locally uniformly to `exp(-c^2/(4pi^2))>0`. AF-416 closes the remaining loopholes by an exact singular-block decomposition plus uniform Schur bounds: exponent sets omitting `1`, the one-singular-block terms and the zero-singular-block term are negligible relative to the double-block baseline. Consequently the **full** normalized determinant satisfies

`H_(n+3)(log(c/n)) / (K_(n+1)(c/n)^(n^2+n+1)) -> exp(-c^2/(4 pi^2))`

locally uniformly for `c` in compact subsets of `(0,infinity)`.

The reusable lesson is narrower and stronger than the earlier warning about missing sectors: a same-scale negative perturbative coefficient can be real while the complete moving ensemble is positive. On the fixed derivative shifts occurring in the Euler determinant decomposition, the reciprocal-order corridor is now a resolved positive competition regime, not a candidate sign obstruction.

**Boundary.** AF-416 does not prove total positivity at all orders and does not control sequences for which `n e^t` leaves every compact subset of `(0,infinity)`. It also keeps the derivative offsets in the determinant decomposition fixed. AF-417 shows that letting derivative depth grow with `n` creates a second scaling coordinate and therefore lies outside this fixed-shift closure. No statement about the zeta zero divisor or RH follows from the Cauchy limit itself.