# MI-012 — Regular recovery is governed by a stratified multiscale information budget, not only one modulus or dimension

**Evidence level:** supported by AF-117--AF-125; exact for the stated entropy, coherent-refinement, conditional information-dimension, random-resolution, and stratified recovery models

## Core intuition

Multiscale information has a hierarchy that one scalar dimension or one worst-case modulus cannot capture. Finite entropy decides whether one coherent exact description can have bounded mean information; information dimension measures only the linear Cesaro innovation rate; and the full conditional quantization profile records sublinear growth that dimension can erase.

The newer results sharpen the regularity side. Recovery need not have one uniform modulus over retained states: what matters is the **fiberwise input resolution actually needed to resolve each target scale, coupled to the information carried on that same fiber before averaging**. Rare rough fibers can be harmless when they are information-poor, while a worst-case modulus can be needlessly pessimistic.

## Strongest justified principle

AF-117--AF-119 identify the exact-description endpoint. Finite Shannon entropy is the one-shot mean-bit gate, its finiteness is equivalent to integrability of logarithmic tolerance-rank complexity, and a nested generating quantizer hierarchy has bounded terminal entropy exactly for finite-entropy atomic sources. Independently optimized finite-tolerance codebooks do not assemble into a bounded-information coherent exact representation.

AF-120 refines the divergent side: Rényi information dimension is the Cesaro innovation rate of coherent dyadic refinement, so dimension zero can coexist with unbounded sublinear exact-information cost. AF-121--AF-122 show that uniformly Lipschitz/Hölder or general uniform-modulus recovery orders conditional information dimension and the full conditional entropy profile after the scale change forced by the decoder.

AF-123 removes unnecessary worst-case uniformity for first-order dimension. Almost-surely finite fiberwise Lipschitz constants already preserve conditional information dimension; if the logarithmic Lipschitz overhead is integrable, they also give a bounded profile defect. Thus a large local condition number is not automatically fatal when its scale cost is sufficiently controlled in distribution.

AF-124 abstracts the mechanism to a random certified resolution depth `Phi_k(Y)`. A high-probability deterministic envelope gives the target-profile bound, and the probabilistic asymptotic rate `p-limsup Phi_k(Y)/k` controls the information-dimension dilation. AF-125 is sharper still: the exact global budget keeps the fiberwise mark entropy `e_M(y,Phi_k(y))` coupled to the required resolution before averaging, rather than replacing the pair by a common depth or tail quantile.

## Evidence synthesis and boundaries

The profile order is category-relative rather than a universal measurable invariant. Digit interleavings and other merely measurable encodings can rearrange fine-scale information while destroying the regularity used by the theorem. Conversely, nonuniform recovery can be faithful even with unbounded local moduli when rough fibers are rare or carry little entropy.

The relevant invariant for an application is therefore the **smallest source-forced stratified scale-transfer budget in the actual recovery category**. Worst-case regularity, information dimension, and average entropy are different projections of that budget and should not be substituted for one another.

## What remains possible

A useful next theorem should identify intrinsic fiberwise resolution depths and conditional entropy profiles for concrete arithmetic representations, or show that a proposed lift crosses a stratified profile lower bound only by losing the regularity or naturality required downstream. For exact generation, finite entropy/atomicity remains the stronger endpoint; for approximate or regular recovery, the coupled multiscale budget is the sharper gate.

## Status / novelty

Shannon entropy, Rényi information dimension, rate-distortion style quantization, regular conditional entropy, and modulus-of-continuity estimates are classical. The persisted synthesis is the hierarchy: **bounded exact information, dimension slope, high-probability scale transfer, and fiberwise stratified entropy are distinct resources, and regular recovery must respect the strongest one actually consumed by the destination**.

## Falsification criterion

Construct a recovery satisfying the AF-123--AF-125 hypotheses whose target conditional entropy profile exceeds the corresponding fiberwise/quantile budget, or an exactly generating coherent hierarchy with bounded terminal entropy for a non-atomic or infinite-entropy source under the AF-119 hypotheses.

## Lean-formalizable core

- Coherent-refinement entropy monotonicity.
- Information dimension as Cesaro innovation rate.
- Almost-sure fiberwise Lipschitz dimension monotonicity.
- Random resolution-depth profile bound.
- Stratified fiberwise entropy budget and its deterministic-envelope corollary.
