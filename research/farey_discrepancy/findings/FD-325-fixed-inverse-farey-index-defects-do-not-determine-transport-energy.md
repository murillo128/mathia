# FD-325 — Fixed-inverse Farey index defects do not determine transport energy

**Status:** EXACT-DERIVED + PNT-AND-DIRICHLET-ASSISTED-ASYMPTOTIC + NEGATIVE/CONTROL-DESIGN.

FD-320 gives an exact, uniformly spectral transport law for prime-order Farey excursion permutations. FD-323 constructed three near-one index defects with an order-one discrepancy energy change. The ordered, scaled values of *all three defects* still do not determine that energy: the modular inverses at the cuts do not determine the rational numerators of their limit locations. The following two progressions have the same local defect coefficients but sixfold different energy limits.

## 1. Fixed-inverse fiber theorem

Fix coprime integers \(a,b\ge3\), \(a\ne b\), and integers \(1\le r<a\), \(1\le s<b\) with \(\gcd(r,a)=\gcd(s,b)=1\) and
\[
 0<\alpha:=r/a<\beta:=s/b<1. \tag{1}
\]
Choose primes satisfying
\[
 rp\equiv-1\pmod a,\qquad sp\equiv-1\pmod b. \tag{2}
\]
The CRT specifies an invertible residue class modulo \(ab\), so Dirichlet's theorem gives infinitely many such primes. For sufficiently large primes in that class set
\[
 k=(rp+1)/a,\qquad c=(sp+1)/b,\qquad 1<k<c\le p-2. \tag{3}
\]
For the order-\(p\) Farey sequence \(0=x_0<\cdots<x_N=1\), \(N=\sum_{q\le p}\varphi(q)\), let \(E_j\) be the complete excursion from \(j/p\) to \((j+1)/p\), \(1\le j\le p-2\). Split its inner excursion word into
\[
 A=E_1\cdots E_{k-1},\quad B=E_k\cdots E_{c-1},
 \quad R=E_c\cdots E_{p-2},
\]
and replace \(ABR\) with \(BAR\). Keep the two outer denominator edges, and reconstruct the increasing point grid by copying each original directed edge \((u,v)\) with its positive gap \(1/(uv)\).

Every directed denominator-edge multiplicity, the gap multiset, and the two outer edges are preserved. Exactly three Hall--Shiu indices are nonintegral, with ordered values
\[
 \boxed{
 (\nu_1,\nu_2,\nu_3)
 =\left(1-\frac{a-1}p,\ 1+\frac{b-1}p,\
 1+\frac{a-b}p\right).} \tag{4}
\]
In particular,
\[
 \boxed{p(\nu_1-1,\nu_2-1,\nu_3-1)
       =(1-a,\ b-1,\ a-b)} \tag{5}
\]
is independent of \(r,s\). All three defective indices converge to the positive integer \(1\), with vanishing total nearest-integer distance.

Let \(E_p=\sum_{i=1}^{N-1}(x_i-i/N)^2\), and let \(E_p^{r,s}\) be the rank-grid energy of the reassembled control. Then, unconditionally,
\[
\boxed{\lim_{\substack{p\to\infty\\p\ {\rm satisfies}\ (2)}}
 (E_p^{r,s}-E_p)=
 C_{a,b;r,s}
 :=\frac3{\pi^2}\left[
 (\beta-\alpha)\left(1-\frac1a\right)^2
 +\alpha\left(\frac1a-\frac1b\right)^2
 \right].} \tag{6}
\]
This is a family of matched *labeled-edge controls*, not a family of genuine Farey sequences. The defect ranks may differ, and the different prime progressions are not two interchangeable reconstructions at the **same** prime.

## 2. Sixfold separation with one ordered defect profile

Set \((a,b,r)=(3,5,1)\) and compare \(s=4\) and \(s=2\). Both use \(k=(p+1)/3\), whereas
\(c=(4p+1)/5\) for primes \(p\equiv11\pmod{15}\) and
\(c=(2p+1)/5\) for primes \(p\equiv2\pmod{15}\). Dirichlet guarantees infinitely many primes in each class; for sufficiently large primes the required cuts are valid. The two rational-anchor pairs are
\[
 (\alpha,\beta)=(1/3,4/5)
 \quad\hbox{and}\quad
 (\alpha,\beta)=(1/3,2/5). \tag{7}
\]
For *every* prime of either family, the ordered defective indices are exactly
\[
 (1-2/p,\ 1+4/p,\ 1-2/p),\qquad
 p(\nu_i-1)_{i=1}^3=(-2,4,-2), \tag{8}
\]
and the total nearest-integer defect is \(8/p\). Yet equation (6) gives
\[
\begin{aligned}
 C_{3,5;1,4}
 &=\frac3{\pi^2}
    \left(\frac7{15}\frac49+\frac13\frac4{225}\right)
   =\boxed{\frac{16}{25\pi^2}},\\
 C_{3,5;1,2}
 &=\frac3{\pi^2}
    \left(\frac1{15}\frac49+\frac13\frac4{225}\right)
   =\boxed{\frac8{75\pi^2}}.
\end{aligned} \tag{9}
\]
Their ratio is **six**. Thus no p-independent limiting energy formula can be based solely on the three scaled ordered defect coefficients. The stronger data of the prime \(p\), inverse labels, and permutation topology recover the cuts; this example does not refute recovery from those data.

## 3. Exact index and transport derivation

For a join after excursion \(E_j\) and before \(E_\ell\), FD-320 gives
\[
 \nu_{j,\ell}
 =1+\frac{[(j+1)^{-1}]_p-[\ell^{-1}]_p}{p}, \tag{10}
\]
where \(0,p-1\) are outer sentinel labels. Since \(ak=rp+1\) and \(bc=sp+1\),
\([k^{-1}]_p=a\), \([c^{-1}]_p=b\), independently of \(r,s\).
The sole altered joins are \((0,k)\), \((c-1,1)\), and \((k-1,c)\). Their inverse differences are respectively \(1-a,b-1,a-b\), proving (4)--(5); all untouched triples keep integral indices.

Let \(\rho_p(\gamma)\) be the count of positive Farey fractions at most a fixed reduced rational \(\gamma\in(0,1)\). The exact Möbius formula, used in FD-323, is
\[
 \rho_p(\gamma)-\gamma N
 =\sum_{d\le p}\mu(d)
   \sum_{m\le\lfloor p/d\rfloor}
     (\lfloor\gamma m\rfloor-\gamma m). \tag{11}
\]
For fixed \(\gamma\) the inner sum is a linear function of its integer length plus a bounded periodic remainder. The linear part reduces to a constant using
\(\sum_{d\le p}\mu(d)\lfloor p/d\rfloor=1\).
For the remainder split \(d\le\epsilon p\) and \(d>\epsilon p\). The former contributes \(O_\gamma(\epsilon p)\); in the latter, \(\lfloor p/d\rfloor\) takes finitely many values and each Möbius summatory interval contributes \(o(p)\) by PNT, \(M(t)=o(t)\). Take \(p\to\infty\) and then \(\epsilon\downarrow0\) to get
\[
 \rho_p(\gamma)=\gamma N+o_\gamma(p). \tag{12}
\]
Because \(ak-rp=bc-sp=1\), \(k/p\) and \(c/p\) are the immediate right Farey neighbors of \(\alpha=r/a\), \(\beta=s/b\) respectively once \(a+p>p\), \(b+p>p\). Hence the gap counts of blocks \(A\) and \(B\) satisfy
\[
 L_A=\rho_p(\alpha),\quad
 L_B=\rho_p(\beta)-\rho_p(\alpha),\quad
 \frac{L_A}N=\alpha+o(p^{-1}),\quad
 \frac{L_B}N=\beta-\alpha+o(p^{-1}). \tag{13}
\]
Their length-versus-width deviations are
\[
 w_A=\frac{L_A}N-\frac{k-1}p,\qquad
 w_B=\frac{L_B}N-\frac{c-k}p. \tag{14}
\]
Substituting (3) and (13) yields
\[
 pw_A\to 1-\frac1a,\qquad
 pw_B\to\frac1a-\frac1b. \tag{15}
\]
The exact FD-320 permutation identity is \(D^{r,s}=PD+v\), with \(v=w_A\) on the \(L_B\) moved \(B\)-coordinates, \(v=-w_B\) on the \(L_A\) moved \(A\)-coordinates, and zero elsewhere. Therefore, *at finite p*,
\[
 T_p=\|v\|_2^2=L_Bw_A^2+L_Aw_B^2,\qquad
 E_p^{r,s}-E_p=T_p+2\langle PD,v\rangle. \tag{16}
\]
The standard totient asymptotic \(N/p^2\to3/\pi^2\) and (13)--(15) give \(T_p\to C_{a,b;r,s}\). FD-002/FD-318 establish \(E_p=\|D\|_2^2=o(1)\) unconditionally by the exact Franel--Mertens identity and PNT. As \(T_p\) is bounded, the cross term in (16) is at most \(2\sqrt{E_pT_p}=o(1)\), completing the proof of (6).

By FD-320, the sine transform of \(D^{r,s}-v\) has squared norm \(E_p=o(1)\). The normalized-rank step function of \(pv\) tends to
\[
 g_{\alpha,\beta}(t)=
 \begin{cases}
 1-1/a,&0<t<\beta-\alpha,\\
 1/b-1/a,&\beta-\alpha<t<\beta,\\
 0,&\beta<t<1,
 \end{cases} \tag{17}
\]
and \((3/\pi^2)\int_0^1g_{\alpha,\beta}(t)^2dt=C_{a,b;r,s}\).
Thus the different cut numerators change the limiting *full* transport spectrum as well as its total energy. No positive limiting norm is lost to diverging sine modes, by Parseval for the step function.

## 4. Independent rational checks and adversarial controls

A separate exact-rational enumerator constructed the genuine reduced fractions and the original directed gaps, performed the cut-and-swap, reconstructed each gap cumulatively, and checked the complete directed-edge multiset, all Hall--Shiu indices, the pointwise block permutation identity, and (16).

For \(p=11\), \(s=4\), it found \(N=42\), \(k=4\), \(c=9\), \((L_A,L_B)=(14,20)\), nonintegral indices \((9/11,15/11,9/11)\), \(T_p=610/7623\), and exact energy difference \(41033/640332\). For \(p=17\), \(s=2\), it found \(N=96\), \(k=6\), \(c=7\), \((L_A,L_B)=(32,6)\), nonintegral indices \((15/17,21/17,15/17)\), \(T_p=67/6936\), and energy difference \(32477/3884160\). The exact edge, defect, and transport checks were repeated for \(p=41,47,71,107,131,137\). These finite checks falsify possible mistakes in the construction but do **not** replace the PNT-assisted proof of its limits.

## 5. Prior art and boundaries

The Hall--Shiu Farey index, modular-inverse neighbor denominators, Farey adjacency, Dirichlet's theorem, PNT, and the totient count are classical. Hall--Shiu, *The index of a Farey sequence* (Michigan Math. J., 2003; DOI 10.1307/mmj/1049832901) is the index anchor. García, *New Analytical Formulas for the Rank of Farey Fractions and Estimates of the Local Discrepancy* (Mathematics 2025; DOI 10.3390/math13010140) concerns Farey ranks; García, *A General Lower Bound for Average Local Discrepancy and an Application to the Farey Sequence* (Mathematics 2026; DOI 10.3390/math14142543) examines gap permutations for a distinct average-local quantity. These sources are already anchored in the line's SOURCES.md. FD-320 and FD-323 supply the exact transport and fixed-inverse construction. The new mathematical delta here is nonconstant transport energy within a single **fixed inverse/index-defect fiber**, exposed by distinct rational numerators. A targeted comparison did not identify this explicit separation in the cited literature, but this is not an exhaustive novelty or priority claim.

The controls are reassembled labeled-edge grids: at invalid joins the inherited denominator labels need not be the *actual reduced denominators of the reconstructed points*. Nothing contradicts genuine Farey index rigidity (FD-315), supplies a stronger bound for genuine Franel energy, or advances RH. The result identifies the missing datum in any local-index-only coercivity argument: the cut numerators/rank locations, or more intrinsically the weighted cumulative excursion transport of FD-320.
