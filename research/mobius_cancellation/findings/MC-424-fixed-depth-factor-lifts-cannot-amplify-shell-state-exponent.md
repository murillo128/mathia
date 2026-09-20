# MC-424 — Fixed-depth factor lifts cannot amplify the shell state exponent

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-422` bounds full coordinate-axis boxes inside a thin product shell, while `MC-423` bounds one exact-product tangent fiber. The remaining near-tangent possibility can be bounded without choosing coordinates, a shear, or a lattice shape.

For an integer depth `d>=2`, define the complete ordered factor-state shell

\[
\mathcal S_d(X,\Delta)
:=
\left\{(u_1,\ldots,u_d)\in\mathbb N^d:
X<u_1\cdots u_d\le X+\Delta\right\},
\qquad 1\le\Delta\le X.
\tag{1}
\]

Let `d_d(n)` be the ordered `d`-fold divisor function. Grouping tuples by their product gives the exact identity

\[
\boxed{
|\mathcal S_d(X,\Delta)|
=
\sum_{X<n\le X+\Delta} d_d(n).
}
\tag{2}
\]

For every fixed `d`, the classical maximal-order bound `d_d(n)=n^{o(1)}` therefore implies

\[
\boxed{
|\mathcal S_d(X,\Delta)|
\le (\lfloor\Delta\rfloor+1)X^{o(1)}.
}
\tag{3}
\]

The opposite exponent bound is elementary: for every integer `n` in the shell, the tuple `(n,1,\ldots,1)` belongs to `\mathcal S_d(X,\Delta)`. Hence, whenever

\[
\Delta=X^{\theta+o(1)},\qquad 0<\theta\le1,
\tag{4}
\]

one has

\[
\boxed{
|\mathcal S_d(X,\Delta)|=X^{\theta+o(1)}.
}
\tag{5}
\]

Thus **fixed-depth factorization does not amplify the polynomial state-space exponent of a short product shell**. The shell may have many tangent directions geometrically, but all ordered factorizations over all products in the shell together contain only the shell-length exponent `theta`, up to subpolynomial multiplicity.

Consequently, any support-preserving arithmetic realization of a positive-kernel bandwidth family by distinct factor states satisfies

\[
V_{\mathrm{eff}}
\le |\mathcal S_d(X,\Delta)|
=X^{\theta+o(1)}
\tag{6}
\]

at fixed depth. Combined only as a **necessary state-count condition** with the tensorized Fejér floor of `MC-419`, this means that such a factor lift cannot justify a normalized diagonal improvement beyond `X^{-\theta-o(1)}` merely by declaring more factor coordinates, tilting the lattice, or replacing a rectangle by an arbitrary injective family inside the same shell.

The same count quantifies the growing-depth escape. Norton’s maximal-order theorem, as summarized and extended in Pollack’s work on the `k`-fold divisor function, gives in the regime

\[
d=d(X)=o(\log X)
\tag{7}
\]

the upper-bound scale

\[
\log d_d(n)
\le
(1+o(1))\log d\,\frac{\log n}{\log\log n}.
\tag{8}
\]

Uniformly for `X<n\le2X`, `(2)` therefore yields

\[
\boxed{
|\mathcal S_d(X,\Delta)|
\le
(\Delta+1)
X^{(1+o(1))\frac{\log d}{\log\log X}}.
}
\tag{9}
\]

In particular, if `\Delta=X^{\theta+o(1)}` and a proposal needs an additional fixed state-volume exponent `delta>0` beyond `theta`, then this route can supply it only if

\[
\boxed{
d\ge (\log X)^{\delta-o(1)}}
\tag{10}
\]

within the range where `(8)` applies. Constant depth, or more generally `d=(\log X)^{o(1)}`, contributes only `X^{o(1)}` extra state multiplicity.

This does **not** rule out analytic cancellation obtained from the weights on those states, zero-extended correlations whose parameter family is not an orbit inside the shell, transformed nonseparable phases, or genuinely growing-depth decompositions. It closes only the idea that fixed-depth factor coordinates themselves can manufacture a larger polynomial number of independent arithmetic cells than the short shell already contains.

No improved Möbius estimate, character-sum estimate, source-depth exponent, Mertens bound, or RH consequence follows.

## 1. The whole shell is a disjoint union of exact-product fibers

For each integer `n`, `MC-423` identifies the exact fiber

\[
\mathcal F_d(n)
=
\{(u_1,\ldots,u_d):u_1\cdots u_d=n\}
\tag{11}
\]

with cardinality `d_d(n)`. Since distinct products give disjoint fibers,

\[
\mathcal S_d(X,\Delta)
=
\bigsqcup_{X<n\le X+\Delta}\mathcal F_d(n),
\tag{12}
\]

which proves `(2)`.

For fixed `d`, `MC-423` records the classical bound `d_d(n)=n^{o(1)}`. Because `\Delta\le X`, every product in `(12)` is at most `2X`; hence for every fixed `epsilon>0` and all sufficiently large `X`,

\[
d_d(n)\le X^\epsilon
\qquad(X<n\le X+\Delta),
\tag{13}
\]

up to an inessential fixed constant absorbed in `X^\epsilon`. Summing `(13)` over at most `\lfloor\Delta\rfloor+1` possible products proves `(3)`.

Conversely, one ordered factorization exists for every product value: `(n,1,\ldots,1)`. Thus

\[
|\mathcal S_d(X,\Delta)|
\ge
\#\{n\in\mathbb N:X<n\le X+\Delta\}
=\Delta+O(1).
\tag{14}
\]

Equations `(3)` and `(14)` give `(5)` when `\Delta` has a positive polynomial exponent.

The upper bound is deliberately generous. A concrete Ramaré/Heath-Brown component generally imposes dyadic boxes, prime support, square-free support, coefficient support, or ordering restrictions, all of which can only shrink the available state set.

## 2. Coordinate changes cannot create missing states

The point of `(5)` is not a sharper divisor estimate. It removes the coordinate dependence left between `MC-422` and `MC-423`.

`MC-422` shows that a full axis-aligned box is expensive because it moves in the thin normal direction of the hyperbolic shell. `MC-423` then shows that exact tangent redistribution inside one product fiber has only subpolynomially many states. A proposed shear, tilted lattice, curved patch, multiplicative redistribution, or piecewise tangent chart can interpolate between those two extremes, but if every parameter value is represented by a **distinct ordered factor tuple that remains in the same shell**, its effective number of arithmetic cells is bounded by the cardinality of the entire shell `(2)`.

Therefore no reparameterization of fixed-depth factor tuples can turn a shell of width `X^theta` into `X^{theta+delta}` distinct support-preserving states for fixed `delta>0`. Colliding parameter labels do not help: as in the effective-rank principle of `MC-420`, labels that represent the same arithmetic state must be quotiented before they are credited as independent bandwidth cells.

This is stronger than the rectangular bound in one narrow sense and weaker in another. It applies to **arbitrary injective state families**, not only boxes, but it gives only a total-cardinality exponent. It does not determine whether those states form a stationary translation action, whether their Fourier frequencies are independent, or whether a positive kernel can reconstruct the desired Möbius observable. Those additional requirements can only reduce the usable bandwidth further.

## 3. Growing factor depth has a quantifiable state-volume price

The fixed-depth conclusion leaves the possibility already noted in `MC-423`: let the number of factor coordinates grow with `X`.

Pollack defines `d_k(n)` as the number of ordered products of `k` positive integers and records the classical Norton regime

\[
\log d_k(n)
\le
(1+o(1))\log k\,\frac{\log n}{\log\log n}
\qquad(k=o(\log n)).
\tag{15}
\]

Applying `(15)` to every fiber in `(12)` gives `(9)`. This converts “growing depth might help” into a quantitative admission test.

For example, if

\[
d=(\log X)^{\alpha+o(1)},\qquad 0<\alpha<1,
\tag{16}
\]

then

\[
|\mathcal S_d(X,\Delta)|
\le
X^{\theta+\alpha+o(1)}.
\tag{17}
\]

So an extra polynomial exponent can indeed become combinatorially available, but only after factor depth itself reaches a corresponding polylogarithmic scale. Any such proposal must then pay the actual cost of producing, weighting, and controlling that many factor coordinates; `(17)` supplies no analytic theorem that those states can be used coherently.

## 4. Prior art and novelty boundary

The identities `(2)` and `(12)` are standard divisor-function counting, and no novelty is claimed for them. Paul Pollack, *The maximal size of the k-fold divisor function for very large k*, Journal of the Ramanujan Mathematical Society **35** (2020), 341–345, defines `d_k(n)` as ordered `k`-factor representations and records that Norton’s classical maximal-order formula `(15)` holds for `k=o(log n)`. `MC-423` already uses the same source to bound one exact-product fiber.

The new content here is only the **frontier consequence** obtained by summing those classical fiber bounds across the whole short product shell: at fixed depth, the entire near-tangent state space has the same polynomial exponent as the shell width itself, independent of how it is parameterized. The growing-depth version `(9)` similarly translates the classical `d_k` maximal order into an explicit cost for any attempt to gain state exponent through additional factor coordinates.

A targeted literature audit also checked short-interval divisor-function work. Such literature studies finer averages and fluctuations of `d_k` in short intervals; none is needed for `(3)`, whose deliberately crude maximal-order bound is stronger for the present **worst-case state-count admission test** because it is unconditional for every shell location. No novelty is claimed for short-interval divisor estimates themselves.

## Boundaries and falsification tests

- **Fixed depth is load-bearing for `(5)`.** Growing depth is governed only by the separate estimate `(9)` in its stated range.
- **Support-preserving state realization is load-bearing for `(6)`.** Zero-extended van der Corput shifts may leave the shell and still produce nonzero overlap correlations; their parameter count is not bounded merely by `|\mathcal S_d|`.
- **State count is not Fourier rank.** Having `V` states is necessary but not sufficient for `V` independent stationary translation cells. The finding supplies an upper bound, not a construction.
- **A decomposition may carry extra labels not determined by the ordered factor tuple.** Genuine conductor, residue, interval-position, or transformed phase data must be counted separately if it survives exact quotienting. Merely renaming the same tuple does not qualify.
- **Weights can matter without increasing state count.** Oscillatory coefficients on `\mathcal S_d` may yield analytic cancellation that cardinality alone cannot see. This result does not bound such cancellation.
- **The lower bound in `(14)` concerns the unrestricted shell.** A specific dyadic/prime-supported component may have many fewer states; only the upper bound transfers automatically to every subset.
- **The Norton/Pollack estimate must be used only in its stated growth regime.** Nothing here extrapolates `(9)` to `d` comparable with or larger than `log X`.
- **No zero information is imported.** The derivation uses finite factor counting and classical divisor-function maximal order only.

## Consequence for the research line

The pre-quadratic factor-lift frontier is now narrower. `MC-422` rules out crediting nominal coordinate rank as a free rectangular bandwidth, and `MC-423` rules out obtaining polynomial volume from one exact tangent fiber at fixed depth. `MC-424` shows that allowing **all nearby fibers and arbitrary support-preserving reparameterizations still cannot amplify the shell exponent at fixed depth**: the complete factor-state shell itself has only `X^{theta+o(1)}` states when its product width is `X^{theta+o(1)}`.

The next live escape therefore needs more than geometric cleverness with a fixed number of factor coordinates. It must either obtain an analytic gain from structured weights on this bounded state set, use a transformed phase or extra arithmetic variable not determined by the factor tuple, tolerate boundary-crossing correlations in a way that changes the count, or increase factor depth enough that `(9)` allows genuinely new polynomial state volume and then pay the resulting decomposition/source costs explicitly.