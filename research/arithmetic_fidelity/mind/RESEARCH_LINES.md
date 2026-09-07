# Arithmetic-fidelity research lines

This file holds the current mathematical lines of investigation suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Declare quotient, metric, source complexity, regularity, scale, and observation bandwidth together

**Linked intuitions:** `MI-007-provenance-must-survive-the-endpoint-quotient`, `MI-017-exact-sufficiency-geometry-does-not-fix-approximate-recovery-scale`.

AF-169--AF-177 show that exact finite representation and stable inversion are different questions: after the correct output quotient, local recovery is governed by a source-separation/interpolation modulus rather than by representation completeness alone. AF-180--AF-186 add adaptive positive source clusters whose exact distance stays `W_1=delta` while bounded-band observations become super-algebraically invisible when the derivative budget cannot resolve the growing cancellation order.

AF-187--AF-188 show that this obstruction is not monotone in cancellation order alone. For the actual Euler logarithm, reciprocal vertical bandwidth turns the same high-order parity cluster into a harmonic residue-class filter. Fixed positive `delta T` gives order-one visibility, while the logarithmic window `delta T log(1/delta) -> lambda` has an exact algebraic discrepancy exponent `pi sigma x/lambda` for the calibrated controls.

A stable theorem must therefore specify the output quotient and metric together with admissible source-complexity growth, derivative/regularity weight, locality cap, observation bandwidth, and any algebraic/harmonic structure of the kernel. Neither exact infinite-bandwidth sufficiency nor a derivative envelope alone determines the inverse scale.

## Compare the associated-function obstruction with kernel-specific harmonic recovery

AF-186 identifies the exact optimized upper envelope for the parity-split finite-difference mechanism under a derivative budget: `exp[-Omega_(M,n_delta)(2/(A_delta delta))]`. It remains the correct first obstruction test when only regularity information is used.

AF-187--AF-188 provide the necessary counterweight. The Euler harmonic ladder can defeat that low-band invisibility once the band reaches reciprocal separation, and the intermediate logarithmic Rayleigh window carries a continuum of algebraic fidelity exponents rather than a binary visible/invisible transition. The live problem is to derive source-class lower bounds or kernel-specific converse estimates that match these exact controls, rather than promoting the associated-function upper envelope to a universal recovery law.

## Keep provenance and endpoint sufficiency separate from conditioning

A representation can be exactly sufficient yet lose source identity after quotienting, or preserve provenance while becoming badly conditioned on an expanding source class. Recovery claims should state separately what is reconstructible, which equivalences are harmless, and at what quantitative cost the inverse remains stable.
