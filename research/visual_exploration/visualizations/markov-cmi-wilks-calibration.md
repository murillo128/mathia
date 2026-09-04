# Markov-order calibration of the three-gap conditional residual

![Markov-order calibration](markov-cmi-wilks-calibration.png)

## Question

The accepted three-gap clue uses

`I(G_{n-1}; G_{n+1} | G_n) = D(P_3 || Q)`

as the scalar distance from the adjacent-pair-preserving maximum-entropy closure. Before comparing zeta with a finite-size CUE/arithmetic control, what finite-sample scale should be expected from this plug-in quantity even when the binned gap sequence is genuinely first-order Markov?

## Construction and encoding

Fix four symbolic states and the strictly positive first-order transition matrix

`P = [[.55,.20,.15,.10], [.15,.55,.20,.10], [.10,.20,.55,.15], [.20,.10,.15,.55]]`.

For each simulated stationary chain of length `N`, form the overlapping triple counts `n_ijk` from `(X_{t-1},X_t,X_{t+1})`. Let `m=N-2` and calculate the plug-in conditional mutual information in nats,

`I_hat = sum_ijk (n_ijk/m) log[(n_ijk n_j)/(n_ij n_jk)]`.

The plotted likelihood-ratio statistic is `G^2 = 2m I_hat`. For four fully supported states, the first-order-versus-second-order Markov test has

`nu = 4(4-1)^2 = 36`

degrees of freedom.

The left panel compares empirical quantiles of `G^2` from 600 independent simulated chains at `N=500, 2000, 8000` with `chi^2_36`. The right panel compares the Monte Carlo mean of `I_hat` with the first-order asymptotic null bias `nu/(2m)` implied by `E[chi^2_nu]=nu`. The pseudorandom seed is `20260904`.

## Observation

The calibration converges in the expected direction. For `N=500`, the empirical mean `G^2` is about `40.09`, visibly above the asymptotic mean `36`; at `N=2000` it is about `36.94`, and at `N=8000` about `35.55`. The corresponding mean plug-in CMI values are approximately `0.04025`, `0.009244`, and `0.002223` nats, compared with the asymptotic bias values `0.03614`, `0.009009`, and `0.002251`.

This is a calibration picture, not evidence about zeta or CUE. Its purpose is to make the finite-sample floor visible before a positive three-gap CMI is interpreted as structure.

## Robustness and controls

The exact algebraic identity `G^2=2m I_hat` does not depend on the simulation. It is the log-likelihood-ratio between the unrestricted second-order Markov fit `p(k|i,j)` and the first-order fit `p(k|j)` built from the same triple counts.

The chi-square curve is only asymptotic and requires the usual regularity/full-support conditions. Sparse or data-adaptively deleted cells can invalidate the nominal `s(s-1)^2` calibration. Besag and Mondal (2013) explicitly discuss exact conditional Monte Carlo tests for Markov chains when ordinary chi-square asymptotics are unreliable.

Most importantly, a determinantal CUE gap sequence is not asserted to be first-order Markov. Therefore `chi^2_nu` is **not** the arithmetic/RMT null for the accepted zeta experiment. It is a lower-level estimator/model-order calibration. The decisive zeta test must still compare zeta with its matched finite-size CUE/arithmetic process after applying the same binning and residualization to both.

## Research implication

The scalar residual from `VIS-020` has a sharper interpretation: on a fixed finite partition it is exactly a Markov-order likelihood-ratio statistic after multiplication by `2m`. This supplies a principled finite-sample sanity check and makes the leading positive plug-in bias explicit. It also rules out treating a small positive `I_hat` as meaningful merely because zero conditional dependence would give exactly zero at the population level.

The next zeta/CUE visualization should report the matched-process excess, not raw CMI, and should preserve enough information to distinguish a genuine zeta-minus-CUE difference from ordinary Markov-order test bias or sparse-cell failure.
