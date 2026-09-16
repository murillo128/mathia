# MI-037 — High-ordinate analyticity turns the boundary tariff into a transport budget

**Evidence level:** literature+derived synthesis from [NB-154](../../findings/NB-154-boundary-approach-amplifies-target-and-euler-response-by-the-same-poisson-width.md), [NB-160](../../findings/NB-160-separated-jordan-supports-force-adverse-zero-reservoir.md) through [NB-166](../../findings/NB-166-high-ordinate-analyticity-replaces-conditioning-by-poisson-transport.md). The high-ordinate `zeta'/zeta` estimate is external literature; the transport insertion into the signed conservation law is line-specific synthesis.

NB-154 gives the elementary boundary currency for a compact zero-mass signed sampler: absolute convergence prices the Euler side by `C_G/a_G`, where `C_G` is total-variation conditioning and `a_G` the horizontal gap from `Re s=1`. NB-165 corrects that tariff for the actual high-ordinate zeta source. Uniformly on `sigma>=1`, the verified pointwise bound `|zeta'/zeta| << log G/log log G` gives the better multiplier

`E_G=min{a_G^(-1), log G/log log G}`,

so the total-variation conservation cost is `C_G E_G`. Boundary motion stops buying inverse-gap amplification below the crossover `a_G~log log G/log G`.

NB-166 shows that total variation is still not the right final currency when the Jordan signs interlace. Analyticity converts the high-ordinate pointwise estimate into a vertical derivative bound of size `O(E_G/a_G)` by Cauchy's estimate. If `ell_G` is the mean optimal transport distance between the positive and negative Jordan parts and

`Theta_G=C_G ell_G/a_G`,

then pairing the derivative bound with an optimal Jordan coupling yields

`|int (zeta'/zeta)(1+a_G+it) dnu_G(t)| << q_G Theta_G E_G`.

The same transport treatment controls the completed Gamma/rational terms and the zero-side tails. Thus the entire signed conservation remainder is governed by `Theta_G E_G`, not by `C_G E_G`, when transport information is retained before absolute values are taken.

This is a qualitative change in the escape geometry. Arbitrarily large total variation is not itself useful if the two signs are interlaced finely enough that `Theta_G` stays small. For a logarithmic target packet, essentially full adverse debt is exported whenever

`Theta_G E_G=o(log G)`.

In the extreme boundary layer this becomes `Theta_G=o(log log G)`, independent of `C_G`. The adverse mass can also be localized on radius `O(1+sqrt(a_G Theta_G))`, improving the older `O(1+C_G)` localization, and the explicit zero-free region then forces a divergent adverse-zero population under the same conservation hypothesis.

The reusable principle is stronger than “use the best pointwise source estimate.” **Apply source regularity before destroying the signed geometry.** A pointwise analytic bound plus Cauchy differentiation can turn Wasserstein/Jordan transport into the correct source norm, replacing a large total-variation bill by a scale-invariant transport bill. The order of inequalities matters: taking absolute values too early loses the cancellation the source theorem can actually see.

For Nyman--Beurling, the surviving one-width regime must therefore beat a transport-aware high-ordinate conservation law, not merely tolerate large `C_G`. A successful sampler needs target gain while making the actual values of `zeta'/zeta` cancel more strongly than the verified Lipschitz/pointwise bounds predict, or must move to a nonlocal geometry whose transport and support costs are separately controlled.

**Boundary.** The derivative estimate pays one factor `1/a_G` and uses holomorphy to the right of the one-line. The result is an upper/conservation theorem, not an optimality statement for actual high-ordinate cancellation. The target packet remains conditional and the argument does not imply RH. Growing vertical support or a different horizontal geometry requires a fresh analytic audit.
