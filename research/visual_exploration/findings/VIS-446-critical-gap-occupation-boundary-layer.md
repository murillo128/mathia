# VIS-446 — universal critical-gap crossover of occupation moments

## Claim

Let \(E\) be a nonempty proper finite union of disjoint nondegenerate arcs of the unit-speed circle of circumference \(C=2\pi\). Write \(g_1,\ldots,g_K\) for its complementary gap lengths. For \(L\in(0,C)\), set

\[
Z_L(x)=L^{-1}\int_{-L/2}^{L/2}\mathbf1_E(x+u)\,du,\quad
A_n(L)=\int(1-Z_L)^n\,dm_H,\quad
p_L=C^{-1}\sum_i(g_i-L)_+.
\]

Fix one gap length \(g\), let \(N_>=\#\{i:g_i>g\}\) and \(N_==\#\{i:g_i=g\}\), and put \(L_n=g(1+t/n)\) for fixed real \(t\) and sufficiently large \(n\). Then

\[
\boxed{\lim_{n\to\infty}\frac Cg\,n[A_n(L_n)-p_{L_n}]
=2N_>+N_=\Psi(t)},\qquad
\Psi(t)=
\begin{cases}
2,&t\le0,\\
(2+t)e^{-t},&t\ge0.
\end{cases}
\]

**Evidence/status:** EXACT-DERIVED + CLASSICAL INTERVAL-EROSION/ENDPOINT-LAPLACE INGREDIENTS + MATCHED ANALYTIC-POLYNOMIAL CONTROL + NO GENERAL NOVELTY CLAIM. This is a fixed finite-arc statement, not an arithmetic or RH result.

## Uniform local contact identity and proof

There are \(\delta>0\) and \(q\in(0,1)\), depending only on \(E,g\), such that uniformly for \(|L-g|<\delta\) and \(n\ge1\),

\[
A_n(L)-p_L
=\frac1C\left[\frac{2LN_>}{n+1}+N_= B_{n,g}(L)\right]
+O_{E,g}(q^n),
\]

where

\[
B_{n,g}(L)=
\begin{cases}
2L/(n+1),&L\le g,\\
(L-g)(g/L)^n+[2L/(n+1)](g/L)^{n+1},&L\ge g.
\end{cases}
\]

For a complementary gap longer than \(L\), zero-occupation window centers form an interval of length \(h-L\). Subtracting this atom leaves two one-sided linear overlap ramps, each with \(Z_L=u/L\); integration of \((1-u/L)^n\) contributes \(L/(n+1)\) up to an exponentially small truncation.

For a critical gap of length \(g\), the same contact law holds when \(L\le g\). When \(L>g\), window centers that protrude beyond *both* gap endpoints form a central interval of width \(L-g\), with constant target overlap \(L-g\). Its contribution is \((L-g)(g/L)^n\). The two adjacent ramps start at \(Z_L=(L-g)/L\), and each contributes \([L/(n+1)](g/L)^{n+1}\) up to an exponentially small truncation. Gaps strictly shorter than \(g\) are separated from zero occupation by a positive overlap floor in a neighborhood of \(L=g\).

Because the target arcs and the gaps are finitely many and have positive lengths, choose \(\delta\) and the ramp cutoffs small enough that the local intervals do not overlap, gap lengths different from \(g\) stay separated, and all neglected positive-occupation portions have \(Z_L\ge\varepsilon>0\) uniformly. This gives the stated \(O((1-\varepsilon)^n)\) remainder. The proof depends on exact interval geometry, not sampling or the rendering.

Substitute \(L_n=g(1+t/n)\), multiply by \(Cn/g\), and use \((g/L_n)^n\to e^{-t}\), locally uniformly in \(t\). Below the contact transition the critical contribution is \(2\); above it the central plateau contributes \(t e^{-t}\) and the two ramps contribute \(2e^{-t}\). The crossover is continuous at \(t=0\).

## Matched analytic-target controls

Use the two degree-two analytic-polynomial superlevel targets at the common regular threshold constructed in VIS-441:

\[
E_A=[0,\pi/6]\cup[\pi,3\pi/2],\qquad
E_B=[0,\pi/6]\cup[\pi/2,\pi].
\]

They share target Haar mass \(1/3\), directional level-crossing flux \(2/\pi\), and exact analytic Fourier coefficient support \(\{0,1,2\}\), but have complementary gaps \(A:\{5\pi/6,\pi/2\}\) and \(B:\{\pi/3,\pi\}\). At \(g=\pi/2\), target A has one longer gap and one critical gap, while B has one longer gap and no critical gap. Hence

\[
\lim_{n\to\infty}n[A_n^A(L_n)-p^A_{L_n}]
=\begin{cases}
1,&t\le0,\\
\tfrac12+\tfrac{2+t}{4}e^{-t},&t\ge0,
\end{cases}
\qquad
\lim_{n\to\infty}n[A_n^B(L_n)-p^B_{L_n}]
=\tfrac12.
\]

As an independent exact-integration check, rescale the circumference to one. The arcs become \(A:[0,1/12]\cup[1/2,3/4]\), \(B:[0,1/12]\cup[1/4,1/2]\), and the critical gap is \(g=1/4\). For every \(L_n\), partition the window-center coordinate at shifted target-arc endpoints. On each cell \(1-Z_L\) is affine, so its \(n\)-th power integrates by endpoint values without discretization. At \(t=1\), the rescaled A residual \(n[A_n^A-p^A]\) equals \(0.77555242\) at \(n=128\) and \(0.77581990\) at \(n=512\), approaching the exact limit \(0.77590958\). The B residual approaches \(0.5\). At \(t=-1\), A yields \(0.939400517437\), \(0.984496124031\), and \(0.996101364522\) at \(n=32,128,512\), converging to \(1\). This independent window-partition test probes both sides of the critical gap.

## Prior art, boundaries, and consequence

VIS-441 supplies gap erosion and the matched polynomial realizations; VIS-444 introduces the integrated occupation moments; VIS-445 proves their sharp fixed-window \(1/n\) coefficient and identifies the failure of uniformity near a gap length. The present double scaling provides the **contact transition** that cannot be obtained by substituting \(L_n\) into an asymptotic whose exponential error constants depend on fixed \(L\).

The endpoint integral and exponential scaling are classical Watson/Laplace-type ingredients, with the Watson-lemma citation already recorded in the line's SOURCES.md; the NIST DLMF §2.3 (https://dlmf.nist.gov/2.3) discusses nonuniformity and uniform asymptotics near moving boundaries. No claim is made that the abstract transition is new in asymptotic analysis, nor that a precise identical-result precedent has been excluded.

Rotation and rephasing cannot change the result, which depends on the complementary gap lengths. The matched B target rules out mass, crossing flux, common threshold, and Fourier-support equality as sufficient explanations of the transition. A target with infinitely many or shrinking arcs, a varying Wang shell, or a non-circle multidimensional flow needs new uniform geometric and Fourier/Gram bounds. No selected-height anomaly, zeta-zero exclusion, or RH consequence follows from this circle control.
