# VIS-036 — empirical CA energy is the Pearson Markov-order statistic with a nonzero null floor

## Claim

Use the fixed `s`-state three-gap setup of `VIS-020` through `VIS-025` and `VIS-035`. For one observed symbolic sequence `x_0,...,x_(N-1)`, let

`n_ijk = #{t : (x_(t-1),x_t,x_(t+1))=(i,j,k)}`,

with `m=N-2`, and write `n_ij=sum_k n_ijk`, `n_jk=sum_i n_ijk`, and `n_j=sum_(i,k) n_ijk`. The fitted first-order Markov expected count in cell `(i,j,k)` is

`e_ijk = n_ij n_jk / n_j`

for positive-count middle states. Let `P_hat=n/m` and let `Q_hat` be the adjacent-pair-preserving closure from `VIS-020`.

Then the Pearson first-order-versus-second-order Markov statistic is exactly

`X_P^2`
` = sum_(i,j,k) (n_ijk-e_ijk)^2/e_ijk`
` = m chi_P^2(P_hat||Q_hat)`.

By the conditional correspondence-analysis decomposition of `VIS-025`/`VIS-035`, this is also exactly

`X_P^2 = sum_j n_j sum_l rho_hat_(j,l)^2`,

where `rho_hat_(j,l)` are the nontrivial singular values/principal-inertia coefficients of the empirical conditional table in middle-state fiber `j`.

Thus the complete count-weighted visual CA spectrum is not merely analogous to a classical goodness-of-fit statistic: **its total squared energy is exactly the Pearson Markov-order statistic**.

For a regular fully supported stationary first-order `s`-state Markov chain,

`X_P^2 => chi^2_nu`,  with  `nu=s(s-1)^2`.

Moreover the same finite-state concentration argument used in `VIS-023` yields uniform integrability, so

`E[X_P^2] -> nu`

and therefore

`E[chi_P^2(P_hat||Q_hat)] = nu/m + o(1/m)`.

Equivalently,

`E[sum_j p_hat_j sum_l rho_hat_(j,l)^2] = s(s-1)^2/m + o(1/m)`.

The empirical Pearson/CA interaction energy therefore has an unavoidable positive `O(1/m)` floor even when the population chain is exactly first-order Markov.

**Evidence/status:** `CLASSICAL-PEARSON MARKOV-ORDER TEST + EXACT-DERIVED CA SPECIALIZATION + FINITE-SAMPLE REPRESENTATION CONTROL + NO-NOVELTY-CLAIM`.

No zeta-specific dependence, CUE calibration, arithmetic signal, asymptotic zero statistic, or RH implication is claimed.

## 1. Exact Pearson identity

The empirical Markov closure is

`Q_hat_ijk`
` = (n_ij/m)(n_jk/m)/(n_j/m)`
` = n_ij n_jk/(m n_j)`.

Hence the fitted expected count is exactly

`m Q_hat_ijk=e_ijk=n_ij n_jk/n_j`.

For every cell with positive fitted expectation,

`m (P_hat_ijk-Q_hat_ijk)^2/Q_hat_ijk`
` = (n_ijk-e_ijk)^2/e_ijk`.

If `e_ijk=0`, then at least one required adjacent count is zero, which forces `n_ijk=0`; such structurally absent empirical cells contribute zero after restricting to the positive fitted support. Summing gives

`boxed: X_P^2 = m chi_P^2(P_hat||Q_hat)`.

This is exact at finite `m`. It does not use a Taylor approximation or asymptotic likelihood theory.

## 2. Exact CA/principal-inertia representation

For middle state `j`, `VIS-035` gives

`chi_P^2(P_hat||Q_hat)`
` = sum_j p_hat_j sum_l rho_hat_(j,l)^2`,

where `p_hat_j=n_j/m`. Multiplying by `m` therefore gives the count-weighted form

`boxed: X_P^2 = sum_j n_j sum_l rho_hat_(j,l)^2`.

This identifies the correct aggregate scale for the empirical visual spectrum. A heatmap or singular-value plot can show where the fitted first-order Markov model fails, but the total count-weighted squared principal-inertia energy is already the classical Pearson order-test statistic.

The identity also makes the sampling issue in `VIS-024` concrete. Even under a true first-order Markov law, fitted residual singular values are not exactly zero in a finite sample because the empirical three-way table fluctuates around its fitted pair-marginal closure.

## 3. Classical chi-square limit

A fully supported first-order `s`-state transition matrix has `s(s-1)` free transition parameters. A second-order model has `s^2(s-1)`, so the dimension difference is

`nu=s^2(s-1)-s(s-1)=s(s-1)^2`.

Anderson and Goodman (1957) derive likelihood-ratio and Pearson chi-square tests for the order of finite-state Markov chains. In the regular fully supported case, the first-order-versus-second-order Pearson statistic above therefore has the classical limit

`X_P^2 => chi^2_(s(s-1)^2)`.

This is the Pearson counterpart of the likelihood-ratio calibration in `VIS-023`. The two statistics are asymptotically equivalent locally but are not identical at finite sample size:

`G^2 = 2m D(P_hat||Q_hat)`,
`X_P^2 = m chi_P^2(P_hat||Q_hat)`.

Thus the accepted three-gap clue has two classical model-order calibrations attached to its two scalar geometries rather than one invented visual score and one statistical score.

## 4. Expectation floor under the first-order null

Weak convergence alone does not justify taking expectations, so use the same finite-state concentration structure as `VIS-023`.

Let `p` be the strictly positive stationary triple law of a regular first-order Markov chain and let `p_hat_m` be the empirical overlapping-triple law. In a sufficiently small neighborhood of `p`, every fitted pair marginal remains bounded away from zero and the Pearson functional

`J(q)=chi_P^2(q||Q(q))`

is smooth. It is nonnegative and vanishes on the first-order Markov manifold, so its first differential vanishes at `p` in tangent directions and, for some local constant `C`,

`J(q) <= C ||q-p||^2`.

Therefore on that neighborhood

`X_P^2=m J(p_hat_m) <= C m ||p_hat_m-p||^2`.

The overlapping-triple process is a finite-state Markov chain, so the same exponential concentration input used in `VIS-023` gives uniformly controlled moments of this local quadratic form.

On the exponentially unlikely complement one only needs a crude polynomial bound. Whenever `e_ijk>0`, integer counts imply

`e_ijk=n_ij n_jk/n_j >= 1/m`,

while `|n_ijk-e_ijk|<=m`; with fixed `s`, this gives `X_P^2=O_s(m^3)`. Exponential concentration therefore kills every fixed polynomial moment contribution from the bad event. Hence `{X_P^2}` is uniformly integrable.

Combining uniform integrability with the classical chi-square weak limit gives

`E[X_P^2] -> nu`.

Using the exact finite-sample identity then yields

`E[chi_P^2] = nu/m + o(1/m)`.

For equal outer alphabets, the bounded scale control from `VIS-035` consequently has first-order-null floor

`E[chi_P^2/(s-1)] = s(s-1)/m + o(1/m)`.

This is only an asymptotic null scale, not a finite-sample bias correction guaranteed to be accurate in sparse tables.

## 5. Prior art and novelty assessment

The statistical test is classical. T. W. Anderson and Leo A. Goodman, **Statistical Inference about Markov Chains**, *Annals of Mathematical Statistics* 28:1 (1957), 89–110, DOI `10.1214/aoms/1177707039`, develops maximum-likelihood inference and both likelihood-ratio and contingency-table-type chi-square tests for hypotheses including lower-order versus higher-order Markov dependence.

J. Besag and D. Mondal, **Exact Goodness-of-Fit Tests for Markov Chains**, *Biometrics* 69:2 (2013), 488–496, DOI `10.1111/biom.12009`, reviews the classical asymptotic tests and emphasizes exact conditional Monte Carlo alternatives when ordinary chi-square calibration is unreliable because of sparse data or nonstandard statistics.

Pascal Lezaud, **Chernoff-type bound for finite Markov chains**, *Annals of Applied Probability* 8:3 (1998), 849–867, DOI `10.1214/aoap/1028903453`, supplies the finite-state exponential-concentration ingredient already used in `VIS-023` and reused here only to justify passage from the Pearson weak limit to the expectation asymptotic.

No novelty is claimed for Pearson chi-square testing, the Markov-order degrees of freedom, the chi-square limit, or finite-state concentration. The Mathia-specific content is the exact identification of the **visual conditional principal-inertia energy** from `VIS-025`/`VIS-035` with that classical Pearson order statistic and the resulting explicit sampling-floor control for the active visualization.

## 6. Boundary conditions and falsification

The chi-square limit and expectation asymptotic require a regular fully supported first-order Markov null with fixed alphabet size. Sparse contexts, structural zeros, boundary transition probabilities, adaptive bin deletion, or an alphabet growing with sample size can change the effective dimension and invalidate the displayed calibration.

The exact identity `X_P^2=m chi_P^2=sum_j n_j sum_l rho_hat_(j,l)^2` remains an algebraic fitted-table identity on the positive empirical support, but this does not make the nominal chi-square law valid for every process.

In particular, the zeta and finite-size CUE gap sequences are not assumed to be first-order Markov. Their true higher-order dependence can produce an `O(1)` population Pearson/CA energy rather than the `O(1/m)` null floor. The chi-square calibration is therefore an **estimator/model-order sanity check**, not the arithmetic baseline for the zeta experiment. The decisive comparison remains zeta versus the matched finite-size CUE/arithmetic process under identical partition, unfolding, support, and window rules.

Nor should individual empirical singular modes be assigned independent chi-square significances. The classical statistic calibrates the complete fitted interaction space; modewise and fiberwise uncertainty still requires process-level resampling or another covariance-aware method.

## Research consequence

`CLUE-zeta-three-gap-conditional-residual` gains a sharper finite-sample control. For every dataset/window and fixed partition, report

`X_P^2 = m chi_P^2 = sum_j n_j sum_l rho_hat_(j,l)^2`

alongside `G^2=2m I_hat`, occupancy diagnostics, and the full weighted spectrum. Under a synthetic or otherwise justified first-order Markov calibration, compare both scalar statistics against the common `nu=s(s-1)^2` asymptotic scale or an exact/process-level Monte Carlo alternative.

For the actual zeta question, do not subtract `nu/m` and call the remainder arithmetic. Apply the identical statistic to the matched finite-size CUE/arithmetic control. The null-floor result exists to prevent a finite-sample CA spectrum from being mistaken for genuine higher-order structure before that matched comparison is made.