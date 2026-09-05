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
---

# What source-forced affine statistic survives logarithmic two-point Haar flattening?

## Observation

The affine Liouville route has now separated several regimes sharply. Fixed-shift ordinary correlations retain the unresolved Chowla difficulty; canonical uniform shift averaging collapses or reduces to simpler summatory data; and `PL-174` shows that every fixed finite second-order logarithmic shift filter has the universal Haar spectrum. `PL-175` further shows that “higher-order or nonlinear” is not by itself an escape: all odd Walsh sectors vanish under logarithmic averaging, the degree-two sector vanishes, and every bounded observable of three distinct fixed Liouville translates has the complete independent-fair-sign joint law.

Thus the first fixed-shift Walsh sector not removed by the cited published correlation theorems is even degree four. This is only an information boundary: `PL-175` does not show that any fourth- or higher-even-order statistic has a non-Haar limit or carries RH-sensitive data.

`PL-176` now removes the most canonical diffuse use of that boundary. If the degree-four parity is sampled on the additive parallelogram `(x,x+h,x+k,x+h+k)` and summed over all positive base points and both positive directions, its normalized average is unconditionally `o(1)`. The exact statistic is a Fourier fourth moment / additive `U^2` cube, so Davenport's uniform exponential-sum bound already flattens it. Modern higher-uniformity results show analogous Gowers flattening on average for all fixed cube orders in mesoscopic intervals, and do so for general nonpretentious bounded multiplicative functions. Therefore “go to degree four and average all directions” is not a surviving non-Haar mechanism.

## Research question

Is there a canonical prime-lattice operation that retains a non-Haar, source-forced affine invariant outside the theorem-controlled Walsh/Gowers sectors—through an even **fixed or sparse** shift component of degree at least four, a justified non-diffuse/growing shift family not dissolved by standard cube averaging, or a completed/target-relative coupling formed before the logarithmic or directional limit?

## Why it may matter

A survivor would identify arithmetic information that is genuinely present after additive coupling but not erased by the known logarithmic correlation and Gowers-uniformity theorems. A negative result could close a broader family of affine spectral wrappers and redirect effort toward a different information carrier. `PL-175` removes all fixed three-shift nonlinear observables and every odd Walsh component; `PL-176` additionally removes the canonical complete two-direction degree-four cube average.

## Decisive test

Choose one concrete operation before inspecting its outcome and state exactly which theorem-controlled sector it leaves. For a fixed finite family of shifted Liouville parities, first expand the proposed readout in Walsh characters. If every nonconstant component has odd degree or degree two, reject it immediately by `PL-175`.

If a proposed even-degree statistic subsequently averages its shifts over a complete additive cube, test the resulting Gowers/Fourier moment before assigning it any spectral interpretation. The canonical two-direction degree-four average is already rejected by `PL-176`, and higher complete cube averages must be compared with the strongest available higher-uniformity theorem.

A surviving fixed-shift logarithmic candidate must contain an even Walsh component of degree at least four and must supply an independently justified estimate or structural relation for that component; merely renaming an unresolved higher-even Chowla correlation as a trace, determinant, or spectrum does not pass. For sparse/growing/non-diffuse or completed candidates, keep the exact shift scale, weights, topology, completion, and target transport explicit and compare with the strongest applicable correlation/uniformity theorem and a matched control.

## Evidence boundary

`PL-174` proves a second-order logarithmic obstruction, `PL-175` extends the theorem-controlled collapse to all odd Walsh sectors plus degree two, and `PL-176` proves an ordinary-average obstruction for the complete additive-parallelogram degree-four carrier. None of these results proves full Bernoulli behavior, any fixed even-order Chowla case beyond degree two, absence of useful sparse or source-forced shift structure, or absence of useful completed couplings. In particular `PL-176` controls **averaged cube directions**, not a prescribed fixed four-point tuple. No non-Haar survivor, analytic continuation, or RH implication is established here. Ordinary fixed-shift Cesaro correlations remain a harder arithmetic problem rather than a solved escape.

## Research disposition

Accepted for active investigation, but narrowed again by `PL-176`. The fixed-shift nonlinear branch still begins, under the current theorem inputs, in even Walsh degree at least four, but degree four is only the first uncontrolled **fixed-configuration** case. Complete/diffuse additive-cube averaging is no longer a candidate: its canonical degree-four instance is Fourier/Gowers-flat, and standard higher cube averages face broad higher-uniformity controls. The live branches are now fixed or sparse source-forced even-degree configurations, independently justified non-diffuse/growing shift constructions outside those averaging theorems, and completed/target-relative couplings formed before flattening. Acceptance records only that these residual questions remain worth testing; it is not evidence for their truth, novelty, or RH relevance.