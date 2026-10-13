# FD-326 — Identical Farey index defects allow unbounded transport-energy ratios

**Status:** EXACT-DERIVED + PNT-AND-DIRICHLET-ASSISTED-ASYMPTOTIC + NEGATIVE/CONTROL-DESIGN + SHARP-LIMIT-SEPARATION.

FD-325 established that ordered, scaled Hall--Shiu index defects do not uniquely determine the Franel energy of prime-order Farey excursion reassemblies, exhibiting a sixfold disparity for fixed inverse labels. The failure is not merely a bounded ambiguity: one and the same three-defect coefficient vector can be realized by two families whose limiting energies have a ratio growing quadratically in the inverse parameter. Along suitable paired diagonals, one family loses *all* transport energy and its complete sine spectrum, while the other approaches the full natural \(\frac{3}{\pi^2}\) transport scale.

## 1. Unbounded fixed-inverse-fiber separation

For each fixed integer \(a\ge3\), put \(b=a+1\) and use the three-stitch block swap \(ABR\mapsto BAR\) of FD-325 with the following rational anchors:

\[
\begin{array}{c|c|c|c}
 & \alpha=r/a & \beta=s/b & \text{prime progressions}\\ \hline
 H & 1/a & a/(a+1) & p\equiv-1\pmod a,\ p\equiv1\pmod{a+1}\\
 L & (a-1)/a & a/(a+1) & p\equiv1\pmod a,\ p\equiv1\pmod{a+1}.
\end{array} \tag{1}
\]

Both progressions are reduced residue classes modulo \(a(a+1)\), and Dirichlet's theorem supplies infinitely many primes in each. For sufficiently large primes in their respective progressions, the integer cut positions

\[
k=\frac{rp+1}{a},\qquad c=\frac{ap+1}{a+1} \tag{2}
\]

satisfy \(1<k<c\le p-2\). Keep the two original exterior edges and all original directed denominator-edge words, changing only the order of the intact inner Farey excursions.

Every directed labeled-edge multiplicity, positive gap, both endpoints, and both exterior edges remain unchanged. **Both** families have exactly the same ordered profile of three nonintegral indices, at their respective primes:

\[
(\nu_1,\nu_2,\nu_3)=
\left(1-\frac{a-1}{p},\;1+\frac a p,\;1-\frac1p\right),
\qquad
p(\nu_i-1)_{i=1}^{3}=(1-a,\ a,\ -1). \tag{3}
\]

In particular, for every *fixed* \(a\), their defect coefficients are identical and the total distance to the nearest integer is \(2a/p\to0\). These are two distinct prime subsequences, not two reassemblies at the same prime \(p\).

Let \(E_p=\sum_{i=1}^{N_p-1}(x_i-i/N_p)^2\) be genuine Farey energy and \(E_p^H,E_p^L\) the corresponding reassembled energies, with \(N_p=\sum_{q\le p}\varphi(q)\). Their unconditional limiting energy differences, with \(a\) fixed before \(p\to\infty\), are

\[
\boxed{
C_H(a)=\frac3{\pi^2}\,
\frac{a^3-2a^2-a+3}{a(a+1)^2},\qquad
C_L(a)=\frac3{\pi^2}\,
\frac{a-1}{a(a+1)^2}.} \tag{4}
\]

Consequently

\[
\boxed{\frac{C_H(a)}{C_L(a)}
=a^2-a-2+\frac1{a-1}\ \longrightarrow\infty,} \tag{5}
\]

and more sharply,

\[
\boxed{C_H(a)\longrightarrow \frac3{\pi^2},
\qquad C_L(a)\longrightarrow0,
\qquad C_H(a)-C_L(a)\longrightarrow\frac3{\pi^2}.} \tag{6}
\]

Thus no positive **universal multiplicative comparison** for transport energy can depend solely on the ordered scaled defect values and apply to all members of these three-break fixed-inverse fibers. Equation (6) is a limiting separation across the varying vectors \((1-a,a,-1)\), not a claim of two different energies with one fixed finite vector across all \(a\).

## 2. Exact algebra and asymptotic proof

For the FD-325 construction, with \(L_A,L_B\) the gap counts in the swapped blocks, put

\[
w_A=\frac{L_A}{N_p}-\frac{k-1}{p},
\qquad
w_B=\frac{L_B}{N_p}-\frac{c-k}{p}.
\]

The transport vector \(v\) equals \(w_A\) on the moved \(B\)-coordinates and \(-w_B\) on the moved \(A\)-coordinates. Thus the finite identities are

\[
T_p=\|v\|_2^2=L_Bw_A^2+L_Aw_B^2,\qquad
E_p^{r,s}-E_p=T_p+2\langle PD,v\rangle. \tag{7}
\]

For fixed reduced rational anchors \(\alpha=r/a<\beta=s/b\), the exact Möbius rank identity

\[
\rho_p(\gamma)-\gamma N_p=
\sum_{d\le p}\mu(d)
\sum_{m\le\lfloor p/d\rfloor}
\left(\lfloor\gamma m\rfloor-\gamma m\right) \tag{8}
\]

gives \(\rho_p(\gamma)=\gamma N_p+o_\gamma(p)\) by the periodic fractional-part decomposition and \(M(t)=o(t)\) (PNT). As \(k/p,c/p\) are immediate right Farey neighbors of \(\alpha,\beta\), respectively,

\[
\frac{L_A}{N_p}=\alpha+o(p^{-1}),\quad
\frac{L_B}{N_p}=\beta-\alpha+o(p^{-1}),\quad
pw_A\to1-\frac1a,\quad
pw_B\to\frac1a-\frac1b. \tag{9}
\]

Equations (7)--(9) and \(N_p/p^2\to3/\pi^2\) give, for each *fixed* parameter tuple,

\[
T_p\longrightarrow\frac3{\pi^2}
\left[(\beta-\alpha)\left(1-\frac1a\right)^2+
\alpha\left(\frac1a-\frac1b\right)^2\right]. \tag{10}
\]

The unconditional true Farey \(E_p=\|D\|_2^2=o(1)\) follows from the exact Franel--Mertens identity and PNT (FD-002, FD-318). Since \(T_p\) remains bounded at fixed \(a\), the mixed term in (7) is \(o(1)\). This proves that the limit of each energy difference equals (10), without RH.

In family \(H\), substitute \(\alpha=1/a\) and \(\beta=a/(a+1)\); in family \(L\), substitute \(\alpha=(a-1)/a\) and the same \(\beta\). Direct simplification yields (4). Their ratio simplifies to (5), and their positive difference is explicitly

\[
C_H(a)-C_L(a)=\frac3{\pi^2}\,
\frac{(a-2)(a^2-2)}{a(a+1)^2}>0. \tag{11}
\]

For every fixed \(a\), the appropriate prime progressions are infinite and the proof uses only fixed-rational estimates. To obtain a **single pair of diagonal sequences**, first choose \(a_n\to\infty\), then choose primes \(p_n^H,p_n^L\) in the respective progressions so large that each finite energy difference is within \(o(a_n^{-2})\) of (4), that \(2a_n/p_n^{H,L}\to0\), and that any prescribed first \(n\) sine coefficients approximate their fixed-\(a_n\) limits. Fixed-\(a\) convergence and Dirichlet permit this choice. Along these paired diagonals the energies approach respectively \(3/\pi^2\) and zero; the ratio of their positive energy differences diverges like \(a_n^2\). **No uniform-in-growing-\(a\) PNT bound is invoked.**

## 3. Complete sine-spectrum separation

FD-325's normalized rank transport profile is

\[
g_{\alpha,\beta}(t)=
\begin{cases}
1-1/a,&0<t<\beta-\alpha,\\
1/(a+1)-1/a,&\beta-\alpha<t<\beta,\\
0,&\beta<t<1.
\end{cases} \tag{12}
\]

For fixed \(a\), the sine transform of \(D^{r,s}-v\) has \(\ell^2\)-norm \(\sqrt{E_p}=o(1)\), and the normalized-rank step representation of \(pv\) converges to (12) in \(L^2\). Sending \(a\to\infty\) *after* the fixed-\(a\) limit,

\[
g_H\longrightarrow1,\qquad g_L\longrightarrow0
\quad\text{in }L^2(0,1). \tag{13}
\]

The first interval of \(g_H\) expands to full measure and its height tends to one; the positive-height first interval of \(g_L\) shrinks to length \(1/[a(a+1)]\), while the remaining height is only \(1/[a(a+1)]\) in absolute value. Hence the normalized Dirichlet sine coefficients on the paired diagonals satisfy, for every fixed \(m\ge1\),

\[
\boxed{
\widehat D_m^{\,H}\longrightarrow
\frac{\sqrt6}{\pi^2m}\bigl(1-(-1)^m\bigr),
\qquad
\widehat D_m^{\,L}\longrightarrow0.} \tag{14}
\]

Sine Parseval and (6), together with the fixed-mode limits in (14), show that **all** \(3/\pi^2\) limiting energy of \(H\) sits in the displayed fixed-mode spectrum, whereas the *entire* spectral energy of \(L\) tends to zero. This is full spectral separation, not merely different scalar sums.

## 4. Independent finite falsification checks

An exact-rational verifier enumerated the genuine Farey order-\(p\) fractions, copied and swapped complete directed denominator-edge/gap words, reconstructed every rational point, and checked that the directed edge multiset, the complete Hall--Shiu index list, and identity (7) hold. Two paired checks are:

- \(a=3\), \(H\) at \(p=17\): \((L_A,L_B)=(32,40)\), \(T_p=18/289\), \(E_p^H-E_p=3523261/59510880\). The \(L\) family at \(p=13\): \((L_A,L_B)=(39,5)\), \(T_p=2789/142129\), \(E_p^L-E_p=401353/45285240\). Both have scaled ordered defects \((-2,3,-1)\).
- \(a=5\), \(H\) at \(p=19\): \((L_A,L_B)=(23,78)\), \(T_p=83839/866400\); \(L\) at \(p=31\): \((L_A,L_B)=(247,11)\), \(T_p=47339/4143832\). Both have scaled ordered defects \((-4,5,-1)\).

Additional exact checks with \(a=3,5,8\) and larger primes (including \(p=41,61,109,151,271,73\) on the respective sides) checked all noninteger indices and the finite energy identity. These samples are independent falsification controls; they are not used to infer (4)--(6).

## 5. Prior art, interpretation, and limits

The Hall--Shiu index, Farey adjacency, the Möbius rank formula, the totient asymptotic, PNT and Dirichlet's theorem are classical. Hall--Shiu, *The index of a Farey sequence*, Michigan Math. J. **51** (2003), 209--223, anchors the local index. García, *New Analytical Formulas for the Rank of Farey Fractions and Estimates of the Local Discrepancy*, Mathematics **13** (2025), 140, studies Farey rank; García, *A General Lower Bound for Average Local Discrepancy and an Application to the Farey Sequence*, Mathematics **14** (2026), 2543, considers gap permutations for a different mean-absolute statistic. The line's SOURCES.md already anchors these works. A targeted comparison exposed no identical unbounded fixed-index-fiber separation, but this is not an exhaustive priority or novelty assertion.

FD-320 supplies the all-permutation transport law and FD-325 the fixed-inverse two-cut theorem. The new delta is the **unbounded relative ambiguity, maximal absolute high/low separation, and full-spectrum survival/extinction** within matched ordered scaled index profiles, by choosing two distinct numerator branches for each pair \((a,a+1)\). These are *labeled-edge matched controls*, not genuine second Farey sequences; at defective joins the copied denominator labels need not equal actual reduced denominators of the reconstructed points. The constructions do not preserve defect **rank positions**, do not live at the same prime, and do not dispute exact Farey index rigidity (FD-315). The supremum \(3/\pi^2\) is only an approach within this explicit family, not a universal energy ceiling. There is no improvement to the genuine Franel--Landau discrepancy estimate or implication toward RH. Any attempted coercive index-based geometry must retain the rational cut locations or directly control cumulative excursion transport; the three ordered defect coefficients alone cannot even distinguish vanishing from near-maximal full spectral transport across these fibers.
