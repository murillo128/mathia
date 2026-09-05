# MI-005 — Pointwise selector control is not time-frequency coercivity

**Evidence level:** exact Xi-selector transport and matched finite-gap obstruction through XF-052--XF-057

## Core intuition

Excluding every coherent slow mode one frequency at a time does not control a transition quantity that can distribute its variation across many nearby frequency cells. The missing source-to-transition theorem is an **aggregate coercivity statement**, not another pointwise selector estimate.

## Strongest justified principle

XF-052--XF-054 identify a prime-free endpoint sector and transport the shrinking memory statistic uniformly over fixed heat time. XF-055--XF-056 extend the matched separation from discrete periodic harmonics to a continuous slow-frequency cone: every pure critical slow wave has order-one response at its own center, while the Xi carrier is uniformly `o(1)`.

XF-057 constructs a chirped finite-gap control whose instantaneous frequency remains inside the same slow cone and whose critical triple-flux variation stays at the borderline nonzero scale, yet every individual selector coefficient is uniformly `o(1)`. The chirp spreads the budget across many `1/M` resolution cells. Therefore a frequency supremum is noncoercive even when its center ranges continuously.

## What remains possible

A square-function, lower-frame, variation, wave-packet, or phase-space norm may aggregate the continuous selector family strongly enough to control the transition flux. Alternatively, exact Xi dynamics may forbid the chirped distribution admitted by the finite-gap control. Either route must prove its source-conditioned margin at the `q~log^2 T` memory scale.

## Status / novelty

Van der Corput bounds, chirp dispersion, frames, and time-frequency aggregation are classical themes. The line-specific synthesis is the precise inverse boundary: **continuous pointwise spectral exclusion is weaker than mesoscopic coercivity because the transition budget can spread across frequency**.

## Falsification criterion

Prove that `sup_theta |S(theta)|=o(1)` alone forces the XF transition-side flux to be `o(1)` under the hypotheses admitted by XF-057, or find an error in the chirped matched control or its uniform selector estimate.
