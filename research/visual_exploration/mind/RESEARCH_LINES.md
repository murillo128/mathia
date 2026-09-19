# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Treat the moving lower-source branch as closed after exact gamma recentering

**Linked intuitions:** `MI-029-fixed-margin-pair-correlation-accuracy-must-outrun-packet-conditioning` through `MI-039-wang-lower-source-crossover-is-resolution-dependent`.

VIS-282--VIS-298 separate coefficient profile, Wang's complete pair statistic, deterministic gamma structure and the source transform. After exact gamma recentering, the apparent `sqrt(log T)` and related lower-source thresholds disappear: they were proof-packaging artifacts rather than arithmetic transitions.

## Sieve the unimodular Bezout strip rather than determinant fibres

**Linked intuitions:** `MI-040-wang-pointwise-upper-ceiling-is-a-localization-coherence-budget` and `MI-041-wang-natural-window-is-a-taper-weighted-prime-ratio-occupancy-problem`.

VIS-299--VIS-316 reduce the natural Wang mean-square window to a taper-weighted prime-ratio occupancy problem. VIS-317 shows that scalar determinant projection loses the two prime exclusions; VIS-318 shows that a fixed determinant fibre keeps those exclusions but contains only `O(1)` same-shell lattice points.

VIS-319 resolves the representation dilemma exactly. A Bezout change of variables `(t,h)->(q,r)` is unimodular and preserves the full pair of prime residue exclusions modulo every prime, recovering the local factor `(1-1/ell)^2`. The shell becomes a long-thin skew domain: each `h` has only boundedly many `t` values, but the transverse `h` range is long.

The live theorem is therefore no longer “find coordinates that retain sieve dimension.” Those coordinates are explicit. It is a **uniform thin-domain distribution/sieve problem**: control prime-pair occupancy in the skew Bezout strip, uniformly in the represented slope/center and strongly enough after Wang taper weighting. A slice-by-slice asymptotic is neither available nor necessary if the joint domain can be controlled directly.

## Keep local arithmetic dimension, transverse aggregation and destination taper together

Projection can preserve geometric distance while deleting arithmetic exclusions; exact fibres can preserve the exclusions while deleting averaging length. VIS-319 shows that a faithful chart can keep both resources, but they live in different coordinates.

A successful argument should therefore measure the whole long-thin domain with the Wang destination weight still visible. Remote worst-case clusters are irrelevant unless the taper prices them, and local dimension-two density is useful only if the skew-domain discrepancy is uniform enough to survive aggregation.