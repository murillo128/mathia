# MI-023 — Growing oriented tensor order saturates at source-sparsity resolution, not ambient modulus size

**Evidence level:** exact growing-order source-recovery boundary and prior-art classicalization from [PC-304](../../findings/PC-304-growing-oriented-frame-tensor-order-becomes-exact-source-reconstruction.md), sharpened by the source-sparsity reconstruction theorem [PC-305](../../findings/PC-305-sublinear-oriented-tensor-order-already-reconstructs-the-prime-source.md), extending the fixed-finite polyspectral classification [PC-303](../../findings/PC-303-finite-oriented-frame-tensors-are-joint-fourier-polyspectra.md)

For prime modulus `q`, one native labelled oriented-frame coordinate has the form

`y_s=N^(-1/2) zeta_q^s`.

Its degree-`d` moment is exactly an additive Fourier coefficient. PC-304 therefore showed that degrees `1,...,q-1` reconstruct an arbitrary source law by inverse DFT, and that for the canonical prime support the full bispectrum already determines the source up to cyclic translation.

PC-305 shows that `q` is the wrong saturation scale for the actual source. The canonical measure has only

`L_q=pi(q)-2`

distinct equally weighted atoms. Its first `L_q` power sums determine the elementary symmetric polynomials by Newton--Girard and hence recover the complete prime support exactly. Since `L_q=O(q/log q)`, exact source reconstruction occurs already at **sublinear tensor order** even with a single frame coordinate.

The spatial window lowers the sufficient tensor degree further. With `H_B={-B,...,B}`, a degree-`d` monomial exposes every consecutive source frequency through order `dB`; therefore

`dB >= L_q`

already suffices for exact reconstruction. The relevant capacity parameter is the additive frequency packet relative to source sparsity, not tensor degree relative to the ambient modulus.

This closes `d(q)<<q` as a meaningful standalone definition of an intermediate regime. A sublinear hierarchy can already be a lossless source encoding. Conversely, `dB<L_q` is only a necessary warning boundary, not a theorem of nonreconstruction: nonconsecutive moments or arithmetic side information could identify the special source earlier.

The reusable distinction is **representation order versus resolving capacity**. Fixed finite tensor order classicalizes to finite Fourier/polyspectral data; once enough moments are exposed relative to the number of source atoms, classical sparse-moment recovery reconstructs the source. Neither endpoint creates an RH mechanism. A genuinely new carrier must identify an operation that consumes a still-incomplete packet before Newton/Prony/Fourier reconstruction becomes available, or use cross-level/mixed-conductor structure that is not reproducible by separately reconstructing each modulus and post-processing it.

**Boundary.** The condition `dB>=L_q` is a sufficient reconstruction threshold, not a necessary one. Exact prime-support recovery supplies no critical spectral parameter, Gamma factor, functional-equation constraint or zero-location theorem. The result is an information/classification boundary for the Prime-Circle hierarchy, not progress from source recovery to RH.