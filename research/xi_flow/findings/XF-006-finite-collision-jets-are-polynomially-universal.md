# XF-006 — finite collision jets are polynomially universal at a real-rooted threshold

**Status:** `EXACT-DERIVED` + `CLASSICAL-APPROXIMATION` + `NEGATIVE/OBSTRUCTION`. Laguerre--Pólya approximation by real-rooted polynomials and preservation of real-rootedness by backward polynomial heat flow are classical. The line-specific obstruction is that, at a hypothetical simple Xi-flow threshold collision, every finite local heat-flow jet can be approximated arbitrarily well by finite real-rooted polynomial controls whose de Bruijn--Newman transition occurs at that same collision. Consequently no robust selector depending only on finitely many local collision derivatives can distinguish the Xi flow from matched positive-transition controls.

## 1. Claim

Work in the Xi normalization

\[
\partial_t H_t=-\partial_{zz}H_t.
\]

Suppose a candidate transition slice `t=t_*` is real-rooted and contains an isolated simple double zero `z_* != 0`,

\[
H_{t_*}(z_*)=H'_{t_*}(z_*)=0,
\qquad H''_{t_*}(z_*)\ne0,
\]

with all other zeros real. Put `F(z)=H_{t_*}(z)` and let `D_H(\tau)` denote the analytic local discriminant of the colliding pair for `H_{t_*+\tau}` as in XF-002.

Then for every finite integer `M>=1` and every `epsilon>0` there is a finite real-rooted polynomial `P` with the same simple double zero `z_*` such that, for the exact polynomial backward-heat family

\[
P_\tau(z):=e^{-\tau\partial_z^2}P(z),
\]

all of the following hold:

1. every zero of `P_\tau` is real for `\tau>=0`;
2. the local pair issuing from `z_*` is nonreal for all sufficiently small `\tau<0`, so the polynomial transition time relative to the collision is exactly `0`;
3. if `D_P(\tau)` is the local discriminant of that pair, then

\[
\boxed{
\max_{1\le r\le M}
\left|D_P^{(r)}(0)-D_H^{(r)}(0)\right|<\epsilon.
}
\]

The same approximation holds for any fixed finite jet of the full local Weierstrass quadratic factor, not only its discriminant.

Therefore a **strict, continuous, time-translation-invariant criterion based on only finitely many local collision derivatives cannot be Xi-specific**. Any such criterion that holds with nonzero margin for the Xi collision is reproduced by a sufficiently large polynomial control. Shifting the control's time coordinate places its transition at any prescribed absolute value, including a positive one.

This does not rule out an invariant using the whole zero configuration, a macroscopic interval of heat time, an infinite tail of normalized fields, or a nonlocal statistic whose information is not continuous in a finite collision jet.

## 2. Real-rooted polynomial controls approximate the threshold germ

On an all-real slice the even real entire function `F` lies in the Laguerre--Pólya regime relevant to de Bruijn--Newman theory. Equivalently for the present argument, its paired Hadamard product may be ordered symmetrically as

\[
F(z)=C z^{2m}
\prod_{\gamma>0}
\left(1-\frac{z^2}{\gamma^2}\right)^{m_\gamma},
\]

where the positive zeros `\gamma` are repeated according to multiplicity. Pairing `+\gamma` with `-\gamma` removes the genus-one exponential terms, and the inverse-square zero tail converges. The standard fixed-`t` zero-counting law gives the required `\sum \gamma^{-2}<\infty`.

Choose symmetric partial products `P_N` that include the double factor at `\pm z_*`. Then every `P_N` has only real zeros, preserves the exact multiplicity-two zero at `z_*`, and

\[
P_N\longrightarrow F
\]

locally uniformly in `z`. By Cauchy's formula, for every fixed `K`,

\[
P_N^{(k)}(z_*)\longrightarrow F^{(k)}(z_*)
\qquad(0\le k\le K).
\]

This is the classical Laguerre--Pólya approximation mechanism specialized to the actual threshold zero set rather than an arbitrary polynomial fit. It preserves the collision and approximates its surrounding analytic germ without importing nonreal control zeros.

## 3. The polynomial control has a genuine transition at the collision

For a polynomial the operator exponential terminates, so

\[
P_{N,\tau}(z)
=e^{-\tau\partial_z^2}P_N(z)
=
\sum_{k\ge0}\frac{(-\tau)^k}{k!}P_N^{(2k)}(z)
\]

is an exact polynomial solution of the same backward heat equation.

The Pólya--Benz real-zero-preserver theorem implies that `e^{-\tau\partial_z^2}` maps a real-rooted polynomial to a real-rooted polynomial for every `\tau>=0`. Thus the full finite zero set is real on the forward side.

At `\tau=0`, however, `z_*` is a simple double collision. XF-002 is purely local and applies equally to this polynomial family, giving

\[
D_{P_N}(0)=0,
\qquad
D_{P_N}'(0)=8.
\]

Hence

\[
D_{P_N}(\tau)=8\tau+O(\tau^2),
\]

so the pair is nonreal for every sufficiently small negative `\tau`. Because real-rootedness under backward heat is hereditary in increasing `\tau`, the polynomial cannot become fully real at an earlier negative time and then lose that property again before `0`. Its transition set is therefore exactly `\tau>=0`.

This is a matched control in the precise sense required by the line README: it obeys the same heat equation, has a real-rooted forward regime, crosses through the same type of collision, but carries no Xi arithmetic. A time shift `\tau=t-L` gives an otherwise identical control with transition constant `L`, so local collision geometry cannot encode the absolute sign of a de Bruijn--Newman constant.

## 4. Every finite heat-flow jet is inherited from finitely many spatial derivatives

The heat equation makes the jet comparison exact. At the collision slice,

\[
\partial_\tau^a\partial_z^b H_{t_*+\tau}(z_*)\big|_{\tau=0}
=(-1)^a F^{(2a+b)}(z_*),
\]

while

\[
\partial_\tau^a\partial_z^b P_{N,\tau}(z_*)\big|_{\tau=0}
=(-1)^a P_N^{(2a+b)}(z_*).
\]

Thus any prescribed finite joint `(\tau,z)` jet of the polynomial family converges coefficientwise to the corresponding Xi-flow jet.

Near a simple double zero, Weierstrass preparation writes either family uniquely as

\[
U(\tau,w)
\bigl(w^2+b(\tau)w+c(\tau)\bigr),
\qquad w=z-z_*,
\]

with `U(0,0) != 0`. Recursive coefficient comparison shows that every fixed derivative of `b`, `c`, and

\[
D=b^2-4c
\]

at `\tau=0` depends continuously on only finitely many derivatives of the ambient heat-flow germ; the only local denominator is controlled by the nonzero quadratic coefficient `F''(z_*)`. Therefore local-uniform convergence of `P_N` upgrades to

\[
D_{P_N}^{(r)}(0)\longrightarrow D_H^{(r)}(0)
\]

for every fixed `r`, proving the stated finite-jet approximation.

XF-003 and XF-005 are the first terms of this hierarchy. The universal value `D'(0)=8` is matched exactly. The curvature `D''(0)=-32S_*` is matched because the truncated exterior inverse-square field converges to `S_*`. Higher collision derivatives merely expose further finite combinations of the same analytic germ; truncating farther out reproduces them to any prescribed finite accuracy.

## 5. The resulting no-go statement

Consider a proposed local barrier expressed as

\[
\mathcal B\bigl(J_M(H,t_*,z_*)\bigr)>0,
\]

where `J_M` is any finite collision jet and `\mathcal B` is continuous in its finite-dimensional arguments. If the inequality holds for the Xi germ with margin `eta>0`, then sufficiently large polynomial controls satisfy the same inequality because their jets converge to the Xi jet.

Such a barrier therefore cannot, by itself, prove that the Xi transition is forced to occur at `t<=0`: the identical local statement is available after time translation for a finite control with transition at any `L>0`. This includes proposed selectors built from finitely many values among

\[
D'(0),D''(0),\ldots,D^{(M)}(0),
\]

or equivalently finitely many local derivatives of the gap, center, exterior field, or normalized coordinate `R=qS`, provided the expression extends continuously through the collision-safe variables.

The qualification **strict and continuous** matters. An exact identity defining a closed, infinite-codimension subclass need not survive approximation, and a criterion whose input includes infinitely many derivatives or a nonlocal norm is outside the claim. The result rules out robust finite local signatures, not every conceivable analytic invariant.

## 6. Why this is stronger than a generic matched-control warning

The README already requires testing against synthetic real-entire controls. XF-003 showed one explicit four-body control and XF-005 warned that `R` itself is universal. The present result is stronger: **no finite extension of the collision Taylor expansion repairs that problem**.

One might hope that `R'`, `R''`, a higher discriminant coefficient, or several neighboring-gap derivatives eventually reveal Xi arithmetic. For every fixed order, however, a sufficiently long real-zero truncation reproduces the same local jet while retaining an independently movable transition time. The failure is therefore structural rather than a bad choice of the first one or two collision coordinates.

This also explains why a finite-particle theorem can still be useful without being a selector. Finite controls are excellent for checking exact algebra, signs, and candidate inequalities. What they cannot supply by themselves is an Xi-specific local threshold certificate unless the argument carries a uniform-in-degree quantity that survives the infinite limit and is not determined by a fixed finite jet.

## 7. Prior-art and novelty boundary

The underlying approximation statement is classical Laguerre--Pólya theory: real entire functions in that class are locally uniform limits of real-rooted polynomials. Theodoros Assiotis, **Random Entire Functions from Random Polynomials with Real Zeros**, *Advances in Mathematics* 410 (2022), 108701, gives a modern convergence framework and explicitly treats the Laguerre--Pólya class as this locally uniform closure.

Real-root preservation under polynomial backward heat is also classical. Alexandru Aleman, Dmitry Beliaev and Håkan Hedenmalm, **Real zero polynomials and Pólya--Schur type theorems**, *Journal d'Analyse Mathématique* 94 (2004), 49--60, analyze real-zero-preserving differential operators. Brian Hall and Ching-Wei Ho, **The heat flow conjecture for polynomials and random matrices**, *Letters in Mathematical Physics* 115 (2025), article 60, explicitly invoke the Pólya--Benz theorem for the fact that polynomial backward heat preserves all-real roots. Zakhar Kabluchko's 2025 work on backward heat flow of high-degree real-rooted polynomials supplies contemporary finite-particle context.

No novelty is claimed for Laguerre--Pólya approximation, polynomial heat flow, or real-root preservation. The Mathia-specific result is their use as a falsification theorem for the Xi-flow program: after combining the exact collision discriminant from XF-002 with polynomial approximation, every finite collision jet becomes a reproducible matched-control feature and therefore cannot be a robust Xi-specific upper-bound selector.

## 8. Boundary conditions and consequence for `xi_flow`

The argument is conditional on a **simple multiplicity-two threshold collision**. A hypothetical transition realized only through a limiting collision at unbounded height, an accumulation mechanism, or higher multiplicity is not covered by this local normal form. The result also does not claim that partial-product heat flows approximate the Xi flow uniformly on a fixed nonzero time interval. Backward heat is unstable enough that convergence of initial entire functions alone is not a license for such an interchange; only finite derivatives at the collision slice are used here.

Nor does the argument show that an arbitrary whole trajectory of `R(t)` can be replicated by one finite control. XF-005's time-integrated equilibrium deficit therefore remains a live object precisely when its control requires information over a time interval or from the infinite zero tail.

The research frontier is consequently sharper. **Higher finite collision jets are a dead end as selectors.** A viable upper-bound mechanism must use information that cannot be compressed into a fixed local Taylor jet: for example a height-uniform statistical law, a macroscopic-time integral with controlled tails, an infinite-dimensional energy, or an unconditional correlation constraint imported from `analytic_frontier`. Any proposed finite-particle approximation must carry such a quantity with a degree-uniform error estimate before it can discriminate Xi from the polynomial controls constructed here.