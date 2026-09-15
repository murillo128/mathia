# VIS-247 — log-product conditioning has an explicit alpha-free coarea law and preserves tent variation

## Claim

Continue the symmetric normalized cyclic-gap null of `VIS-240`--`VIS-246`. Let

`Delta_m^o = {x_i>0 : sum_i x_i=1}`

and define the log-product statistic

`Lambda(x)=sum_(i=1)^m log x_i = log(prod_i x_i)`.

For every level

`lambda < -m log m`,

the set

`S_lambda={x in Delta_m^o : Lambda(x)=lambda}`

is a smooth compact `(m-2)`-dimensional level surface. If

`q_i(x)=1/x_i`,  `qbar(x)=(1/m)sum_i q_i(x)`,

then the simplex-tangent gradient of `Lambda` is

`grad_Delta Lambda(x) = (q_i-qbar)_i`

with norm

`J(x) = [sum_i x_i^(-2) - (1/m)(sum_i x_i^(-1))^2]^(1/2)`.

The symmetric-Dirichlet conditional law on a regular log-product level is therefore

`P_alpha(dx | Lambda=lambda)`
` = Z(lambda)^(-1) J(x)^(-1) d sigma_lambda(x)`,

where `sigma_lambda` is induced Hausdorff surface measure on `S_lambda` and

`Z(lambda)=integral_(S_lambda) J(x)^(-1) d sigma_lambda(x)`.

This law is **exactly independent of `alpha`**. The sufficient-statistic statement of `VIS-246` can therefore be strengthened from an abstract factorization result to an explicit parameter-free geometric disintegration.

The quotient is not automatically degenerate. For any statistic `F` that is differentiable at a regular point `x in S_lambda`, the tangent space is

`T_x S_lambda = {v : sum_i v_i=0, sum_i v_i/x_i=0}`.

Hence a sufficient local nondegeneracy test is

`grad F(x) notin span{(1,...,1),(1/x_1,...,1/x_m)}`.

Whenever this holds, some tangent direction keeps both `sum x_i` and `Lambda(x)` fixed to first order while changing `F`.

For the cut-averaged tent statistic `bar T` of `VIS-241`, this nondegeneracy occurs exactly in a concrete three-gap example. Normalize the circumference to one and choose `u=ell/L=2/5`. The two gap configurations

`A=(1/6,1/6,2/3)`

and

`B=((1+sqrt(3))/6,(1+sqrt(3))/6,(2-sqrt(3))/3)`

have the same sum and the same product,

`prod_i A_i = prod_i B_i = 1/54`,

so they lie on the same `Lambda=log(1/54)` level. Their shorter circular pair-distance multisets are respectively

`{1/6,1/6,1/3}`

and

`{(1+sqrt(3))/6,(1+sqrt(3))/6,(2-sqrt(3))/3}`.

With

`phi_u(t)=(1-t/u)_+(1-t)`,

`bar T=sum_pairs phi_u(delta)`, and direct substitution gives

`bar T(A)=13/12`,

`bar T(B)=(11+sqrt(3))/18`.

Thus

`bar T(A)-bar T(B)=(17-2sqrt(3))/36 > 0`.

Both points are regular and lie away from the tent threshold and the antipodal boundary. Because the conditional density above is positive and finite in neighborhoods of both points, `Law(bar T | Lambda=log(1/54))` is genuinely nonconstant for this example.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL COAREA/EXPONENTIAL-FAMILY SPECIALIZATION + EXACT NONDEGENERACY WITNESS + NO-NOVELTY-CLAIM`.

No closed form for the full conditional distribution of `bar T`, no general power result for arbitrary `m,u,lambda`, no prime-gap model validity, no prime residual, and no RH consequence is claimed.

## 1. Regular log-product levels inside the simplex

Work in the affine hyperplane

`M={x in R^m : sum_i x_i=1}`

with tangent space

`T={v : sum_i v_i=0}`.

The ambient gradient of `Lambda` is

`q=(1/x_1,...,1/x_m)`.

Projecting onto `T` subtracts its mean component:

`grad_Delta Lambda = q-qbar 1`.

Therefore

`||grad_Delta Lambda||^2`
` = sum_i q_i^2 - (1/m)(sum_i q_i)^2`,

which is the displayed `J(x)^2`.

The projected gradient vanishes only when all `q_i` are equal, hence only at the barycenter `x_i=1/m`. By strict concavity of `Lambda`, that point is its unique maximum on the simplex, with value

`Lambda_max = -m log m`.

Every lower level `lambda<Lambda_max` is consequently regular. It is also compact inside the open simplex: fixing `prod_i x_i=e^lambda>0` keeps every coordinate away from zero on the closed simplex. Thus `S_lambda` is a smooth compact codimension-one surface inside the `(m-1)`-dimensional simplex.

The excluded barycentric level is genuinely different: it consists of the single equal-gap configuration and is a degenerate conditioning surface.

## 2. Coarea gives the exact alpha-free conditional surface measure

Relative to ordinary `(m-1)`-dimensional Lebesgue measure on the simplex hyperplane, the symmetric-Dirichlet density is

`f_alpha(x)=K_m(alpha) exp((alpha-1)Lambda(x))`,

where

`K_m(alpha)=Gamma(m alpha)/Gamma(alpha)^m`.

Apply the coarea formula to the scalar map `Lambda`. For an integrable test function `g`, the contribution of a regular level has surface density

`g(x) f_alpha(x) / J(x)`

against `d sigma_lambda(x)`.

On `S_lambda`, both `K_m(alpha)` and

`exp((alpha-1)lambda)`

are constants. They cancel when the level measure is normalized to a conditional probability. What remains is exactly

`J(x)^(-1) d sigma_lambda(x)`

up to the level-dependent normalizing constant `Z(lambda)`.

This supplies an explicit target for same-configuration calibration. Conditioning on `Lambda` does not require estimating `alpha`, drawing from a fitted `alpha_hat`, or retaining an `alpha`-dependent reweighting on the level set. The only geometric weight is the coarea Jacobian, which is determined by the observed gap coordinates themselves and not by the nuisance parameter.

The surface law is not uniform in general. Unlike the concentration levels of `VIS-246`, whose tangent-gradient norm is constant on each sphere, `J(x)` varies along a generic product level. Replacing the conditional law by unweighted uniform surface sampling would therefore introduce a new calibration error.

## 3. A differential test for whether the quotient destroys a statistic

At a regular point, vectors tangent to both the simplex and the log-product level satisfy the two linear constraints

`<1,v>=0`,

`<q,v>=0`.

Their orthogonal complement in `R^m` is

`span{1,q}`.

For a differentiable statistic `F`, its first variation along the conditioned surface is

`dF_x(v)=<grad F(x),v>`.

Therefore, if

`grad F(x) notin span{1,q}`,

there exists a vector `v in T_x S_lambda` with `dF_x(v)!=0`. The statistic changes along the exact nuisance-conditioned surface and is locally nondegenerate there.

Conversely, membership of `grad F(x)` in that span is the precise first-order stationarity condition at `x`; it is not by itself a proof that `F` is globally constant on the whole level.

For `bar T`, this criterion is directly usable away from the piecewise boundaries where a shorter arc crosses `u` or `1/2`. On each such region the statistic is an explicit smooth polynomial in the relevant consecutive gap sums, so the tangent test can be evaluated without simulating the Dirichlet parameter.

## 4. An exact three-gap witness that the tent statistic survives conditioning

For three cyclic gaps, every unordered point pair corresponds to one gap and its complementary two-gap arc. The shorter circular pair distances are therefore

`delta_i=min(x_i,1-x_i)`.

Take

`A=(1/6,1/6,2/3)`.

Its product is `1/54`, and its shorter distances are

`1/6,1/6,1/3`.

Now put

`b=(1+sqrt(3))/6`,

`c=(2-sqrt(3))/3`.

Then `2b+c=1` and

`b^2 c`
` = [(2+sqrt(3))/18][(2-sqrt(3))/3]`
` = 1/54`.

Hence `B=(b,b,c)` lies on the same log-product level as `A`. All three entries of `B` are below `1/2`, so its shorter-distance multiset is simply `{b,b,c}`.

At `u=2/5`, `b>u`, so only `c` contributes for `B`. For `A`, all three shorter distances lie below `u`. Using

`phi_u(t)=(1-t/u)(1-t)`

inside the support,

`bar T(A)`
` = 2 phi_(2/5)(1/6)+phi_(2/5)(1/3)`
` = 13/12`,

while

`bar T(B)`
` = phi_(2/5)(c)`
` = (11+sqrt(3))/18`.

The values are separated by `(17-2sqrt(3))/36`. Neither configuration lies on a threshold surface, so this difference persists on small open pieces of `S_log(1/54)`. Since `J^-1` is positive there, both pieces have positive conditional mass. The conditional tent statistic is therefore nondegenerate, not merely different at two measure-zero points.

This witness is deliberately modest. It shows that exact nuisance removal through `Lambda` does **not structurally force** the tent statistic to collapse. It does not establish that the actual high-dimensional, critical-width prime configuration retains enough conditional variation for a useful test.

## 5. Prior art and novelty boundary

The symmetric-Dirichlet density, exponential-family factorization, Fisher--Neyman sufficiency criterion, and coarea disintegration are classical. `VIS-240` and `VIS-246` already record that prior-art boundary and use the same standard Dirichlet/spacings machinery. No novelty is claimed for conditioning an exponential family on a sufficient statistic, for the coarea formula, or for the reciprocal-gradient surface density in general.

The Mathia-specific contribution is the explicit conditioning geometry for the current representation-matched gap null and the exact answer to the immediate degeneracy concern left by `VIS-246`: the conditional law can be written without `alpha`, its nonuniform surface weight is known exactly, and the current tent statistic is not forced to become constant after the quotient.

A targeted literature search for the present step found standard Dirichlet/exponential-family and simplex-distribution treatments but no reason to reinterpret these classical ingredients as a new probability theorem. The finding is therefore classified only as an exact specialization and calibration result.

## Boundaries and falsification

The explicit surface law concerns the one-parameter **symmetric** Dirichlet family. An asymmetric Dirichlet model has several log-coordinate sufficient statistics; mixtures, renewal models, hard-core processes, and richer gap families require new nuisance factorizations.

Conditioning on an exact continuous statistic is understood through regular conditional disintegration. The formula applies on regular levels `lambda<-m log m`; the equal-gap maximum is singular and degenerate.

The tangent-gradient criterion is local. Failure of the criterion at one point does not imply global degeneracy, while success at one regular point proves only that the statistic varies on that level, not that it has useful power against a prime alternative.

The three-gap witness uses `u=2/5` and is not an asymptotic statement about the critical prime width. It proves that the sufficient-statistic quotient is not intrinsically destructive; the actual `m,u,Lambda` regime must still be evaluated independently.

Falsify the surface law by deriving a residual `alpha`-dependent factor in the normalized coarea measure on a regular `Lambda` level. Falsify the nondegeneracy witness by showing that `A` and `B` have different products or that the displayed `bar T` values are equal. Falsify the tangent criterion by producing a regular point with `grad F notin span{1,q}` but zero derivative in every level-tangent direction.

## Research consequence

`VIS-246` left two questions entangled: whether exact same-configuration nuisance elimination has a usable conditional measure, and whether that quotient necessarily destroys the tent statistic. Both are now separated.

The exact conditional target is the parameter-free coarea law

`Z(lambda)^(-1) J(x)^(-1) d sigma_lambda(x)`.

The tent statistic can retain variation on such a level, so degeneracy is not a formal obstruction. The next coherent step is application-specific rather than another nuisance-identification argument: for the frozen high-dimensional `m,u,Lambda` regime of the critical prime configuration, evaluate or independently validate this conditional law accurately enough to calibrate the predeclared `bar T`, then test whether any prime residual survives. That is a separate thread and is intentionally not opened here.
