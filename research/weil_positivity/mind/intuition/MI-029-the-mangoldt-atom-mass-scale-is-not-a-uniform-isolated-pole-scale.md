# MI-029 — The Mangoldt atom-mass scale is not a uniform isolated-pole scale

**Evidence level:** exact literature-backed support-side obstruction from [WP-315](../../findings/WP-315-mangoldt-atom-mass-blowups-are-not-locally-radon-precompact.md), combining the positive Mangoldt Herglotz source of WP-304--WP-314 with Maynard's unconditional bounded prime-cluster theorem

WP-314 shows that a Julia node moving to infinity on the empty positive side has a universal logarithmic tangent: the density-one source overwhelms arithmetic fluctuations. The natural source-sensitive alternative is to move to the reflected arithmetic support and scale around a prime pole by its intrinsic Mangoldt atom mass

`a_p=log p/(p+1) ~ log p/p`.

WP-315 proves that this canonical mass scale does not produce a uniform local one-pole geometry. For the translated normalized measure

`nu_p(B)=a_p^(-1) mu(log p + a_p B)`,

Maynard's bounded prime clusters imply, for every fixed `r>0`,

`limsup_(p->infinity) nu_p((-r,r)) = infinity`.

The reason is quantitative: bounded additive prime gaps become `o(a_p)` after passing to logarithmic coordinates, while neighboring prime masses remain asymptotically comparable with `a_p`. Arbitrarily many order-one normalized atoms can therefore collapse into every fixed mass-scale neighborhood. The family is not uniformly locally bounded and hence not locally Radon-precompact.

The Herglotz field inherits the same blow-up. At height `a_p` above the reflected pole, every prime in a bounded cluster contributes asymptotically one unit to `Im m`; along growing clusters the normalized response diverges. Even a two-sided adjacent-gap repair fails at this scale: bounded triples give neighboring support gaps `o(a_p)` on both sides, so a regular node constrained to an adjacent gap must move on a strictly smaller scale.

The reusable distinction is **atom weight versus local support spacing**. A positive atomic source may supply a canonical mass at each pole without supplying a canonical isolated-pole tangent. When support points cluster more tightly than the mass scale, scalar local reduction must either adapt to the actual gap, treat several poles collectively, or renormalize by cluster mass. Each choice introduces new source information that is absent from the single-atom invariant.

This brackets the scalar moving-node search. Empty-side scaling is too universal; support-side single-atom mass scaling is too noncompact. A surviving scalar route must derive a spacing-adapted or collective multi-pole normalization and then show that its positive limit still carries the required archimedean/Gamma discriminator. Otherwise the category must change to matrix/operator-valued or explicitly finite--archimedean coupled structure.

**Boundary.** WP-315 does not say every mass-scaled subsequence diverges, that no regular point exists at distance comparable with `a_p`, or that every gap-adapted scaling fails. Sparse subsequences, farther gaps and cluster-dependent normalizations remain possible. The result is a no-go for a uniform single-atom tangent forced solely by the canonical Mangoldt mass, not a no-go for all support-side moving reductions and not a Weil-positivity theorem.