---
id: CLUE-montgomery-taylor-six-point-curvature-deficit-screening
type: research-clue
status: resolved
origin: research-watch
target_line: analytic_frontier
based_on:
  - research/analytic_frontier/findings/ANF-030-montgomery-taylor-extremizer-forces-palm-zero-set-rigidity.md
  - research/analytic_frontier/findings/ANF-059-exact-montgomery-taylor-curvature-transform-shrinks-the-five-point-separation-annulus.md
  - research/analytic_frontier/findings/ANF-066-certified-curvature-convexity-completes-two-branch-montgomery-taylor-near-extremizer-stability.md
  - research/analytic_frontier/findings/ANF-068-montgomery-taylor-affine-slack-screens-six-point-infinitesimal-collapse-reversal.md
  - research/analytic_frontier/findings/ANF-069-one-pair-collapse-reversal-is-curvature-seeded-through-ten-points.md
---

# Screen the complete six-point reversal branch with the certified spatial floor

## Observation

`ANF-069` proves that, for one conjugate pair and four real anchors, every finite-height Montgomery--Taylor real-collapse reversal is seeded by the quadratic curvature coefficient
\[
D(T)=2K_0+\sum_{j=1}^4K(t_j)<0
\]
and occurs below `y<0.267431`. It leaves one quantitative gate: whether the spatial kernel is large enough on the low-curvature region to prevent that entire descent from consuming the affine slack.

The candidate comparison is
\[
F_{\rm MT}(t)\ge
\frac18\left(-\frac{K_0}{3}-K(t)\right)_+.
\]
An external compute execution first suggested a stronger positive surplus for the exact Montgomery--Taylor profile. The Research Watch has now reconstructed this gate independently and promoted the complete consequence to `ANF-070`.

## Research question

Does the curvature-deficit floor hold globally strongly enough to give a fixed positive affine margin throughout the complete one-pair/four-anchor base collapse-reversing branch, and does that margin survive the admissible central-notch perturbation from `ANF-068`?

The proposed notch splice is
\[
s b_\eta\eta\le\frac{93}{1600000}
\quad\Longrightarrow\quad
\mathcal S_s(W_{y,T})>\frac{93}{20000}
\]
whenever the **base Montgomery--Taylor profile** reverses real collapse.

## Why it may matter

A positive answer eliminates the first larger-cardinality scalar failure discovered after the five-point theorem as an actual obstruction to the central-notch route. It separates a real sign change in the collapse energy from saturation of the affine counting inequality and prevents repeated optimization inside a mechanism that is already screened.

## Decisive test

Independently certify the one-dimensional function
\[
Q(t)=8F_{\rm MT}(t)+K(t)+K_0/3
\]
on the only possible active interval `0.545<|t|<1.01`, then combine the resulting spatial surplus with the exact six-point slack identities of `ANF-068` and the all-order height floor and height compactification of `ANF-069`. A failed spatial certificate, multiplicity error, or notch-energy bound would refute the proposed implication.

`ANF-070` performs exactly this test: an independent rational interval mesh plus an analytic Lipschitz bound proves `Q(t)>0.005246646` on the active interval, and the downstream rational endpoint calculation gives
\[
\mathcal S_{\rm MT}(W_{y,T})>\frac{93}{10000}
\]
throughout the negative-curvature class. On the actual reversing branch, the height bound makes the notch loss smaller than `80s b_\eta\eta`, yielding the displayed notched margin.

## Evidence boundary

The resolved result concerns only the fixed Montgomery--Taylor one-pair/six-point base-reversal mechanism. It does not prove the full notched six-point inequality, because configurations whose base profile does not reverse collapse can respond differently to the perturbation. It also does not cover multiple nonreal pairs, total cardinality eleven and above, another spectrum, a universal affine inequality, or RH.

The canonical evidence is `ANF-070`, not this clue or the earlier exploratory compute execution.

## Research disposition

Outcome: supported

Resolved by:
- [[research/analytic_frontier/findings/ANF-070-certified-spatial-floor-screens-complete-montgomery-taylor-one-pair-six-point-collapse-reversal.md]]

`ANF-070` independently validates the compact curvature-deficit certificate and proves the full base-reversal screening and central-notch branch margin stated above. The remaining six-point question, if pursued, must therefore come from a different geometry or from notch behavior outside the base Montgomery--Taylor reversal branch rather than from further tuning of this curvature-seeded mechanism.
