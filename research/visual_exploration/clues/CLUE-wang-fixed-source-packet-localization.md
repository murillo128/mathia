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
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The source side has already collapsed to the normalized Chebyshev-theta remainder

`G(u)=e^(-u)theta(e^u)-1`.

`VIS-333`--`VIS-340` show that Wang's prime and square-log summatory channels are exact transforms of the same source and that pointwise inversion repays one derivative. The subsequent chain `VIS-341`--`VIS-353` prices the bounded source-independent finite-bank geometry: fixed smoothing order, dilation count, translation fibers, moving/shrinking windows, phase entropy, higher tail moments, confluent propagation, phase collisions, and cancellation among a fixed separated family of stable cluster blocks.

`VIS-354` closes the remaining bounded coefficient-conditioning ambiguity. For fixed asymptotic depth `q`, the raw polynomial coefficients in each translation fiber are exactly

`d_b=D_beta V_b c_b`,

where `(V_b)_(k,j)=a_j^(-k)` is an ordinary truncated Vandermonde moment matrix. Across translations the map is block diagonal. The arithmetic source does not enter it.

If a fiber has at most `q` distinct scales in a fixed compact separated inverse-scale geometry, this map has a uniform lower singular value. If it has more than `q` scales, its kernel is exactly the familiar first-`q` moment-cancellation space from `VIS-343`/`VIS-344`; near-kernel smallness is approximate filter-design cancellation, not source localization. Any genuine source-to-coefficient map therefore begins only when the bank parameters or selection rule depend on `G` or equivalent arithmetic information.

## Research question

After quotienting all bounded source-independent finite-bank mechanisms, can a genuinely **source-coupled or growing/global** construction produce a smaller Wang destination without merely importing a stronger estimate for `G`, `theta`, or an equivalent unsmoothed source quantity?

The remaining live mechanisms must expose at least one real resource outside the closed compact regime: growing scale count or tail depth, inverse-scale geometry escaping compactness, growing cluster count/multiplicity/span/density, collapsing inter-cluster hierarchy, shrinking windows, frequency/source-dependent coefficients, an infinite representation, or direct signed arithmetic structure of `G`.

## Why it may matter

The finite-bank story is now conceptually cleaner. There is no hidden arithmetic conditioning left between source-independent bank weights and the confluent Wang tail: the upstream coefficient map is classical block-Vandermonde linear algebra, while the downstream phase geometry has explicit collision and Riesz budgets.

A positive result must therefore identify where new information enters. That makes source-adaptive proposals testable rather than allowing them to borrow unexplained smallness from filter coordinates, and it separates honest growing-complexity mechanisms from bounded-dimensional representation artifacts.

## Decisive test

For any proposed continuation, first state explicitly which closed assumption is being abandoned.

If bank parameters are still source-independent, record the growth/degeneration parameter quantitatively: scale count/depth, inverse-scale range or collision, phase-cluster count/multiplicity/span/density, inter-cluster separation, or window length. Reduce the resulting filter geometry through `VIS-343`--`VIS-354` before crediting any new power gain.

If coefficients, scales, translations, or selection rules depend on `G`, `theta`, signs, or another arithmetic statistic, write that dependence explicitly and formulate the claimed gain directly as a signed/source estimate. Show that the information used to choose the bank is not equivalent to assuming the desired stronger source bound, and then propagate the estimate through Wang's full destination, including every `Q'` or equivalent inverse-derivative repayment.

For an infinite representation, specify the convergence topology, coefficient norm, truncation control, and the finite approximants that preserve the claimed gain. A formal infinite superposition is not evidence unless the gain survives approximation and destination reconstruction.

Kill a route if its improvement disappears after the explicit growth parameter is charged, if its small coefficients reduce to source-free moment cancellation, if source-adaptive weights merely encode the target source estimate, or if the gain is lost in the derivative/destination step.

## Evidence boundary

`VIS-333`--`VIS-354` are exact representation, obstruction, conditioning, and finite-dimensional negative-control results. They do not prove a stronger PNT remainder, a new pointwise estimate for `G`, an RH-equivalent localization theorem, or a destination-level improvement.

In particular, `VIS-354` does not rule out source-dependent/adaptive coefficients or growing/infinite constructions. It establishes only that **under the bounded source-independent finite-bank assumptions there is no separate source-to-polynomial-coefficient channel to exploit**.

The clue therefore remains `accepted`, but its unresolved frontier has moved entirely outside that compact finite-bank regime.

## Research disposition

Outcome: **narrowed**.

Treat bounded source-independent coefficient conditioning as closed. Future work should either quantify an explicit escaping geometric/complexity parameter or formulate a genuinely source-dependent/infinite/signed mechanism and test whether its information survives the unchanged Wang destination audit.