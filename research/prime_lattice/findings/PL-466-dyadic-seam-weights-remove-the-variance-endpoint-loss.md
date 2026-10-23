# PL-466 — Weights vanishing at dyadic seams remove the variance endpoint loss

**Evidence/status:** EXACT-DERIVED + CLASSICAL ZERO-DENSITY INPUT; CONDITIONAL ZERO-FREE TRANSFER; NO EXTERNAL NOVELTY CLAIM.

**Local dependencies:** PL-464 (the dyadic hypothesis and its sharp-block loss), PL-465 (finite differential inversion of a box average).

## Claim

Fix \(0<\theta<1\), a finite \(A\ge0\), and
\[
X_j=2^j,\qquad H_j=\lfloor X_j^\theta\rfloor,\qquad
a_n=\Lambda(n)\mathbf1_{n\equiv1\ (5)},
\]
\[
P_j(y)=\sum_{y<n\le y+H_j}a_n,\qquad
\mu_j=X_j^{-1}\int_{X_j}^{2X_j}P_j(y)\,dy.
\]
Assume the **unproved** bound
\[
V_j:=\int_{X_j}^{2X_j}|P_j(y)-\mu_j|^2\,dy
\ll_{\theta,A}X_jH_j(\log(2X_j))^A
\tag{1}
\]
at every sufficiently large integer \(j\). Then
\[
\boxed{L(s,\chi)\ne0\quad
\text{for }\Re s>\alpha:=1-\theta/2,
\quad\chi\bmod5.}
\tag{2}
\]
There is no assumption on the empirical means, on other scale parameters,
or on other window lengths. In particular, (2) improves PL-464's boundary
\(\max(1-\theta/2,\theta)\) when \(\theta>2/3\).
If (1) holds separately for fixed exponents \(\theta_\nu\uparrow1\), it
implies joint GRH modulo 5. Constants and starting scales may depend on
\(\nu\); no uniform limit in \(\theta\) is used.

The additional arithmetic tool, beyond PL-464's residue-phase argument,
is the classical unconditional fact that zeros in any fixed half-plane
\(\Re s\ge\sigma>1/2\) have count \(o(T)\) up to height \(T\).
The proof does not turn this density theorem alone into zero exclusion.
The variance hypothesis forces a finite-difference law along an entire
vertical progression; sublinear zero density then excludes every nonzero
solution of that law. No variance estimate or unconditional improvement
in zero location is proved here.

## 1. A finite Fourier weight that vanishes at every seam

Put \(L=\log2\), \(\tau=2\pi/L\). Choose integers \(N,m\ge1\) with
\[
N(1-\theta)>\theta/2,\qquad 2m>N.
\tag{3}
\]
Both remain fixed as \(j\to\infty\). Define
\[
q_m(t)=(1-\cos(\tau t))^m
=\sum_{\ell=-m}^m d_\ell e^{i\ell\tau t},
\qquad
d_\ell=2^{-m}(-1)^\ell\binom{2m}{m+\ell}.
\tag{4}
\]
The zeros at \(t\in L\mathbb Z\) have order \(2m\). For complex \(s\),
let \(w_s(u)=q_m(\log u)u^{-s}\) on \([1,2]\), extended by zero outside
that interval. It is globally \(C^N\), supported in \([1,2]\), and its
derivatives through order \(N\) are bounded locally uniformly in \(s\).
Thus no fixed-width gap is discarded around a seam.

For \(h=H_j/X_j\), use the finite differential inverse
\[
c_0=1,\qquad
c_r=-\sum_{k=1}^r\frac{(-1)^k}{(k+1)!}c_{r-k},\qquad
f_{h,s}=\sum_{r=0}^{N-1}c_rh^rw_s^{(r)}.
\tag{5}
\]
With \(B_hf(u)=h^{-1}\int_0^h f(u-v)\,dv\), finite Taylor expansion
on the zero-extended real line gives
\[
B_hf_{h,s}=w_s+O_K(h^N),\qquad
\|f_{h,s}\|_2\ll_K1,\qquad
\int_{\mathbb R}f_{h,s}=J_m(s):=\int_1^2q_m(\log u)u^{-s}\,du,
\tag{6}
\]
uniformly for \(s\) in any compact set \(K\). The coefficients in (5)
cancel the Taylor terms of degrees \(1,\ldots,N-1\). All positive-order
derivative integrals vanish because the endpoint jets vanish. Unlike a
polynomial in translations of the box operator, (5) keeps the test's
support inside the available base-point interval.

Exact finite interchange gives
\[
\sum_n a_n(B_hf_{h,s})(n/X_j)
=\frac1{H_j}\int_{X_j}^{2X_j}f_{h,s}(y/X_j)P_j(y)\,dy.
\tag{7}
\]
The box-averaged test can extend to \(2+h\); the uniform remainder in
(6) includes this upper layer and the lower layer. There are \(O(X_j)\)
relevant integers and \(a_n\le\log(3X_j)\). Subtracting the empirical
mean only inside the integral, Cauchy--Schwarz and (1) yield
\[
\begin{aligned}
W_j(s)&:=\sum_{X_j<n\le2X_j}
 a_nq_m(\log(n/X_j))(n/X_j)^{-s}\\
&=b_jJ_m(s)+R_j(s),\qquad b_j=\frac{X_j\mu_j}{H_j},\\
|R_j(s)|&\ll_K
\frac{\sqrt{X_j}}{H_j}\sqrt{V_j}
+X_j(H_j/X_j)^N\log(3X_j)\\
&\ll_{K,\theta,A}X_j^\alpha(\log(2X_j))^B,
\qquad B=\max(A/2,1).
\end{aligned}
\tag{8}
\]
Each \(R_j\) is entire in \(s\). Equation (3) makes the Taylor remainder
strictly smaller in power than \(X_j^\alpha\).
The only mean bound used is the elementary \(b_j\ll X_j\log(3X_j)\),
which ensures initial absolute convergence. The mean is never replaced
by its expected prime density.

## 2. Exact Mellin decomposition with a periodic mean factor

Let \(j_0\) be an integer after which (1) holds, and set
\[
F(s)=\sum_{j\ge j_0}b_j2^{-js},\qquad
G(s)=\sum_{j\ge j_0}2^{-js}R_j(s).
\tag{9}
\]
The first series converges absolutely for \(\Re s>1\) and satisfies
\(F(s+i\tau)=F(s)\). The second is holomorphic on \(\Re s>\alpha\),
by locally uniform normal convergence using (8).

Define the original and filtered Dirichlet series by
\[
D(s)=\sum_n a_nn^{-s}
=\frac14\sum_{\chi\bmod5}-\frac{L'}L(s,\chi),
\qquad
D_m(s)=\sum_{\ell=-m}^m d_\ell D(s-i\ell\tau).
\tag{10}
\]
In \(\Re s>1\), the latter equals \(\sum_n a_nq_m(\log n)n^{-s}\).
Since \(q_m(\log(n/X_j))=q_m(\log n)\), summing (8) gives the exact
replacement for the sharp-block decomposition:
\[
\boxed{D_m(s)=Q_m(s)+J_m(s)F(s)+G(s).}
\tag{11}
\]
Here \(Q_m(s)=\sum_{n\le2^{j_0}}a_nq_m(\log n)n^{-s}\) is entire.
Seam integers contribute zero to the weighted sum, so there is neither
double counting nor an omitted endpoint correction in (11).
Information potentially hidden at those seams is handled by the
finite-difference argument below, not declared negligible.

The multiplier has an explicit nonvanishing law. Writing \(z=1-s\),
\[
\begin{aligned}
J_m(s)
&=(2^{1-s}-1)\sum_{\ell=-m}^m\frac{d_\ell}{1-s+i\ell\tau}\\
&=(2^{1-s}-1)
\frac{(2m)!\,\tau^{2m}}
{2^m(1-s)\prod_{r=1}^m((1-s)^2+r^2\tau^2)}.
\end{aligned}
\tag{12}
\]
Apparent singularities on \(\Re s=1\) are removable in the integral
definition. To verify the rational identity, put the sum over a common
denominator. The order-\(2m\) zero in (4) makes the numerator constant;
its value follows from the residue at \(z=0\), namely
\(d_0(m!)^2\tau^{2m}=(2m)!\tau^{2m}/2^m\).
In particular,
\[
J_m(s)\ne0\quad(\Re s<1).
\tag{13}
\]

Classical meromorphic continuation of (10) therefore gives the
meromorphic continuation
\[
\widetilde F(s)=\frac{D_m(s)-Q_m(s)-G(s)}{J_m(s)}
\quad(\Re s>\alpha).
\tag{14}
\]
It agrees with \(F\) in its initial domain; the meromorphic identity
theorem extends \(\widetilde F(s+i\tau)=\widetilde F(s)\) to this
whole half-plane. No bound uniform in vertical height is needed.

## 3. Arithmetic zero density excludes poles of the mean factor

For every fixed \(\sigma>1/2\), classical Dirichlet zero-density
estimates give
\[
\mathcal N_5(\sigma,T):=
\sum_{\chi\bmod5}\#\{\rho:L(\rho,\chi)=0,
\ \sigma\le\Re\rho<1,\ |\Im\rho|\le T\}=o(T).
\tag{15}
\]
Zeros are counted with multiplicity. For example, Montgomery's bound,
as stated in Dickinson's introduction (source 128), is
\(\sum_{\chi\bmod q}N(\sigma,T,\chi)
\ll(qT)^{3(1-\sigma)/(2-\sigma)}(\log(qT))^9\)
for \(1/2\le\sigma\le4/5\). At fixed \(q=5\) the exponent is strictly
less than one when \(\sigma>1/2\); for larger \(\sigma\), use
monotonicity at \(4/5\). The principal factor's extra Euler-factor
zeros are on \(\Re s=0\) and are irrelevant.

Suppose \(\widetilde F\) had a pole at \(\rho=\beta+i\gamma\), with
\(\alpha<\beta<1\). Periodicity gives a pole at every
\(\rho+ik\tau\), \(k\in\mathbb Z\). By (13), (11) makes all of these
poles of \(D_m\). But \(D_m\) is a finite sum of translates of \(D\).
Each pole on this line must come from a mod-5 zero on the same line,
shifted by one of \(2m+1\) fixed heights. Thus its number up to height
\(T\) is at most
\((2m+1)\mathcal N_5(\beta,T+m\tau)=o(T)\).
A complete vertical progression has order \(T\) distinct points.
This contradiction proves
\[
\widetilde F\text{ and }D_m\text{ are holomorphic on }
\alpha<\Re s<1.
\tag{16}
\]

The line \(\Re s=1\) is deliberately excluded from this argument.
The principal pole and its finitely many translates in \(D_m\) are
consistent with (11): \(J_m(1+ik\tau)=L d_k\) for \(|k|\le m\), and
is zero for other integer \(k\).

## 4. The filter cannot hide a sparse arithmetic pole sequence

Fix any \(\rho=\beta+i\gamma\) with \(\alpha<\beta<1\), and define
\[
r_k=\operatorname{Res}_{s=\rho+ik\tau}D(s),
\qquad r_k=0\text{ if }D\text{ is holomorphic there}.
\]
All poles of \(D\) in this strip are simple, with residues
\[
r_k=-\frac14\sum_{\chi\bmod5}m_\chi(\rho+ik\tau).
\tag{17}
\]
In particular, a zero of any of the four factors cannot cancel in
\(D\). Holomorphy in (16) gives, at every integer \(k\),
\[
\sum_{\ell=-m}^m d_\ell r_{k-\ell}=0.
\tag{18}
\]
The Laurent symbol is
\[
\sum_{\ell=-m}^m d_\ell u^\ell
=\frac{(-1)^m}{2^m}u^{-m}(u-1)^{2m}.
\tag{19}
\]
Hence (18) is the vanishing of the order-\(2m\) finite difference,
up to a nonzero scalar and an invertible shift. Its two-sided solutions
are polynomials in \(k\) of degree at most \(2m-1\), as follows by
successive discrete integration in the binomial-polynomial basis.
A nonzero polynomial is nonzero at all but finitely many integers.
On the other hand, (15) implies
\[
\#\{|k|\le K:r_k\ne0\}=o(K).
\tag{20}
\]
Consequently \(r_k=0\) for all \(k\). Since the starting point was
arbitrary, (17) excludes every mod-5 zero in this strip. Classical
nonvanishing on \(\Re s=1\) and the Euler product to its right complete
(2). No rightmost zero, simple-zero assumption, or infinite explicit
zero sum was introduced.

This supplies an exact recovery of pole information from the weighted
decomposition. It does not reconstruct the sharp block masses or prove
that two adjacent empirical means are close. Their different window
lengths remain exactly those in (1).

## 5. The positive dyadic control still survives

PL-464's nonarithmetic control extends to the newly relevant regime.
Fix \(2/3<\theta<1\), choose
\[
1-\theta/2<\beta<3/2-\theta<1,
\]
and let \(d\nu(x)=c_j\,dx\) on \([2^j,2^{j+1})\), where
\(c_j=1/4-c2^{j(\beta-1)}\), \(0<c<1/4\).
For \(X=2^j\), \(H=\lfloor X^\theta\rfloor<X\), put
\(\Delta_j=c_{j+1}-c_j\). The window mass differs from \(Hc_j\)
only in its terminal ramp of length \(H\). Direct integration with
its own empirical mean gives exactly
\[
V_j^\nu=\Delta_j^2\left(\frac{H^3}{3}-\frac{H^4}{4X}\right),
\qquad
\frac{V_j^\nu}{XH}\ll X^{2\beta+2\theta-3}=o(1).
\tag{21}
\]
Yet its Mellin transform is
\[
\int_1^\infty x^{-s}\,d\nu(x)
=\frac1{4(s-1)}-
\frac{c(2^{1-s}-1)}{(1-s)(1-2^{\beta-s})}.
\tag{22}
\]
There is a pole at every \(\beta+ik\tau\). Their nonreal residue
ratios are those already identified in PL-464. They also violate
(15): the pole set has linear height density. Multiplication of the
source by \(q_m(\log x)\) retains the term
\(-cJ_m(s)/(1-2^{\beta-s})\), so this control is not excluded by
(8)--(14). It fails precisely at the arithmetic sparsity step.
At \(\theta=1/2\), the original \(3/4<\beta<1\) control satisfies
the same variance calculation and likewise survives.

Thus positivity and small dyadic empirical variance are insufficient
in the generic positive-source class. The proof uses actual arithmetic
information twice: the sublinear zero count and the noncancelling
identity-residue formula (17). It assumes neither for Helson twists
or generalized-prime replacements without a separate proof.

## Prior art, audit and consequence

Finite box-average Taylor inversion is the classical local tool already
derived in PL-465. The authorized MC-521 comparison supplies the finite
deconvolution perspective, but its all-real-scale Mellin integral is not
used here. Geometric Mellin periodicity is classical (source 124).
Variance-to-zero implications are classical (source 123, Section 3.3).
Sources 128--129 supply the arithmetic zero-density and vertical-
progression comparison. In particular, Martin--Ng explicitly explain
that off-critical vertical progressions have almost all entries nonzero
by zero density; this is prior art, not the discovery claimed here.

The derived contribution is the composition of the seam-vanishing
finite Fourier weight, the exact periodic mean decomposition (11), and
the sparse finite-difference recovery (18)--(20), for this empirically
centered dyadic hypothesis. Targeted checks of Selberg-integral
converses, geometric Mellin analysis, approximate deconvolution, and
zeros on vertical progressions did not identify this exact implication.
That search does not establish external novelty. PL-464 remains a
valid alternative proof with a weaker boundary that needs no
zero-density theorem.

The main audit points are zero-extension regularity in (6), inclusion
of both box boundary layers in (8), nonvanishing of (12) on the open
strip, continuation of periodicity, and the necessity of recovering
\(D\) from \(D_m\) rather than stopping at filtered holomorphy.
Exact rational arithmetic checks verified (12) and (19) for
\(m=1,\ldots,12\), and the inverse coefficient cancellation for
\(N=1,\ldots,24\); the general identities and analytic implications
are proved above. These checks are auxiliary, not a numerical proof
or Lean formalization.

The full base-point integral at every sufficiently large dyadic scale,
a fixed exponent strictly below one, and a finite logarithmic loss
remain required. An arbitrary subsequence, isolated windows, or a
single value of \(\theta\) approaching one with \(X\) is not covered.
There is no conclusion on zeros at \(\Re s=\alpha\), no converse from
GRH to (1) proved here, and no covariance or relative-frame estimate.
The result removes the sharp-block endpoint loss from the analytic
implication; it leaves the actual-prime variance premise unproved.
