# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Sieve the fixed-gate Wang path at the run-length frontier, not at the singular-series frontier

**Linked intuitions:** `MI-040-wang-pointwise-upper-ceiling-is-a-localization-coherence-budget` and `MI-041-wang-natural-window-is-a-taper-weighted-prime-ratio-occupancy-problem`.

VIS-299--VIS-319 reduce the natural Wang mean-square window to a faithful two-prime occupancy problem in unimodular coordinates. VIS-320--VIS-322 then compress the long-thin domain to at most three frozen mechanical branches and decimate each branch by the center gap `k=|v-u|` into fixed-gap diagonal runs, at most `min(k,L)+1` per branch.

VIS-323 removes a feared arithmetic loss in the non-maximally-fragmented regime. The exact Bézout geometry makes determinant residue and prime-pair gap the same coordinate modulo `k`, keeps all run gaps in an interval of width `<k+1`, and gives aggregate singular-series mass `sum_s ell_s S(g_s) << L+k`. Hence for `k<=L` the local Hardy--Littlewood factors cost only `O(L)` in total: fragmentation does **not** create an extra singular-series loss.

The live obstruction has therefore moved to **sieve depth versus run length**. A typical residue class contains only about `L/k` points. As `k` grows, each fixed-gap run eventually becomes too short for the available sieve/correlation theorem before the fully fragmented regime `k>L` is reached. A useful estimate should track the theorem's uniformity in the moving gap/offset against this `L/k` length, then aggregate with the Wang taper.

## Keep arithmetic dimension, center gap, run length and destination taper together

The exact chart preserves both prime coordinates, gate motion is negligible at the destination scale, center-gap decimation exposes fixed-gap runs, and VIS-323 shows that the singular-series weights are aggregate-neutral for `k<=L`. The remaining price is not raw run count or exceptional local factors separately, but whether the run-length profile provides enough samples for a uniform two-prime upper bound with the logarithmic saving Wang needs.

A continuation should therefore split by `L/k` rather than by slope vocabulary alone. Any fixed-gap theorem used here must state how its error and sieve depth depend on run length, gap and offset; otherwise a formally strong prime-pair estimate may still be too weak on the short fragments consumed by the actual window.