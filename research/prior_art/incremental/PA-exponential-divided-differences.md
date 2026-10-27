---
id: PA-exponential-divided-differences
type: prior-art
canonical_name: Exponential divided differences
aliases:
  - generalized divided differences of exponentials
kind: confluent exponential representation
topics:
  - nonharmonic-fourier-series
  - clustered-frequencies
---

# Exponential divided differences

## What it is

Divided differences replace nearly coincident exponentials by combinations with a continuous confluent limit. For distinct real frequencies,

\[
\frac{e^{i(\xi+d)t}-e^{i\xi t}}{id}\longrightarrow t e^{i\xi t}
\quad(d\to0).
\]

Higher confluence produces polynomial factors multiplying exponentials. Avdonin–Ivanov define the generalized differences and their integral representation in §2.2; their basis results impose additional hypotheses on the full frequency set.

## Relation to RH / Mathia research

[[research/prime_flute/findings/PF-369-nearly-equal-cuff-lattices-hide-broad-band-residual-mass-beyond-actual-windows|PF-369]], equations (9)–(12), uses first divided differences on two exact cuff lattices. Its explicit remainder is compared with an exponentially small residual norm. This is the persisted mechanism that triggered registration.

## Known scope and limits

The classical representation alone supplies no uniform growing-period weighted estimate. PF-369 proves that comparison separately; it imports no Riesz-basis theorem. Prime realization, pant-energy costs and RH consequences do not follow from confluence.

## Related prior art

[[research/prior_art/incremental/PA-hermite-polynomial-interpolation|Hermite polynomial interpolation]] concerns polynomial value/derivative constraints. It is distinct from using divided differences of the exponential family as functions of time.

## Evidence and provenance

- S. A. Avdonin and S. A. Ivanov, *Exponential Riesz bases of subspaces and divided differences*, Introduction and §2.2, Definition 1 and equations (3)–(4): [primary manuscript, arXiv:math/0103160v1](https://arxiv.org/pdf/math/0103160v1).
- Persisted trigger: `research/prime_flute/findings/PF-369-nearly-equal-cuff-lattices-hide-broad-band-residual-mass-beyond-actual-windows.md`, §§3 and 6. The source explicitly identifies this classical mechanism and excludes transfer of the paper's basis theorem.
