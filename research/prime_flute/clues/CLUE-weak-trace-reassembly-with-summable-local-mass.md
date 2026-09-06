---
id: CLUE-prime-flute-weak-trace-reassembly-with-summable-local-mass
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-112-first-relative-resolvent-is-not-trace-class.md
  - research/prime_flute/findings/PF-173-relative-central-recoupling-is-trace-summable.md
  - research/prime_flute/findings/PF-175-weighted-defect-gives-dual-resolvent-schatten-bridge.md
  - research/prime_flute/findings/PF-183-disjoint-thick-collar-slabs-remove-multiplicity-from-schatten-splice-budget.md
  - research/prime_flute/findings/PF-189-complete-short-collar-central-sector-is-weak-trace-class.md
  - research/prime_flute/findings/PF-190-weighted-endpoint-gives-log-square-resolvent-envelope.md
  - research/prime_flute/findings/PF-191-exact-area-lambert-transport-retains-suppressed-strong-L1-endpoint.md
---

# Can the weak-trace endpoint be recovered by localized reassembly rather than global exponent extrapolation?

## Observation

PF-189 reaches the exact critical ideal `S_{1,infinity}` on the complete fixed-central short-collar sector, and PF-173 makes the matched central recoupling error trace class. PF-190, by contrast, obtains only the global envelope `s_n=O(log^2(n)/n)` when the PF-175 `S_r` estimate is extrapolated as `r->1`; PF-190 already identifies the two gradient half-factor time integrals as the source of the two logarithms.

The endpoint geometry is now stronger than the version that originally motivated this clue. PF-191 sharpens PF-179's **exact area-preserving** Lambert transport from the coarse `O(d_n)` one-body `L^1` estimate to

\[
\int_{Q(a_n)}\delta\,d\mu
\le C\frac{d_n}{\cosh a_n},
\]

and proves that these masses are summable for the exact prime/shift family. Combining that with the already summable endpoint corrections in PF-180--PF-182 upgrades PF-183's assembled body stage to finite unweighted `L^1` defect. PF-183's true-short-collar transition slabs are pairwise disjoint and uniformly thick, so their **weighted** body defect is also summable at `r=1`. Thus the earlier concern that exact area preservation itself destroys the Lambert `L^1` gain is removed.

A targeted prior-art audit of the critical Cwikel--Solomyak theory gives a useful warning and a possible opening. Solomyak's critical theorem, as revisited and optimized by Sukochev--Zanin, places the symmetrized two-dimensional model

\[
(1-\Delta)^{-1/2}M_f(1-\Delta)^{-1/2}
\]

in weak trace class under the critical Orlicz condition `f in L log L`; Sukochev--Zanin also show that this endpoint scale is optimal within the relevant Orlicz/Lorentz classes. In the PF setting the metric deviation is uniformly bounded under quasi-isometry, so on any measured module finite `L^1` defect implies finite `L log L` defect with comparable size up to the fixed quasi-isometry bound. This does **not** import the torus theorem to the hyperbolic vector-gradient factorization, but it removes bare coefficient integrability as an obvious generic reason for PF-190's logarithmic loss.

The unresolved issue is therefore sharper: prove a uniform critical weak-ideal estimate for the actual localized geometric resolvent factors and reassemble those estimates without recreating a logarithm through off-diagonal transmission or infinite localization.

## Research question

Can the exact prime/shift first relative resolvent be decomposed into finitely many families of localized body/interface operators whose members are orthogonal or bounded-overlap at the singular-value counting level, plus a trace-class or separately weak-`S_1` reassembly remainder, so that the PF-189/PF-191 endpoint budgets imply

\[
(\Delta_{g_+}+1)^{-1}F_* - F_*(\Delta_g+1)^{-1}\in\mathcal S_{1,\infty}?
\]

The first geometric subgate is now an endpoint version of PF-183's still-missing conservative splice: on each normalized thick transition slab, can the exact-area collar/body interpolation be constructed with cost linear in the local `L^1` body strain plus the already summable core mismatch? PF-191 shows that such a local estimate would sum over the complete family; it does not prove the estimate itself.

The second analytic subgate is the critical operator estimate. Once a localized coefficient budget is available, can the gradient part of PF-175's form factorization be placed directly at the weak endpoint rather than reached by `r>1` extrapolation? Equivalently, can one prove a project-appropriate weak-`S_2` estimate for each critical gradient-resolvent half-factor, or a direct symmetrized weak-`S_1` estimate for the two-sided localized form, with constants controlled by the same local endpoint mass?

## Why it may matter

A positive answer would identify the natural global endpoint suggested independently by the local two-dimensional pseudodifferential obstruction and by PF-189's complete central sector: weak `S_1` but not `S_1`. It would also show that PF-190's `log^2(n)/n` envelope is an artifact of global strong-Schatten extrapolation rather than a genuine loss created by the full prime/shift geometry.

A negative answer would be equally informative if it exhibits a specific off-diagonal/interface mechanism that converts summable local critical mass into a larger global singular-value envelope. That would locate the first genuine endpoint obstruction beyond the already-solved central collars and prevent further attempts to remove PF-190's logarithms by interpolation bookkeeping alone.

## Decisive test

First settle the geometric endpoint splice on PF-183's normalized thick slabs. Using PF-191's endpoint body budget, prove or refute a uniform exact-area estimate of the schematic form

\[
E_1(\operatorname{splice}_\eta;T_\eta)
\le
C\left(E_1^{\mathrm{body}}(T_\eta)+|t_\eta|\right)
\]

on both source and inverse/target sides. PF-184--PF-188 remain the relevant local constraints: exact flux and marked branch selection are available, but no energy-linear endpoint Sobolev/exact-symplectic cutoff theorem is established. A failed interpolation is not a negative result; a genuine obstruction must show that no admissible marked exact-area splice can satisfy a linear endpoint budget.

In parallel, prove or refute a uniform localized critical operator estimate on the normalized modules. A sufficient prototype is

\[
\|\chi T\chi\|_{\mathcal S_{1,\infty}}^{\#}
\le C\int_{\operatorname{supp}\chi} W\,\delta\,d\mu,
\]

or the corresponding `L log L` estimate, with the bounded PF coefficient used only to compare its Orlicz mass to the persisted local `L^1` budget. The constant must be uniform through the normalized tail geometry; PF-112's pointwise `c/j` asymptotic alone is not enough because it gives no uniform quasi-norm estimate.

A half-factor formulation is equally decisive. If the two gradient-resolvent factors in PF-175 can each be placed uniformly in `S_{2,infinity}` with quasi-norm controlled by the square root of the local endpoint mass, the standard singular-value product inequality gives a weak-`S_1` gradient term without either logarithm. The scalar term is already below that difficulty. This implication is elementary ideal calculus; the unresolved content is the **uniform geometric weak-`S_2` bound**.

If the local estimate holds, use the disjoint PF-183 transition slabs and a finite-color localization of the remaining body pieces so that counting functions can be summed without a logarithmic overlap penalty. Then derive the resolvent/IMS or Krein reassembly formula explicitly and prove every cross term is trace class, weak `S_1` with summable mass, or absorbed into one of the colored families. The route is killed if the local weak-ideal constant cannot be controlled by the persisted endpoint budget or an unavoidable cross term reproduces a logarithmic loss despite finite overlap.

## Evidence boundary

No global weak-`S_1` theorem is established. PF-191 proves an exact-area **unweighted** `L^1` Lambert/body improvement and, through PF-183's thick-slab weight bound, an endpoint weighted budget on those transition slabs. It does not prove a globally finite inverse-unit-ball weighted defect away from the controlled modules and does not construct the endpoint conservative splice.

PF-189 is an orthogonal central Dirichlet-sector statement, PF-173 treats only matched central recoupling, and PF-190 remains the best persisted full weighted-endpoint resolvent consequence. The Cwikel--Solomyak results are nearby critical multiplier models and do not automatically transfer to the noncompact hyperbolic vector-gradient factorization or to the actual prime/shift reassembly. The finite-color decomposition, uniform local endpoint estimate, endpoint collar splice, and control of nonlocal cross terms are all open.

## Research disposition

The clue is `accepted`. PF-191 removes the most immediate geometric-integrability objection to pursuing the weak endpoint in the exact-area gauge, while the critical Cwikel--Solomyak audit shows that bounded `L^1` coefficient mass is compatible with weak trace behavior in the closest standard two-dimensional symmetrized model. Neither fact proves the required hyperbolic/vector-gradient estimate, so acceptance asserts only that the route is now precise, non-duplicative, and worth active investigation.

The active test is deliberately split into two falsifiable gates: **endpoint conservative geometry on the normalized PF-183 slabs**, followed by **uniform critical weak-ideal localization and no-loss reassembly**. Failure of either gate should be persisted as the corresponding obstruction rather than compensated by another `r>1` extrapolation.