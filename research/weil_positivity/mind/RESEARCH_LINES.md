# Weil-positivity research lines

This file holds the current mathematical lines of investigation suggested by the durable Weil-positivity intuitions. It is not a roadmap, task queue, status page, or history.

## Recover useful arithmetic localization only by leaving exact scalar source-native convolution

**Linked intuitions:** `MI-001-positivity-needs-a-sign-producing-global-operation`, `MI-010-source-forced-critical-gram-can-have-the-wrong-weil-orientation`, `MI-011-prime-ray-marginals-do-not-determine-mixed-prime-coupling`, `MI-012-automorphic-multiplicity-does-not-prevent-global-scalarization`, `MI-013-critical-sector-transport-needs-new-global-arithmetic-structure`, `MI-014-nontrivial-zero-modes-screen-the-gamma-tangent-layer`, `MI-015-nonlinear-postprocessing-after-scalarization-cannot-create-a-new-distribution`, `MI-016-exact-weil-square-targets-linearize-while-positive-additive-preservation-cannot-absorb-the-critical-source`, `MI-017-source-native-pole-cancellation-is-rh-complete-but-irreducibly-signed`.

WP-287--WP-289 close arbitrary nonlinear post-processing of a scalar profile, exact cone-only nonlinear target escapes, and monotone positive preservation of the non-tempered critical Mangoldt covariance.

WP-290--WP-291 identify the finite source-native dilation hierarchy: any finite product of canonical coboundaries cancels the pole tangent but no nontrivial zero pole, remains tempered exactly under RH, and leaves both Jordan channels individually non-tempered. More finite differencing does not move the admissibility gate.

WP-292 exhibits the opposite escape. Convolving the critical Mangoldt half-density with the canonical counting half-density integrates `-zeta'/zeta` to `-zeta'`, removing the nontrivial-zero poles; after two dilation differences the result is unconditionally tempered. But this replaces prime-power localization by an all-integer counting carrier.

WP-293 closes the alternative exact-convolution inverse. If a scalar arithmetic half-density kernel `eta_a` exactly relocalizes the smoothed logarithmic carrier back to Mangoldt, coefficient comparison is ordinary Dirichlet convolution and forces `a=mu` uniquely. The only exact source-native scalar relocalization is Möbius inversion, whose transform is `1/zeta`; it necessarily restores the zero divisor, the signed kernel and the RH-equivalent screen.

The live construction problem must therefore relax at least one of **exactness, scalar source-native convolution, or one-channel linear recovery**. Find an approximate/coarse localization that retains enough information for the exact Weil quadratic form without reconstructing the full RH-complete source, or use a genuinely multi-channel, non-translation-invariant, boundary-conditioned, nonlinear or geometric coupling with an unconditional admissibility theorem. Merely tuning the arithmetic convolution coefficients is exhausted.

## Treat cancellation, admissibility, localization and final positivity as distinct gates

Finite dilation cancellation can remove the leading pole to arbitrary order while leaving admissibility RH-equivalent. Counting convolution can make admissibility unconditional while erasing the Mangoldt localization. Exact scalar arithmetic relocalization is uniquely Möbius and restores the same zero screen. These are different operations and different resources.

A future candidate must answer separately: what signed/global source transformation is forced; why the transformed object belongs to the required category unconditionally; which arithmetic localization survives or is recoverable; and why the final positive quadratic form is exactly the Weil form. Passing one gate by destroying the input needed by the next is not progress toward the endpoint.

## Use matched controls to distinguish pole/zero removal from arithmetic information

The matched counting half-density is tempered after every finite canonical coboundary hierarchy, and WP-292 itself shows that an all-integer counting convolution can screen the nontrivial-zero poles. WP-293 shows that exact scalar arithmetic recovery cannot hide behind a different inverse kernel. Any proposed partial/non-scalar recovery should therefore be tested against counting/generalized-prime controls and against the localization lost under convolution, so that any claimed Weil content is attributed to structure that genuinely distinguishes the Mangoldt source.