# FD-246 — Harmonic omission location gives sharp linear high-scale cost

- **Date:** 2026-09-21
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** divisor-response sampling / exact omissions / support geometry / growing defect / quantitative inverse
- **Depends on:** FD-225, FD-241, FD-244, FD-245
- **Classification:** `EXACT-DERIVED + LOCATION-SENSITIVE-OMISSION-BOUND + GROWING-HIGH-SCALE-COERCIVITY + SHARP-TOP-HALF`

## Claim

FD-245 controls a finite set of exact response omissions by solving for the omitted amplitudes through a triangular system, giving a coefficient-mass bound of order `CN 2^K`. That is uniform in the omission locations but loses usefulness when `K` grows. The same exact column representation has a second consequence that does not require controlling the omitted amplitudes at all: **the locations of the omissions control where the coefficient sequence can be supported**.

Let

\[
Y(m)=(\mathscr A b)(m),\qquad Y(0)=0,
\]

and assume

\[
|b_n|\le Cn\qquad(n\ge1).
\tag{1}
\]

Fix `N>=1`, and suppose

\[
Y(m)=0\qquad(1\le m\le N,\ m\notin E_N)
\tag{2}
\]

for some omission set `E_N subseteq {1,...,N}`. Define its finite-horizon divisor footprint

\[
\Lambda_N(E_N)
:=
\sum_{m\in E_N}
\left(
\left\lfloor\frac Nm\right\rfloor
+
\left\lfloor\frac N{m+1}\right\rfloor
\right).
\tag{3}
\]

Then

\[
\boxed{
|\operatorname{supp}(b)\cap[1,N]|
\le \Lambda_N(E_N),
}
\tag{4}
\]

and consequently

\[
\boxed{
\sum_{n\le N}|b_n|
\le C N\,\Lambda_N(E_N)
\le
2C N^2\sum_{m\in E_N}\frac1m.
}
\tag{5}
\]

Thus exact omission geometry has a location-sensitive control independent of the `2^K` triangular conditioning in FD-245. In particular, if every omission lies at scale at least `alpha N`, with fixed `0<alpha<=1`, and `K=|E_N|`, then

\[
\boxed{
\sum_{n\le N}|b_n|
\le \frac{2C}{\alpha}NK,
}
\tag{6}
\]

so

\[
\boxed{
\frac{\sum_{N/2<n\le N}|b_n|}
{\sum_{N/2<n\le N}n}
\ll_\alpha C\frac KN.
}
\tag{7}
\]

Hence **any sublinear number of exact omissions confined to a fixed high-scale annulus remains signed-coercive**, even when `K=K(N)->infinity`. No `log log(N/K)` loss and no exponential dependence on `K` survives in this regime.

For omissions in the top half, `E_N subset (N/2,N]`, the scale `K/N` is sharp up to absolute constants. There are exact-zero sampling examples with `|b_n|<=n` and `K` top-half omissions for which

\[
\sum_{N/2<n\le N}|b_n|\gg NK.
\tag{8}
\]

Thus the growing-defect frontier is not controlled by `K` alone. The omitted locations matter through their divisor footprints; low-scale omissions are the only ones capable of generating many coefficient locations from a small number of missing response values.

## Exact response columns imply an exact support inclusion

FD-225 gives the inverse relation

\[
g=\mu*b,\qquad b=\mathbf1*g,
\qquad g(m)=Y(m)-Y(m-1).
\tag{9}
\]

As recorded in FD-245, under (2) this yields, for every `n<=N`,

\[
\boxed{
b_n
=\sum_{m\in E_N}Y(m)
\left(\mathbf1_{m\mid n}-\mathbf1_{m+1\mid n}\right).}
\tag{10}
\]

Equation (10) immediately implies

\[
\operatorname{supp}(b)\cap[1,N]
\subseteq
\bigcup_{m\in E_N}
\left(
\{n\le N:m\mid n\}
\cup
\{n\le N:m+1\mid n\}
\right).
\tag{11}
\]

Counting the sets in this union without even using overlaps gives (4). The coefficient envelope (1) then gives

\[
\sum_{n\le N}|b_n|
\le CN\,|\operatorname{supp}(b)\cap[1,N]|,
\tag{12}
\]

which proves the first inequality in (5). For the second,

\[
\left\lfloor\frac Nm\right\rfloor
+
\left\lfloor\frac N{m+1}\right\rfloor
\le \frac{2N}{m},
\tag{13}
\]

so summing (13) over `E_N` proves the harmonic-location bound.

This route is complementary to FD-245. There the exact columns are evaluated at the omitted response locations in order to control the amplitudes `Y(m)`. Here the amplitudes can be arbitrarily ill-conditioned: they cannot create a nonzero `b_n` outside the union of the divisor footprints in (11).

## Fixed high-scale annuli have linear growing-defect cost

Suppose

\[
E_N\subseteq[\alpha N,N].
\tag{14}
\]

Then

\[
\sum_{m\in E_N}\frac1m
\le \frac{K}{\alpha N},
\tag{15}
\]

and (6) follows from (5). Since

\[
\sum_{N/2<n\le N}n\asymp N^2,
\tag{16}
\]

we obtain (7). Therefore for every sequence `K(N)=o(N)`, exact-zero sampling remains macroscopically coercive if all omitted points stay in any fixed annulus `[alpha N,N]`.

More generally, decompose the omissions into dyadic location bands

\[
E_r
:=E_N\cap(N/2^{r+1},N/2^r],
\qquad K_r:=|E_r|.
\tag{17}
\]

Then

\[
\sum_{m\in E_N}\frac1m
\le
\frac1N
\sum_{r\ge0}2^{r+1}K_r,
\tag{18}
\]

and hence

\[
\boxed{
\frac{\sum_{N/2<n\le N}|b_n|}
{\sum_{N/2<n\le N}n}
\ll
\frac C N
\sum_{r\ge0}2^rK_r.
}
\tag{19}
\]

This is the natural location profile exposed by the exact column geometry: one omission at scale `N/2^r` can affect only `O(2^r)` multiples below `N`. Treating all missing points only through their cardinality discards precisely this information.

## The top-half `K/N` scale is sharp

Take an even `N` and an integer

\[
1\le K\le \left\lfloor\frac N8\right\rfloor.
\tag{20}
\]

Choose separated omission locations

\[
m_j=\frac N2+2j,
\qquad 1\le j\le K,
\tag{21}
\]

and set

\[
E_N=\{m_1,\ldots,m_K\},
\qquad
Y(m_j)=m_j,
\qquad
Y(m)=0\quad(m\notin E_N).
\tag{22}
\]

Every `m_j` and `m_j+1` lies in `(N/2,N]`, so each has exactly one positive multiple not exceeding `N`, namely itself. The pairs `{m_j,m_j+1}` are disjoint. Equation (10) therefore reduces on `[1,N]` to

\[
b_{m_j}=m_j,
\qquad
b_{m_j+1}=-m_j,
\tag{23}
\]

with every other coefficient zero. The linear envelope holds because

\[
|b_{m_j}|=m_j,
\qquad
|b_{m_j+1}|=m_j<m_j+1.
\tag{24}
\]

Moreover the response is exactly zero at every sampled point outside the `K` omitted locations by construction and exact inversion. All nonzero coefficients lie in the top octave, and

\[
\sum_{N/2<n\le N}|b_n|
=2\sum_{j=1}^K m_j
\ge NK.
\tag{25}
\]

Together with (7), this proves that the normalized `K/N` cost is order-sharp for top-half omissions.

## Relation to the FD-244--FD-245 bounds

There are now three genuinely different controls on exact omissions. FD-244 forgets exact response-column geometry and gives the location-free sparse reciprocal-divisor bound, useful for general growing `K`. FD-245 retains exact columns and controls their amplitudes by a triangular inverse, removing the double logarithm for bounded `K` but paying `2^K`. The present result retains exact columns in a different way and controls only their **reachable coefficient support**, paying their harmonic location footprint instead of an amplitude condition number.

Consequently, for exact observed zeros one may use whichever of the three mechanisms is strongest. Up to absolute constants and the regularization already fixed in FD-244, the top-octave mass has the combined schematic bound

\[
\sum_{N/2<n\le N}|b_n|
\ll
CN\min\left\{
2^K,
K\log\!\left(e+\log\frac NK\right),
N\sum_{m\in E_N}\frac1m
\right\}.
\tag{26}
\]

The third term is new and dominates both earlier relaxations for sublinear high-scale omission sets. It does not improve the worst location-free problem when many omissions occur near the bottom of `[1,N]`; there the divisor footprint can be large and FD-244 can still be the better estimate.

Thus the remaining growing-defect question should not ask only for a function of `K`. One must understand how low the omitted locations can sit, how their divisor footprints overlap, and whether the exact adjacent pairing in (10) forces further cancellation or conditioning gains in those low-scale configurations.

## Prior-art / novelty audit

The nearest classical framework is Möbius inversion on the divisibility poset. Pollack--Sanna's uncertainty principle for Möbius pairs and later poset generalizations such as Goh's concern qualitative/global restrictions on simultaneous supports. A targeted search did not reveal a theorem matching the finite-horizon adjacent-column support estimate (4)--(5) or its high-scale sampling consequence (7).

No external theorem is load-bearing here. The proof is the exact divisor-response column identity already established in FD-225/FD-245, followed by support inclusion, counting multiples, and the coefficient envelope. Accordingly no new literature dependency is required in `SOURCES.md`, and no general priority claim is made for the underlying incidence-algebra observation. The line-specific content is the quantitative location-sensitive sampling bound and the sharp high-scale growing-defect regime it exposes.

## Boundaries and consequences

The theorem is for the relaxed signed divisor-response inverse under `|b_n|<=Cn`. It does not impose positivity, prime-reservoir capacity, squarefree source realizability, or any physical Mertens coherence, and it does not imply RH. It also does not improve the approximate-response residual term `V_S(N)/N` from FD-242.

What it does settle is a nontrivial part of the live FD-245 frontier: **growing exact omissions are harmless at macroscopic coefficient scale whenever their harmonic location mass tends to zero**. In particular, `K=o(N)` omissions in any fixed high-scale annulus have normalized coefficient mass `o(1)`, and the resulting `K/N` scale is best possible in the top-half regime. Any genuinely bad growing exact-omission family must therefore place enough defect mass at lower response scales, or exploit further arithmetic interaction among those lower-scale columns.

## Status

**Proved.** Equations (4)--(7), the dyadic location profile (19), and the top-half sharpness construction (20)--(25) are exact finite-horizon consequences of the established divisor inversion. The result advances the exact sampling inverse problem but remains a response-side statement rather than a physical source theorem.