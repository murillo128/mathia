---
id: CLUE-mobius-cancellation-commutator-decoder-stability-versus-reencoding
type: research-clue
status: accepted
origin: master-researcher
target_line: mobius_cancellation
based_on:
  - research/mobius_cancellation/clues/CLUE-mean-absolute-mertens-transfer-budget.md
  - research/mobius_cancellation/findings/MC-157-single-prime-commutator-spectral-filter-top-mode.md
  - research/mobius_cancellation/findings/MC-160-infinite-prime-linear-commutator-mertens-completeness.md
  - research/mobius_cancellation/findings/MC-161-tail-centered-prime-commutator-charge.md
  - research/README.md
---

# Does a Mertens-complete commutator reading yield a stable, independently estimable transfer?

## Observation

The accepted mean-absolute transfer clue identifies the target D_M(X)=X^(-1) integral_1^X |M(x)| dx and the need for source-side amplitude control. The current global snapshot reports MC-159/MC-160's sharper scalar boundary: finite scalarizations lose orientation, while nonzero absolutely summable infinite-prime readings can be Mertens-complete through a triangular decoder.

The user requested independent feedback on a suggestion to stop producing further scalar encodings and concentrate on a quantitative advantage. Exact invertibility is not itself circular reasoning or evidence of uselessness: useful transforms can be invertible. The unproved issue is whether this transform makes the needed estimate independently easier after inversion and truncation losses are included.

## Research question

For one explicit reading and decoder from the current local commutator construction, is there a weighted input/output norm pair in which the finite-section inverse and the infinite-prime truncation tail have controlled losses, and in which the actual arithmetic input admits an estimate not obtained by assuming the desired Mertens bound?

This is narrower than the accepted general search for any source-natural endpoint statistic. It tests whether the existing linear construction has an analytic advantage before discarding it in favor of an unspecified nonlinear or noncommutative replacement.

## Why it may matter

A stable transfer combined with an independent source estimate, even on a rigorously stated weaker exponent or restricted regime, would be concrete counterevidence to the suggested redirection. Conversely, an exact inverse-loss obstruction for the selected family would explain why its apparent gain does not reach the endpoint, without declaring all invertible representations unproductive.

## Decisive test

Reconstruct the current local MC-160 statement and its proof and review status; the global snapshot is not an independent verification. Fix the reading, coefficient class, scale, and norm before deriving bounds. Write the decoder's finite-section estimate and its truncation error with all dependence on scale, coefficient support, and weights. Separate three obligations: algebraic recovery, stability of recovery, and an independently proved arithmetic estimate for the transformed input.

Either exhibit a regime in which the last two obligations produce a genuine quantitative improvement over the available direct bound, or construct an admissible family showing that the proposed norm estimate necessarily loses that improvement. Restoring all exceptional-set, smoothing, and scale losses is part of this test. Merely rewriting an RH-equivalent bound as a norm of the encoded target is not an independent input; numerical conditioning on fixed sections does not establish uniform stability.

In the normal research disposition, give the strongest argument for retaining the scalar construction, changing to a specified alternative, or narrowing the line. State one exact inequality or counterexample that would change that assessment and, if useful, the precise analytic lemma another researcher could supply. Do not request generic cancellation without its sum, weights, range, and quantifiers. The Master can consume this local disposition directly.

## Evidence boundary

No independent cancellation estimate for a commutator readout is established here. MC-157 does, however, settle an important part of the question for every single-prime odd spectral filter, and MC-160 extends exact reconstruction to absolutely summable infinite-prime linear readouts while distinguishing reconstruction from exponent stability. MC-161 now supplies a complementary nonsummable calibration: after quotienting the eventual constant prime tail, the unit coordinate charge is the classical `mu(n) omega(n)` transform, whose summatory function has an independent Selberg--Delange asymptotic, but whose exact prime-power decoder is power-unstable throughout `0<theta<=1`. An arbitrary synthetic sequence may refute a claim asserted for all sequences but does not automatically refute a claim restricted to the actual arithmetic source. The accepted mean-absolute clue remains unchanged; this is a specific complementary test, not a new endpoint criterion or authorization to modify tasks or mandates.

## Research disposition

**Accepted, now with a concrete source-estimate/stability tradeoff.** MC-157 gives the exact power-transfer test for a single-prime odd filter. For the raw commutator filter `g(t)=t`, its parameters are `a=2` and `c=1`, so the recurrence stability condition `|(c/a)| p^(-theta)<1` holds for every fixed `theta>0`. Recovery uses only the current and downward `p`-dilated scales, so a finite section through height `X` needs no data above `X`. Decoder instability is therefore not the missing ingredient for this canonical scalarization, but no independent arithmetic estimate for that readout is known.

MC-160 shows that passing to an absolutely summable infinite-prime linear readout preserves exact Mertens recoverability; its elementary contraction inequalities are sufficient stability conditions but supply no new arithmetic source bound. MC-161 tests the opposite corner. Tail-centering makes arbitrary algebraic prime weights legitimate, and the unit weight gives the classical source `F(x)=sum_(n<=x) mu(n) omega(n)`, for which the independent unconditional estimate `F(x)=x/log^2 x+O(x/log^3 x)` is known. Yet the exact decoder has absolute tail factor

`1/(2^theta-1) + 2^theta sum_(p>2) 1/(p^theta-1)`,

which diverges for every `0<theta<=1`; moreover the source itself has power exponent one. Thus **independent estimability by itself is not the missing certificate**: the quantitative gain can be lost entirely in the inverse prime-power tail.

The live scalar question is now precise. Find one fixed nonzero transformed input, preferably within the tail-centered weight family of MC-161 or a comparably explicit alternative, for which both obligations hold at the same target-range exponent: (i) an arithmetic theorem proving `F_w(x)=O(x^theta)` without assuming the corresponding Mertens bound, and (ii) either the explicit MC-161 inverse factor

`eta_(theta,q)(w) = |w_q|^(-1) [ |w_q|/(q^theta-1) + q^theta sum_(p>q) |w_p|/(p^theta-1) ] < 1`

or a rigorously stronger signed Möbius-specific substitute controlling that inverse tail. A candidate that supplies only another exact encoding, only conditioning, or only an exponent-one/logarithmic source asymptotic does not answer the clue. A fixed weight and `theta` meeting both obligations would materially change the current assessment and justify retaining the scalar route.