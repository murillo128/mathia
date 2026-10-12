# MC-514 — The q+r collision relation forces cycle dependence and a block-spectrum obstruction

**Evidence:** EXACT-DERIVED · CLASSICAL-SIGNED-GRAPH-SPECIALIZATION · NEGATIVE/OBSTRUCTION · PRIOR-ART-AUDITED · NO-GENERAL-NOVELTY-CLAIM · NON-RH.

## Claim and exact scope

In the cross-root lower-prime sieve of MC-502, fix an **odd** active auxiliary prime \(\ell\) with \(\ell\nmid h\), and take source primes \(q,r\ne\ell\) within its common sieve range. The two shifted forbidden roots collide precisely when \(\ell\mid q+r\). Write \(m=\ell-1\), and consider disjoint finite sets of source primes \(Q,R\), with \(q<r\) for every tested pair, so their roles can be represented by two distinct vertex sets. Define
\[
K_{q,r}=\mathbf 1_{\ell\mid q+r}\qquad(q\in Q,\ r\in R).
\tag{1}
\]
There are two exact, connected obstructions to treating these pair collisions as independent.

**Deterministic rectangle closure.** For distinct \(q_1,q_2\in Q\) and \(r_1,r_2\in R\),
\[
K_{q_1,r_1}=K_{q_1,r_2}=K_{q_2,r_1}=1
\quad\Longrightarrow\quad
K_{q_2,r_2}=1.
\tag{2}
\]
Indeed the first three congruences force \(q_1\equiv q_2\equiv-r_1\equiv-r_2\pmod\ell\). This is a statement about the actual prime residues; no random approximation is involved.

**Exact independent-residue control.** Replace *each distinct source prime* in these disjoint vertex sets by an independent uniform residue in \(\mathbf F_\ell^\times\). For any simple bipartite tested-edge graph \(H=(V,E)\), with \(c(H)\) connected components and cycle rank \(\beta(H)=|E|-|V|+c(H)\), the probability that *every* tested edge collides is
\[
\boxed{\Pr(K_e=1\ \forall e\in E)=m^{-|V|+c(H)}
       =m^{-|E|+\beta(H)}.}
\tag{3}
\]
The indicators on a forest are jointly independent Bernoulli variables with parameter \(1/m\); distinct individual edges are pairwise independent even when they share a vertex. But a bipartite cycle creates a redundant condition. In particular, for a four-edge rectangle,
\[
\boxed{\Pr(\text{all four})=m^{-3},\qquad
       \Pr_{\mathrm{independent\ edges}}(\text{all four})=m^{-4}.}
\tag{4}
\]
Thus *pairwise* agreement with a random-edge model does not validate its four-point or dense-block predictions.

The deterministic matrix \(K\) has another exact property. Write
\[
A_a=\#\{q\in Q:q\equiv a\pmod\ell\},\qquad
B_b=\#\{r\in R:r\equiv b\pmod\ell\}
\quad(a,b\in\mathbf F_\ell^\times).
\]
After permuting rows and columns by residue, \(K\) is a direct sum of all-ones blocks
\[
\boxed{K\simeq\bigoplus_{a\in\mathbf F_\ell^\times}
             J_{A_a,B_{-a}}.}
\tag{5}
\]
Its nonzero singular values, with multiplicity, are precisely
\[
\sqrt{A_a B_{-a}}\qquad(A_a B_{-a}>0).
\tag{6}
\]
The rank is the number of classes with \(A_aB_{-a}>0\). If the two sides have exactly \(n>0\) primes in every nonzero residue class, so that \(|Q|=|R|=N=mn\), then
\[
K\simeq I_m\otimes J_n,\qquad
\boxed{\left\|K-\frac1mJ_{N,N}\right\|_{\mathrm{op}}=n
       =\|K\|_{\mathrm{op}}.}
\tag{7}
\]
Hence even **perfect class balance** does not remove the nontrivial block singular modes. The equality in (7) is an exact *balanced-residue control*, not an assertion that an actual finite prime source realizes such exact counts.

## Derivation

For (3), fix a connected component of \(H\), choose a root residue \(x\in\mathbf F_\ell^\times\), and propagate the edge equations \(X_u+X_v=0\). Every neighbour must have residue \(-x\), every vertex at even distance must have \(x\), and every vertex at odd distance must have \(-x\). Bipartiteness makes this assignment consistent around **all** cycles, so each component admits exactly \(m\) assignments. Across all \(c(H)\) components there are \(m^{c(H)}\) satisfying assignments among \(m^{|V|}\) equiprobable assignments, proving (3). For a forest, expose vertices outward from rooted components: each new vertex is uniform conditional on those previously exposed, and its edge equation succeeds with conditional probability \(1/m\). Repeating for any combination of satisfied/unsatisfied tree edges proves *joint* independence, not merely the all-success probability.

Equation (5) holds because a row of residue \(a\) has ones exactly at columns of residue \(-a\). Each \(J_{A_a,B_{-a}}\) has rank one and singular value \(\sqrt{A_aB_{-a}}\), proving (6). In the balanced case, reorder columns so that opposite residue classes are paired. Then
\[
K-\frac1mJ_{N,N}
=\left(I_m-\frac1mJ_m\right)\otimes J_n .
\]
The first factor is the orthogonal projector onto the zero-sum class directions, with operator norm one for \(m\ge2\), while \(J_n\) has operator norm \(n\). This proves (7).

The number of four-cycles of ones in an arbitrary actual \(K\), counted as unordered choices of two rows and two columns, is exactly
\[
\boxed{\#C_4(K)=\sum_{a\in\mathbf F_\ell^\times}
       \binom{A_a}{2}\binom{B_{-a}}{2}.}
\tag{8}
\]
For balanced classes this is \(m\binom n2^2\). At fixed \(m\), its ratio to the total \(\binom{mn}{2}^2\) candidate rectangles tends to \(m^{-3}\) as \(n\to\infty\), rather than the \(m^{-4}\) rate of an independent-edge Bernoulli model. This makes the cycle obstruction visible even when every marginal class count is balanced.

## Stress tests and limits

Direct enumeration of all \(m^4\) labelings of a four-vertex rectangle gives probabilities \(1/8,\ 1/64,\ 1/216\) for \(\ell=3,5,7\), respectively, exactly \(m^{-3}\). For \(n=3\), direct singular-value computation of the balanced matrix gives centered norm \(3\) and centered rank \(m-1\) for the same three primes. These checks supplement, but are not required for, the proofs.

For \(\ell=2\), \(m=1\) and all nonzero-residue collisions are automatic, so the nontrivial spectral/cycle distinction is absent; (7) is asserted only for odd \(\ell\). If \(\ell\mid h\), MC-502's two shifted forbidden roots coincide independently of \(q+r\), so the chosen collision indicator does not represent that local sieve case. If the two vertex roles reuse an identical underlying source prime, the independent-residue control must identify that repeated variable rather than artificially sample two copies: the disjoint-set hypothesis avoids this issue.

The matrix result is exact for fixed-\(\ell\) residue incidence, **not** an operator bound on the complete lower-prime mask Gram matrix, its product over varying \(\ell\), or the incomplete conductor-projected first-exit coefficients. Likewise, the graph probability is a matched model, not a theorem that actual primes independently occupy residue classes. Individual and even pairwise collision statistics do not imply high-order independence. None of these equations estimates \(M(x)\), proves a zero-free region, or advances RH directly.

## Prior art and mathematical delta

Harary's cycle-balance criterion (MC-S60) and Zaslavsky's signed-graph framework (MC-S61) supply classical background for the alternating-sign propagation around graph cycles. The counting in (3), residue-block factorization (5), and elementary tensor spectrum (7) are derived here directly; **no novelty is claimed for their abstract graph/matrix content**. The specific delta relative to MC-502 is to make its stated "pairwise, not collective" boundary exact at both four-point and spectral levels for the same arithmetic collision relation \(\ell\mid q+r\).

In particular, replacing the deterministic array of local \(q+r\) collisions with independent edges silently discards the rectangle identity (2). Such a replacement may pass all one-edge and two-edge tests in the independent-residue control yet fail at order four. Perfect equidistribution of the prime residue *marginals* is also insufficient to erase the block modes. Therefore any inference from MC-502's two-row complete-period sieve coherence to a collective dense-row cancellation bound needs extra **source-specific** control; it cannot follow from independent-edge combinatorics or class balance alone.

The next decisive question is whether the actual weighted first-exit source, with lower-prime products, endpoints, conductor phases and relative-state constraints retained, suppresses the material rectangular contributions or their *signed* effect after physical pushforward. The present result does not assert that the elementary fixed-\(\ell\) rectangle obstruction survives every such weighting or creates a large Möbius bias.
