# VIS-115 — centered cyclic third-order lag planes have a forced marginal-skewness DC mode

## Claim

Let `N>=3` and let `x_0,...,x_(N-1)` be real numbers with exact sample centering

`sum_i x_i = 0`.

For ordered cyclic lags `a,b in {1,...,N-1}` with `a!=b`, define

`T(a,b) = (1/N) sum_(i=0)^(N-1) x_i x_(i+a) x_(i+b)`,

where all indices are read modulo `N`. Put

`m_3 = (1/N) sum_i x_i^3`.

Then the complete off-diagonal cyclic lag plane obeys the exact identity

`sum_(a!=0) sum_(b!=0,b!=a) T(a,b) = 2 m_3`.

Hence its lag-plane mean is

`T_bar = 2 m_3 / ((N-1)(N-2))`.

Now let `pi` be a uniformly random permutation of the fixed values `x_0,...,x_(N-1)` and form `T_pi(a,b)` from the permuted cyclic sequence. For every admissible lag pair,

`E_pi[T_pi(a,b)] = T_bar`.

Therefore the residual lag plane

`R(a,b) = T(a,b) - 2 m_3 / ((N-1)(N-2))`

has two exact properties:

1. `sum_(a!=0) sum_(b!=0,b!=a) R(a,b)=0` for every centered cyclic sequence;
2. `E_pi[R_pi(a,b)]=0` at every admissible lag pair under the fixed-multiset random-permutation null.

Thus sample mean centering alone does **not** zero a finite cyclic third-order lag map. A nonzero marginal third moment forces a uniform DC component even when chronology is randomized away while the empirical value multiset is preserved.

**Evidence/status:** `EXACT-DERIVED + FINITE-POPULATION/PERMUTATION CONTROL + HIGHER-ORDER-STATISTICS BASELINE + NEGATIVE VISUAL CONTROL + NO-NOVELTY-CLAIM`.

No variance formula for the permutation null, finite-size CUE law, zeta/CUE difference, asymptotic normality, or RH implication is established.

## 1. Exact lag-plane sum

Fix `i`. As `a` and `b` range over distinct nonzero residues modulo `N`, the ordered pair `(i+a,i+b)` ranges over all ordered pairs of distinct indices different from `i`. Therefore

`sum_(a!=0) sum_(b!=0,b!=a) x_(i+a) x_(i+b)`

is the ordered distinct-pair sum over the `N-1` values other than `x_i`. Writing

`S_2 = sum_j x_j^2`,

we obtain

`sum_(a!=0) sum_(b!=0,b!=a) x_(i+a) x_(i+b)`
` = (sum_(j!=i) x_j)^2 - sum_(j!=i) x_j^2`.

Exact centering gives `sum_(j!=i)x_j=-x_i`, while

`sum_(j!=i)x_j^2=S_2-x_i^2`.

Hence the inner sum is

`x_i^2-(S_2-x_i^2)=2x_i^2-S_2`.

Multiplying by `x_i`, summing over `i`, and using `sum_i x_i=0` gives

`sum_i x_i(2x_i^2-S_2)`
` = 2 sum_i x_i^3 - S_2 sum_i x_i`
` = 2 sum_i x_i^3`.

The definition of `T(a,b)` contributes the factor `1/N`, so

`sum_(a!=0) sum_(b!=0,b!=a) T(a,b)`
` = (2/N) sum_i x_i^3`
` = 2m_3`.

There are exactly `(N-1)(N-2)` ordered admissible lag pairs, which yields the displayed `T_bar`.

## 2. Random permutation has the same forced mean at every lag

For any fixed admissible `(a,b)` and any `i`, the three cyclic positions

`i`, `i+a`, `i+b`

are distinct. Under a uniform random permutation, the values occupying those positions are an ordered sample of three distinct members of the fixed population without replacement.

The ordered distinct-triple sum of the centered population is

`sum_(p,q,r all distinct) x_p x_q x_r`.

Expanding `(sum_i x_i)^3` and using `sum_i x_i=0` gives the standard finite-population identity

`sum_(p,q,r all distinct) x_p x_q x_r = 2 sum_i x_i^3`.

Consequently

`E_pi[x_(pi(i)) x_(pi(i+a)) x_(pi(i+b))]`
` = 2 sum_j x_j^3 / (N(N-1)(N-2))`
` = 2m_3 / ((N-1)(N-2))`.

Averaging over `i` leaves the same value, proving

`E_pi[T_pi(a,b)] = T_bar`.

This matches the deterministic lag-plane mean from Section 1 exactly. The random-permutation null therefore makes the **residual** `R(a,b)`, not the raw centered statistic `T(a,b)`, the natural zero-mean chronology diagnostic.

## 3. Why this matters for cyclic gap geometry

For a complete cyclic spectrum with positive gaps `g_i`, normalize by the sample mean and write for example

`x_i = g_i / g_bar - 1`.

Then `sum_i x_i=0` exactly. The empirical gap distribution can nevertheless have nonzero third central moment `m_3`. The raw cyclic third-order lag plane therefore contains a uniform component determined entirely by one-point marginal skewness.

That component is not evidence of ordering, phase coupling, long memory, or arithmetic structure. It survives because fixing the complete value multiset and sampling without replacement introduces a finite-population dependence absent from the population-centered independent model of `VIS-114`.

This distinction is easy to miss visually. A heatmap of `T(a,b)` may appear globally shifted even under chronology-destroying permutations. For a fixed-multiset chronology test, the first exact subtraction is instead

`R(a,b)=T(a,b)-T_bar`.

Only structure inside the residual plane can distinguish the observed ordering from the mean of the complete random-shuffle ensemble.

The correction is pointwise small when `m_3=O(1)` and `N` is large, since `T_bar=O(N^-2)`. But it accumulates coherently across the `Theta(N^2)` lag plane: the raw plane sum is exactly `2m_3`. It therefore cannot be ignored automatically when the proposed statistic pools many lag pairs or uses a global visual offset, integrated energy around a nonzero baseline, or another aggregate sensitive to the DC mode.

## 4. Relation to the current higher-order branch

`VIS-110` shows that uniformly bounded lags remain finite-block information. `VIS-111` and `VIS-113` show that growing/macroscopic lags can escape every fixed block quotient and can retain constant synthetic amplitude even after complete two-point homometry. `VIS-114` then gives the exact `M^(-1/2)` scale for a population-centered independent third-order lag average.

The present result supplies a different finite-size control needed before transferring that statistic to a complete cyclic gap sequence. Under an exact fixed-sum/fixed-multiset shuffle, the coordinates are not independent, and the raw third-order coefficient is not mean-zero unless the empirical third central moment itself vanishes.

These two nulls answer different questions:

- the independent centered null supplies an elementary fluctuation-scale sanity check;
- the fixed-multiset permutation null removes chronology while preserving the exact one-point empirical distribution and therefore exposes the marginal-skewness DC term.

Neither null substitutes for a finite-size CUE or other source-faithful non-arithmetic control. In particular, random permutation destroys two-point spacing dependence and level-repulsion chronology that a CUE comparison should preserve statistically.

## 5. Prior art and novelty assessment

Third-order correlations, cumulants, and bispectra are classical higher-order-statistics objects; `VIS-109` and `VIS-114` already record standard references including Brillinger, Nikias--Raghuveer, and Mendel. Randomized surrogate testing is likewise classical: James Theiler, Stephen Eubank, André Longtin, Bryan Galdrikian, and J. Doyne Farmer, **Testing for nonlinearity in time series: the method of surrogate data**, *Physica D* 58 (1992), 77--94, DOI `10.1016/0167-2789(92)90102-S`, provides the standard null/surrogate framework in which preserved statistics must be separated from the discriminating temporal statistic.

Finite-population moment identities under sampling without replacement are also classical. Christopher S. Withers and Saralees Nadarajah, **Unbiased Estimates for Products of Moments and Cumulants for Finite Populations**, *Mathematics* 11:17 (2023), 3720, DOI `10.3390/math11173720`, treats products of moments and cumulants for finite populations and sampling without replacement. The visual line already uses finite-population permutation-process prior art in `VIS-026`.

The formulas here are elementary exact specializations to the cyclic third-order lag plane used by the current branch. **No new theorem in finite-population sampling, surrogate-data analysis, or higher-order time-series statistics is claimed.** Their value here is the exact control they impose on any future zeta/CUE lag-plane visualization.

## Boundary and falsification

The exact identities require:

- a complete cyclic sequence of `N` positions;
- exact sample centering `sum_i x_i=0`;
- distinct nonzero cyclic lags;
- for the permutation expectation, a uniform random permutation of the fixed values.

They do not apply unchanged to the noncyclic admissible-start statistic of `VIS-114`, to a statistic using repeated lag positions, to local/window-specific re-centering, or to a surrogate that preserves additional temporal constraints. Those designs need their own finite-sample mean calculation.

The claim would be falsified by a centered finite sequence for which the complete off-diagonal lag-plane sum differs from `2m_3`, or by a fixed-multiset uniform permutation whose expected coefficient at one admissible lag differs from `2m_3/((N-1)(N-2))`. The finite algebra above rules out both possibilities.

## Visual consequence

No canonical PNG is retained. The exact algebra already identifies the visual artifact: a cyclic third-order lag heatmap should be displayed after subtracting its forced marginal-skewness DC level when the comparison null is a random shuffle of the fixed centered values.

A later source-facing visualization should distinguish at least three layers rather than mixing them in one color scale: the exact marginal-skewness baseline, the chronology-sensitive residual relative to a fixed-multiset shuffle, and the residual relative to the actual finite-size source null such as CUE.

## Research consequence

The accepted multiscale-geometry clue can now sharpen its source-specific test without inspecting new zeta values. For any complete cyclic centered-gap third-order panel, subtract the exact `T_bar` baseline before interpreting a lag-plane residual or aggregating many coefficients. Then calibrate the remaining statistic against its **actual** matched finite-size CUE or other source-faithful null; random shuffle is only the lower-information marginal-preserving control.

This closes one finite-population centering loophole but does not choose the natural growing-lag law, derive the CUE covariance, or establish any zeta-specific signal. Those remain the live source questions.