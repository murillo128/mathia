---
id: CLUE-weil-positivity-finite-local-certificates-schiffer-obstruction
type: research-clue
status: proposed
origin: adversarial
target_line: weil_positivity
based_on:
  - research/weil_positivity/findings/WP-014-exact-schiffer-kernel-is-not-positive-definite.md
  - formalization/mathia/WP014SchifferIndefinite.lean
---

# Why do global pole structure and a finite local certificate prove the same Schiffer obstruction?

## Observation

WP-014 proves the decisive inequality

\[
\csc^2 t-\frac1{t^2}>\frac13,
\qquad 0<|t|<\frac\pi2,
\]

through the global Mittag--Leffler expansion of `csc^2`, where every paired pole `\pm k\pi` contributes a strictly positive excess above the diagonal value `1/3`.

The Mathia Lean formalization reaches the same strict inequality without using the pole expansion.  It proves a finite chain of elementary bounds, notably a fifth-order upper bound for `sin t`, and reduces the decisive sign to a polynomial inequality on `0<t^2<4`.

These are not merely two implementations of the same algebraic derivation.  One explanation attributes the excess to the global meromorphic pole structure; the other shows that finitely much analytic information already forces the obstruction on the whole required interval.

## Research question

Is there a mathematical reason these two representations are equivalent at the level needed for the two-point Schiffer obstruction?

More concretely, can one characterize when a global positive-tail representation of a special-function kernel admits a bounded finite inequality certificate that already forces the same strict Cauchy--Schwarz/Gram-determinant failure?

The goal is not a shorter proof of WP-014.  It is to understand whether the existence of the finite certificate exposes a reusable structural principle that is invisible in the Mittag--Leffler presentation.

## Why it may matter

If the finite proof is only accidental, WP-014 remains a special-function calculation with two proof routes.  If instead global pole positivity systematically collapses to a finite local certificate for the relevant sign question, then Mathia gains a different representation of the obstruction: one potentially easier to generalize, search for automatically, and compare across kernels that do not have a convenient explicit pole expansion.

This would also be a concrete example where formalization feedback reveals mathematical structure rather than merely certifying an existing explanation.

## Decisive test

Derive a nontrivial class of scalar kernels or special-function profiles for which both of the following can be proved:

1. a global representation gives a positive-tail proof of a strict diagonal-excess inequality; and
2. a finite-order analytic/polynomial certificate proves the same inequality on the full required domain without using the global representation.

Then identify an explicit condition explaining why the finite certificate exists.  A counterexample class where the global representation proves the inequality but every proposed bounded-order certificate fails would kill the strongest version of the clue.

## Evidence boundary

WP-014 establishes only the concrete `csc^2` inequality and the resulting two-point indefiniteness.  The Lean proof establishes that one finite certificate exists for this case.  Nothing currently shows that the two proof mechanisms are equivalent, that finite certificates exist systematically, or that such a principle extends beyond this specific scalar profile.