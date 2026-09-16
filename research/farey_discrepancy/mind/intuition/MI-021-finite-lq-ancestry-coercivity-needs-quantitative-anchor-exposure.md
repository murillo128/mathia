# MI-021 — Finite-`L^q` ancestry coercivity is anchored cut exposure; anchor mass and depth pay different taxes

**Evidence level:** exact/proved classification from [FD-147](../../findings/FD-147-finite-seed-ancestry-coercivity-is-exactly-an-anchored-cut-problem.md), with the endpoint-weight obstruction quantified by [FD-148](../../findings/FD-148-finite-seed-anchored-expansion-forces-singular-endpoint-marginals.md), the bounded-distortion depth threshold by [FD-149](../../findings/FD-149-bounded-distortion-ancestry-transfer-must-reach-typical-prime-factor-depth.md), the explicit fixed-seed depth/distortion phase curve in [FD-150](../../findings/FD-150-ancestry-depth-trades-only-the-child-tax-along-a-sathe-selberg-phase-curve.md), the growing-anchor parent law [FD-151](../../findings/FD-151-growing-anchors-trade-the-parent-tax-for-coefficient-mass.md), and the joint Gaussian child-window law [FD-152](../../findings/FD-152-growing-rank-anchors-have-a-gaussian-child-depth-window.md).

For binary orientations anchored on `D`, the optimal finite-`L^q` Poincaré constant is exactly

`C^(bin)_(q,D)=h_D(nu,eta)^(-1/q)`.

Thus connectivity is only the zero-boundary endpoint. Stable recovery requires a uniform lower bound on observed boundary mass for every admissible macroscopic cut.

FD-148 identifies a depth-independent parent obstruction for a fixed finite divisor-closed anchor. If the parent marginal satisfies `eta_T^-(d)<=P_T nu_T(d)` on `D`, then for every ancestry depth

`h_(D,T)^(<=L) <= (zeta(2)|D|+o_D(1)) P_T/T`.

Positive anchored expansion therefore requires parent amplification of order `T` for a fixed anchor. Making the ancestry graph deeper does not dilute this tax.

FD-151 shows exactly what changes when the anchor grows. Let `D_T` be any nonempty divisor-closed anchor containing `1` and put `p_T=nu_T(D_T)`. Under the same pointwise parent domination,

`h_(D_T,T) <= P_T p_T/(1-p_T)`.

Hence `h>=c>0` forces

`P_T >= c(1-p_T)/p_T`.

This is the parent-side resource law in its scale-free form. If `P_T=O(1)`, the anchor must carry a positive fraction of all squarefree coefficients. For rank anchors `D_T(r)={n:omega(n)<=r}`, bounded parent distortion therefore pushes `r` into the Erdős--Kac central window `r=log log T+O(sqrt(log log T))` rather than leaving it at a fixed fraction below typical rank.

FD-152 computes the child bill *after* that macroscopic purchase. For a rank anchor and depth `L`, the reachable outside vertices are exactly

`R_(r,L)(T)={n:r<omega(n)<=r+L}`.

If the parent and child marginals are dominated by `P_T nu_T` on the anchor and `K_T nu_T` on this shell, the same complement cut gives the simultaneous bound

`h_(r,T)^(<=L) <= min{P_T p_T(r), K_T s_T(r,L)}/(1-p_T(r))`,

where `s_T(r,L)=nu_T(R_(r,L)(T))`.

Put `lambda_T=log log T`. If

`(r_T-lambda_T)/sqrt(lambda_T) -> z`

and

`L_T/sqrt(lambda_T) -> ell`,

then squarefree Erdős--Kac gives

`p_T(r_T)->Phi(z)`,

`s_T(r_T,L_T)->Phi(z+ell)-Phi(z)`.

Thus the depth currency depends on the starting rank. From a fixed seed, reaching a macroscopic coefficient population costs order `log log T` multiplicative levels as in FD-149--FD-150. From a central rank anchor that has already prepaid typical multiplicative rank, the remaining transition is only the Gaussian fluctuation width:

`L_T=o(sqrt(log log T))` captures asymptotically none of the unanchored tail,

while `L_T~ell sqrt(log log T)` captures the conditional fraction

`[Phi(z+ell)-Phi(z)]/[1-Phi(z)]`.

For bounded child distortion `K` and target expansion `c`, a finite central limit `z` requires this fraction to be at least `c/K`; equivalently the necessary normalized depth is the corresponding conditional Gaussian quantile. So a positive-density anchor does not make depth free: it changes the child scale from the typical rank `log log T` to its fluctuation scale `sqrt(log log T)`.

The resource accounting is therefore genuinely joint. **Anchor growth reduces parent amplification by directly orienting a larger fraction of the source; that purchase also prepays multiplicative rank and shortens the remaining child path. Depth only exposes the still-unanchored tail.** The same cut sees both costs, so they must not be charged independently as if a central anchor and a fixed-seed depth were both still necessary.

A source-valid proposal should expose at least five quantities before a full coercivity argument: anchor mass `p_T`, parent distortion `P_T`, anchor rank/location relative to the squarefree rank law, ancestry depth, and child distortion on the reachable shell. If `p_T->0` with `P_T=O(1)`, FD-151 kills the route immediately. If a central positive-density anchor is used, the first unresolved source question is whether the actual Farey observable legitimately supplies that much absolute Möbius orientation; only then does FD-152 price the remaining Gaussian child depth.

**Boundary.** These results concern binary Möbius orientations, finite `L^q`, positive divisibility-ancestry observations and divisor-closed/rank anchors. They do not exclude `L^infinity`, independently justified singular weights, non-divisibility observations or genuinely nonlocal Farey/Fourier destination functionals. FD-152 treats central rank anchors with a nonvanishing unanchored Gaussian tail; near-total anchors in moderate-deviation regimes need a finer tail law. The complement-cut laws are necessary-condition screens, not sufficiency theorems for expansion.
