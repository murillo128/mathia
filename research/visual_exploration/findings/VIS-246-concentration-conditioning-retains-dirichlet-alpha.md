# VIS-246 — concentration conditioning retains Dirichlet alpha on simplex-sphere slices

## Claim

Continue the symmetric cyclic-gap null of `VIS-240`--`VIS-245`. Let

`X=(X_1,...,X_m) ~ Dirichlet(alpha,...,alpha)`, `alpha>0`,

on the open simplex `sum_i X_i=1`, and retain the complete-gap concentration

`H=sum_i X_i^2`, `C=mH-1`

from `VIS-244`.

For every regular concentration level `h in (1/m,1)`, conditioning on `H=h` restricts the gap vector to the simplex-sphere slice

`M_h={x_i>0: sum_i x_i=1, sum_i x_i^2=h}`.

With respect to the induced `(m-2)`-dimensional Hausdorff surface measure `sigma_h`, the conditional density is

`P_alpha(dx | H=h) proportional to (prod_i x_i)^(alpha-1) d sigma_h(x)`.

The coarea Jacobian introduces no additional `x`-dependence on the slice because the tangent gradient satisfies

`||grad_M H|| = 2 sqrt(h-1/m)`.

Therefore the concentration statistic `C` does **not** remove the nuisance parameter `alpha` in dimensions `m>=3`: the same concentration sphere contains points with different coordinate products, and their conditional likelihood ratio depends on `alpha`.

For `m=2` there is an exact exception. Since `x_1+x_2=1`,

`x_1 x_2=(1-H)/2`,

so the product is determined by `H`; the two permutation points on a regular level have equal weight for every `alpha`. Thus concentration conditioning is `alpha`-free only in the two-gap case.

For every fixed `m`, the scalar

`L(X)=sum_i log X_i = log(prod_i X_i)`

is instead an exact sufficient statistic for `alpha`, because the symmetric-Dirichlet density factors as

`f_alpha(x)=Gamma(m alpha)/Gamma(alpha)^m * exp((alpha-1)L(x))`.

Consequently the conditional law of **any** gap statistic, including the cut-averaged tent statistic `bar T`, given `L`, is independent of `alpha` wherever the regular conditional law is defined. This supplies an exact nuisance-elimination route for same-configuration calibration that is structurally different from plugging the method-of-moments value `alpha_hat(C)` into a fixed-parameter null.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-DIRICHLET/EXPONENTIAL-FAMILY GEOMETRY + NEGATIVE NUISANCE CONTROL + NO-NOVELTY-CLAIM`.

No closed conditional law for `bar T | L`, prime-gap model validity, prime residual, sufficiency of `C` for `m>=3`, new Dirichlet theorem, or RH consequence is claimed.

## 1. Concentration levels are spheres inside the simplex hyperplane

Let

`M={x in R^m: sum_i x_i=1}`

with tangent space `T={v: sum_i v_i=0}`. Write `1` for the all-ones vector and `b=(1/m)1` for the simplex barycenter. Because `sum_i x_i=1`,

`sum_i (x_i-1/m)^2 = H(x)-1/m = C(x)/m`.

Hence fixing `H=h` is geometrically the intersection of the simplex interior with the sphere in the affine hyperplane `M` centered at `b` and radius

`sqrt(h-1/m)`.

The ambient gradient of `H` is `2x`. Projecting it onto `T` gives

`grad_M H = 2(x-b)`.

Therefore

`||grad_M H||^2 = 4 ||x-b||^2 = 4(H-1/m)`.

On the level set `H=h`, this norm is the constant `2 sqrt(h-1/m)`. The barycentric point `h=1/m` is the unique critical level and is excluded from the regular-slice statement.

This constant-gradient fact matters because a conditional law on a nonlinear level set normally acquires a position-dependent coarea Jacobian. Here that Jacobian is constant along each concentration sphere and cannot hide or cancel the remaining Dirichlet weight.

## 2. The exact conditional slice law keeps the product tilt

Relative to ordinary `(m-1)`-dimensional Lebesgue measure on the simplex hyperplane, the symmetric-Dirichlet density is

`f_alpha(x)=K(alpha) prod_i x_i^(alpha-1)`,

where `K(alpha)=Gamma(m alpha)/Gamma(alpha)^m`.

The coarea formula disintegrates this measure along regular `H`-level sets with surface density

`f_alpha(x)/||grad_M H(x)||`.

Since the denominator is constant on `M_h`, normalization on that slice removes both `K(alpha)` and the coarea constant but leaves

`(prod_i x_i)^(alpha-1)`.

Thus, for measurable `A subset M_h`, the conditional probability is proportional to

`integral_A (prod_i x_i)^(alpha-1) d sigma_h(x)`.

At `alpha=1` the slice law is the normalized induced surface measure. For `alpha!=1`, the geometric mean of the gaps tilts that same sphere: `alpha>1` favors larger products, hence configurations more balanced within the fixed quadratic radius, while `0<alpha<1` favors smaller products and therefore more boundary-directed configurations.

This is an exact geometric distinction, not a second-moment effect. `VIS-245` showed that `C` and `bar T` have a nontrivial covariance; the present result shows more strongly that fixing the observed value of `C` does not in general freeze the null law itself.

## 3. An explicit equal-concentration witness kills sufficiency for m at least 3

For `m=3`, consider

`a=(1/2,1/4,1/4)`

and

`b=(5/12,5/12,1/6)`.

Both lie in the open simplex and satisfy

`H(a)=3/8=H(b)`.

But

`prod_i a_i = 1/32 = 27/864`,

whereas

`prod_i b_i = 25/864`.

Their same-level likelihood ratio is therefore

`f_alpha(a)/f_alpha(b) = (27/25)^(alpha-1)`,

which depends on `alpha`. By the likelihood-ratio criterion for sufficiency, `H` and hence `C=mH-1` cannot be sufficient for `alpha` when `m=3`.

The obstruction persists for every `m>3`. Choose any `t>0` with `s=1-(m-3)t>0` and append `m-3` coordinates equal to `t` while scaling the first three coordinates by `s`:

`a'=(s a_1,s a_2,s a_3,t,...,t)`,

`b'=(s b_1,s b_2,s b_3,t,...,t)`.

Then both vectors sum to one and have the same concentration

`H(a')=H(b')=s^2(3/8)+(m-3)t^2`,

while their products differ by the same `27/25` factor. Thus the failure is not a special low-dimensional accident.

For `m=2`, by contrast,

`1=(x_1+x_2)^2=H+2x_1x_2`,

so the product is a function of `H`. The regular concentration level consists only of the two coordinate permutations and the symmetric density gives them equal probability for every `alpha`. This exactly identifies the dimensional boundary of the obstruction.

## 4. The log-product is the exact alpha-sufficient coordinate

The same density can be written

`f_alpha(x)=K(alpha) exp((alpha-1)L(x))`,

where

`L(x)=sum_i log x_i`.

The support does not depend on `alpha`. The Fisher-Neyman factorization criterion therefore makes `L` a sufficient statistic for the one-parameter symmetric-Dirichlet family.

Equivalently, if two interior configurations have the same `L`, their density ratio is independent of `alpha`. Upon conditioning on `L=l`, the factor `exp((alpha-1)l)` is constant on the level set and cancels in normalization. The remaining conditional geometry is parameter-free.

This gives a sharper calibration fork than the method-of-moments route in `VIS-244`:

- `C` is an informative and increasingly concentrated estimator channel for `alpha`, but conditioning on it does not eliminate `alpha` when `m>=3`;
- `L` is an exact sufficient coordinate, so a conditional test based on the law of `bar T | L` can use the same gap vector for nuisance removal without estimating `alpha` at all.

The second statement is structural, not computational. It does not provide a closed form for `bar T | L`; that conditional law may still require exact geometry, deterministic integration, or independently validated conditional simulation.

## 5. Prior art and novelty boundary

The symmetric Dirichlet density, its normalized-gamma construction, aggregation rules, and moment identities are classical. `VIS-240` records the standard prior-art boundary through Pyke's foundational treatment of spacings and Kotz, Balakrishnan, and Johnson's treatment of the Dirichlet distribution. The exponential-family factorization used here is the standard Fisher-Neyman sufficiency criterion.

No novelty is claimed for Dirichlet sufficient statistics, coarea disintegration, simplex geometry, or the fact that a one-parameter exponential family can be conditioned on a sufficient statistic to remove its parameter.

The Mathia-specific contribution is the exact falsification and replacement of the current nuisance-control idea. `VIS-244` showed that quadratic concentration identifies `alpha` in expectation, and `VIS-245` supplied the same-sample cross-covariance with the tent statistic. The present result shows that **conditioning on that concentration is not itself an exact nuisance quotient for three or more gaps**, while exposing the log-product coordinate that is.

## Boundaries and falsification

The result concerns one symmetric Dirichlet parameter shared by all `m` normalized cyclic gaps. For asymmetric Dirichlet families, mixtures, hard-core processes, renewal laws, or richer prime-gap controls, the sufficient-statistic structure changes and must be re-derived.

The slice-density statement is for regular concentration levels in the simplex interior. Boundary strata and the barycentric critical level require their own lower-dimensional disintegrations, although they do not rescue concentration sufficiency for the generic `m>=3` family.

The result does not claim that conditioning on `L` preserves high power for the prime-phase tent statistic. A sufficient nuisance quotient can discard signal as well as nuisance. Any confirmation test must therefore predeclare the statistic and conditioning rule and compare against appropriate representation-matched controls.

The claim is falsified by any equal-`H` interior pair whose Dirichlet likelihood ratio is independent of `alpha` despite unequal products, by a coarea calculation showing a nonconstant `H`-slice Jacobian, or by a factorization of the symmetric-Dirichlet likelihood showing dependence on `alpha` outside `L`.

## Research consequence

`CLUE-prime-phase-critical-logarithmic-occupancy` currently leaves two honest same-configuration routes: derive the full/conditional calibration associated with the concentration fit, or avoid same-sample fitting by freezing `alpha` from held-out/theoretical information.

This finding adds a third, exact structural route and closes one tempting shortcut. For `m>=3`, **`bar T | C` is not automatically nuisance-free**, so merely conditioning on the observed concentration cannot replace the missing calibration. But conditioning on

`L=sum_i log X_i`

removes `alpha` exactly within the symmetric-Dirichlet family. The next coherent step is therefore to determine whether the predeclared tent statistic has a tractable and nondegenerate conditional law given `L`, or whether that exact nuisance quotient destroys too much of the candidate prime-specific pair geometry. That is a separate mathematical question and is intentionally not opened in this finding.