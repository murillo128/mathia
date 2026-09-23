# FD-291 — Gapwise-constant hard remainders need only quadratic-log good-gap occupation

- **Date:** 2026-09-23
- **Status:** proved exact gapwise constancy and a vanishing-density sufficient criterion for the remaining admissible-height intersection
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** hard residue truncation / complementary remainder / zero-gap occupation / admissible-height intersection / right-Perron-collar / route narrowing
- **Depends on:** FD-280, FD-289, FD-290
- **Classification:** `EXACT-DERIVED + GAPWISE-CONSTANT-COMPLEMENT + ZERO-SAFE-CORE + QUADRATIC-LOG-INTERSECTION-CRITERION + ROUTE-NARROWING`

## Claim

FD-290 reduces the current hard-Perron frontier to a three-way intersection: choose a height that is phase-good for the right collar, zero-safe at reciprocal-log scale, and good for the **full complementary remainder**. A direct union bound with an arbitrary remainder-good set would appear to require a fixed positive proportion of the height window, because zero-safety itself removes a fixed fraction.

For the exact hard residue decomposition of FD-280, that is unnecessarily strong. The complementary remainder is **constant on every open interval between consecutive distinct zero ordinates**. Therefore remainder-goodness is a property of zero gaps, while the FD-289 phase condition can still be selected continuously inside each gap. Once a remainder-good gap has been trimmed by `1/L` at both zero boundaries, zero-safety is automatic; one no longer pays the full zero-unsafe measure from FD-290 in the final intersection.

Precisely, write the FD-280 exact decomposition

\[
A(y)=C(y)+P_T(y)+E_T(y),
\qquad
P_T(y)=\sum_{0<\gamma\le T}R_\gamma(y),
\tag{1}
\]

with `C` independent of `T`, and apply the physical Farey map

\[
\mathcal R_{T,N}(d)
:=
\sum_{q\mid d}
\bigl(E_T(Nq)-E_T(N(q-1))\bigr).
\tag{2}
\]

Let `Gamma_*` be the increasing sequence of **distinct** positive ordinates of nontrivial zeta zeros. If

\[
\gamma_j<T_0<T_1<\gamma_{j+1},
\tag{3}
\]

then no residue enters the hard packet between `T_0` and `T_1`, so FD-280 gives exactly

\[
\boxed{
E_{T_1}=E_{T_0},
\qquad
\mathcal R_{T_1,N}=\mathcal R_{T_0,N}.
}
\tag{4}
\]

Thus every band norm

\[
\mathscr R_{N,x}(T)
:=
\sum_{x<d\le2x}|\mathcal R_{T,N}(d)|
\tag{5}
\]

is constant on each zero gap.

Now put, as in FD-289--FD-290,

\[
L:=\log(2Nx),
\qquad
J=[H,2H],
\qquad
H=x^{\tau+o(1)},
\qquad
0<\tau<\frac12.
\tag{6}
\]

Fix any desired physical remainder budget `B_{N,x}`. Call a zero gap `G_j=(\gamma_j,\gamma_{j+1})` **remainder-good** when the constant value in (5) satisfies

\[
\mathscr R_{N,x}(T)\le B_{N,x}
\qquad(T\in G_j).
\tag{7}
\]

Its reciprocal-log safe core inside `J` is

\[
G_j^{\rm safe}(J)
:=
J\cap
\left[
\gamma_j+\frac1L,
\gamma_{j+1}-\frac1L
\right],
\tag{8}
\]

interpreted as empty when the right endpoint is smaller than the left endpoint. Define the total safe remainder-good occupation

\[
\Omega_B(J)
:=
\sum_{j:\,G_j\ \mathrm{remainder\text{-}good}}
\operatorname{meas}G_j^{\rm safe}(J).
\tag{9}
\]

Every height counted by `Omega_B(J)` is already remainder-good and at distance at least `1/L` from every neighboring zero ordinate, hence is zero-safe in the sense of FD-290.

Let

\[
\eta_*:=e^{1-\pi/2},
\qquad
f_*:=e^{\pi/2-1},
\tag{10}
\]

fix `kappa in (0,f_*)`, and put

\[
A_\kappa:=f_*-\kappa,
\qquad
C_\phi(\kappa):=
\frac{C_0}{A_\kappa^2},
\qquad
C_0:=\sum_{n\ge2}\frac{\Lambda(n)^2}{n^2}.
\tag{11}
\]

FD-289 gives for the phase-bad set `P_{kappa,L}(J)`

\[
\operatorname{meas}\mathcal P_{\kappa,L}(J)
\le
\left(C_\phi(\kappa)+o(1)\right)
\frac{H}{L^2}.
\tag{12}
\]

Consequently, for every fixed `delta>0`, the single occupation condition

\[
\boxed{
\Omega_B(J)
\ge
\left(C_\phi(\kappa)+\delta\right)
\frac{H}{L^2}
}
\tag{13}
\]

forces, for all sufficiently large `x`, the existence of a height

\[
T\in J
\tag{14}
\]

that is simultaneously

\[
\boxed{
\text{phase-good}
\quad+\quad
\text{zero-safe}
\quad+\quad
\mathscr R_{N,x}(T)\le B_{N,x}.
}
\tag{15}
\]

Thus the remaining full-remainder theorem does **not** need to prove positive-density goodness in the height window. It is enough to prove that reciprocal-log-safe cores of remainder-good zero gaps occupy slightly more than `O(H/L^2)`. This lowers the deterministic intersection target from a fixed positive window fraction to a **quadratic-log vanishing fraction**.

## 1. The full complementary remainder is exactly constant between zero ordinates

FD-280 proves for any two hard cutoffs `T_0<T_1`

\[
E_{T_1}-E_{T_0}
=-\left(P_{T_1}-P_{T_0}\right).
\tag{16}
\]

If `T_0,T_1` lie in the same open interval between consecutive distinct zero ordinates, the hard packet is identical at both heights. Hence (16) immediately gives the first identity in (4). Applying consecutive sampling and divisor replication, or simply using the coordinatewise FD-280 transfer identity, gives the second.

Multiplicity causes no difficulty. If several zeros share one ordinate, all terms attached to that ordinate enter in the same jump of `P_T`; between two **distinct** ordinates there is still no jump. The statement also does not require RH or zero simplicity. The latter enters only when one interprets reciprocal-log components using the simple-critical-zero formalism of FD-279.

This constancy concerns the **full exact complement** `E_T` in (1). It must not be confused with an individual contour segment or with the pre-shift truncated-Perron error

\[
M(y)-I_{T,c}(y)
\tag{17}
\]

from FD-281. Those pieces can vary continuously with `T` between zeros. After contour shifting, however, all non-packet pieces sum to the exact complement in (1), and their `T`-dependence must cancel between zero crossings because the source and hard residue packet are both fixed there. The present result exploits only that complete grouped object.

## 2. Trimming a good gap builds zero-safety in for free

Take any `T in G_j^{safe}(J)`. By construction,

\[
T-\gamma_j\ge\frac1L,
\qquad
\gamma_{j+1}-T\ge\frac1L.
\tag{18}
\]

There is no distinct zero ordinate inside `G_j`, so

\[
\operatorname{dist}(T,\Gamma_*)\ge\frac1L.
\tag{19}
\]

Zeros farther away can only increase the distance. Therefore every point counted in (9) belongs to the zero-safe set of FD-290. In particular, under the FD-279 reciprocal-log cluster rule connecting consecutive ordinates across gaps `<2/L`, such a `T` cannot split a close cluster.

At the same time (4) makes the remainder condition constant across all of `G_j`. Trimming does not alter the remainder value; it only removes the boundary collar where zero-safety is unavailable. Thus the set

\[
\mathcal Q_B(J)
:=
\bigcup_{j:\,G_j\ \mathrm{remainder\text{-}good}}
G_j^{\rm safe}(J)
\tag{20}
\]

has exactly

\[
\operatorname{meas}\mathcal Q_B(J)=\Omega_B(J)
\tag{21}
\]

and every one of its points is already both remainder-good and zero-safe.

This is the structural gain over treating remainder-goodness as an arbitrary measurable condition. FD-290 had to subtract the entire zero-unsafe set because an arbitrary remainder-good point might sit anywhere. Here the good object is a whole zero gap, so zero-safety can be imposed internally before intersecting with any other condition.

## 3. Only the phase-exceptional budget remains to be beaten

The desired triple intersection is now simply

\[
\mathcal Q_B(J)
\setminus
\mathcal P_{\kappa,L}(J).
\tag{22}
\]

By (12) and (21),

\[
\operatorname{meas}
\left(
\mathcal Q_B(J)
\setminus
\mathcal P_{\kappa,L}(J)
\right)
\ge
\Omega_B(J)
-
\left(C_\phi(\kappa)+o(1)\right)
\frac{H}{L^2}.
\tag{23}
\]

Condition (13) makes the right side positive for all sufficiently large `x`, proving (15). No independence between remainder size, zero gaps, and the near-one phase envelope is used.

The quantitative change from FD-290 is substantial. If the remainder-good set were an arbitrary subset of `J`, a deterministic union-bound argument would have to overcome the zero-unsafe fraction

\[
\frac{\tau}{\pi(1+1/\lambda)}+o(1),
\tag{24}
\]

a fixed positive number. At the balanced first-row scale `lambda=1` and near the top of the current `tau<1/2` range this can approach `1/(4pi)=0.079577...`. Once remainder-goodness is recognized as gapwise constant and the safe core is taken **inside** each good gap, that fixed tax disappears from the final intersection. The only universal set that can still cover all safe good cores is the phase-bad set, whose measure is `O(H/L^2)`.

Therefore a future remainder theorem need not show that `8%`, `1%`, or any other fixed percentage of heights is good. A vanishing weighted occupation slightly larger than `L^{-2}` is enough.

There is also a useful counting corollary. Fix `c>0`. Suppose there are `K` remainder-good zero gaps fully contained in `J`, each of length at least

\[
\frac{2+c}{L}.
\tag{25}
\]

Each contributes at least `c/L` to (9), so (13) follows from

\[
\boxed{
K
\ge
\left(C_\phi(\kappa)+\delta\right)
\frac{H}{cL}.
}
\tag{26}
\]

Riemann--von Mangoldt gives `Theta(H log H)=Theta(HL)` zero gaps in a polynomial window. Thus, among gaps satisfying the fixed reciprocal-log length lower bound (25), only an `O(L^{-2})` fraction of the total gap population would need to be remainder-good to force an admissible height. Equation (26) is only a sufficient counting reformulation; the main criterion (13) is weighted by safe-core length and requires no gap-spacing law.

## 4. What this does and does not solve

The result does not prove that any remainder-good gap exists at the repair budget required by FD-261. It changes the target for such a theorem. Instead of controlling the remainder on a positive proportion of all real heights, it is enough to certify a very sparse family of zero gaps whose **trimmed length mass** exceeds `H/L^2` by a fixed constant factor.

For the canonical repair application one may take, for example,

\[
B_{N,x}=o\!\left(N^\theta x^{2-\beta}\right),
\qquad
\beta=\log_2\frac32,
\tag{27}
\]

whenever the spectral packet is being tested at arithmetic amplitude `N^theta`. If (13) can be proved for that budget, the resulting height is remainder-good, zero-safe, and phase-good. Under RH and the inherited sub-square-root height restriction, FD-289 then supplies the protected prime witness for the complete right collar at the same selected height.

The theorem does not say that the right collar and the full complementary remainder cannot cancel each other in the final exact source. It only removes a selection obstacle: if a sufficiently sparse collection of gaps already has a small full complement, phase-good selection can be made *inside those same gaps* without paying the constant zero-avoidance tax.

Nor does the result apply unchanged to a smoothed spectral cutoff. Smooth weights transfer residue mass continuously with `T`, so the exact complement need not be gapwise constant. Such an architecture may have other advantages, but it requires its own admissible-height analysis.

Finally, the reduction is useful only for a remainder organized as the complete complement of a hard residue packet. Bounding individual horizontal, left-vertical, or Perron-truncation pieces separately can destroy the gapwise constancy even though their sum has it. A proof that keeps those pieces separate must control their mutual cancellation or revert to a stronger pointwise certificate such as FD-281.

## 5. Adversarial and prior-art audit

The first adversarial check is the apparent contradiction with the continuously moving Perron contour. There is none. The top and side contour integrals, together with the initial truncation error, can each depend on `T` between zeros. Equation (4) concerns their **complete sum after the hard residue packet is removed from the exact source**. Because the packet does not change inside a zero gap, that complete sum cannot change either.

The second check is boundary behavior. A good gap shorter than `2/L` contributes nothing to `Omega_B(J)`, exactly as it should: no point in such a gap is guaranteed to be `1/L` away from both bounding ordinates. Gaps crossing `H` or `2H` are handled by intersecting the safe core with `J`; zeros just outside the window therefore cause no missing endpoint collar. Multiple zeros at one ordinate are handled by using distinct ordinates for the gaps.

The third check is circularity with FD-280. FD-280 ruled out moving a chosen cutoff across a close cluster and pretending that the remainder changed little. FD-291 makes no such move. It first classifies whole gaps by the exact constant remainder they already carry, trims their interiors, and then chooses a phase-good point inside a good safe core. No remainder-continuity inference is used.

A fresh prior-art search covered hard zero truncations of the Mertens explicit formula, Perron good-ordinate arguments, cutoff-dependent remainders, and current explicit Mertens work. Classical explicit-formula literature of course contains the underlying residue bookkeeping, and the Lee--Leong treatment already anchored in `SOURCES.md` controls the difference between `M(x)` and a chosen short zero sum by estimating the remaining contour/reciprocal-zeta terms. No novelty is claimed for the algebraic statement that a hard residue packet is unchanged between zero ordinates. The line-specific content here is the combination with FD-289's translated `O(L^{-2})` phase-exceptional measure and FD-290's exact `1/L` cluster-safety scale, which converts the remaining three-way cutoff problem into the weighted occupation criterion (13). No new external theorem is load-bearing, so `SOURCES.md` requires no change.

## Frontier after FD-291

The hard-Perron admissible-height problem is now narrower than the positive-density formulation left by FD-290. The next useful theorem is a **good-zero-gap occupation estimate for the full complementary remainder**:

\[
\sum_{j:\,\mathscr R_{N,x}|_{G_j}\le B_{N,x}}
\operatorname{meas}
\left(
J\cap
\left[\gamma_j+\frac1L,\gamma_{j+1}-\frac1L\right]
\right)
\gg
\frac{H}{L^2}.
\tag{28}
\]

For a repair budget below `N^theta x^(2-beta)`, such an estimate would already produce a cutoff that is simultaneously remainder-good, cluster-complete, and phase-good. Proving a fixed positive density would be much stronger than necessary.

This also clarifies the ownership boundary. If (28) can only be attacked after discarding the physical consecutive-difference/divisor-replication geometry and reducing everything to a generic estimate for a Möbius Mellin transform, then the new bottleneck has left `farey_discrepancy`. If the full grouped contour and its divisor-replicated physical norm are essential to obtaining even this sparse good-gap occupation, the problem remains genuinely Farey-specific.