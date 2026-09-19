# MI-061 — Ford damping is the Laplace dual of nested depth phase, but smooth localization leaves only a shallow active layer

**Evidence level:** exact synthesis from `NB-225`--`NB-229`.

At the exact-Ford scale, let `d_rho=R(1-beta)` be normalized horizontal zero depth and `Y=X/R`. Keep the entire moving-shell coefficient inside

`b_rho=m(rho)e^(iX(gamma-t))F(Hv_rho)`

and define the nested cumulative carrier

`C(D)=sum_(d_rho<=D) b_rho`.

NB-228 applies Stieltjes integration by parts to the exact residue sum and obtains

`Z_(X,H)(t)=e^(-r)[e^(-X)C(R)+Y int_0^R e^(-YD)C(D)dD]`.

The endpoint is negligible on the audited scale, so the residue is, to leading order, the Laplace transform of **one cumulative depth-phase process**. This identifies the nonseparable currency missing from NB-225--NB-227: Ford damping does not price population, depth and phase independently; it integrates their nested signed accumulation.

NB-229 then shows that the formal depth interval is much larger than the physically active one. The smooth shell transform has Schwartz decay in ordinate, and the classical local zero count gives

`sum_rho m(rho)|F(Hv_rho)| << Q`.

Consequently the contribution from depths `d_rho>=D_0` satisfies

`|Z_(d>=D_0)| << Q e^(-Y D_0)`.

Writing `L=log Q`, every depth beyond `(L+omega(1))/Y` is absolutely `o(1)`, before using any zeta-specific density or phase cancellation. Thus the exact-Ford problem is not a cumulative-control theorem on all `0<=D<=R`; the live interval collapses to `D=O(L)`, with the genuinely delicate moving regime `1<<D<<L`.

The cumulative-type criterion from NB-228 remains useful inside that active layer. A tail bound of the form

`|C_(D_0)(D)| <= A_X e^((1-delta)YD)`

forces its Laplace contribution to decay, while the matched controls NB-225--NB-227 attain the critical type `e^(YD)`. But NB-229 changes where such a theorem is needed: deep Ford packets are already killed by carrier localization, so the missing arithmetic input only needs the moving shallow regime.

The prior-art mismatch becomes correspondingly precise. Global zero-density estimates with an `eta^(3/2)` exponent have the right Ford scaling but published logarithmic/fixed-parameter losses dominate when `D=o(L)`; log-free linear-`eta` density has no such prefactor but pays too much in the Ford exponent. The useful target is a local/carrier-weighted/phase-sensitive estimate uniform for `eta=D/R`, `1<<D<<L`, or a direct bound on `C(D)` there.

The reusable lesson is two-stage. **First identify the cumulative signed object dual to the physical attenuation; then use the actual carrier to remove depth ranges that are absolutely harmless before asking for cancellation.** A theorem stated on the full formal parameter range can be much harder than the destination actually requires.

**Boundary.** The Abel/Laplace identity and the absolute `Qe^(-YD_0)` tail localization are largely generic spectral geometry, not zeta-specific new cancellation. The remaining shallow theorem must use actual zeta information and avoid circularly reintroducing the same Euler shell. No Nyman--Beurling distance bound or RH consequence is proved here.
