# WI-448 — Sharp quartic density tariff for orthogonal lattices near Wang's cosine window

**Status:** EXACT-DERIVED + PRIMARY-SOURCE-SPECIALIZATION + SHARP-ASYMPTOTIC/OBSTRUCTION + CLASSICAL-FOURIER-TOOLS + NON-RH + NO-PRIORITY-CLAIM

**Primary source:** Biao Wang, *Simple critical zeros and distinct zeros of the Riemann zeta function in short intervals*, arXiv:2609.07918v2, Proposition 4.1 (cosine variational minimizer and admissible smooth tests) and Proposition 5.1 (finite integer-multiset inequality), https://arxiv.org/html/2609.07918v2.

**Local dependencies:** WI-442 (real-only Gram defect), WI-445 (positive bounded-span triple cost), WI-446 (smooth near-optimal exact infinite orthogonal lattices without a rate), and WI-447 (sharp quartic decay of the optimizer's triple-Gram cost).

## Precise objects and results

Fix \(0<\lambda\le1\), \(a=\lambda/2\), and the convention
\[
\widehat f(\xi)=\int_{\mathbb R}f(t)e^{-2\pi i\xi t}\,dt.
\]
Wang's unique (not endpoint-smooth) normalized optimizer and functional are
\[
f_*(t)=\frac{\cos(\sqrt2t)}{\sqrt2\sin(\lambda/\sqrt2)}
             \mathbf1_{[-a,a]}(t),\quad K_*(\xi)=\widehat f_*(\xi),
\qquad
C(f)=\|f\|_2^2+\iint |t-v|f(t)f(v)\,dt\,dv,
\quad C_\lambda=C(f_*).
\]
The genuinely admissible smooth tests form
\[
\mathcal F_\lambda=
\left\{\eta^2:\eta\in C_c^\infty((-a,a);\mathbb R),
\ \eta\text{ even},\ \int\eta^2=1\right\}.
\]
Set \(\sigma_\lambda=1-2\lambda^2/\pi^2>0\). Wang's exact
second-variation identity implies for all \(f\in\mathcal F_\lambda\)
\[
\sigma_\lambda\|f-f_*\|_2^2
\le C(f)-C_\lambda\le\|f-f_*\|_2^2. \tag{1}
\]

**Theorem A (a finite real-frequency density tariff).** Let \(f\in
\mathcal F_\lambda\) have an orthonormal exponential family
\(\{e^{2\pi ix_jt}\}_{j=1}^n\) in \(L^2(f(t)\,dt)\), with
\(n\ge3\), \(x_1<\cdots<x_n\), span \(X=x_n-x_1\).
Write
\[
\kappa_\lambda(R)=\min_{\substack{r,s\ge0\\r+s\le R}}
[K_*(r)^2+K_*(s)^2+K_*(r+s)^2],\qquad
c_\lambda=\inf_{R\ge0}(1+R)^4\kappa_\lambda(R)>0.
\tag{2}
\]
The positivity of \(c_\lambda\) uses WI-445's strict bounded-span
gap and WI-447's \(\kappa_\lambda(R)\sim3/(2\pi^4R^4)\).
Then the exact, uniform finite-configuration estimate is
\[
\boxed{\quad C(f)-C_\lambda\ \ge\
\frac{\sigma_\lambda c_\lambda}{(4+\pi^2)\lambda}
\frac{(n-2)^5}{n\,(n-2+2X)^4}.\quad}\tag{3}
\]
No minimum gap, lattice structure, or distribution hypothesis on
the \(x_j\) is assumed. In particular, along orthogonal families
with \(n\to\infty\) and \(n/X\to\rho>0\), the lower cost tends
to a *strictly positive* bound
\[
\liminf (C(f)-C_\lambda)\ge
\frac{\sigma_\lambda c_\lambda}{(4+\pi^2)\lambda}
\left(\frac{\rho}{\rho+2}\right)^4.
\tag{4}
\]
Here \(f\) may vary with the family. The only conclusion is
rigidity of finite real-frequency exponential orthogonality under
positive density; no zeta ordinate-density assertion is imported.

**Theorem B (sharp constant on commensurate orthogonal lattices).**
For \(p>0\), define the extended-valued minimum
\[
I_\lambda(p)=\inf\left\{C(f)-C_\lambda:
 f\in\mathcal F_\lambda,\ 
 \widehat f(k/p)=0\ \text{for all }k\in\mathbb Z\setminus\{0\}\right\}.
\tag{5}
\]
An empty feasible set has infimum \(+\infty\).
For the commensurate sequence \(p_q=\lambda/q\), \(q\in\mathbb N\),
the feasible set is nonempty for all sufficiently large \(q\), and
\[
\boxed{\quad I_\lambda(p_q)
=\frac{p_q^4}{180\lambda}+O_\lambda(p_q^5)
\qquad(q\to\infty).\quad}\tag{6}
\]
Thus a near-optimal *infinite* orthogonal lattice has a sharp
quartic cost in its frequency density \(p\) on this sequence.
The exponent and leading coefficient are proved, not fitted
numerically. The upper construction uses an **exact** smooth
nonnegative normalized density \(\eta^2\), not the nonsmooth
minimizer or approximate Fourier zeros. No analogous sharp
coefficient is asserted for arbitrary incommensurate \(p\).

## 1. Proof of finite-density Theorem A

For any three real frequencies with span at most \(R\), WI-445
gives a positive sum of the three squared \(K_*\) overlaps, and
WI-447 gives its sharp \(R^{-4}\) decay. Hence \(c_\lambda>0\)
in (2): the compact interval of small \(R\) has strictly
positive minimum and the large-\(R\) tail has positive limit.

For ordered locations \(x_1<\cdots<x_n\), put
\(s_i=x_{i+2}-x_i\), \(1\le i\le n-2\), and
\(E_*=\sum_{1\le i<j\le n}K_*(x_j-x_i)^2\).
A pair belongs to at most two consecutive triples. Since
\(\sum_{i=1}^{n-2}s_i\le2X\), Jensen's inequality for the
convex decreasing function \((1+t)^{-4}\) yields
\[
\begin{aligned}
2E_* &\ge\sum_{i=1}^{n-2}\kappa_\lambda(s_i)
\ge c_\lambda\sum_{i=1}^{n-2}(1+s_i)^{-4}\\
&\ge c_\lambda\,
\frac{(n-2)^5}{(n-2+2X)^4}.
\end{aligned}\tag{7}
\]
All frequencies of an orthogonal family are automatically
\(\delta_0=1/(2\lambda)\)-separated: if
\(0<|\xi|<1/(2\lambda)\), then
\(\operatorname{Re}\widehat f(\xi)=
\int f(t)\cos(2\pi\xi t)\,dt>0\) for every nonnegative
normalized \(f\) supported in \([-a,a]\); such a \(\xi\)
cannot be a Fourier zero.

Let \(g=f-f_*\), \(H=\widehat g\). Plancherel and support give
\(\|H\|_2=\|g\|_2\) and
\(\|H'\|_2\le\pi\lambda\|g\|_2\).
For any \(\delta_0\)-separated points \(y_j\), the elementary
local Sobolev inequality on the disjoint intervals
\([y_j-\delta_0/2,y_j+\delta_0/2]\) gives
\[
\sum_j|H(y_j)|^2
\le\frac2{\delta_0}\|H\|_2^2+
 2\delta_0\|H'\|_2^2
\le(4+\pi^2)\lambda\|g\|_2^2.
\tag{8}
\]
Indeed, average
\(|H(y_j)|^2\le2|H(t)|^2+
2\delta_0\int_{I_j}|H'|^2\) over each \(I_j\).

For each fixed \(i\), the sampling points
\(y_j=x_j-x_i\) are separated. Since orthogonality gives
\(H(x_j-x_i)=-K_*(x_j-x_i)\) for \(j\ne i\), summing (8)
over \(i\) yields
\[
2E_*\le n(4+\pi^2)\lambda\|g\|_2^2. \tag{9}
\]
Combine (7), (9) and coercivity (1) to obtain (3).
No infinite-dimensional trace interchange occurs: every
sampling argument here is finite.

## 2. Exact reciprocal-lattice constraint

Take \(p=p_q=\lambda/q\).
The periodization \(G_{*,p}(t)=p\sum_{j\in\mathbb Z}
f_*(t+jp)\) has period \(p\) and average one.
Write \(E_p=G_{*,p}-1\); it has period \(p\) and mean zero
on each full period.

The explicit cosine transform in WI-447 gives, **at all
nonzero reciprocal-lattice frequencies**,
\[
\boxed{\quad K_*(k/p)=
(-1)^{qk+1}\frac{p^2}{2\pi^2k^2-p^2},
\qquad k\in\mathbb Z\setminus\{0\}.\quad}\tag{10}
\]
The numerator and the commensurability phase can also be
checked by direct integration of \(\cos(\sqrt2 t)\) between
\(\pm a\). In particular its Fourier series converges
absolutely and
\[
E_p(t)=\sum_{k\ne0}K_*(k/p)e^{2\pi ikt/p},
\quad\|E_p\|_\infty=O_\lambda(p^2). \tag{11}
\]

Suppose an \(L^2([-a,a])\) density \(f\) of integral one
satisfies every nonzero reciprocal-lattice Fourier-zero
constraint, and set \(g=f-f_*\). Fourier uniqueness on the
circle is equivalent to
\[
p\sum_jg(t+jp)=-E_p(t)\quad\text{a.e.} \tag{12}
\]
There are **exactly \(q\)** interior preimages per residue
class \(t\bmod p\), up to measure-zero endpoints, because
\(2a=\lambda=qp\). The least-\(L^2\)-norm solution of (12)
is therefore the equal-share correction
\[
h_p(t)=-\frac{E_p(t)}{\lambda}\,
\mathbf1_{[-a,a]}(t). \tag{13}
\]
Every other solution decomposes orthogonally in \(L^2\):
\(g=h_p+w\), where \(p\sum_jw(t+jp)=0\).
Both \(h_p\) and \(w\) have integral zero. Exact orthogonality
follows by decomposing the \(L^2\) inner product into the
\(q\) preimages of a single residue class.

By Fourier Parseval on one period and (10),
\[
\begin{aligned}
\|h_p\|_2^2
&=\frac1\lambda\sum_{k\ne0}|K_*(k/p)|^2\\
&=\frac{2p^4}{\lambda}
  \sum_{k\ge1}\frac1{(2\pi^2k^2-p^2)^2}
=\frac{p^4}{180\lambda}+O_\lambda(p^6),
\end{aligned}\tag{14}
\]
using \(\sum_{k\ge1}k^{-4}=\pi^4/90\).
The factor \(1/\lambda\), both signs \(k\gtrless0\), and
the \(q\) repeated support copies are essential to the
coefficient \(1/180\).

## 3. The primitive correction cannot beat the leading constant

For any zero-mean \(v\in L^2([-a,a])\) define
\(Pv(t)=\int_{-a}^t v(u)\,du\).
Wang's exact identity says
\[
C(f)-C_\lambda=Q(g):=\|g\|_2^2-2\|Pg\|_2^2.
\tag{15}
\]
The Dirichlet Poincare inequality on the length-\(\lambda\)
interval yields \(Q(v)\ge\sigma_\lambda\|v\|_2^2\).

Because \(E_p\) has zero mean on each \(p\)-period,
(11) gives \(\|Ph_p\|_\infty=O_\lambda(p^3)\),
hence \(\|Ph_p\|_2=O_\lambda(p^3)\).
For \(g=h_p+w\) as above, the \(L^2\) cross term vanishes,
so
\[
Q(g)=Q(h_p)+Q(w)-4\operatorname{Re}
\langle Ph_p,Pw\rangle.
\tag{16}
\]
Using \(\|Pw\|_2\le(\lambda/\pi)\|w\|_2\) and
completing a scalar square,
\[
Q(g)\ge Q(h_p)-
\frac{4\lambda^2}{\sigma_\lambda\pi^2}
\|Ph_p\|_2^2
=\|h_p\|_2^2-O_\lambda(p^6).
\tag{17}
\]
This lower bound holds for the larger class of all signed
\(L^2\) solutions of the lattice constraints, so it also
holds for all admissible smooth nonnegative \(f=\eta^2\).
Equations (14) and (17) prove the sharp leading-constant
lower bound in (6), with an \(O_\lambda(p^6)\) lower error.

## 4. An admissible positive smooth near-equal-share upper construction

The non-smooth equal-share solution \(f_*+h_p\) alone is
*not* an admissible \(\eta^2\). To obtain an exact admissible
test without losing the quartic constant, let
\(\delta=p^6\) and choose an even smooth cutoff
\(0\le\chi_\delta\le1\), supported strictly in \((-a,a)\),
equal to one except in endpoint collars of total width
\(O(\delta)\). Put
\[
\varphi=\chi_\delta^2,\quad
Z_\delta=\int\varphi f_*=1+O_\lambda(\delta),
\quad f_0=\frac{\varphi f_*}{Z_\delta}.
\]
The product is smoothly extended by zero, and
\(\|f_0-f_*\|_2=O_\lambda(\sqrt\delta)=O_\lambda(p^3)\).
Define two positive/smooth, even, \(p\)-periodic functions
\[
W_p(t)=p\sum_j\varphi(t+jp),\qquad
G_{0,p}(t)=p\sum_jf_0(t+jp).
\tag{18}
\]
Since \(p=\lambda/q\), the periodization of the indicator of
\([-a,a]\) is exactly \(\lambda\) a.e., hence
\(W_p=\lambda+O_\lambda(p)\) uniformly, and \(W_p\ge\lambda/2\)
for sufficiently small \(p\).

Define inside \((-a,a)\)
\[
\boxed{\quad
f_p(t)=\varphi(t)
\left[\frac{f_*(t)}{Z_\delta}
-\frac{G_{0,p}(t)-1}{W_p(t)}\right],\quad
f_p=0\ \text{outside}.\quad}\tag{19}
\]
The expression in square brackets is even, smooth and
strictly positive on \([-a,a]\) for small \(p\):
\(\min_{[-a,a]} f_*>0\), whereas
\(G_{0,p}-1=E_p+O_\lambda(p+\delta)=O_\lambda(p)\)
uniformly. Thus \(f_p=\eta_p^2\), with
\(\eta_p=\chi_\delta\sqrt{[\cdots]}\) even, real and in
\(C_c^\infty((-a,a))\). Its periodization is **exactly**
\[
p\sum_j f_p(t+jp)=G_{0,p}(t)-
 (G_{0,p}(t)-1)\frac{W_p(t)}{W_p(t)}=1.
\tag{20}
\]
Consequently \(\int f_p=1\), and unfolding (20) gives
\(\widehat f_p(k/p)=0\) for *every* nonzero integer \(k\).

For clarity, here is the quantitative smoothing audit.
The difference \(R_p=G_{0,p}-G_{*,p}\) consists of a
global \(O_\lambda(\delta)\) normalization perturbation
and an \(O_\lambda(p)\) periodized collar perturbation
on residue sets of length \(O(\delta)\) per period,
provided \(\delta<p/4\). Therefore, measured over
\([-a,a]\),
\[
\|R_p\|_2
=O_\lambda(\delta+\sqrt{p\delta})
=O_\lambda(p^{7/2}),\qquad
\|R_p\|_\infty=O_\lambda(p+\delta).
\tag{21}
\]
From \(G_{0,p}-1=E_p+R_p\),
\(W_p=\lambda+O(p)\), \(\|E_p\|_\infty=O(p^2)\),
and the support of \(1-\varphi\) lying in collars,
\[
\|(f_p-f_*)-h_p\|_2=O_\lambda(p^3).\tag{22}
\]
The quadratic form \(Q\) is continuous on zero-mean
\(L^2\), so (14), (15), (22), and
\(\|h_p\|_2=O(p^2)\) yield
\[
0<C(f_p)-C_\lambda
=Q(h_p)+O_\lambda(p^5)
=\frac{p^4}{180\lambda}+O_\lambda(p^5).
\tag{23}
\]
Uniqueness of Wang's minimizer makes the displayed
difference strictly positive. Together with (17),
this proves Theorem B in its full **source-admissible**
smooth-test class.

## Novelty, falsifiers, and RH-facing boundary

- **Existing mathematics vs derived assembly.** Wang supplies the
  cosine optimizer and functional. WI-445/WI-447 supply the
  triple-Gram positivity and its quartic decay, while WI-446
  supplies existence of smooth infinite orthogonal lattices
  without the sharp density rate. Fourier periodization,
  Parseval, Jensen, one-dimensional Sobolev sampling, the
  equal-share least-norm principle, and Poincare are classical.
  The explicit \(\lambda^{-1}/180\) cost coefficient and
  finite-family density tariff are a source-specific exact
  assembly; no claim of independent discovery priority is made.
  Standard Fourier-series/Poisson tools may be found in
  Stein--Shakarchi, *Fourier Analysis: An Introduction*
  (Princeton, 2003).
- **Exact checks.** Verify the commensurate transform (10) by
  direct cosine integration, the two-sign zeta-four sum in
  (14), and the number \(q\) of support copies in the
  least-norm projection. Check both that the cutoff-defined
  square root is smooth/nonnegative and that the
  periodization in (20) is *exact*. Replacing the exact
  lattice condition by approximate Fourier smallness would
  not prove (6). A numerical check of (14) for
  \(\lambda=0.4,0.75,1\), with \(q=5,10,20,40\),
  approaches \(1/(180\lambda)\) after division by \(p^4\);
  these diagnostics support, but do not replace, the proof.
- **Geometry and limits.** \(p\) is the density (points per
  unit frequency length) of the lattice \(\mathbb Z/p\),
  not its spacing. The upper result is only along
  \(p=\lambda/q\), with fixed \(0<\lambda\le1\); no
  \(\lambda\downarrow0\) or incommensurate uniformity is
  asserted. The finite-family bound applies to freely
  positioned *real* frequencies, not to an arbitrary
  indefinite conjugation-invariant complex multiset.
- **Arithmetic and order-of-limits boundary.** These windows
  and frequencies are engineered jointly. Wang's arithmetic
  zeta passage holds each smooth admissible test fixed as
  \(T\to\infty\), while (6) takes \(p\to0\) afterward.
  Neither a \(T\)-dependent smooth-test estimate nor a
  zeta-zero lattice/distribution theorem is supplied.
  Off-critical zeros produce signed indefinite blocks that
  can offset real-only Gram charges. The density tariff
  excludes no individual off-critical zero, establishes
  no stronger unconditional simple-critical proportion,
  and **does not prove RH**.

**Consequence for Weil inertia.** The near-optimal lattice
countermodel of WI-446 has a *quantified* sharp escape route:
its orthogonal frequency density must vanish, and on
commensurate lattices the best smooth-test cost is
\(p^4/(180\lambda)+O_\lambda(p^5)\). The next RH-facing
step cannot be more Fourier packing alone: it must
connect a surviving Gram/defect charge to actual zeta
source information while retaining off-line indefinite
blocks and their potential screening.
