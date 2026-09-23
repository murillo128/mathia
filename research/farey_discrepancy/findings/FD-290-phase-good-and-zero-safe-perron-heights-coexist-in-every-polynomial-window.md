# FD-290 — Phase-good and zero-safe Perron heights coexist in every polynomial window

- **Date:** 2026-09-23
- **Status:** proved positive-proportion intersection of phase-good and reciprocal-log zero-safe Perron heights in every polynomial dyadic window
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** admissible-height intersection / zero-avoidance / reciprocal-log clusters / right-Perron-collar / route narrowing
- **Depends on:** FD-279, FD-280, FD-287, FD-289
- **Classification:** `DERIVED + UNCONDITIONAL-ZERO-SAFETY-MEASURE + UNCONDITIONAL-PHASE-GOOD-INTERSECTION + RH-CONDITIONAL-RIGHT-COLLAR-CONSEQUENCE + SIMPLE-ZERO-CLUSTER-CONSEQUENCE + ROUTE-NARROWING`

## Claim

FD-289 left one immediate admissibility question open: even though a proportion `1-O(L^{-2})` of every polynomial height window is phase-good for the complete right Perron collar, could the independent requirement that the hard cutoff not split a reciprocal-log zero cluster force us onto a disjoint set of heights?

For the reciprocal-log cluster rule of FD-279, the answer is no. The zero-safety requirement itself removes only an explicit constant fraction of every polynomial window, and that fraction is small enough that the phase-good set must intersect it on positive measure, without any independence assumption and without shifting the cutoff after it has been chosen.

Fix

\[
x=N^{\lambda+o(1)},
\qquad
L:=\log(2Nx)
=
\left(1+\frac1\lambda+o(1)\right)\log x,
\qquad
\lambda>0,
\tag{1}
\]

and a polynomial dyadic height window

\[
J=[H,2H],
\qquad
H=x^{\tau+o(1)},
\qquad
0<\tau<\frac12.
\tag{2}
\]

Let `Gamma` denote the multiset of positive ordinates of nontrivial zeros of `zeta`, and define the reciprocal-log zero-unsafe set

\[
\mathcal Z_L(J)
:=
\left\{
T\in J:
\operatorname{dist}(T,\Gamma)<\frac1L
\right\}.
\tag{3}
\]

Then, unconditionally,

\[
\boxed{
\frac{\operatorname{meas}\mathcal Z_L(J)}{H}
\le
\frac{\tau}{\pi(1+1/\lambda)}+o(1).
}
\tag{4}
\]

Let `eta_*` and `f_*` be the optimized FD-287 phase parameters,

\[
\eta_*:=e^{1-\pi/2},
\qquad
f_*:=e^{\pi/2-1},
\tag{5}
\]

fix any constant `kappa in (0,f_*)`, and let `P_{kappa,L}(J)` be the FD-289 phase-bad set

\[
\mathcal P_{\kappa,L}(J)
:=
\left\{
T\in J:
M^{\mathrm{str}}_{\eta_*,L}(T)
\ge
(f_*-\kappa)L
\right\}.
\tag{6}
\]

FD-289 gives

\[
\operatorname{meas}\mathcal P_{\kappa,L}(J)
=O_\kappa\!\left(\frac{H}{L^2}\right).
\tag{7}
\]

Therefore the jointly admissible set

\[
\mathcal G_{\kappa,L}(J)
:=
J\setminus
\bigl(
\mathcal Z_L(J)\cup
\mathcal P_{\kappa,L}(J)
\bigr)
\tag{8}
\]

satisfies

\[
\boxed{
\frac{\operatorname{meas}\mathcal G_{\kappa,L}(J)}{H}
\ge
1-
\frac{\tau}{\pi(1+1/\lambda)}
-o(1).
}
\tag{9}
\]

Every `T in G_{kappa,L}(J)` is simultaneously phase-good and at distance at least `1/L` from every zeta-zero ordinate. In particular it cannot lie inside any gap of length `<2/L`; hence, under the RH/simple-zero cluster formalism of FD-279, a hard cutoff at such a height does not split any reciprocal-log zero cluster.

For the first-row scale `lambda=1`, (9) becomes

\[
\frac{\operatorname{meas}\mathcal G_{\kappa,L}(J)}H
\ge
1-\frac{\tau}{2\pi}-o(1).
\tag{10}
\]

Across the whole inherited range `0<tau<1/2`, this is uniformly at least

\[
\boxed{
1-\frac1{4\pi}-o(1)
=
0.9204225284\ldots-o(1).
}
\tag{11}
\]

Thus the phase-good and cluster-complete requirements do not merely coexist somewhere: in the first-row regime they coexist on more than about `92%` of every polynomial dyadic window even at the worst end of the current sub-square-root height range.

## 1. A `1/L` zero collar occupies only a controlled fraction of the window

Let `N_zeta(T)` denote the number of nontrivial zeta zeros with positive ordinate at most `T`, counted with multiplicity. By the Riemann--von Mangoldt formula,

\[
N_\zeta(T)
=
\frac{T}{2\pi}\log\frac{T}{2\pi}
-
\frac{T}{2\pi}
+
O(\log T).
\tag{12}
\]

Every point of `Z_L(J)` lies inside an interval of radius `1/L` around a zero ordinate belonging to

\[
[H-1/L,\,2H+1/L].
\tag{13}
\]

The endpoint enlargement in (13) is important: zeros just outside `J` can still contribute a zero-unsafe piece inside `J`.

A union bound, with no spacing assumption and no need to separate multiple zeros, gives

\[
\operatorname{meas}\mathcal Z_L(J)
\le
\frac2L
\left(
N_\zeta(2H+1/L)-N_\zeta(H-1/L)
\right).
\tag{14}
\]

Riemann--von Mangoldt yields the coarse but sufficient count

\[
N_\zeta(2H+1/L)-N_\zeta(H-1/L)
=
\frac{H}{2\pi}\log H+O(H),
\tag{15}
\]

and therefore

\[
\operatorname{meas}\mathcal Z_L(J)
\le
\frac{H\log H}{\pi L}
+O\!\left(\frac HL\right).
\tag{16}
\]

Using (1)--(2),

\[
\frac{\log H}{L}
=
\frac{\tau}{1+1/\lambda}+o(1),
\tag{17}
\]

which proves (4).

This estimate is deliberately insensitive to zero correlations. Overlap between neighboring `1/L` collars can only decrease their union measure. Counting multiplicities in `N_zeta` can only overcount the union when several zeros have the same ordinate. No RH, simplicity, pair-correlation hypothesis, or local zero-spacing theorem is used in (4).

More generally, replacing the radius `1/L` by `c/L` gives the immediate bound

\[
\frac{\operatorname{meas}\mathcal Z_{c,L}(J)}H
\le
\frac{c\tau}{\pi(1+1/\lambda)}+o(1).
\tag{18}
\]

The choice `c=1` is not arbitrary for the present line: it is the smallest symmetric radius that uniformly excludes every point lying inside a gap of length `<2/L`.

## 2. Zero-safe implies cluster-complete at the FD-279 scale

FD-279 connects consecutive critical ordinates whenever their gap is strictly less than

\[
\frac2L.
\tag{19}
\]

Suppose a height `T` lies strictly inside such a gap,

\[
\gamma_j<T<\gamma_{j+1},
\qquad
\gamma_{j+1}-\gamma_j<\frac2L.
\tag{20}
\]

Then elementary geometry gives

\[
\min\{T-\gamma_j,\,\gamma_{j+1}-T\}
\le
\frac{\gamma_{j+1}-\gamma_j}{2}
<
\frac1L.
\tag{21}
\]

Hence every cutoff that splits an edge of a reciprocal-log cluster belongs to `Z_L(J)`. Contrapositively,

\[
\operatorname{dist}(T,\Gamma)\ge\frac1L
\quad\Longrightarrow\quad
T\text{ does not split any edge with gap }<2/L.
\tag{22}
\]

A connected cluster can be split by a hard height cutoff only across one of its internal edges, so (22) is exactly the cluster-completeness condition needed here. The strict inequality in the FD-279 edge rule also removes a boundary ambiguity: a midpoint at distance exactly `1/L` can occur only for a gap of length at least `2/L`, which is not a close edge.

This is stronger operationally than the completion statement of FD-279 for the present purpose. FD-279 showed that a cutoff which does split the boundary cluster can be moved by `O(1/log log x)` to complete it. FD-280 then showed why that move cannot be treated as harmless for the remainder: the remainder jumps by the negative of the newly added zero packet. Equation (22) avoids that issue entirely. We choose a cluster-complete height from the start, so there is no post-selection displacement and no appeal to remainder continuity.

## 3. Intersecting with the FD-289 phase-good set requires no independence

The phase-bad estimate (7) is uniform over the position of the polynomial window. Combining it with (4) is now just a union bound:

\[
\begin{aligned}
\operatorname{meas}\mathcal G_{\kappa,L}(J)
&\ge
H
-
\operatorname{meas}\mathcal Z_L(J)
-
\operatorname{meas}\mathcal P_{\kappa,L}(J)\\
&\ge
H\left(
1-
\frac{\tau}{\pi(1+1/\lambda)}
-o(1)
\right).
\end{aligned}
\tag{23}
\]

No statistical independence between zero locations and the phase envelope is assumed. In fact the two bad sets may be maximally correlated; (23) survives because the zero-unsafe set itself cannot occupy enough of the window to cover the overwhelmingly phase-good set.

For every fixed `lambda>0` and `0<tau<1/2`, the right side of (9) is bounded away from zero. Uniformly over all such `lambda`, the crude worst-case lower fraction is still

\[
1-\frac1{2\pi}-o(1)
=
0.840845\ldots-o(1),
\tag{24}
\]

while the first-row specialization is the stronger `0.920422...` in (11).

Under RH, FD-289 says that every phase-good height in the inherited sub-square-root range carries the protected prime witness for the complete right collar,

\[
\sum_{x<d\le2x}
|\mathcal H_d^R(T)|
\gg
\frac{Nx}{L^2\log x}
=
Nx^{1-o(1)}.
\tag{25}
\]

Under the additional simple-zero convention used by FD-279, every `T` in the same jointly good set is also cluster-complete. Thus (23) supplies a positive-measure family of heights satisfying both currently independent right-side admissibility conditions simultaneously.

## 4. What this closes, and what remains open

FD-289 ended with three qualitatively different ways the admissible-height program could still fail. The first was that zero-cluster completion might select a set disjoint from the phase-good heights. Equations (9) and (23) close that particular obstruction for any Perron argument that is free to choose its cutoff continuously inside a polynomial dyadic window.

The second obstruction remains untouched and is now more isolated: **remainder-goodness**. Nothing here proves that the Perron remainder, the left-side contour contribution, or another full-explicit-formula condition is small on a positive proportion of the same window. FD-280 is especially relevant: because remainder and zero packet exchange mass exactly when a hard cutoff crosses zeros, one cannot manufacture a remainder-good height by first choosing a phase-good height and then making a tiny cluster-completion shift.

The third obstruction also remains: an external argument could prescribe a sparse discrete sequence of heights rather than allow continuous selection. Positive Lebesgue measure in every surrounding window does not force an arbitrary discrete sequence to hit the good set. The current statement is therefore an **existence-and-abundance theorem for selectable heights**, not a theorem about every source-selected sequence.

Nor does (25) prevent cancellation between the protected right collar and contour mass from `Re(s)<=1`. It only says that the right collar itself is simultaneously phase-protected and free of reciprocal-log cluster cuts on the set quantified by (9).

## 5. Adversarial and prior-art audit

The zero-counting input is the classical Riemann--von Mangoldt formula already used in FD-279; no new external theorem is introduced in this finding. The phase-window input is inherited verbatim from FD-289, whose Montgomery--Vaughan source is already anchored in `research/farey_discrepancy/SOURCES.md`. No `SOURCES.md` change is therefore needed.

Several failure modes were checked explicitly. Zeros just outside the dyadic window are included through the expanded interval (13). Overlapping zero collars and multiplicities only make the union bound safer. The strict `<2/L` edge threshold is compatible with the closed zero-safe condition `dist(T,Gamma)>=1/L`. The argument never shifts a selected cutoff, so it does not reuse the false remainder-continuity heuristic ruled out by FD-280. Finally, (23) uses only a union bound and therefore contains no hidden independence hypothesis between the zeta-zero process and the near-one phase envelope.

Classical analytic-number-theory arguments often choose "good ordinates" away from zeta zeros when moving Perron contours; no novelty is claimed for zero avoidance or for Riemann--von Mangoldt itself. A prior-art check found standard contour-selection and zero-counting uses, but no source for the line-specific quantitative intersection here: the exact `1/L` safety radius forced by the FD-279 `<2/L` cluster rule combined with the FD-289 finite-window phase-good density. The result is accordingly classified as a derived route-narrowing statement, not as a new zero-distribution theorem.

## Frontier after FD-290

Within every polynomial window below the current sub-square-root ceiling, there is now a quantitatively large continuum of cutoffs that are simultaneously phase-good for the right Perron collar and cluster-complete at the reciprocal-log zero scale. For `lambda=1`, even the worst end of that range leaves more than `92%` of the window available asymptotically.

The next useful test is therefore the remaining **remainder-good intersection**: obtain a finite-window measure estimate for heights at which the relevant truncated-Perron remainder (or an equivalent full-contour error object) is below the Farey repair threshold, and compare that exceptional measure with the positive reserve in (9). If the remainder-good set has any sufficiently large window density, the three-way intersection `phase-good + zero-safe + remainder-good` follows without needing independence; if it does not, the obstruction will finally be located in the remainder rather than in cutoff geometry.