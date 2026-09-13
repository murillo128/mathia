# MI-013 — Autocorrelation shell energy remains dilute through a growing collision window

**Evidence level:** exact for the autocorrelation-taper subclass through [VIS-203](../../findings/VIS-203-autocorrelation-tapers-make-exact-difference-shells-noncancelling.md), VIS-204--VIS-206, and the growing-window extension [VIS-207](../../findings/VIS-207-growing-window-pair-crowding-bound.md). The limiting window, prime/prime cancellation scale and full sinc-weighted intermediate-shell sum remain open.

For a shifted autocorrelation taper the frequency coefficients share a linear phase, so exact-difference shell amplitudes are nonnegative. With coefficient-energy probability `nu` and normalized collision width `A`, VIS-205 reduces normalized dangerous shell energy to the two-sample close-pair probability `Q(A)` up to a factor four as long as the shell remains in the noncancelling determinant regime.

VIS-206 proved `Q(A)->0` for fixed `A`. VIS-207 shows the mechanism is genuinely uniform over a widening family. If `0<=alpha<1/2` and

`H A^(2+4 alpha) (log y)^2 / y^2 -> 0`,

then every non-isolated frequency uses primes `gg y/A`, the close-pair graph has degree `O(A^2)`, each dangerous vertex has

`nu(lambda) << H A^(4 alpha) (log y)^2/y^2`,

and therefore

`Q_(y,H)(A) << H A^(2+4 alpha) (log y)^2/y^2 -> 0`.

The same condition forces `A=o(y/log y)`, so one-cancellation prime/prime shells stay outside the window and the exact-shell multiplicity comparison remains valid. For `alpha=0`, the positive shell energy is negligible for every `A=o(y/(sqrt(H) log y))`.

This moves the real boundary substantially beyond “fixed normalized width.” The elementary local-degree argument fails only when widening has made either determinant multiplicity or top-scale coefficient mass large enough that the displayed product is no longer small, or when the window approaches the prime/prime cancellation scale. The remaining positive-taper problem is to control the limiting/intermediate region with its actual sinc weights.

**Boundary.** VIS-207 gives an upper regime, not the sharp transition. It does not control the full intermediate-shell sum, does not prove one-sided crowding small, and says nothing about sign-changing/complex tapers beyond the autocorrelation subclass.