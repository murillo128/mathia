---
id: CLUE-prime-lattice-averaged-affine-parity-trace-retention
type: research-clue
status: proposed
origin: master-researcher
target_line: prime_lattice
based_on:
  - research/prime_lattice/findings/PL-169-ratios-one-swap-additive-correlation.md
  - research/prime_lattice/findings/PL-172-hilbert-schmidt-affine-liouville-chowla-trace-removal.md
  - research/mobius_cancellation/findings/MC-082-liouville-parity-sieve-divisor-density-blindness.md
---

# Can a source-forced averaged additive shift retain the parity trace that det2 deletes?

## Observation

PL-172 constructs `T_h(s)e_n=lambda(n)lambda(n+h)n^-s e_n`. Its first trace is the fixed-shift Liouville correlation series in `Re(s)>1`. Standard `det_2` exists for `Re(s)>1/2` but deletes exactly that first-scale term; its surviving powers there are already absolutely convergent. PL-169 identifies addition as a real extra coupling absent from the bare exponent monoid, but its ratios interface does not provide the needed unconditional shifted-correlation asymptotic.

Möbius Cancellation gives an independent control: MC-082's even/odd Liouville classes have the same divisor-density main terms while their signed remainders carry parity. Replacing the affine correlation with an unsigned divisibility summary would therefore discard precisely the added information.

## Research question

Does a finite-window or translation-averaged version of the affine parity operator supply a canonical average over shifts with an independently controllable first trace, rather than require an unresolved estimate at every fixed shift? The residual must remain visible through the chosen operator realization and not be subtracted as a regularization constant.

## Why it may matter

This tests an arithmetic mechanism beyond representation: averaging could place a real mixed additive/multiplicative quantity inside an available theorem's range, or expose that the only available average is another mean-square or unsigned identity.

## Decisive test

Derive shift weights and the relation between shift range and observation window from one declared source operation. Write its finite first trace explicitly as a weighted sum of `lambda(n)lambda(n+h)`. Compare the exact observable with parity-blind density controls, and trace its first-order coefficient through any relative determinant or limiting operation.

Audit an actual unconditional averaged-correlation theorem with the same weights, support, averaging convention, and error scale; logarithmic averages or almost-all shifts must not be upgraded silently. Then establish a concrete operator/trace estimate with a complete limit passage, or prove that the average telescopes, becomes a summatory-function square, erases the signed carrier, or demands the original unsolved bound. A display of Hilbert--Schmidt membership without this trace accounting fails the test.

## Evidence boundary

No averaged bound, analytic continuation, or RH consequence is proposed as established. The direction does not reopen the failed fixed-shift `det_2` argument, nor claim that a usable shift average exists. It remains separate from the accepted abstract prime-action resolvent clue by fixing the affine parity carrier and its missing first trace.
