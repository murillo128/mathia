# PL-472 — Gevrey box inversion reaches near-linear prime windows

**Evidence/status:** LITERATURE+DERIVED / EXACT CONDITIONAL VARIANCE FLOOR;
NON-EFFECTIVE CONSTANTS; NO EXTERNAL NOVELTY CLAIM.

## Claim and mathematical delta

Use the actual identity-residue source and empirical variance
\[
a_n=\Lambda(n)\mathbf1_{n\equiv1\ (5)},\qquad
S_{X,H}(y)=\sum_{y<n\le y+H}a_n,\qquad
m_{X,H}=X^{-1}\int_X^{2X}S_{X,H}(y)\,dy,
\]
\[
V_1(X,H)=\int_X^{2X}|S_{X,H}(y)-m_{X,H}|^2\,dy.
\tag{1}
\]
Suppose a mod-5 Dirichlet factor has a nontrivial zero
\(\rho_0=\beta+i\gamma\), \(\beta>1/2\). For every fixed \(B>1\),
there are \(c>0,X_0\) such that, for every real \(X\ge X_0\) and
every integer \(H\) in the displayed range,
\[
\boxed{1\le H\le \frac{X}{(\log X)^B}
\quad\Longrightarrow\quad
V_1(X,H)\ge c H^2X^{2\beta-1}.}
\tag{2}
\]
Constants may depend on the full zero set, \(\rho_0\), and \(B\);
they are uniform in \(X,H\) in this range.

In particular, fix just one \(B>1\) and set
\(H_B(X)=\lfloor X/(\log X)^B\rfloor\). The unproved hypothesis
\[
V_1(X,H_B(X))\le C XH_B(X)(\log X)^A
\tag{3}
\]
on any unbounded set of sufficiently large real \(X\), with fixed
\(C>0\) and finite \(A\ge0\), forces joint GRH for \(\zeta\) and the
three primitive nonprincipal Dirichlet functions modulo 5. No density,
coverage, or gap bound is imposed on the scale set.

[[research/prime_lattice/findings/PL-471-sparse-zero-annihilators-force-prime-variance-on-every-large-block|PL-471]]
proves the floor for each fixed polynomial window \(H=\lfloor
X^\theta\rfloor\), \(0<\theta<1\). It does not provide uniform constants
as \(\theta\uparrow1\), so substituting a moving \(\theta\) is invalid.
The additional result here is a uniformly bounded, increasingly high
order inverse of the box average, with error
\(\exp(-c h^{-1/q})\), \(h=H/X\), for a Gevrey test of order \(q>1\).
This admits the near-linear range (2). It replaces a family of fixed
polynomial-window ceilings approaching exponent 1 by the single
window law (3). It does not establish that ceiling.

## 1. The zero-isolating test retains its Gevrey order

Fix \(1/2<\sigma_0<\beta\). PL-471 uses the classical off-critical
zero-density bound to obtain an exponent \(0<a<1\) for the distinct
zeros with real part exceeding \(\sigma_0\). Its genus-zero product
\[
P(s)=(s-1)\prod_{\substack{\Re\lambda>\sigma_0\\\lambda\ne\rho_0}}
 (1-s/\lambda)=\sum_{j\ge0}p_js^j
\]
satisfies
\[
|p_j|\le C K^j/(j!)^{1/a}.
\tag{4}
\]
Choose
\[
1<q<\min\{B,1/a\}.
\tag{5}
\]
This is possible for every fixed \(B>1\), even when \(\beta\) is
arbitrarily close to \(1/2\); no uniformity in \(\beta\) is needed.

Take the compactly supported Gevrey function \(g\) from PL-471, with
\(\|g^{(r)}\|_\infty\le C R^r(r!)^q\), and its convergent series
\[
k(t)=\sum_{j\ge0}p_j(-1)^jg^{(j)}(t).
\]
Besides convergence in each smooth norm, this series preserves the
same Gevrey order. Indeed,
\[
\begin{aligned}
\|k^{(\ell)}\|_\infty
&\le C\sum_{j\ge0}K^jR^{j+\ell}
                 \frac{((j+\ell)!)^q}{(j!)^{1/a}}\\
&\le C(2^qR)^\ell(\ell!)^q
       \sum_{j\ge0}(2^qKR)^j(j!)^{q-1/a}
 \le C'R'^\ell(\ell!)^q.
\end{aligned}
\tag{6}
\]
The last sum converges because \(q<1/a\).

Normalization and the analytic change \(t=\log u\) therefore give
the PL-471 test \(\varphi\in C_c^\infty((1,2))\) with
\[
\|\varphi^{(r)}\|_\infty\le C_\varphi L^r(r!)^q,\qquad L\ge1.
\tag{7}
\]
For an explicit check on composition, the coefficient of
\(k^{(\ell)}(\log u)\) in \(d^rk(\log u)/du^r\) is
\(u^{-r}s(r,\ell)\), where \(s\) is a signed Stirling number of the
first kind. The elementary bound
\[
|s(r,\ell)|\le \frac{r!}{\ell!}\binom{r-1}{\ell-1}
\]
counts permutations by unordered cycles and dominates them by
partitions into linearly ordered lists. Together with (6) it bounds
the derivative by a constant times
\((1+R')^r(r!)^q\), since \(\ell!^{q-1}\le r!^{q-1}\).
The support stays strictly inside \((1,2)\); zero extension preserves
(7).

Writing \(\Phi(s)=\int\varphi(u)u^{s-1}du\), the unchanged exact
interpolation identities and arithmetic explicit formula are
\[
\Phi(1)=0,\quad \Phi(\rho_0)=1,\quad
\Phi(\lambda)=0\quad(\Re\lambda>\sigma_0,\ \lambda\ne\rho_0),
\]
\[
T_\varphi(X):=\sum_n a_n\varphi(n/X)
=-w_{\rho_0}X^{\rho_0}+O_\varphi(X^{\sigma_0}),\qquad
w_{\rho_0}=\tfrac14\sum_\chi m_\chi(\rho_0)>0.
\tag{8}
\]
PL-471 proves (8) with the full zero family, trivial-zero term,
missing factor at 5, and left-contour remainder retained. The test
\(\varphi\) is fixed once the zero set and parameters are fixed.
We will apply that formula only to this fixed test, not to a family
with uncontrolled growing derivatives.

## 2. Uniform box inversion by growing finite truncation

For a zero-extended test put
\[
A_h f(u)=h^{-1}\int_0^h f(u-v)\,dv.
\]
Define the classical Bernoulli coefficients by
\[
C(z)=\frac{z}{1-e^{-z}}=\sum_{j\ge0}c_jz^j,\qquad |z|<2\pi.
\tag{9}
\]
Thus \(c_0=1,c_1=1/2,c_2=1/12,c_3=0,c_4=-1/720\).
Cauchy's estimate on \(|z|=1\) supplies an absolute constant \(C_0\)
with \(|c_j|\le C_0\) for all \(j\).

For every integer \(M\ge1\), set
\[
f_{h,M}=\sum_{j=0}^{M-1}c_jh^j\varphi^{(j)}.
\]
The generating-function identity
\[
C(z)\sum_{r\ge0}\frac{(-1)^rz^r}{(r+1)!}=1
\tag{10}
\]
cancels all powers of \(h\) below \(M\) except the constant.
More precisely, Taylor expansion of \(\varphi^{(j)}(u-v)\)
through degree \(M-1-j\), with its integral-average remainder, gives
\[
\begin{aligned}
\|A_h f_{h,M}-\varphi\|_\infty
&\le h^M\|\varphi^{(M)}\|_\infty
       \sum_{j=0}^{M-1}\frac{|c_j|}{(M-j+1)!}\\
&\le C_1 C_\varphi(Lh)^M(M!)^q.
\end{aligned}
\tag{11}
\]
The constant \(C_1\) is independent of \(h,M\). This explicit
uniform remainder is essential; a fixed-order \(O_{\varphi,M}(h^M)\)
cannot be used when \(M\) grows.

For sufficiently small \(h>0\), choose
\[
M(h)=\left\lfloor(4Lh)^{-1/q}\right\rfloor,\qquad
f_h=f_{h,M(h)}.
\tag{12}
\]
For \(j<M(h)\), the successive terms
\((Lh)^j(j!)^q\) have ratio at most \(1/4\). Hence
\[
\|f_h\|_\infty
 \le C_0C_\varphi\sum_{j=0}^{M(h)-1}(Lh)^j(j!)^q
 \le \tfrac43C_0C_\varphi.
\]
All \(f_h\) have the same support as \(\varphi\), and
\(\int f_h=\int\varphi=0\). In particular their \(L^2\) norms are
uniformly bounded. Since \(M!\le M^M\), (11) yields
\[
\boxed{\|A_h f_h-\varphi\|_\infty
 \le C_2\,4^{-M(h)}
 \le C_3\exp(-c_3 h^{-1/q}).}
\tag{13}
\]
Every inverse is finite. No convergent infinite inverse series or
inverse across the Fourier zeros of the box is claimed.

## 3. Transfer to near-linear windows and the single-law consequence

The exact centered pairing, using the support inside \((1,2)\), is
\[
\begin{aligned}
L_{X,H}
&=H^{-1}\int_X^{2X}(S_{X,H}(y)-m_{X,H})f_h(y/X)\,dy\\
&=\sum_n a_n(A_h f_h)(n/X),\qquad h=H/X.
\end{aligned}
\tag{14}
\]
The empirical constant disappears because \(\int f_h=0\).
Zero extension handles the window endpoints without a neighboring
block estimate.

For \(h\le(\log X)^{-B}\), the supports in (14) lie in a fixed
dilate of \([X,2X]\), and \(|a_n|\le\log n\). Equations (8) and
(13) therefore imply, uniformly in this range,
\[
L_{X,H}
=-w_{\rho_0}X^{\rho_0}+O(X^{\sigma_0})
 +O\left(X\log(3X)e^{-c_3(\log X)^{B/q}}\right)
=-w_{\rho_0}X^{\rho_0}+O(X^{\sigma_0}).
\tag{15}
\]
Here \(B/q>1\), so the last error is smaller than every fixed
negative power of \(X\). The arithmetic explicit formula has not
been applied to \(f_h\); only the uniform coefficient-side error
has been estimated.

For all sufficiently large \(X\), (15) has modulus at least
\(w_{\rho_0}X^\beta/2\). By Cauchy--Schwarz and the bounded test norm,
\[
|L_{X,H}|^2\le \frac{X}{H^2}V_1(X,H)\|f_h\|_2^2
 \le C_4\frac{X}{H^2}V_1(X,H).
\]
This proves (2). A complex test is legitimate for the real source:
its real and imaginary parts are two real tests, and the complex
modulus avoids a phase-dependent zero at selected scales.

At \(H=H_B(X)\), comparison of (2) with (3) gives
\[
\frac{c H_B(X)^2X^{2\beta-1}}
     {C XH_B(X)(\log X)^A}
\asymp \frac{X^{2\beta-1}}{(\log X)^{A+B}}\longrightarrow\infty
\quad(\beta>1/2).
\tag{16}
\]
Every such zero is excluded by (3), even on an arbitrarily sparse
unbounded scale set. Functional-equation symmetry for the full
mod-5 family excludes zeros left of \(1/2\) as well. This is the
claimed conditional joint-GRH consequence, not a proof of (3).

## Prior art, stress tests and remaining boundary

Bernoulli inversion and truncating a factorially growing expansion
at a scale depending on the small parameter are classical.
[NIST DLMF §24.2](https://dlmf.nist.gov/24.2) gives (9), and
[§2.11](https://dlmf.nist.gov/2.11) gives the classical optimal-truncation
context (source 138). The uniform estimate (11)--(13) is derived here.
Gevrey bump existence and analytic-composition closure are classical;
source 136 supplies that background, and (6)--(7) verify preservation
for this particular sparse-zero construction. The zero-density and
explicit-formula inputs remain sources 128 and 127.

The converse from strong prime-window second moments to zero-free
regions is also classical: Zaccagnini, source 123, §3.3, discusses
a deterministically centered multiplicative-window version. That
result is not quoted as the present empirical additive-window
statement on an arbitrary unbounded set. PL-471 already provides
sparse-scale recovery for fixed polynomial windows. The local delta
is the growing-order, bounded-norm transfer and its new admissible
window range; no external priority claim is made.

The following limits prevent stronger interpretations.

- For a fixed Gevrey order \(q>1\), the proof requires
  \(h^{-1/q}/\log X\to\infty\) to make this error superpolynomially
  small. Choosing \(q<B\) supplies it in (2). At \(B=1\), or at
  macroscopic \(H\asymp X\), this estimate does not suffice.
  This is a limitation of the present proof, not a counterexample
  or a sharp impossibility theorem for those regimes.
- The degree \(M(h)\) grows. There is no fixed finite derivative bank
  as in the fixed-\(\theta\) version of PL-471. Boundedness of the
  combined test, not bounded complexity of acquiring it, is proved.
- The test and constants still depend on the full hypothetical zero
  set. No effective test from a finite zero list, quantitative onset,
  or uniform limit as \(\beta\downarrow1/2\) is supplied.
- The actual Dirichlet explicit formula and noncancelling identity
  residues remain indispensable. Generic positive meromorphic
  sources do not acquire the required growth merely from positivity
  or a sparse pole count; the PL-469/PL-470 controls are unaffected.
- A varying center depending on \(y\), or a relative covariance lower
  frame without an absolute ceiling, is not hypothesis (3).
  No prime-covariance estimate, dephasing-cone proof, or zero-simplicity
  conclusion is obtained.

Exact rational diagnostics checked (10) through truncation orders
1--80 and the Stirling/Lah majorant through derivative order 80.
These are sign/index controls only; the uniform analytic inequalities
above prove the unbounded-order statement. No Lean verification or
independent adversarial approval is claimed.
