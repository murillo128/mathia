# FD-178 — Variable dyadic blocks hide second-order near-maximal multiplicative-rank fidelity

- **Date:** 2026-09-17
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** restricted temporal acquisition / variable dyadic block repair / near-maximal multiplicative-rank compatibility / sparse permanent null source
- **Depends on:** FD-117, FD-170, FD-172, FD-173, FD-175, FD-176, FD-177
- **Classification:** `EXACT-DERIVED + PERMANENT-SOURCE + DYADIC-NULL + SECOND-ORDER-EXTREMAL-RANK-FIDELITY + SUBEXPONENTIAL-DELETION + NONMULTIPLICATIVE`

## Claim

`FD-177` showed that exact fidelity on every fixed subextremal rank cone

\[
\omega(n)\le \rho\frac{\log n}{\log\log n},
\qquad \rho<1,
\]

does not restore dyadic midpoint rigidity once global multiplicativity is removed. Its block length was fixed, so it left open the endpoint regime in which the protected rank itself approaches the maximal possible squarefree rank.

That boundary can be pushed past the leading endpoint.

Fix any

\[
0<c<1
\tag{1}
\]

and any finite cutoff `X`. There exists one permanent arithmetic source `a\not\equiv\mu` such that

\[
a(n)\in\{0,\mu(n)\}\qquad(n\ge1),
\tag{2}
\]

\[
a(n)=\mu(n)\qquad(n\le X),
\tag{3}
\]

and, for every sufficiently large squarefree `n`,

\[
\boxed{
\omega(n)\le
\frac{\log n}{\log\log n}
\left(
1+\frac{c}{\log\log n}
\right)
\quad\Longrightarrow\quad
a(n)=\mu(n).
}
\tag{4}
\]

Nevertheless the entire dyadic midpoint ladder remains exactly physical:

\[
\boxed{
P_a(2^m)=P_\mu(2^m)
\qquad\text{for every }m\ge1.
}
\tag{5}
\]

If

\[
S:=\{n:\mu(n)\ne0,\ a(n)=0\}
\tag{6}
\]

is the deletion set, the construction may moreover be chosen with

\[
\boxed{
\log(2+S(x))
=
O_{c,X}\!\left(
(\log x)^{2/3}(\log\log x)^{4/3}
\right).
}
\tag{7}
\]

In particular

\[
S(x)
=
\exp\!\left(
o\!\left(\frac{\log x}{\log\log x}\right)
\right)
=
x^{o(1)}.
\tag{8}
\]

Thus coordinatewise multiplicative fidelity can extend not merely to `(1-o(1)) log n/loglog n`, but beyond the leading scale by any fixed fraction `c<1` of its first extremal correction, while exact dyadic target-rigidity still fails.

## 1. The exact block lemma of FD-177 is uniform in the block length

Retain the deletion balance

\[
C_H(S)
=
\sum_{\substack{d\in S\\d\le H}}
-\mu(d)\,W_H(d),
\qquad
W_H(d)
=
\left\lfloor\frac{H}{2d}+\frac12\right\rfloor,
\tag{9}
\]

so that

\[
P_a(H)=P_\mu(H)
\iff
C_H(S)=0.
\tag{10}
\]

`FD-177` proves the following finite statement for every integer `k>=2`.

Suppose the old deletion support is contained in `[1,L]`, `C_L=0`, and there are `N` old deletions. There are `k` pairwise disjoint intervals

\[
I_s(L,k)\subset(L,2L],
\qquad 1\le s\le k,
\tag{11}
\]

each of length

\[
|I_s(L,k)|\asymp 2^{-k}L
\tag{12}
\]

with absolute comparison constants, such that signed deletions chosen from those intervals can cancel simultaneously all `k` responses

\[
C_{2L},C_{4L},\ldots,C_{2^kL}.
\tag{13}
\]

The response vectors form an integer unimodular basis, and the binary nearest-integer cocycle gives the total correction budget

\[
M_{\rm fresh}\le kN.
\tag{14}
\]

Nothing in this finite algebra requires `k` to remain fixed from one block to the next. The fixed-`k` restriction in `FD-177` entered only when populating every `I_s` by a prime reservoir with constants depending on `k`.

We now let the block length grow.

Write

\[
y=\log L,
\qquad
\ell=\log y,
\tag{15}
\]

and at block base `L_j` choose

\[
\boxed{
k_j=
\left\lceil
\left(
\frac{\log L_j}{\log\log L_j}
\right)^{1/3}
\right\rceil.
}
\tag{16}
\]

The next block base is

\[
L_{j+1}=2^{k_j}L_j.
\tag{17}
\]

If `N_j` is the number of deletions present at `L_j`, (14) yields

\[
N_{j+1}\le(k_j+1)N_j.
\tag{18}
\]

Since

\[
\log L_{j+1}-\log L_j
=
(\log2)k_j
\tag{19}
\]

while

\[
\log N_{j+1}-\log N_j
\le
\log(k_j+1),
\tag{20}
\]

the source budget now grows much more slowly than the horizon.

More quantitatively, for `y_j=\log L_j`,

\[
\frac{\log(k_j+1)}{k_j}
\ll
y_j^{-1/3}(\log y_j)^{4/3}.
\tag{21}
\]

Summing (20) against the increments (19), or comparing with the corresponding integral, gives

\[
\boxed{
\log N_j
=
O\!\left(
y_j^{2/3}(\log y_j)^{4/3}
\right).
}
\tag{22}
\]

Because

\[
y^{2/3}(\log y)^{4/3}
=
o\!\left(\frac{y}{\log y}\right),
\tag{23}
\]

we obtain

\[
N_j
=
\exp\!\left(
o\!\left(\frac{\log L_j}{\log\log L_j}\right)
\right).
\tag{24}
\]

This is the amount of signed correction capacity that the arithmetic reservoir must beat.

## 2. Near-primorial corrections live above the leading maximal-rank scale

Fix an intermediate constant

\[
c<c_1<1.
\tag{25}
\]

At a large block base `L`, with `y` and `ell` as in (15), put

\[
r=
\left\lfloor
\frac{y}{\ell}
\left(
1+\frac{c_1}{\ell}
\right)
\right\rfloor,
\tag{26}
\]

adjusting `r` by at most one when a prescribed Möbius sign is required. Let

\[
P_r=p_1p_2\cdots p_r.
\tag{27}
\]

The quantitative prime number theorem already anchored in `SOURCES.md` gives, by the standard inversion of `pi(x)=li(x)+O(xe^{-a\sqrt{\log x}})`,

\[
p_r
=
r\left(
\log r+\log\log r-1
+
O\!\left(\frac{\log\log r}{\log r}\right)
\right),
\tag{28}
\]

and

\[
\log P_r
=
\vartheta(p_r)
=
p_r+O\!\left(p_re^{-a\sqrt{\log p_r}}\right).
\tag{29}
\]

For (26),

\[
\log r
=
\ell-\log\ell+\frac{c_1}{\ell}
+
O(\ell^{-2}),
\tag{30}
\]

\[
\log\log r
=
\log\ell-\frac{\log\ell}{\ell}
+
O\!\left(\frac{\log\ell}{\ell^2}\right).
\tag{31}
\]

Substitution in (28)--(29) gives

\[
\boxed{
\log P_r
=
y\left[
1-\frac{1-c_1}{\ell}
+
O\!\left(\frac{\log\ell}{\ell^2}\right)
\right].
}
\tag{32}
\]

Hence the remaining prime factor lives at scale

\[
Q:=\frac{L}{P_r},
\tag{33}
\]

with

\[
\boxed{
\log Q
=
\left(
1-c_1+o(1)
\right)
\frac{\log L}{\log\log L}.
}
\tag{34}
\]

Although `Q=L^{o(1)}`, it is exponentially large on the `log L/loglog L` scale.

Now take any fresh response interval `I_s(L,k)` from (11). Dividing by `P_r` produces a prime interval at scale `Q` of relative width comparable with

\[
\delta_L:=2^{-k}.
\tag{35}
\]

For the choice (16),

\[
k
=
O\!\left(
\left(\frac{y}{\ell}\right)^{1/3}
\right),
\tag{36}
\]

whereas (34) gives

\[
\sqrt{\log Q}
\asymp
\left(\frac{y}{\ell}\right)^{1/2}.
\tag{37}
\]

Therefore

\[
2^{-k}
\gg
e^{-a\sqrt{\log Q}}
\tag{38}
\]

for every fixed positive `a` and all sufficiently large `L`.

The de la Vallée Poussin error term can consequently be subtracted across each shrinking interval. Uniformly in `1<=s<=k`,

\[
\#\left\{
q\ {\rm prime}:
P_rq\in I_s(L,k)
\right\}
\gg
\frac{2^{-k}Q}{\log Q}.
\tag{39}
\]

By (34)--(36),

\[
\log\left(\frac{2^{-k}Q}{\log Q}\right)
=
\left(
1-c_1+o(1)
\right)
\frac{y}{\ell}.
\tag{40}
\]

This dominates the full correction demand from (22):

\[
kN
=
\exp\!\left(o(y/\ell)\right).
\tag{41}
\]

Changing the parity of `r` by one supplies either Möbius sign; the resulting extra prime factor in `P_r` changes (34) only by `O(log y)`, negligible on the `y/ell` scale. Also `q>p_r` eventually, so every correction integer `P_rq` is squarefree and has

\[
\omega(P_rq)=r+1.
\tag{42}
\]

Thus every signed coefficient demanded by the exact unimodular repair can be populated by distinct squarefree integers in the appropriate response interval.

## 3. Every correction lies above the protected second-order rank window

For `n\in(L,2L]`,

\[
\frac{\log n}{\log\log n}
=
\frac{y}{\ell}
\left(
1+o(\ell^{-1})
\right),
\tag{43}
\]

and

\[
\frac1{\log\log n}
=
\frac1\ell+o(\ell^{-2}).
\tag{44}
\]

Equations (26), (42)--(44) therefore imply

\[
\omega(n)
=
\frac{\log n}{\log\log n}
\left(
1+\frac{c_1}{\log\log n}
+
o\!\left(\frac1{\log\log n}\right)
\right).
\tag{45}
\]

Since `c_1>c`, every correction integer eventually satisfies

\[
\omega(n)
>
\frac{\log n}{\log\log n}
\left(
1+\frac{c}{\log\log n}
\right).
\tag{46}
\]

So the whole protected region (4) remains untouched.

To seed a nontrivial source, start after the prescribed cutoff and choose two admissible squarefree deletions of opposite Möbius sign in the same first response interval. Their complete first-block response vectors agree, so their signed contributions cancel. Thereafter apply the block repair recursively with the variable lengths (16). Every dyadic horizon is included in exactly one block, hence (5) holds for the resulting permanent source.

The estimate (22) propagates between block bases because `k_j=o(\log L_j)`, yielding (7)--(8).

There is a useful extremal comparison. If

\[
R(x):=\max_{n\le x}\omega(n),
\tag{47}
\]

then the smallest integer with `r` distinct prime factors is the `r`-th primorial. The same expansion (32), inverted at `P_r\asymp x`, gives

\[
\boxed{
R(x)
=
\frac{\log x}{\log\log x}
\left[
1+\frac1{\log\log x}
+
O\!\left(
\frac{\log\log\log x}{(\log\log x)^2}
\right)
\right].
}
\tag{48}
\]

Thus (4) reaches any fixed fraction `c<1` of the first correction from the leading scale to the true extremal rank. The repair reservoir is confined to the remaining near-primorial cap.

## 4. Stress tests and boundary

The gain is not obtained by weakening the observation family. Every dyadic midpoint sample remains exact, the source is permanent, all coefficients keep the physical Möbius sign when nonzero, and no nonsquarefree support is introduced.

The new ingredient relative to `FD-177` is not a different finite response basis. It is the scale separation created by allowing the exact block length to grow. The combinatorial repair cost becomes

\[
\exp(o(\log L/\log\log L)),
\]

while a near-primorial coefficient with rank (26) still leaves a final prime factor in a reservoir of size

\[
\exp((1-c_1+o(1))\log L/\log\log L).
\]

The quantitative PNT is strong enough to populate the `2^{-k}`-thin response cells because their logarithmic width cost is only `O((log L/loglog L)^{1/3})`, below the `sqrt(log Q)` zero-free-region scale.

The constant `1` in (48) is now the real coordinatewise frontier of this mechanism. This pass does **not** preserve every squarefree coefficient except on a null set, and it does not reach a protected window whose second-order coefficient tends to `1`. At `c=1` the residual factor scale in (34) loses its fixed positive `log L/loglog L` exponent, so the current reservoir comparison no longer closes.

Nor does the result challenge `FD-172`--`FD-174`: those theorems remain exact inside the globally multiplicative cone. The construction still breaks the product law precisely on a tiny family of near-primorial composites. What is ruled out is a much stronger coordinatewise substitute for multiplicativity.

## Representation audit

The representation is unchanged from `FD-170`, `FD-175`, and `FD-177`. The midpoint temporal sensor is kept in its exact odd-multiple weight form (9), and the proof uses the same dyadic response vectors. No new norm, reconstruction map, or target-dependent observable is introduced.

The generic part is a variable-length rounded-dilation block system with a unimodular fresh-shell basis. The Farey/Möbius-specific splice is the exact weight `W_H(d)`, the binary doubling cocycle behind `FD-177`, and the ability to realize prescribed signs by squarefree near-primorial integers while staying inside each response cell.

The information deliberately lost is now extremely localized: global multiplicativity is allowed to fail only on a subexponential family of coefficients lying in the second-order near-maximal `omega` cap. Prime data, every finite prefix, squarefree support, coefficient signs, and the entire rank region (4) remain physical.

## Prior-art audit

A targeted search was run for Farey midpoint reconstruction under lacunary horizons, dyadic nearest-integer cocycles, sparse Möbius null sources, primorial extremal rank, and shrinking relative prime intervals. The search found the classical Farey midpoint symmetry and standard lacunary/rounding literature, but no direct analogue of the permanent blockwise null construction.

The second-order expansion (28) is classical, going back to Cipolla; modern treatments such as Juan Arias de Reyna and Jérémy Toulisse, *The n-th prime asymptotically*, Journal de théorie des nombres de Bordeaux **25** (2013), 521--555, systematize the full expansion. No part of that expansion is claimed new here. For the present argument, (28) is obtained by the standard inversion of the quantitative prime number theorem already anchored locally, and the shrinking-interval lower bound (39) is a direct subtraction of the same de la Vallée Poussin error term. No new durable external theorem dependency is introduced, so `SOURCES.md` is unchanged.

The finite block algebra is already proved in `FD-177`. The new mathematical content is the variable-block schedule, the sub-`exp(log L/loglog L)` correction budget, and its splice to the second-order near-primorial reservoir.

## Formalization and compute audit

No compute handoff is needed: the proof is asymptotic and exact, with no parameter optimization that depends on numerical evidence.

The finite block lemma remains formally bounded, but the substantive strengthening here depends on second-order prime inversion and primes in shrinking relative intervals through the quantitative PNT. Formalizing only the combinatorial schedule would not certify the new near-maximal-rank statement, so no formalization issue is opened in this pass.

## Consequence for the research frontier

`FD-177` left open `(1-o(1)) log n/loglog n` as the coordinatewise endpoint. The present result crosses that leading endpoint and leaves only the **second-order extremal cap**: the maximal possible rank has coefficient `1` in the first `1/loglog n` correction, while every fixed coefficient `c<1` can still be protected by a nonmultiplicative exact dyadic null source.

The remaining coordinatewise question is therefore much narrower: can a variable repair be pushed to a window with

\[
c=c(n)\to1,
\]

or all the way to every squarefree rank? The more structural alternative remains unchanged: identify a genuinely cross-coordinate compatibility that propagates the correct low-rank product law into this rare near-primorial cap. Pairwise sparse inversion and destination coercivity toward the Franel--Landau norm also remain separate obligations.

No accepted clue changes status.
