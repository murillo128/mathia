# MI-061 — Ford damping is the Laplace dual of nested depth phase

**Evidence level:** exact synthesis from `NB-225`--`NB-228`.

At the exact-Ford scale, let `d_rho=R(1-beta)` be normalized horizontal zero depth and `Y=X/R`. Keep the entire moving-shell coefficient inside

`b_rho=m(rho)e^(iX(gamma-t))F(Hv_rho)`

and define the nested cumulative carrier

`C(D)=sum_(d_rho<=D) b_rho`.

NB-228 applies Stieltjes integration by parts to the exact residue sum and obtains

`Z_(X,H)(t)=e^(-r)[e^(-X)C(R)+Y int_0^R e^(-YD)C(D)dD]`.

The endpoint is negligible on the audited scale, so the residue is, to leading order, the Laplace transform of **one cumulative depth-phase process**. This identifies the nonseparable currency missing from NB-225--NB-227: Ford damping does not price population, depth and phase independently; it integrates their nested signed accumulation.

A concrete sufficient threshold follows immediately. If the cumulative tail from depth `D_0` obeys

`|C_(D_0)(D)| <= A_X e^((1-delta)YD)`

uniformly for some fixed `delta>0`, then its residue contribution is at most

`e^(-r) A_X [e^(-delta X)+delta^(-1)e^(-delta YD_0)]`.

Thus any exponential type strictly below `Y` forces the deep tail to decay. The matched packet controls from NB-225--NB-227 are sharp for this interface: they arrange a cumulative jump of size `~e^(YD)` at depth `D`, and its Laplace transform remains order one.

The reusable lesson is that **when a physical attenuation is exponential in a hidden depth variable, the right cancellation object may be the cumulative signed carrier dual to that attenuation, not a per-depth discrepancy bound**. A separable estimate can be defeated by moving diagonally in depth; a uniform subcritical bound on the cumulative process cannot be evaded in the same way.

**Boundary.** The Abel/Laplace identity is generic, not zeta-specific new information. The missing theorem is a zeta-specific estimate forcing the cumulative carrier below critical type without circularly reintroducing the same Euler shell through an explicit formula. The classical Landau--Gonek zero sums are neighboring structure but do not by themselves supply this moving vertical-localization plus horizontal-depth estimate. No Nyman--Beurling distance bound or RH consequence is proved here.
