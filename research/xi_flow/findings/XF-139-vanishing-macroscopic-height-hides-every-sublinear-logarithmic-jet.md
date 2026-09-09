# XF-139 — vanishing macroscopic height hides every sublinear logarithmic jet

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE/TRANSITION-CONDITIONING` + `MOVING-EXTERIOR-LOG-JET` + `SUBLINEAR-DEPTH` + `ZERO-DELAY` + `UNIT-CIRCLE-MATCHED-CONTROL` + `CROSS-SCALE`. XF-137 shows that a macroscopic exterior point can hide a full degree-order logarithmic heat jet, while XF-138 shows that a fixed root-spacing exterior point still hides a jet of depth `Theta(N/log N)`. The missing interpolation is not merely quantitative. The same central packet gives a complete height-versus-jet phase law, and it implies that **every sublinear raw logarithmic jet can remain exponentially transition-blind at an observation height that itself tends to zero as a fraction of the period**.

Let

\[
b_*
:=
\frac12\sqrt{W_0(2)\bigl(2+W_0(2)\bigr)}
=0.779767136088\ldots
\tag{1}
\]

be the optimized XF-136 packet exponent, let `N=2M`, and use the XF-134 transition-sharp matched control with the XF-136 optimal packet depth. Write

\[
Q_s(\beta):=E_{\rm c}(-e^{\beta/N},s),
\qquad
q_0(\beta):=1+e^\beta.
\tag{2}
\]

For every `rho>=0`, the shifted control has trace `Q_(s+rho)` and

\[
\Lambda_{\rm per}(E_{\rm c})=0,
\qquad
\Lambda_{\rm per}(E_{{\rm c},\rho})=-\rho.
\tag{3}
\]

There are two equivalent useful forms of the new bound.

First, let `h_N>=2` satisfy

\[
h_N=o(N),
\tag{4}
\]

and observe at the moving exterior point

\[
\boxed{\beta_N=h_N.}
\tag{5}
\]

For any fixed `0<c<b_*`, define

\[
\boxed{
J_N(c,h_N)
:=
\left\lfloor
\frac{cN}{
W_0\!\left(\frac{2cN}{e h_N}\right)
}
\right\rfloor .
}
\tag{6}
\]

Then `J_N(c,h_N)=o(N)` and

\[
\boxed{
\sup_{\substack{s\ge0,\ \rho\ge0\\1\le j\le J_N(c,h_N)}}
\left|
\partial_\beta^j\log Q_s(h_N)
-
\partial_\beta^j\log Q_{s+\rho}(h_N)
\right|
\le
\exp\!\left[-(b_*-c)N+o(N)\right].
}
\tag{7}
\]

Thus the fixed-height `N/log N` threshold of XF-138 is only one endpoint of a continuous tradeoff. As the exterior point is allowed to recede by a sublinear number of root spacings, the certifiably blind raw jet becomes correspondingly deeper while the physical observation point still approaches the divisor line on the macroscopic scale.

Second, the phase law has a sharper inverse corollary. Let `K_N` be **any** integer sequence with

\[
K_N\to\infty,
\qquad
K_N=o(N).
\tag{8}
\]

Choose

\[
\boxed{
d_N:=\frac{K_N}{e},
\qquad
\beta_N:=2d_N=\frac{2K_N}{e}.}
\tag{9}
\]

Then the entire future raw logarithmic jet through order `K_N` obeys

\[
\boxed{
\sup_{\substack{s\ge0,\ \rho\ge0\\1\le j\le K_N}}
\left|
\partial_\beta^j\log Q_s(\beta_N)
-
\partial_\beta^j\log Q_{s+\rho}(\beta_N)
\right|
\le
\exp\!\left[-b_*N+\frac{2K_N}{e}+O(\log N)\right]
=
\exp[-(b_*-o(1))N].
}
\tag{10}
\]

So even a jet as deep as, for example, `N/log log N`, `N/sqrt(log log N)`, or more generally `N/g(N)` for any `g(N)->infinity`, can remain exponentially insensitive to an order-one change in transition time. The price is moving the observation point outward by only `Theta(K_N)` root-spacing units, which is still `o(N)` and hence a vanishing fraction of the physical period.

## 1. A moving zero-free disk costs only its radius, not its center

As in XF-135--XF-138, write

\[
Q_s(\beta)=q_0(\beta)+u_s(\beta),
\tag{11}
\]

where `u_s=t_* Delta E(-e^(beta/N),s)`, `|t_*|<=2`, and the optimized central packet satisfies

\[
A_N
:=
\frac{(r!)^2}{(M^2-r^2)^r}
=
\exp[-b_*N+O(\log N)].
\tag{12}
\]

The XF-133 complex-patch estimate is global in the probe coordinate:

\[
|u_s(\gamma)|
\le
2e^{|\gamma|}A_N,
\qquad
s\ge0.
\tag{13}
\]

For a real exterior center `h>=2`, take the disk

\[
D_h:=\{\gamma:|\gamma-h|\le h/2\}.
\tag{14}
\]

On this disk,

\[
|\gamma|\le\frac{3h}{2},
\qquad
\Re\gamma\ge\frac h2,
\tag{15}
\]

so

\[
|q_0(\gamma)|
=|1+e^\gamma|
\ge e^{h/2}-1.
\tag{16}
\]

Combining `(12)`--`(16)`,

\[
\begin{aligned}
\left|\frac{u_s(\gamma)}{q_0(\gamma)}\right|
&\le
\frac{2e^{3h/2}}{e^{h/2}-1}A_N\\
&\le
C e^h A_N\\
&=
\exp[-b_*N+h+O(\log N)],
\end{aligned}
\tag{17}
\]

with an absolute `C`, uniformly in `s>=0`. The key cancellation is the same one used macroscopically in XF-137: after relative normalization by the endpoint carrier, the center itself disappears from the leading radial growth. Only the radius of the zero-free disk is paid.

If `h=h_N=o(N)`, the right side of `(17)` is exponentially small with rate `b_*-o(1)`. Hence for all sufficiently large `N`,

\[
F_s(\gamma)
:=
\log\!\left(1+\frac{u_s(\gamma)}{q_0(\gamma)}\right)
\tag{18}
\]

is analytic on `D_(h_N)` and satisfies

\[
\boxed{
\sup_{\gamma\in D_{h_N}}|F_s(\gamma)|
\le
\exp[-b_*N+h_N+O(\log N)]
}
\tag{19}
\]

uniformly in the complete future heat history.

## 2. The Lambert-W law is the exact factorial budget for a moving center

For every `j>=1`, the stationary carrier again cancels:

\[
\partial_\beta^j\log Q_s
-
\partial_\beta^j\log Q_{s+\rho}
=
\partial_\beta^jF_s
-
\partial_\beta^jF_{s+\rho}.
\tag{20}
\]

Cauchy's estimate on the radius `h_N/2` disk gives

\[
\left|
\partial_\beta^j\log Q_s(h_N)
-
\partial_\beta^j\log Q_{s+\rho}(h_N)
\right|
\le
\exp[-b_*N+h_N+O(\log N)]
\frac{j!}{(h_N/2)^j}.
\tag{21}
\]

Set

\[
x_N
:=
\frac{cN}{W_0(2cN/(e h_N))}.
\tag{22}
\]

The defining identity of Lambert W gives the exact inversion

\[
\boxed{
x_N\log\!\left(\frac{2x_N}{e h_N}\right)=cN.}
\tag{23}
\]

Because `h_N=o(N)`, the Lambert-W argument tends to infinity, so `x_N/N->0`. Stirling then yields

\[
\log\frac{J_N!}{(h_N/2)^{J_N}}
\le
cN+O(\log N),
\qquad
J_N=\lfloor x_N\rfloor.
\tag{24}
\]

The sequence `j!/(h_N/2)^j` decreases and then increases, so its maximum over `1<=j<=J_N` occurs at an endpoint. Since `h_N>=2`, the lower endpoint is at most one; `(24)` controls the upper endpoint. Combining with `(21)` gives

\[
\sup_{1\le j\le J_N}
|\cdots|
\le
\exp[-(b_*-c)N+h_N+O(\log N)],
\tag{25}
\]

which is `(7)` because `h_N=o(N)`.

Equation `(6)` provides a simple phase diagram. If `h_N=2`, it reduces exactly to the XF-138 scale

\[
J_N(c,2)
=
\frac{cN}{W_0(cN/e)}+O(1)
\sim c\frac{N}{\log N}.
\tag{26}
\]

If `h_N=N^alpha` for a fixed `0<alpha<1`, then

\[
\boxed{
J_N(c,h_N)
=
\left(\frac{c}{1-\alpha}+o(1)\right)
\frac{N}{\log N}.}
\tag{27}
\]

If instead

\[
h_N=\frac{N}{(\log N)^p},
\qquad p>0,
\tag{28}
\]

then

\[
\boxed{
J_N(c,h_N)
=
\left(\frac{c}{p}+o(1)\right)
\frac{N}{\log\log N}.}
\tag{29}
\]

Thus a point whose physical height is already only `L/(log N)^p` can still hide a jet much deeper than `N/log N`.

## 3. Every sublinear jet can be hidden while the physical height tends to zero

The inverse statement `(10)` is even simpler and does not spend a fixed fraction `cN` of the packet exponent. Given `(8)`, choose `(9)` and use the disk

\[
D_N:=\{\gamma:|\gamma-2d_N|\le d_N\}.
\tag{30}
\]

Exactly as in `(17)`--`(19)`, now with center `2d_N` and radius `d_N`,

\[
\sup_{\gamma\in D_N}|F_s(\gamma)|
\le
\exp[-b_*N+2d_N+O(\log N)]
=
\exp\!\left[-b_*N+\frac{2K_N}{e}+O(\log N)\right].
\tag{31}
\]

Cauchy's estimate gives an additional factor `j!/d_N^j`. For `1<=j<=K_N`, the uniform Stirling bound gives

\[
\frac{j!}{d_N^j}
=
\frac{j!}{(K_N/e)^j}
\le
C\sqrt{j}\left(\frac{j}{K_N}\right)^j
\le
C\sqrt{K_N}.
\tag{32}
\]

This polynomial factor is absorbed in `O(log N)`, proving `(10)`.

In the XF-067 physical coordinate

\[
\beta=-\frac{2\pi iN}{L}z,
\tag{33}
\]

the observation point `(9)` is

\[
\boxed{
z_N
=i\frac{K_N}{\pi e N}L,}
\tag{34}
\]

and the Cauchy disk has physical radius

\[
\boxed{
R_N
=
\frac{K_N}{2\pi e N}L.}
\tag{35}
\]

Hence the disk stays strictly off the real divisor line, while

\[
\frac{|\Im z_N|}{L}
=
\frac{K_N}{\pi eN}
\longrightarrow0.
\tag{36}
\]

This is the main qualitative point. A local observation need not remain a fixed macroscopic distance from the divisor to inherit the full exponential central-packet obstruction. It may approach the real line at any rate corresponding to a sublinear jet depth, including extremely slowly vanishing macroscopic heights, and still be exponentially blind to a finite transition-time shift.

For any fixed `rho>0`, the two matched controls have transition-time separation `rho` by `(3)`. If the complete future jet in `(10)` is given the sup norm, every Lipschitz decoder of `Lambda_per` on this two-point family therefore has condition number at least

\[
\boxed{
\exp[(b_*-o(1))N].}
\tag{37}
\]

## 4. Boundary, falsifier, and next gate

The quantifiers matter. Equation `(10)` does **not** show that a prescribed fixed root-spacing observation point hides every sublinear jet. At fixed `beta=O(1)`, XF-138 still only certifies the Lambert-W depth `Theta(N/log N)`. Here the observation point is allowed to move outward with the requested jet depth. Nor does `(10)` reach `K_N=theta N` while keeping `|Im z_N|/L->0`; linear jet depth forces a macroscopic Cauchy radius and returns to the XF-137 regime.

So the target-side frontier is now two-dimensional. Merely saying that the probe approaches the divisor (`|Im z_N|=o(L)`) is insufficient: the relevant quantity is its distance in root-spacing units **relative to the derivative depth**. Any proposed stable local decoder must beat the phase law `(6)`, or must use genuinely linear degree-order information while remaining microscopically close to the divisor, or must exploit an observable not controlled by local analytic continuation. The source-specific alternative is unchanged: prove that Xi excludes the XF-133 central packet before target inversion. The accepted Gaussian-reference quotient clue remains live on that side.

The falsifier for `(7)` is explicit: one would need either a failure of the global XF-133 estimate `(13)`, a zero of `Q_s/q_0` inside the disk despite `(17)`, or a derivative order below `(6)` whose Cauchy factorial exceeds the Lambert-W budget `(23)`. None occurs. The matched-control transition separation is inherited unchanged from XF-134.

A directed prior-art audit checked quantitative analytic continuation and heat observability, including the same Trefethen analytic-continuation framework already anchored around XF-137--XF-138 and point/sensor observability results for the heat equation. Those works address generic continuation or observability geometry, not this finite periodic combination of a transition-sharp unit-circle matched control, a moving exterior zero-free radius, and the Lambert-W height-versus-raw-jet law `(6)`. No external theorem is load-bearing here: the proof uses only XF-133, XF-134, XF-136, Cauchy's estimate, Stirling, and the defining identity of `W_0`. No new source anchor is therefore added to `SOURCES.md`.

## Conclusion

The apparent gap between XF-137 and XF-138 is governed by a single geometric parameter: the zero-free Cauchy radius available at the exterior probe. At a submacroscopic center `h_N=o(N)`, the blind jet depth is

\[
\boxed{
J_N(c,h_N)
=
\frac{cN}{W_0(2cN/(e h_N))}+O(1),
\qquad 0<c<b_*.
}
\]

More strongly, for **every** `K_N=o(N)` one can place the probe at height `Theta(K_N/N)` of the period and hide the entire raw logarithmic jet through order `K_N` with essentially the full packet rate `b_*`. Thus `o(L)` proximity by itself is not a cure for the target-side conditioning obstruction; the unresolved local regime is where the probe stays much closer in root-spacing units than the depth of the raw jet, most notably the genuinely degree-order jet near the divisor.