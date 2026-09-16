# MI-027 — Uniform triple Gibbs has a mandatory linear relaxation scale

**Evidence level:** proved for the exact uniform random-scan heat-bath kernel by [VIS-252](../../findings/VIS-252-uniform-triple-gibbs-linear-eigenmode.md).

On every regular non-singleton symmetric log-product level, let `P` be the exact three-coordinate Gibbs operator and `g_i(x)=x_i-1/m`. Then

`P g_i = rho_m g_i`, with `rho_m=(m-3)/(m-1)`.

Every coordinate contrast `x_i-x_j` is therefore an exact eigenfunction with the same eigenvalue. This identity is independent of the conditioned log-product level `lambda` and of the detailed one-dimensional block-fibre density; it comes only from uniform triple selection, block-mass preservation and exchangeability of the exact conditional.

Consequently the reversible chain has

`gap(P) <= 2/(m-1)`,

and at stationarity every nondegenerate coordinate contrast obeys

`Corr(f(X_0),f(X_t)) = rho_m^t`,

with integrated autocorrelation time `tau_int=m-2` when time is measured in individual triple updates. Raw triple scanning therefore has an unavoidable linear `Theta(m)` relaxation benchmark even before any nonlinear occupancy statistic is considered.

This is an implementation and interpretation gate, not a full mixing theorem. The spectral-gap inequality need not be sharp, and `bar T` or another collective observable may have a slower mode. Passing the exact `rho_m^t` benchmark only removes the trivial uniform-scan refresh rate as an explanation of additional slowdown; failure to pass it means the sampler is not yet qualified. If the benchmark passes while `bar T` remains much slower, the unresolved bottleneck is genuinely nonlinear conditioned geometry, another conductance cut, or numerical error rather than dominant-label trapping.
