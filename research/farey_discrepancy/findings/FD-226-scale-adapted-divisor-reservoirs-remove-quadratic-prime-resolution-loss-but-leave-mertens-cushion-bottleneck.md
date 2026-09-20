# FD-226 — Scale-adapted divisor reservoirs remove the quadratic prime-resolution loss but leave the Mertens cushion bottleneck

- **Date:** 2026-09-20
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** scale-adapted exact floor cells / divisor-reservoir geometry / prime-capacity improvement / Mertens-cushion diagnosis / pre-coverage obstruction
- **Depends on:** FD-225, FD-223, FD-005
- **Classification:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + SCALE-ADAPTED-RESERVOIRS + PRIME-RESOLUTION-IMPROVEMENT + MERTENS-CUSHION-BOTTLENECK`

## Claim

The surviving `D^2` sufficient-condition budget in FD-225 does not come indivisibly from the shrinking divisor reservoirs. The equal-width cells used there can be replaced by wider, scale-adapted exact floor cells

\[
I_d^*=\left(dN\left(1-\frac1{4D}\right),dN\right],
\qquad 1\le d\le D,
\tag{1}
\]

for which the complete divisor-response table is unchanged:

\[
\boxed{
\left\lfloor\frac{mN}{r}\right\rfloor
=
\left\lfloor\frac md\right\rfloor
\qquad
(r\in I_d^*,\ 1\le m,d\le D).
}
\tag{2}
\]

The interval width is now

\[
|I_d^*|=\frac{dN}{4D},
\tag{3}
\]

so the Vinogradov--Korobov prime-number-theorem remainder has uniform relative size only

\[
O\!\left(D\,e^{-c\Phi(N)}\right)
\tag{4}
\]

(up to harmless fixed polylogarithmic factors), rather than the `O(D^2 e^{-c\Phi(N)})` worst-case ratio produced by FD-223--FD-225's common width `asymp N/D` at ambient scale as large as `DN`.

Thus the quadratic loss is removable from the **prime-resolution** side of the construction.

However, this does **not** improve the presently certified block depth of FD-225. Full-grid flattening uses one common positive occupancy `A` in every reservoir. Exact divisor inversion makes that common occupancy forced if the baseline response is required to be constant, and the smallest cell `I_1^*` still limits

\[
A\asymp \frac{N}{D\log N}.
\tag{5}
\]

The correction that cancels the physical Mertens baseline still satisfies only the unconditional estimate

\[
\max_{d\le D}|c(d)|
\ll
DN\log N\,D^{o(1)}e^{-c_M\Phi(N)}+D^{o(1)},
\tag{6}
\]

so fitting `A+c(d)` into every reservoir continues to require, by the current argument,

\[
\boxed{
D^2D^{o(1)}(\log N)^2e^{-c_M\Phi(N)}=o(1).
}
\tag{7}
\]

Consequently FD-226 does not claim a longer switched blind block. It isolates the remaining quadratic pressure: after scale-adapting the exact floor cells, the extra factor `D` no longer comes from locating primes in the reservoirs; it comes from fitting the physical Mertens correction around the common occupancy needed by the constant full-grid target.

## 1. Exact scale-adapted floor cells

Put

\[
\epsilon=\frac1{4D},
\qquad
I_d^*=(dN(1-\epsilon),dN].
\]

Fix `1<=m,d<=D`, write

\[
m=qd+s,
\qquad 0\le s<d,
\]

and take `r in I_d^*`. Since `r<=dN`,

\[
\frac{mN}{r}\ge\frac md=q+\frac sd,
\]

so

\[
\left\lfloor\frac{mN}{r}\right\rfloor\ge q.
\tag{8}
\]

For the reverse inequality,

\[
\frac{mN}{r}
<
\frac{q+s/d}{1-\epsilon}.
\]

It is enough to prove

\[
q+\frac sd<(q+1)(1-\epsilon),
\]

or equivalently

\[
1-\frac sd>\epsilon(q+1).
\tag{9}
\]

The left side is at least `1/d`. Also

\[
q+1\le\frac Dd+1,
\]

hence

\[
\epsilon(q+1)
\le
\frac1{4d}+\frac1{4D}
\le
\frac1{2d}
<
\frac1d.
\tag{10}
\]

Thus (9) holds strictly, proving (2).

The cells are pairwise disjoint. Indeed, for `d<D`,

\[
(d+1)N(1-\epsilon)>dN
\]

because `\epsilon(d+1)<1`. For every fixed `0<beta<1`, the first lower endpoint also exceeds `beta N` once `D` is sufficiently large (and the bounded-`D` cases are harmless after enlarging `N`). Therefore every reservoir prime remains outside the exact Euler cutoff `p<=beta N` used in FD-223--FD-225.

## 2. Source-side response remains exact

Retain the selected-Euler source representation from FD-225. A flipped core prime `r in I_d^*` changes the sampled prefix at `mN` by

\[
2M\!\left(\left\lfloor\frac{mN}{r}\right\rfloor\right)
=
2M\!\left(\left\lfloor\frac md\right\rfloor\right).
\tag{11}
\]

There is no transform-space relaxation in (11). In the Vinogradov--Korobov range of FD-225 one has `D=N^{o(1)}`, hence eventually `D<beta N`. Every quotient in (11) is at most `D`, so all of its prime factors lie inside the locked Euler set and the Euler-cube extension gives the physical Mertens kernel exactly.

Different selected reservoir primes also cannot interact inside any sampled prefix. Every such prime is `>(1-o(1))N`, whereas the largest sampled argument is `DN=N^{1+o(1)}`. Thus the product of two selected reservoir primes exceeds `DN` for sufficiently large `N`. Their source-side responses therefore add without overlap exactly as in FD-225.

Consequently the complete response operator remains

\[
(\mathscr A c)(m)
=
\sum_{d\le m}
c_dM\!\left(\left\lfloor\frac md\right\rfloor\right),
\tag{12}
\]

with the exact inverse already proved in FD-225,

\[
\mathscr A c=y
\quad\Longleftrightarrow\quad
c(n)=\sum_{d\mid n}\bigl(y(d)-y(d-1)\bigr).
\tag{13}
\]

Thus changing the reservoir geometry has not changed a single algebraic response coefficient.

## 3. Prime capacity loses only one factor `D`

Let

\[
\Phi(x)=\frac{(\log x)^{3/5}}{(\log\log x)^{1/5}}.
\]

Use the same unconditional Vinogradov--Korobov prime-number-theorem remainder already anchored in `SOURCES.md` for FD-223. Uniformly for `d<=D=N^{o(1)}`, after weakening the exponential constant once,

\[
\vartheta(dN)-
\vartheta\!\left(dN\left(1-\frac1{4D}\right)\right)
=
\frac{dN}{4D}
+
O\!\left(dN e^{-c'_\vartheta\Phi(N)}\right).
\tag{14}
\]

The error-to-main ratio is therefore

\[
O\!\left(D e^{-c'_\vartheta\Phi(N)}\right),
\tag{15}
\]

independently of `d`. Allowing the fixed logarithmic factors needed to pass from `vartheta` to prime counts, the prime-capacity condition is of the form

\[
D\,\operatorname{polylog}(DN)
\,e^{-c'_\vartheta\Phi(N)}=o(1).
\tag{16}
\]

Under (16),

\[
|I_d^*\cap\mathbb P|
\gg
\frac{dN}{D\log(dN)}
\tag{17}
\]

uniformly for `1<=d<=D`.

This is the precise geometric gain. With the common-width cells `((d-h)N,dN)` of FD-223--FD-225, `h asymp 1/D`, the main term was `asymp N/D` even at ambient scale `dN asymp DN`, while the global PNT remainder there was `O(DN e^{-c\Phi(N)})`; the worst relative ratio therefore carried `D^2`. The scale-adapted cells make the main interval length grow proportionally to the ambient scale, so the prime-resolution ratio carries only one `D`.

No stronger prime-distribution theorem is being imported. The improvement is entirely from choosing the exact floor cells at their natural relative width.

## 4. Why the full-grid Mertens repair still pays `D^2`

FD-225 flattens the whole sampled grid by taking

\[
y(m)=\operatorname{nint}\!\left(-\frac{M(mN)}2\right),
\qquad
\varepsilon_m=M(mN)+2y(m),
\qquad
|\varepsilon_m|\le1,
\tag{18}
\]

and then using the inverse (13). It adds a positive baseline occupancy whose response is constant. This baseline cannot simply be rescaled with `d` to exploit the larger cells.

Indeed, suppose a baseline occupancy vector `b` has constant response

\[
\mathscr A b=A\mathbf 1.
\]

Since (13) is an exact inverse and the ordinary difference of `A\mathbf 1` is zero except at its first coordinate,

\[
\boxed{b_d=A\quad(1\le d\le D).}
\tag{19}
\]

Thus the constant full-grid target forces equal occupancy in every reservoir. The smallest cell `I_1^*`, whose prime capacity is `asymp N/(D\log N)`, still forces the scale (5).

Now let `c` be the exact correction obtained from (18). The same Mertens estimate used in FD-225 gives, uniformly for `d<=D`,

\[
|y(d)-y(d-1)|
\ll
 dN\log(DN)e^{-c'_M\Phi(N)}+1.
\tag{20}
\]

Hence, using (13),

\[
|c(n)|
\ll
N\log(DN)e^{-c'_M\Phi(N)}
\sum_{d\mid n}d
+
\tau(n).
\tag{21}
\]

The elementary bound

\[
\sum_{d\mid n}d\le n\tau(n)
\]

and `T(D):=max_{n<=D}tau(n)=D^{o(1)}` give

\[
\max_{n\le D}|c(n)|
\ll
DN\log N\,T(D)e^{-c'_M\Phi(N)}+T(D).
\tag{22}
\]

Comparing (22) with the forced common occupancy `A asymp N/(D\log N)` yields

\[
\frac{\max|c(n)|}{A}
\ll
D^2T(D)(\log N)^2e^{-c'_M\Phi(N)}
+
\frac{DT(D)\log N}{N}.
\tag{23}
\]

Thus the presently available physical-baseline repair still requires (7). The scale-adapted cells improve the prime-capacity side, but they do not by themselves improve the overall certified `J=O(\Phi(N))` range or the currently admissible constant in that range, because the Mertens cushion can remain the stricter condition.

This also shows why it would be incorrect to advertise (1) as a `D^2 -> D` improvement of the whole FD-225 construction. It is a `D^2 -> D` improvement of one specific analytic pressure, followed by an exact diagnosis of where the other quadratic pressure survives.

## 5. Boundary and next test

FD-225 already removed the `17^J` triangular-conditioning artifact. FD-226 now removes the additional quadratic loss from **prime-reservoir resolution** by matching each exact floor cell to its natural ambient scale. Neither algebraic conditioning nor the prime-number-theorem capacity estimate therefore explains the surviving `D^2` sufficient-condition budget.

Within the current full-grid-flattening architecture, the remaining quadratic term comes from two coupled facts: the physical Mertens correction can be as large as `DN e^{-c\Phi(N)}` at the top sampled scale under the available global bound, while a constant response forces a common positive occupancy and hence a cushion only of order `N/(D\log N)` from the smallest reservoir.

This identifies a sharper next negative test. One should ask whether the switched rows admit a nonconstant null target whose exact inverse occupancies grow with the available capacities `asymp dN/(D\log(dN))`. Such a target could use the extra room in large-`d` reservoirs and might remove the remaining common-cushion factor `D`. Alternatively, one needs a source-side estimate for the physical Mertens increments strong enough on these `N`-length intervals to beat the current global-baseline budget, or a genuine capacity obstruction showing that no switched-null target can exploit the variable capacities.

No clue status changes follow from this finding. No new literature dependency is load-bearing: the only analytic estimates are the same Vinogradov--Korobov PNT and Mertens bounds already recorded in `SOURCES.md`. Exact floor-quotient cells are classical in flavor and formula (2) is proved directly here; no novelty is claimed for floor-function constancy itself. The repository-specific conclusion is the separation of the FD-225 quadratic budget into a removable prime-resolution loss and a surviving Mertens/common-cushion loss.
