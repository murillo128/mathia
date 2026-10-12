# FD-319 — Four vanishing Farey-index defects carry macroscopic energy

**Status:** EXACT-DERIVED + PNT-ASSISTED-ASYMPTOTIC + NEGATIVE/CONTROL-DESIGN + SHARP-FOUR-STITCH-FAMILY.

FD-315 proves rigidity when *every* Hall--Shiu/Farey index is integral; FD-316--FD-318 give reflection-symmetric directed-edge reassemblies with six nonintegral indices, including a nonzero limiting discrepancy energy and fixed sine modes. The six defects are not needed. A different, central Farey excursion makes **four** defects sufficient, and each index differs from the integer \(1\) by only \(1/p\).

For every odd prime \(p\ge7\), there is an explicitly reconstructed increasing rational grid \(F_p^\dagger\) from \(0\) to \(1\) that preserves the complete directed denominator-edge multiset of the genuine \(F_p\), its positive-gap multiset, its outer boundary pair, and reflection. Exactly four of its \(N_p-1\) interior indices \(\nu_i=(q_{i-1}+q_{i+1})/q_i\) are nonintegral; their values in order are
\[
\frac{p-1}{p},\quad\frac{p+1}{p},\quad
\frac{p+1}{p},\quad\frac{p-1}{p}. \tag{1}
\]
Thus \(\max_i\operatorname{dist}(\nu_i,\mathbb Z)=1/p\) and \(\sum_i\operatorname{dist}(\nu_i,\mathbb Z)=4/p\to0\), even though the reassembly is nontrivial.

Let \(N_p=\sum_{q\le p}\varphi(q)\), let \(x_k\) be the genuine Farey points, and define
\[
E_p=\sum_{k=1}^{N_p-1}(x_k-k/N_p)^2.
\]
With \(E_p^\dagger\) defined on the reassembled grid using the same ranks,
\[
\boxed{\lim_{p\to\infty}(E_p^\dagger-E_p)
=\frac{3}{4\pi^2}>0.} \tag{2}
\]
For the normalized Dirichlet sine coefficients
\[
d_j^\dagger(p)=\sqrt{\frac{2}{N_p}}
\sum_{k=1}^{N_p-1}(x_k^\dagger-k/N_p)\sin(\pi jk/N_p),
\]
all odd \(j\) vanish exactly, and for every fixed \(r\ge1\),
\[
\boxed{\lim_{p\to\infty}d_{2r}^\dagger(p)
=\frac{\sqrt6}{2\pi^2r}\,[1-(-1)^r].} \tag{3}
\]
The squares of the limits (3) exhaust the full energy in (2). Four index errors tending to zero therefore do not control even a fixed macroscopic spectral mode under the complete directed-edge and reflection constraints.

## 1. Symmetric exchange around the sparse central excursion

Use FD-316's denominator-\(p\) excursions \(E_j\), \(1\le j\le p-2\), from \(j/p\) to \((j+1)/p\). Set \(a=(p-1)/2\), so \(p=2a+1\). Because
\[
a/p<1/2<(a+1)/p
\]
and both adjacent fractions have determinant one with \(1/2\), the central excursion is exactly
\[
C=E_a=(p,2,p)
\]
as a denominator path, with just two gaps. Let
\[
A=E_1E_2\cdots E_{a-1},\qquad
B=E_{a+1}E_{a+2}\cdots E_{p-2}.
\]
The genuine interior order is \(ACB\), whereas the alternative uses
\[
\boxed{BCA} \tag{4}
\]
between the unchanged external edges \(1\to p\) and \(p\to1\). All excursions begin and end at \(p\), so this permutation keeps every directed denominator edge with the same multiplicity. Reconstruct \(x_k^\dagger\) by putting the original positive Farey gap \(1/(q_k^\dagger q_{k+1}^\dagger)\) on each reassembled edge. The gap multiset is unchanged and sums to one.

Farey reflection gives \(E_{p-1-j}=\operatorname{reverse}(E_j)\); thus \(B=\operatorname{reverse}(A)\), while \(C\) is self-reversed. Consequently \(BCA\) is also a palindromic denominator word, and \(x_{N_p-k}^\dagger=1-x_k^\dagger\).

The genuine points \(a/p\) and \((a+1)/p\) are immediate Farey neighbors of \(1/2\), at ranks \(N_p/2-1\) and \(N_p/2+1\). Hence \(A\) and \(B\) both contain exactly
\[
K=N_p/2-2 \tag{5}
\]
gaps and have the same geometric width \((a-1)/p\). The central two points and the external first/last edges retain their ranks and coordinates.

## 2. Exactly four defects of size \(1/p\)

At every stitch internal to an unchanged excursion the index is the original integer Farey index. The only altered stitches are the four joins created by (4). The first successor denominator of \((a+1)/p\) equals \(p-2\), because \((a+1)^{-1}\equiv2\pmod p\). The predecessor denominator of \((p-1)/p\) is \(p-1\). The middle path \(C\) has its inner denominator \(2\); at the first excursion \(E_1\), the first successor denominator of \(1/p\) is \(p-1\); the predecessor denominator of \(a/p\) is \(p-2\), since \(a^{-1}\equiv-2\pmod p\).

Therefore the four new triples, in order, are
\[
(1,p,p-2),\quad(p-1,p,2),\quad
(2,p,p-1),\quad(p-2,p,1).
\]
Dividing the outer-denominator sums by the middle denominator gives precisely (1). Every other triple remains genuine, so there are exactly four defects. Each is at distance \(1/p\) from the positive integer \(1\), not merely a noninteger with an uncontrolled fractional part.

Four is also the **minimum number of defects among nonidentity, reflection-symmetric permutations of these complete prime-order excursions**. Indeed, the stitch between \(E_j\) and \(E_k\) has index
\[
\nu=1+\frac{(j+1)^{-1}-k^{-1}}p,
\]
using inverses in \(\{1,\ldots,p-1\}\); it is integral exactly when \(k=j+1\). The left and right outer stitches are integral exactly when the first and last excursion have labels \(1\) and \(p-2\). Thus the defect count equals the number of non-successor adjacencies in the excursion-label permutation augmented by sentinels \(0,p-1\). A nonidentity permutation with these fixed sentinels has at least three such breaks: zero, one, or two breaks can only concatenate at most three increasing consecutive runs, which the fixed endpoints force back into their original order. Under reflection, breaks pair across the central position. Because \(p-2\) is odd, no break is self-paired, so the count is even and therefore at least four. This minimality statement is limited to the excursion-permutation family, not arbitrary labeled paths.

## 3. Exact displacement identity and unconditional energy limit

Write \(N=N_p\) and \(D_k=x_k-k/N\). The block \(B\) moves from its original right-half location into the left-half rank slots \(2\le k\le N/2-1\). Its coordinate translation is \(-a/p\), whereas its rank translation is \(-N/2\); hence its discrepancy changes by **exactly** \(+1/(2p)\). The block \(A\) moves in the opposite direction and has discrepancy shift \(-1/(2p)\). All other points retain their discrepancies.

Therefore there is an exact permutation \(P\) of the original discrepancy coordinates with
\[
D^\dagger=PD+v,\qquad
v_k=\begin{cases}
 1/(2p),&2\le k\le N/2-1,\\
-1/(2p),&N/2+2\le k\le N-1,\\
0,&\text{otherwise},
\end{cases}
\]
so
\[
\|v\|_2^2=\frac{2K}{4p^2}
=\frac{N-4}{4p^2},\qquad
E_p^\dagger-E_p=\|v\|_2^2+2\langle PD,v\rangle. \tag{6}
\]

The needed genuine-Farey fact is **unconditional** \(E_p=o(1)\), established in FD-318 from the exact FD-002 Franel--Mertens identity and PNT. Briefly, in FD-002 notation
\(NE_p=(2\pi^2)^{-1}\sum_{k\ge1}|B_p(k)|^2/k^2-1/12\),
where \(B_p(k)=\sum_{d\mid k,d\le p}dM(\lfloor p/d\rfloor)\).
PNT gives \(B_p(k)/p\to0\) for each fixed \(k\), and the domination
\(|B_p(k)|/p\le\tau(k)\) allows dominated convergence since
\(\sum_k\tau(k)^2/k^2<\infty\).
Thus \(E_p=o(1)\) without assuming RH.

As \(\|v\|_2=O(1)\),
\[
|\langle PD,v\rangle|\le\sqrt{E_p}\|v\|_2=o(1).
\]
Together with the standard \(N_p/p^2\to3/\pi^2\), (6) gives (2).

## 4. Fixed modes and complete spectral accounting

The contribution of \(PD\) to each normalized sine coefficient is \(o(1)\) by Cauchy--Schwarz; the coefficients of \(v\) are explicit. Reflection pairs the two nonzero blocks, yielding for fixed \(r\)
\[
d_{2r}^\dagger(p)=
2\sqrt{\frac2N}\frac1{2p}
\sum_{k=2}^{N/2-1}\sin(2\pi rk/N)+o(1).
\]
After division by \(N\), the sum tends to
\(\int_0^{1/2}\sin(2\pi rt)\,dt=[1-(-1)^r]/(2\pi r)\).
Since \(\sqrt{2N}/p\to\sqrt6/\pi\), this proves (3); genuine fixed-mode coefficients tend to zero because \(E_p\to0\).

Only odd values of \(r\) contribute to (3), and
\[
\sum_{r\ge1}\left(
\frac{\sqrt6}{2\pi^2r}[1-(-1)^r]\right)^2
=\frac6{\pi^4}\sum_{\substack{r\ge1\\r\ \mathrm{odd}}}\frac1{r^2}
=\frac3{4\pi^2}. \tag{7}
\]
This matches the complete limiting energy (2). Finite Dirichlet Parseval then shows that no positive residual energy escapes to modes with growing frequency.

## 5. Exact and numerical falsification; prior-art boundary

An independent denominator-word enumeration checked \(p=7,11,29,101,211,809\). Each reassembly preserved every directed edge count, preserved the palindrome, and gave exactly the four indices (1); the total absolute integrality defect was \(4/p\). At \(p=7\), exact rational evaluation gives
\[
E_7=\frac{197}{7560},\qquad
E_7^\dagger=\frac{2567}{52920},\qquad
E_7^\dagger-E_7=\frac{11}{490}.
\]
At \(p=809\), the finite diagnostics were
\(E_{809}^\dagger-E_{809}\simeq0.07514943\) and
\(d_2^\dagger(809)\simeq0.24891578\);
the corresponding limits are \(0.07599088773\) and \(0.24818520006\).
The proof is exact apart from its explicitly PNT-assisted asymptotic; finite checks are falsification controls, not evidence of asymptotic truth.

The Farey neighbor criterion, Hall--Shiu index, modular-inverse neighbor denominators, totient asymptotic, Franel--Mertens identity, and PNT are classical or already derived and sourced in FD-002/FD-315--FD-318 and this line's SOURCES.md. The current same-gap permutation work of García (2026, *Mathematics* 14, 2543), classical BCZ/Farey dynamics, and nearby Farey-discrepancy/kernel papers were checked as prior-art boundaries; none found in the targeted audit supplied this *four vanishing-index-defect* excursion certificate. No broad novelty claim is made beyond this explicit construction and implication.

This is a **matched labeled-edge control**, not an alternative actual Farey sequence. Its denominator labels cease to be the true reduced denominators at the defective joins, so it does not contradict the exact-integrability rigidity of FD-315. It establishes no new estimate on genuine \(E_p\), no RH implication, and no general stability result for arbitrary weakly defective paths. Its control-design conclusion is precise: keeping the complete directed denominator-edge inventory, reflection, all but four exact Farey-index stitches, and even a vanishing \(\ell^1\) *and* uniform distance of indices to integers still does not coerce global quadratic or fixed-mode spectral discrepancy.