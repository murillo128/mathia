# MI-054 — Index-adapted Whittaker sampling has one critical scale, and exact diagonal Hecke equivariance forces it

**Evidence level:** exact synthesis from [WP-368](../../findings/WP-368-bounded-source-fixed-whittaker-scale-forms-have-exponential-arithmetic-index-tails.md), [WP-369](../../findings/WP-369-power-law-cusp-sampling-has-a-unique-critical-whittaker-scale-that-factorizes.md), and [WP-370](../../findings/WP-370-hecke-equivariant-whittaker-sampling-forces-the-critical-factorized-ray.md), interpreted against the homogeneous-globalization obstructions WP-366--WP-367.

WP-366--WP-368 create a two-sided scale trap for componentwise positive Whittaker geometry. Exact common homogeneous globalization Mellin-separates the finite--archimedean carrier, while a bounded positive readout at fixed `Y>=Y_*>0` preserves literal `nY` incidence only by exponentially suppressing high arithmetic indices.

WP-369 lets the source height move with the index. For normalized Eisenstein modes there is an exact reduction

`w_(r,n)(Y_n)=lambda_r(n)n^(-1/2) Psi_r(t_n)`, with `t_n=nY_n`.

Thus the Weil-shaped half-density is a kinematic factor of the Whittaker normalization; all surviving finite--archimedean information sits in the profile `Psi_r(t_n)`. To keep that profile unsuppressed, `t_n` must avoid both zero and infinity.

For the power family `Y_n=c n^(-alpha)`, this becomes a sharp trichotomy. If `alpha<1`, `t_n->infinity` and stretched-exponential decay kills the carrier. If `alpha>1`, `t_n->0` and the normalized amplitude is `o(n^(-1/2))` (up to the logarithmic `r=0` case). The unique critical power is `alpha=1`.

But at that unique scale the mixed coordinate freezes: `t_n=c`. The sampled mode becomes

`B_r(c) lambda_r(n)n^(-1/2)`,

so finite and archimedean factors separate exactly. Canonical boundary `L^2` positivity then produces `|lambda_r(n)|^2/n`, whose Eisenstein Rankin--Selberg series diverges. The half-density survives linearly only before positivity; the clean positive closure squares it and loses the required Weil carrier.

WP-370 asks whether this factorization was merely an artifact of choosing a pure power law rather than a consequence of the intrinsic source symmetry. On the smooth finite-Fourier cusp core, let a diagonal sampler be `(R_Ya)_n=a_n(Y_n)`. Exact intertwining with the Petersson-normalized prime Hecke action,

`R_Y T_p = H_p R_Y` for every prime `p`,

holds if and only if

`Y_(pm)=Y_m/p`.

Multiplying by `pm` gives `t_(pm)=t_m`; prime factorization then forces

`Y_n=c/n`, `t_n=c`.

So exact diagonal Hecke naturality does not generate a source-forced nonconstant transition sequence. It rigidifies the sampler onto precisely the unique critical factorized ray already isolated by WP-369. If the common Bessel factor is nonzero, the result is again `B_r(c)lambda_r(n)n^(-1/2)`; if it vanishes, the sampled channel is null.

The reusable lesson is stronger than “moving a scale can neutralize the coupling.” A naturality condition can itself **force the neutralizing scale**. When a proposed source-adapted section is required to intertwine the source's exact correspondence, solve that covariance equation before crediting the section with new mixed information. Here the Hecke recurrence collapses all diagonal transition coordinates to one constant.

The remaining Whittaker escape is therefore more specific than “let the scale move” or “derive the scale from Hecke symmetry.” A nonconstant transition sequence `t_n=nY_n` staying in a compact positive range must either break exact diagonal Hecke equivariance for a mathematically justified reason, or arise from a genuinely cross-index/operator-valued construction where Hecke covariance acts on the full object rather than on independent point samples. Any positive closure must then preserve a source-specific sign mechanism before diagonal squaring.

**Boundary.** WP-370 classifies diagonal point samplers that exactly intertwine all prime Hecke branches on the smooth cusp core. It does not rule out cross-index kernels, vector/operator-valued samplers, weaker or twisted equivariance, controlled unbounded operators, cohomological/intersection forms, or independent sign theorems. It supplies no RH consequence and does not generate the Mangoldt logarithm intrinsically.
