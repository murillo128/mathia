# FD-321 — Three vanishing Farey-index defects are sharp without reflection

**Status:** EXACT-DERIVED + PNT-ASSISTED-ASYMPTOTIC + NEGATIVE/CONTROL-DESIGN + SHARP-THREE-BREAK-EXCURSION-FAMILY.

FD-315 gives exact index-stitching rigidity. FD-319 supplies a reflection-symmetric prime-order excursion permutation with four noninteger indices tending to positive integers and nonvanishing Franel energy. Without reflection, **three** noninteger indices already suffice to produce nonvanishing energy, and three is the minimum for a nonidentity permutation of complete prime-order excursions with the original endpoint sentinels. Here one defective index tends to **zero**, not to an admissible positive integer, so this result does not replace FD-319 under its stronger positive-index and reflection conditions.

For every odd prime \(p\ge7\), construct an increasing grid \(F_p^\star\) with the same positive gap multiset, complete directed denominator-edge multiset, and outer boundary edges as the genuine \(F_p\). Exactly three stitched Hall--Shiu indices are nonintegral, in order:
\[
\boxed{\nu_1=\frac3p,\qquad \nu_2=1+\frac1p,\qquad
\nu_3=2-\frac4p.} \tag{1}
\]
All other indices are genuine integers. For \(p\ge11\), their total distance to the *nearest integers* is \(8/p\), and their maximum such distance is \(4/p\). But the first index approaches the nonpositive value \(0\), not a positive integral Farey index.

Let \(N=N_p=\sum_{q\le p}\varphi(q)\), let \(D_k=x_k-k/N\) for the genuine Farey points, and put \(E_p=\sum_{k=1}^{N-1}D_k^2\), with the analogous \(D_k^\star,E_p^\star\) for the reassembled grid. Then
\[
\boxed{E_p^\star-E_p\longrightarrow \frac{3}{2\pi^2}>0.} \tag{2}
\]
For the normalized Dirichlet sine coefficients
\[
d_j^\star(p)=\sqrt{\frac2N}\sum_{k=1}^{N-1}
D_k^\star\sin\frac{\pi jk}{N},
\]
every fixed \(j\ge1\) satisfies
\[
\boxed{d_j^\star(p)\longrightarrow
\frac{\sqrt6}{\pi^2j}\left(1-\cos\frac{\pi j}{2}\right).} \tag{3}
\]
The squares of these fixed-mode limits sum to the entire constant in (2); there is no positive limiting residual in growing sine modes.

## 1. Move only the sparse central excursion

Write \(p=2a+1\) and let \(E_j\), \(1\le j\le p-2\), denote the complete denominator-\(p\)-to-\(p\) Farey excursion from \(j/p\) to \((j+1)/p\), as in FD-316 and FD-320. Every excursion has geometric width \(1/p\). Define
\[
 A=E_1\cdots E_{a-1},\quad C=E_a,\quad
 B=E_{a+1}\cdots E_{p-2}.
\]
The central excursion contains exactly the Farey neighbors \(a/p<1/2<(a+1)/p\) and has denominator word \(C=(p,2,p)\), hence two gaps. Reflection implies that \(A,B\) have equal gap counts
\[
K=\frac N2-2, \tag{4}
\]
and both have width \((a-1)/p\).

Replace the genuine excursion order \(ACB\) by
\[
\boxed{CAB} \tag{5}
\]
while retaining the leading edge \(1\to p\) and trailing edge \(p\to1\). At each directed edge \((q,q')\) retain its original positive gap \(1/(qq')\) and reconstruct the grid by cumulative addition starting at zero. Because all excursions begin and end at label \(p\), the *entire* directed-edge and gap multisets survive. Their total width is unchanged, so the endpoint remains exactly \(1\). This is a matched labeled-edge grid, not a second genuine Farey sequence: a denominator label at an invalid join need not equal the reduced denominator of its reconstructed rational position.

## 2. Exactly three invalid stitches, and minimality

The only changed triples occur (i) between the unchanged first edge and \(C\), (ii) between \(C\) and \(A\), and (iii) between \(A\) and \(B\). Their denominator triples are respectively
\[
(1,p,2),\qquad (2,p,p-1),\qquad (p-2,p,p-2).
\]
The last follows from the modular inverses \(a^{-1}\equiv-2\pmod p\) and \((a+1)^{-1}\equiv2\pmod p\); the initial successor of \(1/p\) has denominator \(p-1\). Taking \((q_{k-1}+q_{k+1})/q_k\) gives exactly (1). All other triples lie entirely inside unchanged excursions or at the unchanged last endpoint and retain their integer indices.

For completeness, FD-320 gives an independent combinatorial count. If \(\sigma\) permutes labels \(1,\ldots,n=p-2\), adjoin fixed sentinels \(\sigma(0)=0\), \(\sigma(n+1)=n+1=p-1\). A boundary between labels \(j,k\) is integral **if and only if** \(k=j+1\); thus the number of defective indices is precisely the number of broken consecutive-label adjacencies in this augmented word. A nonidentity word with fixed sentinels cannot have only one or two breaks: cutting at at most two places leaves at most one interior consecutive increasing run between the initial run starting at \(0\) and the final run ending at \(n+1\); the unused labels themselves form the unique consecutive middle interval, forcing the natural order. Consequently every nonidentity full-excursion permutation has at least three defective stitches. The permutation (5) achieves three. This sharpness is **only** within the full-excursion permutation class; it is not a lower bound for arbitrary reassembled labeled paths.

The word \(CAB\) is not reflection symmetric. Reflection and distance to **positive** integral indices matter: the four-defect example FD-319 keeps those stronger constraints, whereas (1) approaches the forbidden index value zero at its first stitch.

## 3. Exact displacement and unconditional energy limit

FD-320 transports the original discrepancy coordinates with their excursions. Under \(ACB\mapsto CAB\), the old \(C\) points occupy the first two interior excursion slots, the \(K\) old \(A\) points shift two ranks to the right, and \(B\) retains its original slots. For the exact cumulative-length mismatch \(w_j=\ell_j/N-1/p\), the central block has \(w_C=2/N-1/p\), and
\[
w_A=\frac KN-\frac{a-1}{p}=\frac{3}{2p}-\frac2N.
\]
Therefore \(D^\star=PD+v\) for a permutation \(P\), with **exact** block-constant displacement
\[
v_k=\begin{cases}
\frac{3}{2p}-\frac2N,&k=2,3,\\[2pt]
\frac1p-\frac2N,&4\le k\le N/2+1,\\[2pt]
0,&k=1\text{ or }N/2+2\le k<N.
\end{cases} \tag{6}
\]
In particular, the finite transport energy is
\[
T_p=\|v\|_2^2=
2\left(\frac{3}{2p}-\frac2N\right)^2+
\left(\frac N2-2\right)\left(\frac1p-\frac2N\right)^2. \tag{7}
\]

The exact FD-002 discrepancy identity and the prime-number theorem imply \(E_p=\|D\|_2^2=o(1)\), as reconstructed in FD-318 and used in FD-319--FD-320. Explicitly, the normalized fixed Fourier/divisor modes tend to zero by PNT and admit a square-summable divisor-function majorant, so dominated convergence applies; no RH hypothesis is used here. Hence
\[
E_p^\star-E_p=T_p+2\langle PD,v\rangle,\qquad
|\langle PD,v\rangle|\le\sqrt{E_pT_p}=o(1).
\]
Since \(N/p^2\to3/\pi^2\), (7) tends to \(3/(2\pi^2)\), proving (2). The quantitative finite bound \(|\sqrt{E_p^\star}-\sqrt{T_p}|\le\sqrt{E_p}\) is also an immediate specialization of FD-320. All constants and ranks in (6)--(7) are exact.

## 4. Every fixed sine mode and exhaustion of the energy

FD-320 gives the exact full-spectrum remainder
\[
\sum_{j=1}^{N-1}|\widehat{D^\star}_j-\widehat v_j|^2=E_p=o(1).
\]
The two exceptional points \(k=2,3\) in (6) contribute \(o(1)\) to each fixed sine coefficient. The \(K\)-point positive displacement contributes
\[
\widehat v_j=
\sqrt{\frac2N}\left(\frac1p-\frac2N\right)
\sum_{k=4}^{N/2+1}\sin\frac{\pi jk}{N}+o(1).
\]
For fixed \(j\), the normalized sum is a Riemann sum for
\[
\int_0^{1/2}\sin(\pi jt)\,dt=
\frac{1-\cos(\pi j/2)}{\pi j},
\]
while \(\sqrt{2N}/p\to\sqrt6/\pi\). This proves (3) for **all** fixed integer modes, with no odd-mode cancellation because reflection was dropped. Indeed,
\[
\sum_{j\ge1}\frac{(1-\cos(\pi j/2))^2}{j^2}
=\sum_{j\ \mathrm{odd}}\frac1{j^2}
+\sum_{j\equiv2\pmod4}\frac4{j^2}
=\frac{\pi^2}4.
\]
Multiplying by \(6/\pi^4\) gives exactly \(3/(2\pi^2)\). The fixed-mode limits therefore carry the whole limiting energy: no positive mass is hidden only at diverging frequencies.

## 5. Falsification checks, prior art, and scope

Independent direct enumeration of genuine Farey gaps, followed by (5), was checked for \(p=7,11,29,101,211,809\). It reproduced the three indices (1), both endpoint denominator pairs, exact total gap \(1\), and the predicted finite transport (7). At \(p=7\), exact rational arithmetic gives
\[
E_7=\frac{197}{7560},\quad
E_7^\star=\frac{691}{10584},\quad
E_7^\star-E_7=\frac{173}{4410},\quad T_7=\frac{25}{882}.
\]
At \(p=809\), the numerical difference \(E_{809}^\star-E_{809}\simeq0.1507629586\) is approaching \(3/(2\pi^2)\simeq0.1519817755\). These checks are independent falsification controls; the asymptotic follows from the exact displacement and the previously established PNT input, not numerical fitting.

Farey adjacency and modular inverse neighbor formulas, the Hall--Shiu index and BCZ recurrence, totient asymptotics, and the classical Franel--Landau criterion are already anchored in this line's SOURCES.md and FD-002/FD-315--FD-320. For nearby reordering prior art, Rogelio Tomás García, *A General Lower Bound for Average Local Discrepancy and an Application to the Farey Sequence*, Mathematics **14** (2026), 2543, DOI 10.3390/math14142543, treats gap-permutation effects on a different discrepancy statistic; Boca--Gologan--Zaharescu, *On the index of Farey sequences*, QJM **53** (2002), 377--391, DOI 10.1093/qjmath/53.4.377, treats the classical Farey-index distribution. Neither is claimed to supply a three-break directed-edge-preserving counterexample. The new claim here is the explicit **sharp three-break** matched control and its exact macroscopic spectral displacement, not a new Farey recurrence, transport algebra, or prime-number theorem.

This construction imposes weaker constraints than FD-319. In particular, \(\nu_1\to0\), so it **does not** show that three defects approaching *positive* Farey indices can give a macroscopic error, and it does not show optimality outside the stated permutation family. No improved estimate for the genuine Farey discrepancy, Franel--Landau critical scale, or RH follows. It closes the minimal *unreflected* break-count question and reinforces the FD-320 boundary: spectral control requires cumulative length transport, not merely few or small fractional index defects.
