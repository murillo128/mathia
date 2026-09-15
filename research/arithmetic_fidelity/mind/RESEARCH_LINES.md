# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Price source information after separating exact discriminator survival, target conditioning and destination consumption

**Linked intuitions:** `MI-001-fidelity-is-quotient-relative`, `MI-004-prime-specificity-depends-on-the-retained-analytic-layer`, `MI-018-signed-complexity-only-transfers-through-sign-regular-observations`, `MI-041-one-riesz-order-crosses-conditioning-without-moving-the-zero-discriminator`.

AF-351--AF-360 isolate the moving Riesz endpoint. Every fixed positive order crosses the critical regularity threshold without moving the zero discriminator; absolute endpoint defect appears first at height `T=exp(Theta(1/delta))`; bounded-ratio shells become projectively scalar after removing one common complex factor.

AF-361 resolves the finite exponentially broad worst-case escape. On a band

`T < gamma <= T exp(v/delta)`

with fixed `v`, normalization by the lower-edge scalar gives the deterministic envelope `e^{-x}`, `x=delta log(gamma/T)`, and relative condition number tending to `e^v`. The separate base-height variable `u=delta log T` controls common attenuation `e^{-u}`.

AF-362 replaces hard bandwidth by the exact target-relative recovery currency. For a declared target representer `a`, normalized optimal recovery from the diagonal Riesz channel costs

`(int e^(2x) dmu_a(x))^(1/2)`,

where `mu_a` is the target-energy distribution on scaled log-frequency. AF-363--AF-364 then give the source-native Sobolev transition: `beta<1/2` pays the full normalized `e^v` edge cost, `beta>1/2` is uniformly conditioned on every fixed scaled band, and the critical `beta=1/2` target has growing-band cost `Theta(e^v/sqrt(v))`. Absolute recovery still pays the separate factor `e^u`.

AF-365 now closes the fractional-order fidelity audit that this conditioning sequence had left open. For every fixed real `delta>=0`, the Mellin multiplier of the Riesz mean is `B(s,delta+1)`, which is zero-free on `Re s>0`. Therefore an `O(X^theta)` Riesz error forces the underlying Dirichlet-series difference to be holomorphic on `Re s>theta`: all meromorphic principal parts above the error line survive the quotient exactly. For the independently specified centered prime-only source, the surviving principal parts include the poles at zeta zeros in `Re s>1/2`; an `O_epsilon(X^(1/2+epsilon))` bound for every `epsilon>0` would exclude every off-critical zero.

This gives an exact separation that was previously only implicit. **Arithmetic discriminator survival and stable coordinate recovery are different currencies.** The same fractional Riesz channel can preserve the prime/zero pole divisor perfectly while detailed finite-band inversion costs `e^u`, `e^(u+v)`, or `e^(u+v)/sqrt(v)` depending on the target.

The missing theorem is no longer to show that some arithmetic information survives small positive Riesz order. The live problem is to identify a destination observable and error model that can **consume the preserved principal-part discriminator without first reconstructing an exponentially ill-conditioned amount of source detail**. The Mellin principal-part quotient and the Hilbert-space target-recovery problem are different categories; a bridge between them must be proved rather than inferred from either exact injectivity or a favorable Sobolev profile.

## Couple the preserved prime-pole discriminator to a stably usable endpoint

**Linked intuition:** `MI-041-one-riesz-order-crosses-conditioning-without-moving-the-zero-discriminator`.

AF-365 provides a source-specified discriminator before the channel: the meromorphic pole divisor of the centered rational-prime Dirichlet transform. Fractional Riesz smoothing does not move or cancel that divisor in the positive half-plane. AF-362--AF-364, however, show that extracting stronger coordinate-level information from the same channel can be badly conditioned.

The next sharp question is therefore a destination-interface problem. Specify the desired endpoint independently of the Riesz multiplier, determine exactly what quotient or functional of the Riesz profile it consumes, and prove whether that functional can read the pole/principal-part information under the available absolute error. If it factors through a linear Hilbert target, derive its representer and Picard profile and price the `u` and `v` costs. If it instead uses a Mellin/analytic-continuation quotient, state the topology and stability needed to infer the relevant principal part from finite or noisy data. Do not silently replace one problem by the other.

A useful endpoint must satisfy both gates: it must remain sensitive to the rational-prime pole divisor rather than a matched frequency background, and it must reach that discriminator with a quantitative modulus strong enough for the final argument. AF-365 proves exact survival; it does not provide stable numerical extraction.

## Build cancellation-coherent source access to the Li root-rate class

**Linked intuitions:** `MI-021-coarse-rh-endpoints-can-still-require-deep-source-access`, `MI-022-prefix-truncation-must-respect-cancellation-orbits`.

The RH root-rate endpoint tolerates large output error but is highly sensitive to breaking its binomial cancellation orbit upstream. The remaining bridge must assemble the required cancellation coherently before taking the root-rate quotient; ordinary prefix accuracy is the wrong resource.

## Replace the conditional Schanuel codimension budget by an unconditional joint-dependence obstruction

**Linked intuitions:** `MI-023-local-completeness-can-preserve-a-root-rate-discriminator-at-zero-density` through `MI-040-unitary-zero-incidence-spends-two-algebraic-codimensions`.

AF-320--AF-336 separate exact recovery, conditioning, support-union geometry and exact incidence. The unconditional target remains to rule out the required independent polynomial relations on the common prime-phase tuple without Schanuel, or find another prime-source theorem strong enough to exclude the middle-singular fibre.

## Keep source complexity, transform fidelity, terminal loss and target-uniform conditioning as different currencies

Observation order, sign density, gap occupancy, concentration profile, raw locality, smoothing order, absolute attenuation, inverse conditioning, target spectral distribution, target regularity, singularity class, destination topology, physical lag resolution, spectral bandwidth, projective quotient and destination slack are different resources. AF-362--AF-364 show that `delta log R` controls only a worst target unless the target-energy profile is specified. AF-365 adds the complementary fact that a zero-free transform multiplier may preserve an arithmetic singularity exactly while inverse recovery remains poorly conditioned. Future work must keep **exact discriminator survival, stable extraction, target-relative recovery and arithmetic specificity** separate until a theorem connects them at the destination.