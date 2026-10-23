# PL-463 — Empirical centering weakens but does not remove the prime-window zero-free prerequisite

**Evidence/status:** EXACT-DERIVED + CLASSICAL MELLIN/SELBERG-VARIANCE METHOD / CONDITIONAL ZERO-FREE OBSTRUCTION.

**Parent findings:** PL-458 (deterministically centered covariance), PL-460--PL-461 (uncentered moment obstruction), PL-462 (modulated raw-moment transfer).

## Precise claim

Fix \(0<\theta<1\) and a finite \(A\ge0\). For every sufficiently large real \(X\), put \(H=\lfloor X^\theta\rfloor\) and define
\[
P_X(y)=\sum_{\substack{y<n\le y+H\\n\equiv1\pmod5}}\Lambda(n),
\qquad
\overline P_X=\frac1X\int_X^{2X}P_X(y)\,dy,
\]
\[
V_1(X,H)=\int_X^{2X}|P_X(y)-\overline P_X|^2\,dy
=\min_{c\in\mathbb R}\int_X^{2X}|P_X(y)-c|^2\,dy.
\tag{1}
\]
If the **unproved, all-large-real-scale bound**
\[
\boxed{V_1(X,H)\ll_{\theta,A} XH(\log(2X))^A}
\tag{2}
\]
holds, then every Dirichlet \(L(s,\chi)\) modulo 5 is zero-free in
\[
\boxed{\Re s>1-\theta/2.}
\tag{3}
\]
There is no assumption on \(\overline P_X-H/4\), no raw-moment ceiling, and no prime-pair asymptotic. The center in (1) is the observed mean, chosen separately at every scale. It also suffices to assume the bound with any other scale-dependent constant centers, since the empirical mean minimizes the integral.

At \(\theta=1/2\), this conclusion excludes zeros only in \(\Re s>3/4\); it does **not** give the RH-strength conclusion of [[research/prime_lattice/findings/PL-461-single-identity-residue-moment-zero-free-gate|PL-461]]'s sharper *raw* moment hypothesis. If (2) holds for each of a sequence of fixed \(\theta_j\uparrow1\), with constants and finite logarithmic exponents allowed to depend on \(j\), it implies joint GRH modulo 5, including RH, by the functional equations. Neither (2) nor any new zero-free region is proved unconditionally here.

The mathematical change from PL-460--PL-462 is a different hypothesis: empirical centering invalidates their Jensen/Landau argument, but mean-zero smooth probes still detect every nonconstant Mellin mode. Finite-order inversion of the short-window average makes this assertion valid for **every fixed \(\theta<1\)**, without an artificial endpoint-error cutoff.

## 1. Remove the unknown mean exactly

Let \(w\in C_c^\infty((1,2);\mathbb R)\) satisfy \(\int_1^2w(u)\,du=0\). We will prove that (2) implies
\[
S_w(X):=\sum_{n\equiv1(5)}\Lambda(n)w(n/X)
\ll_{w,\theta,A}X^{1-\theta/2}(\log(2X))^{A/2}.
\tag{4}
\]
For any mean-zero \(f\in C_c^\infty((1,2))\), Cauchy--Schwarz gives directly
\[
\begin{aligned}
\left|\frac1H\int_X^{2X}f(y/X)P_X(y)\,dy\right|
&=\left|\frac1H\int_X^{2X}f(y/X)(P_X(y)-\overline P_X)\,dy\right|\\
&\le\frac{\sqrt X\,\|f\|_{L^2(1,2)}}H\sqrt{V_1(X,H)}\\
&\ll \|f\|_2\frac X{\sqrt H}(\log(2X))^{A/2}.
\end{aligned}
\tag{5}
\]
The first equality is exact. No estimate of the removed mean enters it.

The window average in (5) must still be converted to the fixed test \(w(n/X)\). Replacing it by \(w\) at first order would cost \(O(H\log X)\), too large for (4) when \(\theta>2/3\). The following finite Taylor construction removes that limitation.

## 2. A finite inverse of the box average

Write \(\tau=H/X\), and extend every test function by zero outside \((1,2)\). Define
\[
(B_\tau f)(u)=\frac1\tau\int_0^\tau f(u-v)\,dv.
\]
Choose an integer \(N\ge1\) with
\[
N(1-\theta)>\theta/2.
\tag{6}
\]
Set \(c_0=1\) and, for \(1\le j<N\),
\[
c_j=-\sum_{k=1}^j\frac{(-1)^k}{(k+1)!}c_{j-k},
\qquad
f_\tau=\sum_{j=0}^{N-1}c_j\tau^jw^{(j)}.
\tag{7}
\]
Thus \(c_1=1/2\), \(c_2=1/12\), \(c_3=0\), \(c_4=-1/720\) when those indices occur. These are simply the finite inverse coefficients of the Taylor symbol \((1-e^{-z})/z\), not an assumption that an infinite derivative series converges.

Every \(f_\tau\) has support in the same compact subset of \((1,2)\), has integral zero, and satisfies \(\|f_\tau\|_2\ll_{w,N}1\) for \(0<\tau\le1\). Taylor's theorem with bounded derivatives gives
\[
B_\tau f_\tau=w+O_{w,N}(\tau^N)
\quad\text{uniformly on }\mathbb R.
\tag{8}
\]
Indeed, the coefficient of \(\tau^\ell w^{(\ell)}\), for \(0\le\ell<N\), is
\[
\sum_{k=0}^{\ell}\frac{(-1)^k}{(k+1)!}c_{\ell-k}
=\mathbf1_{\ell=0}
\]
by (7). Expanding each derivative only through total order \(N-1\) leaves a uniformly bounded Taylor remainder of order \(\tau^N\). There is no division by a Fourier multiplier with real zeros.

Swapping the finite window sum and integral gives the exact identity
\[
\frac1H\int_X^{2X}f_\tau(y/X)P_X(y)\,dy
=\sum_{n\equiv1(5)}\Lambda(n)(B_\tau f_\tau)(n/X).
\tag{9}
\]
Compact interior support permits the \(y\)-integral to be extended to all real \(y\); hence windows touching \(X\) or \(2X\) introduce no unaccounted boundary term. The summands in the difference between (9) and \(S_w(X)\) are supported in \([X,3X]\) for large \(X\). The elementary bound \(\Lambda(n)\le\log n\) and (8) therefore give
\[
S_w(X)=\frac1H\int_X^{2X}f_\tau(y/X)P_X(y)\,dy
+O_{w,N}(X\tau^N\log(3X)).
\tag{10}
\]
By (6), the error is \(o(X^{1-\theta/2})\). Applying (5) to \(f_\tau\), using its uniform norm bound and \(H\asymp X^\theta\), proves (4). The order \(N\) and constants may grow as \(\theta\uparrow1\); only a fixed exponent is used in each application.

## 3. Mean-zero probes retain every nontrivial zero

Put \(\sigma_\theta=1-\theta/2\), and define the entire Mellin transform
\[
W(s)=\int_1^2w(u)u^{s-1}\,du,
\qquad W(1)=0.
\]
Bound (4) makes
\[
\mathcal M_w(s)=\int_0^\infty S_w(X)X^{-s-1}\,dX
\tag{11}
\]
holomorphic for \(\Re s>\sigma_\theta\). Near \(X=0\) the sum vanishes; on any bounded positive \(X\)-interval only finitely many integers contribute, so that part causes no singularity.

For \(\Re s>1\), absolute convergence and the change of variable \(u=n/X\) give
\[
\mathcal M_w(s)=W(s)D_1(s),\qquad
D_1(s)=\sum_{n\equiv1(5)}\frac{\Lambda(n)}{n^s}
=\frac14\sum_{\chi\bmod5}-\frac{L'}L(s,\chi).
\tag{12}
\]
The identity residue is load-bearing: its character weights all equal \(1\). At a common zero \(\rho\ne1\) the residues in \(D_1\) add to
\(-\frac14\sum_\chi m_\chi(\rho)\ne0\), so different characters cannot cancel that pole. The principal pole at \(s=1\) is harmless in (12), because \(W(1)=0\).

For every fixed \(\rho\ne1\), there is a **real** mean-zero test \(w\) with \(W(\rho)\ne0\). For example, take \(w=\varphi'\), where \(0\le\varphi\in C_c^\infty((1,2))\) is nonzero and supported sufficiently close to one interior point. Integration by parts gives
\[
W(\rho)=-(\rho-1)\int_1^2\varphi(u)u^{\rho-2}\,du.
\tag{13}
\]
The last integral is nonzero if the support is narrow enough that its complex phases lie in an open half-plane. For real \(\rho\ne1\), positivity of the integrand already suffices.

If a Dirichlet zero had \(\Re\rho>\sigma_\theta\), select this test. The meromorphic continuation of the right side of (12) would have a pole at \(\rho\), contradicting holomorphy of (11) and uniqueness of analytic continuation. This proves (3). Unlike PL-461's one-sided Landau argument, this proof also detects a possible **real** zero directly; it does not require the special mod-5 real-axis nonvanishing calculation. It uses no separation or simplicity of zeros.

The functional equations pair the primitive mod-5 characters and reflect the zeta zeros about \(\Re s=1/2\). Thus the sequence \(\theta_j\uparrow1\) excludes every off-critical nontrivial zero. The extra zeros of \(L(s,\chi_0)=(1-5^{-s})\zeta(s)\) lie on \(\Re s=0\) and are outside the assertion.

## 4. A positive-source control explains the changed exponent

This is a control for the analytic implication, **not** a model of rational or Beurling primes. On \([1,\infty)\), take the positive density
\[
d\mu(x)=(1/4+c x^{\beta-1})\,dx,
\qquad c>0,\quad0<\beta<1.
\]
Its short-window mass is
\[
P_X^\mu(y)=H/4+\frac c\beta\big((y+H)^\beta-y^\beta\big).
\]
For \(y=Xu\), \(1\le u\le2\), and \(H/X\to0\), Taylor expansion followed by subtraction of the observed mean gives
\[
V^\mu(X,H)=c^2H^2X^{2\beta-1}(C_\beta+o(1)),
\quad
C_\beta=\int_1^2\left(u^{\beta-1}-\frac{2^\beta-1}{\beta}\right)^2du>0.
\tag{14}
\]
Consequently \(V^\mu/(XH)\asymp X^{\theta+2\beta-2}\). A mode at \(\beta=1-\theta/2\) is compatible with the variance ceiling. Its source Mellin transform is
\[
\int_1^\infty x^{-s}\,d\mu(x)
=\frac1{4(s-1)}+\frac c{s-\beta}\qquad(\Re s>1),
\]
and its continuation retains the pole at \(s=\beta\). Empirical centering removes the constant mode, but leaves variation of every nonconstant power over a dyadic interval. This shows why the square-root loss in (3) is natural and cannot be improved for arbitrary positive sources merely by reusing the same variance input. It does not establish optimality for the actual prime source.

## Prior art and consequence for the line

The relation between short-interval second moments and horizontal zero distribution is classical. Alessandro Zaccagnini, *The Selberg integral and a new pair-correlation function for the zeros of the Riemann zeta-function* (2016), Section 3.3, records a converse from strong bounds for the deterministically centered multiplicative Selberg integral to a zero-free half-plane. That theorem uses a different window and center; it is not being quoted as (2)--(3). See [the primary paper](https://arxiv.org/abs/1603.02952), source 123 in SOURCES.md. Dirichlet variance/pair-correlation background is already source 106 and PL-415; logarithmic derivatives and functional equations are source 120. Cauchy--Schwarz, finite Taylor inversion and Mellin pole detection are standard tools. No general novelty of variance-to-zero transfer is claimed.

The line-specific result answers an escape explicitly left outside [[research/prime_lattice/findings/PL-460-raw-window-moment-landau-zero-free-gate|PL-460]]'s raw-moment argument: even after **optimally fitting an arbitrary constant mean at every scale**, a covariance-scale upper bound on one identity-residue channel remains a zero-free input. The retained obstruction is quantitatively weaker than the raw-moment one and must be stated with \(1-\theta/2\), not \(1-\theta\).

This does not refute empirical centering as a useful representation or rule out a direct estimate of the signed/oriented source. It does not establish the variance hypothesis, the normalized mod-5 covariance cone, a covariance asymptotic, or a signed cancellation estimate. A relative lower-frame inequality alone does not imply the absolute upper bound (2). A vertical-frequency average, a sparse sequence of scales, or a center depending on \(y\) is a different hypothesis and is not covered. A single fixed mean-zero probe may miss zeros of its own Mellin transform; the proof uses the whole test family supplied by (2). All large real scales, the actual identity-residue logarithmic derivative, and fixed \(\theta<1\) are essential to the stated proof.
