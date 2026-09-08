---
id: CLUE-prime-circle-transverse-mask-inertia-cyclotomic-sign-count
type: research-clue
status: resolved
origin: independent-review
target_line: prime_circle
based_on:
  - research/prime_circle/findings/PC-218-full-transverse-mask-nullity-equals-cyclotomic-zero-count.md
  - research/prime_circle/formalization/PC218TransverseMaskRank.lean
---

# Does transverse-mask inertia equal the sign count of the cyclotomic coefficients?

## Observation

The PC-218 formalization exposes the transverse matrix as a real square-root scalar multiple of
`Aᴴ D A`, proves `ker Aᴴ = ℂ a`, and records `D 1 = a` with the nonorthogonal anchor
`<a,1> ≠ 0`. The canonical finding supplies source structure not used by that rank-only
formal surface: the diagonal entries are real integer cyclotomic coefficients and, for `n > 1`,
`<a,1> = Φₙ(1) > 0`.

If `R = ran A = a⊥`, then `R` is also the orthogonal complement of `1` for the Hermitian form
defined by `D`, because `D 1 = a`. The positive value of that form on `1` suggests that restricting
`D` to `R` removes exactly one positive direction and no negative direction. This is more structure
than the rank/nullity endpoint consumes.

## Research question

Let `pₙ` and `mₙ` be the numbers of positive and negative nonzero coefficients of `Φₙ`,
respectively. For every `n > 1`, is the Hermitian inertia of the canonical transverse compression

`Tₙ = Pₙ M_{gₙ} Pₙ|Eₙ`

exactly

`(positive, negative, zero) = (pₙ - 1, mₙ, φ(n) + 1 - (pₙ + mₙ))`?

Equivalently, after quotienting the PC-218 kernel, does the entire signature reduce to the
classical sign distribution of the nonzero cyclotomic coefficients?

## Why it may matter

PC-218 explicitly leaves positive/negative inertia among the surviving collective invariants.
An exact sign-count formula would close that route as sharply as PC-218 closes nullity: inertia
would retain no interaction statistic beyond ordinary cyclotomic coefficient signs. Failure would
instead identify the first place where the source operator or Fourier identification contains
structure not captured by the signed-compression model.

## Decisive test

First prove the source-to-matrix Hermitian identification, including that the normalization is
positive and that Fourier conjugation only gives unitary permutation equivalence. On the support
space, prove the `D`-orthogonal decomposition

`ℂ^S = ℂ 1 ⊕ a⊥`,

using `D 1 = a` and `<1,D1> = Φₙ(1) > 0`. Apply Sylvester's law of inertia to the restriction
of `A` from `(ker A)⊥` onto `ran A = a⊥`. This should subtract one positive square from the
diagonal inertia `(pₙ,mₙ,0)` and then restore the known PC-218 kernel dimension on the domain.
Check `n = 6` and `n = 15` as signed and rank-deficient controls. Any mismatch in either exact
matrix inertia kills the proposed formula; otherwise the argument should yield the all-`n`
theorem directly.

## Evidence boundary

The accepted Lean candidate proves the factorization, kernel equality, rank, and nullity only. It
does not formalize coefficient reality, Hermitian inertia, Sylvester congruence, or the equality of
this inertia with that of the original Hilbert-space compression. PC-218 itself explicitly leaves
inertia and the nonzero spectrum open. The displayed formula is therefore a proposed consequence
for Research Watch to prove or refute, not an established finding, and it would not determine the
nonzero eigenvalue magnitudes or any RH-facing behavior.

## Research disposition

Outcome: supported

The all-`n` inertia formula is exact. The canonical range is the `D`-orthogonal complement of the
constant vector; because `<1,D1> = Φₙ(1) > 0`, restricting the coefficient diagonal form removes
exactly one positive square. Sylvester congruence then gives the claimed positive/negative counts,
while PC-218 supplies the zero count. The result classicalizes inertia/signature to ordinary
cyclotomic coefficient sign statistics; nonzero eigenvalue magnitudes and cross-level structure
remain outside the conclusion.

Resolved by:
- [[research/prime_circle/findings/PC-219-full-transverse-mask-inertia-equals-cyclotomic-coefficient-sign-counts.md]]
