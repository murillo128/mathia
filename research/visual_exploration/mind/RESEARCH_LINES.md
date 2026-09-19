# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Treat the moving lower-source branch as closed after exact gamma recentering

**Linked intuitions:** `MI-029-fixed-margin-pair-correlation-accuracy-must-outrun-packet-conditioning` through `MI-039-wang-lower-source-crossover-is-resolution-dependent`.

VIS-282--VIS-298 separate coefficient profile, Wang's complete pair statistic, deterministic gamma structure and the source transform. After exact gamma recentering, the apparent `sqrt(log T)` and related lower-source thresholds disappear: they were proof-packaging artifacts rather than arithmetic transitions.

## Aggregate determinant slices while preserving the two prime coordinates

**Linked intuitions:** `MI-040-wang-pointwise-upper-ceiling-is-a-localization-coherence-budget` and `MI-041-wang-natural-window-is-a-taper-weighted-prime-ratio-occupancy-problem`.

VIS-299--VIS-316 reduce the natural Wang mean-square window to a taper-weighted prime-ratio occupancy problem. Dense global ratio spectrum makes pointwise nearest-neighbour gaps meaningless; dyadic arithmetic shells restore finite-resolution geometry; retaining two-prime sparsity removes one logarithm; and the separated-frequency large sieve reduces a shell to the maximal occupancy `kappa_M(V)` of a Fourier cell. At the natural scale, only the taper-weighted excess over the expected two-prime density matters.

VIS-317 identifies one representation failure. The determinant coordinate `h=qv-ur` correctly measures distance from a represented ratio `u/v`, but it erases the two coordinatewise forbidden residues that supply the dimension-two prime sieve. Determinant-only residue sifting cannot produce the desired `log^(-2) M` density factor.

VIS-318 closes the opposite extreme. For a fixed same-shell represented center and fixed determinant `h`, the solutions of `vq-ur=h` are `(q,r)=(q_0,r_0)+t(u,v)`. Since the step vector itself has size `asymp M`, the shell contains only `O(1)` values of `t`—at most three in the standard `M/2<.<=2M` convention. Thus a fixed-`h` slice retains both prime coordinates but has no long one-dimensional parameter over which an asymptotic two-linear-form sieve can generate the missing density factor.

The live object is therefore the **family of short determinant slices taken together**. A successful argument must preserve `(q,r)` while averaging across the whole thin strip, or use an equivalent weighted/additive-energy formulation that retains the same prime-coordinate information. The remaining candidates include a two-coordinate upper-bound sieve on the strip, a rational/Beatty-type organization of the varying short slices, or a coefficient-weighted energy estimate. VIS-318 does not rule out any of those and applies specifically to represented same-shell centers.

## Recombine exact deterministic structure before interpreting a proof wall

The current ledger separates coefficient weights, support-sensitive spacing, actual prime-log dynamics, dyadic density, prime-pair sparsity, Fourier-cell occupancy, shell taper, determinant projection, slice length and finite-window aggregation.

VIS-317--VIS-318 give a two-sided representation audit. Projecting all the way to the scalar determinant loses sieve dimension; freezing the determinant preserves that dimension but destroys averaging length. The surviving representation must sit between those extremes: retain both prime coordinates **and** aggregate enough neighboring determinant values for arithmetic density to become visible. Remote worst-case clusters remain irrelevant unless the Wang taper gives them destination weight.