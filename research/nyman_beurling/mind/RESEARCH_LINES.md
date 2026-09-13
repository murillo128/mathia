# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem is whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Extend fixed-finite zero-state repair with uniform spectral conditioning, not determinant volume alone

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`, `MI-005-persistent-forward-memory-leakage-is-a-target-near-kernel-phenomenon`, `MI-006-boundary-zeros-force-reciprocal-depth-screening`, `MI-007-aliased-radial-prediction-has-a-positive-szego-floor`, `MI-008-finite-blaschke-defects-are-silent-in-terminal-scalar-energy`, `MI-009-summable-horizontal-zero-mass-keeps-full-terminal-gram-entropy-bounded`, `MI-010-growing-depth-mobius-annulus-exposes-off-critical-blaschke-amplification`, `MI-011-canonical-deflation-cancels-raw-cauchy-crowding-volume`.

NB-092--NB-095 establish the growing-depth near-kernel, one-zero causal state and additive volume-repair exponent for every fixed finite set of distinct off-critical zeros. NB-096 now removes a natural candidate for the hidden finite-set penalty: the raw Cauchy Gram determinant `prod delta_(rs)^2` is cancelled exactly by the reciprocal determinant of the canonical triangular Blaschke-deflation coordinates.

Thus pairwise zero crowding does **not** impose a residual determinant-volume tax at fixed finite dimension. The unnormalized interacting leverage determinant has leading coefficient one after extracting `q^(2 A_F)`. What can still deteriorate is spectral conditioning: small singular values, finite-window approximation as dimension grows, nonuniform `O_F(m^-1)` error, accumulated diagonal-normalization cost, or genuine confluent/multiple-zero structure.

The live growing-family theorem should therefore control one of those stronger resources uniformly as the selected divisor grows, rather than bounding the raw Cauchy determinant again. A separate route remains available: convert the already sharp fixed-finite volume repair directly into a target-relevant Nyman obstruction before taking a growing-divisor limit.

## Keep determinant normalization, spectral conditioning and target conversion separate

NB-096 is an exact cancellation of volumes, not an orthogonalization theorem. Canonical deflation can preserve determinant while the state system becomes ill-conditioned. Exact confluence is not covered by a singular distinct-zero limit, and the final Nyman distance is not determined by correlation-volume repair alone.

Future work should therefore avoid treating a small raw Cauchy determinant as evidence that finite zero-state additivity must collapse. The remaining obstruction must be visible in a stronger norm/condition-number quantity, in dimension-dependent finite-window errors, or at the destination metric itself.