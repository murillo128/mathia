---
id: PA-paley-wiener-ingham-logarithmic-integral
type: prior-art
canonical_name: Paley–Wiener/Ingham logarithmic-integral criterion
aliases:
  - Paley–Wiener Fourier-decay obstruction
  - Ingham compact-support decay theorem
kind: Fourier uncertainty theorem
topics:
  - Fourier decay
  - compact support
  - logarithmic integrals
---

# Paley–Wiener/Ingham logarithmic-integral criterion

## What it is

A nonzero compactly supported continuous function cannot obey `|f_hat(t)| <= C exp(-psi(t))` when the nonnegative, even, locally integrable envelope has divergent integral `int psi(t)/(1+t^2) dt`.

For a nonnegative even `theta` decreasing to zero, Ingham also supplies nonzero continuous functions with arbitrarily small compact support and decay `O(exp(-|t| theta(t)))` exactly when `int_1^infinity theta(t)/t dt < infinity`.

## Relation to RH / Mathia research

[[research/prime_lattice/findings/PL-473-box-fourier-zeros-obstruct-logarithmic-window-test-inversion|PL-473]], Section 1, applies the necessary direction at the box multiplier's exact zeros. [[research/mobius_cancellation/findings/MC-530-nonquasianalytic-tests-reach-logarithmic-mobius-windows|MC-530]], Section 4, explicitly reconstructs that operator boundary for its Möbius transfer. These are the persisted lookup triggers.

## Known scope and limits

This is an analytic uncertainty principle. It supplies neither arithmetic cancellation nor a variance counterexample. An admissible Fourier envelope does not alone prove bounded box inversion or preservation under zero isolation.

## Related prior art

[[research/prior_art/incremental/PA-nonquasianalytic-infinite-convolution-cutoff|Infinite-convolution cutoffs]] provide derivative-controlled bumps.

## Evidence and provenance

- [Bhowmik–Ray–Sen, arXiv:1605.09616v1](https://arxiv.org/pdf/1605.09616), Theorems 1.1–1.2, states both classical results and distinguishes compact support from the more general half-line support theorem.
- [Bhowmik–Sen, arXiv:1606.02125v1](https://arxiv.org/pdf/1606.02125), Theorem 1.1(a)–(b), is PL-473's cited compact-support formulation.
- Original Ingham source: *A Note on Fourier Transforms*, JLMS 9 (1934), 29–32, [DOI](https://doi.org/10.1112/jlms/s1-9.1.29).
