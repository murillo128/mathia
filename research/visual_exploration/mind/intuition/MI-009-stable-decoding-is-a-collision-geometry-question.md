# MI-009 — Stable analytic information is measured by phase-collision geometry, not set-theoretic recoverability

**Evidence level:** proved representation criterion; source-sensitive applications remain open

## Core intuition

Exact prime phases can contain far more set-theoretic information than any stable representation can use. Two distinct prime phases already identify every real height, but the inverse map is nowhere continuous because the Kronecker orbit returns arbitrarily close to itself at arbitrarily distant heights. Hence “the analytic coordinate is not determined by the phases” is the wrong notion of independence at infinite precision.

For Lipschitz recovery there is an exact replacement: the required decoder complexity is the worst ratio between observable separation and prime-phase separation over recurrent near-collisions.

## Strongest justified claim

VIS-161 proves that for distinct primes `p,q`, the map `t -> (p^(-it),q^(-it))` is injective and dense in the two-torus, while its inverse on the orbit is nowhere continuous. Every same-height observable therefore factors set-theoretically through two exact phases, but a continuous torus decoder would have to be bounded and Bohr almost periodic.

VIS-162 freezes a finite prime set `P` and the chordal torus metric. For an observable `A` on a height set `S`, define

`Lambda_P(A;S)=sup_(t!=u) |A(t)-A(u)|/||Phi_P(t)-Phi_P(u)||`.

Kirszbraun's theorem makes this quantity exactly the smallest Lipschitz constant of any exact torus decoder. For approximate decoding, every `L`-Lipschitz decoder with uniform error `epsilon` must pay at least half of the worst collision excess `(|Delta A|-L D_P)_+`.

## Synthesis of evidence

Stable analytic novelty can be tested without searching over decoder architectures. Freeze the representation, metric, normalization, and height window; then study the collision profile `Lambda_P(A;T)`. Large values mean that distant heights recur close in phase while the observable remains separated, forcing any stable decoder to become increasingly ill-conditioned.

The zeta-specific question is comparative rather than absolute. Generic recurrence can make many observables hard to decode. A useful source claim must show that a chosen normalized zeta-facing coordinate has collision-complexity growth not shared by matched deterministic phase/clock controls.

## Counterevidence / boundary cases

The exact criterion is metric- and decoder-class-specific. It concerns Lipschitz maps into a Hilbert target; other regularity classes need their own extension/complexity theorem. A globally unbounded observable trivially has no continuous decoder on a compact torus, so useful tests should use normalized observables or finite expanding windows.

A large collision quotient is not automatically arithmetic. It may reflect generic Kronecker recurrence, an unfortunate normalization, or a deterministic observation clock.

## Epistemic status

**Exact stable-representation boundary:** raw finite-prime phase information identifies height set-theoretically, while Lipschitz recoverability is characterized exactly by one pairwise collision quotient. Whether a specific zeta observable separates from matched controls remains an open source question.

## Novelty/prior-art status

Kronecker recurrence, almost-periodic pullbacks, and Kirszbraun extension are classical. The Mathia-specific content is the representation audit and its use as a precise visual-control criterion.

## Falsification criterion

Find a finite-prime phase orbit function satisfying all pairwise `L`-Lipschitz inequalities but admitting no `L`-Lipschitz torus extension, or prove that a proposed zeta collision profile is reproduced by an appropriate matched deterministic control. The former would contradict the stated criterion; the latter would invalidate the claimed source sensitivity.
