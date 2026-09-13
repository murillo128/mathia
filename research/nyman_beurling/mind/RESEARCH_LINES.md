# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem is whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Compare causal-state leverage with coordinate energy after correlation normalization

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`, `MI-005-persistent-forward-memory-leakage-is-a-target-near-kernel-phenomenon`, `MI-006-boundary-zeros-force-reciprocal-depth-screening`, `MI-007-aliased-radial-prediction-has-a-positive-szego-floor`, `MI-008-finite-blaschke-defects-are-silent-in-terminal-scalar-energy`, `MI-009-summable-horizontal-zero-mass-keeps-full-terminal-gram-entropy-bounded`, `MI-010-growing-depth-mobius-annulus-exposes-off-critical-blaschke-amplification`.

The fixed-depth story is calibrated: terminal scalar channels, the full terminal Gram, and fixed-ratio bands can remain source-silent after universal calibration. [NB-092](../findings/NB-092-growing-depth-mobius-annulus-mode-forces-polynomial-blaschke-gram-gain.md) shows that growing depth is different: the canonical Möbius annulus produces a raw near-kernel, and an off-critical zero repairs that same direction by `q^(2beta-1)`.

[NB-093](../findings/NB-093-single-zero-growing-depth-gram-gain-is-rank-one-causal-state-leverage.md) now resolves the single-zero mechanism exactly. At finite cutoff one elementary Blaschke factor changes the visible Gram by one positive rank-one causal-state update. The full unnormalized single-zero gain is the single leverage scalar

`tau_R=s_R^*A_R^(-1)s_R`,

and the Möbius annulus forces `tau_R>=q^(2beta-1+o(1))`.

The normalized correlation determinant is also exact:

`det R_R^(rho)/det R_tilde_R = (1+tau_R)/prod_j(1+nu_j)`,

where `nu_j` is the same state energy measured coordinatewise. The remaining theorem is therefore no longer “does the determinant gain survive somehow?” It is to compare inverse-correlation leverage against coordinate inflation for the **actual Nyman causal state**, then extend the conclusion coherently to the finite/multiple-zero state family or an aggregate radial statistic.

## Keep raw near-kernel, causal-state leverage and normalized entropy distinct

A polynomial generalized eigenvalue can be erased completely by diagonal normalization in abstract controls. NB-093 shows exactly what extra source geometry must prevent that: the causal state must align with a collective raw near-kernel more strongly than its energy is visible coordinate by coordinate. Any entropy/radial proof should expose that inequality directly instead of returning to another fixed-depth or unnormalized Gram observable.
