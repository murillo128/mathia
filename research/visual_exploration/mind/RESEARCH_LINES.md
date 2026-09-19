# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Sieve the fixed-gate Wang path after center-gap decimation

**Linked intuitions:** `MI-040-wang-pointwise-upper-ceiling-is-a-localization-coherence-budget` and `MI-041-wang-natural-window-is-a-taper-weighted-prime-ratio-occupancy-problem`.

VIS-299--VIS-316 reduce the natural Wang mean-square window to a taper-weighted prime-ratio occupancy problem. VIS-317--VIS-318 show why scalar determinant projection and fixed determinant fibres each throw away a load-bearing resource. VIS-319 resolves the representation dilemma with a unimodular Bezout chart `(t,h)->(q,r)` that preserves both prime exclusions modulo every prime while retaining a long transverse coordinate.

VIS-320 reduces the resulting thin domain to at most three branches `t_j(h)=floor(U(h))-j` governed by one rational rotation of period `max(u,v) asymp M`. At natural resolution `D asymp M/log log M`, the physical segment is shorter than one full period, so full-cycle equidistribution is not the missing theorem.

VIS-321 removes the moving-gate complication. Consecutive branch steps are the two vectors `s_0=(-b,-a)` and `s_1=(u-b,v-a)`, with determinant `1`; all three branches are translates of the same rational mechanical/Christoffel path. The actual moving branch threshold can be frozen with only `O(1)` membership errors per branch at the natural scale.

VIS-322 then exposes a second exact coordinate inside that frozen path. Let `k=|v-u|` be the center gap and `L` the subperiod length. Decimating a branch by residue class modulo `k` makes the regular step exactly diagonal: away from at most one wrap index, a `k`-step changes `(q,r)` by `(sigma,sigma)`. Each residue class therefore becomes at most one fixed-gap diagonal run, with at most one extra split from the wrap. The number of runs is bounded by `min(k,L)+1` per branch.

The live theorem is now more structured than generic simultaneous-prime occupancy on a mechanical word. Near the diagonal, small `k` gives a few long runs of prime pairs at one fixed gap, so classical or modern fixed-gap sieve/correlation machinery may become relevant. For large `k`, the same decomposition produces many short runs, so the remaining cost is fragmentation and destination-weighted aggregation rather than gate motion or coordinate fidelity. A useful theorem should exploit this center-gap split instead of treating all slopes uniformly from the start.

## Keep local arithmetic dimension, subperiod length, center-gap fragmentation and destination taper together

The exact chart preserves the two prime coordinates, the path geometry is unimodular, the gate motion is negligible at the destination scale, and center-gap decimation turns the surviving orbit into fixed-gap diagonal pieces. What remains is the interaction of two-prime exclusion with the number and length distribution of those pieces as `(u,v)` varies.

A successful argument should therefore keep the fixed branch mask, simultaneous-prime condition, center gap `k`, run-length profile and Wang coefficient mass visible until the final estimate. Generic two-dimensional lattice bounds prove more than the representation needs; full-period rational balance proves less than the physical window requires; and a fixed-gap theorem applied without paying the `min(k,L)+1` fragmentation count may hide the actual loss. The next gain must come from arithmetic occupancy or destination-weighted cancellation on this precise decomposed object.