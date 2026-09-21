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
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The source side has already collapsed to the normalized Chebyshev-theta remainder

`G(u)=e^(-u)theta(e^u)-1`.

`VIS-333`--`VIS-340` show that Wang's prime and square-log summatory channels are exact transforms of the same source and that pointwise inversion repays one derivative. `VIS-341`--`VIS-353` price the bounded finite-bank geometry: fixed smoothing order, dilation count, translation fibers, moving/shrinking windows, phase entropy, higher tail moments, confluent propagation, phase collisions, and cancellation among a fixed separated family of stable cluster blocks.

`VIS-354` identifies the upstream coefficient map itself: for fixed asymptotic depth `q`, each translation fiber has the source-free truncated Vandermonde map

`d_b=D_beta V_b c_b`.

`VIS-355` now closes the weakest source-adaptive escape. On any fixed compact nondegenerate family of such scale geometries, the smallest nonzero singular value is uniformly positive, so

`||T_theta c||_2 >= sigma dist(c,ker T_theta)`

uniformly. This inequality remains true pointwise when `theta` and `c` are chosen from `G`. Thus **adaptive selection from an already-uniformly-conditioned bounded family is not a new arithmetic cancellation resource**. Small tail coefficients still mean approach to the classical moment kernel or departure from the compact assumptions.

## Research question

After quotienting bounded source-independent banks **and bounded source-adaptive selection inside the same compact ledger**, can a genuinely source-coupled or growing/global construction produce a smaller Wang destination without merely importing a stronger estimate for `G`, `theta`, or an equivalent unsmoothed source quantity?

The remaining live mechanisms must expose a real resource outside that regime: growing scale count or tail depth, inverse-scale geometry escaping compactness, growing cluster count/multiplicity/span/density, collapsing inter-cluster hierarchy, shrinking windows, an infinite representation, nonlinear source dependence, or direct signed arithmetic structure of `G`.

## Why it may matter

The finite-bank story now separates filter selection from arithmetic information. A source may choose among bounded filters, but a uniform quotient lower bound survives that choice. Therefore a positive result must identify where genuinely new information or asymptotic complexity enters rather than attributing the gain to the word “adaptive.”

This makes the next source-coupled proposal easier to falsify: either it quantifies an escaping geometric/complexity parameter or it proves a new signed statement about the arithmetic source. If it does neither, it remains inside the already-closed compact filter geometry.

## Decisive test

For any proposed continuation, first state exactly which closed assumption is being abandoned.

If a source-dependent selector keeps fixed dimension, bounded separated inverse scales, bounded phase geometry, and a fixed reference window, apply `VIS-355` before crediting any gain. Measure coefficients modulo the exact moment-cancellation kernel. A selector that merely moves closer to that kernel is filter design, not new source localization.

If geometry escapes the compact regime, record the escape quantitatively: scale count/depth, inverse-scale range or collision, phase-cluster count/multiplicity/span/density, inter-cluster separation, or window length. Reduce the resulting filter geometry through `VIS-343`--`VIS-355` before crediting a new power gain.

If coefficients, scales, translations, or selection rules use signed information from `G`, `theta`, or another arithmetic statistic in a way not reducible to compact filter selection, formulate the claimed gain directly as an arithmetic/source estimate. Show that the information used to choose the bank is not equivalent to assuming the desired stronger source bound, and propagate the estimate through Wang's full destination, including every `Q'` or equivalent inverse-derivative repayment.

For an infinite representation, specify the convergence topology, coefficient norm, truncation control, and finite approximants that preserve the claimed gain.

Kill a route if its improvement disappears after the explicit growth/degeneration parameter is charged, if adaptive weights merely approach the known moment kernel, if source-dependent weights encode the target source estimate, or if the gain is lost in the destination derivative step.

## Evidence boundary

`VIS-333`--`VIS-355` are exact representation, obstruction, conditioning, compactness, and finite-dimensional negative-control results. They do not prove a stronger PNT remainder, a new pointwise estimate for `G`, an RH-equivalent localization theorem, or a destination-level improvement.

`VIS-355` does not rule out source-dependent banks that **leave** the compact bounded family, nonlinear operations on `G`, infinite constructions, or direct signed cancellation. It establishes only that source-adaptive selection *within* a uniformly conditioned bounded family obeys the same quotient floor as source-independent selection.

The clue therefore remains `accepted`, but its unresolved frontier is now restricted to an explicit escaping resource or genuinely new arithmetic source information.

## Research disposition

Outcome: **narrowed**.

Treat bounded source-independent coefficient conditioning and bounded source-adaptive selection as closed. Future work should quantify the first resource that genuinely leaves the compact ledger, or formulate a new signed/infinite source mechanism and test whether its information survives the unchanged Wang destination audit.