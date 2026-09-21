# NB-263 — Positive-depth Ford strip restriction is noncoercive at resolved Hilbert scale

> **Representation:** _Nyman–Beurling / resolved signed-carrier destination interface._ The line-specific input is the Euler-normalized `H`-separated carrier dictionary of `NB-255`--`NB-262`, with `J=R/H`, span parameter `m=J/K`, and legal complex Ford coordinate `w=R[(gamma-t_0)+i(1-beta)]`. The generic engine is an approximate-annihilator theorem for Fourier–Laplace restriction strictly inside the decaying half-plane, followed by cell-average discretization. The result corrects the frontier left by `NB-262`: a fixed, or preassigned growing, horizontal shallow strip at positive Ford depth is not Hilbert-coercive in the signed scalar class. The cost may be exported into uncontrolled conditioning and side-lobes outside the prescribed strip while the resolved shell-Hilbert norm tends to zero. This does not control the full `Theta(J)` hard window, total variation, or the final Hardy/Nyman distance.

**Date:** 2026-09-21  
**Status:** `EXACT-DERIVED + SIGNED-CARRIER + EULER-NORMALIZED + FOURIER-LAPLACE-RESTRICTION + APPROXIMATE-ANNIHILATOR + HAHN-BANACH + CELL-DISCRETIZATION + VANISHING-HILBERT-COST + SHALLOW-STRIP-SUPPRESSION + MATCHED-PACKET-EXCLUSION-ON-COVERED-STRIP + NB-262-ROUTE-CORRECTION + METHOD-BOUNDARY + SOURCE-ONLY + FRESH-PRIOR-ART-AUDIT`.

`NB-262` proves that the unique minimum-Hilbert carrier satisfying only the Euler anchor and one exact shallow notch develops a side-lobe of size `Theta(m/u)` on the natural horizontal Ford scale `x~m`, where

\[
m=\frac JK,
\qquad
u:=X(1-\beta)\sim\log m.
\]

Here and below the physical Ford depth is denoted by `u`; the display above uses `u=X(1-beta)`. That one-notch result deliberately leaves open whether additional horizontal constraints can flatten the side-lobe without making the resolved Hilbert cost coercive. They can if no independent conditioning bound is imposed and the target strip is prescribed before the resolved rank `K` is allowed to grow.

For

\[
E_m(a,U,B):=
\left\{-\frac{u}{Ym}+iy:
 a\le u\le U,\ |y|\le B\right\},
\qquad 0<a\le U<\infty,\quad B>0,
\]

and every `epsilon>0`, there exists a real signed density `f in L^2(0,1)` with

\[
\boxed{
\int_0^1f(t)\,dt=1,
\qquad
\sup_{z\in E_m(a,U,B)}
\left|\int_0^1f(t)e^{zt}\,dt\right|<\epsilon.
}
\tag{1}
\]

Thus any compact Ford strip separated from the Euler anchor loses coercive access to the anchor functional. Discretizing `f` into `K` cell masses preserves the anchor exactly and costs only `K^{-1/2}` times the fixed witness norm in coefficient `ell^2`. Taking `K` after the strip and witness are fixed therefore makes both the strip response and the resolved shell-Hilbert cost arbitrarily small.

The consequence for `NB-262` is direct. A box containing `|x|<=Bm` and `X(1-beta)=log m+O(1)` can be uniformly flattened by a signed resolved carrier. If the carrier supremum is `epsilon=o(1/B)`, then even the absolute contribution of every carrier-locked packet with `O(mB)` points in that box is `o(1)` at damping `e^{-u}~1/m`. The packet-scale side-lobe of the two-constraint optimizer is therefore not a universal signed obstruction.

The price is intentionally uncontrolled: the approximate annihilator may require enormous `L^2` and `L^1` norms, the discrete coefficient variation may be enormous, and large side-lobes may appear outside the prescribed box. The result is a method boundary, not a successful Nyman approximant.

## 1. Positive-depth restriction does not control the Euler anchor

Define

\[
T:L^2(0,1)\to C(E_m(a,U,B)),
\qquad
(Tf)(z):=\int_0^1f(t)e^{zt}\,dt,
\]

and

\[
L(f):=\int_0^1f(t)\,dt.
\]

The central claim is

\[
\boxed{
\inf_{L(f)=1}\|Tf\|_{C(E_m(a,U,B))}=0.
}
\tag{2}
\]

Assume instead that the infimum is positive. By homogeneity there is `A<infinity` such that

\[
|L(f)|\le A\|Tf\|_{C(E_m(a,U,B))}
\qquad(f\in L^2(0,1)).
\tag{3}
\]

The map `T` is injective. If `Tf=0` on the rectangle, then at any fixed `u in [a,U]` the entire function `z -> integral_0^1 f(t)e^{zt}dt` vanishes on the nontrivial segment `-u/(Ym)+i[-B,B]`; the identity theorem and Fourier uniqueness give `f=0`.

Hence (3) defines a bounded functional on `Ran(T)` by `ell(Tf)=L(f)`. Hahn--Banach extends it to the ambient `C(E)` space, and Riesz representation supplies a finite complex Borel measure `mu` on `E=E_m(a,U,B)` with

\[
L(f)=\int_E(Tf)(z)\,d\mu(z).
\]

Fubini then gives

\[
1=\int_Ee^{zt}\,d\mu(z)
\tag{4}
\]

for almost every `t in [0,1]`, hence everywhere on that interval by continuity. The right side is entire in `t`, so (4) holds for all complex `t`. But for positive real `t`, every `z in E` has `Re z<=-a/(Ym)`, and therefore

\[
\left|\int_Ee^{zt}\,d\mu(z)\right|
\le\|\mu\|_{TV}e^{-at/(Ym)}\to0,
\]

contradicting (4). This proves (2).

Because `E` is invariant under conjugation, a complex witness can be replaced by its real part:

\[
T(\Re f)(z)=\frac12\left(Tf(z)+\overline{Tf(\bar z)}\right),
\qquad L(\Re f)=1.
\]

Thus real signed densities suffice. The strict condition `a>0` is load-bearing: if the tested set contains `z=0`, then `Tf(0)=L(f)=1` and suppression is impossible.

## 2. Cell discretization preserves the anchor and amortizes witness norm

Fix a real witness `f` from (1), put `M_f=||f||_2`, partition `[0,1]` into `I_j=[j/K,(j+1)/K)`, and define

\[
c_j:=\int_{I_j}f(t)\,dt.
\tag{5}
\]

Then

\[
\sum_{j=0}^{K-1}c_j=1,
\qquad
\boxed{
\sum_{j=0}^{K-1}|c_j|^2\le\frac{M_f^2}{K}
}
\tag{6}
\]

by Cauchy--Schwarz. Take `J=mK` for notational simplicity and set

\[
C_J(w):=\sum_{j=0}^{K-1}c_je^{ijw/J}.
\tag{7}
\]

At the legal Ford coordinate `w=my+i u/Y`,

\[
C_J\!\left(my+i\frac uY\right)
=
\sum_jc_j
\exp\!\left[\left(iy-\frac{u}{Ym}\right)\frac jK\right].
\tag{8}
\]

This is the left-endpoint discretization of `Tf` at `z=-u/(Ym)+iy`. With `L_E=B+U/(Ym)`, the derivative of `e^{zt}` on `[0,1]` has modulus at most `L_E`, so

\[
\boxed{
\sup_{\substack{a\le u\le U\\|y|\le B}}
\left|
C_J\!\left(my+i\frac uY\right)
-(Tf)\!\left(-\frac{u}{Ym}+iy\right)
\right|
\le
\frac{L_E\|f\|_1}{K}
\le\frac{L_EM_f}{K}.
}
\tag{9}
\]

For the fixed witness, sufficiently large `K` therefore makes the discrete carrier uniformly as small as desired on the strip while

\[
\|c\|_2\le\frac{M_f}{\sqrt K}.
\tag{10}
\]

The order of quantifiers is the mechanism: first choose the finite strip and its finite-norm approximate annihilator; then use resolved rank to amortize that norm.

## 3. The discretization is a legal Euler-normalized source

Use the same one-sided `H`-grid as `NB-262`,

\[
\xi_j=jH,
\qquad H=\frac RJ,
\]

and set

\[
\lambda_J:=\sum_{j=0}^{K-1}c_j\delta_{\xi_j}.
\]

Equation (6) gives `lambda_J(mathbb R)=1`. With the physical measure

\[
d\nu_J(\xi)=e^{r\xi/X}d\lambda_J(\xi),
\]

the exact Euler normalization is

\[
\int e^{-r\xi/X}d\nu_J(\xi)=1.
\]

The occupied span is

\[
W\sim KH=\frac Rm,
\qquad
\frac WX\sim\frac1{Ym}.
\]

Thus for `m->infinity` the physical Euler tilt is uniformly `1+o(1)`. The translated `H`-shells are disjoint, so the same shell identity as in `NB-257`--`NB-262` yields

\[
H^{1/2}\|h_{\nu_J}\|_2
=(1+o(1))\|\phi\|_2\|c\|_2
\le
(1+o(1))\|\phi\|_2\frac{M_f}{\sqrt K}.
\tag{11}
\]

This controls only the resolved source norm, not the final Hardy-projected Nyman distance.

## 4. Diagonal suppression of growing preassigned strips

Choose arbitrary integer sequences

\[
m_n\to\infty,
\qquad 0<a_n\le U_n<\infty,
\qquad 0<B_n<\infty,
\qquad \epsilon_n\downarrow0,
\]

where `a_n` may tend to zero and `B_n,U_n` may grow. For each `n`, Section 1 gives a witness `f_n` with anchor one, strip norm below `epsilon_n/2`, and finite `M_n=||f_n||_2`.

Choose `K_n` afterward so large that

\[
\frac{M_n}{\sqrt{K_n}}<\epsilon_n,
\qquad
\frac{(B_n+U_n/(Ym_n))M_n}{K_n}<\frac{\epsilon_n}{2},
\]

and also

\[
\frac{B_n}{K_n}<\frac1n,
\qquad
\frac{U_n}{m_nK_n}<\frac1n,
\qquad
\log K_n\ge n m_n.
\tag{12}
\]

Set `J_n=m_nK_n`. Then `m_n=o(log J_n)`, so the conservative near-full regime of `NB-261`--`NB-262` is retained. The external height may be chosen large enough that the inherited `J_n<=log Q_n` condition holds, after which `R_n`, `X_n=YR_n`, and `H_n=R_n/J_n` are defined exactly as before.

The construction gives

\[
\boxed{
H_n^{1/2}\|h_{\nu_{J_n}}\|_2\to0
}
\tag{13}
\]

and

\[
\boxed{
\sup_{\substack{|x|\le m_nB_n\\a_n\le u\le U_n}}
\left|C_{J_n}\!\left(x+i\frac uY\right)\right|
\le\epsilon_n.
}
\tag{14}
\]

The first two ratios in (12) also keep the original smooth shell coordinate `(x+i u/Y)/J_n` uniformly small, so the fixed envelope remains `F(0)+o(1)` on the box.

The theorem is deliberately nonquantitative in `K_n`. It says that no positive-depth box chosen independently of the eventual rank can be coercive merely because its horizontal or vertical extent grows. A useful lower bound must couple the requested coverage to rank or conditioning itself.

## 5. Consequence for the `NB-262` packet

At the live depth `u=log m+O(1)`, cover `|x|<=mB`. Carrier-locked ordinates have Ford spacing `Theta(1)`, so any such packet with `O(mB)` points in the band has total absolute contribution at most

\[
O(mB)\,O(m^{-1})\,O(\epsilon)=O(B\epsilon)
\tag{15}
\]

before using phase cancellation, because `e^{-u}=Theta(m^{-1})`; the smooth envelope is uniformly bounded. Choosing `epsilon_n=o(B_n^{-1})` therefore forces every such covered matched packet to contribute `o(1)`.

In particular, the `Theta(log m)` side-lobe packet at `x=Theta(m)` from the minimum-Hilbert two-constraint optimizer of `NB-262` is not universal. Extra horizontal freedom can remove the entire exposed packet scale without paying in resolved `ell^2`, provided arbitrary conditioning and sufficiently many resolved channels are allowed.

## 6. Remaining costs and exact boundary

Three resources remain uncontrolled. First, there is no total-variation bound: witness norms and coefficient `ell^1` may diverge arbitrarily as the strip approaches the Euler anchor or grows. The variation currency isolated in `NB-255` remains live.

Second, (14) covers a region prescribed before `K_n` is chosen. It does not suppress a fixed positive fraction of the full hard Ford width `|x|=O(J_n)`, corresponding to `|y|=O(K_n)`. The proof gives no right to demand `B_n=cK_n` after rank is known. A horizontal coverage/rank lower bound is untouched.

Third, (13) is source-side. Exported side-lobes or large variation may survive the exact Hardy projection, while Hardy structure could also cancel source-side cost. The final Nyman distance has not been controlled.

The Euler anchor itself is never suppressed: `C_J(0)=1`. One may take `a_n->0`, but only by allowing conditioning and required rank to deteriorate without any uniform estimate. Nothing extends (14) to `u=0`.

## 7. Prior-art and representation audit

The generic instability is classical. Truncated Fourier/Laplace transforms are standard ill-conditioned inverse problems. Roy Lederman and Vladimir Rokhlin, *On the Analytical and Numerical Properties of the Truncated Laplace Transform I*, SIAM J. Numer. Anal. 53 (2015), 1214--1235, DOI `10.1137/140990681`, develops the truncated-Laplace singular system. Roy Lederman and Stefan Steinerberger, *Lower Bounds for Truncated Fourier and Laplace Transforms*, Integral Equations Operator Theory 87 (2017), 529--543, DOI `10.1007/s00020-017-2364-z`, gives quantitative stability boundaries. Lloyd N. Trefethen, *Quantifying the ill-conditioning of analytic continuation*, BIT Numer. Math. 60 (2020), 901--915, DOI `10.1007/s10543-020-00802-7`, is a modern analytic-continuation boundary. The superoscillation literature already cited in `NB-262` describes the related export of dynamic range outside a locally constrained region.

No novelty is claimed for ill-posed Fourier--Laplace restriction, Hahn--Banach, Riesz representation, or analytic continuation. The line-local delta is their exact placement in the Euler-normalized Ford geometry: the anchor is at `u=0`, every tested box with `u>=a>0` lies strictly in the decaying half-plane, and resolved rank amortizes the arbitrarily poor witness norm in source `ell^2`. This explains why the packet-scale shallow strip exposed by `NB-262` cannot itself be the missing signed-carrier coercive quantity.

No external theorem is load-bearing in the proof, so these references are prior-art boundaries rather than dependencies required by the finding. `SOURCES.md` needs no new durable theorem anchor.

## 8. Adversarial audit and surviving frontier

The result does **not** say that signed scalar carriers solve Nyman--Beurling. It permits catastrophic conditioning and uncontrolled response outside the prescribed strip, and it has not crossed the exact Hardy projection.

It also does not say that a positive fraction of the full Ford window is cheap. The decisive quantifier order is: choose the box, derive a finite-norm approximate annihilator, then choose `K`. A requirement scaling as `B~K` is outside the theorem and is now the cleanest horizontal candidate for a genuine no-go.

Finally, the result needs signs. The conjugation argument shows complex phases are unnecessary, but positivity would destroy the approximate-annihilator mechanism through the coherence results of `NB-254` and `NB-261`.

The frontier after `NB-262` should therefore be narrowed again: **a fixed packet-scale positive-depth strip is not enough**. A genuine signed-scalar obstruction must add at least one quantitative resource that the diagonal construction cannot postpone—horizontal coverage comparable with available rank, a total-variation/conditioning bound tied to the physical source, or a destination-side Hardy/Nyman norm that makes exported side-lobes unavoidable.