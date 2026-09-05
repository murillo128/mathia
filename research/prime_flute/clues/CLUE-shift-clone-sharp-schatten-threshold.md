---
id: CLUE-prime-flute-shift-clone-sharp-schatten-threshold
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-112-first-relative-resolvent-is-not-trace-class.md
  - research/prime_flute/findings/PF-125-shift-clone-has-compact-relative-resolvent.md
  - research/prime_flute/findings/PF-126-shift-clone-metric-defect-is-Lp-above-one.md
  - research/prime_flute/findings/PF-130-lambert-shift-metric-defect-is-strong-L1-summable.md
  - research/prime_flute/findings/PF-171-all-margulis-short-central-first-resolvent-blocks-have-sharp-Sr-threshold.md
  - research/prime_flute/findings/PF-173-relative-central-recoupling-is-trace-summable.md
  - research/prime_flute/findings/PF-174-weighted-defect-controls-smoothed-schatten-scale.md
  - research/prime_flute/findings/PF-175-weighted-defect-gives-dual-resolvent-schatten-bridge.md
---

# Does the prime/shift relative resolvent have the sharp Schatten threshold `S_r`, `r>1`?

## Observation

PF-112 fixes the unavoidable two-dimensional endpoint for the standard density-unitary comparison: the genuinely non-isometric prime/shift first relative resolvent is not trace class, while microlocal order remains compatible with `S_r` for every `r>1`. PF-125 proves global compact relative resolvent, but compactness does not determine the Schatten exponent. PF-126 supplies a global transported coefficient defect in every unweighted `L^r`, `r>1`, without the inverse-unit-ball-volume control needed in the collapsing geometry.

The complete Margulis-short central sector is no longer the plausible obstruction. PF-171 proves that the direct sum of all fixed-central first-resolvent collar blocks has the sharp threshold

\[
\bigoplus_{\eta\in\mathcal S}A_\eta\in\mathcal S_r
\quad(r>1),
\qquad
\bigoplus_{\eta\in\mathcal S}A_\eta\notin\mathcal S_1.
\]

PF-173 then subtracts the matched prime/clone central-cut recoupling problems before taking norms and proves that the complete relative central recoupling correction is trace summable. The common angular zero mode that obstructs separate absolute gluing estimates cancels in the relative problem.

PF-174 closes the weighted heat-factor subgate. Güneysu--Thalmaier heat/gradient multiplier estimates turn weighted `delta^r` integrability into the corresponding heat-smoothed Schatten scale, and every matched collapsing short collar satisfies the required weighted estimate uniformly; PF-138 makes the complete Margulis-short family summable.

PF-175 now closes a genuine **first-resolvent** bridge, but under a form-natural dual-volume identification. If one coherent prime/shift marking satisfies the global weighted metric condition at exponent `r>1`, then

\[
(\Delta_{g_+}+1)^{-1}J^\vee
-
I(\Delta_g+1)^{-1}
\in\mathcal S_r,
\qquad
J^\vee=(I^{-1})^*.
\]

The same weighted input reaches the trivial and density-unitary identifications for `r>=2`. Thus the analytic bridge is no longer wholly open: the residual difficulty separates into **global weighted body/interface geometry** and, for the natural density-unitary comparison, the identification-sensitive strip `1<r<2`.

## Research question

For the common-manifold density-unitary Laplacians associated with a smooth globally coherent prime/shift marking, does

\[
A=(\Delta_{g_+}+1)^{-1}-(\Delta_g+1)^{-1}
\]

satisfy

\[
\boxed{
A\in\mathcal S_r\quad\text{for every }r>1,
\qquad
A\notin\mathcal S_1?
}
\]

The negative endpoint is PF-112. For the positive side, PF-175 shows that no further abstract resolvent unsmoothing theorem is needed once the perturbation can be expressed in the dual-volume form: weighted `delta^r` control already gives `S_r` for all `r>1`. What remains is to obtain that weighted control for the **actual outer collar/body transmission and globally boundary-coherent marking**, and then either transfer the dual result to the density-unitary identification in `1<r<2` or choose a marking for which the identifications coincide.

## Why it may matter

A positive answer would complete the natural operator-ideal classification between PF-112 and PF-125 and place the pair in every Schatten class strictly above the trace endpoint. It would still not be prime-specific: the exact all-composite shift clone shares the same classification.

A negative answer for some `r>1` would now identify a genuinely global amplification mechanism. Such an obstruction cannot be attributed merely to zero systole, the complete fixed-central short-collar family, the central transmission zero mode, failure of Schatten interpolation for the heat factors, or absence of a first-resolvent factorization; those channels are controlled by PF-171, PF-173, PF-174, and PF-175.

## Decisive test

The first obligation is geometric. Construct or obstruct one smooth complete quasi-isometric prime/shift marking, coherent across the PF-145 fixed interior collar interfaces and PF-139/PF-140 body/cusp handoffs, for which

\[
\int W_g\,\delta_{g,g_+}^{\,r}\,d\mu_g
+
\int W_{g_+}\,\delta_{g,g_+}^{\,r}\,d\mu_{g_+}
<\infty
\]

for the desired exponents. The already-controlled Margulis-short central collars must be removed from the uncertainty ledger rather than re-estimated. The live question is the actual outer interface trace, complementary body response, localization overlap, and repeated head-tail assembly.

If that weighted geometric gate succeeds, PF-175 immediately supplies the dual-volume `S_r` comparison for every `r>1` and the density-unitary comparison for `r>=2`. The remaining sharp test is then the strip `1<r<2`. One concrete route is to ask whether the boundary-compatible marking can be chosen area preserving, `rho=1`, without losing the weighted metric budget. In that case `J^\vee=I=U`, so PF-175 would give the standard density-unitary result for every `r>1`. This is only a proposed geometric route; existence of such a marked area-preserving comparison is not established.

A second route is an operator estimate for the one-sided density correction in `1<r<2` that uses more structure than the `S_2`-to-operator interpolation of PF-175. Any such argument must preserve PF-112's endpoint obstruction: a method that also forces the standard first resolvent into `S_1` has erased a real high-frequency contribution.

A decisive negative resolution must instead produce a singular-value lower bound in the unresolved body/interface/nonlocal channel, or show that every coherent marking necessarily violates the required weighted metric integrability. Concentration solely in the already-controlled central short collars or in the heat-factor step is no longer sufficient.

## Evidence boundary

PF-171 concerns the Dirichlet-decoupled fixed-central collar direct sum. PF-173 concerns the matched **central-cut** recoupling family. Neither includes the complementary-body Dirichlet-to-Neumann response or restores the complete outer interfaces of the infinite flute.

PF-174 proves the weighted short-collar input and heat-smoothed Schatten factorization, not the global body/interface estimate. PF-175 proves a conditional first-resolvent theorem from weighted metric deviation, but the strongest `r>1` statement uses `J^\vee=(I^{-1})^*`, not automatically the canonical density-unitary identification. PF-126 remains unweighted, while PF-130/PF-139 give strong unweighted body information without the complete inverse-unit-ball weighted assembly.

Accordingly, neither the desired density-unitary `S_r` conclusion for all `r>1` nor a counterexample for any `r>1` is established. The clue remains a research target rather than evidence.

## Research disposition

The clue remains `accepted`, with two previous analytic subproblems now removed. Future work should not spend another cycle on central short-collar Schatten summation, Güneysu--Thalmaier multiplier interpolation, or a generic attempt to invert heat smoothing. PF-175 supplies the resolvent bridge once weighted geometry is available in the dual-volume gauge.

The live frontier is now more precise: **close the global weighted outer/body/interface metric budget, then close the density-identification strip `1<r<2`**. The area-preserving-marking test is a particularly sharp geometric subquestion because it would make the dual, trivial, and density-unitary identifications coincide without inventing a new operator theorem. The clue resolves only when the full uncut density-unitary first relative resolvent is classified, or when a genuine global operator/geometric obstruction for some `r>1` is found.
