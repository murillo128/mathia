# Arithmetic-fidelity research lines

This file holds the current mathematical lines of investigation suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Declare quotient, metric, source complexity, regularity, scale, and observation bandwidth together

**Linked intuitions:** `MI-007-provenance-must-survive-the-endpoint-quotient`, `MI-017-exact-sufficiency-geometry-does-not-fix-approximate-recovery-scale`.

AF-169--AF-177 show that exact finite representation and stable inversion are different questions: after the correct output quotient, local recovery is governed by a source-separation/interpolation modulus rather than by representation completeness alone. AF-180--AF-185 then show a second conditioning axis. Positive local source clusters can agree on increasingly many moments while remaining exactly `W_1=delta` apart and becoming super-algebraically invisible when the observation derivatives cannot resolve the adaptive cancellation order.

AF-185 makes the Gevrey boundary explicit: for derivative growth `(m!)^q`, the natural obstruction scale contains the logarithmic penalty `[log(1/delta)]^q`. AF-186 gives the general mechanism. For arbitrary derivative weights `M_m`, the best parity-split finite-difference envelope is governed by the **truncated associated function** `Omega_(M,n_delta)(2/(A_delta delta))`, with the cancellation order capped by the locality requirement `n_delta delta -> 0`.

A stable theorem must therefore specify the output quotient and metric together with the admissible source-complexity growth, derivative/regularity weight, locality cap, and observation bandwidth. Fixed derivative order, exact infinite-bandwidth sufficiency, or a single source stratum does not control the adaptive family-wide problem.

## Use the truncated associated function as the mechanism-level resolution diagnostic

AF-186 identifies an exact optimization inside the parity-split matched-control mechanism: among all admissible local cancellation orders, the smallest forward upper envelope is `exp[-Omega_(M,n_delta)(2/(A_delta delta))]`. Super-algebraic invisibility occurs whenever this exponent dominates `log(1/delta)`.

The live question is not to treat that upper envelope as a converse theorem. It is to determine, for source classes and kernels actually used by Mathia, whether independent lower bounds or structural restrictions prevent the adaptive controls from reaching the optimized regime. Any claimed recovery threshold should be compared against this local associated-function obstruction before being interpreted as intrinsic.

## Keep provenance and endpoint sufficiency separate from conditioning

A representation can be exactly sufficient yet lose source identity after quotienting, or preserve provenance while becoming badly conditioned on an expanding source class. Recovery claims should state separately what is reconstructible, which equivalences are harmless, and at what quantitative cost the inverse remains stable.