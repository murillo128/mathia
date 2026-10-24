# MC-525 — Polynomial strip growth forces pole variance on every block

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CONDITIONAL-TRANSFER`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`.

## Claim and scope

Let \(a(n)\) be real, \(|a(n)|\le1\), and put
\[
A(x)=\sum_{n\le x}a(n),\qquad D(s)=\sum_{n\ge1}a(n)n^{-s}
\quad(\Re s>1).
\]
Fix \(1/2<\sigma_0<\beta<1\), \(\gamma>0\),
\(\rho=\beta+i\gamma\), and \(c\ne0\). Assume that
\[
R(s):=D(s)-\frac{c}{s-\rho}-\frac{\bar c}{s-\bar\rho}
\tag{1}
\]
extends holomorphically to an open neighborhood of the closed infinite
strip \(\sigma_0\le\Re s\le2\), and, for some finite \(B,C\),
\[
|R(\sigma+it)|\le C(1+|t|)^B
\quad(\sigma_0\le\sigma\le2,\ t\in\mathbb R).
\tag{2}
\]
Thus the only poles in this strip are the stated simple conjugate pair.
Both the absence of other poles and the uniform growth bound are
substantive hypotheses.

For real \(X\ge2\) and integer \(H\ge1\), define the complete window
sum, its empirical mean and centered variance by
\[
S_{X,H}(y)=A(y+H)-A(y),\qquad
m_{X,H}=X^{-1}\int_X^{2X}S_{X,H}(y)\,dy,
\]
\[
V_a(X,H)=\int_X^{2X}|S_{X,H}(y)-m_{X,H}|^2\,dy.
\]
There are constants \(h_0>0\), \(X_0\), and \(c_0>0\), depending
on the fixed data above, such that
\[
\boxed{V_a(X,H)\ge c_0H^2X^{2\beta-1}
\quad(X\ge X_0,\ 1\le H\le h_0X).}
\tag{3}
\]
In particular, for a fixed \(0<\theta<1\) with
\(\beta>1-\theta/2\), the diagonal-order ceiling
\[
V_a(X,\lfloor X^\theta\rfloor)
\ll_\varepsilon X^{1+\varepsilon}\lfloor X^\theta\rfloor
\quad\hbox{for every }\varepsilon>0
\tag{4}
\]
cannot hold on **any unbounded set of scales**, with constants uniform
on that set. Density one, dyadic spacing and unknown empirical means
are irrelevant to this contradiction.

Applied to the exact control of
[MC-524](MC-524-density-one-window-control-coexists-with-prescribed-sparse-poles.md),
this proves a necessary failure left qualitative there: for every
\(1/2<\sigma_0<\beta\), its pole-subtracted continuation is **not**
bounded by any polynomial in height uniformly on
\(\sigma_0\le\Re s\le2\). This does not refute MC-524; it identifies
an additional analytic condition that its construction necessarily
violates.

No such isolated-pair strip or growth estimate is supplied for
\(1/\zeta\) under the mere supposition of an off-critical zero.
This is not a density-one variance criterion for actual Möbius, an
unconditional estimate for \(M\), or an RH result.

## 1. Two mean-zero tests retain every phase of the pole

For \(1<u<2\), write
\[
p_1(u)=\Re u^{\rho-1},\qquad p_2(u)=\Im u^{\rho-1}.
\]
Choose a fixed nonnegative \(\chi\in C_c^\infty((1,2))\), positive
on an open interval, and normalize \(\int\chi=1\). Set
\[
\bar p_i=\int\chi p_i,\qquad
f_i(u)=\chi(u)(p_i(u)-\bar p_i),\qquad i=1,2.
\tag{5}
\]
Both tests are real and have integral zero. Their moment matrix is
\[
G_{ij}=\int f_i(u)p_j(u)\,du
=\int\chi(u)(p_i(u)-\bar p_i)(p_j(u)-\bar p_j)\,du.
\tag{6}
\]
It is positive definite. Indeed, a zero quadratic form would say that
a nonzero real combination of \(p_1,p_2\) is constant on an interval.
With \(t=\log u\) and \(b=\beta-1\), the Wronskian of
\(1,e^{bt}\cos(\gamma t),e^{bt}\sin(\gamma t)\) is
\[
\gamma(b^2+\gamma^2)e^{2bt}\ne0.
\tag{7}
\]
Those three functions are linearly independent on every open interval.
This also proves that empirical centering cannot erase the entire
two-dimensional pole profile.

Extend each \(f_i\) by zero. For \(h>0\), put
\[
\phi_{i,h}(u)=\frac1h\int_0^h f_i(u-v)\,dv,
\qquad
\widehat\phi_{i,h}(s)=\int_0^\infty\phi_{i,h}(u)u^{s-1}\,du.
\tag{8}
\]
Define the real matrix
\[
G(h)_{i1}=\Re\widehat\phi_{i,h}(\rho),\qquad
G(h)_{i2}=\Im\widehat\phi_{i,h}(\rho).
\]
The supports stay in a fixed compact subset of \((0,\infty)\) for
\(0<h\le1\), and all derivatives are uniformly bounded. Also
\(\phi_{i,h}=f_i+O(h)\) uniformly, so
\(G(h)=G+O(h)\). Choose \(h_0\le1\) sufficiently small that
\[
s_{\min}(G(h))\ge\tfrac12\lambda_{\min}(G)>0
\quad(0<h\le h_0).
\tag{9}
\]
Two tests prevent a phase zero at a selected scale. A single test would
not justify the every-block conclusion.

## 2. The growth hypothesis makes the Mellin contour shift uniform in H

Integration by parts in \(\log u\), using the compact supports and
uniform derivative bounds, gives for every fixed \(N\)
\[
|\widehat\phi_{i,h}(\sigma+it)|
\ll_N(1+|t|)^{-N}
\quad(\sigma_0\le\sigma\le2,\ 0<h\le h_0).
\tag{10}
\]
Mellin inversion and absolute convergence on \(\Re s=2\) give
\[
L_i(X,h):=\sum_n a(n)\phi_{i,h}(n/X)
=\frac1{2\pi i}\int_{(2)}D(s)X^s\widehat\phi_{i,h}(s)\,ds.
\tag{11}
\]
Choose \(N>B+2\). Hypothesis (2) and (10) make both vertical
integrals absolutely convergent and the horizontal sides tend to zero
when shifting to \(\Re s=\sigma_0\). The rational terms in (1) have
only the two fixed poles and are \(O(1/|t|)\) at large height.
The residue theorem therefore yields, uniformly in \(0<h\le h_0\),
\[
L_i(X,h)=2X^\beta\Re\!\left(c e^{i\gamma\log X}
                         \widehat\phi_{i,h}(\rho)\right)
          +O(X^{\sigma_0}).
\tag{12}
\]
No sharp Perron truncation, zero-free contour assertion, or limiting
exchange with a growing family of poles is being used.

Let \(z=c e^{i\gamma\log X}\). The two main terms in (12), as a
real vector, are
\[
2X^\beta G(h)(\Re z,-\Im z)^{\mathsf T}.
\]
Its Euclidean norm is at least
\(\lambda_{\min}(G)|c|X^\beta\) by (9), uniformly in the phase.
Since \(\sigma_0<\beta\), increasing \(X_0\) absorbs the remainder:
\[
|L_1(X,h)|^2+|L_2(X,h)|^2\gg X^{2\beta}
\quad(X\ge X_0,\ 0<h\le h_0).
\tag{13}
\]

## 3. Exact window pairing gives the centered-variance floor

Set \(h=H/X\). Finite interchange in (8), with the substitution
\(y=n-Xv\), gives the exact identity
\[
L_i(X,H/X)
=\frac1H\int_X^{2X}S_{X,H}(y)f_i(y/X)\,dy
=\frac1H\int_X^{2X}(S_{X,H}(y)-m_{X,H})f_i(y/X)\,dy.
\tag{14}
\]
The support of \(f_i\) restricts the integral to the measured block;
the box average may extend beyond the block but precisely represents
the windows crossing its endpoint. There is no unpaid boundary term.
The second equality uses \(\int f_i=0\), without estimating the mean.

Cauchy–Schwarz now gives
\[
\sum_{i=1}^2|L_i(X,H/X)|^2
\le\frac{X}{H^2}V_a(X,H)
                  \sum_{i=1}^2\|f_i\|_2^2.
\tag{15}
\]
Combining (13) and (15) proves (3). For
\(H=\lfloor X^\theta\rfloor\), the ratio of this floor to
\(X^{1+\varepsilon}H\) is bounded below by a positive constant
times
\[
X^{2\beta+\theta-2-\varepsilon}.
\tag{16}
\]
Taking \(0<\varepsilon<2\beta+\theta-2\) proves the stated
incompatibility on any unbounded set, not merely a positive-density set.

## 4. The exact cost to the sparse-pole control

MC-524 has residues \(c=1/2\), only the prescribed poles throughout
\(\Re s>1/2\), and complete **uncentered** moments at most
\(16XH\log X\) on an unbounded density-one dyadic set, simultaneously
for every integer \(1\le H\le X\). Centering only decreases them.
For its fixed \(\beta>1/2\), choose once and for all
\[
2(1-\beta)<\theta<1.
\]
If (2) held on any strip with \(1/2<\sigma_0<\beta\), all the
hypotheses above would hold there. Equations (3) and (16) would
contradict these retained-scale bounds. Hence for every such
\(\sigma_0\) and every \(B\ge0\),
\[
\sup_{\sigma_0\le\sigma\le2,\ t\in\mathbb R}
\frac{|D(\sigma+it)-\tfrac1{2(\sigma+it-\rho)}
                    -\tfrac1{2(\sigma+it-\bar\rho)}|}
     {(1+|t|)^B}=\infty.
\tag{17}
\]
Holomorphy of the pole-subtracted function makes it bounded on compact
subsets of this strip, so the failure occurs at unbounded heights.
Equation (17) is a uniform-strip statement; it does not identify a
particular vertical line with this growth, nor an exponential order.

## Prior art and mathematical delta

Mellin inversion and conversion of finitely many poles into smoothed
asymptotic terms under vertical growth/decay hypotheses are classical.
See Philippe Flajolet, Xavier Gourdon and Philippe Dumas,
[*Mellin Transforms and Asymptotics: Harmonic Sums*](https://algo.inria.fr/flajolet/Publications/mellin-harm.pdf),
Theoretical Computer Science 144 (1995), 3–58, Theorem 4 (converse
mapping); and [DLMF §2.5(i)](https://dlmf.nist.gov/2.5).
Multiplying by a compact smooth test supplies the decay needed here.
The contour argument is proved directly above, including uniformity in
the shrinking additive-window parameter. No new Mellin mapping theorem
or covariance inequality is claimed.

Targeted searches of Mellin converse mapping, Möbius short-interval
variance, and pole-driven oscillations identify the classical transform
mechanism; they do not establish novelty of this specialization.
The durable local delta is the every-block **empirically centered**
lower bound (3), together with the consequent necessary superpolynomial
strip growth (17) of the already-persisted MC-524 control. The two
mean-zero tests eliminate both an unknown block mean and accidental
phase cancellation. Meromorphic continuation plus a pole count was
insufficient in MC-524; this calculation isolates one additional,
quantitatively testable hypothesis that changes that conclusion.

## Stress tests and remaining arithmetic boundary

- The factor in (3) is \(H^2X^{2\beta-1}\), not \(HX^{2\beta}\).
  The \(1/H\) in the exact pairing and the \(X\) in the test's
  squared norm account for both powers. At the critical balance
  \(\beta=1-\theta/2\), it does not contradict diagonal order.
- A pole at \(s=1\) with a constant source profile can be erased by
  empirical centering: \(a(n)=1\) has zero variance for integer
  windows. Here \(\gamma>0\) and the independence (7) explicitly
  exclude that degeneration. Constants need not remain uniform as
  the pole parameters degenerate.
- Polynomial growth is imposed **after subtracting the poles** and
  uniformly throughout the strip. Bounding only \(D\) on the
  original half-plane of absolute convergence does not suffice.
  Nor is a polynomial bound for \(\zeta\) a polynomial bound for
  its reciprocal near zeros.
- Only a fixed simple conjugate pair is treated. An arbitrary
  sparse infinite family of reciprocal-zeta poles need not admit
  this pole-free remainder or the contour shift. A finite-height
  isolated zero does not supply isolation across an infinite strip.
  Sparse pole counting in MC-522 cannot be substituted for (1)–(2).
- The proof is analytic, with exact finite-dimensional phase
  separation and an exact window identity. No numerical evidence
  for Möbius variance, independent adversarial approval, or Lean
  verification is asserted.

As an auxiliary normalization check, exact rational arithmetic verified
(14) in 62 cases: integers \(4\le X\le16\),
\(1\le H\le\lfloor X/2\rfloor\), coefficients
\(a(n)=(-1)^{n(n+1)/2}\), and the zero-extended mean-zero test
\(f(u)=(u-1)^2(2-u)^2(u-3/2)\) on \([1,2]\).
The coefficient-side integrals and the piecewise constant window-side
integrals were evaluated separately. This checks the orientation and
scaling of the finite identity; the displayed analytic proof, not this
finite check or this finite-smoothness test, supplies the contour result.

The result closes the polynomial-strip-growth repair for the specific
two-pole control. Whether actual Möbius selected-scale moments can
exploit additional reciprocal-zeta structure without assuming the
zero-free conclusion remains unresolved.
