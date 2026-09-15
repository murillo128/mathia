# MI-031 — Common ramification shifts collective capacity into radical size or totient roughness

**Evidence level:** exact/literature-derived selected-family capacity dichotomy from [MC-304](../../findings/MC-304-fixed-ramification-radical-capacity-dichotomy.md), refining the multiquadratic packaging in [MC-303](../../findings/MC-303-multiquadratic-packaging-turns-source-cost-into-discriminant-complexity.md)

The independent selected quadratic characters do not carry unrelated conductors. If `U` is the union of their lower-prime supports and `P=prod_(p in U) p`, then every selected character has primitive conductor dividing the same squarefree radical `P`. For the generated rank-`R` family `X`, each ramified prime occurs in exactly half of the `2^R` characters, so the multiquadratic discriminant factorization is exactly

`|D_K| = P^(2^(R-1))`.

Thus the large field discriminant found in MC-303 can arise from exponential degree replication of one finite ramification set. Field discriminant and ramification-radical size are different source currencies.

The fixed-radical organization also sharpens the collective shell-capacity estimate. For the selected family energy `E_X`, MC-304 obtains a bound with two competing capacities: reduced-residue density `phi(P)/P`, and a sparse-character collision term of size controlled by `2^R sqrt(P) log(2P)/y`. Against the reciprocal endpoint energy `E_X=2^R/R`, every endpoint partition must therefore pay at least one of two costs:

`phi(P)/P >> 2^R/(R log y)`

or

`sqrt(P) log(2P) >> y/(R log y)`.

At the blind-support floor `R=log_2 log y+o(log log y)`, the second branch forces `P>=y^(2-o(1))`, while the first says that the common radical must remain sufficiently totient-rough, at roughly the `1/R` scale up to the stated subpower slack.

This is the source-specific refinement missing after MC-303. **Putting all modes into one ramification radical does not remove the factor-`R` capacity gap; it splits the possible escape into two explicit arithmetic currencies.** A closing theorem can now target either the reduced-residue density of the actual common radical or its size, rather than ask abstractly for stronger multiquadratic mixing.

**Boundary.** MC-304 gives necessary conditions for the reciprocal endpoint model, not a contradiction. Existing source-cost information rules out neither the totient-rough branch nor a near-quadratic radical. The Page-induced discriminant lower bound only forces `P=y^(o(1))` at the critical rank, so it cannot be substituted for the much stronger `P>=y^(2-o(1))` capacity branch. No Mertens estimate follows.