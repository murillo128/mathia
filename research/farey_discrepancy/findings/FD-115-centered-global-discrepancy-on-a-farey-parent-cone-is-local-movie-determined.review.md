---
type: adversarial-review
target: research/farey_discrepancy/findings/FD-115-centered-global-discrepancy-on-a-farey-parent-cone-is-local-movie-determined.md
---

# Adversarial review

## Adversary

Equation (6) defines `Lambda_Q(u,v)` by quantifying over integer pairs `(m,n)` with a coprimality and denominator condition, but it omits the required restriction `m,n>=0`. Without that cone restriction the set is not the visible Farey packet used in the proof and can admit irrelevant signed solutions; the exact identity (13) therefore does not follow from the formula as written. The objection is resolved if the definition is restricted explicitly to primitive nonnegative rays, matching the bijection established in `FD-114`, and the subsequent proof is checked under that corrected domain.

## Owner

The objection is valid as a defect in the displayed definition, not in the intended claim. The proof uses exactly the primitive nonnegative cone from `FD-114`; adding `m,n>=0` to (6) makes the quantified set identical to `(A,x_(u,v)] intersect F_Q` under the unimodular bijection. With that domain restored, (13)--(15) and the common-mode decomposition are unchanged. The finite rational checks also used nonnegative ray coordinates. I accept the correction.
