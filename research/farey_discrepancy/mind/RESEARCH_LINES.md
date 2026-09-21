# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Go below capacity scale after the sharp density-one sampling threshold

**Linked intuitions:** `MI-039-periodic-scale-switching-can-create-a-supercritical-floquet-blind-mode`, `MI-040-response-space-rounding-makes-interior-integrality-asymptotically-cheap`, `MI-041-sublinear-point-sampling-cannot-make-divisor-response-signed-coercive`, `MI-042-subfull-point-sampling-density-cannot-make-divisor-response-signed-coercive`, `MI-043-approximate-density-one-sampling-has-a-defect-plus-residual-coercivity-ledger`.

FD-238--FD-240 show that exact point samples with any fixed missing fraction leave a macroscopic signed kernel under the linear envelope `|b_n|=O(n)`. FD-241 closes the qualitative density-one endpoint: if `R(N)` counts omissions, density-one omissions force normalized dyadic octave capacity to decay.

FD-242 makes the exact-zero theorem robust. Writing `g=mu*b=Y(m)-Y(m-1)` splits the inverted response into arbitrary increments on the sparse omission boundary and observed increments along sampled runs. With

`V_S(N)=sum_(m<=N, m,m-1 sampled) |Y(m)-Y(m-1)|/m`,

it obtains an omission-defect term plus the exact weighted residual term `V_S(N)/N`.

FD-243 sharpens only the omission side. For `T_N={m<=N: m notin S or m-1 notin S_0}`, `rho_N=|T_N|/N`, and `eta_N=min(1,2R(N)/N)`,

`normalized octave capacity << C rho_N log(e/rho_N) + V_S(N)/N`

and hence

`normalized octave capacity << C eta_N log(e/eta_N) + V_S(N)/N`.

The improvement comes from the sparse-subset estimate `sum_(m in A) sigma_-1(m) << N delta log(e/delta)`, obtained by adapting the moment order of `n/phi(n)` to `delta=|A|/N`. The previous `sqrt(R(N)/N)` defect was the cost of stopping at the second moment, not a sharp structural threshold. Since `V_S(N)<=2Q_S(N)` for `Q_S(N)=sum_(m<=N,m in S)|Y(m)|/m`, density-one sampling plus `Q_S(N)=o(N)` remains capacity-coercive; the linear weighted-residual barrier is unchanged.

The live response-side question is now sharper: what is the actual extremal sparse-set mass of `sigma_-1` on subsets of `[1,N]`, and therefore the correct slowly varying factor replacing or confirming `delta log(e/delta)`? Any improvement immediately tightens every proper density-one exact-kernel bound without changing the divisor-response algebra. Separately, can positivity, finite reservoir capacities or arithmetic coherence force coercivity at the still-admissible linear weighted-residual scale? That second question is source-side transversality, not another omission-density interpolation.

## Separate boundary/source admissibility from interior integrality

FD-237 removes integer realization as an independent bulk obstruction once a real reservoir profile is safely inside the capacity box: response-space rounding followed by exact unimodular inversion produces integer occupancies with coefficient error at most `tau(n)` and only bounded changes in the switched rows used there.

FD-241--FD-243 settle the macroscopic signed-capacity density-one threshold, its robust approximate form, and a substantially sharper sparse-omission defect. The unresolved discrete boundary is the sharp finer-than-capacity sparse-set norm and, independently, a proof that positivity/capacity/arithmetic coherence excludes signed directions that remain legal at the linear residual scale. None follows from integrality alone.