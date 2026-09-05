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
  - research/weil_inertia/findings/WI-172-c2330-four-point-candidate-awaits-kernel-check.md
---

# Can a source-constrained cover evade the sharp positive-cover relaxation?

## Observation

WI-166 closes the arbitrary nonnegative pair-weight/gap relaxation behind the four-point positive-cover program: coefficientwise pair-energy domination admits an exact witness that makes the relaxation sharp. WI-171 closes the most immediate generic-matrix escape: that exact pair-weight witness is realized by uniformly well-conditioned positive-definite Toeplitz Gram matrices, so PSD, principal-minor, determinant, interlacing, conditioning, and generic stationary-Gram constraints alone do not exclude it. The surviving source information is the specific Montgomery--Taylor kernel-value relation tied to the same ordered gaps that fund the pressure, or genuinely additional arithmetic information.

WI-172 narrows the first source-specific test further. `teal-sea/zeta-lab` already contains a preserved generated candidate for the genuine MT four-point functional at `c=2330/10^6`, `p=2500`, with exact search-tree closure and a zero-problem emitted-source preflight. Its complete Lean build was canceled before the candidate proof modules ran, so the candidate is not established evidence. If it kernel-checks at the corrected admissible block size `m=432`, the ordinary `n_point_bound` bridge already yields `0.672860358838866...`, strictly above WI-036's current exact `0.672852930121184...` bound.

## Research question

Does the actual source coupling

\[
w_{ij}=|K_{\rm MT}(y_j-y_i)|^2,
\]

together with ordered additive gap geometry and the common span-pressure ledger, force a strict surplus over the WI-166 saturation resource that survives the complete global assembly? Or can a source-realizable periodic/aperiodic family asymptotically saturate the same resource despite those couplings?

## Why it may matter

This is the precise remaining question after the positive-cover optimization and the PSD-only escape have both been exhausted. A positive answer identifies genuinely source-specific information discarded by the arbitrary-weight relaxation; a negative answer closes another apparent matrix-refinement route and redirects attention toward independent profiles, the exceptional indefinite block, or stronger arithmetic observables.

The WI-172 candidate makes the smallest positive test concrete: no new search is needed to ask whether the actual four-point source functional already has at least `20/10^6` more uniform local margin than the Lean-checked `2310/10^6` certificate.

## Decisive test

First perform a bounded complete Lean replay of the preserved `teal-sea/zeta-lab` candidate at commit `d28df5f992479cd32751cb90c8c88551550582a3`. Require the recorded emitted-source preflight, then actually compile `four_point_cert`, `Phi_four`, the downstream bound declarations, and the repository's no-`sorry`/axiom audit. Separate theorem/proof failure from cancellation, timeout, or environment failure.

If that replay succeeds, accept a strict finite source-constrained escape from the WI-166 saturation value as established and then ask the remaining larger question: determine the optimal finite/periodic MT-constrained `E+P` resource, or produce a source-realizable family that asymptotically approaches the relaxed value. If the replay fails mathematically, inspect the first failing theorem/cell before reopening any parameter search.

Generic Gram or Toeplitz feasibility is no longer a valid decisive test: WI-171 already supplies those properties for the WI-166 witness. Any later numerical experiment must preserve the fixed kernel-value relation and pressure coupling from the start.

## Evidence boundary

No `c=2330/10^6` theorem is established yet. WI-172 records generated Lean source plus exact-rational preflight evidence, but the only complete build attempt was canceled before candidate modules ran. The established local certificate remains `2310/10^6`, and the established exact Mathia proportion remains WI-036's `0.672852930121184...` until a stronger proof is actually checked.

Even a successful `c=2330/10^6` replay would resolve only the smallest strict-source-surplus question. It would not determine the optimal MT-constrained cover, defeat WI-026's single-profile pressure-family ceiling, identify the exceptional complement, or imply RH.

## Research disposition

Accepted and **narrowed to a bounded formal check first**. WI-171 refutes the PSD/Gram-only branch exactly; WI-172 shows that the first genuine MT-kernel escape need not begin with a new optimization campaign because a stronger source-aware candidate already exists in prior art. Continued open work after that check remains restricted to the specific kernel--placement--pressure coupling (or an independent arithmetic constraint) that the arbitrary-weight and generic-PSD relaxations discard.