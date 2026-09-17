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

The unresolved question therefore remains source-specific throughout the bow range not already excluded by `WI-202`, but the missing resource now depends on exponent. For fixed `0<vartheta<3/16`, every-start linear-amplitude nilsequence cancellation is already available and the remaining obstruction is the stronger norm-matched `L^2`/off-diagonal cancellation. For `3/16<=vartheta<=3943/12011`, the all-start linear-amplitude step itself is also not supplied by the known theorem. A resolving result must control the actual signed off-diagonal at the distinguished `U`, with the `Lambda^sharp` structured component kept in the same norm, derive a stronger source theorem in the uncovered exponent band when needed, or prove a pointwise structural obstruction. Neither neighboring bow heights on the cubic block, phase dephasing combined only with the 2026 almost-all theorem, nor the standard Riemann--Siegel height-to-source map removes the norm barrier. The transferred `ANF-102` statement remains provenance/motivation only for this line; it is not used as evidence here. Resolve this clue only after a pointwise arithmetic cancellation theorem or a pointwise structural obstruction is persisted.
