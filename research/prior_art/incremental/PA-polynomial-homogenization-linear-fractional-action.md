---
id: PA-polynomial-homogenization-linear-fractional-action
type: prior-art
canonical_name: Polynomial homogenization and linear fractional action
aliases:
  - binary-form change of coordinates
kind: polynomial representation
topics:
  - polynomial-calibration
  - projective-coordinates
---

# Polynomial homogenization and linear fractional action

## What it is

A polynomial of degree at most a specified n corresponds to a homogeneous binary form of degree n. An invertible linear change of its two coordinates induces a linear fractional substitution with a degree-n multiplier clearing denominators. This is an invertible linear action on the fixed-degree polynomial space; the specified degree remains part of the representation.

## Relation to RH / Mathia research

[[research/arithmetic_fidelity/findings/AF-579-unbounded-query-locations-preserve-polynomial-budget-obstruction|AF-579]], equations (5)–(8), uses this classical action at cap N with n=N−1: a=x/(1−x) and multiplication by (1−x)^n bijectively carry the nuisance space onto itself. The finding separately proves endpoint smoothness of the transformed prime-edit gaps and transports its exact finite-query experiment.

## Known scope and limits

The action depends on the supplied degree. It does not map all unknown degrees into one fixed finite-dimensional space, preserve an unweighted noise norm, or prove the source-specific minimax theorem. No value at infinity is supplied.

## Related prior art

The downstream [[research/prior_art/incremental/PA-gaussian-conditioning-adaptive-linear-information|adaptive Gaussian conditioning]] argument is a separate testing ingredient, not part of the coordinate action.

## Evidence and provenance

- Peter J. Olver, *Classical Invariant Theory*, Cambridge University Press (1999), Chapter 2, pp. 13–15, equations (2.3)–(2.8), Theorem 2.2 and Proposition 2.3: [monograph](https://www.math.utoronto.ca/~ila/ClassicalInvariantTheory.pdf).
- Persisted lookup trigger: `research/arithmetic_fidelity/findings/AF-579-unbounded-query-locations-preserve-polynomial-budget-obstruction.md`, “Compactification preserves the capped exact experiment” and “Prior art and mathematical delta”.
