# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Go below capacity scale after the sharp density-one sampling threshold

**Linked intuitions:** `MI-039-periodic-scale-switching-can-create-a-supercritical-floquet-blind-mode`, `MI-040-response-space-rounding-makes-interior-integrality-asymptotically-cheap`, `MI-041-sublinear-point-sampling-cannot-make-divisor-response-signed-coercive`, `MI-042-subfull-point-sampling-density-cannot-make-divisor-response-signed-coercive`, `MI-043-approximate-density-one-sampling-has-a-defect-plus-residual-coercivity-ledger`.

FD-238--FD-240 show that exact point samples with any fixed missing fraction leave a macroscopic signed kernel under the linear envelope `|b_n|=O(n)`. FD-241 closes the density-one endpoint: if `R(N)` counts omissions, the normalized dyadic octave mass is `O(C sqrt((R(N)+1)/N))`, and density-one omissions force capacity decay.

FD-242 now shows that exact sampled zeros are not a singular endpoint. Writing `g=mu*b=Y(m)-Y(m-1)` splits the inverted response into arbitrary increments on the sparse omission boundary and observed increments along sampled runs. With

`V_S(N)=sum_(m<=N, m,m-1 sampled) |Y(m)-Y(m-1)|/m`,

one has

`normalized octave capacity << C sqrt((R(N)+1)/N) + V_S(N)/N`.

Since `V_S(N)<=2Q_S(N)` for `Q_S(N)=sum_(m<=N,m in S)|Y(m)|/m`, density-one sampling plus `Q_S(N)=o(N)` remains capacity-coercive; sampled `Y(m)=o(m)` is sufficient. Existing signed blind profiles occupy the linear residual scale, so replacing `o(N)` by a universal `O(N)` condition is impossible without additional structure.

The live response question is therefore genuinely below this settled capacity ledger. For proper density-one sampling, what finer norm of the exact or approximate kernel can remain large? Can positivity, finite reservoir capacities or arithmetic coherence force coercivity even at linear weighted residual order? Those are source-side transversality questions rather than another interpolation in point-sample density.

## Separate boundary/source admissibility from interior integrality

FD-237 removes integer realization as an independent bulk obstruction once a real reservoir profile is safely inside the capacity box: response-space rounding followed by exact unimodular inversion produces integer occupancies with coefficient error at most `tau(n)` and only bounded changes in the switched rows used there.

FD-241--FD-242 settle the macroscopic signed-capacity point-sampling threshold and its robust approximate form. The unresolved discrete boundary is finer-than-capacity control or a proof that positivity/capacity/arithmetic coherence excludes signed directions that remain legal at the linear residual scale. None follows from integrality alone.