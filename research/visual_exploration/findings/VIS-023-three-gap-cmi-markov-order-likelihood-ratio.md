# VIS-023 — binned three-gap CMI is the first-vs-second-order Markov likelihood-ratio statistic

## Claim

Let `x_0,...,x_{N-1}` be a sequence in a fixed finite alphabet of `s` states, and let `n_ijk` be the number of overlapping triples

`(x_{t-1},x_t,x_{t+1}) = (i,j,k)`,  `t=1,...,N-2`.

Write `m=N-2`, `n_ij=sum_k n_ijk`, `n_jk=sum_i n_ijk`, and `n_j=sum_{i,k} n_ijk`. Define the empirical three-way distribution `P_hat(i,j,k)=n_ijk/m` and its adjacent-pair-preserving Markov closure

`Q_hat(i,j,k) = (n_ij/m)(n_jk/m)/(n_j/m)`

on positive-mass middle states.

Then the conditional log-likelihood ratio between the unrestricted second-order Markov model and the first-order Markov model fitted to the same sequence is exactly

`G^2 = 2 sum_ijk n_ijk log[(n_ijk n_j)/(n_ij n_jk)]`
`    = 2m I_hat(X_{t-1}; X_{t+1} | X_t)`
`    = 2m D(P_hat || Q_hat)`.

For a regular fully supported `s`-state first-order Markov chain, the classical asymptotic null distribution is

`G^2 -> chi^2_{s(s-1)^2}`.

Moreover, finite-state Markov concentration makes this family uniformly integrable, so the leading asymptotic positive plug-in CMI floor under that null is

`E[I_hat] = s(s-1)^2/(2m) + o(1/m)` nats.

**Evidence/status:** `CLASSICAL-LIKELIHOOD-RATIO + EXACT-DERIVED SPECIALIZATION`.

This does not make the first-order Markov model a valid model of zeta or CUE gap sequences. It calibrates the finite-partition statistic used by `VIS-020` and the accepted three-gap clue.

## Exact likelihood identity

Condition on the initial states and use the overlapping triple counts as transition statistics.

Under an unrestricted second-order Markov model, the conditional probability of the next state is `p(k|i,j)`. Its maximum-likelihood estimate on every positive-count `(i,j)` context is

`p_hat_2(k|i,j) = n_ijk/n_ij`.

The maximized conditional log likelihood is therefore

`ell_2 = sum_ijk n_ijk log(n_ijk/n_ij)`,

with zero-count cells contributing zero by continuity.

Under the first-order Markov restriction the next-state law depends only on the middle state, `p(k|j)`, and the MLE is

`p_hat_1(k|j) = n_jk/n_j`.

Thus

`ell_1 = sum_ijk n_ijk log(n_jk/n_j)`.

Subtracting gives

`2(ell_2-ell_1) = 2 sum_ijk n_ijk log[(n_ijk n_j)/(n_ij n_jk)]`.

But the right-hand side is exactly `2m` times the plug-in conditional mutual information of the empirical triple table. By `VIS-020`, the same conditional mutual information is `D(P_hat||Q_hat)`. Hence the three descriptions — conditional dependence, KL distance from the pair-marginal maximum-entropy closure, and Markov-order likelihood ratio — are one statistic.

This derivation also explains why the overlapping triples must not be treated as if they were independent contingency-table observations merely by analogy. Their valid likelihood interpretation is the sequence likelihood for nested Markov models.

## Degrees of freedom and asymptotic floor

A fully supported first-order `s`-state transition matrix has `s(s-1)` free transition parameters. A fully supported second-order model has one `s`-category next-state distribution for each ordered pair of previous states, hence `s^2(s-1)` free transition parameters. Their dimension difference is

`s^2(s-1) - s(s-1) = s(s-1)^2`.

Classical Markov-chain likelihood-ratio theory therefore gives an asymptotic `chi^2` law with that many degrees of freedom under a regular first-order null. Besag and Mondal (2013), reviewing the classical Bartlett/Hoel/Anderson/Goodman/Billingsley tests, state this first-order-versus-second-order statistic and the same `s(s-1)^2` asymptotic degrees of freedom explicitly.

The expectation statement requires more than weak convergence. Let `p` be the stationary triple law under a fully supported first-order null and let `p_hat_m` be the empirical triple law. The overlapping-triple process

`Z_t=(X_{t-1},X_t,X_{t+1})`

is itself a finite-state irreducible aperiodic Markov chain. Finite-state Markov Chernoff bounds therefore give exponential concentration of each coordinate of `p_hat_m` around `p`; a canonical source is Pascal Lezaud, **Chernoff-type bound for finite Markov chains**, *Annals of Applied Probability* 8 (1998), 849–867, DOI `10.1214/aoap/1028903453`.

Define on the positive simplex

`F(q)=2 I_q(X_{t-1};X_{t+1}|X_t)`.

At the first-order Markov law `p`, `F(p)=0`. Full support puts `p` in the interior, so `F` is `C^2` on a neighborhood `U` of `p`; since `p` is a minimum of the nonnegative function `F`, its first differential vanishes on the simplex tangent space. Taylor's theorem gives a constant `C` such that

`F(q) <= C ||q-p||^2`

for `q in U`. Hence

`G^2 = m F(p_hat_m) <= C m ||p_hat_m-p||^2`

on `{p_hat_m in U}`. Coordinatewise exponential concentration then gives an exponentially decaying tail for this local quadratic form, and therefore a uniformly bounded `1+delta` moment for some fixed `delta>0`.

The complement is also negligible. Conditional mutual information on an `s`-state alphabet satisfies `I_hat <= log s`, so globally

`0 <= G^2 <= 2m log s`,

while the same finite-state concentration gives `P(p_hat_m notin U) <= a exp(-bm)` for suitable constants. Thus

`E[(G^2)^(1+delta) 1_{p_hat_m notin U}] <= (2m log s)^(1+delta) a exp(-bm) -> 0`.

Consequently `{G^2}` is uniformly integrable. Combining uniform integrability with

`G^2 => chi^2_nu`,  `nu=s(s-1)^2`,

gives

`E[G^2] -> nu`,

and the exact identity `I_hat=G^2/(2m)` yields

`E[I_hat] = nu/(2m) + o(1/m)`.

A positive empirical CMI of this order is therefore expected even when the population conditional mutual information is zero.

## Visual sanity check

The paired artifact

`research/visual_exploration/visualizations/markov-cmi-wilks-calibration.md`

uses a fixed, strictly positive four-state transition matrix and 600 simulated stationary sequences at each of `N=500,2000,8000`. With `nu=36`, the mean simulated `G^2` values are about `40.09`, `36.94`, and `35.55`, converging toward the asymptotic mean `36`. The empirical plug-in CMI means similarly approach `36/[2(N-2)]`.

The simulation is not evidence for the theorem or for zeta. It is retained because it makes the finite-sample bias and the approach to the asymptotic calibration visible, while also showing that `N=500` is still noticeably non-asymptotic for this four-state example.

## Prior art and novelty assessment

The Markov-order likelihood-ratio test is classical. Besag and Mondal, **Exact Goodness-of-Fit Tests for Markov Chains**, *Biometrics* 69:2 (2013), 488–496, DOI `10.1111/biom.12009`, summarize the older asymptotic theory, write the first-order-versus-second-order likelihood-ratio statistic in terms of triple frequencies, and give the `s(s-1)^2` chi-square calibration. Their main contribution is exact conditional testing when the asymptotic approximation is unreliable.

Conditional mutual information as a Markov-order diagnostic is also established literature; for example Papapetrou and Kugiumtzis, **Markov Chain Order estimation with Conditional Mutual Information** (2013), arXiv:`1301.0148`, develop CMI significance tests for symbolic Markov sequences. Lezaud's finite-state concentration theorem supplies a standard route to the uniform-integrability step needed to pass from the Wilks weak limit to the stated leading expectation asymptotic in the fully supported finite-state setting.

No novelty is claimed for the likelihood-ratio test, degrees of freedom, asymptotic chi-square law, or Markov concentration. The Mathia contribution is the **specialization and control boundary** for `VIS-020`: its three-gap residual scalar is not merely an information measure but exactly the classical first-vs-second-order Markov likelihood-ratio statistic for the binned gap sequence.

## Boundary conditions

The displayed likelihood identity is exact for the empirical counts and fixed partition, but the `chi^2` calibration is not exact in finite samples. It assumes a regular model with adequate support. Structural zeros, rare states, sparse contexts, boundary MLEs, or data-adaptive bin deletion change the effective model and can invalidate the nominal degrees of freedom and the uniform-integrability argument as stated.

The leading bias `nu/(2m)` is only asymptotic. It should be treated as a scale diagnostic, not as a finite-sample correction guaranteed to remove all bias. Exact conditional Monte Carlo tests or process-specific resampling are preferable when the table is sparse.

Most importantly, failure of the first-order Markov null is not an arithmetic signal. CUE and other determinantal point processes have genuine higher-order dependence. The accepted zeta experiment therefore still requires a matched finite-size CUE/arithmetic baseline, with identical binning and estimation on both processes. A `G^2` value large relative to `chi^2_nu` only says that a first-order Markov description is inadequate for that binned sequence.

## Research consequence

`CLUE-zeta-three-gap-conditional-residual` remains live but gains a mandatory statistical floor. For every fixed partition/window, report `m`, support/occupancy diagnostics, `I_hat`, and `G^2=2m I_hat`; use the Markov-order chi-square or an exact/Monte-Carlo analogue only as an estimator/model-order calibration. The actual arithmetic question remains the **zeta-minus-matched-CUE/arithmetic residual**, not rejection of first-order Markovity.

This sharply reduces one source of false visual discovery: a positive three-gap CMI that merely reflects plug-in bias, sparse cells, or ordinary higher-order dependence can no longer be promoted as a candidate zeta-specific structure.
