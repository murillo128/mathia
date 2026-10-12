# FD-318 — Six index defects create macroscopic Farey energy and fixed modes

**Status:** EXACT-DERIVED + PNT-ASSISTED-ASYMPTOTIC + NEGATIVE/CONTROL-DESIGN + FIXED-MODE-SPECTRAL-NONRIGIDITY.

FD-316 preserves the directed denominator-edge inventory of a prime-order Farey sequence while breaking precisely six Hall--Shiu index stitches. FD-317 swaps two *short endpoint excursions*, obtaining an energy change of order \(1/p\), with the change invisible in sublinear modes. A longer excursion swap changes the outcome qualitatively.

For every fixed \(0<\theta<1/2\), there is an explicit reflection-symmetric rational grid \(F_p^*(\theta)\), for all sufficiently large primes \(p\), with exactly the same directed denominator-edge inventory, induced positive-gap multiset, and boundary pair as the genuine \(F_p\), but with **exactly six noninteger Farey indices**. Writing \(N_p=\sum_{q\le p}\varphi(q)\) for the number of gaps and
\[
E_p=\sum_{k=1}^{N_p-1}(x_k-k/N_p)^2,
\]
the reassembled grid has
\[
\boxed{\lim_{p\to\infty}(E_p^*-E_p)
=\frac{6\theta}{\pi^2}\left(\frac{\pi^2}{6}-1\right)^2>0.}\tag{1}
\]
In particular, the defect density is \(6/(N_p-1)=\Theta(p^{-2})\), but the quadratic discrepancy changes by an **order-one** quantity, not merely by the Franel \(1/p\) power scale of FD-317.

Use the orthonormal Dirichlet sine coefficients on the *rank* grid
\[
d_j(p)=\sqrt{\frac2{N_p}}\sum_{k=1}^{N_p-1}
(x_k-k/N_p)\sin(\pi jk/N_p),\qquad 1\le j<N_p.
\]
Reflection makes all odd \(j\) coefficients vanish. For each **fixed** \(r\ge1\), the genuine coefficients tend to zero, while
\[
\boxed{\lim_{p\to\infty}d_{2r}^*(p)
=\frac{\sqrt6}{\pi^2 r}\left(\frac{\pi^2}{6}-1\right)
[1-\cos(2\pi r\theta)].}\tag{2}
\]
The squares of these fixed-mode limits sum to the *entire* energy limit (1). Hence the effect is not merely mass escaping into higher and higher frequencies.

## 1. An exact six-defect excursion permutation

Let \(E_a\), \(1\le a\le p-2\), be the denominator-edge path in \(F_p\) from \(a/p\) to \((a+1)/p\). Each begins and ends at denominator \(p\); reflection gives \(E_{p-1-a}=\operatorname{reverse}(E_a)\) as denominator paths. Fix \(m=\lfloor\theta p\rfloor\). For all sufficiently large \(p\), \(2\le m\) and \(2m<p-1\), so the following two swaps are disjoint.

In the left portion replace
\[
E_1\,(E_2\cdots E_m)\quad\longmapsto\quad
(E_2\cdots E_m)\,E_1,
\]
and perform the reflected swap in the right portion. Leave every other excursion and the two external edges \(1\to p\) and \(p\to1\) unchanged. Every excursion is a closed \(p\)-to-\(p\) denominator path, so concatenation preserves **each directed edge with its exact multiplicity**. Assigning to an edge \((a,b)\) its original Farey gap \(1/(ab)\) then gives an increasing rational grid from zero to one with the same gap multiset. The reflected swap preserves the palindrome of gaps and therefore exact point reflection.

All interior triples of an original excursion are unchanged. Only three stitches on the left (and their three reflected partners) can change. Let \(s\in\{1,\dots,p-1\}\) be the inverse of \(m+1\bmod p\). The three new triples of denominator labels at the left interfaces are
\[
(1,p,(p-1)/2),\qquad
(s,p,p-1),\qquad
((p+1)/2,p,p-s).
\]
The middle Hall--Shiu index \((a+c)/b\) at these triples is never an integer. For the first triple the numerator is \((p+1)/2\), strictly between zero and \(p\). For the second, divisibility by \(p\) would force \(s=1\), or \(m+1\equiv1\pmod p\). For the third it would force \(s=(p+1)/2\), or \(m+1\equiv2\pmod p\). Both congruences contradict \(2\le m<p-1\). All remaining stitches are genuine, so the number of noninteger indices is **exactly six**.

This preserves local *edge labels*, not global realizability as actual reduced denominators at every reassembled point; it is deliberately a matched control rather than another Farey sequence.

## 2. Exact permutation-plus-displacement identity

Set \(N=N_p\), \(D_k=x_k-k/N\), and \(L=(p+1)/2\), the gap count of \(E_1\). Let \(B\) denote the concatenated block \(E_2\cdots E_m\), with \(K\) gaps. Its geometric width is \((m-1)/p\).

Index each excursion by the points *after* its starting vertex and up to and including its terminal vertex, avoiding duplicate boundary vertices. Upon swapping, each point of \(B\) moves geometrically left by \(1/p\) and earlier by \(L\) rank positions. Thus its discrepancy changes by the same exact amount
\[
\beta_p=\frac{L}{N}-\frac1p.
\]
Each point of \(E_1\) moves geometrically right by \((m-1)/p\) and later by \(K\) ranks, giving
\[
\alpha_p=\frac{m-1}{p}-\frac KN.
\]
Reflected points experience the negatives of these shifts. All other points keep their discrepancies.

There is consequently an **exact permutation** \(P_p\) of the original rank-discrepancy vector \(D=(D_1,\dots,D_{N-1})\) and a displacement vector \(v_p\) such that
\[
D^*=P_pD+v_p,\qquad
\|v_p\|_2^2=2K\beta_p^2+2L\alpha_p^2. \tag{3}
\]
On the left, \(v_p\) equals \(\beta_p\) at the \(K\) new positions occupied by \(B\), and \(\alpha_p\) at the \(L\) new positions occupied by \(E_1\); on the right it has the reflected negative values. In particular,
\[
E_p^*-E_p=\|v_p\|_2^2+2\langle P_pD,v_p\rangle. \tag{4}
\]
This formula is finite and uses no asymptotics or random sampling.

## 3. Unconditional disappearance of genuine Farey energy

The uniform Farey counting estimate, obtained by Möbius inversion and the elementary divisor-sum bound, is
\[
\#\{x_k\le x\}=Nx+O(p\log p)
\]
uniformly for \(x\in[0,1]\), up to the harmless endpoint convention. It yields
\[
K/N=(m-1)/p+O(\log p/p),\qquad
\alpha_p=O(\log p/p), \tag{5}
\]
and, from \(N=(3/\pi^2)p^2+O(p\log p)\),
\[
\frac K{p^2}\longrightarrow \frac{3\theta}{\pi^2},\quad
p\beta_p\longrightarrow a:=\frac{\pi^2}{6}-1,\quad
2L\alpha_p^2=O(\log^2p/p)\longrightarrow0. \tag{6}
\]

For the cross term, it is essential not to assume the RH-strength Franel bound. The **unconditional** \(E_p=o(1)\) follows directly from the exact FD-002 identity and the prime number theorem. In FD-002 notation, let \(M(t)=\sum_{n\le t}\mu(n)\) and
\[
B_p(k)=\sum_{\substack{d\mid k\\d\le p}}d\,M(\lfloor p/d\rfloor).
\]
That exact identity reads
\[
NE_p=\frac1{2\pi^2}\sum_{k\ge1}\frac{|B_p(k)|^2}{k^2}-\frac1{12}. \tag{7}
\]
PNT is equivalent to \(M(t)=o(t)\); for each fixed \(k\), it implies \(B_p(k)/p\to0\). The trivial bound \(|M(t)|\le t\) gives \(|B_p(k)|/p\le\tau(k)\), and
\(\sum_{k\ge1}\tau(k)^2/k^2<\infty\). Dominated convergence in (7) gives \(\sum_{k\ge1}|B_p(k)|^2/k^2=o(p^2)\). Since \(N\asymp p^2\),
\[
\boxed{E_p=o(1)\qquad\text{unconditionally}.} \tag{8}
\]
No RH bound, zero-free-region rate, or unproved cancellation estimate is used.

Combining (3)--(8) gives \(\|v_p\|_2=O(1)\) and
\[
|\langle P_pD,v_p\rangle|
\le\sqrt{E_p}\,\|v_p\|_2=o(1).
\]
Therefore
\[
E_p^*-E_p=2K\beta_p^2+o(1)
\longrightarrow \frac{6\theta}{\pi^2}a^2,
\]
which is (1).

## 4. Every fixed even coefficient, and exhaustion of the full limit

The \(K\) left-block displacement entries lie at consecutive ranks \(2,\dots,K+1\); their reflected entries lie at \(N-K-1,\dots,N-2\). The contributions of \(P_pD\) to any normalized sine coefficient are \(o(1)\) by (8) and Cauchy--Schwarz. The entries of size \(\alpha_p\) likewise have total squared norm \(2L\alpha_p^2=o(1)\).

For fixed \(r\), exact reflection doubles the left-block sine contribution:
\[
d_{2r}^*(p)=
2\sqrt{\frac2N}\,\beta_p
\sum_{k=2}^{K+1}\sin(2\pi rk/N)+o(1).
\]
As \(K/N\to\theta\), the sum divided by \(N\) tends to
\[
\int_0^\theta\sin(2\pi rt)\,dt
=\frac{1-\cos(2\pi r\theta)}{2\pi r}.
\]
Using \(\sqrt{2N}\,\beta_p\to(\sqrt6/\pi)a\) proves (2). The same argument with \(D\) alone gives \(d_{2r}(p)\to0\).

The classical Fourier-series identity
\[
\sum_{r\ge1}\frac{\cos(2\pi r t)}{r^2}
=\pi^2(t^2-t+1/6),\qquad0\le t\le1,
\]
implies, for \(0<\theta<1/2\),
\[
\sum_{r\ge1}\frac{[1-\cos(2\pi r\theta)]^2}{r^2}
=\pi^2\theta. \tag{9}
\]
Hence the sum of squares of the limits in (2) is
\[
\frac{6a^2}{\pi^4}\pi^2\theta
=\frac{6\theta a^2}{\pi^2},
\]
exactly the limiting total energy in (1), because \(E_p\to0\). By finite Dirichlet Parseval, the high-mode tail can therefore be made uniformly small after fixing a sufficiently large mode cutoff: **there is no missing limiting energy carried by growing frequencies**. This is a strong spectral conclusion, not just a fixed-coefficient calculation.

## 5. Finite falsification and literature boundary

The construction was checked independently by generating prime-order Farey denominator words using the classical successor recurrence, permuting entire \(p\)-to-\(p\) excursions, reconstructing gaps as \(1/(q_iq_{i+1})\), and checking the directed-edge multiset and the count of noninteger indices. For tested primes through \(809\) and \(\theta\in\{0.18,0.25,0.33\}\), each reassembly preserved the edge multiset and gave **exactly six** noninteger indices. Numerical energies and sine coefficients approached (1)--(2).

For example, at \(\theta=1/4\) the limits are \(E_p^*-E_p\to0.06321529218\) and \(d_2^*(p)\to0.16006309041\); at \(p=809\) the corresponding finite diagnostics were approximately \(0.0633651\) and \(0.1590866\). These computations test the implementation; the theorem follows from the exact displacement identity and PNT, not from numerical extrapolation.

The Farey neighbor relation, Hall--Shiu/BCZ index recurrence, totient count, Möbius/Farey harmonic identity, prime number theorem, and Bernoulli Fourier series are classical. Their source anchors already appear in this line's SOURCES.md (including FD-002 and the Hall--Shiu/Farey-index sources). García's 2026 treatment of same-gap permutations is relevant neighboring literature, but does not supply this six-defect macroblock/fixed-mode control certificate. We claim only the explicit matched-control obstruction and its stated asymptotics, not general novelty for Farey dynamics or discrepancy theory.

Most importantly, the new grid is **not** Farey-realizable with the assigned denominator labels at all stitches; the result does not contradict the rigidity of FD-315. No bound on genuine Farey discrepancy has improved, and no Möbius cancellation or RH consequence is claimed. The obstruction is to an inference from *density-one local index compatibility plus the full directed denominator-edge inventory* to global quadratic or even fixed-mode spectral control. The missing information is where the exceptional stitches sit and which macroscopic excursion blocks they rewire.
