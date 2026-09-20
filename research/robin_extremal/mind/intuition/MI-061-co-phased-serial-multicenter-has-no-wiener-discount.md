# MI-061 — Same-ray serial multi-center predictors have exact multiplicative Wiener cost

**Evidence level:** exact synthesis from [RE-237](../../findings/RE-237-co-phased-single-center-cascades-have-exact-multiplicative-wiener-cost.md), building on the single-center coefficient phase law of RE-220 and the predictor-cost boundary RE-229--RE-236.

For a normalized truncated negative-binomial single-center factor with center `a_r=rho_r e^(i phi)`, the coefficient at relative degree `j` has the form

`gamma_r omega^j B_(r,j)`,

where `B_(r,j)>0` and `omega=-e^(-i phi)`. Thus every factor whose center lies on the same complex ray has the same relative one-dimensional phase character.

When such factors are multiplied, every convolution path contributing to one output degree `j` carries the same phase `omega^j`. There is no internal coefficient cancellation. For every finite same-ray cascade

`G=prod_r F_r`,

RE-237 proves the exact identities

`||G||_A = prod_r ||F_r||_A`

and, in the delay-measure representation,

`||mu_1 * ... * mu_J||_(TV) = prod_r ||mu_r||_(TV)`.

The minimum delays add. If each factor is itself a valid predictor on the same arc, then the normalized cascade Wiener rate is exactly the minimum-delay-weighted average of the constituent rates. Serial composition therefore cannot improve on the best stage. Repeating or mixing positive-real/same-ray single-center predictors creates architectural multiplicity without a new cost-reduction mechanism.

The mechanism is specifically **phase coherence before the absolute-value norm**. The generic Wiener algebra inequality can be strict only when convolution paths reaching the same coefficient have different phases. RE-237 supplies an explicit different-phase finite example where the middle coefficient cancels and the product norm is strictly submultiplicative, confirming that the common-ray hypothesis is not cosmetic.

The reusable discriminator for multi-component prediction is therefore not the number of centers but the final coefficient interference geometry. Before crediting a multi-center construction, write the output coefficients as sums over component paths and ask whether those paths are co-phased after normalization. If yes, serial composition cannot create a Wiener discount. If not, quantify the surviving cancellation together with the predictor constraint; generic submultiplicativity alone does not show that the cheaper product still predicts.

**Boundary.** The exact multiplicative law covers centers on one common ray. The rate corollary additionally assumes the factors are individually successful predictors. Different-phase products, parallel/additive/minimax synthesis, or deliberately coupled products whose factors are not predictors remain open. Strict algebraic submultiplicativity is only a necessary opportunity for an improved predictor, not evidence that such an architecture reaches a better separated-prediction constant.