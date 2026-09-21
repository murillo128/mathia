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
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The source side has already collapsed to the normalized Chebyshev-theta remainder

`G(u)=e^(-u)theta(e^u)-1`.

`VIS-333`--`VIS-340` show that Wang's prime and square-log summatory channels are exact transforms of the same source and that pointwise inversion repays one derivative. `VIS-341`--`VIS-353` price the bounded finite-bank geometry: fixed smoothing order, dilation count, translation fibers, moving/shrinking windows, phase entropy, higher tail moments, confluent propagation, phase collisions, and cancellation among a fixed separated family of stable cluster blocks.

`VIS-354` identifies the upstream coefficient map itself: for fixed asymptotic depth `q`, each translation fiber has the source-free truncated Vandermonde map

`d_b=D_beta V_b c_b`.

`VIS-355` closes bounded source-adaptive selection inside a compact nondegenerate family: after quotienting the exact moment kernel, a uniform smallest-nonzero-singular-value floor survives pointwise even when `G` chooses the admissible bank.

`VIS-356` now separates **raw scale-count growth** from genuine order growth. If a growing fixed-depth bank retains one uniformly conditioned `q`-scale anchor, appending arbitrarily many additional columns only adds positive-semidefinite Gram mass, so the quotient singular-value floor cannot decrease. Extra scales enlarge the known first-`q` moment kernel but do not create another conditioning channel. Scale count is therefore an asymptotic resource only when it enables growing cancellation depth/order or when every fixed-depth anchor itself degenerates.

## Research question

After quotienting bounded source-independent banks, bounded source-adaptive selection, and fixed-depth bank enlargement with a stable anchor, can a genuinely source-coupled or growing/global construction produce a smaller Wang destination without merely importing a stronger estimate for `G`, `theta`, or an equivalent unsmoothed source quantity?

The remaining live mechanisms must expose a real resource outside that regime: growing tail depth/order; scale geometry for which every relevant fixed-depth anchor degenerates or escapes; growing/global phase complexity; shrinking windows; an infinite-dimensional topology not captured by the finite Euclidean quotient; nonlinear source dependence; or direct signed arithmetic structure of `G`.

## Why it may matter

The finite-bank story now distinguishes dimensional abundance from actual asymptotic power. A source may choose among bounded filters, and a bank may even accumulate arbitrarily many extra scales, without weakening the fixed-depth quotient floor as long as a stable anchor survives. Thus a positive result must identify **which mathematical parameter truly grows or degenerates**, rather than crediting “adaptivity” or “many scales” by themselves.

This makes growing-bank proposals more falsifiable: either the effective tail depth grows, all stable anchors are lost in a quantified way, the functional topology changes, or the source contributes a genuinely new signed estimate. If none occurs, the construction remains inside the already-priced Wang ledger.

## Decisive test

For any proposed continuation, first state exactly which closed assumption is being abandoned.

If a source-dependent selector stays inside a fixed compact nondegenerate family, apply `VIS-355` before crediting any gain. Measure coefficients modulo the exact moment-cancellation kernel.

If the number of scales grows while the asymptotic depth `q` remains fixed, apply `VIS-356`: identify whether the bank contains a uniformly conditioned `q`-column anchor. If it does, raw count growth is closed as an independent conditioning resource. If it does not, quantify why **every** candidate anchor degenerates and charge the corresponding collision, escape, or small-scale parameter explicitly.

If the effective cancellation depth grows, combine `VIS-342`--`VIS-343` with the conditioning of the growing moment system; scale count matters only insofar as it supports that increasing order. If downstream phase geometry also grows or degenerates, price its cluster count/multiplicity/span/density, separation, and window length through `VIS-344`--`VIS-353`.

If coefficients, scales, translations, or selection rules use signed information from `G`, `theta`, or another arithmetic statistic in a way not reducible to compact filter selection or anchored bank enlargement, formulate the claimed gain directly as an arithmetic/source estimate. Show that the information used to choose the bank is not equivalent to assuming the desired stronger source bound, and propagate the estimate through Wang's full destination, including every `Q'` or equivalent inverse-derivative repayment.

For an infinite representation, specify the convergence topology, coefficient norm, truncation control, and finite approximants that preserve the claimed gain.

Kill a route if its improvement disappears after the explicit growth/degeneration parameter is charged, if adaptive weights merely approach the known moment kernel, if extra scales leave a stable fixed-depth anchor intact, if source-dependent weights encode the target source estimate, or if the gain is lost in the destination derivative step.

## Evidence boundary

`VIS-333`--`VIS-356` are exact representation, obstruction, conditioning, compactness, and finite-dimensional negative-control results. They do not prove a stronger PNT remainder, a new pointwise estimate for `G`, an RH-equivalent localization theorem, or a destination-level improvement.

`VIS-356` does not rule out growing cancellation depth, degeneration of every fixed-depth anchor, a different infinite-dimensional coefficient topology, nonlinear operations on `G`, or direct signed cancellation. It establishes only that **raw bank enlargement at fixed depth cannot lower the quotient floor while a uniformly conditioned anchor survives**.

The clue therefore remains `accepted`, but its unresolved frontier is now restricted to a genuinely growing order, a quantified loss of all fixed-depth anchors, another explicit phase/window/infinite-dimensional resource, or genuinely new arithmetic source information.

## Research disposition

Outcome: **narrowed**.

Treat bounded source-independent coefficient conditioning, bounded source-adaptive selection, and anchored fixed-depth scale-count growth as closed. Future work should quantify the first resource that truly leaves this ledger or formulate a new signed/infinite source mechanism and test whether its information survives the unchanged Wang destination audit.