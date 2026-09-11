---
id: CLUE-prime-lattice-localized-weil-multi-edge-bridge
type: research-clue
status: proposed
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

No comparison between the CvS path and Suzuki's localized operator is currently established. PL-264 proves only the insufficiency of single-edge singular geometry. WI-238 supplies the finite-radius zero-mode consequence and finite-prime locality, not an identification with Prime Lattice's finite path. The clue asks for that missing bridge and must not be cited as evidence that the two operator families are equivalent or that either yields RH positivity unconditionally.
