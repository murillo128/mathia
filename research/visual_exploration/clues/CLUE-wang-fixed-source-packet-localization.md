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
  - research/visual_exploration/findings/VIS-360-pooled-rescaling-colliding-center-floor.md
  - research/visual_exploration/findings/VIS-361-weighted-pooled-moment-gram-floor.md
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

`VIS-359` closes the regular separated multicluster extension. If cluster `ell` has occupancy `N_ell asymp epsilon_ell^(-2a_ell)`, it supplies exactly

`kappa_ell=floor(a_ell)+1`

stable Hermite jets under the current Euclidean normalization. These capacities add across separated cluster centers.

`VIS-360` prices the first colliding-center regime. If all samples are pooled inside an outer width `rho` around a positive center and the rescaled node cloud has a uniformly nondegenerate degree-`q-1` moment Gram, then

`s_q(D_beta V) asymp sqrt(N) rho^(q-1)`.

`VIS-361` now prices arbitrary **positive diagonal coefficient weights**. If `w_j>0`, `M=sum_j w_j`, and the coefficient norm is `sum |a_j|^2/w_j`, then the relevant matrix is `D_beta V W^(1/2)`. Whenever the normalized weighted moment Gram

`M^(-1) S^* W S`

has a positive degree-`q-1` eigenvalue floor,

`s_q(D_beta V W^(1/2)) asymp sqrt(M) rho^(q-1)`.

Thus neither shrinking separation between named subclusters nor unequal positive weights are independent compact resources. After the correct outer rescaling, the invariant is the normalized positive weighted sampling measure. A genuinely new compact degeneration requires that this weighted moment Gram itself lose polynomial modes and that the loss survive further rescaling, or that the coefficient geometry leave the positive diagonal Hilbert setting.

## Research question

After quotienting bounded source-independent banks, bounded source-adaptive selection, anchored bank enlargement, compact square-anchor loss, regular one-cluster occupancy repayment, regular separated multicluster Hermite-jet capacity, pooled colliding-center configurations with a stable outer sampling Gram, and positive diagonal coefficient weights with a stable weighted Gram, can a genuinely source-coupled or growing/global construction produce a smaller Wang destination without merely importing a stronger estimate for `G`, `theta`, or an equivalent unsmoothed source quantity?

The remaining live compact mechanisms must expose a real resource outside that ledger: a **hierarchically degenerate rescaled positive weighted sampling Gram** whose deficient modes remain small after successive rescaling, a genuinely non-diagonal/indefinite coefficient topology, or source-dependent coefficients carrying signed arithmetic information. Other exits remain growing tail depth/order, scale escape toward zero or infinity, growing/global phase complexity, shrinking windows, an infinite-dimensional topology, nonlinear source dependence, or direct signed arithmetic structure of `G`.

## Why it may matter

The compact fixed-depth branch is now close to a multiscale classification. `VIS-358` prices one dense cluster; `VIS-359` prices regular separated clusters by local Hermite capacity; `VIS-360` pools colliding centers at their outer scale; `VIS-361` shows that positive nonuniform coefficient weights merely replace raw occupancy by a positive weighted moment measure.

A positive compact-bank mechanism must therefore exhibit an actual hierarchy of lost polynomial modes. If the normalized positive weighted cloud keeps a positive `q`-moment Gram at some scale, the branch closes there with the ordinary mass-width law. Only when the Gram is deficient does finer geometry become relevant, and that deficiency must then survive the next rescaling rather than being an artifact of named subclusters, raw occupancy, or unequal positive masses.

## Decisive test

For any proposed continuation, first state exactly which closed assumption is being abandoned.

If a source-dependent selector stays inside a fixed compact nondegenerate family, apply `VIS-355` before crediting any gain. Measure coefficients modulo the exact moment-cancellation kernel.

If the number of scales grows at fixed asymptotic depth while one uniformly conditioned `q`-column anchor survives, apply `VIS-356`: raw count growth is closed as an independent conditioning resource.

If every fixed-depth square anchor degenerates inside a compact interval, apply `VIS-357` to identify the shrinking-cluster geometry. For one regular cluster, apply `VIS-358` and charge the occupancy-width scale `N epsilon^(2(q-1))`.

For several regular clusters with fixed positive separated centers, apply `VIS-359`. In general choose Hermite multiplicities `m_ell` summing to `q`; a uniform lower bound follows whenever the deepest assigned jet masses `N_ell epsilon_ell^(2(m_ell-1))` stay bounded below. In the power-law regime compute `kappa_ell=floor(a_ell)+1`: total capacity at least `q` closes quotient degeneration, while total capacity below `q` produces the explicit source-free collapsing polynomial from `VIS-359`.

If the cluster centers themselves approach one another, do not treat pairwise separation as an additional escape parameter before pooling the cloud. Choose the outer diameter/scale `rho`, write every sample as `c+rho t_j`, and form the normalized degree-`q-1` sampling Gram `(1/N)S^*S`. Apply `VIS-360`: if its smallest eigenvalue stays bounded below, the whole colliding configuration has quotient scale `sqrt(N) rho^(q-1)` and is closed. Continue inward only through the Gram-deficient polynomial directions when that normalized Gram actually degenerates.

If the coefficient space uses positive diagonal weights `w_j`, set `M=sum_j w_j` and form the normalized weighted Gram `M^(-1)S^*WS`. Apply `VIS-361`: if its smallest eigenvalue stays bounded below, the weighted quotient scale is `sqrt(M) rho^(q-1)` no matter how unequal the individual positive weights are. Continue only if the normalized weighted measure itself loses polynomial rank/conditioning, or if the proposed coefficient geometry is genuinely non-diagonal or indefinite.

For a claimed compact escape beyond `VIS-361`, exhibit the deficient weighted rescaled polynomial modes at each relevant scale. A hierarchical construction must show that the next normalized Gram still loses a positive eigenvalue after the already-visible modes are quotiented or rescaled. Do not infer degeneration from pairwise collisions, bad square minors, large raw occupancy, unequal positive weights, or a chosen subcluster decomposition.

If the effective cancellation depth grows, combine `VIS-342`--`VIS-343` with the conditioning of the growing moment system. If downstream phase geometry also grows or degenerates, price its cluster count/multiplicity/span/density, separation, and window length through `VIS-344`--`VIS-353`.

If coefficients, scales, translations, weights, or selection rules use signed information from `G`, `theta`, or another arithmetic statistic, formulate the claimed gain directly as an arithmetic/source estimate. Show that the information used to choose the bank is not equivalent to assuming the desired stronger source bound, and propagate the estimate through Wang's full destination, including every `Q'` or equivalent inverse-derivative repayment.

For an infinite representation, specify the convergence topology, coefficient norm, truncation control, and finite approximants that preserve the claimed gain.

Kill a route if its improvement disappears after the explicit growth/degeneration parameter is charged, if adaptive weights merely approach the known moment kernel, if extra scales leave a stable anchor intact, if regular occupancy restores the full-map floor as in `VIS-358`--`VIS-359`, if pooled center collisions retain a stable normalized moment Gram as in `VIS-360`, if positive diagonal weights retain a stable normalized weighted moment Gram as in `VIS-361`, if a changed norm or weighting is doing the real work but is not priced, if source-dependent weights encode the target source estimate, or if the gain is lost in the destination derivative step.

## Evidence boundary

`VIS-333`--`VIS-361` are exact representation, obstruction, conditioning, compactness, packing, Hermite-interpolation, pooled-rescaling, weighted-moment, and finite-dimensional negative-control results. They do not prove a stronger PNT remainder, a new pointwise estimate for `G`, an RH-equivalent localization theorem, or a destination-level improvement.

`VIS-361` handles positive diagonal coefficient metrics when the normalized weighted polynomial-sampling Gram is uniformly nondegenerate. It does not classify a hierarchy in which that weighted Gram itself becomes singular after successive rescaling, non-diagonal or indefinite coefficient geometries, growing asymptotic depth, or infinite-dimensional limits. Those are now the precise compact questions rather than generic “nonuniform weights.”

The clue therefore remains `accepted`, but its compact frontier is narrowed to hierarchical degeneration of successive rescaled **weighted** sampling/jet Grams, or a genuinely different coefficient topology, after occupancy, weights, center separation, and norm are accounted for. Growing order, scale escape, phase/window/infinite-dimensional resources, and genuinely new arithmetic source information remain separate exits.

## Research disposition

Outcome: **narrowed**.

Treat bounded source-independent conditioning, bounded source-adaptive selection, anchored fixed-depth scale growth, diffuse compact anchor loss, regular one-cluster collapse, regular separated multicluster occupancy, colliding-center clouds with a stable pooled outer Gram, and arbitrary positive diagonal weights with a stable weighted Gram as closed. Future compact-bank work must exhibit a genuinely hierarchical weighted degeneration that survives successive rescaling or leave the positive diagonal Hilbert setting; other continuations must expose growing order, scale escape, infinite/nonlinear structure, or a new signed source estimate that survives the unchanged Wang destination audit.