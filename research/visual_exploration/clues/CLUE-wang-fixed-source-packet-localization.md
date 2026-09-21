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
  - research/visual_exploration/findings/VIS-367-growing-depth-chebyshev-capacity-baseline.md
  - research/visual_exploration/findings/VIS-368-uniform-positive-hilbert-correlation-is-bounded-preconditioning.md
  - research/visual_exploration/findings/VIS-369-source-free-degenerate-positive-metric-prescribes-singular-spectrum.md
  - research/visual_exploration/findings/VIS-370-source-free-commuting-positive-metrics-are-spectral-filters.md
  - research/visual_exploration/findings/VIS-371-unitary-equivariant-gram-metrics-are-spectral.md
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

For discrete support, `Z_k` is the exact positive sum over all `k`-point weighted Vandermonde squares. This remains valid when support cardinality grows, when the support converges to a continuous positive measure, and when masses/separations have no common power-law valuation.

`VIS-367` identifies the first generic growing-depth effect. For every positive probability measure on `[-1,1]`,

`Z_q(mu) <= 2^(-(q-1)(q-2))`

and the raw monomial sampling map satisfies

`s_q(q) <= 2^(2-q)`.

These bounds come from the classical Chebyshev minimax polynomial and are completely source-free. Thus even before arithmetic information enters, growing polynomial depth creates a super-exponentially shrinking determinant scale and an exponentially small raw monomial singular direction.

`VIS-368` closes bounded positive coefficient correlation. If an already priced diagonal covariance `W` and a positive-definite correlated covariance `H` satisfy

`mW <= H <= MW`,

then every corresponding Wang singular value changes by at most the fixed factors `sqrt(m)` and `sqrt(M)`. Uniform positive off-diagonal correlation is therefore only bounded preconditioning.

`VIS-369` closes the opposite unconstrained loophole. If a positive metric may degenerate freely and align with the right-singular basis of the already priced source-free Wang map `A_W`, then any desired positive active singular spectrum can be prescribed, with the relative metric eigenvalues paying exactly the square of the imposed singular-value factors.

`VIS-370` closes source-free metrics already known to commute with the Wang Gram `G_W=A_W^*A_W`: they act only by sectorwise weights, and every explicit spectral rule `C=f(G_W)` is deterministic filtering of the baseline singular spectrum.

`VIS-371` removes the remaining “canonical but perhaps noncommuting” wording loophole for rules built from the Gram alone. If a positive metric rule `F` uses only `G_W` and respects unitary changes of coefficient coordinates,

`F(U G_W U^*) = U F(G_W) U^*`,

then stabilizer equivariance forces

`F(G_W)=sum_lambda c_lambda P_lambda`.

So the output commutes with `G_W` automatically and is a spectral filter for that fixed Gram, even when the weights depend on the complete spectrum and the rule is not written as a simple one-variable formula. A noncommuting metric therefore certifies the presence of additional structure beyond the Gram alone: preferred coordinates, packet labels/nodes, another physical operator, boundary data, or arithmetic source information.

So **fixed depth is closed by the partition-sum audit, growing depth must first quotient the universal Chebyshev/capacity baseline, bounded positive correlations are only preconditioning, arbitrary free degeneration is non-identifying, and every coordinate-free positive metric derived solely from the source-free Gram is spectral filtering**.

## Research question

After quotienting fixed-depth positive compact polynomial-sampling geometry, the universal source-free high-degree Chebyshev/capacity collapse, uniformly equivalent positive coefficient metrics, freely engineered metric degeneration, and all unitary-equivariant positive metric rules whose only matrix input is the baseline Wang Gram, can a genuinely external physical topology, arithmetic source-dependent metric, indefinite/non-Hilbert structure, noncompact/global mechanism, nonlinear source coupling, or controlled infinite-dimensional limit produce a smaller Wang destination without merely importing a stronger estimate for `G`, `theta`, or an equivalent unsmoothed source quantity?

The positive-metric route is now more specific. A proposed noncommuting metric must identify the **extra non-Gram structure** that fixes its orientation. If that structure is freely selectable, `VIS-369` makes the diagnostic non-identifying. If it is arithmetic source data, the rule must be charged as part of the source estimate. If it is genuinely physical/external geometry, its norm and destination cost must be propagated explicitly.

## Why it may matter

The Wang branch has progressively separated arithmetic information from representation and conditioning geometry. `VIS-366` prices all fixed-depth positive compact coefficient measures, `VIS-367` identifies the universal growing-depth capacity collapse, `VIS-368` removes bounded positive correlation, `VIS-369` removes arbitrary free metric degeneration, `VIS-370` classifies commuting and spectral-functional metrics, and `VIS-371` shows that coordinate-free dependence on the Gram alone cannot even generate a noncommuting escape.

This sharpens the remaining frontier materially. A tiny singular value, dramatic condition-number change, correlated/degenerating positive norm, whitening, regularized spectral flattening, or invariant optimization over the baseline Gram is not enough. A future positive result must expose the additional information or geometry that is absent from the source-free Gram and show a net destination gain after its full cost is charged.

## Decisive test

For any proposed continuation, first state exactly which closed assumption is being abandoned or which source-free baseline is claimed to be beaten.

If the effective polynomial/cancellation depth `q` is fixed, the coefficient geometry is positive Hilbert after normalization, and the normalized support lies in one fixed compact interval, apply `VIS-366` to the underlying positive polynomial-sampling geometry. For a non-diagonal positive covariance `H`, choose the physically natural priced baseline `W` and form

`C=W^(-1/2) H W^(-1/2)`.

If the spectrum of `C` stays in one fixed interval `[m,M] subset (0,infinity)`, apply `VIS-368` and kill the supposed metric gain as bounded preconditioning.

If `C` degenerates and is claimed to be a canonical or coordinate-free construction from `G_W=A_W^*A_W` alone, test the rule under unitary conjugation. If it is equivariant, apply `VIS-371`: `C` must be scalar on every Gram eigenspace and hence commute with `G_W`. Then apply `VIS-370` and charge the sector weights explicitly. A rule based on global spectral statistics does not escape this gate merely because its weight at one eigenvalue depends on all the other eigenvalues.

If a proposed `C` does not commute with `G_W`, identify the additional input that breaks Gram-only equivariance. Preferred coordinates, packet/node labels, another operator, external physical topology, boundary data, or source-dependent arithmetic information are all real extra resources and must be stated rather than hidden inside the metric constructor. If the resulting orientation remains freely adjustable against the baseline singular vectors, apply `VIS-369` and kill the gain as engineered preconditioning.

If `q=q(parameter)` grows, first affine-normalize the compact node coordinate and identify the actual coefficient norm used by the Wang destination. Apply `VIS-367` to quotient the universal compact Chebyshev/capacity collapse. Then apply `VIS-368`--`VIS-371` to the positive metric dimension by dimension, include any basis-change cost needed to return to physical Wang coefficients, and combine any residual gain with `VIS-342`, which requires polynomial growth of effective scalar order for a fixed Vinogradov--Korobov power-class improvement.

If coefficient geometry is genuinely indefinite/non-Hilbert, define its topology and destination norm precisely and identify exactly which positive-Hilbert step fails. If nodes, weights, scales, translations, metric, selectors, or extra operators use signed information from `G`, `theta`, or another arithmetic statistic, formulate the claimed gain directly as a source estimate and show that the selection rule does not already encode the desired stronger bound.

If support escapes the compact normalized regime, or the route uses global phase/window growth, nonlinear dependence, or an infinite-dimensional representation, specify the growth parameter, convergence topology, truncation control, coefficient normalization, and full destination cost. Kill the route if the gain disappears once those costs are charged or if it reduces to a stronger source estimate assumed rather than proved.

## Evidence boundary

`VIS-333`--`VIS-365` are exact representation, obstruction, conditioning, interpolation, compactness, and finite-dimensional negative-control results. `VIS-366` gives a support-cardinality-independent exact partition-sum comparison for every positive compact coefficient measure at fixed polynomial depth. `VIS-367` gives the universal growing-depth Chebyshev/capacity baseline. `VIS-368` shows that uniformly equivalent positive non-diagonal Hilbert metrics preserve singular-value scales up to bounded factors. `VIS-369` shows that unrestricted source-free degenerating metrics can prescribe the active singular spectrum. `VIS-370` classifies positive metrics commuting with the baseline Gram as sectorwise spectral filters. `VIS-371` adds the exact stabilizer-equivariance result that any unitary-equivariant positive metric rule built from that Gram alone is automatically of this commuting spectral form.

These findings do not prove a stronger PNT remainder, a new pointwise estimate for `G`, an RH-equivalent localization theorem, or a destination-level improvement. `VIS-371` does not say that every physically meaningful metric must be a spectral function of the Wang Gram. It says that **Gram-only + coordinate-free/unitary-equivariant** metric construction forces that form. A noncommuting metric may still be meaningful when another independently justified structure fixes it. Indefinite/non-Hilbert coefficient spaces, noncompact/global phase-window escape, nonlinear dependence, source-dependent selectors, and genuinely different infinite-dimensional topologies remain outside these closures.

The clue therefore remains `accepted`, but positive-Hilbert metric design based only on invariant processing of the source-free Gram is now closed as a standalone explanation of arithmetic gain.

## Research disposition

Outcome: **narrowed**.

Treat fixed-depth positive compact Wang banks through `VIS-366`, growing raw polynomial depth through `VIS-367`, uniformly comparable metrics through `VIS-368`, freely oriented degeneration through `VIS-369`, commuting/spectral metrics through `VIS-370`, and any coordinate-free Gram-only metric constructor through `VIS-371`. Future positive-metric work must identify and price the extra non-Gram structure that fixes a genuinely new orientation or topology. Otherwise move to a different mechanism class: source-dependent arithmetic information, indefinite/non-Hilbert geometry, noncompact/global structure, nonlinear dependence, or a controlled infinite-dimensional limit.