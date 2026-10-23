# AF-573 — Near-threshold smooth calibration localizes prime-edit information

## Status and experiment

EXACT-DERIVED · LITERATURE+DERIVED · ARITHMETIC-FIDELITY · CALIBRATION-MISSPECIFICATION · SHARP-LOCAL-MINIMAX · MATCHED-CONTROL · NO-GENERAL-NOVELTY-CLAIM

AF-572 fixes the smooth-calibration budget before shrinking the window. Its below-threshold certificate requires the signed source derivative to exceed the nuisance budget throughout that window. For a **first-derivative bound**, the regime where this inequality changes sign inside the window has a different answer: the surviving information concentrates near the excluded endpoint, and every fixed finite design aliases before the full curve does.

Retain the registered generalized-prime edit curves
\[
 P(s)=\sum_{\ell\ {\rm prime}}\ell^{-s},\quad
 h_p(s)=p^{-s}-(p+1)^{-s},\quad
 \Phi_p(a)=(P-h_p)^{-1}(E_1(a)),\quad
 E_1(a)=\int_a^\infty e^{-u}\frac{du}{u}.
\tag{1}
\]
Fix a known finite candidate set \(S=\{p_1<\cdots<p_m\}\), \(m\ge2\), of sufficiently large odd rational-prime edit locations. Observe
\[
 y(a)=\Phi_p(a)+b(a)+\eta(a),\quad 0<a\le A,\qquad
 b\in C^1[0,A],\quad \|b'\|_\infty\le L,\quad |\eta|\le\varepsilon.
\tag{2}
\]
One nuisance function is shared within an experiment; competing source hypotheses may have different functions. Its constant term is unrestricted. The derivative bound refers to the retained coordinate \(a\).

Write \(\varepsilon_{\rm full}(A,S,L)\) for the supremal noise radius permitting unique identification from the full window, \(\varepsilon_T\) for a fixed finite set of query coordinates, and \(\varepsilon_2\) for the supremum over legal two-point designs. Zero radius means no positive guaranteed noise margin; exact noiseless aliases are stated separately.

## Exact margin throughout the calibration transition

There is \(A_0(S)>0\), **independent of \(L\)**, on which all adjacent gaps \(G_i=\Phi_{p_{i+1}}-\Phi_{p_i}\) satisfy \(G_i'>0\), \(G_i''<0\), and one gap \(g=G_{i_*}\) has
\[
 0<g'(a)\le G_i'(a)\qquad(0\le a\le A_0,\ i<m).
\tag{3}
\]
The source justification is given below. Put
\[
 d=g'(0)>0,\qquad k=-g''(0)>0,\qquad L_{\rm crit}=d/2.
\tag{4}
\]
For every \(0<A\le A_0\) and **every** \(L\ge0\),
\[
 \boxed{\displaystyle
 \varepsilon_2(A,S,L)=\varepsilon_{\rm full}(A,S,L)
 =\frac14\max_{0\le t\le A}\{g(t)-2Lt\}
 =\frac14\int_0^A(g'(a)-2L)_+\,da.}
\tag{5}
\]
Here \(g(0)=0\). If \(L<L_{\rm crit}\), the maximizer is
\[
 t_L=\begin{cases}
 A,&2L\le g'(A),\\
 (g')^{-1}(2L),&g'(A)<2L<d.
 \end{cases}
\tag{6}
\]
The closed-window optimal pair is \((0,t_L)\); legal positive pairs approach its margin. Thus (5) is equality of suprema. One query fails even at zero noise because its value can always be matched by a constant nuisance. If \(L\ge L_{\rm crit}\), the least-gap pair aliases exactly on the full window via nuisances \(g/2\) and \(-g/2\).

For fixed \(A\), write the remaining derivative-budget slack as
\(\delta=d-2L\). As \(\delta\downarrow0\),
\[
 \boxed{\displaystyle t_L=\frac{\delta}{k}+O_S(\delta^2),\qquad
 \varepsilon_{\rm full}=\frac{\delta^2}{8k}+O_S(\delta^3).}
\tag{7}
\]
When \(g'(A)\le2L<d\), the derivative-crossing point has been reached, and enlarging the window within \([0,A_0]\) adds no margin. This quadratic slack law cannot be obtained by using AF-572's fixed-\(L\) leading term \(\delta A/4\) uniformly up to the threshold.

There is also an explicit joint window/slack transition. For \(A\downarrow0\) with \(\delta=kA\tau\), uniformly for \(\tau\) in any fixed bounded interval,
\[
 \varepsilon_{\rm full}=\frac{kA^2}{4}\Psi(\tau)+O_S(A^3),\qquad
 \Psi(\tau)=\begin{cases}
 0,&\tau\le0,\\
 \tau^2/2,&0<\tau\le1,\\
 \tau-1/2,&\tau\ge1.
 \end{cases}
\tag{8}
\]
For \(\tau\le0\) the margin is exactly zero. Equation (7), rather than the absolute remainder in (8), controls relative accuracy when \(\tau\to0\).

## A finite design has an earlier alias threshold

For any fixed finite legal design \(T\) with at least two distinct points,
\[
 \boxed{\displaystyle
 \varepsilon_T(A,S,L)
 =\frac14\max_{x<y,\ x,y\in T}
       [g(y)-g(x)-2L(y-x)]_+.}
\tag{9}
\]
If \(u<v\) are its two smallest points, strict concavity gives
\[
 L_T:=\frac12\max_{x<y\in T}\frac{g(y)-g(x)}{y-x}
 =\frac{g(v)-g(u)}{2(v-u)}<L_{\rm crit}.
\tag{10}
\]
Thus \(\varepsilon_T>0\) exactly when \(L<L_T\). For every
\(L_T<L<L_{\rm crit}\), two sources have **identical noiseless data on \(T\)** although the full curve has a positive margin. This exact alias assertion uses strict inequality; no attainment claim at \(L=L_T\) is needed.

The obstruction persists even if the otherwise excluded endpoint zero is added to a finite design: its second point is still positive and its first secant slope is strictly below \(d\). For two smallest nodes \(u,v\to0\),
\[
 d-2L_T=\frac{k}{2}(u+v)+O_S(v^2).
\tag{11}
\]
Consequently, fixed positive sampling fractions \(u=x_0A,v=x_1A\) have a transition at \(\tau=(x_0+x_1)/2+O_S(A)\), while the continuum remains identifiable for every \(\tau>0\). The equality \(\varepsilon_2=\varepsilon_{\rm full}\) requires designs that may depend on the known budget \(L\); there is no single finite design that stays identifiable for all \(L<L_{\rm crit}\).

## Proof: a clipped derivative and a finite-data envelope

The difference of two nuisance classes in (2) is exactly
\(\{b\in C^1[0,A]:\|b'\|_\infty\le2L\}\). For any source gap \(h\), the distance between its two noiseless observation classes is
\[
 D(h)=\inf_{\|b'\|_\infty\le2L}\|h-b\|_\infty.
\tag{12}
\]
The supremal two-source noise radius is \(D(h)/2\); for a finite candidate set take the least pairwise distance. The factor \(2L\) compares two calibrations, and the later factor \(1/2\) compares two observation-error balls.

Let \(C=2L<d\), \(H(a)=g(a)-Ca\), and \(H_*=H(t_L)>0\). The explicit approximant
\[
 b_*(a)=\begin{cases}
 Ca+H_*/2,&a\le t_L,\\
 g(a)-H_*/2,&a\ge t_L
 \end{cases}
\tag{13}
\]
belongs to \(C^1[0,A]\) and satisfies \(0\le b_*'\le C\). At an interior join, \(g'(t_L)=C\); if \(t_L=A\), only the first branch is needed. The residual increases from \(-H_*/2\) to \(H_*/2\) and is constant thereafter. Thus \(D(g)\le H_*/2\).

Conversely, any positive source gap \(h=\sum G_i\) has \(h'\ge g'\) by (3). For every admissible \(b\),
\[
 2\|h-b\|_\infty\ge
 h(t_L)-h(0)-[b(t_L)-b(0)]\ge H_*.
\tag{14}
\]
This lower bound uses only \((0,t_L)\), applies to every source pair, and is sharp for \(g\) by (13). Moving zero to a positive coordinate changes the source increments and the bound \(C(t_L-x)\) continuously, proving the legal-design supremum. If \(C\ge d\), \(\|g'\|_\infty=d\le C\), so \(g\) itself is an admissible difference nuisance and gives the claimed exact alias. This proves (5).

For completeness, the finite-set distance formula used in (9) holds for any real data \(f\) on \(T\):
\[
 \inf_{\|b'\|_\infty\le C}\max_{x\in T}|f(x)-b(x)|
 =\frac12\max_{x,y\in T}[|f(y)-f(x)|-C|y-x|]_+.
\tag{15}
\]
Let the maximum on the right before the factor \(1/2\) be \(E\). Pairwise subtraction gives the lower bound. The classical lower Lipschitz envelope
\(q(z)=\min_{x\in T}\{f(x)+C|z-x|\}\)
satisfies \(0\le f-q\le E\) on \(T\); hence \(q+E/2\) attains error at most \(E/2\) in the Lipschitz class. Convolution with a smooth nonnegative unit-mass kernel approximates this globally Lipschitz extension uniformly without increasing its Lipschitz constant. Restriction to \([0,A]\) gives smooth approximants with \(\|b'\|_\infty\le C\), proving the same **infimum** in the stated \(C^1\) class. For \(C=0\), the midpoint constant suffices. Every positive source gap has increments at least those of \(g\), so (15), followed by the observation-noise factor, proves (9).

For the exact noiseless finite-design alias when \(C>2L_T\), interpolate \(g|_T\) piecewise linearly and extend constantly outside the extreme nodes. Its Lipschitz constant is \(2L_T<C\). Smooth it by convolution, then correct its finitely many value errors with fixed smooth cardinal functions on \([0,A]\). As the smoothing scale vanishes, the correction's derivative norm tends to zero, so the strict derivative slack preserves \(\|b'\|_\infty<C\) while making \(b|_T=g|_T\) exactly. The two nuisances \(\pm b/2\) are admissible and give identical sampled observations. This separates exact interpolation from the closure argument for (15).

Finally, \(g(a)=da-ka^2/2+O_S(a^3)\). The inverse-function theorem applied to \(g'\) yields (7). Rescaling \(a=Ax\) in the maximum in (5) gives (8) by maximizing \(\tau x-x^2/2\) on \([0,1]\). Integrating \(g'(a)=d-ka+O_S(a^2)\) from \(u\) to \(v\) proves (11) with an error uniform even when \(v-u\) is very small.

## Arithmetic instantiation and source limits

AF-570's exact analytic boundary expansion is
\[
 \Phi_p(a)=1+K_pa+M_pa^2+O_p(a^3),\qquad
 K_p=ce^{-b_p},\quad
 M_p=K_p[(C_1-h_p'(1))K_p-1],
\tag{16}
\]
where \(b_p=1/[p(p+1)]\), \(c=e^{B_1}\), \(B_1\) is the Meissel–Mertens constant, and \(C_1\) is the coefficient of \(x\) in the analytic regular part of \(P(1+x)\). AF-571 derives, uniformly over \(q>p\to\infty\),
\[
 K_q-K_p=c\Delta_{p,q}[1+O(p^{-2})],\qquad
 2(M_p-M_q)=2c^2\Delta_{p,q}\log p\,[1+O(1/\log p)],
 \quad \Delta_{p,q}=b_p-b_q>0.
\tag{17}
\]
These signs follow by integrating the positive edit-parameter sensitivity, rather than subtracting uncontrolled source remainders. They give \(G_i'(0)>0\) and \(G_i''(0)<0\). Finitely many analytic gaps then have positive decreasing derivatives on a common window. Differences between their derivative germs either vanish identically or have a fixed sign sufficiently near zero, giving a pointwise least derivative and (3), independently of \(L\). In particular \(d=\min_i G_i'(0)\), so (4) agrees with AF-572's \(n=1\) threshold; ties are resolved by the derivative germs.

For a two-source set \(\{p,q\}\), write \(\theta=1-L/L_{\rm crit}\). First fixing the source pair and letting \(\theta\downarrow0\), (7) becomes
\[
 t_L\sim\theta\frac{d}{k},\qquad
 \varepsilon_{\rm full}\sim\theta^2\frac{d^2}{8k}.
\tag{18}
\]
The coefficients themselves have the remote-prime asymptotics
\[
 \frac{d}{k}=\frac{1+O(1/\log p)}{2c\log p},\qquad
 \frac{d^2}{8k}=\frac{\Delta_{p,q}}{16\log p}
 [1+O(1/\log p)].
\tag{19}
\]
No uniform simultaneous \(\theta,p,A\) limit is asserted. These curves are generalized-prime matched controls indexed by genuine prime edit locations. They do not establish a discriminator of the ordinary prime system against all generalized-prime systems or a bridge to RH.

## Prior art, audit controls and consequence

The envelope and extension machinery is classical: [Gutev (2020), §2, Theorems 2.1 and 2.3 and Remark 2.5](https://arxiv.org/abs/2002.07205) reconstructs the Pasch–Hausdorff and McShane–Whitney formulas. The uniform-distance identity (15) is an elementary consequence, proved here rather than claimed as a new approximation theorem. [Wiens (2009), §2](https://sites.ualberta.ca/~dwiens/home%20page/pubs/discriminationDesign.pdf) already treats overlap of model neighbourhoods as a robust-discrimination obstruction, under a different stochastic criterion. AF-572's bounded-derivative/perfect-spline prior art remains relevant. No general approximation or experimental-design priority is claimed.

An exact non-arithmetic control is \(g(a)=2a-a^2\) on \([0,1/2]\). Here \(d=k=2\), and with \(\delta=2-2L\in(0,1)\), (5) gives \(t_L=\delta/2\) and \(\varepsilon_{\rm full}=\delta^2/16\). The legal endpoint pair \(T=\{1/4,1/2\}\) has \(L_T=5/8\). At \(L=3/4\) it aliases exactly, whereas the full radius is \(1/64\); the \(C^1\) approximant (13) verifies the matching upper bound. These rational identities check normalization and the finite/full separation, not an unproved prime statement.

The new source-specific conclusion is a precise failure of **one fixed finite sampling design** near the smooth-calibration threshold, despite exact full-margin saturation by two probes tailored to each budget. The margin is quadratic in calibration slack and its informative interval shrinks linearly. Positivity of the full margin therefore does not supply a uniform sampling geometry. This closes the first-derivative transition left outside AF-572's fixed-budget window estimate; it does not classify higher-derivative constraints, independently recalibrated probes, unknown source lists, or measurement-coordinate errors.
