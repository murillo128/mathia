# RE-273 — First insertion classifies three-prime repairs without a prime-chain hypothesis

**Status:** EXACT-DERIVED + FINITE-SOURCE-OBSTRUCTION + CLASSICAL-CONVEX-ORDER-MECHANISM; independent adversarial review pending.

**Dependencies:** RE-262 (prime-valuation obstruction), RE-268 (subdyadic triple positivity), RE-272 (arbitrary-spread pair positivity and the surviving triple question).

For an exactly Euler-matched three-prime repair, nonnegativity of the weighted counting primitive is equivalent to placing the first insertion before the first deletion. This is an exact classification of the primitive's sign property, not a classification of which insertion triples exist. An explicit **chain-free** triple violates the property at absolute counting budget one. Thus prime-predecessor cancellation is not necessary for the failure found in RE-272: removing all prime-chain edges does not rescue the triple sign theorem once deletion spread is unrestricted.

## 1. Source class and classification

Let `p >= 3` be an ordinary prime. Let
\[
D=\{r<s<t\},\qquad B=\{a<b<c\}
\]
be respectively distinct ordinary primes and distinct composite integers, with every label greater than `p`. Suppose
\[
\prod_{q\in D}F(q)=\prod_{z\in B}F(z),\qquad
F(x)=\frac{x}{x-1},\quad f(x)=\log F(x).
\tag{1}
\]
No restriction on prime-chain relations or deletion spread is imposed. Define
\[
A(x)=\#(B\cap(-\infty,x])-\#(D\cap(-\infty,x]),
\qquad M(U)=\int_p^U\frac{A(x)}{x(x-1)}\,dx.
\tag{2}
\]
Then
\[
\boxed{M(U)\ge0\text{ for every }U\ge p\quad\Longleftrightarrow\quad a<r.}
\tag{3}
\]
In particular, if `a>r`, the negative primitive already appears immediately after the first deletion; it cannot first arise as a hidden later dip in a triple whose first insertion was early. The equality `a=r` is excluded by compositeness.

## 2. The last insertion and the three-coordinate comparison

The largest deleted prime cannot cancel against any deleted predecessor, so
\[
v_t\left(\prod_{q\in D}F(q)\right)=1.
\]
Taking valuations in (1) yields
\[
\sum_{z\in B}v_t(z)=1+\sum_{z\in B}v_t(z-1)\ge1.
\]
Some composite insertion is a multiple of `t`; consequently
\[
c\ge2t>t.
\tag{4}
\]
This argument does not require `D` to be chain-free.

Since `f'(x)=-1/(x(x-1))`, direct integration of the finite counting steps gives
\[
M(U)=\sum_{z\in B}(f(z)-f(U))_+
      -\sum_{q\in D}(f(q)-f(U))_+.
\tag{5}
\]
Set the decreasing vectors `x=(f(a),f(b),f(c))` and `y=(f(r),f(s),f(t))`. They have the same sum `S` by (1). If `a<r`, then
\[
x_1>y_1,\qquad x_3<y_3,\qquad
x_1+x_2=S-x_3>S-y_3=y_1+y_2.
\tag{6}
\]
For any decreasing three-vector `z` of sum `S` and any real `v`,
\[
\sum_{j=1}^3(z_j-v)_+
=\max\{0,z_1-v,z_1+z_2-2v,S-3v\}.
\tag{7}
\]
Each corresponding entry for `x` is at least the one for `y`; using `v=f(U)` proves sufficiency in (3), including all event cutoffs. This is the elementary three-coordinate majorization calculation.

Conversely, if `a>r`, choose `r<U<min(a,s)`. Only the deletion at `r` has occurred, and
\[
M(U)=f(U)-f(r)<0.
\tag{8}
\]
This proves necessity. Exact matching also gives `M(infinity)=0`, which does not prevent (8).

## 3. A chain-free unit-budget counterexample

Take
\[
p=3,\qquad D=\{5,43,103\},\qquad
B=\{6,14,1439425\}.
\tag{9}
\]
All insertions are composite, including
\[
1439425=65\cdot5\cdot43\cdot103=5^2\cdot13\cdot43\cdot103.
\]
There are no prime-chain edges among the deletions:
\[
5\nmid42,\quad5\nmid102,\quad43\nmid102.
\tag{10}
\]
The matching is exact:
\[
\prod_{q\in D}F(q)=\frac{22145}{17136},\qquad
F(6)F(14)=\frac{84}{65},\qquad
\frac{22145/17136}{84/65}=\frac{1439425}{1439424}.
\tag{11}
\]
At the ordered events `5,6,14,43,103,1439425`, the count values are
\[
-1,0,1,0,-1,0.
\]
Thus `sup |A|=1`, yet
\[
\boxed{\exp M(6)=\frac{F(6)}{F(5)}=\frac{24}{25}<1.}
\tag{12}
\]
The forced multi-prime insertion of RE-262 is present, indeed containing all three deleted primes. That distant support is insufficient to control the primitive without the deletion geometry used in RE-268 and RE-271. There is no contradiction to either finding because `103>2*5`.

The packet cannot decompose into proper independently exact balanced repairs. Any proper part has one or two deletions; RE-272 makes its primitive nonnegative, so a decomposition would contradict (12). The 18 proper equal-cardinality subset-product comparisons also verify this directly.

## 4. Robin-coordinate consequence and its limit

For the synthetic source `Q=(P\D) union B`, where `P` is the ordinary-prime set, put
\[
h(x)=\frac{f(x)}{\log x},\quad
\Delta\vartheta(x)=\sum_{q\in Q,\ q\le x}\log q-
                         \sum_{q\in P,\ q\le x}\log q,
\quad E_Q(U)=\int_p^U\Delta\vartheta(x)h'(x)\,dx.
\]
In (9), only the deletion at 5 contributes on the open interval `(5,6)`, so
\[
E_Q(6)=\log5\,[h(5)-h(6)]>0.
\tag{13}
\]
Here `h'<0` follows from `f>0` and `f'<0`. Both `E_Q(infinity)=0` and preservation of the ordinary Mertens constant follow from finite exact matching. They do not force a transient sign.

For the positive side of (3), arbitrary finite disjoint collections of exactly matched triples with `min B_j<min D_j` have `M=sum_j M_j>=0`, regardless of deletion spread or chain relations. With a common unchanged prefix through `p` and net counting bound `|A|<=K`, partial summation gives the already established bridge
\[
E_Q(U)=-M(U)-h(U)\int_p^U\frac{A(x)}x\,dx
\le K h(U)\log(U/p).
\]
Using `f(U)<=1/(U-1)` and `max_(v>=1) log(v)/v=1/e` yields
\[
\sqrt p\log p\sup_{U\ge p}E_Q(U)
\le\frac{K\sqrt p}{e(p-1)}.
\tag{14}
\]
The estimate is not new; (3) identifies exactly which individual triples supply its nonnegative-primitive premise. A globally matched source need not decompose into such triples, and cancellation between packets can make their sum nonnegative even when an individual primitive fails. No converse for the superposed source is claimed.

## 5. Exact audit and prior-art boundary

The counterexample uses rational arithmetic only:

```python
from fractions import Fraction as Q
from itertools import combinations
from math import prod, isqrt

def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))

def F(n):
    return Q(n, n-1)

def euler(xs):
    return prod(map(F, xs))

D, B = (5, 43, 103), (6, 14, 1439425)
assert all(map(prime, D)) and all(not prime(b) for b in B)
assert min(D+B) > 3 and len(set(D+B)) == 6
assert all((v-1) % u for u, v in combinations(D, 2))
assert B[-1] == 65*prod(D)
assert euler(D) == euler(B) == Q(22145, 17136)
assert [sum(b <= u for b in B)-sum(q <= u for q in D)
        for u in sorted(D+B)] == [-1, 0, 1, 0, -1, 0]
assert F(6)/F(5) == Q(24, 25) < 1
assert all(euler(ds) != euler(bs)
           for k in (1, 2)
           for ds in combinations(D, k) for bs in combinations(B, k))
```

A supplementary exact audit covered all 286 prime triples `5<=r<s<t<50` and all their distinct composite insertion triples with labels above 3, without an insertion-height cutoff. The smallest insertion must be below `t`, since otherwise its Euler product is smaller than `F(t)^3<F(r)F(s)F(t)`. For each composite `4<=a<t`, write the reduced residual `F(r)F(s)F(t)/F(a)=P/V>1` and `d=P-V`. The remaining labels satisfy
\[
(db-P)(dc-P)=PV.
\tag{15}
\]
Both factors are positive because `P/d=bc/(b+c-1)<b,c`. Enumerating the positive divisor pairs of `PV`, requiring the two congruences modulo `d`, and retaining `a<b<c` composite therefore exhausts this finite deletion domain with no bound on `c`. It found 811 repairs: 806 with a nonnegative primitive and five with a negative primitive, one of the latter chain-free. Every repair satisfied (3) and (4). All 4866 event-cutoff checks used exact values
\[
\exp M(U)=
\frac{\prod_{b\in B,\ b\le U}(F(b)/F(U))}
     {\prod_{q\in D,\ q\le U}(F(q)/F(U))}.
\]
Between events the derivative has constant sign, so these event checks also certify the finite examples' entire primitives. The proof of (3) is (4)--(8), not the enumeration.

The positive-part comparison is classical convex order: Baringhaus and Grübel, [*Nonparametric two-sample tests for increasing convex order*, Bernoulli **15** (2009), 99--123](https://www.ivfm.uni-hannover.de/fileadmin/stochastik/Publications/Gruebel/rg_Nonparametric_two_sample_test.pdf), equations (1.2)--(1.5). Formula (7) explicitly proves the small-dimensional step used here. The prime-chain relation is classical in Ford, Konyagin and Luca, [*Prime chains and Pratt trees*](https://arxiv.org/abs/0904.0473), Section 1.1. The shifted-product enumeration is the same elementary Diophantine mechanism compared in RE-263 and RE-272 with Chen and Koo, [*Two-term Egyptian fractions*](https://www.nntdm.net/papers/nntdm-19/NNTDM-19-2-15-25.pdf), Section 2; their equation is different and no existence theorem is imported.

A targeted comparison by Euler-factor replacement, totient ratios, convex order, prime-chain cancellation and the exact numerical identity did not identify an external source for this repair-specific statement. That does not establish global novelty. The durable delta is the exact triple sign criterion and the chain-free unit-budget failure, which closes the proposed replacement of subdyadic geometry by absence of prime-chain edges. The general majorization mechanism and the bound (14) are not claimed as new.

The counterexample is finite. It supplies neither an unbounded family of such prime triples nor replication at large frontiers, and therefore no order-one positive normalized excursion at critical counting budget. Approximate Euler matching, infinite repairs and real insertion labels are outside (3). Composite insertions are synthetic Euler atoms `b/(b-1)`, not ordinary divisor-sum factors. No CA realization, selected ordinary-prime tail estimate, Robin counterexample or RH consequence is established.
