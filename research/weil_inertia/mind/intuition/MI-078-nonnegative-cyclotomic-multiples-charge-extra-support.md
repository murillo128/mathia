# MI-078 — Nonnegative cyclotomic multiples can charge an extra Fourier support cell

**Evidence level:** exact finite-grid reduction and Wang-class criterion in [WI-452](../../findings/WI-452-commensurate-cyclotomic-positive-support-gap.md), extending the two-grid formula [WI-451](../../findings/WI-451-rational-fourier-lattice-common-grid-support-rebate.md) and [WI-450](../../findings/WI-450-sharp-simultaneous-reciprocal-lattice-support-budget.md).

Prescribe `fhat(k/(m h))=0` for each nonzero integer `k` and each `m` in a finite set `M` of positive integers, with `int f=1`. Put
`Q_M(z)=lcm_(m in M)(1+z+...+z^(m-1))`, `D=deg Q_M` and `d_+(Q_M)=min{deg P: 0!=P in R[z], Q_M|P, all coefficients(P)>=0}`.
Periodization at each residue `x mod h` forces the cell polynomial `A_x(z)=sum_j f(x+jh)z^j` to be divisible by `Q_M`. Signed densities need at least `D+1` cells; nonnegative densities need `d_++1`. Normalized step functions attain the bounds, so the sharp **enclosing-interval** lengths are `(D+1)h` and `(d_++1)h`. Superflat smoothing makes Wang's even `f=eta^2` class feasible iff `(d_++1)h<lambda`.

For `M={12,15,20,22,33}`, the cyclotomic product has `D=75` but negative coefficients, whereas `(1+z)Q_M(z)` is nonnegative and has degree 76. Hence `d_+=76`, and nonnegativity raises minimal length from `76h` to `77h`. Two-grid families have `d_+=D`; their common-grid overlap rebate does **not** extend as a complete positivity criterion to arbitrary finite families.

The result concerns artificially prescribed exact Fourier-zero lattices and enclosing interval length, not support measure or a zeta-sourced lattice. It supplies no test function whose zeros are forced by actual zeta ordinates and no consequence for RH.
