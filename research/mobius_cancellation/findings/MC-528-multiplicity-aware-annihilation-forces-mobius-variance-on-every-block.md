# MC-528 — Multiplicity-aware annihilation forces Möbius variance on every block

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `CONDITIONAL-TRANSFER`,
`NO-NOVELTY-CLAIM`. Constants depend on the full hypothetical zero set.

## Claim and arithmetic boundary

Put
\[
S_{X,H}(y)=M(y+H)-M(y),\quad
m_{X,H}=X^{-1}\int_X^{2X}S_{X,H}(y)\,dy,\quad
V_\mu(X,H)=\int_X^{2X}|S_{X,H}(y)-m_{X,H}|^2dy.
\]
If \(\rho_0=\beta+i\gamma\) is any zeta zero with \(\beta>1/2\)
and multiplicity \(m\), then for every fixed \(0<\theta<1\) there
are \(c>0,X_0\) such that, for every real \(X\ge X_0\),
\[
\boxed{V_\mu(X,\lfloor X^\theta\rfloor)
 \ge c\lfloor X^\theta\rfloor^2X^{2\beta-1}
                    (\log X)^{2m-2}.}                    \tag{1}
\]
There is no rightmost-zero, simplicity, finite-exception, zero-spacing,
or inverse-derivative bound hypothesis.

Consequently, on **any unbounded set** \(E\) of real scales, the premise
\[
V_\mu(X,\lfloor X^\theta\rfloor)
 \ll_\varepsilon X^{1+\varepsilon}\lfloor X^\theta\rfloor
\quad(X\in E),\qquad\text{for every }\varepsilon>0,       \tag{2}
\]
with constants uniform on \(E\), excludes every zero with
\(\Re\rho>1-\theta/2\). The selected scales need no density or
spacing assumption. Neither (2) nor any improved unconditional bound
for \(M\) is proved here.

The new local step is quantitative division after annihilating all
unwanted off-critical zeros **with their multiplicities**. It extends
[MC-526](MC-526-selected-mobius-variance-excludes-finite-exceptional-zero-clusters.md)
beyond finite exceptional clusters and resolves the infinite-family
transfer left by
[MC-527](MC-527-good-height-truncation-isolates-selected-scale-pole-cancellation.md).
The test depends on infinitely many hypothetical zeros; it is a necessity
certificate, not independently obtained arithmetic cancellation data.

## 1. A compact test that cancels all unwanted principal parts

Fix \(1/2<\sigma_0<\sigma_1<\beta\). Montgomery's classical
zero-density bound gives, for some fixed \(0<a<1\),
\[
\sum_{\substack{\zeta(\rho)=0,\ \Re\rho>\sigma_0\\|\rho|\le R}}
 m_\rho\ll(1+R)^a.                                    \tag{3}
\]
The sum is over distinct nontrivial zeros with their multiplicities.
Indeed the exponent \(3(1-\sigma)/(2-\sigma)\) is less than one
for \(\sigma>1/2\); take \(\sigma=\min(\sigma_0,4/5)\),
enlarge the exponent slightly to absorb \(\log^9 R\), and use
conjugation. Source MC-S73 states the applicable \(q=1\) theorem.

Exclude all copies of the selected point and form
\[
P(s)=(s-1)\prod_{\substack{\Re\rho>\sigma_0\\\rho\ne\rho_0}}
                         (1-s/\rho)^{m_\rho}.          \tag{4}
\]
The product converges absolutely on compact sets since
\(\sum m_\rho/|\rho|<\infty\). Its zeros are precisely the
prescribed points, so \(P(\rho_0)\ne0\). In particular the
conjugate of \(\rho_0\) is included: zeta has no real zero in
\((0,1)\), as its paired alternating eta series shows.

If \(n(r)\) counts the unwanted zeta zeros in (4) with multiplicity, then
\[
\sum m_\rho\log(1+R/|\rho|)
 =R\int_0^\infty\frac{n(r)}{r(r+R)}dr\ll1+R^a.
\]
There are no zeros near zero. Including the extra linear factor gives
\[
|P(s)|\le C e^{C|s|^a},\qquad
P(s)=\sum_{j\ge0}p_js^j,\qquad
|p_j|\le C B^j/(j!)^{1/a}.                             \tag{5}
\]
The coefficient estimate follows from Cauchy's inequality with radius
proportional to \(j^{1/a}\); exponential-in-\(j\) constants absorb
the Stirling factors.

Choose \(1<q<1/a\), and a nonzero nonnegative Gevrey bump \(\eta\)
supported in a compact subinterval of \((0,\log2)\), with
\(\|\eta^{(j)}\|_\infty\le C A^j(j!)^q\). Such bumps exist
for every \(q>1\) (MC-S79). Set \(g(t)=e^{-\rho_0t}\eta(t)\)
and
\[
k(t)=\sum_{j\ge0}p_j(-1)^jg^{(j)}(t),\qquad
D=P(\rho_0)\int\eta\ne0,\qquad
\phi(u)=k(\log u)/D.                                  \tag{6}
\]
For each fixed derivative order \(\ell\), the terms in the first
series are bounded by
\(C_\ell B_1^j((j+\ell)!)^q/(j!)^{1/a}\), a summable sequence.
Thus the series converges in every \(C^\ell\) norm, retains compact
support, and defines an actual \(\phi\in C_c^\infty((1,2);\mathbb C)\).
No formal infinite-order operator is substituted for a test function.

Integration by parts and \(u=e^t\) give
\[
\Phi(s):=\int_0^\infty\phi(u)u^{s-1}du
       =D^{-1}P(s)G(s),\qquad G(s)=\int g(t)e^{st}dt.   \tag{7}
\]
Here \(u^{s-1}du=e^{st}dt\); there is no additional Jacobian in
(6). Consequently
\[
\Phi(1)=0,\quad\Phi(\rho_0)=1,\quad
\Phi^{(j)}(\rho)=0\quad
(\rho\ne\rho_0,\ \Re\rho>\sigma_0,\ 0\le j<m_\rho).
                                                               \tag{8}
\]
Moreover, uniformly for \(\sigma_1\le\sigma\le2\),
\[
|G(\sigma+it)|\le C\exp(-c|t|^b),\qquad b=1/q>a.      \tag{9}
\]
To see this directly, the derivatives of \(e^{\sigma t}g(t)\)
obey \(CA_1^j(j!)^q\), uniformly on this fixed strip. Integrate
by parts \(j\) times and optimize \(j\) proportional to
\(|t|^{1/q}\). Compact support removes all boundary terms.

This reconstructs the sparse-product method in the explicitly granted
source
[[research/prime_lattice/findings/PL-471-sparse-zero-annihilators-force-prime-variance-on-every-large-block|PL-471]],
with repeated product factors rather than one per zero. Its
logarithmic-derivative residue sum is not used for reciprocal zeta.

## 2. Quantitative division, including arbitrarily close zeros

For large \(T=|t|\), write \(\mathcal N_t\) for the multiset of
nontrivial zeros with \(|\Im\rho-t|\le1\). Titchmarsh's
Theorem 9.6(B), or integration of 9.6(A) from \(2+it\), gives
\[
\log|\zeta(\sigma+it)|
 =\sum_{\rho\in\mathcal N_t}\log|\sigma+it-\rho|
                  +O(\log T),\qquad \sigma_1\le\sigma\le2.
                                                               \tag{10}
\]
This holds away from zeros, uniformly in the strip; the zero count
\(|\mathcal N_t|=O(\log T)\) includes multiplicities. Reference
factors \(|2+it-\rho|\) are bounded above and below and are absorbed
in the error. The statement for negative heights follows by conjugation.

Separate \(\mathcal N_t=\mathcal N_t^+\cup\mathcal N_t^-\)
by \(\Re\rho>\sigma_0\) and \(\Re\rho\le\sigma_0\).
Every member of \(\mathcal N_t^-\) is at distance at least
\(d=\sigma_1-\sigma_0>0\) from the strip. Choose
\(T>|\gamma|+2\), so the selected zero is not in \(\mathcal N_t\).
All factors for \(\mathcal N_t^+\) occur in (4), and **cancel
algebraically before taking bounds**. Off the zeros, (10) implies
\[
\left|\frac{P(s)}{\zeta(s)}\right|
 \le T^C\left|\frac{P(s)}{
              \prod_{\rho\in\mathcal N_t^+}(s-\rho)}\right|
       \prod_{\rho\in\mathcal N_t^-}|s-\rho|^{-1}.
                                                               \tag{11}
\]
The last product is at most \(\max(1,d^{-1})^{O(\log T)}\),
which is a fixed power of \(T\). In the middle quotient, each
removed factor \(1-s/\rho\) contributes only \(-1/\rho\).
At large height \(|\rho|>1\), and the remaining product obeys
the same majorant used in (5):
\[
\left|\frac{P(s)}{\prod_{\rho\in\mathcal N_t^+}(s-\rho)}\right|
 \le |s-1|\prod_{\rho\notin\mathcal N_t^+}
                 (1+|s|/|\rho|)^{m_\rho}
 \le C\exp(C T^a).                                   \tag{12}
\]
The product in (12) runs only over the unwanted zeros of (4).
Repetitions in the denominator of (12) match exactly their exponents.
The estimates extend across cancelled zeros by removability and continuity.
No minimum separation, bound on \(1/\zeta'(\rho)\), or absolute
sum of Laurent coefficients is required. We obtain
\[
\left|\frac{P(\sigma+it)}{\zeta(\sigma+it)}\right|
 \le C T^{C_d}e^{CT^a}\qquad(T\text{ sufficiently large}). \tag{13}
\]
Combining (7), (9), and (13), and using \(b>a\), yields
\[
\left|\frac{\Phi(\sigma+it)}{\zeta(\sigma+it)}\right|
 \le C\exp(-c'|t|^b),\qquad \sigma_1\le\sigma\le2,
 \quad |t|\text{ sufficiently large}.                  \tag{14}
\]
Thus removability is accompanied by a proved vertical growth bound.
This is the missing reciprocal estimate in the clue. On bounded
portions of the strip the quotient is meromorphic with only the
selected pole; on the line \(\Re s=\sigma_1\) it is regular and
bounded on compact sets. Zeta's pole at 1 causes no obstruction.

## 3. One retained pole, with its entire Laurent contribution

Mellin inversion on \(\Re s=2\) is justified by absolute convergence
of \(\sum\mu(n)n^{-s}\). Shift to \(\Re s=\sigma_1\).
After (8), the integrand has only one pole in this strip. Equation
(14) makes the left vertical integral absolutely convergent and the
horizontal edges tend to zero. There is no infinite residue interchange.
Therefore, for every real \(X\ge2\),
\[
T_\phi(X):=\sum_n\mu(n)\phi(n/X)
 =X^{\rho_0}Q_{m-1}(\log X)+O_\phi(X^{\sigma_1}),       \tag{15}
\]
where, if \(1/\zeta(s)=\sum_{r=1}^m c_r(s-\rho_0)^{-r}
+\text{holomorphic}\),
\[
Q_{m-1}(v)=\sum_{r=1}^m c_r
 \sum_{j=0}^{r-1}\frac{v^{r-1-j}\Phi^{(j)}(\rho_0)}
                          {(r-1-j)!j!},\qquad
[v^{m-1}]Q_{m-1}=c_m/(m-1)!\ne0.                     \tag{16}
\]
It follows that
\[
|T_\phi(X)|\gg_\phi X^\beta(\log X)^{m-1}
\quad\text{for every sufficiently large }X.            \tag{17}
\]
The conjugate pole was cancelled, so no cosine phase can make this
complex measurement vanish along a selected scale sequence. Its real
and imaginary parts are admissible real measurements.

For the explicit multiple-pole control \(c_m\ne0\) and
\(c_1=\cdots=c_{m-1}=0\), (16) still has its nonzero leading
term. In particular a double pole with zero ordinary residue gives
\(c_2X^{\rho_0}(\log X+\Phi'(\rho_0))\). Conversely, one
simple test zero at an unwanted pole of order \(m>1\) leaves a
pole of order \(m-1\); full multiplicity in (4) is essential.

## 4. Return to the original block and remove its empirical mean

Let \(H=\lfloor X^\theta\rfloor\), \(h=H/X\), and choose one
fixed integer \(K\) with \(K(1-\theta)>1-\sigma_1\). Define
\[
c_0^*=1,\qquad
c_j^*=-\sum_{r=1}^j\frac{(-1)^r}{(r+1)!}c_{j-r}^*,\qquad
f_h=\sum_{j=0}^{K-1}c_j^*h^j\phi^{(j)},
\]
\[
A_h f(u)=h^{-1}\int_0^h f(u-v)\,dv.
\]
Taylor expansion with remainder, using the recurrence, proves
\[
A_hf_h=\phi+O_{\phi,K}(h^K)\quad\text{uniformly in }u. \tag{18}
\]
All functions are extended by zero. The error has support in a common
compact set; every \(f_h\) is supported inside \((1,2)\), has
zero integral by (8) and integration of derivatives, and has uniformly
bounded \(L^2\) norm for \(0<h\le1\). This is a finite inverse
polynomial, not inversion across the box multiplier's zeros.

Using \(|\mu(n)|\le1\), (18) costs at most
\(O(Xh^K)=o(X^{\sigma_1})\) in the coefficient sum. Finite
interchange gives the exact identity
\[
L_h:=\sum_n\mu(n)(A_hf_h)(n/X)
 =H^{-1}\int_X^{2X}(S_{X,H}(y)-m_{X,H})f_h(y/X)\,dy.    \tag{19}
\]
The coefficient of \(\mu(n)\) is
\(H^{-1}\int_{n-H}^n f_h(y/X)dy\), including endpoint-crossing
windows. Equations (15)–(18) apply to \(L_h\), while Cauchy–Schwarz
in (19) gives
\[
|L_h|^2\le XH^{-2}V_\mu(X,H)\|f_h\|_2^2.
\]
This proves (1) on the very same block \([X,2X]\).

If a fixed bank is desired, take the real and imaginary components of
\(\phi^{(j)}\), \(0\le j<K\). Their coefficients in \(f_h\)
are uniformly bounded. The bank is finite and fixed before \(X\)
varies, although it depends on the full zero set and on \(\theta\).

Finally, dividing (1) by (2) gives a factor comparable to
\(X^{2\beta+\theta-2-\varepsilon}(\log X)^{2m-2}\).
Choose \(0<\varepsilon<2\beta+\theta-2\) to contradict (2)
along any unbounded \(E\) when \(\beta>1-\theta/2\).

## Prior art, controls, and consequence

The construction uses classical canonical products and compact Gevrey
functions; Lissy's moment-method paper (MC-S79, §§2 and 3.2) explicitly
uses Gevrey Fourier multipliers to dominate canonical-product growth.
The local product estimate (10) is Titchmarsh, second edition, Theorem
9.6(B), pp. 217–218 (MC-S67). Montgomery's multiplicity-counted
power-saving density theorem is MC-S73. Their combination here proves
(13)–(14), rather than assuming a reciprocal growth bound.

The closest local source PL-471 supplies the sparse compact-test
construction and finite box inverse for a logarithmic derivative. The
present proof reconstructs these for higher-order reciprocal poles and
supplies the additional quantitative division argument. MC-527's
good-height grouped contour remains valid, but is not an absolute
residue-sum theorem and is not needed to exchange infinitely many
residues here. MC-526 remains a valid finite-cluster theorem with its
stronger window range \(1\le H\le h_0X\); (1) asserts fixed power
windows, not that full uniform range.

Classical zero/oscillation and variance converses remain the relevant
prior-art boundary. Pintz's *Oscillation of partial sums of the Möbius
function and zeros of Riemann's zeta function*, arXiv:2608.24878v2,
§2, Theorems 2.1–2.2 (MC-S19), concerns prefix mean-absolute size and
maxima over \([x^{1-\delta},x]\). Zaccagnini's Selberg-integral
discussion (MC-S72) concerns prime-counting variance. These are
comparisons, not substitutes for the centered same-block calculation
(18)–(19). No external priority or new general oscillation theorem is
claimed. The durable local delta is closure of the reciprocal
infinite-family gate with every principal part retained.

- Sparsity with a fixed exponent \(a<1\), the strict gap
  \(\sigma_1-\sigma_0>0\), and zeta's local factorization are
  separate load-bearing inputs. A bare \(o(T)\) count or generic
  meromorphic continuation does not supply this argument. Thus the
  arbitrary-coefficient control MC-524 is not contradicted.
- There is no uniform bound on the test norm, the normalization
  \(P(\rho_0)\), the onset scale, or the derivative order as the
  zero set changes, \(\sigma_0\downarrow1/2\), or
  \(\theta\uparrow1\). A finite numerical zero list does not
  construct this certificate.
- At \(\beta=1/2\), the sparse half-plane cannot be chosen below
  the selected zero. At \(\beta=1-\theta/2\), an epsilon-loss
  ceiling is not contradicted, even at a multiple zero. No simplicity
  statement follows.
- Centering kills the constant profile: the all-plus sequence with
  its pole at 1 would have zero centered integer-window variance.
  It is not a control satisfying the retained-pole hypotheses here.
- An unbounded selected-scale diagonal ceiling for each of a sequence
  of fixed \(\theta\) approaching 1 therefore implies RH; the
  converse is supplied by MC-520's all-scale RH bound. This is a
  conditional criterion, not an independently verified ceiling.

Auxiliary exact rational arithmetic checked full and pure principal-part
coefficient extraction in 16 cases of orders 1 through 8, and the finite
box inverse through order 12, including its Bernoulli coefficients
through degree 6. These are algebra checks, not checks of analytic limits
or evidence about the actual zero set.

The evidence is an analytic derivation from the stated classical inputs.
No numerical evidence about off-critical zeros, independent adversarial
approval, or Lean verification is asserted. The arithmetic task remaining
is a source-derived variance upper bound strong enough for its intended
application, not acquisition of the hypothetical all-zero-dependent test.
