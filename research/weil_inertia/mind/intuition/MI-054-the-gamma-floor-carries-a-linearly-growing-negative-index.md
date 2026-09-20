# MI-054 — The exact gamma dispersion forces a positive-density repair spectral profile

**Evidence level:** exact synthesis from WI-369--[WI-373](../../findings/WI-373-exact-digamma-dispersion-sharpens-gamma-negative-index-profile.md). This is an archimedean/operator repair barrier; it does not classify the full source-conditioned Weil form or imply anything about RH.

WI-369 decomposes the corrected odd archimedean block as `A_A+C_Gamma I=R_A>=0`. WI-371 proved a linear negative-index density by replacing the screened nonlocal kernel with its quadratic second-moment majorant, and WI-372 converted that bound into a necessary eigenvalue/singular-value profile for additive or factorized repairs.

WI-373 retains the exact bulk dispersion. If

`m(q)=Re psi(1/4+iq/2)-log pi`,

then the screened-difference symbol satisfies `d(q)-C_Gamma=m(q)` exactly. For each `0<eta<C_Gamma`, let `q_eta` be the unique positive solution of `m(q_eta)=-eta`. The corrected gamma block then obeys

`liminf_(A->infinity) iota_eta(A_A)/A >= q_eta/pi`.

At zero depth, `q_0/pi≈2.00211698`, strictly stronger than the earlier second-moment coefficient. The improvement is structural: `d(q)<M_2 q^2` for every `q>0`, so the exact digamma profile dominates the parabolic lower bound at every nonzero depth.

The additive-repair tariff is therefore the full digamma profile. If bounded self-adjoint `K_A` makes `A_A+K_A` nonnegative, then

`liminf N_A^+(t)/A >= q_t/pi`.

For positive compact repairs this gives the quantile envelope

`liminf kappa_(A,ceil(alpha A)) >= -m(pi alpha)`

for `0<alpha<q_0/pi`; factorized repairs `K_A=B_A^*B_A` inherit `s_(ceil(alpha A))(B_A)>=sqrt(-m(pi alpha))`. The corresponding Schatten lower constants are the integrals of `[-m(q)]^p` over `0<q<q_0`, not merely consequences of one threshold.

Thus source dimension, rank, total norm and even the older parabolic profile are insufficient proxies. A source mechanism reducible to additive/factorized repair must place the required positive spectrum on the actual negative bulk with the full depth dependence dictated by the archimedean digamma multiplier.

**Boundary.** Desogus's common-cut/rooted-Schur architecture is not asserted to be a uniformly bounded additive or factorized repair. It may change the admissible geometry rather than repair the gamma block after the fact. WI-373 is therefore a sharper necessary audit gate for such reductions, not a disproof of the source construction or evidence against RH.