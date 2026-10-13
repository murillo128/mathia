# WI-451 — Rational reciprocal Fourier lattices have a sharp common-grid support rebate

**Status:** LITERATURE+DERIVED + EXACT-SUPPORT/EXISTENCE + CLASSICAL-SIMULTANEOUS-TILING + WANG-CLASS-SPECIALIZATION + NON-RH + NO-NOVELTY-CLAIM

**Local dependencies:** WI-450 (pairwise-incommensurate aggregate support theorem and superflat smooth-square convolution), WI-446 (smooth reciprocal-lattice orthogonality), WI-449 (single-lattice near-optimality versus support geometry).

**Primary prior art:** M. M. Etkind and N. Lev, *Functions tiling simultaneously with two arithmetic progressions*, Proc. London Math. Soc. 127 (2023), 1775–1815, DOI 10.1112/plms.12570, Theorems 2.9–2.10. Those theorems already give the sharp, stronger **Lebesgue measure of support** threshold for commensurate periods and a nonnegative construction. The argument below records an elementary enclosing-interval/Fourier proof and the exact Wang smooth-square consequence; it claims no new general tiling theorem.

## Exact statement

Fix the Fourier normalization
\[
\widehat f(\xi)=\int_{\mathbb R} f(t)e^{-2\pi i\xi t}\,dt,\qquad
\int f=1.
\]
Let \(p,q>0\) be **rationally commensurate**: write
\(p=mh,\ q=nh\) where \(m,n\) are coprime positive integers and
\(h>0\) is the real greatest common period. Suppose
\[
\widehat f(k/p)=\widehat f(\ell/q)=0
\quad(k,\ell\in\mathbb Z\setminus\{0\}).
\tag{1}
\]

**Sharp enclosing support.** Any such \(f\in L^1(\mathbb R)\) supported inside an interval of length \(L\) satisfies
\[
\boxed{L\ge p+q-h=(m+n-1)h.}
\tag{2}
\]
The bound does not require that \(f\) be nonnegative or even. Equality is attained by a nonnegative even compactly supported probability density, which is generally not smooth.

**Sharp source-admissible criterion.** For the Wang class
\[
\mathcal F_\lambda=
\{\eta^2:\ \eta\in C_c^\infty((-\lambda/2,\lambda/2);\mathbb R),
\ \eta\ \text{even},\ \int\eta^2=1\},
\qquad 0<\lambda\le1,
\]
there exists \(f\in\mathcal F_\lambda\) satisfying every zero in (1) **if and only if**
\[
\boxed{p+q-h<\lambda.}
\tag{3}
\]
The strict inequality is essential: the enclosing support of a member of this class lies strictly inside the open window.

For completeness, when \(p/q\notin\mathbb Q\), WI-450 gives the corresponding bound \(L\ge p+q\) and Wang criterion \(p+q<\lambda\). Hence for two prescribed periods, writing \(h=0\) in the irrational case, the formula \(p+q-h\) gives the complete interval-length feasibility boundary; the new mathematical content here is the rational overlap correction.

## 1. Exact overlap and the necessary bound

The two reciprocal zero grids are
\[
\Lambda_p=\{k/p:k\in\mathbb Z\setminus\{0\}\},\quad
\Lambda_q=\{\ell/q:\ell\in\mathbb Z\setminus\{0\}\}.
\]
Coprimality yields
\[
\Lambda_p\cap\Lambda_q
=\{r/h:r\in\mathbb Z\setminus\{0\}\}.
\tag{4}
\]
Indeed \(k/(mh)=\ell/(nh)\) implies \(nk=m\ell\), so
\(k=mr,\ \ell=nr\). The exact positive-frequency count up to
\(R\) is therefore
\[
\lfloor pR\rfloor+\lfloor qR\rfloor-\lfloor hR\rfloor
=(p+q-h)R+O(1).
\tag{5}
\]
In particular, **two rationally dependent lattices are not two disjoint grids**; using WI-450's irrational sum without subtracting their common grid is invalid.

Translate the enclosing support interval to center it at \(0\). This multiplies the Fourier transform by a zero-free exponential. The resulting entire \(F\), with \(F(0)=1\), obeys
\[
|F(Re^{i\theta})|\le\|f\|_1
          e^{\pi LR|\sin\theta|}.
\tag{6}
\]
By (5), counting positive and negative real zeros, its Jensen counting function satisfies
\(n_F(R)\ge2(p+q-h)R+O(1)\).
Jensen's formula and (6) give
\[
\int_0^R\frac{n_F(r)}r\,dr
=\frac1{2\pi}\int_0^{2\pi}\log|F(Re^{i\theta})|\,d\theta
\le \log\|f\|_1+2LR.
\tag{7}
\]
Since the grid counting is exact up to bounded floor errors, the left side is \(2(p+q-h)R+O(\log(2+R))\). Divide by \(2R\), let \(R\to\infty\), and obtain (2).

## 2. Explicit nonnegative equality construction

Let \(U_p\) be the even uniform probability density on
\([-p/2,p/2]\), and define the even probability measure
\[
D_{n,h}
=\frac1n\sum_{j=0}^{n-1}
 \delta_{h(j-(n-1)/2)}.
\tag{8}
\]
Set \(\rho=U_p*D_{n,h}\). Its support is precisely the closed interval of length
\[
p+(n-1)h=(m+n-1)h=p+q-h.
\tag{9}
\]
Indeed the shifted intervals of length \(p=mh\) have spacing \(h\le p\), hence no gaps. The density is nonnegative and even, and \(\int\rho=1\).

We have
\[
\widehat U_p(\xi)=\frac{\sin(\pi p\xi)}{\pi p\xi},
\qquad
\widehat D_{n,h}(\xi)
=\frac{\sin(\pi nh\xi)}{n\sin(\pi h\xi)},
\tag{10}
\]
with removable singularities interpreted by continuity.
Every nonzero \(k/p\) is a zero of \(\widehat U_p\). At
\(\xi=\ell/q=\ell/(nh)\), either \(n\nmid\ell\), in which case
\(\widehat D_{n,h}(\xi)=0\), or \(n\mid\ell\), in which case
\(\xi=r/h\ne0\), so \(\widehat U_p(\xi)=0\).
Thus \(\widehat\rho=\widehat U_p\,\widehat D_{n,h}\)
vanishes on the entire union (1), proving sharpness.

An explicit check is \(p=2h,q=3h\): the density has successive
length-\(h\) cells with heights proportional to \(1,2,2,1\),
and encloses length \(4h\), not the naive \(5h\).
If \(m=1\) or \(n=1\), one grid is contained in the other,
and (2) correctly reduces to \(L\ge\max(p,q)\).

## 3. Exact Wang smooth-square realization

Suppose \(p+q-h<\lambda\). Choose
\(0<\delta<\lambda-(p+q-h)\) and the even probability bump
\[
g_\delta(t)=Z^{-1}
 \exp\!\left(-\frac1{1-(2t/\delta)^2}\right)
 {\bf1}_{|t|<\delta/2}.
\tag{11}
\]
Put \(f=\rho*g_\delta\). It is nonnegative, even, normalized,
\(C_c^\infty\), supported within an interval of length
\(p+q-h+\delta<\lambda\), and has **exactly** the required
Fourier zeros, since \(\widehat f=\widehat\rho\,\widehat g_\delta\).

The remaining issue is the smoothness of \(\eta=\sqrt f\), not automatic for arbitrary nonnegative smooth functions. For each derivative order \(r\) and each \(0<\alpha<1\), the explicit superflat bump satisfies
\[
|g_\delta^{(r)}(t)|\le C_{r,\alpha}g_\delta(t)^\alpha.
\tag{12}
\]
Since \(\rho\) is a probability measure, differentiation under
convolution and concavity of \(x^\alpha\) give
\[
|f^{(r)}(t)|
\le C_{r,\alpha}\int g_\delta(t-u)^\alpha\,d\rho(u)
\le C_{r,\alpha} f(t)^\alpha.
\tag{13}
\]
On \(\{f>0\}\), a term in the \(r\)-th derivative of \(\sqrt f\)
with \(j\) factors of derivatives of \(f\) is
\(O(f^{1/2-j(1-\alpha)})\). Choose
\(\alpha>1-1/(2r)\): these terms vanish at zeros, and
all derivatives extend continuously by zero.
Induction using the mean-value theorem then establishes
\(\eta\in C_c^\infty\). Evenness and \(\int\eta^2=1\) follow
from \(f\), so \(f\in\mathcal F_\lambda\).
Together with (2) and the strict Wang support containment,
this proves (3).

## Prior art, stress tests, and RH boundary

Etkind–Lev (2023), Theorems 2.9–2.10, establish the sharper **measure-of-support** lower bound and an interval-supported nonnegative equality construction for commensurate translation tilings. Our Fourier vanishing conditions are exactly uniform nonzero-level periodization/tiling conditions: by Fourier uniqueness,
\[
\widehat f(k/p)=\mathbf1_{\{k=0\}}
\quad\Longleftrightarrow\quad
\sum_{j\in\mathbb Z}f(t-jp)=1/p\quad\text{a.e.}
\tag{14}
\]
and similarly for \(q\). Rescaling Etkind–Lev's periods and levels recovers (2); the explicit \(U_p*D_{n,h}\) example and superflat smoothing specialize the same classical phenomenon to Wang's real-even smooth-square class. Thus this is **an independent derivation and source-interface identification, not a new tiling theorem**.

**Falsification controls.** Both (4) and the construction fail if one treats overlapping grids as disjoint. A support **measure** and the length of an enclosing support **interval** are different notions; Jensen alone proves the latter, while the cited tiling theorem proves the stronger former. Ordinary mollification preserves Fourier zeros but does not, by itself, ensure that the square root remains smooth: inequalities (12)–(13) are needed. At \(p+q-h=\lambda\), the nonsmooth equality construction fits a closed interval but not Wang's strictly compactly supported smooth window.

**Consequence for Weil inertia.** The rational-overlap loophole left explicit in WI-450 has an exact one-common-grid rebate \(h\); no unrestricted sum of dependent lattice periods is a valid support charge. This concerns manufactured real-frequency orthogonality inside a selectable Wang test. It supplies no source-fixed information tying actual zeta ordinates or off-critical indefinite Weil blocks to these grids, and excludes no individual off-critical zero. It does not improve the currently certified simple-critical proportion or prove RH.
