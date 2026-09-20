# MC-422 — Thin hyperbolic shells tax coordinate-factor translation bandwidth

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-421` leaves open a genuinely rank-two arithmetic lift **before** positive quadratic closure. Classical short-interval decompositions do create many pre-quadratic factor coordinates. In particular, the Ramaré/Heath-Brown decomposition used by Matomäki–Teräväinen rewrites a short Möbius sum into dyadically localized products of variables subject to one thin product constraint of the form

\[
X< u_1u_2\cdots u_d\le X+\Delta.
\tag{1}
\]

Those factor coordinates are algebraically genuine, but `(1)` does **not** supply a free rectangular translation lattice. The short-interval support itself imposes a quantitative bandwidth tax.

Let `U_j>0`, `B_j\ge0`, and suppose the full positive coordinate box

\[
\mathcal B=\prod_{j=1}^d[U_j,U_j+B_j]
\tag{2}
\]

has all of its product values inside an interval of width `\Delta`. Put

\[
P_0:=\prod_{j=1}^dU_j.
\tag{3}
\]

Because the product is coordinatewise increasing,

\[
\prod_{j=1}^d(U_j+B_j)-P_0\le\Delta.
\tag{4}
\]

Writing `t_j=B_j/U_j`, expansion of the left side gives

\[
\prod_{j=1}^d(1+t_j)-1
\ge
\sum_{j=1}^dt_j,
\tag{5}
\]

hence the exact necessary condition

\[
\boxed{
\sum_{j=1}^d\frac{B_j}{U_j}
\le
\frac{\Delta}{P_0}.
}
\tag{6}
\]

AM–GM therefore gives the bandwidth-volume bound

\[
\boxed{
\prod_{j=1}^d B_j
\le
\frac{\Delta^d}{d^dP_0^{d-1}}.
}
\tag{7}
\]

When `P_0\asymp X` and `\Delta=X^\theta`, this becomes

\[
\boxed{
\prod_{j=1}^d B_j
\ll_d
X^{\,1-d(1-\theta)}.
}
\tag{8}
\]

Thus a **full coordinate-axis translation box with growing lattice volume** is possible only beyond the elementary threshold

\[
\boxed{
\theta>1-\frac1d.
}
\tag{9}
\]

This directly limits the naive continuation of the `MC-419` tensorized-Fejér escape. More formal factor variables do not automatically mean more usable stationary translation rank. In the endpoint regime `\theta=0.55+o(1)` reached by Matomäki–Teräväinen, two coordinate axes can have at most total bandwidth volume `\ll X^{0.10+o(1)}`, while three simultaneously growing coordinate axes already fail the threshold because `0.55<2/3`.

The geometric reason is clearer in logarithmic factor coordinates `y_j=\log u_j`. The shell `(1)` becomes the exact slab

\[
\log X<\sum_{j=1}^dy_j
\le
\log X+\log\!\left(1+\frac{\Delta}{X}\right).
\tag{10}
\]

So the product condition leaves a `(d-1)`-dimensional tangent geometry but only a very thin normal direction of width `\asymp\Delta/X` when `\Delta=o(X)`. Independent **additive coordinate shifts** point partly in that expensive normal direction. A successful multi-axis escape therefore has to exploit tangent or product-preserving structure, boundary-aware correlations, or a nonstationary/sheared geometry; it cannot credit every extracted factor as an independent rectangular Fejér bandwidth.

The correct negative conclusion is limited:

> Ramaré/Heath-Brown factor extraction does create multiple pre-quadratic arithmetic coordinates, but a short product shell couples them strongly enough that a support-preserving positive coordinate box has bandwidth volume at most `\Delta^d/(d^dP_0^{d-1})`. Consequently, factor count by itself is not the effective translation rank relevant to the positive-kernel escape of `MC-419`–`MC-421`.

This does **not** rule out tilted lattices, multiplicative redistributions of factors, zero-extended correlations, hyperbola-adapted partitions, or estimates that tolerate substantial boundary loss. It identifies the geometric obligation that such an escape must beat.

No improved Möbius estimate, character-sum estimate, source-depth exponent, Mertens bound, or RH consequence follows.

## 1. Exact coordinate-box bound

For positive coordinates, the product map is monotone on `(2)`. Its minimum and maximum on the box are therefore

\[
P_{\min}=P_0,
\qquad
P_{\max}=\prod_{j=1}^d(U_j+B_j).
\tag{11}
\]

If the whole box lies in any product shell of width `\Delta`, necessarily `P_{\max}-P_{\min}\le\Delta`. Dividing by `P_0` gives

\[
\prod_{j=1}^d(1+t_j)-1\le\frac{\Delta}{P_0}.
\tag{12}
\]

All mixed terms in the product are nonnegative, so

\[
\sum_jt_j\le\prod_j(1+t_j)-1.
\tag{13}
\]

This proves `(6)`. Applying AM–GM to the nonnegative `t_j` gives

\[
\prod_{j=1}^dt_j
\le
\left(\frac1d\sum_{j=1}^dt_j\right)^d
\le
\left(\frac{\Delta}{dP_0}\right)^d.
\tag{14}
\]

Multiplication by `P_0=\prod U_j` proves `(7)`.

The same estimate applies to any chosen subset of `r` active coordinate directions after freezing the remaining factors: replace `d` by `r` and absorb the frozen product into `P_0`. Hence the obstruction is about the number of **simultaneously translated factor axes**, not the total number of formal variables in a decomposition.

The estimate is deliberately generous. In an arithmetic decomposition some coordinates may be prime-supported, square-free-supported, or carry short coefficient sequences; a literal integer rectangle need not exist at all. The inequality ignores those additional restrictions and therefore cannot be blamed on arithmetic sparsity.

## 2. Why Ramaré/Heath-Brown supplies the right stress test

Kaisa Matomäki and Joni Teräväinen, *On the Möbius function in all short intervals*, J. Eur. Math. Soc. **25** (2023), 1207–1225, DOI `10.4171/JEMS/1205`, proves cancellation in every interval of length `X^\theta` for `\theta>0.55`. Its main new device is Ramaré's identity, used to extract a small prime factor before applying a Heath-Brown decomposition.

Their Lemma 3.1 rewrites the short Möbius sum, up to a controlled sieve error, in terms of variables `p,r,n` with a small prime `p` and the product restricted by `X<prn\le X+\Delta`. Section 4 then applies Heath-Brown's identity and dyadic subdivision, producing sums of the form

\[
X<prn_1\cdots n_{2k-1}\le X+\Delta
\tag{15}
\]

with each variable localized to its own dyadic range. This is exactly the kind of pre-quadratic factor lift that `MC-421` leaves open: several arithmetic coordinates exist before any Cauchy/positive closure is applied.

The present finding shows why the existence of those coordinates is not yet the `MC-419` escape. Their support remains one thin hyperbolic shell. If one tries to assign independent stationary additive shift bandwidths directly to `p,r,n_1,\ldots`, the full coordinate box must obey `(7)`. Increasing the number of active axes eventually makes the available rectangular bandwidth volume **smaller**, not larger, at a fixed short-interval exponent.

For example, at `\Delta=X^{0.55+o(1)}` and `P_0\asymp X`,

\[
B_1B_2\ll X^{0.10+o(1)},
\tag{16}
\]

whereas

\[
B_1B_2B_3\ll X^{-0.35+o(1)}.
\tag{17}
\]

The second display means that a full three-axis integer box with every `B_j\ge1` cannot persist asymptotically at this scale. It does **not** mean that a three-factor decomposition is useless: the useful geometry, if any, must be nonrectangular or must allow boundary crossings.

## 3. The shell has tangent dimension, not free coordinate rank

Equation `(10)` exposes the missing distinction. In log coordinates, a product shell is a thin slab around the hyperplane

\[
\sum_jy_j=\log X.
\tag{18}
\]

The tangent space has dimension `d-1`. Infinitesimally, a perturbation `\delta u` is tangent at `u` when

\[
\sum_{j=1}^d\frac{\delta u_j}{u_j}=0.
\tag{19}
\]

For two factors this is the familiar first-order condition

\[
v\,\delta u+u\,\delta v=0.
\tag{20}
\]

So mixed-sign or multiplicative redistribution directions can avoid the first-order normal cost that forces `(6)`. This is a real escape from the coordinate-box obstruction.

But it comes with a new structural requirement. The tangent direction depends on the base point in the original additive coordinates, while `MC-419`–`MC-420` concern genuine stationary translation lattices and their Fourier support. A fixed additive direction that is tangent near one point drifts away from the hyperbola elsewhere; an exactly product-preserving motion is naturally multiplicative rather than additive. Any proposed rank-two lift must therefore show how its source phase, sieve coefficients, and reconstruction formula transform under the chosen shear or multiplicative redistribution. Merely drawing two tangent coordinates locally is not enough.

This suggests the sharper continuation of the frontier: **search for source-compatible fixed or piecewise-fixed tangent translations whose localization cost is smaller than the coordinate bandwidth tax**.

## 4. Prior art and novelty boundary

The product-shell geometry is classical and no novelty is claimed for `(6)`–`(10)`. Matomäki–Teräväinen's 2023 paper is primary prior art for the exact Möbius factorization that motivates the test; the paper itself treats the hyperbolic product restriction as a central part of the Dirichlet-polynomial analysis rather than as a free tensor product.

A second adjacent reference is Cameron Wilson, *General bilinear forms in the Jacobi symbol over hyperbolic regions*, Monatshefte für Mathematik **202** (2023), 435–451, DOI `10.1007/s00605-023-01848-9`, arXiv:`2208.14909`. Wilson studies bilinear character sums under a bounded-product condition and, in the proof of the main hyperbolic-region estimate, explicitly covers portions of the hyperbolic region by rectangles before applying rectangular bilinear bounds. This is a useful prior-art boundary: modern character-sum arguments already treat the hyperbolic support geometry as an analytic cost that must be localized, not as an automatically independent pair of variables.

A targeted literature audit on 20 September 2026 found these established hyperbolic-region and short-interval mechanisms but no basis for claiming novelty for the elementary bandwidth-volume inequality itself. The Mathia contribution is its use as a **frontier admission test** connecting the classical pre-quadratic factor lift to the effective-rank requirement isolated in `MC-419`–`MC-421`.

## Boundaries and falsification tests

- **Only a full coordinate-axis box is bounded by `(7)`.** A tilted parallelogram, curved patch, sparse shift set, or multiplicative orbit can evade the positive-corner argument.
- **Support preservation is stronger than nonempty overlap.** Van der Corput on a zero-extended sequence may use shifts that leave the shell; then the correlation survives only on the overlap. Such a method is outside the literal box hypothesis, but its useful bandwidth must be recomputed after the overlap/boundary loss rather than credited for free.
- **A tangent escape is genuinely open.** Mixed-sign directions can cancel first-order product drift. They must be tested for stationarity, integer/arithmetic realizability, source-phase retention, and curvature/localization cost.
- **The threshold `(9)` is not a universal short-interval barrier.** It is only the threshold for growing volume of a support-preserving coordinate rectangle. Matomäki–Teräväinen themselves beat much cruder rectangle reasoning by combining factorization with Dirichlet-polynomial estimates.
- **The factor variables are not assumed independent probabilistically.** The obstruction is deterministic geometry of the product support.
- **Prime-supported coordinates only make the rectangle model less automatic.** The proof does not use primality, so it cannot establish a Möbius-specific impossibility by itself.
- **No zero information is imported.** The derivation of `(6)`–`(10)` is finite elementary geometry; the literature is used only to identify an authentic Möbius factorization and an established hyperbolic-region analytic boundary.

## Consequence for the research line

`MC-421` asked whether the source can create at least two independent translation directions before positive closure. The answer now splits into two different notions of independence.

Classical factorization gives **algebraically independent factor coordinates** immediately. What it does not give is an unconstrained stationary additive translation box: one normal degree of freedom is compressed by the short product shell, and `(7)` quantifies the resulting coordinate bandwidth budget. Therefore a direct tensorization over extracted factors cannot be justified by factor count alone.

The next decisive test is the remaining tangent possibility. Start from a concrete two-factor or three-factor dyadic component of the Ramaré/Heath-Brown representation and construct the largest **fixed rank-two tilted lattice or multiplicative redistribution family** for which the shell overlap remains macroscopic. Then propagate its exact source phase and sieve weights through one quadratic closure. If its effective lattice volume beats the coordinate bound `(7)` after localization and boundary costs, it is a genuine `MC-419` escape. If every source-compatible tangent lift collapses to rank one or pays an equivalent curvature/localization tax, the pre-quadratic multi-factor route narrows again.