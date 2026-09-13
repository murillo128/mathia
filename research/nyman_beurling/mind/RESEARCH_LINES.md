# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem is whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Control collective canonical shear and finite-window loss for a growing zero divisor

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`, `MI-005-persistent-forward-memory-leakage-is-a-target-near-kernel-phenomenon`, `MI-006-boundary-zeros-force-reciprocal-depth-screening`, `MI-007-aliased-radial-prediction-has-a-positive-szego-floor`, `MI-008-finite-blaschke-defects-are-silent-in-terminal-scalar-energy`, `MI-009-summable-horizontal-zero-mass-keeps-full-terminal-gram-entropy-bounded`, `MI-010-growing-depth-mobius-annulus-exposes-off-critical-blaschke-amplification`, `MI-011-canonical-deflation-cancels-raw-cauchy-crowding-volume`.

NB-092--NB-095 establish the growing-depth near-kernel, one-zero causal state and additive volume-repair exponent for every fixed finite set of distinct off-critical zeros. NB-096 removes the raw Cauchy determinant penalty exactly through canonical Blaschke deflation.

NB-097 now closes two stronger finite-dimensional failure modes. Every leading principal minor of the canonically transformed half-line Gram is one, so every Cholesky/Schur pivot is exactly one. For two distinct zero states the remaining unit-triangular shear has modulus at most `2`, giving the uniform spectral bounds

`(3-2 sqrt(2)) I <= C_2 <= (3+2 sqrt(2)) I`.

Thus neither pairwise zero crowding nor a collapsing sequence of canonical pivots can explain an unbounded half-line condition number. If conditioning fails as the divisor grows, the failure must be **collective unit-triangular shear** involving increasing dimension, or it must enter through finite-window approximation/discretization and later normalization rather than the half-line two-state geometry.

The live theorem is therefore to control `||R_F||` and `||R_F^(-1)||` for the unit-upper-triangular Cholesky factor of the canonical interacting Gram as `|F|` grows, ideally in a way insensitive to raw pseudo-hyperbolic separation, while simultaneously quantifying the finite-window replacement, the currently nonuniform `O_F(m^-1)` discretization error and accumulated diagonal-normalization cost. A counterexample should identify a genuinely collective amplification, not repackage a close pair.

A separate route remains available: convert the already sharp fixed-finite repair directly into a target-relevant Nyman obstruction before taking a growing-divisor limit.

## Keep half-line conditioning, finite-window uniformity, confluence and target conversion separate

NB-096 is exact volume cancellation; NB-097 upgrades it to unit canonical pivots and uniform two-state conditioning. Neither is a dimension-free orthogonalization theorem. A high-dimensional unit-triangular shear can still be badly conditioned even though every prefix determinant is one.

Exact confluence/multiple zeros require their own Jordan/derivative causal system; the distinct two-zero collision has path-dependent limits and cannot define it by continuity. And even perfect generator-state conditioning would still need a theorem transferring that geometry into the final Nyman distance. Future work should keep those gates explicit rather than treating raw zero separation as the missing resource.
