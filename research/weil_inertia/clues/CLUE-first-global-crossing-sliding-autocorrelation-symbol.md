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
---

# Can the first-crossing saturated source reserve force unscreenable arithmetic overlap?

## Observation

The first-crossing route has narrowed from generic support geometry to a quantitative source-budget problem. `WI-253` and `WI-258` supplied lower-envelope constraints for every hypothetical first unrestricted localized Weil zero mode. `WI-264` and `WI-265` showed that finite prime layers and generic first-crossing positivity can be screened at the autocorrelation level, while `WI-266` and `WI-267` restored Suzuki-specific rigidity: the actual null equation excludes the endpoint screen and no nonzero null vector can have an open support gap simultaneously free of every active prime translation. `WI-268` rules out ordinary positivity-preserving-semigroup/Perron--Frobenius shortcuts in the relevant radius regime, and `WI-269` replaces them with the exact PSD signed-source multiplier Laplacian conditioned on the null mode.

`WI-273` then identified the remaining narrow-gap obstruction as a positive-source Hankel/Hardy saturation problem. `WI-274` bypassed the single-cut saturation loss by integrating all complementary sharp cuts. For an attained first crossing `a`, normalized real null mode `v`, common complementary cut energy `Q_t`, and first-eigenvalue profile `\lambda_r`, it proved

\[
\mathcal S_v=\int_{-a}^{a}Q_t\,dt
\ge 2\int_{a/2}^{a}\lambda_r\,dr>0,
\]

where `\mathcal S_v` is the exact saturated prime-plus-archimedean source functional. On the one-signed branch this reduces complete prime screening to comparison of that reserve with the finite positive archimedean budget

\[
K_+=\int_0^{h_0}h\,w(h)\,dh.
\]

`WI-275` sharpens the same cut data before integration. The two simultaneous inequalities

\[
Q_t\ge \lambda_{(a+t)/2}M_L(t),
\qquad
Q_t\ge \lambda_{(a-t)/2}M_R(t),
\qquad M_L+M_R=1,
\]

imply the exact pointwise minimax floor. Consequently

\[
\boxed{
\mathcal S_v\ge R_{\rm harm}(a)
:=2\int_0^a
\frac{\lambda_r\lambda_{a-r}}
{\lambda_r+\lambda_{a-r}}\,dr.
}
\]

This dominates the `WI-274` reserve by the exact nonnegative difference

\[
R_{\rm harm}(a)-2\int_{a/2}^{a}\lambda_s\,ds
=
2\int_0^{a/2}
\frac{\lambda_{a-r}(\lambda_r-\lambda_{a-r})}
{\lambda_r+\lambda_{a-r}}\,dr.
\]

The improvement is also a boundary result. The pointwise equality mass

\[
M_L^*(t)=
\frac{\lambda_{(a-t)/2}}
{\lambda_{(a+t)/2}+\lambda_{(a-t)/2}}
\]

is monotone in `t`. Therefore CDF monotonicity alone cannot strengthen the harmonic envelope; any further reserve must use more of the actual null eigenfunction/source coupling than complementary masses and firstness.

`WI-276` supplies the first such cross-cut correction without assuming a sign for the null mode. If `f(t)=\sqrt{Q_t}` and `h=2r`, the PSD null-form geometry of the three consecutive pieces cut at `t` and `t+h` gives

\[
|\mathcal F_v(r)-\mathcal S_v|
\le \int f(t)f(t+h)\,dt.
\]

Because `f` is supported on an interval of length `2a`, translation by `h` is a nilpotent contraction of order `N=\lceil a/r\rceil`. The sharp Haagerup--de la Harpe numerical-radius inequality therefore yields

\[
\boxed{
\mathcal S_v\ge
\sup_{0<r<a}
\frac{r\lambda_r}
{1+\cos\!\left(\pi/(\lceil a/r\rceil+1)\right)}.
}
\]

This information is independent of the mass-only minimax relaxation, so the live reserve is the maximum of this shift bound and `R_harm(a)`. The numerical-radius coefficient is itself sharp for arbitrary nonnegative cut-energy profiles with only the support constraint `supp Q\subset[-a,a]`. Hence any further cross-cut gain must use actual Weil-source/eigenfunction structure or simultaneous relations at several shifts, not merely generic compact-support decorrelation.

## Research question

Can the combined harmonic and cross-cut shift reserve be controlled strongly enough to force the relevant source budget at a hypothetical first crossing, thereby ruling out complete prime-lag screening on the one-signed branch? If not, can the exact Suzuki null equation or the PSD signed-source multiplier family force an additional positive correction by constraining the *actual shape* of `Q_t` or by coupling several translations simultaneously?

The key distinction is now explicit. Improving the scalar optimization of the two complementary inequalities is exhausted by `WI-275`, while improving the one-shift support-only correlation constant is exhausted by `WI-276`. A successful next step must either constrain `r\mapsto\lambda_r` quantitatively or introduce information these relaxations discard: source-dependent shape restrictions on `Q_t`, regularity/nodal geometry of the actual null eigenfunction, multi-shift consistency, or a finite compression of the exact multiplier form.

## Decisive test

First attack the combined spectral-budget comparison with exact inequalities. Derive rigorous lower information on the first-eigenvalue profile and test whether

\[
\max\!\left\{
R_{\rm harm}(a),
\sup_{0<r<a}
\frac{r\lambda_r}
{1+\cos\!\left(\pi/(\lceil a/r\rceil+1)\right)}
\right\}>K_+.
\]

A proof would force positive weighted prime overlap for a one-signed first null mode. A rigorous admissible profile satisfying every presently proved spectral constraint while keeping both reserves at or below `K_+` would close the scalar spectral-profile route and redirect the clue entirely to source/eigenfunction shape.

If the budget test does not close, preserve the exact source. Use the Suzuki null equation or `WI-269` multiplier form to constrain the translated correlations of `sqrt(Q_t)` beyond the sharp support-only Haagerup--de la Harpe bound. The most concrete next experiment is a multi-shift/finite-partition compression that keeps several `Q_{t+h_j}` simultaneously and retains the continuum archimedean edges and their sign change at `h_0`; unsigned compression erases the known screening channel.

## Stress tests

Any proposed bootstrap must survive the existing obstructions. `WI-257` blocks generic bounded-self-adjoint regularity upgrades. `WI-263` defeats one-prime sign/Bochner reasoning. `WI-264` shows that finitely many source atoms can be hidden from autocorrelation observables, and `WI-265` shows generic first-crossing positivity does not recover the missing source geometry. `WI-268` prevents silently assuming a one-signed ground state from standard semigroup theory. `WI-273` shows why the single narrow-cut Carleman route saturates. `WI-275` prevents counting a different convex combination of the same two complementary mass inequalities as new progress: their sharp mass-only envelope is already the harmonic minimax reserve. `WI-276` additionally prevents claiming a better one-shift compact-support decorrelation constant without using extra structure: its nilpotent-shift coefficient is sharp even for nonnegative square-root energy profiles.

The support cover from `WI-267` remains necessary but insufficient. Translated activity at a gap point does not by itself imply nonzero `C_v(\log n)`, because the autocorrelation integrand also contains the unshifted value. Likewise the PSD multiplier form of `WI-269` does not by itself force a positive prime edge: long-range archimedean interaction can finance short-range/nodal overlap unless a quantitative source-specific obstruction rules that channel out.

Any argument using pointwise formulas must respect the full-domain issue. The first null mode lies in `D(A_a)`, not automatically in `H_0^1`; stronger regularity used to constrain `M_L`, `Q_t`, or couple cuts must be proved from Suzuki's operator/form rather than assumed.

## Evidence boundary

The harmonic reserve and the cross-cut shift reserve are exact consequences of the already established first-crossing form identities plus, for the latter, the classical nilpotent numerical-radius theorem. Neither proves that the combined reserve exceeds `K_+`, neither proves that the first null mode is one-signed, and neither forces a prime-lag autocorrelation on the sign-changing branch.

The sharpness statements are relaxation statements. `WI-275` is sharp for the mass-only pointwise problem, and `WI-276` is sharp for the one-shift compact-support correlation problem. Their abstract extremizers need not be compatible with the exact Suzuki source equation simultaneously. That incompatibility is now one of the main remaining opportunities.

## Research disposition

The clue remains `accepted`. The immediate target is the **combined spectral-budget test** using `max(R_harm, R_shift)` rather than `R_harm` alone. Do not spend further passes optimizing scalar averages of the two complementary cut inequalities or generic one-shift support bounds; `WI-275` and `WI-276` are sharp for those information sets. If the combined budget cannot be forced from known `\lambda_r` constraints, move to genuine source-shape or multi-shift information from the exact Suzuki null equation/PSD signed-source multiplier form.