# MI-023 — Growing oriented tensor order terminates in source reconstruction

**Evidence level:** exact growing-order source-recovery boundary and prior-art classicalization from [PC-304](../../findings/PC-304-growing-oriented-frame-tensor-order-becomes-exact-source-reconstruction.md), extending the fixed-finite polyspectral classification [PC-303](../../findings/PC-303-finite-oriented-frame-tensors-are-joint-fourier-polyspectra.md)

For prime modulus `q`, one native labelled oriented-frame coordinate already has the form

`y_s=N^(-1/2) zeta_q^s`.

Its degree-`d` moment under a source law `mu` is exactly

`E[y_s^d]=N^(-d/2) \hat mu(d mod q)`.

Thus degrees `1,...,q-1` expose every nonzero additive Fourier mode; normalization supplies the zero mode, and inverse DFT reconstructs `mu` exactly. The fixed-order hierarchy of PC-303 therefore has a concrete terminal state: once tensor degree reaches order `q`, it is no longer a partial higher-order observable but a lossless encoding of the source itself.

The canonical prime source makes the translation-invariant boundary even sharper. At prime modulus, the indicator of any nonempty proper subset has no nonzero Fourier zero: otherwise its `0/1` polynomial would vanish at a primitive `q`-th root and hence be divisible by the full cyclotomic polynomial. The prime support is nonempty and proper, so its DFT is nowhere zero. Equal full bispectra then force the ratio of two Fourier vectors to be a cyclic character, which means the sources differ only by translation. Hence the complete bispectrum already determines the canonical source orbit; higher translation-invariant polyspectra carry no additional orbit-discriminating information.

This gives a two-sided boundary for the oriented-frame program. **Fixed finite order** is classical joint Fourier/polyspectral data; **order high enough to cover all frequencies** is exact source reconstruction. A genuinely new carrier can only live between those endpoints if a growing partial packet has a load-bearing asymptotic effect before reconstruction saturates, or if another operation acts on the oriented fields before they are reduced to source Fourier coordinates.

The research question is therefore quantitative rather than categorical: is there a regime `d(q)<<q` in which the accessible frequency set has a stable source-sensitive limit consumed by a geometry-forced zero-sensitive operator, with a discriminator not equivalent to reconstructing the same source packet more accurately? Cross-level or mixed-conductor interactions are another honest escape only when the coupling is not reproducible by separately reconstructing each modulus and post-processing the results.

**Boundary.** PC-304 does not rule out useful intermediate growth, nonpolynomial/operator dynamics before Fourier reduction, or genuine cross-level coupling. Exact reconstruction of prime residues is also not an RH mechanism: it supplies no critical spectral parameter, Gamma factor, functional-equation constraint or zero-location theorem by itself. The result closes “keep increasing tensor order” as an information-gain argument unless the intermediate operation is specified and shown to do more than encode the source.
