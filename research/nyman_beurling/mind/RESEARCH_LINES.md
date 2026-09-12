# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem remains whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Bound the renormalized nonstationary prediction-volume charge on an unbounded sequence of windows

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`, `MI-005-persistent-forward-memory-leakage-is-a-target-near-kernel-phenomenon`.

NB-066--NB-071 reduce a persistent late quotient to a global continuation mode and show that exact branching, the full finite-window local flag, zero one-cell memory, and even uniformly good global Gram conditioning do not determine whether a stable tail survives.

NB-072--NB-073 classify the stationary matched-control mechanism. Inner--outer factorization separates stable-tail geometry from conditioning, and the missing inner datum is recovered by comparing global future-prediction energy with causal first-cell feedthrough.

NB-074 supplies the actual nonstationary finite-window replacement. For the visible Gram `A_R` and future Schur complement `S_(R,N)`, the scalar charge

`J_(R,N)=log det(A_R^(-1/2) S_(R,N) A_R^(-1/2))`

is nonnegative and dominates the previous generalized-eigenvalue obstruction. Every nonzero stable-tail vector forces `J_(R,N(R))->infinity` for every finite horizon schedule `N(R)>=R`; conversely, bounded charge along any unbounded sequence of windows rules out the stable tail.

The charge has an exact causal meaning:

`J_(R,N)=sum_(j<R) log(Pi_(j,N)^2/PiHat_(j,R)^2)`.

Each summand is nonnegative. `PiHat` removes prediction error already explained by forward memory visible inside the current window, so the charge isolates genuinely unseen continuation rather than conflating it with the raw feedthrough gap. On stationary Wold rays it reduces exactly to the NB-073 inner charge.

The live theorem is now a concrete arithmetic determinant/prediction estimate: find a legitimate finite horizon schedule and prove `J_(R,N(R))` bounded on an unbounded sequence, or obtain a comparably strong source estimate for the same renormalized quantity. Even the one-step determinant ratio `J_(R,R)` is already a finite source-only sufficient test if it can be bounded.

## Treat local memory, branching covariance, inner-factor defect, global Gram conditioning, visible prediction memory, unseen prediction-volume charge, causal feedthrough, continuation cost, and finite certification separately

NB-074 corrects the direct stationary analogy: a large global-prediction/feedthrough ratio may be entirely explained by memory already visible before the cutoff. The load-bearing quantity subtracts that visible memory. Future progress should bound the renormalized continuation charge rather than strengthen generic locality, Riesz bounds, or the raw Gram alone.