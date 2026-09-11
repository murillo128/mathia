# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the useful rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem remains whether the canonical arithmetic coefficients can force a near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Control the target-selected repair geometry without rebuilding the Nyman oracle

**Linked intuitions:** `MI-001-coefficient-geometry-needs-target-coupling`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`.

NB-024--NB-039 build a weighted moving-tail quotient that preserves source coordinates, has polynomial conditioning independent of the discarded upper section, and has a sharp target-loss floor `Theta(1/M)`. Its upper-section correction carries a multiplicatively accurate copy of the original distance in an explicit Möbius/Vasyunin direction. Representation compression, target preservation, and oracle cost are therefore separate gates.

NB-040 shows that the target-loss floor is not dimensional. One additional retained direction gives an exactly zero-loss, still polynomially conditioned skeleton, but that unique direction is precisely the weighted-tail target projection `P_W e`. Exact repair therefore isolates rather than removes the target oracle.

NB-041 gives a nontrivial source reduction for the associated logarithmic tail scalar. An explicit Möbius dual `Omega_M`, independent of the upper section, predicts that scalar with stability norm `O(1/log M)`. NB-042 then identifies the sharp endpoint of this norm route: near-square-root decay `||Omega_M||=O_epsilon(M^(-1/2+epsilon))` for every `epsilon>0` is **equivalent to RH**. Pushing the ambient dual all the way to its geometric support floor is therefore not a cheap explicit-estimate improvement.

The live theorem is narrower. Obtain the projected repair geometry, the explicit Burnol-scale directional correction, or a one-sided target certificate at the required accuracy **without** proving an RH-equivalent norm estimate or solving an `N`-scale projection problem. Directional correlation may still be cheaper than ambient norm control; alternatively a materially different quotient could change the target-loss/oracle boundary for a structural reason.

## Treat compression, exact repair, scalar source access, and critical norm decay as separate gates

The weighted skeleton is a good source representation but loses `Theta(1/M)` target energy. A rank-one target-selected repair removes that loss exactly. Its scalar coefficient has a source-defined shrinking dual, yet driving that dual to near-square-root norm decay is already RH-equivalent and still does not by itself give the required uniform Burnol-scale accuracy for every merely superlogarithmic cutoff. Future claims should price these four facts separately rather than infer cheap target access from low dimension or a shrinking scalar error.