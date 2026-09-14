---
type: adversarial-review
target: research/farey_discrepancy/findings/FD-115-centered-global-discrepancy-on-a-farey-parent-cone-is-local-movie-determined.md
---

# Adversarial review

## Adversary

Equation (6) defines `Lambda_Q(u,v)` by quantifying over integer pairs `(m,n)` with a coprimality and denominator condition, but it omits the required restriction `m,n>=0`. Without that cone restriction the set is not the visible Farey packet used in the proof and can admit irrelevant signed solutions; the exact identity (13) therefore does not follow from the formula as written. The objection is resolved if the definition is restricted explicitly to primitive nonnegative rays, matching the bijection established in `FD-114`, and the subsequent proof is checked under that corrected domain.
