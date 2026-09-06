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
  - research/prime_flute/findings/PF-178-support-controlled-moser-removes-global-volume-gauge-gluing-obstruction.md
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

PF-176 shows that on every compactly truncated matched one-cusp pant, equal area plus boundary Moser removes the abstract obstruction to an area-preserving correction. PF-177 removes the dangerous local quantitative interpretation of that problem: every matched collapsing short collar admits a gauge with `rho=1` throughout the potentially collapsing area-coordinate core, while unavoidable Jacobian defect is pushed into a uniformly thick outer rim with weighted `L^r` size `O(|t|^rL^{2r})`; those thick-rim budgets are summable over the complete PF-138 short-collar family.

PF-178 now removes the remaining **qualitative smooth-gluing/existence** issue. Explicit area-preserving two-sided Fermi germs can be imposed at every matched decomposition cuff, the common normalized cusp supplies an exact isometric germ, and support-controlled Moser correction can be made identity on whole boundary neighborhoods. The pant corrections therefore glue smoothly to a global marked diffeomorphism with `rho=1` exactly. This does not solve the Schatten route because support-controlled Moser supplies no degeneration-uniform metric estimate: the remaining geometric problem is purely quantitative.

## Research question

For the common-manifold density-unitary Laplacians associated with a quantitatively controlled smooth prime/shift marking, does

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

The negative endpoint is PF-112. For the positive side, PF-175 shows that weighted `delta^r` control yields `S_r` for every `r>1` in the dual-volume gauge. PF-178 proves that a smooth global area-preserving gauge exists, so the live geometric route is no longer to establish `rho=1` abstractly; it is to realize `rho=1` **while retaining tail-uniform quasi-isometry and the two-sided inverse-unit-ball weighted metric budget**. PF-177 already supplies the required quantitative localization on every collapsing short-collar core.

If that quantitative geometric route fails, the parallel operator question remains whether the one-sided density-identification correction can be controlled directly in `S_r` for `1<r<2` without imposing `rho=1`.

## Why it may matter

A positive answer would complete the natural operator-ideal classification between PF-112 and PF-125 and place the pair in every Schatten class strictly above the trace endpoint. It would still be a negative arithmetic control: the exact all-composite shift clone would share the same classification, so the ideal class itself could not certify primality or RH.

A negative answer for some `r>1` would now identify a genuinely global **quantitative** amplification mechanism. Such an obstruction cannot be attributed merely to zero systole, the complete fixed-central short-collar family, central transmission zero modes, the heat-factor Schatten step, absence of a first-resolvent factorization, qualitative area-preserving pant existence, smooth global `rho=1` gluing, or the need to solve a Jacobian equation inside collapsed collar cores. Those channels are controlled by PF-171, PF-173, PF-174, PF-175, PF-176, PF-177, and PF-178.

## Decisive test

The geometric test should freeze all solved existence and thin-geometry issues. On every PF-138 matched short collar use the PF-177 gauge, so `rho=1` on the whole potentially collapsing core and all residual density forcing lies in the uniformly thick rim. Use PF-178's principle that volume correction may be supported away from common gluing germs, rather than reopening boundary-jet compatibility as an abstract problem.

The decisive task is to construct, or obstruct, a **quantitative representative inside the PF-178 global `rho=1` class** such that:

1. the interior volume redistribution can be performed through uniformly controlled thick regions while retaining the common cuff/cusp germs;
2. the correction is uniformly quasi-isometric on the tail, with metric strain at the scale supplied by the existing prime/shift body/interface estimates;
3. for every desired `r>1`, the final transported metric satisfies
   \[
   \int W_g\,\delta_{g,g_+}^{\,r}\,d\mu_g
   +
   \int W_{g_+}\,\delta_{g,g_+}^{\,r}\,d\mu_{g_+}
   <\infty.
   \]

A promising sufficient route would place every residual Jacobian forcing a **uniform positive geometric distance** from the relevant correction-domain boundary and prove a uniform Hölder/Sobolev estimate for the support-controlled divergence/Jacobian solver. This qualification matters: the classical support-control construction itself does not give a norm constant independent of support-to-boundary distance, so PF-178 cannot simply be iterated with shrinking collars and declared quantitative.

If such a controlled `rho=1` marking is obtained, `J^\vee=I=U` and PF-175 immediately gives the canonical density-unitary `S_r` conclusion for every `r>1`.

The alternative operator route is to prove directly that the one-sided density correction in PF-175 belongs to `S_r` for `1<r<2` using structure beyond the `S_2`-to-operator interpolation currently available. Any such argument must preserve PF-112's endpoint obstruction: a method that also forces the standard first resolvent into `S_1` has erased a real high-frequency contribution.

A decisive negative resolution must produce a singular-value lower bound in the unresolved body/interface/nonlocal channel, prove that every quantitatively controlled global area-preserving redistribution necessarily violates the weighted metric budget, or otherwise show that the `1<r<2` density-unitary transfer fails intrinsically. Failure of one arbitrary support-controlled Moser construction is not enough, because PF-178 proves qualitative `rho=1` existence with substantial gauge freedom.

## Evidence boundary

PF-171 concerns the Dirichlet-decoupled fixed-central collar direct sum, and PF-173 concerns the matched central-cut recoupling family. Neither includes the complementary-body Dirichlet-to-Neumann response or complete outer interfaces of the infinite flute.

PF-174 supplies the weighted short-collar input and heat-smoothed Schatten factorization. PF-175 supplies a conditional first-resolvent theorem from weighted metric deviation, but its strongest `r>1` statement uses the dual-volume identification rather than automatically the canonical density-unitary map. PF-126 remains unweighted, while PF-130/PF-139 give strong unweighted body information without the complete inverse-unit-ball weighted assembly.

PF-176 is qualitative pant-local boundary Moser theory. PF-177 is an exact quantitative collar gauge: it removes Jacobian forcing from the collapsing core and proves summable thick-rim density budgets, but an isolated full standard collar cannot be area preserving when its source and target areas differ. PF-178 uses support-controlled Moser and explicit cuff/cusp germs to prove that those local conservation mismatches can nevertheless be absorbed in a **smooth global area-preserving marking**. It does not control the derivative size of the pant-interior corrections, prove global quasi-isometry for that marking, or establish the final weighted metric condition.

Accordingly, neither the desired density-unitary `S_r` conclusion for all `r>1` nor a counterexample for any `r>1` is established. The clue remains a research target rather than evidence.

## Research disposition

The clue remains `accepted`, with PF-178 closing the qualitative global volume-gauge/gluing question. Future work should not revisit central short-collar Schatten summation, central recoupling cancellation, heat-factor interpolation, qualitative pant-wise area correction, smooth global area-preserving existence, or degeneration-uniform Jacobian correction *inside* the collapsed collar cores.

The live frontier is now: **build a quantitatively controlled representative of the already-existing global `rho=1` gauge, keeping volume redistribution in uniformly controlled thick body/interface regions and proving the two-sided weighted `delta^r` budget, then invoke PF-175**. The only independent analytic alternative is the density-identification strip `1<r<2`. The clue resolves only when the full uncut density-unitary first relative resolvent is classified, or when a genuine global operator/geometric obstruction for some `r>1` is found.