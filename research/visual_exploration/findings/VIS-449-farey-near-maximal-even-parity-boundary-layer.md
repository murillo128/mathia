# VIS-449 — a parity-resolved spectral boundary layer in near-maximal Farey transport

## Exact claim and evidence

For integer \(k\ge4\), specialize the fixed-inverse, unreflected, three-defect excursion swap of FD-323 to \((a,b)=(k,k+1)\). Put
\[
\alpha_k=1/k,\quad \delta_k=1/(k+1),\quad
\gamma_k=1-\alpha_k-\delta_k,\quad \beta_k=1-\delta_k,
\quad A_k=1-\alpha_k,\quad B_k=\delta_k-\alpha_k.
\]
The continuum rank transport from FD-323 is
\[
g_k(t)=
\begin{cases}
A_k,&0<t<\gamma_k,\\
B_k,&\gamma_k<t<\beta_k,\\
0,&\beta_k<t<1.
\end{cases}
\]
Define \(I_{k,m}=\int_0^1g_k(t)\sin(\pi mt)\,dt\) and the total continuum energy
\[
d_k=\int_0^1g_k(t)^2dt=\gamma_k A_k^2+\alpha_k B_k^2.
\]
The normalized full Dirichlet sine-mode probabilities are \(P_k(m)=2I_{k,m}^2/d_k\), \(m\ge1\).

**The parity-and-scale conclusion is exact/asymptotic as follows.** The unnormalized even-mode energy \(e_k=\sum_{j\ge1}2I_{k,2j}^2\) obeys
\[
\boxed{\ e_k=\tfrac12(\delta_k A_k^2+\alpha_k\beta_k^2),\qquad
e_k/d_k\sim 1/k.\ } \tag{1}
\]
For every fixed even mode, \(I_{k,m}=O(m/k^2)\). Nevertheless, **after conditioning on the vanishing even sector**, the probability measures
\[
\nu_k=\sum_{j\ge1}\frac{2I_{k,2j}^2}{e_k}\,\delta_{2j/k}
\]
converge weakly on \([0,\infty)\) to the probability density
\[
\boxed{\ f(x)=\frac{(1-\cos 2\pi x)^2}{\pi^2x^2},\quad x>0,
\qquad f(0)=0,\qquad\int_0^\infty f(x)\,dx=1.\ } \tag{2}
\]
In particular, for a cutoff \(q_k\), the conditional even-band fraction tends to zero when \(q_k/k\to0\); when \(q_k/k\to X\in(0,\infty)\), it tends to \(\int_0^X f(x)\,dx\); and when \(q_k/k\to\infty\), it tends to one. This isolates a parity-resolved transition at sine index \(m\asymp k\), even though the **unconditioned** near-maximal spectrum becomes odd-only.

**Evidence/status:** EXACT-DERIVED + CLASSICAL SINE-PARSEVAL/REFLECTION DECOMPOSITION + FD-323 FIXED-PRIME-LIMIT SPECIALIZATION + VIS-447 TRANSFER + NEGATIVE PARITY-NORMALIZATION CONTROL. No novel general Fourier theorem, genuine-Farey anomaly, or RH implication is claimed.

## Exact finite-step calculation and reflection identity

Direct integration of the two nonzero intervals gives, for every integer \(m\ge1\),
\[
I_{k,m}=\frac{A_k-\beta_k\cos(\pi m\gamma_k)-B_k\cos(\pi m\beta_k)}{\pi m}. \tag{3}
\]
Here \(A_k-B_k=\beta_k\). For even \(m\), using \(\cos(\pi m\gamma_k)=\cos(\pi m(\alpha_k+\delta_k))\) and \(\cos(\pi m\beta_k)=\cos(\pi m\delta_k)\),
\[
I_{k,m}=
\frac{\beta_k[1-\cos(\pi m(\alpha_k+\delta_k))]
+B_k[1-\cos(\pi m\delta_k)]}{\pi m}. \tag{4}
\]
Consequently \(|I_{k,m}|\le C m/k^2\) for \(m\le k\), and \(|I_{k,m}|\le C/m\) uniformly in \(k,m\). The former is the low-even-mode cancellation; the latter ensures a controlled spectral tail.

The reflection operator \(Rg(t)=g(1-t)\) acts on \(\sin(\pi mt)\) by \((-1)^{m+1}\). Thus the even sine modes are precisely the antisymmetric-under-reflection projection. Since \(k\ge4\), the intervals \((0,\delta_k),(\delta_k,\alpha_k+\delta_k),(\alpha_k+\delta_k,\gamma_k),(\gamma_k,\beta_k),(\beta_k,1)\) occur in that order and \(g_k-Rg_k\) takes values \(A_k,\beta_k,0,-\beta_k,-A_k\), respectively. By sine Parseval,
\[
\sum_{j\ge1}2I_{k,2j}^2
=\left\|\tfrac12(g_k-Rg_k)\right\|_{L^2}^2
=\tfrac12(\delta_kA_k^2+\alpha_k\beta_k^2),
\]
proving (1), since \(k e_k\to1\) and \(d_k\to1\). The odd parity sector carries the remaining mass \(1-e_k/d_k\to1\), consistent with the odd-only nested limit of FD-323.

## Boundary-layer limit and normalization

For even \(m\) with \(m/k\to x\in(0,\infty)\), (4) and \(\alpha_k+\delta_k\sim2/k\), \(B_k=O(k^{-2})\) imply
\[
k I_{k,m}\longrightarrow \frac{1-\cos(2\pi x)}{\pi x}.
\]
The even-mode mesh in \(x=m/k\) has spacing \(2/k\), while \(e_k\sim1/k\); hence the conditional mass per mode is asymptotic to \((2/k)f(x)\). This is a Riemann sum on compact subintervals of \((0,\infty)\), not a continuum replacement assumed without error control.

For \(m\le\varepsilon k\), (4) and \(1-\cos u\le u^2/2\) imply that the conditional mass below \(\varepsilon\) is \(O(\varepsilon^3)\), uniformly for large \(k\). For \(m\ge Rk\), (3) gives a conditional tail \(O(R^{-1})\). These two bounds provide tightness and exclude escaped mass at the endpoints, establishing (2) and the cutoff conclusions. The limiting density integrates to one exactly, because
\[
(1-\cos 2\pi x)^2
=2(1-\cos 2\pi x)-\tfrac12(1-\cos 4\pi x)
\]
and the classical integral \(\int_0^\infty(1-\cos(cx))x^{-2}dx=\pi c/2\) for \(c>0\) gives total integral \(\pi^2/\pi^2=1\). This also reconciles the noncommuting limits: fixed even modes vanish faster than total even-sector energy, which is concentrated on frequencies growing with \(k\).

## Transfer to the artificial Farey controls

For **each fixed** \(k\), FD-323 constructs infinitely many primes \(p\) in the required reduced progression, and its exact three-defect reassembled discrepancy \(D_{p,k}^\star\) has total energy tending to \((3/\pi^2)d_k>0\). Its fixed sine-mode coefficients tend to \((\sqrt6/\pi)I_{k,m}\), and fixed-mode limits exhaust the total energy by sine Parseval. The VIS-447 total-variation bound applies because the exact excursion transport has \(T_{p,k}\to(3/\pi^2)d_k>0\), while genuine Farey energy \(E_p=o(1)\). Therefore, **first letting \(p\to\infty\) with \(k\) fixed**, the full normalized sine distribution of the reconstructed path converges to \(P_k\). Only **after that** may one send \(k\to\infty\) to obtain (1)–(2).

Since the even-sector denominator behaves as \(1/k\), an arbitrary simultaneous \(p,k\to\infty\) transfer requires errors \(o(1/k)\) in unconditioned spectral total variation (as well as adequate resolution of modes \(m\asymp k\)), not merely \(o(1)\). A sufficiently slow diagonal can be chosen from the fixed-\(k\) convergence, but no uniform quantitative prime-progressions theorem is supplied here. These artificial denominator-edge controls are **not additional genuine Farey sequences**.

The true Farey discrepancy and FD-319's reflected comparator have the opposite parity constraint: reflection symmetry of the grid forces *odd sine coefficients to vanish*. Hence the reflection-specific even-band null expectation of VIS-032/VIS-034 cannot be transplanted to this unreflected FD-323 family. An apparent disappearance of low even energy under such a transplant is a **parity/normalizer artifact**, not an arithmetic source-order certificate. Even after normalizing by this control's own even energy, its fixed-even-band fraction vanishes and its effective bandwidth scales as \(k\).

## Independent checks, prior art, and scope

For \(k=4,16,64,256\), direct sine-integral summation with large even-mode cutoffs agrees with the closed reflection energy in (1) to the expected \(O(1/M)\) Fourier-tail precision. The values of \(k e_k\) are approximately \(0.5450,0.85651,0.96178,0.99029\), respectively. Numerical integration of (2) and Riemann-sum conditional band fractions for \(k=16,64,256,1024\) agree toward the stated limiting cumulative distribution; the low-\(x\) and high-\(x\) bounds, not the plot or numerics, establish the theorem.

The reflection projections, orthogonal sine series, Parseval identity, and step-function spectral concentration are classical Fourier analysis; see Stein and Shakarchi, *Fourier Analysis: An Introduction* (Princeton, 2003), already anchored in this line's SOURCES.md, and John P. Boyd, *Chebyshev and Fourier Spectral Methods*, revised 2nd ed. (Dover, 2001), for symmetry/parity in Fourier methods. FD-323 supplies the source-specific fixed-inverse block construction and nested near-maximal step; VIS-447 supplies the necessary uniform all-mode *within-fixed-\(k\)* transfer. The Mathia-specific contribution is the **exact parity leakage coefficient and its conditional mesoscopic spectral law**, which prevent a misleading comparison of incompatible Farey controls. No exhaustive external priority assertion is made.

The theorem predicts neither the genuine Farey low-band distribution nor a false positive under a **properly** transport-, parity-, and model-normalized null. It cannot replace a specified control ensemble with a single deterministic artificial path, cannot infer significance from null expectations alone, and does not give a new Franel–Landau estimate. If one asks whether a genuine Farey allocation anomaly survives matched controls, the parity constraint and full-mode/conditional denominator must first be fixed and recalculated separately.

## Research consequence

The local near-maximal Farey clue is accepted for further testing, rather than resolved. Its first quantitative calibration is now explicit: under the nested FD-323 control, even-sector mass decays as \(1/k\), while its *conditional* even spectrum has a nontrivial \(m/k\) boundary layer. A future source-natural null comparison must predefine full-mode versus parity-conditional statistics, appropriate model-specific normalizers, and joint prime/cutoff limits. Reflection mismatch alone cannot be reported as evidence of arithmetic spectral depletion.