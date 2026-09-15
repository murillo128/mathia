---
id: WP-309
title: Jointly holomorphic scalar boundary-automorphism families are constant
branch: weil_positivity
status: supported
kind: holomorphic-scalar-boundary-gauge-rigidity
claim_strength: exact rigidity theorem for source-independent scalar spectral-variable boundary gauges; a jointly holomorphic family whose every value slice is an automorphism of the Herglotz half-plane is constant, so the z-dependent automorphism loophole left by WP-308 collapses back to its constant Möbius classification
created: 2026-09-15
related: [WP-304, WP-305, WP-307, WP-308]
prior_art:
  - Schwarz--Pick lemma and the classical classification of disk/upper-half-plane automorphisms; the rigidity theorem below is an elementary consequence and is not claimed as new complex analysis
  - Daniel Alpay, Aad Dijksma, and Heinz Langer, The Schur transformation for Nevanlinna functions: operator representations, resolvent matrices, and orthogonal polynomials, Operator Theory: Advances and Applications 190 (2009), 27-63, DOI 10.1007/978-3-7643-9919-1_4, arXiv:0711.4236, for genuinely z-dependent/function-level Nevanlinna transforms tied to asymptotic moments and operator realizations
---

# WP-309 — Jointly holomorphic scalar boundary-automorphism families are constant

## Claim

`WP-308` rules out every **constant** scalar Herglotz projective recoding of the reflected Mangoldt response, but deliberately leaves `z`-dependent transfer matrices outside its scope. There is a precise distinction inside that escape: a `z`-dependent transform cannot remain merely a holomorphic scalar boundary-coordinate gauge if it is required to be an automorphism of the Herglotz half-plane at every spectral value.

Let `Omega` be a connected complex domain and let

\[
\Phi:\Omega\times\mathbb H\longrightarrow\mathbb H
\tag{1}
\]

be jointly holomorphic. Assume that for every `z in Omega`, the slice

\[
\Phi_z(w):=\Phi(z,w)
\tag{2}
\]

is a biholomorphic automorphism of the upper half-plane. Then

\[
\boxed{\Phi_z\text{ is independent of }z.}
\tag{3}
\]

Thus a source-independent scalar coordinate change that is simultaneously

1. holomorphic in the spectral parameter,
2. positivity preserving by pointwise Herglotz-half-plane automorphism, and
3. invertible as a boundary coordinate at every spectral value,

has **no nonconstant spectral-variable freedom at all**.

Applied to the `WP-305` reflected Mangoldt Herglotz response `m_-`, any candidate

\[
\widetilde m(z)=\Phi(z,m_-(z))
\tag{4}
\]

satisfying these hypotheses reduces to one constant real Möbius map. `WP-308` then applies verbatim: a non-affine map destroys the logarithmic end, while an end-preserving map is `T(w)=alpha w+beta` with `alpha>0`; unit logarithmic normalization forces `alpha=1`, leaving the wrong positive `+A_0/y^2` curvature unchanged. Hence

\[
\boxed{
\text{a jointly holomorphic scalar automorphism gauge cannot repair the Mangoldt--Gamma curvature mismatch.}
}
\tag{5}
\]

This does **not** rule out `z`-dependent Schur/Nevanlinna transforms, operator-valued boundary spaces, generalized resolvents, compressions, or an added Herglotz channel. It shows instead that any genuinely `z`-dependent scalar mechanism of that kind is new structure rather than hidden coordinate freedom.

**Classification:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + CLASSICAL-SCHWARZ-PICK-RIGIDITY + SCALAR-HERGLOTZ-BOUNDARY-GAUGE-NO-GO + MATCHED-CONTROLS + PRIOR-ART-REDIRECT + NOT-WEIL-POSITIVITY`.

## 1. Disk reduction

Let

\[
C(w)=\frac{w-i}{w+i}
\tag{6}
\]

be the Cayley transform from `H` to the unit disk `D`, and define

\[
F(z,u)=C\!\left(\Phi(z,C^{-1}(u))\right).
\tag{7}
\]

Then `F` is jointly holomorphic on `Omega x D`, and each slice `F_z` is an automorphism of `D`.

Set

\[
a(z):=F(z,0),
\qquad
b(z):=\partial_u F(z,0).
\tag{8}
\]

Joint holomorphy makes both `a` and `b` holomorphic in `z`. Since every `F_z` is an automorphism, `b(z)` never vanishes. Equality in Schwarz--Pick at the origin gives

\[
\boxed{|b(z)|=1-|a(z)|^2.}
\tag{9}
\]

The key point is that (9) asks a holomorphic parameter to move inside a real three-dimensional automorphism group while remaining holomorphic in the complex parameter. That is rigid.

## 2. Schwarz--Pick equality forces the parameter motion to vanish

Because `b` is holomorphic and nonzero,

\[
\log|b(z)|
\tag{10}
\]

is harmonic. Taking logarithms in (9) gives

\[
\log|b(z)|=\log(1-|a(z)|^2).
\tag{11}
\]

For holomorphic `a`, direct Wirtinger differentiation yields

\[
\Delta\log(1-|a|^2)
=
-\frac{4|a'|^2}{(1-|a|^2)^2}.
\tag{12}
\]

The left side of (11) has zero Laplacian, so (12) forces

\[
a'(z)=0
\qquad\text{throughout }\Omega.
\tag{13}
\]

Thus `a` is constant. Equation (9) then makes `|b|` constant. A holomorphic function of constant modulus on a connected domain is constant, so `b` is constant as well.

Finally, a disk automorphism is uniquely determined by its value and derivative at one interior point. Indeed, if two automorphisms have the same value and derivative at zero, their quotient by composition fixes zero with derivative one, hence is the identity by Schwarz's lemma. Therefore all `F_z` coincide, proving (3).

No zeta zeros, RH input, regularization choice, or asymptotic approximation enters this rigidity argument.

## 3. Consequence for the `WP-305` curvature mismatch

Suppose a proposed scalar boundary recoding is source independent and has the form (4), with `Phi` satisfying the theorem. Then there is one fixed `T in Aut(H)` such that

\[
\widetilde m(z)=T(m_-(z)).
\tag{14}
\]

`WP-308` classifies exactly these fixed maps. If

\[
T(w)=\frac{aw+b}{cw+d},
\qquad ad-bc>0,
\tag{15}
\]

then `c!=0` sends the unbounded logarithmic end to the finite boundary value `a/c`. Preserving

\[
\operatorname{Re}\widetilde m(iy)=\log y+O(1)
\tag{16}
\]

therefore forces `c=0`, hence

\[
T(w)=\alpha w+\beta,
\qquad \alpha>0.
\tag{17}
\]

Matching the unit coefficient of `log y` forces `alpha=1`. Consequently

\[
\operatorname{Re}\widetilde m(iy)
=
\log y+O(1)+\frac{A_0}{y^2}+o(y^{-2}),
\qquad A_0>0,
\tag{18}
\]

whereas the Riemann Gamma channel has

\[
\operatorname{Re}\psi\!\left(\frac14+\frac{iy}{2}\right)
=
\log\frac y2-\frac1{24y^2}+O(y^{-4}).
\tag{19}
\]

Thus allowing a holomorphic spectral parameter in the scalar **automorphism gauge** adds no repair freedom beyond `WP-308`.

## 4. Matched controls: each dropped hypothesis reopens a genuinely different class

The rigidity is not a statement that every spectral-variable scalar transform is constant.

If holomorphy in the spectral parameter is dropped, nonconstant automorphism families are immediate. For example,

\[
T_z(w)=w+\operatorname{Re}z
\tag{20}
\]

is an upper-half-plane automorphism for every fixed `z`, but its dependence on `z` is not holomorphic. Therefore composing it with a Herglotz response does not define a source-independent holomorphic Nevanlinna coordinate change.

If pointwise invertibility is dropped instead, nonconstant jointly holomorphic families also exist. For `z,w in H`,

\[
S(z,w)=w+z
\tag{21}
\]

maps `H x H` holomorphically into `H`, but `w -> w+z` is not onto `H` when `Im z>0`. Applied to a response `m`, it produces `m(z)+z`: this is an **added positive channel**, not a coordinate recoding. More generally, adding an independently derived Herglotz function has exactly this character.

A transform engineered only along the particular graph `w=m_-(z)` can also evade the theorem because it need not extend to a jointly holomorphic automorphism family on `Omega x H`. But then the operation is source dependent and must supply its own intrinsic construction and positivity theorem; it cannot be justified as universal scalar boundary gauge freedom.

These controls make the boundary exact: the theorem removes only the putative nonconstant **gauge** escape, not genuinely new dynamics.

## 5. Prior-art and novelty audit

The mathematical rigidity in (3) is an elementary consequence of classical Schwarz--Pick equality and the standard automorphism group of the disk/upper half-plane. No novelty is claimed for that complex-analysis statement.

The relevant operator-theory control is the Schur transformation for Nevanlinna functions studied by Alpay--Dijksma--Langer. Their transform is fractional-linear at the **function level**, uses prescribed asymptotic data at infinity, and changes self-adjoint resolvent realizations through block-operator/compression structure. This is precisely why such a transform is not contradicted by (3): it is not a freely varying pointwise automorphism of `H` independent of the input function. It carries additional moment/realization information.

A targeted search over holomorphic families of disk/half-plane automorphisms, Schwarz--Pick rigidity, and Nevanlinna Schur transformations found no reason to treat (3) as new function theory. The Mathia-specific content is the consequence for the exact escape explicitly left open by `WP-308`:

\[
\boxed{
\text{spectral-variable scalar automorphism gauge}
\Longrightarrow
\text{constant gauge}
\Longrightarrow
\text{the WP-308 curvature obstruction remains.}
}
\tag{22}
\]

Conversely, the classical Schur literature sharpens the surviving interpretation: a useful `z`-dependent scalar transform must import source moments, interpolation data, or a changed operator realization. Such data may be legitimate if Mathia derives them independently, but they are no longer coordinate freedom.

## 6. Consequence for the research frontier

`WP-307` closes orientation-preserving affine changes of the spectral **input**. `WP-308` closes constant projective changes of the scalar Herglotz **output**. `WP-309` now shows that making that output automorphism depend holomorphically on the spectral variable does not enlarge the gauge class at all.

The scalar source-resolvent route therefore has a sharper next gate. Any surviving `z`-dependent operation must fail at least one of the gauge hypotheses above: it must be a noninvertible Herglotz self-map, a source-moment Schur transform, a compression/generalized resolvent, an added archimedean channel, or part of a higher-dimensional/nonseparable finite--archimedean structure. Such a construction must derive both its extra data and its sign theorem before comparison with the Gamma target.

This remains a negative structural result. It does not construct a global Weil form, does not produce the polar/global counterterms, and does not prove Weil positivity or RH.

## Dependencies

- `research/weil_positivity/findings/WP-304-bounded-source-resolvents-are-too-small-pole-normalized-mangoldt-energy-yields-only-an-oriented-universal-logarithmic-herglotz-tail.md`
- `research/weil_positivity/findings/WP-305-canonical-reflected-mangoldt-herglotz-has-the-wrong-next-order-gamma-curvature.md`
- `research/weil_positivity/findings/WP-307-pole-normalized-mangoldt-curvature-stays-positive-under-every-affine-spectral-recentering.md`
- `research/weil_positivity/findings/WP-308-scalar-herglotz-projective-recodings-cannot-repair-mangoldt-gamma-curvature.md`
