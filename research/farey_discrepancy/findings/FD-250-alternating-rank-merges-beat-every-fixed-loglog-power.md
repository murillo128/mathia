# FD-250 — Alternating rank merges beat every fixed power of log log N

- **Date:** 2026-09-21
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** divisor-response sampling / exact omissions / weighted incidence inversion / rank-selected Boolean lattices / descent classes / conditioning lower bound
- **Depends on:** FD-225, FD-245, FD-248, FD-249
- **Classification:** `EXACT-DERIVED + NESTED-RANK-MERGE-LOWER-BOUND + EXACT-OMISSION-REALIZATION + SUBPOLYNOMIAL-DEFECT`

## Claim

FD-249 shows that one high-arity merge already makes the weighted incidence inverse norm

\[
\kappa(D)
=
\max_{d\in D}
\sum_{\substack{q\in D\\q\mid d}}
|\mu_D(q,d)|\frac qd
\]

unbounded, with a single-star lower bound of order

\[
\frac{\log\log N}{\sqrt{\log\log\log N}}.
\]

Nested rank-selected merges can do much more. There is an infinite sequence of horizons `N` and exact omission responses

\[
Y(m)=(\mathscr A b)(m),\qquad 1\le m\le N,
\]

with

\[
|b_n|\le n,
\qquad
K=N^{o(1)},
\]

such that, for

\[
D_N=\operatorname{supp}(\Delta Y)\cap[1,N],
\]

one has

\[
\boxed{
\log \kappa(D_N)
\ge
(1-o(1))
(\log\log\log N)
(\log\log\log\log N).
}
\tag{1}
\]

Equivalently,

\[
\boxed{
\kappa(D_N)
\ge
(\log\log N)^{(1-o(1))\log\log\log\log N}.
}
\tag{2}
\]

Consequently, for every fixed `A>0`,

\[
\boxed{
\frac{\kappa(D_N)}{(\log\log N)^A}\to\infty
}
\tag{3}
\]

along this family.

Thus the single-star scale from FD-249 is not close to the largest conditioning permitted by exact adjacent-pair omissions. Alternating rank selections inside one squarefree divisor lattice create Möbius coefficients of factorial size on a rank that still carries substantial reciprocal divisor mass.

This remains a response-side signed statement. It does not show that `kappa(D_N)` reaches the much larger `N/K` scale required by FD-248 for sublinear omissions to hide macroscopic coefficient mass, and it does not impose positivity, finite prime-reservoir capacity, squarefree physical-source realization, or full Möbius coherence.

## Choose a reciprocal-heavy squarefree rank

As in FD-249, let

\[
R_y:=\prod_{p\le y}p
\tag{4}
\]

and define

\[
S_k(y)
:=
\sum_{\substack{r\mid R_y\\\omega(r)=k}}
\frac1r.
\tag{5}
\]

The total reciprocal divisor mass is

\[
T_y
=
\sum_{r\mid R_y}\frac1r
=
\prod_{p\le y}\left(1+\frac1p\right)
\asymp \log y.
\tag{6}
\]

Under the probability measure proportional to `1/r` on divisors of `R_y`, the indicators `1_(p|r)` are independent with probability `1/(p+1)`. Hence, for `W=omega(r)`,

\[
\lambda_y:=\mathbb E W
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
\log\log y+O(1).
\tag{8}
\]

Chebyshev therefore places a fixed positive proportion of the reciprocal mass in `O(sqrt(lambda_y))` consecutive ranks around `lambda_y`. For at least one integer

\[
k=k(y)=\lambda_y+O(\sqrt{\lambda_y})
\tag{9}
\]

we have

\[
\boxed{
S_k(y)
\gg
\frac{\log y}{\sqrt{\lambda_y}}.
}
\tag{10}
\]

For large `y`, this `k` tends to infinity and satisfies `k<pi(y)`.

## Alternating rank selection has factorial Möbius coefficient

Fix such a `k` and put

\[
A_k:=\{1,3,5,\ldots\}\cap\{1,\ldots,k-1\}.
\tag{11}
\]

Consider the induced subposet of the Boolean lattice on a `k`-element set consisting only of the bottom element, the top element, and the ranks in `A_k`. We derive its top Möbius coefficient directly.

For `T={t_1<\cdots<t_j}\subseteq A_k`, the number of chains whose intermediate ranks are exactly `T` is

\[
\alpha_k(T)
=
\frac{k!}
{t_1!(t_2-t_1)!\cdots(k-t_j)!}.
\tag{12}
\]

The chain expansion of the Möbius function gives

\[
\mu_k(A_k)
=
\sum_{T\subseteq A_k}
(-1)^{|T|+1}\alpha_k(T).
\tag{13}
\]

The same multinomial `alpha_k(T)` counts permutations of `[k]` whose descent set is contained in `T`: positions outside `T` must be ascents, so the permutation is increasing inside the consecutive blocks cut at `T`, and choosing the value sets of those blocks gives (12). Inclusion-exclusion therefore shows that the number

\[
\beta_k(A_k)
:=
\#\{\pi\in S_k:\operatorname{Des}(\pi)=A_k\}
\tag{14}
\]

satisfies

\[
\beta_k(A_k)
=
\sum_{T\subseteq A_k}
(-1)^{|A_k|-|T|}\alpha_k(T).
\tag{15}
\]

Comparing (13) and (15),

\[
\boxed{
|\mu_k(A_k)|=\beta_k(A_k).
}
\tag{16}
\]

For the alternating set (11), these are exactly the permutations

\[
\pi_1>\pi_2<\pi_3>\pi_4<\cdots.
\]

A completely elementary subfamily already gives the required factorial lower bound. Put the largest `ceil(k/2)` values in the odd positions and the smallest `floor(k/2)` values in the even positions. Every independent ordering within the two position classes is alternating, so

\[
\boxed{
|\mu_k(A_k)|
\ge
\left\lceil\frac k2\right\rceil!
\left\lfloor\frac k2\right\rfloor!.
}
\tag{17}
\]

Thus no asymptotic formula for Euler zigzag numbers is needed.

## Embed the alternating rank lattice in an exact omission support

Set

\[
L_y:=R_y+1,
\qquad
N_y:=L_yR_y.
\tag{18}
\]

Let the selected complement ranks be

\[
J_k:=A_k\cup\{k\},
\tag{19}
\]

and define

\[
Q_y
:=
\left\{
q_r:=\frac{N_y}{r}:
 r\mid R_y,\ \omega(r)\in J_k
\right\}.
\tag{20}
\]

Every selected `r` is nontrivial and proper for large `y`, so, writing `t=R_y/r`,

\[
2\le t\le\frac{R_y}{2},
\qquad
q_r=L_yt,
\qquad
2L_y\le q_r\le\frac{N_y}{2}.
\tag{21}
\]

Distinct points of `Q_y` are distinct multiples of `L_y`, hence differ by at least `L_y`. Define the response on `[0,N_y]` by

\[
Y(0)=0,
\qquad
Y(m)=
\begin{cases}
1,&m\in Q_y\cup\{N_y\},\\
0,&\text{otherwise}.
\end{cases}
\tag{22}
\]

The omission set is therefore

\[
E_y=Q_y\cup\{N_y\}.
\tag{23}
\]

Because the omitted points in `Q_y` are separated by more than one,

\[
g:=\Delta Y
\]

has value `+1` on `Q_y` and at `N_y`, value `-1` on `Q_y+1`, and zero elsewhere up to the horizon. Put

\[
b=\mathbf1*g.
\tag{24}
\]

Then `mu*b=g`, and the exact divisor-response identity from FD-225 gives

\[
(\mathscr A b)(m)
=
\sum_{d\le m}g(d)
=Y(m).
\tag{25}
\]

Moreover

\[
|b_n|
\le
\sum_{d\mid n}|g(d)|
\le
\tau(n)
\le n,
\tag{26}
\]

so the linear coefficient envelope holds with `C=1`.

## The adjacent companions are isolated from the designed divisor lattice

The exact-omission constraint adds the points `q_r+1` to `supp(g)`. They do not contaminate the rank-selected divisibility component.

Write

\[
c_r=q_r+1=L_yt+1.
\]

Then `gcd(c_r,L_y)=1` and `c_r>R_y`. If `c_r` divided `N_y=L_yR_y`, it would divide `R_y`, impossible. If `c_r` divided another selected point `q_s=L_yt_s`, coprimality with `L_y` would force `c_r|t_s`, again impossible because `c_r>R_y>=t_s`. Conversely no `q_s` can divide `c_r`, since `q_s` is divisible by `L_y` while `c_r` is `1 mod L_y`.

Finally, two distinct companions cannot divide one another. If

\[
c_s=a c_r,
\]

then reduction modulo `L_y` gives `a=1 mod L_y`. But by (21) the ratio of any two companions is strictly smaller than `L_y` for all sufficiently large `y`, so no integer `a>1` is possible.

Thus the companion points are isolated vertices of the induced divisibility poset on

\[
D_y=\operatorname{supp}(g)\cap[1,N_y].
\tag{27}
\]

All nontrivial conditioning in the component below `N_y` is exactly the rank-selected squarefree geometry prescribed by (19)--(20).

## The top inverse row contains a factorially amplified reciprocal rank

Fix `r|R_y` with `omega(r)=k`. The active interval from `q_r=N_y/r` up to `N_y` is, after reversing complements, the Boolean lattice on the `k` prime factors of `r` with only ranks `A_k` retained between its endpoints. Hence (16)--(17) give

\[
|\mu_{D_y}(q_r,N_y)|
\ge
\left\lceil\frac k2\right\rceil!
\left\lfloor\frac k2\right\rfloor!.
\tag{28}
\]

Since

\[
\frac{q_r}{N_y}=\frac1r,
\]

the `N_y` row of the weighted inverse satisfies

\[
\begin{aligned}
\kappa(D_y)
&\ge
\sum_{\substack{r\mid R_y\\\omega(r)=k}}
|\mu_{D_y}(q_r,N_y)|\frac1r\\
&\ge
\left\lceil\frac k2\right\rceil!
\left\lfloor\frac k2\right\rfloor!
S_k(y).
\end{aligned}
\tag{29}
\]

Combining (10) and (29),

\[
\boxed{
\kappa(D_y)
\gg
\frac{\log y}{\sqrt{\lambda_y}}
\left\lceil\frac k2\right\rceil!
\left\lfloor\frac k2\right\rfloor!.
}
\tag{30}
\]

By Stirling and (9),

\[
\log\!\left(
\left\lceil\frac k2\right\rceil!
\left\lfloor\frac k2\right\rfloor!
\right)
=
k\log k-O(k)
=
(1-o(1))\lambda_y\log\lambda_y.
\tag{31}
\]

The logarithm of the prefactor in (30) is lower order. Since

\[
\log N_y\sim2y,
\]

we have

\[
\log\log N_y=\log y+O(1),
\]

\[
\lambda_y
=
\log\log y+O(1)
=
\log\log\log N_y+O(1),
\tag{32}
\]

and

\[
\log\lambda_y
=
\log\log\log\log N_y+o(1).
\tag{33}
\]

Equations (30)--(33) prove (1)--(3).

## The omission count remains subpolynomial

The number of omitted response points is

\[
K_y
=
1+
\sum_{j\in J_k}
\binom{\pi(y)}j.
\tag{34}
\]

Because `k=O(log log y)` while `pi(y)` is much larger, the elementary binomial bound gives

\[
K_y
\le
1+(k+1)
\left(\frac{e\pi(y)}k\right)^k.
\tag{35}
\]

Therefore

\[
\log K_y
=O((\log\log y)(\log y))
=o(y)
=o(\log N_y),
\tag{36}
\]

and hence

\[
\boxed{K_y=N_y^{o(1)}.}
\tag{37}
\]

So the stronger conditioning is not obtained by making the omitted response set dense.

## Finite audit example

Take `y=7`, so

\[
R_y=210,
\qquad
L_y=211,
\qquad
N_y=44310.
\]

For the structural finite check choose `k=4` and `A_4={1,3}`. The selected complement ranks are `1,3,4`. On the rank-four interval the chain/inclusion-exclusion calculation gives

\[
\mu=-5,
\]

matching the five alternating permutations of four letters. The point for the full complement is

\[
q_{210}=44310/210=211,
\]

so its contribution to the top weighted row is `5/210` rather than `1/210`.

The complete designed top row is

\[
1
+
\sum_{\omega(r)=1}\frac1r
+
2\sum_{\omega(r)=3}\frac1r
+
5\sum_{\omega(r)=4}\frac1r
=
\frac{248}{105}.
\tag{38}
\]

A direct finite incidence inversion gives the same value. The companion points are isolated exactly as proved above. This example is only a consistency audit; the asymptotic gain comes from choosing the reciprocal-heavy rank (9) with `k` tending to infinity.

## Prior-art / novelty audit

Rank-selected Boolean lattices, their Möbius invariants, and the identification of those invariants with fixed descent-set counts are classical. It is also classical that alternating rank selections maximize the absolute rank-selected Möbius invariant of the Boolean lattice; the literature traces the corresponding maximum descent-class result to Niven and de Bruijn, with later poset formulations in the rank-selection literature. Those facts delimit the combinatorial prior art.

They are not load-bearing external inputs here: equations (12)--(17) derive directly the exact identity needed for the construction and use only the elementary two-block subfamily for the factorial lower bound. A targeted prior-art search did not reveal the specific embedding (18)--(29) into an exact adjacent-pair omission support for the divisor-response inverse, nor the iterated-log lower bound (1). No novelty is claimed for alternating permutations, descent classes, Boolean-lattice Möbius inversion, or their extremal rank selection.

No new durable literature dependency is therefore required in `SOURCES.md`; the only analytic asymptotics used above are the same PNT/Mertens consequences already anchored for FD-249.

## Boundary and next audit

FD-249 ruled out a uniform `O(1)` conditioning bound from shallow merge geometry. The present construction shows considerably more: even within one primorial divisor lattice, nested alternating rank merges make `kappa(D)` grow faster than every fixed power of `log log N`. Therefore any future upper bound based only on exact adjacent-pair support must allow genuinely large rank-selected Möbius amplification.

The result still leaves a large quantitative gap. The certified lower bound in (1) is `N^{o(1)}`, whereas FD-248 requires `kappa(D) >> N/K` for a sublinear omission family to support macroscopic coefficient mass. The next useful response-side question is whether exact omission geometry can push `kappa(D)` to a fixed power of `log N`, to `N^{o(1)}` on a substantially larger scale, or even toward `N/K`; alternatively, one should seek an upper bound that keeps it uniformly below that macroscopic threshold.

The source-side frontier is unchanged: positivity, finite reservoir capacities, squarefree physical realization and arithmetic coherence may exclude these signed incidence directions even when the response-side inverse is badly conditioned.

## Status

**Proved.** The rank-selected Möbius identity, alternating-permutation lower bound, companion isolation, exact response realization and subpolynomial omission count are finite/exact. The only asymptotic inputs are the reciprocal-rank concentration and standard PNT/Mertens consequences already used in FD-249 to translate the construction into horizon scale.