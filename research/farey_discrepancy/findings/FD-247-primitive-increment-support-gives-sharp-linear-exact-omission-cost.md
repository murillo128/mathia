# FD-247 — Primitive increment support gives sharp linear exact-omission cost

- **Date:** 2026-09-21
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** divisor-response sampling / exact omissions / divisibility antichains / growing defect / quantitative inverse
- **Depends on:** FD-225, FD-244, FD-245, FD-246
- **Classification:** `EXACT-DERIVED + PRIMITIVE-INCREMENT-SUPPORT + SINGLE-OCTAVE-OMISSION-BOUND + SHARP-LINEAR-DEFECT`

## Claim

FD-245 shows that exact missing response values generate adjacent divisor-difference columns, while FD-246 shows that their absolute locations control the reachable coefficient support. There is a stronger regime in which neither the exponential triangular bound nor the reciprocal-divisor sparse loss is needed: **if the actual response increments form a divisibility antichain, divisor inversion is diagonal on those active coordinates.**

Let

\[
Y(m)=(\mathscr A b)(m),\qquad Y(0)=0,
\]

with

\[
|b_n|\le Cn\qquad(n\ge1).
\tag{1}
\]

Fix `N>=1`, and suppose

\[
Y(m)=0\qquad(1\le m\le N,\ m\notin E_N)
\tag{2}
\]

for an omission set `E_N subseteq {1,...,N}` of cardinality `K`. Define

\[
g=\mu*b,
\qquad
D_N:=\{d\le N:g(d)\ne0\}.
\tag{3}
\]

By the exact inversion of FD-225,

\[
b=\mathbf1*g,
\qquad
g(d)=Y(d)-Y(d-1).
\tag{4}
\]

Assume that `D_N` is a divisibility antichain: for distinct `d,e in D_N`, neither divides the other. Then

\[
\boxed{
\sum_{n\le N}|b_n|
\le C N\,|D_N|
\le 2 C N K.
}
\tag{5}
\]

Consequently,

\[
\boxed{
\frac{\sum_{N/2<n\le N}|b_n|}
     {\sum_{N/2<n\le N}n}
\ll C\frac KN.
}
\tag{6}
\]

A particularly useful sufficient condition is purely geometric. If, for some integer `M>=1`,

\[
E_N\subseteq(M,2M],
\tag{7}
\]

then `D_N` is automatically a divisibility antichain, and therefore (5)--(6) hold **independently of the absolute scale `M`**. Thus any `K=o(N)` exact omissions confined to one multiplicative octave remain signed-coercive at macroscopic coefficient scale, even if that octave lies far below the top of `[1,N]`.

The `K/N` normalized scale is sharp up to constants for this class: the top-half construction of FD-246 is a single-octave example with `|b_n|<=n` and

\[
\sum_{N/2<n\le N}|b_n|\gg NK.
\tag{8}
\]

Hence a genuinely bad growing exact-omission family cannot be produced merely by moving a sublinear number of omissions to a lower absolute scale. To recover larger amplification, the active increments must develop **cross-scale divisibility incidences**.

## Exact inversion is diagonal on primitive increment support

From (4), for every `n<=N`,

\[
b_n=\sum_{d\mid n}g(d)
    =\sum_{\substack{d\mid n\\d\in D_N}}g(d).
\tag{9}
\]

Now take `d in D_N`. Evaluating (9) at `n=d` gives

\[
b_d=\sum_{\substack{q\mid d\\q\in D_N}}g(q).
\tag{10}
\]

Because `D_N` is a divisibility antichain, the only active divisor `q in D_N` of `d` is `q=d`. Therefore

\[
\boxed{b_d=g(d)\qquad(d\in D_N).}
\tag{11}
\]

The coefficient envelope (1) now controls each active increment without any triangular recursion:

\[
|g(d)|=|b_d|\le Cd.
\tag{12}
\]

Summing (9) in absolute value and exchanging the finite sums,

\[
\begin{aligned}
\sum_{n\le N}|b_n|
&\le
\sum_{d\in D_N}|g(d)|
\left\lfloor\frac Nd\right\rfloor\\
&\le
\sum_{d\in D_N}Cd\,\frac Nd\\
&=CN|D_N|.
\end{aligned}
\tag{13}
\]

This proves the first inequality in (5). It is stronger than estimating the omitted response amplitudes `Y(m)` themselves: those amplitudes may interact, but once their discrete derivative has primitive support, the divisor zeta transform has no off-diagonal active-to-active coupling.

## Exact omissions create at most two active increments each

Equation (2) implies that the nonzero response values in `[1,N]` are contained in `E_N`. Since

\[
g(d)=Y(d)-Y(d-1),
\]

a nonzero `g(d)` with `d<=N` requires either `Y(d)\ne0` or `Y(d-1)\ne0`. Hence

\[
\boxed{
D_N\subseteq E_N\cup\bigl((E_N+1)\cap[1,N]\bigr),
}
\tag{14}
\]

and therefore

\[
|D_N|\le2K.
\tag{15}
\]

Combining (13) and (15) proves the second inequality in (5). Since

\[
\sum_{N/2<n\le N}n\asymp N^2,
\tag{16}
\]

(6) follows immediately.

Notice that (14) does not require every declared omission to have nonzero response. Zero-valued omitted points simply fail to contribute to `D_N`, so the bound is valid for the same omission convention used in FD-245 and FD-246.

## One multiplicative octave is automatically primitive

Assume (7) with integer `M>=1`. From (14),

\[
D_N\subseteq(M,2M+1].
\tag{17}
\]

Take distinct `d<e` in this interval. Because the variables are integers,

\[
d\ge M+1,
\]

so

\[
2d\ge2M+2>2M+1\ge e.
\tag{18}
\]

If `d` divided `e`, then `e>=2d`, contradicting (18). Thus no two distinct elements of `D_N` divide one another, proving the single-octave corollary.

This removes the location penalty in FD-246 for a large and natural class of low-scale omission sets. FD-246 alone gives schematically

\[
\sum_{n\le N}|b_n|
\ll C N^2\sum_{m\in E_N}\frac1m,
\tag{19}
\]

which for `K` omissions near scale `M` is `O(CN^2K/M)`. Under the one-octave hypothesis, the exact divisibility geometry improves this to

\[
\boxed{
\sum_{n\le N}|b_n|\le2CNK,
}
\tag{20}
\]

with no dependence on `M`. The gain can therefore be arbitrarily large when `M=o(N)`.

Likewise, the location-free FD-244 estimate pays a slowly varying reciprocal-divisor factor for a general sparse defect. Equation (20) shows that this factor is absent whenever the active increment set has no internal divisibility relations.

## Sharpness inside the single-octave class

Take the top-half construction from FD-246: for even `N` and `1<=K<=N/8`, choose

\[
m_j=\frac N2+2j,
\qquad 1\le j\le K,
\]

set `E_N={m_1,...,m_K}`, put `Y(m_j)=m_j`, and set every other response value in `[1,N]` to zero. Then

\[
b_{m_j}=m_j,
\qquad
b_{m_j+1}=-m_j,
\]

and all other coefficients in `[1,N]` vanish. Hence `|b_n|<=n` and

\[
\sum_{N/2<n\le N}|b_n|
=2\sum_{j=1}^K m_j
\ge NK.
\tag{21}
\]

Here `E_N subset (N/2,N]`, so it is exactly a one-octave omission set with `M=N/2`. Together with (20), this proves that the linear `NK` dependence is order-sharp for the single-octave class.

## What this changes in the growing-defect frontier

FD-246 identified low response scales as the only locations where one omitted sample can have a large divisor footprint. The present theorem shows that **large footprint is not by itself enough**. If all active increments remain in one octave, their divisor relation is an antichain and the inverse has linear defect cost regardless of how many multiples each increment has below `N`.

Thus the remaining exact-omission problem is more structural than a location profile alone suggests. Any family that approaches the worse location-free behavior must create divisibility chains or a denser divisibility incidence pattern across several multiplicative scales. Equivalently, the next quantitative object is not just the number or harmonic mass of omitted locations, but the conditioning generated by the divisibility poset on the actual support of `g=\Delta Y`.

This distinction also keeps the response-side and source-side frontiers separate. The theorem concerns exact-zero sampling of the relaxed signed divisor response. It does not address the linear weighted-residual threshold of FD-242, nor positivity, finite prime-reservoir capacity, squarefree source realization, or arithmetic coherence of the physical Mertens source.

## Prior-art / novelty audit

Divisibility antichains are the classical **primitive sets** of multiplicative number theory, and Möbius/divisor-zeta inversion on the divisibility poset is standard. The primitive-set literature studies density and weighted extremal questions; the Möbius-pair uncertainty literature studies global restrictions on supports of divisor-transform pairs. A targeted search of those formulations did not reveal the finite-horizon estimate (5), the exact-omission corollary (20), or the observation that one multiplicative octave removes the sparse reciprocal-divisor penalty in this response problem.

No external theorem is load-bearing. The proof uses only the exact inverse relation already established in FD-225/FD-245, the coefficient envelope, and the elementary fact that an interval `(M,2M+1]` of integers is a divisibility antichain. Accordingly no new literature dependency is required in `SOURCES.md`, and no novelty claim is made for primitive sets or incidence-algebra inversion themselves.

## Status

**Proved.** The primitive-support estimate (5), the single-octave corollary (20), and the `NK` sharpness scale follow by exact finite divisor algebra. The result materially narrows the growing exact-omission frontier but remains a signed response-side theorem rather than a new Farey bound or an RH implication.