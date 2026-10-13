# PL-452 — Polynomial vertical source approximation does not decide the centered residue frame

**Evidence/status:** LITERATURE+EXACT-DERIVED + SOURCE-REALIZABLE NEGATIVE/OBSTRUCTION.

**Parent findings:** PL-418, PL-421, PL-422, PL-434, PL-435, PL-450, PL-451.

## Claim

Fix \(1/6<\theta\le1/2\), \(H=X^\theta\), and \(1/6<\sigma<\theta\). Write \(u=X/T\), \(m=\min(H,u)\), and for \(a\in U_5=\{1,2,3,4\}\) define the uncentered prime-residue Dirichlet windows and the **phase-matched continuum**:
\[
P_{a,t}(y)=\sum_{\substack{y<n\le y+H\\n\equiv a\ (5)}}\Lambda(n)n^{-it},
\qquad Q_t(y)=\int_y^{y+H}x^{-it}\,dx,
\qquad R_{a,t}(y)=P_{a,t}(y)-\tfrac14Q_t(y).
\]
For any fixed \(C\ge1/2\), consider **any** nonnegative time density \(w_{X,T}\) supported on \([-T,T]\), with \(\int w_{X,T}=1\) and \(w_{X,T}\le C/T\). Then, uniformly for \(0<T\le X^{1-\sigma}\) and all these densities,
\[
\boxed{
\left\|\int_{\mathbb R}w_{X,T}(t)\int_X^{2X}
R_t(y)R_t(y)^*\,dy\,dt\right\|_{\rm op}
=o\!\left(XH\min(H,X/T)\right).}
\tag{1}
\]
In particular this holds for both the symmetric rectangular density \(1_{[-T,T]}/(2T)\) and the triangular Fejér density \((1-|t|/T)_+/T\). The assertion concerns **absolute centered energy at the first-order common-mode scale**. It does **not** imply that the *diagonal-normalized centered* covariance tends to zero, has a lower spectral floor, or even has a determinate limiting shape.

The latter failure is exact, not just a missing estimate. There exist two families of four **nonnegative continuous channel measures** with (i) identical mass \(\delta/4\) in every cell of a chosen grid of size \(\delta=X^\rho\), \(1/6<\rho<\sigma\), and (ii) uniformly \(O(\delta e^{-\sqrt{\log X}})\) discrepancy from \(\delta/4\) in **every shifted interval of length \(\delta\)**, for which the phase-matched centered Gram has respectively
\[
\boxed{C_{\rm centered}^{\rm shared}=\mathbf1\mathbf1^*,
\qquad C_{\rm centered}^{\rm separated}=I_4}
\tag{2}
\]
for every positive \(T\) and every above nonnegative time density. Both centered Grams have strictly positive diagonals. Thus even arbitrarily strong *first-order* short-progression equidistribution and positivity of the channel sources, without arithmetic second-order input, admit **opposite** outcomes at the PL-421 \(1/4\) lower-frame gate.

These are matched **continuous channel-source controls**, not alleged Beurling prime systems or counterexamples about the actual rational primes. They isolate exactly what cannot follow from the first-order input used in PL-450--PL-451 alone.

## Proof of the actual-prime centered estimate

Put \(\delta=X^\rho\) with \(1/6<\rho<\sigma\), so \(\delta=o(H)\), \(\delta=o(u)\) uniformly in the stated horizon range. On \([X,2X+H]\), introduce the signed, real channel measures
\[
d\nu_a(x)=\sum_{n\equiv a\ (5)}\Lambda(n)\,\delta_n(dx)-\tfrac14\,dx.
\]
Then \(R_{a,t}(y)=\int_{(y,y+H]}x^{-it}\,d\nu_a(x)\) exactly. Koukoulopoulos (2015), Theorem 1.2 for fixed \(q=5\) and length \(\delta>X^{1/6+\epsilon}\), supplies the arbitrary-logarithmic-saving **averaged** first-order error. The elementary supremum bound upgrades it to a squared-\(L^2\) error. Proper prime powers contribute a polynomially smaller error, since their total weight on \([X,3X]\) is \(O(\sqrt X\log X)\). Averaging over shifts of a common \(\delta\)-grid, as in PL-450--PL-451, therefore yields one grid shift for which, for any chosen fixed \(B>0\),
\[
e_{a,j}:=\nu_a(I_j),\qquad
\sum_{a\in U_5}\sum_j|e_{a,j}|^2
\ll_B \frac{X\delta}{(\log X)^B}.
\tag{3}
\]
Full cells are used in a slightly enlarged dyadic neighborhood; the two possible partial endpoint cells contribute \(O(\delta^2)\), absorbed in (3). If \(V_{a,j}=|\nu_a|(I_j)\), nonnegativity of \(\Lambda\) and (3) also give
\[
\sum_a\sum_j V_{a,j}^2\ll X\delta.
\tag{4}
\]

For the rectangular time average, the exact positive-definite integrated kernel is
\[
k_T(x,z)=W_X(x,z)\operatorname{sinc}(T\log(x/z)),\quad
W_X(x,z)=|[X,2X]\cap[x-H,x)\cap[z-H,z)|.
\tag{5}
\]
Its individual entries can be signed; positivity here refers to the **quadratic form** induced by the time/origin average. Let \(c_j\) be cell centers, \(K_{j\ell}=k_T(c_j,c_\ell)\), and \(E_{j\ell}=\sup_{x\in I_j,z\in I_\ell}|k_T(x,z)-K_{j\ell}|\). The elementary sinc-derivative and overlap estimates established explicitly in PL-451 give, with \(L=1+\log^+(H/u)\ll\log X\),
\[
\|K\|_{\rm op}\ll HmL/\delta,\qquad
\|E\|_{\rm op}\ll mL(1+H/u).
\tag{6}
\]
Expanding the signed-measure quadratic form, replacing each cell interaction by its center, and bounding the absolute-error bilinear form by \(\|E\|_{\rm op}\|V_a\|_2^2\), yields
\[
\begin{split}
\frac1{2T}\int_{-T}^T\int_X^{2X}|R_{a,t}(y)|^2\,dy\,dt
&=\sum_{j,\ell}e_{a,j}\overline{e_{a,\ell}}K_{j\ell}
+O(\|E\|_{\rm op}\|V_a\|_2^2)\\
&\ll_B XHmL\left((\log X)^{-B}+\delta/H+\delta/u\right).
\end{split}
\tag{7}
\]
All constants are uniform over \(u\ge X^\sigma\). Choose \(B>2\). Since \(\delta/H\le X^{\rho-\theta}\) and \(\delta/u\le X^{\rho-\sigma}\), the right side is \(o(XHm)\). The rectangular centered Gram is positive semidefinite; its operator norm is at most its trace, the sum of these four diagonal energies. Finally for any admissible nonnegative \(w\),
\[
\int w(t)\int\|R_t(y)\|^2dy\,dt
\le 2C\left(\frac1{2T}\int_{-T}^T\int\|R_t(y)\|^2dy\,dt\right),
\tag{8}
\]
which proves (1) for all stated time windows. Crucially the argument gives no lower bound at the **much smaller**, possibly vanishing, centered-energy scale.

## Source-realizable matched controls

Take any shifted full-cell grid of length \(\delta\) in the active interval. Let \(f_j\) equal \(\sin(2\pi(x-c_j)/\delta)\) on the cell \(I_j=[c_j,c_j+\delta]\) and zero outside. Each \(f_j\) is real, bounded by one, nonzero, and has exactly zero integral on every full grid cell. Choose cells well inside \([X,2X]\), and put \(\varepsilon_X=e^{-\sqrt{\log X}}<1/4\). For either control define
\[
d\mu_a(x)=\left(\tfrac14+\varepsilon_X f_a(x)\right)dx,
\qquad
P_{a,t}^{\mu}(y)=\int_y^{y+H}x^{-it}\,d\mu_a(x).
\tag{9}
\]
These are positive measures. Every complete \(\delta\)-cell has **exactly** mass \(\delta/4\) in each channel. Any shifted interval of length \(\delta\) consists of complete cells plus at most two partial cells, giving
\[
\sup_y\left|\mu_a((y,y+\delta])-\delta/4\right|
\le 2\varepsilon_X\delta
\ll_A\delta/(\log X)^A
\quad\text{for every fixed }A.
\tag{10}
\]
Thus both controls satisfy the fixed-modulus first-order estimate used in (3), in fact pointwise with super-logarithmic accuracy.

For the **shared** control set \(f_a=f_j\) for all four residues using one interior cell. Subtracting \(\tfrac14Q_t(y)\) leaves the same nonzero vector in all four channels, so its time/origin Gram is a positive scalar multiple of \(\mathbf1\mathbf1^*\), giving the first identity in (2).

For the **separated** control select four cells \(I_{j_a}\) at mutual distance strictly greater than \(H\), possible because \(H\le X^{1/2}\ll X\), and set \(f_a=f_{j_a}\). No window \((y,y+H]\) can intersect two distinct perturbation supports. The centered cross-products therefore vanish **pointwise in \((y,t)\)**; each centered self-energy is strictly positive because the window transform of a nonzero cell perturbation is not identically zero. The centered Gram is diagonal with positive entries, hence diagonal normalization gives \(I_4\). These opposite conclusions remain exact for every nonnegative density \(w\) of total mass one; no phase-cancellation or limiting argument is needed.

## Prior art, audit, and consequence

The genuine prime-distribution input is **D. Koukoulopoulos, “Primes in short arithmetic progressions,”** *International Journal of Number Theory* 11 (2015), Theorem 1.2 (source 116 in this line's SOURCES.md). The rectangular sinc transfer estimates and the discrete-grid normalization are already in **PL-451**; PL-450 provides the parallel Fejér raw-Gram analysis. Schur's test, signed-measure binning, and disjoint-support Gram realizations are standard analysis. No new theorem about prime distribution or zeta zeros, and no independent originality for these tools, is claimed.

The mathematical delta from PL-450--PL-451 is the **positive quadratic bound on the genuinely continuum-subtracted, complex-phase-centered source itself**, rather than only a rank-one asymptotic for its uncentered Gram. The explicit matched controls then show why this stronger first-order approximation still cannot decide the **normalized centered** PL-421 cone: normalization removes the size information on which (1) rests. Source atomicity, prime-pair singular series, and higher-order correlations are absent from these controls, so they do **not** rule out an arithmetic theorem using such additional information.

The remaining live implication has a precise missing premise: to assert the \(1/4\) lower frame for the actual centered residue covariance, one needs a **second-order covariance estimate at its own scale**, including oriented mixed channels, not merely finer first-order equidistribution or longer averaging that makes the common mode dominant. In particular (1) is not a positive local-factor deletion theorem, an RH/GRH implication, or a variance-scale asymptotic.
