# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem is whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Match finite-window radial depth to ordinate resolution in the source packet

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`, `MI-005-persistent-forward-memory-leakage-is-a-target-near-kernel-phenomenon`, `MI-006-boundary-zeros-force-reciprocal-depth-screening`, `MI-007-aliased-radial-prediction-has-a-positive-szego-floor`, `MI-008-finite-blaschke-defects-are-silent-in-terminal-scalar-energy`, `MI-009-summable-horizontal-zero-mass-keeps-full-terminal-gram-entropy-bounded`, `MI-010-growing-depth-mobius-annulus-exposes-off-critical-blaschke-amplification`, `MI-011-canonical-deflation-cancels-raw-cauchy-crowding-volume`, `MI-012-three-state-transverse-confluence-exposes-collective-shear`, `MI-013-absolute-height-and-global-zero-counts-are-invisible-to-the-collective-shear-obstruction`, `MI-014-quadratic-horizontal-tangency-is-the-three-state-conditioning-threshold`, `MI-015-confluent-volume-is-curvature-blind-and-controlled-by-radial-depth`.

NB-098--NB-102 classify the local three-state **conditioning** problem: after canonical deflation, dimensionless Menger curvature governs the condition number.

NB-103 shows that fixed-multiplicity normalized **determinant volume** uses a different currency. For a fixed interior center its confluent coefficient is path-independent and depends on radial depth

`x=2 Re(lambda_*) log q`

through the Laguerre determinant `Delta_d(x)`.

NB-104 now resolves the previously nonuniform boundary `a=Re(lambda_*)->0`. The finite logarithmic cells introduce an ordinate-resolution delay

`y=2a log^+(|Gamma|/m)`.

At fixed multiplicity and `x_j->x`, `y_j->y`, the confluent volume tends to `e^(-dy) Delta_d(x-y)` for `0<=y<x`, and to zero for `y>=x`. The finite window therefore spends radial depth before it can resolve a rapidly rotating Mellin phase. Continuum height-gauge invariance is not violated; the new variable is the ratio between source ordinate and discrete cell scale.

The live source/representation question is to choose or control the window parameters `m,q` so that a hypothetical off-critical packet retains enough **post-delay depth** in the exact destination quantity the Nyman argument consumes. Moving `m` can remove the delay, so a useful obstruction must survive the admissible target-aware choice of band start rather than treating `|Gamma|` alone as a defect.

## Decide the first genuinely new invariant beyond fixed-multiplicity determinant geometry

NB-102 closes three-distinct-state local conditioning. NB-103--NB-104 close the fixed-multiplicity confluent determinant law across the interior and boundary double-scaling regimes, including the ordinate-resolution variable. The next geometric directions are growing multiplicity, genuine repeated-zero derivative/Jordan states, diagonal normalization, or a target conversion showing which combination of conditioning, post-delay volume and finite-window placement actually controls Nyman approximation.

A separate route remains available: convert the sharp fixed-finite repair directly into a target-relevant Nyman obstruction before taking a growing-divisor limit.

## Keep curvature, radial depth, ordinate delay and target conversion separate

Curvature is a spectral-conditioning resource. Radial depth is the continuum fixed-multiplicity volume resource. Ordinate delay is a finite-window resolution cost that subtracts from that depth. None of these statements decides the geometry of actual zeta-zero packets or whether the final Nyman target is sensitive to the corresponding resource. Future arguments should not use one currency as a proxy for another.
