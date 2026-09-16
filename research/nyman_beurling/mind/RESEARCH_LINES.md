# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Resolve the one-Poisson-width interlaced signed-sampler regime

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-037-high-ordinate-zeta-bounds-cap-the-boundary-approach-tariff`.

NB-148 identifies the signed escape from positive exterior Poisson sampling: zero total sampler mass cancels the universal Hadamard logarithm but exports an equal sign debt. NB-150--NB-155 show that mesoscopic spreading, fixed-scale packets, compact signed samplers, boundary approach and sublinear vertical widening do not isolate a logarithmic target packet under sublogarithmic effective conditioning.

NB-156 crossed the macroscopic-support boundary. NB-157 showed that the leading completed-Gamma contribution is one signed log-height moment, so polynomially separated heights can cancel both total mass and the Gamma moment. NB-158--NB-159 show that any fixed finite polynomial-height atomic repair with bounded target conditioning exports a comparable negative lobe into a routine `Omega(log G)` zero reservoir.

NB-160 removes the finite-cardinality and atomicity loopholes. For an arbitrary finite signed Borel height measure with zero total mass, polynomially high support, bounded total-variation conditioning and positive/negative Jordan supports separated by a sufficiently large fixed number of Poisson widths, every infinitesimal piece of negative mass sees local zero density `Theta(log G)`. The zero-summed positive cross-talk decays like `1/Delta`, so the adverse charge remains `Omega(c_G log G)` and forces `Omega(log G)` negative-response zeros. Spreading the negative mass over growing cardinality or a continuum does not help.

NB-161 closes the opposite geometric extreme at fixed horizontal scale. If `nu=nu^+-nu^-` is zero-mass and `ell(nu)=W_1(nu^+,nu^-)/M` is the mean optimal Jordan transport length, the exterior Poisson response is bounded by total variation times `ell`; hence genuine transport collapse at bounded conditioning loses fixed target gain.

NB-162 supplies the boundary-covariant form of that statement. If the exterior gap is `a_G`, conditioning is `C_G=||nu_G||_TV/c_G`, and

`Theta_G = C_G ell(nu_G)/a_G`,

then `Theta_G` controls every Poisson target response relative to its own natural kernel height and also controls the signed Euler-product response relative to the boundary scale `c_G/a_G`. Thus absolute `ell_G->0` is not itself fatal when the Poisson width shrinks. What is fatal is **sub-Poisson transport**, `Theta_G=o(1)`: it buys excellent prime-side cancellation only by making the sampler equally invisible to the target.

NB-163 shows that imposing finitely many additional local moment cancellations does not create a second currency. If moments through order `r-1` vanish around `t_0`, the dimensionless quantity

`Xi_r = M_r(nu;t_0)/(c a^r)`

with `M_r=int |t-t_0|^r d|nu|` bounds both every normalized Poisson target response and the signed Euler response relative to its natural `c/a` boundary scale. For fixed `r`, `Xi_r=o(1)` therefore suppresses target and Euler sides together.

NB-164 closes the growing-order local-moment escape on the target side. Exact minimax duality identifies the residual target capacity after annihilating degree `<r` polynomials with the polynomial-approximation error of the scaled Poisson kernel. At any fixed number of Poisson widths that capacity decays exponentially in `r`; fixed target gain therefore requires exponentially growing conditioning, while bounded conditioning forces support to spread at least linearly in `r` measured in Poisson widths. Increasing formal moment order is not a free arithmetic resource.

NB-165 then corrects the boundary tariff itself for the **actual high-ordinate zeta source**. The absolute Euler estimate `O(V_G/a_G)` remains valid, but Cully--Hugill--Leong's uniform one-line estimate gives the stronger alternative `O(V_G log G/log log G)`. The signed conservation cost is therefore governed by

`C_G min{a_G^(-1), log G/log log G}`.

Once `a_G << log log G/log G`, moving the sampler still closer to `Re s=1` no longer increases the source-side bill at the inverse-gap rate. In that extreme boundary regime `C_G=o(log log G)` is sufficient for essentially the full target charge to reappear as adverse signed zero mass, and a fixed fraction remains within ordinate radius `O(1+C_G)`. Combined with the explicit zero-free region, the required adverse zero population still diverges.

The bounded-conditioning signed route is therefore narrowed to a scale-invariant and source-specific intermediate geometry. Many-width sign separation exports an adverse zero reservoir; sub-Poisson transport loses the target; high local moment order requires nonlocal support or exponential conditioning; and arbitrarily close boundary approach no longer supplies unbounded arithmetic leverage because the actual one-line logarithmic derivative caps the inverse-gap tariff.

The live theorem is whether **one-Poisson-width local interlacing can exploit cancellation in the actual values of `zeta'/zeta` beyond the available pointwise `log G/log log G` control while retaining target gain**, or whether a genuinely nonlocal geometry can do so with its support and conditioning costs controlled. A claim based only on boundary motion or formal moment cancellation is no longer an escape.

## Keep signed conservation, conditioning, boundary scale, sign-support geometry, transport length, moment order, high-ordinate source control and adverse occupancy separate

Positive sampling pays the Hadamard background. Zero-mass sampling removes it but creates sign debt. First-order target transport is priced by `Theta_G=C_G ell_G/a_G`; fixed-order Taylor cancellation is priced by `Xi_r=M_r/(c a^r)`; growing order pays the minimax support/conditioning tradeoff of NB-164. NB-165 adds a genuinely source-specific cap: for the global conservation remainder, the effective boundary multiplier is `min{a_G^(-1), log G/log log G}` rather than `a_G^(-1)` in every regime.

A future sampler must therefore expose target charge, total variation, boundary gap, Jordan-support overlap/separation in Poisson units, mean optimal transport length, local moment order and normalized moment size, support growth, signed background moments, the actual high-ordinate logarithmic-derivative input, local zero population, and any further arithmetic cancellation simultaneously. Cardinality and atomicity are no longer relevant escape resources, and neither absolute minimum support distance nor a list of vanishing moments is useful without the corresponding normalized destination cost.

## Push canonical shell discrepancy independently

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem is whether the canonical arithmetic coefficients force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate being targeted. This route remains distinct from the zero-packet Poisson budgets above.