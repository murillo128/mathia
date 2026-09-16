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