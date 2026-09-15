# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Find a source-visible ancestry law whose information budget is coercive without reconstructing the source

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-019-sub-root-rank-observation-budgets-can-remain-uniformly-blind-to-one-common-source-wall`.

FD-117--FD-142 separate the reversible Farey skeleton, sparse/common-source escape, fixed-coordinate blindness and the opposite reconstruction boundary. One exact additive scalar with `Theta(log T)` bits can already identify the whole squarefree prefix, so coordinate count alone does not measure source information.

FD-143 established a growing blind regime `K_T M_T=o(sqrt(r_T))` for arbitrary source-independent prime-cell partitions. FD-144 strengthens the same common-source obstruction to the **sublinear-rank** scale. Using min-wise prime selectors rather than Rademacher anti-concentration, it constructs one fixed infinite prime coloring and a subsequence for which all observed normalized nonnegative ancestry tests are asymptotically blind whenever

`K_T M_T=o(r_T)`.

In the central regime `r_T~log log T`, every observation budget `o(log log T)` of this class can therefore miss a macroscopic source wall. This is a lower-bound frontier, not a proof that linear-rank observation is sufficient.

The live coefficient-side theorem must now cross a linear-rank information scale or exploit structure excluded from the matched family: source-dependent/Farey-derived tests, signed structure not covered by the nonnegative normalized class, a sharper joint observation law, or an independent theorem ruling out the matched prime-color source for the physical coefficients. Jumping directly to a source-identity coordinate remains circular.

A destination-side Fourier-skeleton coercivity theorem remains a distinct route because it could bypass coefficient recovery entirely.

## Determine the first genuinely different regime between sublinear rank and source reconstruction

FD-140 shows fixed periodic alphabets can be under-resolved; FD-144 extends blindness to arbitrary source-independent normalized ancestry observations with total complexity `o(r_T)`; FD-142 shows full prefix reconstruction is available at `Theta(log T)` bits. The useful middle regime must therefore be judged by effective resolving capacity and provenance, not by the number of named coordinates.

The decisive audit for any proposal is whether it has merely become an indirect squarefree-parent label. Noninjectivity is necessary but not sufficient: FD-144 gives a broad noninjective regime that is still noncoercive.

## Keep information equivalence, horizon entropy, scale visibility, precision, provenance and target recovery separate

A coercive law must specify which prime coordinates remain visible, how many independent source constraints are imposed at rank `r_T`, how the tests are normalized, whether they are source-independent, what precision is consumed, and how much source freedom remains. FD-144 replaces the earlier square-root union-budget obstruction by a linear-rank min-wise-selector obstruction; future ancestry claims should be tested against that stronger matched control before being treated as evidence of source recovery.