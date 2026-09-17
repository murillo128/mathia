---
id: WP-354
title: Bi-invariant unitary scattering metrics orthogonally split the scalar phase from noncentral directions
branch: weil_positivity
status: supported
kind: bi-invariant-scattering-metric-center-splitting-no-go
claim_strength: exact compact-Lie-algebra classification plus Wigner-Smith specialization and orientation matched control
created: 2026-09-17
related: [WP-171, WP-244, WP-245, WP-348, WP-350, WP-351, WP-352, WP-353]
clues: [CLUE-maass-selberg-remainder-sign-interface]
prior_art:
  - classical classification of Ad-invariant inner products on compact reductive Lie algebras and bi-invariant Riemannian metrics
  - John Milnor, Curvatures of left invariant metrics on Lie groups, Adv. Math. 21 (1976), 293-329, DOI 10.1016/S0001-8708(76)80002-3
  - Felix T. Smith, Lifetime Matrix in Collision Theory, Phys. Rev. 118 (1960), 349-356, DOI 10.1103/PhysRev.118.349
---

# WP-354 — Bi-invariant unitary scattering metrics orthogonally split the scalar phase from noncentral directions

## Claim

`WP-353` leaves a specific route open: retain the scalar completed-zeta phase inside a larger noncentral scattering object **before** scalarization, and hope that a canonical positive geometry on that larger object couples the scalar arithmetic to the matrix directions strongly enough to produce the Weil sign.

The most canonical finite-dimensional version of that idea — a conjugation-invariant positive quadratic metric on a unitary scattering family — cannot provide such a coupling. Let

\[
U(t)\in U(m),\qquad
Q_U(t):=-iU(t)^*\dot U(t)\in\operatorname{Herm}(m),
\tag{1}
\]

and let `B` be any real symmetric positive-semidefinite bilinear form on `Herm(m)` invariant under unitary conjugation,

\[
B(V^*HV,V^*KV)=B(H,K)
\qquad(V\in U(m)).
\tag{2}
\]

For `m>=2`, every such form has the exact shape

\[
\boxed{
B(H,K)
=a\,\operatorname{tr}(H_0K_0)
+b\,\operatorname{tr}(H)\operatorname{tr}(K),
\qquad a,b\ge0,
}
\tag{3}
\]

where

\[
H_0=H-\frac{\operatorname{tr}H}{m}I.
\tag{4}
\]

Thus the center and the traceless `SU(m)` directions are forced to be orthogonal by the same invariance that makes the metric canonical.

If the scattering family factors on the critical line as

\[
U(t)=g(t)R(t),\qquad |g(t)|=1,
\tag{5}
\]

with scalar phase velocity

\[
q_g(t):=-i g(t)^{-1}\dot g(t)\in\mathbb R,
\tag{6}
\]

then

\[
Q_U=q_g I+Q_R,
\qquad
Q_R=-iR^*\dot R,
\tag{7}
\]

and (3) gives

\[
\boxed{
B(Q_U,Q_U)
=a\,\operatorname{tr}\big((Q_R)_0^2\big)
+b\big(mq_g+\operatorname{tr}Q_R\big)^2.
}
\tag{8}
\]

The scalar arithmetic can therefore enter a bi-invariant positive quadratic energy only through the **square of the total determinant-phase velocity**. It has no cross term with the genuinely noncentral traceless scattering directions.

Equivalently, after the intrinsic local factorization into center and determinant-one parts,

\[
U(t)=e^{i\psi(t)}\widehat R(t),
\qquad \widehat R(t)\in SU(m),
\tag{9}
\]

one has

\[
B(Q_U,Q_U)
=a\,\operatorname{tr}(Q_{\widehat R}^2)
+b m^2\dot\psi(t)^2.
\tag{10}
\]

Hence the positive metric is exactly insensitive to the **orientation** of the central phase. The matched paths

\[
U_+(t)=e^{i\psi(t)}\widehat R(t),
\qquad
U_-(t)=e^{-i\psi(t)}\widehat R(t)
\tag{11}
\]

have identical noncentral dynamics and identical value of every energy (3), while their determinant-phase velocities have opposite sign.

This is decisive for the direct finite-channel Riemannian escape. In the Maaß--Selberg/scattering interface used throughout `WP-345`--`WP-353`, the scalar logarithmic derivative enters the explicit-formula side **linearly and with orientation**. A positive bi-invariant quadratic metric can either ignore the central direction (`b=0`) or square it (`b>0`); it cannot use the traceless channel geometry to turn that oriented linear scalar term into positivity.

The result does **not** rule out a source-defined metric that breaks conjugation invariance, a nonquadratic/Finsler functional, an operator-order theorem such as `Q_U\succeq0`, an infinite-dimensional/categorical coupling, or a global form acting on several spectral parameters before reduction to a pointwise unitary metric. It does show that merely retaining the zeta scalar inside a finite unitary matrix and equipping that matrix with its natural invariant positive Riemannian geometry does not realize the surviving route of `WP-353`.

**Classification:** `EXACT-DERIVED + COMPACT-LIE-ALGEBRA-CLASSIFICATION + WIGNER-SMITH-SPECIALIZATION + CENTER-SEMISIMPLE-ORTHOGONALITY + CENTRAL-ORIENTATION-CONTROL + FINITE-CHANNEL-RIEMANNIAN-NO-GO + PRIOR-ART-CLASSICALIZATION + DECISIVE-NARROWING + NOT-A-WEIL-BRIDGE`.

## 1. Conjugation invariance forces center/traceless orthogonality

Work on the real vector space `Herm(m)`. Every `H` has the canonical decomposition

\[
H=hI+H_0,
\qquad
h=\frac{\operatorname{tr}H}{m},
\qquad
\operatorname{tr}H_0=0.
\tag{12}
\]

Let `dV` be normalized Haar measure on `U(m)`. For traceless `H_0`, Schur averaging gives

\[
\int_{U(m)}V^*H_0V\,dV
=\frac{\operatorname{tr}H_0}{m}I
=0.
\tag{13}
\]

Because `I` is fixed by conjugation and `B` is invariant,

\[
\begin{aligned}
B(I,H_0)
&=\int_{U(m)}B(I,V^*H_0V)\,dV\\
&=B\!\left(I,\int_{U(m)}V^*H_0V\,dV\right)
=0.
\end{aligned}
\tag{14}
\]

So the center `R I` is orthogonal to all traceless Hermitian matrices for **every** conjugation-invariant symmetric form, before positivity is used.

Multiplication by `i` identifies the traceless Hermitian matrices with the compact simple Lie algebra `su(m)`. For `m>=2`, every invariant symmetric bilinear form on this simple factor is a scalar multiple of its Killing form, equivalently of the Hilbert--Schmidt form `tr(H_0K_0)`. On the one-dimensional center an invariant symmetric form is arbitrary. This proves (3) for some real `a,b`; positive semidefiniteness forces

\[
a\ge0,\qquad b\ge0.
\tag{15}
\]

For `m=1` only the central term remains, so the conclusion is even simpler: an invariant quadratic metric can only see the square of the scalar phase velocity.

This is the classical classification of bi-invariant Riemannian metrics on a compact reductive group specialized to `U(m)`. The Lie-theoretic theorem is not new; its role here is to test whether the canonical metric geometry of the enlarged scattering object supplies the missing arithmetic coupling.

## 2. Wigner--Smith velocity makes the arithmetic split explicit

For a differentiable unitary family, Smith's scattering lifetime/time-delay matrix is, up to the standard left/right convention,

\[
Q_U=-iU^*\dot U.
\tag{16}
\]

It is Hermitian because differentiation of `U^*U=I` gives

\[
\dot U^*U+U^*\dot U=0.
\tag{17}
\]

Now insert the scalar/noncentral factorization (5):

\[
\begin{aligned}
U^*\dot U
&=R^*\bar g\,(\dot g R+g\dot R)\\
&=g^{-1}\dot g\,I+R^*\dot R,
\end{aligned}
\tag{18}
\]

which proves (7). Its traceless part is

\[
(Q_U)_0=(Q_R)_0,
\tag{19}
\]

while its center is determined by the total determinant phase,

\[
\frac1m\operatorname{tr}Q_U
=q_g+\frac1m\operatorname{tr}Q_R
=-\frac{i}{m}\frac{d}{dt}\log\det U.
\tag{20}
\]

Substituting (19)--(20) into (3) gives (8).

This formula identifies exactly what an invariant positive metric can and cannot do. It **can** assign independent positive weights to total central motion and traceless channel motion. It **cannot** create a bilinear term between them. Any apparent center/traceless coupling obtained after a basis-dependent coordinate choice disappears when the canonical decomposition (12) is restored.

For the squarefree congruence setting of `WP-348`--`WP-350`, the common completed-zeta scattering factor is precisely a scalar multiplier of the finite cusp scattering matrix. Equation (8) therefore applies without changing the arithmetic factorization: enlarging from the scalar coefficient to the full finite cusp matrix does not by itself make the common zeta phase interact with the traceless channel geometry inside any bi-invariant quadratic metric.

## 3. The orientation matched control kills the hoped-for linear readout

The determinant-one factorization (9) exists locally along every differentiable unitary path: choose a local phase `psi` with

\[
e^{im\psi(t)}=\det U(t),
\tag{21}
\]

and put `\widehat R=e^{-i\psi}U`. Then `det \widehat R=1` and

\[
\operatorname{tr}Q_{\widehat R}=0.
\tag{22}
\]

For the two paths (11),

\[
Q_+=\dot\psi I+Q_{\widehat R},
\qquad
Q_-=-\dot\psi I+Q_{\widehat R}.
\tag{23}
\]

Using (3) and (22),

\[
\boxed{
B(Q_+,Q_+)=B(Q_-,Q_-)
=a\operatorname{tr}(Q_{\widehat R}^2)+bm^2\dot\psi^2.
}
\tag{24}
\]

But

\[
-i\frac{d}{dt}\log\det U_+
=+m\dot\psi,
\qquad
-i\frac{d}{dt}\log\det U_-
=-m\dot\psi.
\tag{25}
\]

So the complete class of invariant positive quadratic energies has an exact matched control with the same noncentral motion and opposite oriented central logarithmic derivative.

If one additionally wants critical-line reciprocity, choose `psi` odd and a determinant-one path satisfying `\widehat R(-t)=\widehat R(t)^*`; then both `U_+` and `U_-` obey the same unitary reversal relation. The control is therefore not an artifact of abandoning the basic real-axis scattering symmetry. It need not, and does not, claim that both paths are the same arithmetic automorphic scattering matrix. Its purpose is narrower: the **metric positivity theorem itself** contains no orientation selector for the central phase. Any arithmetic rule selecting one orientation is additional source structure whose role must be proved separately.

This differs from `WP-351`, where contraction-defect positivity was completely blind to scalar unimodular phase. Here the invariant metric does see central motion, but only through an even quadratic quantity. It also differs from `WP-352`--`WP-353`, which classify scalar gauge/curvature information. The new obstruction is the orthogonal splitting forced when one tries to rescue the scalar by embedding it in a larger finite-dimensional unitary geometry.

## 4. Why polarization does not restore a positive Weil mechanism

Because `B` is bilinear, one can recover the signed center by pairing with the central direction. For example,

\[
B(Q_U,I)=bm\,\operatorname{tr}Q_U.
\tag{26}
\]

Likewise, polarization writes this signed quantity as a difference of positive quadratic energies. But that move does not inherit the sign theorem:

\[
4B(Q_U,I)
=B(Q_U+I,Q_U+I)-B(Q_U-I,Q_U-I).
\tag{27}
\]

The right-hand side is a **difference** of nonnegative numbers, with no determined sign. Therefore the existence of the positive metric does not force the linear determinant-phase term merely because that term can be reconstructed algebraically from the metric tensor.

This distinction is exactly the line mandate's evidence boundary. A geometry may contain enough information to reconstruct the explicit formula and still fail to explain its positivity. Equations (26)--(27) show that a bi-invariant metric contains the scalar logarithmic derivative as recoverable signed data, but its own nonnegativity applies only to the square/norm, not to that linear projection.

An operator-order theorem is different. If source geometry independently forced

\[
Q_U(t)\succeq0,
\tag{28}
\]

then positive linear readouts would retain the phase with sign. `WP-171` explains the classical Schur/passive setting in which such a boundary-delay theorem exists and why the actual signed Gamma/scattering target does not fit it globally. The present finding therefore does not subsume that route; it closes the weaker hope that ordinary invariant **Riemannian** positivity on the full unitary matrix is already enough.

## 5. Prior-art and novelty audit

The mathematical ingredients are classical. Ad-invariant inner products on compact reductive Lie algebras correspond to bi-invariant Riemannian metrics, and the reductive decomposition forces the center to be orthogonal to the semisimple ideals. Milnor's 1976 treatment of invariant metrics is a standard geometric anchor for this structure. Smith's 1960 lifetime matrix is the classical scattering-theory source for the Hermitian logarithmic derivative (16).

No new Lie-group or scattering theorem is claimed.

The Mathia-specific contribution is the branch-specific obstruction obtained by combining those classical facts with the current `weil_positivity` frontier. `WP-353` says that scalar normalized scattering has collapsed to divisor reconstruction and therefore pushes any surviving mechanism toward a larger noncentral object. Equations (3), (8), and (24) show that the most canonical finite-dimensional positive quadratic geometry on such an object **still cannot couple the scalar center to its genuinely noncentral directions**: canonical conjugation invariance itself forbids the required cross term.

A targeted prior-art audit found the ingredients separately in standard compact-Lie-group metric theory and Wigner--Smith scattering theory, but no distinct theorem converting their combination into a Weil-positivity mechanism. The conclusion is therefore a decisive research-line narrowing built from classical components, not a novelty claim for the underlying mathematics.

## 6. Boundaries and consequence for the research line

The no-go is intentionally limited to finite-dimensional, pointwise, conjugation-invariant **quadratic** geometry on a unitary scattering family. Several materially different routes remain open:

- a source-defined positive form that is not conjugation invariant and therefore carries a canonical arithmetic tensor coupling center and noncentral directions;
- a nonquadratic/Finsler or order-theoretic structure whose positivity is not merely a norm square;
- a global kernel or boundary form coupling different spectral parameters before pointwise reduction;
- an infinite-dimensional or adelic/cohomological object where the relevant center/commutator decomposition is different;
- a genuinely nonunitary construction with an independent positivity theorem not reducible to the defect geometry rejected in `WP-351`.

But each escape now has a sharper burden. **Finite channel size plus matrix noncommutativity is not enough.** If the positive geometry is the natural bi-invariant Riemannian metric of the unitary scattering object, the global scalar phase and the noncentral directions decouple orthogonally, and the scalar survives only as an orientation-blind square. A successful noncentral Weil bridge must therefore obtain its cross-place coupling from additional source structure before this invariant metric reduction, not from the bare unitary matrix geometry itself.
