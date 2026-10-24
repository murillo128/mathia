# MC-527 — Good-height truncation isolates selected-scale pole cancellation

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `CONDITIONAL-TRANSFER`, `NO-NOVELTY-CLAIM`.

## Claim and evidence boundary

For a **fixed** finite bank of real mean-zero tests
\(f_i\in C_c^\infty((1,2))\), the complete smoothed reciprocal-zeta
pole packet admits an unconditional finite-height approximation, uniform
in the additive-window ratio. For every fixed \(\delta>0\), one may
take, for all sufficiently large \(X\), a suitable height
\(T(X)\in[X^\delta,X^\delta+1]\) and obtain
\[
L_i(X,h)=
\sum_{|\Im\rho|<T(X)}\operatorname{Res}_{s=\rho}
 \frac{X^s\Phi_{i,h}(s)}{\zeta(s)}+O_{f,\delta}(X^{-1/2}),
\qquad 0<h\le1.                                      \tag{1}
\]
Here the sum contains **every distinct nontrivial zero** below the
height, with its full Laurent principal part. The definitions of
\(L_i,\Phi_{i,h}\) and the quantitative error are given below.
No RH, simplicity, residue-size bound, rightmost zero, or finite-exception
hypothesis is used. Equation (1) is a contour-grouped formula, not an
assertion of absolute convergence of individual zero contributions.

Consequently, if complete centered Möbius variance has diagonal order on
an unbounded scale set \(E\), any hypothetical zero to the right of the
associated threshold forces quantitative cancellation by the rest of
this polynomial-height packet on those **same scales**. Equations
(15)–(16) specify the necessary cancellation, including multiple poles.

This narrows the local pole-tail clue: for fixed smooth tests, a small
complete contour remainder is already available by classical good-height
estimates. The missing input is a lower bound for the **aggregate growing
packet**, or control of its complement to a fixed pole. The theorem does
not supply that input, exclude an infinite exceptional zero family,
prove a variance upper bound, or advance an unconditional Mertens exponent.

## 1. Exact centered measurement

Extend the tests by zero, and define
\[
\phi_{i,h}(u)=h^{-1}\int_0^h f_i(u-v)\,dv,
\qquad
\Phi_{i,h}(s)=\int_0^\infty\phi_{i,h}(u)u^{s-1}\,du,
\qquad L_i(X,h)=\sum_n\mu(n)\phi_{i,h}(n/X).             \tag{2}
\]
Let \(S(y)=M(y+H)-M(y)\),
\(m=X^{-1}\int_X^{2X}S(y)\,dy\),
\(V_\mu(X,H)=\int_X^{2X}|S(y)-m|^2dy\), and
\(F^2=\sum_i\|f_i\|_2^2>0\). Finite interchange gives
\[
L_i(X,H/X)=H^{-1}\int_X^{2X}(S(y)-m)f_i(y/X)\,dy,
\qquad
\|L\|_2^2\le XF^2H^{-2}V_\mu(X,H).                    \tag{3}
\]
The coefficient of \(\mu(n)\) is exactly
\(H^{-1}\int_{n-H}^n f_i(y/X)dy\). Thus endpoint-crossing windows
and the empirical mean are accounted for without an error term. This
is the normalization in [MC-526](MC-526-selected-mobius-variance-excludes-finite-exceptional-zero-clusters.md).

All derivatives of \(\phi_{i,h}\) have uniform bounds for \(0<h\le1\),
with support in one compact subset of \((0,\infty)\). Set
\[
K_N(f)=\sup_{\substack{0<h\le1\\-1/2\le\sigma\le2\\t\in\mathbb R}}
 (1+|t|)^N\|\Phi_h(\sigma+it)\|_2<\infty.             \tag{4}
\]
Integration by parts in \(\log u\) proves finiteness for every fixed
integer \(N\). Also \(\Phi_{i,h}(1)=0\), although reciprocal zeta
has no pole at 1 requiring this cancellation.

## 2. Unconditional good heights and the left edge

There are absolute \(B\ge1,c>0,Y_0\) such that for every
\(Y\ge Y_0\) one can choose \(T\in[Y,Y+1]\) with
\[
\sup_{-1/2\le\sigma\le2}|1/\zeta(\sigma\pm iT)|\ll Y^B,
\qquad \min_{\rho}|T-\Im\rho|\ge c/\log Y.             \tag{5}
\]
The minimum here is over nontrivial zero ordinates. This is a modest
strengthening of the height selection in Titchmarsh's Theorem 9.7,
whose exceptional-set form allows the simultaneous distance condition.

For completeness, the classical local logarithmic-derivative formula
(Titchmarsh, Theorem 9.6(A)) integrated from \(2+it\) gives
\[
\log|\zeta(\sigma+it)|
 =\sum_{|\gamma-t|\le1}\log|\sigma+it-\rho|+O(\log Y)
\quad(-1/2\le\sigma\le2,\ Y\le t\le Y+1),             \tag{6}
\]
away from zero ordinates, with multiplicities in the sum. The bounded
Euler-product value at \(2+it\) and its \(O(\log Y)\) nearby zeros
absorb the reference terms. With
\[
Q(t)=\sum_{Y-1\le\gamma\le Y+2}
       \log^+\!\frac1{|t-\gamma|},
\]
the unit-height zero count and integrability of the logarithmic
singularity give \(\int_Y^{Y+1}Q(t)dt\ll\log Y\).
Outside a set of measure at most \(1/4\), therefore,
\(Q(t)\le C\log Y\) for an absolute \(C\).
The union of intervals of radius \(c/\log Y\) around all nearby
ordinates has measure at most \(1/4\) when \(c\) is sufficiently
small. Select \(T\) outside both sets; (6) gives (5).
Conjugation gives the negative-height edge. This argument neither
bounds individual inverse derivatives nor assumes separation of zeros
from one another.

On the entire left vertical edge the functional equation gives
\[
|1/\zeta(-1/2+it)|\ll(1+|t|)^{-1}.                    \tag{7}
\]
Indeed the reciprocal Euler product at \(3/2-it\) is bounded and
the functional-equation factor has modulus comparable to \(|t|\)
at large height. Compactness handles bounded height. There are no
zeta zeros on this line.

## 3. The finite rectangle, all principal parts, and its error

Mellin inversion starts on \(\Re s=2\), where the Dirichlet series
is absolutely convergent. Write
\[
P_T(X,h)=\left(
 \sum_{|\Im\rho|<T}\operatorname{Res}_{s=\rho}
              \frac{X^s\Phi_{i,h}(s)}{\zeta(s)}
                         \right)_i,
\qquad
B_f(X,h)=\frac1{2\pi i}\int_{(-1/2)}
                  \frac{X^s\Phi_h(s)}{\zeta(s)}\,ds.    \tag{8}
\]
Use the rectangle with vertical edges \(-1/2,2\) and heights
\(\pm T\) from (5). Its only poles are the nontrivial zeta zeros:
the reciprocal is regular at 0, vanishes at 1, and the first trivial
zero lies at \(-2\). For every integer \(N>1\),
\[
L=P_T+B_f+E_T,\qquad
\|B_f\|_2\ll K_2(f)X^{-1/2},\qquad
\|E_T\|_2\ll K_N(f)X^2Y^{B+1-N}.                      \tag{9}
\]
All bounds are uniform for \(X\ge2,0<h\le1\). Specifically, the
discarded right tail is \(O(K_N X^2Y^{1-N})\), the two horizontal
edges are \(O(K_N X^2Y^{B-N})\), and completing the left edge
costs \(O(K_N X^{-1/2}Y^{-N})\), by (7). Their sum implies the
slightly looser final bound in (9).

If \(1/\zeta(s)=\sum_{r=1}^{d_\rho}c_{\rho,r}(s-\rho)^{-r}
+\text{holomorphic}\), its full summand is
\[
X^\rho\sum_{r=1}^{d_\rho}c_{\rho,r}
 \sum_{\ell=0}^{r-1}
 \frac{(\log X)^{r-1-\ell}\Phi_{i,h}^{(\ell)}(\rho)}
      {(r-1-\ell)!\,\ell!}.                            \tag{10}
\]
Only at a simple zero does this reduce to
\(X^\rho\Phi_{i,h}(\rho)/\zeta'(\rho)\).
A zero ordinary residue \(c_{\rho,1}\) does not remove a higher-order
pole; for a pure double principal part it leaves
\(c_{\rho,2}X^\rho(\log X\,\Phi_{i,h}(\rho)+\Phi'_{i,h}(\rho))\).

For fixed \(X,h,f\), taking good heights to infinity proves the
grouped limit \(L=B_f+\lim P_T\). This does **not** justify
reordering the terms or summing their absolute values. Alternatively,
set \(Y=X^\delta\). Given a fixed \(A>0\), choose one fixed
integer \(N>B+1+(A+2)/\delta\). Then (9) gives
\(E_T=O_{f,\delta,A}(X^{-A})\); taking \(A\ge1/2\) proves (1).

## 4. What a selected-scale ceiling forces the other poles to do

Fix \(0<\theta<1\), put \(\alpha=1-\theta/2\), and suppose on
an unbounded set \(E\) that
\[
V_\mu(X,\lfloor X^\theta\rfloor)
 \ll_\varepsilon X^{1+\varepsilon}\lfloor X^\theta\rfloor
\quad\text{for every }\varepsilon>0.                  \tag{11}
\]
Constants are uniform on the measured scales. Equations (1) and (3)
imply for every fixed bank, \(\delta>0\), and \(\varepsilon>0\),
\[
\|P_{T(X)}(X,H/X)\|_2\ll_{f,\delta,\varepsilon}
                         X^{\alpha+\varepsilon}
\quad(X\in E).                                        \tag{12}
\]

Suppose hypothetically that \(\rho_0=\beta+i\gamma\),
\(\gamma>0,\beta>\alpha\), is a zero of order \(m\), and let
\(c_m\ne0\) be the highest Laurent coefficient of its reciprocal.
Choose the two fixed tests
\[
p_1=\Re u^{\rho_0-1},\quad p_2=\Im u^{\rho_0-1},\qquad
f_i=\chi(p_i-\textstyle\int\chi p_i),
\quad \chi\ge0,\ \int\chi=1,                           \tag{13}
\]
where \(\chi\in C_c^\infty((1,2))\) is positive on an interval.
The covariance matrix \(G_{ij}=\int f_i p_j\) is positive definite:
\(1,p_1,p_2\) are independent, as follows from distinct exponentials
in \(\log u\). The matrix \(G(h)\) of real and imaginary
\(\Phi_{i,h}(\rho_0)\) columns tends to \(G\).

Let \(Q_0(X,h)\) be the contribution of just \(\rho_0,\bar\rho_0\)
to (8), with all their Laurent terms. Formula (10) gives
\[
Q_0=\frac{2X^\beta(\log X)^{m-1}}{(m-1)!}G(h)
 \begin{pmatrix}\Re(c_m e^{i\gamma\log X})\\
                 -\Im(c_m e^{i\gamma\log X})\end{pmatrix}
 +O_f(X^\beta(\log X)^{m-2}),
\qquad
\|Q_0\|_2\gg_f X^\beta(\log X)^{m-1}.                 \tag{14}
\]
For \(m=1\) the remainder displayed here is identically zero.
The lower bound holds at every sufficiently large \(X\), since
\(h=H/X\to0\). No hypothesis on any other zero is needed.

For large \(X\), the full packet includes this pair. Put
\(C_T=P_T-Q_0\), which retains **all** the other zeros below
\(T(X)\), including zeros on the critical line. For every fixed
\(0<\varepsilon<\beta-\alpha\), (12)–(14) force
\[
\boxed{\frac{\|C_T+Q_0\|_2}{\|Q_0\|_2}
 \ll_{f,\delta,\varepsilon}
 X^{-(\beta-\alpha-\varepsilon)}(\log X)^{1-m}
 =:r(X)\longrightarrow0\quad(X\in E).}                \tag{15}
\]
In particular, with \(r\) denoting an upper bound in (15),
\[
\left|\frac{\|C_T\|_2}{\|Q_0\|_2}-1\right|\le r,
\qquad
\left\|\frac{C_T}{\|C_T\|_2}
       +\frac{Q_0}{\|Q_0\|_2}\right\|_2\le2r.          \tag{16}
\]
The second inequality is used only when \(r<1\), so \(C_T\ne0\).
Thus both the magnitude and direction of the complementary packet
must cancel the chosen pole vector. Merely showing large values on
different scales would not contradict (11).

## Costs, prior art, and consequence

Titchmarsh, second edition, Theorems 9.6–9.7, pp. 217–219
([book scan](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf)),
provides the unconditional good-height input; the proof above makes
the extra distance condition explicit. The functional equation and
smoothed Mellin residue method are classical. Section 9.8 already
uses reciprocal-zeta contour sums, and Section 14.27 treats the sharper
unsmoothed Mertens representation under RH. The latter's hypotheses
are not imported here: arbitrary smooth decay in (4) absorbs the fixed
polynomial exponent of (5). Source MC-S67 records these distinct roles.
No new explicit-formula theorem or external priority is claimed.

The bounded comparison with
[[research/prime_lattice/findings/PL-470-positive-source-strip-growth-and-the-infinite-pole-tail-gate|PL-470]]
uses only the local clue's exact-path grant. Its logarithmic-derivative
sum is absolutely convergent with multiplicity residues. That estimate
is not transferred to \(1/\zeta\). Here the finite contour supplies a
small **grouped** tail without bounding inverse derivatives. The new
local consequence is the explicit same-scale cancellation requirement
(15) with all principal parts, together with the unconditional error
budget (9).

- Enlarging the packet while keeping the tests fixed preserves (9),
  but gives no lower singular-value bound for all packet coefficients.
  Rank deficiency is not evidence that the actual arithmetic phase
  vector cancels; equation (15) is a conditional requirement from (11).
- Adapting the test bank to the growing packet changes \(F,K_N\),
  Gram margins, and allowable \(h\). The normalized error is
  \(O((K_2/F)X^{-1/2}+(K_N/F)X^2Y^{B+1-N})\); these ratios cannot
  be treated as fixed without proof. Taking \(N\) to grow with \(X\)
  likewise requires estimates for its seminorms.
- With a fixed packet cutoff, (9) supplies no error small compared
  with \(X^\beta\). The polynomially growing complete packet is
  essential to (1); (1) does not bound the complement of a fixed pair
  separately.
- Neither sparse zero counts nor bounds for \(1/\zeta\) in a known
  zero-free region settle (15). A successful continuation of this
  route must disprove the required cancellation on the measured scales
  using additional arithmetic information. Its possibility remains open.
- At \(\beta=\alpha\), an epsilon-loss ceiling does not force the
  relative error in (15) to vanish. Strict inequality is load-bearing.

Auxiliary exact rational arithmetic checked the coefficient extraction
in (10) in 16 cases of orders 1 through 8, including pure higher
principal parts with zero ordinary residue. It also checked (3) by
independent box-coefficient summation and integration of the centered
step function for all 99 integer pairs \(4\le X\le14,1\le H\le X\),
using the zero-extended mean-zero polynomial
\((u-1)^2(2-u)^2(u-3/2)\). This finite-smoothness polynomial checks
only normalization; it is not substituted for the smooth contour tests.

The theorem is an analytic derivation with an explicit classical source
bridge, not numerical evidence about off-line zeros or an independent
adversarial or formal verification.
