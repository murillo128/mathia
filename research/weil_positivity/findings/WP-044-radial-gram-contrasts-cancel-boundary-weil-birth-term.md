# WP-044 — radial Gram contrasts cancel the Prime-Circle boundary Weil birth term

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE` for the finite-dimensional radial-contrast/compression escape left open by `WP-036`. The positive primitive Prime-Circle radial Gram family admits a canonical cross-radius polarization, so any fixed finite linear combination of radii gives another unconditional positive Gram form. However, near the boundary the universal collision divergence and the finite arithmetic birth operator `C` occupy the **same radial common-mode tensor channel**. A radial contrast that removes the common collision mode therefore removes `C` as well; if the common mode is retained, `C` survives only behind the same divergent scalar identity term. Thus positive finite radial differencing, secant energies, or fixed finite radial Gram quotients cannot isolate the Weil-signed finite part while preserving geometric positivity.

This result sharpens the boundary identified in `WP-034`/`WP-036`. It does **not** rule out shell-dependent radial filters, unbounded cutoff-dependent contrasts, an infinite-dimensional radial/archimedean sector, a nonlinear determinant/intersection construction, or a genuinely nonseparable finite--archimedean coupling. Those escapes would have to break the common-mode factorization proved below rather than merely take a positive difference of the existing radial Gram states.

## 1. Canonical cross-radius polarization of the positive primitive Gram

On a fixed finite primitive-shell set `S`, `WP-036` gives the exact coefficientwise positive decomposition

\[
\boxed{
\widehat G_x
=\sum_{r\ge1}\frac{x^r}{r}\,u_r u_r^*,
\qquad 0<x<1,
}
\tag{1}
\]

where

\[
(u_r)_n=\frac{c_n(r)}{\sqrt{\varphi(n)}}.
\tag{2}
\]

Equation (1) has a canonical Hilbert-space polarization in the radial variable: use feature amplitude

\[
\Phi_x(r)=\frac{x^{r/2}}{\sqrt r}\,u_r.
\tag{3}
\]

Then the cross-radius Gram operator is forced to be

\[
\boxed{
\widehat G_{x,y}
:=\sum_{r\ge1}\frac{(xy)^{r/2}}r\,u_ru_r^*
=\widehat G_{\sqrt{xy}}.
}
\tag{4}
\]

For radii `x_1,...,x_k in (0,1)`, the block operator

\[
\mathbb K_X
:=\left[\widehat G_{\sqrt{x_ix_j}}\right]_{i,j=1}^k
\tag{5}
\]

is positive semidefinite. Indeed, with

\[
(v_r)_i=x_i^{r/2},
\]

one has the exact rank-one decomposition

\[
\boxed{
\mathbb K_X
=\sum_{r\ge1}\frac1r
(v_rv_r^*)\otimes(u_ru_r^*)\succeq0.
}
\tag{6}
\]

Equivalently, for every radial coefficient vector `a=(a_i)` the compression

\[
Q_{a,X}
:=(a^*\otimes I)\mathbb K_X(a\otimes I)
\tag{7}
\]

satisfies

\[
\boxed{
Q_{a,X}
=\sum_{r\ge1}\frac1r
\left|\sum_i a_i x_i^{r/2}\right|^2u_ru_r^*
\succeq0.
}
\tag{8}
\]

Thus radial differencing is not being dismissed because it lacks a sign theorem: the sign theorem is exact and elementary. The question is whether its positive boundary limit retains the arithmetic finite part.

## 2. Collision and arithmetic are locked to the same radial common mode

`WP-034` gives, on every fixed finite shell set,

\[
\boxed{
\widehat G_z
=L(z)I+C+o(1),
\qquad
L(z)=-\log(1-z),
\qquad z\to1^-.
}
\tag{9}
\]

Here `C` is the finite normalized Prime-Circle birth operator; on every interior prime-power ray it contains

\[
C_{dp^m,d}
=-\frac{\log p}{p^{m/2}}
=-\frac{\Lambda(p^m)}{\sqrt{p^m}}
\qquad(p\mid d).
\tag{10}
\]

Let every `x_i -> 1^-`. Since there are only finitely many cross radii, equation (9) applies uniformly over the finite set `sqrt(x_i x_j)`. Therefore

\[
\boxed{
\mathbb K_X
=\mathbb L_X\otimes I
+J_k\otimes C
+o(1),
}
\tag{11}
\]

where

\[
(\mathbb L_X)_{ij}
=L(\sqrt{x_ix_j}),
\qquad
J_k=\mathbf1\mathbf1^*.
\tag{12}
\]

The key point is structural: the same matrix `C` occurs in **every** radial block. Hence its radial tensor factor is exactly the rank-one common-mode matrix `J_k`.

Compressing (11) by a fixed `a` gives

\[
\boxed{
Q_{a,X}
=\ell_a(X)I
+|\mathbf1^*a|^2C
+o(1),
}
\tag{13}
\]

with

\[
\ell_a(X)
:=a^*\mathbb L_Xa\ge0.
\tag{14}
\]

The inequality in (14) is itself exact: from the scalar log-series,

\[
\mathbb L_X
=\sum_{r\ge1}\frac1r v_rv_r^*\succeq0.
\tag{15}
\]

Equation (13) is the obstruction. The arithmetic finite part and the divergent collision background are not two independent radial channels that a positive finite-dimensional rotation can separate. The arithmetic part lives in the same common radial direction as the zeroth-order collision mode.

## 3. Every zero-sum radial contrast kills the arithmetic term

Suppose

\[
\boxed{\mathbf1^*a=0.}
\tag{16}
\]

Then (13) reduces to

\[
\boxed{
Q_{a,X}=\ell_a(X)I+o(1).
}
\tag{17}
\]

The entire finite arithmetic operator `C` cancels. This includes all fixed finite-difference operators whose coefficients sum to zero and, more generally, the whole radial contrast subspace `\mathbf1^\perp`.

A particularly transparent two-radius example is

\[
D_{x,y}
:=\widehat G_x+\widehat G_y
-2\widehat G_{\sqrt{xy}}.
\tag{18}
\]

By (1),

\[
\boxed{
D_{x,y}
=\sum_{r\ge1}\frac{(x^{r/2}-y^{r/2})^2}{r}\,u_ru_r^*
\succeq0.
}
\tag{19}
\]

Yet equation (9) gives

\[
D_{x,y}
=\left[
L(x)+L(y)-2L(\sqrt{xy})
\right]I+o(1),
\tag{20}
\]

with **no `C` term at all**.

Thus the most canonical positive radial secant energy removes exactly the arithmetic information that one hoped differencing would expose.

## 4. Comparable boundary approaches leave only a universal positive scalar contrast

The previous cancellation needs no relation between the rates at which the radii approach the boundary. A sharper limit is available when

\[
x_i=1-c_i\varepsilon+o(\varepsilon),
\qquad c_i>0,
\qquad \varepsilon\downarrow0.
\tag{21}
\]

Then

\[
1-\sqrt{x_ix_j}
=\frac{c_i+c_j}{2}\varepsilon+o(\varepsilon),
\tag{22}
\]

and therefore

\[
\boxed{
L(\sqrt{x_ix_j})
=-\log\varepsilon
-\log\frac{c_i+c_j}{2}
+o(1).
}
\tag{23}
\]

Set

\[
B(c)_{ij}
:=-\log\frac{c_i+c_j}{2}.
\tag{24}
\]

Then

\[
\boxed{
\mathbb K_X
=(-\log\varepsilon)J_k\otimes I
+B(c)\otimes I
+J_k\otimes C
+o(1).
}
\tag{25}
\]

On the contrast subspace `\mathbf1^\perp`, both terms carrying `J_k` vanish. The finite boundary limit is therefore

\[
\boxed{
\mathbb K_X|_{\mathbf1^\perp}
\longrightarrow
B(c)|_{\mathbf1^\perp}\otimes I.
}
\tag{26}
\]

It is universal in shell space.

The remaining scalar radial form is indeed nonnegative. For `\sum_i a_i=0`, the elementary logarithm integral gives

\[
\begin{aligned}
a^*B(c)a
&=\int_0^\infty
\frac{\left|\sum_i a_i e^{-c_it/2}\right|^2}{t}\,dt\\
&\ge0.
\end{aligned}
\tag{27}
\]

The integral is finite: the zero-sum condition makes the numerator `O(t^2)` at the origin, and exponential decay handles infinity.

For the two-radius contrast `a=(1,-1)`, (26) becomes the explicit scalar limit

\[
\boxed{
D_{1-c\varepsilon,\,1-d\varepsilon}
\longrightarrow
\log\frac{(c+d)^2}{4cd}\,I
\succeq0,
}
\tag{28}
\]

by the arithmetic-geometric mean inequality. The positivity survives perfectly; the arithmetic does not.

## 5. Retaining the common mode retains the divergence

For a fixed radial vector with

\[
s:=\mathbf1^*a\ne0,
\tag{29}
\]

equations (13) and (23) give

\[
\boxed{
Q_{a,X}
=(-\log\varepsilon)|s|^2I
+(a^*B(c)a)I
+|s|^2C
+o(1).
}
\tag{30}
\]

Thus the coefficient of `C` is nonzero exactly when the common collision mode is retained. But in that case the same coefficient multiplies a positive scalar divergence of size `log(1/epsilon)`.

Consequently there is a strict fixed-finite-dimensional dichotomy:

```text
annihilate the radial common mode
    -> positive finite contrast survives
    -> C vanishes;

retain the radial common mode
    -> C survives
    -> the positive scalar collision term diverges.
```

Extracting `C` in the second branch still requires the scalar subtraction already identified in `WP-034`/`WP-036`, and that subtraction exposes an operator unbounded below on cofinal prime-power boxes.

The same conclusion holds for any **bounded** family of coefficients `a(ε)` in a fixed finite radial space. If `|1^*a(ε)|` stays bounded away from zero, the common scalar term diverges. If `1^*a(ε)->0`, the coefficient of `C` in (13) tends to zero. A singular unbounded family of cutoff-dependent coefficients is deliberately outside this claim.

## 6. Basis-invariant finite radial compression cannot separate the channels

Equation (11) is not an artifact of choosing a particular contrast basis. Let `R` be any fixed finite radial mixing/compression matrix. Then

\[
(R^*\otimes I)\mathbb K_X(R\otimes I)
=
(R^*\mathbb L_XR)\otimes I
+(R^*J_kR)\otimes C
+o(1).
\tag{31}
\]

Under the comparable scaling (21),

\[
R^*\mathbb L_XR
=(-\log\varepsilon)R^*J_kR
+R^*B(c)R+o(1).
\tag{32}
\]

Hence the divergent identity term and `C` have the **same radial range** `Ran(R^*J_kR)`. Any fixed projection or quotient that annihilates that radial rank-one range annihilates both. Any fixed compression that keeps it keeps both.

This closes a concrete escape left by `WP-036`: enlarging the positive radial Gram to finitely many nearby radii and then taking a sign-preserving linear contrast cannot geometrically subtract the collision background while retaining the finite Weil birth operator.

It also explains why the obstruction is different from `WP-026`. `WP-026` concerns Schur/Kron closure of passive spatial networks. Here the starting object is already a positive Prime-Circle radial Gram kernel, and the no-go comes from an exact **boundary tensor factorization** of its multiscale polarization.

## 7. Consequence for radial derivatives and Fisher/secant ideas

For every fixed pair `x,y`, equation (19) is the squared Hilbert distance between the two radial feature states. It is therefore the direct secant analogue of a radial metric or Fisher-type energy. Finite-difference approximants to a radial derivative use zero-sum coefficients and fall under (16)--(17): the boundary constant term `C` is annihilated before any sign issue arises.

One should not infer from this alone that every singularly rescaled radial derivative has a universal limit; differentiating an `o(1)` boundary remainder requires additional estimates. The exact conclusion is narrower and sufficient: **the arithmetic operator `C` cannot come from the constant boundary finite part of any bounded fixed finite radial contrast**, because that finite part is multiplied by `|sum a_i|^2` and vanishes for every derivative-like zero-sum filter.

Any higher-order radial scheme that recovers arithmetic from a smaller remainder would therefore be a new asymptotic mechanism with a new normalization, not a hidden positivity of the already-derived boundary birth term.

## 8. Archimedean/global implication

`WP-036` remains the strongest same-parent finite/archimedean bridge: a Mellin diagonal of the positive radial family contains the Riemann `psi(s/2)` scale, while its boundary finite part contains the critical finite-prime coefficients through `C`.

The present result shows that **finite radial ancillae cannot merge those two readouts by positive background cancellation**. The collision mode and `C` are locked together before the boundary limit. Removing that radial common mode leaves a universal scalar shell identity, not a finite-prime pairing to which the `q=2` Mellin channel could be attached.

This strengthens the surviving design requirement already visible in `WP-043`: a successful construction must introduce mixing that is not scalar and not separable in the existing shell/radial tensor product. Plausible remaining categories include a shell-dependent radial response, an infinite-dimensional archimedean boundary sector, a singular unbounded compression with an independently proved sign theorem, a nonlinear global determinant/intersection object, or a cohomological pairing formed before finite and archimedean pieces are extracted.

## 9. Matched controls and novelty audit

The general facts used above are standard Hilbert-space geometry: Gram kernels remain positive under finite block formation and congruence, and the logarithmic kernel in (27) has an elementary Laplace representation on the zero-sum subspace. No novelty is claimed for positive-definite kernels, radial secant energies, or conditionally positive logarithmic kernels.

The closest Weil-positivity comparison already recorded in `SOURCES.md` is Connes--Consani's archimedean compression mechanism. Their sign theorem comes from compressing the scaling action to the orthogonal complement of phase-space cutoff projections and controlling the resulting trace with Sonin/prolate/Toeplitz structure. The present calculation neither reproduces nor rules out that mechanism. It shows only that the much simpler Mathia-native proposal

```text
positive Prime-Circle radial Gram
    -> finitely many radii
    -> positive radial contrast / fixed compression
    -> cancel universal collision background
    -> retain C
```

fails exactly at the last step.

The obstruction is also deliberately non-RH-specific. Any positive feature family with a common boundary expansion

\[
G_z=L(z)I+C+o(1)
\]

and geometric-mean cross polarization has the same common-mode cancellation. This universality is itself a matched control: positivity of radial contrasts cannot distinguish the Riemann arithmetic from another system with the same boundary architecture.

The Mathia-specific durable content is the identification, using the exact `WP-036` feature system and `WP-034` birth asymptotic, that **the actual Prime-Circle finite arithmetic operator shares the radial common mode with the collision divergence**.

## 10. Boundary and exact falsification tests

This finding is falsified by any failure of the following checks on a fixed finite shell set:

1. `WP-036`'s coefficientwise identity (1) holds;
2. its canonical feature polarization gives `G_{x,y}=G_{sqrt(xy)}`;
3. the resulting finite radial block kernel (6) is positive;
4. `WP-034`'s boundary expansion (9) holds at every cross radius approaching one;
5. summing the common `C` term over radial coefficients gives exactly `|sum a_i|^2 C`;
6. every zero-sum fixed contrast therefore cancels `C`;
7. under `x_i=1-c_i epsilon+o(epsilon)`, equation (23) holds and the contrast limit is `B(c)|_{1^perp} tensor I`;
8. the integral representation (27) makes that surviving radial scalar form nonnegative;
9. any fixed radial compression has the common-mode factorization (31)--(32).

The claim does **not** cover:

- radial weights depending on shell/conductor;
- unbounded or singular cutoff-dependent coefficient families;
- infinitely many radial channels with a nontrivial limiting topology;
- nonlinear operations such as determinants before boundary extraction;
- nonseparable finite--archimedean operators that change the tensor factorization;
- or cohomological/intersection constructions with an independent sign theorem.

Those are genuine remaining routes. What is now closed is the natural attempt to rescue `WP-036` by ordinary finite positive radial differencing: the operation that removes the universal background removes the finite Weil birth term with it.
