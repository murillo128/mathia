# XF-138 — Lambert-W depth pushes root-spacing jet blindness to the N/log N scale

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE/TRANSITION-CONDITIONING` + `ROOT-SPACING-LOG-JET` + `N-OVER-LOG-N-THRESHOLD` + `ZERO-DELAY` + `UNIT-CIRCLE-MATCHED-CONTROL` + `CROSS-SCALE`. XF-137 shows that the optimized central packet can hide every logarithmic derivative through order `N` when the observation point is moved a macroscopic distance into the exterior. Its explicit remaining loophole is proximity: a degree-order jet only `O(1)` in the `beta` coordinate from the unit-circle line was not covered because the available zero-free Cauchy radius is then only `O(1)`. The same packet nevertheless hides a much larger root-spacing jet than the earlier condition `J_N log J_N=o(N)` records. At any fixed exterior root-spacing point it remains exponentially transition-blind through a sharp Lambert-W depth of order `N/log N`.

Let

\[
b_*
:=
\frac12\sqrt{W_0(2)\bigl(2+W_0(2)\bigr)}
=0.779767136088\ldots
\tag{1}
\]

be the optimized XF-136 packet exponent, and let `N=2M`. Use the XF-134 transition-sharp control with the XF-136 optimal packet depth and write

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

Fix the single exterior observation point

\[
\boxed{\beta_0=2.}
\tag{4}
\]

For any fixed `0<c<b_*`, define

\[
\boxed{
J_N(c)
:=
\left\lfloor
\frac{cN}{W_0(cN/e)}
\right\rfloor .
}
\tag{5}
\]

Then

\[
J_N(c)
=
(c+o(1))\frac{N}{\log N},
\tag{6}
\]

and the complete future raw logarithmic jet through that depth satisfies

\[
\boxed{
\sup_{\substack{s\ge0,\ \rho\ge0\\1\le j\le J_N(c)}}
\left|
\partial_\beta^j\log Q_s(2)
-
\partial_\beta^j\log Q_{s+\rho}(2)
\right|
\le
\exp\!\left[-(b_*-c)N+O(\log N)\right].
}
\tag{7}
\]

Thus for every fixed `epsilon>0`, taking `c=b_*-epsilon` gives an exponentially transition-blind jet of depth

\[
\boxed{
J_N
=
(b_*-\epsilon+o(1))\frac{N}{\log N}.
}
\tag{8}
\]

The point `(4)` is only root-spacing distance from the divisor. In the XF-067 physical coordinate

\[
\beta=-\frac{2\pi iN}{L}z,
\tag{9}
\]

it is

\[
\boxed{
z_0=i\frac{L}{\pi N},}
\tag{10}
\]

while the unit Cauchy disk used below has physical radius `L/(2 pi N)` and remains at least that same radius away from the real line. Equation `(7)` therefore closes a substantial part of XF-137's proximity loophole: moving the observation from a macroscopic exterior point all the way down to a fixed number of root spacings does **not** make every large raw jet transition-sensitive. One must at least cross the `N/log N` derivative scale before this central-packet obstruction ceases to certify exponential blindness.

## 1. The optimized packet is exponentially tiny on a fixed root-spacing disk

As in XF-135--XF-137, write

\[
Q_s(\beta)=q_0(\beta)+u_s(\beta),
\tag{11}
\]

where `u_s=t_* Delta E(-e^(beta/N),s)`, `|t_*|<=2`, and the optimized packet amplitude obeys

\[
A_N
:=
\frac{(r!)^2}{(M^2-r^2)^r}
=
\exp[-b_*N+O(\log N)].
\tag{12}
\]

XF-133 gives the simultaneous complex-patch estimate

\[
|u_s(\gamma)|
\le
2e^{|\gamma|}A_N,
\qquad s\ge0.
\tag{13}
\]

Take the fixed disk

\[
D:=\{\gamma:|\gamma-2|\le1\}.
\tag{14}
\]

On `D`,

\[
|\gamma|\le3,
\qquad
\operatorname{Re}\gamma\ge1,
\tag{15}
\]

and therefore

\[
|q_0(\gamma)|
=|1+e^\gamma|
\ge e-1.
\tag{16}
\]

Consequently

\[
\left|\frac{u_s(\gamma)}{q_0(\gamma)}\right|
\le
\frac{2e^3}{e-1}A_N
=
\exp[-b_*N+O(\log N)]
\tag{17}
\]

uniformly on `D` and uniformly for every `s>=0`. For large `N` the right side is below `1/2`, so

\[
F_s(\gamma)
:=
\log\!\left(1+\frac{u_s(\gamma)}{q_0(\gamma)}\right)
\tag{18}
\]

is analytic on `D` with

\[
\boxed{
\sup_{\gamma\in D}|F_s(\gamma)|
\le
\exp[-b_*N+O(\log N)].
}
\tag{19}
\]

The estimate is independent of the heat time. In particular it applies simultaneously to `F_s` and `F_(s+rho)` for every finite `rho>=0`.

## 2. Fixed-radius Cauchy costs exactly one factorial

The common stationary carrier cancels from every positive logarithmic derivative:

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

Cauchy's estimate on the unit disk `(14)` therefore gives

\[
\boxed{
\left|
\partial_\beta^j\log Q_s(2)
-
\partial_\beta^j\log Q_{s+\rho}(2)
\right|
\le
\exp[-b_*N+O(\log N)]\,j!
}
\tag{21}
\]

for every `j>=1`, uniformly in `s` and `rho`.

This is the root-spacing counterpart of XF-137's growing-disk estimate. There the radius was proportional to `N`, so the denominator `R^j` could pay a linear-depth jet. Here the radius is fixed, so the factorial itself determines the crossover scale.

## 3. Lambert W inverts the factorial budget

Let

\[
x_N(c)
:=
\frac{cN}{W_0(cN/e)}.
\tag{22}
\]

By the defining identity `W(y)e^(W(y))=y`, one has the exact relation

\[
\boxed{
x_N(c)\log\!\left(\frac{x_N(c)}e\right)=cN.}
\tag{23}
\]

Since `J_N(c)=floor(x_N(c))`, Stirling's formula gives

\[
\log(J_N(c)!)
\le
cN+O(\log N).
\tag{24}
\]

Combining `(21)` and `(24)` proves `(7)`.

The standard large-argument expansion

\[
W_0(y)=\log y-\log\log y+O(1)
\tag{25}
\]

then yields `(6)`. More explicitly,

\[
J_N(c)
=
\frac{cN}
{\log N-\log\log N+O(1)}.
\tag{26}
\]

The earlier XF-135 hypothesis `J_N log(J_N+2)=o(N)` sits strictly below this boundary. Equation `(7)` reaches the critical factorial regime itself: any fixed fraction `c<b_*` of the available packet exponent can be spent on the Cauchy factorial while leaving the residual exponential transition-blindness rate `b_*-c`.

The theorem deliberately stops short of claiming that `c=b_*` is a sharp observability threshold. At that endpoint the leading packet exponent and the leading Stirling exponent balance, and the `O(log N)` packet prefactor is no longer enough to force exponential decay. Nor does failure of this proof for `c>b_*` imply that such a jet detects the transition. The result is a certified lower boundary on the raw derivative depth required to escape this matched-control obstruction.

## 4. Physical normalization and transition conditioning

From `(9)`,

\[
\left(\frac{L}{2\pi N}\right)^j
\partial_z^j
=(-i)^j\partial_\beta^j.
\tag{27}
\]

Thus `(7)` is exactly the same estimate for the root-spacing-normalized physical logarithmic derivatives at the point `(10)`. The observation is not macroscopically separated from the zero line: both its height and its analytic safety radius are `Theta(L/N)`.

For any fixed `rho>0`, the two controls still satisfy

\[
|\Lambda_{\rm per}(E_{\rm c})
-
\Lambda_{\rm per}(E_{{\rm c},\rho})|
=\rho.
\tag{28}
\]

If `Obs_(N,c)` denotes the complete future jet in `(7)` with the sup norm, then every Lipschitz decoder of `Lambda_per` on this two-point matched-control family has condition number at least

\[
\boxed{
\exp[(b_*-c)N-O(\log N)]
}
\tag{29}
\]

up to the fixed factor `rho`. As in XF-134--XF-137, the observation bound itself is uniform in `rho`, so the statement is about target-side conditioning rather than the scale of the actual Xi Newman constant.

A common known analytic reference does not alter the conclusion for positive logarithmic derivatives: its logarithmic jet cancels from `(20)` exactly, as already noted in XF-135. The accepted Gaussian-reference clue therefore remains a source-specific route, not a target-side cure for this matched-control conditioning.

## 5. Prior-art boundary and next gate

Cauchy's derivative estimate, Stirling asymptotics, and the Lambert-W inversion in `(22)`--`(25)` are classical. The neighboring analytic-continuation literature already audited in XF-137, including Trefethen's quantitative treatment of ill-conditioning, explains why exact local analytic data can have severe conditioning losses. A directed follow-up search did not locate a result matching the present finite periodic combination: a transition-sharp unit-circle heat pair, complete zero-delay future history, a fixed root-spacing exterior observation point, and a Lambert-W `N/log N` raw logarithmic-jet blindness threshold. No external theorem is load-bearing in `(7)`, so no new source anchor is added to `SOURCES.md`.

The remaining target-side loophole is now quantitatively narrower than XF-137 stated. A root-spacing jet of fixed or slowly growing order is far from enough, and even a jet containing almost `b_*N/log N` raw normalized derivatives can remain exponentially blind. What is not settled is the regime beyond this certified depth, especially whether derivatives of order `Theta(N/log N)` with coefficient above `b_*`, or a genuinely degree-order root-spacing jet, necessarily see the discriminant with useful conditioning. The alternative remains to prove an Xi-specific source theorem that excludes the central packet before any such inversion is attempted.

## Conclusion

The macroscopic displacement in XF-137 is needed only to hide a **linear-depth** raw jet. At a fixed root-spacing exterior point, the optimized central packet still hides a much deeper jet than the previous `J log J=o(N)` statement makes explicit. The exact factorial budget is inverted by Lambert W: for every `c<b_*`, all normalized logarithmic derivatives through

\[
\boxed{
J_N(c)=\frac{cN}{W_0(cN/e)}+O(1)
=(c+o(1))\frac{N}{\log N}
}
\]

remain exponentially insensitive to an order-one change in periodic transition time. The next local conditioning gate is therefore not merely "take many derivatives near the divisor"; it begins at the `N/log N` scale.