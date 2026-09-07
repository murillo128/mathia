# VIS-070 — the finite shared-prime-phase null has an exact factorized characteristic law

## Claim

Let `I={1,...,d}` be a finite set of predeclared coordinates and let

`A_alpha(theta) = Re sum_p sum_(k>=1) c_(alpha,p,k) exp(i k theta_p)`,

where only finitely many primes and harmonics have nonzero coefficients, and the prime phases `theta_p` are independent uniform variables on `[0,2 pi)`, shared across all powers and all coordinates for the same prime.

For `t=(t_alpha) in R^d`, define the prime-local combined harmonic coefficient

`C_(p,k)(t) = sum_alpha t_alpha c_(alpha,p,k)`.

Then the joint characteristic function of `A=(A_alpha)_alpha` is exactly

`Phi_A(t) = E exp(i sum_alpha t_alpha A_alpha)`
`         = prod_p Psi_p(t)`,

with

`Psi_p(t) = (1/(2 pi)) integral_0^(2 pi)`
`  exp(i Re sum_(k>=1) C_(p,k)(t) exp(i k theta)) dtheta`.

Thus the **entire finite-dimensional law** of the shared-prime-phase null is determined exactly by the deterministic prime-power coefficient arrays. The covariance kernel of `VIS-067` and the connected cumulants of `VIS-068`--`VIS-069` are derivatives of this same characteristic law at the origin; they are not separate null models.

If only the first harmonic is retained for each prime, then

`Psi_p(t) = J_0(|C_(p,1)(t)|)`

and therefore

`Phi_A(t) = prod_p J_0(|C_(p,1)(t)|)`,

where `J_0` is the Bessel function of the first kind.

More generally, write for each nonzero harmonic

`C_(p,k)(t) = r_(p,k)(t) exp(i phi_(p,k)(t))`.

Jacobi--Anger expansion gives the exact constant-term formula

`Psi_p(t)`
` = sum_((n_k) in Z^K; sum_k k n_k=0)`
`     prod_k [i^(n_k) J_(n_k)(r_(p,k)(t)) exp(i n_k phi_(p,k)(t))]`,

where `K` contains the finitely many active harmonics for prime `p`. The constraint `sum_k k n_k=0` is the same prime-local resonance condition that generated the moment and cumulant tensors in `VIS-068`--`VIS-069`, now before taking any finite-order derivative.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL CHARACTERISTIC-FUNCTION/HAAR/JACOBI-ANGER SPECIALIZATION + NEGATIVE/CONTROL + NO-NOVELTY-CLAIM`.

No new theorem about random multiplicative functions, random Euler products, zeta value distributions, hybrid Euler--Hadamard products, or RH is claimed.

## 1. Prime independence factorizes the characteristic function

Set

`A_(alpha,p)(theta_p) = Re sum_k c_(alpha,p,k) exp(i k theta_p)`

so that `A_alpha=sum_p A_(alpha,p)`.

For fixed `t`,

`sum_alpha t_alpha A_alpha`
` = sum_p Re sum_k [sum_alpha t_alpha c_(alpha,p,k)] exp(i k theta_p)`
` = sum_p Re sum_k C_(p,k)(t) exp(i k theta_p)`.

Hence

`exp(i t dot A)`
` = prod_p exp(i Re sum_k C_(p,k)(t) exp(i k theta_p))`.

The factors depend on independent prime phases, so expectation factors prime by prime and gives the displayed product of one-circle Haar integrals. No approximation or asymptotic passage is involved.

Because characteristic functions uniquely determine probability laws on `R^d`, this product determines the complete joint distribution of every predeclared finite coordinate field under the shared-phase null.

## 2. First harmonics give an ordinary Bessel product

Suppose only `k=1` is active at prime `p`. Write

`C_(p,1)(t)=r exp(i phi)`.

Then

`Psi_p(t) = (1/(2 pi)) integral_0^(2 pi)`
`  exp(i r cos(theta+phi)) dtheta`.

A shift of the integration variable removes `phi`, and the standard integral/Jacobi--Anger representation gives

`Psi_p(t)=J_0(r)`.

Therefore the first-harmonic shared-prime-phase field has the exact multivariate characteristic function

`Phi_A(t)=prod_p J_0(|sum_alpha t_alpha c_(alpha,p,1)|)`.

For one scalar coefficient `c`, this reduces to the familiar arcsine/cosine law `A=|c| cos(theta+phi)` with characteristic function `J_0(|c|t)`. Expanding at the origin recovers `Var(A)=|c|^2/2` and `kappa_4(A)=-3|c|^4/8`, matching the sanity check in `VIS-069`.

## 3. Prime-power harmonics give a resonant Bessel constant term

For finitely many active harmonics, Jacobi--Anger gives

`exp(i r_k cos(k theta+phi_k))`
` = sum_(n in Z) i^n J_n(r_k) exp(i n(k theta+phi_k))`.

Multiplying the finitely many harmonic expansions and integrating over `theta` keeps exactly the zero Fourier mode. The surviving integer tuples satisfy

`sum_k k n_k=0`,

which yields the displayed constant-term formula for `Psi_p(t)`.

This is the full-law analogue of the resonance bookkeeping in `VIS-068`--`VIS-069`. Finite moments arise by differentiating `Phi_A`; connected cumulants arise by differentiating `log Phi_A` near `t=0`, where `Phi_A(0)=1` guarantees a nonzero neighborhood. The same zero-frequency arithmetic is therefore visible either in the Bessel constant term or after expansion into moments/cumulants.

## 4. What this closes for visual control design

A finite non-cumulant statistic does not escape calibration merely because `VIS-069` only wrote finite cumulants. For any deterministic statistic

`T = F(A_1,...,A_d)`

on a frozen finite coordinate field, the null law of `T` is the pushforward of the exact torus law above. It may lack a convenient closed-form density, but it is neither unspecified nor featureless. One may evaluate it by the exact characteristic function when tractable, by deterministic torus quadrature/Fourier methods, or by direct independent prime-phase sampling from the same fully specified law.

This includes nonlinear norms, extrema over a predeclared finite grid, threshold counts, cluster summaries, persistence summaries, and other finite deterministic post-processings. Such a statistic can still separate the arithmetic field from the randomized control, but the signal is the **difference from this realizable null law**, not the mere existence of nonlinear or topological structure.

The result does not remove statistical uncertainty from finite control samples. `VIS-060`--`VIS-063` still govern the distinction between a frozen finite-table comparison, a fixed witness, and a population-level statement. Exact specification of the null and finite-sample uncertainty are different questions.

## 5. Prior art and novelty boundary

Primewise independent Steinhaus phases are standard in probabilistic number theory and random multiplicative-function models. The random-multiplicative literature already cited in `VIS-068`--`VIS-069` is the relevant arithmetic prior-art boundary; this finding does not claim a new random Euler-product distribution theorem.

The analytic ingredients are classical. NIST Digital Library of Mathematical Functions, **§10.12 Generating Function and Associated Series**, records the Bessel generating function and Jacobi--Anger expansions used to extract the zero Fourier coefficient. The factorization of characteristic functions for independent random vectors and uniqueness of characteristic functions are standard probability theory.

The present result is only the finite product-torus specialization needed to make Mathia's chosen shared-prime-phase control explicit at the level of the complete finite-dimensional law. It therefore carries `NO-NOVELTY-CLAIM`.

## 6. Boundary of the control

The claim assumes finitely many nonzero prime/harmonic coefficients and finitely many predeclared coordinates. Infinite random Euler products, continuum-indexed fields, and limits in which the number of coordinates or primes grows require separate convergence, tightness, and interchange arguments.

It also assumes one phase per prime shared across prime powers and across all coordinates. Resampling by prime power, by height, or by scale produces a different factorization and a different null law. The exact phase-sharing convention must therefore be frozen before confirmation.

The theorem specifies the chosen randomized null; it does **not** prove that this null is the right arithmetic comparator, that the arithmetic zeta-derived field follows it, or that a discrepancy from it has an RH consequence. Nor does an exact characteristic function make every derived statistic computationally cheap.

Falsify the claim by giving a finite coefficient family and `t in R^d` for which direct product-torus integration of `exp(i t dot A)` disagrees with the displayed prime-factorized Haar integral or, in the first-harmonic case, with the Bessel product.

## Research consequence

The accepted prime-phase recursive-geometry clue is narrowed again. `VIS-067`--`VIS-069` made the second-, third-, and arbitrary finite-cumulant null geometry explicit. The present finding shows that **the full finite-dimensional shared-prime-phase law is already exact before choosing a statistic**.

The next admissible within-factor experiment should therefore freeze an actual arithmetic statistic and compare it with the pushforward of this exact null on the same frozen coordinate field, with uncertainty calibrated at the claim strength intended. Moving from cumulants to an arbitrary nonlinear or topological summary is not by itself a new information channel or an escape from null calibration.