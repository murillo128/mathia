# VIS-116 — fixed-multiset cyclic third-order variance factors through lag-triangle overlap geometry

## Claim

Let `N>=6` and let `x_0,...,x_(N-1)` be fixed real values with exact centering

`sum_i x_i = 0`.

Let `pi` be a uniformly random permutation of these values around the cyclic positions `Z/NZ`, and write

`X_i = x_(pi(i))`.

For distinct nonzero lags `a,b in Z/NZ`, define

`T_pi(a,b) = (1/N) sum_i X_i X_(i+a) X_(i+b)`.

Put

`p_k = sum_i x_i^k`

and let `(N)_m=N(N-1)...(N-m+1)`. As in `VIS-115`, the exact mean is

`mu = E_pi[T_pi(a,b)] = 2 p_3/(N)_3`.

Now set

`D={0,a,b} subset Z/NZ`

and, for `r=0,1,2,3`, define the lag-triangle overlap counts

`c_r = #{d in Z/NZ : |D intersection (D+d)| = r}`.

Define four finite-population overlap moments

`Q_0 = -5(3p_2^3-18p_2p_4-8p_3^2+24p_6)/(N)_6`,

`Q_1 =  (3p_2^3-18p_2p_4-8p_3^2+24p_6)/(N)_5`,

`Q_2 = (-p_2^3+5p_2p_4+2p_3^2-6p_6)/(N)_4`,

`Q_3 = (p_2^3-3p_2p_4+2p_6)/(N)_3`.

Then exactly

`E_pi[T_pi(a,b)^2] = (1/N) sum_(r=0)^3 c_r Q_r`,

and therefore

`Var_pi(T_pi(a,b)) = (1/N) sum_(r=0)^3 c_r Q_r - mu^2`.

The entire single-coefficient random-permutation variance thus factors into two independent pieces:

1. the empirical one-point moments `p_2,p_3,p_4,p_6` of the fixed multiset;
2. the translation-overlap geometry of the three-point lag set `D={0,a,b}`.

Moreover,

`sum_r c_r=N`,

`sum_r r c_r=9`,

and `c_3` is the size of the translation stabilizer of `D`, hence `c_3 in {1,3}`. If `c_3=1` and `rho=c_2`, then

`c_1=6-2rho`,

`c_0=N-7+rho`,

with `0<=rho<=3`. In particular, when all six nonzero directed differences

`+/-a, +/-b, +/-(b-a)`

are distinct, `rho=0` and

`Var_pi(T_pi(a,b))`
` = [Q_3 + 6Q_1 + (N-7)Q_0]/N - mu^2`.

If the empirical moments `m_k=p_k/N` remain bounded as `N` grows, then for every non-stabilized lag triangle (`c_3=1`)

`Var_pi(T_pi(a,b)) = m_2^3/N + O(N^-2)`.

For the exceptional order-three subgroup geometry (`c_3=3`),

`Var_pi(T_pi(a,b)) = 3m_2^3/N + O(N^-2)`.

Thus the fixed-multiset permutation dependence and the marginal-skewness correction of `VIS-115` do **not** change the generic `N^(-1/2)` standard-deviation scale found for the independent centered null in `VIS-114`. They do change the exact finite-size mean and variance, and the variance carries a precise lag-triangle resonance correction that a flat independent-null normalization cannot see.

**Evidence/status:** `EXACT-DERIVED + FINITE-POPULATION/PERMUTATION CONTROL + HIGHER-ORDER-STATISTICS BASELINE + LAG-GEOMETRY CLASSIFICATION + NO-NOVELTY-CLAIM`.

No joint covariance formula for several lag pairs, constrained-surrogate variance, finite-size CUE law, zeta/CUE difference, asymptotic normality, or RH implication is established.

## 1. Products of two cyclic triple terms depend only on overlap size

Write

`Y_i = X_i X_(i+a) X_(i+b)`.

Then

`T_pi(a,b)=N^(-1) sum_i Y_i`.

For a pair `(i,j)`, put `d=j-i`. The two position triples are translates

`i+D`

and

`i+d+D`.

Their intersection size is therefore

`r(d)=|D intersection (D+d)|`.

Under a uniform random permutation, the values occupying any fixed collection of distinct positions are an ordered sample without replacement from the same fixed population. Consequently `E[Y_iY_j]` depends only on how many positions are shared by the two triples, not on their absolute locations.

If the overlap size is `r`, then the shared values occur squared in `Y_iY_j`, while the `6-2r` nonshared values occur to the first power. Thus the exponent patterns are

`r=0: (1,1,1,1,1,1)`,

`r=1: (2,1,1,1,1)`,

`r=2: (2,2,1,1)`,

`r=3: (2,2,2)`.

The corresponding expectations are exactly `Q_0,Q_1,Q_2,Q_3` above.

For each shift `d` there are exactly `N` ordered pairs `(i,j)` with `j-i=d`. Hence

`E[T_pi^2]`
` = N^(-2) sum_(i,j) E[Y_iY_j]`
` = N^(-1) sum_d Q_(r(d))`
` = N^(-1) sum_r c_r Q_r`.

Subtracting the squared mean from `VIS-115` gives the variance formula.

## 2. Exact finite-population moment reduction

For an exponent vector `alpha=(alpha_1,...,alpha_m)`, let

`S(alpha) = sum_(i_1,...,i_m distinct) product_(j=1)^m x_(i_j)^(alpha_j)`.

Möbius inversion on the lattice of set partitions gives the standard distinct-index identity

`S(alpha)`
` = sum_(P partition of {1,...,m})`
`   [product_(B in P) (-1)^(|B|-1)(|B|-1)!]`
`   product_(B in P) p_(sum_(j in B) alpha_j)`.

Because `p_1=0`, substituting the four exponent patterns yields

`S(1,1,1,1,1,1)`
` = -15p_2^3 + 90p_2p_4 + 40p_3^2 - 120p_6`,

`S(2,1,1,1,1)`
` = 3p_2^3 - 18p_2p_4 - 8p_3^2 + 24p_6`,

`S(2,2,1,1)`
` = -p_2^3 + 5p_2p_4 + 2p_3^2 - 6p_6`,

`S(2,2,2)`
` = p_2^3 - 3p_2p_4 + 2p_6`.

Dividing by the appropriate number `(N)_(6-r)` of ordered samples without replacement gives `Q_r`.

This also supplies a direct falsification route for the formulas: brute enumeration of all permutations for any centered finite population with `N>=6` must match the displayed variance once the four overlap counts are computed.

## 3. The overlap counts are the directed-difference geometry of the lag triangle

For each cyclic shift `d`,

`r(d)=|D intersection (D+d)|`

is also the number of ordered pairs `(u,v) in D^2` with

`v-u=d`.

So the overlap profile is exactly the multiplicity profile of the directed difference multiset `D-D`.

Summing over all shifts counts every ordered pair in `D^2` once, which gives

`sum_d r(d)=|D|^2=9`.

Equivalently,

`c_1+2c_2+3c_3=9`.

The shifts with `r(d)=3` are precisely the translation stabilizer

`H={d : D+d=D}`.

`H` is a subgroup of `Z/NZ`, and `D` is a union of `H`-cosets. Since `|D|=3`, the stabilizer size divides `3`, so

`c_3=|H| in {1,3}`.

The generic case has only the identity stabilizer, `c_3=1`. Then setting `rho=c_2` gives immediately

`c_1=6-2rho`

and, from `sum_r c_r=N`,

`c_0=N-7+rho`.

Repeated nonzero directed differences are therefore exactly the finite-size resonance that injects `Q_2` terms into the permutation variance. When the six nonzero directed differences are all distinct, `rho=0`.

The exceptional case `c_3=3` occurs exactly when `D` is a coset of the order-three subgroup of `Z/NZ`. Then translating by either nonzero stabilizer element reproduces the same three positions, so the cyclic average contains each unordered triple product three times. The factor `3` in the leading variance is therefore structural rather than a moment accident.

## 4. Large-`N` scale and relation to the independent null

Write `m_k=p_k/N` and suppose `m_2,...,m_6=O(1)`. Direct expansion gives

`Q_3 = m_2^3 + O(N^-1)`,

`Q_2 = -m_2^3/N + O(N^-2)`,

`Q_1 = 3m_2^3/N^2 + O(N^-3)`,

`Q_0 = -15m_2^3/N^3 + O(N^-4)`,

while

`mu=O(N^-2)`.

For `c_3=1`, the remaining overlap counts are uniformly bounded except `c_0=N+O(1)`, so the only `N^-1` contribution to the variance is `Q_3/N`. Therefore

`Var_pi(T_pi)=m_2^3/N+O(N^-2)`.

This matches the leading independent-null variance from `VIS-114` after identifying `m_2` with the empirical variance scale. The agreement is only leading-order. Random permutation preserves the exact fixed multiset and therefore carries the finite-population mean from `VIS-115`, higher empirical moments, and lag-overlap corrections absent from the independent model.

For `c_3=3`, the three identical-translate copies of each lag triangle make the leading term `3Q_3/N`, producing the exceptional factor `3`.

This establishes a useful hierarchy of controls. The independent centered null gives the elementary `N^-1/2` sanity-check scale; the fixed-multiset shuffle preserves the exact one-point empirical distribution and supplies exact finite-size corrections; a source-faithful CUE or other structured null must still preserve the dependence relevant to the actual zeta comparison.

## 5. Prior art and novelty assessment

Finite-population moments and product moments under sampling without replacement are classical. J. G. Skellam, **The Distribution of the Moment Statistics of Samples Drawn Without Replacement from a Finite Population**, *Journal of the Royal Statistical Society: Series B* 11:2 (1949), 291–296, DOI `10.1111/j.2517-6161.1949.tb00035.x`, is an early direct source.

Paul S. Dwyer and Derrick S. Tracy, **Expectation and Estimation of Product Moments in Sampling From a Finite Population**, *Journal of the American Statistical Association* 75:370 (1980), 431–437, DOI `10.1080/01621459.1980.10477490`, develops compact expectation formulae for finite-population product moments.

Christopher S. Withers and Saralees Nadarajah, **Unbiased Estimates for Products of Moments and Cumulants for Finite Populations**, *Mathematics* 11:17 (2023), 3720, DOI `10.3390/math11173720`, gives explicit finite-population moment/cumulant product expressions through total order six, exactly the order needed by the squared third-order statistic here.

The displayed `Q_r` formulae are elementary specializations of this classical finite-population product-moment machinery, and the decomposition by `c_r` is the direct overlap bookkeeping for the cyclic three-point statistic used by the current visual branch. **No new general theorem in sampling theory, permutation testing, or higher-order time-series statistics is claimed.**

The Mathia-specific value is the exact identification of which part of a future third-order lag heatmap is forced by the empirical value multiset and which finite-size variance correction is forced by the geometry of the chosen lag triangle before any zeta/CUE comparison is attempted.

## Boundary and falsification

The theorem requires:

- a complete cyclic sequence of `N>=6` positions;
- three distinct cyclic positions `0,a,b`;
- exact centering of the fixed value multiset;
- a uniform random permutation of that exact multiset.

It does not apply unchanged to the noncyclic admissible-start statistic of `VIS-114`, local/window-specific re-centering, repeated lag positions, a Markov-type-constrained surrogate, a shuffle preserving autocorrelation, CUE eigenangle gaps, or any other source-preserving null. Those designs have different overlap and sampling laws.

The formula calibrates one lag coefficient at a time. A pooled lag-plane statistic also needs the **joint covariance between different lag triangles**; the present result does not derive it. Likewise the generic `N^-1/2` scale does not imply Gaussianity.

The exact claim would be falsified by a centered finite population, admissible lag pair, and exhaustive permutation calculation whose empirical second moment differs from `N^-1 sum_r c_r Q_r`, or whose overlap counts fail the directed-difference identities above.

## Visual consequence

No canonical PNG is retained. The algebra already determines the relevant visual correction.

A fixed-multiset third-order lag heatmap should first subtract the exact marginal-skewness DC level from `VIS-115`. If coefficients are then standardized against the random-shuffle null, the denominator should use the **lag-specific exact variance above**, not a globally flat independent-noise variance. Away from repeated-difference or subgroup resonances the leading scale is asymptotically flat, but the finite-size correction is mathematically determined by the lag-triangle overlap class.

A useful diagnostic rendering may later mark repeated-difference and order-three-subgroup lag triangles explicitly, because those are null-geometry features rather than source discoveries.

## Research consequence

`VIS-114` established the exact independent-centered fluctuation scale. `VIS-115` replaced the incorrect zero-mean assumption for a complete cyclic fixed-multiset shuffle by the exact marginal-skewness baseline. The present finding completes the corresponding **single-coefficient variance calibration** for that shuffle.

The accepted multiscale clue can therefore require three distinct gates before a source-facing third-order residual is interpreted: subtract the exact fixed-multiset mean, standardize against the correct lag-geometry-aware lower-information null, and then compare the surviving statistic against the actual finite-size source-faithful control such as CUE.

The next mathematical boundary is not another consequence of the single-coefficient formula. It is either a joint covariance theorem for a predeclared low-dimensional lag panel or, more importantly, a finite-size CUE/source-null calibration for the chosen growing-lag statistic. Those are separate research questions and are intentionally left for later invocations.
