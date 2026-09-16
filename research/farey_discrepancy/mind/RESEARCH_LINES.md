# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Derive source-native coercivity that pays the anchor-mass/parent-distortion trade and the depth-dependent child tax

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-021-finite-lq-ancestry-coercivity-needs-quantitative-anchor-exposure`.

FD-145--FD-147 classify the binary coefficient-side obstruction exactly. For an anchored seed `D`, finite-`L^q` binary recovery is controlled by the anchored Cheeger ratio `h_D(nu,eta)`: connectivity only excludes zero boundary, while stability requires uniformly positive observed boundary mass for every macroscopic flipped region.

FD-148 shows that a fixed finite divisor-closed anchor has an unavoidable parent-side endpoint cost. If the parent marginal on the seed is at most `P_T` times uniform, then `h_(D,T) <<_D P_T/T`; positive expansion therefore requires parent amplification of order `T`.

FD-149--FD-150 quantify what additional child-side cost can be traded for nonlocal ancestry depth. At depth `L_T=floor(alpha log log T)`, `0<alpha<1`, the reachable squarefree mass is

`nu_T(R_(D,L_T)) asymp_(D,alpha) [sqrt(log log T) (log T)^(I(alpha))]^-1`,

where `I(alpha)=1-alpha+alpha log alpha`. If the child marginal is at most `K_T` times uniform on the reachable set, constant expansion forces

`K_T >> sqrt(log log T) (log T)^(I(alpha))`.

FD-151 now removes the fixed-anchor qualifier from the parent obstruction. For any divisor-closed anchor `D_T`, write `p_T=nu_T(D_T)`. If `eta_T^-(d)<=P_T nu_T(d)` on the anchor, then independently of ancestry depth

`h_(D_T,T) <= P_T p_T/(1-p_T)`.

Thus `h>=c>0` forces `P_T>=c(1-p_T)/p_T`. Bounded parent distortion is possible under this complement cut only when the anchor itself has positive asymptotic coefficient mass. For rank anchors `D_T(r)={omega(n)<=r}`, the same Sathe--Selberg rate function reappears on the parent side: at `r=floor(alpha log log T)`, `alpha<1`, bounded expansion requires `P_T >> sqrt(log log T)(log T)^(I(alpha))`; bounded `P_T` pushes the anchor into the Erdős--Kac window and hence to macroscopic mass.

The structural correction is therefore stronger than “depth only trades the child tax.” **A growing anchor trades parent singularity for direct source orientation on a larger fraction of coefficients.** Typical ancestry depth does not pay that bill; it can only move where the information is spent.

The live coefficient-side theorem must now justify the source cost explicitly. If it keeps a sparse anchor, it must explain the required parent distortion. If it uses bounded parent distortion, it must explain why the actual Farey observable legitimately anchors a positive-density coefficient set without simply encoding/reconstructing Möbius orientation. Only after that parent/source audit does ancestry depth and the child phase curve become relevant.

## Apply the information-budget gate only after cut exposure survives

FD-144 remains a separate lower bound: even after anchoring and quantitative cut exposure are solved, `o(r_T)` arbitrary source-independent normalized ancestry tests can still be fooled along a subsequence. This is a later information threshold, not a substitute for the cut theorem. Conversely, sufficiently direct high-information coordinates can reconstruct the source and risk circularity.

Future ancestry proposals should therefore be audited in this order: **anchor mass -> parent distortion -> depth/child distortion -> source justification for those resources -> information and precision budget -> destination relevance**. `L^infinity` remains qualitatively different because for binary data it sees any visible bridge rather than its normalized mass.

## Keep binary cut coercivity and nonlocal destination coercivity separate

FD-147--FD-151 concern binary Möbius orientations, finite `L^q`, positive divisibility-ancestry observations and divisor-closed anchors. They do not rule out `L^infinity`, independently justified singular weights, non-divisibility observations, or genuinely nonlocal Farey/Fourier destination functionals outside this edge model. Any escape should state which hypothesis changes and why the new destination does not simply reconstruct the source.
