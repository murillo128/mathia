# ANF-193 — Bonferroni truncation eliminates rough-only critical-width logarithmic coherence

**Status:** EXACT-DERIVED + CLASSICAL-INCLUSION-EXCLUSION + CLASSICAL-THIRD-DERIVATIVE-BOUND + SOURCE-SPECIFIC-ROUGH-TWIST-CANCELLATION + PARTIAL-BOW-REDUCTION. No new general exponential-sum or sieve theorem is claimed.

## 1. Uniform theorem for the actual Ramanujan/rough counterterm

Use the fixed-source normalization of ANF-149/162/163:
\[
R=\exp((\log X)^{1/10}),\quad
P(R)=\prod_{p<R}p,\quad
c_R=\frac{P(R)}{\varphi(P(R))}\ll(\log X)^{1/10},\quad
Q_R(n)=c_R\mathbf1_{(n,P(R))=1}.
\tag{1}
\]
Fix \(0<A_0<B_0\) and \(0<\eta<2/3\). Uniformly over real heights
\(A_0X^2\le |U|\le B_0X^2\), integer intervals \(I\subset[X,3X]\)
of length \(H\) with \(X^{1/3+\eta}\le H\le X\), and the location of
the interval,
\[
\boxed{\displaystyle
\sup_{I,U}\frac1H\left|
  \sum_{n\in I}Q_R(n)(n/X)^{-iU}
\right|=o_{A_0,B_0,\eta}(1).}
\tag{2}
\]
This conclusion is **unconditional**: unlike ANF-192, it does not use
Liu's proposed zero-free half-plane, RH, or a hypothesis about prime
correlations. It exploits the actual rough indicator rather than a
source-alphabet matched control.

In particular, for fixed \(C>0\) and the critical charge
\(a_X=\sqrt{\Delta X\log X}\), \(\Delta>0\) fixed, every interval
\(J\subset[X,3X]\) of length at most \(Ca_X\) satisfies
\[
\boxed{\displaystyle
\sup_{J,U}\left|
 \sum_{n\in J}Q_R(n)(n/X)^{-iU}
\right|=o(a_X).}
\tag{3}
\]
Consequently the physical residual \(r_X=\vartheta-Q_R\) and the prime
component \(\vartheta\) have the **same critical-block twisted sum up
to \(o(a_X)\)**, uniformly in the block's position:
\[
\sum_{n\in J}r_X(n)(n/X)^{-iU}
=\sum_{n\in J}\vartheta(n)(n/X)^{-iU}+o(a_X).
\tag{4}
\]
This does not assert prime cancellation, or a bound for prefixes of the
full bow length \(K=X^{1-2\varepsilon+o(1)}\).

## 2. An elementary finite-sieve approximation with subpolynomial support

Write \(t=\log X\), \(z=R=e^{t^{1/10}}\), and choose the even integer
\[
m=2\left\lfloor\frac{t^{1/20}}2\right\rfloor,\qquad
D=z^m=\exp(O(t^{3/20}))=X^{o(1)}.
\tag{5}
\]
For \(w(n)=\#\{p<z:p\mid n\}\) define the Bonferroni polynomials
\[
B_j(n)=\sum_{\nu=0}^j(-1)^\nu\binom{w(n)}\nu.
\]
The exact alternating-binomial identity gives the **pointwise** bounds
\[
B_{m-1}(n)\le\mathbf1_{w(n)=0}\le B_m(n),
\qquad B_m(n)-B_{m-1}(n)=\binom{w(n)}m.
\tag{6}
\]
Thus replacing the rough indicator by \(B_{m-1}\) costs, even against
arbitrary complex weights of modulus one, at most
\[
\begin{aligned}
\sum_{n\in I}\bigl|\mathbf1_{w(n)=0}-B_{m-1}(n)\bigr|
&\le\sum_{\substack{d\mid P(z)\\\omega(d)=m}}
       \left(\frac Hd+1\right)\\
&\le H\frac{M_z^m}{m!}+\binom{\pi(z)}m,
\qquad M_z=\sum_{p<z}\frac1p.
\end{aligned}\tag{7}
\]
The classical reciprocal-prime estimate gives
\(M_z\ll\log\log z\ll\log t\); hence \(m\gg M_z\) and
\[
\frac{M_z^m}{m!}\le(eM_z/m)^m
\le\exp(-c\,t^{1/20}\log t)=o(t^{-A})
\quad\text{for every fixed }A>0.
\tag{8}
\]
Moreover \(\binom{\pi(z)}m\le z^m=D=X^{o(1)}\).
The truncated polynomial has the **exact** divisor expansion
\[
B_{m-1}(n)=
\sum_{\substack{d\mid P(z)\\\omega(d)<m\\d\mid n}}\mu(d).
\tag{9}
\]
All participating \(d\) obey \(d\le D\), and their number is at most
\(\sum_{\nu<m}\binom{\pi(z)}\nu\le mD=X^{o(1)}\).
No use is made of the full period \(P(R)\), which is **not**
\(X^{o(1)}\) and cannot be treated as a short modulus.

## 3. Third-derivative cancellation on every surviving progression

For each divisor \(d\) in (9), write \(n=dk\) on the interval \(I\);
the number of terms is \(N=H/d+O(1)\asymp H/d\), because
\(d\le D=X^{o(1)}\). For
\[
f_d(k)=-\frac{U}{2\pi}\log(dk/X),
\]
the exact third derivative is \(f_d'''(k)=-U/(\pi k^3)\), so
\[
|f_d'''(k)|\asymp_{A_0,B_0}\frac{d^3}{X}
\tag{10}
\]
throughout every progression in \([X,3X]\), uniformly in the height
window. The classical third-derivative van der Corput estimate
(the same form used for the carrier in ANF-186/188) gives
\[
\left|\sum_{dk\in I}e(f_d(k))\right|
\ll N\left[
  N^{-1/4}
  +\left(\frac{d^3}{X}\right)^{1/6}
  +\left(\frac{d^3N^3}{X}\right)^{-1/4}
\right].
\tag{11}
\]
With \(d\le D\) and \(N\asymp H/d\), the bracket is at most a constant
times
\[
\rho_X(H):=
\left(\frac DH\right)^{1/4}
 +D^{1/2}X^{-1/6}
 +\left(\frac X{H^3}\right)^{1/4}.
\tag{12}
\]
For every fixed \(\eta>0\), uniformly over \(H\ge X^{1/3+\eta}\),
\[
\rho_X(H)
\ll X^{-(1/3+\eta)/4+o(1)}
   +X^{-1/6+o(1)}
   +X^{-3\eta/4}
=X^{-c(\eta)+o(1)}
\tag{13}
\]
for \(c(\eta)=\min\{(1/3+\eta)/4,1/6,3\eta/4\}>0\).
Summing (11) over at most \(mD=X^{o(1)}\) divisor terms
and combining (7)--(8) yields the explicit controlled error
\[
\left|\sum_{n\in I}Q_R(n)(n/X)^{-iU}\right|
\ll c_R\left[
HmD\rho_X(H)+H(eM_z/m)^m+O(mD)
\right]=o(H).
\tag{14}
\]
Every term in (14) is uniform in the translated interval and the
prescribed height. This proves (2). For (3), take
\(H_0=X^{2/5}\), which lies above \(X^{1/3+1/30}\) and below \(a_X\).
When \(|J|<H_0\), the trivial estimate
\(|\sum_JQ_R(n)(n/X)^{-iU}|\le c_RH_0=o(a_X)\)
suffices; otherwise (2), with \(\eta=1/30\), gives \(o(|J|)=o(a_X)\).
This proves (3)--(4).

## 4. Scope, falsification controls, and prior-art boundary

The statement needs a **fixed height annulus** \(|U|\asymp X^2\):
the third derivative used in (10) is not bounded below for small
\(|U|\). It proves relative cancellation only above the cubic
physical scale \(X^{1/3+\eta}\), not on intervals at or below
\(X^{1/3}\). The \(o(a_X)\) absolute assertion concerns **individual
blocks of length \(O(a_X)\)**; summing the errors over
\(K/a_X\) blocks is not legitimate evidence for an \(o(a_X)\)
full-prefix bound. Weighted variants follow by Abel summation on a
critical block only for uniformly bounded-variation weights; no
arbitrary carrier-dependent sign weights are controlled.

The two inputs are classical: Bonferroni/inclusion-exclusion with
reciprocal-prime summation, and the third-derivative van der Corput
estimate already invoked and bibliographically delimited in
ANF-186/188 and SOURCES.md. This is a specialization to the **actual**
Mathia rough counterterm, not a new result about zeta zeros or a new
general sieve theorem. It is stronger on the critical physical block
than ANF-162/163's phase-blind \(L^2/L^1\) estimates, and unlike
ANF-186/189's synthetic source-alphabet matched controls it constrains
where genuine rough sites can sit relative to the exact logarithmic
carrier.

A decisive way to falsify this argument is to find an invalid
Bonferroni sandwich, a divisor-count factor that grows as a fixed power
of \(X\), or a loss of cubic derivative uniformity on \(d\)-progressions;
(5)--(14) display all three necessary bounds. **The prime term is
untouched**, so even on one critical block this does not supply
\(\sum_Jr_X(n)(n/X)^{-iU}=o(a_X)\). At full bow length, neither the
rough nor the prime component has yet been shown individually
\(o(a_X)\). This finding therefore narrows one source-side obstruction
without solving the distinguished-height endpoint or RH.
