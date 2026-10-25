# RE-264 — Maynard panels realize finite balanced integer Robin sharpness at fixed budget

**Status:** LITERATURE+DERIVED + EXACT-FINITE-SOURCE-REALIZATION; independent adversarial review pending.

**Dependencies:** RE-261 (counting-budget upper bound and Robin coordinate), RE-262 (quadratic support necessity), RE-263 (two-prime repair classification); Maynard, *Dense clusters of primes in subsets*, Theorem 3.4.

For each **fixed** counting budget, the sharp Robin source-discrepancy constant survives simultaneous integrality, distinctness, finite modification, exact Mertens normalization, and preservation of the total number of labels. The compensators can finish at the optimal quadratic scale. The construction uses a sufficiently large admissible panel of linear forms whose **every prime pair** admits an exact repair; it does not prescribe a pair and assume a prime-tuple conjecture.

## 1. Precise source theorem

Let \(\mathbb P\) be the ordinary primes. Fix an integer \(K\ge1\), and let \(p\to\infty\) through ordinary primes. One may also prescribe a frozen prefix \(T=T(p)\ge p\), with \(T/p\to1\).

For every sufficiently large \(p\), there is a distinct integer-label source
\[
Q=(\mathbb P\setminus D)\cup B
\]
with exactly \(2K\) deleted primes and \(2K\) inserted composites, such that
\[
Q\cap(1,T]=\mathbb P\cap(1,T],\qquad
\Gamma(Q)=\gamma,\qquad
|A(t)|\le K\quad(t\ge p),\qquad A(t)=0\text{ eventually},
\tag{1}
\]
where
\[
A(t)=\Pi_Q(t)-\pi(t),\qquad
\Gamma(Q)=\lim_{x\to\infty}
\left(\sum_{q\in Q,\ q\le x}\log\frac q{q-1}-\log\log x\right).
\]
The altered labels form three ordered packets, uniformly within each packet:
\[
B=\{a_1,\ldots,a_K,b_1,\ldots,b_K\},\qquad
a_j=p+o(p)>T,
\]
\[
D=\{r_1,\ldots,r_{2K}\},\quad r_i=2p+o(p),\qquad
b_j=4p^2+o(p^2).
\tag{2}
\]
Write
\[
f(t)=\log\frac t{t-1},\quad h(t)=\frac{f(t)}{\log t},\quad
\Delta\vartheta(t)=\sum_{q\in Q,\ q\le t}\log q
-\sum_{r\in\mathbb P,\ r\le t}\log r,
\quad E_Q(U)=\int_p^U\Delta\vartheta(t)h'(t)\,dt.
\]
At \(U=\min D\),
\[
\boxed{E_Q(U)=-\left(\frac12+o(1)\right)\frac Kp.}
\tag{3}
\]
Consequently, over the finite, cardinality-preserving integer subclass of RE-261 with budget \(K\) and the prescribed prefix,
\[
\boxed{\sup_Q\sup_{U\ge p}|E_Q(U)|
=\left(\frac12+o(1)\right)\frac Kp\qquad(K\text{ fixed}).}
\tag{4}
\]
The construction applies at every sufficiently large frontier, not just an unspecified subsequence. All thresholds may depend on \(K\) and the chosen accuracy. No uniformity for a prescribed growing \(K(p)\) is asserted.

## 2. An integer repair for every pair in a panel

Choose distinct positive integers \(c_1<\cdots<c_k\), all congruent to one modulo three. Put
\[
M=\operatorname{lcm}_{i<j}(c_i+c_j),\qquad
\nu\in\{1,2\},\quad M\nu\equiv1\pmod3,
\qquad t=M(3n+\nu).
\tag{5}
\]
No pair sum is divisible by three, so \(3\nmid M\) and \(\nu\) exists. Define
\[
L_i(n)=c_it+1=3Mc_i n+(Mc_i\nu+1).
\tag{6}
\]
For any pair \(i<j\), let
\[
r=L_i(n),\quad s=L_j(n),\qquad
a=1+\frac{c_ic_j}{c_i+c_j}t,\qquad b=rs.
\tag{7}
\]
Then \(a\) is an integer, and direct multiplication gives
\[
a=\frac{rs-1}{r+s-2},\qquad
\boxed{\frac r{r-1}\frac s{s-1}=\frac a{a-1}\frac b{b-1}.}
\tag{8}
\]
Indeed \(rs-1=t(c_i+c_j+c_ic_jt)\), while
\((r-1)(s-1)=c_ic_jt^2\). This is the \(b=rs\) case of RE-263's repair equation.

Moreover, division modulo three is legitimate in (7), since \(c_i+c_j\equiv2\pmod3\). Because \(t\equiv1\pmod3\),
\[
a\equiv1+\frac{1}{2}\equiv0\pmod3,\qquad
L_i(n)\equiv2\pmod3.
\tag{9}
\]
Thus \(a>3\) is composite. Whenever \(r,s\) are prime, \(b=rs\) is also composite, and both can be inserted into the ordinary-prime source without duplicating a surviving prime.

The full panel (6) is admissible. At the prime three, every form is two modulo three. If a prime \(\ell\ne3\) divides \(M\), every form is one modulo \(\ell\). Otherwise choose \(n\) with \(3n+\nu\equiv0\pmod\ell\); again every form is one modulo \(\ell\). Hence the product has no fixed prime divisor. Each form is primitive, its coefficients are positive, and the forms are distinct. Their pairwise determinants are \(3M(c_i-c_j)\ne0\).

This admissibility argument is for every prime, not just a finite numerical check. It also explains why imposing composite early insertions does not create a local obstruction to the prime deletions.

## 3. Prime supply in the required interval

We use the following fixed-parameter consequence of Maynard's Theorem 3.4: for each fixed \(m\), a sufficiently large finite admissible panel of distinct positive integer linear forms has at least \(m\) prime values for some integer \(n\) in every interval \([x,x+y]\), once \(x\) is sufficiently large and \(x^{2/3}\le y\le x\). All panel coefficients are held fixed here. This follows by taking the theorem's short-interval parameter to be \(1/12\); its coefficient restrictions eventually hold for any fixed panel.

Fix temporarily \(0<\eta<1/10\). Take the panel size \(k=k(2K)\) supplied by that theorem. Choose \(C\equiv1\pmod3\) sufficiently large that
\[
c_i=C+3(i-1),\qquad C\le c_i\le(1+\eta)C.
\tag{10}
\]
The constants \(C,M,\nu\) now depend on \(K,\eta\), but are independent of \(p\).

Require the parameter in (5) to lie in
\[
\frac{2(1+\eta)p}{C}\le t\le
\frac{2(1+2\eta)p}{C}.
\tag{11}
\]
The corresponding interval of real \(n\)'s has left endpoint
\(2(1+\eta)p/(3MC)-\nu/3\) and length
\(2\eta p/(3MC)\). After rounding the endpoints inward, it contains an integer-endpoint interval with \(x\asymp_{K,\eta}p\) and \(y\asymp_{K,\eta}p\). In particular \(x^{2/3}\le y\le x\) for all sufficiently large \(p\). Maynard therefore supplies at least \(2K\) prime values at a common \(n\) satisfying (11).

Order any \(2K\) of those primes by their coefficients and pair them consecutively. For each pair insert the two labels (7). The harmonic expression \(cd/(c+d)\) is strictly increasing in each positive argument. Thus the early labels of consecutive disjoint pairs are strictly ordered and distinct. The late products are also distinct, by unique prime factorization (or their strict ordering). Uniformly over the chosen pairs,
\[
(1+\eta)p+1\le a_j\le(1+\eta)(1+2\eta)p+1,
\tag{12}
\]
\[
2(1+\eta)p+1\le r_i\le
2(1+\eta)(1+2\eta)p+1.
\tag{13}
\]
For \(\eta<1/10\), every early insertion precedes every deletion; every late product follows every deletion for large \(p\). All insertions are composites, by (9), and there are exactly \(2K\) of them. Since \(T/p\to1\), (12) also puts every alteration beyond \(T\) eventually.

Multiplying (8) over the \(K\) disjoint pairs gives exact finite Euler-product equality. Finite modification then gives \(\Gamma(Q)=\gamma\). The counting discrepancy rises from zero to \(K\) through the early packet, falls to \(-K\) through the \(2K\) deletions, and rises back to zero through the late packet. This proves every exact condition in (1).

For each fixed accuracy \(\eta\), these conclusions hold for **all** sufficiently large \(p\). Taking a staircase of fixed accuracies tending to zero, with increasing thresholds beyond their respective prime-supply and prefix bounds, gives witnesses with (2). This is a diagonal choice of fixed panels, not an invocation of Maynard with uncontrolled coefficients varying inside one asymptotic estimate.

## 4. Robin amplitude and the necessary support scale

At \(U=\min D\), only the early insertions have contributed to the integral; the deletion at the endpoint has no effect on its value. Thus
\[
E_Q(U)=\sum_{j=1}^K\log a_j\,[h(U)-h(a_j)]
=h(U)\sum_{j=1}^K\log a_j-\sum_{j=1}^Kf(a_j).
\tag{14}
\]
Using (2), \(f(a_j)=(1+o(1))/p\) and
\(h(U)\log a_j=(1+o(1))/(2p)\), proving (3).
RE-261's universal bound
\[
\sup_U|E_Q(U)|\le\left(\frac12+O((\log p)^{-1})\right)\frac Kp
\]
proves (4).

The largest inserted label is \((4+o(1))p^2\). Conversely, for any nontrivial finite balanced repair whose deleted primes all equal \(2p+o(p)\), RE-262 forces an insertion at least as large as the product of the two smallest deletions, namely \((4+o(1))p^2\). Hence the leading support constant four is attained within this deletion-packet regime. This is not a lower support theorem for arbitrary multi-packet deletions.

There is no conflict with RE-263's square-root gap obstruction. At any fixed panel, distinct selected coefficients differ by at least three, so each repaired pair has gap at least \(3t\asymp_{K,\eta}p\). Shrinking the panel's relative width uses a later, larger scale; the construction does not force gaps \(o(\sqrt p)\). In particular it establishes existence of the near-diagonal asymptotic family left open in RE-263 without specifying a fixed pair of linear forms in advance.

## 5. Validation, prior art, and limits

Supplementary exact checks used the small panel \((10,13,16,19)\), for which \(M=9711520\) and \(\nu=1\). All six pairs at \(n=1,\ldots,50\) passed the rational identity (8), the integer/divisibility conditions, and the order \(a<r<s<b\): 300 exact pair checks. Admissibility was additionally checked at all 46 primes below 200. Fifty consecutive-pair combinations verified distinct labels, packet order, exact product equality, maximum absolute count two, and final count zero; primality of all their deletion labels was not assumed.

Two single-pair source controls were checked by trial-division primality and exact rational arithmetic:
\[
(r,s,a,b)=(679806401,883748321,384238401,600777765488802721),
\]
\[
(r,s,a,b)=(5924027201,7701235361,3348363201,45622327759867054561).
\]
Both have distinct composite insertions, exact normalization and counting budget one. The small panel is a control of the algebra and source bookkeeping, not a certified panel size for Maynard's theorem or numerical evidence for its asymptotic conclusion.

The load-bearing external theorem is James Maynard, [*Dense clusters of primes in subsets*, Compositio Mathematica **152** (2016), 1517–1554](https://doi.org/10.1112/S0010437X16007296), [primary paper, Theorem 3.4](https://compositio.nl/Content/prize2018_maynard.pdf). Its prime supply is unconditional; neither Dickson's conjecture nor a new sieve estimate is asserted here.

The broader method of arranging that any prime pair selected from an admissible panel yields a desired arithmetic consequence is established prior art. A close comparison is Kevin Ford and Sergei Konyagin, [*Differences between totients*, author manuscript, 16 September 2021](https://www.ford126.web.illinois.edu/wwwpapers/totient_gaps.pdf), especially Theorem 4 and its proof. Their application concerns differences of totients. The pairwise Euler identity is elementary and belongs to RE-263's already classified bilinear mechanism.

The mathematical delta is the **finite balanced integer source construction at every large frontier for fixed budget**, including composite-label admissibility, simultaneous packet ordering, exact normalization, sharp Robin amplitude and optimal quadratic support. RE-261's finite integer sharpness witnesses leave a positive terminal count; its balanced witnesses use real labels, and its alternative integer completion is infinite. RE-262 gives a necessary support barrier. RE-263 gives a complete pair test without an infinite near-diagonal existence theorem. The present argument supplies that missing prime-existence input. The literature audit does not establish global novelty for the algebraic identity or panel strategy.

The fixed-budget quantifier is essential. The sieve panel size, coefficients and onset may grow very rapidly with \(K\) or accuracy. No conclusion follows here for \(K\asymp\sqrt p/\log p\), or for an arbitrary prescribed unbounded \(K(p)\). For fixed \(K\), the Robin-normalized amplitude \(\sqrt p\log p\,|E_Q(U)|\sim K\log p/(2\sqrt p)\) tends to zero. Thus this theorem removes a fixed-budget realization obstruction, not the unresolved critical-budget or CA-selected signed-tail problem.

The inserted composites are synthetic Euler atoms with factors \(q/(q-1)\), not their ordinary divisor-sum contributions. No new CA exponent restriction, actual-prime counterexample, Robin inequality, or RH conclusion is proved. The external sieve theorem is not formally verified here; the displayed finite checks do not replace it.
