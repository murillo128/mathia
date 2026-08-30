---
id: CLUE-prime-flute-shift-clone-sharp-schatten-threshold
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-107-shift-clone-cuff-defect-is-l2-not-l1.md
  - research/prime_flute/findings/PF-112-first-relative-resolvent-is-not-trace-class.md
  - research/prime_flute/findings/PF-125-shift-clone-has-compact-relative-resolvent.md
  - research/prime_flute/findings/PF-126-shift-clone-metric-defect-is-Lp-above-one.md
---

# Does the prime/shift relative resolvent have the sharp Schatten threshold `S_r`, `r>1`?

## Observation

PF-112 fixes the **local** microlocal threshold for the first relative resolvent of any non-isometric two-dimensional metric pair: after compact localization its order is `-2`, so the singular-value scale is weak `S_1`; local `S_r` membership is compatible with every `r>1`, while `S_1` is impossible.

PF-125 now supplies the previously missing global ingredient at the compactness level for the exact prime flute and the exact all-composite shift clone `p_n -> p_n+1`. PF-126 strengthens the geometric side further: for the same explicit global marking, the transported metric/density defect lies in weak `L^1` and in every `L^r`, `r>1`. The reciprocal-prime exponent on the coefficient side therefore matches the classical two-dimensional local Schatten exponent unusually closely.

This alignment is not yet operator evidence. The surface has cusps, infinite type, and collapsing injectivity radius, so compact/bounded-geometry pseudodifferential results cannot simply be globalized.

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

PF-112 already proves the second statement. The unresolved content is the positive `S_r`, `r>1`, side (or a precise failure threshold caused by the thin/infinite-type geometry).

## Why it may matter

A positive answer would finish the natural operator-ideal classification between PF-112 and PF-125 and show that even this refined first-resolvent scale is compatible with an exact all-composite control. It would also identify `det_2`/higher modified Fredholm constructions as analytically available candidates while simultaneously warning that their mere existence cannot be prime-specific.

A negative answer for some `r>1` would be more interesting geometrically: it would exhibit a genuine global amplification mechanism caused by cusps, zero-systole regions, or infinite gluing that is invisible both to compact relative resolvent and to the unweighted coefficient integrability of PF-126. Such a mechanism would deserve separate investigation before any arithmetic interpretation.

## Decisive test

A positive resolution must prove a **global** singular-value estimate, not extrapolate from local pseudodifferential order. Viable routes include:

1. use PF-125's explicit Lambert/Fermi charts to build a uniform factorization of the resolvent identity and prove `S_r` summability from PF-126's `L^r` coefficient bound;
2. prove a Cwikel/Birman--Solomyak-type estimate adapted to this particular hyperbolic pants exhaustion without assuming a positive injectivity-radius lower bound;
3. establish the needed heat-kernel/gradient Schatten factors directly, with explicit control through cusp and short-geodesic thin parts.

A decisive negative resolution should construct a lower bound on singular values, or an orthogonal family concentrated in thin regions, showing `A notin S_r` for some `r>1` despite PF-126. Failure of one sufficient theorem is not enough: the obstruction must concern the operator itself.

Any positive ideal result must then be stress-tested against the all-composite nature of `X_+`; membership alone cannot be promoted as an RH mechanism.

## Evidence boundary

Nothing in PF-126 implies Schatten membership by itself. Joachim Toft's Weyl-Hörmander results (`Ann. Global Anal. Geom.` 30 (2006), DOI `10.1007/s10455-006-9027-7`) are representative of standard symbol-`L^p` to Schatten implications, but their global hypotheses are not established for this degenerating infinite-type surface. The compact-manifold Birman--Solomyak theory used in PF-112 only controls localized pieces.

Güneysu--Thalmaier (`Ann. Inst. Fourier` 70 (2020), DOI `10.5802/aif.3316`) show that wave operators for quasi-isometric metrics can be obtained without injectivity-radius assumptions under a weighted heat-kernel/metric-deviation integral criterion. That is useful prior art for the thin-geometry issue but is neither a Schatten theorem nor a consequence of PF-126's unweighted `L^r` estimate.

No directed search located a theorem that directly classifies the first relative resolvent for an infinite-type hyperbolic surface with this combination of cusp degeneration, zero systole, and reciprocal-prime coefficient decay. The conjectured `S_r`, `r>1`, threshold is therefore a falsifiable research target, not a novelty or truth claim.

## Research disposition

The clue is accepted for active investigation because PF-112, PF-125, and PF-126 now isolate a single missing global operator step with a sharp predicted threshold and clear countertests. Acceptance asserts only that the question is mathematically well-posed and worth pursuing; it does not assert `S_r` membership, determinant existence, scattering equivalence, or any RH consequence.