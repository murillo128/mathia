# WP-173 — Passive Hilbert termination of regular J-contractive channels collapses back to Schur

**Status:** `LITERATURE+DERIVED + J-CONTRACTIVE-LFT-NO-GO + PASSIVE-HILBERT-TERMINATION + ARCHIMEDEAN-GAMMA + DECISIVE-NARROWING + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION`.

`WP-170` shows that the exact archimedean phase

\[
R_\infty(\tau)
=\pi^{i\tau}
\frac{\Gamma(\tfrac14-\tfrac{i\tau}{2})}
     {\Gamma(\tfrac14+\tfrac{i\tau}{2})}
\tag{1}
\]

is unimodular on the real axis but is not an ordinary Schur/inner function in the upper half-plane: its zeros

\[
\tau_n=i\left(2n+\frac12\right),\qquad n\ge0,
\tag{2}
\]

violate the Blaschke condition, while `R_infty^{-1}` has upper-half-plane poles at the same points. `WP-171` rules out the regular positive Hilbert matrix-inner lift, and `WP-172` rules out finite-negative-index generalized-Schur/Pontryagin repair. One explicit escape left by `WP-172` is to put an **indefinite metric on the external channels themselves** and try to recover a positive Hilbert response only after a passive termination.

For the standard regular linear-fractional/Redheffer closure, that escape does not work. If the indefinite external block is pointwise `J`-contractive and the terminating load is an ordinary Hilbert-space Schur contraction, then the visible closed-loop response is automatically an ordinary Hilbert-space Schur function. The proof is a one-line negative-cone argument and is dimension independent. Consequently an arbitrarily large, even infinite-dimensional, collection of ordinary `J`-ports does not by itself evade the `WP-170` obstruction if it is finally closed by passive Hilbert feedback.

This is classical linear-fractional `J`-inner/Schur theory, not a new systems theorem. The Mathia-specific result is the narrowing: **indefinite external channels help only if the final closure leaves the ordinary passive Hilbert LFT category, or if finite and archimedean data are coupled before the exact Gamma phase becomes a separate transfer readout.**

## 1. Negative-cone proof of the collapse

Let `E_+` and `E_-` be Hilbert spaces and put

\[
J=\begin{pmatrix}I_{E_+}&0\\0&-I_{E_-}\end{pmatrix}.
\tag{3}
\]

At a point `z` of the analytic domain let

\[
W(z)=
\begin{pmatrix}
w_{11}(z)&w_{12}(z)\\
w_{21}(z)&w_{22}(z)
\end{pmatrix}
\tag{4}
\]

be a bounded operator on `E_+\oplus E_-` satisfying the passive `J`-contractive inequality

\[
W(z)^*J W(z)\le J.
\tag{5}
\]

A standard conservative `J`-inner transfer block is the boundary-unitary special case together with the corresponding interior `J`-contractivity. Let the terminating Hilbert-space load

\[
\varepsilon(z):E_-\to E_+
\tag{6}
\]

be Schur, so

\[
\varepsilon(z)^*\varepsilon(z)\le I_{E_-}.
\tag{7}
\]

Define

\[
D(z)=w_{21}(z)\varepsilon(z)+w_{22}(z)
\tag{8}
\]

and suppose the feedback is regular: `D(z)` is invertible and the inverse is analytic on the domain under consideration. The usual linear-fractional response is

\[
s(z)=T_W[\varepsilon](z)
=\bigl(w_{11}(z)\varepsilon(z)+w_{12}(z)\bigr)D(z)^{-1}.
\tag{9}
\]

Now set

\[
X(z)=\binom{\varepsilon(z)}{I_{E_-}}.
\tag{10}
\]

The load graph lies in the negative `J`-cone because

\[
X^*JX=\varepsilon^*\varepsilon-I\le0.
\tag{11}
\]

By (5),

\[
X^*W^*JWX\le X^*JX\le0.
\tag{12}
\]

But (8)--(9) give

\[
WX
=\binom{w_{11}\varepsilon+w_{12}}
        {w_{21}\varepsilon+w_{22}}
=\binom{s}{I}D.
\tag{13}
\]

Therefore

\[
D^*(s^*s-I)D\le0.
\tag{14}
\]

Invertibility of `D` yields

\[
\boxed{s(z)^*s(z)\le I.}
\tag{15}
\]

If `W`, `epsilon`, and the regular feedback inverse are analytic, then `s` is analytic as well. Thus

\[
\boxed{
W\text{ pointwise }J\text{-contractive}
+\varepsilon\text{ Hilbert-Schur}
+\text{regular LFT closure}
\Longrightarrow
s\text{ Hilbert-Schur}.
}
\tag{16}
\]

No finite-dimensionality has been used. The indefinite external channel may have arbitrarily many positive and negative coordinates; once the input graph is a passive Hilbert contraction and the `J`-contractive block maps the negative cone into itself, regular graph elimination returns an ordinary contraction.

Changing the sign convention for `J` only swaps which graph cone is called positive or negative. The invariant content is that the standard `J`-contractive map preserves the contractive graph domain on which the linear-fractional transform is defined.

## 2. Exact Gamma readouts are therefore still impossible

Suppose a candidate Mathia boundary construction places the exact real-place response (1) after such a regular passive closure. If the closed response is scalar, (16) makes it an ordinary Schur function. That contradicts the exact `WP-170` divisor calculation: the analytic orientation `R_infty` has the non-Blaschke zero sequence (2), and the inverse orientation has poles there. Hence

\[
\boxed{s\ne R_\infty^{\pm1}}
\tag{17}
\]

as exact analytic transfer functions in the upper-half-plane orientation used by `WP-170`.

The same conclusion survives operator-valued output whenever the proposed arithmetic readout is a fixed matrix coefficient. For unit vectors `u,v`,

\[
f_{u,v}(z)=\langle u,s(z)v\rangle
\tag{18}
\]

is analytic and satisfies `|f_{u,v}(z)|<=1`; it is an ordinary scalar Schur function. Thus no fixed coefficient can be the exact analytic `R_infty^{+/-1}`.

For a finite-dimensional square output, the determinant cannot hide the phase either. From (15), every singular value of `s(z)` is at most one, so

\[
|\det s(z)|\le1.
\tag{19}
\]

The determinant is analytic wherever `s` is analytic and hence is scalar Schur. Therefore

\[
\boxed{\det s\ne cR_\infty^{\pm1}}
\tag{20}
\]

for every unimodular constant `c`. Equation (20) is intentionally restricted to finite-dimensional determinant readouts; no Fredholm determinant claim is made for arbitrary infinite-dimensional outputs.

The claim concerns an **exact analytic transfer realization**, which is the route under audit. It does not classify arbitrary boundary-only scalarizations for which no analytic continuation is specified.

## 3. Matched control: ordinary indefinite ports do not enlarge the passive scalar class

The obstruction is not caused by choosing a trivial `J`-block. In the scalar case, for any `|a|<1`,

\[
W_a=\frac1{\sqrt{1-|a|^2}}
\begin{pmatrix}
1&a\\
\bar a&1
\end{pmatrix}
\tag{21}
\]

is `J`-unitary for `J=diag(1,-1)`. Its linear-fractional action is

\[
T_{W_a}[\varepsilon]
=\frac{\varepsilon+a}{\bar a\,\varepsilon+1},
\tag{22}
\]

which is the standard disk automorphism of a Schur load. The indefinite two-port geometry is real and nontrivial, yet passive termination merely moves within the Schur class. This is exactly what the cone calculation predicts.

Conversely, if the load is allowed to violate `epsilon^* epsilon<=I`, then (11) fails and the conclusion need not hold. That is a genuine escape, but it no longer obtains the final sign from **passive Hilbert termination**. A Mathia proposal using such a load must supply an independent geometric coercivity/positivity theorem rather than treating the indefinite feedback algebra itself as the desired positivity mechanism.

## 4. Aggressive falsification and exact scope

**Boundary `J`-unitarity alone is insufficient for this theorem.** The proof uses the interior pointwise inequality (5). A meromorphic object that is merely `J`-unitary on the real boundary but is not in the standard `J`-contractive analytic class is outside the result. It also lacks the ordinary passive realization theorem being tested, so its sign must be justified separately.

**Singular feedback is not covered.** If `D` loses invertibility, a pole, relation-valued response, quotient, or domain change can appear. Such singular geometry may be mathematically meaningful, but it is not a regular Schur-preserving termination. The branch should test any such proposal by deriving its domain and sign theorem from the source geometry, not by regularizing `D^{-1}` by hand.

**Generalized `J`-inner functions with negative squares are not collapsed to index zero by this argument.** Derkach--Dym linear-fractional theory permits a generalized `J`-inner coefficient with negative index `kappa_1` acting on a generalized Schur parameter of index `kappa_2`, with output negative index bounded by the combined defect under the corresponding hypotheses. `WP-172` already proves that every finite combined defect is too small for the exact Gamma divisor. Infinite negative index remains outside both results.

**An indefinite load is not a passive Hilbert load.** Closing a `J`-block with another indefinite system can retain negative squares. This may accommodate the Gamma phase analytically, but then the research problem is pushed to a later stage: where does the independently positive Weil form arise, and why is the required indefinite sector source-forced rather than chosen to interpolate (1)?

**Nonseparable finite--archimedean assembly remains open.** The result assumes the real-place factor becomes a separate transfer response that is then subjected to regular passive closure. It does not apply if finite-prime incidence and the real-place structure are coupled first so that no intermediate scalar or fixed coefficient equals `R_infty`.

These controls make the narrowing precise: the theorem does not say that every Krein-space or `J`-inner idea is impossible. It says that **ordinary external indefiniteness followed by ordinary passive Hilbert termination gives no new analytic freedom at the visible response**.

## 5. Prior-art and novelty audit

The Schur-preserving linear-fractional mechanism is classical. Harry Dym, *Linear fractional transformations*, in *Directions in Mathematical Systems Theory and Optimization*, Lecture Notes in Control and Information Sciences 286 (2003), 127--133, DOI `10.1007/3-540-36106-5_8`, explicitly studies the linear-fractional transformation of the Schur class by a `J`-inner matrix-valued function. Damir Z. Arov and Harry Dym, *J-Contractive Matrix Valued Functions and Related Topics*, Cambridge University Press (2008), develops `J`-contractive/`J`-inner functions, passive systems, and Darlington/linear-fractional machinery in a unified setting.

For the indefinite extension, Vladimir Derkach and Harry Dym, *On Linear Fractional Transformations Associated with Generalized J-Inner Matrix Functions*, Integral Equations and Operator Theory 65 (2009), 1--50, DOI `10.1007/s00020-009-1709-7`, arXiv `0901.0193`, studies the range of `T_W` for generalized `J`-inner `W` acting on generalized Schur classes and records the additive negative-index bound in the relevant subclasses. In particular, the zero-index specialization is the ordinary `J`-inner/Schur-preserving situation proved directly in (10)--(16).

No novelty is claimed for (16). The Mathia-specific substantive content is its application to the exact phase isolated by `WP-169` and the resulting closure of an explicit `WP-172` escape category:

\[
\boxed{
\text{indefinite external }J\text{-ports}
+\text{ passive Hilbert closure}
\not\Rightarrow
\text{new Gamma-compatible positive response}.
}
\tag{23}
\]

This is a prior-art classicalization plus a decisive narrowing, not a candidate proof of Weil positivity.

## 6. Research consequence

After `WP-170`--`WP-173`, a viable boundary/scattering route cannot obtain the missing archimedean sign merely by successively enlarging an ordinary passive transfer system: scalar Schur fails; positive matrix Schur fails; finite generalized-Schur defect fails; and regular `J`-contractive external ports closed with a Hilbert-Schur load collapse back to the scalar/matrix Schur category.

The remaining categories are correspondingly sharper. A successful construction must use at least one genuinely new ingredient: a source-forced singular/domain-changing closure; an infinite-negative-index or otherwise generalized indefinite structure together with a later independent coercive quotient; a nonpassive load whose final positivity is proved by another geometric theorem; or, most naturally relative to the branch mandate, a **nonseparable finite--archimedean object formed before positive scalarization** so that the exact Gamma phase is only a derived component and not itself the passive characteristic response.

The last option continues to fit the central mandate best. It is also the hardest control to fake: the same intrinsic construction must then explain the finite Mangoldt support, the real-place Gamma term, the polar/global counterterms, and the final sign without importing zero data or an RH-equivalent functional.