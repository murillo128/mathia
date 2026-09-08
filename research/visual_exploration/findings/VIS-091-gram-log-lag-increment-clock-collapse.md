# VIS-091 — logarithmic-lag Gram prime-phase increments collapse to the deterministic clock orbit

## Claim

Let `g_k` be the Gram points, defined for all sufficiently large `k` by

`theta(g_k)=pi k`,

up to the harmless conventional integer shift in the Gram indexing, and let

`z_k=(p^(-i g_k))_p in Omega`,

where

`Omega = product_(p prime) {z in C : |z|=1}`.

Let `M=M(N)` and `ell=ell(N)` satisfy

`1 <= M <= N-1`,

`0 <= ell <= M`,

and

`ell/log N -> tau`

for some fixed `tau in [0,infinity)`.

For `N <= k <= N+M-ell`, define the ordered lag increment

`Delta_(k,ell)=z_(k+ell) overline(z_k)`

coordinatewise, so

`Delta_(k,ell)(p)=p^(-i(g_(k+ell)-g_k))`.

Then, for every fixed prime `p`,

`max_(N<=k<=N+M-ell) |Delta_(k,ell)(p)-p^(-2 pi i tau)| -> 0`.

More generally, for every fixed finite prime set the whole lag-increment block converges uniformly to the deterministic torus point

`omega_tau=(p^(-2 pi i tau))_p`.

Consequently, if

`I_(N,M,ell) = (1/(M-ell+1)) sum_(k=N)^(N+M-ell) delta_(Delta_(k,ell))`,

then

`I_(N,M,ell) => delta_(omega_tau)`

weakly on `Omega`.

Equivalently, for every fixed nontrivial torus character

`chi_m(omega)=product_p omega(p)^(m_p)`,

with scalar frequency

`a_m=sum_p m_p log p != 0`,

one has the lag correlation limit

`(1/(M-ell+1)) sum_(k=N)^(N+M-ell) chi_m(z_(k+ell)) overline(chi_m(z_k))`
` -> exp(-2 pi i tau a_m)`.

The limiting correlation therefore has modulus one.

The same statement holds jointly for any fixed finite collection of lags `ell_(j,N)` with `ell_(j,N)/log N -> tau_j`: the corresponding increment tuple converges to the deterministic point `(omega_(tau_1),...,omega_(tau_q))`.

If additionally

`M/log N -> infinity`,

then `VIS-090` gives the simultaneous contrast

`(1/(M+1)) sum_(k=N)^(N+M) delta_(z_k) => m_H`

while

`I_(N,M,ell) => delta_(omega_tau)`.

Thus a long consecutive Gram block can be Haar as an unordered prime-phase population while its fixed finite collection of logarithmic-scale lag increments remains asymptotically deterministic. This ordered structure is forced by the Gram clock and is not an independent arithmetic channel.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-GRAM-SPACING COROLLARY + NEGATIVE/CONTROL + NO-NOVELTY-CLAIM`.

No mixing theorem, growing-prime-support result, superlogarithmic-lag classification, prime/zero independence statement, or RH consequence is claimed.

## 1. Logarithmic lags have one uniform deterministic height increment

Let `g(x)` denote the continuous inverse of the eventual monotone branch of the Riemann-Siegel theta function,

`theta(g(x))=pi x`.

The classical theta asymptotics give

`theta'(t) = (1/2) log(t/(2 pi)) + O(t^(-2))`.

They also give the standard Gram asymptotic

`g_n ~ 2 pi n/log n`.

Hence, uniformly for integers `j` with `N <= j <= 2N`,

`theta'(g_j) = (1/2) log N (1+o(1))`.

For every `k` in the lag block, the mean-value theorem gives a point `xi_(k,ell)` between `g_k` and `g_(k+ell)` such that

`pi ell = theta(g_(k+ell))-theta(g_k)`
`       = theta'(xi_(k,ell)) (g_(k+ell)-g_k)`.

Because `k` and `k+ell` both lie in `[N,2N]`, the same uniform logarithmic comparison applies throughout that interval. Therefore

`g_(k+ell)-g_k`
` = [pi ell/theta'(xi_(k,ell))]`
` = [2 pi ell/log N](1+o(1))`
` -> 2 pi tau`

uniformly in `k`.

The key point is that `ell=O(log N)` automatically follows from `ell/log N -> tau<infinity`, so the multiplicative `o(1)` above becomes an additive `o(1)` in the height increment.

## 2. Prime-phase increments collapse coordinatewise and as a measure

For each fixed prime `p`, the elementary chord inequality gives

`|p^(-i(g_(k+ell)-g_k)) - p^(-2 pi i tau)|`
` <= log p |(g_(k+ell)-g_k)-2 pi tau|`.

The right-hand side tends to zero uniformly over the block. Taking the maximum over any fixed finite prime set proves uniform collapse in every fixed finite torus projection.

For a fixed finite-support character `m`,

`chi_m(Delta_(k,ell))`
` = exp(-i a_m (g_(k+ell)-g_k))`
` -> exp(-2 pi i tau a_m)`

uniformly. Hence every character Fourier coefficient of `I_(N,M,ell)` converges to the corresponding coefficient of the point mass `delta_(omega_tau)`.

Characters determine probability measures on the compact abelian group `Omega`, so

`I_(N,M,ell) => delta_(omega_tau)`.

Repeating the same argument componentwise proves the finite-multiple-lag statement.

## 3. Haar population and deterministic path increments are compatible

When `M/log N -> infinity`, `VIS-090` gives weak Haar convergence of the raw empirical state measure on the same consecutive block. The present result shows that this does not imply an independent or mixing path law.

At any lag satisfying `ell/log N -> tau<infinity`, the empirical increment law collapses to a single clock-determined torus point. In character coordinates, the raw mean tends to zero while the lag correlation tends to a unit-modulus phase.

This is not a contradiction. The raw empirical measure forgets ordering, whereas the lag increment retains the deterministic local parametrization of the Gram sequence. A visual cloud can therefore fill the torus in population while the path joining successive or logarithmically separated samples remains highly organized for a completely non-arithmetic reason.

The result extends the local arc control of `VIS-084` across a long sliding block. `VIS-084` describes one `O(log g_n)` neighborhood of a starting Gram point; here the same clock law is uniform over all moving starts `k in [N,N+M]` with `M<=N-1`, so finite-lag delay embeddings and local edge fields remain a deterministic null even inside a population-Haar block.

## Prior art and novelty assessment

The only analytic input is the classical Riemann-Siegel theta/Gram-spacing asymptotic already used in `VIS-084`. The global and short-interval Gram-point prime-phase equidistribution literature used in `VIS-083` and `VIS-090`, including Antanas Laurincikas, *Joint Discrete Approximation of Analytic Functions by Shifts of the Riemann Zeta-Function Twisted by Gram Points* (Mathematics 11 (2023), 565, DOI `10.3390/math11030565`) and its short-interval sequel (Axioms 12 (2023), 426, DOI `10.3390/axioms12050426`), treats the state-population weak-convergence side of the comparison.

A targeted literature check around Gram-point spacing, prime-phase equidistribution, and lag/correlation language did not expose a reason to present the sliding lag-increment formulation as a new theorem. It is an elementary consequence of the standard Gram clock combined with the population control already recorded by Mathia. **No novelty is claimed.** The durable value is the explicit ordered-path null: population Haar behavior does not license interpreting local delay, edge, or finite-lag correlation geometry as new arithmetic structure.

## Boundary and falsification

The theorem fixes `tau<infinity`, hence treats lags of order at most `log N`. It does not classify `ell/log N -> infinity`; genuinely superlogarithmic or nonlocal order statistics require a separate sampling analysis.

The convergence is fixed-coordinate/fixed-character. It is not uniform over primes, character support, lag count, or Fourier complexity growing with `N`. A growing-dimensional delay representation needs its own quantitative theorem.

The result concerns consecutive Gram sampling only. A selected or nonconsecutive subsequence can have a different induced lag law.

No conclusion is made about additional coordinates such as `Z(g_k)`, zeta derivatives, zero occupancy, or nearby-zero geometry. Those may carry information not determined by the prime phases and the Gram clock.

Falsify the derivation by breaking the classical theta derivative/Gram asymptotics or the mean-value identity. A proposed ordered visual separator in this regime must show a residual after quotienting the deterministic clock increment law rather than merely displaying finite-lag coherence.

## Visual consequence

No canonical PNG is retained. The exact limiting increment law is stronger than a finite delay plot. A scatter or path rendering would make the deterministic coherence visually striking but would add no evidence beyond the clock asymptotic and could encourage the very false-positive interpretation this finding rules out.

## Research consequence

The accepted `CLUE-zeta-prime-phase-recursive-geometry` should be narrowed once more. Naive ordered/path-sensitive statistics based on any fixed finite collection of `O(log N)` lags — including local edge fields, fixed-lag autocorrelations, and finite delay embeddings — are controlled by the deterministic Gram clock even when the underlying long-block population is Haar.

A surviving ordered Gram/prime-phase route must therefore use genuinely longer-range order, nonconsecutive sampling, growing complexity with a uniform theorem, an explicitly clock-quotiented residual, or an independently informative analytic coordinate. Merely retaining sample order is not by itself a new information channel.