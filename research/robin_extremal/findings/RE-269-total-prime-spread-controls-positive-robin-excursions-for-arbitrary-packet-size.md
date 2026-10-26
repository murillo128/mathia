# RE-269 — Total prime spread controls positive Robin excursions for arbitrary packet size

**Status:** EXACT-DERIVED + ONE-SIDED-SOURCE-OBSTRUCTION + CLASSICAL-CONVEX-ORDER-MECHANISM; independent adversarial review pending.

**Dependencies:** RE-262 (the forced insertion divisible by two deleted primes), RE-261 (the counting representation), RE-267--RE-268 (the positive-excursion question for balanced pairs and triples).

Balanced packets need not have only two or three deletions to retain a nonnegative weighted counting primitive. A quantitative condition on the **total spread of their deleted Euler logarithms** suffices at arbitrary, even growing, packet size. The proof uses the distant insertion forced by prime valuations and a finite convex-order comparison, rather than a bound on the number of counting sign changes. Failure of this sufficient condition is not evidence of an integer repair with a negative primitive.

## 1. Packet and source theorem

Let `p >= 3` be an ordinary prime. Consider finitely many disjoint, individually exact repairs
\[
D_j=\{r_j=q_{j,1}<q_{j,2}<\cdots<q_{j,m_j}<2r_j\},
\qquad |B_j|=m_j\ge2,
\qquad
\prod_{b\in B_j}\frac b{b-1}
=\prod_{q\in D_j}\frac q{q-1}.
\tag{1}
\]
The deletions are ordinary odd primes, the insertions are distinct composite integers, and all altered labels exceed `p`. Different packets have disjoint labels. There is no fixed upper bound on either `m_j` or the number of packets. Set
\[
Q=(\mathbb P\setminus\bigcup_jD_j)\cup\bigcup_j B_j,
\qquad A(x)=\Pi_Q(x)-\pi(x),\qquad |A(x)|\le K\quad(x\ge p).
\tag{2}
\]
Write
\[
f(x)=\log\frac x{x-1},\quad h(x)=\frac{f(x)}{\log x},
\quad d\mu(x)=\frac{dx}{x(x-1)},
\]
\[
M(U)=\int_p^U A\,d\mu,\qquad
E_Q(U)=\int_p^U(\vartheta_Q(x)-\vartheta_{\mathbb P}(x))h'(x)\,dx,
\quad\vartheta_S(x)=\sum_{q\in S,\ q\le x}\log q.
\tag{3}
\]
For each packet define quantities depending only on its deleted primes:
\[
c_j=f(r_jq_{j,2}),\qquad S_j=\sum_{q\in D_j}f(q),
\qquad z_j=\frac{S_j-c_j}{m_j-1},
\qquad \delta_j=\sum_{q\in D_j}(f(q)-z_j)_+.
\tag{4}
\]
Then, for every finite `U >= p`,
\[
\boxed{M(U)\ge-\sum_j\delta_j,\qquad
E_Q(U)\le\sum_j\delta_j+\frac{K}{e(p-1)\log p}.}
\tag{5}
\]
In particular, the explicit spread condition
\[
\boxed{\sum_{q\in D_j}\bigl(f(r_j)-f(q)\bigr)
\le f(r_j)-f(r_jq_{j,2})\quad\text{for every }j}
\tag{6}
\]
is equivalent to `z_j >= f(r_j)`, and makes every `delta_j` zero. Consequently
\[
\boxed{M(U)\ge0,\qquad
\sqrt p\log p\,\sup_{U\ge p}E_Q(U)
\le\frac{K\sqrt p}{e(p-1)}.}
\tag{7}
\]
At `K=O(sqrt(p)/log(p))`, the positive normalized supremum is `O(1/log(p))`, regardless of packet cardinality or interleaving. More generally it vanishes if `K=o(sqrt(p))` and `sqrt(p)log(p) sum_j delta_j=o(1)`. The bound uses the **net** counting budget, not a sum of individual packet budgets.

Finite exact matching also gives eventual zero count and
\[
\Gamma(Q)=\lim_{x\to\infty}
\left(\sum_{q\in Q,\ q\le x}f(q)-\log\log x\right)=\gamma,
\qquad E_Q(\infty)=0.
\tag{8}
\]
No optimality for the source-class constant in (5) or (7) is claimed.

## 2. Prime valuations force one small Euler logarithm

For one packet suppress `j` and put `r=q_1`, `s=q_2`, `m=|D|`. Since all deletions are odd primes in `[r,2r)`, no deleted prime divides another's predecessor: `q | q'-1` would force `q'=q+1`, an even number greater than two. Thus each deleted prime has valuation one in the reduced deleted Euler product. Taking valuations in (1) forces it to divide an insertion numerator.

If every insertion numerator contained at most one deleted prime, equal cardinality would bijectively match the deleted primes to the insertion labels by divisibility. Each corresponding label would be at least that prime. Strict decrease of `x/(x-1)` and equality of the products would force all corresponding labels to equal their primes, contradicting compositeness. This reconstructs the RE-262 argument, including possible insertion-denominator cancellation: such cancellation only increases the required numerator valuation.

Therefore at least one insertion `b_*` contains two deleted prime factors, and
\[
b_*\ge rs,\qquad f(b_*)\le c:=f(rs)<\min_{q\in D}f(q).
\tag{9}
\]
The proof below uses just this one forced small Euler logarithm; it does not assign the other prime factors or assume a decomposition into smaller repairs.

## 3. The exact comparison in the one-small-coordinate relaxation

Let `d_1,...,d_m > c > 0`, let `S=sum_i d_i`, and set
\[
z=\frac{S-c}{m-1}>\min_i d_i,\qquad
\delta=\sum_i(d_i-z)_+.
\]
For any positive vector `y_1,...,y_m` with the same sum `S` and at least one coordinate at most `c`, define
\[
H(t)=\sum_i(y_i-t)_+-\sum_i(d_i-t)_+.
\]
The three elementary lower bounds for the first sum are `0`, `S-mt`, and `S-c-(m-1)t`. The last follows by omitting the coordinate at most `c` and replacing each remaining positive part by its argument. Their maximum is exactly
\[
\sum_i(y_i-t)_+\ge
(c-t)_++(m-1)(z-t)_+.
\tag{10}
\]
This is also Jensen's inequality after fixing the small coordinate. Equality for every `t` is attained by the vector `(c,z,...,z)`.

Subtract the deleted-vector hinge sum from the right side of (10). For `t <= c` the difference is zero. On `[c,min_i d_i]` it equals `t-c` and is nonnegative. Between `min_i d_i` and `z`, its derivative wherever defined is
\[
-(m-1)+\#\{i:d_i>t\}\le0.
\]
Above `z` its derivative is `#{i:d_i>t}>=0`. Its global minimum is therefore the value at `z`, namely `-delta`, or the same zero value outside the support when `delta=0`. Hence
\[
\boxed{H(t)\ge-\delta\quad(t\ge0).}
\tag{11}
\]
This lower bound is exact in the positive-vector relaxation. In particular, all equal-sum completions with one coordinate at most `c` satisfy `H>=0` **if and only if**
\[
z\ge\max_i d_i.
\tag{12}
\]
If (12) fails, the vector `(c,z,...,z)` has `H(z)=-delta<0`. Small distinct perturbations of its `m-1` repeated entries, preserving their sum, retain a negative value. This is a sharp statement about the relaxation, not about existence of an integer Euler-product repair.

Apply (11) with `d_i=f(q_i)` and `y_i=f(b_i)`. Exact Euler matching gives equal sums and (9) supplies the small coordinate. For `t=f(U)`, each altered label contributes
\[
\int_p^U\mathbf1_{[b,\infty)}(x)\,d\mu(x)
=(f(b)-f(U))_+,
\]
so `H(f(U))` is precisely the packet's counting primitive. Summing over packets proves the first part of (5). Equation (12) gives (6). No one-sign-change property of the counting path is required.

For completeness, the endpoint-cancelled counting identity is
\[
E_Q(U)=-M(U)-h(U)\int_p^U\frac{A(x)}x\,dx.
\tag{13}
\]
It follows from partial summation of the Euler-log sum and of `Delta vartheta`, using `h(U)log(U)=f(U)`. Thus
\[
E_Q(U)\le\sum_j\delta_j+Kh(U)\log(U/p).
\]
Finally, with `v=U/p>=1`,
\[
h(U)\log(U/p)
\le\frac{\log v}{v(p-1)\log p}
\le\frac1{e(p-1)\log p}.
\tag{14}
\]
Here `f(U)<=1/(U-1)` and `U-1>=(p-1)U/p`. This proves the remaining source bounds, including cutoffs at altered labels.

## 4. An elementary geometric sufficient condition

A condition with no logarithms is
\[
\boxed{\sum_{q\in D}(q-r)\le r-2.}
\tag{15}
\]
Indeed
\[
\sum_{q\in D}(f(r)-f(q))
\le\frac{\sum_{q\in D}(q-r)}{r(r-1)},
\]
whereas `s>r` and elementary logarithmic bounds give
\[
r(r-1)(f(r)-f(rs))
>r(r-1)\left(\frac1r-\frac1{r^2-1}\right)
=r-2+\frac1{r+1}.
\tag{16}
\]
Thus (15) implies (6). It also forces the deletion packet to be subdyadic. For a packet in `[r,r+H]`, the simpler `(m-1)H<=r-2` suffices. Consequently every fixed-cardinality coalescing packet satisfies this certificate eventually, and growing packets do too whenever `mH=o(r)`. This is a conditional restriction on any exact repair of such packets, not a prime-supply theorem on shrinking intervals.

## 5. Exact controls and the surviving boundary

A four-deletion example not decomposable into smaller balanced exact repairs is
\[
D=\{17,19,23,29\},\qquad B=\{8,33,34,12673\},
\qquad p=7.
\tag{17}
\]
It follows by combining the two identities
\[
F(17)=F(33)F(34),\qquad
F(19)F(23)F(29)=F(8)F(12673),\quad
F(x)=\frac{x}{x-1},\quad12673=19\cdot23\cdot29.
\]
Both sides of (1) equal `215441/177408`. The spread condition (6) is certified without floating-point logarithms by
\[
\frac{\prod_{q\in D}F(q)}{F(17\cdot19)F(17)^3}
=\frac{490912}{486387}>1.
\tag{18}
\]
The event counts are `1,0,-1,-2,-3,-2,-1,0`, so `K=3`. The 68 comparisons of products over nonempty proper equal-cardinality subsets of `D` and `B` give no equality. This is a finite exact certificate of indecomposability into balanced subrepairs, not an infinite existence claim. Direct rational evaluation of `exp(M(U))` at all eight events gives values at least one; monotonicity between events completes this check. The general proof is (9)--(14), not the example.

The distant-atom condition alone does not force the sign in the distinct-real-label source class. For
\[
D=\{101,179,181,191\},\qquad
B=\left\{110,115,\frac{493639309}{4139309},18079\right\},
\qquad p=97,
\tag{19}
\]
exact rational multiplication gives equal Euler products and equal cardinalities. The last label is `101*179`, and every insertion is greater than `105`. At `U=105`,
\[
\exp(M(105))=\frac{2625}{2626}<1,\qquad
E_Q(105)=\log(101)[h(101)-h(105)]>0.
\tag{20}
\]
The deleted packet remains subdyadic. Its spread fails (6). One inserted label is nonintegral; (19) is explicitly **not** an integer counterexample to any stronger source theorem. It demonstrates why a support argument alone, without more information on the remaining coordinates, cannot replace the comparison condition.

Supplementary exact rational checks tested (10)--(12) on 2480 positive-vector pairs, with sizes `2` through `32`, at their coordinate breakpoints, `c`, `z`, and intervening midpoints: 157288 cutoff tests passed. These vectors test the elementary comparison, not prime-source realization. The displayed source identities, (18), and (20) were checked with rational arithmetic. No numerical search supplies an asymptotic claim.

## 6. Prior art and research consequence

The positive-part comparison is classical convex order/majorization, not a new general inequality. Ludwig Baringhaus and Rudolf Grübel, [*Nonparametric two-sample tests for increasing convex order*, Bernoulli **15** (2009), 99--123, DOI `10.3150/08-BEJ151`](https://www.ivfm.uni-hannover.de/fileadmin/stochastik/Publications/Gruebel/rg_Nonparametric_two_sample_test.pdf), equations (1.2)--(1.5), state the convex-order comparison through positive-part expectations and integrated survival functions. Equation (10) is the elementary fixed-sum extremizer behind that comparison. The counting/variation bridge has the prior-art boundary already recorded in RE-261: Aistleitner and Dick, [*Functions of bounded variation, signed measures, and a general Koksma--Hlawka inequality*](https://arxiv.org/abs/1406.0230). Neither source is claimed to contain the prime-packet theorem here.

The mathematical delta is the arithmetic use of the forced quadratic insertion to obtain a **deletion-only spread certificate and quantitative deficit for packets of unrestricted size**, including repairs not partitionable into balanced pairs or triples. This is not a claim that arbitrary larger subdyadic packets have a nonnegative primitive. The relaxed comparison is exact, but extra valuation and integrality constraints could strengthen it; failure of (6) does not prove an integer escape. No global novelty claim for the general comparison method follows from the literature search.

In particular, increasing the coupled packet size does not evade the positive-excursion obstruction when total prime spread satisfies (6), or when the total deficit in (5) is negligible at Robin scale. A remaining integer escape must defeat this dispersion certificate, use prime-chain packets outside the subdyadic class, abandon individual exact matching, or change another stated hypothesis. The pair class still has its stronger quadratic-height bound from RE-267; no such bound is proved here.

All composite insertions carry synthetic factors `q/(q-1)`, not their ordinary divisor-sum contributions. The result supplies no new restriction on actual CA exponent vectors, no estimate of the CA-selected ordinary-prime signed tail, and no Robin inequality or RH conclusion.
