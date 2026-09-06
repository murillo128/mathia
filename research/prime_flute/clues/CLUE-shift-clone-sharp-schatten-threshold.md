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
  - research/prime_flute/findings/PF-187-boundary-normalized-marked-collar-strain-is-uniformly-qualitatively-sobolev-rigid.md
---

# Does the prime/shift relative resolvent have the sharp Schatten threshold `S_r`, `r>1`?

## Observation

The operator-theoretic endpoints are already separated. PF-112 shows that the canonical first relative resolvent is not trace class, PF-125 gives compact relative resolvent, and PF-171/PF-173 remove the complete Margulis-short central block and its recoupling as stronger obstructions. PF-174--PF-175 give the positive bridge: a complete quasi-isometric comparison with two-sided inverse-unit-ball weighted metric defect in `L^r`, `r>1`, yields an `S_r` first-resolvent comparison; in the exact-area gauge the dual and density-unitary identifications coincide.

PF-177--PF-182 construct the exact-area body/collar ingredients and remove the volume, Lambert-body, artificial-split, cusp, and distinguished decomposition-cuff interfaces. PF-183 then shows that the complete family of true PF-138 short collars creates no additional multiplicity loss if each remaining splice is confined to its fixed thick slab and is charged to the **actual local body energy**. PF-184 removes annular flux: the canonical relative germ is exact symplectic. PF-185 removes the linearized/Killing-field kernel under the zero-twist reflection and proves the desired energy-local cutoff once the germ lies in one fixed `C^1` generating neighborhood.

PF-186 rules out the tempting generic route to that final hypothesis. Even on the normalized PF-185 slab, exact symplectic reflection-equivariant boundary-fixed maps can have zero flux and metric deviation tending to zero in `L^infinity` while their derivative equals `-I` at reflected interior points. Hence neither local `L^r` energy nor even small pointwise metric strain selects the near-identity derivative branch in `C^1`.

PF-187 now closes the corresponding **qualitative Sobolev** question after boundary normalization. Kupferman--Maor--Shachar's Riemannian Reshetnyak theorem, combined with compactness of the normalized metric family `g_L`, `0<=L<=mu_*`, gives a modulus uniform through the cusp limit: a boundary-preserving reflection-equivariant annulus diffeomorphism whose differential distortion and collar-parameter mismatch tend to zero must approach a global isometry in `W^{1,r}`. The only reflection-compatible orientation-preserving isometries are the identity and the half-turn, and the ordered PF-142 marking removes the half-turn. Thus PF-186's localized rotations are a `C^1` obstruction but not a qualitative `W^{1,r}` obstruction.

This does **not** yet supply PF-183 equation (11). PF-187 is qualitative and assumes that the relative germ has already been normalized as a boundary-preserving self-map of the fixed annulus. It gives no linear estimate in the local strain, no controlled boundary-normalization step for the raw PF-179--PF-184 germ, and no exact-symplectic cutoff. Conti--Dolzmann--Müller's optimal quantitative rigidity theorem supplies the desired linear scaling modulo a global isometry on compact manifolds to themselves, but the audited theorem does not state the boundary version needed here.

## Research question

Can one construct, for every `r>1`, one smooth complete area-preserving marking `F:X->X_+` whose true-short-collar transitions satisfy PF-183's uniform energy-local estimate and therefore give

\[
(\Delta_{g_+}+1)^{-1}F_* - F_*(\Delta_g+1)^{-1}\in\mathcal S_r
\qquad(r>1),
\]

while PF-112 keeps the endpoint outside `S_1`?

After PF-184--PF-187, the low-regularity route is no longer blocked by a possible qualitative loss of Sobolev rigidity at the cusp limit. The precise missing local theorem is now an **energy-linear boundary-normalization and marked rigidity estimate**, followed by an **energy-linear exact-symplectic localization**. The alternative route remains to prove that the actual canonical PF-179--PF-184 germ has additional structure forcing entry into PF-185's fixed `C^1` generating chart.

## Why it may matter

A positive answer would complete the natural operator-ideal classification

\[
A\in\mathcal S_r\ \text{for every }r>1,
\qquad A\notin\mathcal S_1,
\]

for the exact all-composite shift clone. That would be a strong negative arithmetic control: this entire relative-resolvent Schatten hierarchy would fail to distinguish literal primality, so any RH-relevant mechanism would have to live in finer data not fixed by the clone equivalence.

A negative answer is now correspondingly constrained. It must expose a genuine quantitative localization obstruction, a boundary-normalization cost not absorbed by local body energy, a trace mode not absorbed by the marked Sobolev branch, or an operator-level amplification. It cannot be blamed on volume mismatch, global collar multiplicity, annular flux, the reflection-marked linearized kernel, qualitative Sobolev degeneration as `L->0`, or a supposed automatic implication from small strain to `C^1` chart entry.

## Decisive test

Freeze PF-179--PF-187 rather than reopening their solved modules. Use PF-138 for the full tail family and PF-177's exact area coordinate. On PF-183's fixed thick slab, seek an exact-area interpolation joining the PF-177 core gauge to the canonical body germ with

\[
E_r(\operatorname{splice}_\eta)
\le C_r\bigl(E_r^{\mathrm{body}}(T_\eta)+|t_\eta|^r\bigr),
\]

on both source and inverse/target sides.

For the low-regularity route, separate three quantitative operations rather than treating rigidity as one black box.

First, take the raw canonical PF-184 annular germ and normalize it to a self-diffeomorphism of the fixed PF-183 slab carrying boundary to boundary, while proving that the normalization cost is bounded by the same local body-strain energy plus `|t|^r`. PF-187 must not be invoked before this boundary-normalization hypothesis is actually established.

Second, prove, or decisively refute, a **linear** marked rigidity estimate on the boundary-normalized fixed annulus of the schematic form

\[
\|H-\operatorname{id}\|_{W^{1,r}}
\le
C_r\left(
\|\delta_{g_L,H^*g_{L^+}}\|_{L^r}+|t|
\right),
\]

with `C_r` uniform for `0<=L<=mu_*`. PF-187 supplies the qualitative compactness control and identity selection, so a counterexample to the desired linear estimate must exhibit a genuinely quantitative loss rather than merely a drifting isometry branch or a cusp-family degeneration. Conti--Dolzmann--Müller supplies the target optimal scaling in the boundaryless/global setting; the missing bridge is the marked annulus-with-boundary version with the required uniform constant.

Third, assuming that marked `W^{1,r}` estimate, construct an exact-symplectic cutoff between the core identity and outer canonical germ with the same linear `W^{1,r}` cost. This is the genuinely symplectic part of the low-regularity route; neither PF-187 nor a geometric-rigidity theorem by itself provides the Hamiltonian/exact-area interpolation.

The alternative positive route remains **canonical `C^1` chart entry**: derive a uniform near-identity bound for the actual relative germs from the explicit PF-179--PF-182 assembly plus PF-142 marking/PF-184 exactness, not from metric strain alone; then PF-185's generating-function cutoff applies.

PF-143--PF-145 remain the interface falsifiers, PF-186 is the `C^1` chart-entry falsifier, and PF-187 is now the qualitative Sobolev falsification control. A claimed proof that begins with only `delta->0`, exactness, zero flux, and reflection and concludes `C^1` closeness is invalid. Conversely, a claimed low-regularity obstruction cannot consist only of a sequence whose strain tends to zero while its marked boundary-normalized `W^{1,r}` distance stays bounded away from zero: PF-187 rules that out. A decisive negative result must show an unavoidable **rate** loss or localization cost for the canonical germ.

## Evidence boundary

No complete weighted area-preserving marking is established. PF-183 remains conditional on the local splice estimate. PF-184 proves exactness but no quantitative cutoff. PF-185 proves marked coercivity and the cutoff estimate only after fixed `C^1` chart entry. PF-186 proves that such entry is not a consequence of the generic energy/topology/marking hypotheses, but it does **not** show that the canonical prime/shift germ realizes its counterexample and does not refute a low-regularity splice theorem.

PF-187 proves only a uniform **qualitative** `W^{1,r}` modulus for boundary-normalized marked annulus diffeomorphisms. It does not provide the per-collar linear estimate needed for summability and does not establish that the raw canonical germ satisfies the boundary-normalization hypothesis at controlled cost. Kupferman--Maor--Shachar therefore close the qualitative compactness question, not the quantitative PF-183 budget. Conti--Dolzmann--Müller give the desired optimal `W^{1,r}`-versus-strain scaling modulo isometries on compact manifolds to themselves, but the required boundary extension and the subsequent exact-symplectic localization remain unproved here.

PF-175 therefore remains conditional, and neither `S_r` membership for all `r>1` nor a counterexample above the trace endpoint has been proved.

## Research disposition

The clue remains `accepted`. The live problem is now factored more sharply into **energy-linear boundary normalization**, **uniform linear marked Sobolev rigidity**, and **energy-linear exact-symplectic localization**. PF-187 establishes that the normalized collar family itself has no qualitative Sobolev degeneration through `L=0`, so further work should target quantitative constants and the symplectic splice rather than another compactness argument. The canonical `C^1` route remains available if the explicit prime/shift assembly supplies stronger information. PF-183 handles the infinite collar family automatically once either local route yields the required estimate. The clue resolves only when those local splices assemble to the complete PF-175 hypothesis and yield the density-unitary `S_r`, `r>1`, classification, or when a genuine unavoidable obstruction to that local energy estimate is proved.