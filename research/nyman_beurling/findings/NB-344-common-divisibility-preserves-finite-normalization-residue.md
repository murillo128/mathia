# NB-344 — Common-divisibility dilations retain a finite normalization residue

- **Status:** proved (author derivation; independent adversarial review pending)
- **Research line:** nyman_beurling
- **Depends on:** NB-304, NB-314, NB-338, NB-341, NB-342, NB-343
- **Classification:** EXACT-DERIVED + SOURCE-SIDE + COMMON-DIVISIBILITY + FINITE-NORMALIZATION-RESIDUE + NON-TARGET-AWARE + PRIOR-ART-AUDITED

## Claim

Keep the actual Nyman finite section, projected integer dilation, and rank-one comparison of NB-314:
\[
U_n=\operatorname{span}\{g_2,\ldots,g_n\},\qquad
T_{n,m}=P_{U_n}A_m|_{U_n},\qquad
E_{n,m}=\sqrt m\,T_{n,m}-R_n.
\]
Take integers \(n\ge8\), \(m\ge n^2\), and \(8\le q\le n\) with the **local** divisibility condition \(q(q-1)\mid m\). Let
\[
\nu_q=g_q-\frac{q-1}{q}g_{q-1}.
\]
Then the exact physical coefficient admits the uniform two-term expansion
\[
\boxed{\begin{aligned}
\langle E_{n,m}g_2,\nu_q\rangle
={}&-\frac{\pi^2}{288m}\left(2-\frac1q\right)\\
&+\frac{7\pi^4}{172800}\frac{q^3}{m^3}
\left[1-\left(1-\frac1q\right)^4\right]
+O\left(\frac{q^5}{m^5}\right).
\end{aligned}}
\tag{1}
\]
The constants in this asymptotic are absolute: there is no assumption that \(m/q^2\) stays bounded, and no Diophantine genericity condition. Since the bracket in the second term is \(O(q^{-1})\), one obtains
\[
\boxed{\langle E_{n,m}g_2,\nu_q\rangle
=-\frac{\pi^2}{288m}\left(2-\frac1q\right)
+O\left(\frac{q^2}{m^3}\right).}
\tag{2}
\]
For every sequence \(m_n\ge n^2\) of integers with \(n(n-1)\mid m_n\), including \(m_n=2n(n-1)\) and \(m_n=n!\),
\[
\boxed{
\liminf_{n\to\infty}
\frac{m_n\sqrt{\log n}}{n}\,\|E_{n,m_n}\|
\ge\frac{\pi^2}{144}\sqrt{\frac2{\log2}}
\approx0.116423>0.
}
\tag{3}
\]
In particular, the first multiple of \(n(n-1)\) satisfying \(m\ge n^2\) is already \(m=2n(n-1)\), and (3) gives the genuinely quadratic-scale specialization
\[
\boxed{
\liminf_{n\to\infty}
n\sqrt{\log n}\,\|E_{n,\,2n(n-1)}\|
\ge \frac{\pi^2}{288}\sqrt{\frac2{\log2}}>0.
}
\tag{3a}
\]
The norm in (3)--(3a) is the physical operator norm on \(U_n\), not an artificial coefficient or Cesaro norm. Its unweighted lower bound decreases as \(n/(m_n\sqrt{\log n})\); no nonzero limiting operator-norm gap is proved.

## 1. Exact integer-phase reduction

In NB-338(13) the adjacent selector coefficient is expressed through
\[
F(x)=\int_x^\infty\frac{\{t\}-\frac12}{t^2}\,dt
\]
as
\[
q\langle E_{n,m}g_2,\nu_q\rangle
=\frac{qu}{2}\sum_{k\ge1}(-1)^{k+1}
\big[F(ku)-F(kv)\big],
\qquad u=\frac mq,\quad v=\frac m{q-1}.
\tag{4}
\]
Indeed \(q(q-1)\mid m\) implies \(m=dq\), \(r=0\), and \(d=m/q\ge q\) since \(m\ge n^2\ge q^2\). Thus the original NB-338 selector identity applies exactly, with no limiting interchange. Both \(u=m/q\) and \(v=m/(q-1)\) are positive integers, and conversely their integrality is equivalent to \(q(q-1)\mid m\) because \(\gcd(q,q-1)=1\). Divisibility by \(\operatorname{lcm}(1,\ldots,n)\) was a sufficient but unnecessary global hypothesis.

For any integer \(a\ge1\), split the integral for \(F(a)\) into unit intervals. Direct integration gives
\[
\int_j^{j+1}\frac{t-j-\frac12}{t^2}\,dt
=\log\frac{j+1}{j}
-\frac12\left(\frac1j+\frac1{j+1}\right).
\tag{5}
\]
Summing (5) from \(j=a\) through \(J\) and sending \(J\to\infty\), using
\(H_J-\log J\to\gamma\), proves the **exact identity**
\[
\boxed{
F(a)=H_a-\log a-\gamma-\frac1{2a},
\qquad H_a=\sum_{j=1}^a\frac1j.
}
\tag{6}
\]
Thus (4) is an alternating series of harmonic-number remainders. It has no residual fractional-part phase for these common-divisibility dilations. The finite \(q\) versus \(q-1\) scale difference remains present.

## 2. Uniform Euler--Maclaurin expansion

Euler--Maclaurin summation, or the equivalent digamma expansion, yields for all positive integers \(a\), with an absolute remainder bound,
\[
H_a-\log a-\gamma-\frac1{2a}
=-\frac1{12a^2}+\frac1{120a^4}+O(a^{-6}).
\tag{7}
\]
The coefficients follow from the classical digamma asymptotic; see the NIST DLMF, section 5.11(i), equation 5.11.2 (https://dlmf.nist.gov/5.11.E2). Enlarging the constant on a finite initial range makes the \(O(a^{-6})\) bound valid uniformly for integers \(a\ge1\).

Put \(c=u/v=(q-1)/q\). Substituting (7) into (4), dividing by \(q\), and absolutely summing the errors gives
\[
\begin{aligned}
\langle E_{n,m}g_2,\nu_q\rangle
={}&-\frac{1-c^2}{24u}
\sum_{k\ge1}\frac{(-1)^{k+1}}{k^2}\\
&+\frac{1-c^4}{240u^3}
\sum_{k\ge1}\frac{(-1)^{k+1}}{k^4}
+O(u^{-5}).
\end{aligned}
\tag{8}
\]
The error is uniform because \(v\ge u\) and
\(\sum_{k\ge1} k^{-6}<\infty\). Evaluate the two classical alternating sums:
\[
\sum_{k\ge1}\frac{(-1)^{k+1}}{k^2}=\frac{\pi^2}{12},
\qquad
\sum_{k\ge1}\frac{(-1)^{k+1}}{k^4}=\frac{7\pi^4}{720}.
\tag{9}
\]
Use \(u=m/q\),
\[
1-c^2=\frac2q-\frac1{q^2},
\qquad
1-c^4=1-\left(1-\frac1q\right)^4\le\frac4q
\]
to obtain (1) and (2). Note that \(m\ge n^2\ge q^2\) gives a relative error \(O(q^2/m^2)=O(n^{-2})\) in (2). Its coefficient is therefore strictly negative, uniformly over permitted \(q,m\), for all sufficiently large \(n\).

By contrast, for the phase profile in NB-342--343,
\[
\mathfrak D(m/q)-\mathfrak D(m/(q-1))=0
\]
**exactly**, because both arguments are integers. Common divisibility kills the leading *phase-contrast observer*, not the full Nyman coefficient. Formula (1) identifies the finite normalization remainder surviving the cancellation.

## 3. Lower bound in the actual Hilbert metric

Select \(q=n\). NB-304(15) proves for the genuine adjacent vector
\[
\|\nu_n\|_2^2
\le\frac{2H_{n-2}+1+\pi^2/18}{n^2},
\]
and the canonical generator obeys \(\|g_2\|_2=\sqrt{\log2}/2\). Cauchy--Schwarz within the actual \(U_n\) yields
\[
\|E_{n,m}\|\ge
\frac{|\langle E_{n,m}g_2,\nu_n\rangle|}
{\|g_2\|_2\|\nu_n\|_2}
\ge
\frac{2n|\langle E_{n,m}g_2,\nu_n\rangle|}
{\sqrt{\log2}\sqrt{2H_{n-2}+1+\pi^2/18}}.
\tag{10}
\]
Since \(H_{n-2}/\log n\to1\), and (2) implies uniformly over admissible \(m\) that
\[
m|\langle E_{n,m}g_2,\nu_n\rangle|
=\frac{\pi^2}{288}\left(2-\frac1n\right)+O(n^2/m^2)
\longrightarrow\frac{\pi^2}{144},
\]
multiplying (10) by \(m\sqrt{\log n}/n\) and taking a limit inferior proves (3). This uses only source and observer vectors that genuinely belong to the canonical finite Nyman section; it makes no assumption about the actual first-free Ford datum or the best-approximation residual.

## 4. Numerical and adversarial controls

The exact series (4) with (6), evaluated at high precision for \(q=n\) and \(m=L_n\), gives
\[
\begin{array}{c|r|r}
(n,m)&\langle E_{n,m}g_2,\nu_n\rangle&
(\text{exact}-\text{first term})/(\text{second term})\\\hline
(8,840)&-7.6492919256718928\cdot10^{-5}&0.9999401\\
(10,2520)&-2.5837999917199398\cdot10^{-5}&0.9999894\\
(12,27720)&-2.3695212313562693\cdot10^{-6}&0.9999999
\end{array}
\]
These are sign/constant checks, not the proof. In particular, applying only the \(O((q\delta)^{-1})\) coarse error of NB-341 at integral phases would *not* recover the sharp coefficient: (6)--(9) are needed to expose its sign and normalization.

Complementary uniformity stress tests are the quadratic sequence \(m=2n(n-1)\), with \(q=n\) and the minimal permitted local multiple, and the far-external sequence \(m=n!\), beyond the window of NB-343. At the endpoint \(q=n\), physical adjacent-vector conditioning costs \(\sqrt{\log n}/n\). Equation (7) is used only at positive integers, so fractional folds introduce no hidden regularity assumption. No fixed-\(n\) convergence statement is silently upgraded to a uniform moving-\(n\) bound.

**Prior-art boundary.** The harmonic/digamma asymptotic is classical (NIST DLMF above). The inner-product arithmetic of the Nyman generators and harmonic-series summation are likewise established themes; see L. Báez-Duarte, *Harmonic Series Summation Lemma and Vasyunin's Formulas*, J. Math. Sci. 120 (2004), 1653--1656, DOI 10.1023/B:JOTH.0000018862.38853.fe, and the Báez-Duarte--Balazard--Landreau--Saias / Balazard--Martin fractional-part autocorrelation works already recorded in this line. No originality is claimed for those tools, nor is an absence of exact-match search results treated as a priority claim. The **line-local mathematical delta** is the locally coprime-divisible specialization of NB-338's exact finite selector coefficient. Only \(q(q-1)\mid m\) is needed, so the physical norm consequence (3) reaches the quadratic scale (3a), not just global lcm multiples. This is an immediate strengthening within the same finite-normalization-residue mechanism, not a best-approximation theorem or an originality claim.

**RH-facing boundary.** The coefficient and bound apply to \(E_{n,m}\), not to
\(d_n=\operatorname{dist}({\bf1},U_n)\). They do not show occupation by the actual Ford target, supply stable inverse-section conditioning, control off-critical zero sampling, or imply RH or its negation. The bound is consistent with rank-one mixing because \(n/(m_n\sqrt{\log n})\to0\) even on the quadratic sequence \(m_n=2n(n-1)\), and faster still for factorial dilations.

## Research consequence

The exact vanishing of reciprocal-phase contrast whenever both adjacent rational phases are integers is a failure of that observer's leading-order discrimination, **not** exact cancellation of the projected-dilation error. Local divisibility \(q(q-1)\mid m\) already forces this phase cancellation, yet a smaller explicitly signed normalization residue survives. At \(q=n\), this happens as early as \(m=2n(n-1)\), rather than requiring factorial or global-lcm dilation. Sharpening source-only lower bounds remains separate from the missing target-occupation bridge.