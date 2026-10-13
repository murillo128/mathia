# FD-329 — Four exact Farey defect ranks are rigid; five permit transport-energy ambiguity

**Status:** EXACT-DERIVED + FINITE-CLASSIFICATION + NEGATIVE/CONTROL-DESIGN + TOTIENT-ASYMPTOTIC.

FD-328 reconstructs every three-break permutation of whole prime-Farey excursions from its three noninteger Hall--Shiu index ranks. The next threshold is sharp: **four** exact defective ranks still reconstruct the entire excursion permutation, but **five** can be identical for distinct reassemblies with different exact transport potentials and (already at order seven) different reconstructed Franel energies. No equality of the *defective index values* is asserted for the five-break controls.

## 1. Four-break rigidity and rank certificate

Let \(p\ge7\) be an odd prime, \(n=p-2\), \(N=N_p=\sum_{q\le p}\varphi(q)\), and \(E_1,\ldots,E_n\) the complete prime-denominator excursions from FD-320. Write \(\ell_j>0\) for their original gap counts and
\[
S_0=0,\qquad S_j=\sum_{u=1}^{j}\ell_u,\qquad S_n=N-2.
\tag{1}
\]
Each permuted excursion retains its directed denominator-edge word and each original positive gap. The unchanged first and last gaps make the reassembled grid end at \(1\).

**Four-break classification.** Every whole-excursion permutation having exactly four noninteger interior Hall--Shiu indices is uniquely of the form
\[
\boxed{P\,C\,B\,A\,R},
\tag{2}
\]
where, for unique cuts \(1\le i<k<l<c\le n+1\),
\[
\begin{split}
P&=E_1\cdots E_{i-1},&
A&=E_i\cdots E_{k-1},\\
B&=E_k\cdots E_{l-1},&
C&=E_l\cdots E_{c-1},&
R&=E_c\cdots E_n .
\end{split}
\tag{3}
\]
Empty exterior \(P,R\) are allowed; \(A,B,C\) are nonempty. There are exactly \(\binom{n+1}{4}=\binom{p-1}{4}\) such permutations.

Their four defective *rank positions*, numbered as in FD-328 among \(x_0,\ldots,x_N\), satisfy
\[
\begin{split}
r_1&=1+S_{i-1},\\
r_2&=1+S_{i-1}+S_{c-1}-S_{l-1},\\
r_3&=1+S_{i-1}+S_{c-1}-S_{k-1},\\
r_4&=1+S_{c-1}.
\end{split}
\tag{4}
\]
Consequently, for fixed \(p\), the increasing rank quadruple uniquely reconstructs the cuts:
\[
\boxed{\begin{split}
i&=1+S^{-1}(r_1-1),\\
k&=1+S^{-1}(r_1+r_4-r_3-1),\\
l&=1+S^{-1}(r_1+r_4-r_2-1),\\
c&=1+S^{-1}(r_4-1).
\end{split}}
\tag{5}
\]
Here \(S^{-1}\) is defined only on the strictly increasing finite image \(\{S_0,\ldots,S_n\}\). An increasing integer quadruple occurs as the *complete* four-defect rank signature if and only if all four arguments in (5) belong to that image. Their increasing order then follows from \(r_1<r_2<r_3<r_4\). In particular, fixing \(p\) and the four exact defective ranks fixes the entire reassembly and thus, by FD-320, the full transport vector, quadratic energy and sine spectrum.

**Proof.** Adjoin sentinel excursion labels \(0\) and \(n+1\). FD-320, equation (7), says that an interface is nonintegral exactly when its next label is not its current label plus one. Four defects therefore produce five maximal increasing-by-one runs. The first consists of the sentinel followed by the untouched prefix \(P\), and the last of the untouched suffix \(R\) followed by the final sentinel. The other three runs partition the remaining consecutive label interval into exactly three contiguous nonempty blocks \(A,B,C\), written here in original label order. To have breaks at **all four** interfaces, their reordered block permutation must begin with a block other than \(A\), end with a block other than \(C\), and never place \(A\) immediately before \(B\) or \(B\) immediately before \(C\). Among the six possible three-block orders, **only \(CBA\)** meets all these conditions. Conversely \(PCBAR\) has exactly four breaks. The initial outer gap contributes rank one; summing the gap counts of \(P,C,B,A\) gives (4). Strict monotonicity of \(S\) gives (5), the realizability criterion and the count.

## 2. Five matching ranks with unequal transport potentials

The four-break injectivity cannot extend to five breaks. For **every** odd prime \(p\ge7\), set \(n=p-2\) and partition the original excursion word as
\[
A=E_1,\quad B=E_2,\quad
C=E_3\cdots E_{n-2},\quad D=E_{n-1},\quad R=E_n.
\tag{6}
\]
Consider the two different complete reassemblies
\[
\boxed{\sigma=B\,D\,A\,C\,R,\qquad
       \tau=D\,B\,A\,C\,R.}
\tag{7}
\]
Both retain the same first/last Farey gaps and the *entire* directed denominator-edge multiset. Both have exactly five noninteger index junctions: the first boundary, each of the three following joins among the four reordered blocks, and the join \(C|R\).

Reflection of the genuine Farey grid yields \(\ell_j=\ell_{n+1-j}\). Put \(a=\ell_1=\ell_n\), \(b=\ell_2=\ell_{n-1}\), and \(h=\sum_{j=3}^{n-2}\ell_j=N-2-2a-2b>0\). Because the two interchanged blocks \(B,D\) each contain exactly \(b\) gaps, their *ordered* five defect-rank signatures coincide **exactly**:
\[
\boxed{(r_1,r_2,r_3,r_4,r_5)
=(1,\ 1+b,\ 1+2b,\ 1+2b+a,\ N-1-a).}
\tag{8}
\]

The resulting transport potentials nevertheless need not agree. Define the mismatches
\[
x=\frac{a}{N}-\frac1p,\quad
y=\frac{b}{N}-\frac1p,\quad
z=\frac{h}{N}-\frac{n-4}{p}.
\tag{9}
\]
Applying the blockwise exact decomposition of FD-320, the displacements on \(B,D,A,C\) for \(\sigma\) are respectively
\((x,x+z,-2y,-y)\), whereas those on \(D,B,A,C\) for \(\tau\) are
\((x+y+z,x-y,-2y,-y)\). Thus the weighted energy difference is the **finite identity**
\[
\begin{split}
T_p(\sigma)-T_p(\tau)
&=b\{x^2+(x+z)^2-(x+y+z)^2-(x-y)^2\}\\
&=-2b\,y(y+z)\\
&=\boxed{-2b\left(\frac bN-\frac1p\right)
\left(\frac5p-\frac{p+3+b}{N}\right)}.
\end{split}
\tag{10}
\]
The final equality uses \(h=N-2-2a-2b\), \(n=p-2\), and \(2a=p+1\).

In fact, direct counting of reduced fractions in the first two excursion intervals gives
\[
a=\frac{p+1}{2},\qquad b=\left\lfloor\frac p3\right\rfloor+1.
\tag{11}
\]
For the second interval \((2/p,3/p)\), all interior reduced fractions have numerator \(1\) or \(2\). For \(p=6m+1\), each numerator contributes \(m\) fractions; for \(p=6m-1\), the contributions are \(m\) and \(m-1\), respectively; the closing gap contributes one in both cases. Using the classical totient summatory asymptotic \(N=3p^2/\pi^2+O(p\log p)\) in (10) proves
\[
\boxed{\lim_{\substack{p\to\infty\\p\ \mathrm{prime}}}
p\big(T_p(\sigma)-T_p(\tau)\big)
=-\frac23\left(\frac{\pi^2}{9}-1\right)
\left(5-\frac{4\pi^2}{9}\right)\ne0.}
\tag{12}
\]
Thus **arbitrarily large primes admit different five-break controls with identical five defect ranks and unequal exact transport energies**. Their energy separation is of order \(1/p\); (12) does **not** assert a macroscopic or RH-critical separation of their actual Franel energies.

## 3. Exact falsification controls

At \(p=7\), \(N=18\) and the true excursion lengths are \((4,3,2,3,4)\). Formula (7) gives the different words \((2,4,1,3,5)\) and \((4,2,1,3,5)\), both with rank signature \((1,4,7,11,13)\). Their noninteger index **values** differ: they are respectively
\[
(4,10,9,6,6)/7\quad\text{and}\quad(6,6,11,6,6)/7.
\tag{13}
\]
Exact rational Farey-gap reconstruction, performed independently of the transport formula, gives
\[
T_7(\sigma)=\frac{95}{2646},\qquad
T_7(\tau)=\frac{46}{1323},\qquad
T_7(\sigma)-T_7(\tau)=\frac1{882},
\tag{14}
\]
and even the full reconstructed Franel energies differ:
\[
E_7^\sigma=\frac{55}{1176},\qquad
E_7^\tau=\frac{793}{17640},\qquad
E_7^\sigma-E_7^\tau=\frac4{2205}.
\tag{15}
\]
The genuine energy for this order is \(E_7=197/7560\), and both reconstructions have endpoint \(1\). At \(p=7\) and \(11\), exhaustive independent enumeration of all \(5!\) and \(9!\) excursion permutations respectively found exactly \(15\) and \(210\) four-break permutations and **no** repeated four-break rank signatures. Separate exact cut enumeration at \(p=13,17\) checked all \(495,1820\) four-break possibilities. Exact rational evaluations of (10) for \(p=7,11,13,17,19,23,31,43\) matched both direct block-transport evaluations; finite checks test indexing and arithmetic, while the proofs above are combinatorial and asymptotic.

## 4. Prior art, boundaries, and consequence

Breakpoints, maximal consecutive runs and rearrangements of permutation blocks are classical in genome-rearrangement combinatorics; see Fertin, Labarre, Rusu, Tannier and Vialette, *Combinatorics of Genome Rearrangements* (MIT Press, 2009), also cited by FD-328. Hall and Shiu, *The index of a Farey sequence*, Michigan Math. J. **51** (2003), 209--223, DOI 10.1307/mmj/1049832901, establish the classical index notion. García, *A General Lower Bound for Average Local Discrepancy and an Application to the Farey Sequence*, Mathematics **14** (2026), 2543, DOI 10.3390/math14142543, studies different gap-permutation statistics. No broad novelty or priority claim is made for generic permutation combinatorics; the line-local mathematical delta is the **sharp four-versus-five defective-rank identifiability threshold together with the Farey-specific exact transport-energy witness**.

As in FD-320 and FD-328, these are *labeled-edge controls*, not second genuine Farey sequences: at nonintegral stitches the inherited denominator labels may not coincide with denominators of the reconstructed reduced points. Fixing the **defective rank positions alone** identifies three- and four-break controls but fails at five. The five-break counterexample does not fix the defective **index values**, and no claim is made about simultaneous rank-and-value matching, or about higher-break classification. The asymptotic difference (12) concerns \(T_p\), whereas (15) supplies an exact finite-order difference of true reconstructed energies. Neither is an improvement to the Franel--Landau exponent nor a step proving RH.