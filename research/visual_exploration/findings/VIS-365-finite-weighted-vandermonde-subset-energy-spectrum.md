# VIS-365 — finite positive weighted Vandermonde hierarchies tropicalize to subset energies

## Claim

Fix integers `N>=q>=1`. For `0<epsilon<epsilon_0`, let

`T_epsilon={t_1(epsilon),...,t_N(epsilon)}`

be distinct real nodes contained in one fixed compact interval, and let `pi_i(epsilon)>0` be positive normalized weights. Assume that every weight and pair separation has a stable power valuation:

`sqrt(pi_i(epsilon)) asymp epsilon^(a_i)`,

`|t_i(epsilon)-t_j(epsilon)| asymp epsilon^(kappa_ij)` for `i!=j`,

with finite exponents `a_i>=0` and `kappa_ij>=0`. The `kappa_ij` are the exponents of the actual node family; they are not arbitrary pair labels.

Form the weighted degree-`q-1` sampling matrix

`B_epsilon=(sqrt(pi_i) t_i^d)_(1<=i<=N, 0<=d<=q-1)`.

Let its singular values be

`s_1>=s_2>=...>=s_q>0`.

For `1<=k<=q`, define the finite weighted Vandermonde subset energy

`Gamma_k = min_(I subset {1,...,N}, |I|=k) E(I)`,

where

`E(I)=sum_(i in I) a_i + sum_(i<j, i,j in I) kappa_ij`,

and put `Gamma_0=0`.

Then

`prod_(r=1)^k s_r(B_epsilon) asymp epsilon^(Gamma_k)`

for every `1<=k<=q`. Consequently, with

`gamma_k=Gamma_k-Gamma_(k-1)`,

one has the full singular-value spectrum

`s_k(B_epsilon) asymp epsilon^(gamma_k)`.

Equivalently, the eigenvalues of the normalized weighted moment Gram

`G_epsilon=B_epsilon^* B_epsilon`

satisfy

`lambda_k(G_epsilon) asymp epsilon^(2 gamma_k)`

when ordered decreasingly.

Thus **every fixed finite branching hierarchy of positive power-law masses and power-law node separations is already priced by a finite tropical subset ledger**. A branch tree does not create an unpriced compact cancellation resource merely because it is not reducible to one Newton chain.

For the normalized Wang coefficient map after the outer pooled rescaling of `VIS-360`--`VIS-361`, if total coefficient mass is `M` and the outer width is `rho`, the same result gives

`s_q(A_w) asymp sqrt(M) rho^(q-1) epsilon^(gamma_q)`

under their fixed positive-center hypotheses.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL COMPOUND-MATRIX/TROPICAL SPECIALIZATION + STRUCTURAL NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This proves no estimate for the arithmetic source `G`, `theta`, the zeta zero set, or RH.

## 1. Exterior powers reduce the spectrum to minors

For each `k`, let `C_k(B_epsilon)` be the `k`-th compound matrix. Its entries are all `k x k` minors of `B_epsilon`, indexed by a row subset `I` of size `k` and a degree subset

`D={d_1<...<d_k} subset {0,...,q-1}`.

The singular values of the exterior-power operator are the `k`-fold products of singular values of `B_epsilon`. Hence

`||C_k(B_epsilon)||_2 = prod_(r=1)^k s_r(B_epsilon)`.

Because `N` and `q` are fixed, the operator norm of the compound matrix is comparable, with constants independent of `epsilon`, to the largest absolute entry of that compound matrix. Therefore the exponent of the leading singular-value product is the smallest exponent among all `k x k` minors.

This is the point at which branching ceases to be a qualitative issue: the exterior power asks globally which `k` support points carry the cheapest nonzero `k`-volume.

## 2. Every minor contains the same Vandermonde separation cost

Fix a row set `I={i_1,...,i_k}` and degree set `D`. Its minor is

`Delta_(I,D)`
` = (prod_(i in I) sqrt(pi_i)) det(t_i^(d_j))_(i in I, j=1,...,k)`.

The generalized alternant

`det(t_i^(d_j))`

is divisible by the ordinary Vandermonde

`V_I=prod_(i<j, i,j in I) (t_j-t_i)`.

For each fixed `D`, the quotient is a fixed symmetric polynomial in the nodes (equivalently a Schur-polynomial alternant quotient after the usual degree reindexing). Since all normalized nodes stay in one fixed compact interval and only finitely many degree subsets occur, those quotient polynomials are uniformly bounded. Thus every minor obeys

`|Delta_(I,D)| <= C (prod_(i in I) sqrt(pi_i)) |V_I|`

and therefore

`|Delta_(I,D)| <= C' epsilon^(E(I))`.

For the consecutive degree set

`D_0={0,1,...,k-1}`,

the quotient is exactly `1`, so

`|Delta_(I,D_0)|`
` = (prod_(i in I) sqrt(pi_i)) |V_I|`
` asymp epsilon^(E(I))`.

Choose `I` attaining `Gamma_k`. Then one compound entry is of exact order `epsilon^(Gamma_k)`, while every compound entry is at most a constant times that order. Hence

`||C_k(B_epsilon)||_2 asymp epsilon^(Gamma_k)`.

Combining this with the exterior-power identity proves

`prod_(r=1)^k s_r(B_epsilon) asymp epsilon^(Gamma_k)`.

## 3. The complete singular spectrum is the sequence of marginal subset costs

Divide the `k`-volume asymptotic by the `(k-1)`-volume asymptotic:

`s_k(B_epsilon)`
` = [prod_(r=1)^k s_r]/[prod_(r=1)^(k-1) s_r]`
` asymp epsilon^(Gamma_k-Gamma_(k-1))`.

Therefore

`gamma_k=Gamma_k-Gamma_(k-1)`

is the exact asymptotic exponent of the `k`-th singular value.

Because the `s_k` are ordered decreasingly, the realizable node/weight valuations automatically force

`gamma_1<=gamma_2<=...<=gamma_q`.

This is a useful consistency condition. An arbitrary table of proposed pair exponents `kappa_ij` need not satisfy it, but exponents coming from an actual one-parameter node family do.

The smallest singular exponent is

`gamma_q=Gamma_q-Gamma_(q-1)`.

The minimizing `(q-1)`-subset and `q`-subset need not lie on one nested branch. That is exactly why this formulation covers finite branching: the spectrum is determined by global minimum-volume support selections rather than by imposing a single Newton ordering.

## 4. Recovery of the previous one-branch and weighted-Hermite ledgers

`VIS-364` considered the maximally nested chain

`0, epsilon^(kappa_1), ..., epsilon^(kappa_(q-1))`

with zero weight valuations. The pairwise separation exponents produced by this actual chain give

`Gamma_k=sum_(r=1)^(k-1) K_r`,

where

`K_r=sum_(j=1)^r kappa_j`.

Hence

`gamma_k=K_(k-1)`,

recovering the cumulative Newton spectrum

`1, epsilon^(K_1), ..., epsilon^(K_(q-1))`.

Likewise, polynomially vanishing positive masses simply add the vertex costs `a_i` to the same subset energy. This is the finite-support global form of the local weighted-Hermite accounting in `VIS-363`: mass loss and geometric collision are not separate hidden resources; both enter the same exterior-volume valuation.

The new contribution is not a new singular-value theorem. It is the exact observation that, for Mathia's fixed finite positive weighted polynomial-sampling problem, **arbitrary finite branching can be priced without choosing a branch decomposition at all**.

## 5. Wang consequence

Use the pooled normalized coordinate from `VIS-360`--`VIS-361`:

`x_i=c+rho t_i`,

with `c` in a fixed positive compact interval and positive diagonal coefficient weights of total mass `M`. Those findings reduce the fixed-depth Wang quotient, up to uniformly conditioned factors, to the normalized weighted degree-`q-1` sampling Gram, with the outer polynomial scale `rho^(q-1)` and mass scale `sqrt(M)` exposed separately.

Applying the present result to the normalized weights `pi_i=w_i/M` gives

`lambda_min(G_epsilon) asymp epsilon^(2 gamma_q)`

and therefore

`s_q(A_w) asymp sqrt(M) rho^(q-1) epsilon^(gamma_q)`.

A finite recursively branching positive cluster tree with stable power valuations is consequently source-free conditioning geometry. Its deepest loss can be severe, but it is completely visible in the weighted Vandermonde subset energies.

## 6. What this closes and what remains

`VIS-364` left recursive branching as the first obvious compact positive-diagonal geometry not covered by a single Newton chain. The present compound-matrix reduction closes the **fixed finite, power-valued** version of that escape.

The following are no longer sufficient by themselves to claim a new compact mechanism:

- a finite branch tree of colliding centers;
- several incomparable positive power-law separation exponents;
- positive support masses vanishing at different power rates;
- changing which finite branch supplies the cheapest local interpolation directions.

All of those effects alter `Gamma_k`, but they do not leave the subset-energy ledger.

What remains outside this result is materially different:

- support cardinality `N=N(epsilon)` growing with the asymptotic parameter, where the number and occupancy of competing minors can itself change scale;
- cancellation depth `q` growing;
- node or mass scales without stable power valuations, including genuinely non-power or non-comparable asymptotics that cannot be captured after one fixed valuation parameterization;
- signed, indefinite, non-diagonal, or otherwise non-Hilbert coefficient geometry;
- source-dependent weights or node choices carrying signed arithmetic information from `G`, `theta`, or an equivalent source statistic;
- global phase/window geometry, scale escape, infinite-dimensional limits, or nonlinear source dependence already separated by the Wang clue.

For a proposed positive-diagonal compact continuation with fixed `N,q`, the decisive check is now finite: compute the actual weight valuations `a_i`, pair-separation valuations `kappa_ij`, the energies `Gamma_k`, and the marginal exponent `gamma_q`. If the claimed gain is exactly `epsilon^(gamma_q)`, it is conditioning geometry, not new arithmetic cancellation.

## Prior-art audit

The exterior-power identity used above is standard matrix analysis: the singular values of the `k`-th compound/exterior power are the `k`-fold products of the singular values of the original matrix, so its operator norm is the product of the `k` largest singular values. The Cauchy-Binet/compound-matrix viewpoint is classical.

The valuation interpretation is also classical in a more general form. Kiumars Kaveh and Peter Makhnatch, **Invariant Factors as Limit of Singular Values of a Matrix**, *Arnold Mathematical Journal* 8 (2022), 561--571, DOI `10.1007/s40598-022-00217-y`, prove that logarithmic singular-value asymptotics of Laurent-series matrix families converge to invariant-factor data. The present result is a concrete fixed-support weighted-Vandermonde specialization whose exponents can be written explicitly as minimum subset energies.

Generalized Vandermonde minors factoring into the ordinary Vandermonde times a symmetric/Schur factor are classical. Milan Janjic, **On Vandermonde determinants via n-determinants**, arXiv `2202.02075`, records subdeterminant/Schur-polynomial formulations. The clustered-Vandermonde literature already cited in `VIS-364` -- Kunis and Nagel (2020) and Batenkov, Diederichs, Goldman, and Yomdin (2021) -- likewise treats node-cluster geometry as the controlling spectral datum.

Accordingly, no novelty is claimed for compound matrices, tropical singular values, generalized Vandermonde factorization, or clustered-Vandermonde spectral theory. The durable Mathia value is the explicit subset-energy ledger and the resulting closure of the finite branching positive-weight Wang escape.

## Dependencies

- `VIS-360`: pooled outer rescaling isolates the normalized polynomial-sampling Gram.
- `VIS-361`: positive diagonal coefficient weights reduce conditioning to a weighted moment Gram.
- `VIS-362`: one common healthy inner scale prices a first outer rank collapse.
- `VIS-363`: polynomially vanishing masses become additive weighted Hermite costs on one common inner scale.
- `VIS-364`: a maximally nested one-branch hierarchy has cumulative Newton separation exponents.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue whose compact frontier this result narrows.

## Research consequence

For fixed `N` and `q`, positive diagonal weights, compact normalized nodes, and stable power valuations of every weight and pair separation, **the entire weighted polynomial-sampling singular spectrum is determined by the finite energies `Gamma_k`**. Finite branching, by itself, is therefore closed as an unpriced compact Wang resource.

The compact frontier moves to growing support/depth, non-power asymptotic geometry, non-positive/non-diagonal coefficient topology, or genuine source-dependent arithmetic information. Any future fixed finite positive branching proposal must beat the subset-energy formula rather than merely exhibit a more complicated cluster tree.
