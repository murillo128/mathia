# Xi-flow research lines

This file holds the current mathematical questions suggested by the durable Xi-flow intuitions. It is not a roadmap, task queue, status page, or history.

## Convert exact square-lattice identification into quantitative transition coercivity

**Linked intuitions:** `MI-004-endpoint-prime-free-fourier-sector-is-volterra-triangular`, `MI-008-gaussian-reference-localization-is-relatively-exact-but-not-global`, `MI-011-cross-scale-observability-can-compress-to-one-off-circle-heat-trace`, `MI-012-xi-tail-hazard-is-source-specific-but-not-yet-coercive`.

XF-154--XF-168 separate source identification from RH transition control. Positive complete-monotone Jacobi-reflecting mixtures can have the wrong heat origin when scaled square lattices are allowed, while exact support on the single Xi lattice `pi n^2` forces the theta coefficients by Hamburger rigidity.

XF-169 identifies the residual freedom exactly. Positive log-scale mixtures preserving the normalized Riemann functional equation multiply the completed zeta function by a self-reciprocal entire Mellin factor; the same factor multiplies the time-zero Xi transform. Small lattice displacement is therefore spectrally active even though the functional equation does not see it. XF-170 proves the sharp quantitative boundary for this whole positive compact mixture class: if the logarithmic support displacement is `delta`, every newly introduced nonreal zero satisfies `delta |Re z| >= 4 pi`, with equality attainable by a three-point mixture.

XF-171 adds a compact-support-free stability modulus inside the same positive normalized scale-mixture gauge. The intrinsic central Mellin deficit `d=1-M(1/2)` obeys `|M(s)-M(1/2)| <= 4 d |s-1/2|^2` throughout the critical strip, so `d < 1/(4T^2+2)` excludes all added multiplier zeros through height `T`. The XF-167 three-point family has `d T^2 -> pi^2/16`, showing that the `T ~ d^(-1/2)` resolution scale is optimal in order even though the universal constant is not claimed sharp.

XF-172 converts that hidden mixture defect into a source-visible spectral-edge quantity. If `mu_nu` is the positive Laplace measure of the mixed theta prekernel, the weighted subfundamental leakage

`L_nu = integral_(0,pi) [ (pi/lambda)^(1/4) - 1 ]^2 dmu_nu(lambda)`

satisfies `d_nu <= L_nu`. Hence `L_nu < 1/(4T^2+2)` rules out every added common-mixture multiplier zero in the full critical strip through height `T`, while `L_nu=0` forces `nu=delta_0` inside this gauge. The XF-167 three-atom family has `L_nu=d_nu` for sufficiently small displacement and `L_nu T^2 -> pi^2/16`, so the inverse-square-root resolution scale is already order-sharp at the source spectral edge.

XF-173 qualifies that source bridge on unbounded scale mixtures. The leakage has the exact positive-shift kernel

`K(b)=e^-b sum_(n<e^(2b)) (e^b/sqrt(n)-1)^2`,

which equals `2(cosh b-1)` for `b <= (1/2)log 2` but grows as `2b e^b+O(e^b)` for remote shifts. Thus `L_nu<infinity` is equivalent to a logarithmically reinforced tail moment `integral b e^b dnu(b)<infinity`, whereas the normalization and the XF-171 defect require only the underlying `e^b` moment. There are normalized positive even mixtures with arbitrarily small `d_nu` but `L_nu=infinity`; for any fixed height `T`, XF-171 can therefore certify a multiplier zero-free critical strip through `T` while the XF-172 sufficient condition is vacuous.

XF-174 resolves that topology mismatch and identifies why it appeared. For the renormalized edge family

`E_(nu,alpha) = integral_(0,pi) W_alpha(pi/lambda) dmu_nu(lambda)`,

with `W_alpha(x)=((x^alpha-1)/alpha)^2` for `alpha>0` and `W_0(x)=log^2 x`, every fixed `0 <= alpha < 1/4` satisfies a two-sided comparison `c_alpha d_nu <= E_(nu,alpha) <= C_alpha d_nu` on the full normalized unbounded common-scale gauge. The associated one-shift kernel is asymptotic to `8 e^b / ((1-4 alpha)(1-2 alpha))` for `0<alpha<1/4` and to `8e^b` at `alpha=0`, exactly matching the normalization tail. At `alpha=1/4`, `E_(nu,1/4)=16 L_nu` and the XF-173 `b e^b` surcharge reappears; above `1/4` the surcharge is exponential. Thus the quarter-power is a genuine critical spectral-edge exponent, while the parameter-free logarithmic leakage is a source-visible defect equivalent to `d_nu` with no extra tail hypothesis.

XF-175 begins the genuinely atomwise regime. Writing the `lambda`-shell extracted from a Laplace atom as `kappa_lambda(u)=lambda e^(5u)(2 lambda e^(4u)-3)e^(-lambda e^(4u))`, independently moving and reweighting matched atoms admits an explicit strip budget `B_q` built from the weighted shell norm `K_q(lambda)` and its logarithmic scale derivative `J_q(lambda)`. Finite `B_q` gives `sup_(|Im z|<=q) |H_tilde(z)-H_Xi(z)| <= B_q`; on a fixed Xi-zero-free contour, `B_q` below the boundary Xi margin preserves the zero count by Rouche. For fixed strip width, however, `K_q(lambda) ~ (1/2)lambda e^-lambda` and `J_q(lambda) ~ 2 lambda^2 e^-lambda`. Consequently bounded-factor deformation of all atoms beyond index `N` costs only `poly(N)e^(-c pi N^2)`. Remote square-lattice placement is therefore Gaussian-invisible to fixed compact zero geometry through this direct source interface.

The common positive scale-mixture metric problem is quantitatively settled at finite height, and XF-175 shows that the first atomwise gate has a qualitatively different obstruction. A local spectral budget exists, but it is strongly concentrated at the low spectral edge and, unlike the common-mixture case, independent atom motion destroys the multiplier factorization. The next source-side target is therefore **cross-index spectral coupling**: use exact Jacobi/Poisson or coefficient arithmetic to show that an admissible high-index atom error must create a visible low-spectral defect, or obtain quantitative Xi contour margins that can be compared with the atomwise budget on height-growing domains. Neither route may assume RH or line preservation. Merely demanding increasingly accurate bounded-factor placement of sufficiently remote `pi n^2` atoms cannot coerce finite-height zero geometry.

## Treat functional-equation preservation and finite-height source resolution as separate gates

The normalized functional equation admits a nontrivial scale-mixture gauge. Positivity and compact support make that gauge quantitatively resolvable at the sharp inverse-displacement height of XF-170; XF-171 shows that even without compact support the central Mellin deficit gives an order-sharp inverse-square-root height modulus. XF-172 makes that soft modulus source-visible through weighted Laplace spectrum leaking below the first Xi atom, while XF-173 shows that the quarter-power edge weight is too singular to be topology-equivalent on unbounded mixtures.

XF-174 supplies the corrected source-visible topology. Every edge exponent below `1/4`, including the logarithmic endpoint `alpha=0`, is globally equivalent to the central Mellin deficit under only the original Jacobi normalization; `1/4` is exactly where the logarithmic tail tax begins. Future common-scale stability statements can therefore use the logarithmic/subcritical observable directly and need not impose an artificial `b e^b` uniform-integrability assumption.

XF-175 shows why the atomwise extension cannot simply imitate that scalar theory. The direct shell budget controls the deformed transform uniformly on the critical-strip coordinate, but remote bounded-factor atom errors are suppressed as `e^(-c pi n^2)`, and zero-count transfer additionally needs a nonzero Xi contour margin. Functional-equation preservation and source resolution must therefore be coupled again at the coefficient level: either modular/arithmetic structure transports remote spectral error into the visible edge, or a separate quantitative base-Xi margin theorem is needed before atomwise source closeness can become height-growing zero control.