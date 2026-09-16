# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Quantify source information in anchor geometries that actually give coercivity

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-021-finite-lq-ancestry-coercivity-needs-quantitative-anchor-exposure`.

FD-145--FD-147 reduce finite-`L^q` binary ancestry recovery to anchored cut exposure. FD-148--FD-153 price rank-aligned anchors: sparse anchors pay parent distortion, central-rank anchors buy bounded parent load with macroscopic source information but retain a `sqrt(log log T)` child window, and bounded residual depth requires orienting almost all coefficients.

FD-154 shows that this rank-depth law is not universal. A fixed finite-prime avoidance face is divisor-closed, has positive asymptotic mass, and gives bounded ancestry depth and `T`-uniform endpoint distortion. FD-155 then prices thinning that face: reducing anchored exposure to `alpha` needs `s_alpha=exp(alpha^(-1+o(1)))` prime coordinates and the direct parent load becomes double exponential in `alpha^(-1+o(1))`.

FD-156--FD-160 successively remove one-parent, multi-parent, finite auxiliary vocabulary, divisor-downward support and static sparse-hole escapes. For an arbitrary sparse active-core family, taking divisor closure of the depth-`r` cores internalizes hole inflow and restores the exponential pressure `P+L/|D_r(C)|>=h(2^r-1)`.

FD-161 now prices the terminal-core loophole for the initial-prime anchor. If `S_s={p_1,...,p_s}` and a nontrivial `S_s`-free auxiliary core `c` lies below `T/2`, its principal divisor ideal necessarily contains a full primary Boolean face through depth

`b_s=max{j<=s:P_j<=p_(s+1)}`.

The average occupied fibre in that closure is at least `(2^(b_s)-1)/2`, so the cut pressure still diverges like

`2^(b_s)=exp((log 2+o(1)) log s/log log s)`.

Thus bounded **visible** primary depth at a terminal core does not imply bounded depth after the natural divisor closure. Terminal migration only survives if the closure itself leaves the controlled regime or another architecture hypothesis is abandoned.

For the initial-prime avoidance family the remaining structural escapes are therefore sharper: growing endpoint distortion/expansion/leakage, a different anchor or cut geometry, trivial root behavior, closure outside the controlled truncation, or a source-native constraint that changes which coefficient flips are admissible. Static holes, finite auxiliary vocabularies and merely terminal auxiliary labels no longer provide distinct escapes.

## Apply the information-budget gate only after cut exposure survives

FD-144 remains a later lower bound: even after anchoring and quantitative cut exposure are solved, `o(r_T)` arbitrary source-independent normalized ancestry tests can still be fooled along a subsequence. Neither a large cross-core recipient population, fresh-prime migration nor growing primorial closure is by itself an information lower bound; a deterministic rule may generate many recipients from little description. Any epistemic claim still needs a theorem connecting geometric leakage to independent source information and then to the Franel--Landau destination.

Audit future ancestry proposals in the order **anchor geometry and mass -> source justification -> parent distortion -> hole/cross-core/outer leakage -> divisor/principal-ideal closure -> closure depth -> anchored expansion -> child distortion/recipient population -> information and precision budget -> destination relevance**.

## Keep coefficient coercivity and nonlocal destination coercivity separate

FD-147--FD-161 concern binary Möbius orientations, finite `L^q` and positive divisibility-ancestry observations. They show exactly how excellent coefficient-side coercivity can be purchased and why extra parents, finite auxiliary vocabularies, sparse holes and terminal-core presentation do not remove the hidden-fibre cut once the intrinsic divisor closure is taken. None proves that Farey discrepancy supplies the orientation or that the resulting norm controls the RH-equivalent destination. Any surviving route must state which source hypothesis or geometry changes and why it does not simply reconstruct the source.