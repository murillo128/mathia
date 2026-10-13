# FD-330 — Five identical Farey defect ranks permit macroscopic energy separation

**Status:** EXACT-DERIVED + PNT/DIRICHLET-ASSISTED-ASYMPTOTIC + NEGATIVE/CONTROL-DESIGN + EXACT-RATIONAL-CHECKS.

FD-329 proves four-break rank rigidity and constructs distinct five-break prime-Farey excursion reassemblies with exactly the same defective rank positions, but its transport-energy separation is only of order \(1/p\). The **same-rank obstruction is macroscopic**: symmetric blocks occupying fixed positive proportions of the Farey grid yield a nonzero limiting difference of reconstructed Franel energies. The defective index *values* are not matched.

## 1. Same-prime five-rank theorem

Fix integers \(u>v\ge3\) and put \(L=\operatorname{lcm}(u,v)\). Let \(p\to\infty\) through primes \(p\equiv-1\pmod L\), which exist by Dirichlet. Write \(n=p-2\), \(N=N_p=\sum_{q\le p}\varphi(q)\), and \(E_1,\ldots,E_n\) for the complete directed denominator-\(p\) excursions in the genuine prime-order Farey sequence, following FD-320. For sufficiently large such \(p\), set
\[
i=\frac{p+1}{u},\qquad j=\frac{p+1}{v},
\qquad 2\le i<j<p-j<p-i\le p-2.
\tag{1}
\]
Partition the **original consecutive excursion word** into five nonempty blocks
\[
\begin{split}
A&=E_1\cdots E_{i-1},&
B&=E_i\cdots E_{j-1},\\
C&=E_j\cdots E_{p-j-1},&
D&=E_{p-j}\cdots E_{p-i-1},\\
R&=E_{p-i}\cdots E_{p-2}.
\end{split}
\tag{2}
\]
Consider the two reassemblies, preserving every directed denominator-edge word, every gap \(1/(ab)\), and the genuine outer edges,
\[
\boxed{\sigma=B\,D\,A\,C\,R,\qquad
       \tau=D\,B\,A\,C\,R.}
\tag{3}
\]
Reflection of the Farey grid gives equal gap counts for \(A,R\) and for \(B,D\). Write \(a=\ell(A)=\ell(R)\), \(b=\ell(B)=\ell(D)\), \(h=\ell(C)\), where \(\ell\) counts gaps. Thus \(2a+2b+h=N-2\).

**Exact matching signature.** Both reassemblies have exactly five noninteger Hall--Shiu indices, at the *same increasing rank positions*
\[
\boxed{(r_1,r_2,r_3,r_4,r_5)=
(1,\ 1+b,\ 1+2b,\ 1+2b+a,\ N-1-a).}
\tag{4}
\]
They are distinct permutations of the **same** \(F_p\) and share the complete directed-edge and gap multisets, endpoint \(1\), first/last edges, and defective rank set. Nevertheless their FD-320 transport potentials \(T_p\), and their full reconstructed Franel energies \(E_p^\sigma,E_p^\tau\), obey
\[
\boxed{
\lim_{\substack{p\to\infty\\p\equiv-1\pmod L}}
\bigl(T_p(\sigma)-T_p(\tau)\bigr)
=
\lim_{\substack{p\to\infty\\p\equiv-1\pmod L}}
\bigl(E_p^\sigma-E_p^\tau\bigr)
=
\frac6{\pi^2}
\left(\frac1v-\frac1u\right)^2
\left(\frac1u+\frac1v\right)>0.
}
\tag{5}
\]
For \(u=4,v=3\), the limit is \(7/(288\pi^2)\). Unlike FD-329, this is **order-one**, not a vanishing \(O(1/p)\) difference. Neither (4) nor (5) asserts matching defective-index values.

## 2. Finite rank and transport identities

The two words in (3) have five nonconsecutive-label interfaces (including the initial sentinel interface), with all within-block interfaces consecutive. The final \(R\) is unchanged; \(i<j<p-j<p-i\) rules out accidental consecutive-label joins. By FD-320, equation (7), these and only these five interfaces have noninteger indices. Because \(B,D\) both have \(b\) gaps and \(A,C\) retain their gap counts, the cumulative lengths before those interfaces agree for the two words, giving (4).

Define the three original-block length-versus-geometric-width mismatches
\[
x=\frac aN-\frac{i-1}{p},\qquad
y=\frac bN-\frac{j-i}{p},\qquad
z=\frac hN-\frac{p-2j}{p}.
\tag{6}
\]
The total length and width identities imply the **finite exact conservation law**
\[
2x+2y+z=\frac2p-\frac2N.
\tag{7}
\]
Apply the exact block-displacement decomposition \(D^\omega=P_\omega D+v^\omega\) of FD-320. On the reordered blocks \(B,D,A,C\), the shifts for \(\sigma\) are respectively \((x,x+z,-2y,-y)\); for \(\tau\), on \(D,B,A,C\), they are \((x+y+z,x-y,-2y,-y)\). The last block \(R\) has zero shift. Weighting squared shifts by the actual gap counts proves, **without limits or unproved cancellation**,
\[
\begin{split}
T_p(\sigma)&=b[x^2+(x+z)^2]+4ay^2+hy^2,\\
T_p(\tau)&=b[(x+y+z)^2+(x-y)^2]+4ay^2+hy^2,\\
\boxed{T_p(\sigma)-T_p(\tau)}&=
\boxed{-2b\,y(y+z).}
\end{split}
\tag{8}
\]
Thus the same-rank ambiguity can be checked from the **three genuine Farey block counts** \(a,b,h\), independently of the full reassembled coordinates.

## 3. The rational-rank asymptotic and limiting constant

For every fixed integer \(q\ge2\), let \(\rho_p(1/q)\) be the number of **positive** fractions in \(F_p\) at most \(1/q\). The fixed-rational Farey-rank estimate needed here is
\[
\boxed{\rho_p(1/q)=N_p/q+o_q(p).}
\tag{9}
\]
For completeness, Möbius inversion gives the exact difference
\[
\rho_p(1/q)-N_p/q=
\sum_{d\le p}\mu(d)\,
G_q\!\left(\left\lfloor p/d\right\rfloor\right),\qquad
G_q(H)=\sum_{m=1}^{H}\left(\left\lfloor m/q\right\rfloor-m/q\right).
\tag{10}
\]
Here \(G_q(H)=-(q-1)H/(2q)+O_q(1)\), while
\(\sum_{d\le p}\mu(d)\lfloor p/d\rfloor=1\). For the bounded remainder in \(G_q\), split \(d\le\delta p\) (contribution \(O_q(\delta p)\)) from \(d>\delta p\). In the latter region \(\lfloor p/d\rfloor\) takes only finitely many values depending on fixed \(\delta\); grouping these quotient intervals and using \(M(X)=o(X)\) from the prime number theorem makes each group's signed sum \(o(p)\). Let \(\delta\downarrow0\) to prove (9). No RH input enters this estimate.

Since \(ui-p=vj-p=1\), the reduced fractions \(1/u,i/p\) are adjacent in \(F_p\), as are \(1/v,j/p\), with \(i/p,j/p\) on their right. Therefore the gap counts in (2) satisfy **exactly**
\[
a=\rho_p(1/u),\qquad
b=\rho_p(1/v)-\rho_p(1/u).
\tag{11}
\]
Put \(\alpha=1/u\), \(\beta=1/v\), \(d=\beta-\alpha>0\). Equations (9)--(11), together with the classical totient asymptotic \(N_p=3p^2/\pi^2+O(p\log p)\), yield
\[
\frac{a}{N_p}=\alpha+o(p^{-1}),\quad
\frac{b}{N_p}=d+o(p^{-1}),\quad
\frac b{p^2}\longrightarrow\frac3{\pi^2}d,
\quad px\longrightarrow1-\alpha,\quad py\longrightarrow-d.
\tag{12}
\]
Combining (7) with (12) gives
\[
p(y+z)\longrightarrow
2-2(1-\alpha)+d=\alpha+\beta.
\tag{13}
\]
Substitution into the **exact** identity (8) proves the transport limit (5).

Each of \(a,b,h\) is \(O(p^2)\) and \(x,y,z=O(p^{-1})\), so both \(T_p(\sigma)\) and \(T_p(\tau)\) are bounded. FD-320 gives
\[
\left|\sqrt{E_p^\omega}-\sqrt{T_p(\omega)}\right|
\le\sqrt{E_p}=o(1)
\qquad(\omega=\sigma,\tau)
\tag{14}
\]
unconditionally from the prime-number-theorem Franel--Mertens estimate for the genuine Farey energy. With bounded transport, (14) implies \(E_p^\omega-T_p(\omega)=o(1)\) for each word and proves the **Franel-energy** limit in (5). This inference is valid here precisely because the transport potentials remain bounded.

## 4. Independent exact-rational falsification

An independent check generated \(F_p\) by the Farey recurrence, cut the **actual directed denominator-edge/gap words** at each \(j/p\), and concatenated the words (3). The reconstructed points were summed as exact rational numbers from the gaps \(1/(ab)\), not inferred from the transport formula. For \(p=11,23,47,59\), the check verified: endpoint exactly \(1\), identical directed-edge inventories, exactly five defective Hall--Shiu indices at the common ranks (4), and the exact identity (8) against separately computed energies. In particular:

| \(p\) | \(N_p\) | common defective ranks | exact \(T_p(\sigma)-T_p(\tau)\) | \(E_p^\sigma-E_p^\tau\) |
| --- | ---: | --- | ---: | ---: |
| 11 | 42 | \((1,5,9,19,31)\) | \(-32/53361\) | \(-164/266805\) |
| 23 | 172 | \((1,15,29,72,128)\) | \(2387/978121\) | \(559599563/240696925560\) |
| 47 | 696 | \((1,60,119,292,522)\) | \(232991/535037472\) | \(\approx0.00038913148\) |
| 59 | 1086 | \((1,91,181,453,813)\) | \(291600/114041041\) | \(\approx0.00289020388\) |

At \(p=23\), for example, the **five index values differ**: they are \((20,6,41,24,24)/23\) for \(\sigma\) and \((4,38,25,24,24)/23\) for \(\tau\), although the five ranks match. The negative finite differences at \(p=11\) also emphasize that (5) is an asymptotic claim, not a positivity theorem for every admissible prime. The exact computations are falsification checks of the indexing and block algebra, not evidence replacing the proof of the limit.

## 5. Prior art, information boundary, and consequence

The Hall--Shiu index and Farey-neighbor determinant tests are classical (Hall and Shiu, *The index of a Farey sequence*, Michigan Math. J. **51** (2003), 209--223, DOI 10.1307/mmj/1049832901). Breakpoint/block-permutation combinatorics are classical (Fertin et al., *Combinatorics of Genome Rearrangements*, MIT Press, 2009). García, *A General Lower Bound for Average Local Discrepancy and an Application to the Farey Sequence*, *Mathematics* **14** (2026), 2543, DOI 10.3390/math14142543, analyzes gap permutations for a different **average local** statistic. The relevant arithmetic inputs and their roles are recorded in this line's SOURCES.md and FD-320. No general priority claim is made for rearrangement or discrepancy algebra; the line-local delta is the **macroscopic, same-prime, exact-five-rank counterexample** strengthening FD-329.

These are deliberately **labeled-edge reassemblies**, not alternative genuine Farey sequences. At defective stitches, denominator labels carried with the copied edge need not be the true reduced denominators of the reconstructed rational vertices. Matching five *rank positions* is not matching their five *index values*, nor does it provide an RH-sensitive coercive invariant; an argument using both ranks and values remains a separate question. The conclusion rules out **rank-only** multiplicative or asymptotically vanishing additive energy control in this matched-control class. It proves no improvement to the Franel--Landau criterion or RH.
