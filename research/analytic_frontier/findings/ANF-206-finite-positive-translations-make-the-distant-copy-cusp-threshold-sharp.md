# ANF-206 — Finite positive translations make the distant-copy cusp threshold sharp

**Status:** EXACT-DERIVED + COMPLEX-MULTISET + FINITE-POSITIVE-TRANSLATION + SHARP-DISTANT-COPY-THRESHOLD. For a fixed dominated triangular notch, ANF-205's central-cusp amplitude is the exact threshold for the existence of a finite configuration stable against every sufficiently distant duplicate. At and below the threshold, an explicit combination of 16 real translates of **any** finite conjugation-invariant seed passes that test strictly. At the critical amplitude its interaction has a positive inverse-fourth-power tail. Above the threshold no finite configuration passes. This classifies the distant-copy test, not finite attainment or the unrestricted energy floor.

## Object and precise threshold

Use \(\widehat f(x)=\int f(u)e^{-2\pi iux}\,du\), and set
\[
\theta=1/\sqrt2,\qquad
g(u)=\frac{\cos(\sqrt2u)}{\sqrt2\sin\theta}
\mathbf1_{[-1/2,1/2]}(u),\quad J_0=g*g,\quad
d=\tfrac12\cot^2\theta>0.
\tag{1}
\]
Freeze \(0<\eta<1\) and \(b>0\) such that
\[
\phi(u)=b(1-|u|/\eta)_+\le J_0(u),\qquad
J_t=J_0-t\phi,\qquad t_c=d\eta/b.
\tag{2}
\]
Throughout, \(0<t<1\). For a nonempty finite multiset
\(W=\overline W\), count entries with their positive integer
multiplicities and define
\[
N=|W|,\quad L(W)=2N-\sigma(W),\quad
S_W(u)=\sum_{z\in W}e^{-2\pi iuz},\quad P_W(u)=|S_W(u)|^2,
\]
\[
Q_t(W)=\frac{\int J_t(u)P_W(u)\,du}{L(W)},\qquad
H_{t,W}(R)=\widehat{J_tP_W}(R).
\tag{3}
\]
Here \(\sigma\) counts distinct simple real sites. Lamzouri's
inequality gives \(Q_t(W)\ge1-t>0\), but positivity alone
does not give minimization. Say that \(W\) passes the distant-copy
test if there is \(R_0>\operatorname{diam}(\Re W)\) such that
\[
Q_t(W\cup(W+R))\ge Q_t(W)\qquad(R\ge R_0).
\tag{4}
\]
The union in this definition retains multiplicities. The exact result is
\[
\boxed{
\exists W\text{ satisfying (4)}\quad\Longleftrightarrow\quad t\le t_c.
}
\tag{5}
\]
The same equivalence holds when \(W\) is required to be real.
If \(t_c\ge1\), the positive side covers the entire prescribed
amplitude range and the critical point is outside it. The critical
statements below concern \(t_c<1\).

## Why the critical test forces two exact source zeros

For any conjugation-invariant \(W\), \(P_W\) is real analytic
and even on the real axis, with \(P_W(0)=N^2\). Disjoint real
projections give
\[
L(W\cup(W+R))=2L(W),\qquad
Q_t(W\cup(W+R))-Q_t(W)=\frac{H_{t,W}(R)}{L(W)}.
\tag{6}
\]
Thus (4) is exactly eventual nonnegativity of \(H_{t,W}\).

The explicit source formula is
\[
J_0(u)=\frac{(1-u)\cos(\sqrt2u)+\sin(\sqrt2(1-u))/\sqrt2}
{4\sin^2\theta}\qquad(0\le u\le1).
\tag{7}
\]
It gives
\[
J_0'(0+)=J_0'(1-)=-d,\qquad
J_0'''(0+)=\frac{3+\cos\sqrt2}{2\sin^2\theta}=1+4d>0.
\tag{8}
\]
The second distributional derivative of \(J_tP_W\) has an
integrable piecewise smooth part and atoms at \(0,\pm\eta,\pm1\).
Fourier differentiation and Riemann--Lebesgue therefore give, as in
ANF-205,
\[
R^2H_{t,W}(R)=\frac1{2\pi^2}
\left[(d-tb/\eta)N^2-dP_W(1)\cos(2\pi R)
+(tb/\eta)P_W(\eta)\cos(2\pi\eta R)\right]+o_W(1).
\tag{9}
\]
Parameters and the configuration are fixed before taking the limit.

At \(t=t_c\), (4) forces
\[
\boxed{S_W(1)=S_W(\eta)=0.}
\tag{10}
\]
Here is an argument that does not require rational independence of
\(1,\eta\). Let
\(T(R)=-P_W(1)\cos(2\pi R)+P_W(\eta)\cos(2\pi\eta R)\).
Its Cesaro mean is zero and, since \(0<\eta<1\), its mean square is
\((P_W(1)^2+P_W(\eta)^2)/2\). Eventual nonnegativity in (9)
implies \(T(R)\ge-\varepsilon\) for all sufficiently large
\(R\), for every \(\varepsilon>0\). If \(B=\sup|T|\), then
\(T^2\le BT+(B+\varepsilon)\varepsilon\) on that tail.
Averaging and sending \(\varepsilon\downarrow0\) makes its
mean square zero. Both coefficients vanish, proving (10).

Condition (10) is necessary, not asserted sufficient: zeros of
\(S_W\) of order one leave fourth-order endpoint interactions.
The following construction removes those as well.

## A positive finite translation that removes the endpoint terms

For an arbitrary finite seed \(W=\overline W\), let
\[
V=\bigsqcup_{a,c=0}^{2}
\binom2a\binom2c\left(W+\frac a2+\frac{c}{2\eta}\right).
\tag{11}
\]
There are 16 copies counted with multiplicity; coincident translated
sites are retained. In particular \(M:=|V|=16N\), \(V=\overline V\),
and a real seed gives a real \(V\). Its exact source is
\[
S_V(u)=S_W(u)(1+e^{-\pi iu})^2(1+e^{-\pi iu/\eta})^2,
\]
\[
P_V(u)=256P_W(u)\cos^4(\pi u/2)\cos^4(\pi u/(2\eta)).
\tag{12}
\]
Thus \(P_V\) vanishes to order at least four at both
\(\pm1\) and \(\pm\eta\), while \(P_V(0)=M^2\).
No signed coefficient, complex translation, or fractional multiplicity
is used. No minimality of the number 16 is claimed.

For \(t<t_c\), (9) immediately becomes
\[
\boxed{
H_{t,V}(R)=\frac{(d-tb/\eta)M^2}{2\pi^2R^2}+o(R^{-2})>0
\quad\text{for all sufficiently large }R.
}
\tag{13}
\]
At \(t=t_c\), the first derivative at the origin cancels:
\(J_{t_c}'(0+)=0\). Write \(f=J_{t_c}P_V\), extended by
zero outside \([-1,1]\). It is \(C^2\) on the whole real
line. The fourth-order zeros in (12) make its derivatives through
order three continuous across \(\pm\eta,\pm1\). At the origin,
evenness, \(P_V'(0)=P_V'''(0)=0\), and (8) give
\[
f'''(0+)=(1+4d)M^2,\qquad f'''(0-)=-f'''(0+).
\tag{14}
\]
Consequently its fourth distributional derivative is
\[
f^{(4)}=2(1+4d)M^2\delta_0+h,\qquad h\in L^1(\mathbb R).
\tag{15}
\]
The remainder is integrable because each of the finitely many pieces
is smooth up to its endpoints; there are no other distributional
atoms or derivatives of atoms. With the Fourier convention in (1),
\((2\pi iR)^4=16\pi^4R^4\). Hence
\[
\boxed{
H_{t_c,V}(R)=\frac{(1+4d)M^2}{8\pi^4R^4}+o(R^{-4})>0
\quad\text{for all sufficiently large }R.
}
\tag{16}
\]
This establishes strict (4) even at the critical amplitude. Above it,
ANF-205 proves arbitrarily distant strictly improving duplicates for
every finite configuration. Equivalently, the Cesaro mean of the
right side of (9) is then strictly negative, precluding eventual
nonnegativity. This proves both directions of (5).

## Prior art, validation and the remaining mathematical boundary

The positive translation product is classical binomial filtering;
see Torralba--Isola--Freeman, [*Foundations of Computer Vision*,
section 17.4](https://visionbook.mit.edu/blurring_2.html).
ANF-130 already realizes finite prescribed-zero products as positive
integer translation clouds, there to suppress interior Laplace
saddles. That mechanism is reused here, not claimed as new.
Derivative-jump Fourier asymptotics and the Cesaro orthogonality of
distinct frequencies are standard. The present local delta is the
exact threshold (5), its critical source-zero necessity (10), and
the all-seed completion whose surviving positive central cubic term
gives (16).

[Logan's eventually-positive bandlimited problem](https://doi.org/10.1137/0514022)
and [Gorbachev--Ivanov--Tikhonov's generalized sign/moment
problems](https://arxiv.org/abs/1904.11328) supply the closest
eventual-sign prior-art boundary. Their extremal sign radii and
vanishing-moment theorems are not imported. The auxiliary source
inequality is [Lamzouri, Proposition 2.1](https://arxiv.org/html/2609.02882v2#S2),
with the source extremizer recorded by
[Carneiro--Chandee--Littmann--Milinovich, Corollary 14](https://arxiv.org/pdf/1406.5462).
No RH-conditional zero-statistics input is used. Targeted searches
of eventual Fourier sign, finite-energy replication, endpoint jumps
and positive binomial filters did not identify this exact
Montgomery--Taylor threshold classification. This is not an exhaustive
novelty claim or a new general Fourier theorem.

As a noncertifying check, 65-digit decimal arithmetic evaluated the
exact finite pair sum for \(H_{t,V}\), using the closed kernel
\(F=K^2\) from ANF-204 and
\(\widehat\phi(x)=b\eta\operatorname{sinc}^2(\eta x)\).
With \(b=1/10\), widths \(1/20,\sqrt2/20\), and seeds
\(\{0\}\), \(\{0,0,0.37\}\), the ratio of
\(R^4H_{t_c,V}(R)\) to \((1+4d)M^2/(8\pi^4)\) at
\(R=25600.37\) differed from one by less than \(8.2\cdot10^{-4}\)
in all four cases. Checks at \(R=1600.37,6400.37\) and at
subcritical and supercritical amplitudes also matched the predicted
leading signs and decay. These finite checks are not tail certificates;
(9)--(16) are the analytic proof. No Lean verification is claimed.

The substantive limitation is essential: the translation in (11)
can change the energy and affine normalization substantially. In
general \(L(V)\ne16L(W)\), because internal translated sites
can collide. That equality is neither assumed nor needed. Only
disjoint *final* duplication in (6) uses denominator additivity.
The onset of the positive tail depends on the seed and width; no
uniform bound in growing geometry or as \(\eta\downarrow0\)
is established. Passing (4) does not imply stability under bounded
translations, nonidentical companions, deletion, or arbitrary
configuration changes.

Thus distant-copy nonattainment cannot be extended universally
through \(t=t_c\). Whether the unrestricted floor is attained
there, or at every sufficiently small positive amplitude in the
complex class, remains open. The initial unrestricted exposure
envelope is unchanged. There is no new zero-density bound,
critical-line proportion, or RH conclusion.
