# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Derive source-native coercivity that pays the fixed-anchor parent tax and the depth-dependent child tax

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-021-finite-lq-ancestry-coercivity-needs-quantitative-anchor-exposure`.

FD-145--FD-147 classify the binary coefficient-side obstruction exactly. For an anchored seed `D`, finite-`L^q` binary recovery is controlled by the anchored Cheeger ratio `h_D(nu,eta)`: connectivity only excludes zero boundary, while stability requires uniformly positive observed boundary mass for every macroscopic flipped region.

FD-148 shows that a fixed finite divisor-closed anchor has an unavoidable parent-side endpoint cost. If the parent marginal on the seed is at most `P_T` times uniform, then `h_(D,T) <<_D P_T/T`; positive expansion therefore requires parent amplification of order `T`.

FD-149--FD-150 now quantify what additional child-side cost can be traded for nonlocal ancestry depth. At depth

`L_T=floor(alpha log log T)`,  `0<alpha<1`,

the reachable squarefree mass is

`nu_T(R_(D,L_T)) asymp_(D,alpha) [sqrt(log log T) (log T)^(I(alpha))]^-1`,

where `I(alpha)=1-alpha+alpha log alpha`. If the child marginal is at most `K_T` times uniform on the reachable set, then

`h_(D,T)^(<=L_T) <<_(D,alpha) K_T/[sqrt(log log T) (log T)^(I(alpha))]`.

Hence constant expansion forces

`K_T >> sqrt(log log T) (log T)^(I(alpha))`.

The important correction is structural: **depth only trades the child tax. It never removes the fixed-anchor parent tax.** Even at or beyond the typical Erdős--Kac depth, a fixed anchor still requires order-`T` parent amplification unless the anchor itself changes.

The live coefficient-side theorem must therefore explain two resources separately: why genuine Farey/arithmetic structure supplies the unavoidable concentration on the fixed anchor, and, if the child law is not singular, why the observation reaches deeply enough in ancestry to pay the explicit `I(alpha)` phase curve. A growing anchor is a different escape and must be audited as source information rather than treated as free geometry.

## Apply the information-budget gate only after cut exposure survives

FD-144 remains a separate lower bound: even after anchoring and quantitative cut exposure are solved, `o(r_T)` arbitrary source-independent normalized ancestry tests can still be fooled along a subsequence. This is a later information threshold, not a substitute for the cut theorem. Conversely, sufficiently direct high-information coordinates can reconstruct the source and risk circularity.

Future ancestry proposals should therefore be audited in this order: **anchor geometry -> parent concentration -> depth/child distortion -> source justification for those resources -> information and precision budget -> destination relevance**. `L^infinity` remains qualitatively different because for binary data it sees any visible bridge rather than its normalized mass.

## Keep binary cut coercivity and nonlocal destination coercivity separate

FD-147--FD-150 concern binary Möbius orientations, finite `L^q`, positive divisibility-ancestry observations and a fixed finite anchor. They do not rule out a growing source-native anchor, `L^infinity`, independently justified singular weights, or genuinely nonlocal Farey/Fourier destination functionals outside this edge model. Any escape should state which hypothesis changes and why the new destination does not simply reconstruct the source.
