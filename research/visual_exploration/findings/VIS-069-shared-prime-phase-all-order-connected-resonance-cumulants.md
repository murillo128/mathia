# VIS-069 — every finite-order shared-prime-phase cumulant is an exact connected resonance polynomial

## Claim

Let `I` be a finite set of predeclared coordinates and let

`A_alpha(theta) = Re sum_p sum_(k>=1) c_(alpha,p,k) exp(i k theta_p)`,

where only finitely many coefficients are nonzero and the prime phases `theta_p` are independent uniform variables on `[0,2 pi)`, shared across all powers and all coordinates for the same prime.

For `m in Z\{0}` define the two-sided Fourier coefficient

`d_(alpha,p,m) = c_(alpha,p,m)/2` for `m>0`,

`d_(alpha,p,m) = conjugate(c_(alpha,p,-m))/2` for `m<0`.

Then

`A_(alpha,p)(theta_p) = sum_(m!=0) d_(alpha,p,m) exp(i m theta_p)`

and `A_alpha=sum_p A_(alpha,p)`.

For any nonempty block `B` of coordinate labels define the exact one-prime resonant moment

`M_p(B) = sum_(m_j!=0, j in B; sum_(j in B) m_j=0) prod_(j in B) d_(alpha_j,p,m_j)`.

For every order `r>=2`, the joint cumulant is

`kappa_r(A_(alpha_1),...,A_(alpha_r))`
` = sum_p sum_(pi in Pi_r) (-1)^(|pi|-1) (|pi|-1)!`
`     prod_(B in pi) M_p(B)`,

where `Pi_r` is the set of partitions of `{1,...,r}`. Because `M_p({j})=0`, every partition containing a singleton contributes zero.

Thus **every finite-order cumulant of the shared-prime-phase null is an exact deterministic connected resonance polynomial in the prime-power coefficient arrays**. Haar orthogonality supplies the zero-sum frequency constraints inside each block, and the ordinary cumulant partition formula removes products of lower-order disconnected resonances.

`VIS-067` is the `r=2` case. `VIS-068` is the `r=3` case. At fourth order,

`kappa_4 = sum_p [ M_p(1234)`
`  - M_p(12)M_p(34)`
`  - M_p(13)M_p(24)`
`  - M_p(14)M_p(23) ]`.

In particular, moving to fourth or higher cumulants does not create an automatically featureless baseline. Even the first-harmonic-only null is already non-Gaussian at fourth order.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL CUMULANT/PARTITION-LATTICE AND TORUS-ORTHOGONALITY SPECIALIZATION + NEGATIVE/CONTROL + NO-NOVELTY-CLAIM`.

No new theorem about random multiplicative functions, random Euler products, zeta moments, hybrid Euler–Hadamard products, or RH is claimed.

## 1. Primewise reduction

Write `A_alpha=sum_p A_(alpha,p)`. The vectors

`(A_(alpha,p))_(alpha in I)`

are independent across distinct primes because each depends only on `theta_p`.

Joint cumulants are additive across independent vector summands. Hence

`kappa_r(A_(alpha_1),...,A_(alpha_r))`
` = sum_p kappa_r(A_(alpha_1,p),...,A_(alpha_r,p))`.

The null therefore remains prime-local at every finite cumulant order. Cross-prime terms can appear in raw moments through products of lower-order primewise moments, but the connected cumulant removes exactly those disconnected products.

## 2. Haar integration gives the resonant moments

For one prime,

`A_(alpha,p) = sum_(m!=0) d_(alpha,p,m) exp(i m theta_p)`.

For any block `B`, finite expansion gives

`E prod_(j in B) A_(alpha_j,p)`
` = sum_(m_j!=0, j in B) [prod_(j in B) d_(alpha_j,p,m_j)]`
`     E exp(i theta_p sum_(j in B) m_j)`.

Uniform Haar integration on the circle is zero unless the signed frequencies sum to zero. Therefore the block moment is exactly `M_p(B)`.

This zero-sum condition contains all finite harmonic resonances allowed by the chosen prime-power coefficients: pair matches, additive three-wave relations, four-wave relations, and their higher-order analogues.

## 3. Partition Möbius inversion extracts the connected resonance

For random variables `X_1,...,X_r`, the standard moment-cumulant relation is

`kappa(X_1,...,X_r)`
` = sum_(pi in Pi_r) (-1)^(|pi|-1)(|pi|-1)!`
`     prod_(B in pi) E prod_(j in B) X_j`.

Substituting the exact resonant moments `M_p(B)` gives the displayed formula prime by prime.

This distinction matters from fourth order onward. A raw zero-sum `r`-tuple need not represent a genuinely connected `r`-way effect: it may factor into two or more lower-order zero-sum blocks. The partition terms subtract those factorizations exactly. The surviving cumulant is therefore the appropriate connected resonance baseline for skewness, trispectra, higher polyspectra, and other finite-order cumulant visualizations.

## 4. Recovery of the second- and third-order controls

For `r=2`, singleton blocks vanish and only one block remains:

`kappa_2(A_alpha,A_beta)=sum_p M_p(12)`.

Pairing frequency `m` with `-m` yields

`M_p(12) = (1/2) Re sum_(k>=1) c_(alpha,p,k) conjugate(c_(beta,p,k))`,

which is the coefficient-Gram covariance kernel of `VIS-067`.

For `r=3`, every nontrivial partition other than the one-block partition contains a singleton, so

`kappa_3=sum_p M_p(123)`.

The zero-sum signed triples are exactly the additive relations `k+l=m` and their placements, reproducing `VIS-068`.

The present formula therefore does not replace those findings; it identifies them as the first two members of one all-order finite null calculus.

## 5. Fourth-order sanity check: first harmonics are already non-Gaussian

Take one prime, one coordinate, and only the first harmonic:

`A(theta)=Re(c exp(i theta)) = |c| cos(theta+phi)`.

Then

`E[A^2]=|c|^2/2`,

`E[A^4]=3|c|^4/8`,

so

`kappa_4(A)=E[A^4]-3E[A^2]^2 = -3|c|^4/8`.

For independent primes with first-harmonic coefficients `c_p`, cumulant additivity gives

`kappa_4(sum_p Re(c_p exp(i theta_p))) = -(3/8) sum_p |c_p|^4`.

Thus the first-harmonic truncation that kills the third cumulant in `VIS-068` does **not** make the null Gaussian at the next order. A fourth-order excess, trispectral pattern, or kurtosis-like visual signal must still be compared with a nonzero exact null.

## 6. Prior art and novelty boundary

The partition-lattice formula for joint cumulants is classical. T. P. Speed, **Cumulants and partition lattices**, *Australian Journal of Statistics* 25:2 (1983), 378–388, DOI `10.1111/j.1467-842X.1983.tb00391.x`, treats cumulants explicitly as Möbius inversion on the partition lattice.

Independent Steinhaus phases at primes and their higher moments are likewise standard in probabilistic number theory. Jacques Benatar, Alon Nishry, and Brad Rodgers, **Moments of polynomials with random multiplicative coefficients**, *Mathematika* 68:1 (2022), 191–216, DOI `10.1112/mtk.12121`, study higher moments for polynomials with Steinhaus or Rademacher multiplicative coefficients and emphasize that multiplicative dependence produces nontrivial high-moment behavior. The random-multiplicative-function and random-zeta literature cited in `VIS-068` supplies the broader established context.

The present finding is only the finite product-torus specialization needed to make Mathia's chosen shared-prime-phase control explicit at arbitrary finite cumulant order. The formula follows directly from classical Haar orthogonality plus the classical moment-cumulant relation and therefore carries `NO-NOVELTY-CLAIM`.

## 7. Boundary of the control

The formula assumes a finite coefficient family. Infinite random Euler products require separate convergence, integrability, and interchange arguments.

It also assumes one phase per prime shared across prime powers and across all predeclared coordinates. Resampling by prime power or by cell changes the moment constraints and therefore defines a different null.

The result does not say that higher-order statistics are useless or that the arithmetic object must match the randomized null. It says that **finite-order moment/cumulant structure is not an uncalibrated escape route**: its shared-phase null is exactly computable from the chosen coefficient arrays before confirmation data are inspected.

A residual beyond this connected-resonance baseline can still be informative if the statistic, coordinates, normalization, and confirmation windows are frozen in advance and uncertainty is calibrated under a realizable control law. Non-cumulant nonlinear or topological statistics likewise require their own null audit; this finding does not reduce every deterministic statistic to cumulants.

Falsify the claim by giving a finite coefficient family and order `r>=2` for which direct product-torus integration and the standard joint-cumulant definition disagree with the displayed connected-resonance formula.

## Research consequence

The accepted prime-phase recursive-geometry clue is narrowed once more. After `VIS-067` and `VIS-068`, second- and third-order null tensors were explicit. This finding shows that the same calibration principle extends to **every finite cumulant order** without inventing a new null model each time.

The next admissible higher-order experiment should therefore freeze a concrete cumulant or polyspectral witness and subtract or compare against this exact connected-resonance baseline before examining arithmetic confirmation data. Simply escalating from covariance to skewness to kurtosis or higher polyspectra is not evidence of a new arithmetic channel.