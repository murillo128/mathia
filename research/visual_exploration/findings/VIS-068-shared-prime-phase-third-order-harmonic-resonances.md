# VIS-068 — shared prime phases force exact third-order harmonic resonances

## Claim

Let `I` be a finite set of predeclared visual coordinates and, as in `VIS-067`, define

`A_alpha(theta) = Re sum_p sum_(k>=1) c_(alpha,p,k) exp(i k theta_p)`,

where only finitely many coefficients are nonzero and the phases `theta_p` are independent uniform variables on `[0,2 pi)`, with one phase shared by all powers of a given prime.

Then the joint third cumulant is exact and entirely determined by same-prime additive harmonic resonances:

`kappa_3(A_alpha,A_beta,A_gamma)`
` = (1/4) Re sum_p sum_(k,l>=1) [`
`     c_(alpha,p,k) c_(beta,p,l) conjugate(c_(gamma,p,k+l))`
`   + c_(alpha,p,k) c_(gamma,p,l) conjugate(c_(beta,p,k+l))`
`   + c_(beta,p,k) c_(gamma,p,l) conjugate(c_(alpha,p,k+l)) ]`,

with absent coefficients interpreted as zero.

Because `E[A_alpha]=0` by `VIS-067`, this cumulant equals the third joint moment. Consequently a shared-Steinhaus prime-phase null is generally **not Gaussian at third order** once prime-power harmonics are retained. Skewness, a three-coordinate bispectral pattern, or a third-order scale tensor can be present under the randomized control for the completely deterministic reason that two harmonics `k,l` of one prime resonate with the harmonic `k+l` of the same prime.

If every prime contributes only its first harmonic `k=1`, the displayed tensor vanishes identically. Thus the first nonzero third-order baseline is specifically a prime-power coherence effect, not an independent cross-prime arithmetic signal.

For a single coordinate,

`E[A_alpha^3] = (3/4) Re sum_p sum_(k,l>=1)`
`  c_(alpha,p,k) c_(alpha,p,l) conjugate(c_(alpha,p,k+l))`.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL TORUS-ORTHOGONALITY SPECIALIZATION + NEGATIVE/CONTROL + NO-NOVELTY-CLAIM`.

No new theorem about random multiplicative functions, random Euler products, hybrid Euler–Hadamard moments, zeta, or RH is claimed.

## 1. Reduction to one prime

Write the contribution from prime `p` as

`A_(alpha,p)(theta_p) = Re sum_(k>=1) c_(alpha,p,k) exp(i k theta_p)`.

The full field is the finite sum

`A_alpha = sum_p A_(alpha,p)`.

Each prime component has mean zero, and components attached to distinct primes are independent. Joint cumulants of order at least two are additive across independent summands. Equivalently, if the third moment is expanded directly, every term involving more than one prime contains at least one prime that occurs only once, and integration over that prime phase kills the term.

Therefore

`kappa_3(A_alpha,A_beta,A_gamma)`
` = sum_p E[A_(alpha,p) A_(beta,p) A_(gamma,p)]`.

The higher-order control is prime-local before the prime contributions are summed.

## 2. Exact three-wave resonance formula

For a fixed prime put

`U_alpha = sum_(k>=1) c_(alpha,p,k) exp(i k theta_p)`,

so `A_(alpha,p)=(U_alpha+conjugate(U_alpha))/2`.

Expanding the product of three real parts gives eight signed Fourier terms. Haar integration over `theta_p` annihilates every term whose signed frequency is nonzero. Since all harmonic indices are positive, a surviving triple must have one index equal to the sum of the other two.

The three possible placements of the conjugated factor give

`E[U_alpha U_beta conjugate(U_gamma)]`
` = sum_(k,l>=1) c_(alpha,p,k)c_(beta,p,l)`
`   conjugate(c_(gamma,p,k+l))`,

and the two analogous permutations. Their complex-conjugate partners supply twice the real part. The factor `1/8` from the three real parts therefore becomes `1/4`, yielding the displayed formula.

This is the third-order analogue of the coefficient Gram kernel in `VIS-067`: second order selects the resonance `k=l`, while third order selects the additive resonance `k+l=m`.

## 3. Prime powers are exactly what makes the third cumulant survive

If the null were artificially truncated to one harmonic per prime,

`A_(alpha,p)=Re(c_(alpha,p,1) exp(i theta_p))`,

there is no positive pair `k,l` with `k+l=1`. Hence every third joint cumulant is zero.

The standard Euler-factor logarithm instead contains prime powers. In a finite smoothed prime factor one encounters coefficients proportional to weighted terms of the form

`p^(-k sigma) / k`

with the phase `exp(-i k t log p)` and a cutoff/smoothing weight. Whenever the chosen scale increment retains harmonics `k`, `l`, and `k+l` for the same prime, the shared-phase randomized null has a potentially nonzero third cumulant before any arithmetic confirmation data are examined.

For height-dependent coefficients

`c_(alpha,p,k)=d_(alpha,p,k) exp(-i k t_alpha log p)`

with real `d`, the first resonance term contributes

`d_(alpha,p,k)d_(beta,p,l)d_(gamma,p,k+l)`
` cos((k t_alpha + l t_beta - (k+l)t_gamma) log p)`,

and similarly for the two permutations. Structured height/scale oscillations in a third-order tensor can therefore be forced by the same deterministic prime frequencies and smoothing weights that define the null.

## 4. Sanity check on the smallest resonant example

Take one prime phase and one coordinate with

`A(theta)=cos(theta)+a cos(2 theta)`.

Here `c_1=1`, `c_2=a`, and the only positive additive resonance is `1+1=2`. The formula gives

`E[A^3]=3a/4`.

Direct trigonometric integration gives the same result: all cubic terms average to zero except `3a cos^2(theta)cos(2 theta)`, whose mean is `3a/4`.

This example also shows why treating the randomized field as automatically symmetric or Gaussian is unsafe once multiple harmonics of the same prime are kept.

## 5. Prior art and novelty boundary

Independent Steinhaus variables on the primes are standard random-multiplicative-function machinery. Bondarenko and Seip, **Helson's problem for sums of a random multiplicative function**, *Mathematika* 62:1 (2016), 101–110, DOI `10.1112/S0025579315000236`, explicitly use completely multiplicative random functions generated by independent Steinhaus variables at the primes. Harper's work on moments of Steinhaus random multiplicative functions, including **Moments of random multiplicative functions, II: High moments** (2018, arXiv `1804.04114`), and the random-zeta Euler-product literature likewise make clear that non-Gaussian/high-moment structure of such models is established territory. Saksman and Webb, **Multiplicative chaos measures for a random model of the Riemann zeta function** (2016, arXiv `1604.08378`), provide a nearby random-zeta model in which Gaussian approximation and non-Gaussian multiplicative-chaos structure are central.

The present statement is intentionally narrower. It is the elementary finite product-torus Fourier identity needed to calibrate the exact third-order null of the Mathia hybrid prime-phase experiment. The additive-harmonic formula is derived here directly and carries `NO-NOVELTY-CLAIM`; no claim is made that this is a new theorem in harmonic analysis or random multiplicative functions.

The underlying critical-strip factor remains the hybrid Euler–Hadamard construction of Gonek, Hughes, and Keating, **A hybrid Euler-Hadamard product for the Riemann zeta function**, *Duke Mathematical Journal* 136:3 (2007), 507–549, DOI `10.1215/S0012-7094-07-13634-2`.

## 6. Boundary of the control

The result assumes a finite coefficient family, exactly the regime required for finite visual grids and finite smoothed prime factors. Infinite random Euler products require separate convergence and interchange arguments.

The result also depends on sharing one phase per prime across all powers and all predeclared field coordinates. Resampling phases independently by prime power destroys the `k+l=m` coherence; resampling independently by cell destroys cross-cell third cumulants. Those are different nulls, not implementation details.

The formula does not imply that every third-order statistic is useless. It says that any proposed arithmetic skewness, bispectrum, or third-order scale interaction must first be compared with this exact resonance tensor. A residual beyond the tensor may still be informative if the statistic is frozen in advance and its finite-control uncertainty is calibrated honestly.

Falsify the exact claim by giving a finite coefficient family with independent uniform prime phases for which direct product-torus integration disagrees with the displayed resonance formula.

## Research consequence

The accepted prime-phase recursive-geometry clue is narrowed again. After `VIS-067`, second-order covariance must be measured relative to the exact coefficient Gram kernel. After this finding, a move to third-order structure does not by itself escape that control: the shared prime-phase null already has an exact nonzero third-order tensor whenever prime-power harmonics close under `k+l`.

The next admissible within-prime experiment should therefore precompute both the second-order Gram kernel and, when a third-order witness is contemplated, this additive-harmonic resonance tensor before inspecting arithmetic confirmation data. A genuinely higher-order signal must be a residual beyond the corresponding exact null, not merely a visually striking skewness or bispectral band.