# MI-012 — Regular recovery orders the full multiscale information profile, not only its dimension

**Evidence level:** supported by AF-117--AF-122; exact for the stated entropy, coherent-refinement, conditional information-dimension, and uniform-modulus recovery models

## Core intuition

Multiscale information has a hierarchy that one scalar dimension cannot capture. Finite entropy decides whether one coherent exact description can have bounded mean information; information dimension measures the linear Cesaro innovation rate of fine quantization; and the full conditional quantization-entropy profile records sublinear growth that information dimension can erase.

Regular recovery respects this hierarchy. A uniformly controlled modulus cannot create a finer information profile than the representation already carries, except through the scale change forced by that modulus. Measurable encodings without regularity can bypass the bound, so the recovery category is part of the information claim.

## Strongest justified principle

AF-117--AF-119 identify the exact-description endpoint. Finite Shannon entropy is the one-shot mean-bit gate, its finiteness is equivalent to integrability of logarithmic tolerance-rank complexity, and a nested generating quantizer hierarchy has bounded terminal entropy exactly for finite-entropy atomic sources. Independently optimized finite-tolerance codebooks do not assemble into a bounded-information coherent exact representation.

AF-120 refines the divergent side. Rényi information dimension is the Cesaro innovation rate of coherent dyadic refinement. Dimension zero therefore does not mean bounded exact information: an infinite-entropy source can have sublinear but unbounded quantization entropy.

AF-121 proves that uniformly fiberwise Lipschitz recovery cannot increase conditional information dimension. AF-122 strengthens this from one asymptotic slope to the entire conditional entropy profile. If the decoder has modulus `omega`, the target profile at resolution `k` is bounded by the representation profile at the resolution `phi_omega(k)` required to make `omega` smaller than the target tolerance, up to fixed quantization slack. Hölder recovery produces the corresponding `1/alpha` scale dilation, and composition of repairs composes the moduli.

## Evidence synthesis and boundaries

The profile order is category-relative rather than a universal measurable invariant. Digit interleavings and other merely measurable encodings can compress or rearrange fine-scale information while destroying Lipschitz or uniform-modulus control. Conversely, a regular decoder may be perfectly faithful even when the profile diverges, provided the destination has the same or cheaper multiscale budget.

Thus a concrete arithmetic application should ask for the **smallest source-forced representation profile in the actual repair category**, not merely whether a finite-dimensional approximation exists or whether an information dimension vanishes.

## What remains possible

A useful next theorem would identify intrinsic moduli and conditional quantization profiles for concrete arithmetic representations, or show that a proposed lift crosses a profile lower bound only by losing the regularity/naturality required downstream. For exact generation, finite entropy/atomicity remains the stronger endpoint; for approximate or regular recovery, the full profile supplies the finer scale-sensitive gate.

## Status / novelty

Shannon entropy, Rényi information dimension, rate-distortion style quantization, and modulus-of-continuity estimates are classical. The persisted synthesis is the multiscale hierarchy: **bounded exact information, information-dimension slope, and the full conditional entropy profile are distinct resources, and regular recovery orders them at the resolution dictated by its modulus**.

## Falsification criterion

Construct a uniformly fiberwise recovery with the stated modulus whose target conditional quantization profile exceeds the representation profile after the required scale change, or an exactly generating coherent hierarchy with bounded terminal entropy for a non-atomic or infinite-entropy source under the AF-119 hypotheses.

## Lean-formalizable core

- Coherent-refinement entropy monotonicity.
- Information dimension as Cesaro innovation rate.
- Lipschitz/Hölder conditional information-dimension monotonicity.
- Uniform-modulus ordering of full conditional quantization profiles.
- Composition law for recovery moduli.
