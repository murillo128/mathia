---
id: CLUE-left-tail-diagonal-order-drift-scale
type: research-clue
status: accepted
origin: research-watch
target_line: arithmetic_fidelity
based_on:
  - research/arithmetic_fidelity/findings/AF-412-every-fixed-euler-confluent-order-is-positive-in-the-left-tail.md
  - research/arithmetic_fidelity/findings/AF-413-left-tail-leading-margin-has-reciprocal-order-scale.md
---

# Does the Euler left-tail confluent hierarchy have a uniform `x ~ c/m` double-scaling law?

## Observation

AF-412 proves that every fixed Euler-log confluent order is eventually positive in the left tail, but explicitly leaves the threshold nonuniform in the order. AF-413 now simplifies the exact AF-412 leading coefficient. With `n=m-3`, `x=e^t`, and `S_n=n^2+n+1`, the fixed-order leading term is

\[
K_{n+1}x^{S_n},
\]

and

\[
K_{n+1}^{1/S_n}\sim\frac{n}{\pi e^{3/2}}.
\]

Therefore the root-normalized leading monomial has the first nontrivial joint balance when `nx` stays of order one. In particular, along the formal scaling `x=c/n`, its `S_n`-th root tends to `c/(\pi e^{3/2})`.

This does not make the AF-412 asymptotic uniform. Higher Cauchy--Binet terms are suppressed by extra powers of `x` for each fixed `n`, but their coefficients also depend on `n` and may become comparable on precisely this diagonal.

## Research question

For the exact full Euler-log profile, does the derivative-Hankel determinant admit a uniform large-order/small-`x` asymptotic when

\[
n=m-3\to\infty,
\qquad
x=e^t=\frac{c}{n}
\]

with `c` in a fixed compact subset of `(0,\infty)`?

More sharply, after normalizing by the AF-412 leading term, does

\[
\frac{H_{n+3}(\log(c/n))}{K_{n+1}(c/n)^{S_n}}
\]

converge to a positive limit, remain uniformly positive, or instead acquire a competing contribution that changes sign or order of magnitude?

## Why it may matter

AF-411 and AF-412 force any tail obstruction to total positivity into growing determinant order. AF-413 identifies the first quantitative corridor in which that order drift can interact with the shrinking left-tail coordinate. If the AF-412 leading term remains uniformly dominant there, one concrete escape route for the all-order obstruction is eliminated. If it does not, the first competing exponent family would expose the actual mechanism that fixed-order asymptotics hide.

This also turns the line's general fidelity question into a precise asymptotic one: the compressed certificate is faithful at each bounded complexity, but the complexity budget itself grows while the observation scale collapses.

## Decisive test

Return to the exact rank-two plus analytic-germ decomposition used in AF-412 and organize the **full** determinant expansion by Cauchy--Binet exponent sets, not only the smallest set `Lambda_{n+1}`. In the regime `x=c/n`:

1. obtain uniform asymptotics or rigorous bounds for the ratio of every relevant next exponent family to the leading `Lambda_{n+1}` contribution;
2. control terms using fewer entries from the rank-two singular block, including the polynomial `u=-log x` factors, on the same scale;
3. prove uniform dominance of the positive leading term for `c` in a nontrivial interval, or exhibit a rigorously comparable/opposite-sign family.

Known double-scaling Hankel-determinant methods may provide useful asymptotic language, but a theorem for a different varying moment weight is not a transfer without an explicit dictionary to this derivative-Hankel Euler-log matrix.

A fixed-`m` asymptotic, a finite scan over determinant orders, or merely evaluating the AF-413 leading monomial at `x=c/n` does not decide the question.

## Evidence boundary

AF-413 proves only the exact coefficient and its large-order asymptotic. It does not establish a uniform remainder, a diagonal sign theorem, a sharp threshold in `c`, or any all-order total-positivity statement. The proposed `x~1/m` regime is a mathematically forced balance scale for the leading coefficient, not yet an observed or proved transition of the full determinant. No arithmetic-prime discriminator or RH consequence is established.

## Research disposition

Accepted. AF-414 first proved that `x=c/n` is a genuine nonuniformity scale inside the double-rank-two Cauchy--Binet sector: every fixed excess degree survives with a signed Plancherel profile and the degree-one correction has opposite sign. AF-415 now closes the previously open partition-tail interchange for the complete subfamily whose exponent set contains the exceptional exponent `1`: after normalization by the AF-412 leading term, that entire subfamily converges locally uniformly to the positive factor `exp(-c^2/(4 pi^2))`.

The clue remains unresolved because its decisive test concerns the **full** determinant. The load-bearing open terms are now narrower: exponent sets that omit `1`, and determinant sectors using only one or zero entries from the rank-two singular block, must still be controlled on the same `x=c/n` diagonal before a uniform full-determinant asymptotic or sign statement is justified.
