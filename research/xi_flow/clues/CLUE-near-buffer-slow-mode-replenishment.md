---
id: CLUE-xi-flow-near-buffer-slow-mode-replenishment
type: research-clue
status: resolved
origin: master-researcher
target_line: xi_flow
based_on:
  - research/xi_flow/findings/XF-042-finite-window-cauchy-relaxation-is-input-to-state-stable-under-centered-exterior-mismatch.md
  - research/xi_flow/findings/XF-044-cauchy-slow-mode-imposes-logarithmic-precision-clock-at-memory-scale.md
  - research/xi_flow/findings/XF-046-source-counting-makes-remote-memory-scale-forcing-little-o-at-critical-r2.md
  - research/xi_flow/findings/XF-047-source-compatible-memory-waves-survive-fixed-heat-time-at-critical-flux-scale.md
  - research/xi_flow/clues/CLUE-overlap-discriminant-taper-summation-by-parts.md
---

# Which Xi-specific constraint excludes the persistent memory wave already compatible with local counting?

## Observation

XF-042 isolates centered exterior gap mismatch as the adverse input to finite-window Cauchy relaxation. XF-044 proves a genuine slow-mode obstruction: at period of order `log^2 T`, bounded heat time gives only a fixed-factor contraction. XF-046, with its persisted source-density normalization, now controls the genuinely remote contribution at `o(R^-2)` for a memory-scale core and buffer distance `D=R(T)log T`, under the stated real-simple and upper-gap hypotheses.

XF-047 supplies an exact nonlinear periodic control with corrected source spacing `sigma_T=4pi/log(T/4pi)`, period `q~log^2 T`, `R=q`, and relative amplitude `kappa/q^2`. It respects the locally used counting tolerances and gap envelope but retains critical triple-flux variation through every fixed heat-time interval. It is not a global Xi zero set, and its infinite periodic continuation does not satisfy global Xi counting. This already answers the generic local persistence test negatively; reproducing it is not the next task.

## Research question

Is there a specific unconditional identity or analytic constraint of the actual Xi flow, beyond the local counting/envelope information used in XF-047, that excludes its coherent memory phase at critical amplitude? Test the constraint on a localized insertion of the wave into a configuration with the genuine global density, so that a distinction caused solely by the artificial periodic continuation is not mistaken for the needed local selector.

## Why it may matter

A quantitative suppression theorem would address the remaining source input directly. Conversely, an insertion retaining the critical local flux while meeting an additional proposed source constraint would rule out that constraint as the missing selector. This is separate from the accepted taper-identity clue: it tests the arithmetic content that could make such an identity effective.

## Decisive test

Fix the core and buffer scales within XF-046/XF-047's ranges. Select one actual Xi-specific identity with an explicit unconditional domain of validity; calculate its response to the critical wave before estimating absolute values. Separate a response to global density mismatch from a response to the local coherent phase. A static insertion alone is insufficient if the argument consumes evolution over a fixed time interval.

Either derive a phase-sensitive inequality that forces the required extra vanishing factor beyond `R^-2` under independently verified Xi hypotheses, or construct a controlled localized wave whose fixed-time evolution meets the selected additional hypothesis and still violates the desired `M V_M=o(1)` gate. Include source-density normalization, near-buffer exchange, and maintenance of the upper-gap envelope. If verifying the extra identity already assumes real-rootedness outside the legitimate regime or the desired flux bound, reject that proposed input as circular.

## Evidence boundary

XF-047 establishes nonlinear periodic persistence and compatibility with the locally consumed source tolerances, not global Xi realizability. No phase-sensitive Xi selector or globally compatible evolving insertion is established here. No zero-motion equation is extended through collisions, and no bound on the de Bruijn--Newman constant follows from this proposed test.

## Research disposition

Outcome: narrowed

Resolved by:
- [[research/xi_flow/findings/XF-048-endpoint-explicit-formula-prime-free-gap-excludes-critical-memory-wave]]

XF-048 identifies a source-specific selector for the coherent wave itself. In the endpoint coordinate `x=2 gamma`, the Guinand--Weil explicit formula places the first prime-power Fourier line at `log 2/2`, while the XF-047 memory frequency is only `Theta(1/log T)`. A Gaussian taper of width `Theta(log^3 T)` therefore has actual Xi zero statistic `o(1)` but gives the critical memory wave the nonzero limit `-sqrt(2pi) kappa/2`. The same contradiction survives a localized insertion over a slowly enlarged source buffer, so it is not caused by the infinite periodic continuation or by a mean-density mismatch.

This resolves the clue's request for an actual phase-sensitive Xi constraint, but only at `t=0`. It does not yet control arbitrary broadband/cancelling near-buffer forcing or propagate the filtered coefficient through the real-simple `t<0` dynamics. The remaining problem has therefore moved from identifying a selector to proving a dynamic transport/cancellation estimate compatible with that endpoint spectral constraint.