# MI-003 — Fixed-time Xi memory is mesoscopic; counting permits the slow wave but the endpoint explicit formula selects against it

**Evidence level:** supported through XF-049; the source-compatible nonlinear memory-wave control, endpoint explicit-formula selector, and finite Volterra Fourier transport are exact in their stated regimes, while infinite localized propagation remains open

## Core intuition

Order-one heat-time memory at height `T` lives on about `log^2 T` gaps, not in a finite collision jet or bounded stencil. Universal Cauchy dynamics does not eliminate the slowest mode at the precision needed for the inverse-buffer flux gate: XF-047 gives an exact nonlinear memory wave that survives fixed heat time while satisfying the counting information previously consumed by the line.

But this matched control is not source-complete. At the endpoint, the explicit formula gives the actual Xi zero measure a fixed prime-free low-frequency gap. The critical memory wave has a detectable Fourier coefficient inside that gap and is therefore excluded unless another low-frequency structure compensates it. The remaining problem is no longer to discover some unspecified source-specific cancellation; it is to **transport this endpoint low-frequency selector through the localized infinite heat flow**.

## Strongest justified principle

XF-034--XF-046 establish the static/dynamic localization. Conditional on the inverse-buffer flux budget, translated counting forces lattice/Cauchy rigidity; short-period nonlinear modes are damped; finite windows are input-to-state stable; and remote forcing is suppressed quadratically by buffering. The memory-scale slow Cauchy mode nevertheless has only order-one relaxation on fixed heat time.

XF-047 makes that obstruction nonlinear and source-count compatible. A `q~log^2 T` periodic gap wave with relative amplitude `kappa/q^2` evolves under the exact logarithmic-particle dynamics with memory-mode decay rate tending to `1/4`, while `M V_M` stays bounded away from zero for any fixed heat interval. Every local span differs from the corrected source lattice by far less than the counting tolerance. Thus counting plus universal repulsion cannot force the desired flux smallness.

XF-048 adds the missing source selector at `t=0`. In the `H_0` zero coordinate, the explicit-formula arithmetic frequencies start at `log 2/2`, whereas the memory frequency is `Theta(1/log T)`. A Gaussian of physical width `Theta(log^3 T)` isolates that low frequency while its prime-power Fourier samples are exponentially suppressed. The actual endpoint zero statistic is `o(1)`; the coherent XF-047 wave gives a nonzero limiting response. Hence the exact wave cannot occur in the endpoint Xi source without compensating low-frequency structure.

XF-049 identifies the relevant transport architecture. For every finite real-simple polynomial heat flow, the positive-frequency zero characteristic sum satisfies an exact Volterra equation depending only on frequencies between `0` and the target frequency. Linearization about flat density reproduces exactly the XF-047 slow-mode rate. The missing step is to preserve this one-sided structure after renormalizing the infinite Xi zero measure and applying the `Theta(log^3 T)` spatial taper.

## What remains possible

A positive continuation should prove an `o(1)` localized transport estimate for the prime-free memory coefficient over the fixed heat interval, controlling renormalization, taper commutators, and buffer errors. That would let the endpoint explicit formula exclude the critical coherent slow mode dynamically and could unlock the conditional Cauchy-rigidity/coercivity machinery.

A decisive negative would construct a source-compatible localized Xi-like flow in which the endpoint low-frequency coefficient is small but the infinite/tapered dynamics generates the required compensating memory coefficient despite the finite Volterra triangularity. More counting estimates, periodic controls, or undifferentiated far-tail bounds no longer address the exact missing step.

## Status / novelty

The explicit formula, complex Burgers/Calogero pole dynamics, Cauchy fractional relaxation, and Gaussian Fourier localization are classical ingredients. The persisted synthesis is the frontier shift: **the memory-scale wave survives the previously used source counts, but the actual endpoint explicit formula excludes it in a prime-free Fourier band; the unresolved burden is dynamic preservation of that source-selected band under the infinite localized Xi flow**.

## Falsification criterion

Construct an XF-047-scale coherent endpoint wave consistent with the XF-048 explicit-formula statistic, or show that the finite positive-frequency Volterra law admits direct high-to-low generation contradicting XF-049. A rigorous infinite localized transport theorem would extend and close the current frontier rather than falsify it.

## Lean-formalizable core

- Source-compatible periodic memory-wave estimates.
- Explicit prime-free Fourier-gap probe calculation.
- Finite positive-frequency Volterra evolution identity.
- Exact match between Burgers linearization and the memory slow-mode rate.
