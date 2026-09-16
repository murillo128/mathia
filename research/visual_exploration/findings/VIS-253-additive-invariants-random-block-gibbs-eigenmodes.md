# VIS-253 — additive invariants force exact random-block Gibbs eigenmodes

## Claim

Let a permutation-invariant probability law be supported on a level set

`S_A={x : sum_(i=1)^m a(x_i)=A_0}`

for some coordinate function `a`, and let `P_b` be an exact random-scan heat-bath kernel that chooses an unordered block `B` of size `b`, uniformly among all `b`-subsets, then resamples the selected coordinates from their exact conditional law given the complement.

Assume the block conditional is exchangeable in the selected labels. Then, whenever the displayed observables are integrable,

`g_i(x)=a(x_i)-A_0/m`

is an exact eigenfunction of `P_b` with eigenvalue

`rho_(m,b)=(m-b)/(m-1)`.

Equivalently, every contrast

`a(x_i)-a(x_j)`

is an exact eigenfunction with the same eigenvalue.

For any nondegenerate such contrast in `L^2` under a reversible stationary law,

`Corr(f(X_0),f(X_t))=rho_(m,b)^t`

and the standard integrated autocorrelation time is

`tau_int=(1+rho_(m,b))/(1-rho_(m,b))=(2m-b-1)/(b-1)`.

The `VIS-249` triple Gibbs chain is the case `b=3` on

`S_lambda={x_i>0 : sum_i x_i=1, sum_i log x_i=lambda}`.

It therefore has two exact calibration families at the same eigenvalue

`rho_m=(m-3)/(m-1)`:

`P(x_i-1/m)=rho_m(x_i-1/m)`

and

`P(log x_i-lambda/m)=rho_m(log x_i-lambda/m)`.

Thus both ordinary coordinate contrasts `x_i-x_j` and multiplicative-coordinate contrasts `log x_i-log x_j` have exact stationary autocorrelation `rho_m^t` and integrated autocorrelation time `m-2` under the uniform triple scan.

The first family recovers `VIS-252`; the second gives an additional exact benchmark tied directly to the log-product constraint used to define the alpha-free quotient.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL RANDOM-SCAN GIBBS SPECIALIZATION + MULTIPLICATIVE CALIBRATION + NO-NOVELTY-CLAIM`.

This does not prove the full spectral gap, independence of the two diagnostic families, rapid mixing of nonlinear observables such as `bar T`, numerical correctness of an implementation, a prime residual, or any RH consequence.

## 1. Exchangeability fixes the conditional block mean of an additive invariant

Fix the current state `x` and a selected block `B` of size `b` containing coordinate `i`. Because the complement is held fixed and the chain remains on `S_A`, the selected block has deterministic additive mass

`A_B=sum_(k in B) a(x_k)`.

The exact conditional distribution of the selected coordinates is exchangeable by assumption. Therefore all `b` updated values `a(X'_k)`, `k in B`, have the same conditional expectation. Their sum is deterministically `A_B`, so

`E[a(X'_i) | X=x,B]=A_B/b`.

If `i` is not selected, then `a(X'_i)=a(x_i)`.

No density formula for the block conditional is needed. The conclusion uses only exact heat-bath resampling, preservation of the additive level, and exchangeability of selected labels.

## 2. Uniform block averaging gives the universal eigenvalue

A uniformly selected unordered `b`-block contains `i` with probability

`b/m`.

Conditional on containing `i`, the remaining `b-1` labels form a uniform `(b-1)`-subset of the other `m-1` coordinates. Hence

`E[A_B | X=x, i in B]`
` = a(x_i) + [(b-1)/(m-1)] [A_0-a(x_i)]`.

Using the block-mean identity above,

`P_b a(x_i)`
` = (1-b/m)a(x_i)`
`   + (b/m)(1/b) E[A_B | X=x,i in B]`
` = (1-b/m)a(x_i)`
`   + (1/m){a(x_i)+[(b-1)/(m-1)] [A_0-a(x_i)]}`.

Collecting the coefficient of `a(x_i)` gives

`P_b a(x_i)`
` = [(m-b)/(m-1)] a(x_i)`
`   + [(b-1)/(m(m-1))] A_0`.

Since

`1-rho_(m,b)=(b-1)/(m-1)`, 

this is exactly

`P_b a(x_i)=rho_(m,b) a(x_i)+(1-rho_(m,b)) A_0/m`.

Subtracting `A_0/m` proves

`P_b g_i=rho_(m,b) g_i`.

Subtracting the identities for coordinates `i` and `j` proves the contrast statement.

For `b=m`, `rho_(m,b)=0`, as expected for a full-state exact heat-bath refresh. For fixed `b` and large `m`, `1-rho_(m,b)=(b-1)/(m-1)`, making the scan-induced linear relaxation scale explicit.

## 3. Stationary autocorrelation and the exact time scale

For a nonzero mean-zero eigenfunction `f` with eigenvalue `rho_(m,b)` under a stationary reversible chain,

`E[f(X_t)|X_0]=rho_(m,b)^t f(X_0)`.

Therefore

`Cov(f(X_0),f(X_t))=rho_(m,b)^t Var(f)`

and the normalized autocorrelation is exactly `rho_(m,b)^t`.

Because `0<=rho_(m,b)<1` for `2<=b<=m`, the standard integrated autocorrelation time is

`1+2 sum_(t>=1) rho_(m,b)^t`
` = (1+rho_(m,b))/(1-rho_(m,b))`
` = (2m-b-1)/(b-1)`.

This is an exact calibration scale for every additive-coordinate contrast admitted by the lemma. It remains only an eigenmode-specific statement: another nonlinear mode may have an eigenvalue closer to one.

## 4. The log-product quotient supplies a second exact diagnostic family

The `VIS-249` target fixes two symmetric additive coordinate sums simultaneously:

`sum_i x_i=1`

and

`sum_i log x_i=lambda`.

The exact three-coordinate heat-bath conditional preserves the selected block sum and product. Equivalently, it preserves both

`sum_(i in B) x_i`

and

`sum_(i in B) log x_i`.

It is exchangeable under permutations of the three selected labels. The general lemma therefore applies twice with `b=3`.

Choosing `a(u)=u`, `A_0=1`, recovers `VIS-252`:

`P(x_i-1/m)=rho_m(x_i-1/m)`.

Choosing `a(u)=log u`, `A_0=lambda`, gives the new multiplicative-coordinate identity

`P(log x_i-lambda/m)=rho_m(log x_i-lambda/m)`.

Hence every log contrast satisfies

`P(log x_i-log x_j)=rho_m(log x_i-log x_j)`.

On a fixed positive sum/product level the coordinates stay in a compact subset of the positive simplex: if one coordinate approached zero while the sum stayed one, the fixed positive product would be violated. Thus the log-coordinate contrasts are bounded on each regular level and belong to `L^2(mu_lambda)`.

The two benchmark families probe different preserved coordinate descriptions of the same exact block update. The ordinary-coordinate benchmark is sensitive to the simplex-mass refresh algebra; the log-coordinate benchmark is tied directly to the multiplicative constraint whose conditioning removes the Dirichlet nuisance parameter. Passing both is therefore a stronger implementation audit than passing the ordinary-coordinate law alone, although the two diagnostics are not asserted to be statistically independent.

## 5. Prior art and novelty boundary

Random-scan Gibbs and heat-bath kernels, detailed balance, conditional-expectation Markov operators, spectral gaps, and autocorrelation diagnostics are classical. Luke Tierney, **Markov Chains for Exploring Posterior Distributions**, *The Annals of Statistics* 22:4 (1994), 1701–1762, DOI `10.1214/aos/1176325750`, is the general Gibbs/MCMC anchor already used by `VIS-249` and `VIS-252`.

Modern random-scan Gibbs theory studies spectral-gap and convergence bounds far beyond this elementary specialization; for example Qian Qin and Guanyang Wang, **Spectral Telescope: Convergence Rate Bounds for Random-Scan Gibbs Samplers Based on a Hierarchical Structure**, *The Annals of Applied Probability* 34:1B (2024), 1319–1349, DOI `10.1214/23-AAP1992`.

No new general Gibbs theorem is claimed. The durable Mathia-specific point is that the current constrained quotient exposes an exact additive-invariant eigenmode calculation twice: once in ordinary simplex coordinates and once in logarithmic coordinates. The latter supplies a closed-form multiplicative calibration channel without integrating over the complicated conditioned law.

## Boundaries and falsification

The exact scalar eigenvalue requires uniform selection among unordered blocks of a fixed size `b`. Fixed nonuniform scan weights generally produce a different linear operator, while state-dependent scans require their own balance and expectation analysis.

The block conditional must be exchangeable in the selected labels and must preserve the relevant additive quantity exactly. Approximate numerical preservation gives only an approximate diagnostic and must be compared against the implementation's declared tolerance.

The result is about additive-coordinate observables `a(x_i)`. It does not say that every function of the invariant, every nonlinear statistic, or the slowest mode shares the same eigenvalue.

For the log-product specialization, the fixed level must remain in the positive simplex. Degenerate boundary limits require separate care.

Falsify the general claim by producing a qualifying exact uniform-block heat-bath kernel for which the selected-label exchangeability and fixed block additive sum hold but the displayed conditional block mean or uniform-block averaging identity fails. Falsify the log specialization by showing that the `VIS-249` conditional does not preserve the selected log sum or is not exchangeable in its selected labels.

## Research consequence

The accepted critical-logarithmic-occupancy clue now has two exact high-dimensional linear qualification tests before any nonlinear `bar T` calibration is interpreted. A frozen implementation of the `VIS-249` uniform triple kernel should reproduce `rho_m^t` and `m-2` not only for ordinary coordinate contrasts but also for log-coordinate contrasts.

If the ordinary-coordinate benchmark passes while the log-coordinate benchmark fails, the implementation has not faithfully realized the product-conditioned heat-bath geometry. If both pass while `bar T` remains substantially slower from separated admissible starts, the remaining slowdown cannot be blamed on the universal additive-invariant scan mode and becomes evidence for a genuinely nonlinear conditioned-geometric bottleneck.

The next coherent step remains the bounded computational implementation/mixing validation already specified by the accepted clue. That step is intentionally left outside this finding.