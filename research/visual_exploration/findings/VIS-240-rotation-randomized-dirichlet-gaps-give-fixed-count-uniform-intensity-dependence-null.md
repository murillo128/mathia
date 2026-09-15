# VIS-240 — rotation-randomized Dirichlet gaps give a fixed-count uniform-intensity dependence null

## Claim

Fix an interval length `L>0`, a point count `m>=2`, a gap-shape parameter `alpha>0`, and a tent width `0<ell<=L/2`. Put `u=ell/L`.

Construct a random `m`-point configuration as follows. First draw cyclic gaps

`(G_1,...,G_m)/L ~ Dirichlet(alpha,...,alpha)`

with `sum_j G_j=L`. Choose an independent uniform rotation `Theta in [0,L)`, place the `m` cyclic points at the partial sums of the gaps modulo `L`, then cut at `0` and sort the resulting points as

`0<=X_(1)<...<X_(m)<L`.

This model has all three structural properties required by the current critical-cell calibration route:

1. the point count is exactly `m`;
2. after sorting, realizations stay on the same monotone ordered-point support as the prime-coordinate representation;
3. the one-point intensity is exactly uniform, `m/L`, for every `alpha`, because of the independent random rotation.

At the same time `alpha` changes the short-gap dependence. The normalized cyclic gaps have

`E[G_j/L]=1/m`,

`Var(G_j/L)=(m-1)/(m^2(m alpha+1))`,

so their squared coefficient of variation is

`CV^2=(m-1)/(m alpha+1)`.

Thus `alpha=1` gives the classical iid-uniform circular-spacing law, `alpha>1` regularizes/repels the gaps, and `0<alpha<1` makes them more uneven/clustered, without changing the point count or one-point intensity.

For the linear tent statistic after the cut,

`T_(m,alpha)=sum_(i<j) (1-|X_(j)-X_(i)|/ell)_+`,

the finite-sample mean is exact. Let `I_u(a,b)` denote the regularized incomplete beta function and define

`J_(a,b)(u)`
` = I_u(a,b)`
`   -(1+1/u) [a/(a+b)] I_u(a+1,b)`
`   +(1/u) [a(a+1)/((a+b)(a+b+1))] I_u(a+2,b)`.

Then

`E[T_(m,alpha)]`
` = (m/2) sum_(r=1)^(m-1)`
`   [J_(r alpha,(m-r) alpha)(u)`
`    +J_((m-r) alpha,r alpha)(u)]`.

Equivalently, by the symmetry of the sum over `r`,

`E[T_(m,alpha)] = m sum_(r=1)^(m-1) J_(r alpha,(m-r) alpha)(u)`.

For `alpha=1` this model is exactly the fixed-count iid-uniform point model of `VIS-238`, so the formula collapses to

`E[T_(m,1)] = binom(m,2)(u-u^2/3)`.

Hence there is an explicit one-parameter family of **fixed-count, uniform-intensity, monotone-support dependence controls** for the critical tent statistic. The iid-uniform calibration is one member rather than the only representation-matched null.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-DIRICHLET/SPACING SPECIALIZATION + REPRESENTATION-MATCHED DEPENDENCE NULL + NO-NOVELTY-CLAIM`.

No prime-gap law, fitted value of `alpha`, variance formula for this dependent tent statistic, prime-specific residual, asymptotic point-process theorem, or RH consequence is claimed.

## 1. The random rotation removes the one-point marginal confound exactly

The cyclic gap law is exchangeable but dependent because the gaps sum to `L`. Before the random rotation, choosing one partial sum as a distinguished origin would introduce an arbitrary phase. The independent `Theta` removes that phase: rotating the entire point set by a uniform amount makes the law translation-invariant on the circle.

Therefore every individual cyclic point is uniform modulo `L`, and the expected counting measure is exactly

`E[N(A)] = (m/L) |A|`

for every measurable `A subset [0,L)` after cutting the circle at `0`. This holds for every `alpha`.

The cut and sort operation preserves the actual representation support relevant to `VIS-236` and `VIS-237`: the observed coordinates are again one strictly increasing real sequence. Unlike the generic Markov-label controls closed by `VIS-236`, this model never creates cell-label revisits or backtracking by construction.

The family therefore changes genuine spacing dependence while holding fixed the two nuisance quantities already isolated by `VIS-238` and `VIS-239`: total count and one-point intensity.

## 2. Dirichlet aggregation gives the pair-arc law

Fix a cyclic starting point and move forward across `r` consecutive gaps, `1<=r<=m-1`. The corresponding forward arc length is

`A_r=G_i+...+G_(i+r-1)`

with indices read cyclically. By the aggregation property of the Dirichlet distribution,

`S_r=A_r/L ~ Beta(r alpha,(m-r) alpha)`.

This statement is independent of the starting point because the symmetric gap law is cyclically exchangeable.

The parameter `alpha` therefore changes pair geometry without introducing a separate one-point density. In particular, the nearest-neighbor normalized gap is `Beta(alpha,(m-1)alpha)`, while sums of `r` consecutive gaps are the corresponding beta aggregates.

For `alpha=1`, the symmetric Dirichlet gap vector is the classical circular-spacing law of `m` iid uniform points. Thus this family contains the `VIS-238` fixed-count homogeneous model exactly at `alpha=1`.

## 3. A random cut converts a cyclic arc into the correct linear separation

Condition on one oriented pair whose forward arc fraction is `S_r=s`. Relative to the fixed cut at `0`, the independent uniform rotation is equivalent to placing the cut uniformly around the circle.

With probability `1-s`, the cut does not fall inside the forward arc, so the two linear coordinates are separated by `sL`. With probability `s`, the cut falls inside that arc and the linear separation becomes `(1-s)L`.

Let

`K_u(t)=(1-t/u)_+`.

The conditional expected tent contribution of that oriented cyclic pair is therefore

`q_u(s)=(1-s)K_u(s)+s K_u(1-s)`.

Every unordered pair appears twice among the `m(m-1)` oriented cyclic pairs, once with forward arc `s` and once with `1-s`. Hence

`E[T_(m,alpha)]`
` =(m/2) sum_(r=1)^(m-1) E[q_u(S_r)]`.

This is already an exact calibration identity before evaluating the beta integrals.

## 4. The beta integral is explicit

For `S~Beta(a,b)` and `u<=1/2`, the two support pieces in `q_u` do not overlap. The near-zero piece is

`J_(a,b)(u)`
` = integral_0^u (1-s)(1-s/u) f_(a,b)(s) ds`.

Expanding the polynomial gives

`(1-s)(1-s/u)=1-(1+1/u)s+s^2/u`.

The three truncated beta moments are

`int_0^u f_(a,b)(s) ds = I_u(a,b)`,

`int_0^u s f_(a,b)(s) ds`
` = [a/(a+b)] I_u(a+1,b)`,

`int_0^u s^2 f_(a,b)(s) ds`
` = [a(a+1)/((a+b)(a+b+1))] I_u(a+2,b)`.

Substitution gives the displayed formula for `J_(a,b)(u)`.

For the near-one piece, set `t=1-s`; it is exactly `J_(b,a)(u)`. Therefore

`E[q_u(S)] = J_(a,b)(u)+J_(b,a)(u)`,

and inserting `a=r alpha`, `b=(m-r)alpha` proves the finite-sample mean formula.

No simulation or asymptotic approximation enters this calibration.

## 5. The family is nondegenerate and separates dependence from intensity

For every finite `alpha>0`, the Dirichlet density is positive on the interior of the gap simplex. The model therefore assigns positive probability to open sets of configurations with different short-gap patterns. For `0<u<1/2`, the tent statistic is not fixed by `m`, the one-point intensity, or the rotation: moving gap mass across the threshold `ell` changes at least one pair contribution on open subsets of the sample space.

This is the property the earlier categorical controls failed to preserve. Conditioning on the realized occupancy histogram in `VIS-232` fixed the collision statistic, and the actual endpoint-matched first-order transition table in `VIS-236` had a singleton realization. Here the statistic remains random while all realizations remain monotone point configurations with fixed count and uniform marginal intensity.

The parameter is also interpretable directly through the gaps. Since

`CV^2=(m-1)/(m alpha+1)`,

larger `alpha` suppresses gap heterogeneity and approaches an equally spaced lattice after random rotation, while smaller `alpha` increases clustering. The family therefore supplies a controlled dependence axis rather than another arbitrary label randomization.

## 6. Prior art and novelty boundary

Uniform spacings and their Dirichlet/exponential representation are classical. Ronald Pyke, **Spacings**, *Journal of the Royal Statistical Society, Series B* 27:3 (1965), 395–449, JSTOR `2345793`, is a standard foundational reference for uniform spacings and related statistics.

The normalized-gamma construction, aggregation rule, beta marginals, and elementary moment formulas of the Dirichlet distribution are standard multivariate-probability facts; see, for example, Samuel Kotz, N. Balakrishnan, and Norman L. Johnson, **Continuous Multivariate Distributions, Volume 1: Models and Applications**, 2nd ed., Wiley (2000), in its treatment of the Dirichlet distribution.

Circular spacing tests and random-arc statistics are likewise classical. No novelty is claimed for using a symmetric Dirichlet law as a random partition of the circle, for random rotation, for beta aggregation, or for incomplete-beta evaluation.

The Mathia-specific result is the calibration fit to the current representation boundary: after `VIS-236`--`VIS-239` separately remove label-support mismatch, grid phase, total-count fluctuation, and specified one-point intensity, this construction gives an explicit dependent null that keeps all four constraints simultaneously and yields the exact finite-sample center of the surviving tent statistic.

## Boundaries and falsification

This family is a **calibration family**, not a claimed model of prime gaps. A value of `alpha` chosen after looking at the same confirmation statistic would reintroduce tuning bias. Any later use must freeze `alpha` from theory or independent/held-out data, or carry parameter-estimation uncertainty through the null.

The exact mean does not provide the dependent variance or full law of `T_(m,alpha)`. Those require joint beta/Dirichlet overlap calculations or an independently validated simulation procedure. The family is therefore not yet a complete confirmation null merely because its center is explicit.

Random rotation makes the one-point intensity exactly uniform, but it does not make points independent. That dependence is the purpose of the construction. Conversely, the single `alpha` parameter does not represent arbitrary prime-gap correlations, long-range arithmetic structure, or higher-order constraints.

The circular construction followed by a cut is representation-matched only for statistics on the ordered coordinates themselves. If a later statistic treats the two physical interval endpoints as mathematically distinguished rather than as a nuisance truncation, the random-rotation model would need to be re-audited.

Falsify the displayed finite-sample formula by giving `m`, `alpha`, `u` and an exact or high-precision Dirichlet integration for which the expectation differs. Falsify the support claim by exhibiting a realization after cut-and-sort that is not a monotone ordered point configuration, or the intensity claim by showing a measurable interval whose expected count is not `(m/L)` times its length.

## Research consequence

`CLUE-prime-phase-critical-logarithmic-occupancy` asked for a stronger fixed-count ordered-point control after quotienting grid origin, Poisson count noise, and independently specified one-point intensity. This finding supplies such a control family at the level of the exact center.

The next coherent step is now sharply defined rather than open-ended: derive or independently calibrate the variance/covariance of the same tent statistic under the frozen `alpha` family, with `alpha` fixed independently of confirmation data. Only after that dependent calibration is available should the prime configuration be tested for a residual. A residual that disappears inside this gap-dependence family is not evidence of prime-specific structure; one that survives still requires translation back through the signed prime-phase kernel before it becomes RH-relevant.