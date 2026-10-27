---
id: PA-positive-shift-interval-dirichlet-to-neumann
type: prior-art
canonical_name: Positive-shift interval Dirichlet-to-Neumann form
aliases:
  - interval DtN matrix
  - transverse-plus-mass interval minimum
kind: boundary energy identity
topics:
  - dirichlet-to-neumann
  - coercive-quadratic-forms
---

# Positive-shift interval Dirichlet-to-Neumann form

## What it is

For `ell,kappa>0`, minimizing `integral_0^ell (|u'|²+kappa²|u|²) dx` with endpoints `a,b` gives

\[
\kappa\coth(\kappa\ell)(|a|^2+|b|^2)
-2\kappa\operatorname{csch}(\kappa\ell)\Re(\overline a b).
\]

The symmetric and antisymmetric eigenvalues are `kappa tanh(kappa ell/2)` and `kappa coth(kappa ell/2)`. Post's §6.1, equation (6.2), gives the matrix and these eigenvalues at spectral parameter `-kappa²`.

## Relation to RH / Mathia research

[[research/prime_flute/findings/PF-370-positive-shift-trace-cost-dominates-the-two-cuff-escape-construction|PF-370]], §2, uses this identity with `ell=s cosh(t)` and `kappa=1` to retain the common-amplitude cost omitted by difference-only energy. Its actual-pant comparison and specified-witness estimate are separate derived inputs.

## Known scope and limits

At zero shift the common mode costs zero and only `|b-a|²/ell` remains. The interval identity alone supplies no pant embedding, arbitrary-band full-line comparison, global minimizer or RH result.

## Related prior art

[[research/prior_art/incremental/PA-exponential-divided-differences|Exponential divided differences]] construct the separate scalar witness priced in PF-370; they do not supply this coercive energy identity.

## Evidence and provenance

- Olaf Post, *Boundary pairs associated with quadratic forms*, §6.1, equation (6.2), p. 31: [primary manuscript, arXiv:1210.4707v2](https://arxiv.org/pdf/1210.4707v2).
- Persisted trigger: `research/prime_flute/findings/PF-370-positive-shift-trace-cost-dominates-the-two-cuff-escape-construction.md`, §§2 and 6. It explicitly identifies and directly derives the classical identity.
