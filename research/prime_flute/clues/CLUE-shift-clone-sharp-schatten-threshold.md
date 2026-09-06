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
  - research/prime_flute/findings/PF-188-fixed-germ-marked-collar-strain-is-qualitatively-sobolev-rigid-without-boundary-normalization.md
---

# Does the prime/shift relative resolvent have the sharp Schatten threshold `S_r`, `r>1`?

## Observation

The operator-theoretic endpoints are already separated. PF-112 shows that the canonical first relative resolvent is not trace class, PF-125 gives compact relative resolvent, and PF-171/PF-173 remove the complete Margulis-short central block and its recoupling as stronger obstructions. PF-174--PF-175 give the positive bridge: a complete quasi-isometric comparison with two-sided inverse-unit-ball weighted metric defect in `L^r`, `r>1`, yields an `S_r` first-resolvent comparison; in the exact-area gauge the dual and density-unitary identifications coincide.

PF-177--PF-182 construct the exact-area body/collar ingredients and remove the volume, Lambert-body, artificial-split, cusp, and distinguished decomposition-cuff interfaces. PF-183 then shows that the complete family of true PF-138 short collars creates no additional multiplicity loss if each remaining splice is confined to its fixed thick slab and is charged to the **actual local body energy**. PF-184 removes annular flux: the canonical relative germ is exact symplectic. PF-185 removes the linearized/Killing-field kernel under the zero-twist reflection and proves the desired energy-local cutoff once the germ lies in one fixed `C^1` generating neighborhood.

PF-186 rules out a generic shortcut to that final `C^1` hypothesis. Exact-symplectic reflection-equivariant boundary-fixed maps can have metric strain tending to zero even in `L^infinity` while their derivative retains the wrong branch on shrinking disks. PF-187 then shows that this is not a qualitative `W^{1,r}` obstruction after boundary normalization: Riemannian Reshetnyak compactness plus the PF-142 marking forces convergence to the identity uniformly through `L=0`.

PF-188 removes one more artificial prerequisite. Reshetnyak's basic conclusion is an isometric **immersion**, so the relative germ need not first be turned into a boundary-preserving self-map merely to obtain qualitative marked Sobolev rigidity. On nested fixed positive-side slabs `A=[1,5/4]xS^1` inside `B=[3/4,3/2]xS^1`, every reflection-marked limiting isometric immersion is the canonical inclusion. At `L>0` hyperbolic translation length fixes the winding; at `L=0` higher cusp windings have the form `(x,theta)->(x/k,k theta+c)` and leave the fixed target slab when `k>=2`. Thus one established qualitative route needs only **fixed-germ confinement**, not boundary-to-boundary normalization.

This still does **not** supply PF-183's energy-linear splice estimate. PF-188 gives no rate, does not prove the actual PF-179--PF-184 germ stays in one fixed larger target slab, and does not construct an exact-symplectic cutoff. Conti--Dolzmann--Müller's optimal quantitative rigidity theorem supplies the desired linear scaling modulo a global isometry on compact manifolds to themselves, but the audited theorem does not state the annulus-with-boundary/localization result needed here.

A closer audit of that quantitative route sharpens the missing ingredient. Conti--Dolzmann--Müller's proof separates optimal rigidity into a Lipschitz approximation, a Riemannian Piola/almost-harmonic regularization step producing a sufficiently regular nearby map, and a final linearization/Korn argument; for Korn on Riemannian domains with boundary they refer to Chen--Jost, *A Riemannian version of Korn's inequality*, Calc. Var. PDE 14 (2002), 517--530, DOI `10.1007/s005260100113`. PF-185 already supplies the stronger project-specific fact needed at the last stage: a **uniform marked Korn constant for the entire normalized collar family through `L=0`**. Thus the unresolved quantitative transfer should not be described as another Korn problem. The missing analytic bridge is the nonlinear, energy-linear **nested-domain regularization/rigidity step** that turns local `L^r` strain into `O(strain)` `W^{1,r}` distance from the marked isometric branch without first imposing boundary-to-boundary normalization.

A fresh primary-source audit exposes a potentially useful way to weaken the remaining *raw target-confinement* prerequisite. Mert Baştuğ, *Rigidity of codimension-1 isometric immersions in complete manifolds*, arXiv:2604.11130v1 (2026), develops local quantitative rigidity on `epsilon`-isometric charts by reduction to Euclidean Friesecke--James--Müller rigidity. The paper explicitly introduces **globally defined cutoff extensions of target charts** because an arbitrary Sobolev map into a complete noncompact target need not send a small source region into one coordinate chart. This is methodologically close to the PF obstruction: analytic localization may be possible before proving that the raw canonical germ is contained in PF-188's fixed target annulus.

The full theorem audit narrows that transfer substantially. Baştuğ's Theorem 3.6 is an **equidimensional Euclidean-target** rigidity estimate for a source cube with nonconstant metric; its bound already contains the source-metric oscillation. Theorem 3.7 then uses the globally extended target chart in the codimension-one problem, but the resulting local bound carries additive chart/truncation/metric-oscillation errors in addition to stretching energy and the codimension-one normal/bending energy. Therefore the extended chart solves the *definition and codomain-localization* problem; it does **not** by itself provide the zero-floor energy-linear estimate required by PF-183. A fixed `epsilon`-chart cannot simply be inserted into the PF argument and then sent to zero strain while keeping an `O(strain)` conclusion.

This also clarifies what genuinely should transfer to the equidimensional PF collar. The independent bending/normal term enters Baştuğ because a `d`-dimensional immersion into dimension `d+1` must first be projected onto a `d`-plane before Theorem 3.6 applies. That positive-codimension step has no direct analogue for an equidimensional PF diffeomorphism. But removing it is only half the problem: one must also make the chart, curvature/metric-oscillation, and target-leakage errors **scale with the actual PF strain**, or bypass those errors with an intrinsic hyperbolic/nested-domain rigidity argument. This is a sharper transfer target, not an imported theorem and not evidence that fixed-germ confinement has already been removed.

## Research question

Can one construct, for every `r>1`, one smooth complete area-preserving marking `F:X->X_+` whose true-short-collar transitions satisfy PF-183's uniform energy-local estimate and therefore give

\[
(\Delta_{g_+}+1)^{-1}F_* - F_*(\Delta_g+1)^{-1}\in\mathcal S_r
\qquad(r>1),
\]

while PF-112 keeps the endpoint outside `S_1`?

After PF-184--PF-188, the low-regularity route is no longer blocked by annular flux, a linearized Killing kernel, qualitative Sobolev degeneration at the cusp, or the need to boundary-normalize the germ before applying compactness. The precise missing local theorem is an **energy-linear marked rigidity/localization estimate on a buffered collar germ**, followed by an **energy-linear exact-symplectic cutoff**. One route is to establish PF-188-style fixed-germ confinement for the canonical maps first. A second, now concrete route is to replace that prerequisite by an extended-chart/local target-tightness argument strong enough to obtain the quantitative estimate while still excluding cusp winding/drift escape.

The alternative high-regularity route remains to prove that the actual canonical PF-179--PF-184 germ has additional source-specific regularity forcing entry into PF-185's fixed `C^1` generating chart. PF-186 shows that such regularity cannot be inferred from strain, exactness, zero flux, and reflection alone.

## Why it may matter

A positive answer would complete the natural operator-ideal classification

\[
A\in\mathcal S_r\ \text{for every }r>1,
\qquad A\notin\mathcal S_1,
\]

for the exact all-composite shift clone. That would be a strong negative arithmetic control: this entire relative-resolvent Schatten hierarchy would fail to distinguish literal primality, so any RH-relevant mechanism would have to live in finer data not fixed by the clone equivalence.

A negative answer is now correspondingly constrained. It must expose a genuine quantitative localization obstruction, an unavoidable target-escape mode for the canonical map, a trace mode not absorbed by the marked Sobolev branch, or an operator-level amplification. It cannot be blamed on volume mismatch, global collar multiplicity, annular flux, the reflection-marked linearized kernel, qualitative Sobolev degeneration as `L->0`, or boundary-to-boundary normalization as such.

## Decisive test

Freeze PF-179--PF-188 rather than reopening their solved modules. Use PF-138 for the full tail family and PF-177's exact area coordinate. On PF-183's fixed thick slab, seek an exact-area interpolation joining the PF-177 core gauge to the canonical body germ with

\[
E_r(\operatorname{splice}_\eta)
\le C_r\bigl(E_r^{\mathrm{body}}(T_\eta)+|t_\eta|^r\bigr),
\]

on both source and inverse/target sides.

For the low-regularity route, separate the remaining operations instead of treating rigidity as one black box. Work with buffered source annuli `A_0 compactly contained A_1` inside the fixed thick PF-183 transition slab and pursue either of the following two localization gates.

The **fixed-germ route** is to prove that the actual canonical PF-179--PF-184 relative germ on `A_1` is contained, for all sufficiently short tail collars, in one fixed slightly larger positive-side target germ of the kind used in PF-188. An equivalent source-specific confinement condition that excludes the cusp power immersions is acceptable. Do **not** spend local energy merely to force boundary to boundary unless a later construction genuinely needs it; PF-188 shows that Reshetnyak compactness itself does not.

The **extended-chart route** is now a two-part test rather than a direct application of Baştuğ. First, obtain a globally defined target-coordinate representation whose leakage/tightness error for the actual canonical PF-179--PF-184 germ tends to zero at a rate controlled by the same local strain; a fixed `epsilon`-chart with a strain-independent error floor is insufficient. Second, prove the equidimensional local rigidity estimate after that representation without importing Baştuğ's codimension-one bending term. An energy-dependent chart scale is admissible only if the induced source-metric oscillation, target-chart error, overlap constants, and patching of local isometry modes remain `O(strain)` uniformly through `0<=L,L^+<=mu_*`. An intrinsic hyperbolic or lifted-chart argument that achieves the same zero-floor estimate is equally valid. Any auxiliary target-tightness assumption must be derived from the actual canonical map and cannot simply rename PF-188's fixed-germ hypothesis.

Either localization route must then prove or decisively refute a **linear** marked rigidity estimate, schematically

\[
\|H-\iota\|_{W^{1,r}(A_0)}
\le
C_r\left(
\|\delta_{g_L,H^*g_{L^+}}\|_{L^r(A_1)}+|t|
\right),
\]

with `C_r` uniform for `0<=L,L^+<=mu_*`. The estimate must include enough target control or marked topology to rule out the exact higher-winding cusp immersions exposed by PF-188; an extended chart alone is not a branch-selection theorem.

For the fixed-germ route, Conti--Dolzmann--Müller's architecture remains the most direct template: localize the Lipschitz approximation and Piola/almost-harmonic regularization on `A_1`, obtain on `A_0` a sufficiently regular comparison with `W^{1,r}` error **linear in the original local strain**, then use PF-185's uniform marked Korn estimate and PF-188's marked identity-branch selection. Chen--Jost indicates that boundary Korn itself is not the missing ingredient, so a boundary difficulty should first be attacked with the buffer/interior localization rather than by reintroducing boundary-to-boundary normalization.

For the extended-chart route, the primary-source falsifier is now explicit. A proof that simply invokes Baştuğ's Theorem 3.7 while retaining fixed positive `epsilon`, source-metric oscillation, or truncation/leakage terms has **not** proved PF-183's energy-local estimate, because those terms need not vanish with the collar's actual strain. A successful transfer must absorb or eliminate every such additive term before PF-185's marked Korn step. Conversely, proving that one of those terms has an unavoidable strain-independent lower floor for the canonical PF geometry would kill this route without refuting the separate fixed-germ route.

Finally, from the marked `W^{1,r}` control, construct an exact-symplectic cutoff between the core identity and outer canonical germ with the same energy-linear cost. This is the genuinely symplectic part of the low-regularity route; neither PF-187/PF-188 nor any audited geometric-rigidity theorem provides the Hamiltonian/exact-area interpolation automatically.

The alternative positive route remains **canonical `C^1` chart entry**: derive derivative equicontinuity or another stronger estimate from the explicit PF-179--PF-182 assembly plus PF-142 marking/PF-184 exactness; combine it with the qualitative `W^{1,r}` control when useful; then PF-185's generating-function cutoff applies. The extra derivative control must be source-specific because PF-186 kills the generic implication.

PF-143--PF-145 remain the interface falsifiers, PF-186 remains the generic `C^1` chart-entry falsifier, and PF-188 remains the exact warning that unconstrained cusp target escape can carry zero strain. A claimed low-regularity obstruction cannot consist only of vanishing strain with marked `W^{1,r}` distance bounded away from the inclusion **while the hypotheses of the chosen localization route hold**. A decisive negative result must show an unavoidable rate/localization loss, a genuine target-escape mode compatible with the canonical map, or failure of the exact-symplectic energy budget.

## Evidence boundary

No complete weighted area-preserving marking is established. PF-183 remains conditional on the local splice estimate. PF-184 proves exactness but no quantitative cutoff. PF-185 proves marked coercivity and the cutoff estimate only after fixed `C^1` chart entry. PF-186 proves that such entry is not a consequence of the generic energy/topology/marking hypotheses, but it does **not** show that the canonical prime/shift germ realizes its counterexample and does not refute a low-regularity splice theorem.

PF-187 proves only a uniform qualitative `W^{1,r}` modulus after boundary normalization. PF-188 strengthens the qualitative statement to maps of an inner slab into a fixed larger positive-side annulus, so boundary-to-boundary normalization is no longer part of the qualitative gate. But PF-188 deliberately retains fixed-germ confinement: at `L=0`, higher-winding exact cusp immersions escape toward `x=0` if that condition is removed. Neither finding provides the per-collar linear estimate needed for summability, and neither constructs the exact-symplectic localization.

Kupferman--Maor--Shachar therefore close the relevant compactness question, not the quantitative PF-183 budget. Conti--Dolzmann--Müller give the desired optimal `W^{1,r}`-versus-strain scaling modulo isometries on compact manifolds to themselves, and their proof architecture together with Chen--Jost's boundary Korn theorem identifies one plausible route to the nested-annulus estimate.

Baştuğ's 2026 preprint adds a distinct **codomain-localization technique**, not a theorem applicable as stated. Its extended charts address maps whose images do not lie in one target chart, but the published local estimate is codimension one and carries bending plus additive chart/truncation/source-metric errors. The equidimensional Theorem 3.6 removes the normal/bending issue only in Euclidean codomain and still retains source-metric oscillation. Thus the precise open transfer is narrower than previously stated: obtain a target-localization/reduction in which every chart and curvature error is controlled by the actual PF strain (or eliminated intrinsically), while separately enforcing the marked branch selection needed to exclude PF-188's cusp windings. No such zero-floor local estimate, canonical target-tightness theorem, or exact-symplectic cutoff is established here.

PF-175 therefore remains conditional, and neither `S_r` membership for all `r>1` nor a counterexample above the trace endpoint has been proved.

## Research disposition

The clue remains `accepted`. The live problem is now factored into **quantitative target localization/marked rigidity** and **energy-linear exact-symplectic cutoff**, with two concrete ways to attack the first factor. The fixed-germ route still asks for source-specific confinement and then a localized Conti--Dolzmann--Müller-style regularization argument. The extended-chart route is now more sharply constrained: the valuable Baştuğ idea is the globally defined codomain localization, but a successful PF transfer must remove the published estimate's strain-independent chart/truncation/metric-oscillation floor rather than merely dropping its codimension-one bending term. PF-185 means neither route has an unresolved linearized/Korn subproblem; PF-188 supplies the exact cusp-winding falsifier that either route must still exclude. Further work should therefore test whether the canonical body germ admits strain-controlled target localization, or prove the simpler source-specific confinement lemma, before addressing the genuinely symplectic cutoff. PF-183 handles the infinite collar family automatically once either local route yields the required estimate. The clue resolves only when those local splices assemble to the complete PF-175 hypothesis and yield the density-unitary `S_r`, `r>1`, classification, or when a genuine unavoidable obstruction to that local energy estimate is proved.