# MI-061 — Ford damping is the Laplace dual of nested depth phase, carrier width sets the shallow scale, and global pair statistics miss sparse critical packets

**Evidence level:** exact synthesis from `NB-225`--`NB-232`.

At the exact-Ford scale, let `d_rho=R(1-beta)` be normalized horizontal zero depth and `Y=X/R`. Keep the full moving-shell coefficient inside

`b_rho=m(rho)e^(iX(gamma-t))F(Hv_rho)`

and define the nested cumulative carrier

`C(D)=sum_(d_rho<=D) b_rho`.

NB-228 applies Stieltjes integration by parts to the exact residue sum and shows that, up to a negligible endpoint, the residue is the Laplace transform of **one cumulative depth-phase process** against `e^(-YD)`. Ford damping therefore does not price population, depth and phase independently; it integrates their nested signed accumulation.

NB-229 removes the deep formal Ford interval. NB-230 retains vertical carrier width in the shallow layer. Bellotti's local zero-disk theorem gives `M_(t,H)(D) << D+J`, with `J=1+R/H`, and the same Ford weight yields

`T(D_0,D_1) << e^(-YD_0)(D_0+J+1)`.

Hence every moving depth with `YD_0-log J -> +infinity` is absolutely negligible. The active shallow window is controlled by `log(1+R/H)`, not by `log Q` alone.

NB-231 shows that this logarithmic carrier-width threshold is sharp for the currently audited information when `1 << R/H <= log Q`. A phase-aligned abstract zero packet can use `Theta(R/H)` carrier slots at `D=(log(R/H)+w)/Y`, with `w=O(1)`, while remaining compatible with the zero-free boundary, growing-density allowance, local disk count and ordinary local zero counting. Its exact signed residue stays bounded away from zero. Thus the upper and lower controls meet at the dimensionless balance `YD-log J`.

NB-232 identifies a further quantifier mismatch. The aligned packet spacing is `Theta(1/X)`, whereas the mean zero spacing is `Theta(1/Q)` and `Q/X -> infinity`. The obstruction is therefore mesoscopic rather than a close-gap anomaly. Moreover a sparse insertion set of size `A(T)` changes the standard globally weighted pair numerator by only

`O(A(T) log T + A(T)^2)`.

Choosing infinitely many transition-saturating packets with cumulative `A(T)=O(sqrt(log T) log log T)` makes that change `o(T log T)` uniformly in the pair-correlation Fourier parameter. Global Montgomery-type pair statistics can consequently remain asymptotically unchanged while the inserted packet carries order-one Ford residue at each selected height.

The missing source information must therefore act on the same three coordinates as the carrier: horizontal depth `R(1-beta)`, local window `H(gamma-t)`, and carrier phase `X(gamma-t) mod 2pi`. A density-one/global two-point theorem can average away the exceptional windows relevant to a uniform endpoint, while natural-scale gap repulsion resolves a much finer spacing than the packet uses. A viable next theorem is local and depth-conditioned, controlling the carrier-frequency phase sum on the `YD-log J=O(1)` slab, or is an equivalent arithmetic statement that forbids the packet geometry without first averaging over height.

The reusable lesson is now four-stage. **First identify the cumulative signed object dual to the physical attenuation. Second use the actual carrier to remove absolutely harmless parameter ranges. Third test sharpness with a matched control that spends the same carrier capacity. Fourth audit the quantifier and scale of any proposed external statistic: a global or finer-scale statistic need not see the sparse local configuration that matters pointwise.**

**Boundary.** NB-231--NB-232 construct matched controls, not actual zeta-zero configurations. NB-232 rules out the usual globally normalized pair-correlation information as sufficient by itself; it does not rule out short-window, depth-conditioned pair/phase theorems that essentially control the missing carrier observable. The source-side analysis still does not prove a quantitative Nyman--Beurling distance bound or RH consequence.