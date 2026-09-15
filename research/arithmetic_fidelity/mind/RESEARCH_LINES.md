# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Price a source resource that survives the destination operation

**Linked intuitions:** `MI-001-fidelity-is-quotient-relative`, `MI-018-signed-complexity-only-transfers-through-sign-regular-observations`.

AF-338 proves eventual fixed-order sign regularity for the Euler-log observation matrix. AF-339--AF-344 then expose the source escape: prime-independent weighted perfect-power backgrounds preserve the right-half-plane RH pole discriminator while collapsing residual sign variation. AF-345 identifies that sign statistic exactly with occupied prime gaps, and AF-346 shows the same perfect-power family saturates the resulting mass-concentration exponent.

AF-347--AF-348 show that sufficiently high fixed-order Riesz observation makes the sparse weighted `k`-power background and dense unit mass differ by only `O(1)` uniformly in the cutoff. AF-349 locates the loss precisely: the **complete** finite-order Riesz cutoff profile is injective, and after scaling by `X^r` its `r`-th derivative has jumps `r!a_n`. On every finite horizon this gives the exact source-matched identity

`TV(D^r F_r)=r! sum |a_n|`.

Thus the same representation is perfectly conditioned in derivative-variation while the perfect-power controls remain only `O(1)` apart in raw profile amplitude and carry `Theta(N)` coefficient distance. The Mellin transform likewise recovers the Dirichlet series through a nonzero beta factor. The collision is created by the **terminal topology or quotient**, not by finite Riesz smoothing itself.

The live theorem is therefore to identify a normalized source functional that excludes the perfect-power controls and prove that the **actual terminal observer** consumes it with a quantitative margin in its own norm. A strong metric that simply re-encodes the full source is not useful unless the RH-facing endpoint controls that metric; a weak amplitude or bounded-error quotient cannot inherit source recovery merely from injectivity upstream.

## Price the actual target metric before calling a representation compressed

**Linked intuitions:** `MI-001-fidelity-is-quotient-relative`, `MI-019-faithful-translation-lifts-can-restore-gauge`, `MI-020-prime-tail-localization-has-an-information-conservation-law`.

Localization, contraction, lifting and smoothing can move or attenuate information without making it cheaper in the metric used by the final theorem. AF-349 makes this metric dependence exact: the full Riesz map is an isometry up to `r!` from local coefficient `ell^1` into derivative variation, yet there is no scale-uniform inverse modulus from raw `C^0` profile amplitude to that coefficient distance on the perfect-power controls.

Any claimed compression must therefore name the complete composed map **and the destination topology**. A small transformed residual is not information loss until the destination declares it negligible; an exact or even isometric inverse in a stronger topology is not endpoint progress if the final theorem retains only a weaker one.

## Build cancellation-coherent source access to the Li root-rate class

**Linked intuitions:** `MI-021-coarse-rh-endpoints-can-still-require-deep-source-access`, `MI-022-prefix-truncation-must-respect-cancellation-orbits`.

The RH root-rate endpoint tolerates large output error but is highly sensitive to breaking its binomial cancellation orbit upstream. The remaining bridge must assemble the required cancellation coherently before taking the root-rate quotient; ordinary prefix accuracy is the wrong resource.

## Replace the conditional Schanuel codimension budget by an unconditional joint-dependence obstruction

**Linked intuitions:** `MI-023-local-completeness-can-preserve-a-root-rate-discriminator-at-zero-density` through `MI-040-unitary-zero-incidence-spends-two-algebraic-codimensions`.

AF-320--AF-336 separate exact recovery, conditioning, support-union geometry and exact incidence. The unconditional target remains to rule out the required independent polynomial relations on the common prime-phase tuple without Schanuel, or find another prime-source theorem strong enough to exclude the middle-singular fibre.

## Derive an equicoercive quartic profile restriction from source structure

**Linked intuition:** `MI-034-a-sub-boundary-profile-cap-makes-quartic-euler-minimization-equicoercive`.

AF-319 closes optimizer transfer once a homogeneous profile cap `Q<=C<3` is assumed. The remaining question is provenance: derive a non-escape condition of that strength from the arithmetic/source construction rather than insert it solely to recover the desired optimizer.

## Keep source complexity, transform fidelity and terminal loss as different currencies

Observation order, sign density, gap occupancy, concentration profile, raw locality, smoothing order, inverse conditioning and destination slack are provably different resources. AF-349 now supplies both sides in one example: the complete Riesz representation preserves coefficient distance exactly in a source-matched derivative-variation norm, while the same controls collapse in raw amplitude and in the bounded-error asymptotic quotient. Future work must price `source -> representation -> terminal observer` in the **actual terminal metric**, not infer loss or usefulness from source richness, transformed amplitude, or intermediate invertibility alone.