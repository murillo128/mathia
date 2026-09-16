# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Derive source-native coercivity that pays the anchor-mass/parent-distortion trade and the depth-dependent child tax

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-021-finite-lq-ancestry-coercivity-needs-quantitative-anchor-exposure`.

FD-145--FD-147 classify the binary coefficient-side obstruction exactly. For an anchored seed `D`, finite-`L^q` binary recovery is controlled by the anchored Cheeger ratio `h_D(nu,eta)`: connectivity only excludes zero boundary, while stability requires uniformly positive observed boundary mass for every macroscopic flipped region.

FD-148 shows that a fixed finite divisor-closed anchor has an unavoidable parent-side endpoint cost. If the parent marginal on the seed is at most `P_T` times uniform, then `h_(D,T) <<_D P_T/T`; positive expansion therefore requires parent amplification of order `T`.

FD-149--FD-150 quantify the child-side cost from such a low-rank starting point. At depth `L_T=floor(alpha log log T)`, `0<alpha<1`, the reachable squarefree mass is

`nu_T(R_(D,L_T)) asymp_(D,alpha) [sqrt(log log T) (log T)^(I(alpha))]^-1`,

where `I(alpha)=1-alpha+alpha log alpha`. If the child marginal is at most `K_T` times uniform on the reachable set, constant expansion forces

`K_T >> sqrt(log log T) (log T)^(I(alpha))`.

FD-151 removes the fixed-anchor qualifier from the parent obstruction. For any divisor-closed anchor `D_T`, write `p_T=nu_T(D_T)`. If `eta_T^-(d)<=P_T nu_T(d)` on the anchor, then independently of ancestry depth

`h_(D_T,T) <= P_T p_T/(1-p_T)`.

Thus `h>=c>0` forces `P_T>=c(1-p_T)/p_T`. Bounded parent distortion is possible under this complement cut only when the anchor itself has positive asymptotic coefficient mass. For rank anchors `D_T(r)={omega(n)<=r}`, bounded `P_T` therefore pushes the anchor into the central Erdős--Kac window and makes it macroscopic.

FD-152 computes what that macroscopic anchor buys on the child side. For rank anchor `r` and ancestry depth `L`, the descendants outside the anchor are exactly the shell `r<omega(n)<=r+L`, and the complement cut gives the joint screen

`h <= min{P_T p_T(r), K_T s_T(r,L)}/(1-p_T(r))`.

If `lambda_T=log log T`, `(r_T-lambda_T)/sqrt(lambda_T)->z`, and `L_T/sqrt(lambda_T)->ell`, then `p_T(r_T)->Phi(z)` and `s_T(r_T,L_T)->Phi(z+ell)-Phi(z)`. Hence a central anchor leaving a fixed positive upper tail still needs `L_T=Omega(sqrt(log log T))` under bounded child distortion.

FD-153 now resolves the near-total-anchor regime left open by FD-152. If `r_T/lambda_T->alpha in (1,2)`, the conditional overshoot `J_T=omega-r_T` above the anchor converges to a geometric law with `Pr(J<=L)->1-alpha^(-L)`: bounded depth can expose a fixed fraction of the remaining coefficients, but only after the anchor mass has already tended to one at the large-deviation rate `1-p_T(r_T) asymp [sqrt(lambda_T)(log T)^(I(alpha))]^-1`. In the moderate-deviation transition `alpha_T=1+delta_T`, `delta_T sqrt(lambda_T)->infinity`, the rescaled overshoot satisfies `delta_T J_T => Exp(1)`, so the residual child-depth scale is `L_T asymp delta_T^(-1)=sqrt(log log T)/z_T`. This interpolates continuously between the central `sqrt(log log T)` scale and constant depth.

The near-total-anchor escape is therefore real only in a precise accounting sense: ancestry depth becomes cheap exactly when source orientation has already fixed `1-o(1)` of the coefficient space. A source-valid theorem must justify the whole purchase. Sparse anchors pay parent distortion; central anchors pay macroscopic direct source information and a Gaussian-width child depth; supertypical anchors can reduce the residual depth further but pay an asymptotically total anchor. None of these trades is free.

## Apply the information-budget gate only after cut exposure survives

FD-144 remains a separate lower bound: even after anchoring and quantitative cut exposure are solved, `o(r_T)` arbitrary source-independent normalized ancestry tests can still be fooled along a subsequence. This is a later information threshold, not a substitute for the cut theorem. Conversely, sufficiently direct high-information coordinates can reconstruct the source and risk circularity.

Future ancestry proposals should therefore be audited in this order: **anchor mass/tail regime -> parent distortion -> anchor rank/source justification -> residual conditional overshoot law -> child distortion/depth -> information and precision budget -> destination relevance**. `L^infinity` remains qualitatively different because for binary data it sees any visible bridge rather than its normalized mass.

## Keep binary cut coercivity and nonlocal destination coercivity separate

FD-147--FD-153 concern binary Möbius orientations, finite `L^q`, positive divisibility-ancestry observations and divisor-closed/rank anchors. They do not rule out `L^infinity`, independently justified singular weights, non-divisibility observations, genuinely nonlocal Farey/Fourier destination functionals outside this edge model, or a source theorem that justifies an almost-total anchor without circularly encoding Möbius orientation. Any escape should state which hypothesis changes and why the new destination does not simply reconstruct the source.
