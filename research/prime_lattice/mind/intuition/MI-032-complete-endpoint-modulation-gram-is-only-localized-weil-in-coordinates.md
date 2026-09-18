# MI-032 — Complete endpoint-modulation Gram is only localized Weil in coordinates

**Evidence level:** literature-backed exact synthesis from [PL-345](../../findings/PL-345-schur-endpoint-log-riesz-zero-spectrum.md) through [PL-347](../../findings/PL-347-endpoint-modulation-gram-weil-core.md). The completed Weil criterion and localized form theory are classical/prior art; the Mathia content is the exact placement of the endpoint modulation family inside that form.

For a fixed aperture `A`, let `u_A` be the normalized endpoint envelope and modulate it by the ordinary interval Fourier frequencies

`u_(A,k)(x)=e^(i pi k x/A) u_A(x)`.

The off-diagonal Gram entries

`K_A(k,l)=Q_W^A(u_(A,k),u_(A,l))`

retain genuine prime phases and therefore contain strictly more information than the single diagonal endpoint channel of PL-345--PL-346. But the additional information has a precise ceiling.

On `(-A,A)`, `u_A` is bounded and bounded away from zero, so multiplication by `u_A` is an invertible bounded map. The exponentials `e^(i pi k x/A)` are the complete Fourier basis. More importantly, the span of the modulated endpoint states is not merely `L^2` dense: for every `0<s<1/2`, Fourier approximation passes through `H^s`, and

`log(2+|xi|) <= C_s(1+|xi|^(2s))`

embeds that approximation into the logarithmic form norm of the localized Weil operator. The endpoint jumps remain compatible with this subcritical Sobolev control. Hence

`closure_form span{u_(A,k)} = D(Q_W^A)`.

Therefore finite-matrix positivity of `K_A` is exactly positivity of the localized Weil form:

`K_A >= 0 on all finite index sets  <=>  Q_W^A >= 0 on D(Q_W^A)`.

Taking every aperture `A>0` gives precisely Weil positivity and hence RH. This equivalence is exact but not a new mechanism. The full modulation family is simply a complete coordinate system for a pre-existing classical quadratic form.

Together with PL-346 this classifies the natural endpoint family at both extremes. One completed endpoint state scalarizes to the classical logarithmic Riesz residual; the complete cross-modulation family restores the entire localized Weil problem. The only potentially new region is between them: a restricted/source-forced family whose span is **not** automatically a form core but for which arithmetic supplies a nontrivial sufficiency theorem, or a coupling law not reducible to arbitrary complete-frame coordinates.

**Boundary.** The result does not say that diagonal modulations alone determine the form, that one fixed aperture proves RH, or that every matrix-valued Prime-Lattice construction is classical. It closes the specific continuation obtained by taking all cross-modulations of the same endpoint envelope.
