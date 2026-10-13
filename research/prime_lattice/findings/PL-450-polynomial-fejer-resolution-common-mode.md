# PL-450 — Polynomial Fejér resolution retains the rank-one prime-residue common mode

**Evidence/status:** LITERATURE+EXACT-DERIVED + NEGATIVE/OBSTRUCTION (raw, uncentered, Fejér-averaged covariance).

**Parent findings:** PL-421, PL-422, PL-446, PL-447, PL-449.

## Claim

Fix \(1/6<\theta\le 1/2\), \(H=X^\theta\), and \(1/6<\sigma<\theta\). Retain the four uncentered von-Mangoldt residue windows and the triangular time average of PL-449:

\[
P_{a,t}(y)=\sum_{\substack{y<n\le y+H\\n\equiv a\ (5)}}\Lambda(n)n^{-it},\quad
F_{X,T}=\frac1T\int_{-T}^{T}\left(1-\frac{|t|}{T}\right)
\int_X^{2X}P_t(y)P_t(y)^*\,dy\,dt.
\]

For \(T>0\), put \(u=X/T\), \(m=\min(H,u)\), and define the positive continuum common-mode mass

\[
G_{X,T}:=\int_X^{2X}\int_y^{y+H}\int_y^{y+H}
\operatorname{sinc}^2\!\left(\frac T2\log\frac{x}{z}\right)\,dx\,dz\,dy.
\]

Then, **uniformly over every \(0<T\le X^{1-\sigma}\)**,

\[
G_{X,T}\asymp XHm,\qquad
\boxed{\max_{a,b\in\{1,2,3,4\}}
\frac{|F_{X,T;ab}-G_{X,T}/16|}{XHm}\longrightarrow0.}
\tag{1}
\]

Thus the diagonal-normalized correlation matrix obeys

\[
\boxed{\sup_{0<T\le X^{1-\sigma}}
\|C^F_{X,T}-\mathbf1\mathbf1^*\|_{\rm op}\longrightarrow0,\quad
\sup_{0<T\le X^{1-\sigma}}\lambda_{\min}(C^F_{X,T})\longrightarrow0.}
\tag{2}
\]

Every such horizon eventually **fails** the strict mod-5 inverse-dephasing lower-frame threshold \(\lambda_{\min}>1/4\) of PL-421. This includes horizons satisfying \(TH/X\to\infty\): choose any \(1/6<\beta<\theta\) and \(T=X^{1-\beta}\), when \(TH/X=X^{\theta-\beta}\to\infty\).

If \(X^\sigma\le u=o(H)\), there is the additional explicit asymptotic

\[
\boxed{G_{X,T}=(3\pi+o(1))XHu,\qquad
F_{X,T;ab}=(3\pi/16+o(1))XHu.}
\tag{3}
\]

It follows that any horizon sequence eventually passing the raw Fejér image-cone criterion at polynomial \(H=X^\theta\) must satisfy the **necessary exponent condition**

\[
\boxed{\liminf_{X\to\infty}\frac{\log T_X}{\log X}\ge\frac56.}
\tag{4}
\]

This is not a sufficient condition. PL-449 proves the separate sufficient regime \(T_X\log X/X\to\infty\).

## Short arithmetic-progression equidistribution on a finer grid

Choose fixed \(\rho\) with \(1/6<\rho<\sigma\) and put \(\delta=X^\rho\). Koukoulopoulos (2015), Theorem 1.2, at the fixed modulus 5 supplies arbitrarily strong logarithmic \(L^1\) equidistribution savings for prime sums over length-\(\delta\) intervals, in a bounded dyadic neighborhood of \([X,2X+H]\). Combining with the trivial \(O(\delta\log X)\) supremum gives, for each reduced residue \(a\),

\[
\int_{X-O(\delta)}^{2X+H+O(\delta)}
\left|\sum_{\substack{v<p\le v+\delta\\p\equiv a\ (5)}}\log p-\frac\delta4\right|^2dv
=o(X\delta^2).
\tag{5}
\]

As in PL-422, proper prime powers contribute squared \(L^2\) norm \(O(X\delta\log^2 X)=o(X\delta^2)\). Thus (5) is true for sums weighted by \(\Lambda(n)\).

Take a shifted cell grid \(I_j=(r+j\delta,r+(j+1)\delta]\) covering the active integer support, with
\[
M_{a,j}(r)=\sum_{\substack{n\in I_j\\n\equiv a\ (5)}}\Lambda(n),\qquad
e_{a,j}(r)=M_{a,j}(r)-\delta/4.
\]
Averaging over the common offset \(r\in[0,\delta)\) converts the sum of the four residue-wise squared cell errors into the origin integral (5), divided by \(\delta\). The harmless endpoint cells can be covered within the enlarged interval in (5). There is consequently one grid offset for all four residues such that

\[
\sum_{a=1}^4\sum_j|e_{a,j}|^2=o(X\delta),
\qquad \|M_a\|_{\ell^2}=O(\sqrt{X\delta}).
\tag{6}
\]

The choice of offset is merely a proof device; no pointwise-in-origin PNT is asserted.

## Fejér-kernel transfer and spectral collapse

Define the continuous overlap
\[
W_X(x,z)=|[X,2X]\cap[x-H,x)\cap[z-H,z)|,\quad
k_T(x,z)=W_X(x,z)\operatorname{sinc}^2\!\left(\frac T2\log\frac{x}{z}\right).
\]

PL-449's exact Fejér identity gives
\(F_{X,T;ab}=\sum_{n\equiv a(5),m\equiv b(5)}\Lambda(n)\Lambda(m)k_T(n,m)\).
Let \(c_j\) denote cell centers, and \(K_{j\ell}=k_T(c_j,c_\ell)\). Since \(u=X/T\), all arguments are comparable to \(X\), and \(H\le X/2\),

\[
\operatorname{sinc}^2\!\left(\frac T2\log\frac{x}{z}\right)
\ll\big(1+|x-z|^2/u^2\big)^{-1},\quad
\left|\partial_x\operatorname{sinc}^2\!\left(\frac T2\log\frac{x}{z}\right)\right|
\ll u^{-1}\big(1+|x-z|^2/u^2\big)^{-1}.
\tag{7}
\]

The overlap \(W_X\) is bounded by \(H\), vanishes for \(|x-z|\ge H\), and is Lipschitz in both variables. Because \(\delta=o(m)\), discrete Schur summation of the envelopes (7) yields

\[
\sup_j\sum_\ell|K_{j\ell}|\ll Hm/\delta,\qquad
\sup_j\sum_\ell E_{j\ell}\ll m+Hm/u,
\tag{8}
\]

where \(E_{j\ell}:=\sup_{x\in I_j,z\in I_\ell}|k_T(x,z)-k_T(c_j,c_\ell)|\). The same bounds hold for column sums. The overlap's support can expand by only \(O(\delta)\) when comparing cells with centers; this is absorbed because \(\delta=o(m)\).

All von-Mangoldt coefficients are nonnegative. Applying the Schur estimate for \(E\) and (6) to the exact-to-bin error gives

\[
O\!\big(X\delta(m+Hm/u)\big)
=O\!\big(XHm(\delta/H+\delta/u)\big)=o(XHm).
\tag{9}
\]

For the bin bilinear form, substitute \(M_a=(\delta/4)\mathbf1+e_a\). The estimate \(\|K\|_{\rm op}\ll Hm/\delta\), (6), and Cauchy–Schwarz show that all error terms containing any \(e_a\) are \(o(XHm)\). Applying (9) to flat cell masses identifies the main Riemann sum with \(G_{X,T}/16\). Therefore

\[
F_{X,T;ab}=\frac{\delta^2}{16}\sum_{j,\ell}K_{j\ell}+o(XHm)
=\frac{G_{X,T}}{16}+o(XHm)
\]

uniformly for \(u\ge X^\sigma\).

An upper estimate for \(G\) follows from the integrable kernel envelope and the overlap window: \(G\ll XH\min(H,u)\). Restricting the double integral to \(|x-z|\le c\min(H,u)\), for a sufficiently small constant \(c>0\), gives a uniformly positive sinc-squared factor and the reverse bound \(G\gg XHm\). Thus the four entries have the same positive leading term, and normalizing by their diagonal entries proves (1)–(2).

When \(u=o(H)\), we also have \(H=o(X)\), and the effective displacement scale is \(|x-z|=O(u)\). Changing variable \(v=x-z\), the logarithmic phase is \(Tv/(2y)+o(1)\) on each fixed multiple of this scale; the uniform integrable bound permits a dominated-convergence argument. Since

\[
\int_{\mathbb R}\operatorname{sinc}^2(Tv/(2y))\,dv=2\pi y/T,
\]

we get
\[
G_{X,T}=(1+o(1))H\int_X^{2X}(2\pi y/T)\,dy
=(3\pi+o(1))X^2H/T,
\]
which proves (3). For (4), if the liminf exponent were smaller than \(5/6\), some subsequence would satisfy \(T_X\le X^{1-\sigma}\) for an admissible \(1/6<\sigma<\theta\), contradicting the positive image-cone criterion by (2).

## Prior art, controls, and boundaries

The load-bearing arithmetic input is **D. Koukoulopoulos**, “Primes in short arithmetic progressions” (2015), Theorem 1.2, already source 116 in this line's SOURCES.md and the primary anchor of PL-422/PL-447. The Fejér transform and exact prime-window Gram are in PL-449. Cellwise \(L^2\) averaging, Schur bounds, and convolution approximation of locally equidistributed measures are standard analysis. No novel prime-distribution theorem, prime-pair asymptotic, or originality claim for those tools is made.

This is a line-specific derived obstruction to a raw local-factor cone certificate. It extends PL-447's negative horizon \(TH/X=O(1)\) into regimes with \(TH/X\to\infty\), without narrowing PL-449's universal high-resolution sufficient bound. It uses uncentered, nonnegative residue masses; a matched generalized-prime source satisfying the same finer-scale \(L^2\) equidistribution has the same obstruction. The limiting rank-one geometry is the deterministic common source mode, not signed prime cancellation.

The result says nothing about sharp rectangular averaging (PL-448), centered/model-subtracted covariance (PL-418/PL-435), pointwise-in-\(t\) positive cones outside the earlier range, analytic continuation, or the Riemann zero divisor. It does not prove or disprove RH.
