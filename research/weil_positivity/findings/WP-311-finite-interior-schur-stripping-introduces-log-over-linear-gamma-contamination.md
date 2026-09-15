---
id: WP-311
title: Finite interior Schur stripping introduces a logarithmic-over-linear defect before the Gamma curvature
branch: weil_positivity
status: supported
kind: finite-reference-schur-log-end-obstruction
claim_strength: exact asymptotic obstruction for the canonical scalar one-point Schur reduction and every finite end-normalized chain at fixed interior reference points; preserving the unit logarithmic Herglotz end forces a strictly positive (log y)/y term, whereas the Riemann Gamma channel has no such term
created: 2026-09-15
related: [WP-305, WP-308, WP-309, WP-310]
prior_art:
  - Schwarz--Pick lemma and the classical Schur algorithm for scalar Schur functions
  - Laurent Baratchart, Stanislav Kupin, Vincent Lunot, and Martine Olivi, Multipoint Schur algorithm and orthogonal rational functions. I: Convergence properties, Journal d'Analyse Mathématique 114 (2011/2012), 1-43, DOI 10.1007/s11854-011-0016-9, arXiv:0812.2050, for Schur reduction at arbitrary interior interpolation points
  - Daniel Alpay, Aad Dijksma, and Heinz Langer, The Schur transformation for Nevanlinna functions: operator representations, resolvent matrices, and orthogonal polynomials, Operator Theory: Advances and Applications 190 (2009), 27-63, arXiv:0711.4236, for the distinct moment/asymptotic-at-infinity Schur transformation audited in WP-310
---

# WP-311 — Finite interior Schur stripping introduces a logarithmic-over-linear defect before the Gamma curvature

## Claim

`WP-310` closes the classical moment-Schur step at infinity for the critical Mangoldt Herglotz source but deliberately leaves **finite-reference interpolation transforms** open. The canonical scalar finite-point Schur reduction can be tested exactly, and it fails more strongly than the infinity step: after the unique positive affine normalization that preserves the unit logarithmic end, it creates a new positive `log(y)/y` term. The Riemann Gamma channel has no term of that order.

Let `f:H->H` be a scalar Herglotz function with

\[
\operatorname{Re}f(iy)
=
\log y+c+A\frac{\log y}{y}+O(y^{-1}),
\qquad
\operatorname{Im}f(iy)
=
q+O\!\left(\frac{(\log y)^2}{y}\right),
\tag{1}
\]

where `q>0`. Fix an interior interpolation point

\[
a=u+iv\in\mathbb H,
\qquad
f(a)=\xi+i\eta,
\qquad v,\eta>0.
\tag{2}
\]

Use the half-plane Blaschke factors normalized to tend to one at infinity,

\[
b_a(z)=\frac{z-a}{z-\bar a},
\qquad
c_{f(a)}(w)=\frac{w-f(a)}{w-\overline{f(a)}}.
\tag{3}
\]

Schwarz--Pick gives

\[
s_a(z):=
\frac{c_{f(a)}(f(z))}{b_a(z)}
\in\overline{\mathbb D},
\tag{4}
\]

with the removable value at `z=a`; this is the standard one-point interior Schur stripping step up to harmless unimodular phase conventions. Return the boundary value `s_a(iy)->1` to the Herglotz infinite end by

\[
R_a[f](z)=i\frac{1+s_a(z)}{1-s_a(z)}.
\tag{5}
\]

Then the exact algebraic identity is

\[
R_a[f](z)
=
\frac{(z-u)(f(z)-\xi)+\eta v}
{\eta(z-u)-v(f(z)-\xi)}.
\tag{6}
\]

The leading logarithmic coefficient of `R_a[f]` is `1/eta`. Hence every positivity-preserving output normalization that restores coefficient one and keeps the same infinite end is, up to a real constant,

\[
\mathcal S_a[f](z)=\eta R_a[f](z)+\beta,
\qquad \beta\in\mathbb R.
\tag{7}
\]

For every such normalization,

\[
\boxed{
\operatorname{Re}\mathcal S_a[f](iy)
=
\log y+c'
+\left(A+\frac{2qv}{\eta}\right)\frac{\log y}{y}
+O(y^{-1}).
}
\tag{8}
\]

Moreover

\[
\operatorname{Im}\mathcal S_a[f](iy)
=
q+O\!\left(\frac{(\log y)^2}{y}\right),
\tag{9}
\]

so the same statement iterates. After any finite chain of fixed interior Schur stripping steps at `a_j=u_j+iv_j`, each followed by unit-log end normalization, one obtains

\[
\boxed{
A_N=A_0+2q\sum_{j=1}^N\frac{v_j}{\eta_j},
\qquad
\eta_j:=\operatorname{Im}f_{j-1}(a_j)>0.
}
\tag{10}
\]

In particular every nonempty finite chain adds a **strictly positive** logarithmic-over-linear coefficient.

For the reflected critical Mangoldt response `m_-` of `WP-305`,

\[
A_0=0,
\qquad q=\frac\pi2,
\tag{11}
\]

because

\[
m_-(iy)
=
\log y-B+\frac{A_{\rm M}}{y^2}+o(y^{-2})
+i\left(\frac\pi2+\frac{C_+}{y}+o(y^{-1})\right),
\qquad A_{\rm M}>0.
\tag{12}
\]

Therefore one finite interior Schur strip already forces

\[
\operatorname{Re}\mathcal S_a[m_-](iy)
=
\log y+c_a
+\frac{\pi v}{\eta}\frac{\log y}{y}
+O(y^{-1}),
\qquad \frac{\pi v}{\eta}>0,
\tag{13}
\]

and a finite chain forces the positive coefficient

\[
\pi\sum_{j=1}^N\frac{v_j}{\eta_j}>0.
\tag{14}
\]

By contrast the Riemann archimedean term has

\[
\operatorname{Re}\psi\!\left(\frac14+\frac{iy}{2}\right)
=
\log\frac y2-\frac1{24y^2}+O(y^{-4}),
\tag{15}
\]

with **no** `log(y)/y` contribution. Thus canonical finite interior Schur stripping does not repair the `WP-305` curvature mismatch. It introduces an earlier asymptotic defect before the `y^-2` Gamma curvature is even reached.

**Classification:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + FINITE-REFERENCE-SCHUR-NO-GO + LOG-END-ASYMPTOTIC-RIGIDITY + SOURCE-PHASE-DEPENDENT + FINITE-CHAIN-STABILITY + MATCHED-CONTROLS + CLASSICAL-SCHUR-PRIOR-ART + NOT-WEIL-POSITIVITY`.

## 1. The finite-point reduction is forced by Schwarz--Pick

For `a in H`, both maps in (3) are biholomorphisms from the upper half-plane to the disk, with

\[
b_a(a)=0,
\qquad
c_{f(a)}(f(a))=0.
\tag{16}
\]

The invariant Schwarz--Pick inequality gives

\[
\left|c_{f(a)}(f(z))\right|
\le
|b_a(z)|.
\tag{17}
\]

Hence their quotient in (4) extends holomorphically through `a` and is Schur-class. This is exactly the scalar one-node reduction underlying the Schur/Nevanlinna--Pick algorithm, written in half-plane coordinates and normalized so both factors approach one at the high-energy end.

Different unimodular phase conventions do not create extra asymptotic freedom. They merely rotate the disk coordinate. Once the limiting boundary point is sent back to infinity, any two resulting Herglotz coordinates differ by an upper-half-plane automorphism fixing infinity, hence by a positive affine map. `WP-308` then says that retaining unit logarithmic growth fixes the positive scale, leaving only an additive real constant. Thus (7) captures the whole end-preserving scalar output freedom relevant to the Gamma comparison.

## 2. Exact rational form of the reduced Herglotz response

Write

\[
a=u+iv,
\qquad
f(a)=\xi+i\eta.
\tag{18}
\]

Substituting (3)-(4) into (5) and clearing denominators gives

\[
1-s_a(z)
=
\frac{2i\bigl(\eta(z-u)-v(f(z)-\xi)\bigr)}
{(f(z)-\xi+i\eta)(z-u-iv)},
\tag{19}
\]

while the corresponding numerator yields (6). No asymptotic approximation enters this identity.

The denominator in (6) is not an arbitrary fitted counterterm. Its two terms are forced respectively by the input interpolation height `v` and the positive output height `eta=Im f(a)`. The resulting map remains Herglotz because it was obtained by a Schur-class reduction followed by a Cayley inverse.

For the critical Mangoldt source, `f` is not a half-plane automorphism, so the reduction is nondegenerate. The exceptional equality case of Schwarz--Pick would make `s_a` unimodular constant and corresponds to an automorphism, which is already incompatible with the logarithmic source asymptotic.

## 3. The `log(y)/y` coefficient is exact and positive

Put

\[
L(y):=\operatorname{Re}f(iy)-\xi,
\qquad
Q(y):=\operatorname{Im}f(iy).
\tag{20}
\]

From (6), direct multiplication by the conjugate denominator gives

\[
\operatorname{Re}R_a[f](iy)
=
\frac{N(y)}{D(y)},
\tag{21}
\]

where

\[
\begin{aligned}
N(y)
={}&
\eta y^2L
+uv\bigl(L^2+Q^2-\eta^2\bigr)
+\eta(u^2-v^2)L,
\\
D(y)
={}&
\eta^2y^2-2\eta vQy
+v^2(L^2+Q^2)
+2\eta uvL+\eta^2u^2.
\end{aligned}
\tag{22}
\]

Under (1), `L=log y+O(1)` and `Q=q+O((log y)^2/y)`. Therefore

\[
N(y)=\eta y^2L+O((\log y)^2),
\tag{23}
\]

and

\[
D(y)
=
\eta^2y^2
\left(
1-\frac{2vq}{\eta y}
+O\!\left(\frac{(\log y)^2}{y^2}\right)
\right).
\tag{24}
\]

Multiplying (21) by `eta` and expanding the reciprocal of (24) gives

\[
\operatorname{Re}\bigl(\eta R_a[f](iy)\bigr)
=
L(y)
+\frac{2vq}{\eta}\frac{L(y)}{y}
+O(y^{-1}).
\tag{25}
\]

The `O(y^-1)` remainder absorbs terms such as `(log y)^3/y^2`, which are `o(y^-1)`. Inserting (1) into (25), and observing that the real shift `beta` only changes the constant, proves (8).

The sign is rigid:

\[
q>0,
\quad v>0,
\quad \eta>0
\quad\Longrightarrow\quad
\frac{2qv}{\eta}>0.
\tag{26}
\]

Thus the contamination cannot be tuned away by selecting a different fixed interior reference point. The reference changes its magnitude, not its sign.

## 4. The imaginary end is preserved, so the obstruction accumulates under finite stripping

The same exact calculation gives

\[
\operatorname{Im}R_a[f](iy)
=
\frac{
-vy(L^2+Q^2)+\eta Q(u^2+v^2+y^2)-\eta^2vy
}{D(y)}.
\tag{27}
\]

Using (24),

\[
\operatorname{Im}\bigl(\eta R_a[f](iy)\bigr)
=
q+O\!\left(\frac{(\log y)^2}{y}\right).
\tag{28}
\]

Hence the normalized transform remains in the asymptotic class (1), with the same limiting imaginary height `q`. If the incoming coefficient of `log(y)/y` is `A`, (8) sends it to

\[
A\longmapsto A+\frac{2qv}{\eta}.
\tag{29}
\]

Induction proves (10). Real translations between steps do not matter because they change neither the limiting imaginary height nor `eta_j=Im f_{j-1}(a_j)`. Positive affine output changes are also harmless once the unit logarithmic coefficient is restored: that normalization fixes their scale.

For `m_-`, `q=pi/2`; equations (13)-(14) follow immediately. Every nonempty finite end-normalized chain is therefore farther from the Riemann Gamma asymptotic than the unstripped source at the first order below the logarithm.

## 5. Aggressive falsification and matched controls

The result is intentionally narrower than a statement about every possible Schur or Nevanlinna transform.

First, the strict increment uses an **interior** reference: `v=Im a>0`. If the reference approaches the real boundary, the coefficient in (8) tends to zero at fixed output height, and Julia--Nevanlinna boundary reduction uses derivative data rather than the interior formula above. Boundary-reference stripping is therefore not ruled out here.

Second, the increment is proportional to the limiting imaginary height `q`. If a logarithmic Herglotz end had `q=0`, this particular obstruction would disappear. The critical reflected Mangoldt source instead has the source-forced half-line phase `q=pi/2`; the no-go is therefore not a tautology of logarithmic growth alone.

Third, allowing the interpolation point itself to move with the high-energy scale is not a fixed finite-reference Schur transform. Such a construction is a cutoff/scaling renormalization and must justify the moving reference independently. Likewise, an operator-valued Schur complement, generalized resolvent, noninvertible Herglotz operation, or an added archimedean channel lies outside the scalar one-node mechanism audited here.

Fourth, one can of course append a target-dependent analytic term chosen to cancel `(pi v/eta) log(y)/y`. That is exactly the forbidden move: the missing archimedean structure would have been inserted after the source was inspected rather than forced by Mathia. The present finding only says that canonical scalar finite-point positivity does not supply that cancellation itself.

Finally, the theorem does not claim that every arbitrary finite composition of all possible disk automorphisms and Schur reductions is represented by (10). It covers the natural **end-normalized** chain in which each reduced scalar response is returned to the same unit-log Herglotz coordinate before the next fixed interior node is stripped. This is the composition class that preserves the asymptotic object being compared to the Gamma channel at every stage. More exotic compositions must state and justify their different boundary normalization explicitly.

## 6. Prior-art and novelty audit

The function theory is classical. Schwarz--Pick gives (17), and the usual Schur algorithm is precisely the operation of moving an interpolation value to zero and dividing by the corresponding Blaschke factor. Baratchart--Kupin--Lunot--Olivi develop the multipoint Schur algorithm when interpolation nodes may lie anywhere in the open disk. No novelty is claimed for the reduction (4), its positivity preservation, or the general interpolation framework.

`WP-310` audited a different classical mechanism: the Nevanlinna Schur transform based on finite moment asymptotics at infinity. The critical Mangoldt source cannot enter that algorithm because its mass is infinite and its Herglotz end is logarithmic. The present calculation asks whether moving the reduction to an ordinary **finite interior interpolation point** avoids that mass-class barrier. It does, in the sense that (4) is perfectly well-defined and positivity preserving, but the exact high-energy asymptotic (8) creates a new defect.

A bounded literature search over multipoint Schur algorithms, Nevanlinna--Pick reduction, Herglotz logarithmic asymptotics, and Mangoldt/Herglotz transforms found the classical interpolation machinery but no source stating the specific asymptotic collision

\[
\text{critical Mangoldt half-line phase}
+\text{interior Schur stripping}
\Longrightarrow
+\frac{\pi v}{\eta}\frac{\log y}{y}.
\tag{30}
\]

The Mathia-specific contribution is therefore not a new Schur theorem. It is the exact falsification of the finite-reference scalar escape left open by `WP-310`, using the source asymptotic already forced by `WP-304`--`WP-305`.

Relevant literature anchors:

- Baratchart, Kupin, Lunot, Olivi, *Multipoint Schur algorithm and orthogonal rational functions. I: Convergence properties*, J. Analyse Math. 114, DOI `10.1007/s11854-011-0016-9`, arXiv:`0812.2050`.
- Alpay, Dijksma, Langer, *The Schur transformation for Nevanlinna functions: operator representations, resolvent matrices, and orthogonal polynomials*, arXiv:`0711.4236`.
- Classical Schwarz--Pick / Nevanlinna--Pick interpolation theory.

## 7. Consequence for the research frontier

The scalar source-resolvent route now has two distinct Schur gates.

`WP-310` shows that **moment stripping at infinity cannot even start** on the critical positive Mangoldt source without cutoff-dependent divergent mass or signed background subtraction. `WP-311` shows that moving the stripping point into the interior avoids that domain failure but produces a strictly positive `log(y)/y` term as soon as the reduced response is normalized back to the unit logarithmic end. The desired Riemann Gamma profile has no such term.

Thus a finite scalar interpolation reference is not the missing finite--archimedean coupling. The next live scalar escape is narrower: a genuinely boundary-reference Julia/Nevanlinna reduction, a moving-reference/cutoff construction with an independently forced renormalization law, or a noninvertible source-derived Herglotz operation. Beyond scalar function theory, operator/matrix-valued boundary sectors, generalized resolvents, determinant/scattering mechanisms, and nonseparable finite--archimedean couplings remain open under the README mandate.

This is still a negative result. It produces no global Weil quadratic form and no independent proof of Weil positivity. Its value is to close a canonical positivity-preserving interpolation route without invoking RH, zero data, or a fitted Gamma counterterm.

## Dependencies

- `research/weil_positivity/findings/WP-305-canonical-reflected-mangoldt-herglotz-has-the-wrong-next-order-gamma-curvature.md`
- `research/weil_positivity/findings/WP-308-scalar-herglotz-projective-recodings-cannot-repair-mangoldt-gamma-curvature.md`
- `research/weil_positivity/findings/WP-309-jointly-holomorphic-scalar-boundary-automorphism-families-are-constant.md`
- `research/weil_positivity/findings/WP-310-classical-moment-schur-reduction-cannot-start-on-the-critical-mangoldt-herglotz-source.md`

## Bottom line

The canonical finite interior Schur algorithm is well-defined on the critical Mangoldt Herglotz source, but that does not help the Gamma bridge. Returning the reduced Schur function to the same unit-log Herglotz end forces a positive `log(y)/y` correction, `pi Im(a)/Im(f(a))` after one step and a positive sum after any finite end-normalized chain. Since the Riemann Gamma asymptotic has no term of this order, finite interior scalar Schur stripping cannot be the missing Mathia-native positivity mechanism.