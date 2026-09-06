# VIS-062 — generic simplex-replicate L1 calibration must pay the support-dimension scale

## Claim

The `sqrt((K-1)/B)` expectation term in the whole-replicate `L^1` control radius of `VIS-061` is unavoidable up to an absolute constant under the generic information model “one independent simplex-valued table per control replicate.”

Fix `K>=2`. Let each replicate be a uniformly random simplex vertex,

`X_b in {e_1,...,e_K}`,

with

`Pr(X_b=e_c)=1/K`,

independently for `b=1,...,B`. Then

`P=E[X_b]=(1/K,...,1/K)`

and `P_hat=(1/B)sum_b X_b` is the ordinary empirical distribution of `B` categorical draws on `K` cells.

If

`B (K-1)/K^2 >= 1`,

then

`E ||P_hat-P||_1 >= (1/2) sqrt((K-1)/B)`.

Together with the refined upper estimate in `VIS-061`,

`E ||P_hat-P||_1 <= sqrt((K-1)/B)`,

this shows that the distribution-free whole-replicate empirical-mean calibration has the correct support-size dependence within a factor of `2` in expectation.

Therefore a materially sharper control certificate cannot, in general, be obtained merely by replacing McDiarmid or tightening the same distribution-free simplex argument while keeping `L^1` raw-law control and no structure inside a replicate. It must use additional information: for example CUE-specific covariance/concentration, a smaller predeclared support, a different stable error geometry with its own propagation theorem, or more independent control replicates.

**Evidence/status:** `EXACT-DERIVED + SHARPNESS/NO-GO CONTROL + CLASSICAL DISTRIBUTION-ESTIMATION PRIOR ART + NO-NOVELTY-CLAIM`.

No new minimax theorem is claimed. The exact finite witness below is elementary; the stronger general statement that discrete-distribution estimation under `L^1` has the same `sqrt(K/B)` difficulty is classical prior art.

## 1. The one-hot subclass is already inside the whole-replicate model

The generic hypothesis of `VIS-061` allows each `X_b` to be any random probability vector on the declared `K`-cell support. In particular it allows the extreme case where a complete replicate returns exactly one simplex vertex.

Write

`N_c = #{b : X_b=e_c}`.

Then every marginal count satisfies

`N_c ~ Bin(B,1/K)`

and

`P_hat(c)=N_c/B`.

The coordinates are dependent through `sum_c N_c=B`, but expectation of the `L^1` norm separates coordinatewise:

`E||P_hat-P||_1`
` = sum_(c=1)^K E |N_c/B-1/K|`
` = (K/B) E|N-B/K|`,

where `N~Bin(B,1/K)`.

Thus the question reduces to one binomial mean absolute deviation.

## 2. A fourth-moment bound gives an explicit finite lower constant

Let

`p=1/K`,
`Z=N-Bp`,
`sigma^2=Bp(1-p)=B(K-1)/K^2`.

For a binomial variable the fourth central moment is

`E Z^4 = 3 sigma^4 + sigma^2 [1-6p(1-p)]`

and hence

`E Z^4 <= 3 sigma^4 + sigma^2`.

Under the stated condition `sigma^2>=1`, this gives

`E Z^4 <= 4 sigma^4`.

Interpolation between `L^1`, `L^2`, and `L^4` gives

`E Z^2 <= (E|Z|)^(2/3) (E|Z|^4)^(1/3)`,

so

`E|Z| >= (E Z^2)^(3/2)/(E Z^4)^(1/2) >= sigma/2`.

Substituting into the coordinate sum yields

`E||P_hat-P||_1`
` >= (K/(2B)) sqrt(B(1/K)(1-1/K))`
` = (1/2) sqrt((K-1)/B)`.

This is already half of the generic upper expectation term in `VIS-061`. No asymptotics, independence between cells, or within-replicate model is used.

## 3. The dimension penalty is not just an empirical-mean proof artifact

The one-hot subclass is the ordinary multinomial distribution-estimation problem. Classical results are stronger than the finite witness above.

Yanjun Han, Jiantao Jiao, and Tsachy Weissman, **Minimax Estimation of Discrete Distributions Under `ell_1` Loss**, *IEEE Transactions on Information Theory* 61:11 (2015), 6343–6354, DOI `10.1109/TIT.2015.2478816`, arXiv `1411.1467`, give tight upper and lower bounds for discrete-distribution estimation in `L^1`. In fixed-support asymptotics they identify the minimax/empirical-distribution constant after `sqrt(B)` scaling as `sqrt(2(K-1)/pi)`, and in the high-dimensional regime they retain the corresponding `sqrt(K/B)` difficulty.

Daniel Berend and Aryeh Kontorovich, **A sharp estimate of the binomial mean absolute deviation with applications**, *Statistics & Probability Letters* 83:4 (2013), 1254–1259, DOI `10.1016/j.spl.2013.01.023`, give sharp non-asymptotic binomial mean-absolute-deviation estimates and apply them to total-variation error of empirical discrete distributions.

These sources mean the scale itself is prior art. The useful Mathia-specific conclusion is narrower: because categorical one-hot controls are a subclass of the broad simplex-valued replicate model admitted by `VIS-061`, **no generic whole-replicate calibration can promise to erase the support-size penalty without adding assumptions that exclude or control this subclass**.

## 4. What can still improve

This no-go result does not say the current CUE application must actually attain the worst-case categorical geometry. A whole CUE matrix produces a highly structured empirical table, not a one-hot vector. Its replicate covariance may live in a much smaller effective subspace, and the nonlinear residual map may discard large raw-law directions.

Accordingly, three improvement routes remain legitimate.

First, exploit actual control structure: prove a concentration/covariance theorem for the complete finite-size CUE table or for the propagated residual itself. Second, predeclare a coarser support or lower-dimensional statistic whose information loss is acceptable and whose generic radius is smaller. Third, retain the existing representation and increase the number of independent control matrices.

What is ruled out is only the hope that the `sqrt(K/B)` behavior is a removable artifact of the coarse `VIS-061` proof while all of its assumptions and target norm remain unchanged.

## 5. Falsification and boundaries

The finite lower bound requires only `K>=2` and `B(K-1)/K^2>=1`. Falsify it by finding such `K,B` for which the uniform one-hot construction violates the displayed expectation inequality, or by identifying an error in the binomial fourth-moment or interpolation step.

The result is an expectation lower bound, not a high-probability lower bound for every confidence level. It does not prove the `sqrt(2 log(1/rho)/B)` tail term in `VIS-061` is optimal, and it does not constrain sharper bounds for restricted replicate families.

It also does not say a finer partition is scientifically wrong. It says a finer generic `L^1` representation carries a real worst-case control cost. Any claim that a fine partition is still practical should therefore exhibit the extra CUE/control structure or replicate budget that pays for it rather than expecting distribution-free concentration alone to do so.

## Research consequence

The accepted zeta three-gap residual experiment now has a clean feasibility boundary. `VIS-061` supplies a safe whole-matrix control radius and `VIS-062` shows that its leading support-dimension scale is generically correct.

If the predeclared three-gap table makes `a_B` too large to test the frozen zeta residual, the next useful mathematical question is **not** “which generic inequality removes `sqrt(K)`?” The admissible choices are to use genuine finite-CUE/internal covariance structure, reduce the declared representation before confirmation, or increase independent control replication. This prevents the visual branch from spending further cycles chasing a distribution-free improvement that the admitted model class itself forbids.