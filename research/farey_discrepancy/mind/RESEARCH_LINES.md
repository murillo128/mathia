# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Quantify source information in anchor geometries that actually give coercivity

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-021-finite-lq-ancestry-coercivity-needs-quantitative-anchor-exposure`.

FD-145--FD-147 reduce finite-`L^q` binary ancestry recovery to anchored cut exposure. FD-148--FD-153 price rank-aligned anchors: sparse anchors pay parent distortion, central-rank anchors buy bounded parent load with macroscopic source information but retain a `sqrt(log log T)` child window, and bounded residual depth requires orienting almost all coefficients.

FD-154 shows that this rank-depth law is not universal. A fixed finite-prime avoidance face is divisor-closed, has positive asymptotic mass, and gives bounded ancestry depth and `T`-uniform endpoint distortion. FD-155 then prices thinning that face: reducing anchored exposure to `alpha` needs `s_alpha=exp(alpha^(-1+o(1)))` prime coordinates and the direct parent load becomes double exponential in `alpha^(-1+o(1))`.

FD-156 proves the architecture law for every one-parent forest on the same face: `P/h >= 2^|S|-1`. FD-157 closes the naive multi-parent escape. If `L` is normalized edge mass that changes the `S`-free core, then every positive multi-parent divisibility relation obeys

`P + L >= h (2^|S|-1)`.

Thus more parents inside one core do not buy coercivity; cheap parent load at fixed expansion must transport boundary mass across distinct source cores.

FD-158 now rules out the simplest attempt to absorb that leakage into a finite auxiliary prime vocabulary. For disjoint finite prime sets `S,U`, once the complete `S union U` Boolean box lies below the truncation, fresh-prime leakage `L_(S,U,T)` satisfies

`P_(S,T) + 2^(-|U|) L_(S,U,T) >= h_(S,T) (2^|S|-1)`.

The factor `2^|U|` cancels exactly between packet volume and the enlarged anchor face. If child distortion is bounded by `K`, the completed box forces `Omega(2^(|S|+|U|)/K)` distinct recipients carrying a prime outside `S union U`. **Finite completed auxiliary prime support is therefore not a terminal resource.** The obstruction replicates over every auxiliary core instead of being diluted by it.

The live escape is now narrower: sparse or scale-dependent auxiliary support that never closes to a full box before the truncation ceiling, a migrating prime vocabulary, loss of the bounded-load hypotheses, or a genuinely Farey-native invariant that controls the fresh-prime flux without reconstructing Möbius signs. A useful next theorem would replace full-box cardinality by a truncated-down-set quantity such as divisor shadow or occupied prime-coordinate entropy and recover a coercive leakage law before the product `P_S P_U` exceeds `T`.

## Apply the information-budget gate only after cut exposure survives

FD-144 remains a later lower bound: even after anchoring and quantitative cut exposure are solved, `o(r_T)` arbitrary source-independent normalized ancestry tests can still be fooled along a subsequence. Neither a large cross-core recipient population nor fresh-prime migration by itself is an information lower bound; a deterministic rule may generate many recipients from little description. Any epistemic claim still needs a theorem connecting the geometric leakage to independent source information and then to the Franel--Landau destination.

Audit future ancestry proposals in the order **anchor geometry and mass -> source justification -> parent distortion -> cross-core/fresh-prime leakage -> anchored expansion -> residual depth -> child distortion/recipient population -> support-completion or truncation geometry -> information and precision budget -> destination relevance**.

## Keep coefficient coercivity and nonlocal destination coercivity separate

FD-147--FD-158 concern binary Möbius orientations, finite `L^q` and positive divisibility-ancestry observations. They show exactly how excellent coefficient-side coercivity can be purchased and why finite completed prime vocabularies cannot terminate the required leakage. None proves that Farey discrepancy supplies the orientation or that the resulting norm controls the RH-equivalent destination. Any surviving route must state which source hypothesis changes and why it does not simply reconstruct the source.
