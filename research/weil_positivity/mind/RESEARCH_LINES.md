# Weil-positivity research lines

This file holds the current mathematical lines of investigation suggested by the durable Weil-positivity intuitions. It is not a roadmap, task queue, status page, or history.

## Recover useful arithmetic localization only by leaving exact one-channel scalar source-native convolution

**Linked intuitions:** `MI-001-positivity-needs-a-sign-producing-global-operation`, `MI-010-source-forced-critical-gram-can-have-the-wrong-weil-orientation`, `MI-011-prime-ray-marginals-do-not-determine-mixed-prime-coupling`, `MI-012-automorphic-multiplicity-does-not-prevent-global-scalarization`, `MI-013-critical-sector-transport-needs-new-global-arithmetic-structure`, `MI-014-nontrivial-zero-modes-screen-the-gamma-tangent-layer`, `MI-015-nonlinear-postprocessing-after-scalarization-cannot-create-a-new-distribution`, `MI-016-exact-weil-square-targets-linearize-while-positive-additive-preservation-cannot-absorb-the-critical-source`, `MI-017-source-native-pole-cancellation-is-rh-complete-but-irreducibly-signed`, `MI-018-exact-weil-square-equality-makes-coarse-scalar-relocalization-exact`.

WP-287--WP-289 close arbitrary nonlinear post-processing of a scalar profile, exact cone-only nonlinear target escapes, and monotone positive preservation of the non-tempered critical Mangoldt covariance.

WP-290--WP-291 identify the finite source-native dilation hierarchy: any finite product of canonical coboundaries cancels the pole tangent but no nontrivial zero pole, remains tempered exactly under RH, and leaves both Jordan channels individually non-tempered. More finite differencing does not move the admissibility gate.

WP-292 exhibits the opposite escape. Convolving the critical Mangoldt half-density with the canonical counting half-density integrates `-zeta'/zeta` to `-zeta'`, removing the nontrivial-zero poles; after two dilation differences the result is unconditionally tempered. But this replaces prime-power localization by an all-integer counting carrier.

WP-293 closes exact coefficientwise scalar relocalization. If a scalar arithmetic half-density kernel `eta_a` exactly sends the smoothed logarithmic carrier back to Mangoldt, Dirichlet-convolution uniqueness forces `a=mu`; the inverse transform is `1/zeta`, restoring the signed kernel and zero screen.

WP-294 now closes the proposed **coarse/approximate-coefficient escape when the final Weil square form is still exact**. Equality on every autocorrelation square forces equality of the underlying distributions by polarization and Dixmier--Malliavin factorization; isolated log-integer atoms then force coefficientwise equality, and WP-293 again forces Möbius inversion. A smooth non-finite completion cannot hide atomic errors unless it imports compensating finite-place delta masses.

The live construction problem must therefore leave the direct one-channel scalar arithmetic-convolution architecture, not merely tune its accuracy. Plausible classes include genuinely multi-channel recovery, operator-valued or nonlinear source couplings formed before scalarization, non-translation-invariant/boundary-conditioned maps, or an approximate/restricted intermediate criterion equipped with a separate stability/equivalence theorem that reaches the exact Weil form. Merely making scalar relocalization coarse while retaining exact final equality is exhausted.

## Treat cancellation, admissibility, localization, recovery architecture and target exactness as distinct gates

Finite dilation cancellation can remove the leading pole to arbitrary order while leaving admissibility RH-equivalent. Counting convolution can make admissibility unconditional while erasing Mangoldt localization. Exact scalar arithmetic relocalization is uniquely Möbius and restores the same zero screen. WP-294 adds that exact equality on the full Weil square cone itself forces scalar relocalization to become exact, so coefficient approximation is not a free extra currency in that architecture.

A future candidate must answer separately: what signed/global source transformation is forced; why the transformed object belongs to the required category unconditionally; which arithmetic localization survives or is recoverable; why the recovery architecture escapes scalar uniqueness; and why the final positive quadratic form is exactly the Weil form. Passing one gate by destroying the input needed by the next is not progress toward the endpoint.

## Use matched controls to distinguish pole/zero removal from arithmetic information

The matched counting half-density is tempered after every finite canonical coboundary hierarchy, and WP-292 itself shows that an all-integer counting convolution can screen the nontrivial-zero poles. WP-293 shows that exact scalar arithmetic recovery cannot hide behind a different inverse kernel; WP-294 shows it also cannot hide coefficient errors behind the full autocorrelation cone. Any proposed non-scalar or restricted recovery should therefore be tested against counting/generalized-prime controls and against the localization lost under convolution, so that any claimed Weil content is attributed to structure that genuinely distinguishes the Mangoldt source.
