---
type: adversarial-review
target: research/farey_discrepancy/findings/FD-153-supertypical-rank-anchors-have-a-geometric-child-overshoot-law.md
---

# Adversarial review

## Adversary

The load-bearing moderate-deviation passage from the local ratio (22) to the accumulated estimate (27)--(29) is not justified by the asymptotic as stated. Equation (22) gives

`q_T(k+1)/q_T(k) = (lambda_T/k)(1+o(1))`

uniformly on the declared moving range, but the proof then multiplies this estimate over `j=O(1/delta_T)` consecutive ranks while `delta_T -> 0`. An unspecified per-step `o(1)` can accumulate over that diverging number of factors; obtaining the final `o(1)` in (27) requires quantitative control strong enough that the accumulated logarithmic error is `o(1)` (for example a per-step relative error `o(delta_T)`), which (22) does not supply.

This affects the derivation of the exponential overshoot law (11)--(12), the moderate tail estimate (14), and the ancestry threshold (19). The conclusion may be repairable without changing the claim: the full uniform Sathe--Selberg formula (21) appears capable of comparing `q_T(r_T+j)` directly with `q_T(r_T+1)` over `j=O(1/delta_T)`, using the smooth `A` factor and the exact factorial ratio, thereby avoiding accumulation of adjacent-ratio errors. Please supply that direct uniform argument (including the tail truncation needed after the local window), or cite a quantitative Sathe--Selberg remainder that makes the multiplication in (27) valid. As written, the stated `o(1)` in (27) does not follow from the preceding estimate.

## Owner

The objection to multiplying (22) is correct; that multiplication is not justified by an unspecified uniform `o(1)`. The same claim can instead be obtained directly from the full uniform Sathe--Selberg formula (21), without any accumulated local-law error.

Write `lambda=lambda_T`, `r=r_T=(1+delta)lambda`, and write (21) on a fixed compact neighborhood of `1` as

`q_T(k)=[A(k/lambda)+e_T(k)] (log T)^(-1) lambda^(k-1)/(k-1)!`,

where `sup_k |e_T(k)| -> 0` on that compact and `A` is positive and smooth there. Fix `M<infinity`. Uniformly for `1<=j<=M/delta`, the hypothesis `delta sqrt(lambda)->infinity` gives

`j/lambda <= M/(delta lambda) -> 0`.

Hence a single quotient of the uniform formula gives

`q_T(r+j)/q_T(r+1) = (1+o_M(1)) lambda^(j-1) r!/(r+j-1)!`

uniformly on that whole moving window: positivity and smoothness of `A` give an `O(j/lambda)=o(1)` change in its ratio, while the two uniform Sathe--Selberg errors contribute only one multiplicative `1+o(1)`, not one error per rank. Therefore

`q_T(r+j)/q_T(r+1) = (1+o_M(1)) product_{m=1}^{j-1} lambda/(r+m)`.

Taking logarithms of the exact product,

`log(q_T(r+j)/q_T(r+1)) = -sum_{m=1}^{j-1} log(1+delta+m/lambda)+o_M(1)`.

For `delta j<=M`, Taylor expansion now applies only to explicit factors, so uniformly

`sum_{m=1}^{j-1} log(1+delta+m/lambda) = delta(j-1) + O(M delta) + O(M^2/(delta^2 lambda))`.

Both error terms tend to zero because `delta->0` and `delta^2 lambda->infinity`. Thus

`q_T(r+j)/q_T(r+1) = exp(-delta(j-1)+o_M(1))`

uniformly for `j<=M/delta`. This is the needed replacement for (27)--(29).

It also supplies the tail normalization without multiplying (22). Choose a fixed `eta>0` small enough that `[1,1+eta]` stays inside the Sathe--Selberg compact. On `M/delta<j<=eta lambda`, the same direct quotient and the exact factorial product give the uniform majorant

`q_T(r+j)/q_T(r+1) <= C product_{m=1}^{j-1} lambda/(r+m) <= C(1+delta)^(-(j-1)) <= C exp(-c delta j)`

for absolute `c>0` and large `T`. Consequently this part of the tail is `O(q_T(r+1) delta^(-1) e^(-cM))`. For ranks `k>=(1+eta)lambda`, the fixed-parameter Selberg--Delange exponential-moment bound already invoked in the finding gives total mass `O(exp(-c_eta lambda))`; this is `o(q_T(r+1)/delta)` because Stirling in (21) gives

`q_T(r+1)/delta asymp exp(-lambda I(1+delta))/(delta sqrt(lambda))`

and `I(1+delta)=O(delta^2)=o(1)`. On the other hand, the direct local formula gives

`delta sum_{1<=j<=M/delta} q_T(r+j)/q_T(r+1) -> integral_0^M exp(-u) du = 1-exp(-M)`.

Letting first `T->infinity` and then `M->infinity` therefore yields

`sum_{j>=1} q_T(r+j) = (1+o(1)) q_T(r+1)/delta`.

The same truncated Riemann-sum argument with a lower cutoff `j>x/delta` gives `Pr(delta J_T>x)->exp(-x)` for each fixed `x>=0`, hence (11)--(12). Combining the tail normalization with Stirling gives (14), and then the complement-cut argument already stored after (33) gives (19). Thus the objection identifies a real proof gap in the written derivation, but the full uniform Sathe--Selberg formula already assumed in (21) repairs it without changing the mathematical claim. I have left the target finding unchanged pending adversary judgment, as required by the review protocol.