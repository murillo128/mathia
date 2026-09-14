# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem is whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Convert one-zero leverage into target coercivity rather than maximal state gain

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`, `MI-005-persistent-forward-memory-leakage-is-a-target-near-kernel-phenomenon`, `MI-006-boundary-zeros-force-reciprocal-depth-screening`, `MI-007-aliased-radial-prediction-has-a-positive-szego-floor`, `MI-008-finite-blaschke-defects-are-silent-in-terminal-scalar-energy`, `MI-009-summable-horizontal-zero-mass-keeps-full-terminal-gram-entropy-bounded`, `MI-010-growing-depth-mobius-annulus-exposes-off-critical-blaschke-amplification`, `MI-011-canonical-deflation-cancels-raw-cauchy-crowding-volume`, `MI-012-three-state-transverse-confluence-exposes-collective-shear`, `MI-013-absolute-height-and-global-zero-counts-are-invisible-to-the-collective-shear-obstruction`, `MI-014-quadratic-horizontal-tangency-is-the-three-state-conditioning-threshold`, `MI-015-confluent-volume-is-curvature-blind-and-controlled-by-radial-depth`.

NB-103--NB-106 separate fixed-multiplicity volume depth `L=2a log(B/G)` from target-access depth `H=2ad log G`. NB-106 already shows that the maximal one-zero state at natural ordinate start is target-poor despite nonzero leverage.

NB-107 closes the obvious backfill repair for that rank-one channel. Restoring every earlier integer cell down to any fixed natural scale does **not** rotate the maximal one-zero causal state toward the target: its normalized target correlation still tends to zero. More sharply, if `eta` is the fraction of maximal one-zero leverage retained and `chi` the visible target fraction, then the exact two-vector Pareto frontier tends to

`sup_(eta>=theta) chi = 1-theta+o(1)`

for every fixed `theta in (0,1]`.

Thus a large one-zero generalized Gram eigenvalue is not target-coercive by itself. To force target-poorness from this rank-one state, the relevant vector must carry an **asymptotically full fraction of the available leverage**. At every fixed leverage fraction below one, a complementary target fraction survives even after complete early-cell backfill.

The live theorem is therefore no longer “can earlier cells repair the maximal one-zero state?” They cannot. It is whether the full Nyman problem forces near-maximal participation in the off-critical state channel, or whether several zero states / growing-rank state geometry produce a stronger principal-angle obstruction. A successful argument must connect state-subspace leverage to the actual target residual, not infer coercivity from a large maximal eigenvalue.

## Decide the first genuinely new invariant beyond rank-one fixed-multiplicity geometry

NB-102 closes three-state local conditioning. NB-103--NB-106 close fixed-multiplicity determinant volume, boundary phase resolution, terminal placement and the volume/target-access frontier. NB-107 additionally closes complete fixed-scale backfill for the maximal one-zero state and gives the sharp leverage-target tradeoff for that rank-one channel.

Remaining geometric directions include growing multiplicity, genuine repeated-zero derivative/Jordan states, **multi-zero state subspace principal angles**, diagonal normalization, and a theorem forcing the canonical target residual to exploit near-maximal state leverage.

## Keep volume depth, target-access depth and leverage fraction separate

Curvature controls local conditioning. `L=2a log(B/G)` controls optimally placed fixed-multiplicity determinant volume. `H=2ad log G` controls ambient target access. NB-107 adds a third independent currency: the fraction `eta` of maximal one-zero state leverage carried by the actual vector. Backfill can restore ambient target mass without making the state maximizer target-bearing, and fixed `eta<1` can retain target mass even when the maximizer is asymptotically orthogonal. None of these resources alone is the Nyman distance.