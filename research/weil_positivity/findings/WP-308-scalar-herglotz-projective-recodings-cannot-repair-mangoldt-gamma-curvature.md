---
id: WP-308
title: Scalar Herglotz projective recodings cannot repair the Mangoldt–Gamma curvature mismatch
branch: weil_positivity
status: supported
kind: scalar-nevanlinna-projective-coordinate-gamma-curvature-obstruction
claim_strength: exact classification of constant real linear-fractional value-coordinate changes preserving scalar Herglotz positivity at the WP-305 reflected Mangoldt response; every non-affine automorphism destroys the required logarithmic growth, while every growth-preserving automorphism is positive affine and therefore preserves the wrong sign of the first real y^-2 curvature
created: 2026-09-15
related: [WP-184, WP-185, WP-304, WP-305, WP-306, WP-307]
prior_art:
  - Fritz Gesztesy and Eduard Tsekanovskii, On Matrix-Valued Herglotz Functions, Mathematische Nachrichten 218 (2000), 61-138, DOI 10.1002/1522-2616(200010)218:1<61::AID-MANA61>3.0.CO;2-D, for classical linear-fractional transformations of Herglotz/Weyl functions and their self-adjoint-extension interpretation
  - Fritz Gesztesy, Konstantin A. Makarov, and Eduard Tsekanovskii, An Addendum to Krein's Formula, arXiv:funct-an/9711003, for linear-fractional relations between Weyl-Titchmarsh functions of self-adjoint extensions
  - Daniel Alpay, Aad Dijksma, and Heinz Langer, The Schur transformation for Nevanlinna functions: operator representations, resolvent matrices, and orthogonal polynomials, arXiv:0711.4236, for classical fractional-linear Nevanlinna transformations tied to asymptotics at infinity; its z-dependent Schur transform is outside the constant projective class ruled out here
  - NIST Digital Library of Mathematical Functions, Section 5.11, for the Riemann digamma asymptotic used in WP-305
---

# WP-308 — Scalar Herglotz projective recodings cannot repair the Mangoldt–Gamma curvature mismatch

## Claim

`WP-304`--`WP-307` leave a natural scalar boundary-response escape: perhaps the reflected source Herglotz function has the wrong coordinate, and a different self-adjoint scalar boundary coordinate could convert its positive source geometry into the Riemann archimedean response. For the canonical constant projective freedom of a scalar Herglotz/Weyl function, this does not work.

Let `m_-` be the reflected pole-normalized Mangoldt Herglotz function of `WP-305`. Along the imaginary axis,

\[
m_-(iy)
=
\log y-B+\frac{A_0}{y^2}+o(y^{-2})
+i\left(\frac\pi2+\frac{C_+}{y}+o(y^{-1})\right),
\qquad A_0>0.
\tag{1}
\]

In particular `m_-(iy) -> infinity` in modulus and its real part has the required unit logarithmic leading growth but the wrong positive first curvature. Consider any constant real linear-fractional automorphism of the upper half-plane,

\[
T(w)=\frac{aw+b}{cw+d},
\qquad a,b,c,d\in\mathbb R,
\qquad \Delta:=ad-bc>0.
\tag{2}
\]

These are exactly the scalar projective coordinate changes that preserve Herglotz positivity bijectively. Then precisely one of two things happens.

If `c != 0`,

\[
T(m_-(iy))
=\frac ac-
\frac{\Delta}{c\bigl(c m_-(iy)+d\bigr)}
=\frac ac+O\!\left(\frac1{\log y}\right),
\tag{3}
\]

so the transformed response tends to a finite real boundary value and loses the logarithmic growth altogether.

If `c=0`, then `ad>0` and

\[
T(w)=\alpha w+\beta,
\qquad \alpha:=a/d>0,
\qquad \beta:=b/d\in\mathbb R.
\tag{4}
\]

Hence

\[
\operatorname{Re}T(m_-(iy))
=
\alpha\log y-\alpha B+\beta
+\frac{\alpha A_0}{y^2}+o(y^{-2}).
\tag{5}
\]

Thus every projective coordinate change that retains logarithmic growth preserves the **positive** sign of the first real curvature. Matching the unit coefficient of the Riemann-Gamma logarithm forces `alpha=1`, after which only the constant is adjustable and the coefficient remains exactly `+A_0`.

By contrast,

\[
\operatorname{Re}\psi\!\left(\frac14+\frac{iy}{2}\right)
=
\log\frac y2-\frac1{24y^2}+O(y^{-4}).
\tag{6}
\]

Therefore

\[
\boxed{
\text{no constant scalar Herglotz projective coordinate change can turn the WP-305 source response into the Riemann Gamma asymptotic.}
}
\tag{7}
\]

This closes a boundary-coordinate escape not covered by `WP-307`: changing the **spectral input coordinate** by an arbitrary orientation-preserving affine map cannot fix the source invariant there, and now changing the **scalar Herglotz output coordinate** by an arbitrary positivity-preserving real Möbius automorphism cannot fix it either.

**Classification:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + SCALAR-HERGLOTZ-PROJECTIVE-NO-GO + LOG-GROWTH-RIGIDITY + CURVATURE-SIGN-INVARIANCE + SELF-ADJOINT-BOUNDARY-COORDINATE-CONTROL + MATCHED-CONTROLS + CLASSICAL-NEVANLINNA-PRIOR-ART + NOT-WEIL-POSITIVITY`.

## 1. Why the Herglotz projective class is the canonical scalar boundary freedom

A scalar Herglotz/Nevanlinna function maps the upper half-plane to itself. The biholomorphic automorphisms of the upper half-plane are the real Möbius maps (2), modulo common nonzero scalar multiplication of the coefficients. In Weyl-function and self-adjoint-extension theory, exactly this kind of linear-fractional change appears when one changes scalar boundary coordinates or compares Weyl-Titchmarsh functions associated with self-adjoint extensions.

That classical structure is important here because the positivity of `m_-` is not a fitted property: it comes from the positive reflected measure underlying the regularized Herglotz representation in `WP-304`--`WP-305`. If the missing Gamma term were merely hidden by the choice of scalar boundary coordinate, one would expect the repair to live inside the positivity-preserving projective freedom (2), rather than require an independently inserted target counterterm.

The theorem below is deliberately only about **constant scalar projective recoding**. Matrix-valued boundary spaces, compressions, nonconstant `z`-dependent transfer matrices, Schur-type transforms involving the spectral variable itself, and genuinely new finite--archimedean couplings are not classified by it.

## 2. Non-affine projective changes compactify the logarithmic end

From (1),

\[
|m_-(iy)|\to\infty.
\tag{8}
\]

For `c != 0`, elementary projective algebra gives the exact identity

\[
\frac{aw+b}{cw+d}
=\frac ac-
\frac{ad-bc}{c(cw+d)}.
\tag{9}
\]

Substituting `w=m_-(iy)` proves (3). More explicitly, because

\[
m_-(iy)=\log y+O(1)+i\left(\frac\pi2+o(1)\right),
\tag{10}
\]

the correction in (9) is `O(1/log y)`. A non-affine upper-half-plane automorphism therefore sends the infinite end approached by the source response to the finite boundary point `a/c`.

This is stronger than a mismatch of the `y^-2` coefficient. Such a recoding cannot even retain the leading archimedean scale. No choice of `a,b,c,d` with `c != 0` can satisfy

\[
\operatorname{Re}T(m_-(iy))
=
\log y+O(1).
\tag{11}
\]

The only way a real projective automorphism can keep the same infinite end is to fix infinity, which is exactly `c=0`.

## 3. Fixing infinity reduces the whole projective freedom to positive affine output scaling

When `c=0`, (2) reduces exactly to (4). Since `Delta=ad>0`, the scale `alpha=a/d` is strictly positive. Applying (4) to (1) gives (5) with no approximation beyond the already-established source expansion.

Two consequences are immediate.

First, positivity-preserving projective recoding cannot flip the curvature sign even before the leading logarithm is normalized:

\[
A_0>0
\quad\Longrightarrow\quad
\alpha A_0>0.
\tag{12}
\]

Second, the exact Riemann-Gamma leading coefficient is one, so any candidate matching (6) must have

\[
\alpha=1.
\tag{13}
\]

Then

\[
\operatorname{Re}T(m_-(iy))
=
\log y+(-B+\beta)
+\frac{A_0}{y^2}+o(y^{-2}).
\tag{14}
\]

The free real translation `beta` can absorb a constant normalization such as `-log 2`, but it cannot affect any inverse-power coefficient. Equations (6) and (14) have opposite `y^-2` signs. This proves (7).

Notice that this argument does not require RH, zero ordinates, numerical fitting, or a conjectural operator model. It uses only the already-derived source asymptotic, `A_0>0`, and the classical geometry of scalar Herglotz coordinate changes.

## 4. Matched controls and aggressive falsification

The obstruction is not the claim that Möbius maps are too weak to alter asymptotics. They can alter them drastically. For example, the upper-half-plane automorphism `w -> -1/w` sends an unbounded Herglotz value to zero. Equation (3) is precisely that phenomenon in general form. What it cannot do is both retain the required logarithmic end and reverse the first real curvature there.

Nor is the positive sign in (12) a generic theorem about arbitrary nonlinear transforms of positive measures. It follows from the much narrower condition that the value-coordinate change be an automorphism of the scalar Herglotz half-plane **and** preserve the infinite end. The stabilizer of that end is the positive affine subgroup, whose derivative is positive and constant.

Orientation-reversing real Möbius maps do not evade the result: `Delta<0` maps the upper half-plane to the lower half-plane and therefore destroys the Herglotz positivity that supplied the proposed geometric sign. If one adds an extra minus sign to return to the upper half-plane, the combined projective map has positive determinant and is already included in (2).

A target-dependent additive function of `z` could of course alter the `y^-2` coefficient, but then the missing archimedean term has been inserted as a new channel rather than recovered by a scalar boundary-coordinate change. Such a proposal must be justified by an independent Mathia-native construction and falls outside the present coordinate-gauge test.

The exact falsification test is correspondingly simple: exhibit a **constant** real Möbius automorphism `T` of the upper half-plane such that `Re T(m_-(iy))` retains unit logarithmic growth and has negative `y^-2` coefficient. Equations (3)--(5) show this is impossible.

## 5. Prior art and novelty audit

No novelty is claimed for the automorphism group of the upper half-plane, for Herglotz/Nevanlinna functions, or for linear-fractional relations between Weyl functions. Gesztesy--Tsekanovskii study matrix-valued Herglotz functions under linear-fractional transformations and connect them to self-adjoint finite-rank perturbations and self-adjoint extensions. Gesztesy--Makarov--Tsekanovskii explicitly derive linear-fractional relations between Weyl-Titchmarsh functions of different self-adjoint extensions. These are the classical operator-theoretic reasons to audit the projective freedom here rather than treat a boundary-coordinate change as a new mechanism.

A targeted literature check also reaches the Schur transformation for Nevanlinna functions studied by Alpay--Dijksma--Langer, where fractional-linear transformations are tied to asymptotic moment data and operator compressions. That theory does **not** make the present claim new as function theory; conversely, its standard Schur transform contains explicit `z`-dependent terms and belongs to a broader class not ruled out by (7).

`WP-184`--`WP-185` are related but not duplicates. They concern the exact **Gamma relative phase** `R_infty`, whose non-Blaschke divisor puts it outside bounded characteristic and obstructs faithful bounded-type projective encodings. The present object is instead the **source-derived reflected Mangoldt Herglotz response** `m_-`, which is already inside the positive Nevanlinna class. The obstruction here comes from its high-energy logarithmic end and the sign of its first subleading coefficient, not from a zero divisor or bounded-characteristic failure.

The Mathia-specific delta is therefore the exact application

\[
\boxed{
\text{source Herglotz positivity}
+\text{unit log end}
+ A_0>0
\quad\Longrightarrow\quad
\text{scalar self-adjoint projective gauge cannot produce Gamma curvature}.
}
\tag{15}
\]

This is a project-specific no-go built from classical Nevanlinna geometry, not a new theorem about Herglotz functions and not a Weil positivity theorem.

## 6. Consequence for the Weil-positivity search

After `WP-307`, one could still hope that the source was correct and only its scalar Weyl/Herglotz coordinate was wrong. `WP-308` removes that interpretation for the canonical projective boundary freedom. A non-affine scalar coordinate sends the logarithmic end to a finite point; a coordinate that preserves the end is positive affine and retains the wrong curvature sign.

Thus the surviving route must change more than scalar coordinates. In the current source-resolvent branch it must introduce a genuinely different archimedean/boundary sector, a higher-dimensional or operator-valued boundary space, a quotient/compression whose positivity theorem is not scalar projective invariance, a source-derived `z`-dependent transformation with independent geometric meaning, or a nonseparable finite--archimedean coupling before the scalar response is formed.

That is a meaningful narrowing of the primary question but still falls short of it: no global Weil quadratic form, finite-prime/archimedean decomposition, or independent global positivity theorem is produced here.

## Dependencies

- `research/weil_positivity/findings/WP-184-gamma-phase-is-outside-bounded-characteristic-and-bounded-type-mobius-repairs-degenerate.md`
- `research/weil_positivity/findings/WP-185-gamma-phase-cannot-be-projective-coordinate-of-bounded-analytic-completion.md`
- `research/weil_positivity/findings/WP-304-bounded-source-resolvents-are-too-small-pole-normalized-mangoldt-energy-yields-only-an-oriented-universal-logarithmic-herglotz-tail.md`
- `research/weil_positivity/findings/WP-305-canonical-reflected-mangoldt-herglotz-has-the-wrong-next-order-gamma-curvature.md`
- `research/weil_positivity/findings/WP-307-pole-normalized-mangoldt-curvature-stays-positive-under-every-affine-spectral-recentering.md`

## Bottom line

The wrong `+A_0/y^2` curvature is not an artifact of the scalar Herglotz/Weyl projective coordinate. Every positivity-preserving constant Möbius recoding either moves the logarithmic end to a finite boundary point or fixes infinity and reduces to a positive affine map, which cannot reverse the curvature sign. Repairing the Mangoldt-to-Gamma bridge therefore requires new geometry rather than a scalar self-adjoint boundary-coordinate change.
