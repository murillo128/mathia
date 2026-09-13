# MI-010 — Aggregate gap moments force first-layer attachment, but paired magnitudes do not encode the remaining incidence

**Evidence level:** exact under the off-RH exponent-gap hypotheses of RE-088, strengthened by RE-090 for same-depth higher-layer chambers, by RE-091 at the sparse-host/second-moment frontier, and by the matched-control sharpness theorem RE-092. The withdrawn RE-089 `3/5` formulation is not current evidence. The result narrows the positive-threshold-measure carrier but does not eliminate first-layer-attached mixed cells.

RE-086 turns selection of a CA layer-`j` event as an adjacent support boundary into an ordinary-prime-gap cost. RE-087 shows that the total marginal one-sided gap pool is too abundant when selection compatibility is ignored. RE-088 instead weights selected cells by depth: sufficiently deep boundaries become threshold-negligible under an off-RH exponent gap.

RE-090 removes a different family. If both adjacent support boundaries contain the same fixed higher depth `j>=2`, their event-free chamber pulls back through the first-layer event map into a large ordinary consecutive-prime gap. Järviniemi's `0.57+epsilon` aggregate gap-length bound makes every fixed `j/j` chamber family threshold-negligible whenever `Theta>0.57`.

RE-091 shows how to attack the mixed-depth survivor without controlling each gap pointwise. A cell touching depth `r` has only `X^(1/r+o(1))` possible boundary hosts. Its first-layer inverse image is a disjoint prime-free interval contained in an ordinary prime gap. Pairing that sparse host count by Cauchy--Schwarz with Stadlmann's mean-square gap estimate produces the mass exponent

`beta_r=(1/2)(123/100+1/r)`.

For `r=3`, `beta_3=469/600`, so depth-`>=3` boundaries become threshold-negligible beyond that frontier; together with RE-090 this forces a first-layer atom on at least one boundary of almost every surviving selected cell. For `r=2`, the same formula gives `beta_2=173/200`.

RE-092 proves that the obvious paired-gap refinement does not improve those exponents. A mixed `1/r` cell forces one anchored ordinary-prime gap near physical scale `X` and another near the host scale `X^(1/r)`. Spread fixed threshold width over the natural `X^(1/r)/log X` host population. At the critical amplitude, the first-layer gap squares saturate the same Stadlmann budget that produced `beta_r`, while the required host-layer gap is only `X^(-b)(log X)^2` and eventually falls below the deterministic gap floor. The second scalar inequality is therefore asymptotically free in exactly the full-width allocation that makes the first one sharp.

This identifies the missing resource precisely. In `469/600<Theta<=173/200`, the surviving depth-2 channel cannot be removed by knowing only the two gap **magnitudes**, even if both inequalities are imposed on each same abstract cell. One must preserve the source identity of the pairing: which prime `q~sqrt(X)` produces the depth-2 event, which ordinary first-layer gap contains the corresponding inverse image, how the two appear as adjacent CA support boundaries, and whether the rightmost-maximizer orientation permits that pairing.

Thus “first-layer-attached joint selection” is not shorthand for multiplying two gap lower bounds. It is a cross-scale incidence problem. Current unconditional gap moments average over locations after exactly the conditioning that matters has been discarded. A successful continuation must recover that conditioned incidence or an equivalent selector correlation.

**Boundary.** RE-092 is a matched information-class control, not a synthetic CA fan or a construction of Robin failure. It shows sharpness of the host-count + paired-magnitude + current separate gap-moment package. For `Theta>173/200`, RE-091's depth-2 estimate already removes the mixed channel; below `469/600`, the weaker finite mixed-depth carrier remains live. Neither threshold is claimed to be an intrinsic CA phase transition.