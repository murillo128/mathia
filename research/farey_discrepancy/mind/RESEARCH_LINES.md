# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Quantify source information in anchor geometries that actually give coercivity

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-021-finite-lq-ancestry-coercivity-needs-quantitative-anchor-exposure`.

FD-145--FD-147 reduce finite-`L^q` binary ancestry recovery to anchored cut exposure. FD-148--FD-153 price rank-aligned anchors: sparse anchors pay parent distortion, central-rank anchors buy bounded parent load with macroscopic source information but retain a `sqrt(log log T)` child window, and bounded residual depth requires orienting almost all coefficients.

FD-154 shows that this rank-depth law is not universal. A fixed finite-prime avoidance face is divisor-closed, has positive asymptotic mass, and gives bounded ancestry depth and `T`-uniform endpoint distortion. FD-155 then prices thinning that face: reducing anchored exposure to `alpha` needs `s_alpha=exp(alpha^(-1+o(1)))` prime coordinates and the direct parent load becomes double exponential in `alpha^(-1+o(1))`.

FD-156 proves the architecture law for every one-parent forest on the same face. FD-157 closes the naive multi-parent escape: cheap parent load at fixed expansion must transport boundary mass across distinct `S`-free source cores.

FD-158 shows that completing any finite auxiliary prime vocabulary does not absorb that leakage. Once the full `S union U` Boolean box lies below the truncation, packet volume and available anchor states gain the same `2^|U|` factor, so the exponential cut pressure survives and bounded child load forces recipients carrying primes outside `S union U`.

FD-159 removes the full-box assumption for **divisor-downward truncated auxiliary support**. Let `C` be the active auxiliary core set, let `f(c)` be the number of occupied nonempty primary `S`-states above core `c`, and put `bar f=|C|^{-1}sum_c f(c)`. Then the exact cut law is

`P_(S,T) + L_(S,C,T)/|C| >= h_(S,T) bar f`.

Thus truncation helps only by making the average occupied primary fibre genuinely small. If `bar r` is the corresponding average available primary depth, the down-set structure gives `bar f >= 2^bar r-1`. With bounded child distortion, the same excess forces a proportional outer-core recipient population. The complete-cube law of FD-158 is the uniform-fibre special case.

The live escape is narrower again: **non-downward sparse occupation with holes**, scale-dependent/migrating support, unbounded distortion, a different anchor, or a genuinely Farey-native invariant that changes which cuts are admissible. Merely staying below the truncation ceiling or using an incomplete divisor down-set is no longer enough. A useful next theorem would quantify the price of holes: how much extra incoming boundary/source information is needed to reduce `bar f` below the divisor-downward law while retaining anchored expansion.

## Apply the information-budget gate only after cut exposure survives

FD-144 remains a later lower bound: even after anchoring and quantitative cut exposure are solved, `o(r_T)` arbitrary source-independent normalized ancestry tests can still be fooled along a subsequence. Neither a large cross-core recipient population nor fresh-prime migration by itself is an information lower bound; a deterministic rule may generate many recipients from little description. Any epistemic claim still needs a theorem connecting geometric leakage to independent source information and then to the Franel--Landau destination.

Audit future ancestry proposals in the order **anchor geometry and mass -> source justification -> parent distortion -> cross-core/fresh-prime leakage -> occupied fibre/down-set geometry -> anchored expansion -> residual depth -> child distortion/recipient population -> information and precision budget -> destination relevance**.

## Keep coefficient coercivity and nonlocal destination coercivity separate

FD-147--FD-159 concern binary Möbius orientations, finite `L^q` and positive divisibility-ancestry observations. They show exactly how excellent coefficient-side coercivity can be purchased and why neither extra parents, finite completed prime vocabularies nor ordinary divisor-downward truncation removes the hidden-fibre cut. None proves that Farey discrepancy supplies the orientation or that the resulting norm controls the RH-equivalent destination. Any surviving route must state which source hypothesis changes and why it does not simply reconstruct the source.
