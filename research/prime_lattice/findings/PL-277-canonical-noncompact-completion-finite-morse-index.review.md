---
type: adversarial-review
target: research/prime_lattice/findings/PL-277-canonical-noncompact-completion-finite-morse-index.md
---

# Adversarial review

## Adversary

The opening claim overstates the finite-source Morse-index conclusion as holding **at every fixed localization radius `a>0`**. Section 1 itself says that at aperture `a` the zeta source contains only prime powers with `log q<2a`. Hence for `0<a<= (log 2)/2` there are no active prime-power atoms at all: the uncompleted arithmetic source operator is zero. In that regime the PL-276 hypothesis of a nonzero finite positive interior source is absent, so the asserted infinite positive and negative Morse index after compact correction does not follow (and is false, for example with compact correction `K=0`).

The later matched-control statement about the completed operator having compact resolvent under arbitrary bounded finite-source replacement is unaffected. What needs correction is the universal fixed-aperture source-side statement and the displayed summary `finite source + compact correction -> infinite two-sided Morse defect`: it must explicitly require a **nonzero positive interior atomic source** (or its overall sign reversal), and the zeta specialization must restrict to apertures for which at least one prime-power atom is active. This is also the exact hypothesis already stated in PL-276 and again acknowledged in PL-277's own boundary section.