# VIS-055 — exact two-ratio Fisher angle is a global sign quotient of the gauge contrast

## Claim

Assume the nondegenerate two-ratio Fisher configuration of `VIS-049` and the exact one-coordinate finite-gauge reduction of `VIS-050`, with `0<|kappa|<1`. Along one fixed real log-gauge direction `h`, write

`A(s)=kappa_h(s)=F(q(s))`,

where

`F(q)=kappa cosh(q/2)/sqrt(1+kappa^2 sinh(q/2)^2)`

and `q=q_h` is the class log-moment contrast. Then the exact Fisher-angle representation loses precisely the orientation of `q`, not its magnitude.

For every finite real `q`,

`|kappa| <= |F(q)| < 1`,

and the magnitude of the hidden gauge contrast is recovered exactly from the Fisher cosine by

`|q|
 = 2 asinh sqrt[(A^2-kappa^2)/(kappa^2(1-A^2))]`.

Consequently:

1. The scalar map `q -> F(q)` is exactly two-to-one away from `q=0`: `F(q_1)=F(q_2)` if and only if `q_2=q_1` or `q_2=-q_1`.

2. If `q_1,q_2` are real-analytic contrasts on one connected real interval and generate the same exact Fisher curve, then either `q_2=q_1` everywhere or `q_2=-q_1` everywhere. Arbitrary pointwise sign choices are incompatible with analyticity. Thus an exact gauge-sweep curve determines the entire analytic contrast path up to one **global orientation bit**.

3. One signed observation at any nonbalance point, for example `sign D_h(s_*)` with `D_h=M_P-M_M` from `VIS-052`, fixes that global branch because `sign q=sign D_h`. After that one bit is supplied, the exact Fisher curve determines `q(s)` everywhere on the connected interval.

4. This exact recoverability is not numerically uniform. With `u=|A|` and `k=|kappa|`, the inverse is singular at both representation boundaries. Near balance,

   `u-k = [k(1-k^2)/8] q^2 + O(q^4)`,

   so recovering `|q|` from vertical angle error has the square-root conditioning quantified in `VIS-054`. At the opposite extreme,

   `1-u^2 ~ [4(1-k^2)/k^2] exp(-|q|)`

   as `|q| -> infinity`, so very large class imbalance is exponentially compressed by saturation of the normalized angle.

5. On every compact contrast annulus `q_0 <= |q| <= Q` with `0<q_0<Q<infinity`, the inverse is ordinarily Lipschitz because

   `d|F(q)|/d|q|
    = [k(1-k^2)/2] sinh(|q|/2)
      / [1+k^2 sinh(|q|/2)^2]^(3/2)`

   is continuous and strictly positive there. The information loss is therefore concentrated at the exact-balance quotient and at extreme cosine saturation, rather than being a generic loss throughout the one-dimensional gauge coordinate.

**Evidence/status:** `EXACT-DERIVED + REPRESENTATION CONTROL + INFORMATION-LOSS CLASSIFICATION + NEGATIVE/OBSTRUCTION + NO-NOVELTY-CLAIM`.

No claim is made that empirical zeta/CUE residuals satisfy the exact two-ratio model, that a noisy angle curve permits stable branch recovery, or that the elementary inversion of this one-dimensional weighted-cosine formula is a new general theorem.

## 1. The Fisher cosine determines the absolute contrast exactly

Put

`y=sinh(q/2)^2 >= 0`.

Squaring the exact formula from `VIS-050` gives

`A^2 = kappa^2 (1+y)/(1+kappa^2 y)`.

Solving for `y` yields

`y = (A^2-kappa^2)/(kappa^2(1-A^2))`.

For finite real `q`, the denominator is positive and `A` has the same sign as `kappa`; moreover `|A|=|kappa|` only at `q=0` and `|A|` increases strictly toward one with `|q|`. Since `y=sinh(|q|/2)^2`, inversion gives

`|q|
 = 2 asinh sqrt[(A^2-kappa^2)/(kappa^2(1-A^2))]`.

Thus the angle does not destroy the scale of the class imbalance on the exact two-ratio locus. Its pointwise quotient is exactly the reflection symmetry

`q <-> -q`.

This sharpens the negative statement in `VIS-054`. Fisher normalization squares away the **sign** near every balance return, but the exact noiseless scalar still contains the full magnitude of the one-coordinate imbalance.

## 2. Analyticity reduces pointwise sign ambiguity to one global bit

Suppose two real-analytic contrasts `q_1,q_2` on a connected interval satisfy

`F(q_1(s))=F(q_2(s))`

for every `s`. The inverse formula gives

`|q_1(s)|=|q_2(s)|`,

hence

`q_1(s)^2=q_2(s)^2`.

Therefore the analytic product

`(q_2-q_1)(q_2+q_1)`

vanishes identically. The ring of real-analytic functions on a connected interval has no zero divisors: if one factor is nonzero at a point, it remains nonzero on a neighborhood there and forces the other factor to vanish on that neighborhood, after which analytic continuation makes that identity global. Hence

`q_2=q_1`

throughout the interval or

`q_2=-q_1`

throughout the interval.

Equivalently, the contact multiplicities visible in the Fisher curve are already sufficient to prevent arbitrary branch flips at separate balance returns. The exact path does not lose one sign bit per return or per connected component of the complement of the zero set; it loses one global orientation choice for the analytic contrast.

## 3. One signed balance observation fixes the branch

`VIS-052` writes

`q(s)=log[M_P(s)/M_M(s)]`,

`D_h(s)=M_P(s)-M_M(s)`

with both moment sums strictly positive. Therefore

`sign q(s)=sign D_h(s)`

whenever the two are nonzero.

Choose any point `s_*` that is not an exact balance return. The Fisher curve gives `|q(s_*)|`; one observation of `sign D_h(s_*)` selects either the `+|q|` or `-|q|` analytic branch. By the preceding section, that single choice determines the branch globally on the connected gauge interval.

This identifies the minimal exact augmentation of the scalar visualization on the two-ratio locus: retain the Fisher curve together with one orientation bit. A complete second signed curve is not mathematically necessary for exact reconstruction of `q`, although it can be far more stable empirically.

The statement concerns the log-moment **ratio** `q`. It does not reconstruct the individual class moment sums `M_P,M_M`, nor the magnitude of `D_h`, because multiplying both moment sums by the same positive function leaves `q` unchanged.

## 4. Exact invertibility and noisy identifiability are different questions

For `q>0`, differentiate the magnitude form of the exact map. With `k=|kappa|`,

`U(q)=|F(q)|
 = k cosh(q/2)/sqrt[1+k^2 sinh(q/2)^2]`.

Direct differentiation gives

`U'(q)
 = [k(1-k^2)/2] sinh(q/2)
   / [1+k^2 sinh(q/2)^2]^(3/2)`.

This is strictly positive for every `q>0`, proving ordinary local invertibility away from balance. On a compact annulus `q_0<=q<=Q`, its positive minimum supplies a finite inverse-Lipschitz constant.

At balance, however, `U'(0)=0` and the first nonzero term is quadratic:

`U(q)-k = [k(1-k^2)/8] q^2+O(q^4)`.

That is exactly the square-root inverse instability behind `VIS-054`; exact information survives, but finite vertical error erases first-order location information.

There is a second compression regime at large imbalance. Since

`1-U(q)^2
 = (1-k^2)/[1+k^2 sinh(q/2)^2]`,

and `sinh(q/2)^2 ~ exp(q)/4`, one has

`1-U(q)^2
 ~ [4(1-k^2)/k^2] exp(-q)`.

Thus increasingly different class moment ratios are packed exponentially close to the saturated cosine magnitude one. The exact inverse still exists, but finite-precision angle measurements become progressively poor coordinates for large `|q|` as well.

## 5. Prior art and novelty boundary

Angles induced by inner products, Fisher/statistical angles, Bhattacharyya-type spherical representations, and the dependence of cosine similarity on metric or gauge choices are classical. The line's existing source anchors already bound that background: Lin and Sinnamon's generalized Wielandt inequality supplies the sharp generic angle-distortion control used in `VIS-045`, while `VIS-050` records neighboring diagonal-gauge/cosine-similarity literature and derives the exact two-ratio reduction used here.

A targeted check of statistical-angle/Bhattacharyya and weighted-cosine literature did not supply a theorem needed for this result. The present statement is elementary algebra and real-analytic branch uniqueness applied to the already-derived `VIS-050` formula. No novelty is claimed for inverse-function conditioning, analytic uniqueness, Fisher/Bhattacharyya geometry, or cosine similarity.

The durable Mathia contribution is the exact representation diagnosis: on the exceptional two-ratio locus, the Fisher visualization is neither fully information-preserving nor generically destructive. It is precisely a `Z_2` quotient of the source-sensitive gauge contrast, with severe conditioning at balance and saturation.

## 6. Boundary conditions and falsification

All hypotheses of `VIS-050` remain active: finite fixed support, fixed residual tensors, positive gauges, exact reciprocal two-ratio classes, one fixed real log-gauge direction, and `0<|kappa|<1`. Rebinning, refitting the residual tensors, changing support, changing the ratio classes, or changing the statistic along the sweep is outside the claim.

The global one-bit statement uses real analyticity on a connected interval. For an arbitrary discontinuous or merely pointwise family, the angle supplies only `|q|` and independent sign choices can be imposed artificially. Likewise, noisy empirical curves do not reveal exact contact orders or an exact analytic continuation, so one measured sign bit does not by itself solve practical branch tracking.

The saturation asymptotic concerns finite `k` with `0<k<1`; the proportional and disjoint degeneracies classified in `VIS-048` are excluded.

Falsify the result by producing a valid `VIS-050` configuration for which two finite real contrasts of different absolute value give the same Fisher cosine; by constructing two nonzero real-analytic contrast paths on one connected interval with the same Fisher curve that are not global sign reflections of each other; by finding a point where `sign q` differs from `sign D_h`; or by violating the displayed derivative or saturation identities.

## Research consequence

The information-loss atlas for Fisher-normalized residual directions should distinguish **exact quotient loss** from **conditioning loss**. On the exact two-ratio locus the visual curve preserves `|q|` completely and forgets one global orientation bit, but that bit and nearby return locations become fragile under finite perturbations because the quotient is quadratic at balance. Large imbalance is also compressed by cosine saturation.

For empirical zeta/CUE work, retaining one explicitly signed, source-sensitive scalar alongside the Fisher angle is therefore conceptually sufficient to break the exact `q<->-q` ambiguity, but practical robustness still requires the model-error and sampling bounds called for by `VIS-054`. The next independent step is not further algebra on the exact quotient. It is to define that signed empirical coordinate on a frozen residual construction and bound how far it can move under the actual closure, binning, support, and sampling errors.