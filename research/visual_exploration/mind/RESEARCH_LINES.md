# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Treat the moving lower-source branch as closed after exact gamma recentering

**Linked intuitions:** `MI-029-fixed-margin-pair-correlation-accuracy-must-outrun-packet-conditioning` through `MI-039-wang-lower-source-crossover-is-resolution-dependent`.

VIS-282--VIS-298 separate coefficient profile, Wang's complete pair statistic, deterministic gamma structure and the source transform. After exact gamma recentering, the apparent `sqrt(log T)` and related lower-source thresholds disappear: they were proof-packaging artifacts rather than arithmetic transitions.

## Sieve the subperiod rational-rotation branches, not a generic two-dimensional strip

**Linked intuitions:** `MI-040-wang-pointwise-upper-ceiling-is-a-localization-coherence-budget` and `MI-041-wang-natural-window-is-a-taper-weighted-prime-ratio-occupancy-problem`.

VIS-299--VIS-316 reduce the natural Wang mean-square window to a taper-weighted prime-ratio occupancy problem. VIS-317 shows that scalar determinant projection loses the two prime exclusions; VIS-318 shows that a fixed determinant fibre keeps those exclusions but contains only `O(1)` same-shell lattice points.

VIS-319 resolves the representation dilemma exactly. A Bezout change of variables `(t,h)->(q,r)` is unimodular and preserves the full pair of prime residue exclusions modulo every prime, recovering the local factor `(1-1/ell)^2`. The shell becomes a long-thin skew domain: each `h` has only boundedly many `t` values, but the transverse `h` range is long.

VIS-320 reduces that domain further at the natural Wang scale. For `D<M/2`, the active shell sides do not switch across the determinant strip, its `t`-width is always below `3`, and every lattice point lies on at most three exact branches `t_j(h)=floor(U(h))-j`. The branch mask is governed by one rational rotation `{U(h)}` of exact period `max(u,v) asymp M`.

At the natural resolution `D asymp M/log log M`, the whole relevant `h` interval has length `o(M)` and therefore sees **less than one period** of that rational rotation. Full-period rational equidistribution cannot by itself solve the occupancy problem. The remaining theorem is a uniform simultaneous-prime sieve/discrepancy estimate on at most three moving rational mechanical branches over a subperiod segment, strong enough after Wang taper weighting.

## Keep local arithmetic dimension, branch geometry, subperiod length and destination taper together

Projection can preserve geometric distance while deleting arithmetic exclusions; exact fibres can preserve the exclusions while deleting averaging length. VIS-319 finds a faithful chart, and VIS-320 identifies the precise one-dimensional branch geometry inside it.

A successful argument should therefore use the actual subperiod branch mask and preserve both prime coordinates. A generic two-dimensional lattice estimate proves more than the representation needs, while full-cycle rotation balance proves less than the natural window requires. Remote worst-case clusters matter only to the extent that the Wang taper retains their mass.