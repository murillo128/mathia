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
  - research/visual_exploration/findings/VIS-362-one-inner-scale-weighted-support-exponent.md
  - research/visual_exploration/findings/VIS-363-polynomial-mass-decay-hermite-order-statistic.md
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

`VIS-361` prices arbitrary **positive diagonal coefficient weights**. If `w_j>0`, `M=sum_j w_j`, and the coefficient norm is `sum |a_j|^2/w_j`, then the relevant matrix is `D_beta V W^(1/2)`. Whenever the normalized weighted moment Gram

`M^(-1) S^* W S`

has a positive degree-`q-1` eigenvalue floor,

`s_q(D_beta V W^(1/2)) asymp sqrt(M) rho^(q-1)`.

`VIS-362` prices the first genuinely degenerate weighted continuation. Suppose the outer normalized weighted cloud collapses onto exactly `L<q` separated atoms, every atom keeps a positive fraction of total mass, and one common finer scale `epsilon` exposes a uniformly nondegenerate local weighted polynomial cloud at each atom. Then, with

`h=floor((q-1)/L)`,

one has

`lambda_min(M^(-1)S^*WS) asymp epsilon^(2h)`

and therefore

`s_q(D_beta V W^(1/2)) asymp sqrt(M) rho^(q-1) epsilon^h`.

`VIS-363` removes the next apparent loophole: polynomially vanishing positive cluster masses. If

`M_ell/M asymp epsilon^(2a_ell)`

while the local weighted clouds stay uniformly nondegenerate at the same inner scale, assign cost `a_ell+d` to the `d`-th Hermite jet at center `ell`. If `tau_q` is the `q`-th smallest such cost, then

`lambda_min(M^(-1)S^*WS) asymp epsilon^(2 tau_q)`

and

`s_q(D_beta V W^(1/2)) asymp sqrt(M) rho^(q-1) epsilon^tau_q`.

Thus neither a singular outer weighted Gram nor polynomially disappearing positive support masses are by themselves new compact cancellation resources. One common inner scale is completely priced by a weighted Hermite filtration.

## Research question

After quotienting bounded source-independent banks, bounded source-adaptive selection, anchored bank enlargement, compact square-anchor loss, regular one-cluster occupancy repayment, regular separated multicluster Hermite-jet capacity, pooled colliding-center configurations, positive diagonal coefficient weights, one-scale weighted Gram collapse, and polynomially vanishing outer mass fractions, can a genuinely source-coupled or growing/global construction produce a smaller Wang destination without merely importing a stronger estimate for `G`, `theta`, or an equivalent unsmoothed source quantity?

The remaining live compact mechanisms must expose a resource outside that ledger: a **recursive weighted degeneration beyond one common Hermite scale** in which local normalized weighted Grams themselves lose rank/conditioning, distinct nested inner scales remain after the first rescaling, or the coefficient geometry leaves the positive diagonal Hilbert setting. Source-dependent coefficients carrying signed arithmetic information remain a separate route. Other exits remain growing tail depth/order, scale escape toward zero or infinity, growing/global phase complexity, shrinking windows, an infinite-dimensional topology, nonlinear source dependence, or direct signed arithmetic structure of `G`.

## Why it may matter

The compact fixed-depth branch is now close to a recursive multiscale classification. `VIS-358` prices one dense cluster; `VIS-359` prices regular separated clusters by local Hermite capacity; `VIS-360` pools colliding centers at their outer scale; `VIS-361` shows that positive nonuniform coefficient weights merely replace raw occupancy by a positive weighted moment measure; `VIS-362` prices a first outer rank collapse when all surviving support masses stay macroscopic; `VIS-363` shows that even polynomially vanishing positive masses are still just additive jet costs when one common inner rescaling keeps every local cloud healthy.

A positive compact-bank mechanism must therefore exhibit an actual **persistent multiscale loss**, not merely light clusters. Once mass decay and jet depth are combined into the cost spectrum `a_ell+d`, the first `q` costs already determine the full one-scale singular exponent. What remains is genuinely recursive geometry: another local Gram collapse, incompatible finer scales, a changed coefficient topology, or arithmetic/source information not present in the source-free bank geometry.

## Decisive test

For any proposed continuation, first state exactly which closed assumption is being abandoned.

If a source-dependent selector stays inside a fixed compact nondegenerate family, apply `VIS-355` before crediting any gain. Measure coefficients modulo the exact moment-cancellation kernel.

If the number of scales grows at fixed asymptotic depth while one uniformly conditioned `q`-column anchor survives, apply `VIS-356`: raw count growth is closed as an independent conditioning resource.

If every fixed-depth square anchor degenerates inside a compact interval, apply `VIS-357` to identify the shrinking-cluster geometry. For one regular cluster, apply `VIS-358` and charge the occupancy-width scale `N epsilon^(2(q-1))`.

For several regular clusters with fixed positive separated centers, apply `VIS-359`. In general choose Hermite multiplicities `m_ell` summing to `q`; a uniform lower bound follows whenever the deepest assigned jet masses `N_ell epsilon_ell^(2(m_ell-1))` stay bounded below. In the power-law regime compute `kappa_ell=floor(a_ell)+1`: total capacity at least `q` closes quotient degeneration, while total capacity below `q` produces the explicit source-free collapsing polynomial from `VIS-359`.

If the cluster centers themselves approach one another, do not treat pairwise separation as an additional escape parameter before pooling the cloud. Choose the outer diameter/scale `rho`, write every sample as `c+rho t_j`, and form the normalized degree-`q-1` sampling Gram. Apply `VIS-360`: if its smallest eigenvalue stays bounded below, the whole colliding configuration has quotient scale `sqrt(N) rho^(q-1)` and is closed.

If the coefficient space uses positive diagonal weights `w_j`, set `M=sum_j w_j` and form the normalized weighted Gram `M^(-1)S^*WS`. Apply `VIS-361`: if its smallest eigenvalue stays bounded below, the weighted quotient scale is `sqrt(M) rho^(q-1)` no matter how unequal the individual positive weights are.

If that weighted outer Gram degenerates because the normalized measure collapses onto `L<q` separated support points and each support point keeps a positive mass fraction, test the first inner scale before crediting a new mechanism. When one common inner rescaling has a uniformly nondegenerate local degree-`q-1` weighted moment Gram, apply `VIS-362`:

`s_q asymp sqrt(M) rho^(q-1) epsilon^floor((q-1)/L)`.

If some outer mass fractions also vanish polynomially at that same inner scale, write

`M_ell/M asymp epsilon^(2a_ell)`

and apply `VIS-363`. Form the finite jet-cost multiset

`{a_ell+d : 0<=d<=q-1}`

and let `tau_q` be its `q`-th smallest element. Then the full one-scale weighted quotient is already priced by

`s_q asymp sqrt(M) rho^(q-1) epsilon^tau_q`.

Continue inward only if the local weighted Grams themselves degenerate after this rescaling, distinct finer scales remain in the deficient modes, or no fixed common-scale valuation describes the relevant mass/local geometry. A claimed deeper hierarchy must identify the deficient polynomial subspace after the priced filtration and show that its next normalized Gram still loses a positive eigenvalue.

If the effective cancellation depth grows, combine `VIS-342`--`VIS-343` with the conditioning of the growing moment system. If downstream phase geometry also grows or degenerates, price its cluster count/multiplicity/span/density, separation, and window length through `VIS-344`--`VIS-353`.

If coefficients, scales, translations, weights, or selection rules use signed information from `G`, `theta`, or another arithmetic statistic, formulate the claimed gain directly as an arithmetic/source estimate. Show that the information used to choose the bank is not equivalent to assuming the desired stronger source bound, and propagate the estimate through Wang's full destination, including every `Q'` or equivalent inverse-derivative repayment.

For an infinite representation, specify the convergence topology, coefficient norm, truncation control, and finite approximants that preserve the claimed gain.

Kill a route if its improvement disappears after the explicit growth/degeneration parameter is charged, if adaptive weights merely approach the known moment kernel, if extra scales leave a stable anchor intact, if regular occupancy restores the full-map floor as in `VIS-358`--`VIS-359`, if pooled center collisions retain a stable normalized moment Gram as in `VIS-360`, if positive diagonal weights retain a stable normalized weighted moment Gram as in `VIS-361`, if a one-level outer weighted collapse is restored by the inner Hermite exponent in `VIS-362`, if polynomially vanishing positive masses are already priced by the weighted jet order statistic in `VIS-363`, if a changed norm or weighting is doing the real work but is not priced, if source-dependent weights encode the target source estimate, or if the gain is lost in the destination derivative step.

## Evidence boundary

`VIS-333`--`VIS-363` are exact representation, obstruction, conditioning, compactness, packing, Hermite-interpolation, pooled-rescaling, weighted-moment, and finite-dimensional negative-control results. They do not prove a stronger PNT remainder, a new pointwise estimate for `G`, an RH-equivalent localization theorem, or a destination-level improvement.

`VIS-363` handles one common inner scale with healthy local positive weighted clouds and cluster mass fractions comparable to fixed powers `epsilon^(2a_ell)`. It does not classify arbitrary recursive cluster trees, locally degenerate weighted measures, multiple incompatible inner scales, non-polynomial valuations requiring a different rescaling, non-diagonal or indefinite coefficient geometries, growing asymptotic depth, or infinite-dimensional limits.

The clue therefore remains `accepted`, but its compact frontier is narrowed to **recursive degeneration beyond a single weighted Hermite filtration**, or a genuinely different coefficient topology. Growing order, scale escape, phase/window/infinite-dimensional resources, and genuinely new arithmetic source information remain separate exits.

## Research disposition

Outcome: **narrowed**.

Treat bounded source-independent conditioning, bounded source-adaptive selection, anchored fixed-depth scale growth, diffuse compact anchor loss, regular one-cluster collapse, regular separated multicluster occupancy, colliding-center clouds with a stable pooled outer Gram, arbitrary positive diagonal weights with a stable weighted Gram, a one-level positive weighted outer collapse with healthy macroscopic inner clouds, and polynomially vanishing positive cluster masses on one common healthy inner scale as closed. Future compact-bank work must exhibit a recursive local Gram loss, genuinely distinct nested scales, a different coefficient topology, or arithmetic source information not already encoded by the source-free weighted Hermite filtration; other continuations must expose growing order, scale escape, infinite/nonlinear structure, or a new signed source estimate that survives the unchanged Wang destination audit.
