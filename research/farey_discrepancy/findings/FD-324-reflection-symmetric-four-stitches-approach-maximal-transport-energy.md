# FD-324 — Reflection-symmetric four-stitch Farey controls approach maximal transport energy

**Status:** EXACT-DERIVED + PNT-AND-DIRICHLET-ASSISTED-ASYMPTOTIC + NEGATIVE/CONTROL-DESIGN + SHARP-WITHIN-EXPLICIT-FAMILY.

FD-319 proves that four Hall--Shiu index defects of size \(1/p\) suffice for nonvanishing Franel quadratic energy even when a matched prime-order Farey denominator-edge reconstruction preserves reflection. FD-323 independently varies fixed modular inverses to approach \(3/\pi^2\) using *three* defects without reflection. Reflection does not lower this explicit near-one-defect transport ceiling: a symmetric four-defect family also approaches \(3/\pi^2\), with vanishing total index error and nonzero **even** fixed sine modes.

## 1. Theorem and quantifiers

Fix any odd integer \(a\ge3\), and put
\[
r=(a-1)/2,\qquad \alpha=r/a=(a-1)/(2a).
\]
Along sufficiently large primes
\[
p\equiv-2\pmod a, \tag{1}
\]
define \(k=(rp-1)/a\), so \(2\le k<(p-1)/2\). The residue class is coprime to \(a\), hence contains infinitely many primes by Dirichlet's theorem. Let \(N=N_p=\sum_{q\le p}\varphi(q)\) and write \(E_j\), \(1\le j\le p-2\), for the genuine denominator-\(p\) excursions from \(j/p\) to \((j+1)/p\).

Split the genuine interior excursion word into
\[
 A=E_1\cdots E_{k-1},\quad
 C=E_k\cdots E_{p-k-1},\quad
 B=E_{p-k}\cdots E_{p-2},
\]
and replace \(ACB\) by **\(BCA\)**, retaining the two original exterior denominator edges. Reconstruct the rational grid by concatenating the original directed denominator edges with their positive gaps \(1/(qq')\).

The resulting increasing grid \(F_p^\dagger\) retains exactly the original directed denominator-edge multiset, positive gap multiset, outer edges, both endpoints, and the reflection relation \(x_{N-i}^\dagger=1-x_i^\dagger\). All but **four** interior Hall--Shiu indices remain genuine integers. The four noninteger indices, in order, are exactly
\[
 \boxed{
 1-\frac{a-1}{p},\
 1+\frac{a-1}{p},\
 1+\frac{a-1}{p},\
 1-\frac{a-1}{p}.} \tag{2}
\]
For fixed \(a\), every defective index approaches the admissible positive integer \(1\), and the sum of its distances to the nearest integer equals \(4(a-1)/p\to0\).

With the usual rank discrepancies \(D_i=x_i-i/N\), \(D_i^\dagger=x_i^\dagger-i/N\) and quadratic energies \(E_p=\sum_{i=1}^{N-1}D_i^2\), \(E_p^\dagger=\sum_{i=1}^{N-1}(D_i^\dagger)^2\), one has **unconditionally**
\[
 \boxed{\lim_{\substack{p\to\infty\\p\equiv-2\ (a)}}
 (E_p^\dagger-E_p)
 =C_a:=\frac3{\pi^2}\left(1-\frac1a\right)^3>0.} \tag{3}
\]
The constants increase toward the sharp **supremum of this explicit family**
\[
 \boxed{\sup_{a\ge3,\ a\ {\rm odd}} C_a=\frac3{\pi^2}
 =0.303963550927\ldots .} \tag{4}
\]
A diagonal sequence of \(a\to\infty\) and sufficiently large primes in their respective progressions has exactly four defects, their maximum and total fractional errors tend to zero, reflection remains exact, and \(E_p^\dagger-E_p\to3/\pi^2\). Equation (4) is *not* a universal ceiling for all reflection-symmetric four-defect reassemblies.

## 2. Four stitches and exact reflection

Farey reflection sends \(E_j\) to the reversed excursion \(E_{p-1-j}\). Thus \(B=\operatorname{reverse}(A)\) and \(C=\operatorname{reverse}(C)\), where reversal reverses the edge/denominator word. The new \(BCA\) word is reflected onto itself. Every excursion starts and ends at denominator \(p\); consequently reordering their intact edge words preserves the complete directed-edge inventory and all gaps, not merely a gap histogram. The two unchanged outer edges ensure that the reconstructed grid still begins at zero and ends at one.

FD-320's exact interface formula, with sentinel labels \(0,p-1\), is
\[
 \nu_{j,\ell}
 =1+\frac{[(j+1)^{-1}]_p-[\ell^{-1}]_p}{p}. \tag{5}
\]
Since \(ak=rp-1\), the least positive modular inverse of \(k\) is \(p-a\); that of \(p-k\) is \(a\). The only changed interfaces are
\[
 (0,p-k),\quad(p-2,k),\quad(p-k-1,1),\quad(k-1,p-1).
\]
Their inverse differences are \(1-a,\ a-1,\ a-1,\ 1-a\), giving (2). Every unchanged interface and every triple inside a copied excursion retains its genuine integral Farey index. For sufficiently large \(p\), the four values in (2) lie strictly between zero and two and are nonintegral; they approach \(1\), not \(0\) or \(2\). FD-319 already establishes that four is the minimum for nonidentity *reflection-symmetric full-excursion permutations*. Nothing here claims a minimum for arbitrary reconstructed denominator-label paths.

## 3. Exact finite transport and the rational-anchor limit

Let \(K\) be the number of gaps in \(A\); by reflection \(B\) has the same gap count \(K\). Let \(\rho_p(\alpha)\) denote the number of positive genuine Farey fractions of order \(p\) at most \(\alpha=r/a\). The identity
\[
 \alpha-\frac{k}{p}=\frac1{ap}
\]
has determinant one and denominator sum \(a+p>p\), so \(k/p\) is immediately to the *left* of \(\alpha\) in \(F_p\). The rank of \(k/p\) is \(1+K=\rho_p(\alpha)-1\), hence
\[
 \boxed{K=\rho_p(\alpha)-2.} \tag{6}
\]

Under \(ACB\mapsto BCA\), every interior discrepancy coordinate belonging to \(B\) moves to the left and acquires the same shift
\[
 s_p=\frac{k+1}{p}-\frac{K+2}{N}
     =\frac{k+1}{p}-\frac{\rho_p(\alpha)}N. \tag{7}
\]
The \(A\) coordinates acquire shift \(-s_p\); those in \(C\), and the first and last exterior coordinates, have shift zero. With \(P\) the exact permutation of original interior discrepancy coordinates,
\[
 D^\dagger=PD+v,\qquad
 v=\bigl(0,\underbrace{s_p,\ldots,s_p}_{K},
 \underbrace{0,\ldots,0}_{N-2-2K},
 \underbrace{-s_p,\ldots,-s_p}_{K}\bigr), \tag{8}
\]
so the **finite exact** transport potential is
\[
 T_p=\|v\|_2^2=2Ks_p^2,\qquad
 E_p^\dagger-E_p=T_p+2\langle PD,v\rangle. \tag{9}
\]

For fixed reduced rational \(\alpha=r/a\), the exact Möbius count is
\[
 \rho_p(\alpha)-\alpha N
 =\sum_{d\le p}\mu(d)\!
   \sum_{m\le\lfloor p/d\rfloor}
       (\lfloor\alpha m\rfloor-\alpha m). \tag{10}
\]
The inner sum is a linear term in \(\lfloor p/d\rfloor\) plus a bounded periodic remainder depending on the fixed \(a\). The linear term collapses to a constant by \(\sum_{d\le p}\mu(d)\lfloor p/d\rfloor=1\). Split the remaining sum at \(\epsilon p\): the small-divisor part is \(O_a(\epsilon p)\), while the large-divisor part has only finitely many quotient values and is \(o_a(p)\) by PNT, \(M(t)=o(t)\). Taking \(p\to\infty\) and then \(\epsilon\downarrow0\) proves
\[
 \rho_p(\alpha)=\alpha N+o_a(p). \tag{11}
\]
This is the fixed-rational rank estimate used in FD-322/FD-323; no uniformity with growing \(a\) is assumed.

Equations (6)--(7), \(k/p=\alpha-1/(ap)\), and (11) give
\[
 \frac{K}{N}\longrightarrow\alpha,\qquad
 p s_p\longrightarrow 1-\frac1a. \tag{12}
\]
Since \(N/p^2\to3/\pi^2\), the exact \(T_p\) in (9) tends to
\[
 \frac3{\pi^2}\,2\alpha\left(1-\frac1a\right)^2
 =\frac3{\pi^2}\left(1-\frac1a\right)^3=C_a. \tag{13}
\]
FD-002/FD-318 prove \(E_p=\|D\|_2^2=o(1)\) unconditionally from the exact Franel--Mertens identity and PNT. Here \(T_p=O_a(1)\), so the cross term in (9) is bounded by \(2\sqrt{E_pT_p}=o(1)\), proving (3).

## 4. Even sine spectrum and the sharp diagonal

For normalized Dirichlet sine coefficients
\[
 d_m^\dagger(p)=\sqrt{2/N}
 \sum_{i=1}^{N-1}D_i^\dagger\sin(\pi mi/N),
\]
reflection gives \(d_{2j-1}^\dagger(p)=0\) **exactly**, for all \(p\). The full-spectrum FD-320 transport identity makes the contribution of \(PD\) vanish in spectral \(\ell^2\) because \(E_p=o(1)\).

For fixed \(a\), the rank-coordinate limit of \(pv\) is the step profile
\[
 g_a(t)=
 \begin{cases}
 h_a,&0<t<\alpha,\\
 0,&\alpha<t<1-\alpha,\\
 -h_a,&1-\alpha<t<1,
 \end{cases}
 \qquad h_a=1-1/a. \tag{14}
\]
Riemann sums and \(\sqrt{2N}/p\to\sqrt6/\pi\) give, for every fixed \(j\ge1\),
\[
 \boxed{\lim_{\substack{p\to\infty\\p\equiv-2\ (a)}}
 d_{2j}^\dagger(p)=
 \frac{\sqrt6\,h_a}{\pi^2j}
    \bigl(1-\cos(2\pi j\alpha)\bigr)
 =
 \frac{\sqrt6\,h_a}{\pi^2j}
    \bigl(1-(-1)^j\cos(\pi j/a)\bigr).} \tag{15}
\]
Sine Parseval for \(g_a\) shows that the squares of these fixed even-mode limits sum to
\[
 \frac3{\pi^2}\int_0^1g_a(t)^2\,dt
 =\frac3{\pi^2}\,2\alpha h_a^2=C_a. \tag{16}
\]
Thus *all* limiting energy is carried by fixed even modes; no positive residual is forced into growing frequencies.

As \(a\) tends through odd integers to infinity, \(\alpha\to1/2\) and \(h_a\to1\), so (13) approaches \(3/\pi^2\) from below. For a rigorous single diagonal choose each \(p_a\equiv-2\pmod a\) large enough that the fixed-\(a\) energy asymptotic, the first \(a\) mode limits, and \(4(a-1)/p_a\) are all accurate within \(1/a\); Dirichlet's theorem and the fixed-\(a\) convergence allow this selection. Along that diagonal,
\[
 d_{2j}^\dagger\longrightarrow
 \frac{\sqrt6}{\pi^2j}\bigl(1-(-1)^j\bigr),
 \qquad d_{2j-1}^\dagger=0,\qquad
 E_p^\dagger-E_p\longrightarrow\frac3{\pi^2}. \tag{17}
\]
Their squares sum to \(3/\pi^2\) using \(\sum_{j\ {\rm odd}}j^{-2}=\pi^2/8\). This establishes the sharp supremum **within this family** without invoking a growing-denominator version of the rational-anchor PNT estimate.

## 5. Independent finite checks, prior art, and boundaries

An independent exact-rational Farey enumerator cut the denominator word at all denominator-\(p\) vertices, performed \(ACB\mapsto BCA\), rebuilt every point from the permuted gaps, compared complete directed-edge multisets, reflection, all Hall--Shiu indices, and the pointwise identity (8). For \((a,p)=(3,7)\) it found \((N,k,K)=(18,2,4)\), four defects \((5/7,9/7,9/7,5/7)\), \(s_p=2/21\), \(T_p=32/441\), and the exact energy difference \(22/2205\). For \((a,p)=(5,23)\), \((N,k,K)=(172,9,67)\), the defects are \((19/23,27/23,27/23,19/23)\), \(s_p=133/3956\), \(T_p=1185163/7824968\), and \(E_p^\dagger-E_p=3935538979/39814529040\). Other exact checks at \((a,p)=(7,19)\) and \((9,43)\) agree with (2), (8), and (9). In a floating-point independent test for \(a=5\), \(p=223\) and \(1013\), energy differences were approximately \(0.14589661\) and \(0.14877258\), against \(C_5\approx0.15562934\); odd modes vanished and even fixed modes approached (15). These finite checks try to falsify the exact construction, **not** to establish its asymptotics.

The Farey-neighbor and modular-inverse criteria, Farey reflection, Hall--Shiu index, Möbius inversion, the totient asymptotic, PNT and Dirichlet's theorem are classical. FD-319 and FD-320 supply the exact local-stitch and transport baselines; FD-323 supplied the fixed-inverse insight without reflection. The line's SOURCES.md already anchors Hall--Shiu, Boca--Gologan--Zaharescu, the Franel--Landau criterion, and García (2026) on permutations of Farey gaps for a different discrepancy quantity. A targeted check of those sources did not locate this **reflection-preserving fixed-inverse four-defect cubic profile**, but this is not an exhaustive novelty or priority claim.

This is a **matched labeled-edge reconstruction, not another genuine Farey sequence**. At a defective join, the copied denominator label need not equal the reduced denominator of its reconstructed rational point; exact Farey-index rigidity (FD-315) remains intact. The ceiling \(3/\pi^2\) applies only to the displayed family, not to arbitrary four-defect permutations or all admissible path controls. The result supplies no improved estimate of the genuine \(E_p\), no Franel--Landau power saving, and no RH implication. Its mathematical consequence is a sharper falsification boundary: even preserving reflection, *all* directed denominator edges, both exterior edges, and positive-near-integer indices except for the minimum four defects does not constrain the full discrepancy energy below the natural \(N/p^2\) transport scale. A coercive intermediate Farey observable must control cumulative excursion transport or retain stronger source-realizability information.