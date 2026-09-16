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

NB-163 shows that imposing finitely many additional local moment cancellations does not create a second currency. If moments through order `r-1` vanish around `t_0`, the dimensionless quantity

`Xi_r = M_r(nu;t_0)/(c a^r)`

with `M_r=int |t-t_0|^r d|nu|` bounds both every normalized Poisson target response and the signed Euler response relative to its natural `c/a` boundary scale. For fixed `r`, `Xi_r=o(1)` therefore suppresses target and Euler sides together. If the sampler is supported in radius `L`, bounded conditioning gives `Xi_r <= C(L/a)^r`: sub-width support gains a factor per vanished moment, but at the unresolved one-width scale `L asymp a` finite-order moment balancing supplies no new small parameter.

The bounded-conditioning signed route is therefore narrowed to a scale-invariant intermediate geometry with an arithmetic requirement. Many-width sign separation exports an adverse `Omega(log G)` zero reservoir; sub-Poisson transport loses the target; and finite-order local Taylor cancellation suppresses target and generic Euler leakage through the same normalized moment. The remaining regime is **one-Poisson-width local interlacing with source-specific cancellation**, where positive and negative mass overlap strongly enough to evade the separated-reservoir argument but arithmetic prime phases must cancel better than the generic transport/moment majorants while preserving natural-scale target gain.

The live theorem is whether such one-width interlacing can exploit actual von Mangoldt phases to suppress the Euler side without shrinking the target by the same factor, or whether a nonlocal geometry/increasing-order architecture can do so with its conditioning cost controlled. A claim based only on finitely many vanishing local moments is no longer an escape. An alternative route must worsen conditioning/lower-height assumptions or couple the signed sampler to the Nyman/source observable before the generic Poisson/Euler Taylor currency becomes load-bearing.

## Keep signed conservation, conditioning, boundary scale, sign-support geometry, transport length, moment order and adverse occupancy separate

Positive sampling pays the Hadamard background. Zero-mass sampling removes it but creates sign debt. Boundary approach and first-order transport combine through `Theta_G=C_G ell_G/a_G`; higher fixed-order local cancellation is priced by `Xi_r=M_r/(c a^r)`. NB-158--NB-160 show that bounded conditioning plus universal moment cancellation does not help while opposite signs remain separated by many Poisson widths. NB-161--NB-162 show that transport much finer than the Poisson width suppresses both prime-side leakage and target response. NB-163 shows the same coupling persists for every fixed finite local Taylor order.

A future sampler must therefore expose target charge, total variation, boundary gap, Jordan-support overlap/separation in Poisson units, mean optimal transport length, local moment order and normalized moment size, signed background moments, local zero population, and any genuinely arithmetic prime/Nyman-side cancellation simultaneously. Cardinality and atomicity are no longer relevant escape resources, and neither absolute minimum support distance nor a list of vanishing moments is a useful resource without normalization by the shrinking Poisson width.

## Push canonical shell discrepancy independently

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem is whether the canonical arithmetic coefficients force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate being targeted. This route remains distinct from the zero-packet Poisson budgets above.
