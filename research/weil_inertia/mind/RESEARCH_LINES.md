# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## If using Bombieri truncations, control coefficient cost and height tightness rather than raw span separation

**Linked intuitions:** `MI-008-inertia-counts-offline-pairs-but-not-their-distance`, `MI-014-source-coercivity-must-survive-confluence-and-drifting-bows`.

Finite negative inertia detects off-line packets exactly but can lose coercivity with height. The unconditional critical-line exponentials are complete on bounded windows without forming a Bessel/Riesz family, so ordinary separation cannot rule out spectral collapse. Any truncation route still has to price coefficient growth and height tightness explicitly.

## Complete one-signed screening is closed; force quantitative unscreening or leave the one-sign class

**Linked intuitions:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols` through `MI-028-dyadic-screening-forces-a-uniform-archimedean-reserve-before-any-nonpositive-one-signed-weil-test`.

WI-284--WI-299 reduce complete one-signed screening to a finite source geometry. Powers of two make the positivity set a selector modulo `log 2`; rearrangement compresses it below radius `r_2=(log 2)/2` and decreases the prime-deleted archimedean form. At first crossing this would force `a_*<=r_2`.

The verification gate in the earlier WI-300 is now discharged. Mathia issue #152 independently reconstructed and interval-certified Zhu's pinned v2 compact-window theorem, including the normalization dictionary, giving

`lambda_0.8 >= 8.9e-18 > 0`.

Monotonicity therefore yields `a_*>0.8`, contradicting the complete-screening first-crossing requirement `a_*<=r_2`. That branch is closed under the ordinary computer-assisted-evidence boundary.

WI-301 removes the first-crossing and null-mode hypotheses altogether. For every nonzero real one-signed compactly supported `f`, dyadic screening

`C_f(k log 2)=0  (k>=1)`

forces

`q_arch(f) >= c_0 ||f||_2^2`,  `c_0=8.9e-18`.

Hence a dyadically screened one-signed test with `Q_W(f)<=0` must carry at least `c_0||f||_2^2` of unscreened prime-power interaction, and complete prime-power screening is impossible for any nonpositive test at any aperture.

The live source question is therefore quantitative **unscreening**. Can the mandatory reserve be localized to specific odd-prime lags, amplified into a coercive source lower bound, or combined with the other first-crossing structure? Alternatively, a surviving obstruction must use sign changes or incomplete dyadic screening, where the selector/rearrangement mechanism no longer applies.

## Keep structural reduction, computer-assisted compact positivity and unrestricted Weil positivity separate

WI-298 is an exact rearrangement theorem. WI-300 contains an independently replayed interval certificate on one fixed compact window. WI-301 combines those established inputs to obtain an aperture-independent theorem on a nonlinear screened one-signed class. None of these statements is unrestricted large-aperture Weil positivity.

The evidence hierarchy must remain explicit. The `8.9e-18` constant is rigorous computer-assisted interval evidence, not a formal Lean proof; the one-sign hypothesis is load-bearing; and sign-changing screened functions can exploit cancellation. A branch-specific positive theorem must not be promoted into a statement about all supported vectors or RH.