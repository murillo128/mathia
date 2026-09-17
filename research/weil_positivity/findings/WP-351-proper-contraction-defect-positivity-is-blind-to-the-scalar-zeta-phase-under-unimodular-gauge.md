---
id: WP-351
title: Proper contraction-defect positivity is blind to the scalar zeta phase under unimodular gauge
branch: weil_positivity
status: supported
kind: contraction-defect-scalar-phase-no-go
claim_strength: exact operator-theoretic derivation with an arbitrary unimodular matched control and targeted prior-art audit
created: 2026-09-17
related: [WP-348, WP-349, WP-350]
clues: []
prior_art:
  - classical Sz.-Nagy--Foias contraction, defect-operator, dilation, and characteristic-function theory
  - de Branges--Rovnyak and model-space positive-kernel theory for Schur/characteristic functions
  - Bela Sz.-Nagy, Ciprian Foias, Hari Bercovici, and Laszlo Kerchy, Harmonic Analysis of Operators on Hilbert Space, 2nd ed., Springer, 2010
---

# WP-351 — Proper contraction-defect positivity is blind to the scalar zeta phase under unimodular gauge

## Claim

`WP-350` closed the moving-channel escape when the pre-differentiation compression is still required to be unitary, but deliberately left **proper nonunitary compression / contraction defect** open. That escape does produce a genuine positive object, independent of RH: a proper compression of a unitary scattering matrix is a contraction, so its standard defect operators are positive.

However, for the squarefree scattering factorization used in `WP-348`--`WP-350`, this positivity cannot by itself recover or force the scalar global zeta phase. If

\[
U(t)=g(t)R(t),\qquad |g(t)|=1,
\tag{1}
\]

and an isometric channel map

\[
V(t):K\to H_N,\qquad V(t)^*V(t)=I_K,
\tag{2}
\]

is used to form the proper compression

\[
B(t)=V(t)^*U(t)V(t),
\tag{3}
\]

then

\[
B(t)=g(t)C(t),\qquad C(t):=V(t)^*R(t)V(t).
\tag{4}
\]

Every standard defect/singular-value positive object is therefore exactly invariant under arbitrary scalar unimodular rephasing. In particular,

\[
I-B^*B=I-C^*C,
\qquad
I-BB^*=I-CC^*.
\tag{5}
\]

Thus a positivity theorem based only on these contraction defects cannot distinguish the physical `g(t)` from `e^{i\phi(t)}g(t)`, even though the scalar logarithmic derivative changes by `\phi'(t)`. The missing arithmetic phase must therefore enter through additional phase-sensitive structure **before** the defect positivity theorem: for example a canonically anchored quotient/channel rule, a cross-parameter connection, or another construction not determined solely by the contraction defects.

This is a no-go for the immediate contraction-defect escape left by `WP-350`, not for every nonunitary or categorical construction.

## 1. Proper compression gives genuine independent positivity

Fix `t` and suppress it from the notation. Let `U` be unitary on `H_N` and `V:K\to H_N` be an isometry. Then

\[
B=V^*UV
\tag{6}
\]

is a contraction. Indeed, for every `x\in K`,

\[
\|Bx\|
=\|V^*UVx\|
\le \|UVx\|
=\|Vx\|
=\|x\|.
\tag{7}
\]

Hence the standard defect operators

\[
D_B=(I-B^*B)^{1/2},
\qquad
D_{B^*}=(I-BB^*)^{1/2}
\tag{8}
\]

are well-defined positive operators. Their nonnegativity is an ordinary Hilbert-space theorem and uses neither RH nor zero data.

So the route is not rejected because positivity is artificial. The issue is **selectivity**: what arithmetic information survives in that independently positive geometry?

## 2. The scalar global phase disappears exactly

On the critical line, use the squarefree scattering decomposition

\[
U=gR,
\qquad |g|=1,
\qquad R^*R=RR^*=I.
\tag{9}
\]

Because `g` is scalar,

\[
B=V^*(gR)V
=g\,V^*RV
=gC.
\tag{10}
\]

Therefore

\[
B^*B
=\bar g C^*gC
=C^*C,
\tag{11}
\]

and similarly

\[
BB^*=CC^*.
\tag{12}
\]

Taking the unique positive square roots gives the exact identities

\[
\boxed{D_B=D_C,\qquad D_{B^*}=D_{C^*}.}
\tag{13}
\]

Consequently every positive form or scalar readout built only from `B^*B`, `BB^*`, the two defect operators, singular values, Schatten norms, or positive functional calculus of those objects is blind to `g`.

This statement is basis-independent and does not depend on the compression being finite-dimensional. The only operator-domain assumption here is boundedness, automatic for a compression of the finite cusp scattering matrix and equally valid in the bounded Hilbert-space formulation.

## 3. Arbitrary unimodular rephasing is a matched control

The blindness in (13) is stronger than failure on one arithmetic example. Let `\phi(t)` be any differentiable real-valued function and define the matched control

\[
\widetilde U(t)
=e^{i\phi(t)}U(t)
=\widetilde g(t)R(t),
\qquad
\widetilde g(t)=e^{i\phi(t)}g(t).
\tag{14}
\]

Keep the same channel map `V(t)` and the same ramified factor `R(t)`. Then

\[
\widetilde B(t)=e^{i\phi(t)}B(t),
\tag{15}
\]

so pointwise

\[
D_{\widetilde B(t)}=D_{B(t)},
\qquad
D_{\widetilde B(t)^*}=D_{B(t)^*}.
\tag{16}
\]

All defect-based positivity is therefore unchanged for **every** choice of `\phi`.

But the scalar phase generator does change. With the sign convention

\[
q_g(t):=-i\,\dot g(t)g(t)^{-1},
\tag{17}
\]

one has

\[
q_{\widetilde g}(t)
=q_g(t)+\phi'(t).
\tag{18}
\]

Thus the same positive defect geometry is compatible with an arbitrary additive perturbation of the scalar logarithmic-derivative term. A theorem whose hypothesis and positive quantity see only the defects cannot force the specific global zeta phase appearing in the physical scattering determinant.

This is the decisive control: the obstruction is not merely that one convenient trace loses information; the complete singular-value/defect data remain unchanged while the target scalar generator can be altered arbitrarily.

## 4. Standard characteristic-function positivity does not rescue phase selection

One might try to retain more of the contraction than its raw defects by passing to the Sz.-Nagy--Foias characteristic function. With the standard convention

\[
\Theta_B(z)
=-B+zD_{B^*}(I-zB^*)^{-1}D_B,
\qquad |z|<1,
\tag{19}
\]

and a scalar `\lambda\in\mathbb T`, the defect identities imply

\[
\Theta_{\lambda B}(z)
=\lambda\,\Theta_B(\bar\lambda z).
\tag{20}
\]

So the characteristic function itself is not phase-blind; rather, scalar rephasing becomes a rotation of its disk coordinate together with an output phase.

The associated de Branges--Rovnyak/model positive kernel

\[
K_B(z,w)
=\frac{I-\Theta_B(z)\Theta_B(w)^*}{1-z\bar w}
\tag{21}
\]

then satisfies

\[
K_{\lambda B}(z,w)
=K_B(\bar\lambda z,\bar\lambda w).
\tag{22}
\]

Hence its positivity is **covariant under disk rotation**. Positivity alone does not select the physical scalar phase `\lambda`; to do so one must provide an additional canonical phase anchor or cross-parameter identification. That extra datum, not the standard contraction-kernel positivity theorem, would carry the required selectivity.

This distinction matters: the claim is not that all functional-model data forget scalar phase. It is that the standard positive defect/kernel structures do not force a preferred scalar phase without an additional non-gauge-invariant input.

## 5. Dependence of the channel rule is the remaining loophole

Equations (10)--(18) hold pointwise even when `V=V(t)` moves with `t`, provided the matched control keeps the same channel rule. If instead `V(t)` is itself chosen by a rule that changes under `U\mapsto e^{i\phi}U`, then phase information can re-enter through that rule.

But that is precisely additional structure. The contraction-defect positivity no longer explains the scalar zeta term by itself; the burden moves to proving that the phase-sensitive channel/quotient rule is canonical, Mathia-native, independently defined, and produces the correct finite and archimedean terms without inserting the desired arithmetic phase.

Accordingly, the route still open after this finding is narrower:

- not a fixed/equivariant proper compression followed only by standard defect or singular-value positivity;
- possibly a source-defined phase-sensitive quotient or channel selection;
- possibly a genuinely cross-parameter connection whose curvature/holonomy has its own positivity theorem;
- possibly a categorical/cohomological construction outside the scalar-gauge-invariant contraction data considered here.

## Representation audit

The mathematical object is the bounded contraction `B(t)=V(t)^*U(t)V(t)` on `K`, with `U(t)` unitary on the physical critical line and `V(t)` an isometry. No basis is selected. Positivity is operator positivity of `I-B^*B` and `I-BB^*`, or positive-definiteness of the standard model kernel; scalar readouts are secondary consequences.

The matched control changes only the scalar unimodular factor `g(t)` and leaves `R(t)` and the compression channel fixed. It therefore tests exactly whether the proposed positive geometry sees the global scalar phase. The answer is no for defects/singular values and only rotation-covariantly for the characteristic-function kernel.

No truncation, zero spectrum, RH assumption, regularization, or hand-picked test kernel is used.

## Prior-art and novelty audit

The positivity of contraction defects, unitary dilation, characteristic functions, and their model-space kernels are classical Sz.-Nagy--Foias/de Branges--Rovnyak operator theory. They are **not** claimed as new mathematics. The targeted literature audit also confirms that characteristic functions are standard unitary invariants for completely nonunitary contractions and that positive Schur/model kernels are standard functional-model machinery.

The research contribution here is narrower and Mathia-specific: applying the exact scalar/ramified factorization isolated in `WP-348`--`WP-350` shows that the immediate `proper nonunitary compression / contraction defect` escape has an exact gauge-selectivity failure. Independent positivity survives the proper compression, but the target global scalar phase does not become forced by it.

This does not reproduce a classical Weil positivity criterion, Hilbert--Polya spectrum, Connes trace formula, or zero-defined operator. It is a negative structural test on whether a standard positive contraction geometry can provide the missing bridge.

## Verdict

**Supported exact negative.** Proper compression genuinely creates independently positive contraction defects, but those defects and all singular-value data satisfy

\[
B=gC\quad\Longrightarrow\quad
(D_B,D_{B^*})=(D_C,D_{C^*})
\tag{23}
\]

for every unimodular scalar `g`. Arbitrary rephasing changes the desired scalar logarithmic derivative while leaving that positive geometry unchanged. Standard characteristic-function kernel positivity is likewise rotation-covariant rather than phase-selecting.

Therefore this immediate route cannot make the global zeta scalar phase emerge *from contraction-defect positivity itself*. Any surviving nonunitary route must supply an additional canonical phase-sensitive structure before the positivity theorem, and that added structure now carries the main arithmetic burden.