# MI-061 — Ford damping is the Laplace dual of nested depth phase, and the critical carrier statistic is marked rather than marginal

**Evidence level:** exact synthesis from `NB-225`--`NB-233`.

At the exact-Ford scale, let `d_rho=R(1-beta)` be normalized horizontal zero depth and `Y=X/R`. Keep the full moving-shell coefficient inside

`b_rho=m(rho)e^(iX(gamma-t))F(Hv_rho)`

and define the nested cumulative carrier

`C(D)=sum_(d_rho<=D) b_rho`.

NB-228 applies Stieltjes integration by parts to the exact residue sum and shows that, up to a negligible endpoint, the residue is the Laplace transform of **one cumulative depth-phase process** against `e^(-YD)`. Ford damping therefore does not price population, depth and phase independently; it integrates their nested signed accumulation.

NB-229 removes the deep formal Ford interval. NB-230 retains vertical carrier width in the shallow layer. Bellotti's local zero-disk theorem gives `M_(t,H)(D) << D+J`, with `J=1+R/H`, and the same Ford weight yields

`T(D_0,D_1) << e^(-YD_0)(D_0+J+1)`.

Hence every moving depth with `YD_0-log J -> +infinity` is absolutely negligible. The active shallow window is controlled by `log(1+R/H)`, not by `log Q` alone.

NB-231 shows that this logarithmic carrier-width threshold is sharp for the currently audited information when `1 << R/H <= log Q`. A phase-aligned abstract zero packet can use `Theta(R/H)` carrier slots at `D=(log(R/H)+w)/Y`, with `w=O(1)`, while remaining compatible with the zero-free boundary, growing-density allowance, local disk count and ordinary local zero counting. Its exact signed residue stays bounded away from zero. Thus the upper and lower controls meet at the dimensionless balance `YD-log J`.

NB-232 identifies a quantifier mismatch. The aligned packet spacing is `Theta(1/X)`, whereas the mean zero spacing is `Theta(1/Q)` and `Q/X -> infinity`. A sparse insertion set can change the globally normalized Montgomery pair statistic by `o(1)` while preserving order-one Ford residue at selected heights. Global two-point information can therefore average away exactly the exceptional windows relevant to a uniform endpoint.

NB-233 strengthens this from a global-versus-local mismatch to a **marked-versus-marginal** mismatch. A carrier packet can have phases equal to the complete roots of unity, so every nontrivial unweighted Fourier mode below the packet size vanishes exactly. If normalized Ford depth is correlated with phase through `YD-log J=w-epsilon cos(theta)`, then the Ford mark `e^(-(YD-log J))` turns the first weighted Fourier coefficient into a nonzero quantity of size `delta e^(-w)(epsilon/2+O(epsilon^2))`; the exact profiled residue remains bounded away from zero. Perfect unweighted phase equidistribution in the correct short window is therefore still the wrong projection.

The missing source information must act on the same joint object as the residue. In the transition slab `YD-log J=O(1)`, a natural target is the first carrier harmonic of the depth-marked empirical measure, with the bounded profile factor retained. Equivalently, one needs a zeta-specific decorrelation theorem between normalized horizontal depth and carrier phase inside each relevant `1/H` window. Pure depth density fails by NB-231, global pair statistics fail by NB-232, and unweighted local phase discrepancy fails by NB-233.

The reusable lesson is now five-stage. **First identify the cumulative signed object dual to the physical attenuation. Second use the actual carrier to remove absolutely harmless parameter ranges. Third test sharpness with a matched control that spends the same carrier capacity. Fourth audit the quantifier and scale of any proposed external statistic. Fifth preserve the marks that the physical attenuation actually applies before projecting to phase or population marginals.** A statistic can be local and frequency-matched yet still be blind because it forgot the source weight consumed downstream.

**Boundary.** NB-231--NB-233 construct matched controls, not actual zeta-zero configurations. NB-233 does not rule out phase control in thin depth slices or a direct estimate for the depth-weighted carrier sum; those are precisely the surviving targets. The source-side analysis still does not prove a quantitative Nyman--Beurling distance bound or RH consequence.