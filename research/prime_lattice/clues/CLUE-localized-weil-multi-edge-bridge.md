---
id: CLUE-prime-lattice-localized-weil-multi-edge-bridge
type: research-clue
status: resolved
origin: mind
target_line: prime_lattice
based_on:
  - research/prime_lattice/findings/PL-264-prime-edge-vonmangoldt-local-universality.md
  - research/weil_inertia/findings/WI-238-suzuki-localized-weil-operator-turns-rh-failure-into-a-finite-prime-zero-mode.md
---

# Can accumulated prime-edge dynamics realize Suzuki's finite-radius Weil crossing?

## Observation

Prime Lattice has now isolated a sharp limitation of event-local geometry: at a prime-power threshold, the finite Connes--van Suijlekom path has a universal singular matrix jet whose arithmetic dependence is only the inserted von Mangoldt scalar and edge location. Single-edge negativity, interlacing, or Weyl-resolvent identities therefore cannot by themselves supply the missing global Weil sign.

A separate persisted source-side theorem gives a more structured finite target. Suzuki localization implies that if RH fails, there is a first finite support radius `a_*` where a localized self-adjoint Weil operator has a nonzero ground-state zero mode. At any fixed radius `a`, its kernel depends only on von Mangoldt data `Lambda(n)` for `n<=exp(2a)` together with explicit archimedean terms. Thus a global RH failure is forced into a finite-prime but nonlocal source operator.

## Research question

Can the accumulated multi-edge finite CvS source path up to a cutoff matched to `exp(2a)` be related by an explicit source-defined transform, compression, Schur complement, or quadratic-form comparison to Suzuki's localized Weil operator at radius `a`, with the original unshifted sign and first-crossing information preserved?

The desired relation must use interaction among many prime-power events and the pole/archimedean completion. It must not reduce to the universal singular jet of one edge or to a spectral shift that manufactures positivity.

## Why it may matter

This would turn PL-264's qualitative demand for a nonlocal event coupling into a concrete finite-prime destination already known to detect every RH failure. A successful bridge could replace an open-ended search for a global sign invariant by the narrower question of whether the accumulated prime-event representation controls the ground-state crossing of one localized Weil operator family.

It would also distinguish source observability from sign: the individual event law supplies the von Mangoldt atoms, while the bridge would have to explain how their joint accumulation and completion determine the actual Weil orientation.

## Decisive test

Fix one finite radius `a` and a compatible finite CvS cutoff containing all prime powers `q<=exp(2a)`. Derive the two source-side quadratic forms explicitly on a common finite test family or through a controlled projection. Then do one of the following:

- prove a comparison whose constants and sign remain stable as the finite test family expands and which sends a Suzuki zero/negative mode to a zero/negative direction of the unshifted CvS/Weil form; or
- prove that no such source-defined comparison can exist because the two constructions retain incompatible completion, support, or operator information.

As a matched control, replace the von Mangoldt weights while keeping the same universal one-edge matrix jets. Any proposed comparison that survives unchanged is still template geometry rather than the arithmetic multi-edge bridge sought here.

## Evidence boundary

At proposal time, PL-264 established only the insufficiency of single-edge singular geometry and the clue treated the relation to Suzuki's localized operator as missing. `PL-265` now resolves that bridge question by identifying both constructions with the same localized completed Weil form under the standard parameter map. This resolution does **not** establish RH positivity, convergence of zeta-zero spectra, or a uniform finite-dimensional theorem for the first crossing radius. Those remain outside the evidence of the clue.

## Research disposition

Outcome: prior-art redirect; bridge question resolved, sign problem remains open.

Resolved by:
- [[research/prime_lattice/findings/PL-265-cvs-suzuki-common-localized-weil-form.md]]

The decisive test has a stronger answer than the clue anticipated. Under the standard normalizations, the accumulated CvS path and Suzuki localization are not distinct completed quadratic forms requiring a new transform. Connes--Consani--Moscovici use the multiplicative semilocal interval `[lambda^-1,lambda]` with prime horizon `x=lambda^2`; Suzuki explicitly rewrites the same closed localized Weil form on `[-a,a]` with `a=log lambda`. Hence

\[
c=x=\lambda^2=e^{2a},\qquad L=\log c=2a,
\]

so the CvS interval `[-L/2,L/2]` and Suzuki interval `[-a,a]` agree. Suzuki's screw kernel gives the same source horizon directly: on that interval the difference variable has `|x-y|<=2a`, and its von-Mangoldt sum contains only `q<=e^{2a}`.

Accordingly, on the defining finite Galerkin family, the CvS matrix already evaluates the same **unshifted localized Weil quadratic form** represented in the continuum by Suzuki's canonical self-adjoint operator `A_a`. The sign comparison on the common test subspace is therefore exact; it is not a new Schur complement or spectral shift.

This does not resolve the RH-facing motivation. The identity supplies no reason that the specific zeta Weil form is nonnegative. Nor does fixed-radius Galerkin completeness automatically give uniform control of the *first crossing radius* as the finite dimension grows. `PL-261` already gives form-core detectability at fixed semilocal scale, while `PL-262` warns that expanding-window analytic conclusions require quantitative stability. The live target is therefore a source-forced sign theorem or a quantitative moving-radius/large-window limit for the **common** form, not a bridge between CvS and Suzuki.

The matched-control test also survives in the narrower form expected from `PL-264`: changing the source weights while retaining the same one-edge templates still leaves the representation bridge intact. What changes is the global signed arithmetic content. Therefore the existence of the bridge itself is template geometry; any future advance must use a zeta-specific global relation that forces the original Weil orientation rather than merely repackaging the accumulated prime-power events.
