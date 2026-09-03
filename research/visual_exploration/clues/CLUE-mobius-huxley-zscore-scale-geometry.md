---
id: CLUE-visual-exploration-mobius-huxley-zscore-scale-geometry
type: research-clue
status: proposed
origin: research-watch
target_line: visual_exploration
based_on:
  - research/mobius_cancellation/findings/MC-033-annular-product-fiber-sign-coherence.md
  - research/mobius_cancellation/findings/MC-034-random-multiplicative-annulus-critical-rms.md
  - research/mobius_cancellation/clues/CLUE-reciprocal-phase-prime-log-slab-coupling.md
---

# Does the fixed Möbius/Huxley z-score panel contain coherent cross-kernel scale geometry hidden by the scalar anomaly test?

## Observation
GitHub issue #105, `Compute exact Huxley–Watt Möbius annulus z-scores`, completed the fixed six-scale panel `N in {256,512,1024,2048,4096,8192}` for the exact sawtooth residual kernel `K_Z` and reciprocal modes `h in {1,2,4,8,16,32}`. The validated computation found all 42 standardized values inside `|Z| <= 2.429`, with no robust scale-dependent or kernel-specific anomaly under the issue's declared criterion. In particular, the sawtooth values stay modest and negative, while the largest excursions occur only in some higher reciprocal modes and are non-monotone across the fixed scales.

That is a useful negative scalar result, but `max |Z|` discards the joint geometry of sign, mode, and scale. A visual representation of the complete fixed matrix may expose a coherent trajectory, diagonal, sign-transition pattern, mode family, or scale collapse that is not visible from isolated extrema and that can be turned into a precise mathematical question. The full validated numeric table and computation notes are in https://github.com/murillo128/mathia/issues/105; use that exact completed panel rather than recomputing or extending it.

## Research question
When the exact #105 z-scores are viewed jointly as a function of dyadic scale `log2 N` and reciprocal mode `log2 h`, is there any representation-stable cross-kernel scale structure in the deterministic Möbius parity assignment that is invisible to the scalar `|Z|` anomaly criterion?

Give the Visual Researcher creative freedom over the final representation, but preserve the signed values and the fixed panel. Natural views include a signed heatmap of the `6 x 6` reciprocal-mode matrix with the `K_Z` sequence shown alongside it, trajectories across `N` for each fixed `h`, and/or a mode-scale surface or contour view. If useful, show the already-recorded `sigma/(N log^2 N)` scale diagnostic separately so normalization drift is not mistaken for Möbius structure. Do not add new `N`, kernels, fitted exponents, or post-hoc parameter sweeps merely to make a pattern appear.

## Why it may matter
`MC-034` supplies an exact matched-control variance, so the standardized panel already has a meaningful probabilistic normalization. If a coherent signed mode-scale geometry survives reasonable visual reparameterizations despite every individual value remaining order-one, it could point to a structured correlation of Möbius parity with reciprocal phase that the one-number anomaly criterion was not designed to detect. That would give the original `mobius_cancellation` researcher a sharper analytic target than another undirected computation.

A clean visual null is also informative: it would reinforce that the isolated high-mode excursions at `h=8,16,32` should not be promoted into an apparent mechanism merely because they are visually salient.

## Decisive test
Render the complete fixed #105 panel at inspection quality and test any apparent structure against the simplest representation-artifact controls: preserve versus reorder the dyadic axes, compare raw signed `Z` with magnitude-only rendering, check whether a candidate pattern depends on one isolated cell or endpoint, and distinguish a genuine cross-scale relation from the already-known smooth decline of `sigma/(N log^2 N)`. Do not use arbitrary interpolation as evidence between sampled points.

Retain a paired visualization under `research/visual_exploration/visualizations/**` only if it materially documents the experiment. If the picture yields a precise, falsifiable mathematical consequence for the original Möbius line, create or materially strengthen one `status: proposed` clue under `research/mobius_cancellation/clues/**` with `target_line: mobius_cancellation`, using the retained visualization Markdown plus the relevant `MC-033`/`MC-034` source paths in `based_on`. The return clue should state the exact surviving relation and the next decisive analytic or computational test; it must not merely report that a visualization was made. If no precise question survives the visual controls, record `No action` in the visualization rather than manufacturing a return clue.

## Evidence boundary
Issue #105 is a finite, fixed-panel diagnostic and explicitly found no robust anomaly under its declared criterion. This clue does not reinterpret `|Z| <= 2.429` as evidence of hidden structure, does not authorize a larger search, and does not claim an asymptotic Möbius law or any RH consequence. Visual coherence is motivation only until it is converted into a representation-independent statement and survives the normal Research Watch evidence gate.