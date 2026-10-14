# MC-518 — Asymmetric residue collisions can converge to Poisson while retaining excess variance

**Evidence:** EXACT-DERIVED · CLASSICAL-CHEN–STEIN-SPECIALIZATION · NEGATIVE/OBSTRUCTION · PRIOR-ART-AUDITED · NO-GENERAL-NOVELTY-CLAIM · NON-RH.

## Claim and precise setting

Extend the independent-residue *control model* of MC-514–MC-517, not the arithmetic prime array. For each \(n\), let \(p=(p_a)\) and \(q=(q_a)\) be possibly different probability laws on the same finite label set. Independently draw \(X_1,\ldots,X_n\) with law \(p\) and \(Y_1,\ldots,Y_n\) with law \(q\), and define

\[
T_n=\sum_{i,j=1}^n\mathbf1_{\{X_i=Y_j\}},
\quad s=\sum_a p_aq_a,\quad
\alpha=\sum_a p_aq_a^2,\quad
\beta=\sum_a p_a^2q_a,\quad
\lambda_n=n^2s.
\]

Then, exactly for every \(n\),

\[
\boxed{\mathbb ET_n=n^2s,\qquad
\operatorname{Var}(T_n)=n^2(s-s^2)
+n^2(n-1)(\alpha+\beta-2s^2).}\tag{1}
\]

If \(n^2s\to c\in(0,\infty)\), the **overlap-cubic criterion**

\[
\boxed{n^3(\alpha+\beta)\longrightarrow0}\tag{2}
\]

is sufficient for \(T_n\to\operatorname{Poisson}(c)\) **in total variation**. Conversely, if \(T_n\) converges to \(\operatorname{Poisson}(c)\) in distribution **and** \(\{T_n^2\}\) is uniformly integrable, then (2) is necessary. In particular, (2) is equivalent to the Poisson limit within families for which second moments are uniformly integrable.

The moment qualification cannot be dropped, even when convergence is in total variation and the means converge. There are explicit unequal laws for which

\[
\boxed{d_{\rm TV}(\mathcal L(T_n),\operatorname{Poisson}(1/2))\to0,
\quad \mathbb ET_n\to1/2,
\quad \operatorname{Var}(T_n)\to3/4.}\tag{3}
\]

Thus MC-517's sharp equal-law largest-atom criterion does not extend to unequal source laws by a moment-converse argument without additional tail control.

## Exact shared-vertex covariance and sufficiency

Two edge indicators with disjoint endpoints are independent. Two distinct edges sharing a left vertex have joint success probability \(\alpha\); those sharing a right vertex have joint success probability \(\beta\). Both covariances are nonnegative:

\[
\alpha-s^2=\operatorname{Var}_{X\sim p}(q_X)\ge0,\qquad
\beta-s^2=\operatorname{Var}_{Y\sim q}(p_Y)\ge0.
\]

Counting the \(n^2(n-1)\) unordered shared-vertex edge pairs proves (1). It also identifies *which* side causes clustering, a distinction absent from the equal-law \(s_3\) formula of MC-517.

For each edge use the dependency neighborhood containing itself and all edges sharing a vertex. The Arratia–Goldstein–Gordon bound (MC-S64) has

\[
b_1=n^2(2n-1)s^2,\quad
b_2=n^2(n-1)(\alpha+\beta),\quad b_3=0,
\]

and in the total-variation convention of MC-517 gives the safe estimate

\[
d_{\rm TV}(\mathcal L(T_n),\operatorname{Poisson}(\lambda_n))
\le2\big[n^2(2n-1)s^2+n^2(n-1)(\alpha+\beta)\big].\tag{4}
\]

Under \(n^2s\to c\), the first term is \(O(1/n)\); (2) makes the second vanish. Continuity of the Poisson law in its parameter proves sufficiency. No individual-edge independence is inferred from pairwise covariance estimates.

For necessity with the stated extra hypothesis, convergence in law plus uniform integrability of \(T_n^2\) implies convergence of first and second moments. Hence (1) and \(n^2s\to c\) force
\(n^3(\alpha+\beta-2s^2)\to0\). Since \(n^3s^2=O(1/n)\), (2) follows. Without uniform integrability this use of the variance is invalid.

## Explicit rare-burst counterexample

For each \(n\ge2\), choose the abstract label set \(\{0,1,\ldots,n^2\}\). Let

\[
p_0=\tfrac12,\qquad p_a=\frac1{2n^2}\ (a\ge1);
\qquad
q_0=n^{-3},\qquad q_a=\frac{1-n^{-3}}{n^2}\ (a\ge1).
\tag{5}
\]

These are probability laws, but intentionally **not equal**. Direct substitution gives

\[
s=\frac1{2n^2}+\frac1{2n^3}-\frac1{2n^5},
\quad n^3\alpha\to0,\quad n^3\beta\to\tfrac14.
\tag{6}
\]

Thus \(\lambda_n\to1/2\) and the exact variance formula (1) yields

\[
\operatorname{Var}(T_n)\to\tfrac12+\tfrac14=\tfrac34.
\tag{7}
\]

Nevertheless the count itself converges to \(\operatorname{Poisson}(1/2)\) in total variation. Let \(U_n=\#\{i:X_i=0\}\sim\operatorname{Bin}(n,1/2)\) and \(V_n=\#\{j:Y_j=0\}\sim\operatorname{Bin}(n,n^{-3})\), independently. Write \(T_n=T_n^{\rm bg}+U_nV_n\), where \(T_n^{\rm bg}\) counts only matches among labels \(1,\ldots,n^2\). The exceptional contribution is absent except on \(\{V_n>0\}\), so

\[
\Pr(T_n\ne T_n^{\rm bg})\le \Pr(V_n>0)\le n^{-2}.
\tag{8}
\]

Conditionally on \((U_n,V_n)=(u,v)\), the nonzero labels on the two sides are independent and uniform on \(n^2\) choices, with sample sizes \(L=n-u\) and \(R=n-v\). Their collision mean is \(LR/n^2\). The rectangular version of (4) has \(b_1=LR(L+R-1)/n^4\) and \(b_2=LR(L+R-2)/n^4\), so its total-variation error is \(O(1/n)\) **uniformly** over \(0\le L,R\le n\). Since \(U_n/n\to1/2\) in probability and \(V_n/n\to0\), the random conditional mean \(LR/n^2\to1/2\) in probability and is bounded by one. Mixing these approximations and using \(d_{\rm TV}(\operatorname{Poi}(a),\operatorname{Poi}(b))\le|a-b|\) proves \(T_n^{\rm bg}\to\operatorname{Poi}(1/2)\) in total variation. Equation (8) proves (3).

The mechanism is a rare **right-side** exceptional draw (\(\Pr(V_n>0)=O(n^{-2})\)) meeting order-\(n\) left-side occurrences of label zero. Its probability vanishes, so it disappears in the distributional limit; its squared contribution remains of constant expected order and survives in the variance. Indeed \(n^3\beta\to1/4\), so the shared-right-vertex term in the Chen–Stein upper bound does not vanish, despite genuine total-variation convergence. This illustrates that the bound is sufficient, not necessary, in this heterogeneous regime.

As a finite algebraic check, exact rational enumeration of all \(5^4\) assignments at \(n=2\) yields \(\mathbb ET_2=11/16\) and \(\operatorname{Var}(T_2)=655/1024\), exactly matching (1). The limiting argument above is analytic; the finite enumeration is only a check.

## Prior art, falsification boundaries, and arithmetic relevance

Local-dependence Chen–Stein bounds are classical (MC-S64); general Poisson convergence for dissociated comparison statistics is classical (MC-S65). Convergence in law without moment convergence, sparse occupancy bursts, and the resulting limitation of second-moment converses are standard probability phenomena. No general probabilistic novelty is claimed. The line-specific delta relative to MC-517 is an **exact unequal-law covariance certificate** and a concrete counterexample showing why its necessity proof cannot simply be recycled when the left and sign-adjusted right source laws differ. In particular, (4) is not a characterization of *all* heterogeneous Poisson limits.

The control model uses a freely chosen abstract label cardinality and independent draws; (5) does not assert that \(n^2+1\) is the number of nonzero residue classes of an auxiliary prime, nor that actual primes have these laws. In the arithmetic relation \(\ell\mid q+r\), source primes are deterministic, not independent, while different source windows can have different residue profiles. Real first-exit weights, cross-prime masks, physical conductor pushforward, and pre-aggregation signed/complex phases are not controlled by (1)–(4). The theorem neither bounds \(M(x)\) nor implies any zero-free region or RH.

A proposed transfer would have to establish source-specific control of **both** directional shared-vertex overlaps and the rare high-multiplicity contribution, with a norm or tail condition appropriate to the *actual weighted arithmetic statistic*. Merely observing a Poisson-like distribution or small average collision count in an independent-label control cannot supply that condition.
