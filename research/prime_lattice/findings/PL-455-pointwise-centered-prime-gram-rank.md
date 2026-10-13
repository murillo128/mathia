# PL-455 — A single vertical frequency gives full rank to the centered prime-residue Gram

**Evidence/status:** LITERATURE+EXACT-DERIVED + QUALITATIVE POINTWISE RANK / ATOMIC-JUMP CONTROL.

**Parent findings:** PL-421, PL-445, PL-452, PL-453, PL-454.

## Claim

Use the genuine von-Mangoldt source in four reduced residue classes \(U_5=\{1,2,3,4\}\), with exactly the phase-matched continuum subtraction of PL-452--PL-454:
\[
P_{a,t}(y)=\sum_{\substack{y<n\le y+H\\n\equiv a\pmod5}}\Lambda(n)n^{-it},\qquad
Q_t(y)=\int_y^{y+H}x^{-it}\,dx,\qquad
R_{a,t}(y)=P_{a,t}(y)-\frac14Q_t(y).
\]
For fixed \(X,H,t\), let
\[
S^R_X(t)_{ab}=\int_X^{2X}R_{a,t}(y)\overline{R_{b,t}(y)}\,dy .
\]

There exists an absolute \(X_0\) such that for **every** \(X\ge X_0\), \(1\le H\le X/2\), and \(t\in\mathbb R\),
\[
\boxed{S^R_X(t)\succ0,\qquad\operatorname{rank}S^R_X(t)=4.}\tag{1}
\]
In particular, **no averaging in vertical frequency is required even for qualitative full rank**. Consequently, for *any* nonzero finite positive Borel measure \(\omega\) on \(\mathbb R\), including a single Dirac mass,
\[
\boxed{\int_{\mathbb R} S^R_X(t)\,d\omega(t)\succ0.}\tag{2}
\]
The threshold \(X_0\) is independent of \(H,t,\omega\). This strengthens PL-454 for the **actual prime source**: PL-454 proved full rank for time weights positive on a positive-Lebesgue-measure set, using Fourier uniqueness; the present theorem also covers a single fixed \(t\).

The assertion is strictly qualitative. It supplies **no lower eigenvalue bound** uniform in \(X,H,t\), and in particular does not imply the \(\lambda_{\min}(C^R)>1/4\) diagonal-normalized inverse-dephasing gate of PL-421.

## An exact unpaired-jump criterion

For each residue \(a\), the function \(y\mapsto P_{a,t}(y)\) is a finite step function on \((X,2X)\). In the sense of distributions on this open interval,
\[
\frac{d}{dy}P_{a,t}(y)=
\sum_{\substack{n\equiv a\pmod5\\\Lambda(n)>0}}
\Lambda(n)n^{-it}(\delta_{n-H}-\delta_n),\tag{3}
\]
with only atoms whose locations lie in \((X,2X)\) contributing. By contrast, the common center is smooth and
\[
Q_t'(y)=(y+H)^{-it}-y^{-it}.\tag{4}
\]

A useful sufficient rank criterion follows: if for each \(a\in U_5\) there is an interior prime power \(n_a\in(X,2X)\), \(n_a\equiv a\pmod5\), such that **no prime power occurs at \(n_a+H\)**, then the four \(R_{a,t}\) are linearly independent in \(L^2([X,2X])\) for every real \(t\). Indeed, at the jump location \(y=n_a\) the *only* atomic derivative term among all four residue channels is
\(-\Lambda(n_a)n_a^{-it}\delta_{n_a}\) in channel \(a\); equation (4) contributes no atom. An \(L^2\) linear relation must have distributional derivative zero, forcing its coefficient in channel \(a\) to vanish. This is a general atomic-source criterion, not a prime-specific theorem.

For nonintegral \(H\), \(n_a+H\) cannot be an integer; for integral \(H\), an arithmetic exclusion is needed. Merely knowing that every residue class has active atoms, as in PL-454, does not alone establish this *pointwise-time* criterion for an arbitrary atomic source.

## Prime arithmetic supplies four unpaired jumps uniformly in the window length

Fix the interior interval \(I_X=(5X/4,7X/4)\), independent of \(H\). The prime number theorem in the four fixed reduced classes modulo \(5\) gives
\[
\#\{p\in I_X:\ p\equiv a\pmod5\}
=\left(\frac18+o(1)\right)\frac{X}{\log X}
\qquad(a\in U_5).\tag{5}
\]
If \(H\) is not an integer, every prime \(p\in I_X\) is automatically unpaired at \(p+H\).

Suppose \(H\) is a positive integer, \(H\le X/2\). The classical two-prime Selberg upper-bound sieve, applied with shift \(H\) uniformly in this range, gives
\[
\#\{p\in I_X:\ p,\ p+H\text{ both prime}\}
\ll \frac{X}{(\log X)^2}\,\mathfrak S(\{0,H\})
\ll \frac{X\log\log(3X)}{(\log X)^2}
=o\!\left(\frac{X}{\log X}\right).\tag{6}
\]
For the final bound, use
\(\mathfrak S(\{0,H\})\ll \prod_{q\mid H,\ q>2}(q-1)/(q-2)\ll\log\log(3H)\);
the odd-shift case is even simpler (the prime-pair singular series vanishes). These uniform sieve and singular-series estimates are the same as in PL-445 and PL-449, sourced to Lichtman--Teräväinen (2022), Lemmas 2.3--2.5, item 115 of SOURCES.md. There are only \(O(\sqrt X\log X)\) proper prime powers \(p^k\), \(k\ge2\), up to \(3X\). Since \(p+H<9X/4\) for \(p\in I_X\), the number of primes \(p\in I_X\) with \(p+H\) a *proper* prime power is also \(O(\sqrt X\log X)\).

The total excluded set in (6), plus proper prime powers at \(p+H\), has size \(o(X/\log X)\), **even before imposing any residue condition**. Comparison with (5) therefore supplies, for all sufficiently large \(X\), one prime \(p_a\in I_X\), \(p_a\equiv a\pmod5\), with \(\Lambda(p_a+H)=0\), simultaneously for all \(a\) and **uniformly over every integer \(1\le H\le X/2\)**. Together with the nonintegral case, this verifies the jump criterion without assumptions on prime-pair asymptotics.

## Proof of pointwise rank and the time-measure extension

For a fixed \(t\), let \(c=(c_a)_{a\in U_5}\in\mathbb C^4\). Its quadratic Gram form is
\[
c^*S^R_X(t)c=\int_X^{2X}\left|\sum_a\overline{c_a}R_{a,t}(y)\right|^2dy.\tag{7}
\]
If this were zero, the function inside the modulus would vanish almost everywhere, hence its distributional derivative would vanish. For each selected prime \(p_a\), the derivative has at \(y=p_a\) the atomic coefficient
\[
-\overline{c_a}(\log p_a)\,p_a^{-it}.\tag{8}
\]
No contribution at the same location comes from another residue channel or the continuum center, because \(\Lambda(p_a+H)=0\) when \(H\) is integral and no integer lies at \(p_a+H\) when \(H\) is nonintegral. Therefore (8) must be zero. As \(\log p_a>0\) and \(|p_a^{-it}|=1\), we obtain \(c_a=0\) for every \(a\). Thus the kernel is trivial and (1) follows.

For fixed finite \(X,H\), every matrix entry \(S^R_X(t)_{ab}\) is bounded and continuous in \(t\). By (1), for any fixed \(c\ne0\) the function \(t\mapsto c^*S^R_X(t)c\) is strictly positive everywhere. Its integral against any nonzero finite positive Borel measure is strictly positive, proving (2), including frequency measures supported on a single point.

## Prior art, falsification controls, and boundary of relevance

Distributional derivatives of translated interval indicators, the fixed-modulus prime number theorem, and the uniform upper-bound Selberg sieve are **classical**. This result does not assert novelty for those tools. The line-specific contribution is a new **source-adapted pointwise rank conclusion** for the phase-matched mod-5 Gram, which PL-454 did not establish. SOURCES.md already contains the primary sieve reference (Lichtman--Teräväinen 2022, item 115); no new source entry is needed.

The principal falsification cases are: a nonintegral window length causes no integer endpoint collisions; an integral length permits cancellation of jumps at \(p\) by an atom at \(p+H\), which is why the sieve exclusion is indispensable; the origin interval must have nonempty interior; and \(H=0\) would make every channel vanish. A matched atomic non-prime source with one unpaired outgoing jump per channel satisfies the identical theorem. A diffuse source can lack jumps entirely, consistent with PL-452's rank-deficient diffuse controls.

**Rank is not frame stability.** No quantitative lower bound on the smallest singular value is obtained; the statement neither gives pointwise-in-\(t\) inverse-dephasing positivity at polynomial \(H\), nor establishes the signed PL-418/PL-435--PL-439 source-covariance cone, analytic continuation, sensitivity to the Riemann zero divisor, or RH. The reason for full rank is the persistence of unmatched **atomic endpoints**, not an arithmetic cancellation mechanism.
