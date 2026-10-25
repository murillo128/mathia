---
id: PA-multichannel-compact-distribution-deconvolution
type: prior-art
canonical_name: Multichannel deconvolution by compact-distribution Bezout identities
aliases:
  - Strongly coprime compact convolvers
  - Analytic Bezout multichannel deconvolution
kind: exact-inversion
topics:
  - convolution
  - compact-distributions
  - small-divisors
---

# Multichannel deconvolution by compact-distribution Bezout identities

## What it is

Compact convolution kernels admit compact distributional deconvolvers whose convolution sum is the Dirac mass precisely under a quantitative strong-coprimeness condition on their Fourier–Laplace transforms. The corresponding analytic Bezout identity sums transform products to one. Absence of common zeros alone is insufficient; growth and near-collision control matter. Casey's report, Section 2.1, Theorem 2.3, states this classical Hörmander criterion. Its printed page 7 explicitly treats two interval kernels with a square-root-of-prime length ratio.

## Relation to RH / Mathia research

[[research/prime_lattice/findings/PL-475-two-box-lengths-force-paired-macroscopic-prime-variance|PL-475]], Sections 1–4, reconstructs the two-box identity at ratio sqrt(2). Convolution with its fixed smooth mean-zero arithmetic target gives localized tests with uniformly bounded norms under dilation. Rounding the second integer length costs O(1/X) in target sup norm and O(log X) against prime coefficients. The resulting conditional floor concerns the sum of two normalized variances; it does not supply either upper bound.

## Known scope and limits

A compact-distribution inverse has finite derivative cost on smooth targets; it is not automatically bounded inversion on arbitrary L² data. PL-475's rational-ratio and Liouville controls distinguish common zeros from uncontrolled small divisors. Its rounded integer pair is only an approximate inverse. The arithmetic pole-isolation formula, non-effective zero-set-dependent target and variance implication are separate application inputs.

## Related prior art

[[research/prior_art/incremental/PA-van-cittert-approximate-deconvolution|Van Cittert deconvolution]] is a finite approximate-inverse polynomial for one filter; the present identity combines several channels. Pensky–Sapatinas study Diophantine channel choices in periodic statistical boxcar deconvolution, a different estimation model.

## Evidence and provenance

- Stephen D. Casey and David F. Walnut, *Systems of Convolution Equations, Deconvolution, Shannon Sampling, and the Wavelet and Gabor Transforms*, SIAM Review 36(4) (1994), 537–577, [DOI](https://doi.org/10.1137/1036140), identified in PL-475's source 142.
- Stephen D. Casey, *Modulation and Sampling Techniques for Multichannel Deconvolution*, University of Maryland ISR TR-96-54 (1996), Section 2.1, Theorem 2.3 and Definition 2.3, printed pp. 5–7; [institutional record](https://drum.lib.umd.edu/items/afce37a2-e785-4d81-90b7-610a94de7310), [inspected report](https://api.drum.lib.umd.edu/server/api/core/bitstreams/fff4ad58-33f1-4d4f-b92d-1117c53a9efc/content). Theorem 2.4 on printed p. 7 gives the square-root-ratio box example.
- Marianna Pensky and Theofanis Sapatinas, *Multichannel boxcar deconvolution with growing number of channels*, Electronic Journal of Statistics 5 (2011), 53–82, [DOI](https://doi.org/10.1214/11-EJS597), [author abstract](https://arxiv.org/abs/1102.2298).
- Persisted lookup trigger: `research/prime_lattice/findings/PL-475-two-box-lengths-force-paired-macroscopic-prime-variance.md`, Sections 1 and 4 and prior-art comparison, at source revision `b76d9d4208485a9c9c04192126afd07979ef2cda`.
