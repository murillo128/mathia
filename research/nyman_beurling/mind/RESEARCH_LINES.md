# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem remains whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Decide the radial Szegő floor charge, then go cross-ray if it diverges

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`, `MI-005-persistent-forward-memory-leakage-is-a-target-near-kernel-phenomenon`, `MI-006-boundary-zeros-force-reciprocal-depth-screening`, `MI-007-aliased-radial-prediction-has-a-positive-szego-floor`.

NB-066--NB-084 reduce persistent continuation to finite-future prediction and identify an exact actual-source Toeplitz certificate along every integer-dilation descendant ray. The relevant periodized density `W_(j,q)` is positive almost everywhere, so ordinary critical-line zeros do not reproduce the stationary unit-circle-zero mechanism of NB-083.

NB-085 now settles the infinite-depth radial limit. For every `j,q`, the actual density satisfies `log W_(j,q) in L^1`, so Szegő--Kolmogorov gives a strictly positive floor `G_(j,q)` and `E_(j,q,L) -> G_(j,q)`. The qualitative radial problem therefore no longer depends on how fast finite depth approaches the floor. Define the aggregate floor charge `S_(R,q)=sum_(j<R) log(G_(j,q)/PiHat_(j,R)^2)`. Boundedness of this charge on an unbounded sequence is exactly enough to choose finite depths that exclude a stable tail; divergence means that no amount of depth on that single ray can produce a bounded radial certificate.

The live theorem is thus to estimate `S_(R,q)` from the actual periodized spectra. If it stays bounded, qualitative stable-tail exclusion follows without a prescribed depth rate. If it diverges, the next mechanism must be genuinely cross-ray or otherwise nonradial. Finite-depth convergence rates matter only for stronger quantitative horizon constraints.

## Keep stationary inverse singularities, aliasing, prediction floor, convergence rate and future geometry separate

NB-083 remains the matched control for a genuine unit-circle zero of a stationary symbol. NB-084 replaces that symbol by the arithmetic alias-periodized density; NB-085 further shows that this density has a positive geometric-mean floor.

A positive floor is not the same as a good certificate: what matters is its ratio to the visible causal prediction error after summing over innovations. Conversely, a bad radial floor is only a failure of one restricted future geometry, not evidence for a nonzero stable tail, because the full nonstationary future can exploit cross-ray cancellation.