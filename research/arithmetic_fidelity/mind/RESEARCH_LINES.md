# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Price a source resource that survives the destination operation

**Linked intuition:** `MI-018-signed-complexity-only-transfers-through-sign-regular-observations`.

AF-338 proves eventual fixed-order sign regularity for the Euler-log observation matrix. AF-339--AF-344 then expose the source escape: prime-independent weighted perfect-power backgrounds preserve the right-half-plane RH pole discriminator while collapsing residual sign variation. AF-345 identifies that sign statistic exactly with occupied prime gaps, and AF-346 shows the same perfect-power family saturates the resulting mass-concentration exponent.

AF-347 showed on exact-power cutoffs that finite Riesz smoothing can erase the much stronger raw locality contrast. AF-348 removes the alignment escape. For every fixed `k>=2` and smoothing order `r>=0`, uniformly for all real cutoffs `X`,

`R_(k,r)(X)=X/(r+1)+O_(k,r)(X^max(1-(r+1)/k,0))`.

Hence once `r>=k-1`, the sparse weighted `k`-power source is only `O_(k,r)(1)` away from dense unit mass under this observable **throughout the cutoff axis**, not merely on `X=M^k`. The terminal fractional cell does not restore locality; exact finite-difference cancellation deforms into enough high-order vanishing to preserve the same exponent.

The live theorem is therefore not to strengthen the raw locality statistic again. It is to identify a normalized source functional that excludes the perfect-power controls and prove that the intended critical-line operation preserves or consumes it with a quantitative margin. A certificate visible only before smoothing/compression is not a usable endpoint resource.

## Price the actual target metric before calling a representation compressed

**Linked intuitions:** `MI-019-faithful-translation-lifts-are-affine`, `MI-020-prime-tail-localization-has-an-information-conservation-law`.

Localization, contraction and lifting can move information without making it cheaper in the metric used by the final theorem. AF-342--AF-348 now show two distinct failure modes: a source can preserve the RH discriminator while reducing sign/gap statistics, and a later smoothing can erase even a much stronger raw locality contrast uniformly in the cutoff. Any claimed compression must identify both the source resource and the destination operator that still sees it.

## Build cancellation-coherent source access to the Li root-rate class

**Linked intuitions:** `MI-021-coarse-rh-endpoints-can-still-require-deep-source-access`, `MI-022-prefix-truncation-must-respect-cancellation-orbits`.

The RH root-rate endpoint tolerates large output error but is highly sensitive to breaking its binomial cancellation orbit upstream. The remaining bridge must assemble the required cancellation coherently before taking the root-rate quotient; ordinary prefix accuracy is the wrong resource.

## Replace the conditional Schanuel codimension budget by an unconditional joint-dependence obstruction

**Linked intuitions:** `MI-023-local-completeness-can-preserve-a-root-rate-discriminator-at-zero-density` through `MI-040-unitary-zero-incidence-spends-two-algebraic-codimensions`.

AF-320--AF-336 separate exact recovery, conditioning, support-union geometry and exact incidence. The unconditional target remains to rule out the required independent polynomial relations on the common prime-phase tuple without Schanuel, or find another prime-source theorem strong enough to exclude the middle-singular fibre.

## Derive an equicoercive quartic profile restriction from source structure

**Linked intuition:** `MI-034-a-sub-boundary-profile-cap-makes-quartic-euler-minimization-equicoercive`.

AF-319 closes optimizer transfer once a homogeneous profile cap `Q<=C<3` is assumed. The remaining question is provenance: derive a non-escape condition of that strength from the arithmetic/source construction rather than insert it solely to recover the desired optimizer.

## Keep source complexity and transport loss as different currencies

Observation order, sign density, gap occupancy, concentration profile, raw locality, smoothing order and destination slack are provably different resources. AF-346 shows one sharp source concentration bill can be saturated; AF-348 shows a stronger raw locality contrast can then disappear uniformly under a finite destination smoothing. Future work must price the composed map `source -> observation -> endpoint`, not only the richness of the source before compression.
