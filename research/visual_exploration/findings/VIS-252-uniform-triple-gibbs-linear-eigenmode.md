# VIS-252 — uniform triple Gibbs has an exact linear eigenmode with relaxation scale `m-2`

## Claim

Continue the exact three-coordinate random-scan heat-bath kernel of `VIS-249` on a regular symmetric log-product level

`S_lambda={x_i>0 : sum_i x_i=1, sum_i log x_i=lambda}`,

with `m>=3`, and choose unordered coordinate triples uniformly.

For every coordinate `i`, define the centered linear observable

`g_i(x)=x_i-1/m`.

Then the Markov operator `P` of one exact triple Gibbs update satisfies

`P g_i = rho_m g_i`,

with the exact eigenvalue

`rho_m=(m-3)/(m-1)`.

Equivalently, every coordinate contrast `x_i-x_j` is an exact eigenfunction with the same eigenvalue. This identity is independent of `lambda` and of the detailed one-dimensional block-fiber density.

Consequently, on every regular non-singleton level, the reversible chain has a nonconstant mean-zero eigenfunction at `rho_m`, so its `L^2` spectral gap can be no larger than

`1-rho_m=2/(m-1)`.

At stationarity the normalized autocorrelation of any nondegenerate coordinate contrast is exactly

`Corr(f(X_0),f(X_t))=rho_m^t`,

and its standard integrated autocorrelation time is

`1+2 sum_(t>=1) rho_m^t = (1+rho_m)/(1-rho_m)=m-2`.

Thus an exact implementation has a target-independent mandatory linear relaxation benchmark: raw triple-update chains cannot decorrelate all observables on an `o(m)` step scale, and a correctly implemented coordinate contrast must exhibit the explicit `rho_m^t` correlation law.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL RANDOM-SCAN GIBBS SPECIALIZATION + QUANTITATIVE CALIBRATION + NO-NOVELTY-CLAIM`.

This does not prove that `2/(m-1)` is the full spectral gap, that nonlinear occupancy observables mix on the same scale, or that the prime residual is nonzero.

## 1. A selected coordinate is replaced by one third of the block mass in conditional mean

Fix a selected unordered triple `B` containing coordinate `i`. The exact `VIS-249` heat-bath conditional preserves the block sum

`s_B=sum_(k in B) x_k`

and is invariant under permutations of the three selected labels. Therefore the three updated coordinates have equal conditional expectations and their sum is deterministically `s_B`. Hence

`E[X'_i | X=x,B]=s_B/3`.

If `i` is not selected, then `X'_i=x_i`.

This step uses only exact heat-bath resampling, block-sum preservation, and label exchangeability. The discriminant shape of the one-dimensional conditional fiber does not enter.

## 2. Averaging over uniform triples gives the eigenvalue

A uniform unordered triple contains `i` with probability `3/m`.

Conditional on selecting `i`, the other two labels form a uniform two-subset of the remaining `m-1` coordinates. Because `sum_k x_k=1`, their expected total mass is

`2(1-x_i)/(m-1)`.

Therefore

`E[X'_i | X=x, i in B]`
` = (1/3)[x_i+2(1-x_i)/(m-1)]`.

Averaging the selected and unselected cases gives

`P x_i`
` = (1-3/m)x_i + (3/m)(1/3)[x_i+2(1-x_i)/(m-1)]`
` = [(m-3)/(m-1)]x_i + 2/[m(m-1)]`.

Since

`1-rho_m = 2/(m-1)`, 

one also has

`2/[m(m-1)]=(1-rho_m)/m`.

Subtracting the stationary symmetric mean `1/m` yields exactly

`P(x_i-1/m)=rho_m(x_i-1/m)`.

Subtracting the corresponding identities for two coordinates gives

`P(x_i-x_j)=rho_m(x_i-x_j)`.

For `m=3`, `rho_m=0`: the only selected triple is the full coordinate set, so one exact Gibbs step resamples the whole conditioned state and every centered coordinate loses linear memory immediately, as the formula requires.

## 3. Spectral and autocorrelation consequences

`VIS-249` proves reversibility of the exact random-scan heat-bath kernel with respect to `mu_lambda`. On a regular non-singleton symmetric level the coordinate contrasts are not all almost surely zero, so at least one is a nonconstant mean-zero `L^2(mu_lambda)` eigenfunction.

The reversible Markov operator therefore contains the eigenvalue `rho_m` on the mean-zero subspace. Hence the usual `L^2` spectral gap obeys

`gap(P) <= 1-rho_m = 2/(m-1)`.

This is an upper bound on the gap, not an equality. Other geometric modes may have eigenvalues closer to one and produce substantially slower mixing.

For any nonzero contrast eigenfunction `f`, stationarity and reversibility give

`E[f(X_t)|X_0]=rho_m^t f(X_0)`,

so

`Cov(f(X_0),f(X_t))=rho_m^t Var(f)`.

Thus the exact normalized autocorrelation is `rho_m^t`. Summing the geometric series under the standard MCMC convention gives

`tau_int(f)=1+2 sum_(t>=1) rho_m^t=(1+rho_m)/(1-rho_m)=m-2`.

This provides an exact effective-sample-size calibration for the easiest nontrivial observables of the chain before any nonlinear `bar T` statistic is interpreted.

## 4. What this calibrates and what it does not

The result supplies a quantitative benchmark that was missing after `VIS-250` and `VIS-251`. `VIS-250` establishes global accessibility/irreducibility; `VIS-251` shows that a strongly dominant label itself does not acquire a `lambda`-dependent switching penalty. The present calculation identifies a different unavoidable time scale that is present everywhere: uniform triple scanning refreshes each coordinate only through an `O(1/m)` fraction of the global state per step, leaving the standard contrast subspace with eigenvalue `1-2/(m-1)`.

A numerical implementation of the frozen Gibbs kernel should therefore reproduce this law before its nonlinear calibration output is trusted. In particular, empirical coordinate-contrast autocorrelations should agree with `rho_m^t` within Monte Carlo error and their estimated integrated autocorrelation time should approach `m-2` when measured in individual triple updates.

Failure of that benchmark indicates a scan, conditional-sampling, permutation, root-reconstruction, numerical, or bookkeeping defect. Passing it is only a necessary test. It does not certify the slowest mode, the burn-in needed from adversarial starts, or the mixing of the final occupancy statistic.

## 5. Prior art and novelty boundary

Random-scan Gibbs/heat-bath dynamics, conditional-expectation Markov operators, spectral gaps, and autocorrelation diagnostics are classical MCMC. `VIS-249` already anchors Luke Tierney, **Markov Chains for Exploring Posterior Distributions**, *The Annals of Statistics* 22:4 (1994), 1701–1762, DOI `10.1214/aos/1176325750`, as the general Gibbs prior-art boundary. Modern random-scan Gibbs literature also studies convergence and spectral-gap bounds in much greater generality.

A bounded structural literature check did not provide a reason to present the displayed eigenvalue as a new general theorem. No novelty is claimed. The durable Mathia-specific content is the exact specialization to the constrained symmetric log-product Gibbs kernel: exchangeability and the fixed simplex mass collapse one full family of implementation diagnostics to the closed form `rho_m=(m-3)/(m-1)` without needing numerical integration over `mu_lambda`.

## Boundaries and falsification

The exact formula assumes uniform random selection of unordered triples and exact heat-bath resampling from the true symmetric conditional. Fixed nonuniform scan weights generally replace the scalar `rho_m` by a coordinate-dependent linear operator; state-dependent scans require a separate balance and expectation calculation.

The claim concerns individual triple-update steps. Reporting time in sweeps or another unit requires the corresponding deterministic rescaling.

The spectral-gap statement is only `gap(P)<=2/(m-1)`. It must not be promoted to equality without excluding every slower nonlinear mode. Likewise `tau_int=m-2` applies exactly to the linear eigenfunctions above, not to `bar T` or arbitrary observables.

Falsify the claim by showing, under the exact `VIS-249` conditional and uniform triple scan, that a selected coordinate does not have conditional mean `s_B/3`, that the averaging identity for `P x_i` is incorrect, or that a nondegenerate regular level can have every coordinate contrast vanish almost surely.

## Research consequence

The accepted critical-logarithmic-occupancy clue now has an exact first quantitative mixing diagnostic before any prime residual is examined. High-dimensional sampler qualification should first reproduce the target-independent `rho_m^t` coordinate-contrast autocorrelation and the `m-2` integrated-autocorrelation benchmark, then continue with deliberately separated starts and nonlinear observables to detect any slower geometric mode.

If those linear diagnostics fail, the Gibbs implementation is not yet qualified. If they pass while `bar T` or other collective observables remain much slower, that discrepancy becomes direct evidence that the remaining bottleneck lies in genuinely nonlinear conditioned geometry rather than in the trivial uniform-scan refresh rate.