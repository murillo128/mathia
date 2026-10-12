# FD-323 — Fixed-inverse three-defect Farey stitches approach maximal two-cut transport energy

**Status:** EXACT-DERIVED + PNT-AND-DIRICHLET-ASSISTED-ASYMPTOTIC + NEGATIVE/CONTROL-DESIGN + SHARP-WITHIN-EXPLICIT-FAMILY.

FD-322 shows that three near-one, nonintegral Farey indices can carry positive macroscopic quadratic discrepancy energy while preserving the full directed denominator-edge inventory. Its particular inverse pairs yield constants \(1/(6\pi^2)\) and \(1/(4\pi^2)\). Those values are not a ceiling even for the same three-break block-swap topology. Varying the *fixed modular inverses* at the two cuts produces a two-parameter family whose limiting transport energies have supremum \(3/\pi^2\), twelve times the larger FD-322 constant. Three defects approaching the positive integer \(1\), with vanishing total fractional error, can therefore carry almost the whole natural \(N_p/p^2\) transport scale.

## 1. Theorem and quantifiers

Fix **coprime integers** \(a,b\ge3\) with \(1/a+1/b<1\). Along primes satisfying

\[
p\equiv-1\pmod a,\qquad p\equiv1\pmod b, \tag{1}
\]

and sufficiently large in terms of \(a,b\), put

\[
k=\frac{p+1}{a},\qquad
c=\frac{(b-1)p+1}{b},\qquad 1<k<c\le p-2. \tag{2}
\]

The Chinese remainder theorem gives one reduced residue class modulo \(ab\); Dirichlet's theorem supplies infinitely many primes in it. All limiting statements below hold **with \(a,b\) fixed before \(p\to\infty\)**.

Write \(N=N_p=\sum_{q\le p}\varphi(q)\) and let \(E_j\), \(1\le j\le p-2\), be the complete denominator-\(p\) excursions of the true Farey sequence \(F_p\). Split the inner word into

\[
A=E_1\cdots E_{k-1},\quad
B=E_k\cdots E_{c-1},\quad
R=E_c\cdots E_{p-2},
\]

and replace \(ABR\) by \(BAR\), keeping the two original exterior edges. Reconstruct an increasing rational grid \(F_p^\star\) by assigning to each directed denominator edge \((q,q')\) its original gap \(1/(qq')\).

The reassembled grid preserves the **complete directed denominator-edge multiset**, positive gap multiset, exterior denominator edges, both endpoints, and total gap sum. Precisely three interior Hall--Shiu indices are nonintegral, appearing in this order:

\[
\boxed{\nu_1=1-\frac{a-1}{p},\qquad
\nu_2=1+\frac{b-1}{p},\qquad
\nu_3=1+\frac{a-b}{p}.} \tag{3}
\]

They all tend to the admissible positive integer \(1\), with total nearest-integer distance

\[
\sum_{\text{defects}}\operatorname{dist}(\nu_i,\mathbb Z)
=\frac{(a-1)+(b-1)+|a-b|}{p}
=\frac{2(\max\{a,b\}-1)}p\longrightarrow0. \tag{4}
\]

Define the usual rank-grid quadratic discrepancies \(E_p=\sum_{i=1}^{N-1}(x_i-i/N)^2\) and \(E_p^\star\) for the reassembled grid. Then **unconditionally**

\[
\boxed{\lim_{\substack{p\to\infty\\p\ {\rm satisfies}\ (1)}}
(E_p^\star-E_p)=
C_{a,b}:=\frac3{\pi^2}\left[
\left(1-\frac1a-\frac1b\right)\left(1-\frac1a\right)^2
+\frac1a\left(\frac1a-\frac1b\right)^2\right]>0.} \tag{5}
\]

Among the asymptotic constants of this *explicit fixed-inverse two-cut family*, the sharp supremum is

\[
\boxed{\sup_{a,b} C_{a,b}=\frac3{\pi^2}
=0.303963550927\ldots .} \tag{6}
\]

For example, the coprime pairs \((a,b)=(m,m+1)\) give \(C_{m,m+1}\to3/\pi^2\). A diagonal choice of sufficiently large primes in their respective Dirichlet progressions produces a single sequence of controls with exactly three near-one defects, total index error tending to zero, and \(E_p^\star-E_p\to3/\pi^2\). Equation (6) is **not** a universal maximum over all three-defect permutations or arbitrary denominator-label paths.

## 2. Exactly three near-one stitches

FD-320 gives for the interface after excursion \(E_j\) and before \(E_\ell\), with outer sentinels \(0,p-1\),

\[
\nu_{j,\ell}=1+\frac{[(j+1)^{-1}]_p-[\ell^{-1}]_p}{p}. \tag{7}
\]

The only changed interfaces in \(ABR\mapsto BAR\) are \((0,k)\), \((c-1,1)\), and \((k-1,c)\). Equations (1)--(2) give

\[
[1^{-1}]_p=1,\qquad [k^{-1}]_p=a,\qquad[c^{-1}]_p=b,
\]

so substitution yields exactly (3), and every unchanged interface or inner excursion triple retains its genuine integer index. Since \(a,b\) are distinct coprime integers, no numerator of the three defects vanishes. Their distances to their nearest integer are as in (4) once \(p>2\max(a,b)\). The full-excursion break-count result of FD-320/FD-321 makes three the minimum for nonidentity permutations *within that family*, but there is no assertion of reflection symmetry or of a global minimality theorem for arbitrary reconstructed paths.

The denominator labels at invalid joins are formal edge labels and need not equal the reduced denominators of the corresponding points. The control is therefore **not a second genuine Farey sequence**, and it does not challenge FD-315 exact-index rigidity.

## 3. Rational-anchor rank estimate and exact transport

For a fixed reduced rational \(\alpha=r/s\in(0,1)\), let \(\rho_p(\alpha)\) be the number of positive Farey fractions of order \(p\) at most \(\alpha\). The identity

\[
\rho_p(\alpha)-\alpha N
=\sum_{d\le p}\mu(d)
\sum_{m\le\lfloor p/d\rfloor}
\bigl(\lfloor\alpha m\rfloor-\alpha m\bigr) \tag{8}
\]

is exact. The partial sum in \(m\) is \(-\frac{s-1}{2s}t+h_\alpha(t)\), where the remainder \(h_\alpha(t)\) is bounded and periodic in the integer \(t\) for fixed \(s\). The elementary identity \(\sum_{d\le p}\mu(d)\lfloor p/d\rfloor=1\) removes the linear term. The bounded remainder contributes \(o(p)\): for \(d\le\epsilon p\) its sum is \(O(\epsilon p)\); for \(d>\epsilon p\), the integer quotient \(\lfloor p/d\rfloor\) takes finitely many values and each associated Möbius sum is \(o(p)\) by PNT, \(M(t)=o(t)\). First send \(p\to\infty\), then \(\epsilon\downarrow0\). Thus, with no RH input,

\[
\boxed{\rho_p(r/s)=\frac rs\,N+o(p)\quad(r/s\ \text{fixed}).} \tag{9}
\]

Set \(\alpha=1/a\) and \(\beta=1-1/b\). The determinant-one and denominator-sum criterion shows that \(k/p\) is the immediate right Farey neighbor of \(1/a\), since \(ak-p=1\), and \(c/p\) the immediate right neighbor of \((b-1)/b\), since \(bc-(b-1)p=1\). Consequently, with \(L_A,L_B\) the numbers of gaps in \(A,B\),

\[
L_A=\rho_p(\alpha),\qquad
L_B=\rho_p(\beta)-\rho_p(\alpha), \tag{10}
\]
\[
\frac{L_A}{N}=\alpha+o(p^{-1}),\qquad
\frac{L_B}{N}=\beta-\alpha+o(p^{-1}). \tag{11}
\]

Apply the exact FD-320 transport decomposition to the block swap. With

\[
w_A=\frac{L_A}N-\frac{k-1}{p},\qquad
w_B=\frac{L_B}N-\frac{c-k}{p},
\]

one has \(D^\star=PD+v\), where \(v=+w_A\) on the \(L_B\) moved \(B\)-coordinates, \(v=-w_B\) on the \(L_A\) moved \(A\)-coordinates, and zero elsewhere. In particular, the **finite** identity is

\[
T_p=\|v\|_2^2=L_B w_A^2+L_A w_B^2,\qquad
E_p^\star-E_p=T_p+2\langle PD,v\rangle. \tag{12}
\]

Using (2) and (11),

\[
p w_A\to1-\frac1a,\qquad
p w_B\to\frac1a-\frac1b,\qquad
\frac N{p^2}\to\frac3{\pi^2}. \tag{13}
\]

Therefore \(T_p\to C_{a,b}\). By FD-002/FD-318 the genuine Farey energy \(E_p=\|D\|_2^2=o(1)\) follows unconditionally from their exact Franel--Mertens identity and PNT. Since \(T_p\) is bounded, Cauchy--Schwarz gives \(|\langle PD,v\rangle|\le\sqrt{E_pT_p}=o(1)\), proving (5). Neither the finite transport identity nor the asymptotic requires RH.

## 4. Sharp family ceiling and full spectral profile

Let \(\gamma=1-1/a-1/b\) and \(\beta=1-1/b\). The limiting rank-coordinate step function is

\[
g_{a,b}(t)=
\begin{cases}
1-1/a,&0<t<\gamma,\\
1/b-1/a,&\gamma<t<\beta,\\
0,&\beta<t<1.
\end{cases} \tag{14}
\]

After the exact transport permutation, \(pv\) converges to this function in normalized rank \(L^2\); the genuine \(D\) part has unscaled \(\ell^2\)-norm \(o(1)\). For every fixed \(m\ge1\), the normalized Dirichlet sine coefficient satisfies

\[
\widehat{D^\star}_m=
\sqrt{\frac2N}\sum_{i=1}^{N-1}D_i^\star
\sin\frac{\pi m i}{N}
\ \longrightarrow\
\frac{\sqrt6}{\pi}\int_0^1g_{a,b}(t)\sin(\pi m t)\,dt. \tag{15}
\]

Sine Parseval and the FD-320 all-mode identity show these fixed-mode limits exhaust the complete energy:
\[
\sum_{m\ge1}\left(\frac{\sqrt6}{\pi}
\int_0^1g_{a,b}(t)\sin(\pi mt)\,dt\right)^2
=\frac3{\pi^2}\int_0^1g_{a,b}(t)^2dt=C_{a,b}. \tag{16}
\]
No positive limiting energy need escape to diverging modes.

Both squared step heights in (14) are strictly less than one and their combined support has length \(\beta<1\); hence \(C_{a,b}<3/\pi^2\). On the other hand, along \(b=a+1\), \(g_{a,a+1}\to1\) in \(L^2(0,1)\), proving the sharp supremum (6). The nested limits can be diagonalized using the infinitude of primes in each *fixed* progression: choose increasing \(a_n\), \(b_n=a_n+1\), and a prime \(p_n\) so large that the finite error in (5) is below \(1/n\) and \(2\max(a_n,b_n)/p_n<1/n\). This does **not** assert a uniform prime-progressions or fixed-rational rank theorem with growing \(a,b\). Along this diagonal, the fixed sine modes tend to the explicit limits

\[
\widehat{D^\star}_m\longrightarrow
\frac{\sqrt6}{\pi^2m}\bigl(1-(-1)^m\bigr), \tag{17}
\]

and their squares sum to \(3/\pi^2\).

## 5. Independent falsification, prior art, and limits

An independent implementation enumerated the genuine Farey fractions, cut them at every denominator-\(p\) vertex, swapped the actual edge and gap subwords, reconstructed the rational grid directly and checked the changed Hall--Shiu indices and directed-edge multiplicities. For \((a,b,p)=(5,6,19)\), it gives \((k,c,N,L_A,L_B)=(4,16,120,23,78)\), precisely three indices \((15/19,24/19,18/19)\), and the **exact** identities
\[
T_{19}=\frac{83839}{866400},\qquad
E_{19}^\star-E_{19}=\frac{1014829951}{12637310400}. \tag{18}
\]
For \((a,b)=(5,6)\) at \(p=79\), the directly computed energy difference is approximately \(0.1143954384\) and the finite transport potential \(0.1166541631\); their common limiting value is \(C_{5,6}=0.1232741068\ldots\). For \((a,b,p)=(9,10,71)\), the three indices are \((63/71,80/71,70/71)\), and the directly computed difference \(0.1585066557\) is compatible with \(C_{9,10}=0.1894706134\ldots\). These are finite falsification controls, not proofs of convergence.

The Hall--Shiu index and Farey denominator recurrence, gap geometry, Franel--Landau relation, Möbius inversion, totient asymptotic, PNT, CRT and Dirichlet's theorem are classical; the prime-order excursion transport identity and fixed-inverse cut method are adaptations of FD-320 and FD-322. Hall--Shiu (Michigan Math. J. **51**, 2003, 209--223) is the local-index prior-art boundary. García, *A General Lower Bound for Average Local Discrepancy and an Application to the Farey Sequence*, Mathematics **14** (2026), 2543, DOI 10.3390/math14142543, studies gap permutations and a different (absolute-average) discrepancy; it does not supply this two-cut quadratic transport ceiling. A targeted check of that work and the Farey-index literature found no identical fixed-inverse two-parameter certificate; no exhaustive novelty/priority assertion follows.

The result concerns **abstract labeled-edge matched controls**, not actual alternative Farey sequences. The bound \(3/\pi^2\) is sharp solely for this explicit family of swaps with fixed modular inverses, not for all three-index-defect paths. It changes neither the unconditional estimate on the genuine \(E_p\) nor the RH-equivalent Franel--Landau threshold. Its concrete control-design implication is stronger than FD-322: even three arbitrarily small near-positive-integer index violations permit spectral transport approaching the entire natural \(N_p/p^2\) energy scale. Additional *source-natural cumulative transport* constraints, rather than index-defect counts or sizes, remain necessary to pursue a coercive Farey-geometric estimate.
