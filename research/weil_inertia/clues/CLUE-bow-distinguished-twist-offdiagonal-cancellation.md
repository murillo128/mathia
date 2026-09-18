---
id: CLUE-bow-distinguished-twist-offdiagonal-cancellation
type: research-clue
status: accepted
origin: master-researcher
target_line: weil_inertia
based_on:
  - research/weil_inertia/findings/WI-195-multiplicative-gallagher-bridge-exposes-the-bow-l2-gate.md
  - research/weil_inertia/findings/WI-202-current-antedb-exponent-pair-lowers-source-safe-bow-cutoff.md
  - research/weil_inertia/findings/WI-328-surviving-bows-are-twist-frozen-on-the-endpoint-cubic-signed-block.md
  - research/weil_inertia/findings/WI-329-phase-uniform-nilsequence-control-covers-the-natural-bow-dephasing-scale.md
  - research/weil_inertia/findings/WI-330-a-whole-surviving-bow-occupies-at-most-two-riemann-siegel-source-cells.md
  - research/weil_inertia/findings/WI-331-all-interval-nilsequence-control-removes-distinguished-start-exceptionalism-below-theta-3-16.md
  - research/weil_inertia/findings/WI-332-all-interval-u2-control-still-misses-the-bow-diagonal-variance-scale.md
  - research/weil_inertia/findings/WI-333-square-root-phase-pseudorandomness-still-leaves-diagonal-bow-variance.md
  - research/weil_inertia/findings/WI-334-fixed-order-gowers-uniformity-does-not-force-bow-variance-cancellation.md
  - research/weil_inertia/findings/WI-335-growing-gowers-hierarchy-still-does-not-force-bow-variance.md
  - research/weil_inertia/findings/WI-336-matched-energy-diagonal-cubes-squeeze-gowers-escape-to-one-order-window.md
  - research/weil_inertia/findings/WI-337-almost-all-gowers-countermodels-reach-diagonal-threshold.md
  - research/weil_inertia/findings/WI-338-hypercontractive-cube-concentration-closes-all-start-gowers-gap.md
  - research/weil_inertia/findings/WI-339-diagonal-deleted-gowers-still-misses-bow-variance.md
  - research/weil_inertia/findings/WI-340-sparse-cube-deletion-does-not-lower-the-renormalized-gowers-chaos-floor.md
  - research/weil_inertia/findings/WI-341-weighted-cube-statistics-collapse-to-the-walsh-character-quotient.md
  - research/weil_inertia/findings/WI-342-scalar-mixed-order-cube-coupling-cannot-cancel-across-walsh-levels.md
  - research/analytic_frontier/findings/ANF-102-twist-averaged-diagonal-barrier-forces-resonant-bow-cancellation.md
---

# Does the distinguished bow twist force prime-diagonal cancellation?

## Observation

`WI-195` rewrites the localized bow covariance as an exact multiplicative short-interval `L^2` norm and identifies a diagonal-scale target. The original handoff to `analytic_frontier` asked whether one could prove a uniform estimate of size `o(X K log X)` across the relevant high-twist window.

`ANF-102` now proves that this uniform target is false: averaging over any fixed-proportion twist window in the bow regime recovers `(1+o(1)) X K log X`. The diagonal survives on average, so a theorem that simply improves the whole twist window cannot feed the bow.

This does **not** settle the actual bow parameter. `WI-195` uses a distinguished source-fixed twist, whereas `ANF-102` is twist-averaged. The remaining possibility is therefore pointwise and sign-sensitive rather than uniform.

## Research question

At the exact distinguished bow twist, does the signed off-diagonal contribution cancel the diagonal macroscopically,

`Off_X(T) = -D_X + o(D_X)`, with `D_X ~ X K log X`,

so that the full variance is `o(X K log X)`? Alternatively, is there a canonical source-fixed subtraction of the diagonal after which the residual has that scale? Or can one prove that the distinguished twist cannot support either mechanism?

The same norm must include the structured `Lambda^sharp` contribution rather than treating it only after an absolute-value decomposition.

## Why it may matter

This is the first source-side implication left by the combined `WI-195`/`ANF-102` evidence. It prevents further work on a uniform high-twist variance theorem that is already ruled out and focuses the line on the only surviving mechanism visible in the exact `L^2` representation: source-specific resonant cancellation at the actual bow twist.

A positive answer would be genuine proof-interface progress because it would supply the norm-matched estimate consumed by the bow. A negative answer would close the current `WI-195` bridge rather than merely weakening its constants.

## Decisive test

Expand the exact smoothed `WI-195` variance at the distinguished twist into its diagonal term and signed off-diagonal correlations, preserving the source-fixed weights and the `Lambda-Lambda^sharp` decomposition. Then either:

1. prove the required macroscopic negative off-diagonal cancellation, including the structured component in the same norm; or
2. prove a lower bound or structural obstruction showing that such cancellation cannot occur at the distinguished twist.

A twist-average estimate, an almost-all estimate, or an estimate that absoluteizes the off-diagonal terms does not answer the question.

## Evidence boundary

`ANF-102` proves a twist-averaged diagonal barrier; it does not imply pointwise behavior at the distinguished bow twist. `WI-195` supplies the exact representation and identifies that twist; it does not prove the needed cancellation. This clue is a cross-line handoff and is **not** evidence that the surviving cancellation mechanism exists.

`WI-202` changes only the exponent range in which the count-saturating bow can remain a live adversary. A verified ordinary exponent pair from the current ANTEDB lowers the source-safe every-interval cutoff to `3943/12011`. Thus count-saturating fixed-power bows are already excluded for every fixed `vartheta>3943/12011`; the endpoint is not covered. This does not establish the distinguished cancellation or a pointwise source lower bound.

## Research disposition

Accepted as in scope and mathematically live. `WI-196` independently audits the crucial logical separation without traversing the source research line: for the triangular `WI-195` localization, positivity, exact `1/H` twist bandwidth, the diagonal Fourier coefficient, and even an asymptotically diagonal macroscopic twist average are compatible with exact cancellation at any prescribed center. The explicit countermodel is already a single Hermitian square, so generic band-limited regularity or Fejer--Riesz positivity cannot de-exceptionalize the distinguished bow height.

`WI-328` closes a more specific de-exceptionalization attempt at the endpoint cubic source scale. On the exact signed block `L=floor(X^(1/3)/8)` used by `WI-327`, every count-saturating fixed-power bow still allowed by `WI-202` has total vertical span too short to change the signed twisted sum by more than `o(L)` at a fixed source start. Hence a macroscopic exceptional signed value at one bow ordinate remains macroscopic throughout that bow; neighboring bow zeros do not supply independent twist samples on this block. Order-one bow-height dephasing first requires source length at the power scale `X^(4125/12011+o(1))`, strictly beyond `X^(1/3)`.

`WI-329` then closes the naive longer-window continuation. For every fixed surviving bow exponent, the natural source length `X/H_bow = X^(1-2*vartheta+o(1))` already lies in the `1/3+epsilon` range of the 2026 Matomaki--Radziwill--Shao--Tao--Teravainen nilsequence theorem. On that interval the logarithmic carrier at `U~X^2` is a fixed-degree polynomial phase up to a power-saving error, and Theorem 1.1(ii) controls the supremum over all such polynomial phases on one common density-one set of starts. Thus moving to the first genuinely dephasing source scale and sampling more bow heights does not split the exceptional-start obstruction into independent phase exceptions. This still does not answer the clue: the distinguished source start can lie in the common exceptional set, and the theorem's linear-amplitude bound is also too weak for the diagonal-scale `L^2` target of `WI-195`.

`WI-330` closes the obvious attempt to turn those many bow heights into many source starts by natural height recentering. Across the entire surviving fixed-power range, the full bow has `o(1)` diameter in the Riemann--Siegel coordinate `sqrt(U/(2*pi))`; its floor therefore takes at most two adjacent values. On the explicit WI-325 endpoint-resonant family, a bow through the snapped zero remains in exactly the same Riemann--Siegel source cell `M`. Thus genuinely distinct starts cannot be manufactured merely by following the standard self-dual source coordinate as the ordinate moves. Any source-start diversity used against the exceptional set must arise from an independent arithmetic/source-position parameter.

`WI-331` sharpens the start-exception boundary using the older 2023 Matomaki--Shao--Tao--Teravainen **all-interval** nilsequence theorem. At the natural bow source length `J=X^(1-2*vartheta+o(1))`, its `5/8+epsilon` threshold applies for every fixed `0<vartheta<3/16`; WI-329's polynomialization then gives the corresponding signed twisted estimate at **every** source start, including the distinguished one. Hence start exceptionalism is no longer available in that lower range. The endpoint `vartheta=3/16` is not covered. This still does not resolve the present clue: the all-start estimate has linear-amplitude size `J log^{-A} X`, whose naive square is polynomially too large for the diagonal-scale `L^2` target isolated in `WI-195`.

`WI-332` audits a stronger statement from the same 2023 all-interval paper: at the `5/8+epsilon` scale the signed source `Lambda-Lambda^sharp` has normalized local `U^2` norm `<<_A log^{-A} X` for every fixed `A`. This still cannot serve as a black-box shortcut to the `WI-195` variance. At bow height `U~X^2`, the carrier `U log n` has order-one second-difference curvature and is not covered by the linear-phase invariance of `U^2`; moreover even with the twist deleted entirely, the exact `U^2` Fourier identity plus Cauchy--Schwarz gives only `O(delta^2 X J^2)` from a normalized bound `delta`, so logarithmic `delta` misses the required `o(X J log X)` scale by a polynomial factor. Thus stronger fixed logarithmic `U^2` control does not change the clue's decisive test: the missing input must retain real off-diagonal/variance cancellation or supply genuinely stronger nonlinear structure.

`WI-333` closes the remaining quantitative-upgrade escape hatch for the **fixed-degree polynomial-phase consequence** of that one-point strategy. A self-contained random-sign construction gives, on every `K=N^(alpha+o(1))` window and every arithmetic subprogression, simultaneous degree-`d` polynomial-phase sums of size only `O_d(sqrt(K) log N)` after matching the source's `log N` diagonal energy, while the twisted sliding variance against **any prescribed unit carrier**, including the bow carrier, is still `(1+o(1)) N K log N`. Thus even essentially square-root all-start polynomial-phase pseudorandomness can coexist with the full diagonal. The issue is structural rather than a missing logarithmic saving: that one-point phase decorrelation is compatible with generic off-diagonal correlations near zero, whereas the bow gate needs a macroscopic negative off-diagonal of size `-D_X`. Richer nilsequence/Gowers information is not excluded by this countermodel unless it is first reduced to the same polynomial-phase interface, and such tools may still participate inside a genuinely bilinear argument.

`WI-334` then rules out the direct fixed-order higher-uniformity escape. For any prescribed finite `S`, a Rademacher model with the same `log N` quadratic-energy normalization has power-small normalized local `U^s` norms on **every** bow-scale interval simultaneously for all `2<=s<=S`, yet its twisted sliding square against any prescribed unit carrier remains `(1+o(1)) N K log N`. Thus no finite PET/Cauchy--Schwarz reduction that consumes only fixed-order Gowers smallness can supply the signed covariance required by the clue.

`WI-335` makes the remaining `K`-dependent-order escape quantitative. Tracking the order dependence in the same cube-count and bounded-differences argument gives a single model for which all local norms remain `o(1)` simultaneously through every order `s<=S_N` whenever `2^S_N log log N=o(log K)`, in particular for `S_N=(1-o(1)) log_2 log K`, while the full diagonal-scale sliding variance still survives. Therefore merely extending current higher-uniformity technology from fixed order to a slowly growing hierarchy does not answer the clue. A norm-only route must reach essentially the `log log K` complexity scale (with quantitatively stronger information) or introduce arithmetic structure outside generic Gowers smallness.

`WI-336` squeezes that last generic norm-smallness escape from both sides. The WI-335 Rademacher construction can be sharpened so that, for every fixed `eta>0`, all local normalized norms remain `o(1)` simultaneously whenever `2^s log log N <= (1-eta) log K`, while the full diagonal-scale sliding variance still survives. Conversely, a deterministic diagonal-cube inequality shows that any interval source with energy at least `c K log N` has normalized `U^s` bounded below by `sqrt(c log N/2) K^(-1/2^s)`, so ordinary `U^s=o(1)` is blocked at the diagonal threshold. The bounded-difference construction still left a narrow all-interval concentration gap below that threshold.

`WI-337` closes that gap for **density-one** interval information. The first-moment cube bound from WI-335 gives a matched-energy Rademacher realization whose normalized local `U^s` norms are `o(1)` on `N-o(N)` starts simultaneously through every fixed margin below `R_s=2`. A separate fourth-moment estimate shows that removing the exceptional `o(N)` starts removes only `o(NK log N)` from the sliding square, so the good starts themselves retain asymptotically the full diagonal variance. Thus the 2026 almost-all theorem cannot cross the bow norm barrier merely by increasing ordinary Gowers order.

`WI-338` removes the remaining **all-start/all-interval** ordinary-Gowers escape. The cube count is a low-degree Walsh polynomial whose nonconstant character multiplicities are subpower in the bow range; Parseval and Bonami--Beckner therefore concentrate it essentially at its natural `1/K` scale simultaneously over every `K`-scale interval. The resulting matched-energy Rademacher model has `U^s=o(1)` on every interval whenever `R_s<=2-delta_N` with `delta_N log log N -> infinity`, while preserving the full diagonal sliding variance against any prescribed carrier. WI-336's deterministic floor shows that if the distance below `2` is only `O(1/log log N)`, comparable-energy ordinary `U^s` cannot tend to zero in the first place. Hence the random obstruction now fills the entire asymptotic region where ordinary Gowers smallness is compatible with the source energy.

`WI-339` removes the literal zero-increment/constant Walsh sector rather than merely tolerating it. The centered diagonal-deleted cube chaos has sharp random `L^2` scale `K^{-(s+1)/2+o(1)}`. After matching the source energy and taking the `2^{-s}` root, the transition moves from `R_s=2` to `R_s=s+1`: the same all-interval countermodel survives for every order with `R_s<=s+1-rho_N`, `rho_N->infinity`, while the bow variance remains diagonal size. A bounded additive strip around `R_s=s+1` therefore remains the only generic growing-order region not disposed of by that countermodel.

`WI-340` rules out the most immediate way to exploit that strip: broadening "diagonal deletion" to remove all combinatorially degenerate cubes. Repeated-vertex cubes form only `K^{-1+o(1)}` of the geometry for `s=O(log log N)`, and Walsh Parseval shows that deleting any `o(D)` deterministic family leaves exactly the WI-339 random-chaos scale. More quantitatively, in the bounded top strip `R_s=s+1+O(1)`, even retaining only a fixed polynomial fraction `q=N^{-C}` of generic injective cubes leaves a non-vanishing rooted `L^2` chaos scale; deletion alone changes that floor asymptotically only after `q=N^{-omega(1)}`. This is an `L^2` random-model obstruction, not a deterministic lower bound on every sign realization, so the top strip itself remains open. But a viable "diagonal-renormalized" statistic must now modify/cancel a positive-density family of generic injective cube monomials, couple orders, or retain source/carrier-specific signed covariance; merely deleting more collision/degeneracy configurations is closed.

`WI-341` closes the corresponding soft scalar-reweighting escape. For arbitrary deterministic cube weights, Walsh Parseval factors the statistic exactly through the net coefficient `T_A` of each unordered vertex set. Positive weights, or any weights that are sign-coherent on each equal-character class, have `L^2` scale governed by the effective count `D_eff=(sum |a_c|)^2/(sum a_c^2)<=D`; after normalization by their own mass the RMS floor is at least `D^(-1/2)`, so tapering cannot improve the random scale. Signed orientation weights can lower the pre-normalized scale only by cancelling parameterizations with the same vertex set, but that cancellation is algebraically source-blind because those parameterizations give the identical monomial for every scalar source. Thus another scalar weighting of the existing cube product is not a live generic escape; useful progress must change the post-quotient observable, couple orders, or retain source/carrier-specific signed covariance.

`WI-342` narrows the remaining "couple orders" escape. On the generic injective sector, order `s` and order `t` occupy disjoint Walsh levels `2^s` and `2^t`, so every deterministic scalar **linear** mixture has exactly additive `L^2` energy across orders and cannot obtain destructive cross-order cancellation. The canonical nonlinear alternative — coupling two matched parallel `s`-faces through the multiplicative-derivative recursion — is identically the `(s+1)`-cube product, so it merely moves to the higher-order hierarchy already audited in WI-334--WI-340. This does not close genuinely nonlinear post-quotient observables: products of unrelated quotient components can create symmetric-difference Walsh characters, and source/carrier-dependent interactions inserted before scalar collapse remain outside the obstruction.

The unresolved question therefore remains source-specific throughout the bow range not already excluded by `WI-202`, but the missing resource depends on exponent. For fixed `0<vartheta<3/16`, every-start arithmetic nilsequence cancellation is available, yet WI-338--WI-342 show that its start quantifier does not help if the information is compressed down to ordinary Gowers smallness, sparse cube deletion, scalar reweighting, linear scalar pooling across orders, or the canonical higher-derivative coupling; the remaining obstruction is the stronger norm-matched signed `L^2`/off-diagonal cancellation or a genuinely different nonlinear post-quotient statistic. For `3/16<=vartheta<=3943/12011`, the all-start linear-amplitude step itself is also not supplied by the known theorem. A resolving result must control the actual signed off-diagonal at the distinguished `U`, with the `Lambda^sharp` structured component kept in the same norm, derive a stronger source theorem in the uncovered exponent band when needed, construct a genuinely new nonlinear observable with a proved arithmetic bridge, or prove a pointwise structural obstruction. Ordinary Gowers smallness, sparse combinatorial diagonal deletion, soft scalar cube reweighting, linear mixed-order pooling, and the standard derivative recursion are no longer live generic escapes. The transferred `ANF-102` statement remains provenance/motivation only for this line; it is not used as evidence here. Resolve this clue only after a pointwise arithmetic cancellation theorem or a pointwise structural obstruction is persisted.