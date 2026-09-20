# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Refine the switched response topology before testing block-Mertens positivity

**Linked intuition:** `MI-039-periodic-scale-switching-can-create-a-supercritical-floquet-blind-mode`.

FD-233 makes vanishing negative-capacity density necessary and sufficient for a positive lift inside a nontrivial switched-response class, and FD-234 identifies the canonical source-forced correction as `tilde c_N=-(1/2)(1*U_N)` modulo a capacity-negligible rounding term. FD-235 shows that the fixed-profile quotient is too coarse: after freezing `N`, the correction itself is switched-blind and the affine class contains zero.

FD-236 now closes the most natural triangular repair as well. Using the physical reservoir scale `L_N=N/(D log N)` and the coupled rows `0<=j<J(N)`, the canonical block-Mertens correction has both vanishing normalized coefficient envelope and vanishing normalized switched response throughout the currently certified reservoir regime. It therefore belongs to the natural capacity-normalized triangular blind class itself. Coupling `N` to `J(N)` fixes the quantifier order but, at the natural `L_N 4^j` response scale, still quotients out the object whose one-sided distance was meant to be tested.

The live coefficient question has moved from choosing `L_N` to choosing a genuinely finer response topology. What source-forced scales `S_{N,j}=o(L_N 4^j)` on decisive rows still regard harmless reservoir adjustments as negligible while keeping the canonical correction visible? Once such a class is defined, the FD-233 positive-lift equivalence must be re-proved at that finer scale rather than imported automatically. Only then can one ask whether the normalized correction has positive one-sided distance from the nonnegative cone.

## Separate family-level coefficient positivity from discrete source realization

Even a nontrivial finer-scale positive lift would not construct an admissible prime occupancy. Integer multiplicities, finite reservoir capacities and the exact source-side constraints would still have to be realized. Conversely, failure of those discrete gates should not be folded into the coefficient-level question. The first task is now to find a non-vacuous source-derived response topology that survives FD-236; only after that quotient is nontrivial does its one-sided capacity distance become an arithmetic obstruction worth transporting to the discrete source.
