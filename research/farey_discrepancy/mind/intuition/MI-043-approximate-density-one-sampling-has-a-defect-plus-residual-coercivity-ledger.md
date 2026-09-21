# MI-043 — Approximate density-one sampling has a defect-plus-residual coercivity ledger

**Evidence level:** supported by [FD-242](../../findings/FD-242-density-one-approximate-sampling-is-stable-under-weighted-response-residual.md), with the omission side sharpened by [FD-243](../../findings/FD-243-sparse-omission-defect-improves-from-square-root-to-entropy-scale.md) and [FD-244](../../findings/FD-244-sparse-reciprocal-divisor-mass-has-sharp-double-logarithmic-density-scale.md). This concerns unrestricted signed profiles under `|b_n|<=Cn`; it does not transfer to physical nonnegative/source-coherent profiles without a separate theorem.

Let `Y(m)` be the divisor response, `S` the sampled locations, `R(N)=|[1,N]\S|`, and define

`V_S(N)=sum_(m<=N, m,m-1 sampled) |Y(m)-Y(m-1)|/m`.

With `S_0=S union {0}`, put `T_N={m<=N: m notin S or m-1 notin S_0}` and `rho_N=|T_N|/N`. FD-244 proves the sharp sparse-weight scale

`sum_(m in A) sigma_-1(m) << N delta log(e+log(1/delta))`, `delta=|A|/N`,

and matching lower bounds up to constants along primorial densities. Transferred through the exact inversion ledger, this gives

`sum_(N/2<n<=N)|b_n| / sum_(N/2<n<=N)n << C rho_N log(e+log(1/rho_N)) + V_S(N)/N`,

with the defect term zero when `rho_N=0`. Since `|T_N|<=2R(N)`, the same form holds with `eta_N=min(1,2R(N)/N)`, and `V_S(N)<=2Q_S(N)` gives the corresponding sampled-amplitude version.

The mechanism is stable support localization. Möbius inversion gives `g(m)=Y(m)-Y(m-1)`. On sampled runs this increment is measured by `V_S`; on the defect set the coefficient envelope bounds it by `Cm sigma_-1(m)`. The square-root and entropy defects of FD-242--FD-243 were moment-method losses: the true arbitrary sparse reciprocal-divisor mass grows only on the `delta log log(1/delta)` scale, up to the regularization above.

This sharp sparse-set norm is still not automatically the sharp **sampling** defect, because exact missing response values generate paired adjacent-difference columns rather than arbitrary sparse increments. FD-245 proves that distinction is decisive for a bounded number of exact omissions; that finite-defect geometry is recorded separately in MI-044.

**Boundary.** The weighted-residual term is unchanged, the coefficient envelope is load-bearing, and no positivity, finite-reservoir constraint or Euler/source coherence is used. Crossing the linear residual barrier remains a source-structure problem. For growing exact omission sets, the sharp interpolation between the arbitrary sparse `delta log log(1/delta)` bound and the finite triangular geometry is not supplied by FD-244 alone.