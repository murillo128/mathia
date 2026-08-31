---
id: CLUE-prime-flute-shift-clone-sharp-schatten-threshold
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-107-shift-clone-cuff-defect-is-l2-not-l1.md
  - research/prime_flute/findings/PF-109-shift-clone-preserves-canonical-separator-pinching-multiplicatively.md
  - research/prime_flute/findings/PF-112-first-relative-resolvent-is-not-trace-class.md
  - research/prime_flute/findings/PF-125-shift-clone-has-compact-relative-resolvent.md
  - research/prime_flute/findings/PF-126-shift-clone-metric-defect-is-Lp-above-one.md
  - research/prime_flute/findings/PF-127-collapsing-canonical-collar-is-schatten-benign-above-trace-endpoint.md
  - research/prime_flute/findings/PF-130-lambert-shift-metric-defect-is-strong-L1-summable.md
---

# Does the prime/shift relative resolvent have the sharp Schatten threshold `S_r`, `r>1`?

## Observation

PF-112 fixes the **local** microlocal threshold for the first relative resolvent of any non-isometric two-dimensional metric pair: after compact localization its order is `-2`, so the singular-value scale is weak `S_1`; local `S_r` membership is compatible with every `r>1`, while `S_1` is impossible.

PF-125 supplies the global compactness gate for the exact prime flute and the exact all-composite shift clone `p_n -> p_n+1`. PF-126 strengthens the coefficient side: for the same explicit global marking, the transported metric/density defect lies in weak `L^1` and in every `L^r`, `r>1`. The reciprocal-prime exponent on the coefficient side therefore matches the classical two-dimensional local Schatten exponent unusually closely.

PF-127 removes one specific feared thin-geometry obstruction. On a fixed central Dirichlet collar around any matched PF-004 canonical separator, the transverse constant collapse mode is exactly independent of the core length and cancels from the relative resolvent. For every `r>1`, the remaining Fourier modes satisfy

\[
\|A_{L,L'}^{(R)}\|_{\mathcal S_r}^r
\le C_{R,r}|\log(L'/L)|^r L^{2r-1}.
\]

Combined with PF-109, the central-collar contribution tends to zero along every canonical prime/shift pinching sequence. Thus loss of injectivity radius by itself is not a counterexample to the conjectured global `S_r` classification.

PF-130 now removes a second coarse obstruction on the coefficient side. For the explicit one-parameter Lambert comparison already constructed in PF-121, the actual strong-`L^1` metric/density mass is not `O(delta_n)` over a fixed pant area but

\[
O\!\left(\frac{\delta_n}{\sinh a_n}\right),
\]

and these masses are summable over the exact prime/shift sequence. Thus PF-126's weak-`L^1` endpoint cannot be treated as an intrinsic divergence of the isolated Lambert bodies. The unresolved issue is the genuinely global operator assembly: boundary-coherent pant maps, collar/body interfaces and commutators, noncanonical thin word classes, and infinite summation.

This alignment is still not operator evidence for the complete surface. The surface has cusps, infinite type, and collapsing injectivity radius, and PF-130's maps are independent Lambert-piece comparisons rather than one globally coherent marking. Compact/bounded-geometry pseudodifferential results therefore cannot simply be globalized.

## Research question

For the common-manifold Laplacians associated with the PF-125 marking, does

\[
A
:=
(\Delta_{g_+}+1)^{-1}
-
(\Delta_g+1)^{-1}
\]

satisfy the sharp global ideal classification

\[
\boxed{
A\in\mathcal S_r\quad\text{for every }r>1,
\qquad
A\notin\mathcal S_1?
}
\]

PF-112 proves the second statement. The unresolved content is the positive `S_r`, `r>1`, side (or a precise global failure threshold caused by interface/infinite-type effects not already eliminated by PF-127's isolated collar model and PF-130's isolated Lambert-body estimate).

## Why it may matter

A positive answer would finish the natural operator-ideal classification between PF-112 and PF-125 and show that even this refined first-resolvent scale is compatible with an exact all-composite control. It would also identify `det_2`/higher modified Fredholm constructions as analytically available candidates while simultaneously warning that their mere existence cannot be prime-specific.

A negative answer for some `r>1` would now be more geometrically specific than the original clue allowed: it would have to exhibit a genuine global amplification mechanism caused by boundary synchronization, interfaces, noncanonical thin channels, or infinite gluing that is invisible to compact relative resolvent, to PF-127's exact central-collar decomposition, and to PF-130's summable isolated Lambert-body coefficient mass. Such a mechanism would deserve separate investigation before any arithmetic interpretation.

## Decisive test

A positive resolution must prove a **global** singular-value estimate, not extrapolate from local pseudodifferential order, PF-127's isolated collars, or PF-130's coefficient integral. Viable routes now include:

1. build boundary-coherent versions of the PF-121/PF-130 Lambert maps and combine them with PF-127's collar estimate in an IMS/partition decomposition whose pant-body and collar-interface `S_r` norms are summable;
2. prove a Cwikel/Birman--Solomyak-type estimate adapted to this particular hyperbolic pants exhaustion without assuming a positive injectivity-radius lower bound, using the exact deep-cusp isometries and the collapse-mode cancellation where necessary;
3. establish the needed heat-kernel/gradient Schatten factors directly, with explicit control of the overlap and commutator terms across cusp and short-geodesic thin parts.

A decisive negative resolution should construct a lower bound on singular values, or an orthogonal family concentrated in a **remaining global/interface channel**, showing `A notin S_r` for some `r>1` despite PF-127 and PF-130. Concentration solely in the central part of canonical collapsing collars is no longer a viable counterexample, and neither is a lower bound obtained solely by assigning order-`1/p_n` distortion to an order-one isolated Lambert body. Failure of one sufficient theorem is still not enough: the obstruction must concern the operator itself.

Any positive ideal result must then be stress-tested against the all-composite nature of `X_+`; membership alone cannot be promoted as an RH mechanism.

## Evidence boundary

PF-126 does not imply Schatten membership by itself. PF-127 proves only a Dirichlet model estimate on fixed central collars. PF-130 proves a strong-`L^1` coefficient estimate only for the independent PF-121 Lambert comparisons and does not show that the same estimate survives the exact split-ray/cuff/cusp traces required by a complete global marking. None of these controls the complete operator's gluing/commutator terms or the infinite sum over the whole surface.

Joachim Toft's Weyl-Hörmander results (`Ann. Global Anal. Geom.` 30 (2006), DOI `10.1007/s10455-006-9027-7`) are representative of standard symbol-`L^p` to Schatten implications, but their global hypotheses are not established for this degenerating infinite-type surface. The compact-manifold Birman--Solomyak theory used in PF-112 only controls localized pieces.

Güneysu--Thalmaier (`Ann. Inst. Fourier` 70 (2020), DOI `10.5802/aif.3316`) show that wave operators for quasi-isometric metrics can be obtained without injectivity-radius assumptions under a weighted heat-kernel/metric-deviation integral criterion. That is useful prior art for the thin-geometry issue but is neither a Schatten theorem nor a consequence of PF-130's unweighted local `L^1` estimate. Their lower-Ricci specialization weights the metric deviation by the inverse volume of a unit ball, underscoring why a genuine global estimate must still treat the collapsing geometry.

Directed searches located the classical literature on degenerating hyperbolic collars/eigenvalues and general heat-kernel/Cwikel estimates, but no theorem that directly classifies the first relative resolvent for an infinite-type hyperbolic surface with this combination of cusp degeneration, zero systole, reciprocal-prime coefficient decay, and exact deep-cusp matching. The conjectured `S_r`, `r>1`, threshold therefore remains a falsifiable research target, not a novelty or truth claim.

## Research disposition

The clue remains accepted for active investigation. PF-127 and PF-130 materially narrow its negative side: canonical central-collar collapse is `S_r`-benign for every `r>1`, and the isolated Lambert bodies admit a summable strong-`L^1` coefficient budget. The next decisive work must therefore control or expose the **boundary/interface/noncanonical-thin/infinite-assembly** contribution at the operator level. Acceptance asserts only that the global question is mathematically well-posed and worth pursuing; it does not assert `S_r` membership, determinant existence, scattering equivalence, or any RH consequence.
