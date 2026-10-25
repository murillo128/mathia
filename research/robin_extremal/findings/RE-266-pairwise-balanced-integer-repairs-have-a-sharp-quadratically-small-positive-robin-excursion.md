# RE-266 — Pairwise balanced integer repairs have a sharp quadratically small positive Robin excursion

**Status:** EXACT-DERIVED + ONE-SIDED-SOURCE-OBSTRUCTION + LITERATURE-BACKED-SHARPNESS; independent adversarial review pending.

**Dependencies:** RE-261 (Robin discrepancy and absolute counting bound), RE-263 (subdyadic two-prime repair classification), RE-265 (disjoint fixed-panel repair supply).

RE-265 reaches the critical **absolute** Robin discrepancy with finite, count-preserving integer sources. Its negative sign is structural within the larger class assembled from individually exact subdyadic two-prime repairs: their positive excursions are smaller by a full power of the frontier. This does not establish a sign restriction for arbitrary balanced repairs whose Euler debts cancel only across larger packets.

## 1. The signed source theorem

Let \(p\ge3\) be an ordinary prime and \(K\ge1\) an integer. Consider sources
\[
Q=(\mathbb P\setminus D)\cup B
\]
built from at most \(K\) nontrivial, individually exact repairs
\[
\{r_j,s_j\}\longmapsto\{a_j,b_j\},\qquad
3\le r_j<s_j<2r_j,
\qquad
\frac{a_j}{a_j-1}\frac{b_j}{b_j-1}
=\frac{r_j}{r_j-1}\frac{s_j}{s_j-1}.
\tag{1}
\]
The deleted labels are distinct ordinary primes. All inserted labels are distinct composite integers, and all alterations lie above \(p\). Different repairs have disjoint labels. Order each insertion pair increasingly. RE-263 implies
\[
p<a_j<r_j<s_j<b_j,\qquad b_j=k_jr_js_j,
\quad k_j\in\mathbb N_{\ge1}.
\tag{2}
\]
Write
\[
f(t)=\log\frac{t}{t-1},\qquad h(t)=\frac{f(t)}{\log t},
\qquad
E_Q(U)=\int_p^U\bigl(\vartheta_Q(t)-\vartheta_{\mathbb P}(t)\bigr)h'(t)\,dt,
\tag{3}
\]
where \(\vartheta_S(t)=\sum_{s\in S,\ s\le t}\log s\), \(\Pi_S(t)=\#\{s\in S:s\le t\}\), and
\[
\Gamma(Q)=\lim_{x\to\infty}\left(\sum_{q\in Q,\ q\le x}f(q)-\log\log x\right).
\]
Every source in this class has exact Mertens constant \(\Gamma(Q)=\gamma\), equal finite insertion and deletion counts, and
\(\sup_t|\Pi_Q(t)-\pi(t)|\le K\). Nevertheless the two signed extrema have different scales:
\[
\boxed{\sup_{U\ge p}E_Q(U)\le\frac{K}{8p(p-1)}.}
\tag{4}
\]
The bound is uniform in insertion height, prime-pair separation within the subdyadic range, and interleaving of the different repairs.

Let \(\mathcal P_{p,K,T}\) denote this class with the additional frozen prefix \(Q\cap(1,T]=\mathbb P\cap(1,T]\), where \(T\ge p\) and \(T/p\to1\). For the fixed absolute integer \(\kappa\) supplied by RE-265, if
\[
1\le K=K(p)=o\!\left(\frac{p}{(\log p)^\kappa}\right),
\tag{5}
\]
then
\[
\boxed{\sup_{Q\in\mathcal P_{p,K,T}}\sup_{U\ge p}E_Q(U)
=\left(\frac18+o(1)\right)\frac{K}{p^2},}
\qquad
\boxed{\sup_{Q\in\mathcal P_{p,K,T}}\sup_{U\ge p}(-E_Q(U))
=\left(\frac12+o(1)\right)\frac{K}{p}.}
\tag{6}
\]
The same witnesses attain both leading constants, at different heights.
Here \(K\) bounds the **number of independently matched pairs**, not merely the net counting discrepancy of an otherwise unrestricted source.

## 2. Exact sign geometry of one repair

Suppress the pair index and set \(P=rs\), \(b=kP\). To recall the algebraic input from RE-263: subdyadic odd primes have neither \(r\mid s-1\) nor \(s\mid r-1\). Thus the reduced deleted Euler product has both primes in its numerator. Each must divide an insertion numerator. If they divide different insertions without sharing one, monotonicity of \(t/(t-1)\) forces the trivial replacement. A nontrivial replacement therefore has \(b=kP\). Solving (1) gives
\[
a=\frac{kP-1}{k(r+s-1)-1},\qquad
\frac{P}{r+s-1}<a\le\frac{P-1}{r+s-2}<r.
\tag{7}
\]
This is a previously classified Diophantine mechanism, not a new prime-existence claim.

The logarithmic mass discrepancy of this single repair is the step function
\[
\Delta\vartheta(t)=
\begin{cases}
0,&t<a,\\
\log a,&a\le t<r,\\
\log(a/r),&r\le t<s,\\
\log(a/P),&s\le t<b,\\
\log(ak),&t\ge b.
\end{cases}
\tag{8}
\]
Since \(h'<0\), its integral \(E\) decreases strictly from \(a\) to \(r\), increases strictly from \(r\) to \(b\), and decreases strictly thereafter to zero. Direct integration gives
\[
E(r)=h(r)\log a-f(a)<0,
\qquad
\boxed{\max_{U\ge p}E(U)=E(b)=h(b)\log(ak)>0.}
\tag{9}
\]
The positive maximum uses exact Euler matching: at and beyond \(b\), the sum of signed \(f\)-weights vanishes, leaving \(h(U)\log(ak)\).

The sign change occurs strictly between the second deletion and the far insertion. Indeed
\[
E(s)=h(s)\log(a/r)-f(s)+f(b)<0,
\]
and throughout \([s,b]\),
\[
E(U)=f(b)-h(U)\log(P/a).
\tag{10}
\]
Consequently the unique zero in \((r,b)\) lies in \((s,b)\) and is determined by
\(h(U)=f(b)/\log(P/a)\). In particular the repair is not globally nonpositive; its positive part appears only after the early negative excursion has been mostly repaid.

## 3. A uniform quadratic bound, including arbitrarily large compensators

Equation (7), with \(r+s\ge2\sqrt P\), implies
\[
P\ge a(r+s-2)+1\ge2a\sqrt P-2a+1.
\]
Because \(\sqrt P>a\), this is equivalent to
\[
\boxed{\sqrt P\ge2a-1,\qquad P-1\ge4a(a-1).}
\tag{11}
\]
Use \(f(t)\le1/(t-1)\). If \(k=1\), then \(P\ge a^2\), so
\[
h(P)\log a
\le\frac{1}{2(P-1)}.
\]
If \(k\ge2\), the logarithm ratio \(\log(ka)/\log(kP)\) is less than one, giving
\[
h(kP)\log(ka)
<\frac{1}{kP-1}<\frac{1}{2(P-1)}.
\]
Together with (9) and (11), this proves the exact pair bound
\[
\boxed{\sup_U E(U)\le\frac{1}{8a(a-1)}
\le\frac{1}{8p(p-1)}.}
\tag{12}
\]
Thus increasing the integer multiplier \(k\) cannot recover a positive excursion of order \(1/p\). The proof does not assume that \(k\) is bounded.

For a source composed of \(m\le K\) disjoint repairs, logarithmic source discrepancies and their integrals add exactly. Apply (12) to each summand at an arbitrary common height to prove (4). Each repair has counting profile \(+1\) on \([a,r)\), \(-1\) on \([s,b)\), and zero elsewhere; hence its absolute count is at most one. Summing proves the stated counting bound even when packets interleave. Products in (1) give exact normalization and equal counts without a limiting compensation step.

## 4. Sharpness and the critical Robin normalization

RE-265 constructs, under (5) and any prescribed \(T/p\to1\), exactly \(K\) disjoint repairs with
\[
a_j=p+o(p)>T,\qquad r_j,s_j=2p+o(p),\qquad
k_j=1,\qquad b_j=(4+o(1))p^2,
\tag{13}
\]
uniformly in \(j\). They are in \(\mathcal P_{p,K,T}\).
At \(U_+=\max_j b_j\), every repair is complete, so
\[
E_Q(U_+)=h(U_+)\sum_{j=1}^K\log a_j
=\left(\frac18+o(1)\right)\frac{K}{p^2}.
\tag{14}
\]
The uniform packet asymptotics justify the sum for growing \(K\). Equation (4) proves optimality of this leading constant.
At \(U_-=\min_j r_j\), RE-265 gives
\[
E_Q(U_-)=-\left(\frac12+o(1)\right)\frac Kp.
\tag{15}
\]
The absolute counting bound from RE-261 applies since \(|\Pi_Q-\pi|\le K\), proving the other half of (6).

For \(K\sim\lambda\sqrt p/\log p\), \(\lambda>0\) fixed, the maximal positive normalized discrepancy is
\[
\sqrt p\log p\,\sup_{Q,U}E_Q(U)
=\frac{\lambda+o(1)}{8p}\longrightarrow0,
\tag{16}
\]
whereas the maximal negative magnitude tends to \(\lambda/2\). The existing critical absolute witnesses therefore do not supply a positive critical excursion in this class. Their positive peak is near quadratic height, and is not a missing sign reversal at the original near-linear height.

## 5. Audit, prior art, and the remaining boundary

The argument was checked against all 1,883 subdyadic odd-prime pairs below 500. RE-263's exact candidate test yielded 144 nontrivial algebraic repairs, of which 92 have composite early insertions and hence are valid distinct-label source repairs. Exact rational arithmetic verified each Euler identity, label ordering, and \(P\ge(2a-1)^2\). Decimal calculations at 40 and 80 digits independently evaluated the atom integrals at every event, intervening midpoints, and twice the final label: all obeyed (9), the negative value at \(s\), and (12). These logarithmic calculations are numerical diagnostics, not certified intervals or substitutes for the analytic proof.

The two disjoint prime-pair controls from RE-265 were also checked by trial division and exact fractions. At their common final cutoff the positive integral is approximately \(2.19545\times10^{-16}\), below the summed bound \(2.30126\times10^{-16}\) obtained using the smaller early insertion. These finite controls neither establish an asymptotic nor certify a sieve onset.

The algebraic prior-art boundary is the classical reduction of two-variable rational equations to shifted products and divisibility tests; see T. Chen and R. Koo, [*Two-term Egyptian fractions*, Notes on Number Theory and Discrete Mathematics **19** (2013), 15–25](https://www.nntdm.net/papers/nntdm-19/NNTDM-19-2-15-25.pdf), Section 2. The signed integration is elementary Abel summation and monotonicity; general discrepancy/variation duality is already classical, as discussed by C. Aistleitner and J. Dick, [*Functions of bounded variation, signed measures, and a general Koksma–Hlawka inequality*](https://arxiv.org/abs/1406.0230). Neither source is asserted to contain the Robin pair-repair bound.

Only sharpness imports a prime-supply theorem. RE-265 uses J. Maynard, [*Dense clusters of primes in subsets*, Compositio Mathematica **152** (2016), 1517–1554](https://compositio.nl/Content/prize2018_maynard.pdf), Theorem 3.4, with a fixed panel and two requested prime forms; its quantitative parameter count and disjointness argument yield (13). The theorem's fixed-panel coefficient and interval requirements match that use. No new sieve input, growing-panel theorem, or effective onset is asserted here.

The mathematical delta is a sharp **one-sided stability theorem for the entire class of disjoint, individually exact subdyadic two-prime repairs**, rather than an observation about the sign of one chosen witness. The elementary arithmetic and discrepancy mechanisms are not claimed as globally new; the literature check bounds the claim to this derived Robin-source application.

The pair decomposition and its cardinality are essential hypotheses. An arbitrary finite balanced integer source with counting budget \(K\) need not decompose into at most \(K\) such repairs. Larger coupled packets, non-subdyadic prime-chain mechanisms, infinite completions, and sources with many individually matched pairs but a smaller net counting norm remain outside (4). The finite unbalanced splitting witnesses of RE-261 already attain a positive \((1/2+o(1))K/p\); their nonzero terminal count excludes them from this theorem.

Composite labels retain synthetic factors \(q/(q-1)\), not their ordinary divisor-sum factors. The result closes the attempt to obtain positive critical Robin discrepancy merely by arranging or enlarging these pairwise balanced repairs. It does not rule out a positive critical excursion in the full balanced integer class, constrain actual CA exponent vectors, or prove a Robin inequality or RH consequence.
