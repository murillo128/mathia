# VIS-366 — fixed-depth positive Vandermonde geometry is priced by partition sums even with growing or continuous support

## Claim

Fix an integer `q>=1` and a compact interval `K subset R`. Let `mu` be any positive probability measure supported on `K`, with finite or infinite support. Define the degree-`q-1` polynomial sampling operator

`T_mu : R^q -> L^2(mu)`

by

`(T_mu a)(t)=sum_(d=0)^(q-1) a_d t^d`,

and let

`s_1(mu)>=...>=s_q(mu)>=0`

be its singular values. For `1<=k<=q`, put

`Z_k(mu) = (1/k!) integral_(K^k) prod_(1<=i<j<=k) (x_j-x_i)^2 dmu(x_1)...dmu(x_k)`,

with `Z_0(mu)=1`.

Then, for every `k` not exceeding the rank of `T_mu`,

`prod_(r=1)^k s_r(mu) asymp_(q,K) sqrt(Z_k(mu))`,

and therefore

`s_k(mu) asymp_(q,K) sqrt(Z_k(mu)/Z_(k-1)(mu))`.

For `k=q` there is the exact identity

`prod_(r=1)^q s_r(mu)^2 = det(T_mu^*T_mu) = Z_q(mu)`.

If `mu` is discrete,

`mu=sum_i pi_i delta_(t_i)`,

with distinct support points and positive normalized masses, then

`Z_k(mu)=sum_(|I|=k) (prod_(i in I) pi_i) prod_(i<j; i,j in I) (t_j-t_i)^2`.

Thus the finite subset energies of `VIS-365` are the tropical hard-min limit of an exact non-asymptotic **Vandermonde partition sum**. At fixed polynomial depth `q`, neither growing support cardinality, continuous positive support, nor non-power/non-comparable compact node and mass scales constitute an unpriced positive-Hilbert conditioning resource: their complete effect on the leading singular products is already encoded by the finite collection `Z_1,...,Z_q`.

For the normalized positive-diagonal Wang coefficient map after the pooled rescaling of `VIS-360`--`VIS-361`, the same statement applies to its normalized coefficient measure. Hence growth of the number of compact positive scales at fixed cancellation depth does not by itself evade the source-free conditioning audit.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL ANDREIEF/ORTHOGONAL-POLYNOMIAL SPECIALIZATION + STRUCTURAL NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This proves no stronger estimate for the Chebyshev-theta remainder, the zeta zero set, or RH.

## 1. The fixed-depth bank is a moment Gram operator

Write

`v(t)=(1,t,...,t^(q-1))^T`.

The Gram matrix of `T_mu` is the `q x q` Hankel moment matrix

`G_mu=T_mu^*T_mu=integral_K v(t)v(t)^T dmu(t)`.

Its eigenvalues are `s_1(mu)^2,...,s_q(mu)^2`. Therefore the `k`-th elementary symmetric polynomial of these eigenvalues is

`e_k(s_1^2,...,s_q^2)=sum_(|D|=k) det G_mu[D,D]`,

where `D` ranges over the `k`-element subsets of the degree set `{0,...,q-1}`.

This step removes support cardinality from the linear-algebraic dimension. The support of `mu` may contain `N(epsilon)->infinity` points or be genuinely continuous; at fixed `q`, all coefficient-side information still enters through one fixed `q x q` moment Gram.

## 2. Each principal minor is an Andreief/Cauchy-Binet integral

Fix a degree set

`D={d_1<...<d_k}`.

Expanding the determinant and using Fubini gives the standard Andreief identity in this specialization:

`det G_mu[D,D]`
` = (1/k!) integral_(K^k) det(x_i^(d_j))_(i,j=1)^k^2 dmu^k(x)`.

For the consecutive degree set

`D_0={0,1,...,k-1}`,

the determinant is exactly the ordinary Vandermonde

`V(x_1,...,x_k)=prod_(i<j)(x_j-x_i)`.

Hence

`det G_mu[D_0,D_0]=Z_k(mu)`.

This is already enough to give a lower bound on `e_k` by `Z_k`.

## 3. The ordinary Vandermonde controls every fixed degree sector

For any fixed increasing degree set `D`, the generalized alternant factors as

`det(x_i^(d_j)) = V(x_1,...,x_k) S_D(x_1,...,x_k)`,

where `S_D` is a symmetric polynomial (equivalently the usual Schur-type alternant quotient after reindexing the degrees).

Because `q` is fixed, only finitely many such `D` occur. Because `K` is compact, every corresponding `S_D` is uniformly bounded on `K^k`. Thus there is a constant `C(q,K)` such that

`det G_mu[D,D] <= C(q,K) Z_k(mu)`

for every `D` and every positive probability measure `mu` on `K`.

Summing the finitely many principal minors gives

`Z_k(mu) <= e_k(s_1^2,...,s_q^2) <= C_1(q,K) Z_k(mu)`.

The constants do not depend on the number of support points, their separations, the individual positive masses, or any asymptotic parameter used to generate `mu`.

## 4. Elementary symmetric sums recover the leading singular products

Since the singular values are ordered decreasingly,

`(prod_(r=1)^k s_r)^2`

is the largest `k`-fold product of the eigenvalues of `G_mu`. It is one term of `e_k`, while `e_k` contains only `binom(q,k)` such nonnegative terms. Therefore

`(prod_(r=1)^k s_r)^2`
` <= e_k(s_1^2,...,s_q^2)`
` <= binom(q,k) (prod_(r=1)^k s_r)^2`.

Combining this with the previous section yields

`prod_(r=1)^k s_r(mu) asymp_(q,K) sqrt(Z_k(mu))`.

Whenever the rank is at least `k`, division by the corresponding `(k-1)` statement gives

`s_k(mu) asymp_(q,K) sqrt(Z_k(mu)/Z_(k-1)(mu))`.

For `k=q`, `e_q` has only one term, so the comparison becomes the exact Gram determinant identity

`det G_mu=Z_q(mu)`.

## 5. Discrete support turns the integral into a partition sum

Let

`mu=sum_i pi_i delta_(t_i)`.

In the `k`-fold integral defining `Z_k`, every tuple with a repeated support point vanishes because its Vandermonde is zero. Each unordered `k`-subset occurs in exactly `k!` permutations. Therefore

`Z_k(mu)=sum_(|I|=k) (prod_(i in I) pi_i) V(t_I)^2`.

This formula remains exact when the support cardinality grows with an external parameter. There is no fixed-`N` constant hidden in the comparison: the only comparison constants come from the fixed polynomial depth `q` and compact normalized support interval `K`.

If, in the special regime of `VIS-365`,

`sqrt(pi_i) asymp epsilon^(a_i)`

and

`|t_i-t_j| asymp epsilon^(kappa_ij)`

for a fixed finite support, each summand has exponent

`2[sum_(i in I)a_i + sum_(i<j; i,j in I)kappa_ij]`.

Because there are only finitely many summands, the smallest exponent dominates and

`sqrt(Z_k) asymp epsilon^(Gamma_k)`.

Thus `VIS-365` is recovered exactly as the tropical zero-temperature/hard-min shadow of the present partition sum. When the number of near-minimizing subsets grows, their multiplicity is not a new hidden resource: it appears directly in `Z_k`.

## 6. Wang consequence

The accepted Wang clue asks whether packet localization can create destination gain without importing a stronger estimate for the underlying normalized Chebyshev-theta remainder. `VIS-354`--`VIS-365` progressively identified and priced the fixed finite positive compact coefficient geometry.

The present result removes two apparent exits that remained after `VIS-365`.

First, **growing compact support at fixed cancellation depth is not an independent escape**. Even if the number of positive scales or translations tends to infinity, the quotient geometry is governed by the same fixed-depth moment Gram and by the partition sums `Z_k`.

Second, **power-law comparability is not essential**. Arbitrary positive masses and compact node separations, including non-power and mutually awkward scales, are already represented exactly in `Z_k`; no common valuation parameter is needed.

The same argument also covers a continuous positive limiting coefficient measure. Thus passing from a large discrete bank to an infinite positive compact support does not by itself create a new fixed-depth conditioning mechanism.

What remains genuinely outside this closure is narrower:

- cancellation depth `q` growing, where the degree sector and the constants above are no longer fixed;
- signed, indefinite, non-diagonal, or otherwise non-positive-Hilbert coefficient geometry;
- source-dependent nodes, weights, or selectors carrying signed arithmetic information rather than source-free geometry;
- normalized support that cannot remain in one compact region with the outer Wang factors uniformly controlled;
- global phase/window mechanisms, nonlinear source dependence, or an infinite-dimensional limit in which the effective polynomial depth itself grows.

For any proposed fixed-depth positive compact continuation, the decisive first audit is now to form its normalized coefficient measure `mu` and the finite family `Z_1,...,Z_q`. If the claimed gain is exactly the smallness of the corresponding partition-sum ratio, it is source-free conditioning geometry rather than evidence of stronger arithmetic cancellation.

## Prior-art audit

The determinant-of-integrals identity used above is the classical Andreief/Cauchy-Binet identity. Squared-Vandermonde product measures and their partition functions are standard objects in orthogonal-polynomial ensembles; the discrete setting is treated systematically by Baik, Kriecherbauer, McLaughlin, and Miller, *Discrete Orthogonal Polynomials: Asymptotics and Applications*, Annals of Mathematics Studies 164, Princeton University Press (2007).

No novelty is claimed for moment Grams, Andreief's identity, generalized Vandermonde factorization, orthogonal-polynomial ensembles, or determinant partition functions. The durable Mathia contribution is the exact observation that these classical identities provide a support-cardinality-independent fixed-depth audit for the current Wang coefficient geometry, thereby closing growing support and non-power compact positive geometry as standalone escape mechanisms.

## Dependencies

- `VIS-360`: pooled outer rescaling isolates the normalized polynomial-sampling Gram.
- `VIS-361`: positive diagonal coefficient weights reduce conditioning to a weighted moment Gram.
- `VIS-365`: fixed finite power-valued positive support tropicalizes to subset energies.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue whose compact positive frontier this result narrows.

## Research consequence

At fixed cancellation depth `q`, **all positive compact polynomial-sampling geometry is priced by the finite Vandermonde partition sums `Z_k`, regardless of support cardinality or power-law structure**. Growing the number of positive compact bank elements, taking a continuous positive support limit, or replacing clean power scales by non-power scales does not itself leave the source-free conditioning category.

The Wang frontier therefore moves to genuinely growing depth, different coefficient topology, source-dependent arithmetic information, noncompact/phase-window escape, or nonlinear/infinite-dimensional mechanisms that cannot be reduced to a fixed-degree positive moment Gram.
