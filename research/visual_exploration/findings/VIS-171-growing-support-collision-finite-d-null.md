# VIS-171 — growing-support collision null has an explicit finite-dimensional calibration

## Claim

Keep the held-out-prime Haar null and notation of `VIS-170`. Let

`U_j = sin^2(pi X_j)`,

`A_d = d^(-1) sum_(j=1)^d U_j`,

and

`h(a) = 1/sqrt(2a)`.

The relative bulk coordinate from `VIS-170` is

`T_d = sqrt(d) (h(A_d)-1)`,

with asymptotic law `Normal(0,1/8)`. Put its unit-variance normalization

`W_d = sqrt(8) T_d = sqrt(8d) (h(A_d)-1)`.

The same Haar null admits a rigorous finite-`d` calibration in two complementary forms.

First, for every `epsilon>0`, define

`delta_+(epsilon) = epsilon(2+epsilon) / (2(1+epsilon)^2)`.

Then

`P(h(A_d) >= 1+epsilon) <= exp(-2 d delta_+(epsilon)^2)`.

For `0<epsilon<1-1/sqrt(2)`, define

`delta_-(epsilon) = epsilon(2-epsilon) / (2(1-epsilon)^2)`.

Then

`P(h(A_d) <= 1-epsilon) <= exp(-2 d delta_-(epsilon)^2)`.

For `epsilon >= 1-1/sqrt(2)` the latter probability is zero, because `A_d<=1` implies `h(A_d)>=1/sqrt(2)`.

Second, let `Phi` be the standard normal distribution function and let `C_BE` denote any valid universal Berry--Esseen constant. For

`q = x/sqrt(8d) > -1`,

set

`y_d(x) = sqrt(2d) [1-(1+q)^(-2)]`.

Then the distribution function `F_d(x)=P(W_d<=x)` satisfies the exact-transformation Berry--Esseen bound

`|F_d(x)-Phi(y_d(x))| <= C_BE [8 sqrt(2)/(3 pi)] d^(-1/2)`.

Moreover, for any fixed `0<r<1` and `|x|<=r sqrt(8d)`,

`|y_d(x)-x| <= [x^2/(4 sqrt(2d))] [(3+2r)/(1-r)^2]`,

so

`|F_d(x)-Phi(x)|`
` <= d^(-1/2) { C_BE 8 sqrt(2)/(3 pi)`
`      + x^2 (3+2r) / [8 sqrt(pi) (1-r)^2] }`.

Thus on every fixed standardized window, the relative collision null is quantitatively Gaussian with an explicit `O(d^(-1/2))` calibration error, while the rare denominator excursions outside the bulk have an explicit exponential concentration envelope.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-HOEFFDING/BERRY-ESSEEN SPECIALIZATION + FINITE-DIMENSIONAL MATCHED-NULL + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This is not a new concentration inequality, a new Berry--Esseen theorem, a sharp finite-`d` constant, a deterministic growing-dimensional prime-log equidistribution theorem, a zeta-facing separation, or an RH consequence.

## 1. The Haar denominator is an average of bounded iid variables

For Haar-uniform independent `X_j` on `T`,

`U_j = sin^2(pi X_j)`

lies in `[0,1]` and, as used in `VIS-170`,

`E[U_j]=1/2`,

`Var(U_j)=1/8`.

The relative collision factor is exactly

`h(A_d)=1/sqrt(2A_d)`.

The singularity at `A_d=0` is therefore separated from the ordinary bulk by concentration of the bounded average `A_d` around `1/2`.

## 2. Hoeffding gives an explicit finite-support safety envelope

The event `h(A_d)>=1+epsilon` is equivalent to

`A_d <= 1/[2(1+epsilon)^2]`
`    = 1/2-delta_+(epsilon)`.

Hoeffding's one-sided inequality for independent variables in `[0,1]` gives

`P(A_d-1/2 <= -delta_+) <= exp(-2d delta_+^2)`,

which is the first displayed bound.

Likewise, `h(A_d)<=1-epsilon` is equivalent to

`A_d >= 1/[2(1-epsilon)^2]`
`    = 1/2+delta_-(epsilon)`.

When this threshold is at most one, Hoeffding gives the second bound. Once `epsilon>=1-1/sqrt(2)`, the threshold reaches or exceeds one and the event has Haar probability zero.

For small `epsilon`, both `delta_+(epsilon)` and `delta_-(epsilon)` equal `epsilon+O(epsilon^2)`. Hence ordinary relative deviations of the collision denominator already have exponentially small probability in `d`; a visually dramatic excursion caused only by an atypical Haar denominator has a precise null envelope rather than an informal asymptotic explanation.

## 3. Berry--Esseen applies before the nonlinear transformation

Define the standardized bounded summands

`V_j = -sqrt(8)(U_j-1/2)`.

Using `U_j-1/2 = -(1/2) cos(2 pi X_j)`,

`V_j = sqrt(2) cos(2 pi X_j)`.

Therefore

`E[V_j]=0`,

`Var(V_j)=1`,

and

`E[|V_j|^3]`
` = 2 sqrt(2) int_0^1 |cos(2 pi x)|^3 dx`
` = 8 sqrt(2)/(3 pi)`.

Let

`L_d = d^(-1/2) sum_(j=1)^d V_j`
`    = -sqrt(8d)(A_d-1/2)`.

The classical Berry--Esseen theorem consequently gives

`sup_y |P(L_d<=y)-Phi(y)|`
` <= C_BE [8 sqrt(2)/(3 pi)] d^(-1/2)`.

No special property of the collision statistic has entered yet; this is the ordinary finite-sample normal approximation for the bounded Haar coordinates.

## 4. The nonlinear collision coordinate has an exact CDF reparameterization

For `q=x/sqrt(8d)>-1`,

`W_d<=x`

is equivalent to

`h(A_d)<=1+q`,

hence to

`A_d >= 1/[2(1+q)^2]`.

In terms of `L_d`, this is exactly

`L_d <= y_d(x)`,

where

`y_d(x)=sqrt(2d)[1-(1+q)^(-2)]`.

Thus

`F_d(x)=P(L_d<=y_d(x))`

with no delta-method approximation. Applying Berry--Esseen at the transformed threshold gives

`|F_d(x)-Phi(y_d(x))|`
` <= C_BE [8 sqrt(2)/(3 pi)] d^(-1/2)`.

This exact reparameterization avoids having to control a Taylor remainder of the singular map on the whole support.

## 5. On central windows the transformed threshold differs from `x` by `O(d^-1/2)`

Since

`x = sqrt(2d) 2q`,

an exact subtraction gives

`y_d(x)-x`
` = -sqrt(2d) q^2 (3+2q)/(1+q)^2`.

If `|q|<=r<1`, then

`|y_d(x)-x|`
` <= [x^2/(4 sqrt(2d))] [(3+2r)/(1-r)^2]`.

The standard normal CDF is globally `1/sqrt(2 pi)`-Lipschitz, so

`|Phi(y_d(x))-Phi(x)|`
` <= x^2 (3+2r) / [8 sqrt(pi d) (1-r)^2]`.

Combining this with the previous section proves the displayed finite-`d` Gaussian calibration.

For any fixed `M`, choose any fixed `r>0`; once `d` is large enough that `M<=r sqrt(8d)`, the bound is uniform on `|x|<=M` and is `O((1+M^2)/sqrt(d))`. This strengthens the weak-convergence statement of `VIS-170` into a directly usable finite-support null on every fixed standardized bulk window.

## 6. Prior art and novelty boundary

The concentration input is classical Hoeffding theory. Wassily Hoeffding, **Probability Inequalities for Sums of Bounded Random Variables**, *Journal of the American Statistical Association* 58:301 (1963), 13--30, DOI `10.1080/01621459.1963.10500830`, derives exponential probability bounds for sums of independent bounded variables. The one-sided `[0,1]` specialization used above is standard and no new concentration theorem is claimed.

The quantitative normal-approximation input is the classical Berry--Esseen theorem. A direct historical reference is C. G. Esseen, **A moment inequality with an application to the central limit theorem**, *Scandinavian Actuarial Journal* 1956:2 (1956), 160--170, DOI `10.1080/03461238.1956.10414946`, which records the finite-third-moment normal-approximation inequality in the Berry--Esseen line of results. The proof above keeps the universal constant symbolic because optimizing it is irrelevant to the Mathia control.

The Mathia-specific content is only the exact specialization of these classical bounds to the nonlinear relative collision coordinate isolated in `VIS-170`, including the explicit third absolute moment and exact CDF threshold map. The result is a matched-null calibration, not a claim of new probability theory.

## 7. Boundaries and falsification

The result assumes the independent Haar model. It does not transfer automatically to deterministic prime-log samples when the support dimension grows with the observation window; that remains a changing-dimensional discrepancy problem.

The Berry--Esseen comparison is most informative in the standardized bulk. The Hoeffding envelope controls denominator excursions, but neither bound is claimed sharp in the far tail. In particular, this finding does not replace the small-ball and extreme-collision analysis of `VIS-164`--`VIS-168`.

The finite-`d` Gaussian bound uses only a universal Berry--Esseen constant. It does not optimize constants, Edgeworth terms, moderate deviations, or higher-order corrections. Any apparent arithmetic signal living only below this conservative null-resolution floor is not separated by the present argument.

Falsify the finding by exhibiting an error in the exact event transformations, the moments of `U_j`, the third absolute moment of `V_j`, or the application hypotheses of Hoeffding/Berry--Esseen. Each displayed finite-`d` bound follows directly from those ingredients.

## Research consequence

`VIS-170` identified the first-order Gaussian width of the growing-support Haar collision null but left finite-dimensional testing open. The present result closes that specific calibration gap: the bulk now has an explicit `O(d^-1/2)` normal-approximation envelope, and the nonlinear denominator has an independent exponential concentration bound.

A future support-varying visual statistic should therefore compare its standardized residual against this finite-`d` null before treating finite-support non-Gaussianity or width changes as source information. A residual that survives this calibration may motivate a sharper deterministic or arithmetic test; agreement with it is another generic Haar effect, not positive evidence.