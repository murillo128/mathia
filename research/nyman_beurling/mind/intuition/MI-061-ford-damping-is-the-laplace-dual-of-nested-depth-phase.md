# MI-061 — Ford damping is the Laplace dual of nested depth phase, and carrier width sets the sharp shallow depth scale

**Evidence level:** exact synthesis from `NB-225`--`NB-231`.

At the exact-Ford scale, let `d_rho=R(1-beta)` be normalized horizontal zero depth and `Y=X/R`. Keep the full moving-shell coefficient inside

`b_rho=m(rho)e^(iX(gamma-t))F(Hv_rho)`

and define the nested cumulative carrier

`C(D)=sum_(d_rho<=D) b_rho`.

NB-228 applies Stieltjes integration by parts to the exact residue sum and shows that, up to a negligible endpoint, the residue is the Laplace transform of **one cumulative depth-phase process** against `e^(-YD)`. Ford damping therefore does not price population, depth and phase independently; it integrates their nested signed accumulation.

NB-229 removes the deep formal Ford interval. Smooth vertical carrier decay plus the classical zero count yields an absolute `Qe^(-YD_0)` tail, so depths beyond `O(log Q)` are harmless before any new zeta-specific phase or density theorem is used.

NB-230 retains the vertical carrier width inside that shallow layer. Bellotti's local zero-disk theorem gives

`M_(t,H)(D) << D + J`, with `J=1+R/H`,

throughout its admissible range, and the same Ford weight yields

`T(D_0,D_1) << e^(-Y D_0)(D_0+J+1)`.

Hence every moving depth with `Y D_0-log J -> +infinity` is absolutely negligible. The active shallow window is controlled by `log(1+R/H)`, not by `log Q` alone.

NB-231 shows that this logarithmic carrier-width threshold is sharp for the currently audited information when `1 << R/H <= log Q`. A phase-aligned abstract zero packet can use `Theta(R/H)` carrier slots at

`D=(log(R/H)+w)/Y`, with `w=O(1)`,

while remaining compatible with the Vinogradov--Korobov zero-free boundary, Bellotti's growing-density allowance, Bellotti's local disk count and ordinary local zero counting. Its exact signed residue stays bounded away from zero. Thus the upper and lower controls meet at the dimensionless balance

`Y D - log J`.

For this information set, `Y D-log J -> +infinity` kills the residue, while `Y D-log J=O(1)` can still carry order-one coherent mass. The additive divergence in NB-230 is therefore not a proof artifact in the controlled capacity regime. A further source-side theorem must attack the bounded transition layer itself by coupling depth to phase or spacing for the actual zeta zeros; improving estimates only beyond that layer targets a region already harmless.

The reusable lesson is three-stage. **First identify the cumulative signed object dual to the physical attenuation. Second use the actual carrier to remove parameter ranges that are absolutely harmless. Third test sharpness with a matched control that spends the same carrier capacity before asking for stronger arithmetic input.** A theorem on a larger formal domain can be much harder while adding no destination leverage.

**Boundary.** NB-231 is an abstract matched-packet method boundary, not evidence that the actual zeta zeros realize the packet. Its sharpness statement is deliberately restricted to `1 << R/H <= log Q`; much narrower shells require a separate population audit. The source-side residue analysis still does not prove a quantitative Nyman--Beurling distance bound or RH consequence.