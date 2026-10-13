# FD-331 — Exact ranks and values of Farey-index defects reconstruct every prime excursion reassembly

**Status:** EXACT-DERIVED + FINITE-INVERSION-CERTIFICATE + EXACT-ENUMERATION-CHECKS + CONTROL-DESIGN BOUNDARY.

FD-327 shows that defect *values* alone do not control transport; FD-329--FD-330 show that five defect *ranks* alone do not, even at order-one energy scale. Combining both exact coordinates removes this ambiguity **for every number of defects** in the complete prime-Farey excursion-permutation class. The statement is an injectivity and realizability theorem, not a quantitative RH estimate or a robustness theorem at a fixed positive error scale.

## 1. Joint-signature theorem

Fix an odd prime $p\ge7$. Write $n=p-2$, $N=N_p=\sum_{q\le p}\varphi(q)$, and let $E_1,\ldots,E_n$ be the complete directed denominator-$p$ excursions in $F_p$ as in FD-320. Let $\ell_j>0$ be their actual gap counts, and set
$$
S_0=0,\qquad S_j=\sum_{h=1}^{j}\ell_h\quad(1\le j\le n),\qquad S_n=N-2.
\tag{1}
$$
For a permutation $\sigma$ of the whole excursions, keep the original outer Farey edges and compute its Hall--Shiu indices at the *inherited labeled denominator interfaces*, as in FD-320. Let
$$
\mathcal J_p(\sigma)=
\big((r_1,\nu_1),\ldots,(r_m,\nu_m)\big),\qquad
1\le r_1<\cdots<r_m\le N-1,
\tag{2}
$$
contain **all and only the noninteger indices**, with their exact rank positions and exact values.

**Theorem.** For fixed $p$ and the genuine excursion counts $(\ell_j)$, the map
$$
\sigma\longmapsto\mathcal J_p(\sigma)
\tag{3}
$$
is injective on **all** $(p-2)!$ whole-excursion permutations, with no bounded-defect, reflection, or asymptotic hypothesis. Moreover, (4)--(7) below give a deterministic finite inverse and a necessary-and-sufficient realizability test for a proposed signature. Thus the same exact joint signature fixes the entire inherited directed-edge word, the reassembled rank grid, FD-320's complete transport vector $v^\sigma$, its energy $T_p(\sigma)$, the reconstructed Franel energy, and all its sine coefficients.

This does **not** say that defective ranks alone or values alone are sufficient. It applies to the labeled-edge reassembly class, not to competing genuine Farey sequences.

## 2. Explicit inverse and realization certificate

Let $I_p(a)=[a^{-1}]_p$ denote the integer representative in $\{1,\ldots,p-1\}$, for $1\le a\le p-1$. It is a bijection of this set. Put
$$
d_i=p(\nu_i-1)\in\mathbb Z\setminus\{0\}.
\tag{4}
$$
For a valid signature, the finite index identity of FD-320, equation (7), says that a boundary between a preceding excursion label $j$ and a following label $k$ satisfies
$$
d_i=I_p(j+1)-I_p(k);
\quad
j\in\{0,\ldots,n\},\quad k\in\{1,\ldots,n+1\}.
\tag{5}
$$
The fictitious labels $0,n+1=p-1$ are the left and right sentinels. The nonzero $d_i$ are exactly the breaks between maximal increasing-by-one runs in the augmented label word.

If $m=0$, the word must be the identity $(1,\ldots,n)$. Otherwise, the first run contains the left sentinel and a possibly empty unchanged prefix $E_1,\ldots,E_a$. Its endpoint $a$ is obtained **solely from the first rank**:
$$
a=S^{-1}(r_1-1),
\tag{6}
$$
where $S^{-1}$ is defined only on $\{S_0,\ldots,S_n\}$; reject if the argument lies outside this image.

Now recursively decode each break. Knowing the final label $j$ of the preceding run (initially $j=a$), compute $b=I_p(j+1)-d_i$. Reject unless $b\in\{1,\ldots,p-1\}$, and set $k=I_p^{-1}(b)$; the *start label of the next run* is thereby uniquely fixed. Its gap length is
$$
L_i=\begin{cases}
r_{i+1}-r_i,&i<m,\\
N-1-r_m,&i=m.
\end{cases}
\tag{7}
$$
For $i<m$, require $1\le k\le n$ and determine the next run's last label $e$ by the **unique**, if it exists, solution $e\in\{k,\ldots,n\}$ of $S_e-S_{k-1}=L_i$. Append the run $(k,k+1,\ldots,e)$ and continue with $j=e$. Positivity of every $\ell_h$ guarantees uniqueness of this endpoint.

At the final break $i=m$, if $L_m>0$ require $k\le n$ and $S_n-S_{k-1}=L_m$, then append the terminal suffix $(k,\ldots,n)$. If $L_m=0$, require $k=n+1$ (the right sentinel with no excursions after the last break). Finally require that the reconstructed prefix and all appended runs contain **every** label $1,\ldots,n$ exactly once and that their recomputed defect signature equals (2). Reject otherwise. These conditions are a necessary-and-sufficient finite realization certificate.

**Proof.** A zero-defect interface is exactly an increasing-by-one label adjacency, by (5) and the injectivity of $I_p$. The maximal runs are therefore contiguous increasing integer-label intervals. The first run is the untouched prefix (possibly empty), so its gap length is $r_1-1$ and strict increase of $S$ gives (6). At each succeeding break the already reconstructed preceding label $j$ and the measured $d_i$ determine $I_p(k)$ by (5), hence determine $k$ uniquely. Before the next break the word traverses a whole consecutive-label run, whose positive gap counts sum to $L_i$; strict increase of $S$ determines its endpoint uniquely. Induction reconstructs every run and the terminal suffix. Every valid permutation must follow these steps, proving injectivity. Conversely, passing the stated cover, endpoint and recomputed-signature checks constructs an admissible whole-excursion permutation realizing precisely the proposed data. No asymptotic assumption enters.

## 3. Falsification, quantization, and boundaries

An independent enumerator generated the true Farey grid and its excursion gap counts via the classical Farey recurrence, formed the complete labeled defect signature using (5), and reconstructed permutations **only from that signature** using the inverse above. It recovered every one of the $5!=120$ permutations for $p=7$ and every one of the $9!=362880$ permutations for $p=11$, plus $10\,000$ independently sampled permutations each for $p=13,17$. For example at $p=7$, $\ell=(4,3,2,3,4)$, the reassembly $(2,4,1,3,5)$ has ranks $(1,4,7,11,13)$ and integer defect numerators $d=(-3,3,2,-1,-1)$; the inverse recovers that word exactly. The finite checks probe the sentinel, rank, and inverse conventions but are not substitutes for the proof.

Every noninteger interface value belongs to the lattice $1+p^{-1}\mathbb Z$. Thus, **with exactly matched defect ranks**, two valid joint signatures whose corresponding values differ by **strictly less than $1/p$** are in fact identical, hence recover the same word and the same energy. This is merely lattice-scale exact rigidity. It supplies no uniform inverse stability under errors of order $1/p$ or larger, nor under shifted or missing defect ranks. FD-319 and FD-330 are warnings against promoting exact coding to a coercive estimate for approximate signatures.

The Hall--Shiu index is classical: R. R. Hall and P. Shiu, *The index of a Farey sequence*, Michigan Math. J. **51** (2003), 209--223, DOI 10.1307/mmj/1049832901. The index/neighbor coding is already expressed as (5) in FD-320; maximal consecutive runs and their encoding are elementary permutation combinatorics (see Fertin et al., *Combinatorics of Genome Rearrangements*, MIT Press, 2009). The novelty claim is **only the Mathia-line exact joint-rank-and-value recovery certificate for this specified control family**, not a new Farey-index identity or a general permutation-coding theorem. Targeted prior-art checks on Farey index statistics, recurrence coding and breakpoint reconstruction did not identify this exact specialized statement, but cannot establish priority.

These reassemblies are *not* alternative genuine Farey sequences: a denominator label inherited across a defective stitch need not be the true reduced denominator of the reconstructed rational vertex. The certificate requires exact knowledge of $p$ and of the original genuine $\ell_j$; if these inputs are unknown or perturbed, the theorem does not apply. In particular, resolving this exact identifiability question does not yield a new Franel--Landau discrepancy bound, a new exclusion of off-critical zeta zeros, or progress toward RH without an additional source-natural arithmetic estimate.
