# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem is whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Extend fixed-finite zero additivity to the growing divisor or to the target Nyman observable

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`, `MI-005-persistent-forward-memory-leakage-is-a-target-near-kernel-phenomenon`, `MI-006-boundary-zeros-force-reciprocal-depth-screening`, `MI-007-aliased-radial-prediction-has-a-positive-szego-floor`, `MI-008-finite-blaschke-defects-are-silent-in-terminal-scalar-energy`, `MI-009-summable-horizontal-zero-mass-keeps-full-terminal-gram-entropy-bounded`, `MI-010-growing-depth-mobius-annulus-exposes-off-critical-blaschke-amplification`.

The fixed-depth story is calibrated: terminal scalar channels, the full terminal Gram and fixed-ratio bands can remain source-silent after universal subtraction. NB-092 shows that growing multiplicative depth is different: a canonical Möbius annulus is a raw near-kernel and an off-critical zero repairs that direction polynomially.

NB-093 identifies the single-zero update as one causal-state rank-one Gram perturbation. NB-094 closes diagonal normalization for an actual zero: the zero identity keeps every coordinate `O_rho(R^(-1/2))`, so the coordinate-normalization cost is bounded, while inverse-Gram leverage on `R=mq` grows like `q^(2beta-1)`.

[NB-095](../findings/NB-095-finite-distinct-zero-states-add-their-growing-depth-volume-repair.md) now closes the interaction problem for every fixed finite set `F` of pairwise distinct off-critical zeros. Successive states on partially deflated sources are a fixed invertible triangular transform of the raw zero states, whose scaled inverse-Gram matrix has a uniformly positive Cauchy/model-space limit. Consequently

`log(det R_(m,mq)^[F]/det R_tilde_(m,mq)) = 2 sum_(rho in F)(Re rho-1/2) log q + O_F(1)`.

Finite distinct states therefore do not screen one another: their normalized volume-repair exponents add with the same sign as the one-zero law. The old question “does finite multi-state interaction erase the signal?” is closed.

The live theorem begins only beyond fixed finite dimension. Determine whether the additive law remains quantitatively useful when the selected divisor grows with depth, when zero states become poorly conditioned or confluent, or when multiplicities must be retained; alternatively, convert the fixed-finite normalized volume repair directly into a target-relevant Nyman obstruction before taking such a limit. Any growing-family theorem must make the dependence on the zero set explicit rather than hide it in `O_F(1)`.

## Keep fixed-finite additivity, growing-family conditioning and target conversion separate

NB-095 proves a strong finite-dimensional fact but not uniformity in the state count. The positive model-space Gram is uniformly controlled for one fixed distinct set, while its conditioning can in principle deteriorate as more zeros are inserted or parameters approach one another. That is a different resource from diagonal normalization, which is already controlled zero by zero.

Future work should therefore distinguish three questions: the exact additive exponent for fixed finite divisors is settled; the stability of the constants and Gram geometry for a growing/confluent divisor is open; and the conversion from correlation-volume repair to Nyman distance remains a separate target-sensitivity problem. Returning to isolated one-zero estimates or assuming finite exponents merely sum in an infinite limit would discard the boundary identified by NB-095.
