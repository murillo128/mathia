# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Go below capacity scale after the sharp density-one point-sampling threshold

**Linked intuitions:** `MI-039-periodic-scale-switching-can-create-a-supercritical-floquet-blind-mode`, `MI-040-response-space-rounding-makes-interior-integrality-asymptotically-cheap`, `MI-041-sublinear-point-sampling-cannot-make-divisor-response-signed-coercive`, `MI-042-subfull-point-sampling-density-cannot-make-divisor-response-signed-coercive`.

FD-238--FD-240 show that exact point samples with any fixed missing fraction leave a macroscopic signed kernel under the linear envelope `|b_n|=O(n)`. Pairwise resetting inside sample cells produces integer profiles with exact sampled zeros, globally controlled response and positive normalized octave capacity.

FD-241 closes the remaining density-one endpoint at that scale. If `E=N\S` is the omitted set, `delta_k=|E cap B_k|/|B_k|`, and the divisor response vanishes on `S`, then

`delta_k -> 0  =>  sum_(n in B_k)|b_n| / sum_(n in B_k)n -> 0`.

More quantitatively, with `R(N)=|E cap [1,N]|` and dyadic `N`, the normalized octave mass is `O(C sqrt((R(N)+1)/N))`. Conversely, if `limsup delta_k>0`, the FD-240 construction retains a positive capacity fraction on infinitely many octaves. Hence sample density tending to one is the exact threshold for **macroscopic signed capacity coercivity** in this exact-zero, linear-envelope model.

The mechanism is sharper than a density count. Möbius inversion writes the response as partial sums of `g=mu*b`; exact zeros at consecutive sampled locations force `supp(g)` into `E union (E+1)`. Density-one omissions therefore make the increment support sparse, and the mean-square bound for `sigma_-1` prevents that sparse support from carrying linear-capacity mass.

The live response question is now below this settled scale. For a proper density-one sampling set, what finer norm of the exact kernel can still remain large, and what quantitative stability replaces support localization when sampled responses are merely small rather than exactly zero? A robust version must expose both the omitted-set geometry and the sampled residual, because `g(m)=Y(m)-Y(m-1)` is no longer literally supported on `E union (E+1)`. Separately, a physical nonnegative/source-coherent correction could still be more coercive than the unrestricted signed class, but that requires a source-side transversality statement rather than more point-sample density.

## Separate boundary/source admissibility from interior integrality

FD-237 removes integer realization as an independent bulk obstruction once a real reservoir profile is safely inside the capacity box: response-space rounding followed by exact unimodular inversion produces integer occupancies with coefficient error at most `tau(n)` and only bounded changes in the switched rows used there.

FD-241 now settles the point-sampling density question at the macroscopic signed-capacity scale. The unresolved discrete boundary is not another fixed density threshold: it is finer-than-capacity control for density-one omissions, stability under approximate response data, or a proof that positivity/capacity/arithmetic coherence excludes signed directions that remain legal in the unrestricted model. None follows from integrality alone.