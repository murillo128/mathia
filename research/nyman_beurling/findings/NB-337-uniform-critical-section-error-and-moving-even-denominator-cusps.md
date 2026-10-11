# NB-337 — Uniform critical-section error and moving even-denominator cusps

- **Date:** 2026-10-11
- **Status:** proved
- **Research line:** nyman_beurling
- **Depends on:** NB-304, NB-332, NB-333, NB-334, NB-336
- **Classification:** EXACT-DERIVED + SOURCE-SIDE + QUANTITATIVE-FINITE-SECTION + MOVING-CRITICAL-CUSP + NON-TARGET-AWARE + PRIOR-ART-AUDITED

## Claim

Use the projected dilation and adjacent witness from NB-333:

\[
U_n=\operatorname{span}\{g_2,\ldots,g_n\},\quad
T_{n,m}=P_{U_n}A_m|_{U_n},\quad
\nu_q=g_q-\frac{q-1}{q}g_{q-1},
\]
\[
m=dq+r,\qquad
\mathcal F_{n;q,d,r}
=\langle(\sqrt m\,T_{n,m}-R_n)g_2,\nu_q\rangle,
\]
where \(8\le q\le n\), \(d\ge1\), \(r\ge0\) are integers. Write
\(\delta=d/q\), \(\rho=r/d\), and retain the exact NB-333 profile

\[
\mathfrak D(x)=\sum_{k\ge1}\frac{\|kx\|_{\mathbb Z}^2}{k^2},
\qquad
\Phi(\delta,\rho)
=\frac{\mathfrak D(\rho\delta)-\mathfrak D((1+\rho)\delta)}{4\delta}.
\tag{1}
\]

**Uniform quantitative critical profile.** For all fixed \(0<a<b<\infty\)
and \(R<\infty\), there exists \(C_{a,b,R}<\infty\) such that

\[
\boxed{
\left|q\mathcal F_{n;q,d,r}-\Phi(d/q,r/d)\right|
\le C_{a,b,R}\frac{\log(2q)}q
}
\tag{2}
\]

uniformly over \(a\le d/q\le b\), \(0\le r/d\le R\), and \(n\ge q\).
In particular, this is a *two-parameter* estimate, not just the
fixed-aspect-ratio sequential limit of NB-333.

**Moving cusp.** Fix \(L\in\mathbb N\) and \(\rho_0>0\) such that the
fractional part of \(L\rho_0\) has reduced even denominator \(B\).
Suppose \(d_q/q=L+\varepsilon_q\to L\), \(\varepsilon_q\ne0\), and
\(|r_q/d_q-\rho_0|\le C/q\) for a fixed \(C\). Then

\[
\boxed{
q\mathcal F_{n;q,d_q,r_q}
=\frac1{4BL}|\varepsilon_q|
\log\frac1{|\varepsilon_q|}
+O_{L,\rho_0,C}\left(
|\varepsilon_q|+\frac{\log(2q)}q
\right).
}
\tag{3}
\]

For integer drift \(d_q=Lq+K_q\), with \(|K_q|\to\infty\) and
\(|K_q|=o(q)\), choose \(r_q\) to be the nearest integer to
\(\rho_0d_q\). Then the main term dominates, giving the *actual
finite-section asymptotic*

\[
\boxed{
q\mathcal F_{n;q,d_q,r_q}
\sim \frac{|K_q|}{4BLq}
\log\frac q{|K_q|}>0.
}
\tag{4}
\]

For the explicit phase \(\rho_0=1/(2L)\), \(B=2\) and the leading
constant in (3) is \(1/(8L)\). Thus the even-denominator log-enhanced
cusp of NB-336 survives every mesoscopic integer displacement
\(|K_q|\to\infty\), \(|K_q|=o(q)\), rather than only when the aspect
ratio is held fixed away from the integer node.

## 1. Exact finite cells and a uniform tail

Set
\[
\varphi(t)=\{t\}-\tfrac12,\quad
\alpha=1+\rho/q,\quad
\beta=1+\frac{1+\rho}{q-1},\quad c=\frac{q-1}{q}.
\]
The exact scaling identity in NB-333 gives, without approximating the
projection or changing the ambient section,
\[
h(y)=\varphi(\alpha y)-c\varphi(\beta y),
\qquad
q\mathcal F_{n;q,d,r}
=\frac{qd}{2}\sum_{J\in S_d}I_{q,J},
\tag{5}
\]
where
\[
S_d=\{J\ge1:\lfloor J/d\rfloor\ \text{is odd}\},
\qquad I_{q,J}=\int_J^{J+1}\frac{h(y)}{y^2}\,dy.
\]
The first selected cell is \(J=d\ge aq\), so no singular behavior
near \(y=0\) enters this argument.

Write \(b_J=\int_J^{J+1}h(y)\,dy\) and
\(H_J(x)=\int_0^x(h(J+t)-b_J)\,dt\). The periodic primitive
\(\Psi(t)=\frac12(\{t\}^2-\{t\})\) is continuous at integers and has
derivative \(\varphi\) off them. Each of the two affine phases in
\(h\) traverses one full period plus a remainder of length
\(O_R(1/q)\). Hence \(|b_J|\le C_R/q\). The centered primitive
\(H_J\) is bounded uniformly in \(J,q,\rho\) for \(0\le\rho\le R\).
An exact integration by parts gives
\[
I_{q,J}=\frac{b_J}{J(J+1)}
      +2\int_0^1\frac{H_J(x)}{(J+x)^3}\,dx,
\qquad
|I_{q,J}|\le C_R\left(\frac1{qJ^2}+\frac1{J^3}\right).
\tag{6}
\]
Consequently, for \(Z\ge a\), the selected tail \(J>qZ\) contributes
\(O_{a,b,R}(Z^{-1})\) to \(q\mathcal F\), uniformly in all parameters.

## 2. The limiting kernel has uniformly bounded variation

For \(z=J/q\), define \(\psi(t)=\{t\}(1-\{t\})\) and
\[
C_\rho(z)=
\frac{\rho\varphi(\rho z)-(1+\rho)\varphi((1+\rho)z)}{z^2}
-\frac{\psi((1+\rho)z)-\psi(\rho z)}{z^3}.
\tag{7}
\]
Away from the fractional-part breakpoints,
\[
C_\rho(z)=B_\rho'(z),\qquad
B_\rho(z)=
\frac{\psi((1+\rho)z)-\psi(\rho z)}{2z^2}.
\tag{8}
\]
The primitive \(B_\rho\) is continuous at all breakpoints.

For \(z\ge a>0\) and \(0\le\rho\le R\), \(C_\rho(z)=O_{a,R}(z^{-2})\).
Its derivative between phase jumps is bounded by
\(C_{a,R}(z^{-2}+z^{-3}+z^{-4})\). The jumps at the lattices
\(k/\rho\) (when \(\rho>0\)) and \(k/(1+\rho)\) have sizes
\(O_R(z^{-2})\); their total weighted variation is uniformly
summable. Thus
\[
\sup_{0\le\rho\le R}
\operatorname{Var}_{[a,\infty)}C_\rho<\infty.
\tag{9}
\]
With \(S_\delta=\bigcup_{j\ge0}[(2j+1)\delta,(2j+2)\delta)\), the
same bound holds for \(\mathbf1_{S_\delta}C_\rho\), uniformly in
\(a\le\delta\le b\): its additional jumps are separated by at
least \(a\), and \(C_\rho(z)=O(z^{-2})\).
The bounded-variation grid estimate therefore yields
\[
\frac1q\sum_{J\in S_d}C_\rho(J/q)
=\int_{S_\delta}C_\rho(z)\,dz+O_{a,b,R}(q^{-1}),
\qquad \delta=d/q.
\tag{10}
\]
Finally the endpoint calculation of NB-333, or integration of
\(B_\rho'\) over the alternating intervals, gives the exact identity
\[
\frac\delta2\int_{S_\delta}C_\rho(z)\,dz=\Phi(\delta,\rho).
\tag{11}
\]

## 3. Uniform cell comparison, including phase folds

It remains to compare \(q^3 I_{q,J}\) with \(C_\rho(z)\). Set
\(z=J/q\) and truncate initially at
\(z\le Z_q=q/[16(1+R)]\). Periodicity of \(\Psi\) gives the **exact**
cell-mean expression
\[
b_J=
\frac{\Psi(\rho z+\rho/q)-\Psi(\rho z)}{\alpha}
-\frac c\beta
\left[
\Psi\left(\frac{(1+\rho)qz}{q-1}+\frac{1+\rho}{q-1}\right)
-\Psi\left(\frac{(1+\rho)qz}{q-1}\right)
\right].
\tag{12}
\]
Call a cell *bad* if either (when \(\rho>0\)) the interval
\([\rho z,\rho z+\rho/q]\) or the interval
\([(1+\rho)z,(1+\rho)z+(1+\rho)(z+1)/(q-1)]\)
meets an integer. Otherwise both differences in (12) lie on
single quadratic branches. Their Taylor expansions give
\[
qb_J=\rho\varphi(\rho z)
-(1+\rho)\varphi((1+\rho)z)
+O_R((1+z)/q).
\tag{13}
\]
The centered function \(h(J+x)-b_J\) differs in \(L^1(0,1)\) by
\(O_R((1+z)/q)\) from the zero-mean translate difference
\(\varphi(x+\rho z)-\varphi(x+(1+\rho)z)\).
Indeed the periodic sawtooth has uniformly controlled \(L^1\)
translation error, even when a phase passes through a jump.
Its primitive therefore satisfies
\[
2\int_0^1H_J(x)\,dx
=-\bigl[\psi((1+\rho)z)-\psi(\rho z)\bigr]
+O_R((1+z)/q).
\tag{14}
\]
Substituting (13)--(14) into the exact formula (6), and using
\(z\ge a\), proves for every good cell
\[
|q^3I_{q,J}-C_\rho(z)|
\le C_{a,R}\frac{1+z}{qz^2}.
\tag{15}
\]
After multiplication by the Riemann-sum weight
\(\delta/(2q)\), the total good-cell error over
\(a\le z\le Z_q\) is \(O_{a,b,R}(\log(2q)/q)\).

Bad cells need no Taylor expansion: (6)--(7) give the crude
\[
|q^3I_{q,J}-C_\rho(z)|\le C_{a,R}z^{-2}.
\tag{16}
\]
For the first phase, each positive integer crossing at \(k/\rho\)
occupies an interval of width \(1/q\) in \(z\), containing
\(O_R(1)\) grid cells. Summing their \(z^{-2}\) weights gives
\(O_{a,R}(1/q)\) after the Riemann prefactor. For the second phase,
the crossing near \(k/(1+\rho)\) occupies a one-sided interval of
width \(O_R((k+1)/q)\), hence at most \(O_R(k+1)\) grid cells of
weight \(O_R(k^{-2})\). Its total error is at most
\[
\frac{C_{a,b,R}}q\sum_{1\le k\le O_R(q)}
\frac{k+1}{k^2}
=O_{a,b,R}\left(\frac{\log(2q)}q\right).
\tag{17}
\]
These estimates also cover phases arbitrarily close to breakpoints:
there is no assumption of Diophantine separation.

The remaining \(z>Z_q\) tails in the cell sum and kernel integral
are \(O_{a,b,R}(1/q)\) by (6)--(7). For the finitely many small
values of \(q\) for which the truncated range is empty, enlarge
\(C_{a,b,R}\) using the same absolute tail bounds. Combining
(10)--(11), (15), and (17) proves (2).

## 4. Transfer through a moving rational cusp

The summand \(f(t)=\|t\|_{\mathbb Z}^2\) is bounded and globally
Lipschitz. Split its series at \(k\asymp|h|^{-1}\); the initial
harmonic sum and the absolutely summable tail give
\[
|\mathfrak D(x+h)-\mathfrak D(x)|
\le C|h|\log(e/|h|),\quad 0<|h|\le\tfrac12,
\tag{18}
\]
uniformly in \(x\). Hence replacing \(\rho_0\) by
\(\rho_q=r_q/d_q\), with \(|\rho_q-\rho_0|\le C/q\), changes
\(\Phi(\delta,\rho)\) by
\(O_{L,\rho_0,C}(\log(2q)/q)\).

NB-336 proves at the fixed rational even-denominator phase
\[
\Phi(L+\varepsilon,\rho_0)
=\frac1{4BL}|\varepsilon|
  \log\frac1{|\varepsilon|}
+O_{L,\rho_0}(|\varepsilon|).
\tag{19}
\]
Combining (19), (18) and (2) proves (3). For
\(\varepsilon_q=K_q/q\), \(|K_q|\to\infty\),
\(|K_q|=o(q)\), both error terms are smaller than
\((|K_q|/q)\log(q/|K_q|)\). In particular,
\(|K_q|\log(q/|K_q|)/\log q\to\infty\):
if \(\log(q/|K_q|)\ge\log|K_q|\), the ratio is
at least \(|K_q|/2\); otherwise it exceeds
\(|K_q|\log(q/|K_q|)/(2\log|K_q|)\).
This proves (4).

## 5. Independent checks, prior art, and boundaries

A numerical falsification check integrated the sawtooth terms
piecewise over the exact alternating selector blocks and computed
the rational profile from trigamma sums. At
\(\delta=6/5\), \(\rho=1/2\), the diagnostic values of
\(q\mathcal F-\Phi\) for \(q=80,160,320\) were approximately
\(0.0015051,0.0007482,0.0003738\), respectively. These
truncated evaluations are corroborative only; the proof rests
on (5)--(19), including the independently controlled tails.

The closest primary literature concerns the discrete
Nyman--Beurling/Báez-Duarte criterion and the multiplicative
autocorrelation of the fractional-part function:
L. Báez-Duarte, M. Balazard, B. Landreau, E. Saias,
*Sur l'autocorrelation multiplicative de la fonction partie
fractionnaire*, arXiv:math/0306251, and M. Balazard,
B. Martin, *Sur l'autocorrélation multiplicative de la fonction
partie fractionnaire et une fonction définie par J. R. Wilton*,
arXiv:1305.4395. Those sources establish the neighboring
autocorrelation setting, not a cited finite-section rate of
the form (2); no bibliographic originality is claimed.
No new external theorem is load-bearing, so the current
SOURCES.md anchors suffice.

The uniformity requires \(d/q\) bounded above and bounded away
from zero and \(r/d\) in a fixed bounded range. Nothing here
resolves \(|K_q|=O(1)\): there the limiting cusp scale is of
the same order as the proved \(O(\log q/q)\) remainder, and
its sign cannot be inferred from (3). The result measures
only one source/probe coefficient, not the occupation of
that channel by the moving Nyman target. It establishes no
uniform positive operator-norm gap, approximation-distance
estimate, or consequence for RH.

**Mathematical delta.** NB-336 left the interchange of the
critical-section and moving-cusp limits unproved. The
quantitative fold estimate (17) supplies a uniform rate
strong enough to settle every mesoscopic integer drift
\(|K_q|\to\infty\), \(|K_q|=o(q)\) for the rational phases
identified there. The microscopic \(O(1)\) drift layer and
the genuinely target-aware implication remain separate
open problems.
