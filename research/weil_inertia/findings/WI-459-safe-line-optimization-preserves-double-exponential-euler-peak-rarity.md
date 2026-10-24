# WI-459 — safe-line optimization preserves double-exponential Euler-peak rarity

**Status:** LITERATURE+EXACT-DERIVED + SOURCE-FAMILY-OBSTRUCTION + CLASSICAL-DISCRETIZATION + NO-NOVELTY-CLAIM + NON-RH

**Local dependencies:** [WI-457](WI-457-normalized-euler-hankel-symbols-have-local-blindness-and-recurrent-peaks.md), for the exact response and pole limit; [WI-458](WI-458-euler-hankel-peaks-have-exponentially-small-height-density.md), for fixed-parameter height-density and finite-window bounds.

## The optimized observable

Use the normalized, absolutely convergent Euler symbols
\[
L(s)=-\frac{\zeta'(s)}{\zeta(s)},\qquad
A_\varepsilon=L(1+\varepsilon),\qquad
\varphi_\varepsilon(t)=\frac{L(1+\varepsilon+it)}{A_\varepsilon},
\quad \varepsilon>0.
\]
With Fourier phase \(e^{-it\xi}\), negative-frequency projection \(P_-\), and unit positive-Hardy kernel
\[
k_{r,\gamma}(t)=\frac{\sqrt{r/\pi}}{r-i(t-\gamma)},
\]
define
\[
Q_\varepsilon(r,\gamma)=\|P_-(\varphi_\varepsilon k_{r,\gamma})\|_2^2,
\qquad M_r(\gamma)=\sup_{\varepsilon>0}Q_\varepsilon(r,\gamma).
\tag{1}
\]
The packet width \(r>0\) is fixed while taking this supremum and while averaging height. The safe-line offset \(\varepsilon\) may be chosen after observing \(\gamma\), with no restriction on the selection rule.

For a measurable height set \(E\), write
\[
d^*(E)=\limsup_{H\to\infty}\sup_T\frac{|E\cap[T,T+H]|}{H},\qquad
d_*(E)=\liminf_{H\to\infty}\inf_T\frac{|E\cap[T,T+H]|}{H}.
\]
For each fixed \(0<\tau<1\), there are positive constants \(c_\tau,C_\tau,r_\tau\) such that, for \(0<r<r_\tau\),
\[
\boxed{d^*\{M_r\ge\tau\}\le\exp[-\exp(c_\tau/r)].}
\tag{2}
\]
The stronger finite-window statement holds after possibly changing these constants:
\[
\boxed{H\ge\exp[\exp(C_\tau/r)]
\quad\Longrightarrow\quad
\sup_T\frac{|\{\gamma\in[T,T+H]:M_r(\gamma)\ge\tau\}|}{H}
\le\exp[-\exp(c_\tau/r)].}
\tag{3}
\]
For every fixed \(0<\tau<1/4\), there is also \(D_\tau>0\) such that
\[
\boxed{d_*\{M_r>\tau\}\ge\exp[-\exp(D_\tau/r)]}
\tag{4}
\]
for sufficiently small \(r\). The global optimized maximum has the exact limiting value
\[
\boxed{\lim_{r\downarrow0}\sup_{\gamma\in\mathbb R}M_r(\gamma)=\frac14.}
\tag{5}
\]
Thus parameter selection does not change the broad double-exponential rarity scale. The maximum in (5) remains present; this is not uniform decay of the family over all heights. The assertions concern Lebesgue height measure, with no implication for the number or locations of off-critical zeros.

## An order-one response forces comparable source and packet scales

Write the positive coefficient probability measure on logarithmic frequencies as
\[
a_{\varepsilon,n}=\frac{\Lambda(n)n^{-1-\varepsilon}}{A_\varepsilon},
\qquad \nu_\varepsilon=\sum_{n\ge2}a_{\varepsilon,n}\delta_{\log n}.
\]
The ordinary pole expansion and positivity give absolute comparison constants in
\[
A_\varepsilon\asymp\varepsilon^{-1},\qquad
m_\varepsilon:=\int x\,d\nu_\varepsilon(x)
=\frac{-L'(1+\varepsilon)}{A_\varepsilon}
\ll\varepsilon^{-1}
\quad(0<\varepsilon\le1).
\tag{6}
\]
At the other end, \(\sup_{\varepsilon\ge1}m_\varepsilon<\infty\). Indeed the \(n=2\) term gives \(A_\varepsilon\ge(\log2)2^{-1-\varepsilon}\), whence
\[
m_\varepsilon\le\frac1{\log2}
\sum_{n\ge2}\Lambda(n)\log n\,(2/n)^2<\infty
\qquad(\varepsilon\ge1).
\tag{7}
\]

The exact WI-457 response has a nonnegative coefficient before each cosine, so
\[
0\le Q_\varepsilon(r,\gamma)\le Q_\varepsilon(r,0)
=\iint\big(e^{-r|x-y|}-e^{-r(x+y)}\big)
\,d\nu_\varepsilon(x)d\nu_\varepsilon(y).
\tag{8}
\]
Since the integrand equals
\(e^{-r|x-y|}(1-e^{-2r\min(x,y)})\le2rx\), equations (6)--(7) imply
\[
Q_\varepsilon(r,\gamma)\ll r/\varepsilon\quad(0<\varepsilon\le1),
\qquad Q_\varepsilon(r,\gamma)\ll r\quad(\varepsilon\ge1).
\tag{9}
\]

The opposite mismatch \(\varepsilon\ll r\) needs an additional elementary arithmetic bound. Chebyshev's estimate
\(\psi(X)=\sum_{n\le X}\Lambda(n)\ll X\) gives, for every integer \(j\ge0\),
\[
\begin{aligned}
\nu_\varepsilon([j,j+1))
&\le A_\varepsilon^{-1}e^{-(1+\varepsilon)j}\psi(e^{j+1})\\
&\ll\varepsilon e^{-\varepsilon j}\le C_0\varepsilon,
\qquad 0<\varepsilon\le1.
\end{aligned}
\tag{10}
\]
This controls mass in fixed unit logarithmic intervals; it assumes no prime estimate in shrinking intervals. For any \(x\ge0\), the geometric sum over these intervals satisfies
\[
\sum_{j\ge0}\sup_{y\in[j,j+1)}e^{-r|x-y|}
\le1+\frac2{1-e^{-r}}\ll r^{-1}
\qquad(0<r\le1).
\]
Dropping the subtracted nonnegative term in (8), then applying (10) to the inner integral, proves
\[
Q_\varepsilon(r,\gamma)\ll\varepsilon/r
\qquad(0<r,\varepsilon\le1).
\tag{11}
\]
Consequently one absolute \(C\ge1\) can be fixed such that
\[
\boxed{Q_\varepsilon(r,\gamma)
\le C\min\{r/\varepsilon,\varepsilon/r\}\quad(0<r,\varepsilon\le1),
\qquad Q_\varepsilon(r,\gamma)\le Cr\quad(\varepsilon\ge1).}
\tag{12}
\]
All these bounds are uniform in height. For fixed \(\tau>0\), if \(r\) is sufficiently small and \(Q_\varepsilon(r,\gamma)\ge\tau/2\), then
\[
\alpha_\tau r\le\varepsilon\le\beta_\tau r<1,
\qquad \alpha_\tau=\frac{\tau}{2C},\quad
\beta_\tau=\frac{2C}{\tau}.
\tag{13}
\]
The harmless threshold \(\tau/2\) ensures that an approximating sequence for the supremum in (1) cannot escape this compact interval when \(M_r(\gamma)\ge\tau\). Continuity in \(\varepsilon\) then makes that superlevel supremum attained inside the interval. This avoids assuming attainment at the outset.

## Uniform continuity turns optimization into finitely many tests

Differentiating the absolutely convergent coefficients gives
\[
\partial_\varepsilon a_{\varepsilon,n}
=a_{\varepsilon,n}(m_\varepsilon-\log n),\qquad
\sum_n|\varepsilon\partial_\varepsilon a_{\varepsilon,n}|
\le2\varepsilon m_\varepsilon\le K
\quad(0<\varepsilon\le1),
\tag{14}
\]
for an absolute \(K>0\). Termwise differentiation is uniform on each closed subinterval of \((0,1]\); integrating the resulting bound yields
\[
\|\varphi_\varepsilon-\varphi_{\varepsilon'}\|_\infty
\le K|\log(\varepsilon/\varepsilon')|.
\]
Contractivity of \(P_-\), the unit norm of the kernel, and the reverse triangle inequality now give
\[
\boxed{|\sqrt{Q_\varepsilon(r,\gamma)}-
\sqrt{Q_{\varepsilon'}(r,\gamma)}|
\le K|\log(\varepsilon/\varepsilon')|}
\quad(0<\varepsilon,\varepsilon'\le1).
\tag{15}
\]
The packet width is unchanged in this comparison. Neither a derivative of \(k_{r,\gamma}\) nor a height-dependent continuity constant is being suppressed.

Choose a finite grid \(\theta_1,\ldots,\theta_J\) in
\([\alpha_\tau,\beta_\tau]\) so every point of this interval is within
\(\sqrt\tau/(2K)\) of some grid point in logarithmic distance. Both the grid and its size \(J\) depend only on \(\tau\), not on \(r\), the height, or the averaging window. Equations (13)--(15) prove the pointwise inclusion
\[
\boxed{\{\gamma:M_r(\gamma)\ge\tau\}
\subseteq\bigcup_{j=1}^J
\{\gamma:Q_{\theta_jr}(r,\gamma)\ge\tau/4\}.}
\tag{16}
\]
Measurability is also immediate: continuity in \(\varepsilon\) expresses (1) as the supremum over positive rational parameters. No interchange of an uncountable supremum and an averaged estimate is used.

## Transfer of the fixed-parameter concentration bounds

For each grid point, set
\(\varepsilon_j=\theta_jr\) and \(q_j=1/\theta_j\). Then
\(r=q_j\varepsilon_j\), with \(q_j\) fixed as \(r\downarrow0\). WI-458 equations (5a) and (5c), applied at threshold \(\tau/4\), give positive constants \(b_j,B_j\) such that
\[
d^*\{Q_{\theta_jr}(r,\cdot)\ge\tau/4\}
\le\exp[-\exp(b_j/r)]
\tag{17}
\]
and the same upper bound for every interval fraction once
\(H\ge\exp[\exp(B_j/r)]\), after adjusting constants and the small-\(r\) threshold. The factors \(\theta_j^{-1}\) have been absorbed into these constants.

For clarity, the imported statement is about the **coherent Hilbert-valued** Hankel response, not an incoherent sum of separate prime-power energies. WI-458 groups dependent powers of each prime together, bounds the squared sensitivities of the independent prime blocks, and splits off small primes before applying bounded differences. Its finite-window proof retains the actual integer frequencies in a Hilbert tensor power and applies Montgomery--Vaughan's mean-value bound. No probabilistic independence at deterministic zero ordinates is part of that statement.

Finite subadditivity and (16) bound the optimized density by
\(J\exp[-\exp(b/r)]\), where \(b=\min_j b_j>0\). For sufficiently small \(r\), this is at most \(\exp[-\exp(b/(2r))]\). Taking the maximum of the finitely many \(B_j\), and enlarging it if needed, proves the same conclusion for the finite-window bound. This proves (2)--(3). In particular no uniform-in-\(q\) version of WI-458 is assumed: only finitely many fixed \(q_j\) occur.

For (4), use the single allowed choice \(\varepsilon=r\). The pointwise inequality \(M_r\ge Q_r(r,\cdot)\) and WI-458 equation (5b), with \(q=1\), prove the lower bound for every fixed threshold strictly below \(1/4\).

## The global maximum remains the pole-scale maximum

Equation (8) gives
\[
\sup_\gamma M_r(\gamma)=M_r(0)=\sup_{\varepsilon>0}Q_\varepsilon(r,0).
\tag{18}
\]
For every fixed \(\theta>0\), WI-457's pole limit, used with \(\varepsilon=\theta r\) and \(q=1/\theta\), gives
\[
Q_{\theta r}(r,0)\longrightarrow\frac{\theta}{(1+\theta)^2}.
\tag{19}
\]
On every compact interval of positive \(\theta\), convergence is uniform: (15) gives a common continuity bound for the square roots in \(\log\theta\), and a finite-grid argument upgrades the pointwise limit to uniform convergence. The limiting function is continuous there.

For any fixed \(0<\eta<1/4\), choose \(0<a<1<b\) so \(Ca<\eta\) and \(C/b<\eta\). Equation (12) bounds the response outside \(a\le\varepsilon/r\le b\) by \(\eta\), except for \(\varepsilon\ge1\), where it is at most \(Cr\). Inside this compact ratio interval, (19) gives a limiting supremum of \(1/4\), attained at \(\theta=1\). This proves (5). It does not assert an exact finite-\(r\) maximum of \(1/4\), or decide the superlevel set at the threshold \(\tau=1/4\).

## Consequences and falsification controls

WI-458 explicitly kept \(\varepsilon\) fixed while averaging and did not bound height-adaptive parameter selection. The new ingredient is the **two-sided scale localization** (12), especially its \(\varepsilon/r\) bound from Chebyshev logarithmic-bin mass. Together with (15), it resolves that particular quantifier gap: every selector \(\varepsilon=\varepsilon(\gamma,r)>0\) lies below the same optimized observable, and therefore obeys (2)--(3) whenever its response is measurable.

The comparison is at a fixed packet width and fixed positive threshold. It does not control an additional arbitrary height-adaptive packet width, thresholds tending to zero, arbitrary translations of each symbol, signed coefficient redesign, or an unnormalized logarithmic derivative. Nor does it shorten the windows required by (3). The narrow pole peak already supplies a lower obstruction to a much shorter uniform-in-starting-height window, as in WI-458.

The essential controls are as follows. The limit \(\varepsilon\to\infty\) gives a single low-frequency tone and response \(O(r)\), consistently with (7)--(9). The limit \(\varepsilon/r\to0\) is suppressed by (10)--(11), even at recurrent phase alignments. The limit \(r/\varepsilon\to0\) is suppressed by the first moment in (9). At comparable scales, the pole model saturates (19), so a claim of global vanishing is false. The net is finite independently of \(r\); a countable union of fixed-parameter upper-density estimates alone would not justify (2). Prime powers remain dependent within their prime blocks. Every series manipulation uses \(\varepsilon>0\) before any limit.

For a Kunik shallow packet with \(r=(1-\vartheta)d\) and fixed \(0<\vartheta<1\), the estimates preserve a double-exponential upper bound on the *height frequency* of order-one response even after adapting the safe line. They do not show that actual exceptional zero ordinates avoid the rare set: a set of zero Lebesgue density can contain an entire discrete zero set. No new simple-zero proportion, exclusion of an individual off-line block, or RH conclusion follows. The missing input remains arithmetic control of alignment with the actual divisor.

## Prior art and evidence boundary

Chebyshev's \(\psi(X)\ll X\) is classical. Noam D. Elkies, *Math 229: Introduction to Analytic Number Theory — Čebyšev (and von Mangoldt and Stirling)*, Harvard course notes (2010), p. 3, gives \(\psi(X)\le(2\log2)X+O(\log^2X)\) ([author-hosted notes](https://people.math.harvard.edu/~elkies/M229.09/chebi.pdf)). Only this coarse upper bound, the Euler expansion and the real pole normalization are needed for (10)--(12); no prime number theorem or new zero-free estimate is used in the reduction.

The concentration and finite-window inputs are already reconstructed in WI-458 from Colin McDiarmid's bounded-differences method and H. L. Montgomery and R. C. Vaughan, *Hilbert's Inequality*, **J. London Math. Soc.** (2) 8 (1974), 73--82, Corollary 3, equation (1.11) ([author-hosted paper](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)). Youness Lamzouri, *The distribution of Euler-Kronecker constants of quadratic fields*, [arXiv:1410.1603](https://arxiv.org/abs/1410.1603), Theorem 1.2, supplies neighboring scalar double-exponential Euler-model prior art; its sharp scalar constants are not asserted here.

Continuity estimates and discretization of Euler-model suprema are also established methods: Louis-Pierre Arguin and Frédéric Ouimet, *Large deviations and continuity estimates for the derivative of a random model of log |ζ| on the critical line*, [arXiv:1807.04860](https://arxiv.org/abs/1807.04860), study a different, truncated critical-line random field. Their continuum-to-grid estimate is relevant prior art for the method, not an imported theorem about this safe-line parameter or Hankel observable. Here the finite grid follows directly from (12)--(15).

The mathematical delta is a proved extension from fixed-parameter rare peaks to the supremum over the whole safe-line family, with two-sided mismatch control and a sharp limiting global maximum. It is a source-specific application of classical estimates and a finite covering argument, with no claim of a new concentration theorem or literature priority. The evidence is an analytic derivation with explicit local dependencies; it is neither numerical evidence nor a Lean-verified proof.
