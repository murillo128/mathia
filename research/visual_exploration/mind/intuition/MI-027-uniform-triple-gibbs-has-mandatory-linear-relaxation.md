# MI-027 — Additive invariants give exact random-block Gibbs calibration modes

**Evidence level:** proved for uniform exact random-scan heat-bath kernels by [VIS-252](../../findings/VIS-252-uniform-triple-gibbs-linear-eigenmode.md) and generalized in [VIS-253](../../findings/VIS-253-additive-invariants-random-block-gibbs-eigenmodes.md).

For a permutation-invariant law supported on an additive level set `sum_i a(x_i)=A_0`, an exact uniform `b`-coordinate heat-bath update with exchangeable selected-label conditional has the exact eigenmodes

`g_i(x)=a(x_i)-A_0/m`,

with

`P_b g_i = rho_(m,b) g_i`,  `rho_(m,b)=(m-b)/(m-1)`.

Every contrast `a(x_i)-a(x_j)` has the same eigenvalue. Under a reversible stationary law its autocorrelation is exactly `rho_(m,b)^t`, and its integrated autocorrelation time is `(2m-b-1)/(b-1)`. This is a structural consequence of additive conservation plus uniform block scanning, not of the detailed conditional density.

The VIS-249 log-product quotient carries **two** such additive invariants under triple updates: `sum_i x_i=1` and `sum_i log x_i=lambda`. Hence for `b=3` both ordinary contrasts `x_i-x_j` and multiplicative contrasts `log x_i-log x_j` have

`rho_m=(m-3)/(m-1)`,  `tau_int=m-2`.

The second family is a stronger implementation audit because it probes the multiplicative coordinate whose conditioning removes the Dirichlet nuisance. Passing the ordinary benchmark while failing the log benchmark means the implemented kernel has not faithfully preserved the intended product-conditioned geometry.

These exact modes do not determine the full spectral gap or mixing of nonlinear observables such as `bar T`. If both benchmark families pass while `bar T` is materially slower from separated admissible starts, the excess timescale cannot be blamed on the universal additive-invariant scan mode; it must come from genuinely nonlinear conditioned geometry, another conductance bottleneck, or numerical error.
