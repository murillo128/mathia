# VIS-026 — fixed-gap discrepancy permutations have an exact bridge covariance

## Claim

Let

`0 = x_0 < x_1 < ... < x_N = 1`

be any finite ordered point set, with gaps

`g_i = x_i - x_(i-1)`

and centered gap increments

`delta_i = g_i - 1/N`.

Put

`sigma_g^2 = (1/N) sum_i delta_i^2`.

For a uniformly random permutation `pi` of the fixed gap multiset, define the reordered discrepancy process

`D_k^(pi) = sum_(r=1)^k delta_(pi(r))`, `1 <= k <= N-1`.

Then, exactly at finite `N`,

`E[D_k^(pi)] = 0`

and

`Cov(D_k^(pi), D_l^(pi))`
` = sigma_g^2 min(k,l) [N-max(k,l)]/(N-1)`.

Therefore the rescaled process

`B_k = sqrt(N-1) D_k^(pi)/(N sigma_g)`

has covariance

`Cov(B_k,B_l) = min(k/N,l/N) - (k/N)(l/N)`,

which is exactly the Brownian-bridge covariance kernel sampled on the rank grid. The finite permutation process need not be Gaussian; the statement is an exact covariance identity, not an invariance principle.

The corresponding squared grid-discrepancy energy

`E_2(pi) = sum_(k=1)^(N-1) [D_k^(pi)]^2`

has exact permutation mean

`E[E_2(pi)] = sigma_g^2 N(N+1)/6`.

Thus the dimensionless ratio

`R = E_2(actual ordering) / [sigma_g^2 N(N+1)/6]`

separates the contribution of the **ordering** from the contribution of the fixed gap multiset at second order. `R=1` is the mean over all same-gap orderings; it is not an RH benchmark and carries no asymptotic implication by itself.

**Evidence/status:** `CLASSICAL-FINITE-POPULATION PROCESS + EXACT-DERIVED SPECIALIZATION`.

No new probability limit theorem is claimed.

## Exact derivation

Since the gaps sum to one,

`sum_i delta_i = 0`.

For every permutation position `r`,

`E[delta_(pi(r))] = 0`

and

`E[delta_(pi(r))^2] = sigma_g^2`.

For two distinct positions `r != s`, sampling without replacement gives

`E[delta_(pi(r)) delta_(pi(s))]`
` = [sum_(a != b) delta_a delta_b]/[N(N-1)]`
` = -sigma_g^2/(N-1)`,

because

`sum_(a != b) delta_a delta_b`
` = (sum_a delta_a)^2 - sum_a delta_a^2`
` = -N sigma_g^2`.

Assume `k <= l`. The covariance of the two partial sums contains `k` identical-position terms and `kl-k` distinct-position terms, so

`Cov(D_k,D_l)`
` = k sigma_g^2 - (kl-k) sigma_g^2/(N-1)`
` = sigma_g^2 k(N-l)/(N-1)`.

Symmetrizing in `k,l` gives the stated kernel. Multiplying by `(N-1)/(N^2 sigma_g^2)` yields

`min(k,l)/N - kl/N^2`,

the standard bridge covariance evaluated at `k/N,l/N`.

Finally,

`E[E_2] = sum_(k=1)^(N-1) Var(D_k)`
` = [sigma_g^2/(N-1)] sum_(k=1)^(N-1) k(N-k)`
` = sigma_g^2 N(N+1)/6`.

No central-limit or large-`N` approximation enters these identities.

## Farey specialization

For the positive Farey fractions of order `n`, append `x_0=0`, retain the terminal point `x_N=1`, and use their consecutive gaps. A direct finite evaluation compares the deterministic Farey discrepancy path with the exact same-gap permutation control.

At `n=100` there are `N=3044` gaps. Direct evaluation gives

`E_2(F_100) = 0.005113787801334398`

while the exact same-gap permutation mean is

`0.2176486473943855`,

so

`R_100 = 0.02349561029923641`.

Evaluating the same finite statistic for `n = 20, 30, 40, 60, 80, 100, 120, 150, 200, 250, 300` gives respectively

`R_n = 0.151974, 0.093801, 0.064789, 0.042856, 0.032204, 0.023496, 0.019657, 0.015320, 0.012163, 0.008516, 0.007014`.

This shows strong finite-order suppression relative to the fixed-gap permutation mean across the tested orders. No asymptotic fit is imposed: the observed decline is a finite-order diagnostic, not evidence for a limiting exponent.

This control answers a narrow representation question. A visual discrepancy path can look unusually small either because its gap **sizes** are special or because their **ordering** cancels partial sums. The same-gap permutation ensemble holds the first channel fixed and randomizes only the second.

## Prior art and novelty assessment

Rogelio Tomás García, **A General Lower Bound for Average Local Discrepancy and an Application to the Farey Sequence**, *Mathematics* 14:14 (2026), 2543, DOI `10.3390/math14142543`, explicitly studies sequences obtained by permuting a fixed gap multiset. For the `L^1` average local discrepancy he proposes the empirical scale `sigma_g N^(3/2)` and emphasizes that Farey gap ordering materially affects discrepancy. This is the nearest direct Farey prior art.

The stochastic-process side is classical finite-population sampling. Jan Hagberg, **Approximation of the Summation Process Obtained by Sampling from a Finite Population**, *Theory of Probability and Its Applications* 18:4 (1974 English edition), 753–766, DOI `10.1137/1118095`, studies partial-sum processes of random permutations of finite populations and their tied-down Wiener-process limits under suitable conditions.

Accordingly, neither the bridge language nor sampling-without-replacement behavior is claimed as novel. The durable contribution here is the elementary finite-`N` covariance and exact `L^2` permutation-energy specialization that turns García's same-gap ordering idea into a deterministic control usable by Mathia's visual/Farey research. A search of the directly relevant García treatment found the `L^1` permutation conjecture but not this finite-`N` squared-energy identity; absence there is not a claim that the identity is new in the wider probability literature.

## Boundary conditions and falsification

The result assumes a uniform random permutation of a fixed multiset of `N` gaps. Repeated gap values cause no ambiguity: every distinct multiset ordering has the same number of labelled-permutation preimages.

The covariance identity does **not** say the finite process is Gaussian. Brownian-bridge terminology refers only to the exact covariance kernel; a tied-down Wiener limit needs additional finite-population conditions such as control of exceptionally large increments.

The scalar `R` is also intentionally lossy. It detects second-order suppression or inflation of cumulative discrepancy relative to the same-gap ensemble but does not say which correlations or denominator strata cause it. Two orderings with the same `E_2` can have very different multiscale geometry.

For Farey data, finite-order suppression is not an RH result. A substantive Farey mechanism would need an exact decomposition or asymptotic estimate showing which arithmetic ordering relations create the suppression and whether that information survives reduction to the classical Franel–Landau/Möbius criteria.

## Research consequence

The exact permutation bridge supplies a clean matched control for `farey_discrepancy`: it removes the complete one-point gap multiset while retaining only ordering information. The visual experiment exposes a large finite-order separation, but the responsible next step is a clue rather than a stronger claim.

A proposed cross-line clue is therefore handed to:

`research/farey_discrepancy/clues/CLUE-farey-gap-order-bridge-suppression.md`.

Its decisive question is whether the observed suppression can be decomposed into a genuinely multiscale Farey ordering mechanism, or whether it collapses to already-known local adjacency, denominator-stratum, or Möbius discrepancy structure.
