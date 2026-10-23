# MC-522 — Centered dyadic Möbius variance recovers every reciprocal-zeta pole

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CONDITIONAL-TRANSFER`, `NO-NOVELTY-CLAIM`.

## Claim and mathematical delta

Fix \(0<\theta<1\), and define
\[
X_j=2^j,\qquad H_j=\lfloor X_j^\theta\rfloor,\qquad
S_j(y)=M(y+H_j)-M(y),\qquad
m_j=X_j^{-1}\int_{X_j}^{2X_j}S_j(y)\,dy.
\]
Suppose that, for every \(\varepsilon>0\), at every sufficiently large
integer \(j\),
\[
V_j:=\int_{X_j}^{2X_j}|S_j(y)-m_j|^2\,dy
\ll_{\theta,\varepsilon}X_j^{1+\varepsilon}H_j.
\tag{1}
\]
Then, with \(\alpha=1-\theta/2\),
\[
\boxed{\zeta(s)\ne0\quad(\Re s>\alpha),\qquad
M(x)\ll_{\theta,\varepsilon}x^{\alpha+\varepsilon}.}
\tag{2}
\]
At \(s=1\), nonvanishing means the absence of a zero; the pole of zeta
is a removable zero of its reciprocal.

There is no input estimate for the empirical means, for nondyadic scales,
or for any other window lengths. No simplicity, common principal-part
sign, or uniform bound on zero multiplicities is assumed. The hypothesis
(1) remains unproved for Möbius. Thus (2) is a calibration of its strength,
not an unconditional cancellation estimate.

[MC-521](MC-521-smooth-deconvolution-removes-the-variance-zero-free-boundary-loss.md)
obtains this boundary from complete **uncentered**, all-real-scale
moments. The present transfer instead retains an unknown periodic mean
factor. The explicitly authorized source
[PL-466](../../prime_lattice/findings/PL-466-dyadic-seam-weights-remove-the-variance-endpoint-loss.md)
provides the seam-weight mechanism for a prime logarithmic derivative.
Here that construction is reconstructed for signed Möbius coefficients,
and sparse-pole recovery is proved for **all Laurent principal parts**
of \(1/\zeta\). In particular, a zero-residue multiple pole is not lost.
The regime \(\theta>2/3\) in the local clue is included.

## 1. A support-preserving inverse retains the empirical mean exactly

Put \(L=\log2\), \(\tau=2\pi/L\). Choose fixed positive integers \(N,m\)
such that
\[
N(1-\theta)>\theta/2,\qquad 2m>N.
\tag{3}
\]
Define
\[
q_m(t)=(1-\cos(\tau t))^m
=\sum_{\ell=-m}^m d_\ell e^{i\ell\tau t},\qquad
d_\ell=2^{-m}(-1)^\ell\binom{2m}{m+\ell},
\]
and let \(w_s(u)=q_m(\log u)u^{-s}\) on \([1,2]\), extended by zero
outside that interval. The order-\(2m\) endpoint zeros make this extension
\(C^N\), with derivatives through order \(N\) bounded locally uniformly
in \(s\). Write
\[
h=H_j/X_j,\qquad B_hf(u)=h^{-1}\int_0^h f(u-v)\,dv,
\]
\[
c_0=1,\qquad
c_r=-\sum_{k=1}^r\frac{(-1)^k}{(k+1)!}c_{r-k},\qquad
f_{h,s}=\sum_{r=0}^{N-1}c_rh^rw_s^{(r)}.
\tag{4}
\]
For the \(r\)-th summand, expand \(w_s^{(r)}(u-v)\) through degree
\(N-1-r\); the remainder after averaging and multiplying by \(h^r\)
is \(O_K(h^N)\). The recurrence cancels every intermediate degree.
Consequently, on the whole zero-extended real line, uniformly for
\(s\) in any compact set \(K\subset\mathbb C\),
\[
B_hf_{h,s}=w_s+O_K(h^N),\qquad
\|f_{h,s}\|_2\ll_K1,\qquad
\int f_{h,s}=J_m(s):=\int_1^2q_m(\log u)u^{-s}\,du.
\tag{5}
\]
The last identity follows because all positive-order derivative integrals
vanish. The test \(f_{h,s}\) stays supported in \([1,2]\); its box average
may extend to \(2+h\), which is included in the uniform remainder.

Finite interchange, with no absolute-value replacement of Möbius, gives
\[
\sum_n\mu(n)(B_hf_{h,s})(n/X_j)
=\frac1{H_j}\int_{X_j}^{2X_j}S_j(y)f_{h,s}(y/X_j)\,dy.
\tag{6}
\]
There are \(O(X_j)\) relevant integers, including the boundary layers,
and \(|\mu(n)|\le1\). Subtract \(m_j\) only inside this integral and
apply Cauchy–Schwarz. With
\[
W_j(s)=\sum_{X_j<n\le2X_j}\mu(n)q_m(\log(n/X_j))(n/X_j)^{-s},
\qquad b_j=X_jm_j/H_j,
\]
the result is
\[
W_j(s)=b_jJ_m(s)+R_j(s),\qquad
|R_j(s)|\ll_K\frac{\sqrt{X_j}}{H_j}\sqrt{V_j}+X_jh^N
\ll_{K,\theta,\delta}X_j^{\alpha+\delta}
\tag{7}
\]
for every \(\delta>0\). Here (1) is used with a sufficiently small
epsilon, and \(H_j\asymp X_j^\theta\). The remainder exponent in the
second term is strictly below \(\alpha\) by (3). Every \(R_j\) is entire
in \(s\). The elementary bound \(|S_j(y)|\le H_j\) gives only
\(|b_j|\le X_j\); no cancellation of means has been presumed.

## 2. The filtered reciprocal has an exact periodic decomposition

For a fixed starting index \(j_0\), set
\[
F(s)=\sum_{j\ge j_0}b_j2^{-js},\qquad
G(s)=\sum_{j\ge j_0}2^{-js}R_j(s).
\tag{8}
\]
The first series converges on \(\Re s>1\) and obeys
\(F(s+i\tau)=F(s)\). The second is holomorphic on \(\Re s>\alpha\).
Indeed, on a compact subset at distance \(d>0\) from that boundary,
choose \(\delta<d\) in (7); the tail is dominated by a geometric series
\(\sum_j2^{-j(d-\delta)}\). A finite number of exceptional initial
scales causes no problem, even if the starting scale for (1) depends
on epsilon.

Write
\[
D(s)=\frac1{\zeta(s)},\qquad
D_m(s)=\sum_{\ell=-m}^m d_\ell D(s-i\ell\tau).
\]
Initially for \(\Re s>1\), this is precisely the Dirichlet series with
coefficients \(\mu(n)q_m(\log n)\). Periodicity of \(q_m\) and (7) give
\[
\boxed{D_m(s)=Q_m(s)+J_m(s)F(s)+G(s),}
\tag{9}
\]
where \(Q_m(s)=\sum_{n\le2^{j_0}}\mu(n)q_m(\log n)n^{-s}\) is entire.
Seam integers have weight zero, so there is no missing endpoint term.

For \(z=1-s\), direct integration and a rational identity give
\[
J_m(s)=(2^{1-s}-1)\sum_{\ell=-m}^m\frac{d_\ell}{1-s+i\ell\tau}
=(2^{1-s}-1)
\frac{(2m)!\tau^{2m}}
{2^m(1-s)\prod_{r=1}^m((1-s)^2+r^2\tau^2)}.
\tag{10}
\]
To check the identity, put the rational sum over a common denominator.
The order-\(2m\) zero of \(q_m\) makes its numerator constant, by its
expansion at infinity. Its residue at \(z=0\) fixes that constant to
\(d_0(m!)^2\tau^{2m}=(2m)!\tau^{2m}/2^m\).
All apparent poles on \(\Re s=1\) are removable in the integral
definition. In particular,
\[
J_m(s)\ne0\quad(\Re s<1).
\tag{11}
\]

Classical meromorphic continuation of reciprocal zeta now defines
\[
\widetilde F(s)=\frac{D_m(s)-Q_m(s)-G(s)}{J_m(s)}
\quad(\Re s>\alpha).
\tag{12}
\]
This is meromorphic, including at isolated zeros of \(J_m\), and agrees
with \(F\) on the original half-plane. The meromorphic identity theorem
extends its period \(i\tau\) throughout \(\Re s>\alpha\). This step
uses meromorphic continuation, not an assumed zero-free region.

## 3. Zero density makes the periodic mean factor holomorphic

The classical unconditional input is, for each fixed \(\sigma>1/2\),
\[
N_\zeta(\sigma,T):=
\#\{\rho:\zeta(\rho)=0,\ \Re\rho\ge\sigma,\ |\Im\rho|\le T\}
=o(T),
\tag{13}
\]
with multiplicities allowed. For example, the Montgomery bound stated
in Dickinson's introduction, with \(q=1\), is
\(N_\zeta(\sigma,T)\ll T^{3(1-\sigma)/(2-\sigma)}(\log T)^9\)
for \(1/2\le\sigma\le4/5\). Its exponent is below one for
\(\sigma>1/2\); monotonicity handles \(\sigma>4/5\).

If \(\widetilde F\) had a pole at \(\rho=\beta+i\gamma\),
\(\alpha<\beta<1\), periodicity would force poles at every
\(\rho+ik\tau\), \(k\in\mathbb Z\). By (9) and (11), all these
would be poles of \(D_m\). Its poles on that line up to height \(T\)
are contained in the union of \(2m+1\) translates of zeta zeros,
so number at most
\((2m+1)N_\zeta(\beta,T+m\tau)=o(T)\).
A full progression has order \(T\) distinct points, a contradiction.
Thus \(\widetilde F\), and hence \(D_m\), is holomorphic on
\(\alpha<\Re s<1\). No residue-sign statement is used.

## 4. Recover every principal part, without a multiplicity bound

Fix any \(\rho=\beta+i\gamma\) in that strip. In the common local
coordinate \(z=s-(\rho+ik\tau)\), let
\[
P_k(z)=\operatorname{pp}_{z=0}D(\rho+ik\tau+z)
\in z^{-1}\mathbb C[z^{-1}].
\]
Each principal part is finite, but their degrees need not be bounded
as \(k\) varies. Holomorphy of \(D_m\) gives the exact vector-space
recurrence
\[
\sum_{\ell=-m}^m d_\ell P_{k-\ell}=0\quad(k\in\mathbb Z).
\tag{14}
\]
For every fixed \(r\ge1\), define \(a_{k,r}\) to be the coefficient
of \(z^{-r}\) in \(P_k\), with zero when that term is absent. Extracting
this coefficient involves only the finite sum in (14). The symbol is
\[
\sum_{\ell=-m}^m d_\ell u^\ell
=\frac{(-1)^m}{2^m}u^{-m}(u-1)^{2m}.
\tag{15}
\]
Consequently \(k\mapsto a_{k,r}\) has vanishing \(2m\)-th finite
difference, so is a polynomial in \(k\) of degree at most \(2m-1\).
This elementary two-sided recurrence classification follows by
successive summation in the binomial-polynomial basis.

But (13) gives
\[
\#\{|k|\le K:a_{k,r}\ne0\}
\le\#\{|k|\le K:P_k\ne0\}=o(K).
\tag{16}
\]
A nonzero polynomial vanishes at only finitely many integers. Hence
\(a_{k,r}=0\) for every \(k\), for this fixed \(r\). Repeating the
argument for each positive integer \(r\) proves \(P_k=0\) for all
\(k\). There is no interchange of infinite Laurent sums or selection
of a largest multiplicity along the progression.

Equivalently, (13) supplies a run of \(2m\) consecutive zero principal
parts: otherwise every disjoint block of that length would contain a
pole, contradicting sparse support. Since \(d_{-m}\) and \(d_m\) are
nonzero, (14) propagates that zero block in both directions in the
vector space of finite principal parts. This gives the same conclusion
without bounding their degrees or their coefficients.

Every zero of zeta gives a nonzero principal part of its exact
reciprocal, even if the residue vanishes. Thus there are no zeta zeros
in the strip. Classical nonvanishing on \(\Re s=1\) and the Euler
product to its right complete the first part of (2).
The fixed-half-plane Littlewood–Titchmarsh argument explicitly proved
in MC-521, Section 4, then supplies the Mertens bound. That last step
uses zeta's growth and Euler-product structure; it is not a general
sharp-cutoff theorem from holomorphy of arbitrary Dirichlet series.

## 5. The positive dyadic control fails precisely at pole sparsity

Retain the PL-466 control. For \(2/3<\theta<1\), choose
\[
1-\theta/2<\beta<3/2-\theta,\qquad 0<c<1/4,
\]
and put \(d\nu(x)=c_j\,dx\) on \([2^j,2^{j+1})\), \(j\ge0\), with
\(c_j=1/4-c2^{j(\beta-1)}\). This is a bounded positive density.
For \(X=2^j\), \(H=\lfloor X^\theta\rfloor<X\), the window mass is
\(Hc_j\) until the terminal ramp of length \(H\), where it increases
by \(\Delta_jt\), \(0\le t\le H\), \(\Delta_j=c_{j+1}-c_j\).
Subtracting its own empirical mean gives exactly
\[
V_j^\nu=\Delta_j^2\left(\frac{H^3}{3}-\frac{H^4}{4X}\right),
\qquad \frac{V_j^\nu}{XH}\ll X^{2\beta+2\theta-3}=o(1).
\tag{17}
\]
Nevertheless, initially for \(\Re s>1\), its Mellin transform is
\[
\int_1^\infty x^{-s}\,d\nu(x)
=\frac1{4(s-1)}
-\frac{c(2^{1-s}-1)}{(1-s)(1-2^{\beta-s})}.
\tag{18}
\]
It has a pole at every \(\beta+ik\tau\); neither numerator nor
\(1-s\) vanishes there. The weighted perturbation is
\(-cJ_m(s)/(1-2^{\beta-s})\), so the seam filter does not erase this
progression. This control meets the variance ceiling but violates
(13), exactly where the arithmetic proof excludes the mean factor's
poles. It is a continuous-source control, not a Möbius sequence or a
counterexample to (2). Positivity and centered variance alone therefore
cannot justify the generic analytic conclusion.

## Prior art, audit and consequences

The source dictionary is explicit: PL-466's prime coefficients are
replaced by \(\mu(n)\), its empirical mean by \(m_j\), and its
logarithmic derivative by the exact reciprocal \(D=1/\zeta\).
Sections 1–3 retain only bounded coefficients, meromorphic continuation,
and sparse pole locations. Section 4 replaces its simple-residue
argument by the full principal-part recurrence. The seam weights,
finite differential inversion and periodic decomposition are credited
to that source; they are not claimed as newly discovered here.

The zero-density input is classical: see [George Dickinson, *Zeros of
Dirichlet L-functions near the critical line*, arXiv:2211.06264v1,
Introduction, p. 1](https://arxiv.org/pdf/2211.06264v1), which states
Montgomery's theorem also for \(q=1\). [Greg Martin and Nathan Ng,
*Nonzero values of Dirichlet L-functions in vertical arithmetic
progressions*, arXiv:1109.1788v2, Introduction,
pp. 1–2](https://arxiv.org/pdf/1109.1788) explicitly discuss
off-critical progression sparsity as a zero-density consequence.
Neither fact alone excludes an isolated off-critical zero; here the
variance forces periodicity and then the recurrence.

[Zaccagnini, *The Selberg integral and a new pair-correlation function
for the zeros of the Riemann zeta-function*, Section 3.3](https://arxiv.org/pdf/1603.02952)
records classical variance-to-zero-location converses for prime counts.
Its prescribed main term and scale-sized multiplicative window differ
from the empirical mean and one sublinear additive length here.
The local-to-global topic and elementary finite-difference algebra are
classical. Targeted checks of centered Möbius moments, Selberg-integral
converses and vertical progressions did not locate this exact transfer;
that does not establish external novelty. The durable delta is the
proved destination transfer, including arbitrary multiple poles.

Exact rational-arithmetic checks verified the inverse coefficient
cancellations for \(N=1,\ldots,24\), the rational multiplier and
finite-difference identities for \(m=1,\ldots,12\), and the centered
ramp formula (17). The arguments above prove the general identities
and analytic convergence. These checks are auxiliary, not numerical
evidence for (1), independent adversarial approval, or Lean validation.

The evidence boundaries are:

- Every sufficiently large dyadic block and the **complete** integral
  over its starts are required. An arbitrary subsequence or an
  almost-all-start bound with unpaid exceptions does not supply (1).
- The fixed restriction \(\theta<1\) permits (3). No moving-exponent
  limit, uniformity in \(\theta\), boundary-line exclusion, or
  epsilon-free Mertens bound is asserted.
- A sequence of fixed \(\theta_\nu\uparrow1\), each satisfying (1)
  with its own constants, would imply RH. Conversely,
  [MC-520](MC-520-rh-mellin-variance-closes-conditional-farey-window-target.md)
  proves the uncentered bound under RH, and subtracting the empirical
  mean only decreases that moment. This equivalence of the whole
  family is a difficulty calibration, not a proof of its premise.
- The proof does not transfer to generic positive, random, or
  generalized-prime sources without their own sparse-pole theorem.
  It does not assume that Möbius behaves like independent signs.

Empirical centering and dyadic-only scale coverage do not, for this
complete moment and this arithmetic source, remove the zero-location
burden. The unresolved arithmetic task is still to prove a useful
moment bound without importing the zero-free consequence it entails.
