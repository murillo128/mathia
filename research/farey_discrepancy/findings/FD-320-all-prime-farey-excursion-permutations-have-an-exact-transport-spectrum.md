# FD-320 — All prime-Farey excursion permutations have an exact transport spectrum

**Status:** EXACT-DERIVED + PNT-ASSISTED-UNIFORM-ASYMPTOTIC + NEGATIVE/CONTROL-DESIGN + FULL-SPECTRAL-TRANSPORT-CLASSIFICATION.

FD-316--FD-319 give particular prime-order denominator-edge reassemblies: six defects can alter fixed modes, and four vanishing-size defects can carry a nonzero energy limit. The whole excursion-permutation class admits a finite combinatorial reduction, not just those examples. Its two relevant outputs are independent: a **permutation-break count** gives the exact number and sizes of noninteger Farey indices, while a **weighted cumulative-length transport potential** gives the complete discrepancy spectrum with an error tending to zero *uniformly over all permutations*. In particular, bounded defect count can coexist with order-one energy (FD-319), whereas an unbounded number of defects can coexist with energy tending to zero.

## 1. Exact objects and claim

Let \(p\ge7\) be an odd prime, \(N=N_p=\sum_{q\le p}\varphi(q)\), and \(0=x_0<\cdots<x_N=1\) the genuine Farey grid. For \(1\le j\le n:=p-2\), let \(E_j\) be the complete denominator-\(p\)-to-\(p\) excursion from \(j/p\) to \((j+1)/p\). Write \(\ell_j\ge1\) for its number of gaps, so \(\sum_{j=1}^n\ell_j=N-2\). Every excursion has exact geometric width \(1/p\).

For any permutation \(\sigma=(\sigma(1),\ldots,\sigma(n))\), concatenate \(E_{\sigma(1)},\ldots,E_{\sigma(n)}\), retaining the original first and last edges \(1\to p\) and \(p\to1\). Identify repeated endpoint \(p\) vertices and reconstruct an increasing rational grid by assigning each directed denominator edge \((a,b)\) its original positive gap \(1/(ab)\). Denote the resulting rank discrepancies by \(D_k^\sigma=x_k^\sigma-k/N\) for \(1\le k<N\).

Define the original and reordered cumulative length mismatches
\[
 w_j=\frac{\ell_j}{N}-\frac1p,\qquad
 U_j=\sum_{i<j}w_i,\qquad
 U_t^\sigma=\sum_{s<t}w_{\sigma(s)}.
\]
Put
\[
 T_p(\sigma)=\sum_{t=1}^{n}\ell_{\sigma(t)}
       (U_{\sigma(t)}-U_t^\sigma)^2. \tag{1}
\]
All entries in (1) are determined by the **excursion gap counts and their permutation**; no within-excursion denominator or point is needed.

**Complete transport theorem.** There is an explicit permutation \(P_\sigma\) of the genuine interior discrepancy vector \(D=(x_k-k/N)_{1\le k<N}\), and a block-constant vector \(v^\sigma\), such that
\[
 D^\sigma=P_\sigma D+v^\sigma,\qquad
 \|v^\sigma\|_2^2=T_p(\sigma). \tag{2}
\]
Consequently, for *every* sequence of permutations \(\sigma=\sigma_p\), including permutations depending arbitrarily on \(p\),
\[
 \boxed{\left|\sqrt{E_p^\sigma}-\sqrt{T_p(\sigma)}\right|
            \le\sqrt{E_p}=o(1),}\qquad
 E_p^\sigma:=\|D^\sigma\|_2^2. \tag{3}
\]
The \(o(1)\) is unconditional and **uniform in \(\sigma\)**. Thus \(E_p^\sigma\to0\) if and only if \(T_p(\sigma)\to0\). If \(T_p(\sigma)\to C<\infty\), then \(E_p^\sigma\to C\). When \(T_p\) is unbounded, (3) remains a norm statement and must not be replaced by the unjustified absolute claim \(E_p^\sigma-T_p=o(1)\).

For the normalized Dirichlet sine transform
\[
 \widehat z_m=\sqrt{\frac2N}\sum_{k=1}^{N-1}
       z_k\sin(\pi mk/N),\qquad 1\le m<N,
\]
the stronger **all-mode identity** holds:
\[
 \boxed{\sum_{m=1}^{N-1}
  |\widehat{D^\sigma}_m-\widehat{v^\sigma}_m|^2=E_p=o(1).} \tag{4}
\]
This is full spectral \(\ell^2\) control, not just convergence of every fixed mode. No reflection assumption is needed for (1)--(4).

## 2. Proof of block transport and uniformity

Let \(A_j=\sum_{i<j}\ell_i\) and \(A_t^\sigma=\sum_{s<t}\ell_{\sigma(s)}\). Represent an excursion by the points *after* its start, including its endpoint; the genuine points of \(E_j\) occupy ranks \(1+A_j+h\), \(1\le h\le\ell_j\). The reassembled copy of \(E_{\sigma(t)}\) occupies ranks \(1+A_t^\sigma+h\). This partitions ranks \(2,\ldots,N-1\) without duplicating a stitch endpoint; rank \(1\) stays untouched.

Because every excursion has width \(1/p\), a point in \(E_{\sigma(t)}\) is translated geometrically by \((t-\sigma(t))/p\), while its rank changes by \(A_t^\sigma-A_{\sigma(t)}\). Its discrepancy shift is therefore exactly
\[
 \frac{t-\sigma(t)}p
 -\frac{A_t^\sigma-A_{\sigma(t)}}N
 =U_{\sigma(t)}-U_t^\sigma. \tag{5}
\]
Set \(v^\sigma_1=0\), and set \(v^\sigma_k\) equal to (5) throughout the corresponding reordered block. Moving the original rank-discrepancy entries along with their excursions defines \(P_\sigma\) and proves (2), including the weighted sum (1).

The reverse triangle inequality applied to (2) proves the finite bound
\[
 \left|\|D^\sigma\|_2-\|v^\sigma\|_2\right|\le\|D\|_2. \tag{6}
\]
FD-318 derives the unconditional \(E_p=\|D\|_2^2=o(1)\) from the exact FD-002 Franel--Mertens identity and the prime number theorem: for each fixed divisor-mode index, the relevant normalized finite Mertens transform tends to zero, and the square-summable divisor-function majorant permits dominated convergence. Crucially, this bound is independent of \(\sigma\). This proves (3). The discrete sine transform is orthogonal on ranks \(1,\ldots,N-1\), so applying Parseval to \(D^\sigma-v^\sigma=P_\sigma D\) proves the exact (4).

## 3. Exact index defect formula for every permutation

Adjoin sentinel labels \(\sigma(0)=0\) and \(\sigma(n+1)=p-1\). At an interface between the preceding excursion label \(j=\sigma(t)\) and the following label \(k=\sigma(t+1)\), including the two outer interfaces, the three denominator labels are
\[
 \big((j+1)^{-1}\bmod p,\ p,\ p-(k^{-1}\bmod p)\big).
\]
Here modular inverses are represented by integers in \(\{1,\ldots,p-1\}\); for the outer sentinels, the expression gives the actual boundary denominator \(1\). Thus the Hall--Shiu index there is exactly
\[
 \nu_{j,k}=1+
 \frac{[(j+1)^{-1}]_p-[k^{-1}]_p}{p},\qquad
 0<\nu_{j,k}<2. \tag{7}
\]
It is an integer precisely when \(k=j+1\). All other interior indices belong to unchanged genuine excursions and stay integral. Consequently,
\[
 \boxed{\#\{\text{noninteger Farey indices}\}
 =\sum_{t=0}^{n}{\bf1}_{\{\sigma(t+1)\ne\sigma(t)+1\}}.} \tag{8}
\]
Formula (7) also supplies each individual distance to the nearest integer. Formula (8) counts **permutation breaks**, whereas (1) measures weighted cumulative length mismatch. Neither statistic determines the other.

If \(\sigma(t)=p-1-\sigma(n+1-t)\), the reordered word is reflection symmetric, so every odd sine coefficient in (4) vanishes identically. The formulas and the energy estimate otherwise remain unchanged. The even-break lower bound of four for nonidentity reflection-symmetric full-excursion permutations was already proved in FD-319; it is not a new general minimum over arbitrary labeled paths.

## 4. Opposite direction: many defects but vanishing energy

For one isolated adjacent excursion transposition \(E_jE_{j+1}\mapsto E_{j+1}E_j\), formula (5) gives shifts \(+w_j\) on the moved \(E_{j+1}\) and \(-w_{j+1}\) on the moved \(E_j\), and zero elsewhere. Hence
\[
 T_p(\text{one swap})=
 \ell_{j+1}w_j^2+\ell_jw_{j+1}^2. \tag{9}
\]
Every denominator \(q\le p\) contributes at most one Farey fraction strictly inside an interval of length \(1/p\), hence \(\ell_j\le p\). As \(N\asymp p^2\), uniformly in \(j\),
\[
 |w_j|\le \frac pN+\frac1p=O(p^{-1}),\qquad
 T_p(\text{one swap})=O(p^{-1}). \tag{10}
\]

Choose \(m=m(p)\to\infty\) with \(m=o(p)\), take \(m\) disjoint adjacent transpositions separated by at least one unchanged excursion in the left portion, and perform the reflected transpositions in the right portion. For sufficiently large \(p\), these \(2m\) transpositions are disjoint and noninteracting. Their individual transport potentials have disjoint supports because each swapped pair has unchanged total length, so
\[
 T_p(\sigma_p)=O(m/p)=o(1),\qquad
 \#\{\text{defects}\}=6m\longrightarrow\infty. \tag{11}
\]
This family preserves reflection and the *complete* directed denominator-edge inventory; by (3), \(E_p^{\sigma_p}\to0\) unconditionally. In particular \(m=\lfloor\sqrt p\rfloor\) produces a diverging defect count with vanishing full spectral energy.

Conversely, FD-319 supplies a reflection-symmetric reassembly with **exactly four** defects, each at distance \(1/p\) from the integer \(1\), but with \(E_p^\dagger-E_p\to3/(4\pi^2)>0\). Together these examples show that neither few defects (even with vanishing total fractional-index error) nor many defects alone predict the quadratic or spectral error. The quantitative transport statistic (1), rather than the defect count (8), is the exact observable for this permutation family.

## 5. Falsification, sources, and scope

A separate finite check enumerated the exact Farey fractions for \(p=7,11,29,101\), reconstructed randomly permuted excursions from the original gap subwords, and independently evaluated both sides of (2). The largest coordinate residual at \(p=101\) was below \(1.5\cdot10^{-15}\) using floating-point gap reconstruction. A discrete orthonormal sine-transform check verified (4) to numerical precision. Reflection-paired disjoint adjacent swaps at \(p=101\) and \(211\) also gave exactly \(6m\) defective stitches and the predicted weighted transport budget. These are implementation falsification checks; (2), (4), (7)--(10) are finite identities/inequalities, and the asymptotic claims use only the FD-002/FD-318 PNT input.

Farey adjacency, modular-inverse neighbor denominators, Hall--Shiu indices, the totient asymptotic, and orthogonality of the discrete sine transform are classical. The existing line SOURCES.md anchors Hall--Shiu/BCZ, Franel--Landau, García's 2026 same-gap permutation work, and the arithmetic inputs used in FD-002/FD-318. Generic block-permutation transport algebra is elementary; the present mathematical delta is the **uniform all-permutation/full-spectrum classification** on this exact labeled-edge control class, plus the two-sided separation between index-break count and spectral cost. No claim of broad novelty for transport identities or permutation statistics is made.

These are deliberately **labeled-edge matched controls**: after a nonintegral interface, a copied denominator label need not be the reduced denominator of the reconstructed rational point. The theorem does not contradict FD-315's exact-stitching rigidity, does not prove spectral coercivity for genuine Farey sequences, and does not improve the Franel--Landau estimate or RH. It identifies precisely which coarse information an excursion-permutation null must retain to avoid falsely attributing spectral shape to a low density of invalid stitches.
