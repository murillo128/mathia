---
id: WP-355
title: Bi-invariant Randers positivity carries central orientation only as a free closed boundary term
branch: weil_positivity
status: supported
kind: bi-invariant-finsler-central-orientation-boundary-term-no-go
claim_strength: exact central-line classification plus explicit bi-invariant Randers matched control and closed-one-form reduction
created: 2026-09-18
related: [WP-171, WP-345, WP-351, WP-352, WP-353, WP-354]
clues: [CLUE-maass-selberg-remainder-sign-interface]
prior_art:
  - classical Randers/Minkowski norm construction
  - Dariush Latifi, Bi-invariant Randers metrics on Lie groups, Publ. Math. Debrecen 76 (2010), 219-226, DOI 10.5486/PMD.2010.4558
  - Dariush Latifi and Megerdich Toomanian, On the existence of bi-invariant Finsler metrics on Lie groups, Math. Sci. 7 (2013), 37, DOI 10.1186/2251-7456-7-37
  - classical fact that adding a closed one-form to a Finsler/Riemannian length leaves fixed-endpoint local geodesics projectively unchanged
---

# WP-355 — Bi-invariant Randers positivity carries central orientation only as a free closed boundary term

## Claim

`WP-354` leaves nonquadratic/Finsler geometry open because a non-reversible Finsler norm need not identify a tangent vector with its negative. That escape is real but does not by itself solve the sign problem. On a unitary scattering space, conjugation-invariant Finsler positivity can retain the orientation of the scalar determinant phase, but the orientation enters as a free asymmetry parameter. In the canonical Randers realization it is exactly a closed determinant-phase one-form, hence a boundary/topological term rather than a sign forced by the positive bulk geometry.

Let

\[
U(t)\in U(m),\qquad Q_U=-iU^*\dot U\in\operatorname{Herm}(m).
\tag{1}
\]

Define the Hilbert--Schmidt norm and normalized central functional

\[
\alpha(H)=\sqrt{\operatorname{tr}(H^2)},\qquad
\beta(H)=\frac{\operatorname{tr}H}{\sqrt m}.
\tag{2}
\]

Cauchy--Schwarz gives `|beta(H)|<=alpha(H)`. Therefore for every `|epsilon|<1`,

\[
\boxed{F_\epsilon(H)=\alpha(H)+\epsilon\beta(H)}
\tag{3}
\]

is a strongly convex Randers/Minkowski norm. Both `alpha` and `beta` are invariant under unitary conjugation, so (3) defines a bi-invariant Finsler metric on `U(m)`.

Unlike the quadratic metrics of `WP-354`, (3) sees the orientation of the center:

\[
F_\epsilon(qI)=\sqrt m\bigl(|q|+\epsilon q\bigr).
\tag{4}
\]

But positivity does not select that orientation. Reversal gives another equally admissible positive bi-invariant Finsler metric,

\[
F_\epsilon(-H)=F_{-\epsilon}(H),
\tag{5}
\]

with exactly the opposite central bias. More generally, **every** Minkowski norm `F` restricted to the central line has the form

\[
\boxed{F(qI)=c|q|+dq,\qquad c>|d|,}
\tag{6}
\]

where

\[
c=\frac{F(I)+F(-I)}2,
\qquad
d=\frac{F(I)-F(-I)}2.
\tag{7}
\]

Thus non-reversibility can store a signed scalar phase, but the Finsler positivity axioms constrain only `|d|<c`; they do not determine the sign of `d`.

For the explicit family (3) the odd term is even more rigid. Along `U(m)`,

\[
\beta(Q_U)\,dt
=-\frac{i}{\sqrt m}\operatorname{tr}(U^*dU)
=\frac1{\sqrt m}\,d\arg\det U
\tag{8}
\]

locally, and globally it is a closed one-form with periods `2pi/sqrt(m)` times the determinant winding number. Hence the Finsler length is

\[
L_\epsilon(U)
=\int\alpha(Q_U)\,dt
+\frac{\epsilon}{\sqrt m}\,\Delta\arg\det U,
\tag{9}
\]

on a chosen lift, with the second term fixed by endpoints and homotopy class. It does not alter the fixed-endpoint local geodesic equation. The two metrics `F_epsilon` and `F_{-epsilon}` therefore have the same reversible Hilbert--Schmidt core and the same local unparameterized geodesics, while carrying opposite oriented determinant-phase boundary terms.

This is a sharp matched control for the Finsler escape. A positive non-reversible metric can **contain** the scalar logarithmic derivative that appears linearly in the Maaß--Selberg/scattering explicit-formula interface, but its positivity yields only a domination bound of the form

\[
\epsilon\beta(H)\ge -\alpha(H),
\tag{10}
\]

not a sign for `beta(H)`. Isolating the oriented term requires subtracting the positive reversible part, or equivalently comparing the metric with its reverse; either operation is a difference of positive quantities and loses the sign theorem. Therefore ordinary bi-invariant Finsler positivity does not convert the scalar scattering phase into Weil positivity merely by permitting non-reversibility.

**Classification:** `EXACT-DERIVED + FINSLER-CENTRAL-LINE-CLASSIFICATION + BI-INVARIANT-RANDERS-CONTROL + CLOSED-DETERMINANT-ONE-FORM + ORIENTATION-FREE-PARAMETER + SAME-GEODESIC-CORE-CONTROL + POSITIVE-REMAINDER-PERSISTS + PRIOR-ART-CLASSICALIZATION + DECISIVE-NARROWING + NOT-A-WEIL-BRIDGE`.

## 1. Any Finsler norm has a free two-slope central restriction

Let `F` be any Minkowski norm on `Herm(m)`. Positive homogeneity is only required for positive scalars. Hence for `q>0`,

\[
F(qI)=qF(I),
\tag{11}
\]

while for `q<0`,

\[
F(qI)=(-q)F(-I).
\tag{12}
\]

Equations (11)--(12) are exactly (6)--(7). Since a Minkowski norm is positive away from zero,

\[
F(I)>0,\qquad F(-I)>0,
\tag{13}
\]

which is equivalent to `c>|d|`.

This observation is independent of conjugation invariance; the center is fixed pointwise by conjugation anyway. Consequently no amount of `Ad(U(m))` invariance can determine the sign of the odd coefficient `d`. The reverse norm

\[
F^{\mathrm{rev}}(H):=F(-H)
\tag{14}
\]

is again a Minkowski norm, is conjugation invariant whenever `F` is, and changes `d` to `-d` while leaving `c` unchanged.

So the precise difference from `WP-354` is now clear. Quadratic/Riemannian invariance forces `d=0` and erases central orientation. General Finsler geometry allows `d\ne0`, but positivity and conjugation invariance leave its sign as an additional datum. The escape exists informationally, not as a positivity theorem.

## 2. Randers metrics realize the ambiguity inside bi-invariant geometry

For (2), Hilbert--Schmidt Cauchy--Schwarz gives

\[
|\operatorname{tr}H|
=|\operatorname{tr}(IH)|
\le \sqrt{\operatorname{tr}(I^2)}\sqrt{\operatorname{tr}(H^2)}
=\sqrt m\,\alpha(H),
\tag{15}
\]

so the dual norm of `beta` with respect to `alpha` is one. The standard Randers criterion therefore makes `F_epsilon=alpha+epsilon beta` a Minkowski norm whenever `|epsilon|<1`.

Both terms satisfy

\[
\alpha(V^*HV)=\alpha(H),\qquad
\beta(V^*HV)=\beta(H),
\tag{16}
\]

for every `V in U(m)`. A left-invariant Finsler metric whose identity norm is `Ad`-invariant is also right-invariant. Thus (3) is genuinely bi-invariant, not merely a coordinate perturbation of the Riemannian example in `WP-354`.

On `H=qI`, equations (2) give

\[
\alpha(qI)=\sqrt m|q|,
\qquad
\beta(qI)=\sqrt m q,
\tag{17}
\]

and hence (4). The two slopes are `sqrt(m)(1+epsilon)` and `sqrt(m)(1-epsilon)`, both positive. Replacing `epsilon` by `-epsilon` preserves every structural hypothesis just used while reversing the signed central preference.

The symmetrized norm is independent of that preference:

\[
\frac{F_\epsilon(H)+F_\epsilon(-H)}2=\alpha(H).
\tag{18}
\]

Thus the entire orientation-sensitive addition disappears under metric symmetrization, while the reversible positive core stays fixed.

## 3. The odd Randers term is the determinant-phase one-form

For a differentiable unitary path, Jacobi's determinant identity gives

\[
\frac{d}{dt}\log\det U(t)
=\operatorname{tr}\bigl(U(t)^*\dot U(t)\bigr).
\tag{19}
\]

Using `Q_U=-iU^*dot U`,

\[
\beta(Q_U)
=-\frac{i}{\sqrt m}\frac{d}{dt}\log\det U.
\tag{20}
\]

Writing locally `det U=e^{i theta}` turns (20) into

\[
\beta(Q_U)=\frac{\dot\theta}{\sqrt m}.
\tag{21}
\]

The corresponding invariant one-form

\[
\omega_\det=-\frac{i}{\sqrt m}\operatorname{tr}(U^*dU)
\tag{22}
\]

is closed because it is locally `d theta/sqrt(m)`. Around a loop its integral is

\[
\oint\omega_\det=\frac{2\pi}{\sqrt m}\,\operatorname{wind}(\det U).
\tag{23}
\]

Therefore the odd contribution to the Randers action is a boundary term on a local lift and a homotopy invariant globally. For variations with fixed endpoints inside a fixed homotopy class its first variation vanishes. This is the standard closed-one-form mechanism behind the projective equivalence of a Randers metric `alpha+beta` with its reversible part when `beta` is closed.

In particular, allowing non-reversibility does not make the determinant phase interact dynamically with the traceless channel geometry in this canonical family. It appends the oriented scalar phase to an independently positive bulk length.

## 4. Positivity gives the same kind of remainder bound, not the desired sign

The Randers inequality itself is

\[
0<F_\epsilon(H)=\alpha(H)+\epsilon\beta(H)
\qquad(H\ne0).
\tag{24}
\]

For `epsilon>0`, rearranging gives

\[
\beta(H)>-\frac{\alpha(H)}{\epsilon},
\tag{25}
\]

and for `epsilon<0` the inequality reverses after division. Neither case forces `beta(H)` to have a fixed sign. The matched norm with `-epsilon` supplies the opposite one-sided inequality with the same positive core.

To extract the signed central term one may antisymmetrize:

\[
F_\epsilon(H)-F_\epsilon(-H)=2\epsilon\beta(H).
\tag{26}
\]

But (26) is a difference of two positive lengths. Nonnegativity of each side separately says nothing about the sign of the difference. This is the Finsler analogue of the polarization obstruction in `WP-354`.

The relevance to the Maaß--Selberg clue is direct. There the positive global object already gives the desired oriented scattering/zero term together with a signed or positive remainder. Equation (24) shows why simply moving from a reversible quadratic metric to a non-reversible positive norm does not remove that structural gap: the odd linear readout becomes visible only while accompanied by a dominating even term. Removing the even term discards the positivity theorem.

## 5. Prior-art and novelty audit

The underlying geometry is classical. Randers norms `alpha+beta` with `||beta||_alpha<1` are standard Finsler metrics; bi-invariant Finsler metrics on compact Lie groups are classically obtained from `Ad`-invariant Minkowski norms. Latifi's work on bi-invariant Randers metrics and Latifi--Toomanian's treatment of bi-invariant Finsler metrics provide direct prior-art anchors. It is also standard that adding a closed one-form to a length functional changes it by an endpoint/homotopy term and leaves local fixed-endpoint geodesics projectively unchanged.

No new theorem in Finsler geometry is claimed. The Mathia-specific contribution is the branch-level matched control: the exact nonquadratic escape explicitly left open by `WP-354` does retain the oriented determinant phase, but it does so through a free reversible-asymmetry parameter, and in the canonical Randers realization that parameter multiplies precisely the closed determinant-phase one-form. The same positive bulk geometry supports both orientations.

This differs materially from `WP-351`, where contraction-defect positivity is blind to unimodular scalar phase, and from `WP-354`, where quadratic metric positivity sees only an even square of that phase. Finsler positivity can see the sign, but the sign is **chosen by the norm**, not forced by its positivity.

## 6. Consequence and surviving route

This finding does not exclude a source-defined non-reversible Finsler metric whose asymmetry is fixed by additional arithmetic geometry. It shows what such a proposal must prove: the source must canonically select the odd central orientation and its coefficient, and that selection must be independent of the target Weil sign rather than a restatement of the completed-zeta logarithmic derivative.

Nor does the result classify all conjugation-invariant Finsler couplings between central and traceless directions. A nonlinear invariant norm can couple them. But the universal central-line lemma (6) means that positivity plus invariance alone can never select the orientation even before those couplings are studied; reversal remains an equally positive invariant control.

The viable frontier after `WP-354`--`WP-355` is therefore narrower: a successful finite-channel nonquadratic construction must contain a **source-forced irreversibility theorem**, not merely a non-reversible norm. Alternatively the sign must come from a genuine operator-order statement, a global multi-spectral form, or an infinite-dimensional/adelic/cohomological coupling before reduction to a pointwise unitary metric. In each case the orientation must be derived from the source geometry and survive a reversal control, rather than being supplied as the free odd part of a positive functional.
