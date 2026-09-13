# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem is whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Transfer the growing-depth Möbius/Blaschke gain into normalized radial entropy

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`, `MI-005-persistent-forward-memory-leakage-is-a-target-near-kernel-phenomenon`, `MI-006-boundary-zeros-force-reciprocal-depth-screening`, `MI-007-aliased-radial-prediction-has-a-positive-szego-floor`, `MI-008-finite-blaschke-defects-are-silent-in-terminal-scalar-energy`, `MI-009-summable-horizontal-zero-mass-keeps-full-terminal-gram-entropy-bounded`, `MI-010-growing-depth-mobius-annulus-exposes-off-critical-blaschke-amplification`.

The finite-depth story is now calibrated. Fixed terminal scalar channels, the full terminal Gram, and every fixed-ratio contiguous band can remain source-silent after subtracting their universal raw baseline when the horizontal off-critical mass is summable. Moving from `R/2` to `R/q` for another constant `q` does not create arithmetic information.

[NB-092](../findings/NB-092-growing-depth-mobius-annulus-mode-forces-polynomial-blaschke-gram-gain.md) shows that the growing-depth frontier is different. On `m<=j<mq`, a canonical coefficient vector built from the weighted Möbius sums synthesizes an exact flat logarithmic annulus. Its norm is governed by `Q_q=sum_(r<q)|sum_(d<=r)mu(d)/d|^2`, and false RH forces `Q_q` to grow at zero-frontier exponent at least `2Theta-1`, producing a raw Gram near-kernel.

The same off-critical zero that forces this deterioration also amplifies the visible annulus through its Blaschke factor by `q^(2beta-1)`. Consequently the generalized determinant ratio `det K/det K_tilde` gains at least `(2beta-1)log q+O(1)` in logarithmic scale. Growing depth therefore already contains a source-specific signal; the old question “does any growing-depth signal exist?” is closed.

The remaining theorem is destination-specific. Show that this unnormalized generalized Gram gain survives diagonal/correlation normalization strongly enough to make the normalized visible entropy or NB-086 radial charge diverge, or embed the same Möbius annulus mode into an inter-scale statistic with a proved lower bridge to the Nyman obstruction. A polynomial determinant repair is not sufficient if normalization removes exactly that volume gain.

## Keep raw near-kernel, Blaschke amplification and normalized entropy distinct

NB-092 couples two exact source effects on one direction: Möbius inversion makes the raw band nearly singular at the zero-frontier scale, and the off-critical inner factor repairs that direction polynomially. Neither fact alone proves the target radial divergence. The next step must preserve their relative gain through the normalization actually consumed by the Nyman criterion rather than return to another fixed-depth Gram observable.