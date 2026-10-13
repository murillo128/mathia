# PL-454 — Exact finite-horizon rank of the phase-matched centered prime-residue Gram

**Evidence/status:** EXACT-DERIVED + CLASSICAL FOURIER UNIQUENESS / QUALITATIVE RANK BOUNDARY.

**Parent findings:** PL-421, PL-422, PL-447, PL-452, PL-453.

## Claim

Fix \(X>1\), \(H>0\), and a nonnegative integrable time weight \(w(t)\), not zero almost everywhere. Write \(U_5=\{1,2,3,4\}\), and use precisely the phase-matched continuum subtraction of PL-452 and PL-453:
\[
P_{a,t}(y)=\sum_{\substack{y<n\le y+H\\n\equiv a\ (5)}}\Lambda(n)n^{-it},\quad
Q_t(y)=\int_y^{y+H}x^{-it}\,dx,\quad
R_{a,t}(y)=P_{a,t}(y)-\tfrac14Q_t(y),\quad X\le y\le2X.
\]
Define the positive semidefinite four-channel Gram
\[
S^R_{ab}=\int_{\mathbb R}w(t)\int_X^{2X}
 R_{a,t}(y)\overline{R_{b,t}(y)}\,dy\,dt.
\]
Let the *active residue set* be
\[
A=\left\{a\in U_5:\ \exists\,n\equiv a\pmod5,\ \Lambda(n)>0,\
\big|[X,2X]\cap[n-H,n)\big|>0\right\}.
\]
Then the **exact kernel**, without any asymptotic hypothesis or lower bound on the time horizon, is
\[
\boxed{\ker S^R=
\left\{c\in\mathbb C^4:\ c_a=0\ (a\in A),\
\sum_{a\in U_5}c_a=0\right\}.}\tag{1}
\]
Consequently, if \(k=|A|\),
\[
\boxed{\operatorname{rank}S^R=\min(4,k+1),\qquad
\dim\ker S^R=\max(3-k,0).}\tag{2}
\]
In particular, **three active residue channels suffice for strict positive definiteness of the four-channel centered Gram**: the continuum-subtraction direction provides the last independent channel. If all four channels are active, the same conclusion holds.

For the actual von-Mangoldt source, the fixed-modulus prime number theorem makes all four channels active for every sufficiently large \(X\), uniformly over \(1\le H\le X/2\), since each residue class contains primes in a fixed interior subinterval of \([X,2X]\). Thus
\[
\boxed{S^R_{X,T}\succ0\quad
\text{for every }T>0,\ 1\le H\le X/2,\text{ and all sufficiently large }X,}\tag{3}
\]
for both rectangular and Fejér time densities in PL-453. Here “sufficiently large” is independent of \(H,T\).

The strict statement (3) is **qualitative**. It supplies no positive lower bound uniform in \(X,H,T\), and in particular does **not** establish the fixed \(\lambda_{\min}(C^R)\ge1/4\) image-cone floor of PL-421. PL-453 supplies a separate quantitative sufficient theorem only at high vertical resolution.

## Proof: finite atomic sources cannot cancel a continuous phase-matched component

For \(c\in\mathbb C^4\), the Gram identity gives
\[
c^*S^R c
=\int_{\mathbb R}w(t)\int_X^{2X}
\left|\sum_{a\in U_5}\overline{c_a}R_{a,t}(y)\right|^2\,dy\,dt.
\tag{4}
\]
Suppose this vanishes. For almost every origin \(y\), the function
\[
F_{c,y}(z)
=\sum_{\substack{y<n\le y+H\\n\bmod5\in U_5}}
\overline{c_{n\bmod5}}\Lambda(n)n^{-iz}
-\frac14\Big(\sum_{a\in U_5}\overline{c_a}\Big)
\int_y^{y+H}x^{-iz}\,dx
\tag{5}
\]
vanishes for almost every real \(t\) in the positive-measure set \(\{w>0\}\). The sum is finite and the integral is over a compact interval of positive numbers, so \(z\mapsto F_{c,y}(z)\) is **entire**. The identity theorem forces \(F_{c,y}\equiv0\).

At each such \(y\), (5) is the Fourier transform, after the change of variable \(v=\log x\), of the finite compactly supported complex measure
\[
d\nu_{c,y}(x)
=\sum_{\substack{y<n\le y+H\\n\bmod5\in U_5}}
\overline{c_{n\bmod5}}\Lambda(n)\,\delta_n(dx)
-\frac14\Big(\sum_a\overline{c_a}\Big)
\mathbf1_{(y,y+H]}(x)\,dx.
\tag{6}
\]
Uniqueness of the Fourier transform of finite measures implies \(\nu_{c,y}=0\). Its discrete and absolutely continuous parts are mutually singular. As \(H>0\), the continuous part first forces
\(\sum_a c_a=0\); then the atomic part forces \(c_{n\bmod5}=0\) for every prime power \(n\) contained in the window, for almost every \(y\).

If \(a\in A\), choose a witnessing prime power \(n\). By the definition of \(A\), the set of origins \(y\in[X,2X]\) with \(y<n\le y+H\) has positive measure, so the preceding almost-everywhere conclusion yields \(c_a=0\). This proves inclusion of the kernel in the right side of (1).

Conversely, if \(c_a=0\) on \(A\) and \(\sum_a c_a=0\), the atomic term in (5) vanishes for almost every origin and the continuum term vanishes identically. Hence (4) is zero and (1) follows. Among the \(4-k\) inactive coordinates, the single linear sum constraint has rank one whenever \(k<4\); for \(k=4\) there is no remaining coordinate. This gives (2).

For \(1\le H\le X/2\), each prime \(p\in[5X/4,7X/4]\) belongs to \((y,y+H]\) for a positive-measure set of origins \(y\in[X,2X]\). The fixed-modulus prime number theorem guarantees primes in each reduced class modulo 5 in this interior interval for all large \(X\). Thus \(A=U_5\), proving (3).

## What this settles, and what it does not

PL-422 and PL-447 exhibit *asymptotic* rank-one behavior for **uncentered** prime-window Grams at low vertical resolution. PL-452 shows that **first-order** equidistribution alone does not determine the normalized *centered* frame and provides diffuse positive-channel controls whose centered Gram has rank one or identity. PL-453 proves a **quantitative** centered frame bound only after sufficient high-frequency dephasing.

The exact theorem above separates these levels: a genuinely finite atomic von-Mangoldt source, with common continuum subtraction and any positive-measure vertical average, has no exact centered linear dependence once three residue classes are active. The rank-one diffuse control from PL-452 does not contradict this statement: smooth perturbations can be linearly dependent and are not singular atomic measures relative to the continuum. On the other hand, arbitrarily weak linear independence can coexist with a vanishing normalized spectral gap along a sequence; exact rank does not imply a stable Riesz lower bound.

The proof is an immediate specialization of **classical** entire-function uniqueness, Fourier uniqueness for compact measures, and separation of mutually singular measures; no new harmonic-analysis theorem or prime-distribution estimate is asserted. The line-specific exact contribution is (1)–(2) for the **phase-matched mod-5 centered source**, including the one-dimensional extra continuum direction and the distinction from PL-452's diffuse controls. This theorem persists for any finite nonnegative atomic source on the same residue channels with the same continuum subtraction; it therefore cannot select rational primes against matched atomic generalized-prime controls, imply analytic continuation, prove the PL-418 source-subtracted signed cone, or establish RH.

The essential falsification boundaries are: \(H>0\); a time weight positive on a set of positive Lebesgue measure (not a single point mass in frequency); exact continuum subtraction as in (5); and genuinely **atomic** rather than diffuse sources. If no residue is active, all four centered channels equal \(-Q_t/4\), and (2) correctly gives rank one. If exactly two are active, the two absent channels have one difference vector in the kernel, and (2) gives rank three. These checks also show the active-set classification is sharp.
