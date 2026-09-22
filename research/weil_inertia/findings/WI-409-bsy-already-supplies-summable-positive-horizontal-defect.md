# WI-409 — Balazard--Saias--Yor already supplies a summable positive horizontal-defect functional

**Status:** `CLASSICAL-IDENTITY + LITERATURE+DERIVED + EXACT-DERIVED + PRIOR-ART-REDIRECT + DECISIVE-NEGATIVE`.

**Parent findings:** [WI-405](./WI-405-signed-widder-mellin-averages-collapse-to-superzeta-and-require-renormalization.md), [WI-406](./WI-406-canonical-superzeta-continuation-at-critical-widder-weight-is-fixed.md), [WI-407](./WI-407-superzeta-derivative-at-minus-one-gives-log-weighted-defect.md), [WI-408](./WI-408-finite-superzeta-jets-only-control-log-moments.md).

## Claim

The recent signed-Widder/superzeta branch has been searching for a globally summable positive statistic that charges every off-critical functional-equation pair and could then be coupled to a source-side identity. Classical prior art shows that the **zero-side part of that objective is already available in a stronger form**.

Balazard, Saias and Yor proved the exact identity

\[
\boxed{
\int_{\Re s=1/2}\frac{\log|\zeta(s)|}{|s|^2}\,|ds|
=
2\pi\sum_{\beta>1/2}
\log\left|\frac{\rho}{1-\rho}\right|,
}
\tag{1}
\]

where the sum is over nontrivial zeros `rho=beta+i gamma` with `beta>1/2`, counted with multiplicity. Bui--Lester--Milinovich restate (1) as equation (1.1), prove a truncated unconditional version, and give another contour proof. Every summand on the right is strictly positive, so (1) vanishes if and only if RH holds.

For an off-critical quartet write its upper-right member as

\[
\rho=\frac12+d+i\gamma,
\qquad 0<d<\frac12,
\qquad \gamma>0.
\]

Its single-zero BSY charge is exactly

\[
\boxed{
q_{\rm BSY}(\gamma,d)
:=\log\left|\frac{\rho}{1-\rho}\right|
=
\operatorname{artanh}
\frac{d}{\gamma^2+\frac14+d^2}.
}
\tag{2}
\]

Hence

\[
q_{\rm BSY}(\gamma,d)>0
\quad(d>0),
\tag{3}
\]

and, uniformly for `0<d<=1/2` as `gamma -> infinity`,

\[
\boxed{
q_{\rm BSY}(\gamma,d)
=
\frac{d}{\gamma^2}
+O\!\left(\frac{d}{\gamma^4}\right).
}
\tag{4}
\]

Thus the classical BSY defect is **linear** in horizontal depth near the critical line. It is stronger there than the `d^2`, `d^2 log gamma`, or fixed-log-moment carriers isolated in WI-405--WI-408.

Moreover the positive zero-side sum is absolutely convergent without any density hypothesis beyond the classical Riemann--von Mangoldt count. Therefore the obstacle exposed by WI-405--WI-408 is not the existence of a canonical summable positive off-line defect. That object already exists. The missing step is instead **source-side coercivity**: one must force the left side of (1) to be exactly zero (or derive an independently incompatible positive lower bound) without assuming RH.

This materially redirects the line. Building another positive summable scalar defect functional, or another family of finite budgets, cannot by itself be a defect-to-zero mechanism. Any useful continuation of the Weil/inertia program must couple its matrix information to a source-side statement that annihilates such a defect, or produce additional rigidity that converts one off-line zero into a nonzero quantum incompatible with an independently vanishing source quantity.

No proof of RH and no improved simple-critical-zero proportion is claimed.

## 1. Exact quartet charge

For

\[
\rho=\frac12+d+i\gamma,
\qquad
1-\rho=\frac12-d-i\gamma,
\]

one has

\[
|\rho|^2
=\gamma^2+\left(\frac12+d\right)^2,
\qquad
|1-\rho|^2
=\gamma^2+\left(\frac12-d\right)^2.
\]

Set

\[
A:=\gamma^2+\frac14+d^2.
\]

Then

\[
q_{\rm BSY}(\gamma,d)
=
\frac12\log\frac{A+d}{A-d}
=
\operatorname{artanh}\frac dA,
\]

which proves (2). Since `A>d` for every nontrivial zero and `d>0`, positivity (3) is exact. The conjugate zero at `-gamma` has the same charge, so a complete off-critical quartet contributes `2 q_BSY(gamma,d)` to the sum in (1).

Expanding `artanh x=x+O(x^3)` and using

\[
\frac1A
=
\frac1{\gamma^2}
+O\!\left(\frac1{\gamma^4}\right)
\]

uniformly for `0<d<=1/2` gives (4). The crucial comparison with the recent superzeta branch is therefore

\[
q_{\rm BSY}(\gamma,d)
\asymp \frac d{\gamma^2},
\]

whereas the WI-408 fixed-order exponent-jet carriers are quadratic in `d`. BSY detects arbitrarily shallow horizontal displacement more strongly at the local level.

## 2. Absolute convergence needs no off-line density theorem

For all sufficiently high zeros the argument of `artanh` in (2) is less than `1/2`, so

\[
0<q_{\rm BSY}(\gamma,d)
\le
2\frac dA
\ll \gamma^{-2}.
\tag{5}
\]

The Riemann--von Mangoldt estimate `N(T)=O(T log T)` implies

\[
\sum_{\rho:\,|\gamma|>1}\frac1{\gamma^2}<\infty.
\tag{6}
\]

Hence the positive sum on the right of (1) converges absolutely. No assumption about a positive proportion, density zero, or a lower bound for horizontal depth is used.

This point is important for the WI-405--WI-408 comparison. The superzeta critical carrier at `sigma=-1` had a useful local charge but required a matched renormalization because the separate actual and criticalized power sums diverged. BSY has already performed a different source-compatible cancellation: the contour kernel `1/[s(1-s)]` turns every horizontal branch cut into the convergent logarithmic ratio in (2). The resulting defect is simultaneously positive, additive, and summable.

## 3. Why this does not already solve the research mandate

Equation (1) is an **equivalence**, not an unconditional vanishing theorem. Its left side is a genuine zeta-side boundary integral, but current theory does not prove that it is zero. Indeed, BSY's theorem states precisely

\[
\mathrm{RH}
\quad\Longleftrightarrow\quad
\int_{\Re s=1/2}\frac{\log|\zeta(s)|}{|s|^2}|ds|=0.
\tag{7}
\]

Therefore the classical identity supplies the desired positive defect ledger but not the missing coercive source conclusion.

Nor can a density statement alone close this gap. A single hypothetical quartet with ordinate `gamma` and arbitrarily small depth `d` has positive charge, but by (4) that charge can be arbitrarily small. More generally, a sparse sequence of off-line quartets with depths tending rapidly to zero can have an arbitrarily small total BSY mass while remaining nonempty. Thus

\[
\text{``almost all zeros are critical''}
\quad\not\Rightarrow\quad
\text{BSY defect}=0,
\tag{8}
\]

and the same remains true for any fixed quantitative improvement of the simple-critical-zero proportion.

This is the same logical distinction isolated in WI-408 in moment language, now sharpened by stronger prior art: **the problem is not to manufacture a positive measure of off-line mass; it is to force its exact annihilation.**

## 4. Consequence for the Weil/inertia program

The BSY identity changes the useful target for the current line.

A new matrix-inertia refinement is relevant to RH only if it does at least one of the following:

1. couples the Weil/inertia defect to the BSY boundary integral (or another source-exact positive functional) in a way that forces the latter to vanish;
2. proves an independent lower/quantization law for the horizontal displacement of any off-line zero, so that even one defect carries a source-incompatible positive quantum;
3. produces a genuinely nonsummable or height-amplifying charge together with a finite source budget, so that the mere existence of an off-line zero eventually contradicts the budget;
4. gives a transform identity whose **exact values**, not merely finiteness, determine the defect and force the zero measure.

Conversely, another construction whose main output is only

\[
0\le \mathfrak D<\infty,
\qquad
\mathfrak D=0\iff\mathrm{RH},
\]

without an independent theorem forcing `mathfrak D=0`, does not by itself advance the defect-elimination objective: BSY already provides such a functional with a stronger linear local tariff.

This also kills a tempting continuation of WI-408. One can form fractional-power same-ordinate gaps such as

\[
(\gamma-id)^u+(\gamma+id)^u-2\gamma^u,
\qquad 0<u<1,
\]

which are positive and, by second-order cancellation, summable like `d^2 gamma^{u-2}`. The construction is exact, but after the prior-art audit it fails the substantive-finding gate as a standalone route: it is weaker near `d=0` than the classical BSY charge and has no better source-side vanishing theorem. It is therefore not pursued as a separate finding.

## 5. Prior-art audit and novelty boundary

The primary classical source is:

- Michel Balazard, Éric Saias and Marc Yor, *Notes sur la fonction zêta de Riemann, 2*, **Advances in Mathematics** 143:2 (1999), 284--287, DOI `10.1006/aima.1998.1797`. This is the source of the integral identity and RH equivalence in (1) and (7).

For an accessible theorem statement, truncation, and independent contour proof:

- H. M. Bui, S. J. Lester and M. B. Milinovich, *On Balazard, Saias, and Yor's equivalence to the Riemann Hypothesis*, **Journal of Mathematical Analysis and Applications** 409:1 (2014), 244--253, DOI `10.1016/j.jmaa.2013.06.063`, arXiv:`1306.0856`. Equation (1.1) is exactly (1); their Theorem 1.2 gives the unconditional truncated zero-sum formula.

Neighboring prior art includes the generalized Littlewood/log-zeta integral criteria of Sekatskii--Beltraminelli--Merlini, which contain BSY and Volchkov-type equalities as special cases. Those families reinforce that positive source-exact RH criteria are classical territory; they do not supply an unconditional proof that the BSY quantity vanishes.

The novelty boundary is deliberately narrow:

- `CLASSICAL-IDENTITY`: equation (1) and the RH equivalence are Balazard--Saias--Yor prior art;
- `LITERATURE+DERIVED`: the comparison with the recent signed-Widder/superzeta branch uses the established BSY formula and WI-405--WI-408;
- `EXACT-DERIVED`: equations (2)--(6), including the exact `artanh` quartet charge, its linear-depth asymptotic, and the elementary absolute-convergence check;
- `PRIOR-ART-REDIRECT`: the line should not spend effort merely constructing another globally summable positive horizontal-defect functional;
- `DECISIVE-NEGATIVE`: density/proportion improvements or finite positive budgets cannot by themselves force the BSY defect to vanish, because one arbitrarily shallow high off-line quartet has arbitrarily small positive charge.

No priority claim is made for BSY, Littlewood-contour criteria, or positive RH-equivalent functionals.

## Consequence

The signed-superzeta branch has now reached a clearer boundary. WI-405--WI-408 correctly identify why fixed power sums and finite exponent jets do not bootstrap to RH, but classical BSY shows that **renormalizing a positive summable horizontal defect is not the core missing theorem**. A stronger such functional has existed since 1999.

The serious next target is source-side: find a theorem linking the Montgomery/Weil inertia data to an exact vanishing mechanism for a positive horizontal defect, with BSY providing a canonical benchmark. Any candidate that only improves summability, positivity, or local sensitivity without supplying that annihilation should be rejected early.