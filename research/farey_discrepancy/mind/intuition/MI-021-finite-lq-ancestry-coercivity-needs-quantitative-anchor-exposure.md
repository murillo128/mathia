# MI-021 — Finite-`L^q` ancestry coercivity is anchored cut exposure; anchor mass and depth pay different taxes

**Evidence level:** exact/proved classification from [FD-147](../../findings/FD-147-finite-seed-ancestry-coercivity-is-exactly-an-anchored-cut-problem.md), with the endpoint-weight obstruction quantified by [FD-148](../../findings/FD-148-finite-seed-anchored-expansion-forces-singular-endpoint-marginals.md), the bounded-distortion depth threshold by [FD-149](../../findings/FD-149-bounded-distortion-ancestry-transfer-must-reach-typical-prime-factor-depth.md), the explicit depth/distortion phase curve in [FD-150](../../findings/FD-150-ancestry-depth-trades-only-the-child-tax-along-a-sathe-selberg-phase-curve.md), and the growing-anchor parent law [FD-151](../../findings/FD-151-growing-anchors-trade-the-parent-tax-for-coefficient-mass.md).

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

This is the parent-side resource law in its scale-free form. If `P_T=O(1)`, the anchor must carry a positive fraction of all squarefree coefficients; if `|D_T|=o(T)`, then `P_T` must grow at least on the reciprocal anchor-density scale. For rank anchors `D_T(r)={n:omega(n)<=r}`, the Sathe--Selberg lower tail gives, at `r=floor(alpha log log T)` with `alpha<1`,

`p_T asymp_alpha 1/[sqrt(log log T)(log T)^(I(alpha))]`,

so positive expansion forces the same factor `sqrt(log log T)(log T)^(I(alpha))` into the parent distortion. Bounded parent distortion is not available until the anchor enters the Erdős--Kac window and becomes macroscopically large.

The child side admits a different quantitative depth trade. FD-150 shows that if the reachable descendants at depth `L_T=floor(alpha log log T)` carry child distortion at most `K_T`, then constant expansion forces

`K_T >> sqrt(log log T)(log T)^(I(alpha))`.

The identical large-deviation rate function therefore prices two different resources: how much multiplicative rank is included directly in the anchor, and how much descendant mass a bounded-depth observation can reach. They are not interchangeable. **Depth can reduce child sparsity; anchor growth can reduce parent amplification; neither resource pays the other for free.**

A source-valid proposal should expose at least four quantities before a full coercivity argument: anchor mass `p_T`, parent distortion `P_T`, ancestry depth, and child distortion on the reachable set. If `p_T->0` with `P_T=O(1)`, FD-151 kills the route immediately. If a positive-density anchor is used instead, the next question is whether the actual Farey data genuinely supply that much absolute Möbius orientation without crossing the source-reconstruction boundary.

**Boundary.** These results concern binary Möbius orientations, finite `L^q`, positive divisibility-ancestry observations and divisor-closed anchors. They do not exclude `L^infinity`, independently justified singular weights, non-divisibility observations or genuinely nonlocal Farey/Fourier destination functionals. The complement-cut laws are necessary-condition screens, not sufficiency theorems for expansion.
