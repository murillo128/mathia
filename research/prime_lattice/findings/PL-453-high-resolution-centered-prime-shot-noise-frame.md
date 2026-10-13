# PL-453 — High vertical resolution restores the centered prime-residue frame through atomic self-pairs

**Evidence/status:** LITERATURE+EXACT-DERIVED + HIGH-RESOLUTION SUFFICIENCY / GENERIC SHOT-NOISE CONTROL.

**Parent findings:** PL-072, PL-421, PL-448, PL-449, PL-451, PL-452.

## Claim

Fix the four reduced residues modulo 5, \(U_5=\{1,2,3,4\}\), and \(X\to\infty\), \(1\le H\le X/2\). Use the *phase-matched*, genuinely continuum-subtracted prime windows of PL-452:
\[
P_{a,t}(y)=\sum_{\substack{y<n\le y+H\\n\equiv a\ (5)}}\Lambda(n)n^{-it},\qquad
Q_t(y)=\int_y^{y+H}x^{-it}\,dx,\qquad
R_{a,t}(y)=P_{a,t}(y)-\tfrac14Q_t(y).
\]
Let \(w_T\) be either the symmetric rectangular probability density \(1_{[-T,T]}/(2T)\) or the triangular Fejér density \((1-|t|/T)_+/T\), and put
\[
S^R_{X,T}=\int_{\mathbb R}w_T(t)\int_X^{2X}R_t(y)R_t(y)^*\,dy\,dt.
\]
Let \(A_X=\operatorname{Diag}(A_a)\) be the **uncentered atomic self-pair diagonal** of PL-448:
\[
A_a=\sum_{n\equiv a\ (5)}\Lambda(n)^2
\big|[X,2X]\cap[n-H,n)\big|,\qquad
A_a=(1+o(1))\frac{XH\log X}{4}
\]
uniformly in \(H\). Write \(u=X/T\), and set
\[
q=\frac{\min(H,u)}{\log X},\qquad
\eta=(1+u)\frac{\log X}{\sqrt X},
\]
\[
e_F=\frac{\min(u,u^2)}{\log X}
+\eta+\sqrt{\left(1+\frac{\min(u,u^2)}{\log X}\right)\eta},
\]
\[
e_R=\frac{u\log\log X}{\log X}
+\eta+\sqrt{\left(1+\frac{u\log\log X}{\log X}\right)\eta}.
\]
For the Fejér and rectangular averages, respectively, put \(e_w=e_F\) and \(e_w=e_R\). Then for all \(T>0\) and \(1\le H\le X/2\),
\[
\boxed{\quad
\frac{\|S^R_{X,T}-A_X\|_{\mathrm{op}}}{XH\log X}
\ll e_w+q+\sqrt{(1+e_w)q}.
\quad}\tag{1}
\]
The implied constant is absolute and uniform in \(H,T\) for sufficiently large \(X\).

In particular, **for the actually centered prime source** the diagonal-normalized matrix
\(C^R_{X,T}=(\operatorname{Diag}S^R_{X,T})^{-1/2}
S^R_{X,T}(\operatorname{Diag}S^R_{X,T})^{-1/2}\) satisfies
\[
\boxed{\quad
\sup_{1\le H\le X/2}\|C^R_{X,T_X}-I_4\|_{\mathrm{op}}\to0
\quad}\tag{2}
\]
under either of the following respective hypotheses:
\[
\text{Fejér: }\frac{T_X\log X}{X}\to\infty;
\qquad
\text{rectangular: }\frac{T_X\log X}{X\log\log X}\to\infty.\tag{3}
\]
Consequently the strict PL-421 local-factor image-cone floor
\(\lambda_{\min}(C^R_{X,T_X})>1/4\) eventually holds, uniformly in \(H\).
For either window, taking a sufficiently large **fixed** constant \(C\) in
\(T=CX/\log X\) (Fejér) or \(T=CX\log\log X/\log X\) (rectangular) also suffices for the strict floor for all sufficiently large \(X\), without claiming convergence to \(I_4\) at a fixed \(C\).

This is an *automatic, high-frequency atomic-diagonal phenomenon*, not a signed arithmetic correlation estimate or an RH mechanism. It complements, rather than contradicts, PL-452's first-order blindness at polynomial horizons \(T\le X^{1-\sigma}\).

## Proof: the continuum cannot carry diagonal mass at high resolution

Write \(V_t(y)=\tfrac14Q_t(y)\mathbf1\), so \(R=P-V\). Denote the uncentered vertical Gram of \(P\) by \(S^P\), and the continuum Gram of \(V\) by \(S^V\). Its exact rank-one form is
\[
S^V=\frac{G_w}{16}\mathbf1\mathbf1^*,
\qquad
G_w=\int w_T(t)\int_X^{2X}|Q_t(y)|^2\,dy\,dt,
\qquad
\|S^V\|_{\rm op}=\frac{G_w}{4}.
\tag{4}
\]
Since both permitted time densities obey \(0\le w_T\le 1/T\), the trivial bound \(|Q_t(y)|\le H\) gives \(G_w\le XH^2\). Mellin--Plancherel, applied at each \(y\), gives the independent estimate
\[
\int_{\mathbb R}|Q_t(y)|^2dt
=2\pi\int_y^{y+H}x\,dx\ll XH
\qquad(X\le y\le2X,\ H\le X/2).
\]
Thus \(G_w\ll X^2H/T=XHu\), and the two estimates combine into
\[
\boxed{\quad G_w\ll XH\min(H,u)=XH\log X\ q.\quad}\tag{5}
\]

The uncentered estimates of PL-448 and PL-449 already establish, with exactly the same \(A_X\),
\[
\|S^P-A_X\|_{\rm op}\ll XH\log X\ e_w,\qquad
\|S^P\|_{\rm op}\ll XH\log X(1+e_w).
\tag{6}
\]
Here PL-448 treats rectangular averaging by the weighted Montgomery--Vaughan estimate and sieve bounds for prime gaps; PL-449 treats the Fejér kernel by its squared-sinc tail and a prime-pair upper-bound sieve. Both include proper prime powers and hold uniformly in \(H\).

For the mixed Gram \(B=\int w_T(t)\int_X^{2X}P_t(y)V_t(y)^*dy\,dt\), the ordinary Hilbert-space Cauchy--Schwarz inequality for analysis operators gives
\[
\|B\|_{\rm op}\le\sqrt{\|S^P\|_{\rm op}\|S^V\|_{\rm op}}.
\tag{7}
\]
Expanding \(S^R=S^P-B-B^*+S^V\), then using (4)--(7), proves (1). No cancellation of cross-terms and no hypothesis on higher prime correlations is used.

Under the Fejér hypothesis in (3), \(u=o(\log X)\), so \(q\le u/\log X=o(1)\), \(\min(u,u^2)/\log X=o(1)\), and \(\eta=o(1)\); hence \(e_F=o(1)\). Under the rectangular hypothesis, \(u=o(\log X/\log\log X)\), so again \(q=o(1)\), \(\eta=o(1)\) and \(e_R=o(1)\). Therefore \(\|S^R-A_X\|_{\rm op}=o(XH\log X)\). Since \(A_a=(1+o(1))XH\log X/4\) uniformly in \(H\), its diagonal normalization proves (2).

At \(T=CX/\log X\) with \(C\) fixed, the Fejér error has \(e_F=O(C^{-1})+o(1)\) and \(q\le C^{-1}\), giving
\[
\limsup_{X\to\infty}\sup_H
\frac{\|S^R-A_X\|_{\rm op}}{XH\log X}
\ll C^{-1/2}+C^{-1}.
\]
At \(T=CX\log\log X/\log X\), the rectangular error satisfies \(e_R=O(C^{-1})+o(1)\), \(q\le1/(C\log\log X)\), so the corresponding limsup is \(O(C^{-1})\).
Choosing \(C\) large enough makes each matrix an arbitrarily small relative perturbation of its positive diagonal. The strict \(1/4\) PL-421 floor then follows by diagonal congruence and the operator-norm eigenvalue bound.

## Why the centered source and PL-452's controls differ

PL-452 proves that on the lower polynomial time range \(T\le X^{1-\sigma}\), first-order prime equidistribution makes the **absolute** centered energy \(o(XH\min(H,X/T))\) but cannot decide its normalized shape. Its matched *diffuse* four-channel sources can have the same arbitrarily accurate short-interval masses and yet produce a rank-one or identity normalized centered Gram.

There is no conflict. The present proof is in the higher-resolution regime \(T\asymp X/\log X\) or larger, outside every fixed polynomial range \(T\le X^{1-\sigma}\) eventually. It uses atomic prime self-pairs of size \(XH\log X\), which survive vertical dephasing, while the smooth continuum contributes at most \(XH(X/T)\). A purely diffuse matched source need not possess that atomic diagonal, so the conclusion does not follow from PL-452's first-order equidistribution hypothesis alone.

The spectral floor established here belongs only to the **time-averaged, phase-matched, centered raw-source Gram**. It does not imply the floor for pointwise \(t\), the covariance centered by PL-418's more specialized singular-series/model subtraction, the finite-unaveraged mod-5 oriented variance problem in PL-435--PL-439, or a zero-side/Weil form after analytic continuation. A source-specific and noncircular transfer would still be necessary.

## Prior art, audit, and consequence

Montgomery--Vaughan (1974), *Hilbert's Inequality* (source 62 in this line's SOURCES.md), the unconditional prime-pair sieve recorded in PL-445 and PL-449 (Lichtman--Teräväinen 2022, source 115), fixed-modulus PNT, Mellin--Plancherel, and Hilbert-space Cauchy--Schwarz are classical. PL-448/PL-449 already prove the load-bearing uncentered bounds. Equation (1) is their direct, explicit **centered transfer**, and no independent new mean-value, prime-distribution, or general functional-analysis theorem is claimed. The line-specific mathematical delta is to settle the complementary high-frequency branch left outside PL-452: for the genuine atomic prime source, phase-matched continuum subtraction does **not** obstruct eventual normalized lower-frame positivity once averaging resolves prime frequencies finely enough.

Falsification controls are exact: the smooth-term estimate does not see prime locations; the uncentered estimate is source-generic for suitable pair-correlation bounds; the matched diffuse controls of PL-452 demonstrate that first moments alone cannot replace the atomic ingredient. If \(H\le1\), ordinary discrete windows contain at most one integer, consistent with the self-pair baseline; the smooth subtraction remains controlled by (5). No RH consequence, zero-divisor sensitivity, sharpness of the horizon, or claim that this high-frequency limit selects rational primes over suitable atomic generalized-prime controls follows.