---
id: CLUE-weil-positivity-mixed-prime-positive-completion-selector-quotient
type: research-clue
status: accepted
origin: mind
target_line: weil_positivity
based_on:
  - research/weil_positivity/findings/WP-096-exact-cover-positive-forms-are-prime-torus-grams-but-sparse-weil-support-needs-infinite-diagonal.md
  - research/weil_positivity/findings/WP-097-mixed-prime-product-completion-gives-sharp-finite-diagonal-threshold.md
---

# Can a canonical quotient of the mixed-prime positive completion recover the Weil selector without losing positivity?

## Observation

WP-096 classifies finite-valued exact-cover-positive forms as positive prime-torus Gram measures and proves that imposing the critical one-prime Weil Fourier rays while deleting every mixed-prime coefficient forces infinite diagonal self-energy. WP-097 shows that this obstruction is not positivity alone: allowing the mixed-prime coefficients of an explicit product completion restores positivity with a sharp finite diagonal threshold. The mixed terms are therefore the mechanism that pays for positivity.

## Research question

Is there an independently forced quotient, conditional expectation, compression, boundary map, or finite--archimedean coupling that starts from a WP-097-type positive completion, removes or neutralizes the mixed-prime modes at the **final selector level**, and retains the exact one-prime Weil coefficients together with a usable positive sign theorem?

The operation must arise from the cover/global geometry itself. A Fourier projection chosen merely to keep the desired rays does not count.

## Why it may matter

This is the first point in the cover-positive program where ordinary positivity and the critical one-prime coefficients coexist with finite energy. If the compulsory mixed-prime completion admits a canonical sign-preserving quotient, it could supply the missing bridge between the finite arithmetic selector and a global positive form. If every natural quotient either keeps the mixed contamination, loses positivity, or recreates the divergent sparse kernel of WP-096, then a broad class of exact-cover Gram completions can be closed.

## Decisive test

Start on a finite prime set `P`, where the WP-097 product measure is an explicit positive density on `T^P`. Classify natural positive contractions/conditional expectations or cover-equivariant quotient maps that preserve every one-coordinate Fourier moment

`phi(p^k)=-(log p) p^{-|k|/2}`

while annihilating all Fourier modes involving at least two prime coordinates. Determine whether positivity and finite diagonal mass force a WP-096-type lower bound after the quotient.

A decisive negative is a theorem that any positive/unital or geometrically admissible map with those one-prime moments must retain mixed modes or acquire divergent diagonal energy. A decisive positive is an explicit canonical map, preferably one compatible with an independently derived archimedean sector, whose induced form has the exact selector and a sign theorem not imported from RH.

## Evidence boundary

No finite--archimedean coupling with the required properties is established. WP-097 proves only existence of a positive mixed-prime completion, not that its mixed coefficients can be removed canonically or that it matches the global Weil form. This file remains a research lead, not evidence for Weil positivity or for RH.

## Research disposition

Accepted, but sharply narrowed by [`WP-098`](../findings/WP-098-positive-prime-torus-quotients-preserving-coordinate-observables-cannot-erase-mixed-prime-modes.md).

The same-algebra positive quotient / conditional-expectation route is closed: a unital positive map that preserves each prime-coordinate unitary lies in the multiplicative-domain regime and therefore preserves all mixed products, while the exact first-order Fourier projector that deletes mixed modes is not positivity preserving. Even a state-specific positive sparse output with finite diagonal mass recreates the divergent `WP-096` bound.

The remaining live question is narrower: can an independently forced **enlarged finite--archimedean architecture** alter the prime-coordinate observables before compression — for example by turning them into strict contractions or coupling them to a non-scalar global sector — so that the multiplicative-domain obstruction no longer applies, while a new sign theorem survives and the exact Weil readout emerges only after the global coupling?