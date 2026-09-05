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
---

# Does the prime/shift relative resolvent have the sharp Schatten threshold `S_r`, `r>1`?

## Observation

PF-112 fixes the unavoidable two-dimensional endpoint: the genuinely non-isometric prime/shift first relative resolvent is not trace class, while microlocal order remains compatible with `S_r` for every `r>1`. PF-125 proves global compact relative resolvent, but compactness does not determine the Schatten exponent. PF-126 supplies a global transported coefficient defect in every unweighted `L^r`, `r>1`, without a theorem converting that estimate directly into a relative-resolvent ideal bound.

The complete Margulis-short central sector is no longer the plausible obstruction. PF-171 proves that the direct sum of all fixed-central first-resolvent collar blocks has the sharp threshold

\[
\bigoplus_{\eta\in\mathcal S}A_\eta\in\mathcal S_r
\quad(r>1),
\qquad
\bigoplus_{\eta\in\mathcal S}A_\eta\notin\mathcal S_1.
\]

PF-173 then subtracts the matched prime/clone central-cut recoupling problems before taking norms and proves that the complete relative central recoupling correction is trace summable. The common angular zero mode that obstructs separate absolute gluing estimates cancels in the relative problem.

PF-174 closes the next analytic subgate. The Güneysu--Thalmaier heat/gradient multiplier estimates interpolate from weighted `L^2 -> S_2` and `L^infinity -> S_infinity` to

\[
L^q\!\left(\mu(B(\cdot,1))^{-1}d\mu\right)
\longrightarrow \mathcal S_q,
\qquad q\ge2.
\]

Because their metric comparison is factored through square-root deviation multipliers, weighted `delta^r` integrability gives the corresponding **heat-smoothed comparison product** in `S_r`. PF-174 also derives from PF-128 that every matched collapsing short collar satisfies the required weighted `L^r` estimate uniformly for all `r>=1`, and PF-138 makes those costs summable over the complete Margulis-short tail.

This is useful but deliberately not the desired theorem. The heat regularization removes high-frequency order and cannot be inverted by a bounded operation. Indeed the short-tail smoothed comparison already reaches `S_1`, while PF-112 proves the full first relative resolvent cannot. Therefore Schatten interpolation of the heat factors is solved; the remaining problem is the **body/interface input and the resolvent-level bridge**.

## Research question

For the common-manifold Laplacians associated with the PF-125 prime/shift marking, does

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

The negative endpoint is PF-112. The positive side now reduces to whether the **actual outer collar/body transmission, complementary body response, localization commutators, and repeated global interactions** preserve the `S_r`, `r>1`, scale when prime and clone are compared before norms are taken.

## Why it may matter

A positive answer would complete the natural operator-ideal classification between PF-112 and PF-125 and place the pair in the Hilbert--Schmidt regime relevant to regularized determinant and second-order spectral-shift machinery. It would still not be prime-specific: the exact all-composite shift clone shares the same classification.

A negative answer for some `r>1` would now identify a genuinely global amplification mechanism. Such an obstruction cannot be attributed merely to zero systole, the complete fixed-central short-collar family, the central transmission zero mode, or failure of Schatten interpolation for the heat factors; all of those channels have already been controlled by PF-171, PF-173, and PF-174.

## Decisive test

There are two surviving routes, and both must retain the actual complementary-body information.

The direct route is to cut prime and clone along the same outer collar/body interfaces, write compatible Krein/Schur-complement or Dirichlet-to-Neumann formulas for the **full** cut surfaces, and subtract source/clone formulas algebraically before taking Schatten norms. PF-173 shows why this order matters. The target estimate must include the complementary-body Dirichlet-to-Neumann maps and remain uniform through the complete zero-systole tail and repeated head-tail propagation.

The heat route should now start **after** PF-174 rather than repeating its interpolation. Derive weighted `L^r` metric deviation for the unresolved boundary-coherent body/interface comparison. If that succeeds, PF-174 places the heat-smoothed comparison operator in `S_r`. The remaining obligation is then an explicit common-Hilbert-space quadratic-form/resolvent factorization that transfers this information to the first relative resolvent without attempting to invert the heat semigroup. PF-112 is the endpoint control: any argument that also forces the full first resolvent into `S_1` has erased a real high-frequency obstruction.

A decisive negative resolution must produce a singular-value lower bound in one of the remaining body/interface/nonlocal channels. Concentration solely in the already-controlled fixed-central Margulis-short collars, the absolute zero-mode budget of one surface, or the heat-factor interpolation step is no longer sufficient.

## Evidence boundary

PF-171 concerns the Dirichlet-decoupled fixed-central collar direct sum. PF-173 concerns the matched **central-cut** recoupling family. Neither includes the complementary-body Dirichlet-to-Neumann response or restores the complete outer interfaces of the infinite flute.

PF-174 is a theorem about the weighted metric input and the **heat-smoothed** Schatten factorization. It is not a theorem about the first resolvent. PF-126 remains unweighted, while PF-130 gives strong unweighted `L^1` on independently compared Lambert bodies but does not control the inverse-unit-ball-volume weight under a globally boundary-coherent assembly.

Accordingly, neither the desired `S_r`, `r>1`, conclusion nor a counterexample for any `r>1` is established. The clue remains a research target rather than evidence.

## Research disposition

The clue remains `accepted`, now with the heat-factor interpolation subproblem closed by PF-174. Future work should not spend another cycle on central short-collar Schatten summation or on proving that the Güneysu--Thalmaier multiplier factors interpolate: those gates are settled.

The live frontier is **outer and body-loaded**. Either prove a common prime/shift outer-interface calculus whose relative transmission/body terms are `S_r` for every `r>1`, or establish the weighted body/interface hypotheses needed by PF-174 and then supply a valid resolvent-level bridge. The clue resolves only when the full uncut first relative resolvent is classified, or when a genuine global operator-level obstruction for some `r>1` is found.