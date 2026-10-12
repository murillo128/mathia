# PL-446 — Vertical Cesàro averaging makes the raw prime-window dephasing gate tautological, but not uniformly in window scale

**Evidence/status:** EXACT-DERIVED + CLASSICAL-ORTHOGONALITY + DECISIVE-NEGATIVE / ORDER-OF-LIMITS.

**Parent findings:** PL-072, PL-421, PL-422, PL-429, PL-445.

## Claim

Fix the live modulus \(p=5\), set \(U_5=\{1,2,3,4\}\), and let \(1\le H\le X/2\). For real \(t\) define the **uncentered** prime-window signals and their Hermitian Gram:
\[
P_{a,t}(y)=\sum_{\substack{y<n\le y+H\\n\equiv a\ (5)}}\Lambda(n)n^{-it},\qquad
S_X(t)_{ab}=\int_X^{2X}P_{a,t}(y)\overline{P_{b,t}(y)}\,dy.
\tag{1}
\]
Write the unweighted symmetric vertical average
\[
\overline S_{X,T}=\frac1{2T}\int_{-T}^T S_X(t)\,dt,\qquad T>0.
\tag{2}
\]

For **each fixed** \(X,H\), the finite Bohr/Cesàro mean exists and is exactly
\[
\boxed{\lim_{T\to\infty}\overline S_{X,T}
=\operatorname{Diag}(A_a(X,H)),\quad
A_a(X,H)=\sum_{n\equiv a\ (5)}
 \Lambda(n)^2 W_X(n,n),}
\tag{3}
\]
where \(W_X(n,m)\) is the nonnegative overlap weight from PL-445. For every sufficiently large \(X\), uniformly over \(1\le H\le X/2\), all \(A_a>0\). Therefore the vertically averaged **raw** covariance has correlation matrix \(I_4\) and passes the PL-421 strict image-cone gate:
\[
\boxed{\lim_{T\to\infty}\overline S_{X,T}
-\tfrac14\operatorname{Diag}\!\left(\lim_{T\to\infty}\overline S_{X,T}\right)
=\tfrac34\operatorname{Diag}(A_a)\succ0.}
\tag{4}
\]

This conclusion is independent of arithmetic pair cancellation and holds for **any** finitely supported nonnegative source weights assigned to disjoint residue channels with nonzero self-energy. Thus an unconditional positive cone verdict obtained only after **unweighted infinite vertical averaging** is a generic self-pair identity, not the missing arithmetic lower-frame theorem.

The order of limits is decisive. Choose \(H=X^\theta\), \(1/6<\theta\le1/2\), and let \(T_X>0\) satisfy
\[
\boxed{T_XH/X\longrightarrow0.}
\tag{5}
\]
The fixed-modulus short-AP \(L^2\) equidistribution already proved in PL-422 yields, uniformly for \(|t|\le T_X\),
\[
\boxed{
\frac{S_X(t)}{XH^2/16}\longrightarrow\mathbf1\mathbf1^*,
\qquad
\frac{\overline S_{X,T_X}}{XH^2/16}\longrightarrow\mathbf1\mathbf1^*
}
\tag{6}
\]
in matrix operator norm. Hence the normalized correlation matrices of both the pointwise and averaged raw Grams have least eigenvalue tending to \(0\), and eventually **fail** the PL-421 \(1/4\) gate. Condition (5) allows \(T_X\to\infty\), for example \(T_X=\log X\).

Writing \(C_{X,T}\) for the diagonal-correlation normalization of \(\overline S_{X,T}\), the iterated limits consequently disagree:
\[
\boxed{
\lim_{X\to\infty}\lim_{T\to\infty}C_{X,T}=I_4,\qquad
\lim_{T\to\infty}\lim_{X\to\infty}C_{X,T}=\mathbf1\mathbf1^*.
}
\tag{7}
\]
Both are legitimate limits; exchanging them erases precisely the covariance information needed for the local-factor test. In particular PL-445's **pointwise-in-\(t\)** sublogarithmic positivity is much stronger than the all-scale, fixed-\(X\) vertical-mean positivity established here.

## Exact Bohr-mean calculation

Opening (1) and using the exact overlap identity in PL-445 gives
\[
S_X(t)_{ab}
=\sum_{\substack{n\equiv a\ (5)\\m\equiv b\ (5)}}
 \Lambda(n)\Lambda(m)\,
 W_X(n,m)\,(n/m)^{-it}.
\tag{8}
\]
Only finitely many integers occur at fixed \(X,H\). Termwise averaging is therefore exact:
\[
\overline S_{X,T;ab}
=\sum_{\substack{n\equiv a\ (5)\\m\equiv b\ (5)}}
 \Lambda(n)\Lambda(m)\,
 W_X(n,m)\,\operatorname{sinc}\!\left(T\log(n/m)\right),
\tag{9}
\]
where \(\operatorname{sinc}(z)=\sin z/z\) and \(\operatorname{sinc}(0)=1\). Since \(\log(n/m)\ne0\) whenever \(n\ne m\), every distinct-integer term tends to zero as \(T\to\infty\); the surviving \(n=m\) terms belong to a single residue channel and give exactly (3). The same identity holds for arbitrary finite source coefficients after replacing \(\Lambda(n)^2\) by their squared magnitudes.

If \(n\in[X+H,2X]\), the full interval of origins \([n-H,n)\) lies inside \([X,2X]\), so \(W_X(n,n)=H\). Because \(H\le X/2\), the fixed-modulus prime number theorem supplies a prime in each reduced class within \([3X/2,2X]\) for all sufficiently large \(X\). This proves uniform strict positivity of every \(A_a\) without an estimate for a single distinct-prime pair.

The argument does not assert that \(S_X(t)\) passes the gate at every \(t\): positivity of each Gram and positivity of its vertical average are strictly weaker than preserving the PL-421 inverse-dephasing floor pointwise.

## Slow vertical horizons retain the polynomial-window collapse

For \(y\in[X,2X]\), \(y<n\le y+H\), and real \(t\),
\[
|n^{-it}-y^{-it}|
\le |t|\,|\log(n/y)|
\le |t|H/X.
\tag{10}
\]
Since \(\Lambda(n)\ge0\), we obtain the pointwise and \(L^2\) comparison
\[
|P_{a,t}(y)-y^{-it}P_{a,0}(y)|
\le |t|H/X\,P_{a,0}(y),
\tag{11}
\]
\[
\|P_{a,t}-y^{-it}P_{a,0}\|_{L^2[X,2X]}
\le |t|H/X\,\|P_{a,0}\|_2.
\tag{12}
\]
No prime-pair theorem enters (10)--(12). On the polynomial scale of the claim, PL-422's short-AP input gives
\[
\left\|P_{a,0}-\frac H4\right\|_2=o(H\sqrt X),
\qquad
\|P_{a,0}\|_2=\left(\frac14+o(1)\right)H\sqrt X.
\tag{13}
\]
Combining (12)--(13), uniformly for \(|t|\le T_X=o(X/H)\),
\[
\left\|P_{a,t}-\frac H4\,y^{-it}\right\|_2=o(H\sqrt X).
\tag{14}
\]
All four channels share the **same** \(y^{-it}H/4\) leading \(L^2\) vector. Cauchy--Schwarz applied to their Grams gives the first assertion in (6), uniformly in the indicated \(t\)-interval; averaging establishes the second. The diagonal entries are \(XH^2/16\,(1+o(1))\), so congruence by their inverse square roots gives the two normalized rank-one limits and the failed \(1/4\) floor.

For each fixed \(T\), condition (5) holds as \(X\to\infty\). For fixed \(X\), however, the finite sum (9) tends to its diagonal as \(T\to\infty\). This proves (7) without commuting either limiting operation. It also exposes a necessary scale distinction: frequencies of integers within the same length-\(H\) window differ by at most \(O(H/X)\). A vertical horizon much shorter than \(X/H\) cannot resolve that common-window coherence; arbitrarily long observation at **fixed** \(X\) eventually can.

## Prior art, matched controls, and limits

The entrywise Bohr mean, orthogonality of distinct logarithmic frequencies, and Dirichlet-polynomial mean-square estimates are classical. The line's existing primary anchor is Montgomery--Vaughan (1974), *Hilbert's Inequality*, DOI 10.1112/jlms/s2-8.1.73, already listed as source 62 in SOURCES.md and used in PL-072 to establish the \(N/T\) Fourier-resolution threshold. PL-429 already uses **frequency-weighted** Bohr means to recover complex covariance data. PL-422 supplies the actual-prime uncentered rank-one input; PL-445 supplies the separate uniformly twisted sublogarithmic self-pair regime. No new prime theorem or original harmonic-analysis identity is claimed.

The line-specific negative is the **noncommuting positive-image verdict** for the same arithmetic raw-window Gram: infinite unweighted vertical averaging passes automatically at all admitted window scales, even when every bounded or \(o(X/H)\) vertical range has a rank-one limit that fails. The result rules out that averaging operation as an independent RH-sensitive certificate and identifies its precise finite-horizon escape boundary.

The controls are essential. Replace \(\Lambda(n)\) by arbitrary finitely supported coefficients in disjoint channels: (3) still holds, so the positive limit cannot distinguish rational primes from sparse Beurling or generic frequency systems. Replace unweighted averaging by the **frequency-resolved** measurements of PL-429: off-diagonal coherence may be reconstructed rather than destroyed, so this finding does not obstruct tomography. Replace the raw Gram by a deterministically centered one: center terms can alter the Bohr mean, so (3)--(7) are **not** asserted without rederivation. Finally, nothing here constructs a zero-side continuation, bounds the source-subtracted PL-418 form, or proves RH.

## Consequence

A claimed local-factor repair for polynomial prime windows must control the original \(S_X(t)\), or a specified finite/resolution-preserving vertical statistic, at the **same** \(X,H,t\) regime where the arithmetic implication is sought. Averaging to \(T=\infty\) first creates a universal self-pair cone certificate and loses the unsymmetrized mixed-residue information. The live second-order fixed-mod-5 covariance and orientation estimates of PL-435--PL-439 remain necessary.
