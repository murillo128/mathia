# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem remains whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Combine integer-dilation branching with finite Schur certificates

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`, `MI-005-persistent-forward-memory-leakage-is-a-target-near-kernel-phenomenon`.

NB-066--NB-067 reduce a persistent late quotient to a global continuation mode and expose it through finite normalized Schur certificates. NB-068 showed that zero one-cell memory and fixed finite Gram bandwidth alone are insufficient by constructing a nearest-neighbor boundary chain with a stable tail.

NB-069 now proves that this strongest matched control omits an exact source law. The canonical Nyman innovations satisfy integer-dilation branching: each coarse innovation is sent isometrically to the normalized sum of one consecutive block of finer innovations. Consequently every coarse Gram entry equals a normalized rectangular block sum of finer Gram entries.

That renormalization is rigid. A uniformly bounded innovation sequence with exact branching and a fixed finite-band Gram matrix must have a diagonal Gram matrix. The nonorthogonal tridiagonal boundary chain from NB-068 therefore cannot be a matched control once the actual source's dilation covariance is included.

The remaining obstruction is more specific: any genuine stable-tail countermodel must preserve branching while using long-range or scale-growing Gram interaction, or compensate the block normalization through unbounded generator size. The positive route is to combine the exact block-renormalization identities with the NB-067 Schur matrices and show that such branch-compatible compensation makes the continuation cost controllable.

## Treat local memory, branching covariance, global continuation cost, and finite certification separately

NB-068 remains a valid warning against one-cell arguments, but NB-069 shows that local matching must include the source's cross-scale covariance before a control is admissible. Further refinement of `Gamma_R` alone is still irrelevant; the new leverage is the finite-Gram branching identity acting across scales.