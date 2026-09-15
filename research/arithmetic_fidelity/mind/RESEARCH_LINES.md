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

AF-363 now computes that currency for a natural source-independent target family. For Sobolev/Bessel probes `a_gamma^(beta,y0)=(1+gamma^2)^(-beta/2)e^(i gamma y0)`, fixed scaled bands exhibit a sharp half-order transition: `beta<1/2` pays the full normalized `e^v` edge cost, whereas `beta>1/2` has normalized recovery modulus tending to `1`. The endpoint `beta=1/2` remains logarithmically spread and needs its own scaling analysis. Absolute recovery still separately pays the base factor `e^u`.

The remaining theorem must therefore identify a **source-native target** and price all three currencies that reach it: absolute error/noise after the `e^{-u}` attenuation, target regularity/Picard mass under the normalized envelope, and arithmetic specificity. Choosing or adapting the target after seeing the multiplier merely hides the inverse cost. Crossing the half-order regularity threshold improves conditioning but does not by itself supply a rational-prime selector.

## Price the actual target metric before calling a representation compressed

AF-349 shows exact stability in the source-matched derivative-variation norm while raw `C^0` recovery can fail. AF-359--AF-363 sharpen that separation: absolute endpoint energy, projective shape, vector worst-case conditioning, target-relative Picard cost, target Sobolev regularity and base attenuation are different resources.

A useful source-to-target argument must therefore state the topology, declared target, physical scale, bandwidth, quotient, error floor and limiting parameter regime explicitly. In the diagonal Riesz model the destination target is recoverable exactly to the extent that its energy avoids the exponentially expensive tail; AF-363 shows that natural power-law target decay can move this question across a precise `beta=1/2` boundary. This must be proved for the actual arithmetic target rather than inferred from raw bandwidth or generic smoothness alone.

## Resolve the critical half-order target rather than extrapolating from either side

**Linked intuition:** `MI-041-one-riesz-order-crosses-conditioning-without-moving-the-zero-discriminator`.

AF-363 deliberately leaves `beta=1/2` distinct. On the zero shell, the target energy is logarithmic across multiplicative scales, so neither the subcritical upper-edge concentration nor the supercritical lower-edge localization applies. The next sharp target-conditioning question is to compute the critical scaling law when `v`, `u` or the physical band are allowed to move, and to compare that law with the error budget of an independently specified arithmetic endpoint.

The critical calculation matters only as a conditioning theorem. Because the same half-order transition arises from the generic shell density, even a favorable endpoint law would still need a separate source theorem proving that the chosen target carries arithmetic information not reproduced by the matched control.

## Build cancellation-coherent source access to the Li root-rate class

**Linked intuitions:** `MI-021-coarse-rh-endpoints-can-still-require-deep-source-access`, `MI-022-prefix-truncation-must-respect-cancellation-orbits`.

The RH root-rate endpoint tolerates large output error but is highly sensitive to breaking its binomial cancellation orbit upstream. The remaining bridge must assemble the required cancellation coherently before taking the root-rate quotient; ordinary prefix accuracy is the wrong resource.

## Replace the conditional Schanuel codimension budget by an unconditional joint-dependence obstruction

**Linked intuitions:** `MI-023-local-completeness-can-preserve-a-root-rate-discriminator-at-zero-density` through `MI-040-unitary-zero-incidence-spends-two-algebraic-codimensions`.

AF-320--AF-336 separate exact recovery, conditioning, support-union geometry and exact incidence. The unconditional target remains to rule out the required independent polynomial relations on the common prime-phase tuple without Schanuel, or find another prime-source theorem strong enough to exclude the middle-singular fibre.

## Keep source complexity, transform fidelity, terminal loss and target-uniform conditioning as different currencies

Observation order, sign density, gap occupancy, concentration profile, raw locality, smoothing order, absolute attenuation, inverse conditioning, target spectral distribution, target regularity, singularity class, destination topology, physical lag resolution, spectral bandwidth, projective quotient and destination slack are different resources. AF-362 adds the decisive refinement that `delta log R` only controls the worst target in a band; AF-363 shows how an independently declared Sobolev target can cross from worst-edge conditioning to asymptotically unit normalized conditioning at `beta=1/2`. Future work must keep that target-relative cost separate from `delta log T` attenuation and from arithmetic specificity.