# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Price a source resource that survives the destination operation and the moving-parameter limit

**Linked intuitions:** `MI-001-fidelity-is-quotient-relative`, `MI-004-prime-specificity-depends-on-the-retained-analytic-layer`, `MI-018-signed-complexity-only-transfers-through-sign-regular-observations`, `MI-041-one-riesz-order-crosses-conditioning-without-moving-the-zero-discriminator`.

AF-338--AF-350 separate source richness, transform fidelity and terminal quotienting. The complete finite-order Riesz cutoff profile is exactly stable in the source-matched derivative-variation norm, while raw profile amplitude can collapse distinct sources; nevertheless an `O(X^theta)` terminal quotient still preserves Dirichlet principal parts strictly to the right of `Re s=theta`.

AF-351--AF-353 identify the fixed-order critical transition and its conditioning cost. Every fixed real `delta>0` gives

`RH <=> R_delta[Lambda-1](X)=O_delta(sqrt(X))`,

whereas the endpoint `delta=0` cannot satisfy the same bound. The absolute critical-zero budget diverges like `1/(2*pi*delta^2)`, while the cancellation-aware norm is also unbounded under RH but can be much smaller.

AF-354--AF-357 show that approaching the endpoint is a genuinely moving-scale problem. Unconditionally, sufficiently fast moving orders inherit Hardy--Littlewood endpoint oscillation; under RH every polynomially vanishing order still fails the sharp root profile. Yet in logarithmic coordinates `||E_delta-E_0||_(B^2)=O(delta)` and the limiting laws are Lipschitz in bounded-Lipschitz distance. The exact Beta kernel has lag `W_delta` with `-delta log W_delta=>Exp(1)`, so fixed mass samples relative shells `exp(-Theta(1/delta))`; the `min(1,delta log X)` endpoint modulus is sharp for every argument based only on a scalar partial-sum envelope, even with pointwise jump bounds.

AF-358 now identifies the exact quadratic spectral ceiling behind that topology split. Under RH,

`E_delta in H^s_(B,zeta) <=> s<1/2+delta`,

but for every fixed `delta>0`,

`E_delta-E_0 in H^s_(B,zeta) <=> s<1/2`.

Every fixed positive order therefore has enough spectral regularity to cross the ordinary `ell^1`/uniform-convergence gate, while the comparison with the endpoint never does. For each fixed `s<1/2` the difference is still `O_s(delta)`. The missing theorem is consequently not another weighted quadratic norm: it must use source-native phase, maximal/tail, signed short-interval or cross-scale information that couples the exponentially moving spectral/physical bands seen by the supremum endpoint.

## Price the actual target metric before calling a representation compressed

**Linked intuitions:** `MI-001-fidelity-is-quotient-relative`, `MI-004-prime-specificity-depends-on-the-retained-analytic-layer`, `MI-019-faithful-translation-lifts-are-affine`, `MI-020-prime-tail-localization-has-an-information-conservation-law`, `MI-041-one-riesz-order-crosses-conditioning-without-moving-the-zero-discriminator`.

Localization, contraction, lifting and smoothing can move or attenuate information without making it cheaper in the metric used by the final theorem. AF-349 makes this metric dependence exact: the full Riesz map is an isometry up to `r!` from local coefficient `ell^1` into derivative variation, yet there is no scale-uniform inverse modulus from raw `C^0` profile amplitude to that coefficient distance on the perfect-power controls.

AF-350 shows that failure of source recovery in `C^0` does not imply failure of every target discriminator. AF-352 adds the converse warning: arbitrarily weak fixed positive smoothing can improve endpoint conditioning without discriminator loss. AF-356--AF-358 sharpen the limiting audit: the family is stable in `B^2` and in every strictly subcritical zero-Sobolev scale, every fixed smoothed profile itself crosses the half-derivative regularity boundary, but the endpoint comparison stays exactly below that boundary. A representation is therefore useful only relative to the topology, scale and parameter regime consumed by the destination.

## Build cancellation-coherent source access to the Li root-rate class

**Linked intuitions:** `MI-021-coarse-rh-endpoints-can-still-require-deep-source-access`, `MI-022-prefix-truncation-must-respect-cancellation-orbits`.

The RH root-rate endpoint tolerates large output error but is highly sensitive to breaking its binomial cancellation orbit upstream. The remaining bridge must assemble the required cancellation coherently before taking the root-rate quotient; ordinary prefix accuracy is the wrong resource.

## Replace the conditional Schanuel codimension budget by an unconditional joint-dependence obstruction

**Linked intuitions:** `MI-023-local-completeness-can-preserve-a-root-rate-discriminator-at-zero-density` through `MI-040-unitary-zero-incidence-spends-two-algebraic-codimensions`.

AF-320--AF-336 separate exact recovery, conditioning, support-union geometry and exact incidence. The unconditional target remains to rule out the required independent polynomial relations on the common prime-phase tuple without Schanuel, or find another prime-source theorem strong enough to exclude the middle-singular fibre.

## Derive an equicoercive quartic profile restriction from source structure

**Linked intuition:** `MI-034-a-sub-boundary-profile-cap-makes-quartic-euler-minimization-equicoercive`.

AF-319 closes optimizer transfer once a homogeneous profile cap `Q<=C<3` is assumed. The remaining question is provenance: derive a non-escape condition of that strength from the arithmetic/source construction rather than insert it solely to recover the desired optimizer.

## Keep source complexity, transform fidelity, terminal loss and parameter-uniform conditioning as different currencies

Observation order, sign density, gap occupancy, concentration profile, raw locality, smoothing order, inverse conditioning, singularity class, destination topology, physical lag resolution and destination slack are provably different resources. AF-349--AF-358 now separate complete representation, weak terminal quotient, fixed-order critical threshold, absolute spectral conditioning cost, moving-order source obstruction, `B^2` stability, exponentially thin source resolution and the exact half-derivative endpoint ceiling. Future work must price `source -> representation -> terminal observer` in the **actual terminal metric, asymptotic scale, discriminator and limiting parameter regime**, not infer usefulness from source richness, transformed amplitude, intermediate invertibility, fixed-parameter smoothing or average spectral regularity alone.