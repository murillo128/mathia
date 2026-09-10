---
id: CLUE-prime-flute-critical-jacobi-square-root-decay-window
type: research-clue
status: resolved
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-243-fixed-seam-robin-homotopy-reduces-high-high-shear-to-one-sided-separated-poisson-smoothing.md
  - research/prime_flute/findings/PF-247-fixed-axis-compactification-is-parity-jacobi-in-corridor-modes.md
  - research/prime_flute/findings/PF-248-parity-jacobi-tail-is-trace-class-but-first-moment-critical.md
  - research/prime_flute/findings/PF-249-positive-separation-preserves-free-jacobi-square-root-threshold.md
  - research/prime_flute/findings/PF-250-half-line-fractional-edge-powers-retain-supercritical-separated-window.md
  - research/prime_flute/findings/PF-251-exact-zero-edge-solutions-select-growing-inverse-square-jacobi-branch.md
  - research/prime_flute/findings/PF-252-zero-edge-ground-state-transform-has-bessel-four-scaling.md
  - research/prime_flute/findings/PF-253-bessel-four-jacobi-fractional-powers-have-sharp-separated-window.md
  - research/prime_flute/findings/PF-254-normalized-noncommuting-robin-injection-splits-square-root-amplitude-from-polar-transport.md
  - research/prime_flute/findings/PF-255-hypercycle-compactification-transport-is-a-parity-local-flow-with-a-two-derivative-leakage-bound.md
  - research/prime_flute/findings/PF-256-variable-corridor-graph-equivalence-transfers-two-derivative-locality-to-the-actual-transverse-scale.md
  - research/prime_flute/findings/PF-257-normalized-robin-injection-is-a-polar-free-resolvent-transform.md
  - research/prime_flute/findings/PF-269-pre-propagation-robin-smoothing-is-an-overstrong-gate.md
  - research/prime_flute/clues/CLUE-robin-homotopy-separated-poisson-shear-estimate.md
---

# Can the fixed-axis combined Robin injection spend the Jacobi smoothing margin?

## Observation

PF-247--PF-253 establish a positive fractional-power window for the fixed-axis parity-Jacobi edge, while PF-254--PF-257 show that the physical normalized Robin source factor should be treated as the combined polar-free transform

\[
B_w=X_w(I+X_w^*X_w)^{-1}
=(I+X_wX_w^*)^{-1}X_w,
\]

rather than by estimating the naked polar partial isometry. This motivated asking whether the combined boundary factor itself could absorb a supercritical `K_a^R`, `R>1`, weight before any longitudinal propagation.

PF-269 now shows that this standalone requirement is not a structurally valid gate for the PF-243 route. In the exact PF-246 commuting calibration with matched seam `Q=K`, one has `X=I` and therefore

\[
B=\frac12I,
\]

so `BK^RP_Z` is unbounded for every `R>0` on unbounded high spectrum. Nevertheless the corresponding separated Robin-Poisson source-to-bulk map is smoothing of every order across any fixed positive longitudinal distance.

## Research question

The original question was whether the actual fixed-axis complete-lift factor `B_w` could itself satisfy a uniform bound

\[
B_wK_a^RP_Z\in\mathcal B(H)
\qquad\text{for some }R>1
\]

before separated longitudinal propagation, perhaps by spending the parity-Jacobi fractional window of PF-253 while retaining the exact PF-257 amplitude/orientation correlation.

PF-269 does not decide whether the actual `B_w` happens to have such additional decay. It decides the route-selection question: **that standalone bound is stronger than PF-243 needs and cannot be required as a generic intermediate theorem.**

## Why it may matter

The distinction prevents a false negative. Even the clean matched Robin model has no positive-order smoothing in `B` itself, yet the far Poisson leg gains arbitrary order because fixed positive separation contributes exponential transverse damping. Therefore failure of an isolated `B_wK_a^RP_Z` estimate would not kill the shear route.

At the same time PF-244 remains load-bearing: a noncommuting source factor can convert high input into genuinely low output before propagation, and such low output is not rescued by high-frequency Poisson damping. The useful target is consequently the **composed conversion/propagation operator**, not the boundary factor in isolation and not an arbitrary bounded-source surrogate.

## Decisive test

PF-269 supplies the decisive calibration. Set `Q=K` in the PF-246 product corridor. Then the PF-257 transform gives `B=1/2 I`, which fails every positive-order pre-propagation weighted bound, while PF-246 simultaneously proves all-order separated Robin-Poisson smoothing for the same seam.

For the actual seam, continue with the four source-to-bulk estimates of PF-243 and [[research/prime_flute/clues/CLUE-robin-homotopy-separated-poisson-shear-estimate|CLUE-robin-homotopy-separated-poisson-shear-estimate]]. A valid proof may still need localized/off-diagonal information about `B_w` or its block resolvent, but only insofar as it prevents dangerous high-to-low conversion inside the composed far-leg map.

## Evidence boundary

PF-269 does **not** prove that the actual complete-lift `B_w` fails or satisfies a positive-order standalone bound. It does not identify `X_wX_w^*` with the parity-Jacobi operator, control the noncommuting reflection factors, or prove PF-243's four actual-seam separated estimates.

The durable conclusion is narrower: standalone positive-order smoothing of the normalized Robin boundary factor is not a necessary intermediate condition for separated Robin-Poisson smoothing. The unresolved actual-seam problem remains the composed source-to-bulk estimate.

## Research disposition

Outcome: narrowed

Resolved by:
- [[research/prime_flute/findings/PF-269-pre-propagation-robin-smoothing-is-an-overstrong-gate|PF-269]]

The clue is resolved as a route-selection question. The literal pre-propagation `B_wK_a^RP_Z` gate is removed from the critical path; the surviving research obligation is the already-accepted composed Robin-Poisson estimate in [[research/prime_flute/clues/CLUE-robin-homotopy-separated-poisson-shear-estimate|CLUE-robin-homotopy-separated-poisson-shear-estimate]].