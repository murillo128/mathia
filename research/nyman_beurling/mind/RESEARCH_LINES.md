# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem remains whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Show that future innovations cancel essentially all raw continuation volume

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`, `MI-005-persistent-forward-memory-leakage-is-a-target-near-kernel-phenomenon`.

NB-066--NB-071 reduce a persistent late quotient to a global continuation mode and show that exact branching, the full finite-window local flag, zero one-cell memory, and uniformly good global Gram conditioning do not determine whether a stable tail survives. NB-072--NB-073 classify the stationary matched-control mechanism through prediction versus feedthrough.

NB-074 supplies the actual nonstationary finite-window charge

`J_(R,N)=log det(A_R^(-1/2) S_(R,N) A_R^(-1/2))`.

Every nonzero stable tail forces this charge to diverge for every finite horizon schedule, while bounded charge on an unbounded sequence rules the tail out.

NB-075 now replaces the opaque determinant target by an exact scalar cancellation budget. With raw continuation volume

`L_R=log(det H_(<R)/det A_R)`

and residualized future partial correlations `beta_(R,n)`, one has

`J_(R,N)=L_R-sum_(n=R)^N[-log(1-beta_(R,n))]`.

The future terms are nonnegative and count only genuinely new predictive overlap after earlier future directions have been removed. The live arithmetic theorem is therefore to prove, along some unbounded `R_k` and finite schedule `N_k`,

`sum_(n=R_k)^N_k[-log(1-beta_(R_k,n))] >= L_(R_k)-O(1)`.

It is sufficient to prove the stronger `sum beta_(R_k,n)>=L_(R_k)-O(1)`. Raw continuation volume may diverge harmlessly if later innovations cancel it to bounded remainder.

## Treat local memory, raw volume, conditional predictability and uncancelled continuation separately

NB-074 subtracts forward memory already visible in the current window; NB-075 subtracts, sequentially, the part of the remaining raw continuation volume explained by each genuinely new future innovation. Large raw tails, large pairwise correlations, poor conditioning, or even large `L_R` are not stable-tail evidence by themselves. The surviving obstruction is the future-conditioned volume that no later innovation explains.