# MI-047 — Euler--Wiener acquisition prices the non-Hilbert scalar escape

**Evidence level:** exact/literature-backed synthesis from [NB-176](../../findings/NB-176-euler-weighted-fourier-fingerprints-certify-source-complexity.md) through [NB-182](../../findings/NB-182-euler-wiener-acquisition-prices-non-hilbert-phase-codes.md).

NB-181 shows that retaining the actual Euler amplitudes inside the natural feature Hilbert space blocks a growing Hadamard-scale phase code at bounded acquisition norm. The genuine scalar Euler readout is outside that Hilbert dual because its phase vector is not `ell^2`; absolute convergence of `-zeta'/zeta` in `Re s>1` supplies a different, `ell^1`-type topology.

NB-182 prices that exact escape instead of treating it as unbounded freedom. At width `a`, charge each Euler character `lambda=log n` by its capped-Poisson Lipschitz cost `M_a(lambda)=max{2,a lambda}` and define

`W(a)=sum_(n>=2) Lambda(n)n^(-1-a) M_a(log n)`.

The pole expansion gives `W(a) asymp 1/a`. After normalization by `W(a)`, the genuine scalar Euler kernel is literally a convex combination of unit capped-transport characters. A height evaluation has unit Fourier--Stieltjes acquisition cost, and a finite mixture of heights has cost equal to the total variation of its mixing measure.

This yields a nuclear factorization that does not use Hilbert square summability. If `N` templates are tested against `K` height-mixture acquisitions with RMS total-variation gain `G`, the response matrix satisfies

`||A||_* <= X sqrt(NK) G`.

Therefore an `N x N` response with all singular values of order `X sqrt N` forces `G=Omega(sqrt N)`. Unit-TV mixtures of genuine scalar Euler translates certify only `O(X^2)` coordinatewise complexity, independently of how many heights are used. The non-Hilbert phase functional is source-natural, but it is not free.

NB-182 also identifies what high-ordinate arithmetic cancellation buys relative to this absolute-convergence baseline. With the uniform source norm

`H_T=min{1/a, log T/log log T}`,

the gain over the Wiener budget is `kappa_T asymp 1/(a H_T)`. Matching the full generic Poisson-packing dimension `N asymp 1/a` at fixed-fraction Hadamard strength requires `a H_T^2=O(1)`. In the one-line-capped regime this narrows to

`a lesssim (log log T/log T)^2`.

Above that square crossover, a full packing-rank arithmetic phase code cannot be justified by the known uniform one-line bound alone; it would require additional height-specific cancellation, and that extra gain must itself be charged.

The reusable lesson is that changing acquisition topology can remove one obstruction while exposing another quantitative currency. Hilbert norm is not canonical merely because it is convenient, but neither is an `ell^1`/Wiener source functional a loophole: once its absolute source exposure and mixing gain are normalized, generic dense coding again has a `sqrt N` tariff. A source-selective certificate must beat the matched Poisson geometry using cancellation or structure that survives this source-faithful normalization.

**Boundary.** The Wiener budget is a representation-level absolute-convergence control, not a theorem that it is the optimal arithmetic normalization at every selected height. The `a H_T^2` crossover uses the current uniform high-ordinate bound; special height sets may have stronger cancellation. NB-182 does not construct such a set, does not remove the ultra-thin regime, and does not connect a surviving source code directly to global Nyman approximation. Its durable content is the finite tariff on the exact non-Hilbert scalar readout left open by NB-181.