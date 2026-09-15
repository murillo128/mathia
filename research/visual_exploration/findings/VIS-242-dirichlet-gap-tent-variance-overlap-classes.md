# VIS-242 — symmetric-Dirichlet tent variance reduces exactly to overlap classes

## Claim

Continue the fixed-count circular dependence null of `VIS-240` and the endpoint-phase quotient of `VIS-241`. Normalize the circumference to `L=1`, put `u=ell/L` with `0<u<=1/2`, and write the cyclic gaps as

`X=(X_0,...,X_(m-1)) ~ Dirichlet(alpha,...,alpha)`,

with indices in `Z/mZ`. For a forward cyclic arc of `r` gaps starting at `i`, define

`S_(i,r)=sum_(a=0)^(r-1) X_(i+a)`, `1<=r<=m-1`.

Let

`q_u(s)=(1-s)(1-s/u)_+ + s(1-(1-s)/u)_+`.

Equivalently, if `d(s)=min(s,1-s)`, then

`q_u(s)=(1-d(s)/u)_+(1-d(s))`.

The cut-averaged tent statistic of `VIS-241` has the exact oriented-arc representation

`bar T = (1/2) sum_(i=0)^(m-1) sum_(r=1)^(m-1) q_u(S_(i,r))`.

For two oriented arcs `A_(0,r)` and `A_(d,s)` let

`k_(r,s)(d)=|A_(0,r) intersect A_(d,s)|`.

For any feasible overlap size `k`, define

`M_(r,s,k)`
` = E[q_u(Z_I+Z_A) q_u(Z_I+Z_B)]`,

where the aggregated masses satisfy

`(Z_I,Z_A,Z_B,Z_R)`
` ~ Dirichlet(k alpha,(r-k) alpha,(s-k) alpha,(m-r-s+k) alpha)`

with zero-size categories omitted and their masses fixed to zero. Also put

`mu_r=E[q_u(B_r)]`, `B_r ~ Beta(r alpha,(m-r) alpha)`.

Then the finite-sample variance under the symmetric-Dirichlet gap null is exactly

`Var_G(bar T)`
` = (m/4) sum_(r=1)^(m-1) sum_(s=1)^(m-1) sum_(d=0)^(m-1)`
`   [M_(r,s,k_(r,s)(d)) - mu_r mu_s]`.

Thus the missing dependent-gap variance from `VIS-240` and `VIS-241` is not an unstructured `2m`-dimensional covariance problem. It reduces exactly to the overlap cardinality of two cyclic gap intervals and a family of at most four-component Dirichlet expectations. Because `q_u` is piecewise quadratic, every `M_(r,s,k)` is a finite combination of truncated Dirichlet polynomial moments over linear half-space intersections and can be evaluated by deterministic low-dimensional integration; Monte Carlo is not required by the mathematics.

The `alpha=1` member admits a stronger closed form. In that case the rotated Dirichlet spacings are exactly `m` iid uniform points on the circle, and

`Var(bar T)`
` = binom(m,2) [2u/3 - 4u^2/3 + 11u^3/15 - u^4/9]`.

Together with the mean from `VIS-240`,

`E[bar T]=binom(m,2)(u-u^2/3)`,

this gives an exact finite-sample center-and-variance benchmark for the iid-uniform specialization and an analytic audit point for any implementation of the general `alpha` formula.

**Evidence/status:** `EXACT-DERIVED + DIRICHLET-AGGREGATION + U-STATISTIC SPECIALIZATION + REPRESENTATION-MATCHED VARIANCE CALIBRATION + NO-NOVELTY-CLAIM`.

No value of `alpha` is inferred from prime data, no prime residual is tested, no asymptotic point-process law is claimed, and no RH consequence follows from this calibration identity.

## 1. The cut average is half the sum over oriented cyclic arcs

For a fixed unordered pair of circular points, let `s` be one forward arc fraction and `1-s` the complementary arc fraction. `VIS-241` shows that its cut-averaged contribution is

`(1-d(s)/u)_+(1-d(s))`,

where `d(s)=min(s,1-s)`. Since `u<=1/2`, this equals `q_u(s)` as defined above, and `q_u(s)=q_u(1-s)`.

Every unordered pair appears exactly twice among the oriented arc variables `S_(i,r)`: once along one direction and once along its complement. Therefore

`bar T=(1/2) sum_(i,r) q_u(S_(i,r))`

exactly, including the even-`m` half-circle case because the two orientations remain the two copies of the same unordered pair and `q_u` is complement-symmetric.

This representation removes the arbitrary cut phase before the dependent-gap variance is attacked. Random rotation no longer appears because `bar T` depends only on the cyclic gaps.

## 2. Two arc sums depend only on four gap categories

Fix two oriented gap intervals

`A=A_(0,r)`, `B=A_(d,s)`.

Partition the `m` Dirichlet coordinates into

`I=A intersect B`,
`P=A setminus B`,
`Q=B setminus A`,
`R=(A union B)^c`.

Their cardinalities are respectively

`k`, `r-k`, `s-k`, `m-r-s+k`.

The aggregation property of the Dirichlet distribution gives the exact joint law

`(Z_I,Z_A,Z_B,Z_R)`
` = (sum_I X_j, sum_P X_j, sum_Q X_j, sum_R X_j)`
` ~ Dirichlet(k alpha,(r-k) alpha,(s-k) alpha,(m-r-s+k) alpha)`.

If one category is empty, its sum is identically zero and the positive categories carry the corresponding lower-dimensional Dirichlet law.

The two arc masses are

`S_A=Z_I+Z_A`, `S_B=Z_I+Z_B`.

Because the symmetric Dirichlet law is exchangeable, no information about the physical placement of the two cyclic intervals survives beyond these four cardinalities. In particular, for the covariance of the chosen statistic, two arc pairs with the same `(r,s,k)` have exactly the same joint law even if their intersections sit at different locations on the circle.

This proves that

`E[q_u(S_A)q_u(S_B)]=M_(r,s,k)`

and that the single-arc mean is

`mu_r=E[q_u(B_r)]`, `B_r~Beta(r alpha,(m-r) alpha)`.

By the notation of `VIS-240`,

`mu_r=J_(r alpha,(m-r) alpha)(u)+J_((m-r) alpha,r alpha)(u)`.

## 3. Cyclic stationarity gives the exact variance sum

Expanding the variance of the oriented-arc representation gives

`Var(bar T)`
` = (1/4) sum_(i,r) sum_(j,s)`
`   Cov(q_u(S_(i,r)),q_u(S_(j,s)))`.

The gap law is invariant under cyclic relabeling. For each first start `i`, the covariance with a second start `j` depends only on the relative displacement `d=j-i mod m`, and there are exactly `m` choices of `i` for every `(r,s,d)`.

Substituting the overlap-class covariance therefore yields

`Var_G(bar T)`
` = (m/4) sum_(r,s,d)`
`   [M_(r,s,k_(r,s)(d))-mu_r mu_s]`.

This is a finite exact formula. If desired, one may compress the displacement sum further by defining

`N_(r,s,k)=#{d in Z/mZ : k_(r,s)(d)=k}`

and replacing `sum_d` by `sum_k N_(r,s,k)`. The overlap counts are deterministic combinatorics of two cyclic intervals; all probability is confined to the low-dimensional `M_(r,s,k)` terms.

Since `q_u` is supported on `[0,u] union [1-u,1]` and is quadratic on each support component, each `M_(r,s,k)` is a finite sum of Dirichlet moments truncated by the two linear conditions on `Z_I+Z_A` and `Z_I+Z_B`. This gives a deterministic quadrature route whose dimension never grows with `m`.

## 4. The iid-uniform member collapses to a pairwise-uncorrelated U-statistic

At `alpha=1`, symmetric circular Dirichlet spacings plus an independent uniform rotation are exactly the circular spacings of `m` iid uniform points. Write those points as `U_1,...,U_m` and let `D_ij` be their shorter circular distance normalized by `L`.

Then

`bar T=sum_(i<j) h_u(D_ij)`,

with

`h_u(d)=(1-d/u)(1-d)` for `0<=d<=u`,

and zero for `d>u`.

For two disjoint pairs, their kernel values are independent. For two pairs sharing one point, say `(1,2)` and `(1,3)`, condition on `U_1`. Rotational invariance makes

`E[h_u(D_12)|U_1]`

independent of `U_1`, while `U_2` and `U_3` are conditionally independent. Hence the covariance of the two shared-point terms is exactly zero. All distinct unordered-pair contributions are therefore pairwise uncorrelated, so

`Var(bar T)=binom(m,2) Var(h_u(D))`,

where `D` has density `2` on `[0,1/2]`.

The first two moments are elementary:

`E[h_u(D)]`
` = 2 integral_0^u (1-d/u)(1-d) dd`
` = u-u^2/3`,

and

`E[h_u(D)^2]`
` = 2 integral_0^u (1-d/u)^2(1-d)^2 dd`
` = 2u/3-u^2/3+u^3/15`.

Subtracting the square of the mean gives

`Var(h_u(D))`
` = 2u/3 - 4u^2/3 + 11u^3/15 - u^4/9`,

which proves the displayed closed form.

This specialization is especially useful because it checks both the mean and covariance bookkeeping without any fitted parameter or numerical integration.

## 5. Prior art and novelty boundary

Uniform spacings, their Dirichlet representation, and sums/functions of spacings are classical; `VIS-240` already records Ronald Pyke's **Spacings** (1965) and standard Dirichlet references as the baseline. Fred W. Huffer, **Divided differences and the joint distribution of linear combinations of spacings**, *Journal of Applied Probability* 25:2 (1988), 346–354, DOI `10.2307/3214442`, explicitly treats exact joint distributions of linear combinations of uniform spacings and exact expectations arising in uniformity testing. This is a prior-art boundary against claiming that exact low-dimensional reduction of uniform-spacing functionals is new in general.

The `alpha=1` pair-sum is a degree-two U-statistic in the classical sense of Wassily Hoeffding, **A Class of Statistics with Asymptotically Normal Distribution**, *Annals of Mathematical Statistics* 19:3 (1948), 293–325, DOI `10.1214/aoms/1177730196`. The vanishing shared-point covariance here is the elementary translation-invariant specialization of that framework, not a new U-statistic theorem.

No novelty is claimed for Dirichlet aggregation, beta marginals, U-statistic variance decomposition, or truncated Dirichlet integration. The Mathia-specific contribution is the exact reduction of the particular endpoint-quotiented tent calibration from `VIS-241` to cyclic overlap classes, together with the closed `alpha=1` audit formula. It closes the previously explicit variance gap in the active representation-matched null without pretending to solve the subsequent prime-specific test.

## Boundaries and falsification

The formula assumes the symmetric-Dirichlet gap family of `VIS-240`, with `alpha` fixed independently of the confirmation statistic, and the endpoint-phase-invariant choice `bar T` from `VIS-241`. If physical endpoints are signal rather than nuisance, the full linear statistic requires adding the separate exact channel `E_G[V_cut]` from `VIS-241`.

For `alpha!=1`, the formula is exact but not an elementary scalar polynomial: the overlap-class terms are truncated multivariate Dirichlet moments. Numerical cubature may evaluate them, but numerical accuracy is then a computational issue distinct from the mathematical reduction. Fitting `alpha` on the same observed tent statistic would still invalidate a confirmatory comparison even though the variance formula itself is exact.

The family is not asserted to model all prime-gap dependence. Long-range arithmetic structure can lie outside one symmetric Dirichlet parameter, and a residual relative to this family would still require comparison with stronger predeclared spacing controls before being called prime-specific.

Falsify the overlap reduction by exhibiting two pairs of oriented arcs with the same `(r,s,k)` but different joint laws under the symmetric Dirichlet gaps. Falsify the variance formula by exact integration or independently validated high-precision computation for some `(m,alpha,u)` that disagrees with the overlap sum. At `alpha=1`, the polynomial variance is a mandatory audit identity.

## Research consequence

The immediate variance-calibration gap in `CLUE-prime-phase-critical-logarithmic-occupancy` is now mathematically closed: for every predeclared `alpha`, the null variance is an exact finite overlap-class sum, and the iid-uniform member has a closed polynomial benchmark.

The next step is a separate confirmation problem and should not be folded into this finding. Freeze `alpha` (or a stronger null) independently, evaluate the exact calibration for the predeclared critical family, and only then compare the prime configuration. Any surviving residual remains a point-process statement until it is translated back through the signed prime-phase kernel.