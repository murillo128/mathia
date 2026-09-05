---
id: CLUE-prime-lattice-affine-log-spectrum-nonhaar-escape
type: research-clue
status: accepted
origin: master-researcher
target_line: prime_lattice
based_on:
  - research/prime_lattice/findings/PL-172-hilbert-schmidt-affine-liouville-chowla-trace-removal.md
  - research/prime_lattice/findings/PL-173-affine-liouville-averaging-collapse.md
  - research/prime_lattice/findings/PL-174-logarithmic-affine-liouville-spectrum-is-haar-flat.md
  - research/prime_lattice/findings/PL-175-logarithmic-affine-liouville-walsh-collapse.md
  - research/prime_lattice/findings/PL-176-liouville-additive-cube-gowers-flattening.md
  - research/prime_lattice/findings/PL-177-prime-axis-affine-closure-flattening.md
---

# What source-forced affine statistic survives logarithmic two-point Haar flattening?

## Observation

The affine Liouville route has now separated several regimes sharply. Fixed-shift ordinary correlations retain the unresolved Chowla difficulty; canonical uniform shift averaging collapses or reduces to simpler summatory data; and `PL-174` shows that every fixed finite second-order logarithmic shift filter has the universal Haar spectrum. `PL-175` further shows that “higher-order or nonlinear” is not by itself an escape: all odd Walsh sectors vanish under logarithmic averaging, the degree-two sector vanishes, and every bounded observable of three distinct fixed Liouville translates has the complete independent-fair-sign joint law.

Thus the first fixed-shift Walsh sector not removed by the cited published correlation theorems is even degree four. This is only an information boundary: `PL-175` does not show that any fourth- or higher-even-order statistic has a non-Haar limit or carries RH-sensitive data.

`PL-176` removes the most canonical diffuse use of that boundary. If the degree-four parity is sampled on the additive parallelogram `(x,x+h,x+k,x+h+k)` and summed over all positive base points and both positive directions, its normalized average is unconditionally `o(1)`. The exact statistic is a Fourier fourth moment / additive `U^2` cube, so Davenport's uniform exponential-sum bound already flattens it. Modern higher-uniformity results show analogous Gowers flattening on average for all fixed cube orders in mesoscopic intervals, and do so for general nonpretentious bounded multiplicative functions. Therefore “go to degree four and average all directions” is not a surviving non-Haar mechanism.

`PL-177` now removes a natural source-forced sparse repair at prime density. If the two directions come from multiplicative source elements `a,b` through the additive parallelogram `(n,an,bn,(a+b-1)n)`, complete multiplicativity collapses its parity exactly to `lambda(a)lambda(b)lambda(a+b-1)`. For any source family `A_X subset (X,2X]`, the complete double-source sum is a single Fourier integral and is bounded by `||sum_{m<=4X} lambda(m)e(m theta)||_infty |A_X|`. Davenport therefore makes the normalized statistic logarithmically flat for every polylogarithmically dense source family, including the primes. Source forcing and prime sparsity alone are consequently not enough if both source axes are still averaged independently and broadly.

## Research question

Is there a canonical prime-lattice operation that retains a non-Haar, source-forced affine invariant outside the theorem-controlled Walsh/Gowers/Fourier sectors—through an even **fixed, single-axis, genuinely thin, or jointly constrained** source configuration of degree at least four, a phase-conditioned/non-product source family not dissolved by `PL-177`, or a completed/target-relative coupling formed before the logarithmic or directional limit?

## Why it may matter

A survivor would identify arithmetic information that is genuinely present after additive coupling but not erased by the known logarithmic correlation, Gowers-uniformity, and Davenport/Fourier flattening theorems. A negative result could close a broader family of affine spectral wrappers and redirect effort toward a different information carrier. `PL-175` removes all fixed three-shift nonlinear observables and every odd Walsh component; `PL-176` removes the canonical complete two-direction degree-four cube average; and `PL-177` shows that even source-forced directions at prime density collapse when both source axes are averaged independently through the canonical additive closure.

## Decisive test

Choose one concrete operation before inspecting its outcome and state exactly which theorem-controlled sector it leaves. For a fixed finite family of shifted Liouville parities, first expand the proposed readout in Walsh characters. If every nonconstant component has odd degree or degree two, reject it immediately by `PL-175`.

If a proposed even-degree statistic subsequently averages its shifts over a complete additive cube, test the resulting Gowers/Fourier moment before assigning it any spectral interpretation. The canonical two-direction degree-four average is already rejected by `PL-176`, and higher complete cube averages must be compared with the strongest available higher-uniformity theorem.

If the shifts are source-forced by multiplicative elements, test whether complete multiplicativity removes the base variable before interpreting the geometry. In particular, any independent two-source construction equivalent to `(n,an,bn,(a+b-1)n)` with `|A_X| >= X/(log X)^K` is already rejected by `PL-177`: after the exact parity reduction, Parseval and Davenport flatten the entire double-source average. A new source-forced candidate must therefore explain why it is fixed/single-axis, genuinely thinner than this density regime, jointly conditioned/non-product in the source variables, phase-conditioned, or otherwise not reducible to the same one-dimensional additive Fourier estimate.

A surviving fixed-shift logarithmic candidate must contain an even Walsh component of degree at least four and must supply an independently justified estimate or structural relation for that component; merely renaming an unresolved higher-even Chowla correlation as a trace, determinant, or spectrum does not pass. For thin/growing/non-diffuse or completed candidates, keep the exact shift scale, weights, topology, completion, pair conditioning, and target transport explicit and compare with the strongest applicable correlation/uniformity theorem and a matched control.

## Evidence boundary

`PL-174` proves a second-order logarithmic obstruction, `PL-175` extends the theorem-controlled collapse to all odd Walsh sectors plus degree two, `PL-176` proves an ordinary-average obstruction for the complete additive-parallelogram degree-four carrier, and `PL-177` proves a Davenport/Fourier obstruction for the canonical source-forced two-axis closure whenever the source family is polylogarithmically dense, in particular for primes. None of these results proves full Bernoulli behavior, any fixed even-order Chowla case beyond degree two, absence of useful fixed or single-axis source structure, absence of genuinely thin/jointly conditioned source families, or absence of useful completed couplings. In particular `PL-177` controls **independent broad averaging over both source axes**; it does not control a prescribed prime pair or a one-axis conditional statistic. No non-Haar survivor, analytic continuation, or RH implication is established here.

## Research disposition

Accepted for active investigation, but narrowed again by `PL-177`. The fixed-shift nonlinear branch still begins, under the current theorem inputs, in even Walsh degree at least four, but degree four is only the first uncontrolled **fixed-configuration** case. Complete/diffuse additive-cube averaging is no longer a candidate by `PL-176`, and prime-density source forcing does not rescue it when two multiplicative directions are independently averaged and additively closed: `PL-177` makes that family Davenport-flat. The live branches are now fixed or single-axis source-forced even-degree configurations, genuinely thinner or jointly constrained/phase-conditioned source geometries that evade the product Fourier reduction, and completed/target-relative couplings formed before flattening. Acceptance records only that these residual questions remain worth testing; it is not evidence for their truth, novelty, or RH relevance.