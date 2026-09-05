# MI-003 — Fixed-time Xi memory is mesoscopic; universal Cauchy smoothing localizes the remaining source problem to near-buffer forcing and logarithmic precision

**Evidence level:** supported through XF-045; translated counting, cross-ratio rigidity, nonlinear periodic/finite-window Cauchy relaxation, and far-tail suppression are exact in their stated regimes. XF-046 is not used here while its canonical finding remains under open adversarial review.

## Core intuition

Order-one heat-time memory at height `T` lives on about `log^2 T` gaps, not in a finite collision jet or bounded stencil. Static translated counting can make a super-mesoscopic block extremely lattice-like once the borderline inverse-buffer flux budget is assumed, but static lattice-likeness alone does not recover that flux norm.

The dynamic picture is now sharper. Universal Cauchy interaction gives nonlinear spectral-gap damping on periodic blocks and input-to-state stability on finite windows; after centering, remote tails are quadratically suppressed by buffer distance. But at the full memory scale the slowest Cauchy mode relaxes only at order-one rate, so a fixed heat interval cannot manufacture the logarithmic precision needed for the flux threshold. The live source problem is therefore **near-buffer replenishment/modulation plus source-specific precision**, not generic far-tail forcing or another universal smoothing estimate.

## Strongest justified principle

XF-034--XF-040 establish the static/dynamic split. Conditional on `M V_M=O(1)`, translated Xi counting forces uniform gap flattening, vanishing total log-gap variation, and Cauchy-rigid cross-ratio conductances. XF-039 constructs a static alternating microcorrugation passing those controls while violating the inverse-buffer flux budget, whereas XF-040 shows that its exact two-gap periodic heat-flow realization is rapidly damped.

XF-041 generalizes periodic damping nonlinearly. Every bounded-contrast `q`-periodic real-simple gap trajectory has a quantitative Cauchy spectral gap; periods `q=o(log T)` are driven through the inverse-buffer amplitude scale in vanishing heat time. Persistent microscopic obstruction therefore cannot be a coherent short-period pattern.

XF-042 removes periodicity from the internal mechanism. On a finite block the centered gap shape obeys an input-to-state inequality at the same Cauchy relaxation scale; only the **centered variation** of the exterior mismatch field can replenish shape, while uniform exterior coupling is dissipative.

XF-043 first suppresses the far exterior with a super-mesoscopic physical buffer. XF-045 sharpens this using the zero-mean shape cancellation and positive diagonal sink: remote forcing is suppressed quadratically in the core-span/buffer ratio rather than linearly. Far zeros therefore cannot sustain an order-one memory-scale shape obstruction once the allowed diverging buffer is inserted.

XF-044 supplies the obstruction to finishing by universal relaxation alone. The exact slow Cauchy Fourier mode has rate `rho~1/(q s^2)`; at `q~c log^2 T` and Xi spacing `s~4pi/log T`, that rate is only order one. A fixed heat-time interval gives a fixed contraction factor, not the vanishing factor needed to reach inverse-buffer precision from a generic memory-scale perturbation.

## What remains possible

A positive continuation must use source information to control the **near-buffer forcing and slow memory-scale mode** beyond what universal Cauchy dissipation supplies. It may exploit translated counting with sharper local transport, modulation equations, a source-specific cancellation in the centered exterior field, or another mechanism that already provides logarithmic precision at memory scale.

A decisive negative would construct a source-compatible near-buffer/slow-mode forcing that survives translated counting and quadratic remote-tail suppression while maintaining `M V_M>>1` for the relevant heat interval. More periodic short waves or undifferentiated far-tail estimates are no longer distinct obstructions.

## Status / novelty

Cauchy fractional diffusion, spectral gaps, input-to-state estimates, buffer localization, and linearized slow-mode analysis are classical ingredients. The persisted synthesis is the frontier shift: **universal dynamics kills short-period microstructure and remote forcing, but its memory-scale slow mode is too slow to create the required logarithmic precision; the remaining burden is source-specific near-buffer control**.

## Falsification criterion

Construct a bounded-contrast short-period or far-tail-forced control violating XF-041/XF-045 under their hypotheses, or show that the memory-scale derivative flow contracts every small perturbation asymptotically faster than the exact slow-mode rate of XF-044. A source-specific near-buffer mechanism that closes the flux budget would extend rather than falsify the synthesis.

## Lean-formalizable core

- Nonlinear periodic Cauchy spectral-gap decay.
- Finite-window centered input-to-state inequality.
- Quadratic far-tail buffer suppression.
- Exact linearized memory-scale slow-mode rate.
- Separation between universal contraction and source-specific precision.
