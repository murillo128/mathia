# RE-274 — A prescribed prime triple conditionally realizes positive critical Robin excursions

**Status:** EXACT-DERIVED algebraic family + CONDITIONAL-SOURCE-REALIZATION; prime supply conjectural; independent adversarial review pending.

**Dependencies:** RE-273 (the triple sign boundary), RE-265 (the distinct negative critical-budget realization). The proof below reconstructs the source matching and positive excursion directly.

There is an exact integer three-deletion/three-insertion family whose first deletion precedes its first insertion by a fixed relative amount. Its counting budget is one, and its positive Robin source excursion is asymptotic to one fifteenth of the reciprocal first-deletion height. Simultaneous primality is required of three specified admissible linear forms. A stated quantitative prime-tuple hypothesis supplies enough disjoint members to obtain a **positive**, order-one Robin-normalized excursion at the critical counting budget.

The algebraic family and its finite prime instances are unconditional. Infinite prime supply, and therefore the critical-budget conclusion, are **not** proved. This identifies an explicit sufficient prime-supply input for the positive balanced-integer escape left open by RE-265--RE-273; it does not settle that escape unconditionally.

## 1. An exact triple family

For an integer `m >= 1`, put
\[
r=14m+1,\quad s=42m+1,\quad t=140m+1,
\qquad a=15m+1,\quad b=28m+1,\quad c=rst.
\tag{1}
\]
With `F(x)=x/(x-1)` and `f(x)=log F(x)`, the identity is
\[
\boxed{F(r)F(s)F(t)=F(a)F(b)F(c).}
\tag{2}
\]
Indeed,
\[
\begin{aligned}
c-1&=196m+8428m^2+82320m^3\\
&=196m(15m+1)(28m+1)=196mab,\\
(r-1)(s-1)(t-1)&=82320m^3,\qquad
(a-1)(b-1)=420m^2.
\end{aligned}
\tag{3}
\]
Both sides of (2) are consequently `c/(82320m^3)`. This proves exact matching at every positive integer parameter without a numerical fitting step.

Restrict now to
\[
m=33n+8,\qquad n\ge0.
\tag{4}
\]
Then `a=495n+121=11(45n+11)` and `b=924n+225=3(308n+75)` are composite. Whenever
\[
L_1(n)=462n+113,\qquad
L_2(n)=1386n+337,\qquad
L_3(n)=4620n+1121
\tag{5}
\]
are all prime, the sets `D={r,s,t}` and `B={a,b,c}` therefore define an admissible finite repair of the ordinary-prime source. All six labels are distinct, and
\[
r<a<b<s<t<c.
\tag{6}
\]
There are no prime-chain edges within `D`. The identities
\[
s-1=3r-3,\qquad t-1=10r-10,
\qquad 3(t-1)=10(s-1)
\]
exclude respectively `r | s-1`, `r | t-1`, and `s | t-1`, since `r>=113` and `s>=337`. Thus the family does not need the prime-chain alternative of RE-262.

The three forms in (5) are admissible. Each is primitive, with positive slope, and their slopes are distinct. Modulo two all three values are odd; modulo three their values are `2,1,2`. For every prime `ell >= 5`, primitivity makes each form vanish on at most one residue class (or none if its slope vanishes), so their union excludes at most three classes. Some class remains. This is a proof of local admissibility, **not** of simultaneous primality.

## 2. The sign and the size of one repair

Let `p` be any ordinary prime below `r`, and let
\[
Q=(\mathbb P\setminus D)\cup B,\qquad
A(x)=\#\{z\in B:z\le x\}-\#\{q\in D:q\le x\}.
\]
At the ordered events in (6), the counting values are
\[
-1,\quad0,\quad1,\quad0,\quad-1,\quad0.
\tag{7}
\]
In particular `sup |A|=1` and the eventual count is zero. For
\[
M(U)=\int_p^U\frac{A(x)}{x(x-1)}\,dx,
\]
the first insertion cutoff has the exact negative primitive
\[
\boxed{\exp M(a)=\frac{F(a)}{F(r)}
=\frac{210m+14}{210m+15}<1.}
\tag{8}
\]
This agrees with RE-273's first-insertion classification.

For the Robin source coordinate, define
\[
h(x)=\frac{f(x)}{\log x},\qquad
\Delta\vartheta(x)=\sum_{q\in Q,q\le x}\log q
-\sum_{q\in\mathbb P,q\le x}\log q,
\qquad E_Q(U)=\int_p^U\Delta\vartheta(x)h'(x)\,dx.
\tag{9}
\]
Only the deletion at `r` contributes before `a`, hence
\[
\boxed{E_Q(a)=\log r\,[h(r)-h(a)]>0.}
\tag{10}
\]
The sign is exact: `f>0`, `f'<0`, and therefore `h'<0`. As `m` tends to infinity through parameters with the required primes,
\[
E_Q(a)=f(r)-\frac{\log r}{\log a}f(a)
=\left(\frac1{15}+o(1)\right)\frac1r,
\tag{11}
\]
because `a/r -> 15/14`, `f(x)=1/x+O(x^-2)`, and `log r/log a -> 1`. Thus this construction permits a positive excursion on the reciprocal-height scale whenever the required prime triples occur at unbounded parameters; their occurrence is a separate hypothesis.

Finite exact matching also gives
\[
\Gamma(Q)=\lim_{x\to\infty}
\left(\sum_{q\in Q,q\le x}f(q)-\log\log x\right)=\gamma.
\tag{12}
\]
Beyond every alteration, direct signed-atom integration gives `E_Q(U)=h(U) Delta vartheta(infinity)`, so `E_Q(infinity)=0`. The transient positivity does not violate either terminal equality.

For example, `n=7`, `m=239` gives prime deletions and composite insertions
\[
D=\{3347,10039,33461\},\qquad
B=\{3586,6693,1124307434713\}.
\tag{13}
\]
Primality here is checked by trial division; (2), (7), and (8) are rational certificates. This example alone is not an infinite-family theorem.

## 3. Exact statement of the missing prime supply

Use the following hypothesis only for the fixed forms (5):

**H.** For every fixed `eta > 0`, for all sufficiently large real `x`,
\[
\#\{n\in\mathbb Z\cap[x,(1+\eta)x]:
L_1(n),L_2(n),L_3(n)\text{ all prime}\}
\gg_\eta\frac{x}{(\log x)^3}.
\tag{14}
\]
The generalized Hardy--Littlewood asymptotic for this admissible triple implies H. Qualitative Dickson infinitude alone does not imply (14), supply a prescribed growing number of repairs near a frontier, or imply the conclusion below.

**Conditional source theorem.** Assume H. Let `p` tend to infinity through ordinary primes, prescribe `T(p)>=p` with `T/p -> 1`, and let
\[
1\le K=K(p)=o\!\left(\frac{p}{(\log p)^3}\right)
\tag{15}
\]
be integer valued. For every sufficiently large `p`, there is a distinct integer-label source obtained from the ordinary primes by exactly `3K` deletions and `3K` composite insertions such that
\[
Q\cap(1,T]=\mathbb P\cap(1,T],\quad
\Gamma(Q)=\gamma,\quad \sup_{x\ge p}|A(x)|=K,
\quad A(x)=0\text{ eventually},
\tag{16}
\]
and at a common cutoff `U`,
\[
\boxed{E_Q(U)=\left(\frac1{15}+o(1)\right)\frac Kp>0.}
\tag{17}
\]
In particular, at `K ~ lambda sqrt(p)/log(p)`, with fixed `lambda>0`,
\[
\sqrt p\log p\,E_Q(U)\longrightarrow\frac{\lambda}{15}.
\tag{18}
\]
No optimality of `1/15` is asserted.

## 4. Packing with separated label bands

Fix first `0<eta<1/100`. Restrict the parameters in (5) by
\[
(1+\eta)p\le r_n\le(1+2\eta)p.
\tag{19}
\]
The corresponding interval of `n` has location and length comparable to `p`, with constants depending only on `eta`. It contains a fixed relative interval of the form in (14). Hence H supplies `gg_eta p/(log p)^3` parameters there. By (15), choose exactly `K` of them for all sufficiently large `p`.

For this small fixed `eta`, the six label bands are separated in the order
\[
\{r_n\}<\{a_n\}<\{b_n\}<\{s_n\}<\{t_n\}<\{c_n\}.
\tag{20}
\]
Here each comparison means every label in the left band precedes every label in the right band. For the closest two bands, for example, `(1+2eta)<(15/14)(1+eta)`; the other linear bands have larger fixed separations. The product band is cubic. Within each band its label is strictly increasing in `n`. All altered labels are therefore distinct, including across repairs. No collision-removal theorem or bound on the number of prime forms at one parameter is needed.

The count falls to `-K` through the first deletion band, rises through the two insertion bands to `K`, falls through the two remaining deletion bands to `-K`, and returns to zero through the product insertions. It never leaves `[-K,K]`. Multiplying (2) gives exact normalization, and (19) puts every alteration beyond `T` eventually.

For a sequence of fixed accuracies `eta_j` decreasing to zero, increase the onset thresholds so that H, (15), all band separations, and the prefix condition hold for every `p` beyond the respective threshold. Use that fixed accuracy until the next threshold. This diagonal choice gives, uniformly over all chosen parameters,
\[
r_n=p+o(p),\quad a_n=\frac{15}{14}p+o(p),\quad b_n=2p+o(p),
\]
\[
s_n=3p+o(p),\quad t_n=10p+o(p),\quad c_n=30p^3+o(p^3).
\tag{21}
\]
It does not assume a prime-tuple estimate in a prescribed shrinking interval.

Set `U=min_n a_n`. All first deletions, and no insertions or other deletions, contribute to the integral through this cutoff. Thus
\[
E_Q(U)=\sum_n\left[f(r_n)-h(U)\log r_n\right].
\tag{22}
\]
The uniform estimates (21) make every summand `(1/15+o(1))/p`. Summation is valid for growing `K`, proving (17)--(18).

## 5. Validation and prior-art boundary

The elementary certificate for the finite control is:

```python
from fractions import Fraction as Q
from math import prod, isqrt

F = lambda x: Q(x, x-1)
def prime(x):
    return x >= 2 and all(x % d for d in range(2, isqrt(x)+1))

n = 7
m = 33*n + 8
D = (14*m+1, 42*m+1, 140*m+1)
B = (15*m+1, 28*m+1, prod(D))
assert all(map(prime, D))
assert B[0] % 11 == B[1] % 3 == 0
assert len(set(D+B)) == 6
assert D[0] < B[0] < B[1] < D[1] < D[2] < B[2]
assert prod(map(F, D)) == prod(map(F, B))
assert F(B[0])/F(D[0]) == Q(210*m+14, 210*m+15) < 1
assert [sum(b <= u for b in B)-sum(q <= u for q in D)
        for u in sorted(D+B)] == [-1, 0, 1, 0, -1, 0]
```

Supplementary checks verified (2), (6), the composite divisors, and the count path for every `0<=n<=1000`; trial division found 31 prime triples in that finite range. All 168 primes below 1001 passed a residue-class admissibility check. The two prime parameters `n=517,520` gave a disjoint twelve-label source with exact Euler matching, maximum absolute count two, and all first deletions preceding the common cutoff `U=256036`. These are finite algebra and source-bookkeeping checks. The proof of (2) is (3), admissibility is proved above for every prime, and no finite count establishes H.

The prime-supply comparison is Ben Green and Terence Tao, [*Linear equations in primes*, Annals of Mathematics **171** (2010), 1753--1850](https://annals.math.princeton.edu/wp-content/uploads/annals-v171-n3-p08-p.pdf), Conjecture 1.4 and the following discussion of the one-variable case. Their generalized Hardy--Littlewood formulation provides the conditional reference for H; their finite-complexity result does not prove it. The three forms here are affinely dependent as one-variable forms.

James Maynard, [*Dense clusters of primes in subsets*, Compositio Mathematica **152** (2016), 1517--1554](https://compositio.nl/Content/prize2018_maynard.pdf), Theorem 3.4, supplies several unspecified prime forms from a sufficiently large admissible panel. That is the input used differently in RE-264--RE-265. Adding forms to (5) does not make that theorem select these three specified forms, and no larger panel with the required identity for every selectable triple is constructed here.

Polynomial products conditioned on simultaneous primality have extensive prior art, including Chernick's universal-form method as treated in Bernd C. Kellner, [*On primary Carmichael numbers*, Integers **22** (2022), A38](https://math.colgate.edu/~integers/w38/w38.pdf), Section 4 and Theorem 4.2. No novelty is claimed for that general strategy or for polynomial factorization. No Carmichael-number property is used or asserted for the family (4).

Targeted comparison by Euler-factor replacement, totient ratios, three-linear-factor parametrization, the coefficient tuple, and Carmichael universal forms did not locate this precise Robin-source construction. Absence from that search does not establish global novelty. The durable delta is the exact **positive** relative-scale triple repair and its explicitly conditional critical-budget assembly, with composite insertion and distinctness conditions proved. It is neither another unconditional finite sign witness nor an unconditional positive counterpart to RE-265.

## 6. Scope and consequences

The distinction between algebra and supply is load-bearing. Formula (2) holds even when one or more deleted labels are composite, but such a parameter is not a repair of the ordinary-prime source. The local admissibility proof cannot remove that restriction. H is a specific unproved prime-tuple lower bound, not a consequence of the ordinary PNT or of currently imported Maynard estimates.

An unconditional uniform `o(K/p)` bound for positive excursions over all finite balanced integer sources would contradict H through (17). At critical budget it would contradict the positive limit (18). This is a conditional obstruction to such a stability theorem, not an unconditional disproof of it. The existing pair, subdyadic-triple, and surplus-one subdyadic positivity theorems remain intact: these deletions have asymptotic ratio ten between largest and smallest.

Each frontier uses a different finite source. No single source with prescribed infinitely many excursions, no optimal positive constant, and no unconditional growing supply of these triples is established. The compensating support is cubic; no support-optimality assertion is made. Composite insertions are synthetic Euler atoms `b/(b-1)`, not their ordinary divisor-sum factors. The family has no proved CA realization and supplies no estimate for the signed tail at selected ordinary-prime frontiers. There is no Robin counterexample or RH conclusion.
