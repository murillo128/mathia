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
  - research/visual_exploration/findings/VIS-359-regular-multicluster-hermite-jet-capacity.md
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The source side has already collapsed to the normalized Chebyshev-theta remainder

`G(u)=e^(-u)theta(e^u)-1`.

`VIS-333`--`VIS-340` show that Wang's prime and square-log summatory channels are exact transforms of the same source and that pointwise inversion repays one derivative. `VIS-341`--`VIS-353` price the bounded finite-bank geometry: fixed smoothing order, dilation count, translation fibers, moving/shrinking windows, phase entropy, higher tail moments, confluent propagation, phase collisions, and cancellation among a fixed separated family of stable cluster blocks.

`VIS-354` identifies the upstream coefficient map itself: for fixed asymptotic depth `q`, each translation fiber has the source-free truncated Vandermonde map

`d_b=D_beta V_b c_b`.

`VIS-355` closes bounded source-adaptive selection inside a compact nondegenerate family. `VIS-356` shows that raw scale-count growth cannot lower the quotient floor while one uniformly conditioned `q`-column anchor survives. `VIS-357` classifies the complementary loss of every compact square anchor as shrinking `q`-point packing, equivalently concentration into fewer than `q` shrinking inverse-scale clusters.

`VIS-358` shows that square-anchor collapse is not the same thing as full rectangular degeneration: an equally spaced one-cluster bank of width `2 epsilon` and occupancy `N` has

`s_q(D_beta V_(N,epsilon)) asymp sqrt(N) epsilon^(q-1)`.

`VIS-359` now closes the regular separated multicluster extension. If cluster `ell` has occupancy `N_ell asymp epsilon_ell^(-2a_ell)`, it supplies exactly

`kappa_ell=floor(a_ell)+1`

stable Hermite jets under the current Euclidean normalization. These capacities add across separated cluster centers. The fixed-depth quotient stays uniformly nondegenerate exactly when the total regular jet capacity reaches `q`; if the total remains below `q`, an explicit polynomial vanishing to the corresponding orders at every center drives the quotient floor to zero.

## Research question

After quotienting bounded source-independent banks, bounded source-adaptive selection, anchored bank enlargement, compact square-anchor loss, regular one-cluster occupancy repayment, and regular separated multicluster Hermite-jet capacity, can a genuinely source-coupled or growing/global construction produce a smaller Wang destination without merely importing a stronger estimate for `G`, `theta`, or an equivalent unsmoothed source quantity?

The remaining live mechanisms must expose a real resource outside that ledger: an irregular or weighted clustered rectangular geometry whose **scaled local sampling Gram** degenerates beyond its effective jet capacity; cluster centers whose mutual separation also collapses; growing tail depth/order; scale escape toward zero or infinity; growing/global phase complexity; shrinking windows; an infinite-dimensional topology; nonlinear source dependence; or direct signed arithmetic structure of `G`.

## Why it may matter

The compact fixed-depth branch is now close to a classification rather than a collection of examples. `VIS-358` priced one dense cluster; `VIS-359` shows that several regular separated clusters simply pool local Hermite conditions. Dense scale clouds do not acquire extra arithmetic power merely by being split among several compact centers.

A positive compact-bank mechanism must therefore identify an actual failure of the regular jet ledger: irregular local sampling that loses polynomial-sampling rank after rescaling, nonuniform weights or a changed norm that alter effective mass, collapsing center separation that turns separate Hermite blocks into a higher confluence problem, or source-dependent coefficients carrying information not present in the source-free bank geometry.

## Decisive test

For any proposed continuation, first state exactly which closed assumption is being abandoned.

If a source-dependent selector stays inside a fixed compact nondegenerate family, apply `VIS-355` before crediting any gain. Measure coefficients modulo the exact moment-cancellation kernel.

If the number of scales grows at fixed asymptotic depth while one uniformly conditioned `q`-column anchor survives, apply `VIS-356`: raw count growth is closed as an independent conditioning resource.

If every fixed-depth square anchor degenerates inside a compact interval, apply `VIS-357` to identify the shrinking-cluster geometry. For one regular cluster, apply `VIS-358` and charge the occupancy-width scale `N epsilon^(2(q-1))`.

For several regular clusters with fixed positive separated centers, apply `VIS-359`. In general choose Hermite multiplicities `m_ell` summing to `q`; a uniform lower bound follows whenever the deepest assigned jet masses `N_ell epsilon_ell^(2(m_ell-1))` stay bounded below. In the power-law regime compute `kappa_ell=floor(a_ell)+1`: total capacity at least `q` closes quotient degeneration, while total capacity below `q` produces the explicit source-free collapsing polynomial from `VIS-359`.

A claimed compact escape beyond `VIS-359` must therefore show why this Hermite allocation model fails. For irregular point clouds, rescale each cluster and study the actual fixed-degree polynomial-sampling Gram rather than nominal point count. For weights, state the coefficient norm and effective sample masses explicitly. If cluster centers themselves collide, price the resulting higher-level confluent geometry rather than treating the blocks as separated. Do not infer degeneration from pairwise collisions, bad square minors, or large raw occupancy alone.

If the effective cancellation depth grows, combine `VIS-342`--`VIS-343` with the conditioning of the growing moment system. If downstream phase geometry also grows or degenerates, price its cluster count/multiplicity/span/density, separation, and window length through `VIS-344`--`VIS-353`.

If coefficients, scales, translations, weights, or selection rules use signed information from `G`, `theta`, or another arithmetic statistic, formulate the claimed gain directly as an arithmetic/source estimate. Show that the information used to choose the bank is not equivalent to assuming the desired stronger source bound, and propagate the estimate through Wang's full destination, including every `Q'` or equivalent inverse-derivative repayment.

For an infinite representation, specify the convergence topology, coefficient norm, truncation control, and finite approximants that preserve the claimed gain.

Kill a route if its improvement disappears after the explicit growth/degeneration parameter is charged, if adaptive weights merely approach the known moment kernel, if extra scales leave a stable anchor intact, if regular one- or multicluster occupancy restores the full-map floor as in `VIS-358`--`VIS-359`, if a changed norm or weighting is doing the real work but is not priced, if source-dependent weights encode the target source estimate, or if the gain is lost in the destination derivative step.

## Evidence boundary

`VIS-333`--`VIS-359` are exact representation, obstruction, conditioning, compactness, packing, Hermite-interpolation, and finite-dimensional negative-control results. They do not prove a stronger PNT remainder, a new pointwise estimate for `G`, an RH-equivalent localization theorem, or a destination-level improvement.

`VIS-359` classifies **regular equally spaced clusters with fixed separated centers** under the current unweighted Euclidean coefficient norm, including an exact power-law occupancy dichotomy. It does not classify arbitrary irregular cluster point clouds, nonuniform weights, collapsing inter-center separations, growing asymptotic depth, or other coefficient topologies. Those are now the precise compact questions rather than generic “multicluster interaction.”

The clue therefore remains `accepted`, but its compact frontier is narrowed to a genuine failure of the regular Hermite-jet ledger after the actual local sampling Gram, weights, center separation, and norm are accounted for. Growing order, scale escape, phase/window/infinite-dimensional resources, and genuinely new arithmetic source information remain separate exits.

## Research disposition

Outcome: **narrowed**.

Treat bounded source-independent conditioning, bounded source-adaptive selection, anchored fixed-depth scale growth, diffuse compact anchor loss, regular one-cluster collapse, and regular separated multicluster occupancy as closed. Future compact-bank work must exhibit irregular/weighted/colliding-center geometry that survives the `VIS-358`--`VIS-359` controls; other continuations must expose growing order, scale escape, infinite/nonlinear structure, or a new signed source estimate that survives the unchanged Wang destination audit.