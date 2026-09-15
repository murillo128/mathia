# MI-024 — Exact gamma geometry gives a support floor and separated-mass tariff under complete screening

**Evidence level:** exact line-local consequence of Suzuki's gamma-plus-pole decomposition, the Fourier density-cap bathtub principle, and [WI-295](../../findings/WI-295-exact-digamma-bathtub-gives-explicit-screened-support-floor.md), strengthening the qualitative floor of WI-294

For a normalized one-signed completely screened first-crossing null mode `v>=0`, the discrete prime source vanishes on `v` and

`q_arch(v)=G(v)+P_a(v)=0`,

with strictly positive pole coupling `P_a(v)=2L_-(v)L_+(v)>0`. Hence the gamma energy must be negative.

WI-295 keeps the exact gamma multiplier

`m(z)=Re psi(1/4+iz/2)-log pi`.

It is even and strictly increasing in `|z|`. If `mu=|{v>0}|`, compact support and Cauchy--Schwarz give the Fourier power density the cap `|vhat(z)|^2/(2pi)<=mu/(2pi)`. The exact bathtub minimizer of this density-cap relaxation is therefore the saturated centered interval, yielding

`G(v) > H(mu)`,

where

`H(mu) = (mu/(2pi)) int_(-pi/mu)^(pi/mu) m(z) dz`.

`H` is continuous and strictly decreasing from `+infinity` to `m(0)<0`, so it has a unique positive zero `mu_*`. The null identity and positive pole term imply

`mu>|mu_*|`,

more precisely `mu>mu_*`, with `mu_*≈0.1760429873` only as non-load-bearing numerical orientation. Together with the exact power-of-two screening bound, every such mode satisfies

`mu_* < mu <= log 2`.

The same exact geometry controls separated components. If measurable `A,B` of the positive support are separated by distance at least `R`, then the positive `cosh((y-x)/2)` pole kernel gives

`M_1(A) M_1(B) < -H(mu)/(4 cosh(R/2))`.

Thus widely separated support pieces can coexist only if their `L^1` amplitudes become exponentially unbalanced. This is stronger than a topological support restriction: a remote satellite may preserve total measure and aperture, but it cannot carry fixed positive `L^1` mass together with another remote component as separation grows.

The remaining gap is not support measure. The null vector is normalized in `L^2`, and without an additional regularity or amplitude principle a positive-measure component can carry arbitrarily small `L^1` mass. The exact tariff therefore does not yet turn many-component screening into an `L^2` contradiction.

The reusable lesson is that preserving the one-signed null vector exposes two coupled resources absent from the unrestricted spectral relaxation: a **strict support-measure floor** and an **exponential separated-mass tariff**. Any many-component escape must satisfy both simultaneously.
