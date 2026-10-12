# PL-447 — Critical-scale vertical averaging still leaves the polynomial prime-window Gram rank one

**Evidence/status:** LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE / FINITE-RESOLUTION BOUNDARY.

**Parent findings:** PL-072, PL-421, PL-422, PL-445, PL-446.

## Claim

Fix the four reduced residues \(a\in U_5=\{1,2,3,4\}\), \(H=X^\theta\), and \(1/6<\theta\le1/2\). Define the **uncentered** twisted von-Mangoldt window vectors and their Gram as in PL-446:
\[
P_{a,t}(y)=\sum_{\substack{y<n\le y+H\\n\equiv a\ (5)}}\Lambda(n)n^{-it},\qquad
S_X(t)_{ab}=\int_X^{2X}P_{a,t}(y)\overline{P_{b,t}(y)}\,dy.
\]
For \(r\in[1,2]\) and \(\tau\in\mathbb R\), set
\[
F_\tau(r)=\int_0^1e^{-i\tau v/r}\,dv,
\qquad
W(\tau)=\int_1^2|F_\tau(r)|^2\,dr
=\int_1^2\operatorname{sinc}^2\!\left(\frac{\tau}{2r}\right)dr,
\]
where \(\operatorname{sinc}(z)=\sin(z)/z\) with its continuous value at zero. **For every fixed \(M<\infty\), uniformly over \(|t|H/X\le M\)**, with \(\tau=tH/X\),
\[
\boxed{\frac{16}{XH^2}S_X(t)
=W(\tau)\,\mathbf1\mathbf1^*+o_M(1)}
\tag{1}
\]
in matrix operator norm. Moreover \(W(\tau)>0\) for every finite \(\tau\), and its minimum on every compact interval is strictly positive. It follows that
\[
\boxed{\sup_{|t|\le MX/H}
\big\|C_X(t)-\mathbf1\mathbf1^*\big\|_{\mathrm{op}}\longrightarrow0,}
\qquad C_X(t)=D_X(t)^{-1/2}S_X(t)D_X(t)^{-1/2}.
\tag{2}
\]
Here \(D_X(t)=\operatorname{Diag}S_X(t)\), which has positive entries for large \(X\) uniformly in the stated range.

Let \(T_X>0\), \(\kappa_X=T_XH/X\le M\), and form the symmetric Cesàro mean \(\bar S_{X,T_X}=(2T_X)^{-1}\int_{-T_X}^{T_X}S_X(t)dt\). Defining
\[
\bar W(\kappa)=
\begin{cases}
(2\kappa)^{-1}\int_{-\kappa}^{\kappa}W(\tau)\,d\tau,&\kappa>0,\\
1,&\kappa=0,
\end{cases}
\]
one has, **uniformly for bounded \(\kappa_X\)**,
\[
\boxed{\frac{16}{XH^2}\bar S_{X,T_X}
=\bar W(\kappa_X)\mathbf1\mathbf1^*+o_M(1),\qquad
\bar C_{X,T_X}\to\mathbf1\mathbf1^*.}
\tag{3}
\]
In particular, the pointwise and averaged normalized Grams eventually fail the PL-421 image-cone threshold \(\lambda_{\min}(C)\ge1/4\) throughout **every bounded multiple of the critical vertical horizon \(X/H\)**. For eventual positivity of the averaged raw-window gate, the condition
\[
\boxed{T_XH/X\longrightarrow\infty}
\tag{4}
\]
is therefore **necessary, not sufficient**. This strictly extends PL-446, which established rank-one collapse only when \(T_XH/X\to0\); the critical regime \(T_X\asymp X/H\) also cannot resolve the residue channels.

## Derivation from fixed-subwindow short-AP equidistribution

PL-422, using Theorem 1.2 of Koukoulopoulos (2015) plus its explicit prime-power bound, gives for any fixed positive integer \(K\), \(\delta=H/K\), and \(j=0,\ldots,K-1\),
\[
A_{a,j}(y):=\sum_{\substack{y+j\delta<n\le y+(j+1)\delta\\n\equiv a\ (5)}}\Lambda(n),
\qquad
\left\|A_{a,j}-\frac\delta4\right\|_{L^2[X,2X]}
=o_K(\delta\sqrt X).
\tag{5}
\]
Indeed \(\delta=X^{\theta+o(1)}\), and for each **fixed** \(K\) the theorem applies with a fixed \(\varepsilon>0\) satisfying \(1/6+2\varepsilon<\theta\). Translating origins by \(j\delta=O(H)\) only adds a boundary strip of length \(O(H)\); its contribution is negligible by \(A_{a,j}\ll\delta\log X\) and \(H/X\to0\). Prime powers contribute \(o_K(\delta\sqrt X)\) in \(L^2\) by PL-422's argument. This requires no result on correlations between distinct primes.

For \(|t|H/X\le M\), an integer \(n\in(y+j\delta,y+(j+1)\delta]\) satisfies
\[
|n^{-it}-(y+j\delta)^{-it}|
\le |t|\log\!\left(1+\frac\delta X\right)\le\frac MK.
\tag{6}
\]
Since \(\Lambda(n)\ge0\), replacing the phase by its left-endpoint value on every subwindow costs at most \((M/K)P_{a,0}(y)\) pointwise. From PL-422, \(\|P_{a,0}\|_2=O(H\sqrt X)\). Replacing the subwindow masses by \(\delta/4\) using (5) then incurs \(o_K(H\sqrt X)\), uniformly in \(t\). The resulting Riemann sum differs from the continuous model
\[
M_t(y):=\frac14\int_y^{y+H}u^{-it}\,du
\tag{7}
\]
by at most \(O(MH/K)\) pointwise. Therefore
\[
\limsup_{X\to\infty}\ 
\sup_{|t|H/X\le M}\frac{\|P_{a,t}-M_t\|_2}{H\sqrt X}
\ll\frac MK.
\]
Letting the **fixed** partition size \(K\to\infty\) proves
\[
\boxed{\sup_{|t|H/X\le M}\|P_{a,t}-M_t\|_2=o_M(H\sqrt X),}
\tag{8}
\]
uniformly in the four residue classes. This is a fixed-mesh approximation followed by a mesh limit, not an unproved uniform prime theorem for all arbitrarily short subwindows.

Writing \(y=Xr\), \(t=\tau X/H\), one has
\[
\frac{4M_t(Xr)}H
=(Xr)^{-it}\int_0^1\exp\!\left[-it\log\left(1+\frac{Hv}{Xr}\right)\right]dv
=(Xr)^{-it}\big(F_\tau(r)+o_M(1)\big)
\tag{9}
\]
uniformly in \(r\in[1,2]\) and \(|\tau|\le M\), because \(H/X\to0\). The unit-modulus prefactor disappears in the squared norm, so
\[
\frac{16}{XH^2}\|M_t\|_2^2=W(\tau)+o_M(1).
\tag{10}
\]
All four channels approximate the **same** vector \(M_t\). Expanding their Gram entries and applying Cauchy--Schwarz to the errors in (8) proves (1). The function \(W\) is continuous; it is positive for each finite \(\tau\) because \(F_\tau(r)\) cannot vanish for almost every \(r\in[1,2]\). Compactness makes its lower bound uniform, so diagonal normalization yields (2). Integrating the uniform relation (1) over \([-T_X,T_X]\), changing variables \(\tau=tH/X\), and normalizing gives (3), including sequences for which \(\kappa_X\) does not converge. If (4) failed for an eventually admissible averaged Gram, a bounded subsequence \(\kappa_X\le M\) would contradict (3).

## Prior art, controls, and boundaries

The only prime-distribution input is Koukoulopoulos (2015), Theorem 1.2, already used in PL-422 for unweighted fixed-modulus short-interval sums. The partition approximation for bounded scaled phase and the limiting \(\operatorname{sinc}\) profile are elementary consequences of that theorem, not new distribution results. PL-072/Montgomery--Vaughan supply the separate classical long-time mean-value perspective. PL-446 gives the fixed-\(X\) \(T\to\infty\) diagonal limit and the previously narrower \(TH/X\to0\) obstruction. The present mathematical delta is the **uniform critical-scale extension** and its explicit universal amplitude profile, yielding the necessary divergence (4).

The same argument applies to any four nonnegative source channels with the common \(L^2\) short-window equidistribution (5), so it does not distinguish rational primes from a suitable matched generalized-frequency model. The positivity failure is for the **uncentered** Gram and its **unweighted symmetric** vertical average. It does not rule out phase-resolved inversion/tomography, a deterministically centered covariance, or any different local-factor representation. Nor does it establish failure at all horizons satisfying \(T_XH/X\to\infty\): condition (4) is necessary only, and even very long finite means may retain information not visible here. No new RH implication or zero-side continuation is obtained.

## Consequence

Increasing a vertical averaging range from \(o(X/H)\) to any **fixed multiple** of \(X/H\) does not repair the polynomial-window positive-image gate. At these scales, the common prime mean acquires a nontrivial \(\operatorname{sinc}\) envelope but the residue channels remain asymptotically collinear. The first possible escape requires genuinely supercritical frequency resolution \(T_XH/X\to\infty\), together with a separately justified arithmetic covariance estimate; infinite-time Bohr orthogonality from PL-446 cannot be used as that estimate.