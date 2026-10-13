# PL-451 — Polynomial rectangular vertical averages retain the prime-residue common mode

**Evidence/status:** LITERATURE+EXACT-DERIVED + NEGATIVE/OBSTRUCTION (raw, uncentered, rectangular Cesàro-averaged Gram).

**Parent findings:** PL-421, PL-422, PL-446, PL-447, PL-448, PL-449, PL-450.

## Claim

Fix \(1/6<\theta\le1/2\), \(H=X^\theta\), and \(1/6<\sigma<\theta\). For residues \(a\in U_5=\{1,2,3,4\}\), put
\[
P_{a,t}(y)=\sum_{\substack{y<n\le y+H\\n\equiv a\ (5)}}\Lambda(n)n^{-it},\qquad
\overline S_{X,T}=\frac1{2T}\int_{-T}^{T}\int_X^{2X}P_t(y)P_t(y)^*\,dy\,dt.
\]
This uses the *unsmoothed* symmetric rectangular time average, not the Fejér statistic of PL-449--PL-450. Let \(u=X/T\), \(m=\min(H,u)\), and define the scalar continuum common-mode mass
\[
G^{\mathrm{rect}}_{X,T}=\frac1{2T}\int_{-T}^{T}\int_X^{2X}
\left|\int_y^{y+H}x^{-it}\,dx\right|^2dy\,dt>0.
\]
Then, **uniformly for \(0<T\le X^{1-\sigma}\)**,
\[
G^{\mathrm{rect}}_{X,T}\asymp XHm,\qquad
\boxed{\max_{a,b\in U_5}\frac{|\overline S_{X,T;ab}-G^{\mathrm{rect}}_{X,T}/16|}{XHm}\longrightarrow0.}
\tag{1}
\]
The diagonal-normalized matrix \(\overline C_{X,T}=\operatorname{Diag}(\overline S_{X,T})^{-1/2}\overline S_{X,T}\operatorname{Diag}(\overline S_{X,T})^{-1/2}\) therefore satisfies
\[
\boxed{\sup_{0<T\le X^{1-\sigma}}\|\overline C_{X,T}-\mathbf1\mathbf1^*\|_{\rm op}\longrightarrow0.}
\tag{2}
\]
Its smallest eigenvalue tends to zero uniformly, failing the \(1/4\) lower-frame image cone of PL-421. For \(X^\sigma\le u=o(H)\), the scalar amplitude additionally obeys
\[
\boxed{G^{\mathrm{rect}}_{X,T}=(3\pi/2+o(1))XHu,\qquad
\overline S_{X,T;ab}=(3\pi/32+o(1))XHu.}
\tag{3}
\]
Consequently, **any eventual passing horizon** for the raw rectangular Gram at \(H=X^\theta\) must obey the necessary condition
\[
\boxed{\liminf_{X\to\infty}\frac{\log T_X}{\log X}\ge\frac56.}
\tag{4}
\]
It is not sufficient: PL-448 supplies the separate sufficient regime \(T_X\gg X\log\log X/\log X\) (with the ratio tending to infinity for convergence). Unlike the bounded \(TH/X\) obstruction of PL-447, (2) still applies to polynomial ranges where \(TH/X\to\infty\).

## Fixed-modulus source on a fine grid

Choose \(\rho\) with \(1/6<\rho<\sigma\) and let \(\delta=X^\rho\). Theorem 1.2 of Koukoulopoulos (2015), at the *fixed* modulus \(q=5\), gives for every \(A>0\) the averaged prime-progression error
\[
\int_{X-O(\delta)}^{2X+H+O(\delta)}
\max_{a\in U_5}\left|\sum_{\substack{v<p\le v+\delta\\p\equiv a\ (5)}}\log p-\frac\delta4\right|\,dv
\ll_A\frac{X\delta}{(\log X)^A}.
\tag{5}
\]
Indeed \(\delta=X^{\rho}\) exceeds \(X^{1/6+2\epsilon}\) for a fixed small \(\epsilon>0\), while \(Q=5\) satisfies the theorem's \(Q^2\le\delta/X^{1/6+\epsilon}\) for large \(X\); a bounded number of dyadic ranges covers the enlarged origin interval. The elementary pointwise bound \(O(\delta\log X)\) upgrades (5) to a squared-\(L^2\) saving of every fixed logarithmic order. Proper prime powers are negligible with a polynomial saving, as in PL-422 and PL-450, so the same conclusion holds with \(\Lambda(n)\) in place of prime-only weights.

On a common shifted grid \(I_j=(r+j\delta,r+(j+1)\delta]\) covering \([X,2X+H]\), write
\[
M_{a,j}=\sum_{\substack{n\in I_j\\n\equiv a\ (5)}}\Lambda(n),\qquad e_{a,j}=M_{a,j}-\delta/4.
\]
Averaging the squared mass discrepancies over one grid offset \(r\in[0,\delta)\) and using (5), choose one offset valid for all four residues with, for every fixed \(B>0\),
\[
\sum_{a\in U_5}\|e_a\|_{\ell^2}^2\ll_B\frac{X\delta}{(\log X)^B},
\qquad \|M_a\|_{\ell^2}+\|(\delta/4)\mathbf1\|_{\ell^2}\ll\sqrt{X\delta}.
\tag{6}
\]
For each desired \(B\), (5) supplies the required choice; no pointwise-in-origin short-interval PNT is asserted.

## Rectangular sinc kernel, Schur transfer and positive continuum limit

At fixed \(X,H,T\), finite expansion and symmetric time integration give exactly
\[
\overline S_{X,T;ab}=\sum_{\substack{n\equiv a\ (5)\\m\equiv b\ (5)}}
\Lambda(n)\Lambda(m)k_T(n,m),\quad
k_T(x,z)=W_X(x,z)\operatorname{sinc}\!\left(T\log\frac{x}{z}\right),
\tag{7}
\]
where \(W_X(x,z)=|[X,2X]\cap[x-H,x)\cap[z-H,z)|\). Thus \(k_T\) is **signed**, unlike PL-450's squared-sinc kernel, but \(\overline S\) remains positive semidefinite as an averaged Gram. The continuum double integral of \(k_T\) is exactly \(G^{\mathrm{rect}}\).

For \(x,z\in[X,3X]\), \(u=X/T\), elementary bounds on \(\operatorname{sinc}\) and its derivative imply
\[
|\operatorname{sinc}(T\log(x/z))|\ll (1+|x-z|/u)^{-1},\qquad
|\partial_x\operatorname{sinc}(T\log(x/z))|\ll u^{-1}(1+|x-z|/u)^{-1}.
\tag{8}
\]
The overlap \(W_X\) is bounded by \(H\), is Lipschitz in each argument, and vanishes for \(|x-z|\ge H\). Put \(L=1+\log^+(H/u)\ll\log X\). For cell centers \(c_j\), define \(K_{j\ell}=k_T(c_j,c_\ell)\) and \(E_{j\ell}=\sup_{x\in I_j,z\in I_\ell}|k_T(x,z)-K_{j\ell}|\). Since \(\delta=o(m)\), row and column summation of the envelopes (8), including \(O(\delta)\) support-boundary strips, yields
\[
\boxed{\|K\|_{\rm op}\ll \frac{HmL}{\delta},\qquad
\|E\|_{\rm op}\ll mL\left(1+\frac Hu\right).}
\tag{9}
\]
The logarithmic loss \(L\) is the price of the nonintegrable **absolute** sinc tail, and cannot simply be dropped as in PL-450. The sums of nonnegative von-Mangoldt masses and (6) allow the exact bilinear form to be binned with error
\[
\|E\|_{\rm op}\|M_a\|_2\|M_b\|_2
\ll X\delta mL(1+H/u)
=XHm\,O\big(L(\delta/H+\delta/u)\big)=o(XHm).
\tag{10}
\]
Replacing binned masses by \((\delta/4)\mathbf1\) incurs, by (6) and (9), an additional \(O_B(XHm L/(\log X)^{B/2})=o(XHm)\) if \(B\) is fixed sufficiently large. Binning the flat continuum integral has the same bound (10), so
\[
\overline S_{X,T;ab}=\frac{\delta^2}{16}\sum_{j,\ell}K_{j\ell}+o(XHm)
=\frac1{16}\iint k_T(x,z)\,dx\,dz+o(XHm)
=\frac{G^{\mathrm{rect}}_{X,T}}{16}+o(XHm).
\tag{11}
\]
All errors are uniform for \(u\ge X^\sigma\), including \(u\gg H\), proving the second part of (1).

Positivity of the continuum amplitude avoids any cancellation assumption about the signed sinc kernel:
\[
G^{\mathrm{rect}}_{X,T}
=\frac1{2T}\int_{-T}^{T}\int_X^{2X}
\left|\int_y^{y+H}x^{-it}dx\right|^2dy\,dt.
\]
If \(u\ge H\), the trivial bound gives \(G\ll XH^2\); if \(u<H\), Mellin--Plancherel, with \(x=e^v\), gives
\[
\int_{\mathbb R}\left|\int_y^{y+H}x^{-it}dx\right|^2dt
=2\pi\int_y^{y+H}x\,dx\ll XH,
\]
so \(G\ll XHu\). For the matching lower bound restrict to \(|t|\le c\min(T,X/H)\); all phases within each window then lie in a fixed small arc, and the integral has modulus \(\gg H\). This region has relative time weight \(\gg\min(1,u/H)\), giving \(G\gg XHm\). Hence (1) and, after diagonal normalization, (2).

Finally, if \(u=o(H)\), the complete Mellin--Plancherel integral and the endpoint antiderivative
\[
\int_y^{y+H}x^{-it}dx
=\frac{(y+H)^{1-it}-y^{1-it}}{1-it}
\]
give the outside-tail bound \(\int_{|t|>T}|\cdots|^2dt\ll X^2/T\). After time normalization and origin integration,
\[
G^{\mathrm{rect}}_{X,T}
=\frac\pi T\int_X^{2X}\int_y^{y+H}x\,dx\,dy
+O(X^3/T^2)
=\frac{3\pi}{2}XHu\big(1+O(H/X+u/H)\big),
\]
which proves (3). If (4) failed, some subsequence would have \(T_X\le X^{1-\sigma}\) for \(1/6<\sigma<\theta\), contradicting (2).

## Prior art, controls, and consequences

The sole short-prime input is Koukoulopoulos (2015), Theorem 1.2 (source 116 in research/prime_lattice/SOURCES.md), already used by PL-422, PL-447 and PL-450. The rectangular Fourier identity, elementary Schur bounds and Mellin--Plancherel are classical; PL-448 supplies the separate rectangular mean-value sufficient condition, and PL-450 treats the *different* Fejér statistic. The mathematical delta is the transfer of polynomial common-mode collapse through the oscillatory, non-absolutely-integrable rectangular sinc kernel, using the theorem's arbitrarily strong logarithmic savings to absorb its extra Schur logarithm. No new prime-distribution theorem is claimed.

The mechanism is source-generic: a matched nonnegative generalized-prime source with the same four-channel fine-grid \(L^2\) equidistribution exhibits the same collapse. The obstruction concerns the **uncentered raw** rectangular Gram, not phase-resolved tomography, centered covariance, the PL-438/PL-439 oriented second-order source gate, or pointwise-in-frequency inequalities outside PL-447's range. It supplies neither signed arithmetic cancellation nor analytic continuation or a conclusion about Riemann zeros. In particular the exponent \(5/6\) is the limit of the *available short-AP equidistribution input*, not a sharp conjectured transition.
