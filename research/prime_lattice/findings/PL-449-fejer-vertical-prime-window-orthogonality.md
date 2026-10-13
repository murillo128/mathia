# PL-449 — Fejér vertical smoothing removes the log-log loss in finite prime-window orthogonality

**Evidence/status:** LITERATURE+EXACT-DERIVED + FINITE-RESOLUTION SUFFICIENCY / GENERIC SELF-PAIR CONTROL.

**Parent findings:** PL-072, PL-421, PL-445, PL-446, PL-447, PL-448.

## Claim

Let \(U_5=\{1,2,3,4\}\), \(X\to\infty\), and \(1\le H\le X/2\). For the **uncentered** von-Mangoldt residue windows
\[
P_{a,t}(y)=\sum_{\substack{y<n\le y+H\\n\equiv a\pmod5}}\Lambda(n)n^{-it},
\qquad
S_X(t)=\int_X^{2X}P_t(y)P_t(y)^*\,dy,
\]
define the normalized, triangularly weighted time mean
\[
F_{X,T}=\frac1T\int_{-T}^T\left(1-\frac{|t|}{T}\right)S_X(t)\,dt
\qquad(T>0).
\]
The weight is nonnegative and has total mass one. Let \(A_X=\operatorname{Diag}(A_a)\) be the exact self-pair diagonal from PL-448:
\[
A_a=\sum_{\substack{n\equiv a\pmod5}}\Lambda(n)^2W_X(n,n),
\quad
W_X(n,m)=\big|[X,2X]\cap[n-H,n)\cap[m-H,m)\big|,
\quad
A_a=(1+o(1))\,XH\log X/4
\]
uniformly in the stated \(H\)-range. Put
\[
u=X/T,\qquad
b_X(T)=\frac{\min(u,u^2)}{\log X},\qquad
\eta_X(T)=(1+u)\frac{\log X}{\sqrt X}.
\]
Then, uniformly for \(T>0\) and \(1\le H\le X/2\),
\[
\boxed{
\frac{\|F_{X,T}-A_X\|_{\mathrm{op}}}{XH\log X}
\ll b_X(T)+\eta_X(T)+
\sqrt{(1+b_X(T))\eta_X(T)}.
}
\tag{1}
\]
In particular, if \(T=T_X\) satisfies
\[
\boxed{\quad \frac{T_X\log X}{X}\longrightarrow\infty,\quad}
\tag{2}
\]
then the diagonal-correlation normalization
\[
C^{F}_{X,T}=\big(\operatorname{Diag}F_{X,T}\big)^{-1/2}
F_{X,T}\big(\operatorname{Diag}F_{X,T}\big)^{-1/2}
\]
obeys
\[
\boxed{\sup_{1\le H\le X/2}
\|C^F_{X,T_X}-I_4\|_{\mathrm{op}}\longrightarrow0.}
\tag{3}
\]
A sufficiently large fixed multiple \(T_X=CX/\log X\) already suffices for the strict PL-421 floor \(\lambda_{\min}(C^F)>1/4\) for large \(X\), although not for convergence to the identity. The sufficient horizon (2) is shorter by a factor \(\log\log X\) than PL-448's **rectangular Cesàro** sufficient horizon, but concerns a different, deliberately smoothed time statistic.

## Exact Fejér kernel and prime-pair bound

At fixed \(X,H\) every Dirichlet polynomial is finite. The Fourier transform of the triangular weight gives exactly
\[
\frac1T\int_{-T}^T\left(1-\frac{|t|}T\right)e^{-it\xi}\,dt
=\operatorname{sinc}^2(T\xi/2),
\qquad \operatorname{sinc}(v)=\frac{\sin v}{v}.
\tag{4}
\]
Consequently
\[
F_{X,T;ab}
=\sum_{\substack{n\equiv a\pmod5\\m\equiv b\pmod5}}
\Lambda(n)\Lambda(m)W_X(n,m)
\operatorname{sinc}^2\left(\frac T2\log(n/m)\right).
\tag{5}
\]
The \(n=m\) terms form exactly \(A_X\). All entries in (5) are real and nonnegative, although this entrywise property is **not** an arithmetic cancellation statement. Moreover \(W_X(n,m)\le H\), and it vanishes whenever \(|n-m|\ge H\).

First restrict (5) to ordinary primes \(p,q\), writing \(F^{\rm pr}\) and \(A^{\rm pr}\). Such primes lie in \([X,3X]\). For \(k=|p-q|\ge1\),
\[
|\log(p/q)|\ge k/(3X),\qquad
\operatorname{sinc}^2\left(\frac T2\log(p/q)\right)
\ll\min\left(1,\frac{u^2}{k^2}\right),
\tag{6}
\]
where absolute constants in the comparison absorb the fixed factor from \(3X\).

The unconditional two-prime Selberg sieve gives, uniformly for \(1\le k\le X/2\),
\[
N_X(k):=\#\{p,p+k\in[X,3X]:p,p+k\text{ prime}\}
\ll\frac{Xw(k)}{\log^2 X},
\quad
w(k)=\prod_{\substack{\ell\mid k\\\ell>2}}\frac{\ell-1}{\ell-2}.
\tag{7}
\]
For odd \(k\) and sufficiently large \(X\), the left side is zero. The elementary squarefree-divisor expansion
\[
w(k)=\sum_{\substack{d\mid k\\d\text{ odd squarefree}}}
\prod_{\ell\mid d}\frac1{\ell-2}
\]
gives
\[
\sum_{1\le k\le U}w(k)
\le U\prod_{\ell>2}\left(1+\frac1{\ell(\ell-2)}\right)\ll U.
\tag{8}
\]
Partial summation in (8) gives \(\sum_{k>U}w(k)/k^2\ll1/U\) for \(U\ge1\), and \(\sum_{k\ge1}w(k)/k^2<\infty\). Splitting at \(k=u\) therefore yields
\[
\sum_{1\le k\le H}w(k)\min(1,u^2/k^2)
\ll
\begin{cases}
u^2,&0<u\le1,\\
u,&u\ge1.
\end{cases}
\tag{9}
\]
Absorb the fixed comparison constant in (6) into the implied constants of (9).

Each ordered pair of distinct primes contributes a rank-one matrix unit of operator norm one, with coefficient at most \(H(\log 3X)^2\) times the kernel. By the triangle inequality, (6)--(9) imply
\[
\boxed{
\|F^{\rm pr}_{X,T}-A^{\rm pr}_X\|_{\rm op}
\ll XH\min(u,u^2)
=XH\log X\,b_X(T).
}
\tag{10}
\]
This is where Fejér smoothing matters: the quadratic tail in (6) permits the **ordinary first moment** \(\sum_{k\le U}w(k)\ll U\), whereas the nearest-gap Hilbert-inequality bound used for the unsmoothed mean in PL-448 carries a reciprocal-gap \(\log\log X\) loss.

## Proper prime powers and normalization

Let \(F^{\rm pp}\) be the same Fejér Gram with the sum restricted to proper prime powers \(n=p^j\), \(j\ge2\). The triangular density never exceeds twice the normalized rectangular density on \([-T,T]\). Since the integrand is a positive semidefinite Gram, the full-integer-frequency Montgomery--Vaughan estimate used in PL-448 applies, giving
\[
\|F^{\rm pp}\|_{\rm op}
\ll (1+X/T)\,H\sqrt X\log^2X
=XH\log X\,\eta_X(T).
\tag{11}
\]
Also \(\|A^{\rm pp}\|_{\rm op}\ll H\sqrt X\log^2X\). Cauchy--Schwarz in the joint weighted time/origin Hilbert space controls the two prime--proper-power cross Grams:
\[
\|\text{cross terms}\|_{\rm op}
\le2\sqrt{\|F^{\rm pr}\|_{\rm op}\|F^{\rm pp}\|_{\rm op}}
\ll XH\log X\sqrt{(1+b_X(T))\eta_X(T)},
\tag{12}
\]
because the fixed-modulus PNT and (10) give \(\|F^{\rm pr}\|_{\rm op}\ll XH\log X(1+b_X(T))\). Combining (10)--(12) and subtracting \(A^{\rm pp}\) proves (1).

The fixed-modulus weighted PNT gives \(A_a=(1+o(1))XH\log X/4\) uniformly in \(H\): write \(A_a=\int_0^H\sum_{X+v<n\le2X+v,\ n\equiv a(5)}\Lambda(n)^2\,dv\) and use the uniform PNT asymptotic for all \(0\le v\le H\le X/2\). Under (2) both \(b_X(T)\) and \(\eta_X(T)\) tend to zero. Thus the diagonal of \(F\) is asymptotic to \(A_X\), and diagonal congruence of (1) proves (3). At \(T=CX/\log X\) the bound is \(O(1/C)+o(1)\); choosing an absolute \(C\) large enough gives the strict \(1/4\) lower-frame margin.

## Prior art, checks, and boundaries

The Fejér identity (4), positivity of a weighted Gram, Selberg prime-pair upper bounds, fixed-modulus PNT, and Montgomery--Vaughan mean-value bounds are all classical. The required primary anchors are already in this line's SOURCES.md: Montgomery--Vaughan (1974), source 62, and Lichtman--Teräväinen (2022), Lemmas 2.3--2.5, source 115. PL-445 gives the prime-pair singular-series average; PL-448 provides the ordinary-prime / proper-prime-power separation and the **different** rectangular-mean comparison. No new prime-pair asymptotic, improvement to the unsmoothed Cesàro bound, or independent theorem about zeta zeros is claimed.

The endpoint controls agree with the exact formula: when \(H\le1\), two distinct integers cannot lie in the same window, so \(F=A_X\) exactly; at fixed \(X,H\), letting \(T\to\infty\) forces \(F\to A_X\) by frequency orthogonality, while \(T\downarrow0\) gives \(F\to S_X(0)\). The same proof works for a matched generic nonnegative source with the same diagonal density, two-point sieve-type upper bound, and negligible sparse secondary frequencies. It does **not** select rational primes over matched Beurling controls.

For polynomial \(H=X^\theta\), \(1/6<\theta\le1/2\), PL-447's rank-one obstruction persists for every Fejér horizon \(TH/X=O(1)\), because its convergence is uniform pointwise on that frequency interval. The necessary critical-scale divergence and the sufficient bound (2) remain separated. The result applies only to the **uncentered raw-window Fejér mean**, not to pointwise-in-\(t\) positivity, the sharp rectangular Cesàro mean of PL-448, the centered PL-418 covariance, or the oriented PL-435--PL-439 arithmetic lower-frame problem. The positive floor arises from smoothed self-pair orthogonality, not RH-relevant signed cancellation.

## Consequence

Replacing the sharp time-window indicator by its nonnegative triangular Fejér convolution changes the quantitative diagonalization threshold from the reciprocal-gap upper bound \(T\gg X\log\log X/\log X\) in PL-448 to \(T\gg X/\log X\). The gain measures the smoothing kernel's Fourier decay rather than new arithmetic information. Any attempt to use this positive-image certificate for a global zeta assertion still needs a separate, source-specific transfer that preserves the missing signed covariance and zero-side structure.
