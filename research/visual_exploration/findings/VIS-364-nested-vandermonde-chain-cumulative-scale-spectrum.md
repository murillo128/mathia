# VIS-364 — polynomially nested Vandermonde chains have a cumulative Newton scale spectrum

## Claim

Fix a finite Wang asymptotic depth `q>=2` and exponents

`0<kappa_1<kappa_2<...<kappa_(q-1)`.

For `0<epsilon<1`, define a maximally nested chain of normalized nodes

`t_0=0`,
`t_r=epsilon^(kappa_r)`, `1<=r<=q-1`,

and let `S_epsilon` be the square degree-`q-1` polynomial-sampling matrix

`(S_epsilon)_(m,d)=t_m^d`, `0<=m,d<=q-1`.

Put

`K_0=0`,
`K_r=sum_(i=1)^r kappa_i`.

Then the singular values of `S_epsilon`, ordered decreasingly, satisfy

`s_(r+1)(S_epsilon) asymp epsilon^(K_r)`, `0<=r<=q-1`.

In particular,

`s_q(S_epsilon) asymp epsilon^(kappa_1+...+kappa_(q-1))`.

The same exponents hold after multiplying the sample rows by fixed positive weights bounded above and below independently of `epsilon`.

For the Wang map, let `D_beta=diag(beta_1,...,beta_q)` be invertible, let `c` stay in a fixed positive compact interval, and put

`x_m=c+rho t_m`

with `rho>0` small enough that all `x_m` remain in a fixed positive compact interval. If

`V_(k,m)=x_m^k`, `1<=k<=q`, `0<=m<=q-1`,

and

`A=D_beta V`,

then uniformly for small `rho,epsilon`,

`s_q(A) asymp rho^(q-1) epsilon^(K_(q-1))`.

Thus a finite hierarchy of strictly nested polynomial scales can create a much smaller compact Vandermonde floor than a one-scale cluster, but the loss is not mysterious: **the exponents accumulate as the Newton interpolation pivots `K_r`**. In the maximally nested chain, each deeper node pays every coarser separation already traversed.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL CLUSTERED-VANDERMONDE SPECIALIZATION + STRUCTURAL NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This is a source-free conditioning statement. It proves no stronger estimate for `theta`, the normalized source remainder `G`, the zeta zero set, or RH.

## 1. Newton interpolation triangularizes the hierarchy

Define the Newton polynomials for the ordered nodes

`N_0(t)=1`,
`N_r(t)=prod_(i=0)^(r-1) (t-t_i)`, `1<=r<=q-1`.

Let `C_epsilon` be the coefficient-change matrix whose `r`-th column contains the monomial coefficients of `N_r`. Every `N_r` is monic and all lower coefficients are elementary symmetric functions of nodes tending to zero, so

`C_epsilon -> I`

as `epsilon->0`. Hence `C_epsilon` and `C_epsilon^(-1)` are uniformly bounded for sufficiently small `epsilon`.

The sampling matrix in the Newton basis is

`L_epsilon=S_epsilon C_epsilon`,

with entries

`(L_epsilon)_(m,r)=N_r(t_m)`.

Because `N_r` vanishes at `t_0,...,t_(r-1)`, the matrix is lower triangular. Its diagonal pivots are

`d_r=N_r(t_r)=prod_(i=0)^(r-1)(t_r-t_i)`.

For `r>=1`,

`|t_r-t_0|=epsilon^(kappa_r)`,

while for `1<=i<r`, strict ordering of the exponents gives

`|t_r-t_i|`
` = epsilon^(kappa_i) |1-epsilon^(kappa_r-kappa_i)|`
` asymp epsilon^(kappa_i)`.

Therefore

`|d_r| asymp epsilon^(kappa_1+...+kappa_r)=epsilon^(K_r)`.

The cumulative exponent is already visible at the interpolation-pivot level: the `r`-th new degree of freedom must cross every previous separation in the chain.

## 2. The diagonal pivot scales are the full singular spectrum

Let

`D_epsilon=diag(d_0,d_1,...,d_(q-1))`, `d_0=1`,

and column-normalize the Newton sampling matrix:

`R_epsilon=L_epsilon D_epsilon^(-1)`.

For `m=r`, `(R_epsilon)_(r,r)=1`; for `m<r` the entry is zero. For `m>r>=1`,

`(R_epsilon)_(m,r)`
` = prod_(i=0)^(r-1) (t_m-t_i)/(t_r-t_i)`.

The `i=0` factor is

`t_m/t_r=epsilon^(kappa_m-kappa_r) -> 0`,

while every factor with `1<=i<r` tends to `1`. The first column is identically `1`. Consequently `R_epsilon` converges to the fixed invertible lower-triangular matrix having an all-ones first column, ones on the remaining diagonal, and zeros elsewhere below those diagonal entries. In particular, `R_epsilon` and `R_epsilon^(-1)` are uniformly bounded.

We therefore have the factorization

`S_epsilon=R_epsilon D_epsilon C_epsilon^(-1)`

between two uniformly conditioned matrices. Singular values are stable up to fixed multiplicative constants under such left and right factors. Since

`1, epsilon^(K_1), ..., epsilon^(K_(q-1))`

are already strictly decreasing scales, it follows that

`s_(r+1)(S_epsilon) asymp epsilon^(K_r)`.

This gives more than the determinant identity. Indeed,

`|det S_epsilon| asymp epsilon^(sum_(r=1)^(q-1) K_r)`

only fixes the product of the singular values; the Newton factorization identifies each scale separately.

For example, with `q=3`, `kappa_1=1`, and `kappa_2=kappa>1`, the nodes are

`0, epsilon, epsilon^kappa`

and the singular spectrum is

`1, epsilon, epsilon^(kappa+1)`

up to fixed factors. After the first `epsilon` rescaling, two support points are visible but one of them still contains an `epsilon^(kappa-1)` split. The last direction therefore pays both the first separation and the deeper one.

## 3. Transfer to the Wang coefficient map

For a row direction `y in C^q`, write

`p_y(x)=sum_(k=1)^q conjugate(y_k) beta_k x^k=x Q_y(x)`

with `deg Q_y<=q-1`. In the normalized coordinate `x=c+rho t`, write

`Q_y(c+rho t)=sum_(d=0)^(q-1) b_d t^d`.

Because `D_beta` is invertible and `c` stays in a fixed positive compact range, the fixed-depth translation/rescaling map from `y` to `b` has smallest singular scale `rho^(q-1)`. Thus

`||b||_2 >= C rho^(q-1) ||y||_2`.

Multiplication by the sample values `x_m` is uniformly invertible because those values stay bounded away from zero. Hence the sampling result gives

`||A^* y||_2`
` >= C rho^(q-1) s_q(S_epsilon) ||y||_2`
` >= C' rho^(q-1) epsilon^(K_(q-1)) ||y||_2`.

For the matching upper bound, take the degree-`q-1` Newton witness

`P_epsilon(t)=N_(q-1)(t)`

and lift it to the original coordinate:

`Q_(rho,epsilon)(x)=rho^(q-1) P_epsilon((x-c)/rho)`
` = prod_(i=0)^(q-2) (x-c-rho t_i)`.

This polynomial is monic of fixed degree and its coefficient norm stays bounded above and below as `rho,epsilon->0`. It vanishes at the first `q-1` Wang sample points, while at the last one

`|Q_(rho,epsilon)(x_(q-1))|`
` = rho^(q-1) |d_(q-1)|`
` asymp rho^(q-1) epsilon^(K_(q-1))`.

After converting `x Q_(rho,epsilon)(x)` back to a normalized Wang row direction, this yields

`s_q(A) <= C rho^(q-1) epsilon^(K_(q-1))`.

Together with the lower bound,

`s_q(A) asymp rho^(q-1) epsilon^(K_(q-1))`.

## 4. What this closes and what remains

`VIS-363` prices one common inner scale by the weighted Hermite costs `a_ell+d`, assuming each local weighted cloud is healthy after that single rescaling. The chain above violates exactly that health hypothesis: after the first rescaling, the local cloud still contains a strictly finer collision.

The new point is that **a nested scale by itself is still not an unpriced cancellation resource**. For the canonical one-dimensional chain, every finite polynomially ordered layer is completely visible in the Newton pivots, and the smallest Wang singular scale is the product of the successive separation scales.

This sharpens the compact frontier in two ways.

First, the phrase “distinct nested inner scales” is too broad as an escape condition. A finite chain of nested positive scales is source-free conditioning geometry and can be charged exactly.

Second, a genuinely new recursive mechanism must do more than insert another smaller distance. It must involve geometry not reducible to this one-branch Newton ledger: for example branching cluster trees with competing local ranks and masses, recursively degenerate weighted clouds whose active subspaces change across levels, scale relations not controlled by a fixed finite valuation hierarchy, or a coefficient topology outside the positive diagonal Hilbert setting. Source-dependent signed arithmetic information remains a separate route and must still be proved at the source.

The result does not classify arbitrary recursive cluster trees. It gives a minimal exact benchmark that any claimed multiscale compact escape must beat.

## Prior-art audit

The underlying phenomenon is classical clustered-Vandermonde conditioning, not a new interpolation theorem. Stefan Kunis and Dominik Nagel, **On the smallest singular value of multivariate Vandermonde matrices with clustered nodes**, *Linear Algebra and its Applications* 604 (2020), 1–20, DOI `10.1016/j.laa.2020.06.003`, prove sharp univariate clustered-node bounds in terms of products of intracluster distances. For the present nested chain, that distance-product perspective already predicts the smallest exponent `K_(q-1)`.

Dmitry Batenkov, Benedikt Diederichs, Gil Goldman, and Yosef Yomdin, **The spectral properties of Vandermonde matrices with clustered nodes**, *Linear Algebra and its Applications* 609 (2021), 37–72, DOI `10.1016/j.laa.2020.08.034`, analyze all singular values of clustered Vandermonde systems and make local cluster geometry the controlling spectral datum. Dmitry Batenkov, Laurent Demanet, Gil Goldman, and Yosef Yomdin, **Conditioning of Partial Nonuniform Fourier Matrices with Clustered Nodes**, *SIAM Journal on Matrix Analysis and Applications* 41:1 (2020), 199–220, DOI `10.1137/18M1212197`, gives the corresponding sharp clustered-node conditioning boundary for partial Fourier/Vandermonde systems.

The displayed cumulative spectrum `K_r` is therefore recorded only as an elementary Newton-basis specialization for Mathia's maximally nested Wang chain. No novelty is claimed for clustered Vandermonde spectral theory itself.

## Dependencies

- `VIS-354`: the fixed-depth Wang tail coefficient map is a truncated inverse-scale Vandermonde map.
- `VIS-360`: pooled outer rescaling isolates the normalized polynomial-sampling Gram as the compact invariant.
- `VIS-361`: positive diagonal coefficient weights reduce conditioning to a weighted moment Gram.
- `VIS-362`: one common healthy inner scale prices a first outer rank collapse.
- `VIS-363`: polynomially vanishing masses on one healthy inner scale become additive weighted Hermite costs.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue narrowed by this recursive benchmark.

## Research consequence

A fixed-depth, one-branch hierarchy of polynomially nested positive scales is **fully priced by cumulative Newton separation exponents**. For nodes `0,epsilon^(kappa_1),...,epsilon^(kappa_(q-1))`, the full singular spectrum has exponents `0,K_1,...,K_(q-1)`, and the Wang floor pays `rho^(q-1) epsilon^(K_(q-1))`.

The compact frontier therefore moves from “any nested inner scale” to **recursive branching or weighted subspace degeneration not reducible to a single Newton chain**, or to a genuinely different coefficient/source topology. Merely stacking smaller positive separations does not create a new arithmetic cancellation mechanism.