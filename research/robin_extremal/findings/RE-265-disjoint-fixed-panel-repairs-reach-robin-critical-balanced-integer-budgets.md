# RE-265 — Disjoint fixed-panel repairs reach Robin-critical balanced integer budgets

**Status:** LITERATURE+DERIVED + EXACT-FINITE-SOURCE-REALIZATION; independent adversarial review pending.

**Dependencies:** RE-261 (universal counting-budget bound), RE-262 (quadratic support obstruction), RE-264 (admissible pair-repair panel); Maynard, *Dense clusters of primes in subsets*, Theorem 3.4.

Finite cardinality preservation does not restore counting stability at the Robin-critical scale, even with distinct integer labels and exact Mertens normalization. The fixed-budget restriction in RE-264 can be removed at that scale by using **many parameters of a fixed two-prime panel**, rather than requiring an increasing number of prime forms at one parameter. A bounded-degree collision argument makes the resulting repairs disjoint.

## 1. Growing-budget source theorem

There is an absolute fixed integer \(\kappa\ge2\) with the following property. Let \(p\to\infty\) through ordinary primes, prescribe \(T(p)\ge p\) with \(T/p\to1\), and let the integer budget satisfy
\[
1\le K=K(p)=o\!\left(\frac p{(\log p)^\kappa}\right).
\tag{1}
\]
For every sufficiently large \(p\), there is a distinct integer-label source
\[
Q=(\mathbb P\setminus D)\cup B
\]
with exactly \(2K\) deleted ordinary primes and \(2K\) inserted composites, such that
\[
Q\cap(1,T]=\mathbb P\cap(1,T],\qquad
\Gamma(Q)=\gamma,\qquad
\sup_{t\ge p}|A(t)|=K,\qquad A(t)=0\text{ eventually},
\tag{2}
\]
where
\[
A(t)=\Pi_Q(t)-\pi(t),\qquad
\Gamma(Q)=\lim_{x\to\infty}
\left(\sum_{q\in Q,\ q\le x}\log\frac q{q-1}-\log\log x\right).
\]
The alterations lie in three packets, uniformly over their growing numbers of labels:
\[
B=\{a_1,\ldots,a_K,b_1,\ldots,b_K\},\quad a_j=p+o(p)>T,
\]
\[
D=\{r_1,\ldots,r_{2K}\},\quad r_i=2p+o(p),\qquad
b_j=4p^2+o(p^2).
\tag{3}
\]
Define
\[
f(t)=\log\frac t{t-1},\quad h(t)=\frac{f(t)}{\log t},\quad
\Delta\vartheta(t)=\sum_{q\in Q,\ q\le t}\log q
-\sum_{r\in\mathbb P,\ r\le t}\log r,
\]
\[
E_Q(U)=\int_p^U\Delta\vartheta(t)h'(t)\,dt.
\]
At \(U=\min D\),
\[
\boxed{E_Q(U)=-\left(\frac12+o(1)\right)\frac Kp.}
\tag{4}
\]
Consequently, if \(\mathcal B_{p,K,T}\) denotes all finite integer-label modifications with the prefix and exact normalization in (2), \(|A|\le K\), and eventual zero count, then
\[
\boxed{\sup_{Q\in\mathcal B_{p,K,T}}\sup_{U\ge p}|E_Q(U)|
=\left(\frac12+o(1)\right)\frac Kp.}
\tag{5}
\]
In particular, for any fixed \(\lambda>0\) and
\(K\sim\lambda\sqrt p/\log p\), multiplying by \(\sqrt p\log p\) makes the supremum tend to \(\lambda/2\), and the displayed witnesses have normalized value tending to \(-\lambda/2\). This is an absolute-discrepancy sharpness result with a negative signed witness, not a positive Robin-height construction.

## 2. A fixed panel supplies many candidate repairs

Fix an accuracy \(0<\eta<1/10\). In Maynard's Theorem 3.4 take \(m=2\) and the short-interval parameter \(\epsilon=1/12\). Let \(k\ge2\) be its fixed panel size and set \(\kappa=k\). In particular, \(k\) is independent of \(K,p,\eta\).

Choose \(C\equiv1\pmod3\) large enough that
\[
c_i=C+3(i-1),\qquad C\le c_i\le(1+\eta)C\quad(1\le i\le k).
\]
Set
\[
M=\operatorname{lcm}_{i<j}(c_i+c_j),\quad
\nu\in\{1,2\},\quad M\nu\equiv1\pmod3,
\]
\[
t_n=M(3n+\nu),\qquad L_i(n)=c_it_n+1.
\tag{6}
\]
These are fixed forms while \(p\) varies at this fixed accuracy. No pair sum is divisible by three, so \(\nu\) exists. At the prime three all forms equal two; at a prime dividing \(M\) all forms equal one; at any other prime choose \(3n+\nu=0\) modulo that prime. Thus the panel is admissible. Each form is primitive, and distinct slopes have nonzero determinants.

Restrict \(n\) by
\[
\frac{2(1+\eta)p}{C}\le t_n\le\frac{2(1+2\eta)p}{C}.
\tag{7}
\]
After integer endpoint adjustment this contains an interval \([x,x+y]\) with \(x\asymp_\eta p\), \(y\asymp_\eta p\), and \(x^{2/3}\le y\le x\) for all sufficiently large \(p\). The coefficients in (6) are fixed, so they eventually meet the theorem's coefficient restrictions. Its quantitative conclusion gives
\[
\#\{n\text{ satisfying (7)}:\text{at least two }L_i(n)\text{ are prime}\}
\gg_\eta\frac p{(\log p)^k}.
\tag{8}
\]
All dependence on the fixed panel is included in the constant and onset. We use the lower bound on the **number of parameters**, not only existence of one parameter. No uniform theorem with \(m=2K\) is invoked.

Assign one prime pair to each parameter counted in (8). Some pair of indices \(i<j\) occurs for a set \(S\) of at least \(1/\binom{k}{2}\) of these parameters. The selected pair may depend on \(p\). We neither prescribe which pair succeeds nor require a fixed pair to work in every interval.

For \(n\in S\), put
\[
r_n=L_i(n),\quad s_n=L_j(n),\qquad
a_n=1+\frac{c_ic_j}{c_i+c_j}t_n,\quad b_n=r_ns_n.
\tag{9}
\]
Since \(c_i+c_j\mid M\), \(a_n\) is integral. Also \(t_n\equiv1\pmod3\) and \(c_i,c_j\equiv1\pmod3\), so \(a_n\equiv0\pmod3\); it exceeds three and is composite. The label \(b_n\) is composite. Direct multiplication gives
\[
a_n=\frac{r_ns_n-1}{r_n+s_n-2},\qquad
\boxed{\frac{r_n}{r_n-1}\frac{s_n}{s_n-1}
=\frac{a_n}{a_n-1}\frac{b_n}{b_n-1}.}
\tag{10}
\]
This is the same exact repair identity as in RE-264.

## 3. Collision removal and a growing number of disjoint repairs

One must not multiply arbitrary identities (10): the same prime could occur in two repairs, whereas the source deletes each prime at most once.

Make a graph on \(S\), joining distinct \(n,n'\) precisely when
\(\{r_n,s_n\}\cap\{r_{n'},s_{n'}\}\ne\varnothing\).
Each form is injective in \(n\). Thus a shared prime must arise from
\[
L_i(n)=L_j(n')\quad\text{or}\quad L_j(n)=L_i(n').
\tag{11}
\]
For fixed \(n\), each equation determines at most one \(n'\). The graph therefore has maximum degree at most two. Greedily keeping one vertex and discarding it and its neighbors produces an independent set of size at least \(|S|/3\). By (8), the number of disjoint candidate repairs is still
\[
\gg_\eta\frac p{(\log p)^k}.
\tag{12}
\]
Condition (1) makes this exceed \(K(p)\) for every sufficiently large \(p\), at each fixed accuracy. Retain exactly \(K\) repairs.

Their early labels \(a_n\) are distinct, since (9) is strictly increasing in \(n\) for the fixed pair. Their late labels \(b_n\) are likewise strictly increasing. All insertions are composite, so they cannot duplicate surviving primes or deleted primes. The packet bounds from (7) are
\[
(1+\eta)p+1\le a_n\le(1+\eta)(1+2\eta)p+1,
\tag{13}
\]
\[
2(1+\eta)p+1\le r_n,s_n\le2(1+\eta)(1+2\eta)p+1.
\tag{14}
\]
For \(\eta<1/10\), every early insertion precedes every deletion, and every late insertion follows all deletions once \(p\) is large. Every alteration exceeds \(T\), because \(T/p\to1\). Thus \(A\) rises from zero to \(K\), falls to \(-K\), and returns to zero. All labels are distinct, and there are exactly \(2K\) insertions and \(2K\) deletions.

Multiplying (10) over these disjoint repairs gives exact finite Euler-product equality, hence \(\Gamma(Q)=\gamma\). No limiting correction or approximate Mertens match is used.

Finally choose fixed accuracies \(\eta_j\downarrow0\). For each \(j\), (1) ensures that (12), the prime-supply theorem, and the prefix condition hold for **all** \(p\) beyond some threshold \(P_j\). Increase these thresholds strictly, and use the \(j\)-th fixed panel on \([P_j,P_{j+1})\). Equations (13)--(14) then give (3), uniformly over all selected repairs. This diagonal step does not assume any control of Maynard's constants as \(\eta\to0\), and \(k\) stays fixed throughout.

## 4. Robin amplitude, sharp support, and the evidence boundary

At \(U=\min D\), only the early insertions contribute to the integral; a deletion exactly at the endpoint contributes zero. Therefore
\[
E_Q(U)=\sum_{j=1}^K\log a_j\,[h(U)-h(a_j)]
=h(U)\sum_{j=1}^K\log a_j-\sum_{j=1}^K f(a_j).
\tag{15}
\]
By (3), uniformly in \(j\),
\[
f(a_j)=\frac{1+o(1)}p,\qquad
h(U)\log a_j=\frac{1+o(1)}{2p}.
\]
The uniformity allows summation over growing \(K\), proving (4). RE-261 supplies the source-independent upper bound
\[
\sup_U|E_Q(U)|\le\left(\frac12+O((\log p)^{-1})\right)\frac Kp,
\]
so (5) follows.

The largest insertion is \((4+o(1))p^2\). RE-262 forces at least the product of the two smallest deleted primes in every nontrivial finite balanced repair with this subdyadic deletion packet. Its argument does not require the number of deletions to be fixed. Thus the same leading quadratic support constant four remains sharp here.

For any fixed \(0<\delta<1\), all budgets \(1\le K\le p^{1-\delta}\) satisfy (1). In particular the Robin-critical budget and power-law budgets above it are included. This does not establish sharpness for every \(K=o(p/\log p)\); the fixed logarithmic-power loss in (8) remains. No numerical onset is claimed: the underlying sieve theorem is not effective as stated, and the accuracy diagonal is qualitative.

The construction produces a different finite synthetic source for each frontier. It does not construct one source with prescribed behavior at infinitely many frontiers. The inserted composites carry synthetic Euler factors \(q/(q-1)\), not their ordinary divisor-sum factors. The theorem rules out restoration of an \(o(1)\) normalized **absolute** source-discrepancy bound from these fidelity conditions alone. It neither proves a positive signed excursion in this balanced class nor estimates the actual-prime CA-selected tail. No Robin inequality or RH consequence follows.

## 5. Validation and prior art

The external input is James Maynard, [*Dense clusters of primes in subsets*, Compositio Mathematica **152** (2016), 1517--1554](https://doi.org/10.1112/S0010437X16007296), [Theorem 3.4, p. 1520](https://compositio.nl/Content/prize2018_maynard.pdf). The admissible-panel and pairwise arithmetic strategy is prior art; a neighboring application is Kevin Ford and Sergei Konyagin, [*Differences between totients*, Theorem 4 and its proof](https://www.ford126.web.illinois.edu/wwwpapers/totient_gaps.pdf). The prime-count theorem, pair-selection principle, elementary graph bound, and identity (10) are not claimed as new general mechanisms.

The mathematical delta from RE-264 is the quantitatively sufficient supply of **disjoint repairs at different parameters**, which removes its fixed-budget limitation and reaches the critical normalized discrepancy while preserving finite balance and optimal quadratic support. RE-261 already gives critical sharpness with finite unbalanced integer sources, finite balanced real sources, or infinite integer completion. None of those is the finite balanced integer conclusion proved here. The literature comparison does not establish global novelty beyond this source-specific derived application.

Supplementary exact checks used the two-form control \((c_i,c_j)=(100,103)\), \(M=203\), \(\nu=2\), for every \(1000\le n\le1100\). All 101 identities (10), integrality conditions and individual orderings passed rational arithmetic. Trial division certified prime pairs at \(n=1066,1070\):
\[
(r,s,a,b)=(64960001,66908801,32960001,4346395779868801),
\]
\[
(r,s,a,b)=(65203601,67159709,33083601,4379054868912109).
\]
Together they give four distinct prime deletions, four distinct composite insertions, exact Euler-product equality, the required three-packet order, count range \([-2,2]\), and terminal count zero. These are algebra/source controls, not a certified Maynard panel or an asymptotic test.

A separate collision control on the forms \(10(3n+1)+1\) and \(13(3n+1)+1\), \(1\le n\le2000\), had 154 collision edges, maximum degree two, and a greedy independent set of size 1857. Primality is unnecessary for this graph lemma. The general proof is (11), not the finite control. Neither the sieve input nor the full theorem has been formally verified here.
