# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Resolve the one-Poisson-width interlaced signed-sampler regime

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-035-jordan-transport-length-is-the-conditioning-price-of-sign-collapse`.

NB-148 identifies the signed escape from positive exterior Poisson sampling: zero total sampler mass cancels the universal Hadamard logarithm but exports an equal sign debt. NB-150--NB-155 show that mesoscopic spreading, fixed-scale packets, compact signed samplers, boundary approach and sublinear vertical widening do not isolate a logarithmic target packet under sublogarithmic effective conditioning.

NB-156 crossed the macroscopic-support boundary. NB-157 showed that the leading completed-Gamma contribution is one signed log-height moment, so polynomially separated heights can cancel both total mass and the Gamma moment. NB-158--NB-159 show that any fixed finite polynomial-height atomic repair with bounded target conditioning exports a comparable negative lobe into a routine `Omega(log G)` zero reservoir.

NB-160 removes the finite-cardinality and atomicity loopholes. For an arbitrary finite signed Borel height measure with zero total mass, polynomially high support, bounded total-variation conditioning and positive/negative Jordan supports separated by a sufficiently large fixed number of Poisson widths, every infinitesimal piece of negative mass sees local zero density `Theta(log G)`. The zero-summed positive cross-talk decays like `1/Delta`, so the adverse charge remains `Omega(c_G log G)` and forces `Omega(log G)` negative-response zeros. Spreading the negative mass over growing cardinality or a continuum does not help.

NB-161 closes the opposite geometric extreme at fixed horizontal scale. If `nu=nu^+-nu^-` is zero-mass and `ell(nu)=W_1(nu^+,nu^-)/M` is the mean optimal Jordan transport length, the exterior Poisson response is bounded by total variation times `ell`; hence genuine transport collapse at bounded conditioning loses fixed target gain.

NB-162 supplies the boundary-covariant form of that statement. If the exterior gap is `a_G`, conditioning is `C_G=||nu_G||_TV/c_G`, and

`Theta_G = C_G ell(nu_G)/a_G`,

then `Theta_G` controls every Poisson target response relative to its own natural kernel height and also controls the signed Euler-product response relative to the boundary scale `c_G/a_G`. Thus absolute `ell_G->0` is not itself fatal when the Poisson width shrinks. What is fatal is **sub-Poisson transport**, `Theta_G=o(1)`: it buys excellent prime-side cancellation only by making the sampler equally invisible to the target.

The bounded-conditioning signed route is therefore narrowed to a scale-invariant intermediate geometry. Many-width sign separation exports an adverse `Omega(log G)` zero reservoir; sub-Poisson transport loses the target. The remaining regime is **one-Poisson-width local interlacing**, `Theta_G=Theta(1)`, where positive and negative mass overlap strongly enough to evade the separated-reservoir argument but remain separated enough in transport units to preserve target gain.

The live theorem is whether one-width interlacing can make the routine local zero population cancel while preserving natural-scale target gain and bounded conditioning, and whether it can exploit source-specific prime cancellation stronger than the generic transport bound without shrinking the target by the same factor. An alternative escape must worsen conditioning/lower-height assumptions or couple the signed sampler to the von Mangoldt/Nyman observable before the Jordan transport description becomes load-bearing.

## Keep signed conservation, conditioning, boundary scale, sign-support geometry, transport length and adverse occupancy separate

Positive sampling pays the Hadamard background. Zero-mass sampling removes it but creates sign debt. Boundary approach and transport now combine through the dimensionless currency `Theta_G=C_G ell_G/a_G`; macroscopic Gamma cancellation is a signed height-moment condition. NB-158--NB-160 show that bounded conditioning plus universal moment cancellation does not help while opposite signs remain separated by many Poisson widths. NB-161--NB-162 show the complementary bill: transport much finer than the Poisson width suppresses both prime-side leakage and target response.

A future sampler must therefore expose target charge, total variation, boundary gap, Jordan-support overlap/separation in Poisson units, mean optimal transport length, signed background moments, local zero population, and any prime/Nyman-side cancellation simultaneously. Cardinality and atomicity are no longer relevant escape resources, and absolute minimum support distance or absolute transport length alone is not the correct coordinate in the shrinking-boundary regime.

## Push canonical shell discrepancy independently

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem is whether the canonical arithmetic coefficients force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate being targeted. This route remains distinct from the zero-packet Poisson budgets above.
