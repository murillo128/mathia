# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Resolve the fixed-width interlaced signed-sampler regime

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-035-jordan-transport-length-is-the-conditioning-price-of-sign-collapse`.

NB-148 identifies the signed escape from positive exterior Poisson sampling: zero total sampler mass cancels the universal Hadamard logarithm but exports an equal sign debt. NB-150--NB-155 show that mesoscopic spreading, fixed-scale packets, compact signed samplers, boundary approach and sublinear vertical widening do not isolate a logarithmic target packet under sublogarithmic effective conditioning.

NB-156 crossed the macroscopic-support boundary. NB-157 showed that the leading completed-Gamma contribution is one signed log-height moment, so polynomially separated heights can cancel both total mass and the Gamma moment. NB-158--NB-159 show that any fixed finite polynomial-height atomic repair with bounded target conditioning exports a comparable negative lobe into a routine `Omega(log G)` zero reservoir.

NB-160 removes the finite-cardinality and atomicity loopholes. For an arbitrary finite signed Borel height measure with zero total mass, polynomially high support, bounded total-variation conditioning and positive/negative Jordan supports separated by a sufficiently large fixed number of Poisson widths, every infinitesimal piece of negative mass sees local zero density `Theta(log G)`. The zero-summed positive cross-talk decays like `1/Delta`, so the adverse charge remains `Omega(c_G log G)` and forces `Omega(log G)` negative-response zeros. Spreading the negative mass over growing cardinality or a continuum does not help.

NB-161 closes the opposite geometric extreme under bounded conditioning. If `nu=nu^+-nu^-` is zero-mass and `ell(nu)=W_1(nu^+,nu^-)/M` is the mean optimal Jordan transport length, the exterior Poisson response obeys

`|Q_nu| <= (9/(16 sqrt(3) a^2)) ||nu||_TV ell(nu)`

uniformly at fixed horizontal offset `x in [a,a+1]`. Hence order-`c_G` target gain forces

`C_G ell(nu_G) >= (16 sqrt(3)/9) q a^2`,

where `C_G=||nu_G||_TV/c_G`. In particular, if opposite Jordan masses can be coupled at scale `epsilon_G->0`, bounded conditioning cannot retain fixed target gain; the conditioning must grow at least like `1/epsilon_G`.

Together NB-160 and NB-161 narrow the bounded-conditioning signed route to a specific intermediate geometry. Large fixed sign separation exports an adverse `Omega(log G)` zero reservoir, while genuine transport collapse becomes invisible to the fixed-offset Poisson probe. The remaining regime has **local sign overlap/interlacing with order-one Jordan transport length**: the supports must interact within `O(1)` Poisson widths without allowing the mass transport itself to shrink to `o(1)`.

The live theorem is whether such fixed-width interlacing can make the routine local zero population cancel while preserving order-`c_G` target gain and bounded conditioning, or whether an additional target-conditioned obstruction closes that last geometric window. An alternative escape must worsen conditioning/lower-height assumptions or couple the signed sampler to the von Mangoldt/Nyman observable before the Jordan decomposition becomes the relevant description.

## Keep signed conservation, conditioning, sign-support geometry, transport length and adverse occupancy separate

Positive sampling pays the Hadamard background. Zero-mass sampling removes it but creates sign debt. Boundary approach is priced by `D_G=C_G/a_G`; macroscopic Gamma cancellation is a signed height-moment condition. NB-158--NB-160 show that bounded conditioning plus universal moment cancellation does not help while opposite signs remain separated at the Poisson scale. NB-161 adds the complementary quantitative bill: too-fine opposite-sign transport loses target response unless total variation grows reciprocally.

A future sampler must therefore expose target charge, total variation, boundary gap, Jordan-support overlap/separation, mean optimal transport length, signed background moments, local zero population, and any prime/Nyman-side cancellation simultaneously. Cardinality and atomicity are no longer relevant escape resources, and minimum support distance alone is not the correct coordinate inside an interlaced regime.

## Push canonical shell discrepancy independently

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem is whether the canonical arithmetic coefficients force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate being targeted. This route remains distinct from the zero-packet Poisson budgets above.
