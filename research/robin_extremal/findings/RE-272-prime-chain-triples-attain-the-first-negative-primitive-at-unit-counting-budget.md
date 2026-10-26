# RE-272 — Prime-chain triples attain the first negative primitive at unit counting budget

**Status:** EXACT-DERIVED + SHARP-PACKET-CARDINALITY + FINITE-SOURCE-OBSTRUCTION; independent adversarial review pending.

**Dependencies:** RE-262 (prime-chain denominator cancellation), RE-267 (counting-primitive bridge), RE-268 (subdyadic triple positivity), RE-270--RE-271 (the subdyadic cardinality and surplus boundaries).

Without a restriction on the spread of deleted primes, **three deletions are the exact minimum for a negative counting primitive** in a finite, exactly Euler-matched, count-preserving integer source repair. Every two-prime repair retains a nonnegative primitive, including prime-chain pairs. A three-prime chain already fails at absolute counting budget one. Thus the subdyadic restriction in RE-271 cannot be removed while retaining its surplus-one conclusion, but prime-chain divisibility alone does not defeat the two-prime sign theorem.

## 1. Source class and sharp statement

Let `p >= 3` be an ordinary prime. Let `D` be a finite set of distinct ordinary primes and `B` a set of distinct composite integers, all greater than `p`, with
\[
|D|=|B|=m,\qquad
\prod_{b\in B}F(b)=\prod_{q\in D}F(q),
\qquad F(x)=\frac{x}{x-1},\quad f(x)=\log F(x).
\tag{1}
\]
No ratio bound on the deletion support is assumed. For the synthetic source
\[
\mathcal Q=(\mathbb P\setminus D)\cup B,
\]
define
\[
A(x)=\#\{b\in B:b\le x\}-\#\{q\in D:q\le x\},
\qquad M(U)=\int_p^U\frac{A(x)}{x(x-1)}\,dx.
\tag{2}
\]
Finite support and (1) give `A(infinity)=0` and `M(infinity)=0`. The precise conclusions are:

- For `m <= 2`, every such repair has `M(U) >= 0` for all `U >= p`.
- For `m = 3`, a repair with `sup |A| = 1` can have `M(U) < 0`.

The second statement is a finite exact witness, not an infinite supply theorem or an asymptotic positive Robin excursion.

## 2. The largest deleted prime closes every two-prime escape

Suppose `D={r,s}`, with `p<r<s`, and write the insertion labels as `a,b`. The larger prime cannot cancel against a deleted predecessor, regardless of whether `r | s-1`:
\[
v_s\!\left(\frac{rs}{(r-1)(s-1)}\right)=1.
\]
Equality (1) therefore forces
\[
v_s(a)+v_s(b)=1+v_s(a-1)+v_s(b-1)\ge1.
\tag{3}
\]
After relabelling, `s | b`. If `b=s`, strict monotonicity of `F` forces `a=r`, the trivial replacement. Otherwise `b >= 2s > s`, so
\[
F(a)=\frac{F(r)F(s)}{F(b)}>F(r),
\qquad a<r.
\]
Every nontrivial integer repair thus has the order
\[
\boxed{p<a<r<s<b.}
\tag{4}
\]
This argument needs only the valuation of the **largest** prime. The stronger conclusion that `b` contains both deleted primes can fail in a chain and is unnecessary for (4).

The counting path is `+1` on `[a,r)`, `-1` on `[s,b)`, and zero elsewhere. Exact matching gives `f(a)+f(b)=f(r)+f(s)`, hence
\[
M(U)=
\begin{cases}
0,&U<a,\\
f(a)-f(U),&a\le U<r,\\
f(a)-f(r),&r\le U<s,\\
f(U)-f(b),&s\le U<b,\\
0,&U\ge b.
\end{cases}
\tag{5}
\]
All five branches are nonnegative, including their continuous endpoint values. A one-deletion balanced repair is trivial by injectivity of `F`. This proves the lower cardinality bound without a subdyadic or chain-free assumption.

For example, the non-subdyadic identity
\[
F(11)F(23)=F(9)F(46)=\frac{23}{20}
\tag{6}
\]
has `11 | 23-1`, composite insertions, prefix `p=7`, and `b=46<11*23`. It loses the quadratic insertion scale but retains (5). Thus the removed hypothesis is not vacuous.

## 3. A three-prime chain with a negative primitive

Take
\[
p=7,\qquad D=\{11,23,47\},\qquad
B=\{12,14,6721\},\qquad 6721=11\cdot13\cdot47.
\tag{7}
\]
The deletions are prime, the insertions are distinct composites, and every altered label exceeds the unchanged prefix. The chain relations are
\[
23-1=2\cdot11,\qquad47-1=2\cdot23.
\]
They collapse the deleted Euler product to
\[
F(11)F(23)F(47)=\frac{47}{40}.
\tag{8}
\]
For the insertions,
\[
F(12)F(14)=\frac{168}{143},\qquad
\frac{47/40}{168/143}=\frac{6721}{6720}=F(6721).
\tag{9}
\]
This reconstructs exact matching, rather than fitting it numerically. The event counts are

| Event | 11 | 12 | 14 | 23 | 47 | 6721 |
|---|---:|---:|---:|---:|---:|---:|
| `A` | -1 | 0 | 1 | 0 | -1 | 0 |

Consequently `sup |A| = sup A = 1`. On `11<U<=12`,
\[
M(U)=f(U)-f(11)<0,
\qquad
\boxed{\exp M(12)=\frac{120}{121}<1.}
\tag{10}
\]
Together with (5), this proves the exact minimum cardinality three. It also attains the smallest possible positive counting surplus: any nontrivial finite exact repair must have `A>0` somewhere, since otherwise the positive weight in (2) would give `M(infinity)<0`. For integer counts that surplus is at least one.

The packet cannot partition into proper, individually exact, balanced subrepairs. Any such part would have at most two deletions and hence a nonnegative primitive by Section 2; summing would contradict (10). The 18 proper equal-cardinality subset-product comparisons independently verify this finite indecomposability.

The largest-prime argument still forces an insertion divisible by 47, as (7) provides. With three coordinates, however, that distant insertion no longer forces an insertion below the smallest deletion. All three insertions here exceed 11. The negative initial segment is therefore compatible with the surviving valuation information.

## 4. Robin consequence and the surviving pair obstruction

Use the same transient Robin source coordinate as RE-267:
\[
h(x)=\frac{f(x)}{\log x},\qquad
\Delta\vartheta(x)=\sum_{q\in\mathcal Q,\ q\le x}\log q
-\sum_{q\in\mathbb P,\ q\le x}\log q,
\qquad E_{\mathcal Q}(U)=\int_p^U\Delta\vartheta(x)h'(x)\,dx.
\tag{11}
\]
For (7), only the deletion at 11 contributes before 12, so
\[
E_{\mathcal Q}(12)=\log(11)\,[h(11)-h(12)]>0.
\tag{12}
\]
The sign is exact because `f>0`, `f'<0`, and thus `h'<0`. Both `M(infinity)=0` and `E_Q(infinity)=0` still hold. Exact finite matching also preserves the Mertens constant `Gamma(Q)=gamma`. None of these terminal equalities controls the transient sign.

In contrast, form a source from any finite number of disjoint, individually exact **two-prime** repairs, now with arbitrary deletion spread and prime-chain relations allowed. Assume only a net counting bound `|A(x)| <= K`; the number of repairs need not be bounded by `K`. Equation (5) gives `M=sum_j M_j >= 0`. Partial summation yields
\[
\Delta\vartheta(U)=\log U\,A(U)-\int_p^U\frac{A(x)}x\,dx,
\qquad
\sum_{b\le U}f(b)-\sum_{q\in D,\ q\le U}f(q)=f(U)A(U)+M(U).
\]
Since `h(U)log U=f(U)`, integration by parts in (11) cancels the endpoint count:
\[
E_{\mathcal Q}(U)=-M(U)-h(U)\int_p^U\frac{A(x)}x\,dx
\le K h(U)\log(U/p).
\tag{13}
\]
Writing `v=U/p>=1`, the inequalities `f(U)<=1/(U-1)`, `U-1>=(p-1)v`, and `log U>=log p` give
\[
h(U)\log(U/p)\le\frac{\log v}{v(p-1)\log p}
\le\frac1{e(p-1)\log p}.
\]
Therefore, throughout this larger pair class,
\[
\boxed{\sqrt p\log p\,\sup_{U\ge p}E_{\mathcal Q}(U)
\le\frac{K\sqrt p}{e(p-1)}.}
\tag{14}
\]
At `K=O(sqrt(p)/log(p))`, the positive normalized excursion is `O(1/log(p))`. Thus prime-chain **pairs** cannot supply a positive critical excursion, even with arbitrarily many interleaving repairs. This extends the nonnegative-primitive mechanism; it does not extend RE-267's stronger quadratic-height or `O(K/p^2)` bound to chain pairs. No sharp constant for (14) is asserted.

## 5. Exact audit and prior art

The witness and its strict sign have a short standard-library certificate:

```python
from fractions import Fraction as Q
from itertools import combinations
from math import prod, isqrt

def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))

def F(n):
    return Q(n) / (Q(n)-1)

def euler(xs):
    return prod(map(F, xs))

D, B = (11, 23, 47), (12, 14, 6721)
assert prime(7) and all(map(prime, D))
assert all(not prime(b) for b in B)
assert len(set(D+B)) == 6 and min(D+B) > 7
assert 6721 == 11*13*47
assert euler(D) == euler(B) == Q(47, 40)
assert [sum(b <= u for b in B)-sum(q <= u for q in D)
        for u in sorted(D+B)] == [-1, 0, 1, 0, -1, 0]
assert F(12)/F(11) == Q(120, 121) < 1
assert all(euler(ds) != euler(bs)
           for k in (1, 2)
           for ds in combinations(D, k) for bs in combinations(B, k))
assert euler((11, 23)) == euler((9, 46)) == Q(23, 20)
```

As a separate check of the universal pair argument, all 276 odd-prime pairs `3<=r<s<100` were audited without an insertion-height cutoff. Put `P=rs`, `V=(r-1)(s-1)`, and `d=P-V`. Every insertion solution satisfies
\[
(da-P)(db-P)=PV,\qquad da-P>0,\quad db-P>0.
\tag{15}
\]
The positivity follows from `ab/(a+b-1)=P/d<a,b`. Enumerating positive divisor pairs `x*y=PV`, `x<=y`, with `d | x+P` and `d | y+P`, therefore finds every unordered integer insertion pair. The 326 solutions included 50 nontrivial ones, 16 of those from prime-chain deletion pairs. Every nontrivial solution satisfied (4); all 200 associated event-cutoff primitive checks were nonnegative by exact rational arithmetic. These checks support the algebra; (3)--(5) prove the unrestricted statement. The algebraic audit allows a prime insertion, while the actual source in (7) satisfies the stricter composite-insertion condition.

The valuation and two-coordinate spreading argument are elementary. The hinge representation
\[
M(U)=\sum_{b\in B}(f(b)-f(U))_+
-\sum_{q\in D}(f(q)-f(U))_+
\]
places the sign question in classical convex order. See Baringhaus and Grübel, [*Nonparametric two-sample tests for increasing convex order*, Bernoulli **15** (2009), 99--123](https://www.ivfm.uni-hannover.de/fileadmin/stochastik/Publications/Gruebel/rg_Nonparametric_two_sample_test.pdf), equations (1.2)--(1.5). The relation `r | s-1` is the classical prime-chain relation in Ford, Konyagin and Luca, [*Prime chains and Pratt trees*](https://arxiv.org/abs/0904.0473), Section 1.1. The shifted-product audit (15) uses the same classical Diophantine method compared in RE-263 with Chen and Koo, [*Two-term Egyptian fractions*](https://www.nntdm.net/papers/nntdm-19/NNTDM-19-2-15-25.pdf), Section 2. No prime-chain distribution or Egyptian-fraction existence theorem is imported.

Searches by Euler-factor matching, composite replacement, totient ratios, the displayed numerical identity, and convex order did not identify an external antecedent for this source boundary. That does not establish global novelty of the rational identity or the elementary largest-prime lemma. The durable delta is the **sharp cardinality-three, unit-budget escape once arbitrary deletion spread is allowed**, together with elimination of the entire two-prime chain escape from the critical positive-excursion route.

## 6. Boundaries

RE-268 and RE-271 remain intact: the triple (7) is not subdyadic. RE-270 still establishes the first negative primitive at cardinality four **within the subdyadic class**. This result does not classify all three-prime failures or prove that every failing triple must contain a prime-chain edge.

Integrality matters in (3); real insertion labels need not carry any prime valuation. Individual exact pair matching matters in (14); it is not implied by a global Euler-product equality, as the indecomposable triple demonstrates. Infinite repairs and approximate matching are outside these arguments.

The finite witness does not yield an unbounded family of prime triples, a way to replicate disjoint copies at arbitrary frontiers, or an order-one positive normalized excursion at the critical counting scale. Scaling its labels would not preserve primality or (1). Composite labels carry synthetic factors `b/(b-1)`, not their ordinary divisor-sum factors. No CA realization, selected ordinary-prime tail estimate, Robin counterexample, or RH conclusion follows.
