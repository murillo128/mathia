# MI-016 — Finite-radius localization makes the missing source term explicit

**Evidence level:** supported

## Core intuition

Bombieri's finite negative matrices are not the only exact way a hypothetical off-line zero can become finitely visible. Localized Weil theory moves the obstruction to the source side: RH failure forces a finite support radius where the completed Weil operator crosses zero, with only finitely many von Mangoldt coefficients entering at that radius.

The later controls show that the value of this localization is not generic first-crossing geometry. The universal logarithmic core crosses zero by itself, and even the full gamma-plus-pole form with the prime source deleted develops unbounded negative index. The missing finite-radius theorem is therefore specifically about **von-Mangoldt compensation in the completed form**.

## Strongest justified claim

WI-236 shows that Bombieri finite truncations detect finite off-line packets but a cofinal negative eigensequence may collapse toward zero and lose height tightness. WI-237 shows that generic interval-exponential separation cannot prevent this: simple critical-line exponentials are complete and non-Bessel on bounded windows, leaving an eigenvector-specific coefficient-budget problem.

WI-238 supplies an independent source-side route. At every radius `a`, Suzuki's localized completed Weil form is represented by a discrete-spectrum self-adjoint operator and uses prime data only up to `n<=exp(2a)`. RH failure therefore yields a finite-radius zero/negative mode without taking a zero-side eigenvector limit.

WI-239 shows that continuity, support nesting, compact resolvent, parity, the universal logarithmic singularity, and even an attained simple first zero mode are not enough. For the pure logarithmic core, dilation gives the exact spectral law

`lambda_{0,k}(a)=mu_k-1-log a`,

so every eigenvalue crosses zero at a finite radius.

WI-240 restores all non-prime zeta terms while deleting only the von Mangoldt contribution. In the odd sector the gamma-plus-pole form has negative index tending to infinity with the radius. The pole part is nonpositive there, and scaled finite-dimensional odd spaces see the negative zero-frequency gamma multiplier. Hence the prime term is not a perturbative decoration: if the full form is nonnegative, its signed contribution must compensate an increasingly large negative non-prime sector.

## Synthesis of evidence

The two main routes now expose sharply different currencies. Bombieri starts from the zero divisor and needs coefficient cost/tightness. Suzuki localization starts from a finite source window and avoids that passage to the limit, but WI-239--WI-240 eliminate generic spectral geometry as the reason positivity might hold. The source-side problem has been reduced to the actual arithmetic prime term relative to a strongly indefinite completed background.

A useful finite-radius advance should therefore identify how the finite collection of von Mangoldt translation/autocorrelation terms controls the dangerous negative subspaces, or derive a prime-specific nondegeneracy invariant. Proving another abstract property shared by the prime-deleted countermodel cannot close the gate.

## Counterevidence / boundary cases

WI-240 does not say the von Mangoldt term is positive semidefinite, nor that its compensation can be checked event by event. The full sign may depend on interference among many prime-power translations and the background completion.

Suzuki's all-radius nondegeneracy remains RH-equivalent. Finite-prime locality narrows the input, but the localized operator remains analytically infinite-dimensional. The Bombieri coefficient-budget route also remains logically independent and may still be useful.

## Epistemic status

**Supported structural redirect plus decisive matched controls:** RH failure has a finite-radius source-side manifestation, but the logarithmic core and the complete prime-deleted non-prime form already exhibit the generic crossing/negative-inertia phenomena. The missing finite-radius currency is zeta-specific von-Mangoldt compensation.

## Novelty/prior-art status

Suzuki/Yoshida localization, logarithmic-form structure, gamma/pole formulas, and related operator ingredients retain the prior-art boundaries recorded in WI-238--WI-240. This intuition is a synthesis.

## Falsification criterion

Show that the prime-deleted form of WI-240 does not have the stated unbounded odd negative index, or that the finite-radius full operator requires prime data beyond `exp(2a)`. Strategically, derive full localized positivity/nondegeneracy from a property also satisfied by the WI-239/WI-240 countermodels; that would show the present claim that von-Mangoldt-specific structure is necessary is too strong.