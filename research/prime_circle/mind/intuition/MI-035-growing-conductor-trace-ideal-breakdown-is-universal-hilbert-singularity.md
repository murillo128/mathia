# MI-035 — Growing-conductor trace-ideal breakdown is a universal Hilbert singularity

**Evidence level:** exact synthesis from [PC-323](../../findings/PC-323-cross-level-green-spectral-lift-is-one-universal-hilbert-band.md), [PC-325](../../findings/PC-325-green-relative-spectrum-is-phase-gauge-and-autocorrelation-only.md), [PC-326](../../findings/PC-326-relative-green-determinant-has-summable-edge-gap-divisor.md), and [PC-327](../../findings/PC-327-band-normalized-green-defect-has-universal-schatten-divergence.md).

At fixed conductors, the canonical cross-level Green pair is one universal Hilbert channel plus a trace-class defect, so its off-band relative zeros obey the `ell^1` edge-gap budget of PC-326. It was therefore natural to ask whether a growing-conductor limit could become more flexible because the normalized comparison defect ceases to have a uniform trace-ideal bound.

PC-327 shows that this loss of uniformity is real but not arithmetic. If `c=sqrt(mu_a mu_b)` normalizes the essential Hilbert band and `m=min(q,r)`, then every nonzero pair of centered periodic source masks satisfies

`||S||_2^2/c^2 >= (1/4) log(m/128)`

for large `m`, and the corresponding self-adjoint defect has diverging normalized `S_2` and `S_1` budgets. The mechanism comes from the universal singular behavior of shifted generalized-Hilbert matrices as their offset approaches zero.

The source only chooses a convex mixture of those shifted universal grids. Matched centered non-arithmetic masks pay the same lower divergence after the same band normalization. Therefore **nonuniform trace-class control is a background singularity of the representation, not a Prime-Circle fingerprint**.

This changes the admissible growing-conductor question. One cannot credit the disappearance of the fixed-conductor `ell^1` budget as arithmetic progress by itself. A useful limit must first identify and subtract, renormalize or quotient the universal generalized-Hilbert singular floor, then prove that the residual depends on source structure not reproduced by matched controls. Only that residual could plausibly support a new spectral-density or zeta-zero theorem.

The result also prevents the converse overinterpretation. A diverging upper trace budget does not force a diverging number or mass of actual bound states; PC-326 supplies an upper constraint, not an equality. What has been proved is only that the old fixed-conductor compactness budget cannot remain uniform after intrinsic band normalization, and that this failure is universally geometric.

**Boundary.** PC-327 does not classify every renormalized spectral-shift limit, exclude a genuinely nonseparable phase-sensitive operator, or prove that every source-dependent excess above the universal floor is trivial. The open object is precisely such a matched-control-resistant residual, still subject to the autocorrelation quotient and the need for an independent zero-sensitive destination theorem.