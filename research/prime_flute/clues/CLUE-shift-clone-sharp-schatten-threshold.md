---
id: CLUE-prime-flute-shift-clone-sharp-schatten-threshold
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-112-first-relative-resolvent-is-not-trace-class.md
  - research/prime_flute/findings/PF-125-shift-clone-has-compact-relative-resolvent.md
  - research/prime_flute/findings/PF-142-zero-twist-reflection-removes-short-collar-phase-gauge.md
  - research/prime_flute/findings/PF-171-all-margulis-short-central-first-resolvent-blocks-have-sharp-Sr-threshold.md
  - research/prime_flute/findings/PF-173-relative-central-recoupling-is-trace-summable.md
  - research/prime_flute/findings/PF-174-weighted-defect-controls-smoothed-schatten-scale.md
  - research/prime_flute/findings/PF-175-weighted-defect-gives-dual-resolvent-schatten-bridge.md
  - research/prime_flute/findings/PF-177-collar-jacobian-defect-can-be-expelled-from-collapsing-core.md
  - research/prime_flute/findings/PF-178-support-controlled-moser-removes-global-volume-gauge-gluing-obstruction.md
  - research/prime_flute/findings/PF-179-lambert-area-transport-is-uniformly-near-isometric.md
  - research/prime_flute/findings/PF-180-area-preserving-lambert-split-synchronization.md
  - research/prime_flute/findings/PF-181-area-preserving-cusp-handoff-has-summable-weighted-cost.md
  - research/prime_flute/findings/PF-182-area-preserving-decomposition-cuff-seams-can-be-smoothed-at-summable-weighted-cost.md
  - research/prime_flute/findings/PF-183-disjoint-thick-collar-slabs-remove-multiplicity-from-schatten-splice-budget.md
  - research/prime_flute/findings/PF-184-canonical-short-collar-relative-flux-vanishes.md
  - research/prime_flute/findings/PF-185-reflection-marked-korn-coercivity-removes-linearized-collar-splice-kernel.md
  - research/prime_flute/findings/PF-186-small-exact-symplectic-collar-strain-does-not-force-c1-chart-entry.md
---

# Does the prime/shift relative resolvent have the sharp Schatten threshold `S_r`, `r>1`?

## Observation

The operator-theoretic endpoints are already separated. PF-112 shows that the canonical first relative resolvent is not trace class, PF-125 gives compact relative resolvent, and PF-171/PF-173 remove the complete Margulis-short central block and its recoupling as stronger obstructions. PF-174--PF-175 give the positive bridge: a complete quasi-isometric comparison with two-sided inverse-unit-ball weighted metric defect in `L^r`, `r>1`, yields an `S_r` first-resolvent comparison; in the exact-area gauge the dual and density-unitary identifications coincide.

PF-177--PF-182 construct the exact-area body/collar ingredients and remove the volume, Lambert-body, artificial-split, cusp, and distinguished decomposition-cuff interfaces. PF-183 then shows that the complete family of true PF-138 short collars creates no additional multiplicity loss if each remaining splice is confined to its fixed thick slab and is charged to the **actual local body energy**. PF-184 removes annular flux: the canonical relative germ is exact symplectic. PF-185 removes the linearized/Killing-field kernel under the zero-twist reflection and proves the desired energy-local cutoff once the germ lies in one fixed `C^1` generating neighborhood.

PF-186 now rules out the tempting generic route to that final hypothesis. Even on the normalized PF-185 slab, exact symplectic reflection-equivariant boundary-fixed maps can have zero flux and metric deviation tending to zero in `L^infinity` while their derivative equals `-I` at reflected interior points. Hence neither local `L^r` energy nor even small pointwise metric strain selects the near-identity derivative branch. The canonical prime/shift construction must supply additional structure, or the splice must be localized directly below the `C^1` chart threshold.

A targeted rigidity audit sharpens that second option. Kupferman--Maor--Shachar, *Reshetnyak rigidity for Riemannian manifolds* (Arch. Ration. Mech. Anal. 231 (2019), 367--408, DOI `10.1007/s00205-018-1282-9`, arXiv:1701.08892), work with compact oriented Riemannian manifolds **possibly with `C^1` boundary** and prove qualitative `W^{1,p}` rigidity: if the differential distance to the orientation-preserving isometries tends to zero in `L^p`, a subsequence converges to an isometric immersion; for diffeomorphisms carrying boundary to boundary between equal-volume manifolds, their proof identifies the limit as an isometry. Conti--Dolzmann--Müller, *Optimal Rigidity Estimates for Maps of a Compact Riemannian Manifold to Itself* (SIAM J. Math. Anal. 56 (2024), 8070--8095, DOI `10.1137/24M1650168`, arXiv:2402.06448), prove the optimal quantitative analogue for `1<p<infinity`, controlling `W^{1,p}` distance to a **single global isometry** by the `L^p` differential-distance energy.

These results show that PF-186's localized rotations are not automatically a Sobolev-scale obstruction: geometric rigidity is designed precisely to couple locally varying rotation frames. But they do **not** yet supply PF-183 equation (11). The Conti--Dolzmann--Müller theorem does not state the quantitative boundary version needed for the normalized annulus, neither source supplies a constant already proved uniform over the compact metric family `g_L`, `0<=L<=mu_*`, and both formulate rigidity modulo a global isometry rather than directly modulo the PF-142 marked identity. The remaining exact-symplectic cutoff is a separate problem even after Sobolev rigidity is established.

## Research question

Can one construct, for every `r>1`, one smooth complete area-preserving marking `F:X->X_+` whose true-short-collar transitions satisfy PF-183's uniform energy-local estimate and therefore give

\[
(\Delta_{g_+}+1)^{-1}F_* - F_*(\Delta_g+1)^{-1}\in\mathcal S_r
\qquad(r>1),
\]

while PF-112 keeps the endpoint outside `S_1`?

After PF-184--PF-186 and the rigidity audit, the local problem has a more precise intermediate gate. On every normalized true-short-collar slab, either prove that the **actual PF-179--PF-184 relative germ** enters PF-185's fixed generating chart using explicit canonical information stronger than strain, or establish a boundary-uniform marked geometric-rigidity estimate at `W^{1,r}` scale and then construct an exact-symplectic localization whose cost is linear in that Sobolev/strain energy.

## Why it may matter

A positive answer would complete the natural operator-ideal classification

\[
A\in\mathcal S_r\ \text{for every }r>1,
\qquad A\notin\mathcal S_1,
\]

for the exact all-composite shift clone. That would be a strong negative arithmetic control: this entire relative-resolvent Schatten hierarchy would fail to distinguish literal primality, so any RH-relevant mechanism would have to live in finer data not fixed by the clone equivalence.

A negative answer is now correspondingly constrained. It must expose a genuine quantitative localization obstruction, a trace mode not absorbed by local metric energy, or an operator-level amplification. It cannot be blamed on volume mismatch, global collar multiplicity, annular flux, the reflection-marked linearized kernel, or a supposed automatic implication from small strain to `C^1` chart entry.

## Decisive test

Freeze PF-179--PF-186 rather than reopening their solved modules. Use PF-138 for the full tail family and PF-177's exact area coordinate. On PF-183's fixed thick slab, seek an exact-area interpolation joining the PF-177 core gauge to the canonical body germ with

\[
E_r(\operatorname{splice}_\eta)
\le C_r\bigl(E_r^{\mathrm{body}}(T_\eta)+|t_\eta|^r\bigr),
\]

on both source and inverse/target sides.

For the low-regularity route, separate **rigidity** from **symplectic localization** instead of treating them as one black box. First prove, or decisively refute, a quantitative estimate on the fixed annulus of the schematic form

\[
\inf_{\phi\in\mathcal I_L}
\|H-\phi\|_{W^{1,r}}
\le
C_r\left(
\|\delta_{g_L,H^*g_{L^+}}\|_{L^r}+|t|
\right),
\]

with `C_r` uniform for `0<=L<=mu_*`, where `mathcal I_L` is the finite-dimensional/global isometry ambiguity compatible with the annular model. The PF-175 quasi-isometry regime makes the metric-deficit and differential-distance energies locally comparable, so the real missing theorem is the **quantitative boundary/uniform-family version**, not a pointwise choice of polar rotation. Kupferman--Maor--Shachar supply a qualitative boundary compactness/falsification control; Conti--Dolzmann--Müller supply the target optimal scaling in the boundaryless/global setting.

Second, show that the canonical PF-142 marking and whatever additional canonical trace or `C^0` information is actually available select the identity component/isometry in a quantitatively stable way. Reflection alone is insufficient: PF-142 explicitly records the half-turn ambiguity before the ordered marking is imposed, and a Sobolev argument must not silently replace that discrete selection by the infinitesimal Korn statement of PF-185.

Third, assuming the marked `W^{1,r}` estimate, construct an exact-symplectic cutoff between the core identity and outer canonical germ with the same linear `W^{1,r}` cost. This is the genuinely symplectic part of the low-regularity route; a geometric-rigidity theorem by itself does not provide the Hamiltonian/exact-area interpolation.

The alternative positive route remains **canonical `C^1` chart entry**: derive a uniform near-identity bound for the actual relative germs from the explicit PF-179--PF-182 assembly plus PF-142 marking/PF-184 exactness, not from metric strain alone; then PF-185's generating-function cutoff applies.

PF-143--PF-145 remain the interface falsifiers, while PF-186 is the chart-entry falsifier. A claimed proof that begins with only `delta->0`, exactness, zero flux, and reflection and concludes `C^1` closeness is invalid. A decisive negative result must instead show an unavoidable cost for the **canonical** germ or for every exact-area localization satisfying the required boundary values; failure of one chosen interpolation or existence of noncanonical microtwists is not enough.

## Evidence boundary

No complete weighted area-preserving marking is established. PF-183 remains conditional on the local splice estimate. PF-184 proves exactness but no quantitative cutoff. PF-185 proves marked coercivity and the cutoff estimate only after fixed `C^1` chart entry. PF-186 proves that such entry is not a consequence of the generic energy/topology/marking hypotheses, but it does **not** show that the canonical prime/shift germ realizes its counterexample and does not refute a low-regularity splice theorem.

The rigidity literature narrows the gap but does not close it. Kupferman--Maor--Shachar give qualitative convergence, not the per-collar linear estimate needed for summability. Conti--Dolzmann--Müller give the desired optimal `W^{1,r}`-versus-strain scaling modulo isometries, but the required annulus-with-boundary extension and uniformity through the `L=0` cusp limit have not been established here. Neither theorem supplies an exact-symplectic cutoff, and no claim is made that PF-142's marking alone gives the required quantitative isometry selection at Sobolev regularity.

PF-175 therefore remains conditional, and neither `S_r` membership for all `r>1` nor a counterexample above the trace endpoint has been proved.

## Research disposition

The clue remains `accepted`. The live problem is now factored into a more precise sequence: **uniform marked Sobolev rigidity on the normalized short-collar family**, followed by **energy-linear exact-symplectic localization**. The existing rigidity literature makes the first step plausible and provides a strong qualitative falsification control, while PF-186 explains why it must stop at Sobolev rather than `C^1` scale. The canonical `C^1` route remains available if the explicit prime/shift assembly supplies stronger information. PF-183 handles the infinite collar family automatically once either local route yields the required estimate. The clue resolves only when those local splices assemble to the complete PF-175 hypothesis and yield the density-unitary `S_r`, `r>1`, classification, or when a genuine unavoidable obstruction to that local energy estimate is proved.