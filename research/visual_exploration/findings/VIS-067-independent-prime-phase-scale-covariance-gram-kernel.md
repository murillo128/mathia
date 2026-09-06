# VIS-067 — independent prime-phase scale covariance is an exact coefficient Gram kernel

## Claim

Let `I` be any finite set of predeclared visual coordinates, such as height/scale-pair cells. For each `alpha in I`, consider a finite randomized-prime-phase log-modulus observable

`A_alpha(theta) = Re sum_p sum_(k>=1) c_(alpha,p,k) exp(i k theta_p)`,

where only finitely many coefficients are nonzero and the prime phases `theta_p` are independent uniform variables on `[0,2 pi)`. This includes the standard Steinhaus-style control obtained by replacing each deterministic prime phase by one independent phase per prime while preserving the prime-power harmonics of that prime.

Then

`E[A_alpha] = 0`

and, exactly,

`Cov(A_alpha,A_beta)`
` = (1/2) Re sum_p sum_(k>=1) c_(alpha,p,k) conjugate(c_(beta,p,k))`.

Consequently the complete covariance matrix of the randomized field is a positive-semidefinite Gram matrix of the deterministic coefficient vectors. In particular, structured covariance across nearby hybrid scales or nearby height coordinates can be forced entirely by overlap of the same prime-power coefficient vectors under the randomized null; a covariance ridge, block, anisotropy, or multiscale band is not by itself evidence of additional arithmetic organization.

For the common case

`c_(alpha,p,k) = d_(alpha,p,k) exp(-i k t_alpha log p)`

with real coefficient weights `d_(alpha,p,k)`, the kernel becomes

`Cov(A_alpha,A_beta)`
` = (1/2) sum_p sum_(k>=1) d_(alpha,p,k) d_(beta,p,k)`
`     cos(k (t_alpha-t_beta) log p)`.

Thus the randomized-prime-phase second-order baseline is analytically computable from the retained prime-power weights; Monte Carlo simulation is needed only for sampling uncertainty, nonlinear statistics, or higher-order distributional questions, not to discover its expected covariance geometry.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL STEINHAUS-NULL SPECIALIZATION + NEGATIVE/CONTROL + NO-NOVELTY-CLAIM`.

Independent Steinhaus variables on primes are classical random-multiplicative-function prior art. The covariance formula here is elementary Fourier orthogonality on the product torus, specialized as a Mathia control for the accepted hybrid prime-phase visual thread. No new theorem about random multiplicative functions, hybrid Euler–Hadamard moments, zeta, or RH is claimed.

## 1. Exact torus orthogonality

Write

`U_alpha(theta)=sum_p sum_k c_(alpha,p,k) exp(i k theta_p)`,

so that

`A_alpha=(U_alpha+conjugate(U_alpha))/2`.

Every nonzero Fourier mode has zero Haar mean, hence `E[A_alpha]=0`.

For distinct primes, independence makes mixed terms vanish. For one prime, orthogonality gives

`E[exp(i(k-l)theta_p)] = 1` when `k=l` and `0` otherwise,

while terms with frequency `k+l>0` also average to zero. Expanding the two real parts therefore leaves only matching prime and matching harmonic:

`E[A_alpha A_beta]`
` = (1/2) Re sum_p sum_k c_(alpha,p,k) conjugate(c_(beta,p,k))`.

Because both means vanish, this is the covariance.

The use of one phase `theta_p` per prime is essential. Prime powers `p^k` retain harmonics `exp(i k theta_p)` and are not randomized independently. An independent phase per prime power is a different null that destroys multiplicative coherence inside each Euler factor.

## 2. The covariance matrix is a deterministic Gram object

Define a real inner product on the finite complex coefficient arrays by

`<c_alpha,c_beta>_R = Re sum_(p,k) c_(alpha,p,k) conjugate(c_(beta,p,k))`.

Then

`Gamma_(alpha,beta) = Cov(A_alpha,A_beta) = (1/2)<c_alpha,c_beta>_R`.

Therefore `Gamma` is positive semidefinite. Its rank is at most the real dimension of the span of the coefficient vectors used by the predeclared visual coordinates.

This is a direct representation-artifact control. If adjacent scale increments reuse nearly the same weighted prime powers, their coefficient vectors are close and the null covariance is automatically large. If two scale bands are nearly orthogonal in coefficient space, the null covariance is small. The shape of a second-order scale heatmap can therefore reflect the geometry of the truncation/smoothing weights before any special property of zeta has entered.

## 3. Height dependence is also forced by the same prime frequencies

Suppose the deterministic height phase is retained in the coefficient,

`c_(alpha,p,k)=d_(alpha,p,k) exp(-i k t_alpha log p)`

with real `d_(alpha,p,k)`. Substitution into the Gram formula gives

`Re[c_alpha conjugate(c_beta)]`
` = d_alpha d_beta cos(k(t_alpha-t_beta)log p)`.

Hence even the cross-height covariance of the randomized control contains a deterministic superposition of the prime frequencies `k log p`. Apparent oscillatory bands or diagonal localization in a height-by-height covariance image may therefore survive phase randomization for a completely understood reason.

This does not make the control useless. It makes it sharper: the exact kernel states what second-order structure the control is *supposed* to retain.

## 4. Application to hybrid within-prime scale increments

The accepted recursive-geometry clue now asks first for a within-prime scale observable such as

`A_XY(s)=log|P_Y(s)/P_X(s)|`.

For any fixed finite hybrid prime factors `P_X,P_Y`, their logarithms are finite weighted prime-power sums. After applying one independent Steinhaus phase per prime, each predeclared height/scale cell has the form above with coefficients equal to the deterministic difference of the two prime-power weight systems, including the factor `p^(-k sigma)` and deterministic height phase.

Therefore a randomized-prime-phase comparison must not treat its own covariance geometry as a featureless baseline. Before interpreting an arithmetic covariance map, compute the exact Gram kernel induced by the chosen smoothing, scale pair, sigma, height grid, and shared-phase convention.

A useful arithmetic residual can then be defined against that exact second-order null, for example through a predeclared quadratic witness or another statistic whose control uncertainty is calibrated according to `VIS-060`--`VIS-063`. The present result does not choose that witness; it removes one avoidable source of visual false positives before confirmation data are inspected.

## 5. Prior art and novelty boundary

Andriy Bondarenko and Kristian Seip, **Helson's problem for sums of a random multiplicative function**, *Mathematika* 62:1 (2016), 101–110, DOI `10.1112/S0025579315000236`, use the standard completely multiplicative random model generated by independent Steinhaus variables `z(p)` on the primes. The broader random-multiplicative-function literature extensively studies Euler-product and prime-phase models.

The Mathia statement is not a new random-multiplicative-function theorem. It is the elementary finite Fourier covariance identity needed to calibrate the particular randomized-prime-phase control proposed by the hybrid visual clue. Its novelty status is therefore deliberately `NO-NOVELTY-CLAIM`.

The hybrid factor itself remains grounded in S. M. Gonek, C. P. Hughes, and J. P. Keating, **A hybrid Euler-Hadamard product for the Riemann zeta function**, *Duke Mathematical Journal* 136:3 (2007), 507–549, DOI `10.1215/S0012-7094-07-13634-2`.

## 6. Boundaries and falsification

The exact formula assumes a finite coefficient family, which is sufficient for the finite hybrid prime factors and finite visual grids considered here. Infinite random Euler products require their own convergence/interchange hypotheses and are outside this finding.

The formula describes the ensemble obtained by sharing the same independent prime phases across all coordinates in the field. If each height or scale cell is randomized independently, cross-cell covariance changes, often to zero. The control protocol must therefore state whether prime phases are shared or resampled; those are mathematically different nulls.

The result controls only second moments. A field can have exactly the predicted covariance and still differ from the null in higher-order, nonlinear, tail, topological, or conditional structure. Such a claim needs a separately frozen statistic and its own calibrated null.

Falsify the exact claim by exhibiting a finite coefficient family with independent uniform prime phases for which either a nonzero mean appears or the displayed covariance differs from direct Haar integration.

## Research consequence

The accepted hybrid prime-phase clue remains live but its simplest randomized control is now exact at second order. A visual covariance ridge or multiscale band that is already present in the coefficient Gram kernel is baseline structure, not an arithmetic discovery.

The next coherent experiment should freeze a within-factor statistic and compare the arithmetic field with the exact Gram baseline plus an honestly calibrated control ensemble. If the intended signal is second-order, subtract or whiten against this deterministic kernel before confirmation. If it is higher-order, preserve the same prime-level multiplicative coherence and test the predeclared higher-order statistic rather than interpreting residual covariance geometry post hoc.