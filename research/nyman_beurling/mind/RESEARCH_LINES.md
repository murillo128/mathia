# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem is whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Convert optimal terminal resolution depth into a target-relevant Nyman obstruction

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`, `MI-005-persistent-forward-memory-leakage-is-a-target-near-kernel-phenomenon`, `MI-006-boundary-zeros-force-reciprocal-depth-screening`, `MI-007-aliased-radial-prediction-has-a-positive-szego-floor`, `MI-008-finite-blaschke-defects-are-silent-in-terminal-scalar-energy`, `MI-009-summable-horizontal-zero-mass-keeps-full-terminal-gram-entropy-bounded`, `MI-010-growing-depth-mobius-annulus-exposes-off-critical-blaschke-amplification`, `MI-011-canonical-deflation-cancels-raw-cauchy-crowding-volume`, `MI-012-three-state-transverse-confluence-exposes-collective-shear`, `MI-013-absolute-height-and-global-zero-counts-are-invisible-to-the-collective-shear-obstruction`, `MI-014-quadratic-horizontal-tangency-is-the-three-state-conditioning-threshold`, `MI-015-confluent-volume-is-curvature-blind-and-controlled-by-radial-depth`.

NB-098--NB-102 classify the local three-state **conditioning** problem: after canonical deflation, dimensionless Menger curvature governs the condition number.

NB-103 shows that fixed-multiplicity normalized **determinant volume** uses a different currency. For a fixed interior center its confluent coefficient is path-independent and depends on radial depth `x=2 Re(lambda_*) log q` through the Laguerre determinant `Delta_d(x)`.

NB-104 resolves the boundary double-scaling problem by exposing the ordinate-resolution delay `y=2a log^+(|Gamma|/m)`. A finite logarithmic window spends radial depth before it resolves a rapidly rotating Mellin phase.

NB-105 now closes the apparent band-placement escape once a terminal natural-index budget `B` is fixed. With `G=max(1,|Gamma|)`, the exact terminal resource is

`L=2a log(B/G)`.

Writing the scaled start offset `s=2a log(m/G)` and unused terminal slack `tau=2a log(B/(mq))`, the limiting fixed-multiplicity volume is maximized **uniquely** at `s=0`, `tau=0`, with value `Delta_d(L)`. Starting above the ordinate scale removes the NB-104 delay but loses the same radial depth from the window; starting below it keeps the interval length but pays an exponential determinant factor. There is no free placement repair.

For any fixed target volume fraction `eta`, NB-105 therefore forces the terminal budget

`B >= |Gamma| exp((Delta_d^(-1)(eta)+o(1))/(2a))`

along a boundary sequence. The live source-to-target question is no longer how to tune `m,q` at the determinant-volume level. It is whether the **optimal terminal resolution depth relative to the zero ordinate** available in an actual Nyman section couples to the target norm or dual certificate strongly enough to obstruct an off-critical zero.

## Decide the first genuinely new invariant beyond fixed-multiplicity determinant geometry

NB-102 closes three-distinct-state local conditioning. NB-103--NB-105 close the fixed-multiplicity confluent determinant law across interior, boundary resolution and terminal-budget placement. The remaining geometric directions are growing multiplicity, genuine repeated-zero derivative/Jordan states, diagonal normalization, or a target conversion showing how curvature and terminal resolution depth enter actual Nyman approximation.

A separate route remains available: convert the sharp fixed-finite repair directly into a target-relevant Nyman obstruction before taking a growing-divisor limit.

## Keep curvature, terminal resolution depth and target conversion separate

Curvature is a spectral-conditioning resource. After optimal finite-window placement, fixed-multiplicity determinant volume is governed by the single terminal resource `L=2a log(B/G)`. NB-105 shows that ordinate delay and nominal radial depth are not independently tunable under a terminal budget. None of these statements decides the geometry of actual zeta-zero packets or whether the final Nyman target is sensitive to determinant volume. Future arguments should not use one currency as a proxy for another.
