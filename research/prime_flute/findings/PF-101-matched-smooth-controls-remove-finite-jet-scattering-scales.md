# PF-101 — matched smooth controls remove finite-jet scattering scales

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE` for interpreting the `p \asymp t^{1/4}` direct-scattering scale of PF-100, or any analogous scale extracted from a fixed finite asymptotic jet of the endpoint map, as a prime-specific or RH-specific spectral mechanism.

## Claim

PF-100 showed that for the exact endpoint map

\[
V(x)=\pi\cot\frac{\pi}{x}
=x-\frac{A}{x}-\frac{B}{x^3}+O(x^{-5}),
\qquad
A=\frac{\pi^2}{3},\quad B=\frac{\pi^4}{45},
\]

the width-one normalized local direct-scattering denominator has the first exact/reference defect

\[
\log\frac{C^V_{xy}}{C^0_{xy}}
=-\frac{A}{2P^4}
\Big((s-r)^2+ab+cd\Big)+O(P^{-5})
\tag{1}
\]

for two local cusps `x=P+r`, `y=P+s`, with fixed positive left/right reference gaps `(a,b)` and `(c,d)`.

The tempting interpretation was that the resulting physical-line elementary phase becomes order one at `P \asymp t^{1/4}`, exposing a distinguished finite-scale signal of the exact cotangent geometry after cusp-width normalization.

That interpretation fails an adversarial matched-control test.

Let

\[
F_{\alpha,\beta}(x)
=x-\frac{\alpha}{x}-\frac{\beta}{x^3}+O(x^{-5})
\tag{2}
\]

be **any** smooth increasing endpoint deformation on the tail. Repeating the same canonical cusp-width normalization gives

\[
\boxed{
\log\frac{C^{F}_{xy}}{C^0_{xy}}
=-\frac{\alpha}{2P^4}
\Big((s-r)^2+ab+cd\Big)+O(P^{-5}).
}
\tag{3}
\]

The coefficient `beta` cancels completely at this order. Therefore the explicit nontrigonometric control

\[
\boxed{
F_1(x)=x-\frac{\pi^2}{3x}
}
\tag{4}
\]

reproduces **exactly the same leading local three-gap coefficient and the same `t^{1/4}` direct-sector phase scale as the cotangent endpoint map**.

The control can be made sharper. Since `B=A^2/5`, direct expansion one order deeper gives

\[
\boxed{
\log\frac{C^V_{xy}}{C^{F_1}_{xy}}
=-\frac{A^2}{P^6}
\Big((s-r)^2+ab+cd\Big)+O(P^{-7}).
}
\tag{5}
\]

Thus, after matching only the first inverse-power coefficient of `V`, the first local direct-scattering distinction moves from `P^{-4}` to `P^{-6}`. On `s=1/2+it` the corresponding elementary phase becomes order one at

\[
P\asymp t^{1/6},
\]

not `t^{1/4}`.

Matching more terms of the ordinary asymptotic expansion of `V` pushes the first difference to still higher order. Consequently **no exponent obtained by asking when a fixed finite endpoint-jet defect becomes order one at spectral height `t` is intrinsic enough to be an RH scale**. It depends on which asymptotically matched smooth reference is subtracted.

The exact formulas of PF-100 remain valid. What is ruled out is their interpretation as a special arithmetic high-energy mechanism.

## 1. The canonical normalized denominator for a general endpoint map

For a strictly increasing endpoint map `F`, define the left/right local finite differences at a cusp `x` by

\[
\Delta_-^F(x;a)=F(x)-F(x-a),
\qquad
\Delta_+^F(x;b)=F(x+b)-F(x),
\]

and the primitive parabolic width

\[
W^F(x;a,b)
=2\left(
\frac1{\Delta_-^F(x;a)}+
\frac1{\Delta_+^F(x;b)}
\right).
\]

For two cusps `x<y`, the width-one normalized direct denominator is

\[
C^F_{xy}
=\sqrt{W^F(x;a,b)W^F(y;c,d)}\,[F(y)-F(x)].
\tag{6}
\]

This is exactly the same geometric quantity used in PF-086/PF-087/PF-100; no new generating function or spectral weight is introduced.

For the identity reference `F_0(x)=x`, write the corresponding objects as `W^0,C^0`.

## 2. Universal local expansion

Assume (2), with fixed offsets and gaps while `P -> infinity`. The width calculation used in PF-100 is algebraic in the coefficients of the endpoint expansion and gives, at a cusp whose local reference coordinate is `x`,

\[
\log\frac{W^F(x;a,b)}{W^0(a,b)}
=
-\frac{\alpha}{x^2}
+
\frac{\alpha^2/2-\alpha ab-3\beta}{x^4}
+O(x^{-5}).
\tag{7}
\]

There is no `x^{-3}` term.

For `x=P+r`, `y=P+s`, the long divided difference satisfies

\[
\log
\frac{F(P+s)-F(P+r)}{s-r}
=
\frac{\alpha}{P^2}
-\frac{\alpha(r+s)}{P^3}
+
\frac{-\alpha^2/2+\alpha(r^2+rs+s^2)+3\beta}{P^4}
+O(P^{-5}).
\tag{8}
\]

Insert two copies of (7) and one copy of (8) into

\[
\log\frac{C^F_{xy}}{C^0_{xy}}
=
\frac12\log\frac{W^F(P+r;a,b)}{W^0(a,b)}
+
\frac12\log\frac{W^F(P+s;c,d)}{W^0(c,d)}
+
\log\frac{F(P+s)-F(P+r)}{s-r}.
\tag{9}
\]

After re-expanding the two width terms around the common base `P`, all contributions of orders `P^{-2}` and `P^{-3}` cancel. At order `P^{-4}`, the terms containing `alpha^2` and `beta` also cancel. The survivor is exactly

\[
-\frac{\alpha}{2}
\big((s-r)^2+ab+cd\big),
\]

which proves (3).

The cancellation is therefore a **projective/Schwarzian response**, not a special identity of the cotangent coefficients.

## 3. Consecutive-gap specialization reproduces PF-100 exactly

For four consecutive positions

\[
P,
\quad P+X,
\quad P+X+Y,
\quad P+X+Y+Z,
\]

take the channel between the middle two cusps. Then

\[
r=X,
\qquad s=X+Y,
\qquad ab=XY,
\qquad cd=YZ,
\]

so

\[
(s-r)^2+ab+cd
=Y^2+XY+YZ
=Y(X+Y+Z).
\]

Hence every map of the form

\[
F(x)=x-\frac{\alpha}{x}+O(x^{-3})
\]

obeys

\[
\boxed{
\log\frac{C^F_{n,n+1}}{C^0_{n,n+1}}
=-\frac{\alpha}{2P^4}Y(X+Y+Z)+O(P^{-5}).
}
\tag{10}
\]

Setting `alpha=pi^2/3` gives PF-100's cotangent coefficient exactly:

\[
-\frac{\pi^2}{6P^4}Y(X+Y+Z).
\]

Thus the same `p^{-4}` three-gap form is present in a smooth featureless endpoint deformation having only the same first asymptotic coefficient as `V`.

## 4. The first cotangent-vs-matched-control difference is sixth order

To determine whether (10) merely delays the special cotangent information, keep the `x^{-3}` coefficient in (2) and expand (9) through `P^{-6}`.

The dependence on `beta` first appears as

\[
-\frac{5\beta}{P^6}
\big((s-r)^2+ab+cd\big).
\tag{11}
\]

All other sixth-order terms depend only on `alpha` and are therefore identical for two maps with the same `alpha`.

For

\[
V(x)=x-\frac{A}{x}-\frac{B}{x^3}+O(x^{-5}),
\qquad
F_1(x)=x-\frac{A}{x},
\]

we have `B=A^2/5`. Subtracting the two expansions gives (5):

\[
\log\frac{C^V_{xy}}{C^{F_1}_{xy}}
=-\frac{A^2}{P^6}
\big((s-r)^2+ab+cd\big)
+O(P^{-7}).
\]

For consecutive gaps this becomes

\[
\boxed{
\log\frac{C^V_{n,n+1}}{C^{F_1}_{n,n+1}}
=-\frac{\pi^4}{9P^6}Y(X+Y+Z)
+O(P^{-7}).
}
\tag{12}
\]

This provides a direct falsification test for the control argument.

## 5. Why the effect is projective rather than cotangent-specific

PF-082 proved the exact identity

\[
S(V)(x)=\frac{2\pi^2}{x^4}
\]

for the Schwarzian derivative. For the matched control (4), an elementary calculation gives

\[
\boxed{
S(F_1)(x)
=
\frac{2\pi^2}{\left(x^2+\pi^2/3\right)^2}
=
\frac{2\pi^2}{x^4}
-\frac{4\pi^4}{3x^6}
+O(x^{-8}).
}
\tag{13}
\]

Thus `V` and `F_1` have the same leading projective curvature. Their first Schwarzian mismatch is sixth order, exactly where the normalized direct denominator first separates them.

This is the standard role of the Schwarzian: it is the first local obstruction to replacing a smooth map by a Möbius transformation, and it controls infinitesimal cross-ratio distortion. Cross-ratio distortion in terms of the Schwarzian is classical; see for example Alexey Teplinsky, *On cross-ratio distortion and Schwarz derivative*, arXiv:0710.2629, and de Faria--de Melo, *Mathematical Tools for One-Dimensional Dynamics*, Chapter 6.

No novelty is claimed for that projective principle.

## 6. Finite-jet matching destroys any privileged phase exponent

The cotangent map has a convergent inverse-power expansion on the tail,

\[
V(x)
=x-\frac{A}{x}-\frac{B}{x^3}-\frac{C}{x^5}-\cdots.
\]

For every fixed finite order one can form a smooth nontrigonometric control by truncating this expansion. Its derivative is `1+O(x^{-2})`, so it is strictly increasing for all sufficiently large `x` and therefore defines a legitimate tail endpoint sequence for the same zero-twist flute construction.

If a control matches more endpoint coefficients, the corresponding finite differences, cusp widths, and normalized local direct denominators match to correspondingly higher asymptotic order. In projective language, one is matching a longer jet of the Schwarzian and its derivatives.

The first two cases already suffice to expose the problem:

```text
identity reference x:
    first local normalized defect  ~ P^-4
    direct elementary phase scale ~ t^(1/4)

matched control x - A/x:
    first cotangent/control defect ~ P^-6
    direct elementary phase scale ~ t^(1/6)
```

Adding further matched inverse-power coefficients pushes the first unmatched finite-jet phase to still smaller powers of `t`.

Therefore a scale extracted solely from

\[
t\times(\text{first unmatched local endpoint-jet defect})\asymp1
\]

is **reference-jet dependent**. It cannot acquire RH significance merely because one particular natural reference (`x`) produces the exponent `1/4`.

## 7. Relation to the hyperbolic gap geometry

The negative does not remove the real geometric content of PF-100. The factor

\[
Y(X+Y+Z)
= XZ\,\sinh^2\frac{L}{4}
\]

still couples the local direct-scattering denominator to the canonical multi-gap separator `L` of PF-004.

What changes is the interpretation of the absolute coefficient multiplying that gap shape. Equation (10) shows that the leading coefficient is supplied by the first Schwarzian jet of the endpoint deformation, and an unrelated smooth deformation with the same jet supplies the same result.

Hence

\[
\boxed{
\text{multi-gap factor}
\;=\;\text{real prime-flute geometry},
\qquad
P^{-4}\text{ high-energy scale}
\;=\;\text{generic finite-jet response}.
}
\]

This is exactly the kind of universal-background separation required by the research-watch controls.

## 8. Interior/exterior duality

The denominator `C_{xy}` is defined after canonical width-one normalization, and the ratios above are unchanged under the common Möbius conjugations/relabelings implementing the interior/exterior realization of the orthogonal-circle construction.

The matched-control obstruction therefore does not depend on choosing the cusp-side picture. It is a statement about the intrinsic projective jet seen by the normalized hyperbolic scattering geometry.

## 9. Prior art and novelty audit

The ingredients are classical or already established in this branch:

- asymptotic expansion of `cot`;
- Schwarzian derivative and its control of infinitesimal cross-ratio distortion;
- width-one cusp normalization and the direct `|c|^{-2s}` term of hyperbolic cusp scattering (PF-086);
- the exact PF-100 cancellation formula for `V`.

Targeted searches for Schwarzian/cross-ratio distortion confirm that the dependence of local projective distortion on the Schwarzian is standard. Hyperbolic scattering/sojourn-time literature likewise treats the direct geometric phases as standard scattering data. No novelty is claimed for either theory.

The durable contribution is the **adversarial control result for this program**:

\[
\boxed{
\text{PF-100's local }P^{-4}\text{ coefficient and }t^{1/4}\text{ scale}
\text{ survive a non-cotangent matched smooth control.}
}
\]

Accordingly, they cannot be used as evidence for a special prime-flute/RH high-energy mechanism.

This is not contradicted by recent work on prime scattering geodesics for the modular surface: that literature imports arithmetic from the modular group and studies counting of scattering geodesics/sojourn times, whereas the present obstruction concerns smooth endpoint-jet universality in the derived prime-flute.

## 10. Boundary of the negative result

PF-101 does **not** say that the exact cotangent flute is isometric to the matched controls. It is not. Their Schwarzian derivatives already differ at order `P^{-6}` in (13), and the full functions have different global analytic structure.

Nor does it rule out every possible exact-vs-projective spectral construction. It rules out the specific strategy

\[
\text{take a fixed finite asymptotic endpoint jet}
\to
\text{read its first scattering phase scale}
\to
\text{interpret that exponent as RH structure}.
\]

A candidate that genuinely uses the exact endpoint geometry would have to depend on information not reproducible by matching an arbitrary finite tail jet -- for example a nonperturbative/global property of the exact map coupled to the actual prime sampling -- and would still have to survive PF-097/PF-099's primality-blindness controls.

## 11. Falsification tests

The two finite algebraic tests are direct:

1. For arbitrary fixed `r<s` and positive `a,b,c,d`, expand (9) for (2) and verify that the `P^{-4}` coefficient is
   \[
   -\frac{\alpha}{2}\big((s-r)^2+ab+cd\big)
   \]
   with no `beta` dependence.
2. Set `alpha=pi^2/3`, compare `V(x)` with `F_1(x)=x-alpha/x`, and verify
   \[
   P^6\log\frac{C^V_{xy}}{C^{F_1}_{xy}}
   \longrightarrow
   -\alpha^2\big((s-r)^2+ab+cd\big).
   \]

Both are finite asymptotic identities and require no theorem about the existence of the full infinite-cusp physical scattering matrix.

## Consequence for PF-100

PF-100's equations for the cotangent map remain correct, but its tentative contrast between the local `t^{1/4}` scale and generic smooth controls is now resolved negatively. The **nonlocal** `sqrt(t)` scale is generic as PF-100 already proved, and PF-101 shows that the **local** `t^{1/4}` scale is generic at the level of a matched first Schwarzian jet as well.

The three-gap coefficient remains a useful exact geometric diagnostic. The exponent `1/4` does not survive the stricter RH-mechanism novelty/control gate.
