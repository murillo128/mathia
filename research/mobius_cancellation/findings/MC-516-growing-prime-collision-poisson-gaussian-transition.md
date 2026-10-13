# MC-516 — Growing-prime collision counts pass from sparse Poisson to Gaussian behavior

**Evidence:** EXACT-DERIVED · CLASSICAL-MONOCHROMATIC-EDGE-SPECIALIZATION · PRIOR-ART-AUDITED · NON-RH · NO-GENERAL-NOVELTY-CLAIM.

## Claim and exact scope

In the **independent-residue control** of MC-514/MC-515 (not the arithmetic prime array), take independent uniform labels
\(X_1,\ldots,X_n,Y_1,\ldots,Y_n\in\{1,\ldots,m\}\), with \(m=\ell-1\ge2\) for an odd auxiliary prime \(\ell\nmid h\). The sign in \(\ell\mid q+r\) is absorbed into the right labels. Put

\[
T_{n,m}=\sum_{i=1}^n\sum_{j=1}^n\mathbf1_{\{X_i=Y_j\}},
\qquad \lambda_{n,m}=\frac{n^2}{m}.
\]

Let \(m=m(n)\to\infty\) and \(n\to\infty\). Then the following regimes exhaust all convergent limits of the mean parameter:

1. If \(\lambda_{n,m}\to0\), then \(\Pr(T_{n,m}=0)\to1\).
2. If \(\lambda_{n,m}\to c\in(0,\infty)\), then \(T_{n,m}\Rightarrow \operatorname{Poisson}(c)\).
3. If \(\lambda_{n,m}\to\infty\), then
   \[
   \boxed{\frac{T_{n,m}-n^2/m}
   {n\sqrt{(m-1)/m^2}}\Rightarrow N(0,1).}
   \tag{1}
   \]

For every finite \(n,m\), \(\mathbb E T_{n,m}=n^2/m\) and
\(\operatorname{Var}(T_{n,m})=n^2(m-1)/m^2\), as already proved in MC-515. The Gaussian conclusion (1) uses **both** \(m\to\infty\) and \(\lambda_{n,m}\to\infty\); it does not replace the non-Gaussian fixed-\(m\) limit of MC-515.

This specialization is covered by the general uniform-graph-coloring theorems of Bhattacharya, Diaconis and Mukherjee (MC-S63, Theorems 1.1–1.2), applied to the graph \(K_{n,n}\). The proof below derives the special case explicitly and gives an exact fluctuation certificate for the conditional variance.

## Sparse regimes: factorial moments

The zero regime follows immediately from
\(\Pr(T_{n,m}>0)\le\mathbb ET_{n,m}=\lambda_{n,m}\).

Suppose now \(\lambda_{n,m}\to c\in(0,\infty)\), hence \(m\asymp n^2\). For each fixed \(k\ge1\), expand the falling factorial \((T_{n,m})_k\) over ordered \(k\)-tuples of **distinct** edges of the complete bipartite graph \(K_{n,n}\). If the selected simple edge graph has \(v\) incident vertices and \(b\) nonempty connected components, MC-514's edge-consistency argument yields

\[
\Pr(\text{all selected edges match})=m^{-(v-b)}.
\tag{2}
\]

There are \(O_k(n^v)\) embeddings of each fixed pattern. Since \(m\asymp n^2\), its total contribution is \(O_k(n^{2b-v})\). Every component contains at least two vertices, with equality only for an isolated edge. Thus a pattern containing any nontrivial component (at least three vertices) contributes \(o(1)\). For \(k\) disjoint edges there are exactly \((n)_k^2\) ordered choices, each with matching probability \(m^{-k}\), so

\[
\mathbb E(T_{n,m})_k
=\frac{(n)_k^2}{m^k}+o(1)\longrightarrow c^k.
\tag{3}
\]

These are the factorial moments of \(\operatorname{Poisson}(c)\), proving the second regime. The argument explicitly accounts for cycle-induced dependence rather than assuming independent edges.

## Dense regime: exact conditional-variance certificate

Write \(A_a=\#\{i:X_i=a\}\), \(U_a=A_a-n/m\). Conditionally on all the left labels, the right contributions are independent:
\[
T_{n,m}-\frac{n^2}{m}
=\sum_{j=1}^nD_j,\qquad
D_j=A_{Y_j}-\frac nm,\qquad
\mathbb E(D_j\mid X)=0.
\tag{4}
\]

Their conditional total variance is
\[
V_X=\operatorname{Var}(T_{n,m}\mid X)
=\frac nm\sum_{a=1}^m\left(A_a-\frac nm\right)^2.
\tag{5}
\]

For independent uniform \(X_i\), the occupancy identity
\(\sum_aA_a^2=n+2\sum_{i<j}\mathbf1_{\{X_i=X_j\}}\)
and pairwise independence of distinct equality indicators (including shared-vertex pairs) give
\[
\mathbb EV_X=\sigma_{n,m}^2=\frac{n^2(m-1)}{m^2},
\qquad
\operatorname{Var}(V_X)=
\frac{2n^3(n-1)(m-1)}{m^4}.
\tag{6}
\]
In particular the following is **exact**, not asymptotic:
\[
\boxed{\frac{\operatorname{Var}(V_X)}
{(\mathbb EV_X)^2}
=\frac{2(n-1)}{n(m-1)}.}
\tag{7}
\]
Consequently \(V_X/\sigma_{n,m}^2\to1\) in \(L^2\) whenever \(m\to\infty\).

It remains to control large conditional increments rather than infer normality from variance concentration alone. A uniformly chosen occupancy \(A_{Y_1}\), averaged also over \(X\), has the \(\operatorname{Binomial}(n,1/m)\) law. Setting \(v_m=(m-1)/m^2\), its exact centered fourth moment is
\[
\mathbb E D_1^4
=3n^2v_m^2+nv_m(1-6v_m)
\le 3n^2/m^2+n/m.
\tag{8}
\]
It follows that
\[
\frac{\mathbb E\big[\sum_{j=1}^n\mathbb E(D_j^4\mid X)\big]}
{\sigma_{n,m}^4}
\le C\left(\frac{m}{n^2}+\frac1n\right)
=C\left(\frac1{\lambda_{n,m}}+\frac1n\right)\to0.
\tag{9}
\]
The nonnegative conditional Lyapunov ratio therefore tends to zero in probability by Markov's inequality, and (7) supplies asymptotically unit conditional variance after deterministic normalization by \(\sigma_{n,m}\). The conditional triangular-array central limit theorem, followed by bounded convergence of conditional characteristic functions in probability, proves (1).

## Fourth moment check and transition boundary

MC-515's exact fourth-moment formula holds for every \(m,n\). In the growing-\(m\) regime it gives
\[
\mathbb E\left(\frac{T_{n,m}-n^2/m}
{n\sqrt{(m-1)/m^2}}\right)^4
=3+\frac{m^2-6m+6}{(m-1)n^2}
+\frac6{m-1}\left(1-\frac1n\right)^2.
\tag{10}
\]

When \(\lambda_{n,m}\to c\in(0,\infty)\), (10) tends to \(3+1/c\), as expected for a centered, standardized Poisson variable. When \(\lambda_{n,m}\to\infty\), it tends to \(3\), consistent with the Gaussian theorem. The normalized rectangle contribution \(6(1-1/n)^2/(m-1)\) vanishes as \(m\to\infty\), even though individual rectangle constraints remain perfectly dependent. Fourth-moment agreement alone is **not** used as the proof of the CLT.

Independent exact enumeration over all labelings confirms (6)–(7) for \((m,n)=(2,1),(2,2),(2,3),(2,4),(3,2),(3,3),(4,2),(4,3)\); these checks are finite diagnostics, not asymptotic evidence.

## Prior art, interpretation, and boundary

Bhattacharya–Diaconis–Mukherjee (2017), MC-S63, established the general Poisson and Gaussian color-collision limit theorems, so neither limiting law nor the general mechanism is claimed as new. The specialization here is the explicit \(K_{n,n}\) proof, the exact identity (7), and the reconciliation of MC-515's fixed-\(m\) rectangle excess with the growing-\(m\) transition.

The prime interpretation additionally requires \(m=\ell-1\) along odd primes \(\ell\), and the left/right source-prime sets must be disjoint for this independent-label control. **Actual prime residues are not independent uniform samples**, and first-exit source weights, local masks across varying primes, and possibly signed/complex coefficients are not represented in \(T_{n,m}\). The result supplies no transfer from this control to a deterministic estimate for \(M(x)=\sum_{n\le x}\mu(n)\), no new zero-free region, and no RH implication. It does, however, rule out using the fixed-prime non-Gaussian phenomenon of MC-515 as an unconditional obstruction after the number of available residue classes grows: the actual weighted arithmetic pushforward must be analyzed separately.
