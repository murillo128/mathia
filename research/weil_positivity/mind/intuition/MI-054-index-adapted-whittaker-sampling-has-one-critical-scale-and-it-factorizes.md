# MI-054 — Index-adapted Whittaker sampling has one critical power scale, and it factorizes

**Evidence level:** exact synthesis from [WP-368](../../findings/WP-368-bounded-source-fixed-whittaker-scale-forms-have-exponential-arithmetic-index-tails.md) and [WP-369](../../findings/WP-369-power-law-cusp-sampling-has-a-unique-critical-whittaker-scale-that-factorizes.md), interpreted against the homogeneous-globalization obstructions WP-366--WP-367.

WP-366--WP-368 create a two-sided scale trap for componentwise positive Whittaker geometry. Exact common homogeneous globalization Mellin-separates the finite--archimedean carrier, while a bounded positive readout at fixed `Y>=Y_*>0` preserves literal `nY` incidence only by exponentially suppressing high arithmetic indices.

WP-369 lets the source height move with the index. For normalized Eisenstein modes there is an exact reduction

`w_(r,n)(Y_n)=lambda_r(n)n^(-1/2) Psi_r(t_n)`, with `t_n=nY_n`.

Thus the Weil-shaped half-density is a kinematic factor of the Whittaker normalization; all surviving finite--archimedean information sits in the profile `Psi_r(t_n)`. To keep that profile unsuppressed, `t_n` must avoid both zero and infinity.

For the power family `Y_n=c n^(-alpha)`, this becomes a sharp trichotomy. If `alpha<1`, `t_n->infinity` and stretched-exponential decay kills the carrier. If `alpha>1`, `t_n->0` and the normalized amplitude is `o(n^(-1/2))` (up to the logarithmic `r=0` case). The unique critical power is `alpha=1`.

But at that unique scale the mixed coordinate freezes: `t_n=c`. The sampled mode becomes

`B_r(c) lambda_r(n)n^(-1/2)`,

so finite and archimedean factors separate exactly. Canonical boundary `L^2` positivity then produces `|lambda_r(n)|^2/n`, whose Eisenstein Rankin--Selberg series diverges. The half-density survives linearly only before positivity; the clean positive closure squares it and loses the required Weil carrier.

The reusable lesson is that **moving a scale to rescue an amplitude can neutralize the coupling that gave the representation meaning**. A critical exponent is not enough: inspect the scale-free coordinate left after normalization. If the only unsuppressed scaling makes that coordinate constant, the apparent mixed representation has collapsed to a tensor product before the sign problem is addressed.

The remaining Whittaker escape is more specific than “let the scale move.” A nonconstant transition sequence `t_n=nY_n` must stay in a compact positive range, be generated canonically by the source rather than fitted to target coefficients, and enter a global sign mechanism that acts before diagonal squaring. Cross-index/operator-valued or cohomological structure remains outside the componentwise classification.

**Boundary.** WP-369 classifies pure power-law sampling and the exact critical ray `Y_n=c/n`; it does not rule out source-forced nonconstant `t_n`, cross-index forms, controlled unbounded operators or independent sign theorems. It supplies no RH consequence and does not generate the Mangoldt logarithm intrinsically.