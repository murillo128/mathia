# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Classify the density-one endpoint, or leave pointwise response sampling

**Linked intuitions:** `MI-039-periodic-scale-switching-can-create-a-supercritical-floquet-blind-mode`, `MI-041-sublinear-point-sampling-cannot-make-divisor-response-signed-coercive`, `MI-042-subfull-point-sampling-density-cannot-make-divisor-response-signed-coercive`.

FD-233--FD-237 separate the positive-lift boundary from interior integrality. FD-238 then shows that the common kernel of all dyadic switched finite-difference rows already contains integer signed profiles with `|b_n|<=n`, exact zero response at every dyadic row and macroscopic capacity in both signs. FD-239 extends that obstruction to a certified low positive-density range of arbitrary point samples.

FD-240 removes the apparent density threshold. If a prescribed point-sampling set has octave upper density `eta<1`, pairwise resetting inside each sample cell constructs integer signed profiles whose divisor response vanishes at every requested sample and every dyadic endpoint, remains `O(m)` globally, and retains normalized octave variation at least `(1-eta)^2/(6 C_phi)` asymptotically. Both signs retain half of that macroscopic scale. Thus **no fixed point-sampling density strictly below one can make the divisor response signed-coercive**, independently of the geometry of the sampled locations.

Full all-integer response is injective, so the remaining point-sampling frontier is the density-one-but-not-full regime. Which sparse omitted sets still permit macroscopic signed capacity, and which omission geometries force a quantitative inverse estimate? If no useful response-side threshold survives there, the route must leave scalar point sampling and use a genuinely non-pointwise observable, or prove that the physical nonnegative/capacity/source-coherent correction class is quantitatively transverse to the signed nullspaces that survive every fixed missing fraction.

## Separate the boundary obstruction from interior integrality

**Linked intuition:** `MI-040-response-space-rounding-makes-interior-integrality-asymptotically-cheap`.

FD-237 removes integer realization as an independent bulk obstruction once a real reservoir profile is safely inside the capacity box. The finite divisor-response map is lower-triangular unimodular: response-space rounding followed by exact inversion produces integer occupancies with coefficient error at most `tau(n)` and only bounded changes in the currently used switched rows.

FD-240 now shows that increasing a pointwise response budget to any fixed fraction below full density still leaves macroscopic signed capacity invisible. The unresolved discrete work is therefore concentrated at a sharper boundary: density-one omission geometry, genuinely non-pointwise response information, or source-side positivity/coherence strong enough to exclude the signed constructions. None of those follows from integrality or point-sample count alone.