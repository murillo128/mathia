# MI-032 — Canonical Green slicing selects one universal Hilbert band; source detail survives only relatively

**Evidence level:** exact/classical-mechanism synthesis from [PC-316](../../findings/PC-316-cross-level-poisson-products-generate-mordell-tornheim-packets.md), [PC-319](../../findings/PC-319-small-mordell-tornheim-coupling-preserves-off-critical-zeros.md)--[PC-321](../../findings/PC-321-large-mordell-tornheim-exponent-is-zero-free-on-right-polyhalfplane.md), and [PC-322](../../findings/PC-322-canonical-green-slice-is-classical-hilbert-criticality.md)--[PC-323](../../findings/PC-323-cross-level-green-spectral-lift-is-one-universal-hilbert-band.md).

The canonical cross-level field of PC-316 contains a continuous additive exponent `u` through `(k+l)^(-u)`. PC-319--PC-321 show that its two easy limits fail oppositely: off-critical zeros persist near `u=0`, while sufficiently large `Re u` isolates the unique lowest output mode and removes zeros from the right polyhalf-plane.

PC-322 identifies a non-fitted intermediate value. Ordinary downstream Green inversion forces `u=1`, where `K_1(k,l)=1/(k+l)` is exactly the classical Hilbert kernel. This is the real `ell^2` transition: `0<u<1` is unbounded, `u=1` bounded noncompact, and `u>1` Hilbert--Schmidt. The accompanying vector threshold `Re s=1/2` occurs for every nonzero periodic source, so the critical axis is matched-control universal.

PC-323 asks whether retaining the **full cross-level operator** instead of one matrix coefficient restores arithmetic structure. For bounded periodic sources `a,b`, residue grouping gives

`X_(a,b)=A_(a,b) tensor H_1 + S`,  with `S` trace class,

and the finite channel matrix is rank one:

`A_(a,b)=L^(-1) a_L b_L^T`.

Its only nonzero singular value is `c_(a,b)=sqrt(mu_a mu_b)`, the product of the two RMS source norms. The canonical self-adjoint dilation therefore has essential spectrum

`[-pi c_(a,b), pi c_(a,b)]`

with one positive and one negative Hilbert absolutely-continuous branch. For the canonical `(5,7)` pair this is `[-pi sqrt(2/7), pi sqrt(2/7)]`.

Thus operator lifting retains more information than scalar evaluation, but the **continuous spectral core still forgets the detailed periodic source pattern**. All detailed arithmetic is pushed into a trace-class relative defect. Because the operator is noncompact, an ordinary absolute Fredholm determinant is unavailable; the first canonical determinant-like object that can remain source-sensitive is a perturbation determinant or scattering/spectral-shift invariant **relative to the universal Hilbert core**.

The reusable distinction is now three-stage. Canonicality can select `u=1`; Hilbert geometry can select a `1/2` boundary; and even the full self-adjoint operator can retain only a universal one-band absolutely-continuous core. None of these selects Riemann zeros. Source specificity, if any, must live in the trace-class relative data, discrete/singular spectrum, or a different nonseparable operator construction whose leading residue channel is not rank one.

Any continuation of this packet route should therefore formulate the destination **after subtracting the universal Hilbert channel**. A proposed relative determinant must be audited for its actual divisor and matched periodic controls before any analogy with zeta zeros is made.

**Boundary.** PC-323 does not classify the complete spectrum of the trace-class perturbation, prove that its relative determinant has a zeta-like divisor, or rule out source-forced operators outside the Green kernel. It closes the direct inference from canonical Green lifting to a new arithmetic continuous spectrum or absolute determinant.