# PL-448 — Finite vertical averaging diagonalizes the prime-window Gram at a prime-gap-weighted horizon

**Evidence/status:** LITERATURE+EXACT-DERIVED + FINITE-RESOLUTION SUFFICIENCY + GENERIC SELF-PAIR CONTROL.

**Parent findings:** PL-072, PL-421, PL-445, PL-446, PL-447.

## Claim

Fix the reduced residues $U_5=\{1,2,3,4\}$, $X\to\infty$ and $1\le H\le X/2$. Define the **uncentered** von-Mangoldt residue windows and their vertical Cesàro-averaged Gram by

$$
P_{a,t}(y)=\sum_{\substack{y<n\le y+H\\n\equiv a\ (5)}}\Lambda(n)n^{-it},\qquad
\overline S_{X,T}=\frac1{2T}\int_{-T}^T\int_X^{2X}P_t(y)P_t(y)^*\,dy\,dt.
$$

Let $A_X=\operatorname{Diag}(A_a)$ be the exact self-pair diagonal, with $A_a=\sum_{n\equiv a\ (5)}\Lambda(n)^2 W_X(n,n)$ and $W_X(n,n)=|[X,2X]\cap[n-H,n)|$. The fixed-modulus PNT yields, uniformly in $H$, $A_a=(1+o(1))XH\log X/4$. Put

$$
\epsilon_X(T)=\frac{X\log\log X}{T\log X},\qquad
\eta_X(T)=\left(1+\frac XT\right)\frac{\log X}{\sqrt X}.
$$

Then, uniformly for $T>0$ and $1\le H\le X/2$,

$$
\boxed{\frac{\|\overline S_{X,T}-A_X\|_{\mathrm{op}}}{XH\log X}
\ll \epsilon_X(T)+\eta_X(T)+\sqrt{(1+\epsilon_X(T))\eta_X(T)}.}
\tag{1}
$$

In particular, if $T_X/(X\log\log X/\log X)\to\infty$, the diagonal-normalized correlation matrix $\overline C_{X,T_X}$ satisfies

$$
\boxed{\sup_{1\le H\le X/2}\|\overline C_{X,T_X}-I_4\|_{\mathrm{op}}\to0,}
$$

and hence eventually passes the strict $\lambda_{\min}>1/4$ inverse-dephasing image-cone threshold of PL-421. A sufficiently large fixed constant multiple of the displayed $T_X$ scale also suffices for a strict cone margin. Neither condition is sharp. This complements the necessary divergence $T_XH/X\to\infty$ at polynomial $H$ proved in PL-447, and improves the generic $T\gg X$ integer-frequency sufficient scale from PL-072 for the prime-supported raw Gram.

## Sieve bound for nearest-prime gaps

Let $I_X=[X,3X]$ and $d_X(p)$ be the nearest distance from a rational prime $p\in I_X$ to another prime of $I_X$. For $K=\lfloor\log X\rfloor$, primes with $d_X(p)>K$ contribute at most $\pi(3X)/K\ll X/(K\log X)$ to $\sum 1/d_X(p)$. For smaller gaps, overcount all pairs of primes $p,p+k$ with $1\le k\le K$. The unconditional Selberg upper-bound sieve gives

$$
\#\{p,p+k\in I_X:p,p+k\text{ prime}\}\ll\frac{Xw(k)}{\log^2X},\qquad
w(k)=\prod_{\substack{\ell\mid k\\\ell>2}}\frac{\ell-1}{\ell-2}.
$$

The divisor expansion from PL-445 yields $\sum_{k\le u}w(k)\ll u$, hence $\sum_{k\le K} w(k)/k\ll\log K\ll\log\log X$. Thus

$$
\sum_{p\in I_X}\frac1{d_X(p)}\ll\frac{X\log\log X}{\log^2X},\qquad
\boxed{\sum_{p\in I_X}\frac{(\log p)^2}{d_X(p)}\ll X\log\log X.}\tag{2}
$$

No conjectural prime-pair asymptotic is used.

## Weighted Montgomery–Vaughan mean value

For each origin $y$ and complex unit vector $z\in\mathbb C^4$, let

$$
Q_{z,y}(t)=\sum_{\substack{y<p\le y+H\\p\text{ prime},\ p\bmod5\in U_5}}
\overline{z_{p\bmod5}}(\log p)p^{-it}.
$$

The nearest logarithmic frequency separation of a prime in that window is at least $d_X(p)/(3X)$. The individually weighted Montgomery–Vaughan Hilbert inequality for distinct real frequencies yields

$$
\left|\frac1{2T}\int_{-T}^{T}|Q_{z,y}(t)|^2\,dt
-\sum_{y<p\le y+H}|z_{p\bmod5}|^2(\log p)^2\right|
\ll\frac XT\sum_{y<p\le y+H}\frac{|z_{p\bmod5}|^2(\log p)^2}{d_X(p)}.
$$

Integrating the origin $y\in[X,2X]$, observing that each prime occurs for at most $H$ origins, and taking the supremum over unit $z$, (2) implies for the ordinary-prime Gram

$$
\boxed{\|\overline S^{\mathrm{pr}}-A^{\mathrm{pr}}\|_{\mathrm{op}}
\ll \frac{HX^2\log\log X}{T}=XH\log X\,\epsilon_X(T),}
$$

with $\|\overline S^{\mathrm{pr}}\|_{\mathrm{op}}\ll XH\log X(1+\epsilon_X(T))$ by fixed-modulus PNT.

## Proper prime powers and normalization

The elementary bound $\sum_{n\in I_X,\ n=r^k,\ k\ge2}\Lambda(n)^2\ll\sqrt X\log^2X$ holds. Applying the ordinary full-integer-frequency Montgomery–Vaughan theorem to the proper-prime-power polynomial for each origin gives

$$
\|\overline S^{\mathrm{pp}}\|_{\mathrm{op}}
\ll (1+X/T)H\sqrt X\log^2X=XH\log X\,\eta_X(T),
$$

and its self-pair diagonal obeys $\|A^{\mathrm{pp}}\|_{\mathrm{op}}\ll XH\log X\eta_X(T)$. Cauchy–Schwarz in the joint time/origin Hilbert space bounds the two prime/power mixed Gram terms by

$$
2\sqrt{\|\overline S^{\mathrm{pr}}\|_{\mathrm{op}}\|\overline S^{\mathrm{pp}}\|_{\mathrm{op}}}
\ll XH\log X\sqrt{(1+\epsilon_X(T))\eta_X(T)}.
$$

Adding these bounds gives (1). The exact diagonal satisfies

$$
A_a=\int_0^H\sum_{\substack{X+u<n\le2X+u\\n\equiv a\ (5)}}\Lambda(n)^2\,du
=\frac{XH\log X}{4}(1+o(1)),
$$

uniformly for $u\le H\le X/2$ by the fixed-modulus weighted PNT. Both errors in (1) tend to zero under the stated $T_X$ hypothesis; since all $A_a\asymp XH\log X$, positive diagonal normalization yields the asserted limit and strict PL-421 cone criterion.

## Prior art and limitations

This is a derived consequence of **Montgomery–Vaughan (1974), “Hilbert's Inequality”**, source 62 in `research/prime_lattice/SOURCES.md`, and **Lichtman–Teräväinen (2022), Lemmas 2.3–2.5**, source 115. The diagonal estimate uses fixed-modulus PNT. The generic inequalities are classical; no new prime-gap theorem, prime-pair asymptotic, or general mean-value bound is claimed. The line-specific delta is the explicit finite-horizon sufficient scale for the PL-446 raw mod-5 Gram.

A sparse generalized-frequency control with the same inverse-nearest-gap bound and diagonal mass also satisfies the estimate. Thus the positive image cone is again dominated by universal **self-pair/shot-noise orthogonality** after averaging, not by signed arithmetic cancellation that distinguishes rational primes. Nothing here establishes the pointwise-in-$t$ cone, the centered/PL-418 source-subtracted covariance, the PL-435–PL-439 oriented second-order lower frame, analytic continuation, or any RH consequence. The intermediate frequency range between PL-447's necessary and this finding's sufficient horizons remains open.