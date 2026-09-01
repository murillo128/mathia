---
id: CLUE-weil-positivity-mixed-prime-positive-completion-selector-quotient
type: research-clue
status: proposed
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

No such quotient or coupling is established. WP-097 proves only existence of a positive mixed-prime completion, not that its mixed coefficients can be removed canonically or that it matches the global Weil form. This file is therefore a research lead, not evidence for Weil positivity or for RH.
