# VIS-117 — fixed-multiset cyclic third-order cross-covariance factors through cross-triangle overlap geometry

## Claim

Let `N>=6` and let `x_0,...,x_(N-1)` be fixed real values with exact centering

`sum_i x_i = 0`.

Let `pi` be a uniformly random permutation of these values around the cyclic positions `Z/NZ`, and write

`X_i = x_(pi(i))`.

For two three-point lag sets

`D={0,a,b}`

and

`E={0,c,d}`

with three distinct residues in each set, define

`T_pi(D) = (1/N) sum_i product_(u in D) X_(i+u)`,

`T_pi(E) = (1/N) sum_i product_(v in E) X_(i+v)`.

Put

`p_k = sum_i x_i^k`,

let `(N)_m=N(N-1)...(N-m+1)`, and use the four finite-population overlap moments from `VIS-116`:

`Q_0 = -5(3p_2^3-18p_2p_4-8p_3^2+24p_6)/(N)_6`,

`Q_1 =  (3p_2^3-18p_2p_4-8p_3^2+24p_6)/(N)_5`,

`Q_2 = (-p_2^3+5p_2p_4+2p_3^2-6p_6)/(N)_4`,

`Q_3 = (p_2^3-3p_2p_4+2p_6)/(N)_3`.

As in `VIS-115`, both coefficients have the same exact permutation mean

`mu = 2p_3/(N)_3`.

For `r=0,1,2,3`, define the **cross-triangle overlap counts**

`c_r(D,E) = #{s in Z/NZ : |D intersection (E+s)| = r}`.

Then exactly

`E_pi[T_pi(D) T_pi(E)] = (1/N) sum_(r=0)^3 c_r(D,E) Q_r`,

and therefore

`Cov_pi(T_pi(D),T_pi(E))`
` = (1/N) sum_(r=0)^3 c_r(D,E) Q_r - mu^2`.

Thus the complete second-order covariance matrix of any predeclared cyclic third-order lag panel under the fixed-multiset random-permutation null is determined by only:

1. the one-point empirical moments `p_2,p_3,p_4,p_6` of the fixed multiset;
2. the pairwise translation-overlap geometry of the lag triangles.

No permutation Monte Carlo is needed to obtain that covariance matrix.

The cross-overlap counts satisfy

`sum_r c_r(D,E)=N`,

`sum_r r c_r(D,E)=9`.

Let

`h=c_3(D,E)`,

`rho=c_2(D,E)`.

Then

`h in {0,1,3}`,

`c_1=9-2rho-3h`,

`c_0=N-9+rho+2h`,

and hence

`Cov_pi(T_pi(D),T_pi(E))`
` = [(N-9+rho+2h)Q_0 + (9-2rho-3h)Q_1 + rho Q_2 + h Q_3]/N - mu^2`.

Moreover `h>0` exactly when `D` and `E` are translates. In that case `T_pi(D)=T_pi(E)` identically, so the apparent two lag-plane coordinates are the same statistic and the displayed covariance reduces to the variance formula of `VIS-116`.

If `D` and `E` are not translates (`h=0`) and the empirical moments `m_k=p_k/N` remain bounded, then

`Cov_pi(T_pi(D),T_pi(E)) = -rho m_2^3/N^2 + O(N^-3)`

when `rho>0`, while in the fully generic cross-difference case `rho=0`,

`Cov_pi(T_pi(D),T_pi(E)) = 12 m_2^3/N^3 + O(N^-4)`.

For ordinary non-stabilized individual triangles, `VIS-116` gives variance `m_2^3/N+O(N^-2)`. Therefore two non-translation-equivalent coefficients have correlation only `O(N^-1)` when a repeated cross-difference creates a two-point overlap resonance, and `O(N^-2)` when all nine cross differences are distinct.

**Evidence/status:** `EXACT-DERIVED + FINITE-POPULATION/PERMUTATION CONTROL + JOINT LAG-PANEL CALIBRATION + CROSS-DIFFERENCE GEOMETRY + NO-NOVELTY-CLAIM`.

No constrained-surrogate covariance, finite-size CUE covariance, zeta/CUE difference, asymptotic Gaussian law, or RH implication is established.

## 1. The cross moment uses the same four finite-population moments as the variance

Write

`Y_i(D)=product_(u in D) X_(i+u)`,

`Y_j(E)=product_(v in E) X_(j+v)`.

Then

`T_pi(D)=N^(-1) sum_i Y_i(D)`,

`T_pi(E)=N^(-1) sum_j Y_j(E)`.

For a pair `(i,j)`, put `s=j-i`. The two position triples are

`i+D`

and

`i+(E+s)`.

Their intersection size is

`r(s)=|D intersection (E+s)|`.

Under a uniform random permutation, the values occupying any fixed collection of distinct positions are an ordered sample without replacement from the same fixed population. If the two triples overlap in `r` positions, the shared values occur squared in the product `Y_i(D)Y_j(E)` and the `6-2r` unshared values occur once. The exponent patterns are therefore exactly the same four patterns used in `VIS-116`:

`r=0: (1,1,1,1,1,1)`,

`r=1: (2,1,1,1,1)`,

`r=2: (2,2,1,1)`,

`r=3: (2,2,2)`.

Their expectations are `Q_0,Q_1,Q_2,Q_3` respectively.

For each cyclic shift `s` there are exactly `N` ordered pairs `(i,j)` with `j-i=s`. Consequently

`E[T_pi(D)T_pi(E)]`
` = N^(-2) sum_(i,j) E[Y_i(D)Y_j(E)]`
` = N^(-1) sum_s Q_(r(s))`
` = N^(-1) sum_r c_r(D,E)Q_r`.

Both coefficients have the same mean `mu` because every admissible triple samples three distinct population values symmetrically. Subtracting `mu^2` gives the covariance formula.

The finite-population algebra is therefore already complete at `VIS-116`: joint calibration does not require new moment identities, only cross-triangle overlap bookkeeping.

## 2. Cross-overlap counts are the multiplicities of `D-E`

For each shift `s`,

`r(s)=|D intersection (E+s)|`

is the number of ordered pairs `(u,v) in D x E` satisfying

`u-v=s`.

Thus `r(s)` is exactly the multiplicity of `s` in the directed cross-difference multiset

`D-E={u-v : u in D, v in E}`.

There are nine ordered cross pairs, so summing multiplicities over all shifts gives

`sum_s r(s)=9`.

Equivalently,

`c_1+2c_2+3c_3=9`.

Together with `c_0+c_1+c_2+c_3=N`, this yields the formulas for `c_0,c_1` once `rho=c_2` and `h=c_3` are fixed.

A shift has overlap three exactly when

`E+s=D`.

If no such shift exists, `h=0`. If one exists, all such shifts form a coset of the translation stabilizer of `E`. A three-point subset can have stabilizer size only `1` or `3`: if a subgroup stabilizes the subset, the subset is a union of its translation cosets, so the subgroup order divides `3`. Hence

`h in {0,1,3}`.

This also exposes an exact visual redundancy. If `E+s=D`, then reindexing the cyclic average gives

`T_pi(E)=T_pi(E+s)=T_pi(D)`.

Cells related by translating the underlying three-point lag set are not merely highly correlated; they are the same random variable. A lag-plane covariance matrix should quotient these exact orbit duplications before any whitening or dimension count.

## 3. Large-`N` off-diagonal covariance hierarchy

Write `m_k=p_k/N` and assume the relevant empirical moments remain `O(1)`. `VIS-116` gives

`Q_3 = m_2^3 + O(N^-1)`,

`Q_2 = -m_2^3/N + O(N^-2)`,

`Q_1 = 3m_2^3/N^2 + O(N^-3)`,

`Q_0 = -15m_2^3/N^3 + O(N^-4)`,

`mu=O(N^-2)`.

Suppose first that `D,E` are not translates, so `h=0`.

If `rho>0`, the `rho Q_2/N` term dominates, giving

`Cov_pi(T_pi(D),T_pi(E)) = -rho m_2^3/N^2 + O(N^-3)`.

The repeated cross difference is therefore the first off-diagonal resonance: two different lag triangles can share two positions under one or more translations, and fixed-multiset sampling turns those overlaps into a negative covariance one order below the individual `N^-1` variance.

If instead all nine cross differences are distinct, then `rho=0`, `c_1=9`, `c_0=N-9`, and

`Cov_pi(T_pi(D),T_pi(E))`
` = [(N-9)Q_0+9Q_1]/N-mu^2`
` = 12m_2^3/N^3+O(N^-4)`.

Thus a generic pair is even closer to orthogonal than a repeated-difference pair. The nonzero `N^-3` covariance is a finite-population effect: the fixed multiset couples disjoint position samples weakly even though chronology has been randomized.

For two ordinary non-stabilized triangles, each marginal variance is `m_2^3/N+O(N^-2)`. Hence the corresponding correlations are

`Corr_pi(T_pi(D),T_pi(E)) = -rho/N + O(N^-2)`

when `rho>0`, and

`Corr_pi(T_pi(D),T_pi(E)) = 12/N^2 + O(N^-3)`

when `rho=0`.

These are asymptotic statements about the fixed-multiset permutation null only. A CUE gap process or another source-preserving null can have materially different long-range covariance.

## 4. Exact covariance of a predeclared panel

Let `D_1,...,D_J` be any finite predeclared collection of admissible lag triangles and define

`Sigma_(alpha,beta)=Cov_pi(T_pi(D_alpha),T_pi(D_beta))`.

The theorem gives every matrix entry exactly from the same `Q_r` and the cross-overlap counts `c_r(D_alpha,D_beta)`. Therefore for deterministic weights `w_alpha`,

`Var_pi(sum_alpha w_alpha T_pi(D_alpha))`
` = sum_(alpha,beta) w_alpha w_beta Sigma_(alpha,beta)`.

The same matrix calibrates the residual coefficients

`R_pi(D_alpha)=T_pi(D_alpha)-mu`,

because subtracting the common deterministic mean does not change covariance.

This closes the second-moment calibration of any fixed-multiset random-shuffle lag panel. A pooled energy, signed contrast, low-dimensional projection, or whitened lag-plane diagnostic no longer needs to assume independent coefficients or estimate its covariance by repeated permutations when the uniform fixed-multiset shuffle is the declared null.

The matrix can be singular before orbit quotienting because translated lag triangles define identical coefficients. Additional exact or accidental linear dependencies are separate questions and should be checked for the chosen finite panel rather than inferred from a heatmap.

## 5. Prior art and novelty assessment

Finite-population product moments under sampling without replacement are classical. The exact `Q_r` quantities were already bounded against this literature in `VIS-116`, including J. G. Skellam, **The Distribution of the Moment Statistics of Samples Drawn Without Replacement from a Finite Population**, *Journal of the Royal Statistical Society: Series B* 11:2 (1949), 291–296, DOI `10.1111/j.2517-6161.1949.tb00035.x`; Paul S. Dwyer and Derrick S. Tracy, **Expectation and Estimation of Product Moments in Sampling From a Finite Population**, *Journal of the American Statistical Association* 75:370 (1980), 431–437, DOI `10.1080/01621459.1980.10477490`; and Christopher S. Withers and Saralees Nadarajah, **Unbiased Estimates for Products of Moments and Cumulants for Finite Populations**, *Mathematics* 11:17 (2023), 3720, DOI `10.3390/math11173720`.

Third-order correlations, cumulants, and bispectra are likewise classical higher-order-statistics objects; `VIS-109` and `VIS-114` record the standard Brillinger, Nikias--Raghuveer, and Mendel references. Random-permutation and surrogate-data calibration is standard methodology rather than a Mathia invention.

The present formulas are an elementary bilinear extension of `VIS-116`: the same finite-population product moments are indexed by the cross-correlation of two three-point support sets rather than the autocorrelation of one support set. The cross-difference counting and translation-orbit quotient are direct finite cyclic combinatorics. **No new general theorem in sampling theory, permutation testing, bispectral estimation, or finite-population statistics is claimed.**

A targeted literature check did not supply a reason to interpret this specialization as novel mathematics. Its value for Mathia is operational and epistemic: it gives the exact lower-information covariance that a third-order visual panel must remove before any residual is compared with a source-faithful zeta/CUE control.

## Boundary and falsification

The theorem requires:

- a complete cyclic sequence of `N>=6` positions;
- three distinct cyclic positions in each lag triangle;
- exact centering of the fixed value multiset;
- a uniform random permutation of that exact multiset.

It does not apply unchanged to the noncyclic admissible-start statistic of `VIS-114`, local/window-specific re-centering, repeated lag positions, a Markov-type-constrained surrogate, a shuffle preserving autocorrelation, CUE eigenangle gaps, or any other source-preserving null.

The exact formula would be falsified by a centered finite population, two admissible lag triangles, and exhaustive permutation calculation whose empirical cross moment differs from

`N^(-1) sum_r c_r(D,E)Q_r`,

or by cross-overlap counts that fail the nine-pair difference identities above. Direct exhaustive enumeration on small centered populations is a cheap independent check, but the proof itself is finite algebra and does not depend on simulation.

The large-`N` correlation statements additionally assume bounded empirical moments and, where stated, non-stabilized individual triangles. They do not imply joint Gaussianity or independence.

## Visual consequence

No canonical PNG is retained. The algebra determines the correction more exactly than a Monte Carlo covariance heatmap would.

For a fixed-multiset shuffle diagnostic, first quotient lag-plane cells that represent the same translated three-point support. Then subtract the common marginal-skewness mean from `VIS-115` and, for any predeclared collection of surviving cells, standardize or whiten using the exact covariance matrix above. Repeated cross differences should be marked as null-geometry resonances rather than source discoveries.

A visually coherent off-diagonal band that disappears after this exact lower-information whitening is therefore a shuffle-geometry artifact. A residual that survives still has not become arithmetic-specific: the next comparison must use the finite-size source-faithful null.

## Research consequence

`VIS-114` gives the independent-centered scale and exact orthogonality of distinct admissible-start coefficients. `VIS-115` gives the fixed-multiset cyclic mean. `VIS-116` gives the exact fixed-multiset marginal variance. The present finding completes the **joint second-moment calibration** of the uniform fixed-multiset cyclic shuffle for any predeclared third-order lag panel.

This closes the natural lower-information covariance question left explicitly open by `VIS-116`. Continuing to derive further consequences of the same shuffle covariance would now be scaffolding rather than the live source question.

The next distinct boundary is the one already identified by the accepted multiscale clue: choose a mathematically motivated growing-lag/global statistic before source inspection and derive or estimate its covariance under the actual finite-size source-faithful non-arithmetic control, such as CUE, before testing untouched zeta material. That is a separate research thread and is intentionally left for a later invocation.
