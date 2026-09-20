# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Refine the switched response topology before testing block-Mertens positivity

**Linked intuition:** `MI-039-periodic-scale-switching-can-create-a-supercritical-floquet-blind-mode`.

FD-233 makes vanishing negative-capacity density necessary and sufficient for a positive lift inside a nontrivial switched-response class, and FD-234 identifies the canonical source-forced correction as `tilde c_N=-(1/2)(1*U_N)` modulo a capacity-negligible rounding term. FD-235 shows that the fixed-profile quotient is too coarse: after freezing `N`, the correction itself is switched-blind and the affine class contains zero.

FD-236 now closes the most natural triangular repair as well. Using the physical reservoir scale `L_N=N/(D log N)` and the coupled rows `0<=j<J(N)`, the canonical block-Mertens correction has both vanishing normalized coefficient envelope and vanishing normalized switched response throughout the currently certified reservoir regime. It therefore belongs to the natural capacity-normalized triangular blind class itself. Coupling `N` to `J(N)` fixes the quantifier order but, at the natural `L_N 4^j` response scale, still quotients out the object whose one-sided distance was meant to be tested.

The live coefficient question has moved from choosing `L_N` to choosing a genuinely finer response topology. What source-forced scales `S_{N,j}=o(L_N 4^j)` on decisive rows still regard harmless reservoir adjustments as negligible while keeping the canonical correction visible? Once such a class is defined, the FD-233 positive-lift equivalence must be re-proved at that finer scale rather than imported automatically. Only then can one ask whether the normalized correction has positive one-sided distance from the nonnegative cone.

## Separate the boundary obstruction from interior integrality

**Linked intuition:** `MI-040-response-space-rounding-makes-interior-integrality-asymptotically-cheap`.

FD-237 removes integer realization as an independent bulk obstruction once a real reservoir profile is safely inside the capacity box. The finite divisor-response map is lower-triangular unimodular. Rounding the response coordinates and pulling them back through its exact integer inverse produces integer occupancies with coefficient error at most `tau(n)`, while every currently used switched row changes by at most an absolute constant. At the physical cell scale `K_n asymp n L_N` with `L_N->infinity`, a real fill with a `tau(n)`-sized safety margin therefore admits a uniformly switched-stable integer lift at negligible relative cost.

This does not solve the positive-lift problem. A finer topology may magnify the bounded response error, and near a capacity face the `tau(n)` coefficient perturbation may be unaffordable. The remaining discrete work is therefore concentrated at the boundary and in global source coherence: prove that the real positive lift stays far enough inside the finite capacities, that the exact source constraints survive the lift, and that the chosen finer response scales still regard the bounded quantization error as negligible.
