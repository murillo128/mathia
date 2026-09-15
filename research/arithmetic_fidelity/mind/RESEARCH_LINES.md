# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Price a source resource that survives the destination operation and the moving-parameter limit

**Linked intuitions:** `MI-001-fidelity-is-quotient-relative`, `MI-004-prime-specificity-depends-on-the-retained-analytic-layer`, `MI-018-signed-complexity-only-transfers-through-sign-regular-observations`, `MI-041-one-riesz-order-crosses-conditioning-without-moving-the-zero-discriminator`.

AF-338--AF-350 separate source richness, transform fidelity and terminal quotienting. In particular, the complete finite-order Riesz cutoff profile is exactly stable in the source-matched derivative-variation norm, while raw profile amplitude can collapse distinct sources; nevertheless an `O(X^theta)` terminal quotient still preserves Dirichlet principal parts strictly to the right of `Re s=theta`.

AF-351--AF-352 identify the fixed-order critical transition: every fixed real `delta>0` gives

`RH <=> R_delta[Lambda-1](X)=O_delta(sqrt(X))`,

whereas the unsmoothed endpoint `delta=0` cannot satisfy the same bound. AF-353 prices the fixed-parameter approach to zero: the absolute critical-zero budget diverges like `1/(2*pi*delta^2)`, while the actual cancellation-aware norm `K(delta)` is also unbounded under RH but can be much smaller.

AF-354--AF-355 show that the endpoint singularity is already visible in the physical source. Unconditionally,

`|R_delta(X_N)-R_0(X_N)| << delta X_N`

on the half-integer mesh, so sufficiently fast moving orders inherit Hardy--Littlewood endpoint oscillation. Under RH the cancellation-aware comparison improves to

`|R_delta(X_N)-R_0(X_N)| << sqrt(X_N) log^2(2X_N) min(1,delta log(2X_N))`.

Consequently every polynomially vanishing order `delta_N=N^-a`, `a>0`, is still too close to the endpoint to satisfy the sharp `O(sqrt(N))` profile under RH. The unresolved moving regime begins around the much slower scale `delta_N >=~ logloglog(N)/log^3(N)`; failure of the known obstruction there is not a positive theorem.

AF-356 separates that extremal obstruction from average spectral stability. Under RH the log-normalized profiles satisfy

`||E_delta-E_0||_(B^2)=O(delta)`

and their limiting distributions converge at the same linear scale in bounded-Lipschitz distance, even though `K(delta)->infinity`. The endpoint is therefore not generically unstable: it is specifically unstable in the uniform/extremal topology consumed by the critical bound.

AF-357 now identifies the source scale hidden by the formal smoothing parameter. The exact one-sided Beta kernel has lag variable `W_delta~Beta(delta,3/2)` with

`-delta log W_delta => Exp(1)`,

so a fixed kernel quantile lies at relative lag `exp(-Theta(1/delta))`, not at scale `delta`. It also proves that the `min(1,delta log X)` endpoint modulus is the exact worst-case order for a scalar partial-sum envelope, and remains sharp after adding a pointwise jump bound. For the RH-calibrated resources `sup|psi(x)-x|` and `|Lambda(n)-1|`, Abel/envelope sharpening alone therefore cannot improve the slow moving-order comparison.

The live theorem is to identify a **source-native cross-scale constraint on the actual prime error** that excludes the extremal profiles saturating AF-357 at the Beta-distributed lag hierarchy, with enough uniformity to control the critical supremum norm in the surviving slow regime. Candidate maximal, short-interval, signed-average, endpoint-to-past correlation or zero-phase estimates must be translated to the physical lag `w~exp(-Theta(1/delta))`; another scalar envelope, jump bound or mean-square estimate is already known to be insufficient.

## Price the actual target metric before calling a representation compressed

**Linked intuitions:** `MI-001-fidelity-is-quotient-relative`, `MI-004-prime-specificity-depends-on-the-retained-analytic-layer`, `MI-019-faithful-translation-lifts-are-affine`, `MI-020-prime-tail-localization-has-an-information-conservation-law`, `MI-041-one-riesz-order-crosses-conditioning-without-moving-the-zero-discriminator`.

Localization, contraction, lifting and smoothing can move or attenuate information without making it cheaper in the metric used by the final theorem. AF-349 makes this metric dependence exact: the full Riesz map is an isometry up to `r!` from local coefficient `ell^1` into derivative variation, yet there is no scale-uniform inverse modulus from raw `C^0` profile amplitude to that coefficient distance on the perfect-power controls.

AF-350 shows that failure of source recovery in `C^0` does not imply failure of every target discriminator. AF-352 adds the converse warning: arbitrarily weak fixed positive smoothing can improve endpoint conditioning without discriminator loss. AF-353--AF-355 add the limiting-parameter audit: fixed-`delta` boundedness does not imply a useful moving family, and even under RH every polynomial approach to the unsmoothed endpoint retains the endpoint oscillation at the critical scale.

AF-356 gives the sharpest topology split, while AF-357 prices the corresponding physical resolution. The smoothed family is Lipschitz at `delta=0` in Besicovitch `B^2` and in its limiting distribution while the uniform critical norm is singular; at the same time the kernel samples endpoint shells on the exponential scale `exp(-Theta(1/delta))`, and scalar `L^infinity` plus jump information is already sharp there. The missing resource is therefore neither generic continuity nor a better estimate in the same source norm, but arithmetic coupling across exactly the scales the supremum observer can exploit.

Any claimed compression must therefore name the complete composed map, destination topology, asymptotic scale, discriminator and parameter regime required there. A small transformed residual is not information loss until the destination declares it negligible; an exact inverse in a stronger topology is not endpoint progress if the final theorem retains only a weaker one; and fixed-parameter or mean-square conditioning is not a uniform resource unless its constants and source comparison remain controlled in the limit, topology and physical resolution actually used.

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

Observation order, sign density, gap occupancy, concentration profile, raw locality, smoothing order, inverse conditioning, singularity class, destination topology, physical lag resolution and destination slack are provably different resources. AF-349--AF-357 now separate the complete representation, weak terminal quotient, fixed-order critical threshold, absolute spectral conditioning cost, moving-order source obstruction, the `B^2`-stable but uniformly singular endpoint, and the exponentially thin source shells actually sampled as `delta->0`. Future work must price `source -> representation -> terminal observer` in the **actual terminal metric, asymptotic scale, discriminator and limiting parameter regime**, not infer usefulness from source richness, transformed amplitude, intermediate invertibility, fixed-parameter smoothing, average spectral stability or scalar source envelopes alone.
