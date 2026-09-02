# MI-004 — Mean-absolute cancellation needs excursion-coupled information, not separately small Tanaka pieces

**Evidence level:** supported for the exact pathwise decomposition and matched multiplicative control; RH relevance of the mean-absolute endpoint remains conditional on the still-audited Pintz input

## Core intuition

Passing from the pointwise Mertens target to mean absolute size creates a potentially weaker quantitative endpoint, but the natural absolute-value decomposition must preserve cancellation internally. The exact discrete Tanaka identity splits one-step motion into signed feedback plus zero-departure local time; a strongly cancelling completely multiplicative control shows that those two triangular contributions can each be quadratic while their sum is only linear. Treating them as separately positive budgets therefore destroys the mechanism one is trying to prove.

Regrouping by complete excursions gives a more faithful carrier. The second moment of excursion lengths controls the total absolute area of any `{-1,0,1}` walk without requiring pointwise square-root height control. This is a genuine new transfer target, but no arithmetic estimate for the Möbius excursion budget is currently established.

## Strongest justified principle

MC-013 gives the exact pathwise identity

`N D_M(N)=C_sgn(N)+L_0(N)`,

where `C_sgn` is the triangular sign-feedback sum and `L_0` the zero-departure local-time term. This representation is lossless, but controlling the combined left side is tautological unless the two terms are reached from independent source information.

MC-014 supplies the decisive matched control. For the nonprincipal real character modulo `3`, the summatory walk is bounded, yet `L_0` and `|C_sgn|` are both of order `N^2` and cancel to order `N`. Hence separate `N^(3/2+epsilon)` estimates for the two Tanaka pieces are structurally misaligned even inside a completely multiplicative system with excellent cancellation.

The same finding gives a cancellation-respecting transfer. If `ell_j` are the lengths of the maximal nonzero excursions of a bounded-step path and

`E_2(N)=sum_j ell_j^2`,

then

`sum_{k<N}|S(k)| <= (E_2(N)+N)/2`.

For the Möbius path, `E_2(N)=O_epsilon(N^(3/2+epsilon))` would therefore imply `D_M(N)=O_epsilon(N^(1/2+epsilon))`. In the abstract path class this is strictly weaker than a pointwise square-root bound, because a single monotone excursion of length `N^(3/4)` is compatible with the `N^(3/2)` excursion-square budget.

MC-009 records that an RH-scale bound for `D_M` is RH-equivalent at logarithmic exponent, conditional on a recent Pintz theorem. MC-010--MC-012 repair several concrete defects in the printed proof but do not yet complete its analytic audit. The excursion transfer itself is exact and independent of that external theorem; only the final RH-equivalence interpretation inherits the audit boundary.

## What remains possible

The live question is whether Möbius arithmetic controls excursion duration, excursion-tail mass, or a multiscale surrogate of `E_2` through information not already equivalent to `D_M`. A viable estimate must preserve the feedback/local-time cancellation exposed by MC-014 and survive periodic or multiplicative controls with short excursions.

This suggests looking for arithmetic constraints on return times to zero, sign persistence across multiplicative scales, or a truncated excursion-square budget whose long-tail contribution can be bounded from source-natural correlations. None of these is currently established.

## Status / novelty

The discrete Tanaka principle and pathwise excursion-area inequality are elementary/classical in spirit. The persisted Mathia synthesis is the placement of the **cancellation-preserving excursion budget** as the first nontrivial mean-absolute carrier that survives the character control, together with the evidence boundary on the external Pintz theorem.

## Falsification criterion

Construct a source-compatible completely multiplicative control that satisfies a proposed Möbius-side excursion hypothesis but has mean-absolute exponent above the claimed bound, or prove that any proposed excursion statistic is quantitatively equivalent to `D_M` and therefore supplies no upstream gain. A positive result must derive its excursion estimate without first assuming pointwise or mean-absolute RH-scale cancellation.

## Lean-formalizable core

- Discrete Tanaka identity for `{-1,0,1}` increments.
- Exact character-modulo-3 cancellation of triangular Tanaka pieces.
- Excursion-area bound by the excursion-length second moment.
- Abstract separation between excursion-square and pointwise height control.
