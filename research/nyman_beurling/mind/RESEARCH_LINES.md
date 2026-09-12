# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem remains whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Recover raw continuation volume from a finite band of interval partial correlations

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`, `MI-005-persistent-forward-memory-leakage-is-a-target-near-kernel-phenomenon`.

NB-066--NB-073 reduce a persistent late quotient to a global continuation mode and show that exact branching, the full finite-window local flag, zero one-cell memory, ordinary global conditioning, and stationary matched controls do not determine whether a stable tail survives.

NB-074 introduces the nonstationary continuation charge `J_(R,N)`. NB-075 resolves it into raw continuation volume `L_R` minus future-conditioned multiple-correlation charges. NB-076 now resolves each of those charges again. If `rho_(j,n)` is the endpoint partial correlation of `D_j` and `D_n` after conditioning only on the intervening innovations `D_(j+1),...,D_(n-1)`, and `kappa_(j,n)=-log(1-|rho_(j,n)|^2)`, then

`J_(R,N)=L_R-sum_(j<R<=n<=N) kappa_(j,n)`.

Every `kappa_(j,n)` is nonnegative and equals a contiguous-Gram determinant cross-ratio, equivalently a mixed second difference of log Gram determinants. The future-cancellation budget is therefore an exact cross-cut area in an interval-partial-correlation lattice, not an opaque growing-dimensional regression.

A source-facing sufficient criterion is now local/mesoscopic: along unbounded `R_k`, it is enough to find finite bandwidths `H_k` for which the sum of `kappa_(j,j+h)` over intervals of length at most `H_k` crossing the cut recovers `L_(R_k)-O(1)`. The stronger sum of `|rho|^2` may be used because `-log(1-u)>=u`.

The live arithmetic theorem is consequently to control **contiguous finite Gram blocks near the cut** strongly enough to recover essentially all raw continuation volume. No theorem requiring inversion of the whole residualized prefix is needed if a finite band already carries the cancellation.

## Treat local memory, raw volume, interval-conditioned correlation and uncancelled continuation separately

NB-074 subtracts memory visible in the current window; NB-075 credits future directions sequentially; NB-076 decomposes each credit into interval-conditioned endpoint links counted exactly once. Large raw tails, raw pairwise correlations, poor conditioning, or even large `L_R` are not stable-tail evidence by themselves. The surviving obstruction is the cross-cut log-Gram curvature that the future fails to supply.
