# PL-473 — Box Fourier zeros obstruct logarithmic-window test inversion

**Evidence/status:** LITERATURE+DERIVED / EXACT METHOD OBSTRUCTION;
CLASSICAL FOURIER UNCERTAINTY; NO PRIME-VARIANCE COUNTEREXAMPLE.

## Claim and mathematical delta

For the backward box average and Fourier convention
\[
A_hf(u)=h^{-1}\int_0^h f(u-v)\,dv,
\qquad \widehat f(\xi)=\int_{\mathbb R}f(u)e^{-iu\xi}\,du,
\tag{1}
\]
fix a nonzero \(\varphi\in C_c^\infty((1,2))\). The following
obstructions hold for **every** choice of integrable inverse tests,
not just Bernoulli derivative truncations or Gevrey tests.

1. If \(f_h\in L^1(\mathbb R)\) and, for every sufficiently small
   real \(h>0\),
   \[
   \|A_hf_h-\varphi\|_1\le C\exp[-\Omega(1/h)],
   \tag{2}
   \]
   where \(\Omega\ge0\) is locally integrable, then necessarily
   \[
   \int_1^\infty\frac{\Omega(t)}{1+t^2}\,dt<\infty.
   \tag{3}
   \]
   In particular (2) is impossible with
   \(\Omega(t)=ct/(\log t)^r\) for large \(t\), any \(c>0\),
   and \(0\le r\le1\).

2. Fix \(0\le r\le1\), and put, for sufficiently large real \(X\),
   \[
   H_r(X)=\left\lfloor\frac{X}{\log X(\log\log X)^r}\right\rfloor,
   \qquad h_X=H_r(X)/X.
   \tag{4}
   \]
   There are no \(C,\delta>0\) and tests \(f_X\in L^1(\mathbb R)\)
   satisfying
   \[
   \|A_{h_X}f_X-\varphi\|_1\le C X^{-\delta}
   \quad\text{for every sufficiently large real }X.
   \tag{5}
   \]
   The same conclusion holds for a uniform-norm error in (5) when
   \(f_X\) is supported in \([1,2]\).

[[research/prime_lattice/findings/PL-472-gevrey-box-inversion-reaches-near-linear-prime-windows|PL-472]]
proves the prime-variance floor through a fixed zero-isolating test,
bounded inverse tests, and a coefficient-side approximation error for
\(H\le X/(\log X)^B\), every fixed \(B>1\). It leaves the
logarithmic endpoint as a limitation of its Gevrey estimate.
The result here closes a specific proposed repair: changing the
regularity class, truncation scheme, or inverse-test norm cannot give
the uniform power-saving approximation (5) for a fixed nonzero target.
It also covers the smaller window \(X/(\log X\log\log X)\).
It does **not** exclude a variance floor proved by another method.

## 1. Exact multiplier zeros and the uncertainty obstruction

For every \(f\in L^1\), Fubini gives
\[
\widehat{A_hf}(\xi)
=\frac{1-e^{-ih\xi}}{ih\xi}\widehat f(\xi).
\tag{6}
\]
The multiplier has its continuous value 1 at \(\xi=0\).
At \(\xi=2\pi k/h\), \(k\in\mathbb Z\setminus\{0\}\), the
multiplier is exactly zero. Consequently
\[
\boxed{\|A_hf-\varphi\|_1
       \ge |\widehat\varphi(2\pi k/h)|.}
\tag{7}
\]
No norm bound, support restriction, or smoothness of \(f\) was used.

Taking \(k=1\) and \(k=-1\) in (7), and then
\(h=2\pi/|\xi|\), converts (2) into
\[
|\widehat\varphi(\xi)|
 \le C\exp[-\Omega(|\xi|/(2\pi))]
\quad (|\xi|\text{ sufficiently large}).
\tag{8}
\]
The classical [[research/prior_art/incremental/PA-paley-wiener-ingham-logarithmic-integral|Paley–Wiener logarithmic-integral theorem]] says that a
nonzero compactly supported continuous function cannot satisfy such
a Fourier envelope when
\(\int_0^\infty\psi(t)/(1+t^2)\,dt=\infty\).
Use \(\psi(t)=\Omega(t/(2\pi))\) at large \(t\), and zero on
a bounded initial interval, increasing the prefactor if needed.
Its integral diverges exactly when the integral in (3) does.
This proves the necessary condition. Source 139 gives the precise
classical theorem, with the same Fourier convention.

For the displayed family of rates, the decisive integral is
\[
\int^{\infty}\frac{dt}{t(\log t)^r},
\tag{9}
\]
which diverges for \(0\le r\le1\).
At \(r=0\) no logarithmic-integral theorem is needed: (8) gives
exponential Fourier decay, so Fourier inversion extends \(\varphi\)
holomorphically to a strip. Compact support and the identity theorem
then force \(\varphi=0\).

## 2. Integer window rounding does not avoid the obstruction

Write \(t=\log X\) and \(Q(t)=t(\log t)^r\). For \(X=e^t\),
the definition (4) implies
\[
\frac1{h_X}=\frac{X}{\lfloor X/Q(t)\rfloor}
           =Q(t)+O(Q(t)^2e^{-t}).
\tag{10}
\]
This follows by writing \(\lfloor X/Q\rfloor=X/Q-\epsilon\),
\(0\le\epsilon<1\), and expanding \((1-\epsilon Q/X)^{-1}\).
The expansion is uniform for large \(t\), including at jumps of
the floor function.

Since \(\varphi\) has compact support, its Fourier transform is
globally Lipschitz on the real axis:
\[
|\widehat\varphi(\xi)-\widehat\varphi(\eta)|
\le |\xi-\eta|\int |u\varphi(u)|\,du.
\tag{11}
\]
If (5) held, (7), (10), and (11) would give
\[
|\widehat\varphi(\pm2\pi Q(t))|
\le C e^{-\delta t}+C_\varphi Q(t)^2e^{-t}
\le C' e^{-\delta' t}
\tag{12}
\]
for any fixed \(0<\delta'<\min\{\delta,1\}\), once \(t\)
is sufficiently large. The constants do not depend on \(t\).
The strictly increasing function \(Q\) maps a terminal interval
onto a terminal interval, and
\[
t\asymp \frac{Q(t)}{(\log Q(t))^r}.
\]
Thus (12) implies the forbidden full-frequency envelope
\[
|\widehat\varphi(\xi)|
 \le C''\exp\left[-c\frac{|\xi|}{(\log|\xi|)^r}\right]
\quad (|\xi|\text{ sufficiently large}).
\tag{13}
\]
Equation (9) proves the contradiction, including \(r=1\).

If \(\operatorname{supp}f_X\subset[1,2]\), then both
\(A_{h_X}f_X\) and \(\varphi\) are supported in
\([1,2+h_X]\). Its length is at most 2 for large \(X\), so a
uniform-norm bound as in (5) implies the same \(L^1\) bound up to
a factor of 2. This proves the claimed norm version without assuming
that the inverse tests themselves have uniformly bounded norms.

## 3. Exact consequence for the prime-window transfer

For \(a_n=\Lambda(n)\mathbf1_{n\equiv1\ (5)}\), PL-471/PL-472
construct a fixed nonzero mean-zero \(\varphi\) with
\[
\sum_n a_n\varphi(n/X)
=-w_{\rho_0}X^{\rho_0}+O(X^{\sigma_0}),
\qquad \tfrac12<\sigma_0<\beta=\Re\rho_0<1.
\tag{14}
\]
Their centered window pairing uses \(f_X\) supported inside
\((1,2)\) with integral zero, and replaces \(\varphi\) by
\(A_{h_X}f_X\). Writing
\(\varepsilon_X=\|A_{h_X}f_X-\varphi\|_\infty\), the
coefficient-envelope estimate is
\[
\left|\sum_n a_n\{A_{h_X}f_X-\varphi\}(n/X)\right|
\le C X\log(3X)\varepsilon_X.
\tag{15}
\]
To certify an \(o(X^\beta)\) error from this estimate alone one
would impose
\(\varepsilon_X=o(X^{\beta-1}/\log X)\). That implies (5)
for some fixed \(\delta>0\), and is therefore impossible uniformly
on all large scales in (4). Replacing \(X\log X\) by an \(O(X)\)
absolute-mass estimate would still require a power-saving inverse
error and would not remove this obstruction.

This identifies the lost information precisely: a global norm estimate
must control the target at each moving zero of the box multiplier.
The existing arithmetic explicit formula establishes (14), but supplies
no cancellation estimate for the discretized error in (15).
A source-specific bound for that sum could evade the argument because
it need not imply a small global inverse error. An \(X\)-dependent
target would likewise require a new uniform explicit-formula analysis.

## Prior art, controls, and limits

The analytic ingredients are classical. Source 139 states the
Paley–Wiener/Ingham Fourier-decay obstruction; source 140 studies the
loss of frequencies in periodic boxcar deconvolution. The present
nonperiodic multiplier calculation, rounding transfer, and application
to PL-472's error certificate are derived above. No new uncertainty
principle, deconvolution theorem, or external priority is claimed.

The result survives replacement of the primes by any coefficient
source: it is a property of the averaging operator, not arithmetic
rigidity. In particular it cannot itself distinguish rational primes
from phase-twisted or generalized-prime sources.

Several boundaries are essential.

- The target \(\varphi\) is fixed and nonzero. A moving target,
  several different window kernels, or an arithmetic estimate for the
  signed sampling error is outside this statement.
- All sufficiently small \(h\), or all sufficiently large \(X\),
  is essential to (8) or (13). No impossibility on an arbitrary sparse
  unbounded scale set is proved.
- Exact inversion at some widths is possible. If
  \(\varphi=A_{h_*}g\) for a nonzero smooth compactly supported
  mean-zero \(g\), then for \(h=h_*/n\),
  \(f_h=n^{-1}\sum_{j=0}^{n-1}g(\,\cdot-jh)\) satisfies
  \(A_hf_h=\varphi\) exactly. Choose the initial supports so that
  they stay inside \((1,2)\). This is a control against interpreting
  the theorem as a lower bound at every individual width.
- For \(r>1\), (9) converges, so this obstruction no longer
  decides the question. No suitable zero-isolating inverse family or
  prime-variance extension in that regime is constructed here.
- PL-472's error \(e^{-c h^{-1/q}}\), \(q>1\), passes the
  necessary integral test. Its theorem is unchanged.

The proof checks both frequency signs (the zero-isolating test can be
complex), the global error norm, exact box zeros, floor-function jumps,
and the distinction between an absolute error certificate and actual
arithmetic cancellation. No finite numerical calculation would prove
the asymptotic obstruction; the displayed argument does. No Lean
verification or independent adversarial approval is claimed. No
variance ceiling, endpoint variance counterexample, or RH/GRH result
is obtained.
