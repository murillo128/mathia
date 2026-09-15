# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Price a source resource that survives the destination operation and the moving-parameter limit

**Linked intuitions:** `MI-001-fidelity-is-quotient-relative`, `MI-004-prime-specificity-depends-on-the-retained-analytic-layer`, `MI-018-signed-complexity-only-transfers-through-sign-regular-observations`, `MI-041-one-riesz-order-crosses-conditioning-without-moving-the-zero-discriminator`.

AF-338--AF-350 separate source richness, transform fidelity and terminal quotienting. The complete finite-order Riesz cutoff profile is exactly stable in the source-matched derivative-variation norm, while raw profile amplitude can collapse distinct sources; nevertheless an `O(X^theta)` terminal quotient still preserves Dirichlet principal parts strictly to the right of `Re s=theta`.

AF-351--AF-353 identify the fixed-order critical transition and its conditioning cost. Every fixed real `delta>0` gives

`RH <=> R_delta[Lambda-1](X)=O_delta(sqrt(X))`,

whereas the endpoint `delta=0` cannot satisfy the same bound. The absolute critical-zero budget diverges like `1/(2*pi*delta^2)`, while the cancellation-aware norm is also unbounded under RH but can be much smaller.

AF-354--AF-358 show that approaching the endpoint is a genuinely moving-scale problem. Unconditionally, sufficiently fast moving orders inherit Hardy--Littlewood endpoint oscillation; under RH every polynomially vanishing order still fails the sharp root profile. Yet in logarithmic coordinates `||E_delta-E_0||_(B^2)=O(delta)` and the limiting laws are Lipschitz in bounded-Lipschitz distance. The exact Beta kernel has lag `W_delta` with `-delta log W_delta=>Exp(1)`, so fixed mass samples relative shells `exp(-Theta(1/delta))`. Under RH the smoothed zero profile satisfies `E_delta in H^s_(B,zeta) <=> s<1/2+delta`, while `E_delta-E_0 in H^s_(B,zeta) <=> s<1/2`.

AF-359 resolves the corresponding two-parameter spectral scale. If `delta_j->0`, `T_j->infinity` and `delta_j log T_j->u`, then the critical half-derivative dyadic shell energies obey

`A_delta(T)/A_0(T) -> exp(-2u)`

and

`D_delta(T)/A_0(T) -> (1-exp(-u))^2`.

Thus a subexponential zero bandwidth in `1/delta` is asymptotically blind to the endpoint defect; an order-one fraction first appears at `T=exp(Theta(1/delta))`. This is the reciprocal spectral scale to the physical Beta-kernel localization, not a general uncertainty principle.

The missing theorem is consequently not another weighted quadratic norm or a larger but subexponential zero cutoff. It must either reach the exponentially moving band in a controlled way or use source-native phase, maximal/tail, signed short-interval or cross-scale information that bypasses magnitude-only shell energy.

## Price the actual target metric before calling a representation compressed

**Linked intuitions:** `MI-001-fidelity-is-quotient-relative`, `MI-004-prime-specificity-depends-on-the-retained-analytic-layer`, `MI-019-faithful-translation-lifts-are-affine`, `MI-020-prime-tail-localization-has-an-information-conservation-law`, `MI-041-one-riesz-order-crosses-conditioning-without-moving-the-zero-discriminator`.

Localization, contraction, lifting and smoothing can move or attenuate information without making it cheaper in the metric used by the final theorem. AF-349 makes this metric dependence exact: the full Riesz map is an isometry up to `r!` from local coefficient `ell^1` into derivative variation, yet there is no scale-uniform inverse modulus from raw `C^0` profile amplitude to that coefficient distance on the perfect-power controls.

AF-350 shows that failure of source recovery in `C^0` does not imply failure of every target discriminator. AF-352 adds the converse warning: arbitrarily weak fixed positive smoothing can improve endpoint conditioning without discriminator loss. AF-356--AF-359 sharpen the limiting audit: every fixed smoothed profile crosses the half-derivative regularity boundary, the endpoint comparison stays exactly below it, and the missing endpoint energy is only detected at exponential spectral height as the smoothing vanishes. A representation is therefore useful only relative to the topology, physical scale, bandwidth and parameter regime consumed by the destination.

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

Observation order, sign density, gap occupancy, concentration profile, raw locality, smoothing order, inverse conditioning, singularity class, destination topology, physical lag resolution, spectral bandwidth and destination slack are different resources. AF-349--AF-359 now separate complete representation, weak terminal quotient, fixed-order critical threshold, absolute conditioning cost, moving-order source obstruction, average-topology stability, exponentially thin physical resolution, the exact half-derivative ceiling and the exact exponential spectral detection law. Future work must price `source -> representation -> terminal observer` in the **actual terminal metric, asymptotic scale, discriminator, bandwidth and limiting parameter regime**, not infer usefulness from source richness, transformed amplitude, intermediate invertibility, fixed-parameter smoothing or average spectral regularity alone.