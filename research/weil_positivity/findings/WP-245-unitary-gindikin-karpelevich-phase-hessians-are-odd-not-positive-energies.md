# WP-245 — Unitary Gindikin–Karpelevich phase Hessians are odd, not positive energies

**Status:** `LITERATURE+EXACT-DERIVED + SPHERICAL-PARAMETER-HESSIAN-CONTROL + UNITARY-PHASE-PARITY + WEYL-DESCENT-OBSTRUCTION + DECISIVE-NEGATIVE-FOR-BARE-HESSIAN-ESCAPE + MATCHED-FUNCTIONAL-EQUATION-CONTROL + NOT-A-WEIL-BRIDGE`.

`WP-244` leaves a deliberately narrow opening inside the higher-rank spherical Maaß–Selberg route. Although the spherical Gindikin–Karpelevich normalizer is scalar, differentiating it in several spectral directions produces the canonical root-space tensor

\[
D^2\log J(w,\lambda)
=
\sum_{\alpha\in I(w)}
 h''(\langle\lambda,\alpha^\vee\rangle)
 \,\alpha^\vee\otimes\alpha^\vee.
\tag{1}
\]

Could this tensor itself be the missing source-defined positive form?

For the unitary spherical parameter where the scattering/Maaß–Selberg Hilbert structure lives, the answer is **no** for an exact symmetry reason. The completed-zeta rank-one factor obeys an inversion law forced by the functional equation. Consequently its modulus is identically one on the unitary axis. The Hessian of the log modulus is therefore zero, while the Hessian of the phase is **odd under spectral reversal**. A nonzero odd real symmetric form cannot be positive semidefinite on the full unitary parameter space: positivity at both `nu` and `-nu` would force the form to vanish.

The same calculation also exposes a Weyl-descent defect. In rank one the Weyl involution identifies `t` with `-t`, but the phase Hessian changes sign, so it cannot descend as a nonzero quadratic tensor to the spherical spectral quotient. In higher rank a simple reflection permutes all positive roots except the simple root it reverses, leaving an explicit rank-one curvature defect. Restricting by hand to one chamber can hide the sign reversal, but then the sign depends on an orientation choice rather than on a Weyl-invariant geometric positivity theorem.

This closes only the **bare parameter-Hessian** escape in `WP-244`. It does not rule out a full higher-rank truncation identity that combines several Weyl channels, boundary terms, or a source-defined weight before taking the quadratic form. Such a construction would be a genuinely different mechanism and must still reproduce the full Weil test class without choosing a chamber, tangent direction, or sign after inspecting the target arithmetic.

## 1. Functional equation forces reciprocal rank-one scattering

Use the same completed Riemann factor as `WP-244`,

\[
\Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s),
\qquad
\Lambda(s)=\Lambda(1-s),
\tag{2}
\]

and the spherical rank-one Gindikin–Karpelevich factor

\[
c(u)=\frac{\Lambda(u)}{\Lambda(u+1)}.
\tag{3}
\]

At every regular point the functional equation gives

\[
\begin{aligned}
c(-u)
&=\frac{\Lambda(-u)}{\Lambda(1-u)}\\
&=\frac{\Lambda(1+u)}{\Lambda(u)}\\
&=c(u)^{-1}.
\end{aligned}
\tag{4}
\]

This identity is stronger for the present question than generic unitarity: it fixes the parity of every logarithmic derivative. Because `Lambda` has the usual real structure,

\[
\overline{c(it)}=c(-it)=c(it)^{-1}
\tag{5}
\]

for real `t` on the regular unitary axis. Hence

\[
|c(it)|=1.
\tag{6}
\]

Locally choose a continuous phase

\[
c(it)=e^{i\theta(t)}.
\tag{7}
\]

Equation (4) implies, up to a locally constant integer multiple of `2 pi`,

\[
\theta(-t)=-\theta(t).
\tag{8}
\]

Therefore

\[
\theta'(-t)=\theta'(t),
\qquad
\theta''(-t)=-\theta''(t).
\tag{9}
\]

The branch ambiguity in (7) disappears after differentiation, so (9) is intrinsic wherever the scattering coefficient is regular.

## 2. The two natural real Hessians are either zero or sign-reversing

On the unitary axis,

\[
\log c(it)=i\theta(t)
\tag{10}
\]

up to the usual logarithm branch. Splitting the logarithm into its two real observables gives

\[
\operatorname{Re}\log c(it)=\log|c(it)|=0
\tag{11}
\]

and

\[
\operatorname{Im}\log c(it)=\theta(t).
\tag{12}
\]

Thus the Hessian of the magnitude is identically trivial,

\[
\frac{d^2}{dt^2}\log|c(it)|=0,
\tag{13}
\]

while the only nontrivial real second derivative available directly from the scalar normalizer is the phase curvature

\[
q_t(x)=\theta''(t)x^2.
\tag{14}
\]

By (9),

\[
q_{-t}(x)=-q_t(x).
\tag{15}
\]

Suppose the bare phase Hessian supplied a global positive energy on the natural unitary parameter line. Then both representatives `t` and `-t` would have to satisfy

\[
q_t\succeq0,
\qquad
q_{-t}\succeq0.
\tag{16}
\]

Together with (15), this forces

\[
q_t=0
\tag{17}
\]

for every regular `t`. Hence there are only two possibilities: the phase Hessian is nonzero somewhere and necessarily fails global semidefinite positivity, or it vanishes identically and therefore carries no arithmetic curvature from which the Weil functional could be obtained. No zero-location hypothesis enters this dichotomy.

This is exactly where first and second derivatives behave differently. The first phase derivative `theta'(t)` is **even** under `t -> -t` and is the familiar real logarithmic-derivative/time-delay quantity retained by Maaß–Selberg formulas. `WP-244` already records that unitarity makes this quantity real but does not fix its sign. Taking one further derivative does not improve the sign problem: it converts the even observable into an odd curvature.

## 3. Higher rank inherits the same obstruction globally

For the longest Weyl element of a split spherical system, write

\[
J_0(\lambda)
=
\prod_{\alpha>0}
 c(\langle\lambda,\alpha^\vee\rangle).
\tag{18}
\]

On the unitary axis `lambda=i nu`, define a local total phase by

\[
J_0(i\nu)=e^{i\Theta(\nu)},
\qquad
\Theta(\nu)=
\sum_{\alpha>0}
\theta(\langle\nu,\alpha^\vee\rangle).
\tag{19}
\]

Equation (8) gives

\[
\Theta(-\nu)=-\Theta(\nu)
\tag{20}
\]

modulo a locally constant phase. Its real Hessian is

\[
H_\nu
:=D^2\Theta(\nu)
=
\sum_{\alpha>0}
\theta''(\langle\nu,\alpha^\vee\rangle)
\,\alpha^\vee\otimes\alpha^\vee.
\tag{21}
\]

Therefore

\[
\boxed{H_{-\nu}=-H_\nu.}
\tag{22}
\]

If `H_nu` were positive semidefinite for every point of the full unitary parameter space, then (22) would make both `H_nu` and `-H_nu` positive semidefinite. Hence `H_nu=0` identically. The multidimensional root system does not evade the rank-one parity obstruction; it packages the odd curvatures into a higher-rank odd tensor.

The statement is about the **full source-defined parameter domain**, not about the sign on one selected ray. A ray or chamber may of course contain a region on which a chosen contraction of `H` has one sign. That does not provide a global geometric positivity theorem unless the source itself canonically selects that restriction and the resulting form still yields the complete Weil criterion.

## 4. The Hessian also fails the naive Weyl-quotient descent test

The spectral parameter of spherical Eisenstein theory is naturally organized modulo Weyl symmetry. The parity obstruction can be sharpened by looking at one simple reflection `s_i` with simple root `alpha_i`.

A standard root-system fact is that `s_i` sends `alpha_i` to `-alpha_i` and permutes the remaining positive roots. Applying this to (19) and using the oddness of `theta` gives

\[
\Theta(s_i\nu)
=
\Theta(\nu)
-2\theta(\langle\nu,\alpha_i^\vee\rangle)
\tag{23}
\]

(up to the same harmless locally constant phase). Differentiating twice yields the pullback relation

\[
D^2(\Theta\circ s_i)_\nu
=
H_\nu
-2\theta''(\langle\nu,\alpha_i^\vee\rangle)
\,\alpha_i^\vee\otimes\alpha_i^\vee.
\tag{24}
\]

Thus the Hessian of the raw longest-element phase is not Weyl invariant whenever the corresponding rank-one curvature is nonzero. In rank one, (24) reduces to the exact sign reversal (15): the quotient identifies `t` and `-t`, while the proposed quadratic tensor assigns opposite forms to the two representatives.

This matters because the hoped-for positive object in `WP-244` was supposed to be supplied by the intrinsic spherical geometry, not by a post hoc orientation. Choosing a positive chamber and declaring only one representative physical is a legitimate coordinate convention for many calculations, but it is not by itself a proof that the phase Hessian defines a canonical positive energy on the Weyl quotient.

## 5. Aggressive escape controls

### Control A — multiply the Hessian by `-1`

A global sign flip does nothing to (22): `-H` is just as odd as `H`. It can exchange the sign at `nu` and `-nu`, not make both positive.

### Control B — take an absolute value, square, or Gram form

Operations such as

\[
H\mapsto H^*H,
\qquad
\theta''\mapsto |\theta''|,
\qquad
q\mapsto q^2
\tag{25}
\]

can manufacture nonnegativity. They are nonlinear in the logarithmic derivative data and destroy the linear explicit-formula interface that motivated the Maaß–Selberg route. Unless such an operation is forced by an independent source-side boundary/intersection theorem and is shown to recover the same Weil functional, it is precisely a positive repackaging rather than the missing bridge.

### Control C — restrict to one chamber or half-line

Discarding `-nu` removes the immediate contradiction, but the restriction chooses an orientation before the sign theorem. Equation (24) shows that the bare Hessian is not a tensor descending unchanged through Weyl identifications. A chamber-restricted construction therefore needs an additional source theorem explaining why its boundary orientation is canonical and why wall-crossing does not change the Weil form. Merely selecting the chamber in which the desired contraction has the favorable sign is target-dependent.

### Control D — contract with a chosen tangent direction

For a tangent vector `v`,

\[
H_\nu(v,v)
=
\sum_{\alpha>0}
\theta''(\langle\nu,\alpha^\vee\rangle)
\langle v,\alpha^\vee\rangle^2.
\tag{26}
\]

The squared root coefficients are nonnegative, but the arithmetic coefficients remain odd under `nu -> -nu`. Choosing `v=v(nu)` after inspecting those signs is a hand-picked kernel/direction and is excluded by the line mandate. A source-defined `v` can still be tested, but it no longer inherits positivity merely from the Hessian.

### Control E — generalized self-reciprocal scattering factors

Nothing in (4)--(22) uses the location of Riemann zeros. The same obstruction holds for any completed scalar factor satisfying the analogous real functional equation and reciprocal scattering identity. Therefore the parity phenomenon is not an arithmetic rigidity distinguishing `Q`; it is a structural consequence of unitary scalar scattering. This is the appropriate matched control for a proposed geometric sign theorem.

### Control F — combine the Hessian with truncation or several Weyl channels

This finding does **not** rule that out. A Maaß–Selberg identity can contain height polynomials, chamber combinatorics, derivatives of several intertwiners and boundary cross terms before the final Hilbert norm is formed. Such an expression need not equal the bare Hessian (21). It remains eligible only if the combination is source-forced, has an independent sign, and maps to the exact full Weil functional without target-chosen cancellations.

## 6. Prior-art and novelty audit

The ingredients used in the obstruction are classical.

- The spherical Gindikin–Karpelevich product and its global completed-zeta scalar factors are the same literature input audited in `WP-244`: Nadya Gurevich and Avner Segal, *Poles of the Standard L-function of G2 and the Rallis–Schiffmann Lift*, Canadian Journal of Mathematics 71 (2019), 1127--1161, DOI `10.4153/CJM-2018-019-7`, Section 3.1.
- Henry H. Kim, *On Local L-Functions and Normalized Intertwining Operators*, Canadian Journal of Mathematics 57 (2005), 535--597, DOI `10.4153/CJM-2005-023-x`, is the retained normalization/prior-art boundary for scalar `L`-factors versus normalized intertwining operators.
- Standard normalized intertwining theory gives holomorphy/unitarity on tempered imaginary parameters and the cocycle relations; this is the same classical structural input already used in `WP-244`. The reciprocal identity (4) for the Riemann spherical factor is derived directly here from the completed-zeta functional equation, so no new analytic continuation or zero theorem is being assumed.

A bounded literature search for `Gindikin--Karpelevich Hessian`, `Maaß--Selberg Hessian`, `higher-rank scattering phase positivity`, and normalized-intertwiner unitarity found the standard scattering/intertwining framework and general scattering-phase literature, but no audited source asserting that the **bare Hessian of the unitary completed-zeta scattering phase** is a positive metric yielding Weil positivity. This is not a completeness claim. The durable contribution is the line-specific exact obstruction (22)--(24), not the classical functional equation or unitarity itself.

Repository novelty was checked against the current `weil_positivity` findings and clue disposition. `WP-244` explicitly left the parameter Hessian open and recorded only that unitarity makes the first phase derivative real without fixing its sign. No stored `WP-*` finding in the audited current set states the second-derivative parity obstruction or the Weyl-descent failure above. The result therefore narrows an explicitly live escape rather than renaming an already closed route.

## 7. Consequence for the research line

The direct chain

\[
\text{spherical scalar normalizer}
\longrightarrow
D^2_{\rm parameter}\log J
\longrightarrow
\text{canonical positive root-space energy}
\longrightarrow
\text{Weil positivity}
\tag{27}
\]

fails at the second arrow on the unitary axis. The magnitude Hessian vanishes; the real phase Hessian is odd under spectral inversion and does not descend as a nonzero Weyl-invariant positive tensor.

The surviving higher-rank Maaß–Selberg search is correspondingly narrower. It must use a **pre-Hessian source coupling** or a full truncation/boundary identity that changes the parity bookkeeping before positivity is read out, or leave the spherical scalar category entirely through genuinely non-spherical/vector-valued inducing data. A chamber choice, tangent selection, absolute value, square, or post hoc root weighting does not solve the problem. `WP-245` proves no case of RH; it removes the bare spherical parameter-Hessian route from the list of plausible independent positivity mechanisms.