# FD-180 — Subpolynomial deletion sources pay an exact prime-extension defect floor

- **Date:** 2026-09-17
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** relational source rigidity / prime-extension ancestry / sparse deletion boundary / dyadic-null discriminator
- **Depends on:** FD-147, FD-175, FD-179
- **Classification:** `EXACT-DERIVED + RELATIONAL-RIGIDITY + PRIME-EXTENSION-BOUNDARY + SUBPOLYNOMIAL-DELETION + DYADIC-NULL-COROLLARY`

## Claim

`FD-175`--`FD-179` show that coordinatewise fidelity can be pushed almost to the maximal squarefree-rank boundary while one permanent deletion-only source still matches every dyadic Farey midpoint. The missing discriminator must therefore relate different source coordinates. In the deletion-only class, the first such relation has an exact quantitative floor.

Let

\[
a(n)\in\{0,\mu(n)\}\qquad(n\ge1),
\tag{1}
\]

assume that every prime is physical,

\[
a(p)=\mu(p)=-1\qquad(p\text{ prime}),
\tag{2}
\]

and write

\[
S:=\{n:\mu(n)\ne0,\ a(n)=0\},
\qquad
S(x):=|S\cap[1,x]|.
\tag{3}
\]

On the squarefree prime-extension graph

\[
E_x:=\{(n,pn):pn\le x,\ p\text{ prime},\ p\nmid n,\ \mu^2(n)=1\},
\tag{4}
\]

define the multiplicative-relation defect count

\[
B_a(x):=
\#\{(n,pn)\in E_x:a(pn)+a(n)\ne0\}.
\tag{5}
\]

Because `a(p)=-1`, exact multiplicativity along a prime extension would require `a(pn)=-a(n)`. For a deletion-only source, the defect in (5) is therefore exactly the edge boundary of `S`: an edge contributes iff precisely one endpoint has been deleted.

There are two levels of rigidity.

First, if `S` is nonempty and `n_0=min S`, then for every `x>=2n_0`,

\[
\boxed{
B_a(x)+S(x)
\ge
\pi(x/n_0)-\omega(n_0).
}
\tag{6}
\]

Thus any nontrivial deletion-only source with `S(x)=o(x/log x)` must already pay

\[
B_a(x)\gg_{n_0}\frac{x}{\log x}.
\tag{7}
\]

Second, if the deletion set is subpolynomial,

\[
S(x)=x^{o(1)},
\tag{8}
\]

then its reciprocal mass

\[
\boxed{
C_S:=\sum_{n\in S}\frac1n
}
\tag{9}
\]

converges, is positive when `S` is nonempty, and one has the exact first-order asymptotic

\[
\boxed{
B_a(x)
=
(C_S+o(1))\frac{x}{\log x}.
}
\tag{10}
\]

Using the squarefree ancestry edge count from `FD-147`,

\[
|E_x|
=
\frac{x}{\zeta(2)}\log\log x+O(x),
\tag{11}
\]

we obtain, for every fixed `1<=q<infinity`,

\[
\boxed{
\left(
\frac1{|E_x|}
\sum_{(n,pn)\in E_x}|a(pn)+a(n)|^q
\right)^{1/q}
=
\left(
\frac{\zeta(2)C_S+o(1)}{\log x\,\log\log x}
\right)^{1/q}.
}
\tag{12}
\]

Consequently, inside the deletion-only class with (2) and (8), the genuinely weaker relational condition

\[
\boxed{
\left(
\frac1{|E_x|}
\sum_{(n,pn)\in E_x}|a(pn)+a(n)|^q
\right)^{1/q}
=o\!\left((\log x\,\log\log x)^{-1/q}\right)
}
\tag{13}
\]

already forces `S=emptyset`, hence `a=mu`. Exact multiplicativity is not required: beating the natural prime-extension boundary scale suffices.

Applied to the permanent dyadic-null source of `FD-179`, whose deletion count is subpolynomial and whose corrections are high-rank composites, (10)--(12) show that all dyadic midpoint measurements can remain exactly physical while multiplicativity fails on only a vanishing proportion

\[
\frac{B_a(x)}{|E_x|}
\sim
\frac{\zeta(2)C_S}{\log x\,\log\log x}
\tag{14}
\]

of prime-extension relations. Thus merely asking for **average multiplicativity tending to zero** is still too weak; the rate relative to the scale in (14) is the first effective relational separator for this sparse-null mechanism.

## 1. A single deleted coefficient emits a prime fan

Let `n_0=min S`. For each prime

\[
p\le x/n_0,
\qquad
p\nmid n_0,
\tag{15}
\]

the edge `(n_0,n_0p)` belongs to `E_x`. Since `n_0` is deleted, exactly one of two things happens.

If `n_0p notin S`, the edge crosses the deletion boundary and contributes to `B_a(x)`. If `n_0p in S`, it contributes a distinct deleted coefficient to `S(x)`. Different primes give different children. At most `omega(n_0)` primes are excluded by `p|n_0`, so

\[
\pi(x/n_0)-\omega(n_0)
\le
B_a(x)+S(x),
\tag{16}
\]

which proves (6).

This finite injection already answers part of the live cross-coordinate question left by `FD-179`. A permanent defect cannot remain isolated once the prime-extension law is inspected: every deleted coordinate has an infinite fan of forced descendants, and hiding the fan by deleting the descendants consumes approximately `x/log x` additional coordinates. The `FD-179` source is far too sparse to do that, so its failure must remain visible in the relational channel even though it is invisible to every dyadic midpoint sample.

## 2. Subpolynomial support has finite reciprocal mass

Assume (8). For every fixed `epsilon>0`, eventually

\[
S(t)\le t^\epsilon.
\tag{17}
\]

Taking for instance `epsilon=1/2` and applying partial summation to the counting measure of `S`,

\[
\sum_{\substack{n\in S\\n>Y}}\frac1n
\le
\frac{S(Y)}Y+
\int_Y^\infty\frac{S(t)}{t^2}\,dt,
\tag{18}
\]

shows that the series in (9) converges. If `S` is nonempty every summand is positive, so `C_S>0`.

This is the only place where the full subpolynomial hypothesis is needed. The cruder finite-fan lower bound (6) requires no density assumption at all.

## 3. Count all outgoing prime extensions from the deletion set

Let

\[
O_S(x):=
\sum_{\substack{n\in S\\n\le x/2}}
\#\{p\le x/n:p\text{ prime},\ p\nmid n\}.
\tag{19}
\]

We first show

\[
\boxed{
O_S(x)
=(C_S+o(1))\frac{x}{\log x}.
}
\tag{20}
\]

Fix `M`. For every fixed `n<=M`, the prime number theorem gives

\[
\#\{p\le x/n:p\nmid n\}
=
(1+o(1))\frac{x}{n\log x},
\tag{21}
\]

because excluding the finitely many prime divisors of `n` changes the count by `O(omega(n))`. Summing over the finite set `S cap [1,M]` gives

\[
\sum_{\substack{n\in S\\n\le M}}
\#\{p\le x/n:p\nmid n\}
=
\left(
\sum_{\substack{n\in S\\n\le M}}\frac1n+o_M(1)
\right)
\frac{x}{\log x}.
\tag{22}
\]

For `M<n<=sqrt(x)`, the standard upper bound `pi(y)<<y/log y` and `log(x/n)>=\tfrac12 log x` give

\[
\sum_{\substack{n\in S\\M<n\le\sqrt x}}
\pi(x/n)
\ll
\frac{x}{\log x}
\sum_{\substack{n\in S\\n>M}}\frac1n.
\tag{23}
\]

The reciprocal tail tends to zero as `M->infinity`. For `sqrt(x)<n<=x/2`, use only `pi(x/n)<=x/n<=sqrt(x)`. The number of possible parents is at most `S(x)=x^{o(1)}`, so this whole range contributes

\[
x^{1/2+o(1)}
=o(x/\log x).
\tag{24}
\]

Finally, excluding primes that divide their parent costs at most

\[
\sum_{\substack{n\in S\\n\le x}}\omega(n)
\le
S(x)\log_2 x
=x^{o(1)}
=o(x/\log x).
\tag{25}
\]

Letting first `x->infinity` and then `M->infinity` in (22)--(24) proves (20).

## 4. Internal deletions are negligible compared with the prime fan

Let `J_S(x)` be the number of prime-extension edges in `E_x` whose child belongs to `S`. Every squarefree child `m` has exactly `omega(m)` incoming prime-extension edges, hence

\[
J_S(x)
\le
\sum_{\substack{m\in S\\m\le x}}\omega(m)
\le
S(x)\log_2 x
=x^{o(1)}.
\tag{26}
\]

Let `I_S(x)` be the number of internal edges having both endpoints in `S`. Then `I_S(x)<=J_S(x)`. Since a boundary edge is either an outgoing edge from a deleted parent to an undeleted child or an incoming edge from an undeleted parent to a deleted child,

\[
B_a(x)
=
O_S(x)+J_S(x)-2I_S(x).
\tag{27}
\]

Equations (20) and (26) now give (10).

For deletion-only coefficients, every defect in (5) has magnitude exactly `1`, independent of `q`. Therefore the numerator in the `q`-th power of (12) is exactly `B_a(x)`. Combining (10) with the ancestry edge asymptotic (11) proves (12), and (13) follows because `C_S` is either zero exactly when `S` is empty or strictly positive otherwise.

## 5. What this does and does not resolve

The result supplies a concrete answer to one part of the current line frontier. Full multiplicativity is stronger than necessary for excluding the `FD-179` sparse-null construction. What is needed, within this source class, is enough cross-coordinate consistency to beat the unavoidable prime-fan boundary scale. A normalized finite-`L^q` multiplicativity defect merely tending to zero does **not** do that; decay strictly faster than `(log x loglog x)^(-1/q)` does.

This does not contradict `FD-147`. That finding shows that normalized finite-`L^q` ancestry energy can vanish at the same order while a binary orientation is wrong on a macroscopic fraction of vertices. Here the coefficient error is at the opposite extreme: the deletion set is subpolynomial and may be confined to the near-maximal-rank cap of `FD-179`. The new point is that even such a tiny error set emits a first-order `x/log x` prime fan, so the same normalized scale reappears for a completely different reason. `FD-147` is an anchored-cut coercivity obstruction; (10) is an exact sparse-boundary asymptotic tied to a permanent Farey-null source.

The theorem is source-class specific. Allowing arbitrary signed perturbations, allowing prime coefficients themselves to move, or measuring a different relation can create cancellations absent from the deletion-only boundary count. Nor does (13) prove the Franel--Landau RH-critical estimate. It only kills this particular source-identifiability escape once one adds a quantitatively strong enough relational law.

## Representation audit

The Farey observable is unchanged: the corollary uses exactly the permanent dyadic midpoint-null source already constructed in `FD-179`. The new coordinate is not another Farey measurement but an explicit source-faithfulness test on the prime-extension ancestry graph. It is therefore deliberately outside the midpoint quotient and tests the relational information that `FD-175`--`FD-179` had discarded.

The generic part of the argument is a boundary principle for a sparse subset of a graph with many prime-labelled outgoing edges. The arithmetic splice is that squarefree Möbius values satisfy `mu(pn)=-mu(n)` and the prime number theorem turns one surviving parent into `x/log x` descendants. Equation (11) then normalizes that boundary against the full squarefree ancestry graph. No information from another Mathia research line is used.

## Prior-art audit

Targeted searches were run for approximate multiplicativity of arithmetic functions, prime/divisor graphs, edge boundaries of squarefree divisor structures, and prime-extension relations. The neighboring literature includes pretentious multiplicative-function metrics and divisibility-graph expansion, but those interfaces either assume genuine multiplicativity or study different graph operators; no direct analogue of the sparse deletion boundary asymptotic (10) coupled to an exact dyadic Farey-null source was found.

No external theorem beyond the prime number theorem is load-bearing in the new derivation. The PNT and the squarefree ancestry edge count are already anchored in `SOURCES.md` and `FD-147`, respectively, so no source-list update is required. No claim is made that graph boundary counting or the PNT argument is novel in isolation; the durable contribution is the exact relational threshold they impose on the existing Farey midpoint null-source mechanism.
