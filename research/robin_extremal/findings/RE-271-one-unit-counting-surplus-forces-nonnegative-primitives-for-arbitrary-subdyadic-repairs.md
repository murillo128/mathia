# RE-271 — One-unit counting surplus forces nonnegative primitives for arbitrary subdyadic repairs

**Status:** EXACT-DERIVED + SHARP-COUNTING-BOUNDARY + ONE-SIDED-SOURCE-OBSTRUCTION; independent adversarial review pending.

**Dependencies:** RE-262 (prime valuations force a quadratic insertion), RE-269 (counting primitive and the distinct deletion-spread certificate), RE-270 (an exact negative primitive with counting surplus two).

The failure at four deletions in RE-270 does not extend to repairs whose **positive counting surplus is at most one**. This condition forces a nonnegative weighted counting primitive for every finite subdyadic deletion packet, independently of its cardinality and without any lower bound on its counting discrepancy. Surplus two is the first possible integer surplus permitting a negative primitive. This is a theorem about synthetic integer-label source repairs, not an ordinary-prime or CA sign theorem.

## 1. Exact source statement

Let `p >= 3` be an ordinary prime and let
\[
D=\{r=q_1<s=q_2<\cdots<q_m=t<2r\},\qquad m\ge2,
\]
be distinct odd primes. Let `B` be a set of `m` distinct composite integers, with every label in `D union B` greater than `p`, and suppose
\[
\prod_{b\in B}\frac b{b-1}=\prod_{q\in D}\frac q{q-1}.
\tag{1}
\]
Define
\[
F(x)=\frac x{x-1},\quad f(x)=\log F(x),\quad
A(x)=\#\{b\in B:b\le x\}-\#\{q\in D:q\le x\},
\]
\[
M(U)=\int_p^U\frac{A(x)}{x(x-1)}\,dx.
\tag{2}
\]
Then
\[
\boxed{A(x)\le1\ (x\ge p)\quad\Longrightarrow\quad
M(U)\ge0\ (U\ge p).}
\tag{3}
\]
In fact exactly one insertion lies below `r`, and throughout the deletion interior,
\[
M(U)\ge\eta_r>0\qquad(r+1\le U\le t),
\tag{4}
\]
where the explicit margin is
\[
\eta_r=\log\left(1+
\frac{r^2+10r-9}{4(r-1)^2(r+1)(r+2)}\right).
\tag{5}
\]
There is no assumption `A >= -1`, no fixed bound on `m`, no decomposition into pair or triple repairs, and no deletion-spread condition.

## 2. A distant insertion forces enough terminal mass

First reconstruct the arithmetic input. No prime in `D` divides the predecessor of another: subdyadic support would force `q'-1=q`, contradicting odd primality. Hence every `q in D` has valuation one in the deleted Euler product. Taking valuations in (1) gives
\[
\sum_{b\in B}v_q(b)=1+\sum_{b\in B}v_q(b-1)\ge1.
\]
Every deleted prime must divide an insertion numerator. If each insertion contained at most one deleted prime, equal cardinality would force a bijection `q -> b_q` with `b_q >= q`. Strict decrease of `F` and equality (1) would force `b_q=q` for every `q`, contradicting compositeness. Thus some insertion satisfies
\[
b_*\ge rs>t.
\tag{6}
\]
Denominator cancellation on the insertion side only increases the numerator valuations required by this argument.

Exact matching and finite support imply `M(infinity)=0`. After the last deletion,
\[
A(x)=-\#\{b\in B:b>x\}\le0\qquad(x\ge t).
\]
Consequently the endpoint value is exactly
\[
M(t)=-\int_t^\infty\frac{A(x)}{x(x-1)}\,dx
=\sum_{b>t}\bigl(f(t)-f(b)\bigr)
\ge f(t)-f(rs).
\tag{7}
\]
For `r <= U <= t`, the upper surplus bound now gives
\[
\begin{aligned}
M(U)
&=M(t)-\int_U^t\frac{A(x)}{x(x-1)}\,dx\\
&\ge2f(t)-f(U)-f(rs).
\end{aligned}
\tag{8}
\]
Negative values of `A` strengthen this bound. The argument does not require a single sign change of `A`.

## 3. The integer spacing closes the first unit interval

Since `t <= 2r-1`, `s >= r+2`, and `f` decreases, (8) implies, for `r+1 <= U <= t`,
\[
M(U)\ge2f(2r-1)-f(r+1)-f(r(r+2))=\eta_r.
\tag{9}
\]
The positivity is an exact rational inequality:
\[
\frac{F(2r-1)^2}{F(r+1)F(r(r+2))}
=1+\frac{r^2+10r-9}{4(r-1)^2(r+1)(r+2)}>1
\qquad(r\ge3).
\tag{10}
\]
Its numerator identity is
\[
(2r-1)^2(r^2+2r-1)
-4(r-1)^2(r+1)(r+2)=r^2+10r-9.
\]
It would be incorrect to replace `r+1` by `r` in (9); that stronger rational inequality can fail. Integrality supplies the remaining step.

If no insertion lay below `r`, then every insertion would be at least `r+1`, while the only deletion through `r+1` would be `r`. Thus
\[
M(r+1)=f(r+1)-f(r)<0,
\]
contradicting (9). At least one insertion therefore lies below `r`. The condition `A <= 1` permits at most one before the first deletion, so there is exactly one, say `a<r`. Before `r` there are no deletions and `M >= 0`. On `[r,r+1]`, no other integer event occurs in the open interval and
\[
A=0\text{ on }[r,r+1),\qquad M(U)=f(a)-f(r)>0.
\]
Together with (9) this covers every cutoff through `t`. For `U >= t`, the terminal identity gives
\[
M(U)=\sum_{b>U}\bigl(f(U)-f(b)\bigr)\ge0.
\tag{11}
\]
The integral is continuous at every event, so the argument includes endpoint cutoffs. This proves (3)--(5).

## 4. The sharp surplus boundary and a control outside the spread certificate

Use the same deletions as RE-270:
\[
D=\{593,739,881,1163\},\qquad P=449008698881=\prod D.
\]
An alternative exact repair is
\[
B=\{398,793,794,P\},\qquad p=397.
\tag{12}
\]
All insertions are composite: `398=2*199`, `793=13*61`, `794=2*397`, and `P` is the product of the four deletions. The telescoping identity is
\[
F(398)F(793)F(794)=\frac{199}{198},\qquad
\prod_{q\in D}F(q)=\frac{199}{198}F(P).
\tag{13}
\]
At the eight ordered events its counts are
\[
1,0,-1,0,1,0,-1,0.
\]
It satisfies (3), although the deletion-only spread certificate of RE-269 fails:
\[
\frac{\prod_{q\in D}F(q)}{F(593\cdot739)F(593)^3}
=\frac{2458766024346328}{2458834330390515}<1.
\tag{14}
\]
It is not a union of proper balanced exact subrepairs: all 68 proper equal-cardinality subset comparisons have unequal Euler products. Thus this is an exact larger-packet control outside both the pair/triple decomposition and the earlier sufficient spread condition.

In contrast, RE-270 inserts `595,596,597,P` for the same deleted set. Its maximum positive surplus is two and
\[
\exp M(594)=\frac{351648}{351649}<1.
\tag{15}
\]
All labels of both repairs exceed the common prefix `397`. Equations (3) and (15) establish the exact minimum **positive counting surplus two** for a negative primitive in this integer source class. This sharpness is finite; no asymptotic family is asserted.

The theorem also covers repairs whose absolute counting budget exceeds one. For example, the exact RE-269 repair
\[
D=\{17,19,23,29\},\quad B=\{8,33,34,12673\},\quad p=7
\]
has event counts `1,0,-1,-2,-3,-2,-1,0`: its positive surplus is one but its negative deficit is three. It is covered by (3).

Integer-label structure is essential. With prime deletions `D={5,7}`, prefix `p=3`, and real insertions `B={175/31,6}`, both Euler products are `35/24` and the positive surplus is one, but
\[
\exp M(11/2)=\frac{44}{45}<1.
\tag{16}
\]
This control loses the forced quadratic insertion (6); it is not an integer counterexample.

## 5. Consequence for superposed repairs and the Robin coordinate

Consider any finite family of individually exact repairs satisfying (1)--(3), with disjoint altered labels and a common unchanged prime prefix through `p`. Their deletion packets need only be subdyadic individually. Write `A=sum_j A_j` and assume the **net** discrepancy satisfies `|A(x)|<=K`. Neither the number of packets nor their cardinalities is bounded in terms of `K`.

For the resulting source `Q`, put
\[
h(x)=\frac{f(x)}{\log x},\quad
\Delta\vartheta(x)=\sum_{q\in Q,q\le x}\log q-\sum_{q\in\mathbb P,q\le x}\log q,
\quad E_Q(U)=\int_p^U\Delta\vartheta(x)h'(x)\,dx.
\]
Every packet has nonnegative primitive, so their sum does too. Partial summation, using `h(U)log U=f(U)`, cancels the endpoint count and gives
\[
E_Q(U)=-M(U)-h(U)\int_p^U\frac{A(x)}x\,dx
\le K h(U)\log(U/p).
\tag{17}
\]
For `v=U/p>=1`, the inequalities `f(U)<=1/(U-1)`, `U-1>=(p-1)v`, and `log U>=log p` give
\[
h(U)\log(U/p)\le\frac{\log v}{v(p-1)\log p}
\le\frac1{e(p-1)\log p}.
\]
Therefore
\[
\boxed{\sqrt p\log p\,\sup_{U\ge p}E_Q(U)
\le\frac{K\sqrt p}{e(p-1)}.}
\tag{18}
\]
At the critical counting scale `K=O(sqrt(p)/log(p))`, the positive normalized excursion is `O(1/log(p))`. The extension here is the source class supplying `M>=0`; the counting estimate itself is already in RE-269. A bound on the total surplus does not imply the corresponding bound on each proposed packet, so the decomposition hypotheses must be checked explicitly.

## 6. Exact checks, prior art, and limits

The elementary rational core and the controls are reproducible without logarithmic rounding:

```python
from fractions import Fraction as Q
from itertools import combinations
from math import prod, isqrt

def F(n):
    return Q(n) / (Q(n) - 1)

def euler(xs):
    return prod(map(F, xs))

def expM(D, B, u):
    return (prod(F(b)/F(u) for b in B if b <= u)
            / prod(F(q)/F(u) for q in D if q <= u))

def counts(D, B):
    return [sum(b <= u for b in B) - sum(q <= u for q in D)
            for u in sorted(D + B)]

def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))

D = (593, 739, 881, 1163)
P = prod(D)
B = (398, 793, 794, P)
assert prime(397) and all(map(prime, D))
assert all(not prime(b) for b in B)
assert len(set(D+B)) == 8 and min(D+B) > 397
assert max(D) < 2*min(D) and euler(D) == euler(B)
assert counts(D, B) == [1, 0, -1, 0, 1, 0, -1, 0]
assert all(expM(D, B, u) >= 1 for u in sorted(D+B))
assert euler(D)/(F(593*739)*F(593)**3) < 1
assert all(euler(ds) != euler(bs)
           for k in range(1, 4)
           for ds in combinations(D, k) for bs in combinations(B, k))
C = (595, 596, 597, P)
assert euler(D) == euler(C) and max(counts(D, C)) == 2
assert expM(D, C, 594) == Q(351648, 351649) < 1
assert euler((5, 7)) == euler((Q(175, 31), 6))
assert max(counts((5, 7), (Q(175, 31), 6))) == 1
assert expM((5, 7), (Q(175, 31), 6), Q(11, 2)) == Q(44, 45) < 1
for r in range(3, 10001):
    ratio = F(2*r-1)**2 / (F(r+1)*F(r*(r+2)))
    assert ratio == 1 + Q(r*r+10*r-9,
                         4*(r-1)**2*(r+1)*(r+2)) > 1
```

The displayed polynomial identity proves the general inequality; the 9998 parameter checks are supplementary diagnostics. Rational event values certify the whole primitive of a finite example because its derivative has constant sign between consecutive events. The subset comparisons establish only the stated finite indecomposability, not a classification or an infinite prime-supply theorem.

The hinge representation
\[
M(U)=\sum_{b\in B}(f(b)-f(U))_+
-\sum_{q\in D}(f(q)-f(U))_+
\]
identifies (3) with the classical convex-order comparison of equal-sum Euler-log vectors. See L. Baringhaus and R. Grübel, [*Nonparametric two-sample tests for increasing convex order*, Bernoulli **15** (2009), 99--123](https://www.ivfm.uni-hannover.de/fileadmin/stochastik/Publications/Gruebel/rg_Nonparametric_two_sample_test.pdf), equations (1.2)--(1.5). No new general convex-order theorem is claimed. The counting/variation mechanism is classical as in C. Aistleitner and J. Dick, [*Functions of bounded variation, signed measures, and a general Koksma--Hlawka inequality*](https://arxiv.org/abs/1406.0230). The prime-predecessor divisibility relation has its standard meaning in K. Ford, S. V. Konyagin and F. Luca, [*Prime chains and Pratt trees*](https://arxiv.org/abs/0904.0473), Section 1.1; no prime-chain distribution theorem is used.

The mathematical delta is the arithmetic implication from **one-sided surplus one**, the forced distant insertion, and integer spacing to nonnegative primitives at arbitrary packet size, with a sharp surplus-two counterexample. The external comparison supports the classical mechanisms, not an attribution of this source theorem or a claim of global novelty. It is not merely the earlier deletion-spread test: (12)--(14) separate their hypotheses on the same deleted primes.

Approximate Euler matching, infinite repairs, nonintegral labels, and deletion sets with prime-chain edges are outside the theorem. Surplus two permits the finite failure (15), but no positive order-one asymptotic Robin excursion for finite balanced integer sources is established. Composite labels carry synthetic factors `b/(b-1)`, not their ordinary divisor-sum contributions. No CA realization, selected ordinary-prime tail estimate, Robin counterexample, or RH conclusion follows.
