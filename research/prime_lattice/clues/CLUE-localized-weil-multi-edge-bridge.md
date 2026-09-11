---
id: CLUE-prime-lattice-localized-weil-multi-edge-bridge
type: research-clue
status: resolved
origin: mind
target_line: prime_lattice
based_on:
  - research/prime_lattice/findings/PL-264-prime-edge-vonmangoldt-local-universality.md
  - research/prime_lattice/findings/PL-265-cvs-suzuki-common-localized-weil-form.md
  - research/prime_lattice/findings/PL-266-domain-monotone-weil-negative-threshold.md
  - research/weil_inertia/findings/WI-238-suzuki-localized-weil-operator-turns-rh-failure-into-a-finite-prime-zero-mode.md
---

# Can accumulated prime-edge dynamics realize Suzuki's finite-radius Weil crossing?

## Observation

Prime Lattice has isolated a sharp limitation of event-local geometry: at a prime-power threshold, the finite Connes--van Suijlekom path has a universal singular matrix jet whose arithmetic dependence is only the inserted von Mangoldt scalar and edge location. Single-edge negativity, interlacing, or Weyl-resolvent identities therefore cannot by themselves supply the missing global Weil sign.

Suzuki localization supplies a more structured finite target. If RH fails, the localized completed Weil form becomes negative at some finite support radius. At any fixed radius `a`, its kernel depends only on von Mangoldt data `Lambda(n)` for `n<=exp(2a)` together with explicit archimedean/pole terms. Thus a global RH failure is forced into a finite-prime but nonlocal source operator.

## Research question

Can the accumulated multi-edge finite CvS source path up to a cutoff matched to `exp(2a)` be related by an explicit source-defined transform, compression, Schur complement, or quadratic-form comparison to Suzuki's localized Weil operator at radius `a`, with the original unshifted sign and crossing information preserved?

The desired relation must use interaction among many prime-power events and the pole/archimedean completion. It must not reduce to the universal singular jet of one edge or to a spectral shift that manufactures positivity.

## Why it may matter

This would turn PL-264's qualitative demand for a nonlocal event coupling into a concrete finite-prime destination already known to detect every RH failure. A successful bridge could replace an open-ended search for a global sign invariant by the narrower question of whether the accumulated prime-event representation controls the ground-state sign of one localized Weil operator family.

It would also distinguish source observability from sign: the individual event law supplies the von Mangoldt atoms, while the bridge would have to explain how their joint accumulation and completion determine the actual Weil orientation.

## Decisive test

Fix one finite radius `a` and a compatible finite CvS cutoff containing all prime powers `q<=exp(2a)`. Derive the two source-side quadratic forms explicitly on a common finite test family or through a controlled projection. Then do one of the following:

- prove a comparison whose constants and sign remain stable as the finite test family expands and which sends a Suzuki zero/negative mode to a zero/negative direction of the unshifted CvS/Weil form; or
- prove that no such source-defined comparison can exist because the two constructions retain incompatible completion, support, or operator information.

As a matched control, replace the von Mangoldt weights while keeping the same universal one-edge matrix jets. Any proposed comparison that survives unchanged is still template geometry rather than the arithmetic multi-edge bridge sought here.

## Evidence boundary

At proposal time, PL-264 established only the insufficiency of single-edge singular geometry and the clue treated the relation to Suzuki's localized operator as missing. `PL-265` resolves that bridge question by identifying both constructions with the same localized completed Weil form under the standard parameter map. `PL-266` then sharpens one residual point: for the nested Laurent-core compressions of `PL-261`, pointwise fixed-radius convergence plus domain monotonicity already forces convergence of the finite **strict-negativity onset** to the continuum onset, so uniform-in-radius convergence is not required for that qualitative threshold statement.

These results do **not** establish RH positivity, convergence of zeta-zero spectra, quantitative threshold rates, moving ground-state eigenvector convergence, absence of a zero plateau, or the expanding-window analytic-transform control required by `PL-262`.

## Research disposition

Outcome: prior-art redirect; bridge question resolved, sign problem remains open.

Resolved by:
- [[research/prime_lattice/findings/PL-265-cvs-suzuki-common-localized-weil-form.md]]
- [[research/prime_lattice/findings/PL-266-domain-monotone-weil-negative-threshold.md]]

The decisive test has a stronger answer than the clue anticipated. Under the standard normalizations, the accumulated CvS path and Suzuki localization are not distinct completed quadratic forms requiring a new transform. Connes--Consani--Moscovici use the multiplicative semilocal interval `[lambda^-1,lambda]` with prime horizon `x=lambda^2`; Suzuki rewrites the same closed localized Weil form on `[-a,a]` with `a=log lambda`. Hence

\[
c=x=\lambda^2=e^{2a},\qquad L=\log c=2a,
\]

so the CvS interval `[-L/2,L/2]` and Suzuki interval `[-a,a]` agree. Suzuki's screw kernel gives the same source horizon directly: on that interval the difference variable has `|x-y|<=2a`, and its von-Mangoldt sum contains only `q<=e^{2a}`.

Accordingly, on the defining finite Galerkin family, the CvS matrix evaluates the same **unshifted localized Weil quadratic form** represented in the continuum by Suzuki's canonical self-adjoint operator `A_a`. The sign comparison on the common test subspace is exact; it is not a new Schur complement or spectral shift.

`PL-266` also removes a qualitative threshold-drift concern for the nested Laurent core. If RH fails and `a_-` is the onset of strict continuum negativity, the finite negative thresholds decrease to `a_-` without any uniform-in-`a` convergence hypothesis. What remains quantitative or stronger—rates, earliest zero if a plateau exists, eigenvectors, and large-window transform convergence—still needs additional control.

None of this supplies a reason that the specific zeta Weil form is nonnegative. The live target is therefore a source-forced sign theorem or a genuinely stronger quantitative/large-window theorem for the **common** form, not a bridge between CvS and Suzuki.

The matched-control test survives: changing the source weights while retaining the same one-edge templates leaves the representation bridge and domain-monotonicity logic intact. What changes is the global signed arithmetic content. Any future advance must therefore use a zeta-specific global relation that forces the original Weil orientation rather than merely repackaging the accumulated prime-power events.
