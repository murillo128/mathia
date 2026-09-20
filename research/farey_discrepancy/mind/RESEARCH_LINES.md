# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Cross the certified positive-density response nullspace, or prove one-sided transversality before it

**Linked intuitions:** `MI-039-periodic-scale-switching-can-create-a-supercritical-floquet-blind-mode`, `MI-041-sublinear-point-sampling-cannot-make-divisor-response-signed-coercive`.

FD-233 makes vanishing negative-capacity density necessary and sufficient for a positive lift inside a nontrivial switched-response class, and FD-234 identifies the canonical source-forced correction modulo a capacity-negligible rounding term. FD-235--FD-236 show that the fixed-profile quotient and natural capacity-normalized triangular quotient are too coarse: the canonical correction itself is switched-blind throughout the certified reservoir regime.

FD-238 shows that the common kernel of all dyadic switched finite-difference rows contains integer signed profiles with `|b_n|<=n`, exact zero response at every dyadic row, and a fixed positive fraction of linear reservoir capacity in both signs. FD-239 now pushes the same obstruction into an explicit positive-density regime. If the prescribed response samples in octave `B_k=(2^(k-1),2^k]` have asymptotic upper density `eta<9/pi^2-3/4=0.161890652...`, one can still build integer signed profiles vanishing at every sample and dyadic endpoint, with full response `O(m)` and normalized coefficient mass at least `12/pi^2-1-(4/3)eta` asymptotically. Both signs remain macroscopic.

The live response question has therefore moved above a quantitative lower-density barrier, not merely from sparse to positive-density sampling. At what response density or with what sample structure does pointwise divisor response become quantitatively signed-coercive? The constant `9/pi^2-3/4` is only the guaranteed survival range of the present nullspace construction, not a sharp coercivity threshold; full all-integer response is injective at the opposite endpoint. Alternatively, can the physical nonnegative/capacity/source-coherent correction class be shown quantitatively transverse to these signed nullspaces before a dense response budget is paid?

## Separate the boundary obstruction from interior integrality

**Linked intuition:** `MI-040-response-space-rounding-makes-interior-integrality-asymptotically-cheap`.

FD-237 removes integer realization as an independent bulk obstruction once a real reservoir profile is safely inside the capacity box. The finite divisor-response map is lower-triangular unimodular. Rounding the response coordinates and pulling them back through its exact integer inverse produces integer occupancies with coefficient error at most `tau(n)`, while every currently used switched row changes by at most an absolute constant.

This does not solve the positive-lift problem. FD-239 now shows that even an arbitrary fixed positive fraction of exact scalar response constraints per octave can leave macroscopic signed capacity invisible when that fraction is below `9/pi^2-3/4`. The remaining discrete work is concentrated at the boundary and in global source coherence: prove that a real positive lift stays far enough inside finite capacities, identify response information dense or structured enough to exclude the signed null directions, or prove that the physical correction class cannot realize them, and verify that quantization error remains negligible there.