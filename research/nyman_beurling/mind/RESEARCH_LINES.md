# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Classify sublogarithmically conditioned exterior samplers after Gamma balancing

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-033-macroscopic-gamma-cost-is-a-rank-one-signed-height-moment`.

NB-148 identifies the signed escape from positive exterior Poisson sampling: zero total sampler mass cancels the universal Hadamard logarithm but exports an equal sign debt. NB-150--NB-155 progressively show that mesoscopic spreading, fixed-scale target packets, arbitrary fixed compact samplers, boundary approach and sublinear vertical widening do not isolate a logarithmic target packet under sublogarithmic effective conditioning.

NB-156 crossed the macroscopic-support boundary with the sufficient envelope

`E_G = D_G + C_G log(G/H_G)`,

suggesting that descending to much smaller ordinates might spend a new Gamma resource.

NB-157 shows that the envelope is not intrinsic. Before absolute values, the leading completed-Gamma contribution is the single signed moment

`int log((G+Im w)/G) d mu_G(w)`.

After normalizing by target charge, call its magnitude `J_G`. The adverse-packet argument survives whenever `D_G+J_G=o(log G)`, independent of the size of `log(G/H_G)` as long as the lowest sampled ordinate still tends to infinity. On the mass-zero sampler space this Gamma term is rank one: two distinct heights cannot cancel it nontrivially, while three heights can cancel it exactly with bounded coefficients even for polynomially separated heights.

The live route is therefore **not vertical range itself**. A genuine escape must simultaneously preserve useful target charge while forcing `J_G=Omega(log G)`, pay `D_G=Omega(log G)`, descend into a regime where the uniform large-height Gamma expansion no longer applies, or obtain source-specific signed prime/Nyman cancellation that changes the conservation law. The decisive next theorem should price the compatibility of target conditioning, Gamma-balanced height moments and arithmetic signed cancellation rather than add another geometric support envelope.

## Keep signed conservation, boundary conditioning and Gamma moments as separate currencies

Positive sampling pays the Hadamard background. Zero-mass sampling removes it but creates sign debt. Boundary approach is priced by `D_G=C_G/a_G`. Vertical transport changes where adverse charge can lie. NB-157 adds the correction that the macroscopic Gamma background is controlled by a **signed log-height moment**, not by support diameter alone.

A future sampler must therefore state target charge, total variation, boundary gap, height distribution, signed log-height defect and prime-side cancellation simultaneously. Replacing the signed moment by its absolute support envelope loses exactly the cancellation that the new three-height construction exposes.

## Push canonical shell discrepancy independently

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem is whether the canonical arithmetic coefficients force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate being targeted. This route remains distinct from the zero-packet Poisson budgets above.
