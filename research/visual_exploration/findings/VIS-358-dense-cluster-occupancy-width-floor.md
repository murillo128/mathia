# VIS-358 — dense compact Wang clusters have an occupancy-width quotient scale

## Claim

Fix a finite Wang asymptotic depth `q>=1`, a cluster center `x_0>0`, and the invertible tail matrix

`D_beta=diag(beta_1,...,beta_q)`.

For `N>=2`, put

`t_(j,N)=-1+2(j-1)/(N-1)`, `1<=j<=N`,

and for `0<epsilon<=epsilon_0<x_0` define the distinct inverse scales

`x_(j,N,epsilon)=x_0+epsilon t_(j,N)`.

Let

`V_(N,epsilon)=(x_j^k)_(1<=k<=q,1<=j<=N)`,
`A_(N,epsilon)=D_beta V_(N,epsilon)`.

Then there exist constants `c,C>0`, `N_0`, and `epsilon_0>0`, depending only on `q`, `x_0`, and `D_beta`, such that for every `N>=N_0` and `0<epsilon<=epsilon_0`,

`c sqrt(N) epsilon^(q-1) <= s_q(A_(N,epsilon)) <= C sqrt(N) epsilon^(q-1)`.

Equivalently,

`lambda_min(A_(N,epsilon) A_(N,epsilon)^*) asymp N epsilon^(2(q-1))`.

Thus the compact anchor collapse classified by `VIS-357` does **not** imply collapse of the full rectangular quotient map. All `q`-column anchors lie inside an interval of width `2 epsilon`, hence their best anchor quality tends to zero as `epsilon->0` for `q>=2`; nevertheless growing occupancy repays that loss whenever

`N epsilon^(2(q-1))`

stays bounded below. In particular, choosing `N asymp epsilon^(-2(q-1))` keeps the full smallest positive singular value uniformly nonzero even though every fixed `q`-column anchor degenerates.

For `q=1`, the exponent is zero and `s_1(A_(N,epsilon)) asymp sqrt(N)`, consistent with the absence of a compact anchor-degeneration branch in `VIS-357`.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL POLYNOMIAL-SAMPLING/VANDERMONDE GEOMETRY + STRUCTURAL NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This finding proves the tradeoff for a canonical equally spaced one-cluster family under the current unweighted Euclidean coefficient norm. It does not classify arbitrary irregular clusters, several interacting clusters, weighted coefficient norms, or infinite-dimensional limits.

## 1. The full quotient singular value is a polynomial sampling problem

For `y in C^q`,

`||A_(N,epsilon)^* y||_2^2 = sum_(j=1)^N |p_y(x_j)|^2`,

where

`p_y(x)=sum_(k=1)^q conjugate(y_k) beta_k x^k`.

Since the constant term vanishes,

`p_y(x)=x Q_y(x)`

with `deg Q_y<=q-1`. Because `D_beta` is fixed and invertible, the coefficient norm of `Q_y` is uniformly equivalent to `||y||_2`.

Choose `epsilon_0` so that `x_0-epsilon_0>=x_0/2`. Then every sample satisfies `x_j>=x_0/2`, and therefore

`sum_j |p_y(x_j)|^2 >= (x_0/2)^2 sum_j |Q_y(x_j)|^2`.

So the only possible small direction is a degree-`q-1` polynomial sampled on a shrinking but increasingly dense cluster.

## 2. Rescaling the cluster exposes the `epsilon^(q-1)` jet cost

Write

`Q_y(x_0+epsilon t)=sum_(d=0)^(q-1) b_d t^d`.

If `a` is the coefficient vector of `Q_y` in the ordinary monomial basis, then

`b = D_epsilon T_(x_0) a`,

where

`D_epsilon=diag(1,epsilon,...,epsilon^(q-1))`

and `T_(x_0)` is the fixed invertible triangular translation matrix from monomials in `x` to Taylor coefficients at `x_0`. Hence, for `0<epsilon<=1`,

`||b||_2 >= c_0 epsilon^(q-1) ||a||_2 >= c_1 epsilon^(q-1) ||y||_2`.

This is the load-bearing collision scale. A nonzero polynomial `p_y(x)=xQ_y(x)` can vanish at the positive center `x_0` to order at most `q-1`; the worst direction is therefore a `(q-1)`-jet, not an arbitrarily flat mode.

## 3. Dense occupancy contributes the compensating `sqrt(N)` factor

Let

`S_N=(t_(j,N)^d)_(1<=j<=N,0<=d<=q-1)`.

Then

`sum_j |Q_y(x_j)|^2 = ||S_N b||_2^2`.

Because `q` is fixed and the grid `t_(j,N)` becomes uniformly distributed on `[-1,1]`,

`(1/N) S_N^* S_N`

converges entrywise to the positive-definite Gram matrix of the monomials `1,t,...,t^(q-1)` in `L^2([-1,1])`. Therefore there are `N_0` and `gamma_q>0` such that for every `N>=N_0`,

`||S_N b||_2^2 >= gamma_q N ||b||_2^2`.

Combining with the rescaling estimate gives, for every `||y||_2=1`,

`||A_(N,epsilon)^* y||_2^2 >= c N epsilon^(2(q-1))`.

Taking the infimum over unit `y` yields

`s_q(A_(N,epsilon)) >= c sqrt(N) epsilon^(q-1)`.

Thus many individually almost-collinear columns can still span the full `q`-dimensional row space stably because the small jet direction is sampled many times.

## 4. The exponent is sharp

Take the fixed polynomial

`p_0(x)=x(x-x_0)^(q-1)`.

It belongs to the admissible span `x,...,x^q`. Let `y_0` be the corresponding fixed nonzero coefficient vector after undoing `D_beta`, and normalize it to `||y_0||_2=1`.

For every cluster point,

`|p_0(x_j)| <= C_0 epsilon^(q-1)`.

Hence

`||A_(N,epsilon)^* y_0||_2^2 <= C N epsilon^(2(q-1))`,

which proves the matching upper bound

`s_q(A_(N,epsilon)) <= C sqrt(N) epsilon^(q-1)`.

The threshold is therefore not an artifact of the lower-bound argument: under this regular one-cluster geometry, the full quotient floor is controlled precisely by occupancy times the square of the deepest available cluster jet.

## 5. Relation to the square-anchor collapse

For the same bank, all inverse scales lie in an interval of diameter `2 epsilon`, so the best `q`-point packing separation from `VIS-357` obeys

`delta_q(X_(N,epsilon)) <= 2 epsilon`.

For `q>=2`, `VIS-357` therefore gives

`alpha_q(X_(N,epsilon))->0`

as `epsilon->0`: every fixed `q`-column square anchor degenerates.

The full rectangular map behaves differently:

- if `N epsilon^(2(q-1))->0`, then `s_q(A)->0`;
- if `N epsilon^(2(q-1)) asymp 1`, then `s_q(A) asymp 1`;
- if `N epsilon^(2(q-1))->infinity`, then the full quotient floor grows.

So **square-anchor degeneration is only a sufficient warning, not the compact escape itself**. The relevant full-map resource is the occupancy-width combination after the coefficient norm has been fixed.

This also makes the norm/topology caveat explicit. Reweighting columns or changing the coefficient norm changes the effective mass that replaces `N`; such a change is a real additional resource and must be stated rather than hidden inside “many scales.”

## Prior-art audit

The ingredients of the proof are classical finite-dimensional polynomial sampling and clustered Vandermonde conditioning. Dmitry Batenkov, Laurent Demanet, Gil Goldman, and Yosef Yomdin, **Conditioning of Partial Nonuniform Fourier Matrices with Clustered Nodes**, *SIAM Journal on Matrix Analysis and Applications* 41:1 (2020), 199–220, DOI `10.1137/18M1212197`, proves sharp smallest-singular-value bounds for rectangular Fourier/Vandermonde matrices with clustered nodes. Dmitry Batenkov, Benedikt Diederichs, Gil Goldman, and Yosef Yomdin, **The spectral properties of Vandermonde matrices with clustered nodes**, *Linear Algebra and Its Applications* 609 (2021), 37–72, DOI `10.1016/j.laa.2020.08.034`, develops the corresponding clustered spectral picture and shows that local cluster multiplicity governs singular-value scales.

Those papers study a different matrix orientation and harmonic/Vandermonde geometry, but they are the closest structural prior art: clustered-node singular values are controlled by collision scale together with the number of available samples/modes. No novelty is claimed for clustered Vandermonde asymptotics, monomial norm equivalence, Riemann-sum convergence of a fixed polynomial Gram matrix, or singular-value characterizations.

The Mathia-specific consequence is only the Wang-frontier bookkeeping: the compact branch left open by `VIS-357` cannot be treated as “anchor collapse implies quotient collapse.” In a regular dense cluster, occupancy can exactly repay the collision scale under the current Euclidean bank norm.

## Dependencies

- `VIS-354`: the fixed-depth Wang tail map is the truncated inverse-scale Vandermonde map.
- `VIS-356`: a surviving stable square anchor gives a full rectangular floor.
- `VIS-357`: loss of every square anchor inside compact scale geometry is exactly shrinking `q`-point packing.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue narrowed by this result.

## Research consequence

The canonical one-cluster compact loophole is now quantitatively priced. **A growing number of scales packed into a width `epsilon` does not create a small fixed-depth Wang quotient merely because every `q`-column anchor collapses; under regular occupancy and the current Euclidean normalization the full floor scales as `sqrt(N) epsilon^(q-1)`.**

Future compact-bank claims must therefore identify why their empirical cluster geometry evades this occupancy repayment: irregular scaled positions with a degenerating polynomial-sampling Gram, several clusters with an unresolved jet-allocation interaction, explicit column weights/norm changes, or another resource outside the current finite-dimensional model. Merely making the scale cloud denser around fewer centers is not enough.