# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Quantify source information in anchor geometries that actually give coercivity

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-021-finite-lq-ancestry-coercivity-needs-quantitative-anchor-exposure`.

FD-145--FD-147 reduce finite-`L^q` binary ancestry recovery to anchored cut exposure. FD-148--FD-153 price rank-aligned anchors: sparse anchors pay parent distortion, central-rank anchors buy bounded parent load with macroscopic source information but retain a `sqrt(log log T)` child window, and bounded residual depth requires orienting almost all coefficients.

FD-154 shows that this rank-depth law is not universal. A fixed finite-prime avoidance face is divisor-closed, has positive asymptotic mass, and gives bounded ancestry depth and `T`-uniform endpoint distortion. FD-155 then prices thinning that face: reducing anchored exposure to `alpha` needs `s_alpha=exp(alpha^(-1+o(1)))` prime coordinates and the direct parent load becomes double exponential in `alpha^(-1+o(1))`.

FD-156 proves the architecture law for every one-parent forest on the same face. FD-157 closes the naive multi-parent escape: cheap parent load at fixed expansion must transport boundary mass across distinct `S`-free source cores.

FD-158 shows that completing any finite auxiliary prime vocabulary does not absorb that leakage. Once the full `S union U` Boolean box lies below the truncation, packet volume and available anchor states gain the same `2^|U|` factor, so the exponential cut pressure survives and bounded child load forces recipients carrying primes outside `S union U`.

FD-159 removes the full-box assumption for **divisor-downward truncated auxiliary support**. Let `C` be the active auxiliary core set, let `f(c)` be the number of occupied nonempty primary `S`-states above core `c`, and put `bar f=|C|^{-1}sum_c f(c)`. Then

`P_(S,T) + L_(S,C,T)/|C| >= h_(S,T) bar f`.

FD-160 closes the remaining static-hole escape. For an arbitrary sparse core family the missing lower cores contribute an explicit incoming bill,

`P_(S,T) + (J_(S,C,T)+L_(S,C,T))/|C| >= h_(S,T) bar f`,

where `J` is the hole-core inflow. More decisively, filling the holes by taking the divisor closure of every depth-`r` subfamily preserves that primary depth and internalizes `J`; FD-159 then gives

`P_(S,T) + L_(S,D_r(C),T)/|D_r(C)| >= h_(S,T)(2^r-1)`.

Thus non-downward sparsity does not erase the exponential prime-depth pressure. It only moves the required boundary farther out in the divisor poset. Even one deep sparse auxiliary core reproduces the same obstruction after taking its principal divisor ideal. Under positive anchored expansion and bounded normalized parent/leakage resources, every usable core has bounded primary depth.

The surviving structural escape is therefore genuinely **terminal or migrating support**, unbounded endpoint distortion/leakage, a different anchor/cut geometry, or a source-native constraint that changes which coefficient flips are admissible. Static holes and incomplete finite auxiliary vocabularies are no longer distinct resources.

## Apply the information-budget gate only after cut exposure survives

FD-144 remains a later lower bound: even after anchoring and quantitative cut exposure are solved, `o(r_T)` arbitrary source-independent normalized ancestry tests can still be fooled along a subsequence. Neither a large cross-core recipient population nor fresh-prime migration by itself is an information lower bound; a deterministic rule may generate many recipients from little description. Any epistemic claim still needs a theorem connecting geometric leakage to independent source information and then to the Franel--Landau destination.

Audit future ancestry proposals in the order **anchor geometry and mass -> source justification -> parent distortion -> hole/cross-core/outer leakage -> divisor closure and occupied depth -> anchored expansion -> residual depth -> child distortion/recipient population -> information and precision budget -> destination relevance**.

## Keep coefficient coercivity and nonlocal destination coercivity separate

FD-147--FD-160 concern binary Möbius orientations, finite `L^q` and positive divisibility-ancestry observations. They show exactly how excellent coefficient-side coercivity can be purchased and why extra parents, finite auxiliary vocabularies, divisor-downward truncation and static sparse holes do not remove the hidden-fibre cut. None proves that Farey discrepancy supplies the orientation or that the resulting norm controls the RH-equivalent destination. Any surviving route must state which source hypothesis or geometry changes and why it does not simply reconstruct the source.
