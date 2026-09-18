# MI-054 — Signed Plancherel sectors make the reciprocal-order left tail genuinely nonuniform

**Evidence level:** exact synthesis from [AF-413](../../findings/AF-413-left-tail-leading-margin-has-reciprocal-order-scale.md), [AF-414](../../findings/AF-414-fixed-excess-left-tail-sectors-have-signed-plancherel-limit.md), and [AF-415](../../findings/AF-415-exceptional-1-double-block-tail-resums-to-positive-cauchy-exponential.md). The hook-content, hook-length, Plancherel and Schur-Cauchy identities are classical; the Mathia content is their exact appearance and uniform resummation in the Euler-log derivative-Hankel diagonal.

AF-413 found the reciprocal-order left-tail scale by examining the root-normalized leading Cauchy--Binet coefficient: for `m=n+3`, the first nontrivial joint regime is `x=e^t=c/n`. AF-414 shows that this scale cannot be treated by substituting `x=c/n` into a fixed-order leading-term asymptotic. Competing exponent families survive at order one on exactly that diagonal.

Inside the double-rank-two sector, exponent sets containing the exceptional exponent `1` are naturally indexed by partitions `lambda`. If `d=|lambda|`, their exact ratio to the leading set satisfies

`T_(n,lambda)(c/n)/T_(n,empty)(c/n) -> (-1)^d (c^2/(4 pi^2))^d/H_lambda^2`.

Thus each fixed excess degree carries a signed Plancherel distribution over partitions, and summing all partitions of fixed size `d` gives `(-1)^d/d! * (c^2/(4 pi^2))^d`. The unique first correction is therefore negative and order one, so the leading monomial is not a relative-error asymptotic on this diagonal.

AF-415 supplies the missing uniform step for this entire exceptional-`1` double-block partition ensemble. Writing `a=c^2/(4pi^2)`, the normalized full sector converges locally uniformly to `exp(-a)>0`. Equivalently, the fixed-degree Plancherel coefficients really do resum to the positive Cauchy exponential once the moving partition tail is controlled. The alternating internal competition is genuine, but it is **not itself a sign obstruction after exact resummation**.

The conceptual shift is therefore sharper than “uniform sector summation is needed.” One complete nonperturbative sector has now been summed and repaired its apparent fixed-degree sign competition. Any diagonal sign failure must come from exponent families omitting `1`, determinant sectors using fewer than two entries from the logarithmic singular block, or their interaction with the positive resummed sector. A negative low-degree coefficient should not be promoted to a determinant obstruction until the full same-scale ensemble has been summed.

**Boundary.** AF-415 controls the exceptional-`1` double-rank-two sector only. It does not control exponent sets omitting `1`, one- or zero-singular-block sectors, or the full diagonal determinant, and it gives no conclusion about the zeta divisor or RH. The reciprocal-order scale remains the first nonuniform all-order regime; what changed is that one previously open moving partition tail is now exactly positive after resummation.
