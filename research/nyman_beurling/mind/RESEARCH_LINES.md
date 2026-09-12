# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem remains whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Exclude a branch-inner factor in the actual nonstationary Nyman innovation system

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`, `MI-005-persistent-forward-memory-leakage-is-a-target-near-kernel-phenomenon`.

NB-066--NB-071 reduce a persistent late quotient to a global continuation mode and show that exact branching, the full finite-window local flag, zero one-cell memory, and even uniformly good global Gram conditioning do not determine whether a stable tail survives.

NB-072 classifies the matched-control mechanism exactly. For every stationary scalar branch filter `D_j=psi(V_m)e_j`, inner--outer factorization `psi=theta g` gives

`stable tail ~= K_theta tensor ker(V_m*)`,

so the stable tail vanishes exactly when `psi` is outer. The outer factor controls synthesis/conditioning; the inner factor alone controls the surviving orthogonal defect. The NB-071 example `1-rho z`, `rho>1`, is precisely a one-Blaschke-factor defect.

This classification also explains why all finite causal trace data missed the obstruction: every filter with nonzero constant term has the same triangular finite-window span and the same exact integer branching, independently of its inner factor. The distinction is global analytic factorization, not another local-memory statistic or condition-number estimate.

The live theorem is now source-specific and narrower. The actual Nyman innovations are nonstationary because the cells shrink, so NB-072 does not itself provide a Wold variable in which the source has a scalar symbol. One must derive a legitimate branching-coordinate representation and prove its source is cyclic/outer, or extract from the exact Mellin/Paley--Wiener Gram structure a no-inner-factor statement that excludes the same model-space defect without assuming stationarity. Burnol's half-plane outer multiplier is suggestive but is not automatically the coefficient-side branch outer factor.

## Treat local memory, branching covariance, inner-factor defect, global Gram conditioning, causal continuation cost, and finite certification separately

NB-072 makes the separation exact in the stationary control class. Good conditioning belongs to the outer factor; nonzero stable tail belongs to the inner factor. Future progress must connect the actual arithmetic source to this factorization boundary or prove a stronger nonstationary analogue, rather than strengthen generic locality or Riesz bounds.