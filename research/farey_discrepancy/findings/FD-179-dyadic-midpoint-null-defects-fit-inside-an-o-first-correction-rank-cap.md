# FD-179 — Dyadic midpoint null defects fit inside an o(first-correction) maximal-rank cap

- **Date:** 2026-09-17
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** restricted temporal acquisition / variable dyadic block repair / exact maximal-rank localization / sparse permanent null source
- **Depends on:** FD-117, FD-170, FD-172, FD-173, FD-175, FD-177, FD-178
- **Classification:** `EXACT-DERIVED + PERMANENT-SOURCE + DYADIC-NULL + MAXIMAL-RANK-CAP + SUBEXPONENTIAL-DELETION + NONMULTIPLICATIVE`

## Claim

`FD-178` left open whether the protected multiplicative-rank window can approach the true maximal rank closely enough that its second-order coefficient tends to `1`. The fixed-`c<1` parametrization is not the correct endpoint coordinate. Measuring the repair shell directly by its **additive distance from the exact maximal rank** removes that artificial fixed gap.

Let

\[
R(x):=\max_{n\le x}\omega(n)
=\max\{r:P_r\le x\},
\tag{1}
\]

where `P_r=p_1\cdots p_r` is the `r`-th primorial, and for sufficiently large `x` set

\[
\boxed{
g(x):=(\log x)^{2/3}(\log\log x)^{-1/3}\log\log\log x.}
\tag{2}
\]

For every finite cutoff `X` there exists one permanent arithmetic source `a\not\equiv\mu` such that

\[
a(n)\in\{0,\mu(n)\}\qquad(n\ge1),
\tag{3}
\]

\[
a(n)=\mu(n)\qquad(n\le X),
\tag{4}
\]

and, for every sufficiently large squarefree `n`,

\[
\boxed{
\omega(n)\le R(n)-2g(n)
\quad\Longrightarrow\quad
a(n)=\mu(n).
}
\tag{5}
\]

Nevertheless the entire dyadic midpoint ladder remains exactly physical:

\[
\boxed{
P_a(2^m)=P_\mu(2^m)
\qquad\text{for every }m\ge1.
}
\tag{6}
\]

If

\[
S:=\{n:\mu(n)\ne0,\ a(n)=0\}
\tag{7}
\]

is the deletion set, the construction can be chosen so that

\[
\boxed{
\log(2+S(x))
=O_X\!\left(
(\log x)^{2/3}(\log\log x)^{2/3}
\right).
}
\tag{8}
\]

Moreover every sufficiently large deletion lies in the top multiplicative-rank cap:

\[
\boxed{
R(n)-\omega(n)=(1+o(1))g(n)
\qquad(n\in S,\ n\to\infty).
}
\tag{9}
\]

Since the first correction in the maximal-rank expansion has size

\[
\frac{\log x}{(\log\log x)^2},
\tag{10}
\]

while

\[
\frac{g(x)}{\log x/(\log\log x)^2}
=
(\log x)^{-1/3}(\log\log x)^{5/3}\log\log\log x
\longrightarrow0,
\tag{11}
\]

(5) protects the full leading term and the full first extremal correction. Exact dyadic midpoint target-rigidity can therefore fail even when every source defect is confined to an additive rank cap that is `o` of the first correction from the leading rank scale to the true maximum.

## 1. Increase the exact block length to the balanced one-third scale

Retain the exact midpoint deletion balance and the finite block lemma used in `FD-177`--`FD-178`. If the old deletion support lies below a dyadic block base `L`, `C_L=0`, and there are `N` old deletions, then for every integer `k>=2` there are `k` pairwise disjoint response intervals

\[
I_s(L,k)\subset(L,2L],
\qquad
|I_s(L,k)|\asymp 2^{-k}L,
\tag{12}
\]

whose integer response vectors form a unimodular basis and in which at most `kN` fresh signed deletions suffice to impose simultaneously

\[
C_{2L}=C_{4L}=\cdots=C_{2^kL}=0.
\tag{13}
\]

Write

\[
y=\log L,
\qquad
\ell=\log y,
\tag{14}
\]

and now choose the larger block length

\[
\boxed{
k(L)=\left\lceil y^{1/3}\ell^{1/3}\right\rceil.}
\tag{15}
\]

The next block base is `L'=2^kL`. If `N(L)` is the accumulated deletion count, the finite lemma gives

\[
N(L')\le(k+1)N(L),
\tag{16}
\]

while

\[
\log L'-\log L=(\log2)k.
\tag{17}
\]

Thus

\[
\frac{\Delta\log N}{\Delta y}
\ll
\frac{\log k}{k}
\ll
y^{-1/3}\ell^{2/3}.
\tag{18}
\]

Summing along the block bases, or comparing with the corresponding integral, yields

\[
\boxed{
\log N(L)
=O\!\left(y^{2/3}\ell^{2/3}\right).
}
\tag{19}
\]

The same estimate propagates between block bases because `k=o(y)`. This is the source-complexity budget that the fresh arithmetic reservoir must beat.

## 2. Remove only coordinates a vanishing cap below the exact maximum

At a large block base `L`, put

\[
m:=R(L),
\tag{20}
\]

so that

\[
P_m\le L<P_{m+1}.
\tag{21}
\]

Choose

\[
\boxed{
s=
\left\lceil
y^{2/3}\ell^{-1/3}\log\ell
\right\rceil,}
\tag{22}
\]

changing `s` by at most one when a prescribed Möbius sign is required, and set

\[
r=m-s.
\tag{23}
\]

The prime number theorem gives

\[
m\sim\frac y\ell,
\qquad
p_m\sim y.
\tag{24}
\]

Since

\[
\frac{s}{m}
\ll
y^{-1/3}\ell^{2/3}\log\ell
\longrightarrow0,
\tag{25}
\]

the primes `p_{m-s+1},\ldots,p_{m+1}` are uniformly `(1+o(1))y`, hence their logarithms are `(1+o(1))\ell`.

Let

\[
Q:=\frac{L}{P_r}.
\tag{26}
\]

From (21),

\[
\prod_{j=r+1}^{m}p_j
\le Q<
\prod_{j=r+1}^{m+1}p_j,
\tag{27}
\]

so (22)--(25) give the exact reservoir scale

\[
\boxed{
\log Q
=(1+o(1))s\ell
=(1+o(1))y^{2/3}\ell^{2/3}\log\ell.
}
\tag{28}
\]

This avoids the fixed second-order coefficient used in `FD-178`: `r` is selected by its exact additive distance from `R(L)`, not by an asymptotic approximation to the endpoint.

## 3. Quantitative PNT fills every shrinking response cell

For each response interval `I_s(L,k)` from (12), dividing by `P_r` gives an interval for the final prime factor `q` at scale `Q` and of relative width comparable with `2^{-k}`. The de la Vallée Poussin estimate already anchored in `SOURCES.md` gives a prime asymptotic in such an interval whenever the main interval width dominates the endpoint error.

Here

\[
k\asymp y^{1/3}\ell^{1/3},
\tag{29}
\]

whereas by (28)

\[
\sqrt{\log Q}
\asymp
y^{1/3}\ell^{1/3}\sqrt{\log\ell}.
\tag{30}
\]

Therefore

\[
\frac{k}{\sqrt{\log Q}}
\longrightarrow0,
\tag{31}
\]

and in particular

\[
2^{-k}\gg \log Q\,e^{-a\sqrt{\log Q}}
\tag{32}
\]

for every fixed sufficiently small positive `a` and all large `L`. Subtracting the quantitative PNT at the two endpoints gives, uniformly over the `k` response cells,

\[
\#\{q\ {\rm prime}:P_rq\in I_s(L,k)\}
\gg
\frac{2^{-k}Q}{\log Q}.
\tag{33}
\]

Its logarithm is

\[
(1+o(1))\log Q
=(1+o(1))y^{2/3}\ell^{2/3}\log\ell,
\tag{34}
\]

which dominates both `\log(kN)` and the source budget (19) by the diverging factor `\log\ell`. Hence every integer coefficient demanded by the exact unimodular repair can be realized by a distinct squarefree integer `P_rq` in the required response cell.

Changing `r` by one changes its parity and supplies either Möbius sign. Equation (28) is unaffected at leading order, and `Q` is much larger than `p_r`, so the selected final primes satisfy `q>p_r`; consequently

\[
\omega(P_rq)=r+1=m-s+1.
\tag{35}
\]

## 4. The defects stay inside the top `g(n)` rank cap

Every fresh correction lies in `(L,2L]`. Since `m=R(L)` and the next two primorials differ from `P_m` by prime factors tending to infinity,

\[
R(L)\le R(n)\le R(L)+1
\qquad(L<n\le2L)
\tag{36}
\]

for all sufficiently large `L`. Combining (22), (35), and (36),

\[
R(n)-\omega(n)
=s+O(1).
\tag{37}
\]

Also `g(n)=(1+o(1))g(L)` uniformly for `L<n\le2L`. Therefore every sufficiently large correction satisfies (9), and in particular

\[
\omega(n)>R(n)-2g(n).
\tag{38}
\]

Starting after an arbitrary cutoff `X`, seed a nontrivial balanced pair in the first response cell using the two adjacent parities for `r`, and then repeat the exact block repair. No deletion ever enters the protected region in (5), while every dyadic horizon belongs to one completed block, proving (6). The count estimate (19) gives (8).

The comparison with `FD-178` is strict. The classical primorial characterization and PNT imply

\[
R(x)
=
\frac{\log x}{\log\log x}
\left[
1+\frac1{\log\log x}
+O\!\left(
\frac{\log\log\log x}{(\log\log x)^2}
\right)
\right].
\tag{39}
\]

`FD-178` protected every fixed fraction `c<1` of the displayed first correction. Equations (5) and (11) instead leave unprotected only an additive cap negligible compared with that entire first correction, so the effective second-order coefficient now tends to `1`.

## 5. Stress tests and boundary

The theorem does not weaken the observation family: all dyadic midpoint samples are still matched exactly by one permanent source. It also does not enlarge the coefficient alphabet: the source remains deletion-only, with physical Möbius signs on every nonzero coefficient and no added nonsquarefree support.

The gain comes from changing the endpoint coordinate and rebalancing the block length. The previous choice `k\asymp(y/\ell)^{1/3}` was tuned for a reservoir with `\log Q\asymp y/\ell`. Near the true maximum, removing `s` prime factors leaves `\log Q\asymp s\ell`. Choosing `k\asymp y^{1/3}\ell^{1/3}` makes the accumulated repair entropy `O(y^{2/3}\ell^{2/3})`; taking `s\ell` larger by the slowly diverging factor `\log\ell` simultaneously dominates that entropy and places the cell width safely above the de la Vallée Poussin error scale.

No optimality of the exponent `2/3` or of the factor `\log\log\log x` is claimed. They are the balance delivered by this exact block-repair plus classical zero-free-region prime-reservoir mechanism. A stronger prime-distribution input or a lower-entropy response realization could shrink the cap further. Conversely, this pass does not reach literal full coordinatewise fidelity: a thin family of composites at ranks within `O(g(n))` of `R(n)` is still allowed to violate the product law.

Most importantly, this remains a source-identifiability obstruction, not a Franel--Landau estimate. It shows that even almost-maximal coordinatewise multiplicative-rank fidelity cannot substitute for a cross-coordinate law. It does not prove RH, improve the RH-critical discrepancy exponent, or contradict the exact multiplicative rigidity of `FD-172`--`FD-174`.

## Representation audit

The representation is unchanged from `FD-170`, `FD-175`, `FD-177`, and `FD-178`: the exact midpoint sensor is kept in the odd-multiple weight form, and the same dyadic unimodular response basis is used. The exact maximal-rank function `R(x)` is only a source-coordinate bookkeeping device; it does not change the observable, norm, noise model, or destination.

The generic mechanism is a rounded-dilation block system whose correction entropy can be traded against a reservoir scale. The Farey/Möbius-specific splice is the exact binary midpoint cocycle and the realization of either signed correction by squarefree `P_rq` coordinates. The information deliberately discarded is global cross-coordinate multiplicativity, now only on a subexponential family lying in an `o(first-correction)` cap at the extreme edge of the squarefree rank simplex.

## Prior-art audit

A targeted literature search was run for Farey midpoint reconstruction on lacunary/dyadic horizons, sparse Möbius null sources, primorial maximal order of `omega`, and prime population of shrinking relative intervals. It found the classical Farey/Möbius identities and standard prime-distribution/maximal-rank ingredients, but no direct analogue of the permanent deletion-only block repair or this maximal-rank-cap localization.

The identity `R(x)=max{r:P_r<=x}` is elementary, and `m~log x/loglog x`, `p_m~log x`, together with the shrinking-interval estimate used above, are direct consequences of the prime number theorem and the de la Vallée Poussin error already anchored in `SOURCES.md`. No new external theorem is load-bearing. The contribution claimed here is only their splice with the exact dyadic midpoint response system and the resulting source-identifiability boundary; `SOURCES.md` therefore needs no update.
