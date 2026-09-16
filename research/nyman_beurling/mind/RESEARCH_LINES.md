# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Make Gamma-balanced exterior samplers selective, not merely well-conditioned

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-033-macroscopic-gamma-cost-is-a-rank-one-signed-height-moment`.

NB-148 identifies the signed escape from positive exterior Poisson sampling: zero total sampler mass cancels the universal Hadamard logarithm but exports an equal sign debt. NB-150--NB-155 progressively show that mesoscopic spreading, fixed-scale target packets, arbitrary fixed compact samplers, boundary approach and sublinear vertical widening do not isolate a logarithmic target packet under sublogarithmic effective conditioning.

NB-156 crossed the macroscopic-support boundary with the sufficient envelope `E_G=D_G+C_G log(G/H_G)`. NB-157 then showed that this envelope is not intrinsic: before absolute values, the leading completed-Gamma contribution is the single signed log-height moment. Three polynomially separated heights can cancel both total mass and that Gamma moment exactly with bounded coefficients.

NB-158 closes the target-conditioning loophole for the explicit three-height construction. The top lobe retains uniformly positive `O(1)` charge on every zero in a fixed window around `G`, while `D_G=O(1)` and `J_G=0`. Gamma balancing can therefore be both polynomially deep and well-conditioned on the same microscopic target cells used by the current route.

What fails is **selection**. The negative middle-height coefficient creates a fixed-width lobe near `G^theta_2` with uniformly negative charge, and the explicit Riemann--von Mangoldt remainder already forces `Omega(log G)` actual zeros into that lobe for every sufficiently large `G`. The signed debt exported by a logarithmic target packet can be absorbed by a routine lower-height zero reservoir. Iterating the descent only walks through ordinary zero density unless some rarer target feature is preserved.

The live route must therefore prevent compensating negative charge from landing in a routinely populated region, preserve the target's horizontal/microscopic localization through the sign change, or couple the exterior sampler to a source-specific Nyman/von-Mangoldt observable before the zero charge is separated by sign. Widening support, cancelling the Gamma moment and keeping target conditioning bounded are no longer sufficient discriminators.

## Keep signed conservation, boundary conditioning, Gamma moments and adverse-reservoir occupancy as separate currencies

Positive sampling pays the Hadamard background. Zero-mass sampling removes it but creates sign debt. Boundary approach is priced by `D_G=C_G/a_G`. NB-157 makes the macroscopic Gamma background a signed log-height moment `J_G`; NB-158 shows that even `D_G=O(1)` and `J_G=0` can coexist with a logarithmically populated adverse lobe.

A future sampler must therefore state target charge, total variation, boundary gap, height distribution, signed log-height defect, **where each opposite-sign lobe lands**, the zero population there, and prime/Nyman-side cancellation simultaneously. A balanced moment is not a selector when ordinary source density already fills the compensating lobe.

## Push canonical shell discrepancy independently

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem is whether the canonical arithmetic coefficients force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate being targeted. This route remains distinct from the zero-packet Poisson budgets above.
