# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem remains whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Decide the terminal visible correlation entropy of the radial certificate

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`, `MI-005-persistent-forward-memory-leakage-is-a-target-near-kernel-phenomenon`, `MI-006-boundary-zeros-force-reciprocal-depth-screening`, `MI-007-aliased-radial-prediction-has-a-positive-szego-floor`.

NB-066--NB-084 reduce persistent continuation to finite-future prediction and identify an exact actual-source Toeplitz certificate along every integer-dilation descendant ray. NB-085 settles the infinite-depth radial limit: the actual periodized density has `log W_(j,q) in L^1`, giving a strictly positive Szegő floor `G_(j,q)` and reducing qualitative success to boundedness of the aggregate floor charge `S_(R,q)`.

NB-086 now lower-bounds that infinite-depth charge by a completely visible finite-window quantity. On the terminal fraction `j>=ceil(R/q)`, the radial future starts beyond the current cutoff while the unrestricted causal predictor still sees the intermediate innovations. If `R_(R,q)` is the normalized Gram matrix of those terminal visible innovations, then

`S_(R,q) >= -log det R_(R,q) >= 0`.

Moreover bounded charge forces the sum of squared off-diagonal terminal correlations to remain `O(1)`. Therefore divergence of the normalized terminal visible pair-correlation energy is already enough to rule out every fixed-`q` radial certificate, without estimating the individual aliased Szegő floors.

The live theorem is now to estimate this terminal correlation entropy for the actual Nyman source. If it diverges, the next mechanism must be cross-ray or otherwise nonradial. If it stays bounded, that necessary condition removes one obstruction but does not by itself prove the full floor charge bounded; the remaining nonterminal contribution must still be controlled.

## Keep stationary inverse singularities, aliasing, prediction floor, visible correlation entropy and future geometry separate

NB-083 remains the matched control for a genuine unit-circle zero of a stationary symbol. NB-084 replaces that symbol by the arithmetic alias-periodized density; NB-085 gives its positive geometric-mean floor; NB-086 exposes an independent finite-window correlation-volume bill on the terminal block.

A positive ray floor is not the same as a good certificate, and a bounded terminal determinant deficit is only necessary, not sufficient, for bounded aggregate charge. Conversely, a bad single-ray charge is a failure of one restricted future geometry, not evidence for a nonzero stable tail, because the full nonstationary future can exploit cross-ray cancellation.