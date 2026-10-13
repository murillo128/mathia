# FD-328 — Three Farey-index defect ranks reconstruct the excursion permutation

**Status:** EXACT-DERIVED + FINITE-CLASSIFICATION + NEGATIVE/CONTROL-DESIGN + RANK-POSITION-RIGIDITY.

FD-327 constructs two permutations of the **same** prime-order Farey excursion word with equal ordered nonintegral Hall--Shiu index values, identical directed denominator-edge inventories, and arbitrarily separated transport energies. Its defect **rank positions differ**. This distinction is sharp in the minimal three-defect class: fixing the prime and those three ranks determines the entire reassembly, without requiring the defect values. Consequently there is no nontrivial three-defect matched ensemble with all three defect ranks fixed.

## 1. Exact theorem and inverse certificate

Let $p\ge7$ be an odd prime, $n=p-2$, $N=\sum_{q\le p}\varphi(q)$, and let $E_1,\ldots,E_n$ be the complete denominator-$p$ excursions of the genuine order-$p$ Farey sequence, as in FD-320. Each $E_j$ goes from $j/p$ to $(j+1)/p$, has positive gap count $\ell_j$, and retains its complete directed denominator-edge word and gaps. Put
$$
S_0=0,\qquad S_j=\sum_{u=1}^{j}\ell_u \quad (1\le j\le n).
\tag{1}
$$
In particular, $S_n=N-2$ and $S_j$ is strictly increasing.

Permute the whole excursions, preserving the original outer edges $1\to p$ and $p\to1$, and reconstruct the increasing rational grid by its original edge gaps $1/(ab)$. Consider a **nonidentity** permutation with exactly three noninteger interior Hall--Shiu indices, occurring at rank positions $1\le r_1<r_2<r_3\le N-1$ (ranks are zero-based for the Farey vertices $x_0,\ldots,x_N$).

**Three-break classification.** There exist unique integers
$$
1\le i<k<c\le n+1=p-1
\tag{2}
$$
such that the complete excursion word is
$$
E_1\cdots E_{i-1}\quad
E_k\cdots E_{c-1}\quad
E_i\cdots E_{k-1}\quad
E_c\cdots E_n .
\tag{3}
$$
Empty exterior words are allowed. Thus every minimal-defect nonidentity excursion permutation is exactly one adjacent swap of two **nonempty contiguous** excursion blocks, with a possibly unchanged prefix and suffix. There are exactly $\binom{n+1}{3}=\binom{p-1}{3}$ such permutations.

**Rank reconstruction.** For this permutation,
$$
r_1=1+S_{i-1},\qquad
r_2=1+S_{i-1}+S_{c-1}-S_{k-1},\qquad
r_3=1+S_{c-1}.
\tag{4}
$$
Define the inverse $S^{-1}$ on the finite image $\{S_0,\ldots,S_n\}$. Then all three cut labels are recovered *solely* from the rank triple and the genuine Farey gap counts:
$$
\boxed{
\begin{aligned}
i&=1+S^{-1}(r_1-1),\\
k&=1+S^{-1}(r_1+r_3-r_2-1),\\
c&=1+S^{-1}(r_3-1).
\end{aligned}}
\tag{5}
$$
Conversely, an increasing integer rank triple is realizable by a three-defect full-excursion permutation **if and only if** each of $r_1-1$, $r_1+r_3-r_2-1$, and $r_3-1$ belongs to $\{S_0,\ldots,S_n\}$. The recovered indices are automatically strictly ordered by $r_1<r_2<r_3$; inserting them in (3) yields the unique realization. In particular, fixing $p$ and the exact three defective *ranks* fixes the entire denominator word, reconstructed grid, all local index values, transport vector, quadratic energy, and full sine spectrum. Fixing only the three *index values*, as in FD-327, does not.

## 2. Proof of classification and rank inversion

Adjoin sentinel excursion labels $\sigma(0)=0$, $\sigma(n+1)=n+1$ to the permutation word. FD-320, equation (7), proves that a boundary between consecutive labels $j,h$ has an integer Hall--Shiu index **exactly when** $h=j+1$. Hence exactly three noninteger indices are exactly three breaks in the augmented word, separating it into four maximal increasing-by-one runs.

The first run must be $(0,1,\ldots,i-1)$ and the last $(c,\ldots,n,n+1)$. The two nonempty middle runs partition the remaining consecutive integer interval $\{i,\ldots,c-1\}$. Each run is itself consecutive and increasing; therefore their underlying integer intervals are adjacent. If they occurred in increasing order they would join into one uninterrupted run, contradicting the assumed three breaks. They must occur in reverse order, uniquely as $(k,\ldots,c-1)$ followed by $(i,\ldots,k-1)$ for $i<k<c$. This proves (3), its uniqueness, and the $\binom{n+1}{3}$ count. Conversely, the three displayed inter-run boundaries are genuine breaks, so every such triple has exactly three noninteger indices.

The initial outer Farey edge accounts for one gap. The unchanged prefix contributes $S_{i-1}$ gaps, so the first changed junction has rank $r_1=1+S_{i-1}$. The moved $B=E_k\cdots E_{c-1}$ contributes $L_B=S_{c-1}-S_{k-1}$ gaps before the second changed junction, whereas the moved $A=E_i\cdots E_{k-1}$ contributes $L_A=S_{k-1}-S_{i-1}$ gaps before the third. This gives (4), hence
$$
S_{i-1}=r_1-1,\qquad
S_{k-1}=r_1+r_3-r_2-1,\qquad
S_{c-1}=r_3-1.
\tag{6}
$$
Strict monotonicity of $S$ proves (5) and the if-and-only-if realizability certificate without any appeal to asymptotics.

## 3. Exact energy from the rank signature

For a valid triple, set
$$
L_B=r_2-r_1,\quad L_A=r_3-r_2,\quad
w_A=\frac{L_A}{N}-\frac{k-i}{p},\quad
w_B=\frac{L_B}{N}-\frac{c-k}{p}.
\tag{7}
$$
As in FD-320, the exact rearranged discrepancy decomposition is $D^\sigma=P_\sigma D+v$: the displacement is $+w_A$ on the $L_B$ ranks of the moved $B$ block (ranks $r_1+1,\ldots,r_2$), $-w_B$ on the $L_A$ ranks of the moved $A$ block (ranks $r_2+1,\ldots,r_3$), and zero on the other interior ranks. Therefore the **finite exact** transport potential, entirely computable from $p$, the original $\ell_j$, and the three defect ranks, is
$$
\boxed{
T_p(r_1,r_2,r_3)
=(r_2-r_1)
 \left(\frac{r_3-r_2}{N}-\frac{k-i}{p}\right)^2
+(r_3-r_2)
 \left(\frac{r_2-r_1}{N}-\frac{c-k}{p}\right)^2.
}
\tag{8}
$$
The reassembled energy satisfies
$$
E_p^\sigma-E_p=T_p+2\langle P_\sigma D,v\rangle,\qquad
\left|\sqrt{E_p^\sigma}-\sqrt{T_p}\right|\le\sqrt{E_p},
\tag{9}
$$
and the sine transform has exact $\ell^2$ error $E_p$ against the transform of $v$, by FD-320. In particular the reconstruction claim is finite and exact, *not* a new RH-critical discrepancy bound; only the uniform residual estimate $E_p=o(1)$ uses the previous PNT argument.

## 4. Independent falsification and prior-art boundary

For each $p=7,11,13$, independent exact-rational enumeration of the genuine Farey grid, original directed denominator-edge words, and **all** three-break reassemblies verified: precisely three noninteger indices at the ranks (4); no duplicate rank signatures; exact reconstruction (5); unchanged directed edge inventory and endpoint $1$; and pointwise $D^\sigma=P_\sigma D+v$ with transport (8). The numbers of enumerated permutations were respectively $20,120,220$, matching $\binom{p-1}{3}$. For example at $p=11$, $N=42$, $(i,k,c)=(1,5,10)$ yields defective ranks $(1,22,41)$, $T_p=520/2541$, and exact $E_p^\sigma-E_p=23057/160083$. These finite checks independently test the indexing and boundary conventions; the theorem follows from the preceding combinatorial proof.

Adjacent-block swaps, transposition distance, and breakpoint terminology are classical in permutation/genome-rearrangement combinatorics; for example, G. Fertin, A. Labarre, I. Rusu, E. Tannier and S. Vialette, *Combinatorics of Genome Rearrangements*, MIT Press (2009), and the related discussion in L. Bulteau, G. Fertin and I. Rusu, *Sorting by Transpositions Is Difficult*, SIAM Journal on Discrete Mathematics **26** (2012), DOI 10.1137/110851390. No novelty is claimed for this elementary permutation classification itself. Hall--Shiu's classical Farey index and the local index formula are already anchored in SOURCES.md and FD-320. The specific addition here is the **exact rank-position identifiability criterion and Farey transport formula** at the sharp three-defect boundary.

The scope is only permutations of **whole labeled prime-Farey excursions**; reconstructed labels at defective joins need not be actual reduced denominators, so these controls are not second genuine Farey sequences. At four or more defects the two-interior-run argument fails; this result asserts neither injectivity for larger defect counts nor a RH estimate. It rules out extending FD-327's same-prime ambiguity to controls that also fix the three **exact defect ranks**, and shows why that stronger matching condition is already a degenerate null at the minimal-defect boundary rather than an intermediate coercive geometric constraint.
