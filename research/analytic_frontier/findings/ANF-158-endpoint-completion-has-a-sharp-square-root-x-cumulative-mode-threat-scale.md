# ANF-158 — endpoint completion has a sharp square-root-X cumulative-mode threat scale

**Status:** `EXACT-DERIVED + ENDPOINT-INTEGRATION-SVD + BOW-SCALE-THREAT-LOCALIZATION + SOURCE-PARTIAL-SUM-GATE`. `ANF-157` writes the integer bow energy as full Fejer energy minus the positive prefix/suffix completion term `E_partial`. The latter cannot be discarded from coefficient-edge mass alone, because coherent partial sums can amplify a negligible edge diagonal into target-scale completion. That obstruction can be localized much more sharply. Each endpoint completion is exactly the squared norm of a finite discrete integration operator, whose singular system is elementary. Under the actual pointwise residual bound `|r_X(n)| << log X`, all cumulative modes above rank

\[
J_*(X,K):=K\sqrt{\frac{\log X}{X}}
\]

contribute negligibly at the bow scale once the cutoff exceeds `J_*` by a diverging factor. This rank scale is sharp under the same pointwise information. Equivalently, target-scale endpoint compensation forces a twisted residual prefix or suffix sum of size `Omega(sqrt(X log X))`, hence coherence across at least `Omega(sqrt(X/log X))` endpoint sites. Thus the finite-horizon obstruction in `ANF-157` is not an arbitrary `K`-dimensional edge phenomenon: it lives in a vanishing low-frequency cumulative sector with a physical coherence length of square-root-`X` order. Controlling that sector would make the Fejer criterion of `ANF-157` asymptotically equivalent to the cropped bow target.

## 1. Endpoint completion is two copies of a discrete integration norm

Retain the exact integer model of `ANF-157`. Thus

\[
M=N+K-1,
\qquad
E_{\partial}(b)
=
\sum_{r=1}^{K-1}\left|\sum_{n=1}^{r}b_n\right|^2
+
\sum_{r=1}^{K-1}\left|\sum_{n=M-r+1}^{M}b_n\right|^2.
\tag{1}
\]

Put

\[
L:=K-1,
\qquad
e^-_n:=b_n,
\qquad
e^+_n:=b_{M+1-n},
\qquad 1\le n\le L.
\tag{2}
\]

Let `P_L` be the lower-triangular cumulative-sum matrix

\[
(P_Le)_r:=\sum_{n=1}^{r}e_n,
\qquad 1\le r\le L.
\tag{3}
\]

Then the two boundary pieces in (1) are literally the same quadratic form:

\[
\boxed{
E_{\partial}(b)
=\|P_Le^-\|_2^2+\|P_Le^+\|_2^2.
}
\tag{4}
\]

The Gram matrix `G_L:=P_L^*P_L` has entries

\[
(G_L)_{nm}=L+1-\max\{n,m\}.
\tag{5}
\]

After reversing coordinates this is the classical discrete Green matrix `(min(i,j))`. The exact form (4) is useful because the apparently nonlocal list of all nested prefix/suffix squares is now one fixed endpoint operator whose dangerous directions can be diagonalized.

## 2. The cumulative operator has an exact sine singular basis

Let

\[
\theta_j:=\frac{(2j-1)\pi}{2L+1},
\qquad 1\le j\le L,
\tag{6}
\]

and define

\[
u_j(n)
:=
\frac{2}{\sqrt{2L+1}}
\sin\bigl((L+1-n)\theta_j\bigr),
\qquad 1\le n\le L.
\tag{7}
\]

These vectors form an orthonormal basis and diagonalize `G_L` with decreasing eigenvalues

\[
\boxed{
\lambda_j
=
\frac{1}
{4\sin^2\!\left(\dfrac{(2j-1)\pi}{4L+2}\right)}.
}
\tag{8}
\]

A direct proof keeps the result independent of any external spectral theorem. Reversing (5) gives `M_L=(min(i,j))`. Its inverse is the tridiagonal second-difference matrix with diagonal `2` except for final diagonal entry `1`, and with adjacent entries `-1`. The vector `v_i=sin(i theta)` is an interior eigenvector with inverse eigenvalue `4 sin^2(theta/2)`. The final boundary condition is `v_{L+1}=v_L`, which is equivalent to

\[
\cos\frac{(2L+1)\theta}{2}=0,
\tag{9}
\]

and yields exactly the angles (6). Reversing back gives (7)--(8).

If

\[
\alpha_j^-:=\langle e^-,u_j\rangle,
\qquad
\alpha_j^+:=\langle e^+,u_j\rangle,
\tag{10}
\]

then (4) becomes the exact endpoint spectral ledger

\[
\boxed{
E_{\partial}(b)
=
\sum_{j=1}^{L}
\lambda_j
\left(
|\alpha_j^-|^2+|\alpha_j^+|^2
\right).
}
\tag{11}
\]

Thus endpoint completion strongly favors the first cumulative sine modes: for `j=o(K)`,

\[
\lambda_j
=(1+o(1))\frac{K^2}{\pi^2j^2}.
\tag{12}
\]

The large deterministic norm of prefix summation is therefore not spread uniformly across the `K-1` boundary dimensions. It is concentrated at low cumulative frequency.

## 3. Only a vanishing low-mode sector can matter at the bow scale

For an integer cutoff `1<=J<L`, let `E_{>J}` denote the contribution to (11) from modes `j>J`. Since the eigenvalues decrease,

\[
E_{>J}
\le
\lambda_{J+1}
\left(\|e^-\|_2^2+\|e^+\|_2^2\right).
\tag{13}
\]

The elementary inequality `sin x >= 2x/pi` on `[0,pi/2]`, applied to (8), gives

\[
\lambda_{J+1}
\le
\frac{(2L+1)^2}{4(2J+1)^2}
<
\frac{K^2}{(2J+1)^2}.
\tag{14}
\]

For the actual post-sieve bow source,

\[
b_n=r_X(X+n)(X+n)^{-iU},
\qquad
r_X=\vartheta-Q_R,
\tag{15}
\]

`ANF-157` records the pointwise bound `|r_X(n)| << log X`. Hence

\[
\|e^-\|_2^2+\|e^+\|_2^2
\ll K\log^2X,
\tag{16}
\]

and therefore

\[
\boxed{
E_{>J}
\ll
\frac{K^3\log^2X}{J^2}.
}
\tag{17}
\]

Compare this with the bow diagonal scale `XK log X`. Define

\[
\boxed{
J_*(X,K)
:=K\sqrt{\frac{\log X}{X}}.
}
\tag{18}
\]

If `J=J_X` satisfies

\[
\frac{J_X}{J_*(X,K)}\longrightarrow\infty,
\qquad
J_X<K,
\tag{19}
\]

then (17) gives

\[
\boxed{
E_{>J_X}=o(XK\log X).
}
\tag{20}
\]

More quantitatively, taking `J=A J_*` gives an `O(A^{-2})` fraction of the bow scale, up to the absolute constant in the residual bound. In the bow regime

\[
K=X^{1-2\varepsilon+o(1)},
\qquad 0<\varepsilon<\frac14,
\tag{21}
\]

one has

\[
J_*
=X^{1/2-2\varepsilon+o(1)}\sqrt{\log X},
\qquad
\frac{J_*}{K}
=\sqrt{\frac{\log X}{X}}
=o(1).
\tag{22}
\]

So every potentially macroscopic endpoint correction is asymptotically confined to a vanishing fraction of the endpoint dimensions. The associated sine frequencies are `theta_j asymp j/K`; at the critical rank (18) their wavelength is

\[
\boxed{
\frac{K}{J_*}
\asymp
\sqrt{\frac{X}{\log X}}.
}
\tag{23}
\]

The physical coherence length is therefore independent of the bow window length to first order.

## 4. The critical rank cannot be improved from pointwise size alone

The scale (18) is not an artifact of the tail estimate. Assume the bow regime (21), choose an index

\[
j_X\sim cJ_*(X,K)
\tag{24}
\]

with fixed `c>0`, and put all left-edge mass in the exact mode `u_{j_X}`:

\[
e^-:=\sqrt K\,\log X\,u_{j_X},
\qquad e^+:=0.
\tag{25}
\]

Because `|u_j(n)|<=2/sqrt(2L+1)`, this control obeys the same crude coefficient scale

\[
\|e^-\|_\infty=O(\log X).
\tag{26}
\]

Since `j_X=o(K)` and, for fixed `epsilon<1/4`, `j_X->infinity`, equations (11)--(12) give

\[
\boxed{
E_{\partial}(b)
=(1+o(1))
\frac{1}{\pi^2c^2}
XK\log X.
}
\tag{27}
\]

At the same time its entire coefficient-edge contribution to the moving diagonal is bounded by

\[
D_{\rm edge}
\le
K\|e^-\|_2^2
=K^2\log^2X
=o(XK\log X),
\tag{28}
\]

because `K log X=o(X)` in (21). Thus a boundary packet can remain negligible in the diagonal and nevertheless create a macroscopic endpoint completion precisely at rank `J_*`.

This is only a matched coefficient-class control, not a claim about the arithmetic source. Its role is to mark the information boundary: neither the pointwise `O(log X)` residual bound nor negligible coefficient-edge diagonal can reduce the dangerous cumulative sector below (18). Any such improvement must use source-specific arithmetic or phase information.

## 5. The same obstruction is equivalent to a square-root-X partial-sum spike

There is a complementary formulation that removes the spectral basis entirely. Define

\[
M_{\partial}(b)
:=
\max_{1\le r<K}
\max\left\{
\left|\sum_{n=1}^{r}b_n\right|,
\left|\sum_{n=M-r+1}^{M}b_n\right|
\right\}.
\tag{29}
\]

From (1), exactly

\[
\boxed{
M_{\partial}(b)^2
\le
E_{\partial}(b)
\le
2(K-1)M_{\partial}(b)^2.
}
\tag{30}
\]

Consequently the source estimate

\[
\boxed{
M_{\partial}(b)=o(\sqrt{X\log X})
}
\tag{31}
\]

is sufficient to make

\[
E_{\partial}(b)=o(XK\log X).
\tag{32}
\]

Conversely, if for some fixed `delta>0`

\[
E_{\partial}(b)\ge\delta XK\log X,
\tag{33}
\]

then

\[
\boxed{
M_{\partial}(b)
\ge
\left(\sqrt{\frac\delta2}+o(1)\right)
\sqrt{X\log X}.
}
\tag{34}
\]

Under `|b_n|<<log X`, any prefix or suffix attaining (34) must contain at least

\[
\boxed{
\Omega\!\left(\sqrt{\frac{X}{\log X}}\right)
}
\tag{35}
\]

terms. The elementary partial-sum gate (34)--(35) and the spectral wavelength (23) identify the same scale from two directions.

For the actual source, (31) asks only for the two endpoint maximal estimates

\[
\max_{1\le r<K}
\left|
\sum_{n=1}^{r}
 r_X(X+n)(X+n)^{-iU}
\right|
=o(\sqrt{X\log X})
\tag{36}
\]

and the analogous reversed sum at the right endpoint. These are source-specific distinguished-twist statements; they are not implied by the generic coefficient facts excluded in `ANF-147`.

Now combine (32) with the exact completion identity from `ANF-157`,

\[
V_{N,K}(b)=K\mathcal F_K(b)-E_{\partial}(b).
\tag{37}
\]

Under (31), one gets the asymptotic equivalence

\[
\boxed{
V_{N,K}(b)=o(XK\log X)
\iff
\mathcal F_K(b)=o(X\log X).
}
\tag{38}
\]

More generally, if a future source theorem proves a fixed positive Fejer lower bound

\[
\mathcal F_K(b)\ge\delta X\log X
\tag{39}
\]

while the bow target nevertheless holds, then (37) forces (33), and hence the square-root-`X` endpoint spike (34). Therefore a positive Fejer theorem and the maximal endpoint estimate (31) form a clean two-part negative test for the bow.

The exact low-mode coefficients make the alternative source interface equally explicit:

\[
\alpha_j^-
=
\frac{2}{\sqrt{2K-1}}
\sum_{n=1}^{K-1}
 r_X(X+n)(X+n)^{-iU}
\sin\left((K-n)\frac{(2j-1)\pi}{2K-1}\right),
\tag{40}
\]

with the analogous right-edge formula. By (20), only `j` up to a slowly enlarged multiple of `J_*` need be controlled to eliminate target-scale endpoint completion. This turns the raw list of `K-1` nested partial sums into a much smaller family of smooth tapered prime--Ramanujan correlations.

## 6. Prior-art boundary, stress tests, and frontier consequence

The matrix in (5) is the standard finite discrete integration/Green matrix, and its inverse-second-difference diagonalization is classical numerical linear algebra. The literature audit found the same `min(i,j)` / modified second-difference structure in classical treatments of discrete Green matrices and cumulative operators. No external theorem is used in (4)--(40): the inverse, boundary condition, eigenvalues, tail bound, and bow-scale consequences are rederived above, so this finding introduces no new load-bearing source and `SOURCES.md` need not change.

Three stress tests delimit the claim. A coherent constant-sign edge has prefix energy of order `K^3`, exactly consistent with concentration in the first cumulative modes. Rapidly oscillating edge data has much smaller cumulative energy and falls into the harmless high-mode side of (17). Most importantly, the synthetic critical mode (25) proves that the `J_*` boundary cannot be improved using only the pointwise residual bound, even though its moving diagonal edge mass is negligible. None of these controls is asserted to model `vartheta-Q_R`; as `ANF-147` already shows, arbitrary real coefficients against the exact logarithmic carrier have too much freedom to substitute for arithmetic information.

The analytic-frontier gate after `ANF-157` is therefore narrower. One no longer needs to control an opaque `K`-dimensional endpoint completion. It is enough either to prove the maximal distinguished-twist bound (31), or to rule out the first `O(J_*)` cumulative sine modes in (40) strongly enough that their weighted contribution is `o(XK log X)`. Once that is done, the hard crop stops being a separate obstruction and the bow question reduces asymptotically to the explicit Fejer-null-frequency source theorem already isolated in `ANF-157`. Conversely, if endpoint completion is genuinely responsible for a successful bow cancellation despite positive Fejer energy, it must manifest as a square-root-`X` coherent boundary event. That is a concrete arithmetic signature that can be attacked or falsified directly.