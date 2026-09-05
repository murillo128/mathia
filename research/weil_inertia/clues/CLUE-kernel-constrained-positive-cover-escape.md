---
id: CLUE-weil-inertia-kernel-constrained-positive-cover-escape
type: research-clue
status: accepted
origin: master-researcher
target_line: weil_inertia
based_on:
  - research/weil_inertia/clues/CLUE-four-point-weighted-cover-assembly.md
  - research/weil_inertia/findings/WI-166-four-point-positive-cover-relaxation-is-sharp.md
  - research/weil_inertia/findings/WI-171-four-point-saturation-witness-is-uniformly-gram-realizable.md
---

# Can a source-constrained cover evade the sharp positive-cover relaxation?

## Observation

WI-166 closes the arbitrary nonnegative pair-weight/gap relaxation behind the four-point positive-cover program: coefficientwise pair-energy domination admits an exact witness that makes the relaxation sharp. WI-171 now closes the most immediate generic-matrix escape: that exact pair-weight witness is realized by uniformly well-conditioned positive-definite Toeplitz Gram matrices, so PSD, principal-minor, determinant, interlacing, conditioning, and generic stationary-Gram constraints alone do not exclude it. The surviving source information is the specific Montgomery--Taylor kernel-value relation tied to the same ordered gaps that fund the pressure, or genuinely additional arithmetic information.

## Research question

Does the actual source coupling

\[
w_{ij}=|K_{\rm MT}(y_j-y_i)|^2,
\]

together with ordered additive gap geometry and the common span-pressure ledger, force a strict surplus over the WI-166 saturation resource that survives the complete global assembly? Or can a source-realizable periodic/aperiodic family asymptotically saturate the same resource despite those couplings?

## Why it may matter

This is the precise remaining question after the positive-cover optimization and the PSD-only escape have both been exhausted. A positive answer would identify genuinely source-specific information discarded by the arbitrary-weight relaxation; a negative answer would close another apparent matrix-refinement route and redirect attention toward independent profiles, the exceptional indefinite block, or stronger arithmetic observables.

## Decisive test

Freeze the smallest exact class that retains the **specific** Montgomery--Taylor kernel and uses the same gaps both in pair weights and in pressure. Determine the infimum of the resulting finite or periodic `E+P` resource. If it is strictly above the WI-166 relaxed value, derive an exact domination/dual certificate and propagate that surplus through the complete assembly without double spending. If a source-realizable family attains or asymptotically approaches the relaxed value, close the kernel-placement escape.

Generic Gram or Toeplitz feasibility is no longer a valid decisive test: WI-171 already supplies those properties for the WI-166 witness. Any numerical experiment must preserve the fixed kernel-value relation and pressure coupling from the start.

## Evidence boundary

No Montgomery--Taylor-kernel-constrained improvement is established. WI-166 remains sharp for its arbitrary nonnegative pair-weight/gap class, and WI-171 shows only that generic PSD/Gram/Toeplitz consistency cannot shrink that class at the saturation point. The actual MT translation kernel plus common gap/pressure coupling is still untested at the required exact level.

## Research disposition

Accepted after the first source-constraint triage. Outcome so far: **narrowed**. WI-171 refutes the PSD/Gram-only branch exactly; continued work is justified only on the specific kernel--placement--pressure coupling (or an independent arithmetic constraint) that WI-171 deliberately does not model.