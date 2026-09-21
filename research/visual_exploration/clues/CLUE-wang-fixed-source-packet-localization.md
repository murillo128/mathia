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
  - research/visual_exploration/findings/VIS-364-nested-vandermonde-chain-cumulative-scale-spectrum.md
  - research/visual_exploration/findings/VIS-365-finite-weighted-vandermonde-subset-energy-spectrum.md
  - research/visual_exploration/findings/VIS-366-fixed-depth-vandermonde-partition-sum-spectrum.md
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The source side has already collapsed to the normalized Chebyshev-theta remainder

`G(u)=e^(-u)theta(e^u)-1`.

`VIS-333`--`VIS-340` show that Wang's prime and square-log summatory channels are exact transforms of the same source and that pointwise inversion repays one derivative. `VIS-341`--`VIS-353` price fixed smoothing/order, finite dilation and translation geometry, moving windows, phase entropy, confluent propagation, phase collisions, and separated finite cluster blocks. `VIS-354`--`VIS-361` reduce bounded compact positive coefficient geometry to truncated Vandermonde/moment conditioning. `VIS-362`--`VIS-365` then price weighted rank collapse, vanishing masses, nested scales, and arbitrary fixed finite positive branching with stable power valuations.

`VIS-366` removes the remaining fixed-depth positive compact support-count and valuation loopholes. For any positive probability measure `mu` on one compact normalized interval and fixed polynomial depth `q`, define

`Z_k(mu)=(1/k!) integral prod_(i<j)(x_j-x_i)^2 dmu^k`.

If `s_1>=...>=s_q` are the singular values of the degree-`q-1` polynomial sampling operator into `L^2(mu)`, then

`prod_(r<=k) s_r asymp_(q,K) sqrt(Z_k(mu))`

and

`s_k asymp_(q,K) sqrt(Z_k(mu)/Z_(k-1)(mu))`.

For discrete support, `Z_k` is the exact positive sum over all `k`-point weighted Vandermonde squares. This remains valid when support cardinality grows, when the support converges to a continuous positive measure, and when masses/separations have no common power-law valuation. `VIS-365` is the tropical hard-min specialization of this exact partition sum.

Thus **fixed cancellation depth plus positive compact Hilbert coefficient geometry is now closed as a standalone source-free escape, independent of support cardinality and power-law regularity**.

## Research question

After quotienting all fixed-depth positive compact polynomial-sampling geometry, can a genuinely growing-depth, source-coupled, different-topology, noncompact/global, or nonlinear construction produce a smaller Wang destination without merely importing a stronger estimate for `G`, `theta`, or an equivalent unsmoothed source quantity?

The live routes must now leave at least one hypothesis of `VIS-366`: cancellation depth `q` may grow; coefficient geometry may become signed, indefinite, non-diagonal, or otherwise non-positive-Hilbert; nodes, weights, or selectors may depend on signed arithmetic information from the source; normalized support may escape compactness together with a nontrivial destination repayment; or the mechanism may use global phase/window geometry, nonlinear source dependence, or a genuinely infinite-dimensional limit whose effective polynomial degree grows.

Merely adding more positive compact support points, allowing a continuous positive support, or replacing power scales by non-power scales at fixed `q` no longer qualifies as a distinct mechanism.

## Why it may matter

The Wang branch has progressively separated arithmetic information from conditioning geometry. `VIS-365` replaced finite branch trees by one tropical subset-energy ledger. `VIS-366` shows that even this valuation language is optional: at fixed depth the exact object is the positive Vandermonde partition family `Z_k`, whose constants are independent of support cardinality.

This makes the remaining frontier materially sharper. Any future positive result must either increase effective cancellation depth or introduce information/topology not present in a positive compact moment Gram. A destination improvement that is merely a small partition-sum ratio is conditioning, not evidence of stronger prime cancellation.

## Decisive test

For any proposed continuation, first state exactly which closed assumption is being abandoned.

If the effective polynomial/cancellation depth `q` is fixed, the coefficient geometry is positive Hilbert/diagonal after the existing normalization, and the normalized support lies in one fixed compact interval, form its positive coefficient measure `mu` and the partition sums

`Z_k(mu)=(1/k!) integral prod_(i<j)(x_j-x_i)^2 dmu^k`, `1<=k<=q`.

Apply `VIS-366`. Kill the route as source-free conditioning geometry if the claimed improvement is exactly the smallness of `sqrt(Z_k/Z_(k-1))` after restoring the outer Wang mass/scale factors. This test already permits growing discrete support, continuous support, non-power scales, and changing sets of near-minimizing support subsets.

If `q=q(parameter)` grows, account explicitly for the growing moment dimension, degree-sector constants, coefficient norm, truncation/order cost, and full Wang destination repayment. Fixed-depth comparison constants from `VIS-366` cannot simply be assumed uniform in `q`.

If coefficient geometry leaves the positive Hilbert setting, define its topology and norm precisely and identify which moment/Gram positivity step fails. If nodes, weights, scales, translations, or selectors use signed information from `G`, `theta`, or another arithmetic statistic, formulate the claimed gain directly as a source estimate and show that the selection rule does not already encode the desired stronger bound.

If support escapes the compact normalized regime, or the route uses phase/window growth, nonlinear dependence, or an infinite-dimensional representation, specify the growth parameter, convergence topology, truncation control, and full destination cost. Kill the route if the gain disappears once those costs are charged or if it reduces to a stronger source estimate assumed rather than proved.

## Evidence boundary

`VIS-333`--`VIS-365` are exact representation, obstruction, conditioning, interpolation, compactness, and finite-dimensional negative-control results. `VIS-366` adds a support-cardinality-independent exact partition-sum comparison for every positive compact coefficient measure at fixed polynomial depth, thereby covering growing and continuous support and arbitrary non-power compact geometry without a valuation assumption.

These findings do not prove a stronger PNT remainder, a new pointwise estimate for `G`, an RH-equivalent localization theorem, or a destination-level improvement. `VIS-366` also does not classify growing cancellation depth, signed/indefinite/non-diagonal coefficient geometries, source-dependent arithmetic selectors, noncompact/global phase-window escape, nonlinear dependence, or genuinely growing-dimensional limits.

The clue therefore remains `accepted`, but the entire fixed-depth positive compact moment-geometry branch is now closed as a standalone escape.

## Research disposition

Outcome: **narrowed**.

Treat any fixed-depth positive compact Wang bank — finite, growing-support, or continuous, with power or non-power scales — as source-free moment conditioning priced by `VIS-366`. Future work must exhibit growing effective depth, different coefficient topology, source-dependent signed arithmetic information, noncompact/global geometry with its costs repaid, nonlinear dependence, or another mechanism outside the fixed-degree positive moment-Gram category.
