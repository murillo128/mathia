# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Resolve growing exact-omission geometry below the sharp arbitrary-sparse scale

**Linked intuitions:** `MI-039-periodic-scale-switching-can-create-a-supercritical-floquet-blind-mode`, `MI-040-response-space-rounding-makes-interior-integrality-asymptotically-cheap`, `MI-041-sublinear-point-sampling-cannot-make-divisor-response-signed-coercive`, `MI-042-subfull-point-sampling-density-cannot-make-divisor-response-signed-coercive`, `MI-043-approximate-density-one-sampling-has-a-defect-plus-residual-coercivity-ledger`, `MI-044-finite-exact-omissions-are-triangular-response-columns-not-arbitrary-sparse-increments`.

FD-238--FD-240 show that exact point samples with any fixed missing fraction leave a macroscopic signed kernel under the linear envelope `|b_n|=O(n)`. FD-241 closes the qualitative density-one endpoint, while FD-242 splits approximate recovery into an omission defect and the weighted sampled-run residual `V_S(N)/N`.

FD-243's entropy-scale omission bound is not sharp for arbitrary sparse reciprocal-divisor mass. FD-244 proves the correct scale, up to constants,

`sum_(m in A) sigma_-1(m) << N delta log(e+log(1/delta))`,

with matching primorial-density examples. Hence the relaxed density-one ledger becomes

`normalized octave capacity << C eta_N log(e+log(1/eta_N)) + V_S(N)/N`,

where `eta_N=min(1,2R(N)/N)`. The weighted-residual barrier remains unchanged.

FD-245 then shows why even this sharp sparse-set norm need not be the exact sampling norm. A missing response value produces the paired column `Y(m)(1_(m|n)-1_((m+1)|n))`, and a set of `K` exact omissions is triangular in increasing omission location. For fixed `K`,

`sum_(n<=N)|b_n| <= 2CN(2^K-1)`,

so the double-log factor disappears completely; the linear `N` scale is already sharp for one omission. The current `2^K` bound, however, loses usefulness when `K` grows.

The live response-side question is now the **growing exact-omission operator norm**. What is the sharp transition, as `K=K(N)` grows, between the finite triangular-column regime and the arbitrary sparse reciprocal-divisor envelope? Which omission configurations maximize the norm, and does exact adjacency/divisibility geometry retain a gain beyond the relaxed `eta log log(1/eta)` scale for any nontrivial growing range? Separately, can positivity, finite reservoir capacities or arithmetic coherence force coercivity at the still-admissible linear weighted-residual scale? That second question is source-side transversality, not omission-density interpolation.

## Separate boundary/source admissibility from interior integrality

FD-237 removes integer realization as an independent bulk obstruction once a real reservoir profile is safely inside the capacity box: response-space rounding followed by exact unimodular inversion produces integer occupancies with coefficient error at most `tau(n)` and only bounded changes in the switched rows used there.

FD-241--FD-245 now separate three different objects: the qualitative density-one threshold, the sharp arbitrary-sparse omission envelope, and the stricter finite exact-omission image created by response columns. None supplies the missing physical source theorem. The unresolved discrete boundary is the growing-defect exact column norm and, independently, a proof that positivity/capacity/arithmetic coherence excludes signed directions that remain legal at linear residual scale. Integrality alone supplies neither.