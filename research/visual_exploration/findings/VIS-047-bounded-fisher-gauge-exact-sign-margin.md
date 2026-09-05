# VIS-047 — bounded Fisher gauge families have an exact signed-cross-mass sign criterion

## Claim

Let `Omega` be a fixed finite support, let `H` be a strictly positive probability gauge on `Omega`, and let `A,B` be fixed nonzero real residual tensors. Define the baseline cellwise cross-contributions

`d_x = A_x B_x / H_x`,

and their positive and negative masses

`P = sum_(d_x>0) d_x`,

`N = -sum_(d_x<0) d_x`.

Fix `omega>=0` and consider the family of strictly positive probability gauges

`F_omega(H) = { G : osc_x log(H_x/G_x) <= omega }`.

Put `R=e^omega`. For every `G in F_omega(H)`, let `kappa_G(A,B)` be the Fisher-angle coefficient under the common gauge `G`. Then the orientation sign over the whole bounded gauge family has the exact classification

- `kappa_G>0` for every `G in F_omega(H)` iff `P>R N`;
- `kappa_G<0` for every `G in F_omega(H)` iff `N>R P`;
- `kappa_G=0` for every `G in F_omega(H)` iff `P=N=0`;
- zero orientation is attainable by some `G in F_omega(H)` iff `P<=R N` and `N<=R P`;
- both positive and negative orientations are attainable iff `P<R N` and `N<R P`.

At equality in exactly one of the last two inequalities, zero and only one strict sign are attainable.

When `P+N>0`, define the signed cross-mass margin

`q_H(A,B) = (P-N)/(P+N)`.

Then the universal sign criteria are equivalently

`q_H > tanh(omega/2)  iff  kappa_G>0 for every G in F_omega(H)`,

`q_H < -tanh(omega/2) iff  kappa_G<0 for every G in F_omega(H)`.

Thus the `tanh(omega/2)` threshold from `VIS-045` is not only a sufficient Fisher-cosine threshold. For a fixed baseline gauge and fixed residual tensors, the same threshold is **exact** after replacing the cosine by the signed `L1` cross-contribution margin `q_H`.

**Evidence/status:** `EXACT-DERIVED + REPRESENTATION CONTROL + ELEMENTARY BOX-LINEAR OPTIMIZATION + NO-NOVELTY-CLAIM`.

No claim is made that the bounded family `F_omega(H)` is scientifically canonical, that arbitrary gauges inside it should be searched after seeing data, that residual tensors may be recomputed as the gauge changes, or that this supplies a zeta/CUE difference or an RH criterion.

## 1. Gauge normalization is projectively irrelevant to the sign

For any positive gauge `G`, write

`r_x = H_x/G_x`.

The Fisher numerator under `G` is

`G_G(A,B) = sum_x A_x B_x/G_x = sum_x d_x r_x`.

The probability normalization on `G` constrains only the overall scale of the positive ratio vector `r`, and an overall positive scale does not change this sign. More precisely, given any positive vector `u`, define

`Z = sum_x H_x/u_x`,

`G_x = (H_x/u_x)/Z`.

Then `G` is a positive probability law and

`H_x/G_x = Z u_x`.

Consequently

`sign G_G(A,B) = sign sum_x d_x u_x`.

Moreover

`osc_x log(H_x/G_x) = osc_x log u_x`.

Therefore the sign problem over `F_omega(H)` is exactly the projective problem of evaluating the linear functional

`L(u)=sum_x d_x u_x`

over all positive vectors with `max u/min u <= R`.

After positive rescaling of `u`, every such ray has a representative in the box

`1 <= u_x <= R`.

This reduction is only a sign reduction. The actual numerical Fisher numerator includes the positive normalization factor `Z`, so the interval below should not be interpreted as the literal range of numerator magnitudes over normalized gauges.

## 2. The extremal signs are determined by two box corners

On the box `1<=u_x<=R`, the linear functional `L(u)` is minimized by assigning the largest weight `R` to every negative `d_x` and the smallest weight `1` to every positive `d_x`. Hence

`min L = P - R N`.

Similarly, maximizing gives

`max L = R P - N`.

These are ordinary corner extrema of a linear function on a hyperrectangle. The box is connected and `L` is continuous, so its image is the complete interval between these two extrema.

It follows immediately that every admissible gauge gives positive orientation exactly when the minimum is strictly positive, namely `P>R N`; every gauge gives negative orientation exactly when the maximum is strictly negative, namely `N>R P`; and zero is attainable exactly when the two extrema straddle or touch zero.

If both extrema have opposite strict signs, both orientations occur and continuity supplies an intermediate zero. If one extremum is exactly zero while the other is strict, the family reaches orthogonality but does not cross it.

The only way the numerator vanishes for every admissible gauge is `P=N=0`, equivalently `A_xB_x=0` in every cell. This agrees with the unrestricted classification in `VIS-046`.

## 3. The exact threshold is a signed `L1` cross-contribution margin

Assume `P+N>0`. Since

`q_H=(P-N)/(P+N)`

and

`tanh(omega/2) = (R-1)/(R+1)`,

a direct rearrangement gives

`q_H > (R-1)/(R+1)  iff  P>R N`,

and

`q_H < -(R-1)/(R+1) iff  N>R P`.

So `q_H` is the exact scalar sign margin for the full log-ratio-oscillation ball around `H`. It measures how much positive versus negative cellwise cross-contribution exists before the allowed gauge reweighting can amplify the minority sign enough to reverse the global orientation.

The ordinary Fisher cosine under `H` is

`kappa_H = (P-N)/(||A||_H ||B||_H)`.

By Cauchy-Schwarz,

`P+N = sum_x |A_xB_x|/H_x <= ||A||_H ||B||_H`.

Therefore `q_H` and `kappa_H` have the same sign and

`|q_H| >= |kappa_H|`.

This explains the relation to `VIS-045`. Its condition

`|kappa_H| > tanh(omega/2)`

is a valid sufficient certificate because it implies the corresponding exact `q_H` inequality. But the cosine certificate can be conservative: cancellation geometry may make `|kappa_H|` small even when the signed cross-mass imbalance is still large enough to prevent a sign flip throughout the entire bounded gauge family.

## 4. The result interpolates exactly between VIS-045 and VIS-046

At `omega=0`, one has `R=1` and `F_0(H)` contains only the baseline gauge itself. The criterion reduces to

`P>N` for positive orientation and `N>P` for negative orientation,

which is simply the sign of the baseline Fisher numerator.

As `omega` grows, `R=e^omega` increases and the exact sign-stability region shrinks. In the unrestricted limit, positive orientation can survive every positive gauge only when `N=0`; negative orientation can survive only when `P=0`. This is precisely the coordinatewise sign-compatibility boundary established in `VIS-046`.

Thus the bounded and unrestricted results form one continuous picture. `VIS-045` controls **angle distortion** between comparable metrics and supplies a convenient cosine-based sufficient sign certificate. `VIS-046` classifies sign under all positive diagonal gauges. The present result gives the missing exact sign classification for the intermediate family defined by a finite likelihood-ratio oscillation budget.

## 5. Prior art and novelty boundary

The nearest specialized prior art remains the generalized Wielandt inequality of Lin and Sinnamon already anchored in `SOURCES.md` and used in `VIS-045`. It gives sharp angle distortion between two inner products from their norm-comparison constants, but it does not need the cellwise sign decomposition used here.

After the reciprocal-gauge reduction, the new calculation is elementary linear optimization on a hyperrectangle: a linear functional reaches its extrema at the sign-selected corners. This is standard convex/interval-analysis mathematics, not a new optimization theorem. A targeted literature check found no basis for claiming novelty for positive diagonal reweighting, box extrema, interval dot-product bounds, or the resulting sign test, and no such novelty is claimed.

The durable Mathia content is the exact specialization to the active Fisher-residual gauge problem and the identification of `q_H` as the sharp bounded-family sign margin. It replaces a potentially conservative sufficient criterion by an iff criterion without searching gauges numerically.

## 6. Boundary conditions and falsification

The support, residual tensors, and baseline gauge must remain fixed. Changing bins, trimming support, recomputing the Markov closure, or residualizing separately after each gauge choice changes the mathematical object rather than merely its Fisher metric.

Every gauge must be strictly positive. The family is controlled by the oscillation of `log(H/G)`, so a structural zero or support deletion lies outside the finite-`omega` problem.

The theorem classifies only the **sign** of the Fisher angle. It does not bound the full angle more sharply than `VIS-045`, and `q_H` is not itself a normalized inner-product cosine or an independent empirical signal.

Falsify the claim by finding fixed positive `H`, fixed residuals `A,B`, and a positive `G` with `osc log(H/G)<=omega` whose orientation sign contradicts the `P`/`N` inequalities above. Equivalently, a counterexample would have to violate the elementary projective box reduction or the two corner extrema.

## Research consequence

For a future frozen zeta/CUE residual-direction comparison, a predeclared bounded gauge family can now be audited without optimizing over references. Compute the baseline cellwise cross-contributions once, form `q_H`, and compare it with `tanh(omega/2)` for the declared family radius. Clearing the threshold is necessary and sufficient for sign robustness over that whole family.

Use `VIS-045` when the magnitude of angle distortion matters, and use this exact margin when the claim is only that alignment versus opposition survives the allowed gauge variation. If the exact margin does not clear the threshold, report the sign as gauge-sensitive rather than selecting a favorable reference. This closes the bounded-family sign question as one coherent representation-control result and does not require a new visualization or clue.