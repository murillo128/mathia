# MI-080 — Finite boundary repair is exactly Hardy zero-sampling geometry

**Evidence level:** exact finite-boundary and reproducing-kernel synthesis from [NB-279](../../findings/NB-279-finite-boundary-repair-collapses-to-hardy-zero-sampling.md), refining the interior-current obstruction of MI-079.

For every finite legal Nyman source

`N[P](s)=zeta(s)/s (P(s)-P(1))`

with residual `r_P(s)=1/s-N[P](s)`, every nonzero zeta zero `rho` forces the exact value

`r_P(rho)=1/rho`.

Thus a finite boundary formula can see the zero divisor without asking the finite source itself to develop poles. If `Omega` avoids `s=1` and has no zero on its boundary,

`(1/(2 pi i)) integral_(partial Omega) q(s) s zeta'(s)/zeta(s) r_P(s) ds = sum_(rho in Omega) m(rho) q(rho)`

for every holomorphic weight `q`. The singularity has moved into the **dual test weight** `zeta'/zeta`; the finite residual remains holomorphic, so NB-278's interior-current obstruction is not bypassed.

Pricing this identity in `H^2(C_(1/2))` removes the apparent extra freedom. For distinct zeros `rho_j`, the evaluation kernels have Gram matrix

`G_(jk)=1/(rho_j+conj(rho_k)-1)`

and the forced data vector is `v_j=1/rho_j`. Every finite residual therefore satisfies the exact interpolation lower bound

`||r_P||_(H^2)^2 >= v* G^(-1) v`.

Optimizing the weighted contour identity over holomorphic `q` gives the same dual problem, not a stronger linear certificate. A single high zero already yields only `||r_P|| >= sqrt(2 Re(rho)-1)/|rho|`; any order-one Ford-scale obstruction must therefore come from the inverse conditioning of the **multi-zero evaluation Gram**, not from zero counting or the residue identity alone.

The boundary route is consequently legal but not a new arithmetic channel. Its discriminating currency is `v*G^(-1)v`: many zero constraints help only when their Hardy evaluation kernels are sufficiently independent. This is target-side zero-sampling geometry and must not be conflated with the source-shell inverse Gram of NB-271.

**Boundary.** NB-279 does not prove that the Ford-scale zero Gram has an order-one inverse floor, does not establish RH or a Nyman lower bound beyond the exact interpolation inequality, and does not invalidate higher-jet constraints at multiple zeros. It closes only the hope that a finite contour identity, by itself, supplies coercivity beyond the classical Hardy point-evaluation geometry.