# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem is whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Convert state-subspace leverage into target coercivity rather than maximal state gain

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`, `MI-005-persistent-forward-memory-leakage-is-a-target-near-kernel-phenomenon`, `MI-006-boundary-zeros-force-reciprocal-depth-screening`, `MI-007-aliased-radial-prediction-has-a-positive-szego-floor`, `MI-008-finite-blaschke-defects-are-silent-in-terminal-scalar-energy`, `MI-009-summable-horizontal-zero-mass-keeps-full-terminal-gram-entropy-bounded`, `MI-010-growing-depth-mobius-annulus-exposes-off-critical-blaschke-amplification`, `MI-011-canonical-deflation-cancels-raw-cauchy-crowding-volume`, `MI-012-three-state-transverse-confluence-exposes-collective-shear`, `MI-013-absolute-height-and-global-zero-counts-are-invisible-to-the-collective-shear-obstruction`, `MI-014-quadratic-horizontal-tangency-is-the-three-state-conditioning-threshold`, `MI-015-confluent-volume-is-curvature-blind-and-controlled-by-radial-depth`, `MI-016-growing-confluent-rank-is-limited-by-endpoint-extrapolation-cost`.

NB-103--NB-106 separate fixed-multiplicity volume depth `L=2a log(B/G)` from target-access depth `H=2ad log G`. NB-107 shows that restoring every earlier integer cell down to any fixed natural scale does not rotate the maximal one-zero state toward the target and gives the sharp rank-one leverage-target frontier `sup_(eta>=theta) chi=1-theta+o(1)`.

NB-108 closes every fixed-dimensional confluent/Jordan repair. NB-109 extends that target-poorness to a genuinely growing packet without using monomial Gram conditioning: if `A=2a log(m/r)` is the radial extrapolation distance, then

`delta^2 << G^(-1) [C_L(1+A)]^(2d)`.

Hence `d log(2+A)=o(log G)` suffices for the whole packet to become target-orthogonal; in particular every `d <= (1/2-epsilon) log G/log log G` packet is still target-poor. The same leverage-target frontier remains valid because it depends only on the principal angle once that angle vanishes.

Thus neither one state, fixed-rank repetition, nor near-logarithmically growing one-zero multiplicity is target-coercive merely because state gain is large. The remaining one-zero multiplicity route must enter the transition where polynomial endpoint extrapolation can compete with terminal coercivity, or use source-specific multiplicity information stronger than the generic `O(log G)` bound. Genuinely several-distinct-zero growing-rank geometry remains separate.

## Decide the transition beyond the polynomial extrapolation window

NB-102 closes three-state local conditioning. NB-103--NB-106 close fixed-multiplicity determinant volume, boundary phase resolution, terminal placement and the volume/target-access frontier. NB-107 closes complete fixed-scale backfill for the maximal one-zero state. NB-108 extends the target-poorness and Pareto frontier to every fixed-dimensional confluent packet; NB-109 pushes this to `d log(2+A)=o(log G)` and shows that whitening cannot erase the real growing-rank cost because Chebyshev extrapolation has the same exponential order.

The next one-zero question is therefore the actual transition region: can the full state measure or zeta-zero source beat the generic polynomial extrapolation cost when `d` approaches the `O(log G)` multiplicity ceiling, or does target-poorness persist farther? A better-conditioned derivative basis alone cannot answer this. The other genuinely new direction is a growing subspace built from several distinct zeros rather than more derivatives of one zero.

## Keep volume depth, target-access depth, subspace rank, extrapolation distance and leverage fraction separate

Curvature controls local conditioning. `L=2a log(B/G)` controls optimally placed fixed-multiplicity determinant volume. `H=2ad log G` controls ambient target access. NB-107--NB-109 add the fraction `eta` of maximal state leverage and show that the sharp complementary target fraction remains dimension-free whenever the state subspace itself is target-poor. NB-109 also identifies the growing-rank invariant `d log(2+A)`: it prices extrapolation from a resolved terminal radial band to the target endpoint and survives changes of basis. None of these currencies alone is the Nyman distance.
