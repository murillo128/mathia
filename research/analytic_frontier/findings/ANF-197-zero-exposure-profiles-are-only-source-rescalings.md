# ANF-197 — Zero-exposure profiles are only source rescalings

**Status:** EXACT-DERIVED + ZERO-SET-RIGIDITY + CLASSICAL-ENTIRE-FUNCTION-METHOD + DEGENERATE-PROFILE-CLOSURE. The case `M_phi=0` excluded from the paired-source argument in ANF-195 contains no new spectral direction. Within the dominated positive-Fourier profile class it consists exactly of scalar multiples of the Montgomery--Taylor spectrum. This is an exact profile classification, not a quantitative claim about profiles with small positive `M_phi`.

## Statement and consequence

Use the Fourier convention
\(\widehat f(t)=\int_{\mathbb R}f(u)e^{-2\pi iut}\,du\), and set
\[
\theta=1/\sqrt2,\qquad
g(u)=\frac{\cos(\sqrt2u)}{\sqrt2\sin\theta}
\mathbf1_{[-1/2,1/2]}(u),\qquad J_0=g*g,
\]
\[
K(z)=\widehat g(z)
=\frac{\cos(\pi z)-az\sin(\pi z)}{1-2\pi^2z^2},
\qquad a=\sqrt2\pi\cot\theta>0.
\tag{1}
\]
The quotient is continued at its two removable points; \(K(0)=1\) and
\(\widehat J_0=K^2\). Write \(r_n\in(n,n+1/2)\), \(n\ge1\), for
the positive source zeros from ANF-087.

Let \(\phi\in L^1(\mathbb R)\) be real and even, supported in
\([-1,1]\), and suppose \(\Phi=\widehat\phi\ge0\) on the real line.
Then
\[
\boxed{\quad
\Phi(r_n)=0\ \text{for every }n\ge1
\quad\Longleftrightarrow\quad
\phi=cJ_0\ \text{almost everywhere, for some }c\ge0.
\quad}
\tag{2}
\]
In particular, under ANF-195's additional domination \(0\le\phi\le J_0\),
\[
M_\phi:=\max_{n\ge1}\Phi(r_n)=0
\quad\Longleftrightarrow\quad \phi=cJ_0,\qquad 0\le c\le1.
\tag{3}
\]
No Sobolev regularity or presumed real-zero classification of the entire
kernel is hidden in this statement; the needed zero classification is
proved below.

For any nonempty finite conjugation-invariant multiset \(W\), define
\[
L(W)=2|W|-\sigma(W),\quad
S_W(\alpha)=\sum_{z\in W}e^{-2\pi i\alpha z},\quad
e(W)=\frac{\int J_0|S_W|^2}{L(W)}-1,\quad
h_\phi(W)=\frac{\int\phi|S_W|^2}{L(W)},
\tag{4}
\]
where \(\sigma\) counts simple real support sites. In the exceptional
case (3), writing \(\beta_\phi^{\mathbb R}=\lim_{\varepsilon\downarrow0}
\sup_{W\subset\mathbb R,\ e(W)\le\varepsilon}h_\phi(W)\) with the
supremum over nonempty finite real multisets, there is the exact identity
\[
h_\phi(W)=c(1+e(W)),\qquad \beta_\phi^{\mathbb R}=c.
\tag{5}
\]
Thus ANF-195's square-root real stability theorem extends to **every**
dominated nonnegative-Fourier \(H^1\) profile: use its section 10 when
\(M_\phi>0\), and (5) when \(M_\phi=0\). The latter case has a linear
modulus and does not require the \(H^1\) hypothesis.

A nonzero profile supported in a proper central subinterval
\([-\eta,\eta]\), \(\eta<1\), necessarily has \(M_\phi>0\), since
\(J_0>0\) on \((-1,1)\). There is consequently no nonzero central notch
that is invisible at every exact two-site equality separation.

## The kernel has no unaccounted complex zeros

Put \(N(z)=\cos(\pi z)-az\sin(\pi z)\). If \(N(z)=0\), the nonzero
function \(u(x)=\cos(2\pi zx)\) on \([0,1/2]\) satisfies
\[
-u''=4\pi^2z^2u,\qquad u'(0)=0,\qquad
u'(1/2)+h u(1/2)=0,\qquad h=2\pi/a>0.
\tag{6}
\]
Integration by parts against \(\overline u\) gives
\[
4\pi^2z^2\int_0^{1/2}|u|^2dx
=\int_0^{1/2}|u'|^2dx+h|u(1/2)|^2>0.
\tag{7}
\]
Strictness follows because zero right side would make \(u\) constant and
zero at the endpoint, whereas \(u(0)=1\). Hence \(z^2\) is positive
real, and \(z\) itself is nonzero real. This elementary Robin-boundary
argument excludes every nonreal zero of \(N\).

At a real root the tangent equation is
\(\tan(\pi z)=1/(az)\). There is exactly one positive root in each
\((n,n+1/2)\), \(n\ge0\). At such a root,
\[
N'(z)=-(\pi+a+a^2\pi z^2)\sin(\pi z)\ne0.
\tag{8}
\]
The \(n=0\) root is \(z_0=1/(\sqrt2\pi)\). The simple zeros
\(\pm z_0\) cancel the two simple denominator zeros in (1), with
nonzero continued values. It follows that the **entire** zero set of
\(K\) consists precisely of the simple real zeros \(\pm r_n\),
\(n\ge1\).

## Vanishing and bandwidth force a polynomial quotient

Compact support gives the entire extension and bound
\[
\Phi(z)=\int_{-1}^{1}\phi(u)e^{-2\pi iuz}\,du,\qquad
|\Phi(z)|\le\|\phi\|_1e^{2\pi|\operatorname{Im}z|}.
\tag{9}
\]
Suppose the left side of (2) holds. Nonnegativity on the real axis
implies \(\Phi'(\pm r_n)=0\): each zero is a real minimum.
Evenness supplies the negative zeros. By (8), all the apparent poles in
\[
Q(z)=\frac{\Phi(z)}{K(z)^2}
\tag{10}
\]
are therefore removable. Equation (7) is essential here: cancellation
only at real zeros would not suffice if \(K\) had other complex zeros.
Thus \(Q\) is entire and even.

Here is a direct global growth bound, avoiding any unverified quotient
rule for exponential types. For integers \(m\) sufficiently large let
\(H_m=m+1/2\) and use the square
\(\{z:|\operatorname{Re}z|\le H_m,\ |\operatorname{Im}z|\le H_m\}\).
On a vertical side,
\[
|\sin(\pi z)|=\cosh(\pi\operatorname{Im}z)
\ge\tfrac12 e^{\pi|\operatorname{Im}z|},\qquad
|\cot(\pi z)|\le1.
\]
On a horizontal side the corresponding bounds are
\(|\sin(\pi z)|\ge\sinh(\pi H_m)\gg e^{\pi H_m}\) and
\(|\cot(\pi z)|\le\coth(\pi H_m)\le2\).
Since \(|z|\ge H_m\) on the boundary, factorization of \(N\) gives,
uniformly there,
\[
|N(z)|=|\sin(\pi z)|\,|\cot(\pi z)-az|
\gg |z|e^{\pi|\operatorname{Im}z|},\qquad
|K(z)|\gg\frac{e^{\pi|\operatorname{Im}z|}}{|z|}.
\tag{11}
\]
The constants are independent of \(m\). Combining (9)--(11) gives
\(|Q(z)|\ll_\phi H_m^2\) on the boundary, and hence throughout the
square by the maximum-modulus principle. Choosing \(H_m\) comparable
to \(1+|z|\) proves
\[
|Q(z)|\ll_\phi(1+|z|)^2\qquad(z\in\mathbb C).
\tag{12}
\]
Cauchy's derivative estimates imply that \(Q\) is a polynomial of
degree at most two. Because it is even and real on the real axis,
\[
\Phi(z)=(Az^2+c)K(z)^2,\qquad A,c\in\mathbb R.
\tag{13}
\]

## Decay removes the last spurious degree of freedom

For the real half-integers \(t_m=m+1/2\), the exact expression (1) yields
\[
t_m^2K(t_m)^2
=\frac{a^2t_m^4}{(1-2\pi^2t_m^2)^2}
\longrightarrow\frac{a^2}{4\pi^4}>0.
\tag{14}
\]
But the Riemann--Lebesgue lemma gives \(\Phi(t_m)\to0\), because
\(\phi\in L^1\). Equations (13)--(14) force \(A=0\).
Also \(c=\Phi(0)\ge0\). Fourier injectivity on \(L^1\) now gives
\(\phi=cJ_0\), proving (2); the converse is immediate from
\(\widehat J_0=K^2\). Domination gives \(c\le1\) in (3).

## Falsification controls and the analytic boundary

Both positivity and the exact bandwidth have mathematical work to do.

- If Fourier nonnegativity is dropped, let
  \(v(u)=d\mathbf1_{[-1/2,1/2]}(u)\), where
  \(d=\cos\theta/(\sqrt2\sin\theta)>0\). Then \(0\le v\le g\),
  so \(\phi=g*v\) satisfies \(0\le\phi\le J_0\) and has support
  \([-1,1]\). Its transform is \(dK(t)\operatorname{sinc}(t)\),
  which vanishes at every \(r_n\) but is negative for
  \(n<t<r_n\), \(n\ge1\). It is not proportional to \(K^2\).
  Thus double-zero cancellation cannot be inferred from mere
  source-zero interpolation in the larger signed-Fourier class.
- If the bandwidth is enlarged, for \(\delta>0\) and \(0<\epsilon<1\),
  the nonnegative function
  \(K(t)^2[1+\epsilon\cos(2\pi\delta t)]\) has the same real zeros.
  Its inverse transform is
  \(J_0(u)+\frac\epsilon2[J_0(u-\delta)+J_0(u+\delta)]\), supported
  in \([-1-\delta,1+\delta]\), and is not a source rescaling.
  This is a control for the bandwidth hypothesis, not an admissible
  dominated profile in (3).

For \(\phi=cJ_0\), the entire fixed ray is
\(J_t=J_0-t\phi=(1-tc)J_0\). For \(1-tc>0\), its optimal affine
floor over all conjugation-invariant multisets is exactly \(1-tc\),
since the source floor is one and real singletons attain it. Any linear
analytic normalization \(C\), including ANF-099's, therefore obeys
\[
\frac{C(J_t)}{1-tc}=C(J_0).
\tag{15}
\]
The zero-exposure branch cannot improve the normalized certificate. This
does not decide the unrestricted complex envelope for a genuine notch,
give a uniform modulus as \(M_\phi\downarrow0\), improve a critical-zero
proportion, or prove RH.

## Prior art and mathematical delta

The kernel and its classical extremal uniqueness are in
[Carneiro--Chandee--Littmann--Milinovich, *Hilbert spaces and the pair
correlation of zeros of the Riemann zeta-function*, section 3.5,
Corollary 14](https://arxiv.org/pdf/1406.5462). That theorem concerns
equality in the one-delta extremal objective. Here the hypothesis is
vanishing on the complete source zero set; no extremal-objective equality
is assumed. The same paper's section 4 places zero interpolation in the
classical de Branges framework. No RH-conditional zero statistic from
that paper enters (2).

The Robin energy identity, real-minimum double zeros, maximum modulus,
Cauchy estimates and Fourier uniqueness are classical. Equations
(6)--(14) give their complete specialization rather than invoking a
sampling or entire-quotient uniqueness theorem with unchecked hypotheses.
Searches by Montgomery--Taylor extremal uniqueness, positive bandlimited
zero interpolation and entire functions with prescribed zeros locate
this classical framework; no general novelty claim is made.

The local delta is the exact classification of ANF-195's omitted
`M_phi=0` branch, removal of that restriction from its full positive-Fourier
Sobolev theorem, and the resulting no-improvement statement (15).
The proof is analytic and exact; no numerical zero search, finite-height
verification, model inference or Lean certification is being reported.
