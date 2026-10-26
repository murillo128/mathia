# RE-270 — Four-prime balanced integer repairs can have a negative counting primitive

**Status:** EXACT-DERIVED + EXACT-COUNTEREXAMPLE + FINITE-SOURCE-BOUNDARY; independent adversarial review pending.

**Dependencies:** RE-267 and RE-268 (nonnegative primitives for subdyadic pairs and triples), RE-269 (the deletion-spread certificate and its real-label escape).

Integrality does **not** extend the nonnegative-primitive theorem from three to arbitrary subdyadic prime deletions. A single exactly matched four-prime packet, with distinct composite integer insertions and net counting budget two, already has a negative primitive. Thus four is the smallest possible deletion cardinality for this failure in the stated source class. This is a finite obstruction to a proposed universal sign lemma, not an asymptotic Robin excursion or a restriction on actual CA integers.

## 1. Exact integer source

Write
\[
F(x)=\frac{x}{x-1},\qquad f(x)=\log F(x),\qquad
h(x)=\frac{f(x)}{\log x}\quad(x>1).
\]
Take the ordinary-prime prefix `p=587` and the sets
\[
D=\{593,739,881,1163\},\qquad
B=\{595,596,597,P\},\qquad P=449008698881.
\tag{1}
\]
All four deletions are ordinary primes. Their product is `P`, and
\[
V:=\prod_{q\in D}(q-1)=446752373760,
\qquad 199V=198(P-1).
\tag{2}
\]
All insertions are distinct composites:
\[
595=5\cdot7\cdot17,\quad596=4\cdot149,\quad597=3\cdot199,
\quad P=593\cdot739\cdot881\cdot1163.
\tag{3}
\]
Every altered label exceeds `p`; the deletion packet is strictly subdyadic since `1163<2*593`. It therefore has no prime-chain edge `q | q'-1` between distinct deletions.

The matching identity is particularly short:
\[
\prod_{b\in B}F(b)
=\frac{597}{594}\frac{P}{P-1}
=\frac{199}{198}\frac{P}{P-1}
=\frac P V
=\prod_{q\in D}F(q).
\tag{4}
\]
Consequently the distinct integer-label source
\[
Q=(\mathbb P\setminus D)\cup B
\]
agrees with the primes through `587`, has equal insertion/deletion counts, and satisfies exact Mertens matching
\[
\Gamma(Q):=\lim_{x\to\infty}
\left(\sum_{q\in Q,\ q\le x}f(q)-\log\log x\right)=\gamma.
\tag{5}
\]
Indeed, the finite difference of the two Euler-log sums is exactly zero after `P`. This uses ordinary-prime Mertens normalization only as the reference constant.

## 2. Negative primitive and positive transient coordinate

Define
\[
A(x)=\Pi_Q(x)-\pi(x),\qquad
M(U)=\int_p^U\frac{A(x)}{x(x-1)}\,dx,
\]
\[
\Delta\vartheta(x)=\sum_{q\in Q,\ q\le x}\log q
-\sum_{q\in\mathbb P,\ q\le x}\log q,
\qquad E_Q(U)=\int_p^U\Delta\vartheta(x)h'(x)\,dx.
\tag{6}
\]
The altered events and their right-continuous counts are

| Event | 593 | 595 | 596 | 597 | 739 | 881 | 1163 | P |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `A` | -1 | 0 | 1 | 2 | 1 | 0 | -1 | 0 |

Hence `sup |A|=2`, and the terminal count is zero. On the first nontrivial interval `593<U<595`,
\[
M(U)=f(U)-f(593)<0,
\qquad
E_Q(U)=\log(593)\,[h(593)-h(U)]>0.
\tag{7}
\]
The latter sign is exact: `f>0`, `f'<0`, and `log x` is positive and increasing, so `h'<0`. A rational certificate at an integer cutoff is
\[
\boxed{\exp M(594)=\frac{F(594)}{F(593)}
=\frac{351648}{351649}<1.}
\tag{8}
\]
Thus neither real labels nor approximate Euler matching are needed for the negative-primitive escape. Positivity of `E_Q` occurs before any insertion, rather than only after the distant compensator.

Both `M(infinity)=0` and `E_Q(infinity)=0` hold. The first follows from exact matching and finite support; for the second, integrating each altered atom gives the negative of the total Euler-log difference, with the remaining endpoint term tending to zero. Neither terminal equality controls the transient sign.

For any such finite source, the elementary atom formula is
\[
M(U)=\sum_{b\in B}(f(b)-f(U))_+
-\sum_{q\in D}(f(q)-f(U))_+.
\tag{9}
\]
Thus the insertion Euler logarithms fail to dominate the deletion Euler logarithms in convex order, despite equal cardinality, equal sum, integrality, and the forced distant insertion. This is the classical positive-part characterization, applied to an arithmetic witness.

## 3. How the integer escape is constructed

For any four-prime packet let `P=prod D`, `V=prod(q-1)`, and `w=P-1-V`. If
\[
a=\frac{P-1+2V}{w}=1+\frac{3V}{w}
\tag{10}
\]
is an integer, then
\[
\frac{a+2}{a-1}=\frac{P-1}{V}.
\]
Therefore three consecutive labels and the product label satisfy
\[
F(a)F(a+1)F(a+2)F(P)=\prod_{q\in D}F(q).
\tag{11}
\]
Whenever the three consecutive labels are composite, distinct from `P`, and strictly greater than the smallest deletion, this provides a balanced composite repair with a negative initial primitive. The exhibited packet has `w=2256325120` and `a=595`. Equation (10) is a sufficient construction, not a classification of all four-prime repairs. No infinitude of prime packets satisfying its divisibility and ordering conditions is asserted.

The mechanism moves the large Euler mass of a compressed factor into three smaller logarithms at consecutive composite labels. Telescoping makes this redistribution exactly integral. The final product label carries all four deleted prime factors, satisfying rather than evading the valuation requirement of RE-262.

## 4. Sharp cardinality boundary and compatibility with existing obstructions

A one-prime balanced replacement is impossible by injectivity of `F`. RE-267 proves `M>=0` for every exact subdyadic two-prime repair. RE-268 proves it for every exact subdyadic three-prime repair. Their arguments use the ordinary-prime deletion and integer-composite insertion hypotheses retained here. The witness therefore establishes the exact minimum **packet cardinality four** for a negative primitive; it makes no smallest-label claim.

It also cannot partition into proper, individually exact balanced subrepairs: every such part would contain at most three deletions, remain subdyadic, and have nonnegative primitive. Their sum could not equal (8). This deduction is independently checkable by the 68 proper equal-cardinality subset comparisons in the certificate below.

The sufficient spread condition of RE-269 is not contradicted. For `r=593` and `s=739`, its multiplicative form would require
\[
\frac{\prod_{q\in D}F(q)}{F(rs)F(r)^3}\ge1.
\]
Here the exact value is
\[
\frac{2458766024346328}{2458834330390515}<1.
\tag{12}
\]
Thus the packet defeats that spread certificate as well as the universal nonnegative-primitive extension. RE-269's quantitative deficit bound still applies.

## 5. Reproducible exact certificate

The following standard-library Python checks primality, compositeness, equality, all counting events, the negative cutoff, the failed spread condition, and irreducibility into proper balanced exact subrepairs. The proof is the displayed algebra; no floating-point calculation or search completeness claim is needed.

```python
from fractions import Fraction
from itertools import combinations
from math import isqrt, prod

def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))

def F(n):
    return Fraction(n, n - 1)

def euler(xs):
    return prod(F(x) for x in xs)

D = (593, 739, 881, 1163)
P = prod(D)
B = (595, 596, 597, P)
V = prod(q - 1 for q in D)
assert prime(587) and all(map(prime, D))
assert all(not prime(b) for b in B)
assert len(set(D + B)) == 8 and min(D + B) > 587
assert max(D) < 2 * min(D)
assert P == 449008698881 and V == 446752373760
assert 199 * V == 198 * (P - 1)
assert euler(D) == euler(B)
counts = [sum(b <= u for b in B) - sum(q <= u for q in D)
          for u in sorted(D + B)]
assert counts == [-1, 0, 1, 2, 1, 0, -1, 0]
assert F(594) / F(593) == Fraction(351648, 351649) < 1
assert euler(D) / (F(593 * 739) * F(593)**3) == Fraction(
    2458766024346328, 2458834330390515) < 1
checks = 0
for k in range(1, 4):
    for ds in combinations(D, k):
        for bs in combinations(B, k):
            assert euler(ds) != euler(bs)
            checks += 1
assert checks == 68
```

## 6. Prior art and research consequence

The finite Euler-product algebra, telescoping consecutive factors, and positive-part characterization of convex order are classical mechanisms. For the latter see L. Baringhaus and R. Grübel, [*Nonparametric two-sample tests for increasing convex order*, Bernoulli **15** (2009), 99--123, DOI `10.3150/08-BEJ151`](https://www.ivfm.uni-hannover.de/fileadmin/stochastik/Publications/Gruebel/rg_Nonparametric_two_sample_test.pdf), equations (1.2)--(1.5). No new convex-order theorem is claimed. Searches by finite Euler-product matching, composite replacements, totient-ratio equations, and the displayed prime packet did not establish an external antecedent for this exact source witness; that does not establish global novelty of the numerical identity.

The durable delta is that the remaining **integer** escape is real: the nonnegative-primitive obstruction has its first cardinality failure at four, even with one subdyadic deletion packet, exact Mertens matching, equal total count, distinct labels and counting budget two. It is no longer sufficient to invoke integrality to dismiss the real-label failure in RE-269.

This result does not refute a possible asymptotic positive-excursion bound for larger integer packets. A fixed example at `p=587` provides no family with `p` tending to infinity, no order-one Robin-normalized positive excursion at critical counting budget, and no method to add disjoint copies at arbitrary scales. Merely dilating its labels would destroy the prime and exact-product hypotheses. Composite labels carry synthetic Euler factors `b/(b-1)`, not their ordinary divisor-sum factors. No CA realization, selected ordinary-prime tail estimate, Robin counterexample, or RH conclusion follows.
