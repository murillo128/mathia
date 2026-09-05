# VIS-046 — unrestricted positive Fisher gauges preserve orientation sign exactly only under coordinatewise sign compatibility

## Claim

Let `Omega` be a fixed finite support and let `A,B` be two nonzero real residual tensors on `Omega`. For every strictly positive probability gauge `H` on that support define

`G_H(A,B) = sum_(x in Omega) A_x B_x / H_x`,

with the corresponding Fisher angle coefficient

`kappa_H(A,B) = G_H(A,B) / (||A||_H ||B||_H)`.

Because the denominator is positive, the sign of `kappa_H` is the sign of `G_H`.

Put `c_x=A_x B_x`. As `H` ranges over all strictly positive probability gauges on the fixed support, the orientation sign has the following exact classification:

- `kappa_H>0` for every positive `H` iff `c_x>=0` for every `x` and `c_x>0` for at least one `x`;
- `kappa_H<0` for every positive `H` iff `c_x<=0` for every `x` and `c_x<0` for at least one `x`;
- `kappa_H=0` for every positive `H` iff `c_x=0` for every `x`;
- if the products `c_x` have both signs, then there exist positive gauges `H_+` and `H_-` with `kappa_(H_+)>0` and `kappa_(H_-)<0`, and there is also a positive gauge with `kappa_H=0`.

Equivalently, after reciprocal reparameterization of the gauge, the zero-orientation set is a hyperplane cutting the positive weight cone whenever the cellwise products have mixed sign.

Thus the common-reference warning in `VIS-041` is sharp in an unrestricted gauge family. A residual direction has a gauge-independent sign under **all** positive diagonal Fisher reweightings only when its two residual tensors agree or oppose cellwise in sign. Any genuinely mixed local agreement/opposition can be made globally aligned, orthogonal, or opposed by changing the positive gauge enough.

**Evidence/status:** `EXACT-DERIVED + REPRESENTATION CONTROL + ELEMENTARY WEIGHTED-INNER-PRODUCT GEOMETRY + NO-NOVELTY-CLAIM`.

No claim is made that arbitrary gauges are scientifically admissible, that cellwise sign compatibility is necessary for robustness inside a bounded or predeclared gauge family, that residual magnitudes are gauge-invariant, or that this gives any zeta/CUE comparison by itself.

## 1. Positive probability gauges realize every positive reciprocal-weight ray

For a positive gauge `H`, set

`w_x = 1/H_x`.

Then

`G_H(A,B)=sum_x c_x w_x`.

The probability normalization on `H` does not restrict the direction of the positive weight vector `w`. Given any vector `u` with every `u_x>0`, define

`H_x = u_x^(-1) / sum_y u_y^(-1)`.

This is a strictly positive probability law and

`1/H_x = (sum_y u_y^(-1)) u_x`.

The common scalar is positive and therefore irrelevant to the sign of the inner product. Hence allowing every positive probability gauge is exactly equivalent, for orientation sign, to allowing every positive weight ray in the open orthant.

This reciprocal parameterization is the natural geometry of the question: the numerator is the linear functional

`L_c(w)=sum_x c_x w_x`

on the positive cone.

## 2. Coordinatewise sign compatibility is sufficient and necessary

If all `c_x>=0` and at least one is strictly positive, then every term in `L_c(w)` is nonnegative and at least one is positive for every positive `w`. Thus `G_H>0` for every gauge. The negative case is identical after multiplying by `-1`, and `c=0` gives exact orthogonality for every gauge.

Conversely suppose there are cells `p,n` with

`c_p>0`,  `c_n<0`.

Take positive weights with `w_p=t` and all other weights fixed at `1`. For sufficiently large `t`,

`L_c(w)=t c_p + sum_(x != p) c_x >0`.

Similarly, making `w_n=t` and keeping the others at `1` makes `L_c(w)<0` for sufficiently large `t`. By the reciprocal construction above, both weight vectors come from strictly positive probability gauges.

The positive orthant is connected and `L_c` is continuous. Along any continuous path between a positive-sign and negative-sign weight vector, `L_c` therefore vanishes at some positive weight. The corresponding gauge gives exact Fisher orthogonality.

So mixed cellwise signs are not merely a warning that a sign flip might occur: they are exactly the condition under which unrestricted positive gauge choice can realize both orientation signs and a zero crossing.

## 3. The gauge-space picture is a hyperplane cut of the positive cone

In reciprocal-weight coordinates the orthogonality locus is

`sum_x c_x w_x = 0`,  with `w_x>0`.

This is the intersection of one linear hyperplane with the positive orthant. It is empty when `c` lies in the positive or negative closed orthant apart from the zero vector, equals the whole cone only when `c=0`, and cuts the cone into positive- and negative-orientation regions exactly when `c` has mixed signs.

This gives a representation-independent visual interpretation of gauge sensitivity. The complicated-looking movement of a Fisher angle under reweighting is, at the level of its sign, just movement through two convex sign regions separated by a linear wall in reciprocal-gauge coordinates.

The statement concerns only the **sign**. The normalized value `kappa_H` also depends on the gauge-weighted norms of `A` and `B`, so its level sets are not the same hyperplanes.

## 4. Relation to the bounded-gauge control in VIS-045

`VIS-045` proves a complementary local/global robustness statement. If two positive gauges `H,G` have bounded log-ratio oscillation

`omega = max_x log(H_x/G_x) - min_x log(H_x/G_x)`,

then the Fisher angle can move only inside the generalized-Wielandt half-angle bound, and a baseline sign is certified whenever

`|kappa_H| > tanh(omega/2)`

with the corresponding sign.

The present result describes what happens when no such envelope is imposed. Letting the admissible likelihood-ratio spread become arbitrarily large sends that coarse threshold to `1`, so no nontrivial sign certificate based only on one baseline cosine can survive over the entire positive-gauge simplex. The exact residual tensors still contain a stronger exceptional certificate: coordinatewise sign compatibility makes the sign invariant for every positive gauge, however extreme.

These are different controls rather than competing criteria. `VIS-045` is useful for a scientifically predeclared family of reasonably comparable gauges even when cellwise products have mixed signs. `VIS-046` identifies the sharp boundary for claiming that orientation sign is intrinsic under **all** positive diagonal Fisher gauges.

## 5. Prior art and novelty boundary

Weighted positive inner products and their metric-dependent angles are classical linear algebra, and `VIS-045` already anchors the broader two-inner-product angle-distortion problem to Lin and Sinnamon's generalized Wielandt inequality. A targeted search for equivalent positive-diagonal-weight formulations exposes the standard fact that positive reweighting can reverse a vector cross-inner-product; no novelty is claimed for that phenomenon, positive diagonal forms, cone separation, or weighted dot products.

The durable Mathia content is the exact specialization needed by the active residual-orientation program: because Fisher gauges enter as reciprocal cell weights, the unrestricted sign question reduces completely to one linear functional on the positive cone. That closes the ambiguity between “reference-dependent” and “arbitrarily reference-dependent”: bounded gauge families have the quantitative stability control of `VIS-045`, while the unrestricted family has the exact coordinatewise classification above.

## 6. Boundary conditions and falsification

The support must remain fixed and every gauge must be strictly positive. Allowing gauge-dependent deletion of cells changes the vector space and is not a diagonal reweighting of the same residuals.

The residual tensors themselves must also remain fixed while the gauge varies. Recomputing the Markov closure, changing bins, changing support, or selecting a process-specific residualization rule mixes a different statistical object into the gauge question.

Cellwise products may vanish without affecting the classification. The strictly positive and strictly negative alternatives require only that at least one nonzero product exists and that every nonzero product has the same sign.

Falsify the claim by exhibiting fixed finite nonzero `A,B` with mixed signs among `A_xB_x` for which no positive gauge produces one of the two signs, or by exhibiting coordinatewise nonnegative products for which a positive gauge makes `G_H<=0`. Either example would contradict the elementary positive-weight reduction above.

## Research consequence

A future zeta/CUE residual-direction comparison should not describe the sign of `kappa_H` as gauge-independent merely because several convenient references agree. Under an unrestricted positive gauge family, such a statement is justified only by coordinatewise sign compatibility of the two fixed residual tensors.

For the scientifically relevant case with mixed local agreement and opposition, freeze the primary gauge and predeclare a bounded alternative family, then use `VIS-045`'s `K_V` or log-ratio-oscillation certificate. If the family is allowed to expand without a quantitative likelihood-ratio bound, sign optimization is representation choice rather than evidence of a process-level geometric agreement.

This closes one coherent continuation of the common-gauge branch and requires no new visualization or clue.