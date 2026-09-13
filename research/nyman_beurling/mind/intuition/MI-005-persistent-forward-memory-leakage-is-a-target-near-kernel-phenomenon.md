# MI-005 — Stable-tail diagnostics are governed by finite prediction error, not qualitative outerness alone

**Evidence level:** supported by NB-063--NB-082. The continuation, prediction, branching, q-adic and variable-horizon identities are exact; NB-082 gives an exact stationary branch-filter classification in terms of finite prediction error. No arithmetic criterion closing the Nyman stable tail is established.

NB-074--NB-079 write the uncancelled continuation charge as a refinement ledger and remove the universal common prediction mode. A nonzero stable tail forces the residual charge to diverge on every fixed-ratio refinement ray, while boundedness on one unbounded schedule excludes such a tail.

NB-080 shows why a shallow converse fails: a boundedly invertible outer source with zero stable tail can still pay a linear finite-horizon boundary cost. NB-081 makes future enlargement an exact screening operation and computes two first-order calibrations: geometric decay for `1-rho z`, `0<rho<1`, and only harmonic decay for the outer boundary filter `1-z`.

NB-082 identifies the general invariant behind those examples. For a stationary branch filter `D_j^(psi)=psi(V_m)e_j`, define

`epsilon_L(psi)=inf_{deg p<=L, p(0)=1} ||psi p||_(H^2)^2`

and the normalized finite-prediction excess

`a_(psi,L)=epsilon_L(psi)/|psi(0)|^2-1`.

At the depth-`L` horizon `N=m^L R-1`, a fixed positive fraction of prefix indices realizes this same scalar prediction defect, and the complete prediction-volume charge satisfies

`K_(m,R,L) log(1+a_(psi,L)) <= J_(R,N) <= (R-1) log(1+a_(psi,L))`,

with `K_(m,R,L)/R -> 1-1/m` uniformly in `L`. For outer `psi` and `L->infinity`, this is exactly `J asymp_m R a_(psi,L)`. Hence bounded screening is equivalent to `R a_(psi,L)=O(1)` and vanishing screening to `R a_(psi,L)->0`.

Inner--outer factorization gives the infinite-depth classification: `a_(psi,L)` decreases to `|theta(0)|^(-2)-1`, so it tends to zero exactly when `psi` is outer. Qualitative outerness therefore answers only whether arbitrarily deep prediction can eventually remove the boundary layer. The amount of future needed is determined by the **rate** of finite cyclic prediction. The earlier models are calibrations: `1-rho z` has geometric prediction excess and needs logarithmic depth, while `1-z` has `a_L=1/(L+1)` and needs depth of order `R` merely for bounded charge.

The reusable principle is sharper than a generic conditioning warning: a finite-horizon continuation residual is meaningful only after pricing the source-specific finite-prediction excess at the depth actually used. A source may be perfectly outer and have zero stable tail while remaining a false positive until its prediction error has fallen to the `1/R` scale.

**Boundary.** NB-082 is exact for stationary scalar filters of the branching isometry. The actual Nyman innovations are nonstationary shrinking-cell outputs, and no theorem identifies their finite-prediction profile with one fixed Hardy filter. The remaining arithmetic work is to derive an analogue of `a_(psi,L)` with enough decay after an affordable future depth, or to find a certificate that avoids this boundary-layer payment altogether.
