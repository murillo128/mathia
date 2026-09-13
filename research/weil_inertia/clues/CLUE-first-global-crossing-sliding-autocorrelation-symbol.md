---
id: CLUE-weil-inertia-first-global-crossing-sliding-autocorrelation-symbol
type: research-clue
status: accepted
origin: research-watch
target_line: weil_inertia
based_on:
  - research/weil_inertia/findings/WI-253-first-global-crossing-has-a-sliding-autocorrelation-flux-constraint.md
  - research/weil_inertia/findings/WI-254-sliding-aperture-profile-is-invertible-but-small-scale-firstness-is-saturated.md
  - research/weil_inertia/findings/WI-255-first-small-aperture-correction-is-universal-and-cannot-bootstrap.md
  - research/weil_inertia/findings/WI-256-next-small-aperture-remainder-is-a-local-translation-defect-modulus.md
  - research/weil_inertia/findings/WI-257-bounded-perturbation-zero-modes-do-not-upgrade-translation-regularity.md
  - research/weil_inertia/findings/WI-258-phase-modulation-couples-firstness-slack-to-localized-cosine-defect.md
  - research/weil_inertia/findings/WI-263-full-span-autocorrelations-can-null-the-first-prime-and-screen-the-localized-phase-defect.md
  - research/weil_inertia/findings/WI-264-finite-aperture-endpoint-autocorrelations-screen-all-prime-layers.md
  - research/weil_inertia/findings/WI-265-endpoint-screening-survives-an-abstract-first-crossing-compression-model.md
  - research/weil_inertia/findings/WI-266-suzuki-null-equation-rules-out-endpoint-bump-screening.md
  - research/weil_inertia/findings/WI-267-suzuki-null-modes-admit-no-prime-translation-free-support-gap.md
  - research/weil_inertia/findings/WI-268-archimedean-sign-change-breaks-unrestricted-semigroup-positivity.md
  - research/weil_inertia/findings/WI-269-first-crossing-null-modes-induce-a-psd-signed-source-laplacian.md
  - research/weil_inertia/findings/WI-270-sharp-cut-localization-reduces-one-signed-prime-screening-to-a-carlman-threshold.md
  - research/weil_inertia/findings/WI-273-first-question-crossing-is-equivalent-to-vanishing-of-a-positive-source-hankel-norm.md
  - research/weil_inertia/findings/WI-274-simultaneous-cuts-create-a-positive-saturated-source-reserve.md
  - research/weil_inertia/findings/WI-275-a-harmonic-minimax-reserve-is-the-sharp-mass-only-cut-bound.md
  - research/weil_inertia/findings/WI-276-cross-cut-energy-obeys-a-sharp-nilpotent-shift-reserve.md
  - research/weil_inertia/findings/WI-277-commensurate-cross-cut-shifts-obey-a-sharp-finite-toeplitz-reserve.md
---

# Can the first-crossing saturated source reserve force unscreenable arithmetic overlap?

## Observation

The first-crossing route has narrowed to a quantitative source-budget problem. `WI-275` exhausts the complementary-mass information and gives the sharp harmonic reserve

\[
\mathcal S_v\ge
R_{\rm harm}(a)
=
2\int_0^a
\frac{\lambda_r\lambda_{a-r}}
{\lambda_r+\lambda_{a-r}}\,dr.
\]

`WI-276` then adds genuinely cross-cut information. For `f(t)=sqrt(Q_t)` and one shift `h=2r`, compact support and the nilpotent numerical-radius theorem give

\[
\mathcal S_v\ge
\frac{r\lambda_r}
{1+\cos\!\left(\pi/(\lceil a/r\rceil+1)\right)}.
\]

That one-shift coefficient is sharp for arbitrary nonnegative `f` supported in `[-a,a]`, so it cannot be improved shift by shift without extra source information.

`WI-277` shows, however, that separately sharp shifts are not generally jointly sharp. For a base radius `r`, `N=ceil(a/r)`, nonnegative weights `alpha_k`, and the finite unilateral shift `J_N`, define

\[
H_N(\alpha)
=
\frac12\sum_k\alpha_k
\left(J_N^k+(J_N^*)^k\right),
\qquad
\rho_N(\alpha)=\lambda_{\max}(H_N(\alpha)).
\]

Then every first-crossing null mode satisfies the exact commensurate multishift reserve

\[
\boxed{
\mathcal S_v\ge
\frac{\sum_k\alpha_k\,kr\,\lambda_{kr}}
{\sum_k\alpha_k+\rho_N(\alpha)}.
}
\]

For each fixed weight vector this support-only coefficient is itself sharp. The new information is the joint compatibility of several correlations of the *same* profile. In the first nontrivial case `N=3`, combining radii `r` and `2r` is strictly stronger than both individual `WI-276` bounds whenever

\[
\frac52-\frac{5\sqrt2}{4}
<
\frac{2\lambda_{2r}}{\lambda_r}
<
\frac32.
\]

Thus the generic support-only frontier is no longer a scalar supremum over radii; it is a finite Toeplitz optimization over commensurate shift families.

On a one-signed first-null branch, `WI-274` still gives the exact finite positive archimedean budget

\[
K_+=\int_0^{h_0}h\,w(h)\,dh,
\]

so any certified lower reserve above `K_+` forces positive weighted prime overlap. None of the current reserve inequalities transfers that conclusion automatically to a sign-changing null mode.

## Research question

Does the actual first-eigenvalue profile `r -> lambda_r` force the optimized multishift Toeplitz reserve, possibly combined with `R_harm(a)`, above `K_+` at a hypothetical first crossing? If not, can one construct an admissible spectral profile satisfying every presently proved constraint while keeping all such support-only reserves below `K_+`?

If the support-only profile test is compatible with complete screening, the next input must use information absent from `WI-275`--`WI-277`: the exact Suzuki source equation, the PSD signed-source multiplier family, regularity/nodal geometry of the actual null eigenfunction, noncommensurate source-shape constraints, or the archimedean sign change itself.

## Decisive test

First obtain rigorous quantitative information on `lambda_r` strong enough to evaluate

\[
R_{\rm multi}(a)
:=
\sup_{\substack{0<r<a\\
\alpha_k\ge0,\ kr<a}}
\frac{\sum_k\alpha_k\,kr\,\lambda_{kr}}
{\sum_k\alpha_k+\rho_{\lceil a/r\rceil}(\alpha)}.
\]

The immediate budget comparison is

\[
\max\{R_{\rm harm}(a),R_{\rm multi}(a)\}>K_+.
\]

A proof forces positive prime overlap for a one-signed first null mode. A rigorous admissible `lambda_r` profile keeping both terms at or below `K_+` would close the generic mass/support multishift route and redirect the clue to genuinely source-specific structure.

The cheap first subtest is the `N=3` window `a/3<=r<a/2`: determine whether known spectral constraints force the ratio `2 lambda_(2r)/lambda_r` into the strict-improvement interval from `WI-277`, and if so whether the resulting reserve moves the budget comparison materially.

## Stress tests

Any bootstrap must survive the existing obstructions. `WI-257` blocks generic bounded-self-adjoint regularity upgrades. `WI-263` defeats one-prime sign/Bochner reasoning. `WI-264` and `WI-265` show that finite source atoms and generic first-crossing positivity can be screened at the autocorrelation level. `WI-268` prevents silently assuming a one-signed ground state from standard semigroup theory. `WI-273` closes the single narrow-cut Carleman route. `WI-275` exhausts the mass-only complementary-cut relaxation. `WI-276` closes the one-shift compact-support coefficient, while `WI-277` closes the coefficient for every fixed nonnegative commensurate multishift combination.

Accordingly, a claimed improvement after `WI-277` must either improve the *spectral-profile numerator* through new information on `lambda_r`, optimize genuinely joint shift families, or add source/eigenfunction structure not present in the arbitrary supported-profile relaxation. Repackaging separately sharp one-shift inequalities is not new progress.

Pointwise arguments must also respect the form domain. The first null mode lies in `D(A_a)`, not automatically in `H_0^1`; stronger regularity used to constrain `Q_t` or its correlations must be proved from Suzuki's operator/form rather than assumed.

## Evidence boundary

The harmonic, one-shift, and commensurate multishift reserves are exact consequences of the established first-crossing form identities plus classical/finite operator theory. They do not prove that the reserve exceeds `K_+`, do not prove that the first null mode is one-signed, and do not force prime overlap on the sign-changing branch.

The sharpness statements are relaxation statements. `WI-275` is sharp for the mass-only pointwise problem; `WI-276` is sharp for one compact-support translation; `WI-277` is sharp for each fixed nonnegative commensurate shift combination in the arbitrary supported-profile class. Their abstract extremizers need not satisfy the exact Suzuki source equation. That remaining incompatibility is the main opportunity after the spectral-budget test.

## Research disposition

The clue remains `accepted`. The immediate target is now the **spectral-profile / finite-Toeplitz budget test** above, not another one-shift decorrelation bound. If known `lambda_r` constraints cannot force `max(R_harm,R_multi)>K_+`, construct a rigorous compatible profile if possible and then move to source-specific shape/sign information rather than further optimizing the same support-only relaxation.
