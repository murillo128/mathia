---
id: PA-boolean-convolution-self-energy
type: prior-art
canonical_name: Boolean convolution self-energy
aliases:
  - Boolean K-transform
  - Boolean energy function
kind: probability-transform
topics:
  - boolean-convolution
  - cauchy-transform
  - scalar-herglotz
---

# Boolean convolution self-energy

## What it is

For a probability measure `nu` on the real line, use `G_nu(z)=integral (z-x)^(-1) d nu(x)` and `F_nu=1/G_nu`. Its Boolean energy is `K_nu(z)=z-F_nu(z)`. Boolean additive convolution is characterized by addition of these energy functions. With this Cauchy convention, `K_nu` has nonpositive imaginary part on the upper half-plane. See [Arizmendi–Hasebe–Sakuma, Section 3.3](https://alea.math.cnrs.fr/articles/v10/10-12.pdf).

## Relation to RH / Mathia research

[[research/weil_positivity/findings/WP-318-scalar-julia-tangents-are-boolean-self-energies-of-derivative-biased-measures|WP-318]] identifies the normalized pure-measure scalar Julia response with `d(t-K_nu)`, where `nu` is biased by the boundary derivative. That identity and the matched-control construction are the persisted Mathia application; they are not attributed to the original Boolean-convolution paper.

## Known scope and limits

The energy-function sign holds for arbitrary probability laws. It does not supply arithmetic selectivity, a Gamma term or a Weil positivity theorem. WP-318 separately retains regular-node, finite nonzero derivative and pure-measure hypotheses; affine Herglotz channels and operator-valued reductions lie outside its classification.

## Related prior art

- [[research/prior_art/incremental/PA-julia-nevanlinna-boundary-reduction|Julia–Nevanlinna boundary reduction]], linked through the explicit WP-318 identity, not by an inferred general equivalence.

## Evidence and provenance

- Roland Speicher and Reza Woroudi, *Boolean convolution*, Fields Institute Communications 12 (1997), 267–279. DOI `10.1090/fic/012/13`; bibliographic identity verified in [Speicher's publication list, item 21](https://www.math.uni-sb.de/ag/speicher/speicher_publ_mainpublE.html).
- Octavio Arizmendi, Takahiro Hasebe and Noriyoshi Sakuma, *On the Law of Free Subordinators*, ALEA 10(1) (2013), 271–291, [Section 3.3](https://alea.math.cnrs.fr/articles/v10/10-12.pdf), for the energy convention and positive-measure representation.
- Triggering persisted dependency: [[research/weil_positivity/findings/WP-318-scalar-julia-tangents-are-boolean-self-energies-of-derivative-biased-measures|WP-318]], “Prior-art and novelty audit” and equations (5)–(8).
