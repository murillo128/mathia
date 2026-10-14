# FD-334 — One-fifth squarefree intervals extend terminal Jordan occupation to four-ninth quotient depth

**Status:** LITERATURE+DERIVED + EXACT-CONVOLUTION + UNIFORM-WEIGHTED-SHORT-INTERVAL-TRANSFER + TERMINAL-QUOTIENT-OCCUPATION.

FD-038 proves universal nonsquarefree occupation of the terminal Schur/Jordan quotient shells for every fixed quotient exponent \(\alpha<1/3\), using an elementary \(O_\sigma(x^\sigma)\), \(\sigma>1/2\), weighted-squarefree summatory remainder. The cube-root threshold is a boundary of that global-remainder method, not of the underlying Farey identity. A quantitative theorem of Mayank Pandey on squarefree counting in every short interval, combined with an absolutely convergent convolution, moves the **source-independent terminal-shell threshold to every fixed \(\alpha<4/9\)**. No RH assumption is used.

## 1. Precise terminal-shell theorem

For integers \(H>D\ge1\), retain the exact physical definitions of FD-033 and FD-038:
\[
w(r)=\frac{J_2(r)}{r^2}=\prod_{p\mid r}(1-p^{-2}),\qquad
\mathcal H(k)=\sum_{s\le k}\frac{M(\lfloor k/s\rfloor)}{s}.
\]
For a nonnegative shell profile \(F:\mathbb N\to[0,\infty)\), let
\[
\begin{aligned}
Q_F(K)&=\sum_{k\le K}\frac{F(k)}{k(k+1)},\\
E^{\rm term}_{H,D}(K;F)
 &=\sum_{\substack{D<r\le H\\\lfloor H/r\rfloor\le K}}w(r)F(\lfloor H/r\rfloor),\\
U^{\rm term}_{H,D}(K;F)
 &=\sum_{\substack{D<r\le H\\\lfloor H/r\rfloor\le K\\\mu(r)=0}}w(r)F(\lfloor H/r\rfloor).
\end{aligned}
\tag{1}
\]
Set
\[
a=\frac1{\zeta(3)},\qquad
c_{\rm sf}=\prod_p(1-p^{-2}-p^{-3}+p^{-4}),\qquad
b=a-c_{\rm sf}>0,\qquad
\delta_{\rm ns}=\frac ba=0.3558220840\ldots .
\tag{2}
\]
**Theorem.** For every fixed \(D\) and \(0<\alpha<4/9\), put \(K=\lfloor H^\alpha\rfloor\). Uniformly over *all* nonnegative \(F\) with \(Q_F(K)>0\),
\[
\boxed{
E^{\rm term}_{H,D}(K;F)=(a+o_{\alpha}(1))H Q_F(K),\qquad
U^{\rm term}_{H,D}(K;F)=(b+o_{\alpha}(1))H Q_F(K).
}
\tag{3}
\]
The error multipliers are independent of \(F\) (and of \(D\) once \(H/(K+1)>D\)). Consequently the ratio in (3) tends to \(\delta_{\rm ns}\). The physical choice \(F(k)=\mathcal H(k)^2\) is included without any regularity hypothesis on the Mertens source.

FD-033 proves \(Q_{\mathcal H^2}(K)\to\infty\). Hence the physical terminal energy and its nonsquarefree part are both \(\gg H Q_{\mathcal H^2}(H^\alpha)\), in particular superlinear. Along any sequence with \(U_{H,D}/E_{H,D}\to0\), where \(E_{H,D}\) and \(U_{H,D}\) are the *full* FD-037 energies, (3) forces
\[
\boxed{
\frac{E_{H,D}}
{H Q_{\mathcal H^2}(\lfloor H^\alpha\rfloor)}
\longrightarrow\infty
\qquad\text{for every fixed }\alpha<4/9.
}
\tag{4}
\]
Compared with FD-038, this rules out an occupation failure sustained only by amplification beyond the old \(H^{1/3}\) quotient range: a bad global horizon must swamp the longer terminal energy bulk, whose Jordan rows reach down to \(r>H^{5/9+o(1)}\).

## 2. Quantitative external input and its uniform consequence

Pandey, *Squarefree numbers in short intervals: explicit and formalized*, arXiv:2608.06682 (7 August 2026), Theorem 1.1, gives, for \(0<\varepsilon\le1/90935\), sufficiently large \(X\), and \(L=X^{1/5-2/90935+\varepsilon}\),
\[
\left|\sum_{X\le n\le X+L}\mu(n)^2-\frac6{\pi^2}L\right|
 \le \frac{10^{450}}{\varepsilon}L X^{-\varepsilon/10^{25}},
\quad
X\ge\exp(10^{27}/\varepsilon^2).
\tag{5}
\]
In particular, for every fixed \(\theta>1/5\), the following consequence holds uniformly as \(x\to\infty\):
\[
\boxed{
\sum_{x<n\le x+h}\mu(n)^2
  =\left(\frac6{\pi^2}+o_\theta(1)\right)h,
\qquad x^\theta\le h\le x.
}
\tag{6}
\]
To see this, choose once and for all an allowed positive \(\varepsilon\) in (5), giving a fixed theorem exponent \(\theta_0<1/5<\theta\). Partition \((x,x+h]\) into consecutive subintervals of the locally prescribed length \(y^{\theta_0}\) at their current starting point \(y\). Their starts lie in \([x,2x]\), so the error in (5) is uniformly \(o(1)\) times the sum of their lengths. The final incomplete interval has length \(O(x^{\theta_0})=o(h)\) and costs at most this length plus one. Endpoint conventions also cost \(O(1)\). Thus (6) follows with no quantitative constant or feasible numerical range claimed.

## 3. Transfer from squarefree counts to Jordan-weighted squarefree counts

Write \(f_{\rm sf}(n)=\mu(n)^2w(n)\). Its Euler factors satisfy
\[
\sum_{j\ge0}f_{\rm sf}(p^j)z^j
 =1+(1-p^{-2})z=(1+z)\left(1-\frac{p^{-2}z}{1+z}\right).
\tag{7}
\]
Accordingly,
\[
\boxed{
f_{\rm sf}=\mu^2*\kappa,\qquad
\kappa(1)=1,\quad \kappa(p^j)=(-1)^j p^{-2}\ (j\ge1).
}
\tag{8}
\]
The Dirichlet series for \(\kappa\) is absolutely convergent in *every* half-plane \(\Re s>0\):
\[
\prod_p\left(1+p^{-2}\sum_{j\ge1}p^{-j\sigma}\right)
 =\prod_p\left(1+\frac{p^{-(2+\sigma)}}{1-p^{-\sigma}}\right)<\infty
 \qquad(\sigma>0).
\tag{9}
\]

Fix \(\theta>1/5\), choose \(1/5<\theta_1<\theta\), and then \(0<\gamma<(\theta-\theta_1)/(1-\theta_1)\). For \(x^\theta\le h\le x\) and \(d\le x^\gamma\),
\[
\frac hd\ge \left(\frac xd\right)^{\theta_1},
\qquad x/d\to\infty
\]
uniformly. By (6), the \(\mu^2\)-count in \((x/d,(x+h)/d]\) equals \((6/\pi^2+o(1))h/d\), uniformly for those \(d\). Summing (8) over the interval therefore gives the main contribution
\[
\frac6{\pi^2}h\sum_{d\le x^\gamma}\frac{\kappa(d)}d+o(h).
\tag{10}
\]
The remaining \(d>x^\gamma\) contribute, absolutely,
\[
\begin{aligned}
&\le h\sum_{d>x^\gamma}\frac{|\kappa(d)|}{d}
    +\sum_{d\le 2x}|\kappa(d)|\\
&=o(h)+O_\sigma(x^\sigma)=o(h)
\qquad (0<\sigma<\theta),
\end{aligned}
\tag{11}
\]
by (9) and \(h\ge x^\theta\). The limiting coefficient in (10) is
\[
\frac6{\pi^2}\sum_{d\ge1}\frac{\kappa(d)}d
=\prod_p(1-p^{-2})
   \left(1-\frac1{p^2(p+1)}\right)
=\boxed{c_{\rm sf}}.
\tag{12}
\]
Thus, **uniformly for \(x^\theta\le h\le x\)**,
\[
\boxed{
\sum_{x<n\le x+h}\mu(n)^2w(n)
   =(c_{\rm sf}+o_\theta(1))h .
}
\tag{13}
\]
Independently,
\[
\sum_{n\le x}w(n)
=\sum_{d\le x}\frac{\mu(d)}{d^2}\left\lfloor\frac xd\right\rfloor
=ax+O(1).
\tag{14}
\]
Subtract (13) from the difference of (14) at the two endpoints to obtain
\[
\boxed{
\sum_{\substack{x<n\le x+h\\\mu(n)=0}}w(n)
=(b+o_\theta(1))h.
}
\tag{15}
\]
The factor \(b>0\) follows because every local factor of \(c_{\rm sf}\) is smaller than its counterpart in \(a\). Equations (13)--(15) are *weighted short-interval* statements, not just global mean-value formulas.

## 4. Farey quotient-block scale and uniformity in the source

The exact quotient shell is the interval
\[
\Gamma_H(k)=\left(\frac{H}{k+1},\frac Hk\right],
\quad
x_k=\frac{H}{k+1},
\quad
h_k=\frac{H}{k(k+1)}.
\tag{16}
\]
For \(1\le k\le K=\lfloor H^\alpha\rfloor\),
\[
\frac{h_k}{x_k^\theta}
=\frac{H^{1-\theta}(k+1)^{\theta-1}}k
\gg_\theta H^{1-\theta-\alpha(2-\theta)}.
\tag{17}
\]
A choice \(1/5<\theta<1\) for which the exponent in (17) is positive exists exactly when
\[
\alpha<\frac{1-1/5}{2-1/5}=\boxed{\frac49}.
\tag{18}
\]
In that range \(\min_{k\le K}x_k\to\infty\), \(h_k\le x_k\), and (13)--(15) hold **simultaneously and uniformly** across all \(k\le K\):
\[
A_H(k):=\sum_{r\in\Gamma_H(k)}w(r)
       =(a+o(1))\frac{H}{k(k+1)},
\quad
B_H(k):=\sum_{\substack{r\in\Gamma_H(k)\\\mu(r)=0}}w(r)
       =(b+o(1))\frac{H}{k(k+1)}.
\tag{19}
\]
The same relative \(o(1)\) in (19) can be chosen for every block. Since \(F(k)\ge0\), summing these estimates after multiplication by \(F(k)\) proves (3), **without** an upper bound, smoothness assumption, or asymptotic law for the shell profile. The fixed cutoff \(r>D\) is immaterial because \(H/(K+1)>D\) eventually.

For the physical source, (4) follows simply from \(U_{H,D}\ge U^{\rm term}_{H,D}\) and \(U_{H,D}/E_{H,D}\to0\). FD-037's separate statement that a bad global horizon must concentrate near \(r\lesssim H^{1/3}\) remains true, but is not improved by this squarefree-counting theorem alone.

## 5. Independent controls, prior art, and limits

The convolution (8) was checked independently against the exact multiplicative definition of \(\mu^2(n)w(n)\) for all \(1\le n<150\). Direct finite summation of the Jordan weights through \(H=200000\) gives terminal nonsquarefree fractions \(0.35586\), \(0.35584\), and \(0.35587\) at illustrative exponents \(\alpha=0.2,0.3,0.4\), respectively; these are arithmetic bookkeeping checks, **not** evidence for the uniform asymptotic or its \(4/9\) threshold.

The short-interval theorem itself is Pandey's prior art. The absolute-convolution transfer and its insertion into FD-038's exact Farey/Mertens quotient shells are the derived contribution. The result does not assert novelty of weighted squarefree density in isolation. The explicit exponent in (5) is slightly smaller than \(1/5\), so a more finely calibrated numerical cutoff is possible, but the clean \(4/9\) statement avoids conflating the large formalization constants with a practically accessible regime.

A decisive audit must verify the exact Euler-factor identity (7), uniformity of (6) after interval subdivision, convergence and tail bounds in (9)--(11), and the block exponent in (17). A mere *existence* theorem for one squarefree integer per short interval would **not** justify (13); the density-with-error theorem (5) is essential.

This result is a **terminal quotient occupation theorem**. It neither controls the full \(U_{H,D}/E_{H,D}\), nor supplies a positive global projective Schur gap, nor estimates the Franel--Landau discrepancy at an improved exponent. It does not establish progress toward RH beyond sharpening a necessary condition on an existing candidate route.
