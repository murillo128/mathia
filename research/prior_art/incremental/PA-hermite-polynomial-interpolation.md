---
id: PA-hermite-polynomial-interpolation
type: prior-art
canonical_name: Hermite polynomial interpolation
aliases:
  - confluent polynomial interpolation
kind: interpolation theorem
topics:
  - polynomial-interpolation
  - value-derivative-information
---

# Hermite polynomial interpolation

## What it is

At distinct real or complex nodes with prescribed multiplicities, values and successive derivatives determine a unique polynomial of degree less than the total multiplicity. Repeated nodes in Newton divided differences encode these derivative conditions. De Boor's Propositions 7 and 32 give the polynomial formulation and arbitrary-data construction.

## Relation to RH / Mathia research

[[research/xi_flow/findings/XF-207-complex-value-queries-retain-the-analytic-calibration-stopping-obstruction|XF-207]], equations (7)–(8), explicitly uses this classical interpolation freedom. A correction vanishing at the queried nodes enforces derivative zero at the critical endpoint while retaining arbitrary values at any at-most-N distinct complex nodes in degree at most N+1. The finding handles both a queried endpoint and an endpoint absent from the value bank.

## Known scope and limits

Interpolation alone supplies neither the source's derivative budget nor the supported-prior testing bound. Exact derivative or contour-integral access is a different information class. A compact analytic norm bound controls approximation without necessarily providing a positive classification margin.

## Related prior art

[[research/prior_art/incremental/PA-polynomial-interpolation-early-termination|Randomized interpolation early termination]] concerns validation and stopping; it is distinct from finite value-and-derivative interpolation. The [[research/prior_art/incremental/PA-gaussian-conditioning-adaptive-linear-information|adaptive Gaussian conditioning]] step uses the resulting independent evaluation rows.

## Evidence and provenance

- Carl de Boor, *Divided Differences*, *Surveys in Approximation Theory* 1 (2005), 46–69, Propositions 7 and 32, equations (8) and (33): [author paper](https://arxiv.org/pdf/math/0502036).
- Persisted lookup trigger: `research/xi_flow/findings/XF-207-complex-value-queries-retain-the-analytic-calibration-stopping-obstruction.md`, “The endpoint derivative is independent of every finite complex value bank” and “Checks, prior art, and mathematical delta”.
