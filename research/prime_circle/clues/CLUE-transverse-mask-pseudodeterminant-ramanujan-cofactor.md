---
id: CLUE-prime-circle-transverse-mask-pseudodeterminant-ramanujan-cofactor
type: research-clue
status: proposed
origin: independent-review
target_line: prime_circle
based_on:
  - research/prime_circle/findings/PC-218-full-transverse-mask-nullity-equals-cyclotomic-zero-count.md
  - research/prime_circle/findings/PC-219-full-transverse-mask-inertia-equals-cyclotomic-coefficient-sign-counts.md
  - research/prime_circle/formalization/PC218TransverseMaskRank.lean
  - research/prime_circle/formalization/PC219TransverseMaskInertia.lean
---

# Does the transverse-mask pseudodeterminant reduce to one Ramanujan-frame cofactor?

## Observation

The PC-219 formalization proves the inertia of

`T_n = alpha_n A_n^* D_n A_n`

by replacing the evaluation map with its range and then retaining only the sign of the diagonal
form on that range. This deliberately discards the metric distortion of `A_n`, hence every
nonzero eigenvalue magnitude. The same checked structure is nevertheless rigid enough to isolate
one magnitude-sensitive scalar: `ker(A_n^*)` is the coefficient line `C a`, `D_n 1 = a`, and
`sum a_r = Phi_n(1) > 0`.

Put `B_n = A_n A_n^*`, let `S_n` be the nonzero coefficient support, and delete from `B_n` the
row and column indexed by `phi(n)`. Since the leading cyclotomic coefficient is `1`, the resulting
principal cofactor

`K_n = det (B_n)_(S_n \ {phi(n)})`

is the scalar in the rank-one adjugate of `B_n`. Moreover, the entries of `B_n` are the integer
Ramanujan sums `c_n(r-s)`. Thus the structure forgotten by the inertia proof is not an arbitrary
frame metric but one exact support-selected Ramanujan Gram cofactor.

## Research question

If `det'` is the signed product of the nonzero eigenvalues and
`k_n = |S_n|-1`, is the exact identity

`det'(T_n) = alpha_n^k_n K_n Phi_n(1) prod_(r in S_n) a_n(r)`

valid for every `n > 1`? If so, can `K_n` be evaluated or sharply classified using ordinary
cyclotomic discriminant, resultant, or Ramanujan-minor data? In the dense-support case the same
cofactor should reduce to `|disc(Phi_n)|`; the sparse-support case is the unresolved part that
tests whether the quotient determinant contains anything beyond classical cyclotomic arithmetic.

## Why it may matter

PC-218 classifies the forced zero eigenspace and PC-219 classifies the signs after that kernel is
removed. The proposed identity is a concrete next test of the smallest spectral-magnitude scalar
on the same canonical operator. A closed classical formula for `K_n` would sharply classicalize
the kernel-quotient determinant as well; failure would identify the primitive-root frame volume,
rather than inertia, as the first surviving source-specific quantity.

## Decisive test

Prove the displayed factorization directly from the coefficient of the first nonzero term of the
characteristic polynomial. The nonzero spectra of `A_n^* D_n A_n` and `D_n B_n` agree, while the
rank-`|S_n|-1` adjugate of `B_n` must be a scalar multiple of `a a^*`; evaluating its leading
principal cofactor fixes that scalar as `K_n`. This either gives the formula or exposes its exact
failure.

Then compute `K_n` from the exact Ramanujan matrix for sparse controls such as `n=12` and `n=15`
and compare it with the dense-support discriminant identity. Kill the direction if the cofactor is
already an immediate standard discriminant/resultant specialization with no residual arithmetic
question, or if matched non-cyclotomic support/Gram controls show that the proposed factor carries
no source-specific content.

## Evidence boundary

The accepted Lean file does not define a signed pseudodeterminant, prove the adjugate/cofactor
factorization, evaluate `K_n`, or restore the source Hilbert-space compression omitted from the
finite matrix bridge. PC-219 proves only inertia/signature, and the generic rank-one adjugate step
is classical linear algebra. The displayed identity and the proposed cyclotomic classification of
the sparse Ramanujan cofactor therefore remain an unvalidated research lead, not a theorem,
novelty claim, full nonzero-spectrum classification, or RH-facing consequence.
