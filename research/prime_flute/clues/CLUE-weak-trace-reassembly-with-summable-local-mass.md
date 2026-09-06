---
id: CLUE-prime-flute-weak-trace-reassembly-with-summable-local-mass
type: research-clue
status: proposed
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-112-first-relative-resolvent-is-not-trace-class.md
  - research/prime_flute/findings/PF-130-lambert-shift-metric-defect-is-strong-L1-summable.md
  - research/prime_flute/findings/PF-173-relative-central-recoupling-is-trace-summable.md
  - research/prime_flute/findings/PF-175-weighted-defect-gives-dual-resolvent-schatten-bridge.md
  - research/prime_flute/findings/PF-183-disjoint-thick-collar-slabs-remove-multiplicity-from-schatten-splice-budget.md
  - research/prime_flute/findings/PF-189-complete-short-collar-central-sector-is-weak-trace-class.md
  - research/prime_flute/findings/PF-190-weighted-endpoint-gives-log-square-resolvent-envelope.md
---

# Can the weak-trace endpoint be recovered by localized reassembly rather than global exponent extrapolation?

## Observation

PF-189 reaches the exact critical ideal `S_{1,infinity}` on the complete fixed-central short-collar sector, and PF-173 makes the matched central recoupling error trace class. PF-190, by contrast, obtains only the global envelope `s_n=O(log^2(n)/n)` when the PF-175 `S_r` estimate is extrapolated as `r->1`; PF-190 already identifies the two gradient half-factor time integrals as the source of the two logarithms.

The remaining geometry has a structure that the global extrapolation does not use. PF-130 gives summable strong-`L^1` metric-defect mass on the isolated Lambert bodies, while PF-183 places every unresolved true-short-collar splice on pairwise disjoint uniformly thick slabs and charges those slabs to the actual body energy. For an orthogonal direct sum, singular-value counting functions add exactly, so a family of local weak-`S_1` pieces with summable counting quasi-norms remains weak `S_1`; adding a trace-class remainder does not change that endpoint.

A targeted prior-art audit of the critical Cwikel--Solomyak theory (Solomyak 1995; Sukochev--Zanin, *Optimal Cwikel--Solomyak Estimates*, JFAA 29 (2023), 21) gives a useful warning and a possible opening. Generic critical symmetrized multiplier estimates naturally use an `L log L` coefficient condition rather than bare `L^1`. But the PF-175 metric deviation is uniformly bounded under quasi-isometry, so on any measured piece finite `L^1` defect automatically gives finite `L log L` defect with comparable size up to the fixed quasi-isometry bound. Thus the known critical Orlicz threshold does not by itself explain PF-190's logarithmic loss. What remains unproved is a uniform local weak-ideal estimate in the actual geometric/vector-gradient setting and a reassembly that does not recreate the loss through nonlocal cross terms.

## Research question

Can the full prime/shift first relative resolvent be decomposed, after the canonical area-preserving comparison is completed, into finitely many families of localized body/interface operators whose members are orthogonal or bounded-overlap at the counting-function level, plus a trace-class or separately weak-`S_1` reassembly remainder, so that the PF-130/PF-183 summable local defect budget implies

\[
(\Delta_{g_+}+1)^{-1}F_* - F_*(\Delta_g+1)^{-1}\in\mathcal S_{1,\infty}?
\]

The point is to test whether PF-190's `log^2(n)/n` envelope is an artifact of global strong-Schatten extrapolation rather than a genuine endpoint loss. This is stronger than the accepted `S_r`, `r>1`, target and remains compatible with PF-112, which forbids ordinary trace class but not weak trace class.

## Why it may matter

A positive answer would identify the natural global endpoint suggested independently by the local two-dimensional pseudodifferential obstruction and by PF-189's complete central sector: weak `S_1` but not `S_1`. It would also isolate any remaining logarithmic loss as a nonlocal reassembly phenomenon rather than a consequence of the collapsing short geometry or of coefficient integrability.

A negative answer would be equally informative if it exhibits a specific off-diagonal/interface mechanism that converts summable local critical mass into a larger global singular-value envelope. That would locate the first genuine endpoint obstruction beyond the already-solved central collars and prevent further attempts to remove PF-190's logarithms by interpolation bookkeeping alone.

## Decisive test

First prove or refute a uniform localized endpoint estimate on the normalized modules already present in PF-130/PF-183. A sufficient prototype is a bound of the form

\[
\|\chi T\chi\|_{\mathcal S_{1,\infty}}^{\#}
\le C\int_{\operatorname{supp}\chi} W\,\delta\,d\mu
\]

for the localized relative first-resolvent contribution, or the corresponding critical `L log L` version with the PF quasi-isometry bound used to reduce it to the same local `L^1` budget. The constant must be uniform through the normalized tail geometry; PF-112's pointwise `c/j` asymptotic alone is not enough because it gives no such uniform quasi-norm estimate.

If that local estimate holds, use the disjoint PF-183 transition slabs and a finite-color localization of the remaining body pieces so that counting functions can be summed without a logarithmic overlap penalty. Then derive the resolvent/IMS or Krein reassembly formula explicitly and prove every cross term is trace class, weak `S_1` with summable mass, or absorbed into one of the colored families. The route is killed if either the local weak-ideal constant cannot be controlled by the persisted local defect budget or an unavoidable cross term reproduces a logarithmic loss despite finite overlap.

## Evidence boundary

No global weak-`S_1` theorem is established. PF-189 is an orthogonal central Dirichlet-sector statement, PF-173 treats only matched central recoupling, and PF-190 remains the best persisted full weighted-endpoint consequence. The Cwikel--Solomyak results cited above concern nearby critical multiplier models and do not automatically transfer to the noncompact hyperbolic vector-gradient factorization or to the actual prime/shift reassembly. The finite-color decomposition, uniform local endpoint estimate, and control of nonlocal cross terms are all open and are precisely what this clue proposes to test.
