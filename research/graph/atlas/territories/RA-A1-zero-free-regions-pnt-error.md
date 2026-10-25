---
id: RA-A1
type: riemann-atlas-territory
atlas_version: 1
parent: RA-A
mass: 0.050
state: active
confidence: source-backed
derived: true
---

# A1 — Zero-free regions / PNT and Möbius-summatory error

This coarse v1 leaf covers the classical analytic route in which RH-strength information is sought through zero-free control or through primary summatory error terms whose scale is governed by the zeta divisor, including prime-counting and Möbius/Mertens cancellation.

## Evidence

- [[research/mobius_cancellation/findings/MC-001-local-to-global-exceptional-mass-barrier|MC-001]]
- [[research/mobius_cancellation/findings/MC-002-prime-harmonic-ceiling-single-scale-pretentiousness|MC-002]]
- [[research/mobius_cancellation/findings/MC-003-mobius-liouville-square-convolution-threshold|MC-003]]
- [[research/mobius_cancellation/findings/MC-004-qualitative-chowla-support-matched-bias|MC-004]]
- [[research/mobius_cancellation/findings/MC-005-exact-support-multiplicativity-slow-mean-cancellation|MC-005]]
- [[research/mobius_cancellation/findings/MC-006-averaged-chowla-vdc-logarithmic-ceiling|MC-006]]
- [[research/mobius_cancellation/findings/MC-007-same-prime-comparator-squarefull-kernel|MC-007]]
- [[research/mobius_cancellation/findings/MC-008-analytic-nonmasking-vs-absolute-inversion|MC-008]]
- [[research/mobius_cancellation/findings/MC-009-pintz-mean-absolute-zero-boundary|MC-009]]

Möbius Cancellation now audits several distinct information channels. Almost-all short-interval magnitude, a single prime-only pretentious scalar, the natural Möbius--Liouville square convolution, qualitative Chowla plus exact support, multiplicativity with only qualitative mean cancellation, and the currently available averaged two-point Chowla input all fail to produce a black-box polynomial Mertens gain at the required scale.

MC-007--MC-008 sharpen the surviving transfer question rather than solving cancellation. Same-prime multiplicative comparators factor through squarefull kernels, and analytic zero-nonmasking can preserve RH equivalence even when coefficientwise absolute inversion is too expensive. That identifies a potentially useful transfer criterion, but no independently proved comparator estimate or new source-side cancellation mechanism is yet established.

MC-009 adds a weaker RH-complete target only conditionally on a very recent Pintz theorem that the finding explicitly marks `NEEDS-AUDIT`: the mean-absolute Mertens exponent would recover the rightmost zero boundary. This could lower the required endpoint from pointwise to mean-absolute control, but it supplies no new unconditional cancellation estimate and is not used to promote the territory.

The territory therefore remains `active`, not `open`: Mathia is traversing the classical summatory-error route deeply enough to isolate multiple quantitative barriers, a sharper transfer equivalence, and a conditional literature endpoint, but it has not produced a surviving positive route that improves the Mertens scale or zero-free region.

## Prime-window moment prerequisites

[[research/prime_lattice/graph/relations/mod5-window-moment-zero-free-prerequisites|The mod-5 window-moment mechanism]] adds the conditional zero-free implications in [[research/prime_lattice/findings/PL-459-integrated-first-moment-zero-free-gate|PL-459]]–[[research/prime_lattice/findings/PL-463-empirically-centered-window-variance-zero-free-gate|PL-463]]. Raw and empirically centered upper moments have different exponents and unproved source hypotheses. They diagnose the strength of proposed covariance inputs; they supply no unconditional zero-free improvement. The territory remains `active`, with unchanged mass.

## Conditional short-window variance

[[research/graph/relations/rh-mellin-variance-and-farey-capacity|RH Mellin variance and balanced Farey capacity]] records MC-520's classical RH-conditional variance input and its application to balanced Farey near-capacity. It supplies no unconditional Mertens or zero-free gain, so the territory remains `active` with unchanged mass.

[[research/mobius_cancellation/findings/MC-521-smooth-deconvolution-removes-the-variance-zero-free-boundary-loss|MC-521]] sharpens the reverse conditional transfer: smooth-test deconvolution removes the sharp-endpoint exponent from zero exclusion under the complete, uncentered, all-scale moment premise. Its Section 4 also recovers the epsilon-loss sharp Mertens consequence through classical reciprocal-zeta growth and Perron. It retains MC-177's direct-method limitation, the unproved variance input, and MC-520's RH converse. This is a conditional transfer refinement inside A1, not an unconditional zero-free gain; its state and mass remain unchanged.

[[research/prime_lattice/graph/relations/dyadic-seam-filtered-zero-recovery|Dyadic seam filtering and arithmetic pole recovery]] records the distinct PL-466 refinement for empirically centered data at every large dyadic scale. Its finite filter requires arithmetic zero-density and noncancelling residues to recover poles. The prime variance premise remains unproved, so A1 remains `active` with unchanged mass.

## Fixed-target logarithmic-window boundary

[[research/graph/relations/fixed-target-box-inversion-regularity-boundary|Fixed-target box inversion and its regularity boundary]] records PL-474 and MC-530's constructive r>1 range together with PL-473's all-scale fixed-target obstruction for 0<=r<=1. The source-dependent variance floors are conditional on an off-critical zero; the required absolute variance ceilings remain unproved. This is a conditional analytic refinement within A1, whose state `active` and mass are unchanged.
