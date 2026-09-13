# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem is whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Extend the single-zero normalized leverage law to the interacting zero family

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`, `MI-005-persistent-forward-memory-leakage-is-a-target-near-kernel-phenomenon`, `MI-006-boundary-zeros-force-reciprocal-depth-screening`, `MI-007-aliased-radial-prediction-has-a-positive-szego-floor`, `MI-008-finite-blaschke-defects-are-silent-in-terminal-scalar-energy`, `MI-009-summable-horizontal-zero-mass-keeps-full-terminal-gram-entropy-bounded`, `MI-010-growing-depth-mobius-annulus-exposes-off-critical-blaschke-amplification`.

The fixed-depth story is calibrated: terminal scalar channels, the full terminal Gram, and fixed-ratio bands can remain source-silent after universal subtraction. NB-092 shows that growing depth is different: a canonical Möbius annulus is a raw near-kernel and one off-critical zero repairs that direction by `q^(2beta-1)`.

NB-093 identifies the single-zero update as one causal-state rank-one Gram perturbation with leverage `tau=s^*A^(-1)s` and an exact diagonal-normalization bill `prod_j(1+nu_j)`. [NB-094](../findings/NB-094-zero-cancellation-keeps-coordinate-state-cost-bounded-while-leverage-grows.md) closes that bridge for an actual zeta zero. The zero identity cancels the large coordinate term, giving uniformly `|s_(j,R)|=O_rho(R^(-1/2))` and hence only `O_rho(1)` total coordinate-inflation cost, while the inverse-Gram leverage on `R=mq` grows two-sided like `q^(2beta-1)`.

Consequently the normalized determinant retains the full zero exponent:

`log(det R_(m,mq)^(rho) / det R_tilde_(m,mq)) = (2beta-1) log q + O_rho(1)`.

The sign is now fixed as well: one off-critical zero repairs the raw correlation volume, so the centered correlation entropy is **lower**, not higher, by `(2beta-1)log q+O(1)`. The old question “does diagonal normalization erase the growing-depth gain?” is closed for one actual zero.

The live theorem is the interacting-zero extension. Successive Blaschke factors act on partially deflated intermediate sources, their causal states need not be orthogonal, and diagonal normalization is not monotone under adding states. Determine whether a finite or growing off-critical divisor still forces a calibrated volume-repair/entropy-deficit observable with a lower bound controlled by the largest real part or an additive state-space invariant, and whether that observable can be converted into a target-relevant Nyman obstruction.

## Keep coordinate suppression, collective leverage, normalized sign and multi-state interaction separate

NB-094 shows a particularly sharp source effect: every individual coordinate is small because `zeta(rho)=0`, yet the same state has polynomial inverse-correlation leverage because it aligns with a collective raw near-kernel. Rowwise energy and global leverage are therefore different resources. The single-zero normalized sign is no longer open; what remains is how several source states interact after each successive deflation and normalization. Future work should not return to an unnormalized determinant gain or assume that independent single-zero exponents simply add.
