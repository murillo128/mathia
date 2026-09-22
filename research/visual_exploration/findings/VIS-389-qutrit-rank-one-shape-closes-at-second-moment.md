# VIS-389 — generic rank-one qutrit spectral shape closes at the second moment

## Claim

Continue in the generic rank-one qutrit setting of `VIS-388`. Let

`S = span(E) subset Herm_0(3)`,

with `tr(E^2)=1`, and let

`Delta_S = ad_E^* ad_E`.

Assume

`0 < tr(E^3)^2 < 1/6`,

so the three positive root-sector eigenvalues of `Delta_S` are distinct. Order them as

`0 < q_1 < q_2 < q_3`.

For any nonzero positive-spectrum Gram tangent `g`, let `P_i` denote the spectral projector of `Delta_S` onto the `q_i` root sector and define

`w_i = ||P_i g||_F^2 / ||g||_F^2`,

so `w_i>=0`, `w_1+w_2+w_3=1`, and the tangent-weighted positive spectral measure is

`mu_g = w_1 delta_(q_1) + w_2 delta_(q_2) + w_3 delta_(q_3)`.

Write its first two moments as

`m_1 = int lambda dmu_g(lambda)`,

`m_2 = int lambda^2 dmu_g(lambda)`.

Then the complete spectral measure is determined exactly by the support `{q_1,q_2,q_3}` and the pair `(m_1,m_2)`. Explicitly, for `{i,j,k}={1,2,3}`,

`w_i = [m_2 - (q_j+q_k)m_1 + q_j q_k] / [(q_i-q_j)(q_i-q_k)]`.

Since `VIS-388` shows that the unordered support `{q_1,q_2,q_3}` is itself determined by the intrinsic source invariant

`t^2 = tr(E^3)^2`,

it follows that the full tangent-weighted positive spectral distribution is determined by exactly three scalar data at this minimal generic test bed:

`t^2`, `m_1`, and `m_2`.

After conditioning on the source cubic invariant `t^2` and the scalar defect rate `m_1`, **only one independent spectral-shape degree of freedom remains**. It may be represented by the second moment `m_2`, the variance

`v = m_2 - m_1^2`,

or any equivalent one-to-one coordinate on the feasible interval below.

At the nongeneric qutrit rank-one boundaries the shape channel collapses further. When `t=0`, the positive support has only two distinct values `{1/2,2}`; when `t^2=1/6`, the positive support has only the single distinct value `3/2`. In both cases the first moment already fixes the positive spectral measure once the source support is fixed.

**Evidence/status:** `EXACT-DERIVED + MOMENT-CLOSURE CLASSIFICATION + CLASSICAL VANDERMONDE/LAGRANGE INGREDIENT + NEGATIVE CONTROL + NO-NOVELTY-CLAIM FOR FINITE-SUPPORT MOMENT INVERSION`.

## 1. The qutrit positive spectral measure is a three-atom probability law

`VIS-388` diagonalizes the rank-one qutrit source and shows that, for generic source cubic invariant, the positive part of `Delta_S` has exactly three distinct eigenvalues `q_1<q_2<q_3`, each with real multiplicity two.

The multiplicities do not create additional spectral-measure coordinates for a fixed tangent. Only the total squared norm of the tangent inside each eigenspace matters. Therefore

`w_i = ||P_i g||_F^2/||g||_F^2`

are nonnegative and sum to one, and every scale-invariant spectral statistic of `g` is a statistic of the three-atom measure `mu_g`.

The scalar defect rate from `VIS-386` is exactly

`m_1 = <g,Delta_S g>/||g||_F^2 = sum_i w_i q_i`.

Thus fixing the source and scalar defect imposes two affine constraints on the three weights: total mass one and mean `m_1`. This leaves at most one shape degree of freedom before any additional moment is measured.

## 2. A second moment recovers all three weights

For each index `i`, let `{i,j,k}={1,2,3}` and consider the quadratic Lagrange polynomial

`L_i(lambda) = [(lambda-q_j)(lambda-q_k)] / [(q_i-q_j)(q_i-q_k)]`.

Because the support points are distinct,

`L_i(q_i)=1`,

and

`L_i(q_j)=L_i(q_k)=0`.

Therefore

`w_i = int L_i(lambda) dmu_g(lambda)`.

Expanding the numerator gives

`int (lambda-q_j)(lambda-q_k) dmu_g`
` = m_2 - (q_j+q_k)m_1 + q_j q_k`,

which yields

`w_i = [m_2-(q_j+q_k)m_1+q_j q_k]/[(q_i-q_j)(q_i-q_k)]`.

This is simply inversion of the three-by-three Vandermonde system with rows corresponding to moments of order `0,1,2`. It proves uniqueness without any approximation or generic probabilistic assumption beyond distinct support.

Consequently, once `t^2` fixes the qutrit source spectrum and `m_1` fixes the scalar defect rate, the full normalized spectral CDF, every higher moment, and every root-sector weight are functions of a single additional scalar `m_2`.

## 3. Exact feasible interval for the residual shape scalar

The nonnegativity conditions `w_i>=0` give an exact allowed interval for `m_2` at fixed support and mean.

If

`q_1 <= m_1 <= q_2`,

then

`(q_1+q_2)m_1 - q_1 q_2 <= m_2 <= (q_1+q_3)m_1 - q_1 q_3`.

The lower endpoint is the two-atom law supported on `{q_1,q_2}` with mean `m_1`; the upper endpoint is the two-atom law supported on `{q_1,q_3}`.

If

`q_2 <= m_1 <= q_3`,

then

`(q_2+q_3)m_1 - q_2 q_3 <= m_2 <= (q_1+q_3)m_1 - q_1 q_3`.

Here the lower endpoint is supported on `{q_2,q_3}` and the upper endpoint again on `{q_1,q_3}`.

Subtracting `m_1^2` gives the corresponding exact interval for the spectral variance `v`.

These bounds are not concentration inequalities. They are the complete convex feasibility region for a probability law on the fixed three-point support. An observed qutrit rank-one tangent outside this interval signals an implementation, normalization, or source-identification error rather than an anomalous arithmetic effect.

## 4. The special source-cubic boundaries lose the residual degree

At `t=0`, `VIS-388` gives root-sector values

`{1/2,1/2,2}`.

After merging equal spectral atoms, the positive spectral measure has only two support points. Total mass and first moment therefore determine its two weights exactly; there is no independent second-moment shape parameter.

At `t^2=1/6`, the root-sector values are

`{0,3/2,3/2}`.

After removing the zero eigenspace as required by the `VIS-386` positive-spectrum quotient, only the single positive support value `3/2` remains. The normalized positive spectral measure is forced to be `delta_(3/2)`.

Thus the one-dimensional residual shape channel is genuinely a generic qutrit phenomenon. It disappears at both symmetry-enhanced source boundaries.

## 5. Consequence for the Wang localization clue

The accepted clue `research/visual_exploration/clues/CLUE-wang-fixed-source-packet-localization.md` asks whether the intrinsic source-subspace commutator spectrum contains source-specific organization after generator gauge, tangent-amplitude gauge, the isotropic defect-energy baseline, and the universal Markov floor are removed.

`VIS-388` showed that qutrit rank-one geometry has enough algebraic capacity for a spectral-shape channel. The present result sharply limits that capacity. In the minimal generic test bed, once a matched control preserves the source cubic invariant `t^2` and the scalar defect rate `m_1`, **the complete remaining spectral-shape comparison is one-dimensional**.

There is therefore no need to treat an arbitrary family of CDF windows, higher moments, or spectral-profile coordinates as independent evidence in `d=3,r=1`. Conditional on `(t^2,m_1)`, all of them are determined by `m_2`, equivalently by `v=m_2-m_1^2`.

A clean qutrit matched-control test should therefore pre-register a scalar residual shape statistic such as

`rho = m_2/m_1^2 - 1`

when `m_1>0`, or the unnormalized variance `v`, and match or stratify controls by `t^2` and `m_1`. If an apparent source-specific CDF anomaly disappears after this conditioning, it was only a re-expression of source conjugacy plus scalar defect energy. If a residual variance anomaly survives, the full positive spectral measure is simultaneously anomalous, but the result still requires a source-specific explanation and destination-level Wang payoff.

This is a reduction of the diagnostic search space, not evidence that such an anomaly exists.

## Prior-art and novelty audit

The mathematical inversion used here is classical finite-support moment interpolation. For known distinct support points, the weights are recovered from moments by an invertible Vandermonde system, equivalently by the quadratic Lagrange basis used above. N. Macon and A. Spitzbart, **Inverses of Vandermonde Matrices**, *American Mathematical Monthly* 65:2 (1958), 95–100, DOI `10.1080/00029890.1958.11989147`, is a classical explicit inverse-Vandermonde reference.

No novelty is claimed for Vandermonde invertibility, Lagrange interpolation, finite discrete moment recovery, or convex moment bounds on a three-point support.

The Mathia-specific contribution is the reduction of the current intrinsic qutrit Wang/source statistic to this classical three-atom structure: `VIS-388` supplies the source-cubic support parameter, while this finding proves that after conditioning on that source geometry and on scalar defect energy, the entire remaining normalized spectral shape has only one scalar degree of freedom.

## Boundaries

- The exact one-scalar closure applies to generic qutrit rank-one sources with three distinct positive root-sector values. Higher source rank or matrix dimension can have larger spectral support and need more moments or other invariants.
- The result classifies an abstract tangent-weighted spectral measure. It does not prove that an admissible Wang Gram tangent realizes any particular feasible variance.
- Matching `t^2` and `m_1` is necessary for the proposed minimal qutrit control but may not preserve every resource relevant to a destination theorem.
- An anomalous `m_2` or variance would still need matched nonarithmetic controls, stability across admissible scale/truncation changes, a structural source explanation, and full destination-cost propagation.
- No retained visualization is needed because the result is exact and representation-independent once the qutrit source spectrum is fixed.
- No RH implication or Wang strip gain is established.