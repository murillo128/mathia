# PL-471 — Sparse-zero annihilators force prime variance on every large block

**Evidence/status:** LITERATURE+DERIVED / EXACT CONDITIONAL VARIANCE FLOOR;
NON-EFFECTIVE CONSTANTS; NO EXTERNAL NOVELTY CLAIM.

## Claim and mathematical delta

Let
\[
a_n=\Lambda(n)\mathbf1_{n\equiv1\ (5)},\quad
S_{X,H}(y)=\sum_{y<n\le y+H}a_n,\quad
m_{X,H}=X^{-1}\int_X^{2X}S_{X,H}(y)\,dy,
\]
\[
V_1(X,H)=\int_X^{2X}|S_{X,H}(y)-m_{X,H}|^2dy.
\tag{1}
\]
Suppose any of the four Dirichlet factors modulo 5 has a nontrivial
zero \(\rho_0=\beta+i\gamma\) with \(\beta>1/2\). For each fixed
\(0<\theta<1\), there are constants \(c>0,X_0\), allowed to depend
on the full zero set, \(\rho_0\), and \(\theta\), such that
\[
\boxed{V_1(X,\lfloor X^\theta\rfloor)
       \ge c\lfloor X^\theta\rfloor^2X^{2\beta-1}
       \qquad(X\ge X_0).}
\tag{2}
\]
The scale \(X\) is real. No rightmost zero, isolated finite pole cluster,
gap below the zero supremum, zero simplicity, or estimate of the removed
mean is assumed. A real nontrivial zero is also covered.

Consequently, for any unbounded set \(\mathcal X\subset[2,\infty)\),
the unproved ceiling
\[
V_1(X,\lfloor X^\theta\rfloor)
 \le C X\lfloor X^\theta\rfloor(\log X)^A
 \quad(X\in\mathcal X,\ X\ge X_1),\qquad C,A<\infty,
\tag{3}
\]
excludes every mod-5 nontrivial zero in \(\Re s>1-\theta/2\).
Here \(A\ge0\), \(C\), and \(\theta\) are fixed on that set.
In particular this implication applies to the retained dyadic mesh in
the density-one clue, and to any unbounded subset of that mesh.
It does not supply (3) on even one such set.

The new local input relative to
[[research/prime_lattice/findings/PL-470-positive-source-strip-growth-and-the-infinite-pole-tail-gate|PL-470]]
is a fixed smooth Mellin test that annihilates **all** unwanted zeros
to the right of a chosen \(\sigma_0\in(1/2,\beta)\). A power-saving
zero count, stronger than a bare \(o(T)\) statement, permits this
construction. The remaining zero sum is \(O(X^{\sigma_0})\).
There is no growing packet whose smallest singular value must be bounded.

## 1. Compact support and exact interpolation of a sparse zero set

We first give the analytic construction, including its convergence cost.
Let \(\mathcal Z\) be a discrete subset of \(\{s:1/2<\Re s<1\}\),
and assume
\[
\#\{\lambda\in\mathcal Z:|\lambda|\le R\}
 \le C(1+R)^a,\qquad 0<a<1.
\tag{4}
\]
Fix \(\rho_0\in\mathcal Z\). There is a complex
\(\varphi\in C_c^\infty((1,2))\) with Mellin transform
\(\Phi(s)=\int\varphi(u)u^{s-1}du\) such that
\[
\Phi(1)=0,\quad \Phi(\rho_0)=1,\quad
\Phi(\lambda)=0\quad(\lambda\in\mathcal Z\setminus\{\rho_0\}).
\tag{5}
\]

Indeed, the genus-zero product
\[
P(s)=(s-1)\prod_{\lambda\in\mathcal Z\setminus\{\rho_0\}}
                  (1-s/\lambda)
\tag{6}
\]
converges absolutely on compact subsets, since (4) gives
\(\sum |\lambda|^{-1}<\infty\). Its only zeros are the specified
ones; in particular \(P(\rho_0)\ne0\). If \(n(t)\) counts the
product zeros, partial integration gives
\[
\sum_\lambda\log(1+R/|\lambda|)
 =R\int_0^\infty\frac{n(t)}{t(t+R)}dt
 \ll 1+R^a.
\tag{7}
\]
There are no zeros near 0, and \(0<a<1\) makes the scaled integral
finite at both ends. Absorbing the factor \(s-1\),
\(|P(s)|\le C_1\exp(C_2|s|^a)\). Cauchy's coefficient bound,
optimized at a radius proportional to \(k^{1/a}\), therefore yields
\[
P(s)=\sum_{k\ge0}p_ks^k,\qquad
|p_k|\le C_3 B^k/(k!)^{1/a}.
\tag{8}
\]
Polynomial factors in the optimization are absorbed into \(B^k\).

Choose \(1<q<1/a\), and a nonzero nonnegative compactly supported
Gevrey function \(\eta\) inside \((0,\log2)\), satisfying
\(\|\eta^{(k)}\|_\infty\le C R^k(k!)^q\). Such bumps exist for
every \(q>1\); this is the classical non-quasianalytic Gevrey regime
(source 136). Put \(g(t)=e^{-\rho_0t}\eta(t)\), which has the same
kind of derivative bound, and define
\[
k(t)=\sum_{j\ge0}p_j(-1)^j g^{(j)}(t).
\tag{9}
\]
For each derivative order \(\ell\), its terms are bounded by
\[
C_\ell B_1^j\frac{((j+\ell)!)^q}{(j!)^{1/a}}.
\]
This is summable because \(q<1/a\). Thus (9) converges in every
\(C^\ell\) norm, has the same compact support, and is an actual
smooth function, not a formal infinite-order differential expression.
Termwise integration and integration by parts give, for every \(s\),
\[
\int k(t)e^{st}dt=P(s)\int g(t)e^{st}dt.
\tag{10}
\]
The value at \(\rho_0\) is \(P(\rho_0)\int\eta\ne0\).
Set \(\varphi(u)=k(\log u)/(P(\rho_0)\int\eta)\).
The substitution \(u=e^t\) gives
\(u^{s-1}du=e^{st}dt\), proving (5), with no missing Jacobian.
In particular \(\int\varphi=0\).

This proof requires a fixed exponent \(a<1\), not merely zero
asymptotic density. It asserts neither uniform test norms as
\(a\uparrow1\) nor an effective test obtainable from finitely many
known zeros. Complex tests are two real measurements; no modification
of the arithmetic source is involved.

## 2. Arithmetic sparsity supplies the interpolation hypothesis

Let \(Z\) be the distinct nontrivial zeros of \(\zeta\) and the three
primitive nonprincipal mod-5 functions. At a common zero define
\(w_\rho=\frac14\sum_\chi m_\chi(\rho)>0\).
Fix \(1/2<\sigma_0<\beta\) and let
\(\mathcal Z=\{\rho\in Z:\Re\rho>\sigma_0\}\).
Montgomery's classical bound, recorded in source 128 and explicitly
stated in [Dickinson's introduction](https://arxiv.org/pdf/2211.06264),
is
\[
\sum_{\chi\bmod5}N(\sigma,T,\chi)
 \ll (5T)^{3(1-\sigma)/(2-\sigma)}\log^9(5T)
 \quad(1/2\le\sigma\le4/5).
\tag{11}
\]
For larger \(\sigma\), monotonicity at \(4/5\) suffices. Choose
\(a\) strictly between the applicable power in (11) and 1, absorbing
the logarithm. Then (4) holds, even with multiplicities. Only one
product zero per distinct point is needed: logarithmic derivatives
have simple poles regardless of the original zero multiplicity.

Apply (5). If \(\rho_0\) is nonreal, its conjugate is among the
annihilated points. The complex output therefore retains one pure
mode rather than a real cosine that could vanish at particular scales.
This use of the full sparse zero set allows zeros arbitrarily far to
the right of \(\rho_0\); no maximal real part is selected.

## 3. The full explicit formula now has a smaller remainder

For this fixed test put \(T_\varphi(X)=\sum_n a_n\varphi(n/X)\).
The smoothed explicit formula from PL-470, applied directly to
\(\varphi\), reads
\[
T_\varphi(X)=-\sum_{\rho\in Z}w_\rho X^\rho\Phi(\rho)
                         +B_\varphi(X),
\tag{12}
\]
\[
B_\varphi(X)=-\frac14\Phi(0)
 -\frac{\log5}{4}\sum_{r\ge1}\varphi(5^r/X)
 +\frac1{2\pi i}\int_{(-1/2)}D_*(s)X^s\Phi(s)\,ds,
\]
\[
D_*(s)=\frac14\left(-\frac{\zeta'}\zeta(s)
                 +\sum_{\chi\ne\chi_0}-\frac{L'}L(s,\chi)\right).
\]
The pole at 1 contributes \(X\Phi(1)/4=0\) exactly. The displayed
\(-\Phi(0)/4\) is the even character's trivial zero contribution;
the powers of 5 subtract the principal character's missing Euler factor.
There are boundedly many of these powers in the test support, and the
left-line integral is \(O_\varphi(X^{-1/2})\). Hence \(B_\varphi=O_\varphi(1)\).

For completeness, compact smooth support makes \(\Phi(\sigma+it)\)
decay faster than every power, uniformly for \(-1/2\le\sigma\le2\).
The classical unit-height count with multiplicity is \(O(\log(2+|t|))\).
Separated horizontal contours and the logarithmic-derivative bounds
in source 127 justify (12) and its absolutely convergent zero sum.
These are actual Dirichlet-function growth inputs, not consequences
of a pole count for an arbitrary meromorphic source.

All terms with \(\Re\rho>\sigma_0\), other than \(\rho_0\), vanish
by (5). The complete remaining sum satisfies
\[
\left|\sum_{\Re\rho\le\sigma_0}
          w_\rho X^\rho\Phi(\rho)\right|
 \le X^{\sigma_0}\sum_{\rho\in Z}w_\rho|\Phi(\rho)|
 =O_\varphi(X^{\sigma_0}).
\]
Consequently
\[
\boxed{T_\varphi(X)=-w_{\rho_0}X^{\rho_0}
                         +O_\varphi(X^{\sigma_0}),}
\qquad |T_\varphi(X)|\ge\tfrac12w_{\rho_0}X^\beta
\tag{13}
\]
for all sufficiently large real \(X\). The residue is nonzero because
the identity-residue channel adds multiplicities with the same sign.
No absolute tail at a growing cutoff has been substituted for this
exact annihilation.

## 4. Recover the additive window without changing the scale set

Write \(h=H/X\), \(H=\lfloor X^\theta\rfloor\). Choose a fixed
integer \(M\) with
\[
M(1-\theta)>1-\sigma_0.
\tag{14}
\]
Use PL-463's finite inverse of the backward box average:
\[
c_0=1,\quad c_j=-\sum_{r=1}^j\frac{(-1)^r}{(r+1)!}c_{j-r},
\quad f_h=\sum_{j=0}^{M-1}c_jh^j\varphi^{(j)},
\]
\[
A_hf(u)=h^{-1}\int_0^h f(u-v)\,dv,
\qquad A_hf_h=\varphi+O_{\varphi,M}(h^M).
\tag{15}
\]
Taylor's theorem proves the last formula: all coefficients below
order \(M\) cancel except the constant. All \(f_h\) have the same
compact support in \((1,2)\), integral zero, and bounded \(L^2\) norm.
The inverse is finite; no inversion across the box multiplier's zeros
or convergence of its full derivative series is claimed.

Finite interchange gives exactly
\[
L_h:=H^{-1}\int_X^{2X}(S_{X,H}(y)-m_{X,H})f_h(y/X)\,dy
       =\sum_n a_n(A_hf_h)(n/X).
\tag{16}
\]
The zero-extended tests account for all windows crossing the block's
endpoints. Since \(|a_n|\le\log n\), (15) costs at most
\(O(Xh^M\log(3X))=o(X^{\sigma_0})\), by (14). Thus (13) also
holds with \(T_\varphi\) replaced by \(L_h\). Cauchy--Schwarz yields
\[
|L_h|^2\le\frac{X}{H^2}V_1(X,H)\|f_h\|_2^2,
\]
proving (2). This argument uses no neighboring scale and no estimates
of omitted block means or variances.

The measurement bank can be fixed in advance of \(X\), once the
hypothetical zero set and \(\theta\) are fixed: take the real and
imaginary parts of \(\varphi^{(j)}\), \(0\le j<M\), discarding zero
functions. Their coefficients \(c_jh^j\) have uniformly bounded
Euclidean norm, so (13)--(16) force the bank's squared response norm
divided by its fixed total squared test norm to be \(\gg X^{2\beta}\).
This is the finite-bank certificate asked for in the continuation clue,
although the bank is non-effective and encodes infinitely many zeros.

Finally, (2) divided by the right side of (3) is bounded below by a
positive constant times
\(X^{2\beta+\theta-2}/(\log X)^A\). It tends to infinity precisely
in the asserted strict region \(\beta>1-\theta/2\). Unboundedness of
\(\mathcal X\) therefore suffices for contradiction.

## Prior art, stress tests and evidence boundary

The ingredients are classical: genus-zero canonical products,
non-quasianalytic Gevrey bumps (source 136), the zero-density theorem
(source 128), and smoothed explicit formulas (sources 120 and 127).
The convergence argument (7)--(10) supplies the exact interpolation
lemma here rather than appealing to an unspecified multiplier theorem.
PL-463 already supplies finite-order box inversion. The general
variance/zero-free converse is classical (Zaccagnini, source 123, §3.3).
Schlage-Puchta's effective oscillation theorem, source 137, is a close
comparison: it locates prime-counting error on \([X,X^{1+\varepsilon}]\)
with explicit dependence on a zero. The present fixed-factor block
statement concerns an empirical window variance and gives no comparable
effective constants. No priority or effective improvement is claimed.

The exact delta is closure of PL-470's infinite-pole transfer for the
actual mod-5 source, and hence the actual-source implication in the
density-one clue. The generic meromorphic countermodel question is a
different statement and is not decided here. In particular, PL-469
remains valid: PL-470 proves that its pole-subtracted transform has
superpolynomial uniform strip growth. Its continuation cannot be
substituted into the arithmetic explicit formula (12). Positivity,
negative residues, and finite or sparse pole counts alone do not imply
that formula or its bounded remainder.

Load-bearing boundaries are explicit:

- At \(\beta=1/2\), no \(\sigma_0\in(1/2,\beta)\) exists. This
  argument gives no critical-line floor or zero simplicity statement.
- A simple density pole at 1 is removed by \(\Phi(1)=0\); a retained
  nontrivial zero has a different profile. Coincident zeros are merged
  with their full positive \(w_\rho\), not cancelled.
- The complex test is essential to the phase-free one-mode formula;
  its two real components implement the same estimate on the real source.
- The power count (4), smooth-series convergence in every derivative,
  and arithmetic contour growth are separate hypotheses. None follows
  from the others in a generic source class.
- Test norms, derivative orders and \(X_0\) are fixed but uncontrolled.
  No uniformity as \(\theta\uparrow1\), \(\sigma_0\downarrow1/2\),
  or the selected zero varies is asserted. A finite numerical zero list
  does not construct the annihilator certified here. Dependence on the
  hypothetical zero set is legitimate in this contrapositive necessity
  proof; it supplies no independently acquired arithmetic test or sign
  mechanism.
- At \(\beta=1-\theta/2\) the comparison does not contradict (3).
  A sequence of fixed exponents approaching 1 would imply joint GRH
  only if the respective unproved ceilings hold on unbounded sets.

The product convergence, integration-by-parts sign, Mellin Jacobian,
empirical-mean cancellation, residue weights, powers-of-5 correction,
finite inverse error and \(H^2/X\) normalization are checked in the
displayed derivation. No numerical experiment, Lean verification or
independent adversarial approval is claimed. The variance ceiling,
the relative covariance gate and an independent route to RH/GRH remain
unproved.
