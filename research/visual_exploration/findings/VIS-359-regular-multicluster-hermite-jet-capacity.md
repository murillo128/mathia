# VIS-359 — regular Wang multiclusters add Hermite-jet occupancy capacities

## Claim

Fix a finite Wang asymptotic depth `q>=1`, an invertible diagonal tail matrix

`D_beta=diag(beta_1,...,beta_q)`,

and distinct positive cluster centers

`0<r<=c_1<...<c_L<=R`.

For cluster `ell`, let

`x_(ell,j)=c_ell+epsilon_ell t_(ell,j)`, `1<=j<=N_ell`,

where `0<epsilon_ell<=epsilon_0`, and the normalized nodes `t_(ell,j)` form the equally spaced grid in `[-1,1]`. Let `V` be the `q x sum N_ell` matrix with column

`(x,x^2,...,x^q)^T`

at every sampled inverse scale, and put `A=D_beta V`.

Choose nonnegative integers `m_1,...,m_L` with

`sum_ell m_ell=q`.

Then, for sufficiently small fixed `epsilon_0` and sufficiently large fixed grid threshold `N_0`, there is a constant `C>0` depending only on `q`, the centers, `[r,R]`, and `D_beta` such that whenever every active cluster has `N_ell>=N_0`, one has

`s_q(A)^2 >= C min_(ell:m_ell>0) N_ell epsilon_ell^(2(m_ell-1))`.

Thus a cluster assigned `m_ell` Hermite conditions supplies those `m_ell` jets at the cost of its deepest admitted jet `N_ell epsilon_ell^(2(m_ell-1))`. Distinct clusters combine through ordinary Hermite interpolation: once the total supplied jet multiplicity reaches `q`, the full fixed-depth Wang quotient retains a positive floor.

Conversely, along any sequence `epsilon_ell->0`, if there are integers `r_ell>=1` with

`sum_ell r_ell <= q-1`

and

`N_ell epsilon_ell^(2 r_ell) -> 0`

for every cluster, then

`s_q(A)->0`.

The witness is the fixed polynomial

`Q(x)=prod_ell (x-c_ell)^(r_ell)`,

whose degree is at most `q-1`; the corresponding Wang polynomial `p(x)=xQ(x)` is simultaneously flat to the required order at every cluster center.

In the power-law regime

`N_ell asymp epsilon_ell^(-2 a_ell)`, `a_ell>=0`,

define the integer jet capacity

`kappa_ell=floor(a_ell)+1`.

Then the regular separated multicluster family has the exact fixed-depth dichotomy

- if `sum_ell kappa_ell >= q`, the smallest positive singular value is uniformly bounded below;
- if `sum_ell kappa_ell <= q-1`, the smallest positive singular value tends to zero.

So under the current unweighted Euclidean coefficient norm, each separated cluster supplies its value jet for free, and each additional factor `epsilon_ell^(-2)` of occupancy buys one further derivative jet. Regular multicluster geometry therefore does not create an unpriced compact escape: its entire fixed-depth conditioning budget is the additive Hermite-jet capacity.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL HERMITE/CONFLUENT-VANDERMONDE GEOMETRY + STRUCTURAL NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This finding treats regular equally spaced clusters with fixed separated centers and the current unweighted Euclidean bank norm. It does not classify arbitrary irregular point clouds, nonuniform column weights, centers whose separation also collapses, growing `q`, or infinite-dimensional coefficient topologies.

## 1. Each cluster is a scaled Taylor-sampling block

For `y in C^q`, write

`p_y(x)=sum_(k=1)^q conjugate(y_k) beta_k x^k=x Q_y(x)`,

where `deg Q_y<=q-1`. Because all centers remain in a fixed positive compact interval and `D_beta` is invertible, the coefficient norm of `Q_y` is uniformly equivalent to `||y||_2`.

At center `c_ell`, expand

`Q_y(c_ell+epsilon_ell t)=sum_(d=0)^(q-1) b_(ell,d) t^d`,

with

`b_(ell,d)=epsilon_ell^d Q_y^(d)(c_ell)/d!`.

Let `S_(N_ell)` be the normalized monomial sampling matrix on the equally spaced grid `t_(ell,j)`. As in `VIS-358`, fixed `q` gives a uniform polynomial-sampling Gram floor:

`||S_(N_ell) b_ell||_2^2 >= gamma_q N_ell ||b_ell||_2^2`

for all `N_ell>=N_0`. Since `x_(ell,j)` stays uniformly away from zero,

`sum_j |p_y(x_(ell,j))|^2 >= C N_ell sum_(d=0)^(q-1) epsilon_ell^(2d) |Q_y^(d)(c_ell)|^2`.

This is the multicluster analogue of the one-cluster occupancy-width law: the full rectangular Gram is a weighted sum of local Taylor-jet Grams.

## 2. Any `q` Hermite jets force a quotient floor

Fix multiplicities `m_ell` with total `q`. For `d<m_ell` and `epsilon_ell<=1`,

`N_ell epsilon_ell^(2d) >= N_ell epsilon_ell^(2(m_ell-1))`.

Hence the total sampling energy controls

`eta sum_ell sum_(d=0)^(m_ell-1) |Q_y^(d)(c_ell)|^2`,

where

`eta=min_(ell:m_ell>0) N_ell epsilon_ell^(2(m_ell-1))`.

The map

`Q -> (Q^(d)(c_ell))_(ell,0<=d<m_ell)`

from polynomials of degree at most `q-1` to `q` Hermite data is invertible because the centers are distinct and the total multiplicity is `q`. Equivalently, its matrix is a square confluent Vandermonde matrix. Since the centers are fixed, its inverse norm is a fixed constant. Therefore

`sum_ell sum_(d<m_ell) |Q_y^(d)(c_ell)|^2 >= C ||Q_y||_coeff^2 >= C' ||y||_2^2`.

Taking the infimum over unit `y` proves the lower bound for `s_q(A)^2`.

The important point is additive rather than multiplicative: different separated clusters need not each resolve all `q` jets. A cluster can supply only the first few local derivatives, and the resulting Hermite conditions from different centers jointly determine the degree-`q-1` polynomial.

## 3. A deficient total jet budget gives an explicit collapsing direction

Suppose integers `r_ell>=1` satisfy `sum r_ell<=q-1`. Then

`Q(x)=prod_ell (x-c_ell)^(r_ell)`

is a nonzero polynomial of degree at most `q-1`. After normalizing its fixed coefficient vector, the corresponding `p(x)=xQ(x)` gives an admissible unit direction in the Wang row space.

On cluster `ell`, all other center factors stay uniformly bounded while

`|Q(c_ell+epsilon_ell t)| <= C epsilon_ell^(r_ell)`.

Therefore

`sum_j |p(x_(ell,j))|^2 <= C N_ell epsilon_ell^(2r_ell)`.

If every term tends to zero, so does the total energy, proving `s_q(A)->0`.

This witness also shows why separated-cluster count matters. If there are at least `q` separated clusters, choose `m_ell=1` on any `q` of them: ordinary value interpolation already gives a uniform floor. Compact degeneration then requires fewer effective centers together with insufficient occupancy to buy the missing derivative jets.

## 4. Power-law occupancies give an exact capacity ledger

Assume `N_ell asymp epsilon_ell^(-2a_ell)`. Cluster `ell` can support any multiplicity

`m_ell<=floor(a_ell)+1=kappa_ell`

because then

`N_ell epsilon_ell^(2(m_ell-1))`

stays bounded below (and usually diverges unless `m_ell-1=a_ell`). If the total capacity is at least `q`, allocate exactly `q` jets across the clusters and apply the lower bound.

If instead `sum kappa_ell<=q-1`, choose `r_ell=kappa_ell`. Since `kappa_ell>a_ell`,

`N_ell epsilon_ell^(2kappa_ell) asymp epsilon_ell^(2(kappa_ell-a_ell))->0`.

The collapsing polynomial from the previous section applies. This proves the dichotomy without an intermediate ambiguous regime.

The ledger is therefore concrete: cluster `ell` contributes `1+floor(a_ell)` stable Hermite conditions. A multicluster bank can lose the fixed-depth quotient floor only when the total purchased jet capacity remains below the polynomial dimension `q`.

## Prior-art audit

The mathematical ingredients are classical Hermite interpolation and clustered Vandermonde conditioning. Hermite interpolation at distinct centers with prescribed derivative multiplicities is exactly the confluent-Vandermonde problem; no novelty is claimed for uniqueness/invertibility of that map. Hao Lu, **Fast Solution of Confluent Vandermonde Linear Systems**, *SIAM Journal on Matrix Analysis and Applications* 15:4 (1994), 1277–1289, DOI `10.1137/S089547989324416X`, is a standard confluent-Vandermonde/Hermite reference.

The closest conditioning literature remains the clustered Vandermonde/Fourier work already used by `VIS-358`: Dmitry Batenkov, Laurent Demanet, Gil Goldman, and Yosef Yomdin, **Conditioning of Partial Nonuniform Fourier Matrices with Clustered Nodes**, *SIAM Journal on Matrix Analysis and Applications* 41:1 (2020), 199–220, DOI `10.1137/18M1212197`, and Dmitry Batenkov, Benedikt Diederichs, Gil Goldman, and Yosef Yomdin, **The spectral properties of Vandermonde matrices with clustered nodes**, *Linear Algebra and Its Applications* 609 (2021), 37–72, DOI `10.1016/j.laa.2020.08.034`. Those works show that local cluster multiplicity and geometry govern singular-value scales and that separated clusters admit a blockwise spectral description.

The Mathia-specific content is only the exact bookkeeping for the fixed-depth Wang tail map: regular cluster occupancies translate into additive Hermite-jet capacities, giving a sharp source-free criterion for when separated compact multiclusters can or cannot collapse the quotient floor.

## Dependencies

- `VIS-354`: the fixed-depth Wang tail coefficient map is the truncated inverse-scale Vandermonde map.
- `VIS-357`: loss of every stable square anchor is shrinking compact cluster geometry.
- `VIS-358`: one regular dense cluster has quotient scale `sqrt(N) epsilon^(q-1)`.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue narrowed by this result.

## Research consequence

The regular separated multicluster branch is now priced. **At fixed asymptotic depth and fixed positive separated centers, occupancy does not create a mysterious collective cancellation resource: it buys local Hermite jets, and those jet counts add across clusters until the degree-`q-1` polynomial is determined.**

A remaining compact-bank escape must therefore use geometry outside this theorem: irregular sampling whose scaled local Gram degenerates despite its nominal occupancy, nonuniform weights or a changed coefficient norm, collapsing center separations that merge the Hermite blocks, or another resource outside the regular fixed-depth Euclidean model. Power-law occupancy in regular separated clusters is no longer an open loophole.