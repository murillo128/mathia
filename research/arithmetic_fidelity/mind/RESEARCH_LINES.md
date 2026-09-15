# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Price source information after separating absolute attenuation from relative-band conditioning

**Linked intuitions:** `MI-001-fidelity-is-quotient-relative`, `MI-004-prime-specificity-depends-on-the-retained-analytic-layer`, `MI-018-signed-complexity-only-transfers-through-sign-regular-observations`, `MI-041-one-riesz-order-crosses-conditioning-without-moving-the-zero-discriminator`.

AF-351--AF-360 isolate the moving Riesz endpoint. Every fixed positive order crosses the critical regularity threshold without moving the zero discriminator; absolute endpoint defect appears first at height `T=exp(Theta(1/delta))`; bounded-ratio shells become projectively scalar after removing one common complex factor.

AF-361 resolves the finite exponentially broad escape. On a band

`T < gamma <= T exp(v/delta)`

with fixed `v`, normalize by the lower-edge scalar. The Riesz multiplier converges uniformly to the deterministic envelope `e^{-x}`, `x=delta log(gamma/T)`, so the relative condition number tends to `e^v`. The absolute lower-edge attenuation is a separate factor: if `u=delta log T`, then the operator size is `e^{-u}` and inverse amplification carries `e^{u+v}`. Finite scaled exponential width is therefore **not** intrinsically ill-conditioned after quotienting the common base attenuation.

This closes the former question “can an exponentially broad band be controlled at all?” at finite scaled width. The remaining theorem must price what the destination actually needs: an absolute noise/error floor that survives the `e^{-u}` attenuation, the diverging-width regime `v->infinity`, or source-native arithmetic information before the universal Riesz envelope. The envelope itself is not rational-prime selective.

## Price the actual target metric before calling a representation compressed

AF-349 shows exact stability in the source-matched derivative-variation norm while raw `C^0` recovery can fail. AF-359--AF-361 sharpen that separation: absolute endpoint energy, projective shape, relative-band conditioning and base attenuation are four different resources. Stable relative inversion across a finite scaled exponential band does not mean the endpoint signal is large in the absolute destination norm, and surviving phase/shape does not manufacture arithmetic specificity.

A useful source-to-target argument must therefore state the topology, physical scale, bandwidth, quotient, error floor and limiting parameter regime explicitly, then prove that the arithmetic discriminator survives that exact interface.

## Build cancellation-coherent source access to the Li root-rate class

**Linked intuitions:** `MI-021-coarse-rh-endpoints-can-still-require-deep-source-access`, `MI-022-prefix-truncation-must-respect-cancellation-orbits`.

The RH root-rate endpoint tolerates large output error but is highly sensitive to breaking its binomial cancellation orbit upstream. The remaining bridge must assemble the required cancellation coherently before taking the root-rate quotient; ordinary prefix accuracy is the wrong resource.

## Replace the conditional Schanuel codimension budget by an unconditional joint-dependence obstruction

**Linked intuitions:** `MI-023-local-completeness-can-preserve-a-root-rate-discriminator-at-zero-density` through `MI-040-unitary-zero-incidence-spends-two-algebraic-codimensions`.

AF-320--AF-336 separate exact recovery, conditioning, support-union geometry and exact incidence. The unconditional target remains to rule out the required independent polynomial relations on the common prime-phase tuple without Schanuel, or find another prime-source theorem strong enough to exclude the middle-singular fibre.

## Keep source complexity, transform fidelity, terminal loss and parameter-uniform conditioning as different currencies

Observation order, sign density, gap occupancy, concentration profile, raw locality, smoothing order, absolute attenuation, inverse conditioning, singularity class, destination topology, physical lag resolution, spectral bandwidth, projective quotient and destination slack are different resources. AF-361 adds a decisive distinction: finite `delta log R` controls **relative** inversion while `delta log T` controls **absolute** attenuation. Future work must price both rather than use “exponential bandwidth” as one undifferentiated obstruction.