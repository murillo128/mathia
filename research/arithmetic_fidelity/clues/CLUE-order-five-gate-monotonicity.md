---
id: CLUE-order-five-gate-monotonicity
type: research-clue
status: accepted
origin: research-watch
target_line: arithmetic_fidelity
based_on:
  - research/arithmetic_fidelity/findings/AF-404-confluent-hankel-toda-recursion-reduces-strict-flags-to-nested-log-concavity.md
  - research/arithmetic_fidelity/findings/AF-405-full-euler-log-is-strictly-sign-regular-through-order-four.md
  - research/arithmetic_fidelity/findings/AF-408-order-five-euler-failure-is-confined-to-compact-log-scale.md
---

# Is the compact order-five Euler Toda gate monotone?

## Observation

AF-404 identifies the order-five scalar gate as

\[
A_4(t)=-(\log H_4(t))'',
\]

while AF-408 leaves its compact behavior unresolved after excluding the two tails analytically. Independent execution of compute issue #162 evaluated the exact full Euler-log profile on `[-14,4]` with arbitrary-precision Taylor jets. The direct determinant route, normalized Toda recursion, AF-404's expanded `R_4`, and an independent derivative audit agreed to roughly 92--120 relative digits. In a 4001-node scan, `A_4`, `A_4'`, and `A_4''` were positive; endpoint refinement placed the smallest sampled value at `t=-14`, where `A_4≈3.3189083716470089392617316757823131435·10^{-12}`. This is independent numerical evidence from issue #162, not a proof.

## Research question

Does the exact Euler-log gate satisfy

\[
A_4'(t)=-(\log H_4(t))'''\ge 0
\qquad(-14\le t\le4)?
\]

## Why it may matter

If true, compact positivity would reduce to the positive endpoint value already observed numerically, moving the order-five question from an interior search to one monotonicity inequality. A counterexample would identify a genuine interior turning point even though the gate has no sampled sign failure.

## Decisive test

Construct a dependency-preserving rigorous enclosure for `A_4'` over the full frozen interval and a positive enclosure for `A_4(-14)`, using the exact profile and keeping AF-408's tail argument separate. Any reproducible negative enclosure for `A_4'` kills this monotonicity route; failure of the enclosure alone is inconclusive.

## Evidence boundary

The issue-#162 result is bounded high-precision sampling with certified point/local enclosures, not a compact-interval positivity theorem and not a rigorous global-minimum proof. The Toda identities and asymptotic ratios used in the computation are already represented by AF-404 and AF-408; no new theorem, order-five positivity, all-order positivity, arithmetic-prime discriminator, or RH consequence is established here.

## Research disposition

The direction is accepted for continued investigation. AF-408 makes the compact sign problem mathematically consequential, while issue #162 supplies independent high-precision evidence that monotonicity is a plausible strengthening rather than a reformulation of the existing tail theorem. A fresh literature audit found classical Hankel/Toda and finite-order total-positivity machinery but no theorem that settles this concrete Euler-log third-log-derivative sign. The unresolved target remains exactly the rigorous sign of `A_4'` on `[-14,4]`; acceptance does not upgrade the numerical evidence.