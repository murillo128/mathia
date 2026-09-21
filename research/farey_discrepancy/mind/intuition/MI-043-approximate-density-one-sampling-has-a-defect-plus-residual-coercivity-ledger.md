# MI-043 — Approximate density-one sampling has a defect-plus-residual coercivity ledger

**Evidence level:** supported by [FD-242](../../findings/FD-242-density-one-approximate-sampling-is-stable-under-weighted-response-residual.md) and its proved sharpening [FD-243](../../findings/FD-243-sparse-omission-defect-improves-from-square-root-to-entropy-scale.md). This concerns unrestricted signed profiles under `|b_n|<=Cn`; it does not transfer to physical nonnegative/source-coherent profiles without a separate theorem.

Let `Y(m)` be the divisor response, `S` the sampled locations, `R(N)=|[1,N]\S|`, and define

`V_S(N)=sum_(m<=N, m,m-1 sampled) |Y(m)-Y(m-1)|/m`.

With `S_0=S union {0}`, put

`T_N={m<=N: m notin S or m-1 notin S_0}`, `rho_N=|T_N|/N`.

FD-243 sharpens the defect side of the FD-242 ledger to

`sum_(N/2<n<=N)|b_n| / sum_(N/2<n<=N)n << C rho_N log(e/rho_N) + V_S(N)/N`,

with the defect term interpreted as zero when `rho_N=0`. Since `|T_N|<=2R(N)`, the same bound holds with `eta_N=min(1,2R(N)/N)` in place of `rho_N`. Also `V_S(N)<=2Q_S(N)` for `Q_S(N)=sum_(m<=N,m in S)|Y(m)|/m`, so the sampled-amplitude version keeps the identical entropy-scale omission term.

The mechanism is the stable form of exact support localization. Möbius inversion gives `g(m)=Y(m)-Y(m-1)`. On sampled runs this increment is measured exactly by `V_S`; on `T_N`, the coefficient envelope gives `|g(m)|<=Cm sigma_-1(m)`. FD-243 replaces the old Cauchy--Schwarz estimate by an adaptive high-moment bound

`sum_(m in A) sigma_-1(m) << N delta log(e/delta)`, `delta=|A|/N`,

obtained from moments of `n/phi(n)` and Hölder with moment order `q` matched to the sparsity. The previous square-root defect was therefore a `q=2` loss, not the structural density-one scale.

The residual side does not improve in this step. Existing signed blind profiles can still have macroscopic capacity with response of linear order, so sublinear weighted sampled residual remains the robust coercive regime for the relaxed signed class. For exact sampled zeros and `R(N)=O(N^alpha)`, the new defect bound gives octave mass `O_C(N^(1+alpha) log N)`, rather than the previous square-root interpolation.

**Boundary.** The entropy factor is not claimed optimal; the next defect-side quantity is the sharp sparse-subset norm of `sigma_-1`. The coefficient envelope is load-bearing, and no positivity, finite-reservoir constraint or Euler/source coherence is used. Crossing the linear weighted-residual barrier still requires additional source structure rather than a further sharpening of omission density alone.