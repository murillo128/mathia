# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Quantify source information in anchor geometries that actually give coercivity

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-021-finite-lq-ancestry-coercivity-needs-quantitative-anchor-exposure`.

FD-145--FD-147 reduce finite-`L^q` binary ancestry recovery to anchored cut exposure. FD-148--FD-153 price rank-aligned anchors: sparse anchors pay parent distortion, central-rank anchors buy bounded parent load with macroscopic source information but retain a `sqrt(log log T)` child window, and bounded residual depth requires orienting almost all coefficients.

FD-154 shows that this rank-depth law is not universal. A fixed finite-prime avoidance face is divisor-closed, has positive asymptotic mass, and gives bounded ancestry depth and `T`-uniform endpoint distortion. FD-155 then prices thinning that face: reducing anchored exposure to `alpha` needs `s_alpha=exp(alpha^(-1+o(1)))` prime coordinates and the direct parent load becomes double exponential in `alpha^(-1+o(1))`.

FD-156 proves the architecture law for every one-parent forest on the same face: `P/h >= 2^|S|-1`. Unique-parent rerouting can reduce anchor congestion only by creating a compensating exponentially narrow cut.

FD-157 closes the naive multi-parent escape. Let `L` denote normalized edge mass that **changes the `S`-free core** rather than remaining inside one Boolean core. For every positive multi-parent divisibility relation on the same prime-avoidance face,

`P + L >= h (2^|S|-1)`.

Hence adding many parents inside the same `S`-free core does not improve the exponential resource law at all: when `L=0`, the FD-156 bound survives verbatim. A genuine same-anchor escape must transport appreciable boundary mass across distinct cores. If child distortion is bounded by `K`, cheap anchor load with fixed positive expansion forces at least `Omega(2^|S|/K)` recipient vertices outside the original core packet; combined with FD-155 thinning, this becomes a double-exponential recipient-population bill in the inverse anchor exposure scale.

The live question is therefore **cross-core provenance and destination relevance**, not merely “use a DAG.” Can a Farey-native observable generate the required cross-core orientation/leakage without already encoding Möbius, and can that large recipient population remain coercive after passage to the Franel--Landau destination? A different divisor-closed anchor geometry remains a separate escape. Recipient cardinality is not itself an information lower bound: a deterministic rule may generate many recipients from little description, so any epistemic claim needs an additional theorem.

## Apply the information-budget gate only after cut exposure survives

FD-144 remains a later lower bound: even after anchoring and quantitative cut exposure are solved, `o(r_T)` arbitrary source-independent normalized ancestry tests can still be fooled along a subsequence. This does not replace the cut theorem, and a large cross-core recipient population does not by itself imply many independent source bits.

Audit future ancestry proposals in the order **anchor geometry and mass -> source justification -> parent distortion -> cross-core leakage -> anchored expansion -> residual depth -> child distortion/recipient population -> information and precision budget -> destination relevance**. Rank-tail asymptotics apply only to rank anchors; the Boolean packet laws apply to finite-prime avoidance faces.

## Keep coefficient coercivity and nonlocal destination coercivity separate

FD-147--FD-157 concern binary Möbius orientations, finite `L^q` and positive divisibility-ancestry observations. They show exactly how excellent coefficient-side coercivity can be purchased and where that purchase must cross source cores. None proves that the Farey discrepancy supplies the orientation or that the resulting norm controls the RH-equivalent destination. Any surviving route must state which hypothesis changes and why it does not simply reconstruct the source.
