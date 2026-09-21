# FD-249 — A single high-arity merge forces unbounded incidence conditioning

- **Date:** 2026-09-21
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** divisor-response sampling / exact omissions / weighted incidence inversion / divisibility antichains / conditioning lower bound
- **Depends on:** FD-225, FD-245, FD-247, FD-248
- **Classification:** `EXACT-DERIVED + SINGLE-MERGE-LOWER-BOUND + EXACT-OMISSION-REALIZATION + SUBPOLYNOMIAL-DEFECT`

## Claim

FD-248 shows that long divisibility chains and forest-like support do not enlarge the weighted inverse norm

\[
\kappa(D)
=
\max_{d\in D}
\sum_{\substack{q\in D\\q\mid d}}
|\mu_D(q,d)|\frac qd,
\]

and leaves open which merge geometries can make `kappa(D)` grow. Repeated merge depth is **not** necessary. A single top element with a sufficiently large antichain of active immediate predecessors already makes the exact-omission inverse norm unbounded.

More precisely, there is an infinite sequence of horizons `N` and exact omission responses

\[
Y(m)=(\mathscr A b)(m),\qquad 1\le m\le N,
\]

with

\[
|b_n|\le n,
\]

whose omission count `K` satisfies

\[
K=N^{o(1)},
\]

such that, for

\[
D_N=\operatorname{supp}(\Delta Y)\cap[1,N],
\]

the induced divisibility interval below the top active point `N` is a height-one star: all active proper divisors of `N` are pairwise incomparable and are covered directly by `N`. Nevertheless

\[
\boxed{
\kappa(D_N)
\gg
\frac{\log\log N}{\sqrt{\log\log\log N}}.
}
\tag{1}
\]

Thus **one high-arity merge is already sufficient for unbounded conditioning**. The growth comes from the reciprocal mass of one weighted antichain in a squarefree divisor lattice, not from chain depth or repeated nested merges.

This does not produce macroscopic hidden coefficient mass: the lower bound in (1) is still tiny compared with the `N/K` conditioning required by FD-248 for a sublinear omission family to carry top-scale mass. Its role is structural. Any attempt to prove a uniform `O(1)` bound for `kappa(D)` from bounded depth, absence of long chains, or absence of repeated merges is false even for exact omission supports.

## A weighted rank of a primorial divisor lattice carries large reciprocal mass

Let

\[
R_y:=\prod_{p\le y}p.
\tag{2}
\]

For `0<=k<=pi(y)` define the reciprocal mass of the `k`th squarefree rank

\[
S_k(y)
:=
\sum_{\substack{r\mid R_y\\\omega(r)=k}}
\frac1r.
\tag{3}
\]

The total reciprocal divisor mass is

\[
T_y
:=
\sum_{r\mid R_y}\frac1r
=
\prod_{p\le y}\left(1+\frac1p\right)
\asymp \log y.
\tag{4}
\]

The last comparison is the standard Mertens consequence of the prime number theorem: write

\[
\prod_{p\le y}\left(1+\frac1p\right)
=
\prod_{p\le y}\left(1-\frac1{p^2}\right)
\prod_{p\le y}\left(1-\frac1p\right)^{-1}.
\]

Normalize the weights `1/r` to a probability measure on divisors of `R_y`:

\[
\mathbb P(X=r)=\frac{1/r}{T_y}.
\tag{5}
\]

Under this measure the prime-divisibility indicators are independent and

\[
\mathbb P(p\mid X)=\frac1{p+1}.
\tag{6}
\]

Hence, for `W=omega(X)`,

\[
\mathbb E W
=
\sum_{p\le y}\frac1{p+1}
=
\log\log y+O(1),
\tag{7}
\]

and

\[
\operatorname{Var}(W)
=
\sum_{p\le y}\frac{p}{(p+1)^2}
=
\log\log y+O(1).
\tag{8}
\]

Chebyshev gives probability at least `3/4` to an interval of `O(sqrt(log log y))` consecutive values of `W`. Therefore at least one rank `k=k(y)` in that interval satisfies

\[
\frac{S_k(y)}{T_y}
\gg
\frac1{\sqrt{\log\log y}},
\]

so

\[
\boxed{
S_k(y)
\gg
\frac{\log y}{\sqrt{\log\log y}}.
}
\tag{9}
\]

For large `y`, this selected rank has

\[
k=O(\log\log y),\qquad 1\le k<\pi(y).
\tag{10}
\]

No optimal weighted-Sperner statement is needed here; concentration of the product measure already supplies a rank with the required mass.

## Realizing that rank inside an exact omission support

The adjacent-pair constraint from exact omissions matters: an omitted value at `q` normally activates both `q` and `q+1` in `Delta Y`. We now separate those companions from the divisor interval that will carry the large row norm.

Put

\[
L_y:=R_y+1,
\qquad
N_y:=L_yR_y.
\tag{11}
\]

Then `gcd(L_y,R_y)=1` and `L_y>R_y`. For the rank `k=k(y)` supplied by (9), define

\[
\mathcal R_y
:=
\{r:r\mid R_y,\ \omega(r)=k\},
\]

and

\[
Q_y
:=
\left\{
q_r:=\frac{N_y}{r}:r\in\mathcal R_y
\right\}.
\tag{12}
\]

Because all `r in mathcal R_y` have the same number of prime factors, they form a divisibility antichain. Reversing divisibility in (12), the set `Q_y` is also a divisibility antichain. Every `q_r` is a multiple of `L_y`, and distinct elements of `Q_y` differ by at least `L_y`, so the pairs `{q_r,q_r+1}` are disjoint.

Moreover `r` is a proper divisor of `R_y` by (10), so `R_y/r>=2` and

\[
q_r=L_y\frac{R_y}{r}>R_y.
\tag{13}
\]

Since `q_r` is a multiple of `L_y`,

\[
\gcd(q_r+1,L_y)=1.
\]

If `q_r+1` divided `N_y=L_yR_y`, it would therefore divide `R_y`, contradicting `q_r+1>R_y`. Thus

\[
\boxed{q_r+1\nmid N_y\qquad(r\in\mathcal R_y).}
\tag{14}
\]

Now define the response on `[0,N_y]` by

\[
Y(0)=0,
\qquad
Y(m)=
\begin{cases}
1,&m\in Q_y\cup\{N_y\},\\
0,&\text{otherwise}.
\end{cases}
\tag{15}
\]

Its exact omission set is

\[
E_y=Q_y\cup\{N_y\}.
\tag{16}
\]

Because the points of `Q_y` are separated by more than one and lie below `N_y/2`, the increment

\[
g=\Delta Y
\]

has support

\[
D_y
=
Q_y\cup(Q_y+1)\cup\{N_y\},
\tag{17}
\]

with value `+1` on `Q_y` and at `N_y`, and value `-1` on `Q_y+1`.

Define

\[
b=\mathbf1*g.
\tag{18}
\]

Then `mu*b=g`, and the exact divisor-response identity used since FD-225 gives

\[
(\mathscr A b)(m)
=
\sum_{j\le m}g(j)
=
Y(m).
\tag{19}
\]

Thus (15) is not merely an abstract support pattern: it is an exact response generated by a coefficient sequence. Since every nonzero `g(d)` has modulus one,

\[
|b_n|
\le
\sum_{d\mid n}|g(d)|
\le
\tau(n)
\le n,
\tag{20}
\]

so the same linear coefficient envelope used in FD-247--FD-248 holds with `C=1`.

## The top row is a single merge star

By (14), none of the companion points `q_r+1` divides `N_y`. Therefore the active divisors of `N_y` inside `D_y` are exactly

\[
Q_y\cup\{N_y\}.
\tag{21}
\]

The elements of `Q_y` are pairwise incomparable, so in the induced divisibility poset each of them is covered directly by `N_y`. Hence

\[
\mu_{D_y}(q_r,N_y)=-1
\qquad(r\in\mathcal R_y),
\tag{22}
\]

and there is no deeper active chain inside these intervals. The weighted inverse row at `N_y` is therefore exactly

\[
\begin{aligned}
\sum_{\substack{q\in D_y\\q\mid N_y}}
|\mu_{D_y}(q,N_y)|\frac q{N_y}
&=
1+
\sum_{r\in\mathcal R_y}\frac{q_r}{N_y}\\
&=
1+
\sum_{r\in\mathcal R_y}\frac1r\\
&=
1+S_k(y).
\end{aligned}
\tag{23}
\]

Combining (9) and (23),

\[
\kappa(D_y)
\gg
\frac{\log y}{\sqrt{\log\log y}}.
\tag{24}
\]

Finally the prime number theorem gives

\[
\log R_y=\vartheta(y)\sim y,
\]

while `N_y=R_y(R_y+1)`. Hence

\[
\log\log N_y=\log y+O(1),
\qquad
\log\log\log N_y=\log\log y+O(1),
\tag{25}
\]

and (24) becomes the asserted bound (1).

## The omission count is subpolynomial

The number of omitted points is

\[
K_y=|E_y|
=\binom{\pi(y)}{k}+1.
\tag{26}
\]

From (10), `k=O(log log y)`, and the elementary binomial estimate gives

\[
\log K_y
\le
k\log\!\left(\frac{e\pi(y)}k\right)+O(1)
=O((\log\log y)(\log y))
=o(y).
\tag{27}
\]

Using `log N_y asymp y`,

\[
\boxed{K_y=N_y^{o(1)}.}
\tag{28}
\]

Thus unbounded incidence conditioning already occurs for an extremely sparse exact-omission family. The obstruction to bounded `kappa` is not a high density of omitted response points; it is the weighted branching geometry seen by the top divisor row.

## Finite audit example

For `y=5`,

\[
R_y=30,
\qquad
L_y=31,
\qquad
N_y=930.
\]

Taking the one-prime rank gives

\[
Q_y=\{930/2,930/3,930/5\}
=\{465,310,186\}.
\]

The exact response supported on `{186,310,465,930}` activates the companion increments `{187,311,466}`, none of which divides `930`. The active divisor interval below `930` is therefore the three-branch star, and its weighted inverse row is

\[
1+\frac12+\frac13+\frac15
=\frac{61}{30}.
\]

This small case is only a consistency check; the asymptotic growth comes from selecting the concentrated reciprocal-weight rank in (9).

## Prior-art / novelty audit

Divisibility antichains are classical primitive sets, and LYM/Sperner-type inequalities for divisor lattices and products of chains are well established; Chudak and Griggs, *A new extension of Lubell's inequality to the lattice of divisors* (1999), is a nearby finite-poset reference. The modern primitive-set literature, including Lichtman's proof of the Erdos primitive-set conjecture, studies different global weights such as `1/(n log n)`. Rank-selected Möbius functions of Boolean algebras/products of chains are also classical objects related to descent-set enumeration.

Those results are prior-art boundaries, not load-bearing inputs. The proof above uses only the exact divisor-response inversion already established in this line, elementary product-measure concentration, and standard PNT/Mertens consequences already anchored in `SOURCES.md`. A targeted search did not reveal the specific exact-omission realization (11)--(23), nor the conclusion that one height-one weighted merge inside the active response support forces the lower bound (1). No novelty is claimed for primitive sets, weighted Boolean ranks, or poset Möbius inversion themselves.

## Boundary and next audit

This is still a signed exact-response statement. It does not impose positivity, finite prime-reservoir capacity, squarefree physical-source realization, or full Möbius coherence, and it gives no new Farey/RH bound.

It also does **not** show that the incidence norm can reach the `N/K` scale required by FD-248 to hide macroscopic coefficient mass. In this construction `K=N^{o(1)}` and `kappa(D)` is only polylogarithmic. The result instead closes a structural possibility: conditioning growth does not require deep or repeated merges.

The next exact-response question is now sharper. One should determine the maximal possible `kappa(D)` for genuine adjacent-pair omission supports, and in particular whether nested/rank-selected merge geometry can beat the single-star scale in (1), or whether a universal polylogarithmic upper bound survives. Any such upper bound must explicitly control high-arity weighted antichains; chain-depth arguments alone cannot do it.

## Status

**Proved.** The primorial-rank concentration, exact adjacent-pair response realization, star-row identity, subpolynomial omission count, and lower bound (1) are finite/exact apart from the standard asymptotics used to express their growth in terms of `N`. The finding advances the FD-248 conditioning frontier without claiming a physical source theorem or an RH implication.
