# FD-348 — Small-denominator half-period pairs are exact rational translates

**Status:** LITERATURE+DERIVED + EXACT-FINITE-REDUCTION.

In the small-denominator part of the half-period count problem, genuine
Farey pairs obey an exact arithmetic restriction: their smaller-denominator
endpoints differ by exactly one half, not merely approximately one half.
Their denominators can therefore differ only by a factor of two or agree.
The count is exactly a weighted count of three consecutive integer values
of a rational rank-displacement function. This identifies a necessary
anti-concentration estimate for the proposed count bound; it does not
prove that estimate or the half-period correlation conjecture.

## 1. Finite theorem and its range

Let `Q>=3`, and write the genuine Farey sequence as
\[
0=x_0<x_1<\cdots<x_N=1,\qquad
N=\sum_{q\le Q}\varphi(q),\qquad h=N/2.
\]
Extend `x_(k+N)=x_k+1` and denominators periodically. Put
\[
g_k=x_{k+1}-x_k=\frac1{q_kq_{k+1}},\qquad
s_k=\min(q_k,q_{k+1}),
\]
\[
C_{Q,r}(A,B)=\#\{0\le k<N:s_k\le A,\ s_{k+h+r}\le B\},\qquad
\epsilon_{Q,r}=\frac2Q+\frac{|r|+1}{N}.
\tag{1}
\]
Here `r` is an integer and `1<=A,B<=Q` are integer thresholds. Assume
\[
\boxed{2AB\epsilon_{Q,r}<1.}\tag{2}
\]
For each pair counted in (1), let `u` and `v` be its two
smaller-denominator endpoints, with the ranks lifted to the real line.
Then
\[
\boxed{v=u+\tfrac12.}\tag{3}
\]
Writing `q(u)` for reduced denominator and `tau(u)={u+1/2}`, this implies
\[
q(\tau(u))=
\begin{cases}
2q(u),&q(u)\text{ odd},\\
q(u)/2,&q(u)\equiv2\pmod4,\\
q(u),&4\mid q(u).
\end{cases}\tag{4}
\]
The assertion holds at composite orders too. For fixed `r`, (2) covers
`AB<Q/(4+o(1))`; the exact strict condition (2) is the operative one.
No sharpness at its boundary is asserted.

Define `R_Q(x)` as the number of positive order-`Q` Farey fractions at
most `x` for `0<=x<=1`, and extend it by
`R_Q(x+1)=R_Q(x)+N`. For a rational vertex `u in [0,1)` whose half
translate also belongs to the Farey sequence, define the integer
\[
\delta_Q(u)=R_Q(u+1/2)-R_Q(u)-h.
\tag{5}
\]
With `w(n)=max(0,2-|n|)` for integers `n`, the exact count formula is
\[
\boxed{
C_{Q,r}(A,B)=
\sum_{\substack{u\in\mathbb Q\cap[0,1)\\
 q(u)\le A,\ q(\tau(u))\le B}}
 w\bigl(r-\delta_Q(u)\bigr).}
\tag{6}
\]
Both vertices in this sum belong to the order-`Q` sequence. In particular,
if `Z_(Q,r)(A,B)` denotes the number of these vertices with
`|delta_Q(u)-r|<=1`, then
\[
Z_{Q,r}(A,B)\le C_{Q,r}(A,B)\le2Z_{Q,r}(A,B).
\tag{7}
\]

## 2. Why approximate rank placement forces exact translation

Dress's absolute-discrepancy theorem, in the positive-point convention,
gives
\[
|D_k|\le1/Q,\qquad D_k=x_k-k/N,
\tag{8}
\]
also for the periodic lift. Condition (2) implies `AB<Q/4`, hence
`A,B<Q/2`. Adjacent Farey denominators sum to more than `Q`, so any
gap counted in (1) has a unique endpoint with denominator at most its
specified threshold.

Its two selected endpoint ranks are `i=k+e` and `j=k+h+r+e'`, where
`e,e' in {0,1}`. Thus
\[
\left|x_j-x_i-\tfrac12\right|
=\left|D_j-D_i+\frac{r+e'-e}{N}\right|
\le\epsilon_{Q,r}.
\tag{9}
\]
If `a/q` and `b/d` are reduced representatives of these lifted points,
then a nonzero difference from one half has size at least
\[
\left|\frac bd-\frac aq-\frac12\right|
=\frac{|2bq-2ad-qd|}{2qd}\ge\frac1{2qd}\ge\frac1{2AB}.
\tag{10}
\]
This contradicts (2), proving (3). Reduction of `(2a+q)/(2q)` proves
(4), including `u=0` and the wrap at `u=1/2`.

To prove (6), consider any eligible ordered pair `u,tau(u)` and use
its positive half-translation lift. If their vertex ranks are `i,j`,
then `j-i=h+delta_Q(u)`. The two gaps incident to the first vertex
have starting ranks `i-1,i`, and those incident to the second have
starting ranks `j-1,j`. Both pairs have the indicated vertex as their
unique small endpoint. The number of choices with starting-rank
difference `h+r` is two if `delta_Q(u)=r`, one if their difference is
one in absolute value, and zero otherwise. This is `w` in (6).
Condition (2) also gives `|r|+1<N/2`, so the required cyclic gap
difference has the unique lift used here. There is no double counting
because the small endpoint of each gap is unique. The argument includes the gap ending at `1=0 mod 1`.

A useful support consequence is that denominator pairs with ratio
outside `{1/2,1,2}` cannot contribute anywhere (2) holds. For dyadic
shells this excludes shell indices differing by at least two whenever
their upper thresholds satisfy (2). It does not exclude the three
remaining shell diagonals.

## 3. The exact rank defect is a periodic Mertens filter

For `0<=x<=1`, elementary coprimality inversion gives
\[
R_Q(x)=\sum_{d\le Q}\mu(d)\sum_{m\le Q/d}\lfloor mx\rfloor
=\sum_{m\le Q}M(\lfloor Q/m\rfloor)\lfloor mx\rfloor.
\tag{11}
\]
This is the classical Farey rank identity, not a new transform. Since
`R_Q(1/2)=N/2`, comparison of (11) at `1` and `1/2` gives
\[
\sum_{\substack{m\le Q\\m\text{ odd}}}M(\lfloor Q/m\rfloor)=0.
\tag{12}
\]
For `0<=u<=1/2`, subtract the two rank formulas at `u+1/2` and `u`.
Even `m` contributes exactly `m/2`. For odd `m`, the excess over `m/2`
is `1_{{m u}>=1/2}-1/2`. Equation (12) therefore yields
\[
\boxed{
\delta_Q(u)=
\sum_{\substack{m\le Q\\m\text{ odd}}}
 M(\lfloor Q/m\rfloor)\,
 \mathbf1_{\{m u\}\ge1/2}.}
\tag{13}
\]
For `1/2<=u<1`, use `delta_Q(u)=-delta_Q(u-1/2)`, which follows directly
from the periodic extension of `R_Q`. For rational `u=a/q`, the indicator
in (13) is periodic in `m` modulo `q`. The inequality at equality is
`>=`, matching the right-continuous rank convention. Equations (11)–(13)
provide a finite arithmetic falsification test for (6), including its
endpoint and rank-offset signs.

## 4. What the proposed denominator bound must still prove

The [joint-denominator clue](../clues/CLUE-half-period-joint-denominator-count.md)
asks, at prime orders, for
\[
C_{Q,r}(A,B)\ll_r A^2B^2/Q^2+\min(A,B).
\tag{14}
\]
Inside (2), the first term is less than `1/16`. Consequently (7) shows
that the restriction of (14) to this range is equivalent, up to fixed
constants, to
\[
\#\{u:q(u)\le A,\ q(\tau(u))\le B,
      |\delta_Q(u)-r|\le1\}\ll_r\min(A,B).
\tag{15}
\]
This is an anti-concentration question for the *integer values* of the
rank filter, simultaneously over growing rational denominators.
A bound on its absolute size alone is not (15).

For example, let `A=B=t->infinity` with `t^2<=Q/8`, and fix `r` before
letting `Q` grow. Condition (2) then holds eventually. There are
`Theta(t^2)` eligible half-translation pairs before imposing the rank
condition: all reduced `u in [0,1)` of denominator at most `floor(t/2)`
are eligible by (4), while all eligible vertices have denominator at
most `t`. The classical totient count gives both quadratic orders.
Thus (14) requires only `O_r(t)` of this quadratic population to have
rank defect in `{r-1,r,r+1}`. The exact translation restriction by itself
does not supply this linear bound. Nor does it refute it.

The contribution beyond a positional approximation is the exact support
restriction and the incidence multiplicities (6): small-denominator
half-period encounters are forced rational resonances. This narrows the
count clue to a precise simultaneous rank anti-concentration problem in
a range where the proposed independent-density term is bounded.
It does not address the remaining threshold rectangles, sum the resonant
products, or prove `S_(h+r)=o(log Q/Q^2)` for even one offset. The
all-fixed-offset quantifier needed for sector equipartition remains.

## 5. Prior art and validation boundary

The only analytic input to (2)–(10) is François Dress,
*Discrépance des suites de Farey*, Journal de théorie des nombres de
Bordeaux **11**(2) (1999), 345–367
([primary paper](https://www.numdam.org/article/JTNB_1999__11_2_345_0.pdf)).
Its positive-point convention gives (8). Rational separation,
reduction under translation by a rational number, Möbius inversion and
the totient asymptotic are classical. The standard rank formula (11) is
proved here to avoid importing a stronger local-discrepancy assertion.
No novelty is claimed for those ingredients or for a new general
Mertens identity. Searches by Farey half-translation, rank correlation,
small-denominator pairing and rational rank discrepancy did not supply
the simultaneous estimate (15); this is not a global novelty claim.

The dynamical comparison is J. S. Athreya and Y. Cheung,
*A Poincaré section for horocycle flow on the space of lattices*,
[arXiv:1206.6597](https://arxiv.org/pdf/1206.6597), §1.3.3 and Lemma 4.1,
and Albert Artiles, Andrew Best and Matteo Bordignon,
*Mixing of the BCZ map*, [arXiv:2610.07347v1](https://arxiv.org/html/2610.07347v1),
Theorem 1.1. The former identifies the Farey denominator orbit and roof;
the latter proves mixing for normalized Lebesgue measure. Neither
statement supplies (15) for the changing finite orbit at its half-period,
or the required uniformity in shrinking denominator thresholds. This
finite theorem does not challenge that mixing result.

Two standard-library scratch audits generated Farey fractions directly
as sorted reduced rational numbers, independently of the rank filter.
For `Q=7,11,17,31,61,127,251` and `-3<=r<=3`, they checked 3,060 exact
count identities (6), every paired gap satisfying its own small-product
condition (120 incidences), and 12,820 instances of (13) and its reflected
extension. A second pass over every `3<=Q<=80`, including composites,
checked 13,538 count identities, 724 translated incidences and 26,934
rank-filter identities. The threshold comparisons and arithmetic used
exact fractions; (4) and (12) were also checked. The two panels overlap
and are not independent statistical evidence. They guard normalization,
cyclic seams and signs; the theorem follows from the proof, not from
extrapolating these finite checks. No Lean or independent adversarial
approval is claimed.

There is no new cancellation estimate, high-band sector limit,
low-frequency Franel bound, or RH improvement. The elementary finite
reduction alone is not a high-value formalization handoff: its unresolved
content is the analytic counting estimate (15), not verification of the
rational separation calculation.
