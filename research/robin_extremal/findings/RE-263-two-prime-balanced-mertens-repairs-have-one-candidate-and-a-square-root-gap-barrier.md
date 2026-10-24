# RE-263 — Two-prime balanced Mertens repairs have one candidate and a square-root gap barrier

**Status:** EXACT-DERIVED + FINITE-INTEGER-SOURCE-CLASSIFICATION + CLASSICAL-DIOPHANTINE-MECHANISM; independent adversarial review pending.

**Dependencies:** RE-262 (valuation/counting obstruction), RE-261 (sharp counting-discrepancy Robin norm and its exact source integral).

Allowing quadratic-height insertions does not suffice to repair an arbitrary pair of deleted primes while preserving the exact Mertens constant and the number of labels. For a subdyadic pair there is at most one nontrivial integer replacement, at any insertion height. An explicit divisibility test decides its existence. In particular, square-root-close pairs have no such replacement at all. This resolves the two-deletion case of the balanced-repair question; larger coupled packets remain outside the classification.

## 1. Complete classification with two deletions

Let \(3\le r<s<2r\) be distinct ordinary primes, and write
\[
P=rs,\qquad S=r+s,\qquad d=S-1,\qquad Q=(r-1)(s-1)=P-d.
\]
For a finite multiset \(B\) of integers at least two, define
\[
\mathscr E(B)=\prod_{b\in B}\frac b{b-1}.
\]
Suppose
\[
|B|\le2,\qquad \mathscr E(B)=\frac P Q.
\tag{1}
\]
Set
\[
a_0=\left\lfloor\frac P d\right\rfloor+1,
\qquad \delta=d a_0-P>0.
\tag{2}
\]
Then the complete list of solutions of (1) is
\[
\boxed{B=\{r,s\},\quad\text{and, precisely when }\delta\mid a_0-1,
\quad B=\{a_0,kP\},\qquad k=\frac{a_0-1}{\delta}.}
\tag{3}
\]
The second solution has \(2\le a_0<r<s<kP\). Thus it is distinct from the original pair, has no repeated label, and is unique when it exists. No upper bound on the inserted integers is assumed.

### Proof

The subdyadic hypothesis and oddness imply \(r\nmid s-1\); also \(s\nmid r-1\). Hence \(\gcd(P,Q)=1\) and
\[
v_r(P/Q)=v_s(P/Q)=1.
\]
Both primes must therefore divide insertion numerators. Zero insertions are impossible. With one insertion \(n\), both primes divide \(n\), so \(n\ge P\) and
\[
\frac n{n-1}\le\frac P{P-1}<\frac P Q,
\]
a contradiction.

With two insertions, suppose neither is divisible by both primes. Each prime must then divide a different occurrence. Monotonicity of \(t/(t-1)\) gives
\[
\mathscr E(B)\le\frac r{r-1}\frac s{s-1},
\]
with equality only for \(B=\{r,s\}\). Every nontrivial solution therefore has an occurrence \(b=kP\), \(k\ge1\). Denote the other by \(a\). Solving (1) gives
\[
\frac a{a-1}=\frac{kP-1}{kQ},\qquad
 a=\frac{kP-1}{kd-1},\qquad
 k(da-P)=a-1.
\tag{4}
\]
In particular
\[
\frac P d<a\le\frac{P-1}{d-1}<r.
\tag{5}
\]
The first two inequalities follow also from
\[
a-\frac P d=\frac{Q}{d(kd-1)}>0,
\]
which decreases with \(k\). The final inequality in (5) is equivalent to \((r-1)^2>0\).

The possible interval for \(a\) has length
\[
\frac{P-1}{d-1}-\frac P d
=\frac{Q}{d(d-1)}
\le\frac{S-2}{4(S-1)}<\frac14,
\tag{6}
\]
where \(rs\le S^2/4\) gives \(Q\le(S-2)^2/4\). Its only possible integer is therefore \(a_0\). Equation (4) forces exactly the divisibility test and value of \(k\) in (3).

Conversely, if \(\delta\mid a_0-1\), then \(k\) in (3) is a positive integer and \(k(da_0-P)=a_0-1\). Reversing (4) proves the product equality. It also recovers (5), so the proposed labels have the stated order. This proves sufficiency as well as necessity. \(\square\)

## 2. A support-independent prime-gap obstruction

Put \(g=s-r\). Every nontrivial solution in (3) necessarily satisfies
\[
\boxed{
\begin{cases}
g^2>S,&S\equiv0\pmod4,\\
g^2>3S-2,&S\equiv2\pmod4.
\end{cases}}
\tag{7}
\]
In particular, \(g^2\le r+s\) forces \(B=\{r,s\}\), regardless of how large insertions are allowed to be. The stronger second line applies when the two odd primes are congruent modulo four.

To prove this, the endpoints of (5) are
\[
\frac P d=\frac S4+\frac{S-g^2}{4(S-1)},\qquad
\frac{P-1}{d-1}=\frac{S+2}{4}-\frac{g^2}{4(S-2)}.
\tag{8}
\]
If \(S=4m\) and \(g^2\le S\), the lower endpoint is at least \(m\), while the upper endpoint is less than \(m+1/2\). The lower endpoint is excluded, so no integer lies in the interval.

If \(S=4m-2\), the upper endpoint is strictly less than \(m\). The lower endpoint equals
\[
m-\frac{S+g^2-2}{4(S-1)},
\]
which is at least \(m-1\) when \(g^2\le3S-2\). Again the open lower endpoint and strict upper bound leave no integer. This proves (7), including the endpoint cases.

These inequalities are necessary, not sufficient. Even when the interval contains \(a_0\), the divisibility test can fail. For example, \((r,s)=(31,41)\) gives \(a_0=18\), \(\delta=7\), and upper endpoint \(127/7>18\). But seven does not divide \(a_0-1=17\), so no nontrivial solution exists although \(g^2=100>S=72\).

## 3. Source realization and the Robin counting boundary

Let \(\mathbb P\) be the ordinary primes. A distinct integer-label source obtained by deleting **exactly** \(r,s\) and inserting two new labels has exact Mertens normalization if and only if its inserted Euler product satisfies (1). Here \(\Gamma(\mathcal Q)=\lim_{x\to\infty}(\sum_{q\in\mathcal Q,\ q\le x}\log(q/(q-1))-\log\log x)\), which exists for a finite modification. Its constant changes by
\[
\Gamma(\mathcal Q)-\gamma
=\sum_{b\in B}\log\frac b{b-1}
-\log\frac r{r-1}-\log\frac s{s-1}.
\tag{9}
\]
For the nontrivial algebraic solution to give such a source, \(a_0\) must be composite: if it is prime, it already belongs to the surviving prime set because \(a_0<r\). The large label \(kP\) is automatically composite. To preserve a prescribed prefix through \(T<r\), one must also have \(a_0>T\). These are genuine source-admissibility conditions, additional to rational-product equality.

When they hold, the counting discrepancy is exactly
\[
A(t)=\Pi_{\mathcal Q}(t)-\pi(t)=
\begin{cases}
1,&a_0\le t<r,\\
-1,&s\le t<kP,\\
0,&\text{otherwise}.
\end{cases}
\tag{10}
\]
Thus the source has counting budget one and zero terminal count. The broad gap between the two deletions contributes an interval where \(A=0\); it cannot simply be ignored in a near-maximizer argument.

For the precise connection, let \(p<a_0\) be a prime prefix, put
\[
f(t)=\log\frac t{t-1},\qquad h(t)=\frac{f(t)}{\log t},\qquad
\Delta\vartheta(t)=\sum_{q\in\mathcal Q,\ q\le t}\log q
-\sum_{q\in\mathbb P,\ q\le t}\log q,
\]
and use the RE-261 transient Robin coordinate
\[
E_{\mathcal Q}(U)=\int_p^U\Delta\vartheta(t)h'(t)\,dt.
\]
Before the first deletion,
\[
E_{\mathcal Q}(r)=h(r)\log a_0-f(a_0).
\tag{11}
\]
The value at the endpoint is unchanged by the counting jump at \(r\).

If an admissible family of these exact repairs has
\[
r=2p+o(p),\qquad s=2p+o(p),\qquad a_0>p,
\tag{12}
\]
then (2) implies \(a_0=p+o(p)\), and (11) yields
\[
E_{\mathcal Q}(r)=-\left(\frac12+o(1)\right)\frac1p.
\tag{13}
\]
Such a family would attain RE-261's leading sharp constant for counting budget one with finite, count-preserving integer modifications. However, (7) requires
\[
s-r>(2+o(1))\sqrt p,
\]
and the modulo-four second case requires \((\sqrt{12}+o(1))\sqrt p\). The integer divisibility and compositeness conditions remain as well. **No infinite family satisfying (12) and those conditions is proved here.** In particular, moving the compensator past quadratic height cannot repair a pair with gap \(o(\sqrt p)\).

This blocks a construction assembled from individually exact balanced repairs of square-root-close pairs. It does not block a product whose Euler debts cancel only across several pairs, or a larger inseparable deletion packet. Nor does the budget-one scale in (13) itself create an order-one Robin-normalized excursion: that requires a growing counting budget, with \(K\asymp\sqrt p/\log p\) in RE-261.

## 4. Exact controls, prior art, and evidence boundary

The product-height example already used in RE-262 is recovered by the test:
\[
(r,s)=(31,61),\quad a_0=21,\quad\delta=20,\quad k=1,
\qquad
\frac{31}{30}\frac{61}{60}=\frac{21}{20}\frac{1891}{1890}.
\]
A repair requiring a larger multiple is
\[
(r,s)=(13,19),\quad a_0=8,\quad\delta=1,\quad k=7,
\qquad
\frac{13}{12}\frac{19}{18}=\frac87\frac{1729}{1728}.
\tag{14}
\]
Both insertions in each example are distinct composites. By contrast, \((11,17)\) gives the algebraic repair \(\{7,561\}\), which duplicates the surviving prime seven and is not an admissible two-deletion source. The pair \((101,103)\) is rigid at every insertion height by (7).

As a supplementary exhaustive finite check, all 1,883 prime pairs
\(3\le r<s<500\), \(s<2r\), were tested using exact integer/rational arithmetic. Independently of the one-candidate test, clearing denominators gives
\[
(da-P)(db-P)=PQ.
\tag{15}
\]
For each pair, enumerate every positive divisor \(x\le\sqrt{PQ}\), put \(y=PQ/x\), and retain those with \(d\mid x+P\) and \(d\mid y+P\). This enumerates all unordered insertion pairs, with **no insertion-height truncation**, since every solution has \(da-P,db-P>0\). The resulting list agreed exactly with (3): 144 pairs had a nontrivial algebraic repair; all 386 pairs covered by (7)'s exclusion were rigid. Every retained identity was also checked with exact fractions. These finite checks audit the algebra and endpoint handling; the proof above establishes the universal result.

The method is elementary unique factorization, monotonicity, and completion of a bilinear equation to a divisor problem. None is claimed as a new general technique. A close classical comparison is Tieling Chen and Reginald Koo, [*Two-term Egyptian fractions*, Notes on Number Theory and Discrete Mathematics **19** (2013), no. 2, 15–25](https://www.nntdm.net/papers/nntdm-19/NNTDM-19-2-15-25.pdf), Section 2, Theorems 2–3, where a two-unit-fraction equation is classified by a shifted product and divisor congruences. Equation (15) is the analogous elementary factorization for a different rational-product equation; no Egyptian-fraction existence theorem is imported. The excluded denominator relation \(r\mid s-1\) is the classical prime-chain relation studied by Ford–Konyagin–Luca and already anchored by RE-262.

The line-specific delta beyond RE-262 is a **complete unbounded-height classification for two deletions**, reducing existence to one integer test and ruling out square-root-close deletion pairs even after the quadratic support barrier is removed. The literature comparison limits the claim to this derived source-fidelity application; it does not establish global novelty for the Diophantine classification.

The hypotheses are load-bearing: prime denominators are chain-free here because of the subdyadic odd-prime packet; integrality and exact equality are essential; there are at most two inserted labels. Real insertions, approximate normalization, extra insertions, larger coupled packets, and infinite completion are not excluded. The composite labels remain synthetic Euler atoms, not ordinary divisor-sum factors. No restriction on actual CA exponent vectors, no signed ordinary-prime tail estimate, and no Robin or RH conclusion follows.
