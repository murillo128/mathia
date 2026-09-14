---
id: CLUE-farey-discrepancy-ordered-plucker-refinement-transfer
type: research-clue
status: resolved
origin: visionary-researcher
target_line: farey_discrepancy
based_on:
  - research/farey_discrepancy/README.md
  - research/farey_discrepancy/clues/CLUE-farey-gap-order-bridge-suppression.md
  - research/visual_exploration/findings/VIS-026-gap-permutation-discrepancy-bridge-covariance.md
  - research/visual_exploration/findings/VIS-034-farey-low-band-suppression-factorization.md
---

# Do ordered two-level Plücker defects retain Farey cancellation beyond scalar discrepancy?

## Observation

The proposed route was to retain an ordered antisymmetric/Plücker field across nested Farey refinements before taking norms or scalar spectral summaries, with the hope that a genuinely independent residual coordinate would survive the controls that collapse ordinary discrepancy statistics.

The Research Watch progressively removed the obvious realizations. `FD-112` showed that one mediant split has only one residual shape scalar after parent-size control. `FD-113` extended that collapse to any fixed finite Stern--Brocot descendant template, even though nonlinear embeddings can have nonzero minors. `FD-114` showed that the complete denominator-truncated local refinement movie is still determined by root split plus parent scale and horizon. `FD-115` showed that centered descendant discrepancy inside one parent cone is the local movie plus a single absolute common-mode anchor, and `FD-116` classified fixed rational anchor histories as periodic Möbius filters.

`FD-117` closes the remaining moving-anchor source-independence escape at the level of the complete cumulative discrepancy field: for every horizon `N`, the entire function `D_N(x)` is an explicit affine linear image of the quotient-Mertens staircase and the transform is invertible.

## Research question

Can an ordered Plücker/refinement transform nevertheless expose a quantitatively useful cancellation or coercivity statement for Farey discrepancy, even though it cannot constitute an arithmetic source independent of the Möbius/Mertens data already equivalent to the complete discrepancy field?

This is narrower than the original clue. The information-independence hypothesis is no longer live; only a possible proof-theoretic reorganization of the same source remains.

## Why it may matter

An invertible change of representation can still be mathematically valuable. Positivity, locality, antisymmetry, or a multiscale coercive inequality may be visible in one representation and opaque in another even when no information is added. Such a theorem would be genuine progress only if it yields a stronger quantitative estimate at the Franel--Landau scale, not merely a nonzero minor or a higher-dimensional encoding.

## Decisive test

Any future Plücker/refinement proposal must derive its exact finite-order identity first and then prove a quantitative estimate that is not already an immediate restatement of the corresponding Mertens bound. Growing vector dimension, moving rational endpoints, growing endpoint denominators, arbitrarily many same-horizon discrepancy samples, or adaptive selection from the cumulative discrepancy field do not pass the source-independence gate: `FD-117` reconstructs all of them from the quotient-Mertens staircase.

A viable continuation therefore needs a coercive/cancellation theorem for the transformed Mertens-equivalent object, with a predeclared normalization and controls, and must show that the theorem has sufficient strength at the RH-critical exponent.

## Evidence boundary

The exact Farey--Möbius and Fourier identities used by `FD-117` are classical/derived from `FD-001`; no novelty is claimed for the underlying arithmetic transforms. The negative conclusion is specifically about **independent source information**. It does not prove that every geometric or exterior reorganization is quantitatively useless, and it does not supply a new Franel--Landau estimate.

## Research disposition

Outcome: refuted

Resolved by:
- [[research/farey_discrepancy/findings/FD-117-full-farey-discrepancy-field-is-invertibly-equivalent-to-the-quotient-mertens-staircase.md]]

The clue's intended independent-source mechanism is refuted: the full cumulative Farey discrepancy field, including moving/growing endpoint observations and its complete horizon history, is explicitly equivalent to quotient/full Mertens data. A Plücker/refinement representation may still be worth studying only as a quantitatively stronger reorganization of that same source; that is no longer evidence for the original independent-carrier hypothesis.
