# MC-421 — Iterated positive differencing creates source-free diagonal faces

**Status:** `EXACT-DERIVED` · `CLASSICAL-IDENTITY` · `LITERATURE+DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-420` leaves genuine independent translation directions as a possible way around the one-dimensional positive-kernel Fejér floor. The most immediate way to manufacture a second shift variable is to iterate additive van der Corput/Cauchy–Schwarz. That does create a genuine higher-dimensional cube, but it also creates a larger degeneracy set than the single zero mode of a quadratic kernel.

For a finitely supported complex sequence `a : Z -> C`, define the multiplicative derivative

\[
\Delta_h f(n):=f(n+h)\overline{f(n)}
\tag{1}
\]

and recursively

\[
D_r(n;h_1,\ldots,h_r)
:=\Delta_{h_r}\cdots\Delta_{h_1}a(n).
\tag{2}
\]

The derivatives commute. Therefore, on **every coordinate hyperplane** `h_j=0`,

\[
\boxed{
D_r(n;h_1,\ldots,h_{j-1},0,h_{j+1},\ldots,h_r)
=
\left|D_{r-1}(n;h_1,\ldots,\widehat{h_j},\ldots,h_r)\right|^2
\ge0.
}
\tag{3}
\]

Thus a new shift axis obtained by ordinary positive differencing always comes with a codimension-one diagonal face, not merely the single all-zero point. With the usual Fejér weight

\[
W_H(h):=(H-|h|)_+,
\qquad
\sum_hW_H(h)=H^2,
\tag{4}
\]

the normalized coefficient mass of the face `h_j=0` is

\[
\boxed{
\frac{W_{H_j}(0)}{\sum_hW_{H_j}(h)}=\frac1{H_j}.
}
\tag{5}
\]

So the formal `1/(H_1\cdots H_r)` weight of the all-zero corner is not the relevant first obstruction for an iterated van-der-Corput cube. Each coordinate-zero face appears already at reciprocal **one-axis** scale `1/H_j` and contains a lower-order squared energy.

For the current source-frame sequence

\[
a_n=w(n)\chi(n),
\tag{6}
\]

where `chi` is a primitive Dirichlet character, `(3)` has a stronger consequence. Since

\[
|\chi(m)|^2=\mathbf 1_{(m,q)=1},
\tag{7}
\]

all source-character phase disappears on a coordinate-zero face:

\[
\boxed{
|D_{r-1}(n;\mathbf h)|^2
=
\prod_{\omega\in\{0,1\}^{r-1}}
|w(n+\omega\cdot\mathbf h)|^2
\mathbf 1_{(n+\omega\cdot\mathbf h,q)=1}.
}
\tag{8}
\]

At depth two this becomes especially concrete. Put

\[
Q_{h,k}
:=
\sum_n
 a_{n+h+k}\overline{a_{n+h}}
 \overline{a_{n+k}}a_n.
\tag{9}
\]

Then

\[
\boxed{
Q_{h,0}
=
\sum_n |a_{n+h}|^2|a_n|^2
\ge0.
}
\tag{10}
\]

The whole `k=0` face has an exact positive sliding-window form:

\[
\boxed{
\sum_hW_H(h)Q_{h,0}
=
\sum_t
\left(\sum_{j=0}^{H-1}|a_{t+j}|^2\right)^2.
}
\tag{11}
\]

If `a` is supported in `[1,N]`, Cauchy–Schwarz gives the quantitative floor

\[
\boxed{
\sum_hW_H(h)Q_{h,0}
\ge
\frac{H^2}{N+H-1}
\left(\sum_n|a_n|^2\right)^2.
}
\tag{12}
\]

If a second Fejér parameter `K` is used in the `k`-variable, the normalized `k=0` face therefore contributes

\[
\frac{1}{H^2K}
\sum_hW_H(h)Q_{h,0}
\ge
\boxed{
\frac{1}{K(N+H-1)}
\left(\sum_n|a_n|^2\right)^2
}
\tag{13}
\]

before any off-face cancellation is used.

For the linear-sieve weight of `MC-409`–`MC-415`,

\[
w(n)=\sum_{d\mid n}\lambda_d,
\qquad
|w(n)|^2=\sum_{\ell\mid n}C_\lambda(\ell),
\tag{14}
\]

so `(10)` is a product of two copies of the lcm-incidence square from `MC-415`:

\[
Q_{h,0}
=
\sum_n
\sum_{\ell_1\mid n+h}C_\lambda(\ell_1)
\sum_{\ell_2\mid n}C_\lambda(\ell_2)
\mathbf 1_{(n(n+h),q)=1}.
\tag{15}
\]

At the intersection `h=k=0` this specializes to `sum_n |w(n)|^4 |chi(n)|^4`. Hence iterating ordinary positive differencing does not simply turn the `MC-420` rank-one quadratic closure into a cost-free rank-two escape. The extra axis is obtained by increasing correlation order, and its coordinate-zero face is source-phase-free and already contains the re-squared sieve energy.

The correct negative conclusion is limited:

> ordinary iterated positive van der Corput does not earn a tensorized diagonal saving merely by introducing more shift variables. At every new shift coordinate it also introduces a codimension-one source-free diagonal face with normalized kernel weight `1/H_j`. A successful higher-order route must control or exploit cancellation against these faces while retaining the off-face arithmetic structure; counting only the all-zero corner gives a false accounting of the positive cost.

This does **not** rule out higher-order differencing, Gowers-type methods, dispersion, or source-specific estimates. Off-face terms can cancel diagonal faces inside the exact positive energy, and deep higher-order information may make that cancellation provable. The finding identifies the additional obligation; it does not prove that the obligation is impossible.

No improved character-sum estimate, source-depth exponent, Mertens bound, or RH consequence follows.

## 1. Coordinate-zero faces are exact squares

Equation `(3)` is immediate from the derivative algebra. Since

\[
\Delta_0 f(n)=f(n)\overline{f(n)}=|f(n)|^2,
\tag{16}
\]

and the operators `Delta_h` commute,

\[
D_r
=
\Delta_{h_j}
\prod_{i\ne j}\Delta_{h_i}a.
\tag{17}
\]

Setting `h_j=0` proves `(3)`.

Equivalently, the explicit `r`-cube product contains `2^r` vertices. When one shift vanishes, opposite vertices in that coordinate coincide and pair into absolute squares. This is the standard degeneracy of the cube underlying repeated Cauchy–Schwarz and Gowers uniformity norms.

The Fejér coefficient statement `(5)` is equally exact: `W_H(0)=H` whereas `sum_h W_H(h)=H^2`. The point is not that the face is necessarily `1/H` of the **final numerical energy**—off-face terms may have either sign before the full positive combination is formed. Rather, the positive differencing architecture assigns a codimension-one degenerate family coefficient mass `1/H`, so any argument that majorizes off-face correlations termwise must pay that face explicitly.

## 2. The second-difference face is a positive energy of `|a|^2`

For `r=2`, direct expansion gives `(9)`. Setting `k=0` yields `(10)`.

Let

\[
b_n:=|a_n|^2\ge0.
\tag{18}
\]

Then the left side of `(11)` is

\[
\sum_hW_H(h)\sum_n b_{n+h}b_n.
\tag{19}
\]

Expanding a sliding-window square gives

\[
\begin{aligned}
\sum_t\left(\sum_{j=0}^{H-1}b_{t+j}\right)^2
&=
\sum_{0\le j,k<H}\sum_t b_{t+j}b_{t+k}\\
&=
\sum_{|h|<H}(H-|h|)\sum_n b_{n+h}b_n,
\end{aligned}
\tag{20}
\]

which is `(11)`.

Only `N+H-1` translated windows can be nonzero, while

\[
\sum_t\sum_{j=0}^{H-1}b_{t+j}
=H\sum_nb_n.
\tag{21}
\]

Cauchy–Schwarz applied to the nonzero windows proves `(12)`.

This is stronger than observing the single point `(h,k)=(0,0)`. The entire second-difference diagonal face is a positive quadratic energy of the first-level magnitude sequence. Its forced scale is controlled by one new bandwidth, not by the product of both shift bandwidths.

## 3. The source character vanishes from every degenerate face

For the source-frame application, each factor of `D_{r-1}` is either

\[
w(m)\chi(m)
\quad\text{or its complex conjugate}.
\tag{22}
\]

Taking the absolute square eliminates every character phase and leaves one factor `|w(m)|^2 |chi(m)|^2` at each cube vertex. This proves `(8)`.

At depth two, insert the exact `MC-415` expansion `(14)` into `(10)` to obtain `(15)`. Thus the first candidate higher-order escape inherits two structural facts simultaneously:

1. the off-face cube may carry genuinely new translated character information;
2. the coordinate-zero face is an entirely phase-free positive incidence problem built from the already re-quadratized linear sieve.

A proof cannot credit the second shift as an independent source-character direction without accounting for both.

## 4. Relation to the positive-kernel frontier

`MC-419` shows that a genuinely multivariable **quadratic** positive kernel can lower its zero-mode floor according to independent bandwidth volume, and `MC-420` shows that merely embedding one relative shift into more coordinates does not increase effective translation rank.

Iterated van der Corput takes a different route: it genuinely introduces new shift variables, but only by increasing the moment order from quadratic correlations to higher cube correlations. The present result identifies the price of that move. A rank-two fourth-order cube has codimension-one degeneracy faces whose coefficient scale is `1/H` or `1/K`; it is therefore incorrect to compare it with a rank-two quadratic kernel solely through the all-zero coefficient `1/(HK)`.

This distinction keeps two possible escape routes open:

- a genuinely rank-two quadratic arithmetic lift derived before positive closure, still subject to `MC-419`–`MC-420`; or
- a higher-order cube/dispersion method that proves enough structured off-face cancellation to overcome the source-free diagonal faces described here.

What is closed is the intermediate shortcut: **“iterate ordinary positive differencing, count the new shift variables, and claim the tensorized Fejér floor.”**

## Prior art and novelty boundary

The cube derivative algebra is classical higher-order Fourier analysis, not a new theorem. W. T. Gowers, *A new proof of Szemerédi's theorem*, Geometric and Functional Analysis **11** (2001), 465–588, DOI `10.1007/s00039-001-0332-9`, introduced the higher-degree uniformity framework in which repeated Cauchy–Schwarz produces exactly these cube products. Modern Gowers norms package the same iterated multiplicative-derivative identity.

The weighted finite-window identity `(11)` is the ordinary Fejér/autocorrelation identity applied to the nonnegative sequence `|a_n|^2`; `(12)` is Cauchy–Schwarz. No novelty is claimed for either analytic ingredient.

The Mathia-specific contribution is the frontier specialization. `MC-415`–`MC-418` identified the unavoidable lcm diagonal of one positive differencing step; `MC-419`–`MC-420` then isolated genuine translation dimension as a possible escape. Equations `(3)`, `(8)`, and `(15)` show that the obvious attempt to realize that escape by **iterating** positive differencing does not inherit the quadratic tensor-product accounting: its new dimension comes with a codimension-one, source-free, re-squared sieve face.

A targeted literature audit on 20 September 2026 found the standard Gowers/cube mechanism but no basis for claiming novelty for the derivative or diagonal identities themselves.

## Boundaries and falsification tests

- **This is not a lower bound for the full cube energy.** Off-face terms can cancel part of a diagonal face inside the exact positive expression. The finding says that a termwise absolute-value or positive-majorant closure must account for the face; it does not forbid structured cancellation against it.
- **Higher-order uniformity can still be useful.** Gowers-type inverse/direct theorems exploit relations among the whole cube, not merely independent estimates for each face. Such a theorem is outside this obstruction if it controls the full weighted arithmetic cube with the actual source/sieve structure.
- **The source-free statement uses absolute squaring.** For a Dirichlet character, `|chi(n)|^2` is the coprimality indicator. The face can still carry arithmetic through those support restrictions and through `w`; what disappears is the oscillatory source-character phase.
- **The lcm statement is inherited, not a new compression theorem.** Equation `(15)` uses the exact square expansion already proved in `MC-415`. The two-endpoint product may contain additional congruence geometry; it is not claimed to collapse to a single lcm coefficient.
- **The `1/H_j` statement concerns normalized Fejér coefficient mass.** It must not be misread as saying that each face contributes a fixed fraction of the final energy.
- **Signed/indefinite or nonstationary higher-order architectures remain open.** The obstruction concerns the ordinary positive repeated-differencing closure.
- **No RH-scale input is used.** Everything through `(15)` is finite algebra plus positivity/Cauchy–Schwarz.

## Consequence for the research line

The positive-kernel frontier is narrower than after `MC-420`. A second translation variable is not sufficient by itself: **how that variable is created matters**. Ordinary iterated van der Corput creates it by raising correlation order, and the resulting cube contains source-free diagonal faces at reciprocal one-axis scale.

For the accepted `CLUE-averaged-qvdc-source-frame-variable-retention`, the next viable higher-order continuation must therefore keep the incomplete off-face translated family intact and demonstrate a collective estimate whose gain survives the coordinate-zero faces and the lcm-incidence energies they expose. Applying another generic Cauchy/absolute-value step and budgeting only the all-zero corner does not meet that gate.

A genuinely rank-two quadratic lift derived before squaring remains logically distinct and is not ruled out here. So do higher-order methods that control the full cube without termwise majorization. The finding closes only the naive dimensional-accounting escape and converts “find a second shift” into the sharper obligation “find a second shift whose full higher-order closure can pay its degenerate faces.”