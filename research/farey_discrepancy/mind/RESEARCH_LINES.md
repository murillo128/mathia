# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Add information beyond the dyadic switched kernel, or prove one-sided transversality to it

**Linked intuition:** `MI-039-periodic-scale-switching-can-create-a-supercritical-floquet-blind-mode`.

FD-233 makes vanishing negative-capacity density necessary and sufficient for a positive lift inside a nontrivial switched-response class, and FD-234 identifies the canonical source-forced correction modulo a capacity-negligible rounding term. FD-235--FD-236 show that the fixed-profile quotient and the natural capacity-normalized triangular quotient are too coarse: the canonical correction itself is switched-blind throughout the certified reservoir regime.

FD-238 shows that this is not only a poor choice of scale. The common kernel of all dyadic switched finite-difference rows contains integer signed profiles with `|b_n|<=n`, exact zero response at every dyadic row, and a fixed positive fraction of linear reservoir capacity in both signs. Therefore no stronger scalar normalization of the same dyadic coordinates can make the signed response coercive.

The live question is now structural. Either add genuinely new source-derived response coordinates—off-dyadic/all-integer or another source-forced observable—and re-prove the positive-lift equivalence there, or show that the physical nonnegative/capacity/source-coherent correction class is quantitatively transverse to the exact signed nullspace. Merely changing the normalization of the existing dyadic rows cannot settle the signed problem.

## Separate the boundary obstruction from interior integrality

**Linked intuition:** `MI-040-response-space-rounding-makes-interior-integrality-asymptotically-cheap`.

FD-237 removes integer realization as an independent bulk obstruction once a real reservoir profile is safely inside the capacity box. The finite divisor-response map is lower-triangular unimodular. Rounding the response coordinates and pulling them back through its exact integer inverse produces integer occupancies with coefficient error at most `tau(n)`, while every currently used switched row changes by at most an absolute constant.

This does not solve the positive-lift problem. A genuinely finer response topology may magnify the bounded response error, and near a capacity face the `tau(n)` coefficient perturbation may be unaffordable. The remaining discrete work is therefore concentrated at the boundary and in global source coherence: prove that a real positive lift stays far enough inside finite capacities, that exact source constraints survive the lift, and that any added response coordinates still regard quantization error as negligible.
