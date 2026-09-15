---
id: PA-julia-nevanlinna-boundary-reduction
type: prior-art
canonical_name: Julia–Nevanlinna boundary reduction
aliases:
  - Julia reduction
  - boundary Nevanlinna-Pick reduction and augmentation
kind: analytic-reduction
topics:
  - pick-functions
  - scalar-herglotz
  - boundary-interpolation
---

# Julia–Nevanlinna boundary reduction

## What it is

For a nonconstant Pick function analytic and real at a real node `t`, regular reduction is `g(z)=-1/(f(z)-f(t))+1/(f'(t)(z-t))`. At a real pole of residue `R<0`, reduction removes `R/(z-t)`. These operations preserve the Pick class under the stated hypotheses; boundary augmentation is the corresponding reconstruction operation. See [Agler–Young, Definition 3.2 and Theorem 3.4](https://arxiv.org/pdf/0905.4759).

## Relation to RH / Mathia research

[[research/weil_positivity/findings/WP-312-fixed-boundary-julia-nevanlinna-reduction-cannot-repair-gamma-asymptotic|WP-312]] uses this classical reduction followed by inversion, `J=-1/g+beta`, to normalize the logarithmic end. [[research/weil_positivity/findings/WP-316-scalar-julia-reduction-erases-every-asymptotically-isolated-mangoldt-pole|WP-316]] analyzes isolated poles; [[research/weil_positivity/findings/WP-317-finite-multipole-julia-reduction-is-interlacing-degree-reduction|WP-317]] identifies finite interlacing degree reduction; [[research/weil_positivity/findings/WP-318-scalar-julia-tangents-are-boolean-self-energies-of-derivative-biased-measures|WP-318]] expresses the pure-measure normalized response by a Boolean self-energy. These are scoped Mathia applications, not new Pick-class preservation theorems.

## Known scope and limits

Regular boundary nodes require the specified boundary value and positive derivative. The classical reduction's positivity alone has no arithmetic specificity. It supplies neither the Mangoldt–Gamma coupling nor global Weil positivity. The normalized response `J` is distinct from the conventional reduction `g`.

## Related prior art

- [[research/prior_art/incremental/PA-boolean-convolution-self-energy|Boolean convolution self-energy]], the explicit pure-measure normalized-response identification in WP-318.

## Evidence and provenance

- Jim Agler and N. J. Young, *Boundary Nevanlinna-Pick interpolation via reduction and augmentation*, Mathematische Zeitschrift 268 (2011), 791–817, DOI `10.1007/s00209-010-0696-3`; [arXiv:0905.4759v3](https://arxiv.org/abs/0905.4759v3), Section 3. The inspected revised version supplies the formulas and Pick-preservation statement used here.
- Triggering persisted dependencies: [[research/weil_positivity/findings/WP-312-fixed-boundary-julia-nevanlinna-reduction-cannot-repair-gamma-asymptotic|WP-312]] equations (3)–(4), and [[research/weil_positivity/findings/WP-318-scalar-julia-tangents-are-boolean-self-energies-of-derivative-biased-measures|WP-318]] “Prior-art and novelty audit.”
