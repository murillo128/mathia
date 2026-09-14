# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem is whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Rule out harmonic-profile interpolation by high-zero power sums at inverse-height cost

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`, `MI-005-persistent-forward-memory-leakage-is-a-target-near-kernel-phenomenon`, `MI-006-boundary-zeros-force-reciprocal-depth-screening`, `MI-007-aliased-radial-prediction-has-a-positive-szego-floor`, `MI-008-finite-blaschke-defects-are-silent-in-terminal-scalar-energy`, `MI-009-summable-horizontal-zero-mass-keeps-full-terminal-gram-entropy-bounded`, `MI-010-growing-depth-mobius-annulus-exposes-off-critical-blaschke-amplification`, `MI-011-canonical-deflation-cancels-raw-cauchy-crowding-volume`, `MI-012-three-state-transverse-confluence-exposes-collective-shear`, `MI-013-absolute-height-and-global-zero-counts-are-invisible-to-the-collective-shear-obstruction`, `MI-014-quadratic-horizontal-tangency-is-the-three-state-conditioning-threshold`, `MI-015-confluent-volume-is-curvature-blind-and-controlled-by-radial-depth`, `MI-016-growing-confluent-rank-is-limited-by-endpoint-extrapolation-cost`, `MI-017-finite-high-zero-target-access-requires-a-target-bearing-compression-near-kernel`.

NB-115 localizes the only canonical finite-section escape: order-one finite target access from a target-poor packet must load cell-compression modes whose retained continuum energy is `O(tau(F)+1/R)`. NB-116 uses the horizontal Burnol weight plus Selberg density to sharpen the actual high-zero packet mass to `tau(F)=O(1/G)`, so the relevant retention scale is `O(1/G+1/R)` independently of packet rank and width.

NB-117 removes the remaining spectral-coordinate ambiguity. For every packet vector `f`, let

`P_f(n)=<f,e 1_[log n,infinity)>`.

Then exactly

`||Q_R f||^2 = sum_(n<R) n(n+1)|Delta P_f(n)|^2`

and

`<Q_R f,e_R> = P_f(1)-P_f(R)`.

Among sequences with those endpoint values, the unique minimum-energy profile is affine in `1/n`. Therefore fixed positive target access is equivalent to the packet primitive approximating `C+D/n` with bounded weighted first-difference excess. For a finite zero packet, that primitive is exactly a confluent zero-power sum

`sum_rho c_rho n^-conj(rho) (log n)^k`.

In the regime `R/G -> infinity`, an order-one target witness can be normalized to have `O(1)` discrete harmonic-profile energy while its continuum model-space norm is `Omega(G)`. The live theorem is now concrete: **exclude an inverse-height-cost approximation of the harmonic `1/n` profile by finite power sums formed from actual off-critical zeros**, or construct such an approximation and understand its consequences.

## Keep conditioning, rank supply, continuum mass, compression retention and interpolation geometry separate

Raw Gram conditioning and canonical packet shear are nuisance coordinates for the exact target quotient in NB-117: any invertible packet-coordinate change leaves the attainable primitive sequences and weighted Dirichlet quotient unchanged. Small compression eigenvalues are still insufficient unless the target occupies them, but the target-bearing condition can now be stated without diagonalizing the Gram matrix.

Future claims should distinguish available zero rank, horizontal zero mass, continuum norm, retained cell energy and approximation of the unique harmonic minimizer. Only the last three enter the exact finite target normal form.
