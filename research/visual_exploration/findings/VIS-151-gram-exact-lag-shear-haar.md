# VIS-151 — exact Gram-clock shear forces Haar for every well-sampled supercritical single lag

## Claim

Let `g_k` be the Gram points, with `theta(g_k)=pi k` up to the usual harmless indexing shift, and let

`z_k=(p^(-i g_k))_p in Omega`,

where `Omega` is the infinite prime torus. For an integer lag `ell=ell(N)` with `1<=ell<=N-1`, put

`D_(k,ell)=g_(k+ell)-g_k`,

`Delta_(k,ell)=z_(k+ell) overline(z_k)`,

and let

`M_N=N-ell+1`

be the number of samples in the block `N<=k<=2N-ell`.

If

`ell M_N / (N (log N)^2) -> infinity`,

then the empirical lag-increment measure

`(1/M_N) sum_(k=N)^(2N-ell) delta_(Delta_(k,ell))`

converges weakly to Haar measure on `Omega`.

The same conclusion holds after any common dephasing of the whole lag cloud, in particular after dividing by `Delta_(N,ell)`.

This removes the upper-range restriction in the supercritical Haar part of `VIS-150`. No finite-lag Taylor replacement is needed: the exact inverse-Gram clock has a monotone phase shear large enough for a first-derivative exponential-sum bound whenever the total available shear

`ell M_N / (N (log N)^2)`

diverges.

Consequently, for every fixed `delta>0`, all lags satisfying

`log^2 N << ell <= (1-delta)N`

have Haar single-lag populations for deterministic clock reasons alone. Macroscopic lags `ell~lambda N`, `0<lambda<1`, are included. More generally, lags may approach `N` provided the remaining sample count is large enough to satisfy the displayed shear condition.

**Evidence/status:** `CLASSICAL-GRAM-ASYMPTOTIC + EXACT-DERIVATIVE EXPONENTIAL-SUM CONTROL + NEGATIVE/CONTROL + NO-NOVELTY-CLAIM`.

No stochastic mixing, multi-lag independence, growing-prime-support theorem, selected-subsequence theorem, zeta-value/zero-coordinate independence, or RH consequence is claimed.

## 1. Exact lag phases avoid the finite-lag approximation barrier

Let `g(x)` be the continuous inverse of the eventual increasing branch of the Riemann--Siegel theta function:

`theta(g(x))=pi x`.

Write

`q(x)=g'(x)`.

The standard theta asymptotics used in `VIS-084`, `VIS-090`, `VIS-091`, and `VIS-150` imply, uniformly for `x` in `[N,2N]`,

`q'(x)=g''(x)=-(2 pi)/(x (log x)^2) (1+o(1))`,

and one further differentiation gives

`q''(x)=g'''(x)=(2 pi)/(x^2 (log x)^2) (1+o(1))`.

In particular, for all sufficiently large `N`, `q'<0` and `q''>0` throughout `[N,2N]`.

For real `x` with `N<=x<=2N-ell`, define the exact lag function

`D_ell(x)=g(x+ell)-g(x)`.

Then

`D_ell'(x)=q(x+ell)-q(x)=integral_x^(x+ell) q'(t) dt`.

Because every `t` in that integral lies in `[N,2N]`, the uniform asymptotic for `q'` gives constants `c,C>0`, independent of `ell`, such that

`c ell/(N (log N)^2) <= -D_ell'(x) <= C ell/(N (log N)^2)`

throughout the entire block.

Also

`D_ell''(x)=q'(x+ell)-q'(x)>0`,

because `q'` is eventually increasing. Thus the exact lag phase is monotone with a monotone first derivative. This is the key point: unlike the proof of the supercritical regime in `VIS-150`, no approximation

`D_(k,ell) approx ell g'(k)`

is required, so there is no `ell=o(sqrt(N) log N)` remainder barrier.

## 2. Every nontrivial fixed torus character cancels

Let

`chi_m(omega)=product_p omega(p)^(m_p)`

be a nontrivial torus character with finite integer support, and put

`a_m=sum_p m_p log p`.

Unique factorization gives `a_m!=0`. Along the lag cloud,

`chi_m(Delta_(k,ell))=exp(-i a_m D_ell(k))`.

Set

`f_m(x)=-(a_m/(2 pi))D_ell(x)`,

so that the character sum is `sum exp(2 pi i f_m(k))`. From the preceding derivative bounds,

`|f_m'(x)| asymp_m ell/(N (log N)^2)`

uniformly, and `f_m'` is monotone. Since `ell<=N`, its magnitude is `O_m((log N)^-2)`, hence eventually below `1/2`. Its distance to the nearest integer is therefore just its absolute value.

The standard first-derivative/Kusmin--Landau exponential-sum estimate now gives

`|sum_(k=N)^(2N-ell) chi_m(Delta_(k,ell))|`
` <<_m N (log N)^2 / ell`.

After division by `M_N`,

`|(1/M_N) sum_(k=N)^(2N-ell) chi_m(Delta_(k,ell))|`
` <<_m N (log N)^2 / (ell M_N)`.

The assumed shear condition makes the right-hand side tend to zero. Every nontrivial fixed finite-support character therefore vanishes in the limit, while the trivial character remains one. By the compact-torus Fourier criterion, the empirical measures converge weakly to Haar measure on `Omega`.

Multiplying every sample by one common torus element only multiplies each character average by a unimodular scalar. Hence the same conclusion holds for any globally dephased version of the lag cloud.

## 3. The apparent higher-order lag frontier was partly an approximation artifact

`VIS-150` identified a genuine second clock transition at `ell~log^2 N`: below that scale the dephased lag cloud collapses, at the scale itself it traces a deterministic logarithmic torus curve, and above it Haar appearance begins through deterministic shear. Its proof of the Haar regime used the local replacement `D_(k,ell)=ell g'(k)+o(1)`, which imposed the sufficient restriction `ell=o(sqrt(N) log N)`.

The exact derivative argument shows that this upper restriction is not a new information boundary for the **single-lag empirical population**. Once `ell/log^2 N` is large and enough consecutive starting indices remain, the exact lag function itself supplies monotone phase motion. No third clock expansion is needed merely to prove population-level Haar cancellation.

For a fixed macroscopic fraction `ell~lambda N`, `0<lambda<1`, one has `M_N~(1-lambda)N`, so

`ell M_N/(N log^2 N) asymp N/log^2 N -> infinity`.

Thus even a lag spanning a positive fraction of the whole Gram block has a Haar-looking fixed-prime population for a completely deterministic sampling-clock reason.

Near the endpoint `ell=N-r_N`, the criterion becomes, up to constants,

`r_N/log^2 N -> infinity`.

Failure there can simply reflect sample starvation: only `r_N+1` starting indices remain. The present theorem does not interpret that thin endpoint regime as an arithmetic signal.

## 4. What this does and does not close

This result closes a specific route: taking a **single consecutive Gram lag** farther beyond the `VIS-150` Taylor-valid range does not by itself escape the clock null. For fixed prime support, essentially the whole well-sampled supercritical lag range already has clock-generated Haar population.

It does not classify ordered path geometry beyond the one-lag population. In particular, a joint vector of several lags has character phases of the form

`sum_j a_j D_(k,ell_j)`,

whose derivatives can cancel between components; the one-phase first-derivative argument does not automatically prove joint Haar behavior. Nor is the estimate uniform in characters whose prime support or coefficients grow with `N`.

Likewise, nonconsecutive or selected Gram indices can change the sampling law, and adding `Z(g_k)`, derivatives, zero occupancy, nearby-zero geometry, or another analytic coordinate introduces a source not handled by the deterministic prime-phase lag calculation.

No untouched confirmation-zero data are used.

## 5. Prior-art and novelty audit

The analytic input is the classical Riemann--Siegel theta asymptotic and its differentiated inverse-Gram consequences. The cancellation step is the classical first-derivative/Kusmin--Landau principle for exponential sums, followed by the standard character criterion for Haar convergence on a compact torus.

A targeted literature check found the established Gram-point discrete-universality framework represented by Antanas Laurincikas, *Joint Discrete Approximation of Analytic Functions by Shifts of the Riemann Zeta-Function Twisted by Gram Points* (Mathematics 11 (2023), 565), together with the same Gram-point sources already used to bound `VIS-090`, `VIS-091`, and `VIS-150`. Those works reinforce that Gram sampling and weak distribution laws are classical territory. No basis was found for claiming the present single-lag shear criterion as a new theorem, and **no novelty is claimed**.

The durable contribution here is a research control: it removes an artificial frontier created by the particular Taylor proof used in `VIS-150` and replaces it with an exact, scale-transparent condition on lag times available sample count.

## Visual consequence

No canonical PNG is retained. A finite macroscopic-lag plot would look increasingly equidistributed on every fixed prime projection, but the theorem already explains that appearance as deterministic clock shear. Rendering it would add illustration rather than evidence.

## Research consequence

The accepted `CLUE-zeta-prime-phase-recursive-geometry` should no longer list merely going beyond `ell=o(sqrt(N) log N)` as a consecutive single-lag escape. For fixed prime support, a single-lag population can remain interesting only near the critical `log^2 N` transition after explicit clock quotienting, in a sample-starved endpoint regime with a separately justified statistic, or through structure not reducible to one marginal lag population: joint multi-lag/path dependence, growing support/complexity, nonconsecutive sampling, or an independently informative analytic coordinate.