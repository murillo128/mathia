# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Price source information after separating absolute attenuation, target conditioning and arithmetic specificity

**Linked intuitions:** `MI-001-fidelity-is-quotient-relative`, `MI-004-prime-specificity-depends-on-the-retained-analytic-layer`, `MI-018-signed-complexity-only-transfers-through-sign-regular-observations`, `MI-041-one-riesz-order-crosses-conditioning-without-moving-the-zero-discriminator`.

AF-351--AF-360 isolate the moving Riesz endpoint. Every fixed positive order crosses the critical regularity threshold without moving the zero discriminator; absolute endpoint defect appears first at height `T=exp(Theta(1/delta))`; bounded-ratio shells become projectively scalar after removing one common complex factor.

AF-361 resolves the finite exponentially broad worst-case escape. On a band

`T < gamma <= T exp(v/delta)`

with fixed `v`, normalization by the lower-edge scalar gives the deterministic envelope `e^{-x}`, `x=delta log(gamma/T)`, and relative condition number tending to `e^v`. The separate base-height variable `u=delta log T` controls common attenuation `e^{-u}`.

AF-362 replaces hard bandwidth by the exact target-relative recovery currency. For a declared target representer `a`, normalized optimal recovery from the diagonal Riesz channel costs

`(int e^(2x) dmu_a(x))^(1/2)`,

where `mu_a` is the target-energy distribution on scaled log-frequency. Thus `v->infinity` is not itself fatal: a target remains uniformly recoverable precisely when its energy has uniformly bounded exponential second moment. Conversely, energy placed near the moving upper edge pays the full `e^v` cost. Hard scaled width is the vector worst-case proxy, not the intrinsic cost of every target.

AF-363 computes that currency for the source-independent Sobolev/Bessel probes `a_gamma^(beta,y0)=(1+gamma^2)^(-beta/2)e^(i gamma y0)`. Fixed scaled bands have a sharp half-order transition: `beta<1/2` pays the full normalized `e^v` edge cost, whereas `beta>1/2` has normalized recovery modulus tending to `1`.

AF-364 now resolves the critical endpoint. Under the inherited RH zero-channel interpretation and the known positive lower density of distinct zeros, `beta=1/2` has a two-sided fixed-band envelope governed by the explicit logarithmic profile `R(u,v)` and, on growing scaled bands,

`K_(1/2)=Theta(e^v/sqrt(v))`.

If the distinct-zero proportion has an asymptotic density, the unknown density cancels and the fixed-band limit is exactly `R(u,v)^(1/2)`. The absolute recovery cost still multiplies by `e^u`, giving `Theta(e^(u+v)/sqrt(v))` on growing critical bands. The square-root bandwidth discount is target-energy geometry, not arithmetic specificity; matched frequency systems with comparable counting density reproduce the same scale.

The remaining theorem must therefore identify an **independently specified arithmetic discriminator** and price all three currencies that reach it: absolute error/noise after the `e^{-u}` attenuation, target regularity/Picard mass under the normalized envelope, and rational-prime specificity. Choosing or adapting the target after seeing the multiplier merely hides the inverse cost.

## Determine whether an arithmetic discriminator occupies the favorable side of the target-recovery law

**Linked intuition:** `MI-041-one-riesz-order-crosses-conditioning-without-moving-the-zero-discriminator`.

The conditioning classification itself is now sharp enough to stop extrapolating from generic bandwidth. Subcritical source-native probes pay `e^v`, the critical half-order probe pays `e^v/sqrt(v)` on growing bands, and supercritical probes remove the differential band cost on fixed bands. None of those probes is yet a rational-prime selector.

The next sharp question is therefore target identification rather than another Riesz asymptotic. Starting from a destination quantity specified independently of the Riesz multiplier, derive its zero-side representer or spectral-energy measure, determine whether it lies below, at or above the half-order threshold, and compare its resulting `e^u`-weighted recovery bill with the endpoint error budget. A favorable Picard profile is useful only if the same target also distinguishes the arithmetic source from matched non-arithmetic controls.

## Build cancellation-coherent source access to the Li root-rate class

**Linked intuitions:** `MI-021-coarse-rh-endpoints-can-still-require-deep-source-access`, `MI-022-prefix-truncation-must-respect-cancellation-orbits`.

The RH root-rate endpoint tolerates large output error but is highly sensitive to breaking its binomial cancellation orbit upstream. The remaining bridge must assemble the required cancellation coherently before taking the root-rate quotient; ordinary prefix accuracy is the wrong resource.

## Replace the conditional Schanuel codimension budget by an unconditional joint-dependence obstruction

**Linked intuitions:** `MI-023-local-completeness-can-preserve-a-root-rate-discriminator-at-zero-density` through `MI-040-unitary-zero-incidence-spends-two-algebraic-codimensions`.

AF-320--AF-336 separate exact recovery, conditioning, support-union geometry and exact incidence. The unconditional target remains to rule out the required independent polynomial relations on the common prime-phase tuple without Schanuel, or find another prime-source theorem strong enough to exclude the middle-singular fibre.

## Keep source complexity, transform fidelity, terminal loss and target-uniform conditioning as different currencies

Observation order, sign density, gap occupancy, concentration profile, raw locality, smoothing order, absolute attenuation, inverse conditioning, target spectral distribution, target regularity, singularity class, destination topology, physical lag resolution, spectral bandwidth, projective quotient and destination slack are different resources. AF-362 adds the decisive refinement that `delta log R` only controls the worst target in a band; AF-363--AF-364 show how a declared Sobolev target crosses from full edge conditioning through the critical `e^v/sqrt(v)` law to the supercritical fixed-band regime. Future work must keep that target-relative cost separate from `delta log T` attenuation and from arithmetic specificity.