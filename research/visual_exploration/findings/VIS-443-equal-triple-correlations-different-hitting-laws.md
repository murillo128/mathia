# VIS-443 — complete three-point target correlations do not fix Haar first-hit laws

## Claim

There exist **two finite unions of regular superlevel arcs of normalized analytic circle polynomials of exact degree ten** whose target indicators have identical full three-point correlations at every pair of continuous shifts, hence also identical mass and two-point autocorrelation, but whose symmetric first-hit distributions differ.

On the unit-speed circle flow, write \(\omega=2\pi/36\) and choose any \(0<\delta<\omega\). The two targets below have common mass \(\mu=10\delta/(2\pi)\), directional level-crossing flux \(J=10/\pi\), and the same cover radius \((9\omega-\delta)/2\). Nevertheless, at \(\rho=3\omega=\pi/6\),

\[
\boxed{\ m_H\{H_E>\rho\}=\frac{5\omega-2\delta}{2\pi},
\qquad m_H\{H_F>\rho\}=\frac{4\omega-2\delta}{2\pi}\ }.
\]

Their avoidance difference is exactly \(1/36\), independently of \(\delta\). At \(\delta=\omega/2\) the probabilities are \(1/9\) and \(1/12\). A single **four-point** target correlation distinguishes them, so the obstruction concerns all information of order at most three, not every possible higher-order statistic.

**Evidence/status:** LITERATURE+EXACT-DERIVED + CLASSICAL CYCLIC THREE-DECK COUNTEREXAMPLE + CLASSICAL FEJÉR–RIESZ + NEGATIVE/OBSTRUCTION. No novelty is claimed for three-deck nonuniqueness or general higher-order phase retrieval. The line-specific consequence is its explicit first-hit-law failure inside regular bounded-degree analytic superlevel families.

## Discrete configuration and third-order equality

The construction specializes the cyclic three-deck counterexample of Keleti--Kolountzakis, Theorem 2.23, to \(n=pqrd=36\) with \((p,q,r,d)=(2,3,2,3)\). In \(\mathbb Z/36\mathbb Z\), put

\[
A=\{0,3,12,15,24,27\},\qquad B=\{0,3,18,21\},
\]
\[
S_E=A\cup(B+1)=\{0,1,3,4,12,15,19,22,24,27\},
\]
\[
S_F=A\cup(B+4)=\{0,3,4,7,12,15,22,24,25,27\}.
\]

Each has ten distinct sites. The equality of *every* three-deck count is exact:

\[
\sum_{x\in\mathbb Z/36}\mathbf1_{S_E}(x)\mathbf1_{S_E}(x+a)\mathbf1_{S_E}(x+b)
=
\sum_{x\in\mathbb Z/36}\mathbf1_{S_F}(x)\mathbf1_{S_F}(x+a)\mathbf1_{S_F}(x+b)
\quad(a,b\in\mathbb Z/36).
\]

For an explicit Fourier certificate, set \(z=e^{-2\pi i j/36}\), \(U=1+z^3\), \(P=1+z^{12}+z^{24}\), \(Q=1+z^{18}\). Their unnormalized discrete Fourier transforms are

\[
\widehat{\mathbf1_{S_E}}(j)=U(P+zQ),\qquad
\widehat{\mathbf1_{S_F}}(j)=U(P+z^4Q).
\]

Here \(P=3\) for \(3\mid j\) and zero otherwise; \(Q=2\) for \(2\mid j\) and zero otherwise. Where these transforms are nonzero, their ratio (F over E) is \(1\) if \(3\mid j\), and \(z^3=e^{-2\pi i j/12}\) if \(2\mid j,\ 3\nmid j\). In the overlap \(6\mid j\), either \(j\equiv6\pmod{12}\), so \(U=0\), or \(j\equiv0\pmod{12}\), so \(z^3=1\).

For every zero-sum triple \(j_1+j_2+j_3\equiv0\pmod{36}\) of nonzero Fourier modes, the count of modes in the second class is zero, two, or three (not one, by reduction modulo 3). With three, the product of phase ratios is \(e^{-2\pi i(j_1+j_2+j_3)/12}=1\). With two, the remaining mode is an even multiple of 3; nonvanishing then forces it to be divisible by 12, so the product of the two phase ratios is again one. Thus all zero-sum Fourier triple products agree. The Fourier transform of the third-order deck is precisely such a triple product, proving the displayed equality without numerical approximation.

## Continuous superlevel targets and exact first-hit geometry

Thicken the sites to short arcs,

\[
T_S=\bigcup_{a\in S}[a\omega,a\omega+\delta]\quad\text{mod }2\pi,
\qquad S=S_E,S_F.
\]

Because \(\delta<\omega\), these arcs are disjoint. If \(h_\delta=\mathbf1_{[0,\delta]}\), their Fourier coefficients satisfy

\[
\widehat{\mathbf1_{T_S}}(k)=\widehat h_\delta(k)
\sum_{a\in S}e^{-ika\omega},\qquad k\in\mathbb Z.
\]

The finite triple-product identity holds for every integer frequency modulo 36. Multiplication by the common three factors \(\widehat h_\delta(k)\) consequently preserves it for every pair of integer frequencies. Fourier uniqueness on the two-torus proves the **full continuous three-point correlation equality**

\[
\int \mathbf1_{T_{S_E}}(\theta)\mathbf1_{T_{S_E}}(\theta+u)
\mathbf1_{T_{S_E}}(\theta+v)\,dm_H(\theta)
=
\int \mathbf1_{T_{S_F}}(\theta)\mathbf1_{T_{S_F}}(\theta+u)
\mathbf1_{T_{S_F}}(\theta+v)\,dm_H(\theta)
\]

for every real \(u,v\). This also implies equal pair correlations by setting one shift to zero, since indicators are idempotent.

The successive circle site-gap multisets, in units of \(\omega\), are respectively

\[
G_E=\{1,1,2,2,3,3,3,4,8,9\},\quad
G_F=\{1,1,2,2,3,3,3,5,7,9\}.
\]

The complementary *arc* gaps are \(g\omega-\delta\) for \(g\in G_S\). By the exact erosion formula of VIS-441,

\[
m_H\{H_{T_S}>\rho\}
=\frac1{2\pi}\sum_{g\in G_S}(g\omega-\delta-2\rho)_+.
\]

At \(2\rho=6\omega\), only \(g=8,9\) contribute for E and only \(g=7,9\) for F. This gives the claimed tails and difference. Both gap lists have maximum 9, so both cover radii are \((9\omega-\delta)/2\). Their ten target arcs produce 20 transverse boundary points and flux \(J=20/(2\pi)=10/\pi\).

At the fourth order, the translation pattern \(\{0,1,3,4\}\) occurs exactly once in \(S_E\) and never in \(S_F\). Therefore

\[
\int\!\prod_{v\in\{0,\omega,3\omega,4\omega\}}
\mathbf1_{T_{S_E}}(\theta+v)\,dm_H(\theta)=\frac{\delta}{2\pi},
\quad
\int\!\prod_{v\in\{0,\omega,3\omega,4\omega\}}
\mathbf1_{T_{S_F}}(\theta+v)\,dm_H(\theta)=0.
\]

This witness is a concrete order-four distinction for the specific pair, **not** a theorem that four-point data always reconstruct arbitrary targets.

## Regular analytic-polynomial realization

For each target, list its 20 distinct cyclic arc endpoints as \(0=\beta_{S,1}<\cdots<\beta_{S,20}<2\pi\), and define

\[
R_S(\theta)=-\prod_{j=1}^{20}\sin\frac{\theta-\beta_{S,j}}2,\quad
M_S=\max R_S>0,\quad L_S=-\min R_S>0.
\]

This is a real trigonometric polynomial of **exact degree ten**, positive precisely on the ten arc interiors and negative on their complement; every endpoint is a simple zero. Set the *same* constant \(c=1+\max(L_E/M_E,L_F/M_F)\), and

\[
Q_S(\theta)=\frac{c+R_S(\theta)/M_S}{c+1}.
\]

Then \(0<Q_S\le1\), \(\max Q_S=1\), and for the common regular threshold \(t=\sqrt{c/(c+1)}\), the superlevel set \(\{\sqrt{Q_S}\ge t\}\) is exactly \(T_S\). The Fejér--Riesz theorem gives analytic polynomials \(F_S(z)=\sum_{j=0}^{10}a_{S,j}z^j\) with \(|F_S(e^{i\theta})|^2=Q_S(\theta)\) and \(\|F_S\|_\infty=1\). The nonzero top harmonic of \(R_S\) forces exact degree ten. All target and first-hit statements therefore apply to ordinary normalized analytic-amplitude superlevels, not merely abstract indicator drawings.

## Audit, prior art, and Mathia consequence

An independent finite audit of all \(36^2=1296\) ordered shift pairs found identical three-deck counts. A separate four-deck count gave \(1\) versus \(0\) for \((0,1,3,4)\). Exact rational gap erosion at \(\delta=\omega/2,\rho=3\omega\) gave \(1/9\) versus \(1/12\), and a high-resolution arc/erosion rendering confirmed the difference without supplying the proof. The continuous correlation equality follows algebraically from discrete Fourier products; sampling or raster resolution plays no evidentiary role. The width family \(0<\delta<\omega\), common translations/reflections, and the full continuum of lag pairs prevent a specially chosen image scale or finite-lag alias from producing the result.

The cyclic equal-three-deck configurations and Fourier method are **classical**, not claimed as new: T. Keleti and M. N. Kolountzakis, *On the determination of sets by their triple correlation in finite cyclic groups*, *Online Journal of Analytic Combinatorics* 1 (2006), paper 4, Theorem 2.23, DOI 10.61091/ojac-104, arXiv:math/0603415. The analytic factorization and one-dimensional erosion are also classical, as recorded for VIS-441/VIS-442. This finding explicitly transfers a literature three-deck ambiguity into a regular polynomial first-hit control with an exact **order-four** diagnostic; it does not assert a novel general reconstruction theorem.

For the Wang fixed-shell torus picture of VIS-419/VIS-430, even exact target mass, crossing flux, full two-point autocorrelation, and now **all three-point correlations** need not determine an abstract analytic-amplitude hitting distribution. The same-shell Haar first-hit law or sufficient additional geometric information remains the comparison target. The controls are not claimed to be arithmetic Wang coefficient arrays and provide no distinguished-height selector, Gram/Haar transport failure, zero exclusion, or RH implication.

The decisive falsifiers are a discrepancy in any of the 1296 finite three-deck counts, a sign/endpoint error in the analytic realization, an incorrect complementary-gap multiset, or a nonzero fourth-order count for F at shifts \((\omega,3\omega,4\omega)\). These checks are mutually independent where their mathematical definitions allow.

## Dependencies

- VIS-419: fixed Wang shells as prime-phase Laurent character polynomials.
- VIS-428: fixed-shell first-hit saturation.
- VIS-430: occupation autocorrelation certificate.
- VIS-440: directional crossing flux.
- VIS-441: exact circle complementary-gap erosion and analytic superlevel realization.
- VIS-442: two-point homometric control and its identifiability boundary.
