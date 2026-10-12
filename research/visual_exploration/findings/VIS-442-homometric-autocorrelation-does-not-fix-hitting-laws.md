# VIS-442 — homometric target autocorrelation does not determine first-hit tails

## Claim

On the unit-speed circle flow \(\theta\mapsto\theta+u\), there are two normalized analytic polynomials of exact degree four and a **common regular amplitude threshold** whose superlevel targets have the same Haar mass, directional crossing flux, and **complete two-point target autocorrelation at every shift**, but different symmetric first-hit laws. The construction forms an exact one-parameter family.

This strengthens VIS-441 from equal mass/flux/support to complete second-order target information, and shows that the autocorrelation employed by VIS-430 does not determine the hitting distribution even when it determines every window-occupation mean and variance.

**Evidence/status:** EXACT-DERIVED + CLASSICAL HOMOMETRY + CLASSICAL FEJÉR–RIESZ FACTORIZATION + NEGATIVE/OBSTRUCTION. No general novelty or RH implication is claimed.

## Homometric construction

Let \(\omega=\pi/6\), and take two finite subsets of \(\mathbb Z/12\mathbb Z\):
\[
S_A=\{0,1,4,6\},\qquad S_B=\{0,1,3,7\}.
\]
Their *oriented* modular difference multiplicities agree: zero occurs four times; residue \(6\) occurs twice; every other nonzero residue occurs once. The configurations are not rotations/reflections of one another, because their successive cyclic spacing multisets differ: \(\{1,2,3,6\}\) versus \(\{1,2,4,5\}\).

Fix any \(0<\delta<\omega\), and form four disjoint closed arcs on the circle
\[
E_S=\bigcup_{a\in S}[a\omega,a\omega+\delta]\pmod{2\pi}.
\]
For the indicator \(h_\delta=1_{[0,\delta]}\), with normalized circle Fourier coefficients,
\[
\widehat{1_{E_S}}(k)=\widehat h_\delta(k)\sum_{a\in S}e^{-ika\omega},\qquad
\left|\sum_{a\in S}e^{-ika\omega}\right|^2
=\sum_{a,b\in S}e^{-ik(a-b)\omega}.
\]
Equality of oriented difference multisets therefore gives
\[
|\widehat{1_{E_A}}(k)|^2=|\widehat{1_{E_B}}(k)|^2
\quad\text{for every integer }k,
\]
and hence, by Fourier uniqueness, equality of the continuous covariograms
\[
C_{E_A}(s)=C_{E_B}(s),\qquad
C_E(s)=m_H(E\cap(E-s)),\quad\text{for every }s\in\mathbb R.
\]
Both targets have mass \(\mu=4\delta/(2\pi)=2\delta/\pi\) and eight transverse boundary points, hence directional flux \(J=8/(2\pi)=4/\pi\). All VIS-430 symmetric window-occupation means and variances consequently agree for every radius.

## Different first-hit distributions

The successive complementary gaps for the two targets, in cyclic order, are
\[
g_A=(\omega-\delta,\,3\omega-\delta,\,2\omega-\delta,\,6\omega-\delta),
\]
\[
g_B=(\omega-\delta,\,2\omega-\delta,\,4\omega-\delta,\,5\omega-\delta).
\]
For the symmetric time-to-target \(H_E(\theta)=\inf\{|u|:\theta+u\in E\}\), elementary erosion of each complementary gap gives the *exact* identity (VIS-441)
\[
m_H\{H_E>\rho\}=\frac1{2\pi}\sum_i(g_i-2\rho)_+,\qquad \rho\ge0.
\]
At the pre-saturation radius \(\rho=\pi/3=2\omega\), exactly the largest gap contributes for each target, so
\[
\boxed{m_H\{H_A>\pi/3\}=\frac16-\frac{\delta}{2\pi},
\qquad m_H\{H_B>\pi/3\}=\frac1{12}-\frac{\delta}{2\pi}.}
\]
The difference is always \(1/12\) for \(0<\delta<\pi/6\). With \(\delta=\pi/12\), the two avoidance probabilities are \(1/8\) and \(1/24\), and their exact cover radii are \(11\pi/24\) and \(3\pi/8\). Neither difference depends on image resolution or numerical integration.

## Analytic-polynomial realization at one normalized threshold

Write the eight distinct endpoints of \(E_S\) as \(0=\beta_{S,1}<\cdots<\beta_{S,8}<2\pi\), and define
\[
R_S(\theta)=-\prod_{j=1}^{8}\sin\left(\frac{\theta-\beta_{S,j}}2\right).
\]
Because there are eight half-angle factors, \(R_S\) is a real, periodic trigonometric polynomial of *exact degree four*, with nonzero top Fourier mode. It has simple zeros precisely at the arc endpoints and is positive in the interiors of the four target arcs, negative on their complement.

Let \(M_S=\max_\theta R_S(\theta)>0\) and \(L_S=-\min_\theta R_S(\theta)>0\). Set the same constant
\[
c=1+\max(L_A/M_A,L_B/M_B)>0
\]
for both, and define
\[
Q_S(\theta)=\frac{c+R_S(\theta)/M_S}{c+1}.
\]
Then \(0<Q_S\le1\), \(\max Q_S=1\), and, at the common regular threshold \(t=\sqrt{c/(c+1)}\),
\[
\{\sqrt{Q_S}\ge t\}=\{R_S\ge0\}=E_S.
\]
Fejér–Riesz factorization supplies an analytic polynomial \(F_S(z)=\sum_{j=0}^{4}a_{S,j}z^j\) with \(|F_S(e^{i\theta})|^2=Q_S(\theta)\) and \(\|F_S\|_\infty=1\). The nonzero top Fourier coefficient of \(Q_S\) forces \(a_{S,0}\overline{a_{S,4}}\ne0\), so each polynomial really has exact outer degree four. The equality of Fourier power spectra is asserted for the **target indicators**, not for the different analytic amplitudes or their coefficient arrays.

## Checks, prior art and research boundary

Independent checks enumerate all 16 modular oriented differences exactly, verify the disjoint-arc/gap geometry, and, at \(\delta=\pi/12\), reproduce \(0.125\) and \(1/24\) from the exact gap formula. A \(2^{16}\)-point Fourier-grid comparison finds target autocorrelation discrepancies at floating-point roundoff scale; numerical sampling is only a cross-check of the algebra, not evidence replacing the proof. The result persists over the full width interval, under common translation/reversal, and under changing render resolution.

**Prior art:** The nonuniqueness of homometric sets and their Patterson/autocorrelation functions is classical: J. Rosenblatt and P. D. Seymour, *The Structure of Homometric Sets*, SIAM J. Algebraic Discrete Methods 3 (1982), 343–350, DOI 10.1137/0603035. For nonconvex-window covariogram nonuniqueness, see M. Baake and U. Grimm, *Homometric model sets and window covariograms*, Z. Kristallographie 222 (2007), 54–58, DOI 10.1524/zkri.2007.222.2.54. B. Galerne, *Computation of the perimeter of measurable sets via their covariogram*, Image Analysis & Stereology 30 (2011), 39–51, DOI 10.5566/ias.v30.p39-51, gives the classical covariogram/directional-perimeter connection. One-variable Fejér–Riesz factorization and the circle gap-erosion identity are also classical. Neither phase-retrieval nonuniqueness nor a general hitting-time theorem is claimed as new.

The line-specific consequence is an exact **failure of identifiability for the VIS-430 second-order hitting certificate** in a regular bounded-degree analytic-amplitude family. Knowing the entire two-point target autocorrelation gives the same window-occupation variance and hence the same upper probability certificate, but it need not give the same probability of *zero* occupation. Higher-order directional avoidance information or the actual same-shell first-hit distribution is needed when this bound is inconclusive.

These are abstract circle controls, not explicit admissible Wang arithmetic coefficient arrays or evidence of an exceptional selected height. The argument gives no Gram-to-Haar transport failure, zeta-zero exclusion, or progress toward proving RH. Its decisive falsifiers would be a mismatch of the modular difference multisets, an incorrect complementary gap, a failure of the shared regular amplitude realization, or a counterexample to the stated gap-erosion formula; each is checked explicitly above.

## Dependencies

- VIS-419: fixed-shell prime-phase Haar self-null.
- VIS-428: fixed-shell hitting and saturation.
- VIS-430: target autocorrelation and occupation-variance upper certificate.
- VIS-440: directional boundary crossing flux.
- VIS-441: complementary-gap erosion and lower-order matched controls.
