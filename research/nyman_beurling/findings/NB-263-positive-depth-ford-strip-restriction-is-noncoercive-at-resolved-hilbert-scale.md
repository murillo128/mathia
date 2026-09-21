# NB-263 — Positive-depth Ford strip restriction is noncoercive at resolved Hilbert scale

> **Representation:** _Nyman–Beurling / resolved signed-carrier destination interface._ The line-specific input is the Euler-normalized `H`-separated carrier dictionary of `NB-255`--`NB-262`, with `J=R/H`, near-full span parameter `m=J/K`, and legal complex Ford coordinate `w=R[(gamma-t_0)+i(1-beta)]`. The generic engine is an approximate-annihilator theorem for Fourier–Laplace restriction strictly inside the decaying half-plane, followed by a cell-average discretization. The result corrects the frontier left by `NB-262`: suppressing a fixed, or even a preassigned growing, horizontal shallow strip at positive Ford depth is **not** Hilbert-coercive in the signed scalar class. The cost can be hidden in arbitrarily large coefficient conditioning and exported outside the prescribed strip while the resolved shell-Hilbert norm tends to zero. This does not control the full `Theta(J)` hard window, total variation, or the final Hardy/Nyman distance.

**Date:** 2026-09-21  
**Status:** `EXACT-DERIVED + SIGNED-CARRIER + EULER-NORMALIZED + FOURIER-LAPLACE-RESTRICTION + APPROXIMATE-ANNIHILATOR + HAHN-BANACH + CELL-DISCRETIZATION + VANISHING-HILBERT-COST + SHALLOW-STRIP-SUPPRESSION + MATCHED-PACKET-EXCLUSION-ON-COVERED-STRIP + NB-262-ROUTE-CORRECTION + METHOD-BOUNDARY + SOURCE-ONLY + FRESH-PRIOR-ART-AUDIT`.

`NB-262` proves that the unique minimum-Hilbert carrier satisfying only the Euler anchor and one exact shallow notch develops a side-lobe of size `Theta(m/u)` on the natural horizontal Ford scale `x~m`, where

\[
m=\frac JK,
\qquad
u:=X(1-\beta)\sim\log m.
\]

That side-lobe supports a shorter carrier-locked matched packet and therefore kills the **one-notch minimum-energy design**. It deliberately leaves open whether extra horizontal constraints can flatten the side-lobe without making the resolved Hilbert cost coercive.

They can, if no independent bound is placed on conditioning and if the horizontal/depth region is prescribed before the resolved rank `K` is allowed to grow. The key fact is stronger than a finite interpolation construction. Let

\[
E_{m}(a,U,B)
:=
\left\{
-\frac{u}{Ym}+iy:
 a\le u\le U,\ |y|\le B
\right\},
\qquad
0<a\le U<\infty,\quad B>0.
\]

For every `epsilon>0` there is a real signed density `f in L^2(0,1)` such that

\[
\boxed{
\int_0^1f(t)\,dt=1,
\qquad
\sup_{z\in E_m(a,U,B)}
\left|\int_0^1 f(t)e^{zt}\,dt\right|<\epsilon.
}
\tag{1}
\]

Thus evaluation on any compact Ford strip staying a positive distance from the Euler anchor does not continuously control the anchor functional. The proof is an exact Hahn--Banach/Riesz contradiction: if the anchor were bounded by that strip restriction, it would be representable by a finite measure supported strictly in the decaying half-plane; analytic continuation would then force a function identically equal to one to decay exponentially on the positive real axis.

Discretizing `f` into `K` cell masses on the resolved `H`-grid preserves the Euler anchor **exactly** and costs only `K^{-1/2}` in coefficient `ell^2`. Since `K` may be taken after the finite strip and the particular approximate annihilator have been fixed, the physical resolved shell-Hilbert cost can be made arbitrarily small while the carrier is uniformly arbitrarily small on the whole strip.

Consequently, one may diagonalize over growing horizontal ranges and shrinking positive lower depths. For any predeclared finite sequence of target boxes, suppression levels and span parameters, `K` can be chosen large enough at each stage to obtain

\[
H^{1/2}\|h_{\nu_J}\|_2\to0
\]

and simultaneously

\[
\sup_{
\substack{|x|\le mB\\
a\le X(1-\beta)\le U}}
|C_J(x+iX(1-\beta)/Y)|\to0.
\]

In particular, choosing a box containing

\[
|x|\le Bm,
\qquad
X(1-\beta)=\log m+O(1)
\]

removes the complete packet-scale side-lobe geometry exhibited by the minimum-Hilbert optimizer in `NB-262`. If the suppression level is `epsilon=o(1/B)`, even the absolute contribution of every carrier-locked packet of the maximal `O(mB)` population inside that covered band is `o(1)` at damping `e^{-u}~1/m`.

The price is deliberately **not** bounded here. The witness `f` may have enormous `L^2` norm and still larger `L^1`/variation, and the discrete carrier may create huge side-lobes immediately outside the prescribed box. The result therefore does not produce a successful Nyman approximant. It proves instead that a no-go based only on a fixed positive-depth strip and resolved `ell^2` cost cannot close the signed scalar route.

## 1. Positive-depth Fourier–Laplace restriction does not control the Euler anchor

Fix finite parameters

\[
m>0,
\qquad
0<a\le U,
\qquad
B>0,
\qquad
Y>0,
\]

and let

\[
E:=E_m(a,U,B)
\subset
\{z:\Re z\le-a/(Ym)\}.
\]

Define

\[
T:L^2(0,1)\to C(E),
\qquad
(Tf)(z):=\int_0^1f(t)e^{zt}\,dt,
\]

and the Euler-anchor functional

\[
L(f):=\int_0^1f(t)\,dt.
\]

### Claim

For every `epsilon>0` there exists `f in L^2(0,1)` with

\[
L(f)=1,
\qquad
\|Tf\|_{C(E)}<\epsilon.
\tag{2}
\]

Equivalently,

\[
\boxed{
\inf_{L(f)=1}\|Tf\|_{C(E)}=0.
}
\tag{3}
\]

### Proof

Assume the contrary. By homogeneity there would be a constant `A<infinity` such that

\[
|L(f)|\le A\|Tf\|_{C(E)}
\qquad
\text{for every }f\in L^2(0,1).
\tag{4}
\]

The map `T` is injective. Indeed, if `Tf=0` on `E`, then for any fixed `u in [a,U]` the entire Fourier--Laplace transform

\[
z\mapsto\int_0^1f(t)e^{zt}\,dt
\]

vanishes on the nontrivial vertical segment

\[
-u/(Ym)+i[-B,B].
\]

The identity theorem makes it identically zero, and Fourier uniqueness then gives `f=0`.

Hence (4) defines a bounded functional on `Ran(T)` by

\[
\ell(Tf):=L(f).
\]

Hahn--Banach extends it to all of `C(E)`. By the Riesz representation theorem there is a finite complex Borel measure `mu` on `E` for which

\[
L(f)
=
\int_E(Tf)(z)\,d\mu(z)
\qquad
\text{for every }f\in L^2(0,1).
\]

Fubini therefore gives

\[
1
=
\int_Ee^{zt}\,d\mu(z)
\tag{5}
\]

for almost every `t in [0,1]`, hence for every such `t` by continuity. The right side is an entire function of `t`; the identity theorem extends (5) to every complex `t`. But for positive real `t`,

\[
\left|
\int_Ee^{zt}\,d\mu(z)
\right|
\le
\|\mu\|_{TV}
\exp\!\left(-\frac{at}{Ym}\right)
\longrightarrow0,
\]

contradicting (5). This proves (3).

Because `E` is invariant under complex conjugation, a complex witness may be replaced by its real part: `L(Re f)=1` and

\[
T(\Re f)(z)
=
\frac12\left(Tf(z)+\overline{Tf(\bar z)}\right).
\]

Thus (2) holds already for real signed densities. Complex coefficients are not needed for the noncoercivity.

The strict inequality `a>0` is load-bearing. If the set contains the Euler anchor `z=0`, then `Tf(0)=L(f)=1`, so uniform suppression is impossible. The theorem says that **every compact region separated from that anchor by any positive depth loses coercive access to it**.

## 2. Cell discretization preserves the anchor and amortizes arbitrary witness norm

Fix one real witness `f` from (2), and write

\[
M_f:=\|f\|_2.
\]

For an integer `K>=1`, partition `[0,1]` into

\[
I_j=[j/K,(j+1)/K),
\qquad
0\le j<K,
\]

and define

\[
\boxed{
c_j:=\int_{I_j}f(t)\,dt.
}
\tag{6}
\]

Then

\[
\sum_{j=0}^{K-1}c_j=1
\tag{7}
\]

exactly, while Cauchy--Schwarz on each cell gives

\[
\boxed{
\sum_{j=0}^{K-1}|c_j|^2
\le
\frac{M_f^2}{K}.
}
\tag{8}
\]

Set

\[
J:=mK
\]

for the moment; rounding `J/m` changes none of the conclusions. The resolved carrier is

\[
C_J(w)
:=
\sum_{j=0}^{K-1}c_je^{ijw/J}.
\tag{9}
\]

At the legal Ford coordinate

\[
w=my+i\frac uY,
\]

formula (9) becomes

\[
C_J\!\left(my+i\frac uY\right)
=
\sum_jc_j
\exp\!\left[
\left(iy-\frac{u}{Ym}\right)\frac jK
\right].
\tag{10}
\]

This is the left-endpoint cell discretization of `Tf` at

\[
z=-u/(Ym)+iy.
\]

If

\[
L_E:=B+\frac{U}{Ym},
\]

then `Re z<=0` and the derivative of `e^{zt}` on `[0,1]` has modulus at most `|z|<=L_E`. Hence

\[
\boxed{
\sup_{\substack{a\le u\le U\\|y|\le B}}
\left|
C_J\!\left(my+i\frac uY\right)
-(Tf)\!\left(-\frac{u}{Ym}+iy\right)
\right|
\le
\frac{L_E\|f\|_1}{K}
\le
\frac{L_EM_f}{K}.
}
\tag{11}
\]

For this fixed witness, taking `K` sufficiently large therefore gives

\[
\sup_{\substack{a\le u\le U\\|y|\le B}}
\left|C_J\!\left(my+i\frac uY\right)\right|
<2\epsilon,
\tag{12}
\]

while simultaneously

\[
\|c\|_2\le\frac{M_f}{\sqrt K}.
\tag{13}
\]

This order of quantifiers is the mechanism: the strip is fixed first; its approximate-annihilator norm may be arbitrarily bad but remains finite; the resolved rank `K` is then made large enough to amortize that finite norm in shell `ell^2`.

## 3. The discretized coefficients are legal Euler-normalized resolved sources

Return to the source normalization of `NB-255`--`NB-262`. Let

\[
\xi_j=jH,
\qquad
H=\frac RJ,
\qquad
0\le j<K,
\]

and place the Euler-normalized signed measure

\[
\lambda_J:=\sum_{j=0}^{K-1}c_j\delta_{\xi_j}.
\]

By (7), `lambda_J(R)=1`. The physical coefficient measure is

\[
d\nu_J(\xi)=e^{r\xi/X}d\lambda_J(\xi),
\]

so its exact Euler normalization is

\[
\int e^{-r\xi/X}d\nu_J(\xi)=1.
\]

The occupied span is

\[
W=(K-1)H\sim KH
=\frac{KR}{J}
=\frac Rm,
\]

and therefore

\[
\frac WX\sim\frac1{Ym}.
\]

Along any diagonal with `m->infinity`, the physical Euler tilt is uniformly `1+o(1)`. The translated `H`-shells are disjoint, so the same identity used in `NB-257`--`NB-262` yields

\[
H^{1/2}\|h_{\nu_J}\|_2
=(1+o(1))\|\phi\|_2\|c\|_2.
\]

Combining with (13),

\[
\boxed{
H^{1/2}\|h_{\nu_J}\|_2
\le
(1+o(1))\|\phi\|_2\frac{M_f}{\sqrt K}.
}
\tag{14}
\]

Thus the strip can be flattened while the normalized resolved source-Hilbert cost tends to zero. Nothing in this step claims that the final Hardy projection or Nyman distance has the same norm.

## 4. A diagonal family suppresses any preassigned growing positive-depth strip

The fixed-parameter lemma can be diagonalized without requiring a quantitative singular-value estimate.

Choose arbitrary sequences

\[
m_n\to\infty,
\qquad
0<a_n\le U_n<\infty,
\qquad
B_n<\infty,
\qquad
\epsilon_n\downarrow0,
\tag{15}
\]

where `a_n` may itself tend to zero and `B_n,U_n` may tend to infinity. For each `n`, apply Section 1 to the compact rectangle

\[
E_{m_n}(a_n,U_n,B_n)
\]

and choose a witness `f_n` with anchor one and strip norm below `epsilon_n/2`. Its norm `M_n=||f_n||_2` may grow with no declared rate.

Now choose `K_n` after `f_n` so large that all of

\[
\frac{M_n}{\sqrt{K_n}}<\epsilon_n,
\qquad
\frac{(B_n+U_n/(Ym_n))M_n}{K_n}<\frac{\epsilon_n}{2},
\qquad
B_n=o(K_n),
\qquad
U_n=o(m_nK_n)
\tag{16}
\]

hold, and also make `log K_n/m_n -> infinity` if the conservative `NB-255`--`NB-262` regime `m=o(log J)` is desired. Put

\[
J_n=m_nK_n.
\]

The external height parameter may then be chosen sufficiently large that the inherited conservative condition `J_n<=log Q_n` holds; set `R_n=Q_n^{2/3}(log Q_n)^{1/3}`, `X_n=YR_n`, and `H_n=R_n/J_n` exactly as in the existing Ford normalization.

Equations (12)--(16) give

\[
\boxed{
H_n^{1/2}\|h_{\nu_{J_n}}\|_2\to0
}
\tag{17}
\]

and

\[
\boxed{
\sup_{
\substack{|x|\le m_nB_n\\
a_n\le u\le U_n}}
\left|C_{J_n}\!\left(x+i\frac uY\right)\right|
\le\epsilon_n.
}
\tag{18}
\]

The auxiliary conditions `B_n=o(K_n)` and `U_n=o(J_n)` also keep the original smooth shell argument

\[
\frac{1}{J_n}\left(x+i\frac uY\right)
\]

uniformly small on the box, so the fixed shell envelope remains `F(0)+o(1)` there.

This diagonal statement is intentionally nonquantitative in `K_n`. It says that **no preassigned sub-full positive-depth box can be coercive merely because its horizontal or vertical extent grows**. A coercive theorem must tie the covered region quantitatively to the same rank/conditioning resource used to build the carrier.

## 5. The `NB-262` side-lobe packet can be removed inside the covered strip

Take the live depth

\[
u=\log m+d,
\qquad |d|\le D,
\]

and choose `a,U` so that this depth range lies inside the box. Let the horizontal coverage be

\[
|x|\le mB.
\]

Carrier-locked ordinates have Ford spacing `Theta(1)`, so the total number of such points in this band is `O(mB)`. Every pole at depth `u=log m+O(1)` carries the Ford damping

\[
e^{-u}=\Theta(m^{-1}).
\]

If (18) holds with carrier supremum `epsilon`, then, before using any phase cancellation, the absolute contribution of **every** carrier-locked packet contained in the covered box is bounded by

\[
O(mB)\cdot O(m^{-1})\cdot O(\epsilon)
=O(B\epsilon),
\tag{19}
\]

up to the uniformly bounded smooth envelope and the fixed normalization factors already present in `NB-261`--`NB-262`.

Thus choosing

\[
\epsilon_n=o(B_n^{-1})
\]

forces the complete matched packet contribution inside the box to be `o(1)`. In particular, the `Theta(log m)` packet around the minimum-Hilbert side-lobe at `x=Theta(m)` from `NB-262` is not a universal signed obstruction. It is a property of that two-constraint optimizer, exactly as `NB-262`'s own boundary section cautioned.

This is a substantive route correction: adding enough horizontal freedom can flatten the entire previously exposed packet scale without paying in resolved `ell^2`, provided one permits uncontrolled conditioning and then takes enough resolved channels.

## 6. What the construction does not suppress

The result leaves three genuinely different costs uncontrolled.

First, it says nothing uniform about coefficient total variation. The Hahn--Banach witness can have arbitrarily large `L^1` and `L^2` norm as the strip approaches the Euler anchor or grows. Its cell averages can therefore carry enormous `ell^1` variation. The total-variation currency isolated by `NB-255` has not disappeared; it is precisely where this noncoercive construction is free to pay.

Second, (18) is a diagonal statement for a region prescribed before `K_n` is chosen. It does **not** suppress a fixed positive fraction of the full hard Ford width

\[
|x|=O(J_n),
\]

which corresponds to `|y|=O(K_n)`. The proof gives no right to set `B_n=cK_n` after seeing the rank. This is the main surviving horizontal distinction.

Third, (17) is the resolved disjoint-shell source cost, not the final Nyman approximation distance. Large variation and side-lobes outside the controlled box may survive or be amplified by the exact Hardy projection. Conversely, Hardy structure could also cancel some source-side cost. A successful scalar construction must still be checked at that destination.

The Euler anchor itself is never suppressed. The exact normalization enforces

\[
C_J(0)=1.
\]

The diagonal may take `a_n->0`, but only by letting the conditioning and the required `K_n` deteriorate without bound. No uniform estimate up to `u=0` follows.

## 7. Prior-art and novelty audit

The generic instability behind Section 1 is classical in neighboring language. Finite/truncated Fourier and Laplace transforms are compact, injective inverse problems with rapidly decaying singular values; Roy Lederman and Vladimir Rokhlin, *On the Analytical and Numerical Properties of the Truncated Laplace Transform I*, SIAM J. Numer. Anal. 53 (2015), 1214--1235, DOI `10.1137/140990681`, develops the singular system of the truncated Laplace transform. Lederman and Stefan Steinerberger, *Stability Estimates for Truncated Fourier and Laplace Transforms*, Integral Equations Operator Theory 87 (2017), 529--543, DOI `10.1007/s00020-017-2364-z`, gives quantitative stability boundaries. Lloyd N. Trefethen, *Quantifying the ill-conditioning of analytic continuation*, BIT Numer. Math. 60 (2020), 901--915, DOI `10.1007/s10543-020-00802-7`, is a modern analytic-continuation boundary. The superoscillation literature cited already in `NB-262` describes the related phenomenon that local interpolation/suppression can export very large dynamic range elsewhere.

No novelty is claimed for ill-posed Fourier--Laplace restriction, Hahn--Banach, Riesz representation, or analytic continuation. The line-local mathematical delta is their exact placement in the Euler-normalized Ford carrier geometry: the anchor lies at the boundary point `u=0`, while every legal box with `u>=a>0` is a compact restriction strictly inside the decaying half-plane; resolved rank can then amortize the arbitrarily bad witness norm in source `ell^2`. This identifies why a packet-scale positive-depth strip cannot by itself be the missing signed-carrier coercive quantity.

No external theorem is load-bearing in the derivation above, so these references are prior-art boundaries rather than dependencies needed to justify the finding. `SOURCES.md` therefore needs no new durable theorem anchor.

## 8. Adversarial audit and surviving frontier

The strongest invalid reading would be that signed scalar carriers now solve the Nyman--Beurling approximation problem. They do not. The construction may have catastrophic total variation and uncontrolled amplitude outside the prescribed strip, and it has not passed through the exact Hardy projection.

A second invalid reading would be that an arbitrarily large fraction of the full Ford window can be flattened at negligible cost. The quantifiers do not establish this. The box is selected first and `K` is then made large enough to realize its approximate annihilator. The theorem allows `B_n->infinity`, but not a post hoc requirement `B_n~K_n`. Any future lower bound coupling horizontal coverage directly to rank remains live.

A third possible concern is that Section 1 merely produces complex coefficients. The conjugation symmetry argument explicitly gives real signed densities and hence real signed resolved coefficients. Positivity, not reality, is the missing hypothesis.

A fourth concern is discretization. Equation (11) is uniform on the full compact box and the exact anchor survives cell averaging. The source `ell^2` estimate (8) is one-sided in the favorable direction and needs no smoothness of `f`. The price is only that the required `K` can be arbitrarily large, which is exactly the unquantified resource this finding exposes.

The frontier after `NB-262` should therefore be narrowed again. **A fixed packet-scale shallow strip is not enough.** Any genuine signed-scalar no-go must introduce at least one quantitative resource that the diagonal construction cannot postpone: a horizontal coverage requirement comparable with the available rank (`B~K` or an equivalent full-window condition), a total-variation/conditioning bound tied to the physical source, or a destination-side Hardy/Nyman norm that makes exported side-lobes unavoidable. Without such a resource, Fourier--Laplace analytic continuation supplies approximate null carriers at vanishing resolved Hilbert cost.