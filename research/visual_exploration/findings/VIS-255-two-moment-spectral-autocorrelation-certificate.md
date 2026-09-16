# VIS-255 — two spectral moments give a sharper autocorrelation certificate

## Claim

Continue the exact fixed-weight heat-bath setting of `VIS-254`. Let `P` be the self-adjoint positive-semidefinite Markov operator, let `g=f-mu f` be a nonzero centered observable, and define

`delta_f = <g,(I-P)g>/<g,g>`

and

`eta_f = <(I-P)g,(I-P)g>/<g,g>`.

Because the spectral measure `nu_f` of `P` is supported on `[0,1]`, if `Z~nu_f` and `S=1-Z`, then

`delta_f = E[S]`, `eta_f = E[S^2]`,

so

`delta_f^2 <= eta_f <= delta_f`.

For `0<delta_f<1` and `eta_f<delta_f`, the integrated autocorrelation time satisfies the sharp two-moment lower bound

`tau_int(f) >= B_2(delta_f,eta_f)`

with

`B_2(delta,eta) = 2(1-delta+delta^2-eta)/(delta-eta) - 1`.

Equivalently, putting `v=eta-delta^2`,

`B_2(delta,eta)`
` = 2/delta - 1`
`   + 2(1-delta)v / [delta(delta(1-delta)-v)]`.

Thus `B_2` is never weaker than the one-moment Jensen bound `2/delta-1` from `VIS-254`, and it is strictly stronger whenever the spectral variable `S=1-Z` has nonzero variance.

The bound is sharp among probability measures on `[0,1]` having the prescribed first two moments. When `eta<delta`, equality is attained by the two-point law

`S in {c,1}`,

where

`c=(delta-eta)/(1-delta)`,

with probabilities

`Pr(S=c)=(1-delta)^2/(1-2delta+eta)`,

`Pr(S=1)=(eta-delta^2)/(1-2delta+eta)`.

At the degenerate boundary `eta=delta^2`, this collapses to `S=delta` and recovers the exact eigenfunction equality of `VIS-254`. If `0<delta<1` and `eta=delta`, then `S` is supported on `{0,1}` with positive mass at `0`, so `tau_int(f)=+infinity`. If `delta=1`, necessarily `eta=1`, `Z=0` almost surely, and `tau_int(f)=1`; if `delta=0`, the observable has an invariant spectral component and `tau_int(f)=+infinity`.

For the uniform triple Gibbs chain of `VIS-249`, the ordinary and logarithmic contrast benchmarks of `VIS-252`--`VIS-253` have

`delta_0=2/(m-1)`, `eta_0=delta_0^2`,

and therefore exactly `B_2=m-2`. For a nonlinear observable such as the cut-averaged tent statistic `bar T`, however, spectral spread can make `B_2(delta_(bar T),eta_(bar T))>m-2` even when the one-moment test `delta_(bar T)<delta_0` does not fire. In particular, if `delta_(bar T)=delta_0` and `eta_(bar T)>delta_0^2`, the nonlinear slowdown relative to both universal linear benchmark families is already certified.

Finally, `eta_f` has an exact block-conditional estimator that does not require fitting a long-lag autocorrelation curve. If `B,C` are independent block choices with the fixed scan weights, independent conditional on `X~mu`, then

`eta_f Var_mu(f)`
` = E[(f(X)-K_B f(X))(f(X)-K_C f(X))]`.

For the current triple chain, every `K_B bar T` is an expectation over the explicit one-dimensional `VIS-248`--`VIS-249` conditional fiber. Hence the second-moment certificate requires only exact inner fiber means plus validated outer target integration; it does not require summing over all triples at each state and does not require long-lag fitting.

**Evidence/status:** `EXACT-DERIVED + SHARP TWO-MOMENT SPECTRAL BOUND + HEAT-BATH CALIBRATION CERTIFICATE + NO-GENERAL-NOVELTY-CLAIM`.

This does not prove the full spectral gap, give an upper bound on nonlinear autocorrelation, validate a numerical sampler, establish a prime residual, or imply RH.

## 1. The second dissipation moment is a spectral moment

Let `nu_f` be the normalized spectral measure of the centered observable `g` under `P`. Since `P` is a positive self-adjoint contraction by `VIS-254`, its spectral variable satisfies `0<=Z<=1`. With `S=1-Z`,

`delta_f = int (1-z) dnu_f(z) = E[S]`.

Also

`eta_f`
` = ||(I-P)g||_2^2/||g||_2^2`
` = int (1-z)^2 dnu_f(z)`
` = E[S^2]`.

The support condition `0<=S<=1` immediately gives

`delta_f^2 <= eta_f <= delta_f`.

Under stationarity one may also write

`eta_f = 1 - 2 r_1(f) + r_2(f)`,

but the block-conditional route below is preferable for the active pre-lag calibration because it uses the exact heat-bath fibers directly.

## 2. A quadratic minorant gives the two-moment bound

For `0<delta<1` and `eta<delta`, put

`c=(delta-eta)/(1-delta)`.

The moment inequalities imply `0<c<=delta<1`. For every `0<s<=1`, the exact identity

`1/s - q_c(s) = (s-c)^2(1-s)/(c^2 s) >= 0`

holds, where

`q_c(s)=1+2/c-(2/c+1/c^2)s+s^2/c^2`.

Therefore, for the spectral variable `S`,

`E[1/S] >= E[q_c(S)]`.

Substituting `E[S]=delta`, `E[S^2]=eta`, and the displayed value of `c` gives

`E[1/S] >= (1-delta+delta^2-eta)/(delta-eta)`.

The heat-bath positivity used in `VIS-254` gives

`tau_int(f)=E[(1+Z)/(1-Z)] = 2E[1/S]-1`,

with value `+infinity` when the integral diverges. This proves

`tau_int(f) >= 2(1-delta+delta^2-eta)/(delta-eta)-1`.

Writing `v=eta-delta^2` and simplifying yields

`B_2(delta,eta)`
` = 2/delta -1`
`   + 2(1-delta)v/[delta(delta(1-delta)-v)]`.

For `eta<delta`, the denominator in the correction is positive. Hence the new correction is nonnegative and is strictly positive exactly when `v>0`.

## 3. The bound is sharp for the admitted moment information

For `delta^2<=eta<delta`, the two-point law stated in the claim has nonnegative probabilities summing to one. A direct calculation gives

`E[S]=delta`, `E[S^2]=eta`.

The quadratic minorant touches `1/s` exactly at `s=c` and `s=1`, so this law attains equality in the bound. Thus no stronger universal lower bound on `tau_int` can be obtained from only support `S in [0,1]` and the two moments `(delta,eta)`.

This sharpness statement concerns the abstract spectral moment problem. A concrete heat-bath operator need not realize every admissible two-point spectral law; additional operator structure can only make a stronger problem-specific bound possible.

If `eta=delta^2`, the moment variance vanishes and `S=delta` almost surely, which is precisely the single-eigenvalue case in which the `VIS-254` Jensen bound is already exact. If `eta=delta` with `0<delta<1`, then `E[S-S^2]=0` forces `S in {0,1}` almost surely; the mean puts positive mass at `S=0`, corresponding to `Z=1`, and the integrated autocorrelation diverges.

## 4. Two independent block residuals estimate `eta` exactly

Let the random block index `B` have the fixed scan law and define

`R_B f = f-K_B f`.

Since `E_B[K_B f | X]=P f(X)`, take two independent block choices `B,C` conditional on the same stationary state `X`. Then

`E[R_B f(X) R_C f(X) | X]`
` = (f(X)-P f(X))^2`.

Averaging over `X~mu` gives

`E[R_B f(X)R_C f(X)] = ||(I-P)f||_2^2`.

Constants are fixed by every `K_B`, so `(I-P)f=(I-P)g`. Dividing by `Var_mu(f)` proves the estimator identity in the claim.

For `bar T` in the exact triple heat-bath chain, each `K_B bar T` is a one-dimensional conditional expectation over the known discriminant fiber. Therefore an outer target sample needs only two independently selected block conditional means per state for an unbiased numerator estimator; it does not need an explicit average over all `binom(m,3)` blocks. The global variance in the denominator and the stationary outer expectation still require an independently validated target integration strategy.

## 5. Consequence for the current nonlinear calibration gate

The current accepted clue uses the exact linear/log benchmark scale

`delta_0=2/(m-1)`, `tau_0=m-2`.

`VIS-254` certifies nonlinear slowdown when `delta_(bar T)<delta_0`. The two-moment certificate strictly contains that test: compute

`B_2(delta_(bar T),eta_(bar T))`.

If

`B_2(delta_(bar T),eta_(bar T)) > m-2`,

then `bar T` is rigorously slower in integrated autocorrelation than both exact additive-coordinate benchmark families, regardless of whether `delta_(bar T)` itself is below `delta_0`.

The certificate remains one-sided. Failure of the inequality does not establish fast mixing because moments beyond `eta`, or a small amount of spectral mass closer to `Z=1`, can still make the actual autocorrelation much larger than the two-moment minimum. Separated-start and long-lag validation therefore remain necessary whenever the operational calibration proceeds.

## 6. Prior art and novelty boundary

The underlying generalized-moment principle is classical. Dimitris Bertsimas and Ioana Popescu, **Optimal Inequalities in Probability Theory: A Convex Optimization Approach**, *SIAM Journal on Optimization* 15:3 (2005), 780--804, DOI `10.1137/S1052623401399903`, develops optimal probability/expectation inequalities from moment information through convex and semidefinite optimization. Steftcho P. Dokov and David P. Morton, **Second-Order Lower Bounds on the Expectation of a Convex Function**, *Mathematics of Operations Research* 30:3 (2005), 662--677, DOI `10.1287/moor.1040.0136`, specifically studies lower bounds for expectations of convex functions from first and second moments with bounded support.

No new general moment-problem theorem is claimed. The explicit reciprocal minorant above is derived directly for the heat-bath spectral variable `S=1-Z`, and no claim is made that this scalar special case is absent from the moment-problem literature. The Mathia-specific contribution is to combine that two-moment bound with `VIS-254`'s positive heat-bath spectrum, the exact `VIS-252`--`VIS-253` eigenmode calibration, and the exact `VIS-248`--`VIS-249` block fibers, yielding a stricter pre-lag nonlinear slowdown certificate and a two-random-block estimator for its second spectral moment.

## Boundaries and falsification

The result inherits the exact fixed-weight heat-bath assumptions of `VIS-254`. A generic reversible chain may have negative spectrum, in which case the support `S in [0,1]` fails and this bound must not be transferred unchanged.

The sharpness claim is only with respect to the abstract support-and-two-moment information. It is not a claim that the active Gibbs operator attains the extremal two-point spectrum.

Numerical estimates of `delta` and `eta` remain target-law quantities. Exact inner block conditionals do not validate a biased or insufficiently mixed outer sample. The two-block numerator estimator can have nontrivial variance and needs its own frozen numerical error budget before it is used as confirmation evidence.

Falsify the mathematical bound by giving an admissible probability law on `S in [0,1]` with the stated first two moments whose `2E[1/S]-1` lies below `B_2`. Falsify the block estimator identity by giving a fixed-weight exact heat-bath family for which two independent scan blocks conditional on `X` do not average to `||(I-P)f||_2^2`.

## Research consequence

The accepted critical-logarithmic-occupancy clue can strengthen its pre-lag calibration without changing the sampler or opening a new long-lag fit. After the exact one-block and linear/log eigenmode implementation checks, estimate both `delta_(bar T)` and `eta_(bar T)` under the frozen target. Use `B_2` as the mandatory lower bound on the `bar T` integrated-autocorrelation budget.

A value above `m-2` is an exact nonlinear slowdown certificate even when the one-moment threshold from `VIS-254` is inconclusive. A value at or below `m-2` remains inconclusive about fast mixing. Actual target integration, long-lag convergence validation, and the prime residual test remain separate computational work.