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
  - research/prime_flute/findings/PF-179-lambert-area-transport-is-uniformly-near-isometric.md
  - research/prime_flute/findings/PF-180-area-preserving-lambert-split-synchronization.md
  - research/prime_flute/findings/PF-181-area-preserving-cusp-handoff-has-summable-weighted-cost.md
---

# Does the prime/shift relative resolvent have the sharp Schatten threshold `S_r`, `r>1`?

## Observation

PF-112 fixes the two-dimensional endpoint for the standard density-unitary comparison: the genuinely non-isometric prime/shift first relative resolvent is not trace class, while microlocal order remains compatible with `S_r` for every `r>1`. PF-125 proves global compact relative resolvent, but compactness does not determine the Schatten exponent.

The complete Margulis-short central sector is no longer the plausible obstruction. PF-171 proves the sharp `S_r`, `r>1`, threshold for the direct sum of all fixed-central first-resolvent collar blocks, PF-173 makes the matched central-cut recoupling correction trace summable, and PF-174 proves the inverse-unit-ball weighted `delta^r` scale on those collapsing collars together with the corresponding heat-smoothed Schatten factorization.

PF-175 closes the first-resolvent analytic bridge under a form-natural dual-volume identification. If one coherent prime/shift marking satisfies the global weighted metric condition at exponent `r>1`, then

\[
(\Delta_{g_+}+1)^{-1}J^\vee
-I(\Delta_g+1)^{-1}
\in\mathcal S_r,
\qquad
J^\vee=(I^{-1})^*.
\]

The same input reaches the trivial and density-unitary identifications for `r>=2`. Thus the residual analytic strip `1<r<2` is identification-sensitive rather than a missing generic resolvent-unsmoothing theorem.

PF-176--PF-178 remove the qualitative volume-gauge obstruction. Equal-area truncated pants admit boundary-preserving correction, dangerous collar Jacobian forcing can be expelled from collapsing cores, and support-controlled Moser plus common cuff/cusp germs gives a smooth global marked diffeomorphism with `rho=1` exactly. The remaining issue after PF-178 was quantitative: its interior Moser construction carries no degeneration-uniform metric estimate.

PF-179--PF-181 now remove three major pieces of that quantitative body/interface problem without using a degenerating pant-wide Moser estimate. PF-179 gives explicit area-preserving `1+O(delta_n)` transports of each Lambert body and an unweighted `L^r` body budget for every `r>1`. PF-180 synchronizes the two area-preserving Lambert transports along their artificial split through the canonical cusp entry by Hamiltonian self-corrections which preserve area exactly and add only a summable strong-`L^1` metric cost. PF-181 then uses the exact area balance of the lower pant to show that its actual cusp trace has zero area flux, allowing a fixed nondegenerating slab to hand that complete area-preserving germ to the exact deep-cusp identity with a summable two-sided inverse-unit-ball weighted cost. Thus **Lambert-body area transport, internal split synchronization, and the full-cusp handoff in the area gauge are no longer live obstructions**.

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

The negative endpoint is PF-112. For the positive side, PF-175 shows that weighted `delta^r` control yields `S_r` for every `r>1` in the dual-volume gauge. PF-178 proves that a smooth global area-preserving gauge exists, while PF-179--PF-181 show that its **Lambert-body, artificial-split, and full-cusp sectors can be realized quantitatively with `rho=1`**. The live geometric route is therefore narrower: realize compatible quantitative zero-twist cuff germs, splice the resulting body/cuff map to every PF-177/PF-138 true short-collar gauge, and prove the final two-sided inverse-unit-ball weighted metric budget in one complete marking.

If that geometric route fails, the parallel operator question remains whether the one-sided density-identification correction can be controlled directly in `S_r` for `1<r<2` without imposing `rho=1`.

## Why it may matter

A positive answer would complete the natural operator-ideal classification between PF-112 and PF-125 and place the pair in every Schatten class strictly above the trace endpoint. It would still be a negative arithmetic control: the exact all-composite shift clone would share the same classification, so the ideal class itself could not certify primality or RH.

A negative answer for some `r>1` would now identify a genuinely global closed-interface/nonlocal amplification mechanism. Such an obstruction cannot be attributed merely to zero systole, the complete central short-collar family, central transmission zero modes, the heat-factor Schatten step, absence of a first-resolvent factorization, qualitative area-preserving existence, Jacobian correction inside collapsed collar cores, Lambert-body volume redistribution, artificial-split synchronization, or the full cusp handoff. Those channels are controlled by PF-171, PF-173, PF-174, PF-175, PF-176, PF-177, PF-178, PF-179, PF-180, and PF-181.

## Decisive test

Freeze the solved body, cusp, and thin-core pieces rather than reopening them. Use PF-179's exact area-preserving Lambert transports, PF-180's area-preserving split synchronization, PF-181's exact-area deep-cusp handoff, and the PF-177 gauge on every PF-138 matched short collar so that `rho=1` on the entire potentially collapsing collar core and all unavoidable collar-area mismatch is deferred to uniformly thick rims.

The decisive task is to construct, or obstruct, **one complete smooth area-preserving prime/shift marking** which simultaneously:

1. realizes compatible two-sided area-preserving zero-twist germs at the distinguished decomposition cuffs and splices the body map to the PF-177 true-short-collar gauges without reintroducing large metric strain;
2. remains uniformly quasi-isometric on the tail;
3. for every desired `r>1`, satisfies
   \[
   \int W_g\,\delta_{g,g_+}^{\,r}\,d\mu_g
   +
   \int W_{g_+}\,\delta_{g,g_+}^{\,r}\,d\mu_{g_+}
   <\infty.
   \]

The unresolved geometry is therefore a **closed-interface compatibility problem**, not a body-volume, split, or cusp-volume existence problem. Any remaining volume exchange should be confined to the controlled cuff/true-short-collar thick-rim regions identified by PF-177 rather than solved by an unconstrained pant-wide Moser correction.

If such a controlled `rho=1` marking is obtained, `J^\vee=I=U` and PF-175 immediately gives the canonical density-unitary `S_r` conclusion for every `r>1`.

The alternative operator route is to prove directly that the one-sided density correction in PF-175 belongs to `S_r` for `1<r<2` using structure beyond the `S_2`-to-operator interpolation currently available. Any such argument must preserve PF-112's endpoint obstruction: a method that also forces the standard first resolvent into `S_1` has erased a real high-frequency contribution.

A decisive negative resolution must produce a singular-value lower bound in the unresolved closed-interface/nonlocal channel, prove that every quantitatively controlled global area-preserving assembly necessarily violates the weighted metric budget, or otherwise show that the `1<r<2` density-unitary transfer fails intrinsically. Failure of one arbitrary cuff/collar interpolation is not enough because PF-178 proves qualitative `rho=1` existence and PF-177/PF-179--PF-181 provide substantial quantitative gauge freedom on the collar core, body, split, and cusp sectors.

## Evidence boundary

PF-171 concerns the Dirichlet-decoupled fixed-central collar direct sum, and PF-173 concerns the matched central-cut recoupling family. Neither includes the complementary-body Dirichlet-to-Neumann response or complete outer interfaces of the infinite flute.

PF-174 supplies weighted short-collar input and heat-smoothed Schatten factorization. PF-175 supplies a conditional first-resolvent theorem from weighted metric deviation, but its strongest `r>1` statement uses the dual-volume identification rather than automatically the canonical density-unitary map. PF-126 remains unweighted.

PF-177 is an exact quantitative collar gauge but does not by itself glue those collars into the body. PF-178 proves smooth global area-preserving existence but not quantitative control. PF-179 proves exact area-preserving near-isometric transport on individual Lambert bodies, PF-180 proves exact area-preserving split synchronization with summable correction cost, and PF-181 proves a summable **weighted** exact-area handoff from that lower body to the deep-cusp identity. None of PF-179--PF-181 proves compatible quantitative gluing across all distinguished cuffs and PF-138 true short collars, and none proves the complete-surface PF-175 weighted hypothesis.

Accordingly, neither the desired density-unitary `S_r` conclusion for all `r>1` nor a counterexample for any `r>1` is established. The clue remains a research target rather than evidence.

## Research disposition

The clue remains `accepted`. PF-181 materially narrows the geometric frontier again: future work should not revisit pant-wise volume existence, Lambert-body area transport, artificial-split synchronization, or the full-cusp handoff as generic Moser problems.

The live frontier is now **closed-interface quantitative assembly**: make the area-preserving decomposition-cuff germs and PF-177 true-short-collar gauges coexist with the controlled body map, prove the resulting two-sided weighted `delta^r` budget on the complete surface, and invoke PF-175. The only independent analytic alternative remains the density-identification strip `1<r<2`. The clue resolves only when the full uncut density-unitary first relative resolvent is classified, or when a genuine global operator/geometric obstruction for some `r>1` is found.