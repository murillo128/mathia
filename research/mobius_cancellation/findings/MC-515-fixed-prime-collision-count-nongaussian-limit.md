# MC-515 — Fixed-prime collision counts match binomial variance but have a non-Gaussian limit

**Evidence:** EXACT-DERIVED · CLASSICAL-TWO-SAMPLE-U-STATISTIC-SPECIALIZATION · NEGATIVE/OBSTRUCTION · PRIOR-ART-AUDITED · NO-GENERAL-NOVELTY-CLAIM · NON-RH.

## Claim and exact scope

Use the **independent-residue control**, not the actual prime array, of MC-514: fix an odd auxiliary prime \(\ell\nmid h\), put \(m=\ell-1\ge2\), and independently choose \(X_1,\ldots,X_n,Y_1,\ldots,Y_n\) uniformly from the \(m\) nonzero residue classes. Absorb the sign on the right, so that the original condition \(\ell\mid q+r\) becomes \(X_i=Y_j\). Define
\[
I_{ij}=\mathbf1_{\{X_i=Y_j\}},\qquad
T_n=\sum_{i,j=1}^n I_{ij},\qquad
v=\frac{m-1}{m^2},\qquad
Z_n=\frac{T_n-n^2/m}{n\sqrt v}.
\]
For **every** integer \(n\ge1\),
\[
\boxed{\mathbb ET_n=\frac{n^2}{m},\qquad
\operatorname{Var}(T_n)=n^2v,}
\tag{1}
\]
and
\[
\boxed{
\mathbb E Z_n^4=
3+\frac{m^2-6m+6}{(m-1)n^2}
+\frac6{m-1}\left(1-\frac1n\right)^2.}
\tag{2}
\]
The first two moments are exactly those of \(\operatorname{Bin}(n^2,1/m)\). Its standardized fourth moment, however, is only the first two terms of (2); the last, strictly positive term for \(n>1\), comes entirely from four-edge rectangles.

For each **fixed** \(m\ge2\), there is the distributional limit
\[
\boxed{
Z_n\ \xrightarrow{d}\ 
Z_\infty=\frac1{\sqrt{m-1}}\sum_{k=1}^{m-1}G_kH_k,}
\tag{3}
\]
where all the \(G_k,H_k\) are independent standard normals. Its characteristic function and fourth moment are
\[
\boxed{
\mathbb E e^{itZ_\infty}
=\left(1+\frac{t^2}{m-1}\right)^{-(m-1)/2},
\qquad
\mathbb E Z_\infty^4=3+\frac6{m-1}
=3+\frac6{\ell-2}>3.}
\tag{4}
\]
Thus matching all one-edge and two-edge statistics, even exactly, does **not** give the central limit theorem of independent edges.

## Exact fourth-moment derivation

Set \(h_{ij}=I_{ij}-1/m\) and \(S_n=\sum_{i,j}h_{ij}=T_n-n^2/m\). Each edge has \(\mathbb Eh_{ij}=0\), \(\mathbb Eh_{ij}^2=v\), and
\[
\mathbb Eh_{ij}^4=v(1-3v).
\]
Two distinct edges are independent, including when they share one vertex: conditional on that vertex's uniform label, the other endpoint labels are independent and each match probability is \(1/m\). In particular \(\mathbb Eh_e^2h_f^2=v^2\) for \(e\ne f\), proving (1).

Expand \(S_n^4\) as ordered four-tuples of edges. Any term with a vertex incident to exactly one of those edges vanishes by conditioning on its label. The remaining possibilities are: one edge four times (\(n^2\) choices); two distinct edges twice each (\(6\binom{n^2}{2}\) choices); or four distinct edges forming a rectangle (\(24\binom n2^2\) choices). No other simple bipartite four-edge configuration has minimum nonzero vertex degree two.

For a rectangle, every proper subgraph is a forest. By MC-514, all proper subsets of its match indicators behave as independent Bernoulli variables, but the four-edge all-match probability is \(m^{-3}\), not \(m^{-4}\). Therefore
\[
\mathbb E[h_{11}h_{12}h_{21}h_{22}]
=m^{-3}-m^{-4}=\frac{m-1}{m^4}.
\]
Collecting the three nonzero types gives the **exact** finite-sample identity
\[
\mathbb ES_n^4
=n^2v(1-3v)+3n^2(n^2-1)v^2+
24\binom n2^2\frac{m-1}{m^4}.
\tag{5}
\]
Division by \(n^4v^2\) proves (2). In contrast, independent Bernoulli edges have no rectangle contribution in (5).

## Distributional limit

Let \(A_a=\sum_i\mathbf1_{\{X_i=a\}}\), \(B_a=\sum_j\mathbf1_{\{Y_j=a\}}\), and write \(U_a=A_a-n/m\), \(V_a=B_a-n/m\). Then the zero-sum identities \(\sum_aU_a=\sum_aV_a=0\) give
\[
S_n=\sum_{a=1}^mA_aB_a-\frac{n^2}{m}
=\sum_{a=1}^m U_aV_a.
\tag{6}
\]
The vectors \(U/\sqrt n\) and \(V/\sqrt n\) converge jointly by the independent multinomial central limit theorems to independent centered Gaussian vectors with covariance
\[
\Sigma=\frac1m\left(I_m-\frac1mJ_m\right).
\]
The projector has rank \(m-1\), and on its zero-sum space each limit vector has covariance \(I_{m-1}/m\). The continuous mapping theorem applied to (6), followed by the normalization in \(Z_n\), proves (3). For independent standard normals \(G,H\), conditioning on \(G\) gives \(\mathbb E e^{itGH}=(1+t^2)^{-1/2}\); multiplication over the independent \(m-1\) terms yields (4). Equivalently, the fixed number of surviving residue-class fluctuation modes prevents Gaussianization as \(n\to\infty\).

## Falsification checks and boundaries

Exact enumeration of all \(m^{2n}\) labelings confirms the variance and (2) for \((m,n)=(2,1),(2,2),(2,3),(3,1),(3,2),(3,3),(4,2),(6,2)\). For instance, the standardized fourth moments are \(4\) at \((m,n)=(2,2)\) and \(27/8\) at \((3,2)\), agreeing with (2). When \(n=1\), the rectangle term vanishes and the statistic is one Bernoulli edge; when \(n\) grows with fixed \(m\), (4) gives a non-Gaussian limit. The theorem **does not** assert a limit in the double-scaling regime \(m=m(n)\to\infty\).

The two source vertex sets must be disjoint when the independent-residue model is interpreted as a control for source primes. The real prime residues are not independent draws, nor do the physical first-exit coefficients have equal weight. The actual lower-prime masks combine many auxiliary primes, endpoints, relative states, and potentially signed conductor phases; their fourth-order contributions could cancel after weighting. The limit is consequently **not** a theorem about a random model of \(\mu(n)\), a bound for \(M(x)\), a zero-free result, or an RH implication.

## Prior art, mathematical delta, and consequence

The general non-Gaussian limiting theory for degenerate two-sample U-statistics, including orthogonal-kernel expansions, is classical; see Eagleson (1979), MC-S62. No novelty is claimed for that statistical mechanism, the product-normal law, or general fourth-moment combinatorics. The contribution here is the explicit finite-\(n\) rectangle correction (2)/(5), its fixed-\(\ell\) law (3)/(4), and the exact interpretation for the particular \(\ell\mid q+r\) collision relation in MC-502/514.

MC-514 establishes cycle dependence and spectral block modes. This independent statistical consequence shows why those modes remain visible at the **distributional** level: matching the mean, variance, and all pairwise collision tests does not permit binomial tail estimates or Gaussian high-order approximations. The decisive arithmetic question is still whether the **actual weighted, possibly signed** first-exit source suppresses these rectangle modes after conductor pushforward. Without an independently proved source estimate, this control-model obstruction alone supplies no new Möbius cancellation.
