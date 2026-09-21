# MI-089 — Ambient cancellation helps a source family only after its weighted image pays the occupancy tariff

**Evidence level:** exact finite harmonic-analysis and CRT synthesis from [MC-446](../../findings/MC-446-source-frame-box-mean-square-has-quadratic-occupancy-threshold.md), [MC-447](../../findings/MC-447-crt-source-frame-fibers-collapse-to-shift-common-primes.md), [MC-448](../../findings/MC-448-fixed-lcm-fourier-weil-averaging-still-pays-polynomial-occupancy.md), and [MC-449](../../findings/MC-449-centered-complement-duality-closes-near-complete-fixed-lcm-escape.md), continuing the incomplete source-frame branch isolated in MC-413.

A favorable second moment on a large ambient parameter box is not automatically a favorable estimate on the arithmetic image that the source actually occupies. For primitive characters, MC-446 computes the exact full `(u,a)`-box second moment of the incomplete translated correlations. In the rough squarefree range it has root-mean-square size `sqrt(H)`, so genuine collective cancellation exists before completion.

Transferring that ambient cancellation to a weighted source family by plain Cauchy has an exact price. If equal source frames are first aggregated into weights `W(u,a)`, the relevant participation ratio is

`R_eff(W)=||W||_1^2/||W||_2^2`.

The full-box `L^2` bound can beat the pointwise `H||W||_1` estimate only when `R_eff` exceeds about `q^2/H`. MC-447 then removes two apparent ways of manufacturing that occupancy in the natural separated-modulus regime. When `d,e<=D`, `D^2<q` and `(h,q)=1`, the frame `(u,a)` recovers the exact lcm and canonical CRT residue. Same-frame ambiguity comes only from primes common to `L` and `h`; for shifts coprime to the sieve support the divisor-pair map is injective. Fixing `a=hL^(-1)` is therefore just fixing the lcm, not gaining a second free averaging coordinate.

MC-448 improves the generic tariff after the constrained coordinate is actually fixed. Fourier expansion in `u`, the mixed Weil bound and Parseval give, for prime conductor `p`,

`|T_H(W,a)| <= C sqrt(pH) ||W||_2`.

Against the pointwise bound, this asks for effective occupancy of order `p/H`, not `p^2/H`. The gain is real: fixing `a` removes one conductor power. But one clean fixed-lcm CRT slice has at most `2^omega(L)=p^(o(1))` distinct starts. Hence throughout every fixed-power incomplete range `H<=p^(1-delta)`, the actual source image is still too sparse to pay the polynomial threshold.

MC-449 closes the apparent near-complete escape in the same method. After subtracting the universal complete-period zero mode, the centered kernel satisfies the exact complement identity

`G_H(u,a) = -G_(p-H)(u-(p-H),a)`.

Thus the correct generic bound depends on `m(H)=min(H,p-H)`:

`|mathcal T_H(W,a)| <= C sqrt(p m(H)) ||W||_2`,

and the occupancy threshold is `R_eff(W) >= c p/m(H)`. Translation preserves the source occupancy. Near either endpoint the fixed-lcm slice therefore faces a polynomial deficit, while in the central range its subpolynomial support can supply at most a subpolynomial conductor saving. For one fixed lcm, **uniform mixed-Weil control followed by generic Parseval/Cauchy is power-closed for every interval length**.

The reusable lesson is to price **image occupancy after quotienting collisions, constrained coordinates, universal modes and weights**. Strong ambient or fixed-coordinate cancellation can be genuine and still be too weak on the source image. Conversely, this closure is method-specific: it discards the detailed correlation between the actual CRT-idempotent Fourier spectrum and the character multiplier.

For the current q-vdC branch, a surviving theorem must use information that MC-448--MC-449 deliberately throw away: the detailed weighted Fourier geometry of the CRT-idempotent set, cancellation across several lcm values before Cauchy, modulus factorization before scalarization, genuinely collective variable-length structure, or another nonuniform estimate correlated with the actual source coefficients. Fibre multiplicity, treating `a` as free, the generic fixed-lcm Fourier envelope, and the near-complete interval are no longer plausible conductor-power gains.

**Boundary.** These results concern prime conductor and the clean separated/coprime fixed-lcm geometry of MC-447. They do not rule out cross-lcm coupling, composite/smooth-conductor factorization, variable lengths correlated with the weights, wraparound/nonunit regimes outside the hypotheses, or estimates using the actual nonuniform Fourier multiplier. The removed complete-period scalar is source-independent coefficient/incidence structure, not restored character phase. Failure of the generic method to give a power saving is not a lower bound for the true weighted correlation, and no Mertens or individual character-sum improvement follows by itself.
