# XF-001 — collision root analyticity fails at the exact backward-heat normal form

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE` for the collision-bridging step in Kevin Schatz, *Riemann Hypothesis: Backward Parabolic Positivity Barriers for the Xi Flow* (2025), DOI `10.5281/zenodo.17636625`, as currently written. This finding does not rule out every possible backward-parabolic approach; it identifies an exact obstruction that any repair must cross.

## 1. Target of the audit

The preprint proposes to propagate

\[
\Im\!\left(-\frac{E_t'(z)}{E_t(z)}\right)\ge 0
\]

backward from a de Bruijn real-zero slice to `t=0`. Its collision stage is load-bearing: Lemma C.1 claims that near a multiple zero `(t_*,z_*)`, the nearby zeros can be labelled by root functions `z_j(t)` that are holomorphic (hence real-analytic on the real time axis) through `t=t_*`; Lemma 7.3 then uses a collision-free energy estimate of the form

\[
|\mathcal E'(t)|\le K\mathcal E(t)
\]

on the interval immediately adjacent to the collision, with `K` depending on the local zero-speed bound, to deduce from `\mathcal E(t_*)=0` that `\mathcal E` vanishes on the other side.

The first assertion is false for backward-heat zero collisions, and the second use of Gronwall loses exactly the uniformity that the false analyticity assertion would have supplied.

## 2. The backward heat equation forces square-root splitting at a double collision

Write the Xi flow locally as `E(t,z)` with

\[
E_t+E_{zz}=0.
\]

Suppose `(t_*,z_*)` is a double zero, so

\[
E(t_*,z_*)=E_z(t_*,z_*)=0,
\qquad A:=E_{zz}(t_*,z_*)\ne0.
\]

The heat equation gives

\[
E_t(t_*,z_*)=-A\ne0.
\]

With `\tau=t-t_*` and `w=z-z_*`, the two-variable Taylor expansion is therefore

\[
E(t,z)
=A\left(\frac{w^2}{2}-\tau\right)
+O\!\left(|w|^3+|\tau||w|+\tau^2\right).
\]

Consequently the two local zero branches have the Puiseux form

\[
w_\pm(\tau)=\pm\sqrt{2\tau}+O(\tau),
\]

up to the choice of square-root branch. In particular,

\[
|\dot z_\pm(t)|\asymp |t-t_*|^{-1/2}.
\]

Thus a generic double collision for the exact Xi-flow PDE is not a crossing of analytic root branches. The heat equation itself makes the collision transverse in time and produces square-root branching.

## 3. An exact matched heat-flow counterexample

The polynomial family

\[
F(t,z)=z^2-2t
\]

solves the same backward heat equation exactly:

\[
F_t+F_{zz}=-2+2=0.
\]

At `t=0` it has a double zero at `z=0`; for `t>0` its zeros are `\pm\sqrt{2t}`, and for `t<0` they are `\pm i\sqrt{-2t}`. Their speeds diverge like `|t|^{-1/2}`.

This also gives a direct algebraic contradiction to the root-labelling step used in Lemma C.1. If there were holomorphic functions `z_1(t),z_2(t)` near `0` with

\[
z^2-2t=(z-z_1(t))(z-z_2(t)),
\qquad z_1(0)=z_2(0)=0,
\]

then coefficient comparison gives `z_1+z_2=0` and `z_1z_2=-2t`, hence

\[
z_1(t)^2=2t.
\]

But the square of a holomorphic function vanishing at `0` has an even-order zero, whereas `2t` has a simple zero. No such holomorphic root functions exist.

The error is the inference that Weierstrass preparation plus factorization of the prepared polynomial produces single-valued holomorphic roots through a multiple-root parameter. Weierstrass preparation gives holomorphic **coefficients** of the local polynomial; its roots generally require Puiseux branching. The example `z^2-2t` already occurs inside the same heat equation, so this is not a generic-complex-analysis control unrelated to the proposed mechanism.

## 4. Why the collision bridge does not follow from the stated energy estimate

The preprint's local speed bound is proved on a **closed collision-free window** by using compactness and a positive minimum pairwise separation. That argument cannot be applied with a finite uniform constant to an interval whose endpoint is a collision. For a double collision, the exact calculation above gives

\[
L_I\gtrsim |t-t_*|^{-1/2}.
\]

The tube estimates and the energy inequality retain this dependence; the paper explicitly records constants containing `L_I^2`. Hence near the collision the effective coefficient is at least of order

\[
L_I^2\asymp |t-t_*|^{-1},
\]

which is not integrable at `t_*`.

Lemma 7.3 nevertheless takes the open interval `I_-=(t_*-\delta,t_*)`, invokes Lemma 7.1 with a single finite constant `K`, and applies endpoint Gronwall. The preceding speed analysis shows that this `K` is not supplied by Lemma 4.7 on such an interval. Continuity of `\mathcal E` at the collision does not repair the gap: an inequality with a nonintegrable coefficient of the form

\[
|\mathcal E'(t)|\le \frac{C}{|t-t_*|}\mathcal E(t)
\]

is compatible with nonzero functions that vanish at the endpoint, for example powers of `|t-t_*|`. Therefore `\mathcal E(t_*)=0` does not force backward vanishing across the collision under the stated estimates.

This is exactly the singular regime that collision bridging was supposed to handle.

## 5. What survives and what would constitute a repair

The local bounds for the logarithmic derivative itself may still be recoverable from the symmetric Weierstrass polynomial without analytically labelling the individual roots. The decisive problem is the **time derivative of a tube that follows the zero set**: a branch-Lipschitz bound necessarily sees the square-root speed singularity.

A repair must therefore avoid assuming bounded zero speed up to a collision. Plausible theorem-level repair targets are:

- build the tube from symmetric polynomial/discriminant data whose time derivative stays controlled through the Puiseux collision;
- derive an energy inequality with coefficient `K(t)` integrable at `t_*` despite `|\dot z|\asymp |t-t_*|^{-1/2}`;
- or prove a collision-local uniqueness/positivity statement directly from the two-variable normal form, without passing through branchwise Lipschitz motion.

The repair test is strict: starting with the exact local model `z^2-2t`, the proposed collision weight and energy estimate must remain valid with constants strong enough to propagate zero negative energy from one side to the other. Any mechanism that still requires `\sup |\dot z_j|<\infty` on an interval reaching the collision fails this test.

## 6. Prior-art and evidence boundary

The audited preprint is an unreviewed RH proof claim, not accepted evidence for `Lambda=0`. The counterargument here is self-contained and uses only the backward heat equation and elementary local analytic algebra. No novelty is claimed for Puiseux branching of roots of analytic polynomial families or for the fact that Weierstrass preparation does not generally produce holomorphic root labels.

The durable Mathia result is the source-specific localization of the failure: **double collisions in the Xi-flow PDE necessarily create the square-root speed singularity that invalidates the preprint's analytic-root lemma and removes the finite endpoint Gronwall constant used by its collision bridge.** Until a replacement collision argument passes the exact `z^2-2t` control, the claimed backward positivity propagation and resulting RH conclusion are unsupported.

## 7. Consequence for `xi_flow`

This identifies an early line-specific falsification control for future dynamical proofs. Collision singularities are not a technical nuisance that can be bypassed by analytic relabelling; the backward heat equation fixes their leading local geometry. Any useful Xi-flow Lyapunov, tube, entropy, or barrier construction must be formulated in variables that survive square-root branching or explicitly cancel its nonintegrable speed cost.
