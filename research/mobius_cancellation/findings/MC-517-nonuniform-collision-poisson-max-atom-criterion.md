# MC-517 — A vanishing largest residue atom is exactly the Poisson threshold for nonuniform two-sample collisions

**Evidence:** EXACT-DERIVED · CLASSICAL-CHEN–STEIN-SPECIALIZATION · NEGATIVE/OBSTRUCTION · PRIOR-ART-AUDITED · NO-GENERAL-NOVELTY-CLAIM · NON-RH.

## Precise claim

Extend only the **independent-residue control** of MC-514–MC-516. For each n let p=(p_a) be an arbitrary probability law on a finite residue-label set, possibly changing with n. Let X_1,...,X_n and Y_1,...,Y_n be mutually independent, each with this same law, and set

\[
T_n=\sum_{i,j=1}^n {\bf1}_{\{X_i=Y_j\}},\qquad
s_r=\sum_a p_a^r,\qquad p_*=\max_a p_a,\qquad
\lambda_n=n^2s_2.
\]

If n grows and \(\lambda_n\to c\in(0,\infty)\), then

\[
\boxed{T_n\Rightarrow\operatorname{Poisson}(c)
       \quad\Longleftrightarrow\quad n p_*\longrightarrow0.}\tag{1}
\]

The class count may vary with n, and no approximate-uniformity hypothesis is required. The condition is sharp for this equal-law, two-independent-sample model; it is **not** asserted for distinct left and right laws or the actual deterministic residues of primes.

For every n there are also exact identities

\[
\boxed{\mathbb ET_n=n^2s_2,\quad
\operatorname{Var}(T_n)=n^2(s_2-s_2^2)
 +2n^2(n-1)(s_3-s_2^2).}\tag{2}
\]

Thus the same-label interactions sharing one source vertex are governed by the cubic mass \(s_3\), which is invisible to the mean \(s_2\) alone.

## Sufficiency: local-dependence Poisson bound

For the edge indicators \(I_{ij}={\bf1}_{\{X_i=Y_j\}}\), use the dependency neighborhood of edges sharing a left or right vertex, including the edge itself. Disjoint-vertex sets of edges depend on disjoint independent source variables. An edge has success probability \(s_2\); two distinct edges sharing a vertex have joint success probability \(s_3\). The Arratia–Goldstein–Gordon Chen–Stein neighborhood quantities (MC-S64) therefore are exactly

\[
b_1=n^2(2n-1)s_2^2,\qquad
b_2=2n^2(n-1)s_3,\qquad b_3=0.
\]

In the usual convention \(d_{\rm TV}=\sup_A|P(T_n\in A)-P(Z\in A)|\), their theorem yields, in particular, the safe bound

\[
d_{\rm TV}\bigl(\mathcal L(T_n),\operatorname{Poisson}(\lambda_n)\bigr)
 \le 2\bigl[n^2(2n-1)s_2^2+2n^2(n-1)s_3\bigr].\tag{3}
\]

Since \(s_3\le p_*s_2\), the assumed \(\lambda_n=O(1)\) makes the right side \(O(1/n+n p_*)\). If \(n p_*\to0\), this goes to zero, and \(\lambda_n\to c\) proves the forward implication of (1).

## Necessity: exact variance and uniform integrability

The covariance of two distinct matching edges is zero if they share no vertex, and \(s_3-s_2^2\) when they share exactly one. There are \(n^2(n-1)\) unordered distinct edge-pairs with one shared vertex, giving (2).

Convergence in law alone does not imply variance convergence, so a moment bound is essential. For any fixed positive integer k, expand \(T_n^k\) over ordered k-tuples of edges, allowing repetitions. For a chosen underlying simple bipartite graph with v incident vertices and connected components of vertex sizes \(v_1,\dots,v_b\), the event that all its selected edges match has probability \(\prod_{\alpha=1}^b s_{v_\alpha}\). Each \(v_\alpha\ge2\), and

\[
s_r\le s_2^{r/2}\quad(r\ge2).
\]

Because \(n^2s_2=O(1)\), each fixed graph pattern contributes at most \(O_k(n^v s_2^{v/2})=O_k(1)\), and there are finitely many patterns for fixed k. In particular, \(\sup_n\mathbb ET_n^4<\infty\), so the family \(T_n^2\) is uniformly integrable.

If \(T_n\Rightarrow\operatorname{Poisson}(c)\), then \(\operatorname{Var}(T_n)\to c\). In (2), the first term tends to c, while \(n^3s_2^2=O(n^{-1})\), hence

\[
n^3(s_3-s_2^2)\to0,\qquad n^3s_3\to0.
\]

But \(p_*^3\le s_3\). Consequently \(np_*\le(n^3s_3)^{1/3}\to0\), proving the reverse implication. The cubic mass is therefore a **necessary** as well as a sufficient sparsity certificate under the stated fixed-positive-mean scaling.

## Total-variation-to-uniform counterexample

Even convergence of the label laws to uniform in total variation does **not** guarantee (1). Fix a>0 and take \(m_n=n^2\) labels, one exceptional label with

\[
p_0=\frac an,\qquad
p_j=\frac{1-a/n}{n^2-1}\quad(1\le j<n^2).
\]

For sufficiently large n these are probabilities and, writing \(u_n\) for the uniform law on these labels,

\[
d_{\rm TV}(p,u_n)=\frac an-\frac1{n^2}\to0,\qquad
n^2s_2\to a^2+1,\qquad np_*\to a.
\]

Let U_n and V_n count exceptional-label occurrences on the two sides. They converge jointly to independent \(U,V\sim\operatorname{Poisson}(a)\). Given \((U_n,V_n)\), the remaining draws on the two sides are uniform on the other \(n^2-1\) labels, with sample sizes \(n-U_n,n-V_n=n-O_{\mathbb P}(1)\). The same sparse factorial-moment argument as MC-516, uniformly for bounded exceptional counts, gives an asymptotically independent \(Z\sim\operatorname{Poisson}(1)\) for their mutual collisions. Therefore

\[
\boxed{T_n\Rightarrow UV+Z, \qquad
\mathbb E(UV+Z)=a^2+1,\quad
\operatorname{Var}(UV+Z)=a^2+2a^3+1.}\tag{4}
\]

For a>0 this limit is not Poisson despite the vanishing total-variation distance from the uniform input law. The issue is the **n-dependent scale of the largest class**, not unweighted proximity of one label law to another.

As a finite algebraic check, exact rational enumeration with p=(1/2,1/3,1/6) yields (mean, variance) (7/18,77/324), (14/9,29/27), and (7/2,97/36) for n=1,2,3 respectively, agreeing with (2). These checks do not prove the asymptotic statement.

## Prior art, arithmetic boundary and consequence

Dependency-neighborhood Chen–Stein theory is classical (MC-S64), as is Poisson convergence for dissociated comparisons of independent but nonidentically distributed observations (MC-S65); occupancy and collision Poisson approximation have a substantial prior literature. Equation (1), (2), and (4) are derived here for the exact balanced bipartite matching observable of MC-514–MC-516. **No general probabilistic novelty is claimed.** The mathematical delta is a sharp replacement for MC-516's uniform-color parameter: in this equal-law nonuniform control, the second moment \(s_2\) alone does not classify the sparse limit; the heavy-atom scale \(np_*\) is decisive.

For the actual relation \(\ell\mid q+r\), neither independence of prime residues nor equality of the left and sign-adjusted right source-label laws is justified. Real first-exit coefficients are weighted and may be signed/complex before aggregation, and local congruences at different primes interact. Even an actual collision law of the form above would be only a control-model fact, not a bound on \(M(x)\), a zero-free region, or an RH implication. Any arithmetic transfer must first establish a source-specific hypothesis strong enough to control the **actual physical pushforward** and its exceptional atoms.
