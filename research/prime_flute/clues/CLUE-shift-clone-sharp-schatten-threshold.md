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
  - research/prime_flute/findings/PF-176-boundary-moser-removes-only-the-volume-gauge-obstruction.md
  - research/prime_flute/findings/PF-177-collar-jacobian-defect-can-be-expelled-from-collapsing-core.md
---

# Does the prime/shift relative resolvent have the sharp Schatten threshold `S_r`, `r>1`?

## Observation

PF-112 fixes the two-dimensional endpoint for the standard density-unitary comparison: the genuinely non-isometric prime/shift first relative resolvent is not trace class, while microlocal order remains compatible with `S_r` for every `r>1`. PF-125 proves global compact relative resolvent, but compactness does not determine the Schatten exponent.

The complete Margulis-short central sector is no longer the plausible obstruction. PF-171 proves the sharp `S_r`, `r>1`, threshold for the direct sum of all fixed-central first-resolvent collar blocks, and PF-173 shows that the matched prime/clone central-cut recoupling correction is trace summable. PF-174 then proves the full inverse-unit-ball weighted `delta^r` scale on those collapsing collars and the corresponding heat-smoothed Schatten factorization.

PF-175 closes the first-resolvent analytic bridge under a form-natural dual-volume identification. If one coherent prime/shift marking satisfies the global weighted metric condition at exponent `r>1`, then

\[
(\Delta_{g_+}+1)^{-1}J^\vee
-I(\Delta_g+1)^{-1}
\in\mathcal S_r,
\qquad
J^\vee=(I^{-1})^*.
\]

The same input reaches the trivial and density-unitary identifications for `r>=2`. Thus the residual analytic strip `1<r<2` is identification-sensitive rather than a missing generic resolvent-unsmoothing theorem.

PF-176 shows that on every compactly truncated matched one-cusp pant, equal area plus boundary Moser removes the *qualitative* obstruction to an area-preserving marking with the prescribed boundary values. PF-177 now removes the dangerous local quantitative interpretation of that problem: every matched collapsing short collar admits a boundary-to-boundary gauge with `rho=1` exactly throughout the whole potentially collapsing area-coordinate core, while all unavoidable Jacobian defect is pushed into a uniformly thick outer rim with weighted `L^r` size `O(|t|^rL^{2r})`. Across the complete PF-138 short-collar family those thick-rim density budgets are summable.

There is, however, an exact conservation coupling. Full source and target standard collars have areas `2A(L)` and `2A(L')`, with `A(L)=L/sinh(L/2)`, so an independently area-preserving boundary-to-boundary map of each full standard collar is impossible when `L!=L'`. The remaining volume-gauge problem is therefore **global thick-region redistribution and smooth assembly**, not prescribed-Jacobian control inside the collapsed cores.

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

The negative endpoint is PF-112. For the positive side, PF-175 shows that weighted `delta^r` control already yields `S_r` for every `r>1` in the dual-volume gauge. The primary live route is now to assemble one **globally area-preserving** prime/shift comparison that retains the required weighted metric budget. PF-177 permits every collapsing collar core to be frozen with `rho=1`; only its summable `O(|t|L^2)` area imbalance has to be exchanged through the uniformly thick collar rims/body.

If that geometric route fails, the parallel operator question remains whether the one-sided density-identification correction can be controlled directly in `S_r` for `1<r<2` without imposing `rho=1`.

## Why it may matter

A positive answer would complete the natural operator-ideal classification between PF-112 and PF-125 and place the pair in every Schatten class strictly above the trace endpoint. It would still be a negative arithmetic control: the exact all-composite shift clone would share the same classification, so the ideal class itself could not certify primality or RH.

A negative answer for some `r>1` would now identify a genuinely global amplification mechanism. Such an obstruction cannot be attributed merely to zero systole, the complete fixed-central short-collar family, central transmission zero modes, the heat-factor Schatten step, absence of a first-resolvent factorization, qualitative nonexistence of an area-preserving pant marking, or the need to solve a Jacobian equation inside collapsed collar cores. Those channels are controlled by PF-171, PF-173, PF-174, PF-175, PF-176, and PF-177.

## Decisive test

The main geometric test should freeze the already-solved thin geometry rather than reopen it. On every PF-138 matched short collar use the PF-177 gauge, so the volume ratio is exactly one on `|x|<=1` and all density forcing lies in the uniformly thick rim. Combine those collar pieces with the PF-139/PF-140 body/cusp comparison and PF-145 fixed interior interfaces.

Then construct, or obstruct, one smooth complete quasi-isometric correction on the **thick complementary assembly** such that:

1. the local collar/body/cusp maps have compatible boundary jets or common fixed-collar models and glue to one smooth global marking;
2. the signed `O(|t_eta|L_eta^2)` collar-area mismatches are redistributed through the thick rims/body so that the final volume ratio satisfies `rho=1` globally;
3. the correction remains uniformly near-isometric on the tail and preserves, for every desired `r>1`,
   \[
   \int W_g\,\delta_{g,g_+}^{\,r}\,d\mu_g
   +
   \int W_{g_+}\,\delta_{g,g_+}^{\,r}\,d\mu_{g_+}
   <\infty.
   \]

Support-controlled Dacorogna--Moser technology is relevant only after the forcing has been placed in this uniformly thick region; it is not a substitute for proving uniform quantitative bounds and coherent infinite assembly. A successful `rho=1` construction makes `J^\vee=I=U`, so PF-175 immediately gives the canonical density-unitary `S_r` conclusion for every `r>1`.

The alternative operator route is to prove directly that the one-sided density correction in PF-175 belongs to `S_r` for `1<r<2` using structure beyond the `S_2`-to-operator interpolation currently available. Any such argument must preserve PF-112's endpoint obstruction: a method that also forces the standard first resolvent into `S_1` has erased a real high-frequency contribution.

A decisive negative resolution must produce a singular-value lower bound in the unresolved body/interface/nonlocal channel, prove that every globally coherent thick-region volume redistribution necessarily violates the weighted metric budget, or otherwise show that the `1<r<2` density-unitary transfer fails intrinsically. Concentration solely in the already-controlled short-collar cores is no longer sufficient.

## Evidence boundary

PF-171 concerns the Dirichlet-decoupled fixed-central collar direct sum, and PF-173 concerns the matched central-cut recoupling family. Neither includes the complementary-body Dirichlet-to-Neumann response or complete outer interfaces of the infinite flute.

PF-174 supplies the weighted short-collar input and heat-smoothed Schatten factorization. PF-175 supplies a conditional first-resolvent theorem from weighted metric deviation, but its strongest `r>1` statement uses the dual-volume identification rather than automatically the canonical density-unitary map. PF-126 remains unweighted, while PF-130/PF-139 give strong unweighted body information without the complete inverse-unit-ball weighted assembly.

PF-176 is qualitative pant-local Moser theory. PF-177 is an exact collar gauge: it removes Jacobian forcing from the collapsing core and proves summable thick-rim density budgets, but it also proves that unequal full standard-collar areas prevent an independent collarwise `rho=1` solution. It does **not** construct the global thick-body redistribution, control its derivatives, or prove the final weighted metric condition.

Accordingly, neither the desired density-unitary `S_r` conclusion for all `r>1` nor a counterexample for any `r>1` is established. The clue remains a research target rather than evidence.

## Research disposition

The clue remains `accepted`, with the local volume-gauge problem narrowed again by PF-177. Future work should not revisit central short-collar Schatten summation, central recoupling cancellation, heat-factor interpolation, qualitative existence of pant-wise area correction, or degeneration-uniform Jacobian correction *inside* the collapsed collar cores.

The live frontier is now: **freeze the PF-177 thin gauges, redistribute their summable area mismatch through one smooth globally coherent thick body/interface correction while preserving the two-sided weighted `delta^r` budget, and then invoke PF-175**. The only independent analytic alternative is the density-identification strip `1<r<2`. The clue resolves only when the full uncut density-unitary first relative resolvent is classified, or when a genuine global operator/geometric obstruction for some `r>1` is found.