# WP-048 — anchored reflection and cycle extremum canonically select the `q=2` Riemann Gamma channel

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + CANDIDATE-BRIDGE + DECISIVE-BOUNDARY` for the unresolved selector issue in `WP-036`. The Prime-Circle radial Mellin family does not merely contain a `q=2` diagonal that happens to reproduce `psi(s/2)`: the original anchored circle geometry independently singles out order two in two compatible ways. The unique orientation-reversing isometry of the fixed circle that preserves the common anchor has fixed boundary locus `mu_2={1,-1}`, and the compatible cycle Laplacian of `WP-043` has its unique maximal nontrivial mode at the order-two character `gamma=1/2`; equivalently, the minimally shifted positive logarithmic Haar-tangent operator of `WP-043` has its unique nontrivial zero there. Since the full-root radial field `V_q(z)=Log(1-z^q)` has boundary singular set `mu_q`, the level selected by these intrinsic structures is exactly `q=2`. Substituting that internally selected level into the exact `WP-036` Mellin formula yields the Riemann archimedean logarithmic derivative `d/ds log(pi^{-s/2} Gamma(s/2))`.

This removes one specific arbitrariness left open by `WP-036`: `q=2` need no longer be chosen solely because the target Gamma factor is already known. It does **not** produce a global Weil-positive form. The Gamma term still appears only after an affine extraction from the positive-real Mellin response, while the finite Mangoldt birth operator still appears after subtracting a universal positive collision background and is indefinite. The selector is also present for any anchored Euclidean circle, so by itself it is geometric rather than RH-specific arithmetic data.

## 1. The anchored circle has a canonical reflection whose fixed locus is exactly `mu_2`

Prime Circle starts from the unit-circle root sets

\[
P_n=\mu_n=\{z\in\mathbb C:z^n=1\}
\]

with common anchored vertex `1`. The center `0` and anchor `1` determine a unique diameter, hence a unique orientation-reversing Euclidean isometry of the circle fixing the anchor. In the canonical complex coordinate this is

\[
\boxed{\jmath(z)=\overline z=z^{-1}\qquad (|z|=1).}
\tag{1}
\]

Indeed every orientation-reversing isometry of the unit circle has the form

\[
z\longmapsto e^{i\theta}\overline z,
\]

and fixing `1` forces `e^{i\theta}=1`.

The boundary fixed points are therefore

\[
\operatorname{Fix}(\jmath)
=\{z\in S^1:z=\overline z\}
=\{1,-1\}
=\mu_2.
\tag{2}
\]

Thus the first nontrivial full-root level is not merely one member of an inversion-invariant family. It is characterized exactly by

\[
\boxed{\mu_q=\operatorname{Fix}(\jmath)\iff q=2.}
\tag{3}
\]

For `q=1`, `mu_1={1}` is only the anchored vacuum point. For every `q>2`, `mu_q` contains non-real roots and is strictly larger than the reflection-fixed locus.

This statement uses only the original anchored Prime-Circle geometry. No zeta function, explicit formula, analytic continuation, or desired Gamma factor is used to identify the integer `2`.

## 2. The compatible positive cycle geometry independently singles out the same order-two mode

`WP-043`, using the compatible polygon-edge geometry of Prime Circle, has the positive cycle Laplacian

\[
L_{\rm cyc}=(U-I)^*(U-I)=2I-U-U^*.
\tag{4}
\]

On a character `chi_gamma`, `gamma in Q/Z`,

\[
L_{\rm cyc}\chi_\gamma
=\lambda(\gamma)\chi_\gamma,
\qquad
\lambda(\gamma)
=|1-e^{2\pi i\gamma}|^2
=4\sin^2(\pi\gamma).
\tag{5}
\]

Hence

\[
0\le \lambda(\gamma)\le4,
\]

and equality at the upper endpoint occurs exactly when

\[
e^{2\pi i\gamma}=-1.
\]

Modulo `1`, this has the unique solution

\[
\boxed{\gamma=\frac12,\qquad \operatorname{ord}(\gamma)=2.}
\tag{6}
\]

So the antipode `-1` is not merely one root among many: it is the unique nontrivial mode maximizing the intrinsic compatible edge energy.

The same fact is encoded in the positive logarithmic repair derived in `WP-043`. The reflection-symmetrized Haar tangent has Fourier value

\[
\eta_R(\chi_\gamma)
=-\frac12\log\lambda(\gamma),
\qquad \gamma\ne0,
\tag{7}
\]

whose minimum is `-log 2`, attained only at `gamma=1/2`. Therefore `log 2` is the unique minimal constant shift making the nontrivial Fourier coefficients nonnegative, and the resulting positive operator

\[
A=\frac12\log\frac4{L_{\rm cyc}}
\tag{8}
\]

has

\[
\boxed{A\chi_{1/2}=0}
\tag{9}
\]

as its unique nontrivial zero mode.

Thus order two is selected both by the real/reflection geometry of the anchored circle and by an extremal property of an independently derived positive operator on the compatible Prime-Circle limit.

## 3. The selected order is exactly the full-root Mellin channel used in `WP-036`

The radial full-root fields of `PC-056`/`WP-036` are

\[
V_q(z)=\Log(1-z^q).
\tag{10}
\]

Their boundary singular set is precisely `mu_q`. Consequently, equations (2)--(3) identify

\[
V_2(z)=\Log(1-z^2)
\tag{11}
\]

as the unique full-root radial field whose singular set is the complete reflection-fixed boundary locus. Its primitive/new part is the singleton order-two shell `mu_2^*={-1}`, exactly the cycle-energy maximizer from (6).

This closes the indexing gap between the two structures: the `q` appearing in the radial Mellin diagonal is the same root-tower level whose primitive shell contains the canonically selected order-two mode. One is not moving from an order-two spectral fact to an unrelated integer label.

The distinction between full-root and primitive coordinates still matters. `V_2` contains the anchor contribution from level `1` as well as the primitive antipodal contribution. The claim here is only that the **level** `q=2` is intrinsically selected; it is not that the full-root response equals a primitive-shell response.

## 4. The internally selected channel gives the exact Riemann archimedean logarithmic derivative

`WP-036` proves for every integer `q>=1` and `Re s>0` that the diagonal of the operator-valued radial Mellin response satisfies

\[
\mathcal M_{q,q}(s)
=\frac{q}{s}
\left[\psi\!\left(1+\frac{s}{q}\right)+\gamma\right],
\tag{12}
\]

hence

\[
\psi\!\left(\frac{s}{q}\right)
=\frac{s}{q}\mathcal M_{q,q}(s)-\gamma-\frac{q}{s}.
\tag{13}
\]

The unresolved control in `WP-036` was precisely that every `q` gives a digamma scale, so choosing `q=2` from (13) because Riemann zeta is already known to contain `Gamma(s/2)` would be target matching.

Equations (1)--(11) now supply a target-independent Prime-Circle selector. Substituting its forced value `q=2` into (13) gives

\[
\psi(s/2)
=\frac{s}{2}\mathcal M_{2,2}(s)-\gamma-\frac2s.
\tag{14}
\]

For the real Riemann Gamma factor

\[
\Gamma_{\mathbb R}(s)
:=\pi^{-s/2}\Gamma(s/2),
\]

its logarithmic derivative is

\[
A_\infty(s)
:=\frac{d}{ds}\log\Gamma_{\mathbb R}(s)
=-\frac12\log\pi+\frac12\psi(s/2).
\tag{15}
\]

Therefore

\[
\boxed{
A_\infty(s)
=\frac{s}{4}\mathcal M_{2,2}(s)
-\frac\gamma2
-\frac1s
-\frac12\log\pi.
}
\tag{16}
\]

The identity itself was already in `WP-036`; the new content is that the `2` entering it is now independently characterized by the original Mathia geometry.

## 5. The selector does not transfer the positive-real theorem to the Gamma term

The full matrix response has the unconditional geometric positivity from `WP-036`,

\[
\operatorname{Re}[s\mathcal M_S(s)]\succeq0,
\qquad \operatorname{Re}s>0.
\tag{17}
\]

Equation (16), however, is not a positive compression of `sM`. It is an affine extraction involving

\[
-\frac\gamma2I,
\qquad
-\frac1s I,
\qquad
-\frac12\log\pi\,I.
\tag{18}
\]

No order theorem derived from (17) says that subtracting (18) leaves a positive-real scalar or operator form. The reflection/cycle selector therefore repairs the **canonicity of the channel**, not the missing **sign theorem after completion**.

The finite side remains unchanged as well. `WP-036` obtains the exact boundary birth operator `C` only as the high-Mellin finite part after removing the universal positive collision background. `WP-034` proves that `C` contains the finite Weil ray coefficients with the correct sign but is unbounded below, while `WP-044`--`WP-047` show that a broad class of finite-dimensional positive Schur responses cannot retain this arithmetic term without divergent self-energy or loss of positivity.

Thus the current same-geometry picture is

\[
\boxed{
\begin{array}{c}
\text{anchored reflection / cycle extremum}\\
\Downarrow\\
q=2\\
\Downarrow\\
\text{positive-real radial Mellin family contains }\Gamma_{\mathbb R}\text{ response}
\end{array}
}
\tag{19}
\]

but the required global implication

\[
\text{intrinsic geometric positivity}
\Longrightarrow
\text{completed Weil positivity}
\tag{20}
\]

is still absent.

## 6. Matched controls and what the selector does not prove

The strongest control is deliberately unfavorable to overinterpretation. Any Euclidean circle equipped with a distinguished boundary anchor has the same unique anchored reflection and antipode, and its ordinary cycle energy has the same half-turn maximizer. Therefore the mechanism selecting order two is **universal anchored-circle geometry**.

This has two consequences.

First, it is sufficient to remove the narrow objection that `q=2` was selected only by looking at the known Riemann Gamma target: Prime Circle itself already distinguishes `2` before any zeta data are consulted.

Second, it cannot by itself distinguish the Riemann arithmetic from a non-arithmetic matched circle. It supplies an archimedean scale selector, not a global arithmetic coupling, a prime-power selector, or an RH-sensitive theorem.

Likewise, inversion invariance alone would be too weak: every `mu_q` is invariant under `z -> z^{-1}`. The exact property used here is the **fixed locus** of the unique anchored reflection, together with the independent unique spectral extremum (6). Replacing “fixed” by merely “invariant” would destroy uniqueness and invalidate the claim.

## 7. Prior-art and novelty audit

No historical novelty is claimed for the classical ingredients.

- The real local factor `Gamma_R(s)=pi^{-s/2}Gamma(s/2)` and the role of archimedean real structure are standard in Tate/Hecke local theory; `research/weil_positivity/SOURCES.md` already records Tate's thesis as the primary adelic Fourier/self-duality anchor.
- The occurrence of `+/-` real-place sectors under complex conjugation and the corresponding `Gamma_R` factors is standard arithmetic geometry/local-factor structure. It is not evidence that Prime Circle has created a new archimedean place.
- The fixed points `+/-1` of complex conjugation on the unit circle, the cycle-Laplacian eigenvalue `4 sin^2(pi gamma)`, and its unique half-turn maximum are elementary classical geometry/harmonic analysis.
- Connes--Consani and related trace-formula work already provide much more developed archimedean positivity mechanisms. This finding is not a substitute for those constructions and does not claim a new proof of archimedean Weil positivity.

Targeted searches around real local Gamma factors, complex conjugation, roots of unity, order-two modes, and Mellin/digamma representations did not identify a literature theorem equating the specific Prime-Circle radial `V_2` channel with an independently selected anchored-circle extremum. Absence of that wording is not treated as novelty evidence. The durable project-specific statement is instead the exact synthesis of previously established Mathia structures: `WP-036` left `q=2` unselected, while `WP-043` and the original anchored root geometry supply a canonical order-two selector that is independent of the desired Gamma formula.

Accordingly the result is classified as a **Mathia-specific candidate bridge**, not as a historically new Gamma-factor theorem.

## 8. Exact audit and falsification tests

The claim has short decisive tests.

1. Starting only from the fixed circle and common anchor `1`, classify orientation-reversing circle isometries fixing the anchor and verify that the unique one is `jmath(z)=bar z`.
2. Verify `Fix(jmath)={1,-1}=mu_2` and that no other full-root set `mu_q` equals this fixed locus.
3. On `Q/Z`, verify from `L_cyc=(U-I)^*(U-I)` that `lambda(gamma)=4 sin^2(pi gamma)` and that its unique maximum is `4` at `gamma=1/2`, of exact order `2`.
4. Verify that the minimal positive shift in `WP-043` is `log 2` and that the shifted logarithmic operator has its unique nontrivial zero at the same order-two character.
5. Verify that `V_2(z)=Log(1-z^2)` is the full-root level indexed by that order and that its boundary singular set is exactly the reflection-fixed locus.
6. Insert `q=2` into the independently derived `WP-036` diagonal Mellin formula and recover (16) without using zeta zeros or analytic continuation.
7. Run the matched anchored-circle control and verify that the same selector survives. This confirms that the selector is geometrically canonical while simultaneously falsifying any stronger claim that it alone contains RH-specific arithmetic information.

Failure of items 1--6 would invalidate the claimed removal of the `q=2` arbitrariness. Success of all seven still does **not** establish global Weil positivity; a surviving program must construct a nonseparable finite--archimedean operation whose sign follows independently while preserving the exact finite birth coefficients and the canonically selected real Gamma response.

## 9. Consequence for the Weil-positivity search

The `WP-036` same-geometry bridge can now be narrowed more sharply. The open problem is no longer “why choose the two-level radial channel?” Prime Circle already answers that at the level of its anchored reflection and compatible positive cycle geometry.

The remaining obstruction is structural rather than index-theoretic:

\[
\boxed{
\text{the same intrinsic geometry canonically identifies the correct real Gamma channel,}
\quad
\text{but its known positive form still lives before the renormalizations that expose the Weil terms.}
}
\]

Future work should therefore not spend effort fitting another `q` or justifying `q=2` from the known completion. It must attack the harder missing step: a quotient, infinite-dimensional boundary response, cohomological/intersection pairing, or genuinely nonseparable finite--archimedean construction in which the subtraction/counterterm structure is internal to a new independent positivity theorem rather than imposed after a positive local response has already been separated.