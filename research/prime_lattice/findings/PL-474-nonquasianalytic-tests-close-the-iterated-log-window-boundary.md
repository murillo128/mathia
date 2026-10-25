# PL-474 — Nonquasianalytic tests close the iterated-log window boundary

**Evidence/status:** LITERATURE+DERIVED / EXACT CONDITIONAL VARIANCE FLOOR;
CLASSICAL REGULARITY THRESHOLD; NON-EFFECTIVE CONSTANTS;
NO EXTERNAL NOVELTY CLAIM.

## Claim and mathematical delta

For the actual identity-residue source define
\[
a_n=\Lambda(n)\mathbf1_{n\equiv1\ (5)},\qquad
S_{X,H}(y)=\sum_{y<n\le y+H}a_n,
\]
\[
m_{X,H}=X^{-1}\int_X^{2X}S_{X,H}(y)\,dy,\qquad
V_1(X,H)=\int_X^{2X}|S_{X,H}(y)-m_{X,H}|^2\,dy.
\tag{1}
\]
Suppose that \(\zeta\) or a primitive nonprincipal Dirichlet function
modulo 5 has a nontrivial zero \(\rho_0=\beta+i\gamma\) with
\(\beta>1/2\). For every fixed \(r>1\), there are \(c>0,X_0\)
such that, uniformly for real \(X\ge X_0\) and integers \(H\),
\[
\boxed{1\le H\le \frac{X}{\log X(\log\log X)^r}
\quad\Longrightarrow\quad
V_1(X,H)\ge cH^2X^{2\beta-1}.}
\tag{2}
\]
Constants may depend on the full zero set, the selected zero, and
\(r\). No rightmost zero, zero simplicity, or pole separation is
assumed.

The fixed-target box-inversion method therefore has an exact boundary
within the family
\(H_r(X)=\lfloor X/[\log X(\log\log X)^r]\rfloor\), \(r\ge0\):

- for every \(r>1\), a fixed nonzero zero-isolating target admits
  compactly supported, mean-zero, uniformly bounded inverse tests
  whose uniform error is smaller than every negative power of \(X\);
- for \(0\le r\le1\), PL-473 excludes even an \(L^1\) error
  \(O(X^{-\delta})\), \(\delta>0\), for every fixed nonzero compact
  target and arbitrary integrable inverse tests on all large scales.

This is a sharp boundary for that **uniform fixed-target approximation
certificate**, not a sharp boundary for prime variance itself.
[[research/prime_lattice/findings/PL-472-gevrey-box-inversion-reaches-near-linear-prime-windows|PL-472]]
reaches \(H\le X/(\log X)^B\), \(B>1\); (2) reaches a strictly
larger range than every such fixed \(B\).
[[research/prime_lattice/findings/PL-473-box-fourier-zeros-obstruct-logarithmic-window-test-inversion|PL-473]]
leaves precisely this convergent-logarithmic-integral side undecided.

As a consequence, for one fixed \(r>1\), the unproved ceiling
\[
V_1(X,H_r(X))\le C XH_r(X)(\log X)^A
\tag{3}
\]
on any unbounded set of real \(X\), with fixed \(C>0\) and finite
\(A\ge0\), implies joint GRH for these four functions. Neither
(3), a covariance lower frame, nor an independent GRH mechanism is
proved here.

## 1. A compact bump finer than every fixed Gevrey order greater than one

Fix \(1<q<r\), and write
\[
L_j=\log(e+j),\qquad M_j=j!L_j^{qj},\qquad M_0=1.
\tag{4}
\]
There is a nonnegative, nonzero \(\eta\in C_c^\infty((0,\log2))\)
with
\[
\|\eta^{(j)}\|_\infty\le C R^j M_j.
\tag{5}
\]
This is a classical [[research/prior_art/incremental/PA-nonquasianalytic-infinite-convolution-cutoff|nonquasianalytic cutoff]]. For the precise bound,
take interval probability densities of widths
\(d_j=\varepsilon/[jL_j^q]\), \(j\ge1\), and one fixed width
\(d_0>0\). Their widths have finite sum because \(q>1\).
Choose them small with \(d_1\le d_0\), and translate their infinite convolution into
\((0,\log2)\). The classical convolution lemma gives a smooth
nonnegative density of integral one and
\[
\|\eta^{(j)}\|_\infty
\le \frac{2^j}{d_0d_1\cdots d_j}
\le d_0^{-1}(2/\varepsilon)^j j!L_j^{qj}.
\tag{6}
\]
Rainer's Lemma 3.3, source 141, states this construction and bound.
Concretely, each differentiated interval density has total variation
\(2/d_j\); the undifferentiated density supplies the \(L^\infty\)
bound. Remaining probability convolutions do not increase it, and
the summable widths give convergence of every derivative.

We need the fine bound (5), not merely membership in some Gevrey
class. For \(j,\ell\ge0\), it satisfies
\[
M_{j+\ell}\le D^{j+\ell}M_jM_\ell,
\qquad D=2^{q+1}.
\tag{7}
\]
For positive \(j,\ell\), put \(n=j+\ell\). Since
\(\log(e+x)/x\) decreases,
\[
\frac{L_n^n}{L_j^jL_\ell^\ell}
\le (n/j)^j(n/\ell)^\ell\le2^n.
\]
Together with \(n!/(j!\ell!)\le2^n\), this proves (7).
Zero indices give equality before the factor \(D^n\).

## 2. Exact sparse-zero isolation preserves this finer class

Fix \(1/2<\sigma_0<\beta\). The unconditional fixed-modulus
zero-density estimate used in
[[research/prime_lattice/findings/PL-471-sparse-zero-annihilators-force-prime-variance-on-every-large-block|PL-471]]
gives an exponent \(0<a<1\) with
\[
\#\{\lambda:\Re\lambda>\sigma_0,\ |\lambda|\le T\}
\ll(1+T)^a.
\tag{8}
\]
Here \(\lambda\) ranges over the distinct nontrivial zeros of the
four functions. This follows from the classical power
\(3(1-\sigma)/(2-\sigma)<1\) for \(\sigma>1/2\), absorbing
logarithms and using monotonicity above \(4/5\); see source 128.
The PL-471 genus-zero product
\[
P(s)=(s-1)\prod_{\substack{\Re\lambda>\sigma_0\\
                                  \lambda\ne\rho_0}}(1-s/\lambda)
=\sum_{j\ge0}p_js^j
\]
has \(P(\rho_0)\ne0\) and
\[
|p_j|\le C K^j/(j!)^{1/a}.
\tag{9}
\]
These are the same product and coefficient estimate as PL-471;
only its input bump is changed.

Set \(g(t)=e^{-\rho_0t}\eta(t)\). Leibniz's rule and the
monotonicity of \(M_j\) preserve (5) with different constants.
For
\[
k(t)=\sum_{j\ge0}p_j(-1)^j g^{(j)}(t),
\tag{10}
\]
equations (7)--(9) give
\[
\|k^{(\ell)}\|_\infty
\le C(RD)^\ell M_\ell
\sum_{j\ge0}(KRD)^j
                 (j!)^{1-1/a}L_j^{qj}
\le C'R'^\ell M_\ell.
\tag{11}
\]
The series converges: its logarithm has the negative leading term
\(-(1/a-1)j\log j\), whereas \(qj\log L_j=O(j\log\log j)\).
Thus (10) converges in every smooth norm, preserves support, and
preserves the same \(q\), with no requirement \(q<1/a\).

Integration by parts gives
\(\int k(t)e^{st}dt=P(s)\int g(t)e^{st}dt\).
Normalize by \(P(\rho_0)\int\eta\) and put
\(\varphi(u)=k(\log u)/(P(\rho_0)\int\eta)\).
Then \(\varphi\in C_c^\infty((1,2))\), and its Mellin transform
\(\Phi(s)=\int\varphi(u)u^{s-1}du\) obeys
\[
\Phi(1)=0,\qquad\Phi(\rho_0)=1,\qquad
\Phi(\lambda)=0\quad(\Re\lambda>\sigma_0,\ \lambda\ne\rho_0).
\tag{12}
\]
The substitution is \(u^{s-1}du=e^{st}dt\), so in particular
\(\int\varphi=0\).

The analytic change of variable also preserves (4): for \(n\ge1\),
the derivative formula for \(k(\log u)\) and the unsigned Stirling
bound
\(|s(n,j)|\le(n!/j!)\binom{n-1}{j-1}\) give
\[
\begin{aligned}
|\varphi^{(n)}(u)|
&\le C n!\sum_{j=1}^n\binom{n-1}{j-1}R'^j L_j^{qj}\\
&\le C n!L_n^{qn}R'(1+R')^{n-1}.
\end{aligned}
\]
On the support, \(u^{-n}\le1\); outside it the smooth zero
extension vanishes. Hence, for some \(B\ge1\),
\[
\boxed{\|\varphi^{(n)}\|_\infty\le C_\varphi B^n M_n.}
\tag{13}
\]

The full arithmetic explicit formula is applied only to this fixed
test. Exactly as in PL-471, (12) leaves
\[
\sum_n a_n\varphi(n/X)
=-w_{\rho_0}X^{\rho_0}+O_\varphi(X^{\sigma_0}),
\qquad w_{\rho_0}=\tfrac14\sum_\chi m_\chi(\rho_0)>0.
\tag{14}
\]
The zero sum below \(\sigma_0\) is absolutely summable against
\(\Phi\); the trivial-zero, missing-factor-at-5 and left-contour
terms are the bounded remainder established there. Its contour-growth
input remains essential and is not inferred from sparsity alone.

## 3. Uniform finite inverse at the logarithmic-integral scale

Let \(A_hf(u)=h^{-1}\int_0^h f(u-v)dv\), and use the classical
Bernoulli coefficients
\[
\frac{z}{1-e^{-z}}=\sum_{j\ge0}c_jz^j,\qquad |c_j|\le C_0.
\]
For every finite \(N\ge1\), PL-472's Taylor remainder gives
\[
f_{h,N}=\sum_{j=0}^{N-1}c_jh^j\varphi^{(j)},\qquad
\|A_hf_{h,N}-\varphi\|_\infty
\le C_1 C_\varphi(Bh)^NM_N.
\tag{15}
\]
The constant is independent of \(N,h\): the remainder coefficient
is bounded by \(\sum_{j<N}|c_j|/(N-j+1)!\).

For small \(h>0\), choose
\[
N(h)=\left\lfloor\frac{1}{4Bh[\log(e+1/h)]^q}\right\rfloor,
\qquad f_h=f_{h,N(h)}.
\tag{16}
\]
Then \(N\to\infty\), \(N\le1/h\), and, for \(1\le j\le N\),
\[
(Bh)^jM_j\le [Bh\,j L_j^q]^j\le4^{-j}.
\tag{17}
\]
Consequently \(\|f_h\|_\infty\) and \(\|f_h\|_2\) are bounded
independently of \(h\). Every test has support in the same compact
subset of \((1,2)\) and integral zero. Equations (15)--(17) imply
\[
\boxed{\|A_hf_h-\varphi\|_\infty
\le C\exp\left[-\frac{c}{h[\log(e+1/h)]^q}\right].}
\tag{18}
\]
This is a finite inverse at each width, not inversion through the
box's Fourier zeros.

If \(h=H/X\le[\log X(\log\log X)^r]^{-1}\), the exponent in
(18) is at least
\[
c'\log X(\log\log X)^{r-q}.
\tag{19}
\]
Indeed \(t/[\log(e+t)]^q\) is increasing for sufficiently large
\(t\); evaluate it at \(t=\log X(\log\log X)^r\).
Since \(r-q>0\), (18) is smaller than every fixed negative power
of \(X\), uniformly throughout the claimed range of \(H\).

## 4. Arithmetic transfer and the exact boundary

Compact support and mean zero give the exact identity
\[
H^{-1}\int_X^{2X}(S_{X,H}(y)-m_{X,H})f_h(y/X)\,dy
=\sum_n a_n(A_hf_h)(n/X).
\tag{20}
\]
The coefficient-side replacement error is at most
\(O(X\log(3X)\|A_hf_h-\varphi\|_\infty)\), since the supports
lie in a fixed dilate of \([X,2X]\) and \(|a_n|\le\log n\).
By (18)--(19) it is negligible compared with \(X^{\sigma_0}\).
Thus (14) gives a lower bound \(w_{\rho_0}X^\beta/2\) for the
modulus of (20) at all sufficiently large \(X\). Its squared modulus
is at most \((X/H^2)V_1(X,H)\|f_h\|_2^2\) by Cauchy--Schwarz.
The uniform \(L^2\) bound proves (2).

At \(H=H_r(X)\), the floor in (2), divided by the ceiling in (3),
is a positive constant times
\[
\frac{X^{2\beta-1}}{(\log X)^{A+1}(\log\log X)^r}
\longrightarrow\infty.
\tag{21}
\]
Hence any unbounded scale set satisfying (3) excludes each
\(\beta>1/2\); functional-equation symmetry for the full family
then gives the stated joint-GRH implication.

For the other side of the method boundary, PL-473 evaluates the
exact box multiplier at \(\xi=\pm2\pi/h\). A power-saving
approximation for a fixed nonzero target on every large scale with
\(0\le r\le1\) would force the forbidden Fourier envelope
\(\exp[-c|\xi|/(\log|\xi|)^r]\). The logarithmic integral
\(\int^\infty dt/[t(\log t)^r]\) diverges precisely in that range.
Integer rounding is already covered by its Lipschitz Fourier estimate.
For \(r>1\), (18)--(19) give the constructive counterpart, including
the exact zero interpolation and bounded test norms needed here.

## Prior art, controls and remaining limits

The cutoff construction is classical Denjoy--Carleman theory:
[Rainer, Lemma 3.3 and Theorem 3.6](https://www.mat.univie.ac.at/~armin/publ/survey-UET.pdf),
source 141. Source 139 gives the corresponding [[research/prior_art/incremental/PA-paley-wiener-ingham-logarithmic-integral|Paley--Wiener/Ingham]]
Fourier boundary. Sources 138, 128 and 127 supply, respectively,
the classical Bernoulli coefficients, arithmetic zero-density input,
and explicit-formula background. Zaccagnini, source 123, §3.3,
records the classical reverse implication from sufficiently strong
Selberg-integral bounds to zero-free regions; it is not the empirical
additive-window statement on arbitrary sparse scales used here.

The local delta is preservation of the finer derivative class through
the full sparse-zero annihilator, followed by the uniform truncation
estimate (18). It closes the stated one-parameter method boundary
and enlarges the admissible prime-window range. No new uncertainty
principle or claim of external priority is made.

The bounds (7), (11), (13), (15) and (17) check the two potentially
destructive operations: infinitely many derivatives for zero isolation
and a growing finite derivative sum for inversion. Support, empirical
centering, both complex phases, rounding and the \(H^2/X\)
normalization are retained. The argument is analytic, not a numerical
extrapolation. No Lean verification or independent adversarial approval
is claimed.

- The analytic inverse works for any coefficient source with a
  comparable absolute envelope. The noncancelling zero residue and
  the controlled explicit formula (14) distinguish this arithmetic
  application; generic positive or phase-twisted sources do not
  acquire them from the cutoff construction.
- The target and constants encode the full hypothetical sparse zero
  set. No effective finite-zero certificate, uniform onset as
  \(\beta\downarrow1/2\) or \(r\downarrow1\), or new acquired
  prime cancellation estimate is supplied.
- The obstruction for \(r\le1\) concerns all large scales and a
  fixed target in a global error norm. Moving targets, several kernels,
  source-specific signed error estimates, or specially selected widths
  remain outside it. No prime-variance counterexample follows.
- This resolves the displayed iterated-log family, not every possible
  slowly varying window law. Further nested logarithms would remain
  classical regularity refinements unless they change an arithmetic
  question. The outstanding input here is still the absolute variance
  ceiling, not another reformulation of the zero-isolating test.
