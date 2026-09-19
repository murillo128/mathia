# MI-061 — Ford damping is the Laplace dual of nested depth phase, and carrier width sets the remaining shallow depth scale

**Evidence level:** exact synthesis from `NB-225`--`NB-230`.

At the exact-Ford scale, let `d_rho=R(1-beta)` be normalized horizontal zero depth and `Y=X/R`. Keep the full moving-shell coefficient inside

`b_rho=m(rho)e^(iX(gamma-t))F(Hv_rho)`

and define the nested cumulative carrier

`C(D)=sum_(d_rho<=D) b_rho`.

NB-228 applies Stieltjes integration by parts to the exact residue sum and shows that, up to a negligible endpoint, the residue is the Laplace transform of **one cumulative depth-phase process** against `e^(-YD)`. Ford damping therefore does not price population, depth and phase independently; it integrates their nested signed accumulation.

NB-229 then removes the deep formal Ford interval. Smooth vertical carrier decay plus the classical zero count yields an absolute `Qe^(-YD_0)` tail, so depths beyond `O(log Q)` are harmless before any new zeta-specific phase or density theorem is used.

NB-230 retains the vertical carrier width inside that shallow layer. Bellotti's local zero-disk theorem already gives, throughout its admissible range,

`M_(t,H)(D) << D + J`, with `J=1+R/H`,

for the absolute carrier-weighted zero population. Stieltjes summation with the same Ford weight then gives

`T(D_0,D_1) << e^(-Y D_0)(D_0+J+1)`.

Thus every moving depth with

`Y D_0-log J -> +infinity`

is already absolutely negligible. The active shallow window is not generically `1<<D<<log Q`; inside the Bellotti range it compresses to

`1 << D \lesssim (1/Y) log(1+R/H)`.

The effect depends on width. If `H` is comparable with `R`, `J=O(1)` and every moving Bellotti depth is harmless. If `R/H` is polylogarithmic, the active depth is only logarithmic in `log Q`. If `log(R/H)=Theta(log Q)`, as for very narrow shells, the width cutoff returns to the coarse `Theta(log Q)` scale and no asymptotic compression follows.

The earlier matched packets explain why this logarithmic width law is the correct currency rather than an artifact of absolute values. They place coherent mass at depths proportional to `log M`, where available vertical population pays the Ford factor. Positive and negative sides therefore meet at the balance

`J ≈ e^(Y D)`.

Inside the resulting width-dependent window, a new theorem must remain genuinely joint: improve the local population/depth relation beyond `D+R/H`, control the signed cumulative carrier `C(D)` using actual zeta phase, or prove that the abstract packet geometry cannot occur for the true zeros. A global zero-density improvement outside this window is solving a region already made subcritical by existing local counts and the physical carrier.

The reusable lesson is three-stage. **First identify the cumulative signed object dual to the physical attenuation. Second use the actual carrier to remove parameter ranges that are absolutely harmless. Third express the remaining danger in the carrier's own capacity variable before asking for cancellation.** A theorem on a larger formal domain can be much harder while adding no destination leverage.

**Boundary.** Bellotti's local estimate is used only in its proved range; a possible `Theta(log Q)` transition band between that range and the coarse NB-229 cutoff remains open. The packet controls do not prove sharpness for every extremely narrow shell. The Abel/Laplace and width-localization steps are largely generic once the zeta-specific local count is supplied. No quantitative Nyman--Beurling distance bound or RH consequence is proved.