# FD-327 — Same-prime three-defect Farey profiles have unbounded energy ratios

**Status:** EXACT-DERIVED + PNT-AND-DIRICHLET-ASSISTED-ASYMPTOTIC + NEGATIVE/CONTROL-DESIGN + SAME-PRIME-FULL-SPECTRUM-SEPARATION.

FD-325 and FD-326 show that a fixed ordered vector of scaled nonintegral Hall--Shiu indices can accompany different, even arbitrarily separated, Franel transport energies. Those comparisons used different prime subsequences. Here **both controls are obtained from the same order-\(p\) Farey sequence at each \(p\)**, preserving the same complete directed denominator-edge inventory and the same ordered three defective index values. Their limiting energy ratio is nevertheless unbounded. The defect *rank positions* are not fixed.

## 1. Same-prime theorem

For any fixed integer \(t\ge2\), put \(m_0=3\), \(m_1=t+3\) and
\[
 L_t=\operatorname{lcm}(3,5,7,t+3,t+5,t+7).
 \tag{1}
\]
Choose primes \(p\equiv1\pmod{L_t}\), which exist arbitrarily far out by Dirichlet's theorem. For each \(m\in\{m_0,m_1\}\), define three excursion cut labels
\[
 h_j=\frac{(j-1)p+1}{j}\quad(j=m,m+2,m+4),\qquad
 i=h_m,\quad k=h_{m+2},\quad c=h_{m+4}.
 \tag{2}
\]
For sufficiently large \(p\), \(1<i<k<c\le p-2\). In the genuine prime-order Farey excursion word \(E_1\cdots E_{p-2}\) of FD-320, partition
\[
 P=E_1\cdots E_{i-1},\quad
 A=E_i\cdots E_{k-1},\quad
 B=E_k\cdots E_{c-1},\quad
 R=E_c\cdots E_{p-2}
\]
and replace \(PABR\) by \(PBAR\), leaving the first and last denominator edges unchanged. Each excursion is copied whole, retaining its **directed** denominator-edge labels and positive gaps \(1/(uv)\). Denote the reassembled Franel rank-grid energy by \(E_p^{(m)}\), and the genuine Farey energy by \(E_p\).

Both controls, **for the same prime \(p\)**, have exactly three nonintegral Hall--Shiu indices. In increasing rank order their values are
\[
 \boxed{(\nu_1,\nu_2,\nu_3)=
 \left(1-\frac2p,\ 1+\frac4p,\ 1-\frac2p\right),\qquad
 p(\nu_i-1)_{i=1}^3=(-2,4,-2).} \tag{3}
\]
In particular, their full directed edge multisets, gap multisets, endpoint edges, number of defects, ordered defective-index values, and total nonintegral index distance \(8/p\) all agree.

For each *fixed* \(m\), as \(p\to\infty\) over primes satisfying (1),
\[
 \boxed{E_p^{(m)}-E_p\longrightarrow
 C_m:=\frac{48}{\pi^2[m(m+2)(m+4)]^2}>0.} \tag{4}
\]
Consequently the **same-prime limiting separation** for the two reassemblies is
\[
 \boxed{\frac{C_{m_0}}{C_{m_1}}=
 \left(\frac{(t+3)(t+5)(t+7)}{105}\right)^2
 \xrightarrow[t\to\infty]{}\infty.} \tag{5}
\]
Moreover, a diagonal sequence \(t_n\to\infty\) and primes \(p_n\equiv1\pmod{L_{t_n}}\), selected sufficiently large for each fixed \(t_n\), satisfies
\[
 E_{p_n}^{(3)}\longrightarrow C_3>0,\qquad
 E_{p_n}^{(t_n+3)}\longrightarrow0.
 \tag{6}
\]
This is an actual pair of distinct controls of **one and the same \(F_{p_n}\)** at every stage, not a comparison of different primes. The ratio of their nonnegative energies therefore diverges along this diagonal whenever the denominator is nonzero; equivalently, the fixed-\(t\) limiting transport-energy ratios are exactly (5).

## 2. Exact three-stitch calculation

For \(p\equiv1\pmod{L_t}\), each integer \(h_j\) in (2) obeys \(jh_j\equiv1\pmod p\), so \([h_j^{-1}]_p=j\). At a junction between \(E_{u-1}\) and \(E_v\), FD-320's exact index formula is
\[
 \nu_{u-1,v}=1+\frac{[u^{-1}]_p-[v^{-1}]_p}{p}. \tag{7}
\]
The only changed junctions in \(PABR\mapsto PBAR\) are \(P|B\), \(B|A\), and \(A|R\). Their inverse-label differences are respectively
\[
 m-(m+2)=-2,\quad (m+4)-m=4,\quad
 (m+2)-(m+4)=-2,
\]
proving (3), with no additional defective interior joins. The prefix and suffix are nonempty for sufficiently large primes, so all three defects are interior. Entire directed-edge words are permuted but never modified, proving the edge/gap claims.

Let \(N_p=\sum_{q\le p}\varphi(q)\), let \(\rho_p(\gamma)\) count positive order-\(p\) Farey fractions at most \(\gamma\), and define
\[
 \alpha_j=\frac{j-1}{j}=1-\frac1j,\qquad
 d_m=\alpha_{m+2}-\alpha_m=\frac2{m(m+2)},\qquad
 e_m=\alpha_{m+4}-\alpha_{m+2}=\frac2{(m+2)(m+4)}.
 \tag{8}
\]
Since \(mh_m-(m-1)p=1\) and \(m+p>p\), the rational \(\alpha_m\) and \(h_m/p\) are consecutive Farey fractions; the same holds for \(m+2,m+4\). Hence the gap counts of the swapped words are **exactly**
\[
 L_A=\rho_p(\alpha_{m+2})-\rho_p(\alpha_m),\qquad
 L_B=\rho_p(\alpha_{m+4})-\rho_p(\alpha_{m+2}). \tag{9}
\]
The fixed-rational Farey-rank estimate from FD-323/FD-325,
\[
 \rho_p(\gamma)=\gamma N_p+o_\gamma(p), \tag{10}
\]
follows from the exact Möbius rank identity, periodic fractional-part sums, and \(M(x)=o(x)\) (the prime number theorem). Applying it to the three *fixed* rational anchors gives
\[
 L_A/N_p=d_m+o_m(p^{-1}),\qquad
 L_B/N_p=e_m+o_m(p^{-1}). \tag{11}
\]
The two excursion-block width/count mismatches are
\[
 w_A=\frac{L_A}{N_p}-\frac{k-i}{p},\qquad
 w_B=\frac{L_B}{N_p}-\frac{c-k}{p}. \tag{12}
\]
Using \(h_j/p=\alpha_j+1/(jp)\) in (2) and (11) yields
\[
 pw_A\longrightarrow d_m,\qquad pw_B\longrightarrow e_m. \tag{13}
\]

The exact FD-320 discrepancy permutation decomposition \(D^{(m)}=P_mD+v^{(m)}\) assigns shift \(+w_A\) to the \(L_B\) ranks in the moved \(B\) word and shift \(-w_B\) to the \(L_A\) ranks in \(A\), with zero shift elsewhere. Thus, with no approximation,
\[
 T_p^{(m)}=\|v^{(m)}\|_2^2=L_Bw_A^2+L_Aw_B^2,\quad
 E_p^{(m)}-E_p=T_p^{(m)}+2\langle P_mD,v^{(m)}\rangle.
 \tag{14}
\]
Combining (11)--(13) with \(N_p/p^2\to3/\pi^2\) gives
\[
 T_p^{(m)}\longrightarrow\frac3{\pi^2}
 \big(e_md_m^2+d_me_m^2\big)
 =\frac3{\pi^2}\frac{16}{[m(m+2)(m+4)]^2}=C_m.
 \tag{15}
\]
The genuine Farey energy \(E_p=\|D\|_2^2=o(1)\) unconditionally by the PNT-based Franel--Mertens argument of FD-318. Since \(T_p^{(m)}=O_m(1)\), the cross term in (14) is bounded by \(2\sqrt{E_pT_p^{(m)}}=o_m(1)\). This proves (4) and then (5). For (6), at each \(t_n\) choose an admissible prime so large that both fixed-\(m\) energy approximations are within \(o(C_{t_n+3})\) and the true Farey energy is small. **The limits are taken in the stated order; no PNT error estimate uniform in growing \(t\) is claimed.**

## 3. Full-spectrum consequence

FD-320 also gives the exact sine-Parseval error
\[
 \sum_{r=1}^{N_p-1}
 |\widehat{D^{(m)}}_r-\widehat{v^{(m)}}_r|^2=E_p=o(1).
 \tag{16}
\]
For fixed \(m\), \(pv^{(m)}\) has the normalized-rank \(L^2\) step limit
\[
 g_m(x)=
 \begin{cases}
 d_m,&\alpha_m<x<\alpha_m+e_m,\\
 -e_m,&\alpha_m+e_m<x<\alpha_{m+4},\\
 0,&\text{elsewhere on }(0,1).
 \end{cases} \tag{17}
\]
Its squared integral is \(e_md_m^2+d_me_m^2\). Thus \(m=3\) retains a nonzero full sine-spectrum norm while \(g_{t+3}\to0\) in \(L^2\) as \(t\to\infty\). The same-prime diagonal in (6) consequently separates the **entire spectral energy**, not only an isolated frequency.

## 4. Independent finite falsification and prior-art boundary

An independent exact-rational verifier enumerated the genuine Farey fractions, reconstructed the shuffled directed-edge/gap word, summed every new rational gap, checked the endpoint \(1\), the *complete* edge multiset and all Hall--Shiu indices, and verified at every interior rank that \(D^{(m)}=P_mD+v^{(m)}\). It also checked (14) exactly, independently summing both rank-grid energies.

At \(p=211\), \(N_p=13624\), the \(m=3\) cuts are \((141,169,181)\); the only nonintegral indices are \(209/211,215/211,209/211\), and \(T_p^{(3)}=1066763203/2065923278224\). More decisively, **both controls at the same prime \(p=631\)**, \(N_p=121318\), give:

| \(m\) | cuts \((i,k,c)\) | \((L_A,L_B)\) | exact \(T_p^{(m)}\) | \(E_p^{(m)}-E_p\) (decimal) |
| --- | --- | --- | --- | --- |
| 3 | \((421,505,541)\) | \((16177,6930)\) | \(1232732791899/2930078171274482\) | \(0.0003792766730\) |
| 5 | \((505,541,561)\) | \((6930,3855)\) | \(186673770135/2930078171274482\) | \(0.0000777950991\) |

For both rows, the **entire** nonintegral-index list is \((629/631,635/631,629/631)\); its ranks differ. The finite transport-energy ratio is about \(6.604\), rather than the limiting \(9\) at \(t=2\), consistent with (4) but not used as evidence for the limit.

Hall--Shiu's Farey index and Farey-neighbor determinant conditions are classical (Hall and Shiu, *The index of a Farey sequence*, Michigan Math. J. **51** (2003), DOI 10.1307/mmj/1049832901). García, *A General Lower Bound for Average Local Discrepancy and an Application to the Farey Sequence*, Mathematics **14** (2026), 2543, DOI 10.3390/math14142543, studies gap permutations for a different average-local statistic. FD-320 supplies the exact transport/spectrum theorem, FD-325 the fixed-inverse cut calculation, and FD-326 the comparison **across different primes**. The present delta is the explicit **same-prime** construction with identical ordered nonintegral index values and arbitrarily large ratios. A targeted comparison to those primary sources did not expose this exact same-prime statement, but no comprehensive priority claim is made.

These are matched **labeled-edge controls**, *not* alternate genuine Farey sequences: at nonintegral stitches, an inherited denominator label need not equal the actual reduced denominator of its reconstructed rational point. The controls preserve neither defect rank positions nor the complete ordered index array. The theorem does not contradict exact genuine-Farey stitching rigidity (FD-315), does not control genuine Farey energy beyond the already known \(E_p=o(1)\), and proves no improvement of the RH-equivalent Franel--Landau bound. Its obstruction is precise: an argument based only on the prime, the exact ordered three defective-index values, and the full directed-edge multiset cannot produce a uniform multiplicative estimate of transport energy without additional **cut-position or cumulative-length information**.
