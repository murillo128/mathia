# VIS-119 — wrapping an unfolded zero block does not inherit the Haar-CUE trace-bispectrum null

## Claim

Let `x_1,...,x_M` be a finite block of unfolded points contained in an interval `[A,A+L]`. A natural way to turn that block into circular Fourier coordinates is

`P_m(A,L) = sum_(j=1)^M exp(2 pi i m (x_j-A)/L)`

for positive integers `m`, and then to form the frequency-conserving third-order triad

`B_(a,b)^(block) = P_a P_b overline(P_(a+b))`.

This construction has the same formal frequency pattern as the Haar-CUE trace triad in `VIS-118`, but **the exact Haar-CUE centered null does not follow from circular wrapping, unfolding, or uniform one-point phase density**.

The distinction is exact. For `M` independent uniform phases `theta_1,...,theta_M` on the unit circle, define

`p_m = sum_(j=1)^M exp(i m theta_j)`.

Then for every positive `a,b`,

`E[p_a p_b overline(p_(a+b))] = M`.

By contrast, `VIS-118` records the classical Haar-CUE identity

`E_CUE[Tr(U^a) Tr(U^b) overline(Tr(U^(a+b)))] = 0`

whenever `a+b<=N`.

Thus two circular point ensembles can have the same uniform one-point angular marginal and radically different third-order trace means. The CUE zero in `VIS-118` comes from joint Haar power-sum/partition orthogonality, not from angular uniformity or the frequency sum `a+b-(a+b)=0`.

Consequently, a zeta-side test based on a finite unfolded zero block may use the `VIS-118` normalization only after a **source-dictionary gate** is supplied. One must either apply the same finite-window/unfolding/compactification statistic to a matched CUE ensemble, or derive the block triad's null directly from correlation information strong enough to control that finite-window functional. Simply wrapping the zero block onto a circle and importing the full-matrix Haar trace null is not source-faithful.

**Evidence/status:** `EXACT-DERIVED + NEGATIVE/CONTROL + SOURCE-DICTIONARY BOUNDARY + NO-NOVELTY-CLAIM`.

No claim is made that zeta zeros fail a CUE comparison, that the wrapped block triad has nonzero limiting mean, or that a suitable matched CUE block statistic cannot be centered. The result only rules out one unjustified transfer of the exact `VIS-118` null.

## 1. The wrapped block triad is rotation invariant but window dependent

Changing the angular origin by a constant `delta` multiplies

`P_m -> exp(-2 pi i m delta/L) P_m`.

Therefore

`P_a P_b overline(P_(a+b))`

is unchanged because the total frequency is

`a+b-(a+b)=0`.

So the proposed block triad correctly removes an arbitrary common circular phase origin. This is useful, but it does not remove the finite-window construction itself. The selected point set, interval length `L`, endpoint convention, unfolding map, and any taper or hard cutoff remain part of the observable.

In particular, the block statistic is a Fourier functional of a finite selected point process. It is not, merely by notation, the trace of powers of an entire Haar-distributed `N x N` unitary matrix.

This distinction matters because `VIS-118` already noted that rotational symmetry alone cannot explain its zero mean: the CUE triad is itself rotation invariant. Its exact centering is instead a consequence of the Diaconis-Shahshahani/Diaconis-Evans joint trace-moment formula.

## 2. Uniform circular phases give an exact nonzero counter-control

Take independent phases

`theta_j ~ Uniform[0,2 pi)`

and write

`p_m = sum_j exp(i m theta_j)`.

Expanding the triad gives

`p_a p_b overline(p_(a+b))`
` = sum_(i,j,k) exp(i[a theta_i + b theta_j - (a+b) theta_k])`.

Because the phases are independent and uniform, the expectation of a summand vanishes unless the total coefficient of every individual phase is zero.

For positive `a,b`, the only surviving index pattern is

`i=j=k`.

Indeed:

- if `i,j,k` are distinct, each phase carries a nonzero coefficient;
- if `i=k != j`, the two surviving coefficients are `-b` and `b`;
- if `j=k != i`, they are `a` and `-a`;
- if `i=j != k`, they are `a+b` and `-(a+b)`.

All of those factor into at least one nonzero Fourier moment of a uniform phase and therefore vanish. When `i=j=k`, the exponent is identically zero. There are exactly `M` such terms, so

`E[p_a p_b overline(p_(a+b))] = M`.

The same conclusion holds conditionally on the count for a circular Poisson point process: given `M`, the triad mean is `M`.

This is an exact falsification control for the proposed dictionary. A circular representation plus uniform one-point density is insufficient to produce the Haar-CUE null.

## 3. What CUE contributes that wrapping does not

For Haar `U(N)`, the eigenangle one-point marginal is uniform, but the eigenangles are strongly correlated. The exact low-degree formula used in `VIS-118` is a statement about joint power-sum moments under Haar measure.

For the CUE triad

`B_(a,b)=p_a p_b overline(p_(a+b))`,

the positive trace partition is `(a,b)` while the negative partition is `(a+b)`. The classical Haar trace-moment formula makes these distinct partitions orthogonal whenever the weighted degree fits inside the finite-`N` corridor. That is why the mean is zero.

The independent-uniform counter-control has the same circular support and the same uniform one-point marginal, but lacks the Haar joint eigenangle law; its third-order mean is `M` instead. Hence the load-bearing information in `VIS-118` is genuinely higher-order ensemble structure.

A visual comparison that first maps both sources onto the unit circle can therefore erase the very distinction that determines the null unless the complete sampling/window rule is included in the source model.

## 4. Local zeta/CUE correspondence does not by itself supply this global trace identity

The current visual source corpus already records substantial finite-height zeta/CUE prior art. Forrester-Mays, Bornemann-Forrester-Mays, and Nishigaki treat finite-size CUE corrections for spacing observables and comparison with high Riemann zeros. Bogomolny-Keating treats finite-height higher correlation structure, including arithmetic corrections to the random-matrix limit.

Those source anchors justify CUE as a serious comparison model for appropriately matched zero statistics. They do **not**, as used anywhere in the current Mathia corpus, provide a theorem identifying a hard-windowed, unfolded, rewrapped finite zero block with the global trace vector of a full Haar unitary matrix.

That missing implication is not a technicality. A finite block statistic depends on window membership and compactification, while the Diaconis-Shahshahani/Diaconis-Evans identity in `VIS-118` is an exact full-ensemble Haar moment statement. Passing from local or finite-height correlation agreement to a growing-frequency Fourier triad requires its own limit theorem or a matched finite-ensemble construction.

Accordingly, no appeal to generic "CUE universality" should be used to insert the exact `VIS-118` mean and covariance into a zeta block analysis without proving that the chosen observable lies inside a justified transfer regime.

## 5. Source-faithful protocol consequence

There are two clean ways forward.

The first is empirical but source-faithful: predeclare the zeta block construction — height windows, unfolding, count/length convention, circular map, taper if any, and frequency panel — and apply **the identical transformation** to finite CUE eigenangle data under a predeclared effective matrix-size rule. The resulting CUE block statistic, not the full-matrix trace formula by itself, is then the null object. Any centering, covariance, or finite-size correction can be estimated or derived for that exact transformed ensemble.

The second is analytic: derive the expectation and covariance of the finite-window triad from the relevant CUE or sine-process correlation functions, with all boundary/window terms kept, and prove a regime in which they reduce to the simpler `VIS-118` calibration. A zeta transfer would then need the corresponding correlation control at the required scale.

Either route preserves the useful insight of `VIS-118`: third-order frequency-conserving panels offer a clean global higher-order channel. What is rejected is only the shortcut that identifies a wrapped finite source block with a Haar trace vector without accounting for the selection map.

## 6. Prior art and novelty assessment

The Haar side is classical and already sourced in `VIS-118`: Persi Diaconis and Mehrdad Shahshahani, **On the eigenvalues of random matrices**, *Journal of Applied Probability* 31A (1994), 49-62, DOI `10.1017/S0021900200106989`, and Persi Diaconis and Steven N. Evans, **Linear functionals of eigenvalues of random matrices**, *Transactions of the American Mathematical Society* 353:7 (2001), 2615-2633, DOI `10.1090/S0002-9947-01-02800-8`.

The distinction between independent uniform circular points and CUE eigenangles is standard random-matrix background. The calculation `E[p_a p_b overline(p_(a+b))]=M` is included here because it is the minimal exact counterexample needed for the current source dictionary; no general point-process or bispectral novelty is claimed.

For the zeta/CUE boundary, the canonical source anchors already recorded in `research/visual_exploration/SOURCES.md` include Peter J. Forrester and Anthony Mays, **Finite-size corrections in random matrix theory and Odlyzko's dataset for the Riemann zeros**, *Proceedings of the Royal Society A* 471 (2015), 20150436, DOI `10.1098/rspa.2015.0436`, and E. Bogomolny and J. P. Keating, **A method for calculating spectral statistics based on random-matrix universality with an application to the three-point correlations of the Riemann zeros**, *Journal of Physics A* 46 (2013), 305203, DOI `10.1088/1751-8113/46/30/305203`.

A targeted prior-art check found no reason to claim the counter-control or source-dictionary warning as a new theorem. Its value is operational: it prevents a mathematically false null transfer immediately before the visual line begins any zeta-side inspection of the `VIS-118` channel.

## Boundary and falsification

The exact independent-phase identity assumes independent uniform phases and fixed positive integer frequencies. It is used only as a counterexample showing that uniform one-point circular density does not imply the Haar-CUE trace null. It is not proposed as a realistic model for zeta zeros.

The finding would be falsified if the displayed independent-phase expectation were wrong, or if the exact Haar-CUE centering in the `VIS-118` corridor followed from one-point uniformity alone. The explicit expansion above rules out both possibilities.

A future theorem may show that a particular zeta block compactification converges, after explicit centering and scaling, to the same triad law as an appropriate CUE block or even to the `VIS-118` full-trace null. Such a theorem would refine this boundary, not contradict it: the required bridge would then have been supplied rather than assumed.

## Visual consequence

No canonical PNG is retained. A circular scatterplot of an unfolded zero block and a CUE spectrum can make the two sources look comparably uniform while concealing the higher-order dependence that changes the triad mean from `M` to `0` in the exact counter-control above.

Therefore uniform angular appearance is specifically an unsafe visual validation for the `VIS-118` source dictionary. Any later visualization of the third-order panel should show the statistic under the exact matched source transformation, not merely the wrapped point clouds.

## Research consequence

`VIS-118` supplied an exact low-degree Haar-CUE third-order null and deliberately left the zeta-side dictionary for a later invocation. This finding resolves the first dictionary question negatively: **naive finite-block circularization is not enough to inherit that null**.

The next distinct research question is now narrower. Before any zeta data are inspected, define a predeclared block observable together with its matched finite-CUE transformation or prove an analytic window-to-trace bridge. Choosing that protocol is a separate thread and is intentionally left for a later invocation.