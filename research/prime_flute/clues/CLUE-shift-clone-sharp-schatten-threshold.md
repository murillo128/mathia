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
  - research/prime_flute/findings/PF-147-square-resolvent-S1-forces-first-resolvent-S2.md
  - research/prime_flute/findings/PF-150-square-resolvent-S1-is-sharp-at-S2-without-geometry.md
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

PF-130 removes a second coarse obstruction on the coefficient side. For the explicit one-parameter Lambert comparison already constructed in PF-121, the actual strong-`L^1` metric/density mass is not `O(delta_n)` over a fixed pant area but

\[
O\!\left(\frac{\delta_n}{\sinh a_n}\right),
\]

and these masses are summable over the exact prime/shift sequence. Thus PF-126's weak-`L^1` endpoint cannot be treated as an intrinsic divergence of the isolated Lambert bodies. The unresolved issue is the genuinely global operator assembly: boundary-coherent pant maps, collar/body interfaces and commutators, noncanonical thin word classes, and infinite summation.

PF-147 adds a **conditional intermediate gate**. If the global PF-146 operator program succeeds in proving

\[
(\Delta_{g_+}+1)^{-2}-(\Delta_g+1)^{-2}\in\mathcal S_1,
\]

then the classical Powers--Størmer/Birman--Koplienko--Solomyak square-root ideal inequality forces the first relative resolvent into `S_2`; PF-112 simultaneously keeps it out of `S_1`. Hence that stronger squared-resolvent gate would settle this clue at `r=2` and, by ideal inclusion, for every `r>=2`.

PF-150 makes the remaining boundary sharp: **no abstract functional-calculus argument from the squared-resolvent `S_1` hypothesis can cross below exponent `2`**. Its explicit commuting diagonal resolvent pair satisfies the square gate while the first difference lies in `S_2` and in no `S_r`, `r<2`. Therefore the interval `1<r<2` is now known to require genuinely additional prime-flute geometry or differential/operator structure; it is not a missing generic consequence of PF-146/PF-147.

This alignment is still not operator evidence for the complete surface. The surface has cusps, infinite type, and collapsing injectivity radius, and the existing local/body estimates do not by themselves control the uncut global operator. Compact/bounded-geometry pseudodifferential results therefore cannot simply be globalized.

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

PF-112 proves the second statement. The unresolved content is the positive `S_r`, `r>1`, side. PF-147 and PF-150 split that positive side cleanly: a proof of the global PF-146 squared-resolvent `S_1` gate would automatically give `A in S_2` and hence `A in S_r` for all `r>=2`, while **every exponent `1<r<2` requires an additional surface-specific estimate** not implied by that gate.

## Why it may matter

A positive answer would finish the natural operator-ideal classification between PF-112 and PF-125 and show that even this refined first-resolvent scale is compatible with an exact all-composite control. PF-147 also clarifies the determinant consequence: once `A in S_2` is actually proved, a natural modified Fredholm `det_2`/Koplienko bounded-resolvent construction becomes available while an ordinary trace-class determinant remains impossible. The existence of such a regularized determinant would still not be prime-specific, and Hilbert--Schmidt membership alone does not guarantee the boundary values needed for a scattering phase.

A negative answer for some `r>1` would have to exhibit a genuine global amplification mechanism caused by boundary synchronization, interfaces, remaining thin channels, or infinite gluing that is invisible to compact relative resolvent and to the existing local collar/body estimates. Such a mechanism would deserve separate investigation before any arithmetic interpretation.

## Decisive test

A positive resolution must prove a **global** singular-value estimate, not extrapolate from local pseudodifferential order, PF-127's isolated collars, PF-130's coefficient integral, or the abstract square gate. Two complementary routes are precise:

1. prove the stronger global PF-146 gate
   \[
   (\Delta_{g_+}+1)^{-2}-(\Delta_g+1)^{-2}\in\mathcal S_1;
   \]
   PF-147 then supplies `A in S_2`, settling the whole range `r>=2`; PF-150 proves that this route alone cannot settle any exponent `1<r<2`;
2. attack the first relative resolvent directly with genuinely geometric input, for example by a boundary-coherent IMS/resolvent decomposition, a Cwikel/Birman--Solomyak estimate adapted to this pants exhaustion, or heat-kernel/gradient Schatten factors with uniform control through the cusp and zero-systole geometry.

A decisive negative resolution should construct a lower bound on singular values, or an orthogonal family concentrated in a **remaining global/interface channel**, showing `A notin S_r` for some `r>1` despite PF-127/PF-130 and the later geometric interface controls. Concentration solely in the central part of canonical collapsing collars is no longer a viable counterexample, and neither is a lower bound obtained solely by assigning order-`1/p_n` distortion to an order-one isolated Lambert body. Failure of one sufficient theorem is still not enough: the obstruction must concern the operator itself.

Any positive ideal result must then be stress-tested against the all-composite nature of `X_+`; membership alone cannot be promoted as an RH mechanism.

## Evidence boundary

PF-126 does not imply Schatten membership by itself. PF-127 proves only a Dirichlet model estimate on fixed central collars. PF-130 proves a strong-`L^1` coefficient estimate only for the independent PF-121 Lambert comparisons and does not by itself control the complete operator's gluing/commutator terms or infinite sum.

PF-147 is an exact **conditional implication**, not evidence that the actual global first relative resolvent is Hilbert--Schmidt. Its hypothesis is the still-open global PF-146 squared-resolvent `S_1` statement; PF-146 currently proves only a fixed-central-collar trace-class estimate for that resolvent power. PF-150 is likewise a boundary theorem, not evidence against the actual prime/shift pair: it proves only that the square gate cannot abstractly force `S_r` below `2`. Accordingly, neither `A in S_2` nor any `A in S_r`, `1<r<2`, is established for the full surface.

Joachim Toft's Weyl-Hörmander results (`Ann. Global Anal. Geom.` 30 (2006), DOI `10.1007/s10455-006-9027-7`) are representative of standard symbol-`L^p` to Schatten implications, but their global hypotheses are not established for this degenerating infinite-type surface. The compact-manifold Birman--Solomyak theory used in PF-112 only controls localized pieces.

Güneysu--Thalmaier (`Ann. Inst. Fourier` 70 (2020), DOI `10.5802/aif.3316`) show that wave operators for quasi-isometric metrics can be obtained without injectivity-radius assumptions under a weighted heat-kernel/metric-deviation integral criterion. That is useful prior art for the thin-geometry issue but is neither a Schatten theorem nor a substitute for the global operator estimates required here.

A renewed directed audit found classical Schatten estimates for resolvent-power differences of elliptic realizations, including Behrndt--Langer--Lotoreichik (`J. London Math. Soc.` 88 (2013), DOI `10.1112/jlms/jdt012`), but those results concern boundary-condition perturbations on smooth Euclidean domains and do not directly globalize the metric-perturbation problem on this zero-systole infinite-type surface. No theorem located in the bounded audit directly settles the actual prime/shift first-resolvent threshold. Search absence is not a novelty claim.

## Research disposition

The clue remains `accepted`. PF-150 materially sharpens the open problem: the global PF-146 squared-resolvent `S_1` gate, if proved, can settle only the `r>=2` half through PF-147; **the entire interval `1<r<2` is now certified to require additional prime-flute-specific structure**. The next decisive work must therefore either prove a direct geometric singular-value estimate crossing below `2`, or exhibit a genuine body/interface/infinite-assembly channel that prevents such membership. Acceptance asserts only that this operator classification remains mathematically well-posed and worth active investigation; it does not assert Schatten membership, determinant existence on the actual surface, scattering equivalence, or any RH consequence.
