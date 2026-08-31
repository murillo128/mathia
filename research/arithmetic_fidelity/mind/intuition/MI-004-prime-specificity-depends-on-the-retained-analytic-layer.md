# MI-004 — Rational-prime specificity depends on which normed analytic layer is retained

**Evidence level:** supported by exact algebraic reconstruction and classical matched-control theorems

## Core intuition

“Contains primes” is not a stable fidelity statement. The bare multiplicative structure remembers atomhood and factorization shape while forgetting which atom is the rational prime `p` and what its Archimedean norm is. Adding a norm can restore that information, but a later analytic compression can erase it again. Prime specificity must therefore be audited at the exact destination layer, not inferred from the provenance of the input.

## Strongest justified principle

AF-015 computes the exact symmetry boundary of the bare multiplicative monoid: `Aut(N_{>0},x)` is the full permutation group of the prime generators. Its orbit quotient remembers exponent multisets, hence primality and factorization shape, but not the ordinary assignments `p`, `log p`, or prime order. Classical arithmetical-semigroup theory makes the missing structure explicit by adjoining a norm/degree as extra data.

AF-017 then separates two analytic destinations. In an absolute-convergence half-plane, the exact Euler-product function determines the prime sum by logarithm plus Möbius inversion, and the prime sum determines the unordered generator-norm multiset. But the zero/pole divisor is not faithful: Grosswald--Schnitzer-type systems can alter generator norms while preserving the zeta zero divisor and pole in the stated half-plane through a nonvanishing analytic factor. Thus

`normed prime system -> exact Euler-product function -> meromorphic divisor`

has a faithful first step for the norm multiset and a nonfaithful second step.

AF-016 prevents a false converse. Killing the obvious prime-permutation automorphisms does not prove that a desired norm or marking is intrinsically recoverable in the declared language; outside regimes with a completeness theorem, base-model automorphism invariance is only a negative obstruction test.

## What remains possible

A rational-prime-specific mechanism can survive if the destination retains enough independently normalized analytic data to fix the norm system or constrain the zero-free factor. Exact values, Euler coefficients, a rigid functional-equation/growth normalization, or another canonical enrichment are possible candidates, but their fidelity has to be proved against matched generalized-prime controls.

## Status / novelty

The free-monoid symmetry, arithmetical-semigroup norm separation, Möbius inversion, Svenonius boundary, and Grosswald--Schnitzer controls are classical or persisted exact findings. The category-indexed fidelity hierarchy is the supported Arithmetic Fidelity synthesis.

## Falsification criterion

Exhibit two different normed prime systems with the same destination object in a category claimed to be faithful, or prove that a proposed destination normalization reconstructs the ordinary rational-prime norm multiset and defeats the strongest matched controls.

## Lean-formalizable core

- Free commutative monoid automorphism/orbit classification.
- Möbius inversion from Euler-product logarithm to prime sum.
- Uniqueness of a locally finite norm multiset from its Dirichlet/Laplace sum.