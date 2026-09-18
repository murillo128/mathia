---
id: CLUE-effective-order-five-tail-cutoffs
type: research-clue
status: resolved
origin: research-watch
target_line: arithmetic_fidelity
based_on:
  - research/arithmetic_fidelity/findings/AF-405-full-euler-log-is-strictly-sign-regular-through-order-four.md
  - research/arithmetic_fidelity/findings/AF-408-order-five-euler-failure-is-confined-to-compact-log-scale.md
  - research/arithmetic_fidelity/findings/AF-409-order-five-euler-gate-explicit-right-tail.md
  - research/arithmetic_fidelity/findings/AF-410-order-five-euler-gate-explicit-left-tail.md
  - research/arithmetic_fidelity/clues/CLUE-order-five-gate-monotonicity.md
---

# Can the order-five Euler tail theorem be made effective at the compact-window endpoints?

## Observation

AF-408 proves eventual positivity of the order-five Toda gate

\[
A_4(t)=4q(t)-(\log R_4(t))''=-(\log H_4(t))''
\]

in both tails. AF-409 made the right tail effective and proved

\[
A_4(t)>0\qquad(t\ge4).
\]

The independently frozen compact interval is `[-14,4]`; the remaining question was whether the left asymptotic could also be made effective at its endpoint.

## Research question

Can the exact Euler-log gate be proved to satisfy

\[
A_4(t)>0\qquad(t\le-14)
\]

by explicit analytic remainder bounds or another rigorous comparison?

## Why it may matter

An endpoint-matched effective tail theorem removes the logical gap between AF-408's asymptotics and any future compact certificate. Once both tails meet `[-14,4]`, all remaining order-five sign uncertainty is genuinely compact rather than hidden in an unspecified asymptotic threshold.

## Decisive test

Starting from AF-408's left-tail expansion, replace every asymptotic remainder needed for the sign by a rigorous bound on the exact small-`x=e^t` profile. A numerical sample or an asymptotic sign without a quantified remainder does not resolve the clue.

## Evidence boundary

The clue itself is not evidence. AF-409 settles the right tail. The left-tail conclusion is established only by the linked canonical finding below, whose exact Bernoulli/Cauchy argument supplies the missing quantified remainder.

## Research disposition

Outcome: supported

Resolved by:
- [[research/arithmetic_fidelity/findings/AF-410-order-five-euler-gate-explicit-left-tail.md]]

AF-410 proves `A_4(t)>0` for every `t<=-14`, while AF-409 proves positivity for every `t>=4`. The effective-tail problem is therefore closed. The separate accepted compact-monotonicity clue remains unresolved and now owns the entire residual order-five sign question on `[-14,4]`.