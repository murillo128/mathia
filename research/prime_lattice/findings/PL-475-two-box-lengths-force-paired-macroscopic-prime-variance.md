# PL-475 — Two box lengths force a paired prime-variance floor up to macroscopic windows

**Evidence/status:** LITERATURE+DERIVED / EXACT CONDITIONAL PAIRED VARIANCE FLOOR;
CLASSICAL MULTICHANNEL DECONVOLUTION; NON-EFFECTIVE CONSTANTS;
NO EXTERNAL NOVELTY CLAIM.

## Claim and mathematical delta

Write
\[
a_n=\Lambda(n)\mathbf1_{n\equiv1\ (5)},\qquad
S_{X,L}(y)=\sum_{y<n\le y+L}a_n,
\]
\[
m_{X,L}=X^{-1}\int_X^{2X}S_{X,L}(y)\,dy,\qquad
V_1(X,L)=\int_X^{2X}|S_{X,L}(y)-m_{X,L}|^2\,dy.
\tag{1}
\]
Suppose that \(\zeta\) or one of the three primitive nonprincipal
Dirichlet functions modulo 5 has a nontrivial zero
\(\rho_0=\beta+i\gamma\), \(\beta>1/2\). There are constants
\(c>0,X_0\), depending on the selected zero and the full zero set,
such that, for every real \(X\ge X_0\) and integer \(1\le H\le X/20\),
putting \(K=\lfloor\sqrt2 H\rfloor\),
\[
\boxed{\frac{V_1(X,H)}{H^2}+\frac{V_1(X,K)}{K^2}
       \ge cX^{2\beta-1}.}
\tag{2}
\]
Both variances use the same base interval \([X,2X]\) and their own
empirical means. The statement forces at least one of the two
normalized variances to be large; it does not identify which one.
There is no assumption of a rightmost zero, simple zeros, or finite
zero packets.

The change from
[[research/prime_lattice/findings/PL-473-box-fourier-zeros-obstruct-logarithmic-window-test-inversion|PL-473]]
and
[[research/prime_lattice/findings/PL-474-nonquasianalytic-tests-close-the-iterated-log-window-boundary|PL-474]]
is the **measurement operator**. Two fixed box kernels with length ratio \(\sqrt2\) admit a compactly supported distributional Bezout identity.
Applied to the fixed smooth zero-isolating target, its dilates give
smooth compact tests with uniformly bounded norms and exact joint
recovery. Integer rounding costs only \(O(X^{-1})\) in the target
norm. No increasingly fine nonquasianalytic approximation is needed.
This evades the single-box obstruction without contradicting it.

For example, let \(H=\lfloor X/20\rfloor\) and
\(K=\lfloor\sqrt2 H\rfloor\). If, on any unbounded set of real
\(X\), both unproved ceilings
\[
V_1(X,H)\le C XH(\log X)^A,\qquad
V_1(X,K)\le C XK(\log X)^A
\tag{3}
\]
hold with fixed \(C>0\) and finite \(A\ge0\), then joint GRH for
these four functions follows. The same implication holds for
\(H=\lfloor X/L(X)\rfloor\) with \(L(X)\to\infty\) and
\(\log L(X)=o(\log X)\). Neither ceiling is established here.

## 1. Compact deconvolvers for two box kernels

Let \(\alpha=\sqrt2\), and let
\[
b_a(u)=a^{-1}\mathbf1_{[0,a]}(u),\qquad
\widehat b_a(\xi)=\frac{1-e^{-ia\xi}}{ia\xi},
\]
with the continuous value 1 at zero. We construct compactly supported
finite-order distributions \(T_1,T_2\) satisfying
\[
b_1*T_1+b_\alpha*T_2=\delta_0.
\tag{4}
\]
This is a classical multichannel-deconvolution mechanism (sources
142--143). The following construction verifies the support and scaling
facts needed by the prime application directly.

The elementary quadratic-irrational bound is
\[
\|\alpha n\|_{\mathbb Z}\ge c_0/|n|\qquad(n\ne0).
\tag{5}
\]
Indeed, for the nearest integer \(m\) to \(\sqrt2|n|\),
\(|2n^2-m^2|\ge1\), and rationalizing the difference gives (5).
Since \(|1-e^{-2\pi ix}|\ge4\|x\|_{\mathbb Z}\), the numbers
\[
v_0=0,\qquad v_n=\widehat b_\alpha(2\pi n)^{-1}\quad(n\ne0)
\tag{6}
\]
satisfy \(|v_n|\ll(1+|n|)^2\). They define a 1-periodic
distribution \(V\) with Fourier coefficients \(v_n\). Smooth
periodic test coefficients decay rapidly, so its Fourier pairing
converges absolutely; four derivatives suffice to bound that pairing.

Choose \(w\in C_c^\infty((-1,1))\) with
\(\sum_{j\in\mathbb Z}w(u+j)=1\). Such a function is obtained by
dividing a nonnegative bump positive on \([-1/2,1/2]\) by its positive
periodization. Set \(T_2=wV\). Then
\[
\operatorname{supp}T_2\subset[-1,1],\qquad
\widehat T_2(2\pi n)=v_n.
\tag{7}
\]
The Fourier-sample identity follows by periodizing the compact test
\(w(u)e^{-2\pi inu}\); it does not multiply a distribution by a
nonsmooth interval indicator.

Put \(D=\delta_0-b_\alpha*T_2\), supported in
\([-1,1+\alpha]\). Equations (6)--(7) imply
\(\widehat D(2\pi n)=0\) for every nonzero integer \(n\).
Thus the periodization of \(D'\) is zero: all its periodic Fourier
coefficients vanish, including the coefficient at zero.

For translation \(\tau_jF(u)=F(u-j)\), define the locally finite sum
\[
T_1=\sum_{j\ge0}\tau_jD'.
\tag{8}
\]
It vanishes to the left of \(-1\). To the right of \(1+\alpha\),
the negative-index translates of \(D'\) vanish, so (8) agrees with
the zero full periodization. Hence
\(\operatorname{supp}T_1\subset[-1,1+\alpha]\).
Locally the sum has only finitely many terms; on a compact neighborhood
of its support it is a finite sum of distributions of order at most
five. In particular it has finite order globally.

Telescoping gives \((I-\tau_1)T_1=D'\). Since
\(b_1'=\delta_0-\delta_1\),
\((b_1*T_1-D)'=0\). The difference is a constant distribution with
compact support, hence zero. This proves (4), including the zero
frequency, where \(\langle T_1,1\rangle=1\) and
\(\langle T_2,1\rangle=0\).

## 2. Dilation gives uniform smooth localized tests

Let \(\varphi\in C_c^\infty((4/3,5/3))\) have integral zero.
For a compact distribution \(T\), define its mass-preserving pushforward
by dilation as
\[
\langle T_h,\psi\rangle=\langle T,\psi(h\,\cdot)\rangle.
\]
It sends \(b_a\) to \(b_{ah}\), preserves convolution and fixes
\(\delta_0\). Convolving the dilation of (4) with \(\varphi\), set
\[
f_{1,h}=T_{1,h}*\varphi,\qquad f_{2,h}=T_{2,h}*\varphi.
\]
Then, with \(A_hf=b_h*f\),
\[
\boxed{A_hf_{1,h}+A_{\alpha h}f_{2,h}=\varphi.}
\tag{9}
\]
For \(0<h\le1/20\), both tests are smooth and supported in the
fixed compact interval
\([4/3-1/20,\,5/3+(1+\alpha)/20]\subset(1,2)\).
Both have integral zero, because the integral of a convolution with a
compact distribution is its mass times \(\int\varphi\).

Finite distributional order gives, for each fixed \(\ell\ge0\),
\[
\|f_{j,h}^{(\ell)}\|_\infty
\le C_j\sum_{r=0}^{M_j}h^r
                   \|\varphi^{(\ell+r)}\|_\infty
\le C_{\varphi,\ell},\qquad j=1,2.
\tag{10}
\]
To see the scale factors, apply \(T_j\) to
\(v\mapsto\varphi^{(\ell)}(u-hv)\); each derivative in \(v\)
produces a factor \(h\). A fixed cutoff equal to one near the
support gives the same estimate for the distribution seminorm.
Consequently the sum of the squared \(L^2\) norms and both first
derivative norms are uniformly bounded.

This is continuity on smooth targets with a finite derivative cost.
It is not a bounded inversion operator on arbitrary \(L^2\) signals,
nor an assertion that the distributions themselves are bounded functions.
Only the tests obtained after convolution with \(\varphi\) are used
against the arithmetic source.

## 3. Integer rounding preserves the needed error scale

Let \(h=H/X\), \(K=\lfloor\alpha H\rfloor\), and \(k=K/X\).
Then \(|k-\alpha h|<X^{-1}\). For a smooth function \(f\),
\[
A_af(u)=\int_0^1f(u-at)\,dt
\quad\Longrightarrow\quad
\|A_af-A_bf\|_\infty\le\tfrac12|a-b|\|f'\|_\infty.
\]
Thus (9)--(10) give
\[
\|A_hf_{1,h}+A_kf_{2,h}-\varphi\|_\infty
\le C_\varphi/X.
\tag{11}
\]
All three terms have support in a fixed compact subinterval of
\((0,3)\). For the actual coefficients \(0\le a_n\le\log n\),
\[
\sum_n a_n\{A_hf_{1,h}+A_kf_{2,h}-\varphi\}(n/X)
=O_\varphi(\log(3X)).
\tag{12}
\]
Although the rounded lengths are commensurable, no exact Bezout
identity for that rational pair is asserted. We use the irrational-pair
identity only to construct the tests, and retain the explicit error (11).
The first common Fourier zero of the rounded pair need not be inverted.

## 4. Arithmetic transfer and the paired variance floor

[[research/prime_lattice/findings/PL-471-sparse-zero-annihilators-force-prime-variance-on-every-large-block|PL-471]],
Sections 1--3, constructs a fixed mean-zero smooth test with
\[
\sum_n a_n\varphi(n/X)
=-w_{\rho_0}X^{\rho_0}+O_\varphi(X^{\sigma_0}),
\qquad \tfrac12<\sigma_0<\beta,
\tag{13}
\]
where \(w_{\rho_0}>0\) is the sum of zero multiplicities divided by
four. Its input bump can be chosen inside
\((\log(4/3),\log(5/3))\): multiplication by an exponential and the
convergent derivative series preserve that support. The resulting
\(\varphi\) therefore has the support required above, with the same
Mellin interpolation and explicit formula.

The inputs to (13) remain essential: the fixed-modulus power-saving
zero count gives the sparse-zero annihilator; actual logarithmic-
derivative contour bounds justify the explicit formula; identity-residue
weights prevent pole-residue cancellation. No such formula follows from
the box kernels or a bare meromorphic continuation statement.

For \((L,f)=(H,f_{1,h})\) or \((K,f_{2,h})\), compact support and
mean zero give exactly
\[
\frac1L\int_X^{2X}(S_{X,L}(y)-m_{X,L})f(y/X)\,dy
=\sum_n a_n(A_{L/X}f)(n/X).
\tag{14}
\]
Indeed a term at \(n\) integrates the zero-extended test over
\([n-L,n]\). There is no lost boundary window or approximation to
either empirical mean.

Adding the two pairings, equations (12)--(13) give a modulus at least
\(w_{\rho_0}X^\beta/2\) for all sufficiently large \(X\), uniformly
in the entire range \(1\le H\le X/20\). Cauchy--Schwarz on the
direct sum of the two \(L^2([X,2X])\) spaces bounds its square by
\[
X\left(\frac{V_1(X,H)}{H^2}+\frac{V_1(X,K)}{K^2}\right)
\left(\|f_{1,h}\|_2^2+\|f_{2,h}\|_2^2\right).
\tag{15}
\]
The uniform norm bound (10) proves (2). No statistical independence
between the two windows is used.

For (3), since \(H\le K\le2H\), the upper bound for the left side
of (2) is at most \(2CX(\log X)^A/H\). At
\(H\asymp X\) this is \(O((\log X)^A)\), contradicted by every
\(\beta>1/2\). At \(H=X^{1-o(1)}\) it is
\(X^{o(1)}\), again contradicted. An arbitrary unbounded scale set
suffices. Functional-equation symmetry of the full family converts
exclusion of every \(\beta>1/2\) into the stated joint-GRH implication.
This is a necessary strength test for the paired ceiling, not its proof.

## Prior art, falsification controls, and remaining limits

[Casey and Walnut (1994)](https://doi.org/10.1137/1036140), source 142,
develop compact-distribution multichannel deconvolution through an
analytic Bezout identity. Casey's accessible 1996 report, Section 2.1,
Theorem 2.3, records the classical strongly-coprime existence criterion.
[Pensky and Sapatinas (2011)](https://doi.org/10.1214/11-EJS597),
source 143, study boxcar channels and Diophantine restrictions in a
periodic statistical model. The compact two-box identity here is an
instance of established theory; neither the use of multiple channels
nor the removal of single-channel Fourier zeros is claimed as new.
The proof above supplies the exact localization, uniform dilation,
mean-zero and rounding properties used for (2).

The local mathematical delta is a paired floor on every sufficiently
large base block for all integer lengths through \(X/20\). PL-474's
single-length theorem remains unchanged. The conclusion (2) requires
two variances, and it cannot be silently substituted into an argument
that assumes a ceiling only at one length.

The following controls distinguish what is and is not recovered.

- **Rational-ratio failure.** If \(\alpha=p/q\), the two unscaled
  multipliers vanish together at \(2\pi q\), so (4) is impossible.
  Merely taking two different lengths is insufficient.
- **Small-divisor failure.** For a Liouville \(\alpha\), an identity
  (4) with compact distributions would require
  \(\widehat T_2(2\pi n)=1/\widehat b_\alpha(2\pi n)\).
  Along arbitrarily accurate rational approximations this exceeds
  every polynomial in \(|n|\), whereas a compact distribution's
  transform is polynomially bounded on the real axis. Thus
  irrationality alone does not give this compact finite-order inverse.
- **No arithmetic selectivity in the inverse.** The same two-box
  construction works for generic coefficient sources. Rational primes
  enter only through (13) and the absolute coefficient envelope in
  (12). Phase-twisted or generalized-prime sources do not inherit the
  noncancelling sparse-zero formula merely by using these windows.
- **Separate centers and retained phase.** Each test kills its own
  window mean exactly. The complex target retains one zero mode;
  its real and imaginary parts are legitimate real measurements of
  the unchanged source. No oscillatory cosine lower bound is assumed.
- **Non-effectivity persists.** The analytic deconvolvers are fixed,
  but the target and constants encode the full hypothetical sparse
  zero set. There is no effective finite-zero certificate, no
  uniform onset as \(\beta\downarrow1/2\), and no critical-line
  or simplicity conclusion.
- **The arithmetic estimate is still missing.** Exact recovery does
  not supply either absolute variance ceiling, the mod-5 relative
  covariance frame, or a source-generated positivity principle.
  No numerical extrapolation, Lean verification, or independent
  adversarial approval is claimed.
