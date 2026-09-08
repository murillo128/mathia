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

No independent cancellation estimate for a commutator readout is established here. MC-157 does, however, settle an important part of the question for every single-prime odd spectral filter, and MC-160 extends exact reconstruction to absolutely summable infinite-prime linear readouts while distinguishing reconstruction from exponent stability. An arbitrary synthetic sequence may refute a claim asserted for all sequences but does not automatically refute a claim restricted to the actual arithmetic source. The accepted mean-absolute clue remains unchanged; this is a specific complementary test, not a new endpoint criterion or authorization to modify tasks or mandates.

## Research disposition

**Accepted, with the conditioning question narrowed away from the canonical single-prime readout.** MC-157 already gives the exact power-transfer test for a single-prime odd filter. For the raw commutator filter `g(t)=t`, its parameters are `a=2` and `c=1`, so the recurrence stability condition `|(c/a)| p^(-theta)<1` holds for every fixed `theta>0`. Recovery uses only the current and downward `p`-dilated scales, so a finite section through height `X` needs no data above `X`. Thus decoder instability is not the missing ingredient for this canonical scalarization.

MC-160 shows that passing to an absolutely summable infinite-prime linear readout preserves exact Mertens recoverability, but its elementary contraction inequalities are only sufficient and do not by themselves decide the full conditioning problem. The live reason to retain the scalar construction is therefore much narrower: produce an **independent arithmetic estimate for one fixed transformed input** whose proof does not already assume the corresponding Mertens bound and whose inversion/truncation losses preserve a meaningful gain. A useful next theorem must state the exact readout and prove such a source estimate; another invertible encoding or another conditioning calculation without a new source bound does not answer the clue.
