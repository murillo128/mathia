---
id: PA-nonquasianalytic-infinite-convolution-cutoff
type: prior-art
canonical_name: Nonquasianalytic cutoffs by infinite convolution
aliases:
  - Summable-width compact smooth bump
  - Iterated-convolution cutoff
kind: smooth cutoff construction
topics:
  - nonquasianalyticity
  - compact support
---

# Nonquasianalytic cutoffs by infinite convolution

## What it is

For decreasing positive widths with `sum a_j < infinity`, convolution of the normalized interval densities converges to a smooth compactly supported probability density. Its derivatives satisfy `||f^(n)||_infinity <= 2^n/(a_0 ... a_n)`.

## Relation to RH / Mathia research

[[research/prime_lattice/findings/PL-474-nonquasianalytic-tests-close-the-iterated-log-window-boundary|PL-474]], Section 1, and [[research/mobius_cancellation/findings/MC-530-nonquasianalytic-tests-reach-logarithmic-mobius-windows|MC-530]], Section 1, use widths proportional to `1/[j log(e+j)^q]`, `q>1`. They separately prove preservation of the resulting derivative bounds through their zero-annihilating operators and finite box inverses.

## Known scope and limits

The construction supplies a bump and derivative bounds, not zero interpolation, arithmetic contour growth, variance bounds, or effective acquisition of a zero-dependent test.

## Related prior art

[[research/prior_art/incremental/PA-paley-wiener-ingham-logarithmic-integral|Paley–Wiener/Ingham logarithmic-integral criterion]] supplies the Fourier-decay boundary; convergence of that integral alone does not construct the required arithmetic inverse.

## Evidence and provenance

[Armin Rainer, *Ultradifferentiable extension theorems: a survey*, Lemma 3.3](https://www.mat.univie.ac.at/~armin/publ/survey-UET.pdf), *Expositiones Mathematicae* 40 (2022), 679–757, [DOI](https://doi.org/10.1016/j.exmath.2021.12.001). Theorem 3.6 gives the related Denjoy–Carleman criterion. The exact persisted lookup triggers are the two finding paths linked above; PL-474 cites this lemma explicitly.
