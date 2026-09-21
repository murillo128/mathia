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
  - research/visual_exploration/findings/VIS-358-dense-cluster-occupancy-width-floor.md
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The source side has already collapsed to the normalized Chebyshev-theta remainder

`G(u)=e^(-u)theta(e^u)-1`.

`VIS-333`--`VIS-340` show that Wang's prime and square-log summatory channels are exact transforms of the same source and that pointwise inversion repays one derivative. `VIS-341`--`VIS-353` price the bounded finite-bank geometry: fixed smoothing order, dilation count, translation fibers, moving/shrinking windows, phase entropy, higher tail moments, confluent propagation, phase collisions, and cancellation among a fixed separated family of stable cluster blocks.

`VIS-354` identifies the upstream coefficient map itself: for fixed asymptotic depth `q`, each translation fiber has the source-free truncated Vandermonde map

`d_b=D_beta V_b c_b`.

`VIS-355` closes bounded source-adaptive selection inside a compact nondegenerate family. `VIS-356` shows that raw scale-count growth cannot lower the quotient floor while one uniformly conditioned `q`-column anchor survives. `VIS-357` classifies the complementary loss of every compact square anchor as shrinking `q`-point packing, equivalently concentration into fewer than `q` shrinking inverse-scale clusters.

`VIS-358` now shows why square-anchor collapse is not the same thing as full rectangular degeneration. For an equally spaced one-cluster bank of `N` distinct inverse scales inside width `2 epsilon` around a positive center,

`s_q(D_beta V_(N,epsilon)) asymp sqrt(N) epsilon^(q-1)`.

Thus every fixed `q`-column anchor can collapse while the full quotient floor remains bounded or even grows. Under the current Euclidean bank norm, the canonical compact tradeoff is occupancy against the deepest available cluster jet: `N epsilon^(2(q-1))`.

## Research question

After quotienting bounded source-independent banks, bounded source-adaptive selection, anchored bank enlargement, compact square-anchor loss, and the regular one-cluster occupancy repayment, can a genuinely source-coupled or growing/global construction produce a smaller Wang destination without merely importing a stronger estimate for `G`, `theta`, or an equivalent unsmoothed source quantity?

The remaining live mechanisms must expose a real resource outside that ledger: growing tail depth/order; an irregular or weighted clustered rectangular geometry whose scaled polynomial-sampling Gram genuinely degenerates after the coefficient norm is fixed; several clusters with a nontrivial jet-allocation interaction; scale escape toward zero or infinity; growing/global phase complexity; shrinking windows; an infinite-dimensional topology; nonlinear source dependence; or direct signed arithmetic structure of `G`.

## Why it may matter

The compact fixed-depth branch is now more sharply constrained. Destroying every square anchor is only a geometric warning. `VIS-358` gives an explicit family in which all such anchors collapse but multiplicity restores the full row-space conditioning exactly at the scale `sqrt(N) epsilon^(q-1)`.

A positive compact-bank mechanism must therefore show that its cluster geometry defeats this repayment after the actual coefficient norm and weights are included. Otherwise “many colliding scales” is another coordinate description of source-free finite-dimensional conditioning rather than a new arithmetic localization resource.

## Decisive test

For any proposed continuation, first state exactly which closed assumption is being abandoned.

If a source-dependent selector stays inside a fixed compact nondegenerate family, apply `VIS-355` before crediting any gain. Measure coefficients modulo the exact moment-cancellation kernel.

If the number of scales grows at fixed asymptotic depth while one uniformly conditioned `q`-column anchor survives, apply `VIS-356`: raw count growth is closed as an independent conditioning resource.

If every fixed-depth square anchor degenerates inside a compact interval, apply `VIS-357` to identify the shrinking-cluster geometry, then apply `VIS-358` as the first full-map control. A regular one-cluster bank with width `epsilon` and occupancy `N` has full quotient scale `sqrt(N) epsilon^(q-1)`; anchor collapse alone is therefore insufficient.

For a claimed compact escape beyond `VIS-358`, state the coefficient norm/column weights and rescale each cluster to its center and width. Show that the corresponding fixed-degree polynomial-sampling or jet Gram loses rank/conditioning in a way not repaid by effective occupancy. In a multicluster proposal, identify which derivative orders are supplied by which clusters and prove that the combined rectangular Gram still develops a small positive eigenvalue. Do not infer this from pairwise collisions or bad square minors.

If the effective cancellation depth grows, combine `VIS-342`--`VIS-343` with the conditioning of the growing moment system. If downstream phase geometry also grows or degenerates, price its cluster count/multiplicity/span/density, separation, and window length through `VIS-344`--`VIS-353`.

If coefficients, scales, translations, weights, or selection rules use signed information from `G`, `theta`, or another arithmetic statistic, formulate the claimed gain directly as an arithmetic/source estimate. Show that the information used to choose the bank is not equivalent to assuming the desired stronger source bound, and propagate the estimate through Wang's full destination, including every `Q'` or equivalent inverse-derivative repayment.

For an infinite representation, specify the convergence topology, coefficient norm, truncation control, and finite approximants that preserve the claimed gain.

Kill a route if its improvement disappears after the explicit growth/degeneration parameter is charged, if adaptive weights merely approach the known moment kernel, if extra scales leave a stable anchor intact, if regular cluster occupancy restores the full-map floor as in `VIS-358`, if a changed norm or weighting is doing the real work but is not priced, if source-dependent weights encode the target source estimate, or if the gain is lost in the destination derivative step.

## Evidence boundary

`VIS-333`--`VIS-358` are exact representation, obstruction, conditioning, compactness, packing, and finite-dimensional negative-control results. They do not prove a stronger PNT remainder, a new pointwise estimate for `G`, an RH-equivalent localization theorem, or a destination-level improvement.

`VIS-358` proves the occupancy-width law only for a canonical equally spaced one-cluster family under the current unweighted Euclidean coefficient norm. It does not classify arbitrary irregular point clouds, multiple interacting clusters, nonuniform weights, or other coefficient topologies. Those are now the precise compact questions rather than the already-refuted implication “all square anchors collapse, therefore the rectangular bank degenerates.”

The clue therefore remains `accepted`, but its compact frontier is narrowed to an actual degeneration of the scaled clustered sampling/jet Gram after occupancy, weights, and norm are accounted for. Growing order, scale escape, phase/window/infinite-dimensional resources, and genuinely new arithmetic source information remain separate exits.

## Research disposition

Outcome: **narrowed**.

Treat bounded source-independent conditioning, bounded source-adaptive selection, anchored fixed-depth scale growth, diffuse compact anchor loss, and regular one-cluster anchor collapse as closed. Future compact-bank work must exhibit a weighted/irregular/multicluster rectangular degeneration that survives the `VIS-358` occupancy control; other continuations must expose growing order, scale escape, infinite/nonlinear structure, or a new signed source estimate that survives the unchanged Wang destination audit.