# MI-035 — Jordan transport and finite local moments must be measured in Poisson widths near the boundary

**Evidence level:** exact synthesis from [NB-160](../../findings/NB-160-continuous-separated-jordan-samplers-still-export-an-adverse-zero-reservoir.md), [NB-161](../../findings/NB-161-collapsing-jordan-transport-forces-conditioning-blowup.md), [NB-162](../../findings/NB-162-poisson-width-transport-controls-target-and-signed-euler-leakage.md), and [NB-163](../../findings/NB-163-finite-order-moment-balancing-shares-one-target-euler-boundary-currency.md), using optimal-transport/Lipschitz bounds, finite-order Taylor remainders and the absolutely convergent Euler series on `Re s>1`.

After zero total mass removes the universal Hadamard background, opposite signs cannot be collapsed for free. For a zero-mass signed height measure `nu=nu^+-nu^-`, let `M=nu^+(R)=nu^-(R)`, `V=||nu||_TV=2M`, and define the mean optimal Jordan transport length

`ell(nu)=W_1(nu^+,nu^-)/M`.

NB-161 showed at fixed horizontal offset that target response is bounded by total variation times `ell`, so transport collapse forces conditioning blowup. NB-162 identifies the correct invariant when the exterior sampler itself approaches `Re s=1`. If `a` is the boundary gap, `c` the positive reference mass and `C=V/c`, define

`Theta = C ell/a`.

For every actual zero, whose Poisson width `x` satisfies `x>=a`, the normalized target response is `O(Theta)`. The same `Theta` controls the signed Euler-product response relative to its natural boundary scale `c/a`. Thus sub-Poisson transport `Theta=o(1)` suppresses **both** nuisance Euler leakage and target signal. A bounded-conditioning sampler retaining a fixed fraction of natural target gain must transport opposite signs across at least a constant fraction of a Poisson width.

NB-163 shows that higher finite-order local cancellation obeys the same structural law. If the signed sampler has vanishing centered moments through order `r-1`, define

`Xi_r = M_r(nu;t_0)/(c a^r)`,

where `M_r=int |t-t_0|^r d|nu|`. The order-`r` Taylor remainder gives two parallel bounds: every exterior Poisson target response is `O((c/x) Xi_r (a/x)^r)`, and the signed Euler response is `O((c/a) Xi_r)` for fixed `r`. Therefore `Xi_r=o(1)` cannot be used to cancel the Euler side while keeping natural-scale target visibility. If the support radius is `L`, then `Xi_r<=C(L/a)^r`; each fixed vanished moment buys another factor only in the already sub-width regime `L<a`.

This extends the first-order transport principle without replacing it. `Theta` uses the optimal Jordan coupling and is sharper than a prescribed-center first moment. `Xi_r` is the correct generic currency once exact higher moments are imposed. At one Poisson width `L asymp a`, finite `r` gives no automatic small parameter. Increasing atom count, sign changes or a finite number of vanishing moments therefore does not by itself solve the unresolved interlaced regime.

Combined with NB-160, the geometry is now narrow. Many-width sign separation exports an `Omega(log G)` adverse-zero reservoir. Sub-Poisson transport becomes target-invisible. Fixed-order local moment balancing at one width cannot generically improve prime cancellation relative to target visibility because the first uncontrolled normalized moment prices both sides. The surviving bounded-cost route must exploit **source-specific arithmetic cancellation** in the actual von Mangoldt phases beyond these absolute-value/Taylor bounds, use genuinely nonlocal geometry, or enter an increasing-order regime whose conditioning and moment growth are themselves controlled.

The reusable audit is to normalize every proposed cancellation scale by the Poisson width consumed by the target. Absolute transport length, support diameter and raw moment size are not invariant currencies near the boundary. After normalization, ask whether the same quantity bounds both the desired target and the nuisance Euler channel. If it does, shrinking that quantity is not selective leverage.

**Boundary.** NB-162 does not close `Theta=Theta(1)`, and NB-163 does not prove that one-width finite-moment interlacing fails. NB-163 is a generic absolute-value obstruction for each fixed finite order `r`; it does not control `r=r(a)->infinity` without uniform estimates for the Taylor/Euler constants and conditioning cost. Zeta-specific phase cancellation may beat the generic Euler majorant while preserving target response, and proving such cancellation would be genuinely new arithmetic input. The results also permit fine absolute transport when the Poisson width shrinks at the same rate.
