# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Prove source-specific visibility outside the rooted mixing-invisibility corridor

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

NB-014--NB-017 reduce progress to source-specific multiplicative graph energy and prove that exact reciprocal blind components prevent full-space quotient coercivity at every finite depth. NB-018 shows eventual fixed-section shell mixing but only through an exponentially large period. NB-019 replaces that lcm cost for the actual residual by the intrinsic coefficient/discrepancy budget `A_N`, giving effective mixing once the dilation dominates the target-selected coefficients.

NB-020 then proves that this budget cannot be anomalously cheap: early-shell Möbius inversion forces a coefficient core close to `-mu(n)` and `A_N >= c min(N^2,d_N^{-2})`. NB-021 exposes the more important incompatibility. If the intrinsic shell discrepancy is `o(N)`, then throughout a growing rooted band up to `N/2` the mixed residual converges to zero, so under a hypothetical positive limiting Nyman distance the full semigroup defect grows while its projection back to the old section becomes asymptotically invisible.

The live theorem must therefore obtain source-specific visibility before the mixing-invisibility band, exploit genuinely unrooted channels beyond the old normal-equation anchor, or prove that the canonical residual has the linear discrepancy needed to avoid NB-021 and then convert that structure into the NB-015 budget. Generic deep mixing by itself is no longer a plausible route.

## Treat small discrepancy, cheap coefficient mixing, and generic frame coercivity as controls

A small consecutive-shell discrepancy improves averaging but simultaneously drives the rooted mixed scalar to zero. The target-selected coefficient budget also has an inverse-distance lower floor. Any proposed enrichment theorem must track **visible source energy**, not merely how rapidly the residual mixes or how many future frame directions exist.
