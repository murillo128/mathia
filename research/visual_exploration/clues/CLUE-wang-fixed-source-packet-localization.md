---
id: CLUE-visual-wang-fixed-source-packet-localization
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-333-wang-summatory-log-frequency-transfer.md
  - research/visual_exploration/findings/VIS-334-wang-summatory-pointwise-inverse-derivative-tax.md
  - research/visual_exploration/findings/VIS-339-wang-prime-source-chebyshev-theta-differential-image.md
  - research/visual_exploration/findings/VIS-340-wang-prime-squarelog-partial-summation-invertible.md
  - research/visual_exploration/findings/VIS-341-vk-scale-stable-under-finite-spectral-smoothing.md
  - research/visual_exploration/findings/VIS-342-vk-power-gain-requires-growing-truncation-order.md
  - research/visual_exploration/findings/VIS-343-wang-dilate-mixture-cancellation-order.md
  - research/visual_exploration/findings/VIS-344-wang-translated-dilate-cancellation-fibers.md
  - research/visual_exploration/findings/VIS-345-long-window-phase-resolution.md
  - research/visual_exploration/findings/VIS-346-turan-nazarov-short-window-obstruction.md
  - research/visual_exploration/findings/VIS-347-variable-wang-phase-entropy-budget.md
  - research/visual_exploration/findings/VIS-348-higher-wang-moments-inherit-phase-entropy-gate.md
  - research/visual_exploration/findings/VIS-349-wang-cross-order-confluent-exponential-polynomial.md
  - research/visual_exploration/findings/VIS-350-confluent-turan-total-multiplicity.md
  - research/visual_exploration/findings/VIS-351-divided-difference-cluster-conditioning.md
  - research/visual_exploration/findings/VIS-352-hermite-collision-scale-budget.md
  - research/visual_exploration/findings/VIS-353-separated-cluster-block-riesz-floor.md
  - research/visual_exploration/findings/VIS-354-wang-tail-coefficient-block-vandermonde.md
  - research/visual_exploration/findings/VIS-355-source-adaptive-compact-bank-floor.md
  - research/visual_exploration/findings/VIS-356-fixed-depth-bank-growth-anchored-floor.md
  - research/visual_exploration/findings/VIS-357-compact-wang-anchor-packing-collapse.md
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The source side has already collapsed to the normalized Chebyshev-theta remainder

`G(u)=e^(-u)theta(e^u)-1`.

`VIS-333`--`VIS-340` show that Wang's prime and square-log summatory channels are exact transforms of the same source and that pointwise inversion repays one derivative. `VIS-341`--`VIS-353` price the bounded finite-bank geometry: fixed smoothing order, dilation count, translation fibers, moving/shrinking windows, phase entropy, higher tail moments, confluent propagation, phase collisions, and cancellation among a fixed separated family of stable cluster blocks.

`VIS-354` identifies the upstream coefficient map itself: for fixed asymptotic depth `q`, each translation fiber has the source-free truncated Vandermonde map

`d_b=D_beta V_b c_b`.

`VIS-355` closes bounded source-adaptive selection inside a compact nondegenerate family: after quotienting the exact moment kernel, a uniform smallest-nonzero-singular-value floor survives pointwise even when `G` chooses the admissible bank.

`VIS-356` separates **raw scale-count growth** from genuine order growth. If a growing fixed-depth bank retains one uniformly conditioned `q`-scale anchor, appending arbitrarily many additional columns only adds positive-semidefinite Gram mass, so the quotient singular-value floor cannot decrease.

`VIS-357` now classifies the complementary compact anchor-loss alternative. If `delta_q(X)` is the best minimum separation among `q` inverse scales in a compact bank and `alpha_q(X)` is the best `q`-column Wang anchor singular value, then for constants depending only on fixed `q`, `[r,R]`, and `D_beta`,

`c delta_q(X)^(q(q-1)/2) <= alpha_q(X) <= C delta_q(X)`.

Hence `alpha_q->0` exactly when `delta_q->0`, equivalently when the inverse-scale bank becomes coverable at every fixed resolution by at most `q-1` shrinking clusters. Compact loss of every fixed-depth anchor is therefore explicit cluster collapse, not diffuse many-scale complexity.

## Research question

After quotienting bounded source-independent banks, bounded source-adaptive selection, anchored fixed-depth bank enlargement, and the compact geometry of total anchor loss, can a genuinely source-coupled or growing/global construction produce a smaller Wang destination without merely importing a stronger estimate for `G`, `theta`, or an equivalent unsmoothed source quantity?

The remaining live mechanisms must expose a real resource outside the closed ledger: growing tail depth/order; a favorable quantitative tradeoff between shrinking scale-cluster widths and growing occupancies/weights in the **full rectangular** moment map; scale escape toward zero or infinity; growing/global phase complexity; shrinking windows; an infinite-dimensional topology not captured by the finite Euclidean quotient; nonlinear source dependence; or direct signed arithmetic structure of `G`.

## Why it may matter

The finite-bank story now distinguishes dimensional abundance from actual asymptotic power. A source may choose among bounded filters, and a bank may accumulate arbitrarily many extra scales, without weakening the fixed-depth quotient floor while a stable anchor survives. `VIS-357` further shows that destroying every such anchor inside compact scale geometry has only one geometric form: concentration into fewer than `q` shrinking clusters.

This makes the remaining compact escape quantitatively testable. It is no longer enough to say that “all anchors become ill-conditioned.” A candidate must specify cluster widths, occupancies/weights, and the coefficient normalization, then show on the full rectangular map that multiplicity does not repay the apparent collision gain. Failure to do so confuses failure of a sufficient square-anchor condition with actual degeneration of the bank operator.

## Decisive test

For any proposed continuation, first state exactly which closed assumption is being abandoned.

If a source-dependent selector stays inside a fixed compact nondegenerate family, apply `VIS-355` before crediting any gain. Measure coefficients modulo the exact moment-cancellation kernel.

If the number of scales grows while the asymptotic depth `q` remains fixed and one uniformly conditioned `q`-column anchor survives, apply `VIS-356`: raw count growth is closed as an independent conditioning resource.

If every fixed-depth anchor is claimed to degenerate while all inverse scales remain in a fixed `[r,R]`, apply `VIS-357`. Replace the qualitative anchor-loss statement by the equivalent shrinking-cluster geometry. Track the cluster radii, cluster occupancies/weights, and the full rectangular Gram/singular-value behavior. **Do not infer full-map degeneration from `alpha_q->0` alone**: many near-colliding columns add positive-semidefinite Gram mass and may compensate the shrinking anchor scale.

If the effective cancellation depth grows, combine `VIS-342`--`VIS-343` with the conditioning of the growing moment system; scale count matters only insofar as it supports that increasing order. If downstream phase geometry also grows or degenerates, price its cluster count/multiplicity/span/density, separation, and window length through `VIS-344`--`VIS-353`.

If coefficients, scales, translations, or selection rules use signed information from `G`, `theta`, or another arithmetic statistic in a way not reducible to compact filter selection, anchored bank enlargement, or compact scale clustering, formulate the claimed gain directly as an arithmetic/source estimate. Show that the information used to choose the bank is not equivalent to assuming the desired stronger source bound, and propagate the estimate through Wang's full destination, including every `Q'` or equivalent inverse-derivative repayment.

For an infinite representation, specify the convergence topology, coefficient norm, truncation control, and finite approximants that preserve the claimed gain.

Kill a route if its improvement disappears after the explicit growth/degeneration parameter is charged, if adaptive weights merely approach the known moment kernel, if extra scales leave a stable fixed-depth anchor intact, if compact anchor loss reduces to shrinking clusters whose multiplicity restores the full-map floor, if source-dependent weights encode the target source estimate, or if the gain is lost in the destination derivative step.

## Evidence boundary

`VIS-333`--`VIS-357` are exact representation, obstruction, conditioning, compactness, packing, and finite-dimensional negative-control results. They do not prove a stronger PNT remainder, a new pointwise estimate for `G`, an RH-equivalent localization theorem, or a destination-level improvement.

`VIS-357` classifies degeneration of the **best square `q`-column anchor** inside fixed compact scale geometry. It does not prove that the full rectangular Wang moment map becomes ill-conditioned when all such anchors collapse. The unresolved compact question is precisely whether growing cluster multiplicity/weights can or cannot offset shrinking cluster width under the relevant quotient normalization.

The clue therefore remains `accepted`, but its unresolved frontier is now restricted to that explicit cluster-width/multiplicity tradeoff, genuinely growing order, scale escape, another phase/window/infinite-dimensional resource, or genuinely new arithmetic source information.

## Research disposition

Outcome: **narrowed**.

Treat bounded source-independent coefficient conditioning, bounded source-adaptive selection, anchored fixed-depth scale-count growth, and diffuse compact anchor loss as closed. Future compact-bank work should analyze the full clustered rectangular moment map rather than square anchors; other continuations must expose growing order, scale escape, infinite/nonlinear structure, or a new signed source estimate that survives the unchanged Wang destination audit.