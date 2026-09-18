# MI-044 — Full-shell finite-measure nullspace is only the universal zeta factor

**Evidence level:** exact synthesis from [PC-339](../../findings/PC-339-semiprime-null-mellin-functionals-reduce-to-prime-log-zero-interpolation.md) through [PC-343](../../findings/PC-343-full-shell-mellin-measure-kernel-is-zeta-zero-support.md). The strip-growth and Fourier-uniqueness ingredients are classical; the Mathia content is their exact placement in the complete Prime-Circle shell family.

For a finite complex Mellin-frequency measure `T`, semiprime nulls alone lead to a prime-log interpolation problem whose rigidity depends on analytic class. PC-343 shows that requiring the response to vanish on **every** shell changes the geometry qualitatively.

Divisor inversion gives, for every integer `m>=2`,

`sum_(d|m,d>1) A_d(s) = m^(1-s)-1`.

Therefore all-shell nulls force the associated interpolation transform `F_T` to vanish at every `log m`, not merely at `log p`. Gamma decay makes `F_T` holomorphic on the native strip `|Im z|<pi/2`, and after removing harmless real-direction growth its sup norm on narrower strips can blow up only polynomially as the boundary gap `delta->0`.

The integer-log zero set is too dense for any nonzero function with that boundary behavior. Under the strip-to-disk map its Blaschke lower bound is governed by `zeta(alpha)~1/(alpha-1)`, so a nonzero survivor would require

`log ||H||_infinity >= c/delta`,

i.e. essential-exponential norm blow-up. This contradicts the polynomial upper bound forced by a finite measure and Gamma decay. Hence `F_T` vanishes identically.

Differentiating then exposes the Fourier transform of the finite measure `V_sigma(t)dT(t)`. Fourier uniqueness gives

`V_sigma(t)dT(t)=0`.

For `sigma!=1`, the real zero set of `V_sigma` is exactly `{t:zeta(sigma+it)=0}`, so the entire all-shell nullspace is support on the **already present common zeta factor**. At `sigma=1`, pole cancellation makes `V_1` nonzero on the real line and the nullspace is trivial. Consequently

`L_(1,T)(n)=c Lambda(n) for all n>1  =>  T=c delta_0`.

The reusable distinction is between **analytic-class rigidity** and **observation-family completeness**. Prime-log constraints can be evaded by leaving bounded-characteristic/finite-order classes; full-shell constraints for finite measures upgrade the zero set to all integer logarithms and eliminate that escape entirely. But the closure does not create a new RH mechanism: away from `sigma=1`, the remaining kernel is precisely the universal zeta-zero support already explicit in each shell response.

**Boundary.** This is a theorem for finite Mellin-frequency measures and the full shell family. It does not classify infinite-order distributions, shell-dependent symbols, nonlinear functionals, matrix/noncommuting carriers or genuinely cross-shell geometry. Nor does it turn the inherited zeta-zero kernel into an independent spectral explanation of those zeros.
