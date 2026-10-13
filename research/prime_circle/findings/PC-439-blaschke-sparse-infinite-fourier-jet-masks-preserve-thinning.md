# PC-439 — Blaschke-sparse infinite Fourier-jet masks preserve sharp prime-log thinning

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + CONTROL-ONLY. The PC-435 completeness threshold persists for a countably infinite, nonperiodic class of polynomial-exponential masks provided their one-sided frequency shifts themselves form a Blaschke-summable set. Unlike PC-436 and PC-438, the multiplier need not have finite Fourier support; unlike PC-437, it need not be periodic or bounded. The exact new hypothesis is a summable *unweighted shifted-zero budget*, not merely summability of Fourier coefficients. This is a control theorem using classical Hardy/Blaschke/Fourier tools, not an RH implication.

## 1. The countable differential-delay theorem

Fix \(a>0\), \(0<\sigma<1\), \(\alpha=\pi/a\), and a positive-a.e. weight satisfying the PC-435 envelope
\[
c\min\{|t|,1\}e^{-a|t|}
\le w(t)\le C(1+|t|)^K e^{-a|t|}
\quad\text{a.e.},\qquad c,C>0,\ K\ge0. \tag{1}
\]
Let \(0\le\beta_1<\beta_2<\cdots\to\infty\) obey
\[
\sum_{j\ge1}e^{-\alpha\beta_j}<\infty. \tag{2}
\]
For a fixed integer \(r\ge0\), choose polynomials \(P_j(t)=\sum_{k=0}^r a_{jk}t^k\) with
\[
\sum_{j\ge1}\sum_{k=0}^r|a_{jk}|<\infty,\qquad
D(t)=\sum_{j\ge1}P_j(t)e^{-i\beta_jt}\not\equiv0. \tag{3}
\]
The series for \(D\) converges locally uniformly on the real axis and extends holomorphically to the lower half-plane. It satisfies
\[
|D(t)|\le C_D(1+|t|)^r. \tag{4}
\]
Moreover \(D\ne0\) almost everywhere. Indeed, \(D(z)/(z-i)^r\) is bounded holomorphic on \(\Im z<0\): there \(|e^{-i\beta_jz}|\le1\), \(|z-i|\ge1\), and \(|z|/|z-i|\le1\). Its continuous boundary function is nonzero, and the classical Hardy boundary-uniqueness theorem excludes a positive-measure set of real zeros.

Let \(X\subset[2,\infty)\) consist of distinct points tending to infinity. In the Hilbert space \(\mathscr H_W=L^2(\mathbb R,W(t)\,dt)\), \(W=w|D|^2\), consider
\[
q_x(t)=e^{it\log x},\qquad
v_{x,\sigma}(t)=1-x^{1-\sigma}e^{it\log x}. \tag{5}
\]
Then the **exact simultaneous completeness criterion** is
\[
\boxed{
\overline{\operatorname{span}}\{q_x:x\in X\}=\mathscr H_W
\iff
\overline{\operatorname{span}}\{v_{x,\sigma}:x\in X\}=\mathscr H_W
\iff
\sum_{x\in X}x^{-\alpha}=\infty.
} \tag{6}
\]
If the series converges, the orthogonal complements of both systems contain one common infinite-dimensional subspace. The assertion includes the endpoint exponent \(\alpha\) and masks with infinitely many frequencies, high-order real zeros, or real zeros approaching arbitrarily small values along unbounded sequences.

## 2. Divergent samples require only an upper spectral envelope

From (1), (4),
\[
W(t)\le C'(1+|t|)^{K+2r}e^{-a|t|}. \tag{7}
\]
For \(h\in\mathscr H_W\), the Fourier transform \(F_h(z)=\int h(t)W(t)e^{-izt}\,dt\) is analytic in \(S_a=\{|\Im z|<a/2\}\), has at most polynomial growth at the strip edges, and vanishes as \(\Re z\to\pm\infty\) on the real axis. The PC-435 strip-to-half-plane Blaschke argument therefore shows that
\[
F_h(\log x)=c_0x^{\sigma-1}\quad(x\in X),\qquad
\sum_{x\in X}x^{-\alpha}=\infty
\]
forces \(F_h\equiv0\) and \(c_0=0\). Fourier uniqueness and \(W>0\) a.e. yield \(h=0\). The choices \(c_0=0\) and \(c_0=F_h(0)\) prove completeness for \(q_x\) and \(v_{x,\sigma}\), respectively.

## 3. Convergent samples: an infinite shifted-zero divisor with finite jets

Assume \(\sum_{x\in X}x^{-\alpha}<\infty\), and prescribe the distinct real zeros
\[
Z=\{\beta_j:j\ge1\}
 \cup\{\log x+\beta_j:x\in X,\ j\ge1\}. \tag{8}
\]
There is no finite accumulation point because the \(\beta_j\) and \(\log x\) tend to infinity. Removing duplicate points only decreases the sum, so
\[
\sum_{z\in Z}e^{-\alpha z}
\le\left(1+\sum_{x\in X}x^{-\alpha}\right)
  \sum_{j\ge1}e^{-\alpha\beta_j}<\infty. \tag{9}
\]
Thus \(Z\) is a Blaschke zero set for the strip \(S_a\), under \(z\mapsto e^{\alpha z}\). Let \(B\in H^\infty(S_a)\), \(B\not\equiv0\), \(|B|\le1\), vanish at every point of \(Z\). A bounded Blaschke product gives such a \(B\), including repeated desired zeros if necessary.

Set \(m=r+1\). For any complex polynomial \(Q\), write
\[
G_Q(z)=e^{-z^2}B(z)^m Q(z),\qquad
g_Q(t)=\frac1{2\pi}\int_{\mathbb R}G_Q(s)e^{ist}\,ds. \tag{10}
\]
Restrict \(Q\) to the infinite-dimensional kernel of
\[
Q\longmapsto\int_{\mathbb R}G_Q(s)\,ds. \tag{11}
\]
Then \(g_Q(0)=0\) and \(g_Q(t)=O(t)\) near zero. The bounded factor \(B^m\) and Gaussian give a uniform horizontal \(H^2\) bound on the **entire** strip, not just on strict substrips. Contour shifting, Plancherel and Fatou at both edges imply
\[
\int_{\mathbb R}|g_Q(t)|^2e^{a|t|}\,dt<\infty,
\qquad
\int_{\mathbb R}\frac{|g_Q(t)|^2}{w(t)}\,dt<\infty. \tag{12}
\]
The first integral also ensures \(t^kg_Q(t)\in L^1\) for each fixed \(0\le k\le r\).

Define \(h_Q=g_Q/(w\overline D)\) away from the real null set of \(D\), arbitrarily on that set. Exact cancellation yields
\[
\|h_Q\|_{\mathscr H_W}^2=\int\frac{|g_Q|^2}{w}<\infty,
\qquad h_QW=g_QD\quad\text{a.e.} \tag{13}
\]
Absolute coefficient summability in (3), together with the fixed finite jet order and (12), justifies exchanging the series, derivatives and Fourier integral:
\[
F_{h_Q}(z)
=\sum_{j\ge1}P_j(i\partial_z)G_Q(z+\beta_j).
\tag{14}
\]
The *plus* sign is forced by \(e^{-i\beta_jt}\), in contrast to the positive-frequency shifts in PC-438. For \(z=0\) or \(z=\log x\), every argument \(z+\beta_j\) lies in \(Z\). Each \(G_Q\) vanishes there to order at least \(m=r+1\), so every summand and every derivative of order at most \(r\) vanishes:
\[
F_{h_Q}(0)=F_{h_Q}(\log x)=0\quad(x\in X). \tag{15}
\]
The vector \(h_Q\) is orthogonal to both systems. The map \(Q\mapsto h_Q\) is injective by \(B\not\equiv0\), Fourier uniqueness, and \(D\ne0\) a.e. Hence their common orthogonal complement contains an infinite-dimensional subspace.

## 4. A genuinely infinite, nonperiodic Dirichlet mask

For \(a=\pi\) (\(\alpha=1\)), take \(r=0\) and
\[
D(t)=\zeta(2+2it)-\zeta(2)
=\sum_{n\ge1}n^{-2}e^{-2it\log n}-\zeta(2). \tag{16}
\]
Combine the constant with the \(n=1\) coefficient. The distinct frequencies are \(\beta_n=2\log n\), and both required series converge:
\[
\sum_{n\ge1}|c_n|<\infty,\qquad
\sum_{n\ge1}e^{-\beta_n}=\sum_{n\ge1}n^{-2}<\infty. \tag{17}
\]
The mask has a real zero at \(t=0\), and no other real zero: equality \(\zeta(2+2it)=\zeta(2)\) saturates the triangle inequality for the absolutely convergent Dirichlet series, forcing \(e^{-2it\log n}=1\) for every \(n\); the irrationality of \(\log2/\log3\) then forces \(t=0\). It is not periodic, since its Fourier frequencies include rationally independent \(2\log2\) and \(2\log3\). It also lacks a bounded inverse: simultaneous approximation of finitely many prime phases, followed by a small absolutely convergent tail, gives arbitrarily large \(t\) with \(|D(t)|\) arbitrarily small. Thus neither finite-Fourier support nor periodic factorization nor uniformly invertible residual multiplication explains this example.

For any \(w\) obeying (1) with \(a=\pi\), the systems in \(L^2(w|D|^2)\) remain complete exactly when \(\sum_{x\in X}1/x\) diverges. For the zero-free matched Prime-Circle seed \(g_{0,\sigma}\) of PC-435, the Hilbert--Schmidt embedding of PC-433 transports (6) to its masked prime shells:
\[
\overline{\operatorname{span}}\{
\mathcal J[(1-p^{1-\sigma}e^{it\log p})Dg_{0,\sigma}]
:p\in\mathcal P\}=\mathcal A
\iff
\sum_{p\in\mathcal P}\frac1p=\infty. \tag{18}
\]
The incomplete case has infinite codimension for shells and marked translates. This is an *auxiliary nonarithmetic control*: neither \(D\) nor its Dirichlet frequencies are asserted to be forced by the roots-of-unity geometry.

## 5. Prior art, sharp boundary and falsification checks

The zero-set and boundary-uniqueness inputs are classical Hardy/Blaschke theory (Duren, *Theory of H^p Spaces*; Remmert, *Classical Topics in Complex Function Theory*); the full-strip Fourier step is classical Paley--Wiener theory (Paley--Wiener, *Fourier Transforms in the Complex Domain*). These authorities are already in Prime Circle's SOURCES.md. The countable shift-budget synthesis and Prime-Circle control specialization are derived here; no independent novelty beyond those classical ingredients is asserted.

Condition (2) is **sufficient**, not claimed necessary. It concerns the frequencies even when the coefficients \(a_{jk}\) are tiny; coefficient summability alone does not make the prescribed infinite zero divisor Blaschke. The argument does not cover two-sided, densely accumulating, or nonsummably shifted frequency supports without a different construction. An invertible infinite-frequency mask can preserve completeness even when (2) fails, so failure of this proof condition is not an obstruction theorem.

Most importantly, the genuine factor \(\zeta(\sigma-it)\), \(0<\sigma<1\), is **not** an absolutely convergent Dirichlet mask of the form (3); its formal unweighted logarithmic shifts would be \(\beta_n=\log n\), for which at \(a=\pi\), \(\sum_n e^{-\beta_n}=\sum_n 1/n=\infty\). Analytic continuation does not justify using (14) with that nonconvergent series. Consequently (6) does not prove a sparse-prime converse for the genuine zeta-weighted Hilbert shells, does not select the critical line, and does not imply RH.

**Audit points:** the sign of the shifts in (14); local finiteness and multiplicity of \(Z\); the *unweighted* double Blaschke sum (9); global lower-envelope use only for the original \(w\), not for \(W\); the cusp moment (11); full-strip endpoint control in (12); the one-sided half-plane boundary-uniqueness argument for \(D\); and precise exclusion of the genuine zeta factor.
