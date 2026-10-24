# PL-470 — Positive-source strip growth and the infinite-pole tail gate

**Evidence/status:** EXACT-DERIVED + CLASSICAL MELLIN/EXPLICIT-FORMULA INPUT;
CONDITIONAL VARIANCE TRANSFER; NO EXTERNAL NOVELTY CLAIM.

## Claim and scope

The positive source in
[[research/prime_lattice/findings/PL-469-positive-sparse-block-sources-retain-negative-pole-residues|PL-469]]
necessarily has superpolynomial **uniform strip growth** after its three
principal parts are subtracted. More precisely, write its identity-residue
transform as \(D_b(s)=\sum_{n\equiv1\ (5)}b_nn^{-s}\), and put
\(\rho=\beta+i\gamma\), with the parameters of PL-469. For every
\(\beta-1<\sigma_0<\beta\) and every finite \(B\ge0\),
\[
\sup_{\substack{\sigma_0\le\sigma\le2\\t\in\mathbb R}}
\frac{|D_b(\sigma+it)-\tfrac1{4(\sigma+it-1)}
                 +\tfrac1{\sigma+it-\rho}
                 +\tfrac1{\sigma+it-\bar\rho}|}
     {(1+|t|)^B}=\infty.                                      \tag{1}
\]
Removable values in (1) are understood by holomorphic extension.
This locates a genuine missing hypothesis in that positive control;
it does not invalidate its meromorphic continuation or variance bound.

For the actual source \(a_n=\Lambda(n)\mathbf1_{n\equiv1\ (5)}\),
the corresponding mean-zero measurements have an absolutely convergent
explicit zero sum, with the pole at 1 erased exactly and the omitted
Euler factor at 5 retained explicitly. Equations (12)--(17) below give
a finite-packet variance certificate and its full tail cost. The fixed
isolated-pair result does **not** by itself verify that certificate for
the infinite arithmetic zero family. No selected-scale zero-free
criterion or actual-prime variance estimate is proved.

The bounded source transfer is from
[[research/mobius_cancellation/findings/MC-525-polynomial-strip-growth-forces-pole-variance-on-every-block|MC-525]],
read under the local quantitative-continuation clue's exact-path grant.
Its argument is reconstructed here with the positive density term,
periodic error, logarithmically growing coefficients, and arithmetic
pole tail accounted for separately.

## 1. Exact centering and a positive density pole

Let \(a_n\) be real with \(|a_n|\ll(\log(2n))^A\), for fixed
\(A\ge0\). Define
\[
S(y)=\sum_{y<n\le y+H}a_n,\quad
m=X^{-1}\int_X^{2X}S(y)\,dy,\quad
V(X,H)=\int_X^{2X}|S(y)-m|^2dy.                            \tag{2}
\]
For real \(f_i\in C_c^\infty((1,2))\), \(\int f_i=0\), extend
by zero and set
\[
h=H/X,\quad \phi_{i,h}(u)=h^{-1}\int_0^h f_i(u-v)\,dv,
\quad \Phi_{i,h}(s)=\int_0^\infty\phi_{i,h}(u)u^{s-1}\,du.
\]
Finite interchange, including windows crossing \(2X\), gives exactly
\[
L_i:=\sum_n a_n\phi_{i,h}(n/X)
 =H^{-1}\int_X^{2X}(S(y)-m)f_i(y/X)\,dy,
\qquad
\|L\|_2^2\le \frac{X}{H^2}V(X,H)F^2,
\quad F^2=\sum_i\|f_i\|_2^2.                              \tag{3}
\]
There is no estimate or substitution for the empirical mean. Also
\(\Phi_{i,h}(1)=\int\phi_{i,h}=0\) exactly.
For fixed tests, all derivatives of \(\phi_{i,h}\) are uniformly
bounded for \(0<h\le1\), with support in a fixed compact subset of
\((0,\infty)\). Thus on any fixed strip, for every integer \(N\),
\[
|\Phi_{i,h}(\sigma+it)|\le C_N(1+|t|)^{-N}.                \tag{4}
\]
Here and below constants may depend on the test bank, never on \(X,H\).

Suppose \(\sigma_0<\beta<1\), \(\gamma>0\), \(c\ne0\), and
\[
R(s)=D(s)-\frac{r}{s-1}-\frac{c}{s-\rho}
                         -\frac{\bar c}{s-\bar\rho},
\quad D(s)=\sum_n a_nn^{-s},\quad r\in\mathbb R,             \tag{5}
\]
is holomorphic near the closed infinite strip
\(\sigma_0\le\Re s\le2\) and uniformly \(O((1+|t|)^B)\) there.
The only allowed poles in this strip are the displayed ones.
Absolute convergence of \(D\) on \(\Re s=2\) follows from the
coefficient bound, also when \(A=1\) as for von Mangoldt.
Mellin inversion, (4), and a contour shift with \(N>B+2\) give
\[
L_i=2X^\beta\Re\{c e^{i\gamma\log X}\Phi_{i,h}(\rho)\}
                 +O(X^{\sigma_0}).                        \tag{6}
\]
The density residue is \(rX\Phi_{i,h}(1)=0\); it has not been
dropped as an approximation. The rational terms have polynomial
growth on the contour away from their fixed poles.

To prevent cancellation at one phase, choose a smooth nonnegative
\(\omega\) supported in \((1,2)\), positive on an interval, with
\(\int\omega=1\). Put
\[
p_1(u)=\Re u^{\rho-1},\quad p_2(u)=\Im u^{\rho-1},\quad
f_i=\omega(p_i-\int\omega p_i),\quad
G_{ij}=\int\omega(p_i-\bar p_i)(p_j-\bar p_j).               \tag{7}
\]
The matrix \(G\) is positive definite: in the variable \(t=\log u\),
the functions \(1,e^{(\beta-1)t}\cos\gamma t,
e^{(\beta-1)t}\sin\gamma t\) have Wronskian
\(\gamma((\beta-1)^2+\gamma^2)e^{2(\beta-1)t}\ne0\).
The matrix with columns \(\Re\Phi_{i,h}(\rho)\) and
\(\Im\Phi_{i,h}(\rho)\) is \(G+O(h)\). For a fixed sufficiently
small \(h_0>0\), its least singular value is at least
\(\lambda_{\min}(G)/2\) throughout \(0<h\le h_0\).
The main vector in (6) therefore has norm at least
\(|c|\lambda_{\min}(G)X^\beta\), uniformly in its phase.
Since \(\sigma_0<\beta\), (3) proves
\[
V(X,H)\ge c_0 H^2X^{2\beta-1}
\quad(X\ge X_0,\ 1\le H\le h_0X).                         \tag{8}
\]
Neither positivity nor boundedness by one was needed. A simple real
pole at 1 is harmless, whereas other poles cannot silently be included
in the holomorphic remainder of (5).

## 2. What the sparse positive construction must pay

For the periodic background \(b_n^0=(5/4)\mathbf1_{n\equiv1\ (5)}\),
its cumulative count minus \(x/4\) is bounded. Stieltjes integration
against \(\phi_{i,h}(x/X)\), whose total variation is uniformly
bounded, therefore gives
\[
\sum_n b_n^0\phi_{i,h}(n/X)
 =\frac X4\int\phi_{i,h}+O(1)=O(1).                       \tag{9}
\]
Thus the periodic counting error is retained; it is not identically
zero, and cannot cancel an \(X^\beta\) pole vector as \(X\to\infty\).

PL-469 has exactly \(r=1/4,c=-1\) in (5), throughout
\(\Re s>\beta-1\). Its complete retained-block variance is at most
\(25X/16\) for every integer \(1\le H\le X\). If a polynomial
bound in (1) existed on any indicated strip, choose a fixed
\(1-\beta<\theta<1\) and \(H=\lfloor X^\theta\rfloor\).
The ratio of (8) to \(X\) grows as
\(X^{2(\theta+\beta-1)}\) on every sufficiently large retained
dyadic scale, a contradiction. This proves (1). Holomorphy bounds
the remainder on compact subsets, so the failure occurs at unbounded
heights. No particular vertical line or exponential growth order is
identified. The same diagnosis holds if the full periodic transform
\((5/4)5^{-s}\zeta(s,1/5)\) is subtracted instead of its density
principal part: their difference is holomorphic and polynomially
bounded on each of these fixed strips, by Euler--Maclaurin continuation.

## 3. The actual source: retain every zero and the factor at 5

Now fix \(a_n=\Lambda(n)\mathbf1_{n\equiv1\ (5)}\). Let
\(\chi_0\) be principal and \(\chi_2\) the quadratic character
modulo 5. The other two characters are odd and conjugate. Define
\[
D_*(s)=\frac14\left(-\frac{\zeta'}\zeta(s)
                  +\sum_{\chi\ne\chi_0}-\frac{L'}L(s,\chi)\right).
\]
Character orthogonality and \(L(s,\chi_0)=(1-5^{-s})\zeta(s)\)
give, first in absolute convergence,
\[
D(s)=D_*(s)-\frac{\log5}{4(5^s-1)},\qquad
L_i=\sum_n a_n^*\phi_{i,h}(n/X)
          -\frac{\log5}{4}\sum_{k\ge1}\phi_{i,h}(5^k/X),    \tag{10}
\]
where \(a_n^*=a_n+(\log5)/4\) at \(n=5^k\), and \(a_n^*=a_n\)
otherwise. The last sum has uniformly boundedly many terms. This
avoids concealing the infinite Euler-factor pole family on \(\Re s=0\).

Let \(Z\) be the distinct nontrivial zeros of the four primitive
functions \(\zeta,L(\cdot,\chi_2)\), and the two odd mod-5
\(L\)-functions. Include real zeros if any; do not assume simplicity.
Set \(w_\rho=\tfrac14\sum m(\rho)>0\), summing multiplicities
over these four functions. The set is conjugation invariant and
\(w_{\bar\rho}=w_\rho\). The only other poles of \(D_*\) in
\(-1/2\le\Re s\le2\) are 1, of residue \(1/4\), and 0, of
residue \(-1/4\) from the simple trivial zero of the even primitive
\(L(s,\chi_2)\). The primitive zeta factor is nonzero at 0.

Shift the smoothed contour to \(\Re s=-1/2\). Classical unit-height
zero counts are \(O(\log(2+|t|))\), with multiplicity, for this fixed
finite family. Choose horizontal heights in each sufficiently large
unit interval at distance \(\gg1/\log T\) from all zero ordinates.
The local logarithmic-derivative expansions bound \(D_*\) on those
segments by \(O(\log^2 T)\). The functional equations and absolute
convergence at \(\Re(1-s)=3/2\) give
\(D_*(-1/2+it)=O(\log(2+|t|))\). Together with (4) these facts
justify the shift and absolute convergence of the resulting zero sum.
The exact formula is
\[
\boxed{L_i=-\sum_{\rho\in Z}w_\rho X^\rho\Phi_{i,h}(\rho)
                     +B_i(X,h),}                          \tag{11}
\]
\[
B_i=-\tfrac14\Phi_{i,h}(0)
 -\tfrac{\log5}{4}\sum_{k\ge1}\phi_{i,h}(5^k/X)
 +\frac1{2\pi i}\int_{(-1/2)}D_*(s)X^s\Phi_{i,h}(s)\,ds.
                                                               \tag{12}
\]
The last integral is \(O(X^{-1/2})\), and \(B_i=O(1)\), uniformly
for \(0<h\le h_0\le1\). The density pole contributes exactly zero.
All nontrivial zeros, the zero at 0, and the removed Euler factor have
now been accounted for. Sources 120 and 127 supply the classical
explicit-formula inputs; no bound for a zero-free holomorphic
remainder in a right-hand strip is being assumed.

## 4. The finite-packet certificate and its nonuniform costs

Let \(\mathcal P\subset Z\) be a finite conjugation-closed packet
containing a chosen nonreal \(\rho_0=\beta+i\gamma\), \(\gamma>0\).
For each pair use the two real profiles
\(\Re u^{\rho-1},\Im u^{\rho-1}\); for each real zero use
\(u^{\rho-1}\) once. Distinct zeros are merged with their full
weights \(w_\rho\). These profiles together with the constant
function are linearly independent, by independence of distinct
exponentials in \(\log u\). Their \(\omega\)-centered covariance
construction as in (7) therefore yields a positive definite matrix
\(G_{\mathcal P}\) and a bank of \(d\) mean-zero real tests.

Let \(M_{\mathcal P}(h)\) have the corresponding real/imaginary
\(\Phi_{i,h}\) columns, and set
\[
F_{\mathcal P}^2=\sum_i\|f_i\|_2^2,\qquad
\kappa_{\mathcal P}
 =\frac{2w_{\rho_0}}{F_{\mathcal P}}
       \inf_{0<h\le h_{\mathcal P}}s_{\min}(M_{\mathcal P}(h))>0.
                                                               \tag{13}
\]
Here \(h_{\mathcal P}>0\) is fixed sufficiently small. The packet
vector in (11) equals \(M_{\mathcal P}(h)v(X)\), where a conjugate
pair contributes coordinates
\((-2w_\rho X^{\Re\rho}\cos(\Im\rho\log X),
  2w_\rho X^{\Re\rho}\sin(\Im\rho\log X))\), and a real zero
contributes \(-w_\rho X^\rho\). In particular
\(\|v(X)\|_2\ge2w_{\rho_0}X^\beta\).
No rightmost zero or common real part within the packet is required.

Define the **complete** residual vector
\[
E_{\mathcal P}(X,h)=B(X,h)
       -\sum_{\rho\notin\mathcal P}w_\rho X^\rho\Phi_h(\rho).
\]
On any declared set of scales where \(h=H/X\le h_{\mathcal P}\),
the sufficient certificate
\[
\frac{\|E_{\mathcal P}(X,h)\|_2}{F_{\mathcal P}}
       \le\tfrac12\kappa_{\mathcal P}X^\beta               \tag{14}
\]
implies, by (3),
\[
V(X,H)\ge\tfrac14\kappa_{\mathcal P}^2H^2X^{2\beta-1}.
                                                               \tag{15}
\]
For a fixed \(\kappa_{\mathcal P}>0\), fixed
\(H=\lfloor X^\theta\rfloor\), and \(\beta>1-\theta/2\), this
contradicts \(V\ll XH(\log X)^A\) on any unbounded set where
**both** estimates hold. An unbounded set of large values elsewhere
does not suffice.

The routine absolute tail estimate for a fixed bank is only
\[
\left\|\sum_{|\Im\rho|>T}w_\rho X^\rho\Phi_h(\rho)\right\|_2
 \le C_{N,f}X\,T^{1-N}\log(2T),\qquad T\ge2,
                                                               \tag{16}
\]
for every fixed integer \(N>2\). This follows by (4),
\(0<\Re\rho<1\), and summing the unit-height zero counts. This
bound does not supply an \(O(X^{\sigma_0})\) residual for a fixed
\(\sigma_0<\beta\).
If a packet omits any zeros below \(T\), their terms must be added
separately to (16). With fixed \(T,N,f\), the upper bound in (16)
divided by \(X^\beta\) grows like \(X^{1-\beta}\); it does not
verify (14). This is a limitation of this estimate, not a lower bound
on the actual residual or a counterexample to arithmetic recovery.

Making \(T\) grow cannot retain all fixed-packet constants for free:

- For an \(r\)-test bank and a \(d\)-dimensional packet with \(d>r\),
  the lower modulus \(\inf_{\|v\|=1}\|M(h)v\|\) is zero by rank.
  This blocks this full-coefficient singular-value certificate, not
  necessarily the actual one-parameter phase vector \(v(X)\).
- For fixed smooth tests and a column at height \(\Gamma\), (4)
  bounds its norm by \(C_{N,f}(1+|\Gamma|)^{-N}\). Hence the lower
  modulus is at most this quantity. A fixed bank has no positive
  uniform lower modulus over packets reaching unbounded height.
- For packet-adapted tests the constants themselves change. In
  particular, retaining half the Gram margin via
  \(\|M(h)-G\|\le C_{\mathcal P}h\) calls for
  \(C_{\mathcal P}h\le\lambda_{\min}(G_{\mathcal P})/2\), and
  the derivative seminorms entering \(C_{N,f}\), the test norm
  \(F_{\mathcal P}\), and \(\kappa_{\mathcal P}\) must all be priced.

For example, even after all lower-height zeros are included, a growing
packet argument based on (16) needs a quantitative inequality of the form
\[
\frac{C_{N,f(X)}}{F_{\mathcal P(X)}}
 X^{1-\beta}T(X)^{1-N}\log(2T(X))
 +\frac{\|B(X,h)\|}{F_{\mathcal P(X)}X^\beta}
 \le\tfrac12\kappa_{\mathcal P(X)},                         \tag{17}
\]
as well as the small-window restriction. To contradict the diagonal
ceiling it also needs
\(\kappa_{\mathcal P(X)}^2X^{2\beta+\theta-2}/(\log X)^A\to\infty\)
on the measured scales. No such estimates are established here.
Negative pole residues prevent cancellation of coincident principal
parts; they do not make the complex summands in (11) point in a common
direction. Sublinear zero counts alone likewise do not supply (14).

## Prior art, audit and consequence

The analytic mechanism is classical smoothed Mellin converse mapping
(source 124, Theorem 4; [DLMF §2.5(i)](https://dlmf.nist.gov/2.5)),
and the arithmetic identity is a smoothed explicit formula. The
contour separation and logarithmic-derivative estimates are described
in [Kedlaya, Chapter 10, §10.3](https://kskedlaya.org/ant/chapter-10.html)
and [Chapter 11, §11.1](https://kskedlaya.org/ant/chapter-11.html).
The general variance/zero-free converse is already classical
(source 123, §3.3). No new transform theorem, finite-dimensional
independence principle, or external priority is claimed.

The local delta is the proved growth diagnosis (1) for the positive
PL-469 control, together with the fully normalized arithmetic
packet/tail interface (11)--(17). The positive background and the
factor at 5 are not hidden errors. The isolated-pair theorem therefore
does distinguish a substantive analytic hypothesis, while its
infinite-pole application remains a separate quantitative problem.

The proof was audited for the signs in (5), the \(1/4\) residues,
the factor 2 for conjugate pairs, the exact \(1/H\) window pairing,
and the \(H^2/X\) conversion in (3). The pole at 1 is a useful
degeneracy control: its profile is constant and is removed exactly;
the nonreal pair is not. All contour decay estimates are uniform in
the shrinking box width for fixed tests. Auxiliary exact rational
checks independently evaluated both sides of (3) in 284 cases
(integer \(4\le X\le24\), \(1\le H\le\lfloor X/2\rfloor\),
two positive periodic/perturbed sources), with the zero-extended test
\((u-1)^2(2-u)^2(u-3/2)\). Exact Gaussian-integer arithmetic also
checked the character average and the correction in (10) at all 711
prime powers at most 5000, comparing coefficients of each \(\log p\).
These finite checks test the normalization only; the finite-smoothness
polynomial is not the test used for the contour theorem. No numerical
prime-variance experiment, Lean verification, or independent
adversarial approval is asserted.

The quantitative-continuation clue remains open for the unrestricted
arithmetic zero family. PL-466's every-dyadic-block theorem and the
accepted thin-mesh question are unchanged. Neither this partial
transfer nor inability to prove (14) is an RH/GRH result or an
impossibility theorem for selected-scale recovery.
