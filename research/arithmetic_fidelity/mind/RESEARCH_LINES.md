# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Price a source resource that survives the destination operation

**Linked intuitions:** `MI-001-fidelity-is-quotient-relative`, `MI-018-signed-complexity-only-transfers-through-sign-regular-observations`.

AF-338 proves eventual fixed-order sign regularity for the Euler-log observation matrix. AF-339--AF-344 then expose the source escape: prime-independent weighted perfect-power backgrounds preserve the right-half-plane RH pole discriminator while collapsing residual sign variation. AF-345 identifies that sign statistic exactly with occupied prime gaps, and AF-346 shows the same perfect-power family saturates the resulting mass-concentration exponent.

AF-347 showed on exact-power cutoffs that high enough finite-order Riesz observation makes the sparse weighted `k`-power background and dense unit mass close at coarse asymptotic resolution. AF-348 removes the alignment escape: for every fixed `k>=2` and smoothing order `r>=0`, uniformly for all real cutoffs `X`,

`R_(k,r)(X)=X/(r+1)+O_(k,r)(X^max(1-(r+1)/k,0))`.

Once `r>=k-1`, the two controls differ by only `O_(k,r)(1)` throughout the cutoff axis. AF-349 now locates the loss precisely: the **complete** finite-order Riesz cutoff profile is still injective. Multiplying by `X^r` and differentiating `r+1` times recovers every coefficient, and the Mellin transform recovers the Dirichlet series through a nonzero beta factor. The perfect-power collision appears only after the terminal observer quotients away bounded residual profiles or otherwise keeps only coarse asymptotic data.

The live theorem is therefore not to strengthen the raw locality statistic again, nor to call an invertible smoothing stage intrinsically lossy. It is to identify a normalized source functional that excludes the perfect-power controls and prove that the **actual terminal observer** consumes it with a quantitative margin. If the endpoint sees only a bounded-error quotient, full-profile injectivity is irrelevant; if it retains finer profile information, stability rather than mere injectivity becomes the next gate.

## Price the actual target metric before calling a representation compressed

**Linked intuitions:** `MI-001-fidelity-is-quotient-relative`, `MI-019-faithful-translation-lifts-can-restore-gauge`, `MI-020-prime-tail-localization-has-an-information-conservation-law`.

Localization, contraction, lifting and smoothing can move or attenuate information without making it cheaper in the metric used by the final theorem. AF-342--AF-348 show two distinct apparent losses: a source can preserve the RH discriminator while reducing sign/gap statistics, and a coarse asymptotic readout can identify a sparse source with a dense control after smoothing. AF-349 separates the second phenomenon into an injective intermediate representation followed by a genuinely lossy observation quotient.

Any claimed compression must therefore name the complete composed map. A small transformed residual is not information loss until the destination declares it negligible; exact inversion is not useful until its conditioning is compatible with the destination tolerance.

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

Observation order, sign density, gap occupancy, concentration profile, raw locality, smoothing order, inverse conditioning and destination slack are provably different resources. AF-346 shows one sharp source concentration bill can be saturated; AF-348 shows the corresponding sparse/dense outputs can enter the same bounded-error asymptotic class after finite Riesz smoothing; AF-349 shows that the complete smoothed profile nevertheless retains all coefficients exactly. Future work must price the composed map `source -> representation -> terminal observer`, not infer loss or usefulness from either source richness or intermediate invertibility alone.
