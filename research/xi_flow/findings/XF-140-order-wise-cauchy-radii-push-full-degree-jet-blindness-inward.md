# XF-140 — order-wise Cauchy radii push full-degree jet blindness inward

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE/TRANSITION-CONDITIONING` + `LINEAR-DEPTH-LOG-JET` + `ORDER-WISE-CAUCHY` + `ZERO-DELAY` + `UNIT-CIRCLE-MATCHED-CONTROL` + `CROSS-SCALE`. XF-137 proves that one macroscopic exterior disk can hide a full degree-order logarithmic heat jet, and XF-139 gives the complementary moving-height law for every sublinear jet. The remaining linear-depth calculation in XF-137 uses one common Cauchy radius for every derivative order. That common-radius requirement is not intrinsic to the observation: each derivative at the same center may be estimated on its own zero-free disk. Optimizing those radii order by order gives a stronger linear-depth height law and moves the certified full-degree blind region strictly closer to the divisor.

Let

\[
b_*
:=
\frac12\sqrt{W_0(2)\bigl(2+W_0(2)\bigr)}
=0.779767136088\ldots
\tag{1}
\]

be the optimized XF-136 packet exponent. For even degree `N=2M`, use the XF-134 transition-sharp matched control at the XF-136 optimal packet depth and, as in XF-137--XF-139, write

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

Fix `0<theta<=1`. For `0<kappa<theta/2`, define the linear-depth Cauchy cost

\[
\boxed{
\Psi_\theta(\kappa)
:=
2\kappa
+\theta\left(\log\frac{\theta}{\kappa}-1\right).
}
\tag{4}
\]

Since `b_*>log 2`, there is a unique `kappa_*(theta) in (0,theta/2)` satisfying

\[
\Psi_\theta(\kappa_*(\theta))=b_*.
\tag{5}
\]

It has the explicit Lambert-W form

\[
\boxed{
\kappa_*(\theta)
=
-\frac{\theta}{2}
W_0\!\left(-2e^{-1-b_*/\theta}\right).
}
\tag{6}
\]

For every fixed

\[
\boxed{
\kappa_*(\theta)<\kappa<\min\left\{\frac\theta2,\frac{b_*}{2}\right\},
}
\tag{7}
\]

observe at the single exterior center

\[
\boxed{
\beta_N=\kappa N+1.
}
\tag{8}
\]

Then the complete future raw logarithmic jet through order `floor(theta N)` satisfies

\[
\boxed{
\sup_{\substack{s\ge0,\ \rho\ge0\\1\le j\le\lfloor\theta N\rfloor}}
\left|
\partial_\beta^j\log Q_s(\beta_N)
-
\partial_\beta^j\log Q_{s+\rho}(\beta_N)
\right|
\le
\exp\!\left[-c_{\theta,\kappa}N+O(\log N)\right],
}
\tag{9}
\]

where

\[
\boxed{
c_{\theta,\kappa}:=b_*-\Psi_\theta(\kappa)>0.}
\tag{10}
\]

Thus every fixed linear fraction of the degree has an explicit inward height threshold within the XF-133 central-packet envelope. In particular, at full degree `theta=1`,

\[
\boxed{
\kappa_*:=\kappa_*(1)
=-\frac12W_0\!\left(-2e^{-1-b_*}\right)
=0.319704509958\ldots .
}
\tag{11}
\]

For every fixed `kappa>kappa_*` sufficiently below `b_*/2`, **all logarithmic derivatives `1<=j<=N` remain exponentially transition-blind at the same center**. In the XF-067 physical coordinate this lowers the certified limiting exterior height from the XF-137 center `0.0620518971... L` to any height strictly above

\[
\boxed{
\frac{\kappa_*}{2\pi}L
=0.05088255309\ldots L.
}
\tag{12}
\]

The threshold `(12)` is a boundary of this order-wise Cauchy argument, not a universal observability threshold.

## 1. Each derivative may use its own zero-free disk

XF-139 records the global XF-133 packet estimate in the form

\[
Q_s(\beta)=q_0(\beta)+u_s(\beta),
\qquad
|u_s(\gamma)|\le 2e^{|\gamma|}A_N,
\tag{13}
\]

uniformly for `s>=0`, where

\[
A_N
=
\exp[-b_*N+O(\log N)].
\tag{14}
\]

Put `h_N=kappa N+1`. For each derivative order `j`, choose the radius

\[
\boxed{
r_{j,N}:=\min\left\{\frac j2,\kappa N\right\}.
}
\tag{15}
\]

Every disk

\[
D_{j,N}:=\{\gamma:|\gamma-h_N|\le r_{j,N}\}
\tag{16}
\]

stays in `Re gamma>=1`. Hence

\[
|q_0(\gamma)|
=|1+e^\gamma|
\ge
(1-e^{-1})e^{\Re\gamma}.
\tag{17}
\]

Also `|gamma|<=h_N+r_(j,N)`. Combining `(13)`--`(17)` gives

\[
\boxed{
\sup_{\gamma\in D_{j,N}}
\left|\frac{u_s(\gamma)}{q_0(\gamma)}\right|
\le
\exp[-b_*N+2r_{j,N}+O(\log N)]
}
\tag{18}
\]

uniformly in the complete future history. Condition `(7)` includes `2kappa<b_*`, so `(18)` is exponentially small on **every** disk `(16)`. Therefore

\[
F_s(\gamma)
:=
\log\!\left(1+\frac{u_s(\gamma)}{q_0(\gamma)}\right)
\tag{19}
\]

is analytic there for all sufficiently large `N`, with the same exponential bound as `(18)`.

The point is that the disks need not coincide. The observation consists only of derivatives at `h_N`; Cauchy's formula for the `j`-th derivative is free to use a radius chosen for that `j`. XF-137 deliberately used one radius to control the whole jet at once. That forces the common radius to pay for low derivative orders even when a much larger radius would only help the high orders. Equation `(15)` removes that artificial coupling.

## 2. Order-wise optimization gives a two-regime exact exponent

The common carrier cancels from every positive logarithmic derivative, so Cauchy's estimate on `D_(j,N)` yields

\[
\left|
\partial_\beta^j\log Q_s(h_N)
-
\partial_\beta^j\log Q_{s+\rho}(h_N)
\right|
\le
\exp[-b_*N+2r_{j,N}+O(\log N)]
\frac{j!}{r_{j,N}^j}.
\tag{20}
\]

There are two regimes.

If `j<=2kappa N`, then `r_(j,N)=j/2`. Stirling gives

\[
\log\!\left(
 e^{2r_{j,N}}\frac{j!}{r_{j,N}^j}
\right)
=
j\log2+O(\log N).
\tag{21}
\]

Thus the `j`-th derivative costs only `j log 2` in the exponent. This is exactly the gain lost when all orders are forced to share one disk: the exponentially small factor `(2/e)^j` from `j!/(j/2)^j` may be used for the high derivative because the low derivatives are estimated on smaller disks of their own.

If `j>2kappa N`, then `r_(j,N)=kappa N`. Writing `x=j/N`, Stirling gives

\[
\log\!\left(
 e^{2r_{j,N}}\frac{j!}{r_{j,N}^j}
\right)
=
N\left[
2\kappa+x\left(\log\frac{x}{\kappa}-1\right)
\right]
+O(\log N).
\tag{22}
\]

For `x>2kappa`, the bracket in `(22)` is strictly increasing because its derivative is `log(x/kappa)>0`. At `x=2kappa` it equals `2kappa log 2`, exactly matching `(21)`. Consequently the worst order in the entire jet `1<=j<=theta N` is the top order, and its cost is precisely `Psi_theta(kappa)` from `(4)`. Equations `(20)`--`(22)` prove `(9)`.

This is an exact improvement of the **certified bound**, not a claim that XF-137's observation itself was suboptimal. The data are the same type of logarithmic jet; only the analytic estimate has stopped imposing a common auxiliary disk on all derivative orders.

## 3. The inward boundary is explicit and unique

For `0<kappa<theta/2`,

\[
\frac{d}{d\kappa}\Psi_\theta(\kappa)
=2-\frac\theta\kappa<0,
\tag{23}
\]

while

\[
\Psi_\theta(\kappa)\to\infty
\quad(\kappa\downarrow0),
\qquad
\Psi_\theta(\theta/2)=\theta\log2<b_*.
\tag{24}
\]

Hence `(5)` has exactly one solution. Setting `x=2kappa/theta` converts `(5)` into

\[
x-\log x+\log2-1=\frac{b_*}{\theta},
\tag{25}
\]

and therefore

\[
x e^{-x}=2e^{-1-b_*/\theta},
\tag{26}
\]

which gives the principal-branch formula `(6)`. The principal branch is the correct one because `x in (0,1)`; the other real Lambert-W branch corresponds to `x>1` and lies outside the inward regime.

At `theta=1`, the full-degree exponent is

\[
\boxed{
c_{1,\kappa}
=b_*-\left(2\kappa-1-\log\kappa\right).}
\tag{27}
\]

It is positive exactly for `kappa_*<kappa<1/2` as far as the factorial balance is concerned. The present proof additionally keeps `kappa<b_*/2` so that every order-wise disk is uniformly zero-free directly from the XF-133 envelope. Since

\[
\kappa_*=0.3197045\ldots
<
\frac{b_*}{2}=0.3898835\ldots,
\tag{28}
\]

there is a nonempty interval in which the new inward improvement is fully certified. For example, `kappa=0.35` gives

\[
c_{1,0.35}=0.0299450\ldots,
\tag{29}
\]

while placing the observation at physical height `0.0557042... L`, already strictly inside the XF-137 center.

For any fixed `rho>0`, the two matched controls still have transition-time separation `rho` by `(3)`. Thus every Lipschitz decoder of `Lambda_per` from the complete future jet in `(9)` has condition number at least

\[
\exp[c_{\theta,\kappa}N-O(\log N)]
\tag{30}
\]

on this two-point family.

## 4. Boundary, prior art, and falsification

The improvement does **not** reach the root-spacing or vanishing-macroscopic-height regime for a degree-order jet. Even at the limiting certified full-degree value `(11)`, the observation height remains a fixed positive fraction of `L`. XF-139 therefore remains the correct statement for sublinear jets approaching the divisor, and the genuinely hard target-side gate is still a linear-depth/nonlocal observable much closer to the real divisor line.

Nor does `(11)` assert a universal lower bound on the height at which transition information becomes stable. It is the solution of the explicit XF-133 packet envelope plus circular Cauchy estimates. A stronger packet estimate, a noncircular contour exploiting more of the carrier geometry, or an Xi-specific source restriction could move or remove this boundary. Failure of `(9)` below `kappa_*(theta)` would only mean that this certificate has exhausted its exponential budget.

The use of derivative-dependent Cauchy radii is classical rather than new complex analysis. A directed prior-art audit included Folkmar Bornemann, *Accuracy and Stability of Computing High-Order Derivatives of Analytic Functions by Cauchy Integrals* (arXiv:0910.1841), which explicitly studies order-dependent radius optimization for high analytic derivatives, and Lloyd N. Trefethen, *Quantifying the ill-conditioning of analytic continuation*, BIT Numerical Mathematics 60 (2020), 901--915, DOI `10.1007/s10543-020-00802-7`. Those works establish the neighboring analytic-continuation/derivative-conditioning context. They do not supply the transition-sharp unit-circle matched controls, the XF-133 packet exponent, or the phase boundary `(4)`--`(12)`. No external theorem is load-bearing in the proof, so `SOURCES.md` needs no new dependency anchor.

A direct falsifier of `(9)` would be a failure of the uniform packet estimate `(13)`, a zero of `Q_s/q_0` on one of the disks despite `(18)`, or an order `j<=theta N` whose Stirling exponent exceeds `(4)`. The first is inherited from XF-133/XF-139, the second is excluded by `2kappa<b_*`, and `(21)`--`(22)` show that the third cannot occur.

## Consequence for the Xi-flow frontier

XF-137's macroscopic full-jet obstruction was not pinned to its symmetric center `beta=(b_*/2)N`. Once the auxiliary Cauchy radius is allowed to depend on derivative order, the same transition-sharp central packet hides every degree-order derivative at centers substantially closer to the unit-circle line. For the full jet, the explicit inward limit of this proof is `kappa_*=0.319704509958...`, corresponding to `0.05088255309... L` in physical height.

This sharpens but does not change the qualitative frontier recorded by the Xi-flow Mind: finite and sublinear exterior tomography is already closed, and even linear-depth local tomography remains exponentially ill-conditioned over a sizeable macroscopic region. The next materially different target-side test must push degree-order information much closer to the divisor or use genuinely nonlocal structure; the source-side alternative remains to prove that Xi itself cannot realize the central packet.

## Conclusion

A full logarithmic jet does not require one common analytic safety radius. Estimating the `j`-th derivative on its own radius `min(j/2,kappa N)` converts the XF-133 packet budget into the exact linear-depth cost

\[
\Psi_\theta(\kappa)
=2\kappa+\theta\left(\log\frac\theta\kappa-1\right).
\]

For every `theta in (0,1]`, exponential transition blindness persists whenever `Psi_theta(kappa)<b_*` in the certified right-half-plane regime. At full degree this pushes the limiting observation height from the XF-137 center `0.0620519... L` down to any fixed height strictly above `0.0508826... L`, while retaining an exponential condition-number obstruction for the complete future heat history.