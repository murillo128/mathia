# Xi-flow research lines

This file holds the current mathematical questions suggested by the durable Xi-flow intuitions. It is not a roadmap, task queue, status page, or history.

## Convert exact square-lattice identification into quantitative transition coercivity

**Linked intuitions:** `MI-004-endpoint-prime-free-fourier-sector-is-volterra-triangular`, `MI-008-gaussian-reference-localization-is-relatively-exact-but-not-global`, `MI-011-cross-scale-observability-can-compress-to-one-off-circle-heat-trace`, `MI-012-xi-tail-hazard-is-source-specific-but-not-yet-coercive`.

XF-154--XF-168 separate source identification from RH transition control. Positive complete-monotone Jacobi-reflecting mixtures can have the wrong heat origin when scaled square lattices are allowed, while exact support on the single Xi lattice `pi n^2` forces the theta coefficients by Hamburger rigidity.

XF-169 identifies the residual freedom exactly. Positive log-scale mixtures preserving the normalized Riemann functional equation multiply the completed zeta function by a self-reciprocal entire Mellin factor; the same factor multiplies the time-zero Xi transform. Small lattice displacement is therefore spectrally active even though the functional equation does not see it. XF-170 proves the sharp quantitative boundary for this whole positive compact mixture class: if the logarithmic support displacement is `delta`, every newly introduced nonreal zero satisfies `delta |Re z| >= 4 pi`, with equality attainable by a three-point mixture.

XF-171 adds a compact-support-free stability modulus inside the same positive normalized scale-mixture gauge. The intrinsic central Mellin deficit `d=1-M(1/2)` obeys `|M(s)-M(1/2)| <= 4 d |s-1/2|^2` throughout the critical strip, so `d < 1/(4T^2+2)` excludes all added multiplier zeros through height `T`. The XF-167 three-point family has `d T^2 -> pi^2/16`, showing that the `T ~ d^{-1/2}` resolution scale is optimal in order even though the universal constant is not claimed sharp.

XF-172 converts that hidden mixture defect into a source-visible spectral-edge quantity. If `mu_nu` is the positive Laplace measure of the mixed theta prekernel, the weighted subfundamental leakage

`L_nu = integral_(0,pi) [ (pi/lambda)^(1/4) - 1 ]^2 dmu_nu(lambda)`

satisfies `d_nu <= L_nu`. Hence `L_nu < 1/(4T^2+2)` rules out every added common-mixture multiplier zero in the full critical strip through height `T`, while `L_nu=0` forces `nu=delta_0` inside this gauge. The XF-167 three-atom family has `L_nu=d_nu` for sufficiently small displacement and `L_nu T^2 -> pi^2/16`, so the inverse-square-root resolution scale is already order-sharp at the source spectral edge.

The live theorem should now quantify how an approximate single-square-lattice law controls this leakage, rather than search for another qualitative common-mixture classifier. A concrete positive target is to derive `L_nu(T)=o(T^{-2})` from a natural norm or reconstruction statement expressing approximate agreement with the Xi Laplace spectrum. If such a control is unavailable or unnatural, the next genuinely different regime is atomwise/mesoscopic deformation of the individual atoms `pi n^2`, where no common shift measure exists and a local spectral-edge budget must replace XF-172.

## Treat functional-equation preservation and finite-height source resolution as separate gates

The normalized functional equation admits a nontrivial scale-mixture gauge. Positivity and compact support make that gauge quantitatively resolvable at the sharp inverse-displacement height of XF-170; XF-171 shows that even without compact support the central Mellin defect gives an order-sharp inverse-square-root height modulus. XF-172 now shows that the same soft modulus is controlled by weighted Laplace spectrum leaking below the first Xi atom, directly connecting finite-height resolution to approximate square-lattice information inside the common-scale gauge.

Future stability statements should therefore carry an explicit height-versus-source-resolution modulus. For common positive scale mixing, the remaining gate is to control `L_nu` from a natural approximation to the exact theta spectral law. Beyond that class, the unresolved problem is to identify an atomwise or mesoscopic source defect that still couples quantitatively to zero geometry and ultimately to the heat transition.