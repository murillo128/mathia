# MC-523 — Density-one dyadic window control permits near-linear prefixes

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `MATCHED-CONTROL`, `NO-NOVELTY-CLAIM`.

## Claim and scope

There is one deterministic sequence \(a(n)\in\{-1,0,1\}\), with
\(|a(n)|=\mu(n)^2\), and a predetermined set \(G\) of positive integers
such that all the following hold.

1. The sequence has every qualitative fixed-shift Chowla correlation:
   for distinct fixed nonnegative shifts \(h_1,\ldots,h_r\) and
   \(e_i\in\{1,2\}\), not all even,
   \[
   \frac1T\sum_{n\le T}\prod_{i=1}^r a(n+h_i)^{e_i}\longrightarrow0.
   \tag{1}
   \]
2. The omitted dyadic indices are sparse:
   \[
   |[1,J]\setminus G|=O(\log J).
   \tag{2}
   \]
   Consecutive indices of \(G\) differ by at most three. Thus successive
   retained physical scales \(2^j\) have ratio at most eight.
3. Put \(A(t)=\sum_{n\le t}a(n)\). At every sufficiently large
   \(j\in G\), with \(X=2^j\), simultaneously for every integer
   \(1\le H\le X\) and every real \(X\le y\le2X\),
   \[
   |A(y+H)-A(y)|\le4\sqrt{H\log X}.
   \tag{3}
   \]
   In particular the **complete uncentered** moment satisfies
   \[
   J_a(X,H):=\int_X^{2X}|A(y+H)-A(y)|^2dy
   \le16XH\log X.
   \tag{4}
   \]
   The variance centered by its own empirical mean is no larger.
4. Nevertheless, along an unbounded sequence \(T_k\),
   \[
   |A(T_k)|\gg T_k/\log T_k.
   \tag{5}
   \]

This is an obstruction to **generic scale interpolation**, even with exact
square-free support, all qualitative Chowla correlations, every window
length, and no exceptional starts on the retained blocks. Density one
in the dyadic index, even supplemented by bounded multiplicative gaps,
does not turn these local moments into any fixed-power global saving.

The control is deliberately **not multiplicative**. Its Dirichlet series
is not asserted to have reciprocal-zeta structure, meromorphic continuation,
or sparse poles. Consequently this is not a counterexample to a theorem
about the actual Möbius function or to
[MC-522](MC-522-centered-dyadic-variance-recovers-all-reciprocal-zeta-poles.md).
That theorem assumes every sufficiently large dyadic block and uses
arithmetic continuation and pole sparsity.

The construction strengthens the sparse overwrite control of
[MC-004](MC-004-qualitative-chowla-support-matched-bias.md) by imposing a
simultaneous interval bound on its random base and locating the overwrites
on an explicit dyadic mesh. The new boundary concerns scale coverage of
complete window moments; it is not a new random-sequence mechanism.

## 1. One base controls all intervals and all fixed correlations

Let \(q(n)=\mu(n)^2\), and let \(\epsilon_n\) be independent symmetric
signs. Initially put \(b(n)=q(n)\epsilon_n\).
For an integer interval \(I\) containing \(H\) integers,
\[
\mathbb E\exp\left(t\sum_{n\in I}b(n)\right)
=\prod_{n\in I:q(n)=1}\cosh t
\le\exp(Ht^2/2).
\]
Chernoff's argument, optimized at \(t=u/H\) and applied to both tails,
gives the Hoeffding special case
\[
\mathbb P\left(\left|\sum_{n\in I}b(n)\right|>u\right)
\le2\exp(-u^2/(2H)).
\tag{6}
\]
This uses independence of the auxiliary signs, not independence of Möbius.

For \(X=2^j\), there are at most \(2X^2\) pairs of integer parameters
\(X\le v\le2X\), \(1\le H\le X\). Substituting
\(u=4\sqrt{H\log X}\) in (6) and taking a union bound gives
\[
\mathbb P\left(\exists(v,H):
 \left|\sum_{v<n\le v+H}b(n)\right|>4\sqrt{H\log X}\right)
\le4X^{-6}.
\tag{7}
\]
The sum over \(j\) converges. Borel–Cantelli therefore gives (3) for
the base \(b\), at every sufficiently large dyadic scale and for all
these lengths simultaneously. For real \(y\) and integer \(H\), the
sum equals the one with \(v=\lfloor y\rfloor\), so no discretization
error or exceptional real starting point is introduced.

For completeness, the same base has (1) almost surely. Fix a pattern,
let \(R=1+\max_i h_i\), and split its starting indices into residue
classes modulo \(R\). Within each class the products
\(Y_n=\prod_i b(n+h_i)^{e_i}\) depend on disjoint sets of independent
signs, are bounded by one, and have mean zero because some exponent
is odd. Hoeffding concentration and Borel–Cantelli imply that their
averages tend to zero in each class. Combining the finitely many
classes proves the pattern limit. A countable intersection over patterns
establishes all of (1) simultaneously with (7). This is also the
independent-sequence case of Shi's Proposition 5.7, already used in MC-004.

Fix one realization in this probability-one set. Change its initial
values, if necessary, so that
\(b(1)=b(2)=b(3)=1\), \(b(6)=-1\). These finitely many changes preserve
all the asymptotic properties and exact support. They will make the final
control visibly nonmultiplicative.

## 2. Sparse overwrites and the exact retained-scale geometry

For integers \(k\ge2\), set
\[
j_k=3^k,\qquad N_k=2^{j_k},\qquad
L_k=\left\lfloor N_k/j_k\right\rfloor,\qquad
D_k=(N_k,N_k+L_k]\cap\mathbb N,
\quad D=\bigcup_{k\ge2}D_k.
\tag{8}
\]
Thus \(N_{k+1}=N_k^3\), \(L_k<N_k\), and
\(L_k\asymp N_k/\log N_k\). The set \(D\) has natural density zero.
Indeed, the total length of earlier blocks is \(O(N_{k-1})\), negligible
compared with \(N_k\); the current block adds at most \(N_k/j_k\).
Between the end of this block and the next one the numerator of its
counting function is constant and the denominator increases.

Define \(a=b\) outside \(D\). Recursively, after the values through
\(N_k\) are fixed, choose
\[
\sigma_k=\begin{cases}1,&A(N_k)\ge0,\\-1,&A(N_k)<0,\end{cases}
\qquad a(n)=\sigma_kq(n)\quad(n\in D_k).
\tag{9}
\]
Exact support is retained. Also \(a(6)\ne a(2)a(3)\), since all overwrite
blocks start above 6.

Take the predetermined set
\[
G=\mathbb N_{\ge1}\setminus
\bigcup_{k\ge2}\{j_k-1,j_k\}.
\tag{10}
\]
There are \(O(\log J)\) excluded indices up to \(J\). The excluded pairs
are disjoint and separated, so a run of omitted indices has length at
most two; this proves (2) and the factor-eight gap bound.

For \(j\in G\), put \(X=2^j\). The **whole** range \((X,3X]\) misses
every overwrite block. To check a fixed \(D_k\):

- if \(j\le j_k-2\), then \(3X\le3N_k/4<N_k\);
- if \(j\ge j_k+1\), then \(X\ge2N_k>N_k+L_k\).

These are exactly the possibilities left by (10). Every window in
(3) lies in \((X,3X]\), so it agrees term by term with the base window.
This proves (3) and (4) for the final deterministic sequence.
Writing \(S(y)=A(y+H)-A(y)\) and
\(m=X^{-1}\int_X^{2X}S(y)dy\), the exact identity
\[
\int_X^{2X}|S(y)-m|^2dy=J_a(X,H)-X|m|^2\le J_a(X,H)
\tag{11}
\]
also proves the centered assertion. Small empirical means are not needed;
the uncentered bound is already supplied.

## 3. Correlations survive while the prefixes become large

For each fixed pattern in (1), the products for \(a\) and \(b\) can
differ only when some \(n+h_i\) belongs to \(D\). At most
\(r|D\cap[1,T+\max h_i]|+O(1)=o(T)\) starts are affected. Each product
has modulus at most one, so the normalized difference tends to zero.
The base limits therefore give (1) for \(a\).

Let \(T_k=N_k+L_k\). The sign choice (9) yields exactly
\[
|A(T_k)|=|A(N_k)|+\sum_{N_k<n\le N_k+L_k}q(n).
\tag{12}
\]
The elementary square-free estimate
\[
Q(x):=\sum_{n\le x}q(n)=\frac{6}{\pi^2}x+O(\sqrt x)
\tag{13}
\]
follows by summing \(q(n)=\sum_{d^2\mid n}\mu(d)\): the floor errors
and \(x\) times the tail of \(\sum\mu(d)/d^2\) are both \(O(\sqrt x)\).
Since \(L_k/\sqrt{N_k}\to\infty\), equations (12)–(13) give
\[
|A(T_k)|\ge(6/\pi^2+o(1))L_k\gg T_k/\log T_k.
\tag{14}
\]
For every fixed \(c>0\), this exceeds every constant multiple of
\(T_k^{1-c}\) eventually. There is no contradiction with the one-point
Chowla limit \(A(T)=o(T)\).

## Prior art and mathematical delta

The concentration estimate is classical: Wassily Hoeffding,
[*Probability Inequalities for Sums of Bounded Random Variables*](https://doi.org/10.1080/01621459.1963.10500830),
JASA 58 (1963), 13–30. Its independent-sign specialization is proved
above. The countable-pattern existence step agrees with Ruxi Shi,
[*Construction of some Chowla sequences*, Proposition 5.7](https://link.springer.com/article/10.1007/s00605-020-01448-x).
The density-zero perturbation and square-free counting ingredients are
already audited in MC-004 and sources MC-S10–MC-S12. No new probability,
normality, or Chowla-sequence principle is claimed.

The additional local conclusion is a precise failure of a tempting
coverage repair: replacing every dyadic block by a density-one set with
bounded multiplicative gaps still does not justify generic local-to-global
interpolation, even if each retained block has complete diagonal-order
control at **every** length. MC-004 alone did not state that simultaneous
window estimate or its retained-scale geometry. A targeted search of
Chowla constructions, short-interval moments and sparse-scale controls
identified these classical ingredients, not a reason to claim external
novelty for their composition.

[MC-116](MC-116-subpower-dense-mean-absolute-checkpoints.md) is consistent
with this result: its interpolation uses a positive **cumulative**
quantity \(\int_1^X|M(t)|dt\), which retains earlier excursions.
The local increment moment (4) does not retain them. Bounded gaps are
therefore not a sufficient substitute for that monotonicity.

## Consequences, audit and remaining boundary

For any fixed \(0<\theta<1\), taking \(H=\lfloor X^\theta\rfloor\)
in (4) gives \(J_a(X,H)\ll_\varepsilon X^{1+\varepsilon}H\) at every
large retained scale, with the same \(G\) for all \(\theta\). No
exceptional-start mass or length-dependent choice of scales is hidden.
Yet (14) rules out every fixed-power global saving for this control.

The decisive checks are the summability in (7), disjointness of all
window supports from \(D\) in Section 2, preservation of fixed-pattern
limits under the density-zero overwrite, and the sign-reinforced identity
(12). These arguments establish an existence theorem; finite random
samples would establish none of its infinite-scale assertions.

The result does **not** decide whether selected-scale moment information
for Möbius, together with its exact multiplicativity and reciprocal-zeta
structure, has a stronger consequence. It also does not realize a
particular Farey selection rule. It rules out a bridge based solely on
the listed local estimates, mesh density/gaps, qualitative correlations
and exact support. An arithmetic transfer must use additional information
that connects the omitted blocks to the retained ones, or a cumulative
observable that cannot forget their contribution. No RH result,
unconditional Möbius estimate, independent adversarial approval, or formal
verification is asserted.
