# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Quantify source information in anchor geometries that actually give coercivity

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-021-finite-lq-ancestry-coercivity-needs-quantitative-anchor-exposure`.

FD-145--FD-147 reduce finite-`L^q` binary ancestry recovery to anchored cut exposure. FD-148--FD-153 then give a sharp resource law for rank-aligned anchors: sparse anchors pay parent distortion; central rank anchors buy bounded parent load with macroscopic source information but still pay a `sqrt(log log T)` child window; supertypical rank anchors can make residual depth bounded only after orienting almost all coefficients.

FD-154 identifies the missing geometric qualification. A fixed finite-prime avoidance face is divisor-closed, has positive asymptotic mass, and places every remaining squarefree coefficient within bounded ancestry depth. With one direct edge per child it gives an exact `L^q` Dirichlet frame and `T`-uniform endpoint distortion. For a single prime the depth is one and all three constants converge to `ell+1`. Therefore the rank-depth laws are exact for their anchor family, not universal lower bounds for ancestry.

The live question has moved to **anchor provenance**. Can a Farey-native observable provide the orientation on a useful macroscopic coordinate face such as `(n,P_S)=1` without already encoding or reconstructing Möbius? The decisive test should compare the information carried by the proposed Farey observable with the anchored orientation it claims to supply, then prove that the exact coefficient coercivity survives the map to the Franel--Landau destination. Cheap edge depth is irrelevant if the anchor itself spends the target source.

## Apply the information-budget gate only after cut exposure survives

FD-144 remains a separate lower bound: even after anchoring and quantitative cut exposure are solved, `o(r_T)` arbitrary source-independent normalized ancestry tests can still be fooled along a subsequence. This is a later information threshold, not a substitute for the cut theorem. Conversely, sufficiently direct high-information coordinates may reconstruct the source and become circular.

Future ancestry proposals should therefore be audited in this order: **anchor geometry and mass -> source justification of the anchor -> parent distortion -> residual ancestry depth -> child distortion -> information/precision budget -> destination relevance**. Rank-tail asymptotics enter only when the anchor is actually rank-initial.

## Keep coefficient coercivity and nonlocal destination coercivity separate

FD-147--FD-154 concern binary Möbius orientations, finite `L^q` and positive divisibility-ancestry observations. FD-154 proves that excellent coefficient-side coercivity is mathematically possible with bounded depth, but it does not show that the Farey discrepancy supplies the required macroscopic anchor or that the resulting norm controls the RH-equivalent destination. Any escape must state which hypothesis changes and why the new destination does not simply reconstruct the source.
