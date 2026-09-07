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
  - research/prime_flute/findings/PF-192-generic-strong-L1-geometric-rigidity-fails-at-the-endpoint.md
  - research/prime_flute/findings/PF-194-hamiltonian-reflection-marked-korn-still-fails-in-L1.md
  - research/prime_flute/findings/PF-195-critical-one-sided-weak-S2-localization-is-not-controlled-by-endpoint-mass-alone.md
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

The geometric splice gate has nevertheless become sharper. PF-192 shows that generic strong-`L^1` geometric rigidity fails, and PF-194 shows that even exact Hamiltonian structure, zero flux, reflection marking, boundary identity, and small interior support do not restore a generic linear `L^1` Korn estimate. These are route boundaries rather than counterexamples to the canonical PF splice: an endpoint conservative interpolation must exploit structure beyond generic strong-`L^1` rigidity, or it must be formulated directly in a weak/Lorentz scale.

A targeted prior-art audit of the critical Cwikel--Solomyak theory gives a parallel analytic warning and a possible opening. Solomyak's critical theorem, as revisited and optimized by Sukochev--Zanin, places the symmetrized two-dimensional model

\[
(1-\Delta)^{-1/2}M_f(1-\Delta)^{-1/2}
\]

in weak trace class under the critical Orlicz condition `f in L log L`; Sukochev--Zanin also show that this endpoint scale is optimal within the relevant Orlicz/Lorentz classes. In the PF setting the metric deviation is uniformly bounded under quasi-isometry, so on any measured module finite `L^1` defect implies finite `L log L` defect with comparable size up to the fixed quasi-isometry bound. This does **not** import the torus theorem to the hyperbolic vector-gradient factorization, but it keeps a directly symmetrized endpoint route compatible with the PF-191 mass currency.

PF-195 closes a tempting shortcut inside the alternative half-factor route. Levitina--Sukochev--Zanin prove that bare `L^2` coefficient control does not imply critical one-sided weak `S_2`; their positive weak-`S_2` theorem instead uses a logarithmically weighted local-`L^infinity` coefficient norm. When that standard sufficient norm is fed the PF-191 Lambert profile, it sees scale `O(d_n)` after multiplying the two half-factors rather than the summable `O(d_n/cosh a_n)` integrated mass. Thus a half-factor proof remains possible only through a **PF-specific mass-sensitive/nonconcentration estimate**; it cannot be justified from endpoint `L^1` mass by generic Cwikel theory alone.

The unresolved issue is therefore sharper: prove a uniform critical weak-ideal estimate for the actual localized geometric resolvent form that preserves the PF endpoint mass, and reassemble those estimates without recreating a logarithm through off-diagonal transmission or infinite localization.

## Research question

Can the exact prime/shift first relative resolvent be decomposed into finitely many families of localized body/interface operators whose members are orthogonal or bounded-overlap at the singular-value counting level, plus a trace-class or separately weak-`S_1` reassembly remainder, so that the PF-189/PF-191 endpoint budgets imply

\[
(\Delta_{g_+}+1)^{-1}F_* - F_*(\Delta_g+1)^{-1}\in\mathcal S_{1,\infty}?
\]

The first geometric subgate is now an endpoint version of PF-183's still-missing conservative splice: on each normalized thick transition slab, can the exact-area collar/body interpolation be constructed with cost linear in the local `L^1` body strain plus the already summable core mismatch? PF-191 shows that such a local estimate would sum over the complete family; PF-192/PF-194 show that generic strong-`L^1` rigidity arguments do not prove it.

The second analytic subgate is the critical operator estimate. Once a localized coefficient budget is available, can the gradient part of PF-175's form factorization be placed directly at the weak endpoint rather than reached by `r>1` extrapolation? There are now two genuinely distinct possibilities: prove a PF-specific weak-`S_2` estimate for each critical gradient-resolvent half-factor with quasi-norm controlled by the square root of the **integrated** local endpoint mass, despite PF-195's generic Cwikel boundary; or prove a direct symmetrized weak-`S_1` estimate for the two-sided localized form whose coefficient currency is `L^1`/`L log L` and therefore retains the PF-191 area suppression.

## Why it may matter

A positive answer would identify the natural global endpoint suggested independently by the local two-dimensional pseudodifferential obstruction and by PF-189's complete central sector: weak `S_1` but not `S_1`. It would also show that PF-190's `log^2(n)/n` envelope is an artifact of global strong-Schatten extrapolation rather than a genuine loss created by the full prime/shift geometry.

A negative answer would be equally informative if it exhibits a specific geometric concentration, off-diagonal/interface mechanism, or operator-localization cost that converts summable local critical mass into a larger global singular-value envelope. That would locate the first genuine endpoint obstruction beyond the already-solved central collars and prevent further attempts to remove PF-190's logarithms by interpolation bookkeeping alone.

## Decisive test

First settle the geometric endpoint splice on PF-183's normalized thick slabs. Using PF-191's endpoint body budget, prove or refute a uniform exact-area estimate of the schematic form

\[
E_1(\operatorname{splice}_\eta;T_\eta)
\le
C\left(E_1^{\mathrm{body}}(T_\eta)+|t_\eta|\right)
\]

on both source and inverse/target sides. PF-184--PF-188 provide exact flux and marked branch control, while PF-192--PF-194 rule out treating strong endpoint coercivity as generic background. A failed interpolation is not a negative result; a genuine obstruction must show that no admissible **canonical** marked exact-area splice can satisfy a linear endpoint budget, or identify precisely which stronger PF structure is still missing.

In parallel, prove or refute a uniform localized critical operator estimate on the normalized modules. A sufficient direct prototype is

\[
\|\chi T\chi\|_{\mathcal S_{1,\infty}}^{\#}
\le C\int_{\operatorname{supp}\chi} W\,\delta\,d\mu,
\]

or the corresponding `L log L` estimate, with the bounded PF coefficient used only to compare its Orlicz mass to the persisted local `L^1` budget. The constant must be uniform through the normalized tail geometry; PF-112's pointwise `c/j` asymptotic alone is not enough because it gives no uniform quasi-norm estimate.

A half-factor formulation is still decisive but now has an additional burden from PF-195. If the two gradient-resolvent factors in PF-175 can each be placed uniformly in `S_{2,infinity}` with quasi-norm controlled by the square root of the local endpoint mass, the standard singular-value product inequality gives a weak-`S_1` gradient term without either logarithm. However, **do not infer this estimate from `L^2` coefficient mass alone**. The proof must identify and verify a PF-specific nonconcentration/localization property strong enough to defeat the critical one-sided Cwikel counterexample while retaining the `d_n/cosh(a_n)` Lambert gain. A local-sup criterion that charges the body at order `d_n` is insufficient for global summation.

If either local operator estimate holds, use the disjoint PF-183 transition slabs and a finite-color localization of the remaining body pieces so that counting functions can be summed without a logarithmic overlap penalty. Then derive the resolvent/IMS or Krein reassembly formula explicitly and prove every cross term is trace class, weak `S_1` with summable mass, or absorbed into one of the colored families. The route is killed if the local weak-ideal constant cannot be controlled by the persisted endpoint budget or an unavoidable cross term reproduces a logarithmic loss despite finite overlap.

## Evidence boundary

No global weak-`S_1` theorem is established. PF-191 proves an exact-area **unweighted** `L^1` Lambert/body improvement and, through PF-183's thick-slab weight bound, an endpoint weighted budget on those transition slabs. It does not prove a globally finite inverse-unit-ball weighted defect away from the controlled modules and does not construct the endpoint conservative splice.

PF-189 is an orthogonal central Dirichlet-sector statement, PF-173 treats only matched central recoupling, and PF-190 remains the best persisted full weighted-endpoint resolvent consequence. PF-195 does not prove failure of the actual PF half-factor; it proves only that its desired mass-linear weak-`S_2` bound is not a generic consequence of critical `L^2` coefficient control and that a standard positive local-sup Cwikel criterion loses the project-specific Lambert effective-area gain. The Cwikel--Solomyak results remain nearby flat critical multiplier models and do not automatically transfer to the noncompact hyperbolic vector-gradient factorization or to the actual prime/shift reassembly. The finite-color decomposition, uniform mass-sensitive local endpoint estimate, endpoint collar splice, and control of nonlocal cross terms are all open.

## Research disposition

The clue remains `accepted`. PF-191 removes the most immediate geometric-integrability objection to pursuing the weak endpoint in the exact-area gauge. PF-192/PF-194 show that the strong geometric conversion must be canonical rather than generic, and PF-195 shows the same for a one-sided weak-`S_2` analytic conversion. Meanwhile the symmetrized critical Cwikel--Solomyak theory keeps a mass-sensitive weak-trace model available. None of these facts proves the required hyperbolic/vector-gradient estimate, but together they make the remaining alternatives more precise and falsifiable.

The active test is deliberately split into two gates: **canonical endpoint conservative geometry on the normalized PF-183 slabs**, followed by **mass-sensitive critical weak-ideal localization and no-loss reassembly**. At the analytic gate, direct symmetrized weak-`S_1` control is now the generic prior-art-aligned route; separate weak-`S_2` half-factors require an additional PF-specific nonconcentration theorem.