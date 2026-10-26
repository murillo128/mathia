# ANF-205 — An upward central cusp prevents finite notch attainment

**Status:** EXACT-DERIVED + COMPLEX-MULTISET + CENTRAL-CUSP-OBSTRUCTION + TRIANGULAR-NOTCH + NONATTAINMENT. A finite configuration stable against all sufficiently distant duplicates forces its continuous spectral weight to have an upper quadratic bound at the origin. A triangular notch violates this condition once its amplitude reverses the Montgomery--Taylor central cusp. Above that explicit threshold, every finite conjugation-invariant multiset can be improved in every sufficiently distant dyadic translation window, and every sequence approaching the unrestricted floor has cardinality tending to infinity. The profile still has a nonnegative inverse-square Fourier tail. Thus ANF-204's necessary tail condition is not sufficient for attainment at a prescribed amplitude. The threshold below is an obstruction threshold, not a proved sharp transition; small-amplitude complex sufficiency and the unrestricted exposure envelope remain open.

## Object and amplitude obstruction

Use \(\widehat f(x)=\int f(u)e^{-2\pi iux}\,du\), and put
\[
\theta=1/\sqrt2,\qquad
g(u)=\frac{\cos(\sqrt2u)}{\sqrt2\sin\theta}
\mathbf1_{[-1/2,1/2]}(u),\qquad J_0=g*g,
\qquad d=\frac12\cot^2\theta>0.
\tag{1}
\]
Fix \(0<\eta<1\) and \(b>0\) with
\[
\phi(u)=b(1-|u|/\eta)_+\le J_0(u),\qquad
\Phi(x)=\widehat\phi(x)=b\eta\operatorname{sinc}^2(\eta x),
\qquad \operatorname{sinc}(x)=\frac{\sin\pi x}{\pi x}.
\tag{2}
\]
In particular \(\Phi\ge0\) and
\(\sup_x(1+x^2)\Phi(x)<\infty\). Freeze this profile before varying
\(t\), and write \(J_t=J_0-t\phi\), \(0<t<1\).

For a nonempty finite multiset \(W=\overline W\), count all entries
with their positive integer multiplicities and define
\[
N=|W|,\quad L(W)=2N-\sigma(W),\quad
S_W(u)=\sum_{z\in W}e^{-2\pi iuz},\quad P_W(u)=|S_W(u)|^2,
\]
\[
E_f(W)=\int f(u)P_W(u)\,du,\qquad Q_t(W)=E_{J_t}(W)/L(W),
\]
\[
q_m(t)=\inf_{\substack{W=\overline W\\1\le|W|\le m}}Q_t(W),
\qquad q_\infty(t)=\inf_{W=\overline W,\ 0<|W|<\infty}Q_t(W).
\tag{3}
\]
Here \(\sigma\) counts distinct simple **real** sites. Lamzouri's
inequality and domination give \(Q_t(W)\ge1-t>0\).

Set
\[
t_c=\frac{d\eta}{b},\qquad \delta=\frac{tb}{\eta}-d.
\tag{4}
\]
If \(t_c<t<1\), then for every fixed \(W\) and every sufficiently
large \(X\) there is \(R\in[X,2X]\), exceeding the horizontal
diameter of \(W\), such that
\[
\boxed{
Q_t(W\cup(W+R))-Q_t(W)
\le-\frac{\delta N^2}{16\pi^2L(W)X^2}<0.
}
\tag{5}
\]
The onset in \(X\) depends on the entire configuration and the fixed
profile and amplitude. Consequently no finite configuration attains
\(q_\infty(t)\), while for every \(m\ge1\)
\[
\boxed{1-t\le q_\infty(t)<q_{2m}(t)<q_m(t).}
\tag{6}
\]
Every sequence approaching \(q_\infty(t)\) therefore has cardinality
tending to infinity. These assertions also hold when all infima and
configurations are restricted to real multisets.

## Eventual Fourier positivity permits only a quadratic upward departure

The elementary Fourier fact needed here is broader than a triangular
notch. Let \(f\) be a real even continuous compactly supported function,
and let \(H=\widehat f\). If \(H(x)\ge0\) for \(|x|\ge A\), then
\[
\boxed{
H\in L^1(\mathbb R),\qquad
f(u)-f(0)\le C_f u^2\quad(u\in\mathbb R),
\quad C_f=2\pi^2\int_{-A}^A x^2H_-(x)\,dx<\infty,
}
\tag{7}
\]
where \(H_-=\max(-H,0)\). No pointwise positivity of \(H\) inside
\([-A,A]\) is required.

To justify integrability before using inversion, Gaussian regularization
and Fubini give
\[
\int H(x)e^{-\pi\varepsilon x^2}\,dx
=\int f(u)\varepsilon^{-1/2}e^{-\pi u^2/\varepsilon}\,du
\longrightarrow f(0)\qquad(\varepsilon\downarrow0).
\tag{8}
\]
The compact part of the left side converges by boundedness of \(H\).
On its complement the integrand is nonnegative and increases as
\(\varepsilon\downarrow0\). Monotone convergence therefore makes
the tail integrable, so Fourier inversion is legitimate. Evenness yields
\[
f(u)-f(0)=\int H(x)\{\cos(2\pi xu)-1\}\,dx
\le\int_{-A}^A H_-(x)\{1-\cos(2\pi xu)\}\,dx
\le C_f u^2.
\tag{9}
\]
This is a classical positivity/inversion argument, not a claim of a
new general Fourier theorem.

Now take any real even continuous compactly supported spectrum \(J\)
and a fixed nonempty conjugation-invariant \(W\). Conjugation gives
\(S_W(-u)=\overline{S_W(u)}\), so \(P_W\) is even and real analytic
on the real axis, with
\[
P_W(0)=N^2>0,\qquad P_W(u)=N^2+O_W(u^2).
\tag{10}
\]
For \(R>\operatorname{diam}(\Re W)\), disjointness of the real
projections preserves multiplicity types and gives exactly
\[
L(W\cup(W+R))=2L(W),\qquad
\frac{E_J(W\cup(W+R))}{L(W\cup(W+R))}
-\frac{E_J(W)}{L(W)}
=\frac{\widehat{JP_W}(R)}{L(W)}.
\tag{11}
\]
Thus stability against every sufficiently distant duplicate makes
\(\widehat{JP_W}\) eventually nonnegative on both tails. Applying
(7) to \(f=JP_W\), and using boundedness of \(J\) and (10), proves
the necessary local condition
\[
\boxed{J(u)\le J(0)+C_{J,W}u^2\quad\hbox{near }0.}
\tag{12}
\]
In particular, if
\(\limsup_{u\to0}(J(u)-J(0))/u^2=+\infty\), every finite
configuration has strictly improving duplicates at arbitrarily large
translations. This does not assume a Fourier sign for a notch profile,
nor any prescribed tail decay. A mere smooth local minimum with a
finite positive quadratic coefficient does not violate (12).

## The actual triangular notch reverses the central cusp

The source formula already derived in ANF-121 is
\[
J_0(u)=
\frac{(1-u)\cos(\sqrt2u)+\sin(\sqrt2(1-u))/\sqrt2}
{4\sin^2\theta}\qquad(0\le u\le1).
\tag{13}
\]
It gives \(J_0'(0+)=-d\), and hence
\[
J_t(u)=J_t(0)+\delta|u|+O(u^2)\qquad(u\to0).
\tag{14}
\]
When \(\delta>0\), (12) is impossible. This already proves
nonattainment and arbitrarily distant improvement. In particular,
finite attainment for this fixed notch at any \(0<t<1\) requires
\(t\le t_c\). If \(t_c\ge1\), this necessary condition is vacuous
throughout the amplitude range considered here.

The obstruction occurs for admissible profiles. For example,
\(\eta=1/20\), \(b=1/10\) satisfy (2): on its support
\(g\ge3/4\), by \(\cos\theta\ge1-\theta^2/2=3/4\) and
\(\sqrt2\sin\theta\le1\). Thus
\(J_0(u)\ge(9/16)(1-|u|)\), which exceeds \(b\) throughout
\([-\eta,\eta]\). Since \(\tan\theta>\theta\), \(d<1\) and
\(t_c=d/2<1/2\). In particular \(t=3/4\) lies strictly in the
nonattaining regime, despite the inverse-square profile tail.

More generally, keep \(b=1/10\) and shrink \(\eta\). Domination
holds for every \(0<\eta\le1/2\), and \(t_c=10d\eta\to0\).
This varies the profile; it does **not** give a single triangular
profile failing attainment at arbitrarily small positive amplitudes.
For each fixed profile, ANF-200 still supplies a positive initial
interval of attained real two-site minima. The present obstruction
places an upper bound on any such interval.

## The full source gives a quantitative translation-window witness

For fixed \(W\), let \(H_W=\widehat{J_tP_W}\). The zero extension
of \(J_tP_W\) is continuous and piecewise smooth. Its second
distributional derivative has an \(L^1\) remainder plus atoms at
\(0,\pm\eta,\pm1\). Their coefficients are respectively
\[
2\delta N^2,\qquad
-\frac{tb}{\eta}P_W(\eta)\ \text{at each of }\pm\eta,\qquad
dP_W(1)\ \text{at each of }\pm1.
\tag{15}
\]
Here \(J_0'(1-)=-d\); the source derivative has no jump, and
\(P_W'(0)=0\). Fourier differentiation and Riemann--Lebesgue applied
to the \(L^1\) remainder yield
\[
R^2H_W(R)=\frac1{2\pi^2}
\left[-\delta N^2-dP_W(1)\cos(2\pi R)
+\frac{tb}{\eta}P_W(\eta)\cos(2\pi\eta R)\right]+o_W(1).
\tag{16}
\]
All parameters are frozen before \(R\to\infty\). Averaging over a
dyadic window removes both nonconstant cosine terms, whether or not
\(\eta\) is rational:
\[
\boxed{
\lim_{X\to\infty}\frac1X\int_X^{2X}R^2H_W(R)\,dR
=-\frac{\delta N^2}{2\pi^2}.
}
\tag{17}
\]
For \(\delta>0\), every sufficiently large window therefore contains
an \(R\) with \(R^2H_W(R)\le-\delta N^2/(4\pi^2)\).
Use \(R\le2X\) in (11) to obtain (5). Complex pair terms have not
been assigned a sign: the calculation retains the nonnegative whole
source \(P_W\), including all multiplicities and all heights.

ANF-203's fixed-cap existence theorem applies to every dominated even
profile at \(0<t<1\), including (2). It confines height, extracts
horizontally separated limiting clusters and uses the collision
inequality \(L(V_a)\ge L_a\) together with \(q_m\ge1-t>0\).
Duplicate an attaining configuration for \(q_m\) using (5); this
proves \(q_{2m}<q_m\). An attained capped floor cannot equal the
unattained unrestricted floor, giving (6) and cardinality divergence.
Restricting the same cluster argument and duplication to real multisets
gives the asserted real version.

## Prior art, checks and evidence boundary

The base inequality is [Lamzouri, Proposition 2.1](https://arxiv.org/html/2609.02882v2#S2);
the explicit extremizer is [Carneiro--Chandee--Littmann--Milinovich,
Corollary 14](https://arxiv.org/pdf/1406.5462). Only the auxiliary
source inequality and kernel are used, not an RH-conditional
zero-statistics theorem. ANF-121 supplies (13); ANF-200, ANF-202,
ANF-203 and ANF-204 establish the distinct initial real attainment,
capped complex reduction, capped existence and necessary Fourier-tail
boundaries used in the comparison.

Finite pair-energy stability and replication are classical, with
[Procacci, equation (1.3)](https://arxiv.org/pdf/2005.10362) and the
local ANF-018--ANF-019 as prior-art anchors. Eventual-sign constraints
on positive-definite bandlimited functions are also classical:
[Logan (1983), part I](https://doi.org/10.1137/0514022) and
[Gorbachev--Ivanov--Tikhonov (2019), sections 1 and 3](https://arxiv.org/abs/1904.11328)
study sign radii and vanishing moments. Their extremal sign-radius
theorems are not imported here. Gaussian regularization, the cosine
increment bound, derivative-jump asymptotics and averaging are standard
Fourier analysis. The additional local result is their application to
the source-weighted translation interaction: (12), the explicit
triangular amplitude obstruction (4), and its all-complex
nonattainment consequence. Targeted searches of eventual Fourier
positivity, spectral cusps and finite pair-energy attainment did not
identify this exact application; no new general sign-uncertainty
theorem or exhaustive novelty claim is made.

As a noncertifying check, direct complex evaluation of
\(H_W(R)=\sum_{z,w\in W}(F-t\Phi)(R+z-\bar w)\), with
\(F=\widehat J_0=K^2\) from ANF-204, tested (16)--(17) at
\(\eta=1/20,b=1/10,t=3/4\). Composite trapezoidal integration with
step \(1/32\) used windows \([X,2X]\), \(X=100,400,1600\), and
five multisets: \(\{0\}\), \(\{0,0\}\), \(\{0,\pm0.3i\}\),
\(\{0,1.2,2.1\pm0.2i\}\), and two copies of
\(\{0.1\pm0.12i\}\). At \(X=1600\), the largest absolute
error in the averaged limit was below \(9.1\cdot10^{-8}\), and
each window in every case contained a negative interaction. These
finite floating-point checks do not certify any sign at infinity or
an unrestricted infimum; (7)--(17) supply the proof. No Lean proof is
claimed.

The audit points are the sign of the central derivative, the factor
\(N^2\) at the origin, integrability before Fourier inversion, both
endpoint jumps in (15), and denominator additivity only for disjoint
copies. The equality case \(t=t_c\) and the region \(t<t_c\) are
not decided by this argument. Neither the onset in (5) nor the capped
gaps in (6) is uniform in growing geometry. The Fourier tail remains
a necessary condition, not an amplitude-independent sufficiency test.

Finally, nonattainment does not imply that the positive global floor
is too low for an affine zero-counting certificate. This finding
neither evaluates that floor nor bounds the initial exposure derivative
from ANF-099. It supplies no improved critical-line proportion,
zero-density estimate or RH conclusion.
