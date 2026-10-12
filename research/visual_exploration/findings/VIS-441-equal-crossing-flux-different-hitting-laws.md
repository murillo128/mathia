# VIS-441 — equal mass, crossing flux and full degree-two support do not fix hitting laws

## Claim

On the unit-speed circle flow \(\theta\mapsto\theta+u\), there exist two analytic polynomials \(F_A,F_B\), **each with exactly the nonzero coefficients of degrees \(0,1,2\)**, for which the normalized amplitudes \(A_j(\theta)=|F_j(e^{i\theta})|/\|F_j\|_\infty\) share the regular threshold \(t=\sqrt{99}/10\), target Haar mass \(\mu=1/3\), directional crossing flux \(J=2/\pi\), and the complete Fourier *support* \(\{0,1,2\}\) of the underlying analytic polynomials. Nevertheless, their symmetric first-hit tails differ:

\[
m_H\{H_A>\pi/4\}=1/6,\qquad
m_H\{H_B>\pi/4\}=1/4,
\]
where \(H_j(\theta)=\inf\{|u|:A_j(\theta+u)\ge t\}\). Their cover radii are \(5\pi/12\) and \(\pi/2\), respectively.

Thus the exact-target mass, full frequency-support set, outer bandwidth, and directional level-crossing flux do **not** determine the hitting-time law. This sharpens the missing-information boundary of VIS-440: the ordered complementary-gap geometry (in this one-dimensional case, its length multiset) survives these aggregates.

**Evidence/status:** EXACT-DERIVED + CLASSICAL GAP EROSION/FEJÉR–RIESZ INPUT + MATCHED-SUPPORT CONTROL + NEGATIVE/OBSTRUCTION + NO GENERAL NOVELTY CLAIM.

## Exact geometric mechanism

Let \(E\) be a nonempty proper closed union of finitely many disjoint circle arcs, and let the lengths of the complementary open gaps be \(g_1,\ldots,g_r\). Symmetric thickening of \(E\) by time radius \(\rho\) leaves in gap \(i\) precisely the central length \((g_i-2\rho)_+\). Therefore, with normalized Haar measure,

\[
\boxed{m_H\{H_E>\rho\}=\frac1{2\pi}\sum_{i=1}^r(g_i-2\rho)_+,\quad \rho\ge0.}
\]

If all \(2r\) boundary crossings are transverse, the target mass and directional flux are

\[
\mu=1-\frac{\sum_i g_i}{2\pi},
\qquad J=\frac{2r}{2\pi}=\frac r\pi.
\]

These determine the total gap length and number of gaps, **not** the individual lengths. The cover radius is \(\frac12\max_i g_i\). The expression is invariant under rotating the origin or relabelling the gaps; it is an exact circle-geometry identity, not a simulated distribution or a probabilistic mixing assumption.

## Matched analytic degree-two construction

For a strictly ordered quadruple \(\beta=(\beta_1,\beta_2,\beta_3,\beta_4)\) with \(\beta_1=0\) and \(\beta_4<2\pi\), define the real trigonometric polynomial

\[
R_\beta(\theta)=-\prod_{j=1}^{4}
\sin\!\left(\frac{\theta-\beta_j}{2}\right),
\qquad M_\beta=\max_\theta R_\beta(\theta)>0,
\]
\[
Q_\beta(\theta)=\frac{99}{100}
+\frac{R_\beta(\theta)}{100M_\beta}.
\]

The product of four half-angle sines is a **periodic trigonometric polynomial of degree two**. It is positive exactly on the two arcs \([\beta_1,\beta_2]\) and \([\beta_3,\beta_4]\), and negative on the complementary gaps. Its four simple zeros are transverse.

Take the two exact root configurations

\[
\beta_A=(0,\pi/6,\pi,3\pi/2),\qquad
\beta_B=(0,\pi/6,\pi/2,\pi).
\]

For \(A\), evaluating \(R_A(5\pi/4)\), and for \(B\), evaluating \(R_B(3\pi/4)\), yields in both cases two sine magnitudes exceeding \(7/10\) and two exceeding \(3/10\), with positive product sign after the leading minus. Hence

\[
M_A,M_B>(7/10)^2(3/10)^2=441/10000>1/99.
\]

Since \(|R_\beta|\le1\), this gives \(Q_\beta\ge99/100-1/(100M_\beta)>0\); moreover \(\max Q_\beta=1\). By the classical one-variable **Fejér–Riesz theorem**, there is an analytic polynomial \(F_\beta(z)=a_0+a_1z+a_2z^2\) with \(|F_\beta(e^{i\theta})|^2=Q_\beta(\theta)\), and its norm is exactly one. The common amplitude threshold is therefore \(t=\sqrt{99}/10\), and \(\{A_\beta\ge t\}=\{R_\beta\ge0\}\) gives exactly the prescribed arcs.

The matching of **full coefficient support**, not just maximal degree, follows without numerical factorization. Writing \(u_j=e^{i\beta_j}\),

\[
R_\beta(\theta)=-\frac{e^{-i\sum_j\beta_j/2}}{16}
z^{-2}\prod_{j=1}^4(z-u_j),\qquad z=e^{i\theta}.
\]

Thus its Fourier coefficients at modes \(\pm2\) are nonzero, and the mode \(1\) is nonzero precisely when \(\sum_j u_j\ne0\). Here \(\sum_j u_j=e^{i\pi/6}-i\) for \(A\), and \(e^{i\pi/6}+i\) for \(B\), both nonzero. Consequently \(Q\) has nonzero coefficients at \(\pm1,\pm2\). In \(|a_0+a_1z+a_2z^2|^2\), mode \(2\) equals \(a_2\overline{a_0}\), so \(a_0,a_2\ne0\); a nonzero mode \(1\) then forces \(a_1\ne0\). Both analytic supports are exactly \(\{0,1,2\}\).

The total target length for either construction is \(\pi/6+\pi/2=2\pi/3\), so \(\mu=1/3\). Both have four simple boundary points and therefore \(J=2/\pi\). Yet their complementary-gap lengths are

\[
(g_{A,1},g_{A,2})=(5\pi/6,\pi/2),\quad
(g_{B,1},g_{B,2})=(\pi/3,\pi).
\]

Substitution into the exact gap formula at \(\rho=\pi/4\) yields \(1/6\) and \(1/4\) as claimed. It also gives \(\max g_A/2=5\pi/12\), \(\max g_B/2=\pi/2\). The VIS-440 lower bound has the common value \([1-1/3-(\pi/4)(2/\pi)]_+=1/6\): it is attained by \(A\) but is strictly loose for \(B\).

## Audits, literature boundary and Wang consequence

A separate dense-grid numerical check of the two explicit \(Q\) functions found positive minima approximately \(0.96792\) and \(0.95029\), superlevel masses \(1/3\) within discretization error, nonzero first/second Fourier modes and the claimed gap-erosion tails. These are checks of the independent exact argument; neither numerical sampling nor a rendered plot is used as proof. Shifting the plot origin or varying resolution changes none of the stated invariants. The controls deliberately match frequency **support** but not coefficient values, phase geometry or Fourier power spectrum; a stronger coefficient-matching claim is neither made nor implied.

The gap-eroding formula is elementary one-dimensional parallel-set geometry. Fejér–Riesz factorization is classical (Encyclopedia of Mathematics, *Fejér–Riesz theorem*, https://encyclopediaofmath.org/wiki/Fej%C3%A9r-Riesz_theorem); level-crossing flux is the classical directional-perimeter/Rice background already recorded for VIS-440. No new general fact about one-dimensional hitting times, spectral factorization, or Rice theory is claimed. The line-specific contribution is the **simultaneous exact-support, same-threshold, same-mass and same-flux counterexample** at the point where VIS-440 proposed flux as an additional Wang Haar calibration.

For a genuine higher-dimensional Wang shell, \(\mu_t\) and \(J_t\) remain useful one-sided controls, but a quiet-time distribution cannot be reconstructed from them and support alone. One must keep or bound further directional target geometry (e.g. overlap volumes of translated sets or the full same-shell hitting law). This does not construct a genuine Wang arithmetic coefficient array or a distinguished-height selector, prove a Gram/Haar transport theorem, or imply RH.

The decisive exact checks are positivity of \(Q_A,Q_B\), nonvanishing first and second Fourier coefficients, regularity of the four threshold crossings, and the complementary-gap lengths. A degenerate zero, a missing mode or a wrong gap length would invalidate the matched control; the explicit factorization and angle computations exclude these cases.

## Dependencies

- VIS-419: fixed Wang shells as finite base-prime torus Laurent polynomials and their exact Haar self-null.
- VIS-428: fixed-shell hitting and saturation.
- VIS-429: mass-based buffered hitting floor.
- VIS-440: directional crossing-flux bound and mass/bandwidth-matched circle controls.
