# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Cross the positive-density response threshold, or prove one-sided transversality before it

**Linked intuitions:** `MI-039-periodic-scale-switching-can-create-a-supercritical-floquet-blind-mode`, `MI-041-sublinear-point-sampling-cannot-make-divisor-response-signed-coercive`.

FD-233 makes vanishing negative-capacity density necessary and sufficient for a positive lift inside a nontrivial switched-response class, and FD-234 identifies the canonical source-forced correction modulo a capacity-negligible rounding term. FD-235--FD-236 show that the fixed-profile quotient and natural capacity-normalized triangular quotient are too coarse: the canonical correction itself is switched-blind throughout the certified reservoir regime.

FD-238 shows that the common kernel of all dyadic switched finite-difference rows contains integer signed profiles with `|b_n|<=n`, exact zero response at every dyadic row, and a fixed positive fraction of linear reservoir capacity in both signs. FD-239 now rules out the obvious sparse off-grid repair. If the number of sampled divisor-response points in octave `k` is `o(2^k)`, one can still build integer signed profiles vanishing at all sampled points and dyadic endpoints while retaining macroscopic positive and negative mass.

The live response question has therefore moved to a density boundary. Does a positive-density family of source-derived response coordinates per octave become quantitatively coercive on the relevant signed class, and at what density? Or can the physical nonnegative/capacity/source-coherent correction class be shown quantitatively transverse to the sparse signed nullspace before such a budget is paid? Merely changing scalar normalization, moving finitely or sublinearly many sample points off the dyadic grid, or bundling the same coordinates cannot settle the signed problem.

## Separate the boundary obstruction from interior integrality

**Linked intuition:** `MI-040-response-space-rounding-makes-interior-integrality-asymptotically-cheap`.

FD-237 removes integer realization as an independent bulk obstruction once a real reservoir profile is safely inside the capacity box. The finite divisor-response map is lower-triangular unimodular. Rounding the response coordinates and pulling them back through its exact integer inverse produces integer occupancies with coefficient error at most `tau(n)`, while every currently used switched row changes by at most an absolute constant.

This does not solve the positive-lift problem. FD-239 also shows why adding only a sparse family of exact scalar response constraints is not enough to create bulk signed coercivity. The remaining discrete work is concentrated at the boundary and in global source coherence: prove that a real positive lift stays far enough inside finite capacities, identify a response topology with enough density or structure to exclude macroscopic signed null directions, and verify that quantization error remains negligible there.