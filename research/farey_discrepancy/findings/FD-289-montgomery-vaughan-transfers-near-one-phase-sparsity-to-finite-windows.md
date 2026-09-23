# FD-289 — Montgomery–Vaughan transfers near-one phase sparsity to finite windows

- **Date:** 2026-09-23
- **Status:** proved uniform finite-window phase-spike sparsity; polynomial-height transference gap from FD-288 closed for continuous height windows
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** right-Perron-collar / Montgomery--Vaughan mean value / logarithmic-derivative local mean square / finite-window transference / route narrowing
- **Depends on:** FD-285, FD-287, FD-288
- **Classification:** `DERIVED + UNCONDITIONAL-STRICT-RIGHT-LOCAL-SPARSITY + FINITE-WINDOW + RIGHT-COLLAR + PHASE-SPIKE + RH-CONDITIONAL-PERRON-CONSEQUENCE + ROUTE-NARROWING`

## Claim

FD-288 showed that the order-`log x` near-one phase spikes required by FD-287 are sparse only in global Besicovitch density, and left open whether a moving polynomial height window could nevertheless lie almost entirely inside the exceptional set. The classical Montgomery--Vaughan mean-value theorem closes that transference gap for continuous windows.

Put

\[
L:=\log(2Nx),
\qquad
b:=L^{-2},
\qquad
a:=\eta/L,
\tag{1}
\]

with fixed

\[
\eta\in(e^{-\pi/2},1),
\tag{2}
\]

and define, as in FD-288,

\[
F_u(t):=-\frac{\zeta'}{\zeta}(1+u+it),
\qquad
M^{\mathrm{str}}_{\eta,L}(t)
:=
\sup_{b\le u\le a}
|\operatorname{Im}F_u(t)|.
\tag{3}
\]

Let `J=[H,H+R]` be an arbitrary real height interval of length `R>0`. There is an absolute constant in the estimates below such that

\[
\boxed{
\left(
\frac1R\int_J
M^{\mathrm{str}}_{\eta,L}(t)^2\,dt
\right)^{1/2}
\le
\sqrt{C_0}
+
O_\eta\!\left(
\frac1L+
\frac{L^3}{\sqrt R}
\right),
}
\tag{4}
\]

where

\[
C_0:=\sum_{n\ge2}\frac{\Lambda(n)^2}{n^2}<\infty.
\tag{5}
\]

Consequently, whenever

\[
\frac{R}{L^6}\longrightarrow\infty,
\tag{6}
\]

then uniformly in the starting height `H`, for every fixed `A>0`,

\[
\boxed{
\frac1R
\operatorname{meas}
\left\{
 t\in J:
 M^{\mathrm{str}}_{\eta,L}(t)\ge AL
\right\}
\le
\frac{C_0+o_\eta(1)}{A^2L^2}.
}
\tag{7}
\]

Thus the `O(L^{-2})` exceptional proportion of FD-288 is not merely a long-height Besicovitch statement. It holds in **every moving height window longer than a sufficient polylogarithmic scale**, with `L^6` a convenient sufficient threshold from the crude argument below.

In particular, if

\[
H=x^{\tau+o(1)},
\qquad \tau>0,
\tag{8}
\]

then the dyadic window `[H,2H]` satisfies (6) automatically. Under RH, in the FD-287 range `0<tau<1/2`, all but an `O(L^{-2})` proportion of that window fail the phase-spike condition required for internal self-cancellation of the complete right Perron collar. For those phase-good heights the FD-287 prime witness survives:

\[
\boxed{
\sum_{x<d\le2x}
|\mathcal H_d^R(T)|
\gg
\frac{Nx}{L^2\log x}
=
Nx^{1-o(1)}.
}
\tag{9}
\]

The strict-right local estimate (4)--(7) is unconditional. RH enters only in the inherited Perron consequence (9), through the prime-sector counting used in FD-287.

## 1. Montgomery--Vaughan gives a translated finite-window mean square

For a coefficient sequence with

\[
\sum_{n\ge1}n|c_n|^2<\infty,
\tag{10}
\]

the Montgomery--Vaughan mean-value theorem gives

\[
\int_0^R
\left|
\sum_{n\ge1}c_n n^{-it}
\right|^2dt
=
R\sum_{n\ge1}|c_n|^2
+
O\!\left(
\sum_{n\ge1}n|c_n|^2
\right).
\tag{11}
\]

The same estimate holds on any translated interval `[H,H+R]`: replace `c_n` by `c_n n^{-iH}`, which leaves every absolute coefficient unchanged. The infinite-series form follows from the finite theorem by truncation because (10) makes the partial sums Cauchy in `L^2(J)`; in the applications below the Dirichlet series also converges absolutely pointwise.

For `u>0`, absolute convergence gives

\[
F_u(t)
=
\sum_{n\ge2}
\frac{\Lambda(n)}{n^{1+u}}e^{-it\log n}.
\tag{12}
\]

Applying (11) with

\[
c_n(u)=\Lambda(n)n^{-1-u}
\tag{13}
\]

yields

\[
\frac1R\int_J|F_u(t)|^2dt
\le
C_0
+
\frac{C}{R}
\sum_{n\ge2}
\frac{\Lambda(n)^2}{n^{1+2u}}.
\tag{14}
\]

Using only `Lambda(n)<=log n`,

\[
\sum_{n\ge2}
\frac{\Lambda(n)^2}{n^{1+2u}}
\ll
\sum_{n\ge2}
\frac{(\log n)^2}{n^{1+2u}}
\ll u^{-3}.
\tag{15}
\]

Hence

\[
\boxed{
\frac1R\int_J|F_u(t)|^2dt
\le
C_0+O\!\left(\frac1{Ru^3}\right).
}
\tag{16}
\]

Differentiate in `u`:

\[
\partial_uF_u(t)
=
-
\sum_{n\ge2}
\frac{\Lambda(n)\log n}{n^{1+u}}
e^{-it\log n}.
\tag{17}
\]

Writing

\[
C_1:=
\sum_{n\ge2}
\frac{\Lambda(n)^2(\log n)^2}{n^2}<\infty,
\tag{18}
\]

the same theorem gives

\[
\frac1R\int_J|\partial_uF_u(t)|^2dt
\le
C_1
+
\frac{C}{R}
\sum_{n\ge2}
\frac{\Lambda(n)^2(\log n)^2}{n^{1+2u}}.
\tag{19}
\]

Again `Lambda(n)<=log n` is enough:

\[
\sum_{n\ge2}
\frac{\Lambda(n)^2(\log n)^2}{n^{1+2u}}
\ll
\sum_{n\ge2}
\frac{(\log n)^4}{n^{1+2u}}
\ll u^{-5},
\tag{20}
\]

so

\[
\boxed{
\frac1R\int_J|\partial_uF_u(t)|^2dt
\le
C_1+O\!\left(\frac1{Ru^5}\right).
}
\tag{21}
\]

Equations (16) and (21) are the finite-window replacement for the infinite-height orthogonality used in FD-288. Their key feature is that the error depends only on the coefficient-weighted moments, not on a hard Dirichlet-polynomial cutoff. The fact that `u=L^{-2}` gives an extremely long effective Dirichlet series therefore does not obstruct local mean square.

## 2. The maximal near-one envelope costs only `L^3/sqrt(R)` locally

For every `u in [b,a]`, the fundamental theorem of calculus gives

\[
|F_u(t)|
\le
|F_a(t)|
+
\int_b^a|\partial_vF_v(t)|\,dv,
\tag{22}
\]

and hence

\[
M^{\mathrm{str}}_{\eta,L}(t)
\le
|F_a(t)|
+
\int_b^a|\partial_vF_v(t)|\,dv.
\tag{23}
\]

Use the normalized local norm

\[
\|h\|_{2,J}
:=
\left(\frac1R\int_J|h(t)|^2dt\right)^{1/2}.
\tag{24}
\]

Minkowski, (16), and (21) give

\[
\|M^{\mathrm{str}}_{\eta,L}\|_{2,J}
\le
\left(C_0+O\!\left(\frac1{Ra^3}\right)\right)^{1/2}
+
\int_b^a
\left(C_1+O\!\left(\frac1{Rv^5}\right)\right)^{1/2}dv.
\tag{25}
\]

Since `a=eta/L`, the first term is

\[
\sqrt{C_0}+O_\eta\!\left(\frac{L^{3/2}}{\sqrt R}\right).
\tag{26}
\]

For the integral, use `sqrt(X+Y)<=sqrt(X)+sqrt(Y)`:

\[
\int_b^a
\left(C_1+O\!\left(\frac1{Rv^5}\right)\right)^{1/2}dv
\le
\frac{\eta\sqrt{C_1}}L
+
O\!\left(
\frac1{\sqrt R}
\int_b^a v^{-5/2}\,dv
\right).
\tag{27}
\]

Because `b=L^{-2}`,

\[
\int_b^a v^{-5/2}\,dv
\ll b^{-3/2}
=L^3.
\tag{28}
\]

Combining (25)--(28) proves (4). If `R/L^6 -> infinity`, the local maximal `L^2` norm is therefore

\[
\|M^{\mathrm{str}}_{\eta,L}\|_{2,J}
\le
\sqrt{C_0}+o_\eta(1),
\tag{29}
\]

uniformly in `H`. Chebyshev immediately yields (7).

The exponent `6` is not asserted to be sharp. It comes from the deliberately crude bounds (15), (20), the boundary choice `b=L^{-2}`, and a one-dimensional fundamental-theorem/Minkowski maximal estimate. The important point for the Farey problem is only that the required window length is **polylogarithmic rather than polynomial**.

## 3. Every polynomial dyadic Perron window is overwhelmingly phase-good

FD-287 showed that internal self-cancellation of the complete right collar requires an order-`L` spike in the near-one phase derivative. FD-288 split off the ultra-thin boundary slice `0<=u<=L^{-2}` and showed, using the already anchored Leong bound, that at polynomial heights its total phase cost is only `o(1)`.

For the remaining strict-inner strip, define

\[
f(\eta)
:=
\frac{\pi/2+\log\eta}{\eta}.
\tag{30}
\]

The optimizer from FD-287 is

\[
\eta_*:=e^{1-\pi/2},
\qquad
f_*:=f(\eta_*)=e^{\pi/2-1}.
\tag{31}
\]

Fix any small constant `kappa in (0,f_*)` and put

\[
A_\kappa:=f_*-\kappa.
\tag{32}
\]

If

\[
M^{\mathrm{str}}_{\eta_*,L}(T)<A_\kappa L,
\tag{33}
\]

then the strict-inner phase cost is at most

\[
\eta_*A_\kappa+o(1)
=
1-\eta_*\kappa+o(1).
\tag{34}
\]

The outer phase cost is

\[
\log(1/\eta_*)+o(1)
=
\frac\pi2-1+o(1),
\tag{35}
\]

so after adding the ultra-thin boundary slice, the total right-collar phase rotation is

\[
\le
\frac\pi2-\eta_*\kappa+o(1).
\tag{36}
\]

Thus a fixed common-half-plane margin survives.

Now take a polynomial dyadic window

\[
J=[H,2H],
\qquad
H=x^{\tau+o(1)},
\qquad
\tau>0.
\tag{37}
\]

Since `H/L^6 -> infinity`, (7) implies

\[
\frac1H
\operatorname{meas}
\left\{
T\in[H,2H]:
M^{\mathrm{str}}_{\eta_*,L}(T)
\ge A_\kappa L
\right\}
\le
\frac{C_0+o(1)}{A_\kappa^2L^2}.
\tag{38}
\]

Hence a proportion

\[
1-O_\kappa(L^{-2})
\tag{39}
\]

of every polynomial dyadic height window has the phase geometry required by FD-287. Under RH, if the whole window stays below `x^(1/2-epsilon)` for some fixed `epsilon>0`, Schoenfeld's prime-counting input from FD-284/FD-287 then supplies the same robust prime sectors for each such good height, and (9) follows.

This is the finite-window statement that FD-288 explicitly lacked. A moving polynomial window can no longer hide almost entirely inside the Besicovitch exceptional set: only an `O(L^{-2})` fraction of that very window is phase-bad.

## 4. What is closed, and what remains open

The result closes one precise loophole and no more. The phrase "global density does not control the moving polynomial window" in FD-288 is no longer an obstruction for **continuous height selection**. The local bound (38) is uniform in the starting point of the window, so it applies even when the polynomial window itself depends on `N` or on the Farey construction.

It does **not** show that an externally prescribed sparse sequence of individual heights avoids the exceptional set. A discrete source-selected sequence can still, in principle, hit only phase-bad points while those points occupy vanishing Lebesgue proportion in every surrounding window. Likewise, a Perron cutoff may have to satisfy additional constraints coming from the remainder, zero-cluster completion, or another contour piece. To exploit the abundance of phase-good heights one must still show that those independent admissibility conditions intersect the `1-O(L^{-2})` good set.

Nor does (9) control cancellation against the part of the contour with `Re(s)<=1`, or against a differently organized remainder. It only rules out internal self-cancellation of the right collar for almost every height in every polynomial window in the stated range.

The strict-right estimate (4) itself is unconditional. The RH dependence of the final Farey/Perron sentence is inherited, not introduced here: it is used to count primes in the `T log p` phase sectors uniformly up to sub-square-root spectral height.

## 5. Adversarial and prior-art audit

The load-bearing external input is classical, not new: Montgomery and Vaughan's Hilbert inequality yields the weighted mean-value theorem (11), including the coefficientwise `O(n)` error. The source is now anchored in `research/farey_discrepancy/SOURCES.md`. The translation from `[0,R]` to `[H,H+R]` is immediate coefficient rotation and does not require stationarity of `F_u`.

The potentially delicate infinite-series step is harmless here. For every `u>=b>0`, both

\[
\sum_n n|c_n(u)|^2
\quad\text{and}\quad
\sum_n n|\partial_uc_n(u)|^2
\tag{40}
\]

converge; therefore finite truncations are Cauchy in local `L^2`, while absolute convergence identifies the limit with `F_u` and `partial_u F_u` pointwise.

The `L^6` window threshold is only sufficient. No novelty is claimed for local mean squares of Dirichlet series, for the Montgomery--Vaughan theorem, or for the logarithmic derivative itself. The line-specific advance is that the exact maximal phase envelope isolated by FD-287/FD-288 has enough weighted coefficient decay that the classical theorem transfers its quadratic-log exceptional density **uniformly to every moving window of polylogarithmic length**, and therefore to every polynomial Perron-height window relevant to the current Farey branch.

A prior-art search for Montgomery--Vaughan mean values, finite-interval logarithmic-derivative bounds, and near-one `zeta'/zeta` mean squares found the classical theorem and standard uses of it, but no source making this Farey/Perron phase-envelope deduction. The claim is accordingly presented as a derived application, not as a new analytic-number-theory mean-value theorem.

## Frontier after FD-289

The right-collar route has moved from **finite-window transference** to **admissible-height intersection**. In every polynomial window below the inherited sub-square-root ceiling, almost every continuous height is now phase-good for the right collar. A viable escape must therefore do at least one of the following:

- force the admissible Perron cutoffs onto a sparse exceptional sequence despite the surrounding `1-O(L^{-2})` good measure;
- require an independent remainder or zero-cluster condition whose admissible set can avoid the phase-good set;
- cancel the protected right-collar witness against contour mass from `Re(s)<=1` or another representation layer;
- move beyond the current sub-square-root prime-sector range or change the Perron representation.

The next useful test is thus not another global or local mean-square estimate for `zeta'/zeta`. It is an **intersection theorem for phase-good heights with the independent cutoff conditions actually needed by the full explicit formula**.