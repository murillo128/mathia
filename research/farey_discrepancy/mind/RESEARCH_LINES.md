# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Quantify source information in anchor geometries that actually give coercivity

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-021-finite-lq-ancestry-coercivity-needs-quantitative-anchor-exposure`.

FD-145--FD-147 reduce finite-`L^q` binary ancestry recovery to anchored cut exposure. FD-148--FD-153 then give a sharp resource law for rank-aligned anchors: sparse anchors pay parent distortion; central rank anchors buy bounded parent load with macroscopic source information but still pay a `sqrt(log log T)` child window; supertypical rank anchors can make residual depth bounded only after orienting almost all coefficients.

FD-154 identifies the missing geometric qualification. A fixed finite-prime avoidance face is divisor-closed, has positive asymptotic mass, and places every remaining squarefree coefficient within bounded ancestry depth. With one direct edge per child it gives an exact `L^q` Dirichlet frame and `T`-uniform endpoint distortion. For a single prime the depth is one and all three constants converge to `ell+1`. Therefore the rank-depth laws are exact for their anchor family, not universal lower bounds for ancestry.

FD-155 prices the obvious attempt to thin that coordinate face. For the direct one-edge-per-child frame, the parent distortion is exactly `(2^|S|-1)/(1-a(S))` in the fixed-`S` limit, where `a(S)=prod_(p in S) p/(p+1)` is the anchored squarefree mass. The first `s` primes minimize `a(S)` at fixed coordinate count. PNT then gives `a_s=(log s)^(-1+o(1))`, so reducing anchor exposure to at most `alpha` requires `s_alpha=exp(alpha^(-1+o(1)))` prime coordinates and the best parent load inside this direct family is `exp(exp(alpha^(-1+o(1))))`. Residual depth is already singly exponential. The frame stays coercive; it is the source/architecture bill that explodes.

This is not a universal lower bound for every divisor-closed anchor or every ancestry measure. It does rule out one tempting interpolation: simply enlarge the avoided-prime set to make the source anchor tiny while keeping the FD-154 architecture cheap. The live question remains **anchor provenance plus architecture**. Can a Farey-native observable provide the orientation on a useful coordinate face without already encoding or reconstructing Möbius, or can a different ancestry measure/divisor geometry achieve a materially better joint law between anchor exposure and endpoint distortion? Any candidate must still prove that coefficient coercivity survives the map to the Franel--Landau destination.

## Apply the information-budget gate only after cut exposure survives

FD-144 remains a separate lower bound: even after anchoring and quantitative cut exposure are solved, `o(r_T)` arbitrary source-independent normalized ancestry tests can still be fooled along a subsequence. This is a later information threshold, not a substitute for the cut theorem. Conversely, sufficiently direct high-information coordinates may reconstruct the source and become circular.

Future ancestry proposals should therefore be audited in this order: **anchor geometry and mass -> source justification of the anchor -> parent distortion -> residual ancestry depth -> child distortion -> information/precision budget -> destination relevance**. Rank-tail asymptotics enter only when the anchor is actually rank-initial; the FD-155 double-exponential parent-load law applies only to the direct finite-prime avoidance family.

## Keep coefficient coercivity and nonlocal destination coercivity separate

FD-147--FD-155 concern binary Möbius orientations, finite `L^q` and positive divisibility-ancestry observations. FD-154 proves that excellent coefficient-side coercivity is mathematically possible with bounded depth, while FD-155 shows that thinning its direct prime-coordinate anchor can make the architecture catastrophically expensive. Neither result shows that the Farey discrepancy supplies the required anchor or that the resulting norm controls the RH-equivalent destination. Any escape must state which hypothesis changes and why the new destination does not simply reconstruct the source.
