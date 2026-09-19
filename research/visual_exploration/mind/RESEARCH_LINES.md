# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Aggregate the near-maximally fragmented Wang regime; polynomial run lengths are already cheap enough

**Linked intuitions:** `MI-040-wang-pointwise-upper-ceiling-is-a-localization-coherence-budget` and `MI-041-wang-natural-window-is-a-taper-weighted-prime-ratio-occupancy-problem`.

VIS-299--VIS-319 reduce the natural Wang mean-square window to a faithful two-prime occupancy problem in unimodular coordinates. VIS-320--VIS-322 then compress the long-thin domain to at most three frozen mechanical branches and decimate each branch by the center gap `k=|v-u|` into fixed-gap diagonal runs, at most `min(k,L)+1` per branch.

VIS-323 removes a feared arithmetic loss in the non-maximally-fragmented regime. The exact Bézout geometry makes determinant residue and prime-pair gap the same coordinate modulo `k`, keeps all run gaps in an interval of width `<k+1`, and gives aggregate singular-series mass `sum_s ell_s S(g_s) << L+k`. Hence for `k<=L` fragmentation does not create an extra singular-series tax.

VIS-324 now inserts the classical dimension-two Selberg upper-bound sieve into that exact run decomposition. For one frozen branch and `1<=k<=L`,

`P_j << L/log^2(3+L/k) + k`.

At the natural scale `L asymp M/log log M`, every fixed `delta>0` and every center gap `k<=M^(1-delta)` therefore already satisfy the required two-prime upper-bound scale `P_j <<_delta L/log^2 M`. Polynomially long runs are no longer part of the worst-cell obstruction.

The live frontier is compressed to the **near-maximal center-gap regime** `k=M^(1-o(1))`, where the effective run length `L/k=M^(o(1))`, together with the fully fragmented range `k>L`. A continuation should use an averaging direction that survives when individual runs are too short: a multi-run sieve, coefficient-weighted energy estimate, destination-taper aggregation, or another joint statistic across many fragments. Re-proving branchwise prime-pair bounds on polynomially long runs is no longer load-bearing.

## Keep arithmetic dimension, center gap, run length, aggregation and destination taper together

The exact chart preserves both prime coordinates, gate motion is negligible at the destination scale, center-gap decimation exposes fixed-gap runs, VIS-323 neutralizes aggregate singular-series cost, and VIS-324 shows that classical branchwise sieve depth is sufficient throughout every fixed polynomial power-saving range.

The remaining price is therefore not raw fragmentation, exceptional local factors, or ordinary fixed-gap sieve theory separately. It is whether **many subpolynomial or singleton fragments can be controlled collectively** at the logarithmic saving demanded by the Wang window. Any proposed estimate should state what is being averaged across fragments, how gap and offset vary, how the Wang taper weights that aggregation, and why the gain survives the transition through `k~L` into `k>L`.

A formally stronger prime-pair theorem is irrelevant if it still needs each individual run to contain a polynomial number of samples. The useful theorem must change the unit of averaging.