# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem remains whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Compare actual causal innovation energy with future-prediction energy in the nonstationary Nyman system

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`, `MI-005-persistent-forward-memory-leakage-is-a-target-near-kernel-phenomenon`.

NB-066--NB-071 reduce a persistent late quotient to a global continuation mode and show that exact branching, the full finite-window local flag, zero one-cell memory, and even uniformly good global Gram conditioning do not determine whether a stable tail survives.

NB-072 classifies the matched-control mechanism exactly. For every stationary scalar branch filter `D_j=psi(V_m)e_j`, inner--outer factorization `psi=theta g` gives

`stable tail ~= K_theta tensor ker(V_m*)`,

so the stable tail vanishes exactly when `psi` is outer. The outer factor controls synthesis/conditioning; the inner factor alone controls the surviving orthogonal defect.

NB-073 identifies the scalar datum that the global Gram was missing. The one-step future-prediction energy

`Pi(psi)^2 = inf ||psi(V_m)(w+x_future)||^2`

is determined by the full Gram and equals `|g(0)|^2`, while the actual causal first-cell feedthrough is `c(psi)^2=|psi(0)|^2`. Their ratio is

`c(psi)^2/Pi(psi)^2 = |theta(0)|^2`,

and the stationary stable tail vanishes exactly when `c(psi)^2=Pi(psi)^2`. Thus the inner defect is not merely “invisible to Gram geometry”: it is exactly the **prediction/feedthrough gap** left after comparing global future energy with one time-oriented causal datum.

This also separates the inner transition from ordinary conditioning. At the outer but noninvertible boundary `psi=1-z`, the Gram lower bound degenerates while the prediction/feedthrough gap is zero; nonconstant Blaschke or singular inner factors give a strict gap even when the outer factor is well conditioned.

The live theorem is now more concrete than a generic outerness statement. For the actual shrinking-cell Nyman innovations, construct from the descendant/future Gram geometry a canonical nonstationary prediction energy `Pi_R^2` and compare it with the genuine newest-cell innovation energy `||C_R||^2`. Prove an asymptotic equality such as `Pi_R^2/||C_R||^2 -> 1`, or an appropriate uniform analogue, from the arithmetic Mellin/Paley--Wiener structure. In the complete stationary matched-control class this equality is exactly the no-inner-factor condition; a persistent gap would instead identify the surviving continuation defect directly.

## Treat local memory, branching covariance, inner-factor defect, global Gram conditioning, future-prediction energy, causal feedthrough, continuation cost, and finite certification separately

NB-072 separates outer conditioning from inner stable-tail geometry; NB-073 shows that the lost inner information is restored by comparing Gram-predicted future error with the causal diagonal. Future progress should seek this prediction/feedthrough comparison in the actual nonstationary arithmetic source rather than strengthening generic locality, Riesz bounds, or the global Gram alone.