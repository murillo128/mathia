# ANF-181 — Exact log-frequency centering defeats growing local derivative jets below the endpoint-memory scale

**Status:** `EXACT-DERIVED + MATCHED-CONTROL + GROWING-JET-BARRIER + COMPLEXITY-THRESHOLD`. `ANF-180` shows that the prime-scale endpoint-loading control can compress its local twist frequencies into an asymptotically narrow band, making every **fixed finite** family of continuous local twist probes asymptotically rank one. The obvious remaining generic escape is to let probe complexity grow with `X`: for example, take more and more derivatives of the demodulated local twist profile until the narrow frequency packet becomes resolvable.

That escape is much more expensive than the fixed-complexity statement suggests. By centering the twist coordinate with the **exact logarithmic phase** instead of the affine approximation used in the previous construction, the same prime-scale dangerous packet can make an entire derivative jet of growing order asymptotically rank one. If

\[
K=X^{1-2\varepsilon+o(1)},
\qquad
0<\varepsilon<\frac1{16},
\qquad
 a_X:=\sqrt{\delta X\log X},
\]

and `r_X` is any positive integer sequence satisfying

\[
\boxed{
\frac{r_X a_X}{K}\longrightarrow0,
}
\tag{1}
\]

then there is a prime-scale matched endpoint-loading control with the same bow-scale completion as `ANF-175`--`ANF-180` for which, after exact log-frequency recentering, all normalized derivatives through order `r_X` satisfy

\[
\boxed{
(-i\xi_*)^{-k}F_X^{(k)}(y)
=
F_X(y)+o(a_X)
\qquad
(0\le k\le r_X),
}
\tag{2}
\]

uniformly for `|y|<=c` for every fixed `c>0`, while

\[
|F_X(y)|\ge a_X-o(a_X).
\tag{3}
\]

Thus the entire growing derivative jet remains asymptotically rank one. Since

\[
\frac{K}{a_X}
=
\frac{X^{1/2-2\varepsilon+o(1)}}{\sqrt{\log X}},
\tag{4}
\]

this rules out not only fixed-degree and polylogarithmic local derivative tomography, but every polynomial derivative order `r_X=X^{\theta+o(1)}` with `theta<1/2-2\varepsilon`. The scale `K/a_X` is also the natural geometric threshold of this compression mechanism: a packet of physical width comparable with `a_X` that must finish loading before `K` cannot have relative exact-log frequency width smaller than order `a_X/K`. Hence the construction cannot force rank-one collapse once `r_X a_X/K` is bounded away from zero. This is a sharpness statement for the **matched-control compression architecture**, not a theorem that derivatives of order `K/a_X` suffice for the arithmetic source.

## 1. Prime-scale endpoint loading with a movable packet

Use the same prime-scale marginals as `ANF-175`--`ANF-180`. Put

\[
A_X:=\log X,
\qquad
q_X:=\lceil\log X\rceil,
\qquad
N_X:=\left\lceil\frac{4\sqrt3\,a_X}{A_X}\right\rceil,
\tag{5}
\]

and let

\[
B_X:=N_Xq_X=\Theta_\delta(a_X)
\tag{6}
\]

be the physical width needed to hold the candidate lattice. Let `r_X>=1` satisfy (1). Because `B_X\asymp a_X`, we also have

\[
\frac{r_XB_X}{K}\to0.
\tag{7}
\]

Choose

\[
d_X:=\sqrt{\frac{B_X}{r_XK}},
\qquad
J_X:=\left\lceil\frac{B_X}{d_X}\right\rceil.
\tag{8}
\]

Then

\[
d_X\to0,
\qquad
r_Xd_X=\sqrt{\frac{r_XB_X}{K}}\to0,
\qquad
\frac{J_X}{K}=O\!\left(\sqrt{\frac{r_XB_X}{K}}\right)\to0,
\tag{9}
\]

and

\[
\frac{B_X}{J_X}\le d_X\to0.
\tag{10}
\]

In particular `J_X+B_X=o(K)`. Take candidate offsets

\[
j_s:=J_X+s q_X,
\qquad
0\le s<N_X.
\tag{11}
\]

For the distinguished twist `U\asymp X^2`, divide the arguments of the exact carrier vectors

\[
(X+j_s)^{-iU}
\]

into six sectors of angular width `pi/3`. One sector contains at least `N_X/6` candidates. Let `S_X` be those candidates and define

\[
P_X(t):=
A_X\sum_{j\in S_X}(X+j)^{-it}.
\tag{12}
\]

Every selected vector has projection at least `cos(pi/6)=sqrt(3)/2` on the center ray of its sector, so by (5)

\[
|P_X(U)|\ge a_X.
\tag{13}
\]

The construction retains the prime-scale marginal envelope. For every interval `I` of offsets of length `H`,

\[
\sum_{j\in I}|c_j|
\le
A_X\left(\frac{H}{q_X}+1\right)
\ll H+\log X,
\tag{14}
\]

where `c_j=A_X` on `S_X` and zero elsewhere. The total absolute mass is

\[
M_X:=\sum_j|c_j|\le A_XN_X=O_\delta(a_X).
\tag{15}
\]

Because all active offsets lie before `J_X+B_X=o(K)`, the prefix sum retains the final load (13) for `(1-o(1))K` later prefixes. Exactly as in the matched controls of `ANF-175`--`ANF-180`, this gives

\[
E_-
\ge
(K-J_X-B_X)|P_X(U)|^2
\ge
(\delta-o(1))XK\log X.
\tag{16}
\]

The diagonal contribution remains lower order:

\[
\Delta_-
\ll
K\sum_j|c_j|^2
\ll
K a_X\log X
=
o(XK\log X).
\tag{17}
\]

Hence the packet is a genuine off-diagonal endpoint obstruction and, through `ANF-169` and `ANF-172`, also forces a target-sized signed dyadic correlation / Fejer scale-slope defect.

## 2. Exact logarithmic recentering removes the curvature loss

The approximate affine frequency coordinate in `ANF-180` introduces a secondary curvature condition when one tries to shrink the normalized band aggressively. That condition is not intrinsic. Demodulate `P_X` by the exact base phase:

\[
G_X(t):=X^{it}P_X(t)
=
A_X\sum_{j\in S_X}
\exp\!\left(-it\log\left(1+\frac jX\right)\right).
\tag{18}
\]

Fix once and for all `xi_* in (0,1)`; for concreteness one may take `xi_*=1/2`. Define the exact local twist scale

\[
W_X:=
\frac{\xi_*}{\log(1+J_X/X)}
\tag{19}
\]

and the rescaled profile

\[
F_X(y):=G_X(U+W_Xy)
=
A_X\sum_{j\in S_X}
\zeta_j e^{-iy\xi_j},
\tag{20}
\]

where

\[
\zeta_j:=
\exp\!\left(-iU\log\left(1+\frac jX\right)\right),
\qquad
\xi_j:=
W_X\log\left(1+\frac jX\right).
\tag{21}
\]

At the left edge `j=J_X`, the normalized frequency is exactly `xi_*`. For every active `j in [J_X,J_X+B_X]`,

\[
\frac{\xi_j}{\xi_*}-1
=
\frac{
\log(1+j/X)-\log(1+J_X/X)
}{
\log(1+J_X/X)
}.
\tag{22}
\]

Now

\[
\log\left(1+\frac{j-J_X}{X+J_X}\right)
\le
\frac{j-J_X}{X+J_X},
\tag{23}
\]

while

\[
\log\left(1+\frac{J_X}{X}\right)
\ge
\frac{J_X}{X+J_X}.
\tag{24}
\]

Therefore

\[
0\le
\frac{\xi_j}{\xi_*}-1
\le
\frac{j-J_X}{J_X}
\le
\frac{B_X}{J_X}
=:\Delta_X
\le d_X.
\tag{25}
\]

This estimate is exact in the logarithmic coordinate; there is no Taylor remainder to control. In particular the additional affine-curvature restriction from `ANF-180` disappears. The only small parameter needed below is the genuine relative packet width `Delta_X`.

For every fixed `c>0`, (15) and (25) imply

\[
\begin{aligned}
|F_X(y)-e^{-iy\xi_*}F_X(0)|
&\le
A_X\sum_{j\in S_X}
|e^{-iy\xi_j}-e^{-iy\xi_*}|\\
&\le
c\,\xi_* M_X\Delta_X
=o(a_X)
\end{aligned}
\tag{26}
\]

uniformly for `|y|<=c`. Since `|F_X(0)|=|P_X(U)|>=a_X`, this proves (3). The dangerous packet remains coherent throughout every fixed normalized local twist window.

The physical twist window is not collapsing. Because `J_X=o(K)=o(X)`,

\[
W_X
\sim
\xi_*\frac{X}{J_X},
\tag{27}
\]

and `J_X/K->0` gives

\[
W_X\gg \frac{X}{K}=X^{2\varepsilon+o(1)}.
\tag{28}
\]

Thus a fixed `y`-window corresponds to a physically widening `t`-window.

## 3. Every derivative up to order `r_X` becomes the same measurement

Differentiate (20). For `k>=0`, define the dimensionless normalized derivative

\[
D_{k,X}(y)
:=
(-i\xi_*)^{-k}F_X^{(k)}(y)
=
A_X\sum_{j\in S_X}
\left(\frac{\xi_j}{\xi_*}\right)^k
\zeta_j e^{-iy\xi_j}.
\tag{29}
\]

Using (15) and (25), for every `0<=k<=r_X`,

\[
\begin{aligned}
|D_{k,X}(y)-F_X(y)|
&\le
M_X\left((1+\Delta_X)^k-1\right)\\
&\le
M_X\left(e^{r_X\Delta_X}-1\right).
\end{aligned}
\tag{30}
\]

But (8)--(10) give

\[
r_X\Delta_X
\le
r_Xd_X
=
\sqrt{\frac{r_XB_X}{K}}
\longrightarrow0.
\tag{31}
\]

Hence

\[
\boxed{
\sup_{0\le k\le r_X}
\sup_{|y|\le c}
|D_{k,X}(y)-F_X(y)|
=o(a_X).
}
\tag{32}
\]

Together with (3), the whole vector

\[
(D_{0,X}(y),D_{1,X}(y),\ldots,D_{r_X,X}(y))
\tag{33}
\]

lies inside an `o(a_X)` `ell^infty`-tube around the rank-one vector

\[
F_X(y)(1,1,\ldots,1).
\tag{34}
\]

Equivalently, in the unnormalized derivatives,

\[
F_X^{(k)}(y)
=
(-i\xi_*)^kF_X(y)+o(a_X)
\tag{35}
\]

uniformly for all `k<=r_X` (with `xi_*` fixed away from zero). Increasing the derivative order therefore adds no asymptotically independent information anywhere below the scale (1).

A useful stress point is

\[
r_X=
\frac{K}{a_X L_X},
\qquad
L_X\to\infty
\tag{36}
\]

arbitrarily slowly. Then the jet order is within a slowly varying factor of the full threshold `K/a_X`, yet (31) still tends to zero. Thus the obstruction is not merely against modestly growing complexity such as powers of `log X`.

## 4. `K/a_X` is the geometric threshold of this compression mechanism

The preceding construction gives an upper bound on how much relative log-frequency width is needed. There is a matching lower bound for any packet of physical width `B` placed before the endpoint horizon.

Let a packet occupy offsets in `[J,J+B]` with `J+B<=K`, and normalize exact log-frequency so the left edge has frequency `xi_*`. Its relative frequency width is

\[
\Delta_{\log}
:=
\frac{
\log(1+(J+B)/X)-\log(1+J/X)
}{
\log(1+J/X)
}.
\tag{37}
\]

The numerator obeys

\[
\log\left(1+\frac{B}{X+J}\right)
\ge
\frac{B}{X+J+B},
\tag{38}
\]

whereas

\[
\log\left(1+\frac JX\right)
\le
\frac JX.
\tag{39}
\]

Consequently

\[
\Delta_{\log}
\ge
\frac{BX}{J(X+J+B)}.
\tag{40}
\]

Because `J+B<=K=o(X)`,

\[
\boxed{
\Delta_{\log}
\ge
(1-o(1))\frac BJ
\ge
(1-o(1))\frac BK.
}
\tag{41}
\]

A normalized derivative of order `r` weights the two ends of such a band differently by a factor comparable with `(1+Delta_log)^r`. For the rank-one collapse mechanism used above one necessarily needs

\[
r\Delta_{\log}\to0.
\tag{42}
\]

For the prime-scale dangerous packet `B\asymp a_X`, (41)--(42) force

\[
\frac{r a_X}{K}\to0.
\tag{43}
\]

Thus the same scale appearing in the construction is also forced by packet geometry. At `r\asymp K/a_X`, the exact-log band can no longer be made asymptotically invisible to all derivative monomials while the packet still finishes loading before `K`.

This is deliberately a **mechanism-level sharpness statement**. It does not show that an order-`K/a_X` derivative jet recovers the true prime-minus-Ramanujan source, nor even that it distinguishes every dangerous matched control. It only says that the present adversarial strategy -- compress a prime-scale loading packet into an almost monochromatic exact-log band -- cannot continue to force asymptotic rank one beyond that complexity scale.

## 5. Stress tests and limitations

The result survives all of the source-marginal stress tests already built into `ANF-175`--`ANF-180`: positive atom amplitudes of size `log X`, support density at most `1/log X`, local absolute mass `O(H+log X)`, exact distinguished carrier `(X+j)^{-iU}`, off-diagonal endpoint completion of bow size, and a physically widening local twist window. The new ingredient changes only where the packet is placed and how the local twist axis is normalized.

The construction still uses the same freedom that remains artificial throughout this obstruction chain: **placement is chosen after seeing the distinguished carrier phase**. Real prime and rough locations cannot be moved into the favorable sector. Therefore (32) is not evidence that the arithmetic source actually has a rank-one derivative jet. It says that no theorem whose hypotheses only encode the matched marginals, endpoint size, and a derivative family of order `o(K/a_X)` can exclude such behavior without some additional source-specific placement law.

Nor does the theorem rule out growing probe families with much larger resolving complexity than their cardinality. A deliberately oscillatory symbol may vary by order one across a band of width `a_X/K` even when there are few such probes. The correct generic quantity is therefore **frequency resolution / symbol variation**, not simply the number of measurements. Derivative order is a clean model because its resolving complexity is explicit: the monomial multiplier `(xi/xi_*)^k` changes appreciably once `k Delta` is order one.

Finally, the lower bound (41) uses the requirement that the packet finish loading before `K`. If one abandons endpoint memory and studies a different observable that can use atoms placed after the endpoint horizon, this geometric threshold need not apply. It is specific to the endpoint-completion obstruction currently governing `analytic_frontier`.

## 6. Prior-art audit and frontier consequence

There is substantial neighboring literature on Fourier/Vandermonde recovery with clustered nodes and on sparse superresolution. In particular, Batenkov--Demanet--Goldman--Yomdin, *Conditioning of Partial Nonuniform Fourier Matrices with Clustered Nodes* (SIAM J. Matrix Anal. Appl. 41 (2020), 199--220, DOI `10.1137/18M1212197`), proves that conditioning deteriorates with the superresolution factor and cluster size. That is conceptually consistent with the role of `r_X Delta_X` here. It is not load-bearing for the present argument, which is an elementary exact-log construction, and it does not provide the endpoint-memory matched control, the prime-scale loading law, or the threshold `K/a_X`. No new external theorem is therefore required in `SOURCES.md`.

The research frontier is sharpened materially. `ANF-180` left `X`-dependent/growing local probe complexity as a generic escape from fixed-rank blindness. `ANF-181` shows that, for derivative tomography, merely allowing growth is nowhere near enough: the order must reach at least the geometric resolution scale

\[
\boxed{
\frac{K}{\sqrt{X\log X}}
=
\frac{X^{1/2-2\varepsilon+o(1)}}{\sqrt{\log X}}
}
\tag{44}
\]

before this specific matched-control obstruction ceases to force rank one. This makes fixed-degree, polylogarithmic, and low-polynomial local jet strategies structurally inadequate as generic source-free replacements for the signed Fejer target.

The surviving directions are correspondingly narrower: exploit a source-specific law tying prime/rough placement to the distinguished carrier; use an observable whose effective log-frequency resolution is at least `a_X/K` rather than merely adding more low-order moments; or return directly to the signed dyadic correlation / Fejer slope defect of `ANF-169`--`ANF-172`, where the arithmetic cancellation is kept intact. No existing clue has its decisive test resolved by this construction, and no adversarial-review sidecar requires a status transition in this pass.