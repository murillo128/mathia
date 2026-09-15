# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Price a source resource that survives the destination operation

**Linked intuitions:** `MI-001-fidelity-is-quotient-relative`, `MI-004-prime-specificity-depends-on-the-retained-analytic-layer`, `MI-018-signed-complexity-only-transfers-through-sign-regular-observations`, `MI-041-one-riesz-order-crosses-conditioning-without-moving-the-zero-discriminator`.

AF-338 proves eventual fixed-order sign regularity for the Euler-log observation matrix. AF-339--AF-346 expose a source escape: prime-independent weighted perfect-power backgrounds preserve the right-half-plane RH pole discriminator while collapsing residual sign variation, and the same family saturates the resulting mass-concentration exponent.

AF-347--AF-349 locate the Riesz loss precisely. Sufficiently high fixed-order Riesz observation makes sparse perfect-power backgrounds and dense unit mass differ by only `O(1)` in raw profile amplitude, yet the **complete** finite-order Riesz cutoff profile remains injective and exactly stable in the source-matched derivative-variation norm:

`TV(D^r F_r)=r! sum |a_n|`.

AF-350 calibrates the weaker terminal quotient. If two fixed-order Riesz profiles differ by `O(X^theta)`, then the difference of their Dirichlet transforms is holomorphic on `Re s>theta`; every meromorphic principal part strictly to the right of the error line survives. For `Lambda-1`, an `O(X^theta)` Riesz bound therefore gives a zero-free half-plane `Re s>theta`.

AF-351--AF-352 identify the open critical conditioning transition. For every fixed real `delta>0`,

`RH <=> R_delta[Lambda-1](X)=O_delta(sqrt(X))`,

while the unsmoothed `delta=0` profile cannot satisfy the same sharp boundary norm. The critical-zero multiplier decays like `|gamma|^(-1-delta)`, so every positive decay gain crosses the absolute-summability threshold without moving the off-critical Mellin discriminator.

AF-353 now prices that gain. The positive-ordinate absolute zero-mode budget has

`A_+(delta)=1/(2*pi*delta^2) - (log(2*pi)+gamma_E)/(2*pi*delta) + O(1)`

as `delta->0+`, while under RH the optimal prime-profile norm `K(delta)` also diverges as `delta->0+` although no rate is proved for it. The qualitative threshold is therefore cheap in exponent but singular in constants.

The live theorem is to derive a **target-scale conditioning gain from admissible source structure with quantitative parameter control**. For a moving order `delta=delta(X)->0`, what source-native estimate can offset the diverging conditioning budget without importing RH or the desired zero-free region? Any proposed gain must distinguish the exact `delta^-2` triangle-inequality spectral cost from the unknown cancellation-aware growth of the physical profile.

## Price the actual target metric before calling a representation compressed

**Linked intuitions:** `MI-001-fidelity-is-quotient-relative`, `MI-004-prime-specificity-depends-on-the-retained-analytic-layer`, `MI-019-faithful-translation-lifts-are-affine`, `MI-020-prime-tail-localization-has-an-information-conservation-law`, `MI-041-one-riesz-order-crosses-conditioning-without-moving-the-zero-discriminator`.

Localization, contraction, lifting and smoothing can move or attenuate information without making it cheaper in the metric used by the final theorem. AF-349 makes this metric dependence exact: the full Riesz map is an isometry up to `r!` from local coefficient `ell^1` into derivative variation, yet there is no scale-uniform inverse modulus from raw `C^0` profile amplitude to that coefficient distance on the perfect-power controls.

AF-350 shows that failure of source recovery in `C^0` does not imply failure of every target discriminator. AF-352 adds the converse warning: arbitrarily weak fixed positive smoothing can improve endpoint conditioning without discriminator loss. AF-353 adds the missing parameter audit: fixed-`delta` boundedness does not imply uniform stability as the representation approaches `delta=0`; the absolute spectral conditioning constant diverges quadratically and the actual critical profile norm is necessarily unbounded.

Any claimed compression must therefore name the complete composed map, destination topology, asymptotic scale, discriminator and parameter regime required there. A small transformed residual is not information loss until the destination declares it negligible; an exact inverse in a stronger topology is not endpoint progress if the final theorem retains only a weaker one; and fixed-parameter conditioning is not a uniform resource unless its constants remain controlled in the limit actually used.

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

Observation order, sign density, gap occupancy, concentration profile, raw locality, smoothing order, inverse conditioning, singularity class and destination slack are provably different resources. AF-349--AF-353 now separate five levels in one example: the complete Riesz representation preserves coefficient distance exactly in a source-matched derivative-variation norm; raw amplitude can collapse distinct sources; the quotient by `O(X^theta)` still preserves Dirichlet principal parts in `Re s>theta`; every fixed positive real Riesz order improves critical boundary conditioning without removing the zero discriminator; and the constants become singular as that order approaches the unsmoothed endpoint. Future work must price `source -> representation -> terminal observer` in the **actual terminal metric, asymptotic scale, discriminator and limiting parameter regime**, not infer loss or usefulness from source richness, transformed amplitude, intermediate invertibility or fixed-parameter smoothing alone.