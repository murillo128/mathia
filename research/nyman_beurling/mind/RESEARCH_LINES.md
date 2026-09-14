# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem is whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Rule out target-bearing near-kernels of the integer-cell compression

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`, `MI-005-persistent-forward-memory-leakage-is-a-target-near-kernel-phenomenon`, `MI-006-boundary-zeros-force-reciprocal-depth-screening`, `MI-007-aliased-radial-prediction-has-a-positive-szego-floor`, `MI-008-finite-blaschke-defects-are-silent-in-terminal-scalar-energy`, `MI-009-summable-horizontal-zero-mass-keeps-full-terminal-gram-entropy-bounded`, `MI-010-growing-depth-mobius-annulus-exposes-off-critical-blaschke-amplification`, `MI-011-canonical-deflation-cancels-raw-cauchy-crowding-volume`, `MI-012-three-state-transverse-confluence-exposes-collective-shear`, `MI-013-absolute-height-and-global-zero-counts-are-invisible-to-the-collective-shear-obstruction`, `MI-014-quadratic-horizontal-tangency-is-the-three-state-conditioning-threshold`, `MI-015-confluent-volume-is-curvature-blind-and-controlled-by-radial-depth`, `MI-016-growing-confluent-rank-is-limited-by-endpoint-extrapolation-cost`, `MI-017-finite-high-zero-target-access-requires-a-target-bearing-compression-near-kernel`.

NB-111--NB-112 close the one-zero multiplicity rescue in the current confluent geometry. NB-113--NB-114 then separate multi-zero conditioning from continuum target access: individual high zeros carry inverse-square Burnol defects, common-ordinate crowding is canonically orthogonal, and raw zero counting already forces the full high right-half target mass to vanish.

NB-115 localizes the only canonical finite-section escape. Let `H_(F,R)` be the Gram of the orthogonal integer-cell compression of a finite Burnol packet and `b_(F,R)` its finite target coordinates. The finite target projection is exactly

`b_(F,R)^* H_(F,R)^+ b_(F,R)`.

If this projection captures a fixed positive fraction of the visible Nyman target while the continuum packet has mass `tau(F)`, then at least half of the finite target projection must pass through compression eigenmodes with retained-energy fraction

`lambda = O(tau(F)+1/R)`.

NB-116 now uses Selberg near-critical zero density in the representation that the Burnol factor actually sees. The weighted horizontal zero count satisfies

`sum_(0<gamma<=T, beta>1/2) (beta-1/2) = O(T)`,

so the entire actual right-half Blaschke tail above `G`, with arbitrary packet width and multiplicity, has

`tau(F) = O(1/G)`.

Therefore any order-one finite target access from any such packet must load cell-compression modes with

`lambda = O(1/G + 1/R)`.

For `R/G -> infinity` the live source-specific scale is `1/G`, one logarithm below the raw zero-counting shell bound from NB-115. Wider packets and extra rank cannot evade it. The next zero-state theorem should prove that the actual zeta packet has negligible target spectral weight below this inverse-height retention scale, or establish a lower retention bound for target-bearing modes that exceeds it.

## Keep conditioning, rank supply, continuum mass and compression retention separate

Collective shear can be arbitrarily bad while Burnol target mass vanishes. A small eigenvalue of the cell-compression Gram is also insufficient by itself: NB-115 requires the finite target coordinates to load that eigenspace. NB-116 adds that actual high-zero continuum target mass is governed by the horizontal first moment, not the total zero count. Future claims must therefore distinguish state conditioning, available zero rank, horizontal zero mass, continuum target occupation, compression retention, and target weight on low-retention modes. Only the last two can amplify a target-poor high-zero packet inside the canonical finite arithmetic window.