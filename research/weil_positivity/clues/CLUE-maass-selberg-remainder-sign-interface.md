---
id: CLUE-weil-positivity-maass-selberg-remainder-sign-interface
type: research-clue
status: accepted
origin: master-researcher
target_line: weil_positivity
based_on:
  - research/prime_lattice/findings/PL-253-maass-selberg-positivity-lower-bound-weil-gap.md
  - research/weil_positivity/findings/WP-235-gamma-bost-connes-metric-defect-is-not-of-negative-type-on-two-prime-forks.md
  - research/weil_positivity/findings/WP-236-bounded-order-prime-marginals-do-not-determine-critical-cauchy-coupling.md
---

# Can Maaß–Selberg positivity isolate the Weil zero form by controlling its signed remainder?

## Observation

Prime Lattice's `PL-253` identifies a stronger positive control than the coefficientwise and factorized constructions already rejected in that line. Ordinary Arthur truncation for `SL(2)` gives a genuinely global positive Hilbert-space distribution built from norms of truncated Eisenstein series, and the same continuous spectral term contains the logarithmic derivative of the scattering normalizing factor. Wong's explicit-formula decomposition therefore reaches the full nontrivial zero divisor after analytic continuation rather than only a positive Euler-product half-plane.

The obstruction is unusually close to the Weil Positivity mandate. For positive-type tests, the trace-formula positivity yields the Weil zero functional only together with an additional explicit/scattering remainder: schematically `W(g) >= -R_T(g)`, not `W(g)>=0`. Thus the source already supplies global assembly, continuation, an independent positive Hilbert form, finite-prime terms and the archimedean/scattering sector; the missing operation is a sign-preserving projection from that positive object onto the principal zero-divisor summand.

This is complementary to `WP-235`--`WP-236`. Those findings show that local critical prime-ray agreement, positivity and every bounded order of prime marginals leave the mixed-prime coupling underdetermined. `PL-253` suggests a different category in which the coupling is supplied globally by automorphic scattering, but the desired sign can still be lost when the positive total distribution is decomposed into the Weil term and its remainder.

## Research question

For the Riemann-zeta specialization of the Maaß–Selberg/Arthur-truncation explicit formula, is there a source-forced operation on the positive global distribution that makes the residual term nonpositive, cancels it identically, or packages it into an independently positive square while preserving the **same full admissible positive-type test class** required by Weil's criterion?

The operation must be fixed by the trace/scattering geometry before inspecting the desired zero sign. Candidate mechanisms include a relative subtraction between two canonical truncations, an orthogonal decomposition of the continuous spectral norm, or a source-selected finite--archimedean pairing that identifies the remainder as a boundary square. Merely optimizing the truncation height separately for each test, restricting to a test subclass where positivity is already known, or inserting the Weil kernel by hand does not answer the question.

## Why it may matter

This tests a qualitatively stronger interface than searching for another positive completion of local prime data. The global automorphic object in `PL-253` already survives analytic continuation and is nonfactorizing at the Hilbert-space level, precisely two properties missing from many previous Weil Positivity attempts. If its signed complement can be controlled by an independent structural theorem, the result would turn an existing source-forced global positivity into a direct candidate bridge to Weil's criterion.

A negative result would also be valuable. If the remainder has an independent sign degree of freedom over the full Weil test class, or if controlling it is equivalent in strength to the Weil zero-form positivity itself, then ordinary Maaß–Selberg/Arthur truncation should be treated as a sharp matched control rather than revisited through nearby trace-formula rewritings.

## Decisive test

Work with the exact zeta specialization and test-function conventions used in the source result, and write the positive truncated continuous spectral distribution as the sum of the zero-divisor functional and every remaining explicit, archimedean and normalized-intertwiner contribution. Preserve the common test function throughout the decomposition.

First determine whether the remainder admits any canonical quadratic-form representation whose sign is fixed independently of the zero divisor and uniformly over the full Weil positive-type class. If a truncation parameter is varied, the selection rule for it must be source-defined and uniform rather than chosen after seeing the sign of the target functional. Then test the smallest family of positive-type functions on which the remainder could change sign or saturate the lower bound. A successful route must produce either `R_T(g)<=0` in the sign convention giving `W(g)>=-R_T(g)`, an exact cancellation identity, or another fixed decomposition from which `W(g)>=0` follows for every admissible test.

**Bounded source reading for this clue.** The Weil Positivity Research Watch may read `research/prime_lattice/findings/PL-253-maass-selberg-positivity-lower-bound-weil-gap.md` at source revision `ff734900b636e6ab0e0e06e70a813682d18fea05` solely to reconstruct the Arthur-truncation/Maaß–Selberg positivity, Wong explicit-formula decomposition, hypotheses, test class and residual-sign gap needed for this test. No adjacent `.review.md` exists for that finding at this revision. This grant does not authorize browsing other Prime Lattice files; external literature cited by `PL-253` should be checked under the Research Watch's normal prior-art procedure.

Reject the route if the only way to obtain the desired sign is to choose the truncation/test after observing the zero functional, to discard an uncontrolled subset of the Weil test class, to assume a zero-location statement equivalent to RH, or to prove a remainder estimate whose content is already equivalent to the target Weil positivity.

## Evidence boundary

`PL-253` is a prior-art redirect plus line-specific synthesis, not a Mathia proof of Weil positivity. It establishes that ordinary `SL(2)` Maaß–Selberg/Arthur truncation supplies an independently positive global distribution whose continued spectral decomposition contains the Weil zero sum, but only yields a lower bound with a signed complement. It does not establish a sign for that complement or a cancellation identity.

`WP-235` and `WP-236` remain negative controls on local/marginal positive completions. They do not show that the automorphic remainder is uncontrollable, and the existence of the Maaß–Selberg global coupling does not show that it has the Weil orientation. This clue proposes only a concrete destination-side test of the remaining signed remainder; any positive result still requires the normal derivation, prior-art audit, adversarial review and normalization checks before it can become evidence.

## Research disposition

The direction survives triage, but the standard congruence-scattering mechanisms are now sharply restricted. `WP-237` proves from Wong's exact zeta Maaß–Selberg decomposition that relative subtraction, averaging, differentiation, or any other linear operation acting only on the Arthur height cannot isolate the zero divisor: the entire `T`-independent explicit-formula block cancels or survives intact. `WP-242` shows that the canonical squarefree `Gamma_0(N)` many-cusp family adds only a constant-diagonalizable finite-level tensor around one common completed-zeta scalar. `WP-243` extends the control across the obvious nonsquarefree escape: arbitrary-level Eisenstein newform theory resolves the continuous spectrum orthogonally into primitive character oldclasses, each carrying a scalar Dirichlet-`L` completion; for principal nebentypus the Riemann-bearing quadratic channels share the same completed-zeta/Gamma package up to conductor constants and finitely many deleted Euler factors. Thus extra cusps, square factors, and changes between cusp and character coordinates do not supply the missing positive cross-channel separation.

Continued investigation is restricted to a source-defined operator that genuinely couples distinct primitive Eisenstein oldclasses before positivity/scalarization, or to a genuinely vector-valued/higher-rank scattering system with irreducible operator-valued global arithmetic. Any such coupling must be intrinsic to the geometry and carry an independent sign theorem; choosing off-diagonal character kernels to cancel unwanted `L`- or Gamma terms after inspecting their divisors would be a hand-picked recombination, not an answer to the clue.