# PL-085 — Full critical prime-support Gram bulk is Poisson under the full local Hardy–Littlewood hierarchy

## Claim

The fixed-moment Poisson hierarchy of `PL-084` upgrades to convergence of the **entire empirical bulk spectral law** once the corresponding local Hardy--Littlewood input is assumed at every fixed tuple order.

Fix

```text
0<a<b<infinity,
c>0,
P_X={p prime : aX<p<=bX},
M_X=|P_X|,
T_X=c X/log X,
```

and let

```text
G_X(p,q)
 =(1/T_X) integral_0^(T_X) exp(i t(log p-log q)) dt,
p,q in P_X.
```

Assume the **full local Hardy--Littlewood hierarchy**: for every fixed integer `r>=1` and every fixed `A>0`, uniformly for distinct shifts

```text
H={0,h_1,...,h_(r-1)} subset [-A log X,A log X],
```

and on fixed macroscopic sub-bands of `[aX,bX]`, the prime `r`-tuple count has the Hardy--Littlewood asymptotic with singular series `S(H)` and error `o(X/(log X)^r)` uniform in the shifts. The order `r` is fixed before `X->infinity`; no uniformity as `r->infinity` is assumed.

If

```text
mu_X=(1/M_X) sum_(j=1)^(M_X) delta_(lambda_j(G_X))
```

is the empirical spectral measure, then there is a deterministic probability law `nu_(a,b,c)` on `[0,infinity)` such that

```text
boxed:
W_2(mu_X,nu_(a,b,c)) -> 0.
```

In particular `mu_X` converges weakly to `nu_(a,b,c)`. The limit is the macroscopic `x in [a,b]` mixture of the unit-intensity **Poisson sinc Euclidean-random-matrix bulk law**, defined rigorously below as the `W_2` limit of compact-range sinc kernels. Its moments are exactly the Palm closed-walk moments derived in `PL-084`:

```text
integral lambda^m d nu_(a,b,c)(lambda)
 = (1/(b-a)) integral_a^b mu_m(x;c) dx
```

for every fixed `m>=1`.

Thus, under the classical Hardy--Littlewood/Gallagher local-prime model at **all fixed orders**, not merely every preselected finite collection of trace moments but the full support-only bulk empirical spectrum at the mean-prime-gap horizon

```text
T=cX/log X
```

is reproduced by a generic Poisson spatial point process with the same local density and sinc observation kernel.

This closes the specific boundary left open in `PL-084`. It does **not** control the hard edge strongly enough for `log det`, raw extreme eigenvalues, moments whose order grows with `X`, arithmetic amplitudes such as `Lambda` or `mu`, Nyman/target-relative observables, or any completed explicit-formula construction.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + CONJECTURAL-INPUT + PRIOR-ART/REDIRECT`, with a `DECISIVE-NEGATIVE` conclusion only for the **full bulk empirical law of the unweighted prime-support critical Gram under the full local Hardy--Littlewood hierarchy**.

## Centering reduces the problem to a real sinc matrix

As in `PL-083`--`PL-084`, centering the observation interval changes the Gram matrix only by diagonal unitary conjugacy. Hence `G_X` has the same eigenvalues as the real symmetric matrix

```text
A_X(p,q)
 = sinc((T_X/2) log(p/q)),

sinc(u)=sin(u)/u.
```

The exact dependence on prime support is therefore contained in the point set `{p}` and the logarithmic difference kernel. No zeta continuation or functional equation has entered.

For a fixed range parameter `A>0`, truncate only the **ordinary additive separation**:

```text
A_X^(A)(p,q)
 = A_X(p,q) 1_(|p-q|<=A log X).
```

This truncation is Hermitian but need not remain positive semidefinite. That is harmless: its empirical eigenvalue measure is a probability measure on `R`, and the truncation is used only as an intermediate spectral approximation. Positivity is recovered for the final law because the untruncated `A_X` is a Gram matrix.

Write

```text
mu_X^(A)
 =(1/M_X) sum_j delta_(lambda_j(A_X^(A))).
```

The proof proceeds in two independent steps: first classify `mu_X^(A)` for each fixed `A`, where the kernel is compact range; then remove the truncation in normalized Hilbert--Schmidt/Wasserstein distance.

## Every compact-range spectral law is moment determinate

Fix `A`. The equality-pattern expansion in `PL-084` applies verbatim to every fixed trace power of `A_X^(A)`. At the critical scale, writing

```text
p_0=xX,
p_j=p_0+u_j log X,
```

turns the limiting compact-range kernel into

```text
k_(x,c,A)(u,v)
 = sinc(c(u-v)/(2x)) 1_(|u-v|<=A).
```

For a closed walk of length `m`, partition its cyclic positions according to which positions represent the same point. Suppose the quotient walk has `r` distinct vertices. Whenever the kernel product is nonzero, each edge constrains the corresponding coordinate difference to size at most `A`. Choose a spanning tree of the connected quotient graph and fix the distinguished vertex at `0`. Successively integrating along the tree confines the remaining `r-1` coordinates to intervals of length at most `2A`. Since `|sinc|<=1`, the absolute value of the corresponding integral is bounded by

```text
(2A)^(r-1).
```

The number of equality partitions of `m` positions into `r` nonempty blocks is the Stirling number `S(m,r)`. Therefore the limiting absolute moments obey a Touchard-type bound

```text
|m_m^(A)|
 <= sum_(r=1)^m S(m,r) (2A)^(r-1)
 <= (C_A m)^m
```

for a constant `C_A` independent of `m`.

In particular

```text
(m_(2m)^(A))^(-1/(2m))
 >= c_A/m,
```

up to an irrelevant change of constants, and hence

```text
sum_(m>=1)
 (m_(2m)^(A))^(-1/(2m))
 = infinity.
```

Carleman's criterion makes the compact-range limiting moment sequence determinate.

This is exactly the standard mechanism appearing in the Euclidean-random-matrix literature: Bordenave expands trace moments by surjective equality patterns and obtains a `(Cm)^m` bound sufficient for Carleman in the fixed-density compact-support model. The derivation above is included because the prime matrix has a slowly varying macroscopic parameter `x` and because the final sinc kernel is not compactly supported.

## Full local Hardy--Littlewood gives the compact-range prime law

For any fixed integer `m`, expand

```text
(1/M_X)Tr((A_X^(A))^m)
```

as closed walks and group them by their equality pattern. If an equality pattern uses `r<=m` distinct primes, all relevant shifts lie in a fixed multiple of `[-A log X,A log X]`. The assumed local Hardy--Littlewood asymptotic at order `r`, followed by Gallagher's average of the singular series, turns the scaled factorial measure of those distinct prime offsets into ordinary Lebesgue measure.

Consequently, for each fixed `m`,

```text
integral lambda^m d mu_X^(A)(lambda)
 -> m_m^(A),
```

where `m_m^(A)` is the corresponding `x`-averaged Palm Poisson closed-walk moment for `k_(x,c,A)`.

The compact-support Poisson Euclidean-random-matrix model supplies an actual probability measure with these moments, and the Carleman estimate above makes it unique. Hence the ordinary method of moments gives a deterministic law `nu_A` such that

```text
mu_X^(A) -> nu_A
```

weakly.

The second moments converge as part of the same hierarchy, so weak convergence plus convergence of second moments yields the stronger statement

```text
boxed:
W_2(mu_X^(A),nu_A) ->0
```

for every fixed `A`.

No single Hardy--Littlewood statement uniform in tuple order is hidden here. To prove convergence of the measure, one invokes the hypothesis separately for each fixed moment order and then uses determinacy of the resulting full moment sequence.

## The sinc tail is small in Wasserstein distance

The crucial point is that passing from compact-range kernels to the full sinc kernel does **not** require moment determinacy for the untruncated infinite-range model.

`PL-083` established, from the unconditional dimension-two prime-pair upper-bound sieve, that for primes in the fixed macroscopic band

```text
|A_X(p,q)|^2
 <<_(a,b,c)
 min(1,(log X/|p-q|)^2),
```

and that the prime-pair local factor has bounded mean. The same calculation gives

```text
limsup_(X->infinity)
 (1/M_X)||A_X-A_X^(A)||_F^2
 <= C_(a,b,c)/A.
```

For Hermitian matrices of the same size, the Hoffman--Wielandt inequality implies

```text
W_2(mu_X,mu_X^(A))^2
 <= (1/M_X)||A_X-A_X^(A)||_F^2.
```

Therefore

```text
limsup_(X->infinity)
 W_2(mu_X,mu_X^(A))
 <= C A^(-1/2).
```

Likewise, if `B>A`,

```text
limsup_(X->infinity)
 W_2(mu_X^(A),mu_X^(B))
 <= C A^(-1/2).
```

Passing to the already-established compact-range limits gives

```text
W_2(nu_A,nu_B)
 <= C A^(-1/2).
```

Thus `{nu_A}` is Cauchy in the complete Wasserstein space `P_2(R)`. Define

```text
nu_(a,b,c)=lim_(A->infinity) nu_A
```

in `W_2`.

Now use the triangle inequality:

```text
W_2(mu_X,nu_(a,b,c))
 <= W_2(mu_X,mu_X^(A))
    +W_2(mu_X^(A),nu_A)
    +W_2(nu_A,nu_(a,b,c)).
```

First let `X->infinity` at fixed `A`, then let `A->infinity`. The first and third terms are `O(A^(-1/2))`, while the middle term vanishes. Hence

```text
boxed:
W_2(mu_X,nu_(a,b,c))->0.
```

Because every `mu_X` is supported on `[0,infinity)`, so is the weak/Wasserstein limit `nu_(a,b,c)`, even though the auxiliary truncated matrices need not be positive.

## The limiting moments are exactly those of `PL-084`

The preceding truncation argument constructs the full limiting law without needing to prove Carleman directly for the infinite-range sinc moment hierarchy.

For every fixed `m`, `PL-084` independently gives

```text
(1/M_X)Tr(G_X^m)
 -> (1/(b-a)) integral_a^b mu_m(x;c) dx.
```

To identify this with the moments of `nu_(a,b,c)`, use any even order `2r>m`. The full local Hardy--Littlewood hierarchy gives a finite limiting `2r`-th moment, so the family `{mu_X}` is uniformly integrable for `|lambda|^m`. The `W_2`/weak convergence can therefore be upgraded for each fixed polynomial moment by this higher-moment control. Thus

```text
int lambda^m d nu_(a,b,c)(lambda)
 = (1/(b-a)) int_a^b mu_m(x;c) dx.
```

The complete moment hierarchy and the full empirical-law statement are therefore consistent, but logically distinct: `PL-084` supplies the explicit moments; compact-range determinacy plus the pair-sieve `L^2` tail supplies convergence of the measure.

## Identification with a generic Poisson Euclidean random matrix

Bordenave studies matrices whose entries are a fixed compact-support function of pairwise differences of random spatial points while the containing region expands at fixed point density. In his fixed-density model he proves almost-sure convergence of the empirical spectral measure and computes its moments by the same surjective/equality-pattern closed-walk expansion. His moment estimate is of order `(Cm)^m`, giving Carleman determinacy.

For fixed `x` and `A`, specialize that model to one dimension, unit point intensity, and the Hermitian compact-range kernel

```text
f_(x,A)(u)
 = sinc(cu/(2x)) 1_(|u|<=A).
```

Its limiting moments are exactly the Palm Poisson closed-walk moments used above. Therefore `nu_A` is the uniform macroscopic mixture over `x in [a,b]` of these standard compact-range Poisson Euclidean-random-matrix laws.

Bordenave's theorem is **not** being applied directly to the full sinc kernel: `sinc(u)` has an infinite `1/u` tail and falls outside the compact-support hypothesis used for this comparison. The full law here is instead the canonical `W_2` completion

```text
nu_(a,b,c)=W_2-lim_(A->infinity) nu_A,
```

whose existence is forced by the prime-pair `L^2` tail estimate. Calling it the Poisson sinc Euclidean-random-matrix law refers to this controlled completion, not to an unchecked black-box theorem.

This matched control is stronger than agreement of finitely many moments. Under the stated arithmetic hypothesis, every bounded continuous bulk spectral observable has exactly the same asymptotic law as this generic local Poisson model after the macroscopic `x` mixture.

## Prior art and novelty audit

The mechanism is an exact synthesis of classical inputs rather than new prime-statistics or random-matrix theory.

- **P. X. Gallagher**, “On the distribution of primes in short intervals,” *Mathematika* **23**(1) (1976), 4--9, DOI `10.1112/S0025579300016442`, proves that suitable Hardy--Littlewood prime-tuple conjectures imply Poisson statistics for prime counts in intervals of length `lambda log X`. His singular-series averaging is the arithmetic engine behind `PL-083`, `PL-084`, and the present all-fixed-orders hypothesis.
- **Tristan Freiberg**, “A Note on the Distribution of Primes in Intervals,” in *Irregularities in the Distribution of Prime Numbers*, Springer, 2018, pp. 23--44, DOI `10.1007/978-3-319-92777-0_2`, derives joint asymptotic independence of prime counts in finitely many adjacent logarithmic intervals under a Hardy--Littlewood hypothesis. This is close prior art for interpreting the finite-dimensional local prime process as Poisson rather than merely matching one count.
- **Charles Bordenave**, “Eigenvalues of Euclidean random matrices,” *Random Structures & Algorithms* **33**(4) (2008), 515--532, DOI `10.1002/rsa.20228`, arXiv `math/0606624`, proves almost-sure empirical spectral convergence for a fixed-density Euclidean-random-matrix model with compact-support kernel, computes the limiting moments by equality patterns, and supplies the `(Cm)^m`/Carleman mechanism used as the matched spectral control.

A targeted search around prime-supported sinc Grams, Hardy--Littlewood prime processes, Poisson Euclidean random matrices, and empirical spectral laws did not locate a source stating this exact prime-Gram `W_2` completion. No novelty is claimed for the Poisson local-prime model, the singular-series averages, the Euclidean-random-matrix moment method, Carleman, or Hoffman--Wielandt. The durable line-specific content is the exact conditional bridge showing that these classical ingredients close the **full bulk ESD** boundary left by `PL-084`.

The novelty audit is decisively negative for the proposed RH mechanism: once the full classical local Hardy--Littlewood hierarchy is granted, the critical support-only bulk spectrum has a generic Poisson matched control and contains no additional visible analytic-continuation structure.

## Adversarial boundaries

1. **The result is conditional.** The required local Hardy--Littlewood hierarchy is not known for the rational primes. This finding must not be quoted as an unconditional ESD theorem.
2. **The assumption is all fixed orders, not growing order.** For every fixed `r` the required asymptotic is assumed, but there is no uniform control when `r=r(X)->infinity`. Consequently large deviations, spectral tails requiring growing moments, and determinant-like quantities may escape.
3. **The full ESD does not control raw extremes.** `PL-082` gives subsequences with `lambda_min->0` and `lambda_max->infinity` at every `T=o(X)`. Such a vanishing fraction of eigenvalues is compatible with a deterministic bulk law.
4. **`log det` remains outside the theorem.** Weak or `W_2` convergence does not give uniform integrability of `log lambda` at the hard edge. Rare near-singular prime clusters can dominate products of eigenvalues while disappearing from the empirical bulk.
5. **The compact-range truncation is not itself a Gram matrix.** It may have negative eigenvalues. Only Hermiticity and moment/Wasserstein comparison are used; the final limit is nonnegative because it is the limit of the original positive Gram matrices.
6. **Bordenave is a compact-support matched control, not a direct theorem for sinc.** The `A->infinity` step is supplied by the prime-pair Frobenius tail and Hoffman--Wielandt, not by silently extending a compact-support ERM theorem to a `1/u` kernel.
7. **The macroscopic `x` dependence survives only as a mixture.** At local height `p~xX`, the kernel is `sinc(c(u-v)/(2x))`; the prime number theorem makes the distinguished macroscopic base point asymptotically uniform in `x` after normalization by `M_X`.
8. **Weights and targets are not covered.** `Lambda`, Möbius orientation, Nyman/Bagchi target couplings, completion-dependent amplitudes, and explicit-formula terms change the local factorial measures or add global information carriers.
9. **No `Re(s)=1/2` is selected.** The only criticality is the finite-time sampling relation `T~X/log X`, where a Fourier cell matches the mean prime gap. There is no complex `sigma` parameter in this support-only matrix.
10. **No analytic continuation occurs.** All exact matrix identities are finite. The Hardy--Littlewood input describes local prime configurations on the integer line and does not continue an Euler product into the critical strip.
11. **Poisson bulk universality is a quotient, not literal independence of primes.** Individual prime tuples retain their singular series. The arithmetic factors disappear only after the averaging relevant to normalized bulk spectral statistics.

## Consequence for the prime-lattice search

The unweighted prime-basis sharp-Gram branch at its first nontrivial bulk scale is now conditionally closed at the level of the **entire empirical spectrum**:

```text
T >> X/log X
    -> bulk delta_1 unconditionally in normalized Hilbert--Schmidt sense
       (`PL-081`);

T = c X/log X
    -> full bulk ESD = generic Poisson sinc ERM law
       under the full local Hardy--Littlewood hierarchy
       (this finding);

any T=o(X)
    -> raw spectral extremes are polluted by bounded prime clusters
       (`PL-082`).
```

The exact mean-gap horizon therefore does not become an RH mechanism merely by replacing finitely many trace moments with the full support-only empirical spectrum. Under the classical local-prime model, the complete bulk law is still a local point-process statistic.

A surviving finite-horizon route must transport information discarded by that quotient: a distinguished arithmetic amplitude or target, a completed explicit-formula coupling, a hard-edge/determinant or growing-order statistic together with a genuinely global arithmetic rigidity theorem, or another construction that imports analytic-continuation information rather than merely resolving the local prime point process.