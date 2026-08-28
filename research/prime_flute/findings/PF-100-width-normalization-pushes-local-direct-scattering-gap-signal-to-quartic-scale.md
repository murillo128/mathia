# PF-100 — width normalization pushes the local direct-scattering gap signal to quartic scale

**Status:** `EXACT-DERIVED` + `CANDIDATE-NEW-STRUCTURE` for the canonical direct identity-double-coset sector, with a `NEGATIVE/CONTROL` result for the tempting `sqrt(t)` high-energy analogy. This is **not** a theorem about the full physical scattering matrix of the infinite flute and does not identify any Riemann zeros.

## Claim

PF-086/PF-087 introduced the width-one normalized direct cusp-scattering denominator

\[
C_{ij}^{\bullet}
=
\sqrt{W_i^{\bullet}W_j^{\bullet}}\,
|x_j^{\bullet}-x_i^{\bullet}|,
\qquad \bullet\in\{E,0\},
\]

for the exact endpoint geometry

\[
x_n^E=V(p_n)=\pi\cot\frac{\pi}{p_n}
\]

and its projective reference

\[
x_n^0=p_n.
\]

For a fixed finite local pattern, width normalization cancels the first two apparent exact/reference distortion orders. More precisely, let two marked cusps lie at

\[
x=P+r,
\qquad
y=P+s,
\qquad r<s,
\]

with fixed positive reference gaps `a,b` immediately to the left/right of `x` and `c,d` immediately to the left/right of `y`. Then, as `P -> infinity`,

\[
\boxed{
\log\frac{C_{xy}^E}{C_{xy}^0}
=
-\frac{\pi^2}{6P^4}
\Big((s-r)^2+ab+cd\Big)
+O(P^{-5}).
}
\tag{1}
\]

In particular, for four consecutive prime positions

\[
p_{n-1}<p_n<p_{n+1}<p_{n+2}
\]

with fixed local gaps

\[
X=p_n-p_{n-1},\qquad
Y=p_{n+1}-p_n,\qquad
Z=p_{n+2}-p_{n+1},
\]

the direct channel between the two middle cusps satisfies

\[
\boxed{
\delta_n
:=
\log\frac{C_{n,n+1}^E}{C_{n,n+1}^0}
=
-\frac{\pi^2}{6p_n^4}
Y(X+Y+Z)
+O(p_n^{-5}).
}
\tag{2}
\]

The same quadratic three-gap form is the numerator of the exact projective cross-ratio coordinate from PF-004:

\[
\chi
=
\frac{Y(X+Y+Z)}{XZ}.
\]

Thus the first surviving local exact/reference defect of this **canonical scattering-geometric quantity** is relational and multi-gap; the one-point `p^{-2}` distortion of `V` disappears after the cusp widths are normalized.

Evaluating the elementary direct factor on the physical spectral line,

\[
s=\frac12+it,
\]

gives

\[
\left(\frac{C_{n,n+1}^E}{C_{n,n+1}^0}\right)^{-2s}
=
\exp(-\delta_n)\exp(-2it\delta_n).
\]

Consequently, along a fixed local pattern and the quartic scaling

\[
t=\tau p_n^4,
\]

its amplitude tends to one while its direct-sector phase has the nontrivial limit

\[
\boxed{
\exp(-2it\delta_n)
\longrightarrow
\exp\!\left(
 i\frac{\pi^2}{3}\tau Y(X+Y+Z)
\right).
}
\tag{3}
\]

Equivalently, the first local gap-sensitive phase of this direct channel becomes order one at

\[
\boxed{p\asymp t^{1/4}.}
\]

This `t^{1/4}` scale must not be confused with the unrelated half-plane threshold `Re s=1/4` in PF-084/PF-086/PF-087.

There is also a decisive control. For two **nonlocal** cusps with coordinates `x<y`, `x,y -> infinity`, `y/x -> lambda>1`, and local gaps negligible compared with `x,y`,

\[
\boxed{
\log\frac{C_{xy}^E}{C_{xy}^0}
=
-\frac{\pi^2}{6}
\left(\frac1x-\frac1y\right)^2
+o(x^{-2}).
}
\tag{4}
\]

That term becomes order one at `x ~ sqrt(t)`, but it contains **no prime-gap information at leading order** and persists for generic endpoint deformations `F(x)=x-a/x+O(x^{-3})`. Therefore a `sqrt(t)` scale in this direct scattering geometry is background kinematics, not a prime-flute analogue of the Riemann--Siegel cutoff.

## 1. Exact endpoint expansion

Write

\[
A=\frac{\pi^2}{3},
\qquad
B=\frac{\pi^4}{45}.
\]

The cotangent expansion gives

\[
\boxed{
V(x)
=x-\frac{A}{x}-\frac{B}{x^3}+O(x^{-5}).
}
\tag{5}
\]

For a cusp at reference position `x`, let its fixed left and right gaps be `a,b>0`. The reference and exact gaps are

\[
\Delta_-^0=a,
\quad
\Delta_+^0=b,
\]

and

\[
\Delta_-^E=V(x)-V(x-a),
\quad
\Delta_+^E=V(x+b)-V(x).
\]

The primitive parabolic width used in PF-019/PF-086 is

\[
W^{\bullet}(x;a,b)
=2\left(
\frac1{\Delta_-^{\bullet}}+
\frac1{\Delta_+^{\bullet}}
\right).
\tag{6}
\]

Expanding (5) in (6) and then taking the logarithm gives

\[
\boxed{
\log\frac{W^E(x;a,b)}{W^0(a,b)}
=
-\frac{A}{x^2}
+
\frac{A^2/2-Aab-3B}{x^4}
+O(x^{-5}).
}
\tag{7}
\]

The `x^{-3}` term cancels **exactly**. This is the first important cancellation: left and right gap distortions are asymmetric at order `x^{-3}`, but the harmonic cusp-width normalization removes that odd contribution.

## 2. The two-cusp cancellation

For

\[
x=P+r,
\qquad
y=P+s,
\]

the exact/reference long divided difference has expansion

\[
\log
\frac{V(P+s)-V(P+r)}{s-r}
=
\frac{A}{P^2}
-
\frac{A(r+s)}{P^3}
+
\frac{-A^2/2+A(r^2+rs+s^2)+3B}{P^4}
+O(P^{-5}).
\tag{8}
\]

By definition,

\[
\log\frac{C_{xy}^E}{C_{xy}^0}
=
\frac12
\log\frac{W^E(P+r;a,b)}{W^0(a,b)}
+
\frac12
\log\frac{W^E(P+s;c,d)}{W^0(c,d)}
+
\log
\frac{V(P+s)-V(P+r)}{s-r}.
\tag{9}
\]

Expanding the two copies of (7) about the common base `P` and adding (8), the coefficients of

\[
P^{-2},
\qquad
P^{-3},
\qquad
A^2P^{-4},
\qquad
BP^{-4}
\]

all cancel. The surviving coefficient is

\[
-\frac{A}{2}
\left((s-r)^2+ab+cd\right),
\]

which proves (1).

The cancellation is structurally important. The endpoint map itself differs from the identity at order `P^{-1}`, its derivative at order `P^{-2}`, and each individual normalized cusp width at order `P^{-2}`. Yet a normalized **two-cusp** direct scattering denominator first distinguishes the exact cotangent geometry locally at order `P^{-4}`.

This matches the projective lesson of PF-082: the first finite-scale Möbius-invariant defect of `V` is governed by

\[
S(V)(P)=\frac{2\pi^2}{P^4}.
\]

Equation (1) is not just another Schwarzian expansion, however. It identifies the specific quadratic local geometry that survives inside the actual width-normalized direct cusp-scattering coordinate.

## 3. Consecutive prime specialization

Use the local four-point configuration

\[
P,
\quad
P+X,
\quad
P+X+Y,
\quad
P+X+Y+Z.
\]

For the channel between the middle two cusps,

\[
r=X,
\qquad
s=X+Y,
\]

and the adjacent-gap products in (1) are

\[
ab=XY,
\qquad
cd=YZ.
\]

Hence

\[
(s-r)^2+ab+cd
=Y^2+XY+YZ
=Y(X+Y+Z),
\]

which yields (2). Replacing the common base `P=p_{n-1}` by `p_n=P+X` changes only the `O(P^{-5})` remainder for a fixed pattern.

PF-004 gives for the same four ordered points

\[
\sinh^2\frac{L}{4}
=
\chi
=
\frac{Y(X+Y+Z)}{XZ}.
\]

Thus the scattering defect coefficient contains the same projective three-gap numerator as the canonical separating geodesic, while the exact cotangent correction supplies its absolute finite-scale weight `p^{-4}`.

This combination is precisely what PF-099 says a genuinely new geometric signal must do: retain relational gap shape **and** break the global projective dilation gauge.

## 4. Direct-sector high-energy phase

For one direct identity-double-coset term, the Gamma-factor-stripped elementary contribution has the standard form

\[
(C_{ij})^{-2s}.
\]

Its exact/reference ratio is therefore

\[
\exp(-2s\delta_{ij}),
\qquad
\delta_{ij}=\log(C_{ij}^E/C_{ij}^0).
\]

On `s=1/2+it`, equations (2)--(3) follow directly. No analytic continuation theorem is needed for this **elementary factor** itself.

This wording is deliberate. In the standard finite-cusp domain `Re s>1`, the factor occurs termwise in the scattering Dirichlet series. On the physical line, the complete scattering coefficient is obtained only after continuation, and there is no theorem allowing the full infinite-cusp physical matrix to be decomposed termwise there. Equation (3) is therefore a direct-sector scaling law, not a claim that the full scattering matrix has the same asymptotic phase.

PF-016 supplies a further hard boundary: if the exact/reference full physical relative scattering operator can eventually be constructed with the expected unitarity and trace-class hypotheses, its Fredholm determinant on the physical line is a phase of modulus one and has no zeros there. Thus (3) cannot by itself be promoted into a Riemann-zero mechanism.

## 5. Nonlocal `sqrt(t)` control

A potentially misleading phenomenon appears when the two cusps are macroscopically separated.

Let `x<y`, with `y/x -> lambda>1`. From (5),

\[
\frac{V(y)-V(x)}{y-x}
=
1+\frac{A}{xy}+o(x^{-2}),
\]

so

\[
\log\frac{V(y)-V(x)}{y-x}
=
\frac{A}{xy}+o(x^{-2}).
\tag{10}
\]

At the two endpoints, (7) gives

\[
\frac12\log\frac{W_x^E}{W_x^0}
+
\frac12\log\frac{W_y^E}{W_y^0}
=
-\frac{A}{2x^2}
-\frac{A}{2y^2}
+o(x^{-2}).
\tag{11}
\]

Combining (10)--(11),

\[
\delta_{xy}
=
-\frac{A}{2}
\left(\frac1x-\frac1y\right)^2
+o(x^{-2}),
\]

which is (4).

At spectral height `t`, the associated elementary phase becomes order one for

\[
x\asymp\sqrt t.
\]

That scale superficially resembles the `sqrt(t)` truncation scale in the classical Riemann--Siegel formula. The resemblance fails the control experiment. Replace `V` by any smooth deformation

\[
F_a(x)=x-\frac{a}{x}+O(x^{-3}).
\]

The same width-normalization calculation gives

\[
\log\frac{C_{xy}^{F_a}}{C_{xy}^0}
=
-\frac{a}{2}
\left(\frac1x-\frac1y\right)^2
+o(x^{-2}).
\]

No prime gaps enter. Therefore

\[
\boxed{
\text{the nonlocal }\sqrt t\text{ scale is generic endpoint kinematics, not prime arithmetic.}
}
\]

The local `t^{1/4}` signal in (3) is qualitatively different because width normalization has canceled those universal one-point terms and exposed the first projectively intrinsic multi-gap correction.

## 6. Relation to the cuff coordinates

The distinguished cuff law

\[
\ell_n
=2\log\frac{4p_n}{g_{n-1}}+o(1)
\]

shows why no one-cuff term could have produced (2): its leading exact/reference finite-scale correction contains a large universal component, while the projective gap information enters through ratios and differences of several cuffs.

For the four-point block,

\[
Y(X+Y+Z)
= XZ\,\sinh^2\frac{L}{4},
\]

where `L` is the canonical multi-gap separator from PF-004. Hence (2) can equally be read as

\[
\delta_n
=
-\frac{\pi^2}{6p_n^4}
XZ\,\sinh^2\frac{L}{4}
+O(p_n^{-5}).
\]

This is an exact finite-scale coupling between the prime-circle endpoint defect and a genuine hyperbolic separator. It does **not** contradict PF-097/PF-099: the tangent length `L` alone is projective and primality-blind; the additional `p_n^{-4}` coefficient is precisely the scale information discarded by the tangent normalization.

## 7. Interior/exterior duality

`C_{ij}` is built from cusp width normalization and a lower-left/sojourn denominator. The ambient interior/exterior realization changes the Fuchsian picture by the same Möbius conjugation/relabeling already discussed in PF-017/PF-086. Ratios such as `C_{ij}^E/C_{ij}^0`, and therefore (1)--(4), are unchanged after the corresponding normalization.

The quartic defect is therefore compatible with the exact interior/exterior duality; it is not produced by choosing one side of the orthogonal-circle picture.

## 8. Prior art and novelty audit

Known ingredients are not claimed as new:

1. width-one cusp scaling and the `|c|^{-2s}` double-coset expansion of finite-cusp hyperbolic scattering coefficients are standard;
2. high-frequency scattering phases and their relation to scattering geodesics/sojourn times are classical; a foundational reference is V. Guillemin, *Sojourn Times and Asymptotic Properties of the Scattering Matrix*, Publ. RIMS 12 Suppl. (1976/77), 69--88, DOI `10.2977/PRIMS/1195196598`;
3. later microlocal work, including A. Sá Barreto and J. Wunsch, *The radiation field is a Fourier integral operator*, Ann. Inst. Fourier 55 (2005), places sojourn-time/scattering relations in a general Fourier-integral framework;
4. Taylor/Schwarzian cross-ratio distortion is classical projective analysis;
5. the `sqrt(t)` scale in the Riemann--Siegel formula is classical and is used here only as an adversarial comparison.

Directed searches for width-normalized cusp scattering combined with the specific endpoint deformation `pi cot(pi/x)`, prime-gap four-point geometry, Schwarzian corrections, and countably-cusped flutes did not locate (1) or (2). Searches by the equivalent structures `sojourn denominator`, `cusp scaling`, `Schwarzian`, and `cross-ratio` likewise found the general scattering/sojourn theory but not this cancellation pattern.

The candidate-new part is therefore narrowly stated as

\[
\boxed{
\pi\cot(\pi/x)
+\text{ canonical cusp-width normalization}
+\text{ local direct scattering}
\Longrightarrow
\text{ cancellation through }P^{-3}
\text{ and the }P^{-4}\text{ three-gap form (2)}.
}
\]

No novelty is claimed for any individual ingredient or for general scattering asymptotics.

## 9. Failure modes and falsification tests

The finite asymptotic core is directly falsifiable:

1. expand `V(P+r)`, both endpoint cusp widths, and the long divided difference independently to order `P^{-4}`;
2. verify that the `P^{-2}` and `P^{-3}` terms cancel and that the coefficient of `P^{-4}` is exactly
   \[
   -\frac{\pi^2}{6}\big((s-r)^2+ab+cd\big);
   \]
3. for consecutive gaps verify the specialization to `-pi^2 Y(X+Y+Z)/(6P^4)`.

The main analytic failure mode is more important: non-direct double cosets in the full physical scattering coefficient may alter or cancel the direct-sector phase. PF-061/PF-078 describe the separate remainder problem in degenerating finite blocks, but they do not prove a global termwise high-energy expansion for the infinite-cusp flute.

Further limitations:

- a fixed local gap pattern remains projectively clonable and does not certify primality (PF-097/PF-099);
- (3) is not a zero statement and supplies no functional equation;
- the `t^{1/4}` scaling is a **spectral-height scaling of one direct factor**, not the `Re s=1/4` Schatten/abscissa boundary;
- the full physical relative determinant, if unitary and trace class on the critical line, is zero-free there by PF-016.

## 10. Consequences for the prime-flute line

This result sharpens the separation already suggested by PF-082, PF-088 and PF-099:

```text
nonlocal direct channel:
    first exact/reference phase ~ t / p^2
    order-one scale p ~ sqrt(t)
    universal; no leading gap information

local width-normalized direct channel:
    p^-2 and p^-3 defects cancel
    first surviving relational coefficient ~ Y(X+Y+Z) / p^4
    order-one scale p ~ t^(1/4)
    exact finite-scale multi-gap geometry
```

The useful positive conclusion is modest but concrete: **canonical cusp normalization automatically strips the universal low-order endpoint deformation and exposes a genuine three-gap finite-scale coefficient.**

The equally important negative conclusion is that a `sqrt(t)` high-energy scale in the same direct sector cannot be used as evidence for a Riemann--Siegel-type mechanism; that scale survives a featureless smooth control and erases the prime gaps.

Any future scattering candidate should therefore be tested against both controls before being promoted:

\[
\boxed{
\text{Does it survive width normalization as a multi-gap invariant?}
\qquad
\text{Does it disappear for }F(x)=x-a/x+O(x^{-3})\text{ controls?}
}
\]
