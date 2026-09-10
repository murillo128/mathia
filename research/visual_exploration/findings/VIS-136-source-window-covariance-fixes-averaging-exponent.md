# VIS-136 — source-window covariance fixes the averaging exponent for a `1/L` residual

## Claim

Let `(Y_j)_(j in Z)` be a centered second-order stationary sequence representing one frozen scalar support-edge contrast evaluated on successive admissible source windows under a matched null, with autocovariance

`gamma(h) = E[Y_0 Y_h]`.

For

`bar Y_m = (1/m) sum_(j=1)^m Y_j`,

the variance is exactly

`Var(bar Y_m) = (1/m) [ gamma(0) + 2 sum_(h=1)^(m-1) (1-h/m) gamma(h) ].`

This elementary identity turns the effective-window question left by `VIS-135` into a covariance-tail problem. In particular, for a putative arithmetic mean displacement of size `a/L` with fixed `a != 0`:

1. if `sum_(h>=1) |gamma(h)| < infinity` and the long-run variance

   `tau = gamma(0) + 2 sum_(h>=1) gamma(h)`

   is strictly positive, then `Var(bar Y_m) ~ tau/m`; fixed signal-to-noise requires `m = Theta(L^2)`, while stochastic error `o(1/L)` requires `m/L^2 -> infinity`;
2. if `gamma(h) ~ c h^(-beta)` with `c>0` and `0<beta<1`, then

   `Var(bar Y_m) ~ [2c / ((1-beta)(2-beta))] m^(-beta)`,

   so fixed signal-to-noise against `a/L` requires `m = Theta(L^(2/beta))`, strictly worse than quadratic averaging;
3. if `gamma(h) -> c_0 > 0`, then `Var(bar Y_m) -> c_0`, so averaging cannot expose a vanishing `1/L` mean at all;
4. beating the ordinary `1/m` short-memory variance rate requires a genuinely degenerate low-frequency covariance structure, such as `tau=0`, and therefore cannot be credited to generic correlation without proving the required cancellation.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL STATIONARY-COVARIANCE/LONG-MEMORY CONTROL + NEGATIVE FEASIBILITY CONTROL + NO-NOVELTY-CLAIM`.

The result does not determine the actual covariance law of separated Riemann-zero source windows and does not establish a zeta-to-CUE transfer estimate. It only identifies the exact averaging regimes that such a covariance calculation must distinguish.

## 1. Exact finite-`m` identity

Stationarity gives

`Var(sum_(j=1)^m Y_j) = sum_(j,k=1)^m gamma(j-k)`.

For lag `h>=1`, exactly `m-h` ordered pairs have difference `h`, and the same number have difference `-h`. Hence

`Var(sum_(j=1)^m Y_j)`
` = m gamma(0) + 2 sum_(h=1)^(m-1) (m-h) gamma(h)`.

Dividing by `m^2` gives the displayed formula. No independence, Gaussianity, mixing assumption, or random-matrix input is used.

When `gamma(0)>0`, an exact covariance-based effective sample size may therefore be defined by

`m_eff(m) = m gamma(0) / [gamma(0) + 2 sum_(h=1)^(m-1) (1-h/m) gamma(h)]`,

whenever the denominator is positive. This is bookkeeping, not an assumption that the correlated windows can be replaced by independent ones.

## 2. Summable covariance gives the quadratic window law

Assume `sum_(h>=1)|gamma(h)|<infinity` and put

`tau = gamma(0)+2 sum_(h>=1) gamma(h)`.

Subtracting `tau/m` from the exact variance gives

`Var(bar Y_m) - tau/m`
` = -(2/m) sum_(h>=m) gamma(h)`
`   -(2/m^2) sum_(h=1)^(m-1) h gamma(h)`.

The first term is `o(1/m)` by absolute summability. For the second,

`(1/m) sum_(h<m) h |gamma(h)| -> 0`

by dominated convergence applied to `(h/m) |gamma(h)|`, so it is also `o(1/m)`. Thus

`Var(bar Y_m) = tau/m + o(1/m)`.

For a mean signal `a/L`, the squared signal-to-noise ratio is asymptotically

`SNR^2 ~ (a^2/tau) m/L^2`.

Therefore `m=o(L^2)` loses the signal, `m=Theta(L^2)` gives only order-one signal-to-noise, and `m/L^2 -> infinity` is needed for averaging noise to become `o(1/L)`.

The independence calculation in the accepted support-edge clue is exactly the special case `gamma(h)=0` for `h!=0`, with `tau=gamma(0)`.

## 3. Power-law long memory changes the exponent

Suppose instead

`gamma(h) ~ c h^(-beta)`, `c>0`, `0<beta<1`.

The diagonal contribution `gamma(0)/m` is lower order because `m^-1=o(m^-beta)`. The weighted covariance sum obeys

`sum_(h=1)^(m-1) (1-h/m) h^(-beta)`
` ~ m^(1-beta) integral_0^1 (1-x) x^(-beta) dx`
` = m^(1-beta) / ((1-beta)(2-beta)).`

Hence

`Var(bar Y_m)`
` ~ [2c / ((1-beta)(2-beta))] m^(-beta)`.

The standard deviation is therefore of order `m^(-beta/2)`. Matching it to a `1/L` signal requires

`m = Theta(L^(2/beta))`.

This makes precise why slowly decaying positive source-window dependence can make the support-edge test much more expensive than the independent-window estimate.

## 4. Persistent common mode and the only escape from `1/m`

If `gamma(h)->c_0>0`, then

`(2/m) sum_(h=1)^(m-1) (1-h/m) gamma(h) -> c_0`,

because the triangular weights have asymptotic total mass `m/2`. Thus `Var(bar Y_m)->c_0`: an order-one common component survives arbitrary averaging.

At the opposite extreme, short-memory covariance can beat the `tau/m` law only if the long-run variance is degenerate, `tau=0`. For a stationary process with an ordinary spectral density this is the statement that the spectral density vanishes at zero frequency. The exact rate then depends on the order and regularity of that zero; it is not supplied by stationarity alone.

This matters for the support-edge program because negative cross-window covariance is not automatically helpful. An improvement over quadratic window count must come with an independently justified low-frequency cancellation mechanism. Otherwise the defensible null is `tau>0` or a slower long-memory regime, not an assumed anti-correlation gain.

## 5. Consequence for the frozen Montgomery support-edge thread

`VIS-133`--`VIS-135` establish an order-one single-window finite-CUE covariance floor for the frozen bounded-tent terminal packet and its smoothed intensity contrasts. They do not determine dependence between distinct zeta height/source windows.

The next source-window calculation should therefore target the covariance sequence, or equivalently its low-frequency mass, for the exact predeclared window-spacing and unfolding convention. The relevant feasibility alternatives are now explicit:

- summable covariance with `tau>0`: the original `Theta(L^2)` effective-window law survives up to the long-run-variance constant;
- positive power-law covariance: the required window count increases to `Theta(L^(2/beta))`;
- a persistent common mode: averaging fails to resolve `1/L`;
- a proved zero of the long-run variance: faster averaging may be possible, but the cancellation itself becomes a new theorem-level obligation.

This reduction should be completed before untouched confirmation zeros are inspected. It also separates the covariance problem from the other unresolved gate: finite-height zeta-to-finite-CUE transfer and nuisance propagation must independently be controlled at `o(1/L)` for a `1/L` arithmetic residual to be interpretable.

## 6. Prior-art audit

The finite-sample variance identity is standard stationary-process algebra and no novelty is claimed for it. The distinction between absolutely summable short memory and power-law long-range dependence, including non-`1/m` sample-mean variance scaling, is classical. Useful anchors are:

- Jan Beran, **Long-range dependence**, *WIREs Computational Statistics* 2 (2010), 26–35, DOI `10.1002/wics.52`;
- Jonathan R. M. Hosking, **Asymptotic distributions of the sample mean, autocovariances, and autocorrelations of long-memory time series**, *Journal of Econometrics* 73:1 (1996), 261–284, DOI `10.1016/0304-4076(95)01740-2`.

The Mathia-specific contribution of this finding is only the application of those standard covariance regimes as an exact feasibility control for the already frozen `1/L` Montgomery support-edge residual program.

## Boundaries

This finding does **not** show that Riemann-zero source windows are stationary, short-memory, long-memory, independent, or CUE-distributed across windows. It does not select a legal window spacing, prove an effective-size map, derive the arithmetic residual amplitude, or bound finite-height transfer errors. Those remain separate obligations.

No confirmation-zero dataset is inspected here.