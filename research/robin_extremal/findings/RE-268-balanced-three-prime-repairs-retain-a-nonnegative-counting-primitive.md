# RE-268 — Balanced three-prime repairs retain a nonnegative counting primitive

**Status:** EXACT-DERIVED + ONE-SIDED-SOURCE-OBSTRUCTION; independent adversarial review pending.

**Dependencies:** RE-261 (counting representation of the transient Robin coordinate), RE-262 (prime-valuation support obstruction), RE-267 (the distinction between net counting budget and packet count).

The nonnegative weighted primitive behind RE-267 survives an independently matched **three-prime** packet, without requiring a decomposition into exact two-prime repairs. Consequently arbitrary finite, disjoint collections of these triples still cannot produce a positive critical Robin excursion at net counting budget `K = O(sqrt(p)/log(p))`. The bound obtained here is logarithmic suppression, not RE-267's stronger quadratic suppression for pairs.

## 1. Source statement

Let `p >= 3` be an ordinary prime. Modify the ordinary-prime source by finitely many disjoint repairs
\[
D_j=\{r_j<s_j<t_j<2r_j\},\qquad
B_j=\{a_j<b_j<c_j\},\qquad
\prod_{q\in B_j}\frac q{q-1}
=\prod_{q\in D_j}\frac q{q-1}.
\tag{1}
\]
Each `D_j` consists of ordinary odd primes; each `B_j` consists of distinct composite integers. All altered labels exceed `p`, and labels belonging to different repairs are disjoint. Put
\[
Q=\left(\mathbb P\setminus\bigcup_jD_j\right)\cup\bigcup_j B_j,
\quad A(x)=\Pi_Q(x)-\pi(x),\quad \sup_{x\ge p}|A(x)|\le K.
\tag{2}
\]
There is no bound on the number of repairs in terms of `K`. Define
\[
f(x)=\log\frac x{x-1},\qquad h(x)=\frac{f(x)}{\log x},
\qquad d\mu(x)=\frac{dx}{x(x-1)},
\]
\[
M(U)=\int_p^U A(x)\,d\mu(x),\qquad
E_Q(U)=\int_p^U\bigl(\vartheta_Q(x)-\vartheta_{\mathbb P}(x)\bigr)h'(x)\,dx,
\quad \vartheta_S(x)=\sum_{q\in S,\ q\le x}\log q.
\tag{3}
\]
Then
\[
\boxed{M(U)\ge0\quad(U\ge p),}
\qquad
\boxed{\sup_{U\ge p}E_Q(U)\le
\frac{K}{e(p-1)\log p}.}
\tag{4}
\]
The source has equal insertion/deletion counts and exact Mertens constant
\[
\Gamma(Q):=\lim_{x\to\infty}
\left(\sum_{q\in Q,\ q\le x}f(q)-\log\log x\right)=\gamma.
\tag{5}
\]
In particular,
\[
\sqrt p\log p\,\sup_U E_Q(U)
\le \frac{K\sqrt p}{e(p-1)}.
\tag{6}
\]
Thus `K=o(sqrt(p))` forces the positive normalized supremum to vanish. A positive excursion of normalized size at least `delta>0` requires
\[
\boxed{K\ge e\delta\frac{p-1}{\sqrt p}.}
\tag{7}
\]
At the unrestricted critical scale `K=O(sqrt(p)/log(p))`, the right side of (6) is `O(1/log(p))`. No optimality of the constant or of the new necessary scale is asserted. The same conclusions hold if disjoint exact subdyadic two-prime repairs are also included, since RE-267 supplies their nonnegative primitives.

## 2. A triple must insert before its first deletion

Suppress the packet index, write `D={r,s,t}`, `P=rst`, and
`V=(r-1)(s-1)(t-1)`. Write `F(x)=x/(x-1)` for the multiplicative Euler factor.

No prime in `D` divides another member's predecessor. Indeed, for odd primes `u,v` in this subdyadic packet, `u | v-1` would force `v-1=u`, contradicting oddness. Therefore `gcd(P,V)=1`, and every deleted prime divides at least one insertion numerator. This follows directly from taking its valuation in (1); insertion-denominator cancellation can only increase the required numerator valuation.

If every insertion numerator contained at most one deleted prime, the three primes and three insertions would be bijectively matched by divisibility. Monotonicity of `F` would then give
\[
\prod_{q\in B}F(q)\le\prod_{q\in D}F(q),
\]
with equality only for `B=D`, impossible for composite insertions. Thus one insertion contains at least two deleted prime factors. In particular
\[
c\ge rs>t.
\tag{8}
\]
We claim, additionally,
\[
\boxed{a<r.}
\tag{9}
\]
Suppose instead that every insertion is at least `r+1`; equality with `r` is impossible because insertions are composite.

**An insertion contains all three deleted primes.** Call it `z`; then `z>=P`. The other two insertions `x,y` obey
\[
F(x)F(y)=\frac{P}{V F(z)}\ge\frac{P-1}{V}.
\tag{10}
\]
The ratio `(rst-1)/((r-1)(s-1)(t-1))` decreases in each of `s,t`: its derivative with respect to `s` has the sign of `1-rt<0`, and similarly for `t`. Since `s,t<=2r-1`,
\[
\frac{P-1}{V}
\ge\frac{r(2r-1)^2-1}{4(r-1)^3}
>\left(\frac{r+1}{r}\right)^2=F(r+1)^2.
\tag{11}
\]
The numerator after clearing denominators in the strict comparison is
\[
r^2\{r(2r-1)^2-1\}-4(r+1)^2(r-1)^3
=(r-1)(9r^2-4)>0.
\]
But `x,y>=r+1` gives the opposite inequality, a contradiction.

**No insertion contains all three.** Choose an insertion `z` divisible by two deleted primes `u,v`; the remaining prime `w` divides a different insertion `y`. Hence `z>=uv` and `y>=w`. If `x` is the third insertion, equality implies
\[
F(x)=\frac{F(u)F(v)F(w)}{F(y)F(z)}
\ge\frac{F(u)F(v)}{F(uv)}
=1+\frac1{u-1}+\frac1{v-1}
\ge1+\frac1{r-1}>F(r+1).
\tag{12}
\]
Here `u,v<=2r-1` gives the penultimate inequality. Again `x>=r+1` is impossible. This completes (9). The argument covers overlapping prime divisibility among insertion numerators; no unique assignment of all prime factors is assumed.

## 3. Counting can cross sign only once

For one repair write
\[
A_j(x)=\#(B_j\cap(1,x])-\#(D_j\cap(1,x]).
\]
Equations (8)--(9) put the first event at an insertion before every deletion and put at least one insertion after every deletion. There is only one other insertion.

Before all three deletions have occurred, a negative counting value requires at least two deletions, because the first insertion is already present. At that point at most one insertion remains available before the last deletion: the far insertion is still beyond it. That available insertion can raise a negative value only to zero. After all deletions, the count cannot be positive because there are only three insertions in total. Thus `A_j` is nonnegative first and nonpositive afterwards, allowing zero intervals on either side; it is not claimed monotone.

Exact Euler matching and Abel summation give
\[
\int_p^\infty A_j\,d\mu
=\sum_{q\in B_j}f(q)-\sum_{q\in D_j}f(q)=0.
\tag{13}
\]
Before the sign change its partial integral is nonnegative. After the sign change it equals minus the nonpositive remaining tail. Consequently
\[
M_j(U)=\int_p^U A_j\,d\mu\ge0
\tag{14}
\]
for every cutoff. Summing proves the first part of (4). The combined `A` need not have one sign change; arbitrary interleaving is allowed because the primitives add.

## 4. Net counting budget gives the positive bound

For completeness, summation by parts yields
\[
\Delta\vartheta(U)=\log U\,A(U)-\int_p^U A(x)\frac{dx}{x},
\]
\[
\sum_{q\in Q,\ q\le U}f(q)-\sum_{q\in\mathbb P,\ q\le U}f(q)
=f(U)A(U)+M(U).
\]
Integration of (3) cancels the endpoint counting terms and gives
\[
E_Q(U)=-M(U)-h(U)\int_p^U A(x)\frac{dx}{x}
\le K h(U)\log(U/p).
\tag{15}
\]
These identities include cutoffs at altered labels. Use `f(U)<=1/(U-1)`, `log(U)>=log(p)`, and `U-1>=(p-1)U/p`. With `v=U/p>=1`,
\[
h(U)\log(U/p)
\le\frac{\log v}{v(p-1)\log p}
\le\frac1{e(p-1)\log p}.
\tag{16}
\]
This proves the remaining assertions. Only the **net** budget in (2) is used, not a sum of packet budgets. Also `E_Q(infinity)=0` by finite exact matching, so its supremum is nonnegative; (4) is not a global nonpositivity claim.

## 5. Exact controls and evidence boundary

A genuine three-deletion repair is
\[
D=\{19,23,29\},\qquad B=\{15,16,12673\},\qquad12673=19\cdot23\cdot29.
\tag{17}
\]
All insertions are distinct composites and `29<2*19`. The identity can be checked in two exact steps:
\[
\prod_{q\in D}F(q)=F(8)F(12673),\qquad F(8)=F(15)F(16).
\]
For prefix `p=13`, its event counts are `1,2,1,0,-1,0`. It has net budget two. Its three prime deletions cannot be partitioned into disjoint two-deletion repairs. This verifies that the larger class is not merely a relabelling of the pair class; no infinite prime-supply claim follows from this example.

Supplementary exact enumeration considered all 79 odd-prime triples `5<=r<s<t<60` with `t<2r`, and found 294 distinct-composite three-label repairs. For each possible smallest insertion `4<=a<t`, divide the deleted Euler product by `F(a)` and reduce it to `P_0/Q_0>1`. The remaining two labels obey
\[
((P_0-Q_0)b-P_0)((P_0-Q_0)c-P_0)=P_0Q_0.
\tag{18}
\]
Enumerating positive divisors therefore checks all such `b<c` without a height cutoff. The upper bound `a<t` is exhaustive because otherwise all three factors would be at most `F(t)`, strictly smaller in product than the deleted factors. Exact rational arithmetic verified every Euler identity, (8)--(9), the single-crossing count property, and `exp(M_j(U))>=1` at every event. Between events the primitive is monotone, so these endpoint tests also cover the finite controls' intervals. Independent 40- and 80-digit evaluations checked the atom formula against (15) and verified (4) at events, intervening midpoints and twice the final insertion. Those logarithmic calculations are diagnostics, not interval certificates; the general proof is (8)--(16).

Unique factorization, monotonicity, and the one-sign-change/zero-integral argument are classical. The discrepancy integration has the same prior-art boundary as RE-261 and RE-267: C. Aistleitner and J. Dick, [*Functions of bounded variation, signed measures, and a general Koksma--Hlawka inequality*, Acta Arithmetica **167** (2015), 143--171](https://arxiv.org/abs/1406.0230). The finite validation's shifted-product method is analogous to the classical two-variable rational-equation analysis in T. Chen and R. Koo, [*Two-term Egyptian fractions*, Notes on Number Theory and Discrete Mathematics **19** (2013), 15--25](https://www.nntdm.net/papers/nntdm-19/NNTDM-19-2-15-25.pdf), Section 2. Neither source is asserted to contain this triple-repair theorem. Searches by finite Euler-product matching, prime-factor valuation, majorization and single-crossing primitives support only this derived source-specific statement, not a global novelty claim for the general techniques.

The substantive extension is that **three** coupled deletions do not yet escape the primitive obstruction, even after unbounded packet count and interleaving are allowed. Integrality, the subdyadic prime packet, exact individual matching, and the bound of three deletions are used. Four or more coupled deletions, prime-chain packets outside the subdyadic range, merely global matching without a packet decomposition, approximate matching, and infinite modifications remain outside the theorem. The proof does not import the pair class's delayed positivity or its `O(K/p^2)` bound.

Composite labels carry synthetic Euler factors, not their ordinary divisor-sum factors. No restriction on actual CA exponent vectors, ordinary-prime signed tail, Robin inequality, or RH is established. The remaining source question is whether larger inseparable packets can violate the nonnegative primitive or realize positive critical excursions while retaining all the other source constraints.
