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
  - research/prime_lattice/findings/PL-178-prime-axis-single-average-shifted-prime-parity-boundary.md
  - research/prime_lattice/findings/PL-179-oriented-prime-axis-phase-closure-shifted-prime-data.md
---

# What source-forced affine statistic survives logarithmic two-point Haar flattening?

## Observation

The affine Liouville route has now separated several regimes sharply. Fixed-shift ordinary correlations retain the unresolved Chowla difficulty; canonical uniform shift averaging collapses or reduces to simpler summatory data; and `PL-174` shows that every fixed finite second-order logarithmic shift filter has the universal Haar spectrum. `PL-175` further shows that “higher-order or nonlinear” is not by itself an escape: all odd Walsh sectors vanish under logarithmic averaging, the degree-two sector vanishes, and every bounded observable of three distinct fixed Liouville translates has the complete independent-fair-sign joint law.

Thus the first fixed-shift Walsh sector not removed by the cited published correlation theorems is even degree four. This is only an information boundary: `PL-175` does not show that any fourth- or higher-even-order statistic has a non-Haar limit or carries RH-sensitive data.

`PL-176` removes the most canonical diffuse use of that boundary. If the degree-four parity is sampled on the additive parallelogram `(x,x+h,x+k,x+h+k)` and summed over all positive base points and both positive directions, its normalized average is unconditionally `o(1)`. The exact statistic is a Fourier fourth moment / additive `U^2` cube, so Davenport's uniform exponential-sum bound already flattens it. Modern higher-uniformity results show analogous Gowers flattening on average for all fixed cube orders in mesoscopic intervals, and do so for general nonpretentious bounded multiplicative functions. Therefore “go to degree four and average all directions” is not a surviving non-Haar mechanism.

`PL-177` removes a natural source-forced sparse repair at prime density. If the two directions come from multiplicative source elements `a,b` through the additive parallelogram `(n,an,bn,(a+b-1)n)`, complete multiplicativity collapses its parity exactly to `lambda(a)lambda(b)lambda(a+b-1)`. For any source family `A_X subset (X,2X]`, the complete double-source sum is a single Fourier integral and is bounded by `||sum_{m<=4X} lambda(m)e(m theta)||_infty |A_X|`. Davenport therefore makes the normalized statistic logarithmically flat for every polylogarithmically dense source family, including the primes. Source forcing and prime sparsity alone are consequently not enough if both source axes are still averaged independently and broadly.

`PL-178` classicalizes the most obvious one-axis repair. Freezing one prime source `r` in the same additive closure and averaging the other prime `q` gives pointwise `lambda(q+r-1)`, so the entire lattice/base geometry collapses to the classical fixed-shift Liouville-on-shifted-primes problem with `h=r-1`. Peer-reviewed theory proves cancellation after averaging over the shift but treats a prescribed fixed shift as the parity frontier. Thus “freeze one prime axis” is not by itself a new non-Haar mechanism; it merely trades the Fourier-flat double average for a classical hard scalar correlation.

`PL-179` now removes the bare total-exponent phase lift of that same one-axis closure. For any unitary completely multiplicative `f`, the oriented phase plaquette `f(n) overline{f(rn)} overline{f(qn)} f((r+q-1)n)` cancels the base point exactly. For the intrinsic exponent character `f_z(m)=z^Omega(m)`, with the same phase `z` on every prime direction, the residual is exactly `z^(Omega(q+r-1)-2)`. Thus replacing Liouville parity by the full one-parameter `Omega` phase does not retain a new lattice holonomy: it lands on the classical theory of multiplicative functions on shifted primes. Hildebrand and Timofeev already treat that setting, Khripunova gives a nontrivial fixed-shift cube-root phase estimate, and current dynamical work proves broad shift-averaged `Omega`-phase statements while leaving prescribed shifts distinct. A surviving “phase-conditioned” construction must therefore add a non-product/source/target ingredient before this oriented multiplicative cancellation, not merely change the character read out from total exponent parity.

## Research question

Is there a canonical prime-lattice operation that retains a non-Haar, source-forced affine invariant outside the theorem-controlled Walsh/Gowers/Fourier and shifted-prime-character sectors—through an even **fixed, genuinely thin, jointly constrained, or target-relative single-axis** source configuration of degree at least four, a phase-conditioned/non-product source family whose phase does not reduce as in `PL-179`, or a completed/target-relative coupling formed before the logarithmic or directional limit?

## Why it may matter

A survivor would identify arithmetic information that is genuinely present after additive coupling but not erased by the known logarithmic correlation, Gowers-uniformity, Davenport/Fourier flattening, shifted-prime parity reduction, or the canonical `Omega`-phase reduction. A negative result could close a broader family of affine spectral wrappers and redirect effort toward a different information carrier. `PL-175` removes all fixed three-shift nonlinear observables and every odd Walsh component; `PL-176` removes the canonical complete two-direction degree-four cube average; `PL-177` removes broad independently averaged prime-density source closure; `PL-178` shows that the raw fixed-one-prime-axis parity version is only the classical shifted-prime Liouville problem; and `PL-179` shows that the natural oriented total-exponent phase refinement is likewise only shifted-prime multiplicative data.

## Decisive test

Choose one concrete operation before inspecting its outcome and state exactly which theorem-controlled sector it leaves. For a fixed finite family of shifted Liouville parities, first expand the proposed readout in Walsh characters. If every nonconstant component has odd degree or degree two, reject it immediately by `PL-175`.

If a proposed even-degree statistic subsequently averages its shifts over a complete additive cube, test the resulting Gowers/Fourier moment before assigning it any spectral interpretation. The canonical two-direction degree-four average is already rejected by `PL-176`, and higher complete cube averages must be compared with the strongest available higher-uniformity theorem.

If the shifts are source-forced by multiplicative elements, test whether complete multiplicativity removes the base variable before interpreting the geometry. Any independent two-source construction equivalent to `(n,an,bn,(a+b-1)n)` with `|A_X| >= X/(log X)^K` is already rejected by `PL-177`. If one source is instead frozen at a fixed prime `r` and the other is broadly averaged over primes, `PL-178` shows that the canonical parity becomes exactly `lambda(q+r-1)`; treating that scalar as an unexplored lattice invariant is rejected by prior art unless an additional structure changes the problem before the collapse.

For a unitary phase refinement, apply the same reduction before assigning holonomy or spectral language. If the candidate is the oriented plaquette `f(n) overline{f(rn)} overline{f(qn)} f((r+q-1)n)`, `PL-179` gives the exact residual `overline{f(r)} overline{f(q)} f(r+q-1)`. In particular the canonical total-exponent family `f_z=z^Omega` becomes only `z^(Omega(q+r-1)-2)`. A new phase-conditioned candidate must therefore explain what non-product condition, prime-dependent source structure, target transport, or completion prevents reduction to an already-classical shifted-prime multiplicative mean. Merely varying `z`, or packaging the resulting fixed-shift characteristic function as a trace/holonomy/spectrum, does not pass.

A surviving fixed-shift logarithmic candidate must contain an even Walsh component of degree at least four and must supply an independently justified estimate or structural relation for that component; merely renaming an unresolved higher-even Chowla, shifted-prime parity, or shifted-prime phase correlation as a trace, determinant, or spectrum does not pass. For thin/growing/non-diffuse or completed candidates, keep the exact shift scale, weights, topology, completion, pair conditioning, phase assignment, and target transport explicit and compare with the strongest applicable correlation/uniformity theorem and a matched control.

## Evidence boundary

`PL-174` proves a second-order logarithmic obstruction, `PL-175` extends the theorem-controlled collapse to all odd Walsh sectors plus degree two, `PL-176` proves an ordinary-average obstruction for the complete additive-parallelogram degree-four carrier, `PL-177` proves a Davenport/Fourier obstruction for canonical source-forced two-axis closure at polylogarithmic density, `PL-178` classicalizes the fixed-one-prime-axis parity closure by reducing it exactly to Liouville on shifted primes, and `PL-179` classicalizes the canonical oriented total-exponent phase lift by reducing it exactly to `z^Omega` on the same shifted-prime sequence. None of these results proves full Bernoulli behavior, any fixed even-order Chowla case beyond degree two, cancellation for a prescribed shifted-prime Liouville sum, zero mean for every fixed shifted-prime `Omega` phase, absence of genuinely thin/jointly conditioned source families, or absence of useful completed couplings. No non-Haar survivor, analytic continuation, or RH implication is established here.

## Research disposition

Accepted for active investigation, narrowed again by `PL-179`. The fixed-shift nonlinear branch still begins, under the current theorem inputs, in even Walsh degree at least four, but degree four is only the first uncontrolled fixed-configuration case. Complete/diffuse additive-cube averaging is eliminated by `PL-176`; independently averaged prime-density source closure is Davenport-flat by `PL-177`; the raw canonical one-prime-axis freeze is not a new escape because `PL-178` identifies it with the classical fixed-shift shifted-prime Liouville problem; and the natural oriented `z^Omega` phase refinement is not a new holonomy because `PL-179` identifies it with the classical shifted-prime factor-count characteristic function. The live branches are now genuinely thin or jointly constrained/non-product source geometries, phase assignments whose residual coupling contains independently justified source information beyond a total-exponent character, single-axis observables that retain additional target/completion data before multiplicative collapse, and completed/target-relative couplings formed before flattening. Acceptance records only that these residual questions remain worth testing; it is not evidence for their truth, novelty, or RH relevance.