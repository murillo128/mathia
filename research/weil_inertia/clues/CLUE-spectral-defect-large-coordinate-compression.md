---
id: CLUE-weil-inertia-spectral-defect-large-coordinate-compression
type: research-clue
status: resolved
origin: adversarial
target_line: weil_inertia
based_on:
  - research/weil_inertia/findings/WI-011-refined-four-point-envelope-improves-certified-bound.md
  - research/weil_inertia/findings/WI-011-refined-four-point-envelope-improves-certified-bound.review.md
---

# Does spectral-defect minimization admit a general one-large-coordinate compression principle?

## Observation

Adversarial review of WI-011 found that its stored `k >= 2` shortcut, `D > 2`, is sufficient for the concrete `m = 438` operating point but does not by itself prove the globally stated trace--energy envelope `D >= Phi_m(E)` for arbitrary energy.

The independent qwen-lean Gate-0 audit for `murillo128/qwen-lean#101` found a stronger repair: when several shifted eigenvalues `x_i = lambda_i - 1` lie above the linear-branch threshold `x_i > 1`, their excess can be concentrated into one large coordinate while replacing the others by threshold coordinates. In the derived construction the defect `D` is preserved, the total zero-sum constraint is preserved, and the comparison energy moves from `E` to `E' >= E`; the problem can then be reduced to the one-large-coordinate case and monotonicity of the envelope.

This compression is more structured than what is needed merely to repair WI-011 and may reflect an extremal principle for piecewise-quadratic/linear spectral penalties.

## Research question

For the WI-011 defect profile

\[
\Psi(1+x)=
\begin{cases}
x^2,&-1\le x\le1,\\
2x-1,&x>1,
\end{cases}
\]

under `x_i >= -1` and `sum_i x_i = 0`, is there a canonical extremal/compression theorem saying that minimization of

\[
D=\sum_i\Psi(1+x_i)
\]

at fixed or lower-bounded quadratic energy

\[
E=\sum_i x_i^2
\]

may always be reduced to configurations with at most one coordinate strictly above the branch threshold, with any remaining large coordinates pinned at the threshold?

If so, characterize the resulting extremizers and determine whether the same principle extends to a useful class of convex profiles that become affine after a threshold.

## Why it may matter

A genuine compression/extremal theorem would turn the ad hoc repair of WI-011 into a reusable description of the worst spectral configurations for the Gram defect. That could simplify future zero-side variational bounds, clarify when multi-large-eigenvalue configurations are harmless, and provide a more conceptual route toward the global dual/variational formulation suggested at the end of WI-011.

It may also distinguish which part of the trace--energy envelope is special to the particular `Psi` profile and which part follows from a general majorization or convex-order mechanism.

## Decisive test

Prove or refute a finite-dimensional compression theorem with explicit hypotheses. A useful first target is:

1. start from arbitrary `x_1,...,x_m >= -1` with zero sum;
2. when at least two coordinates exceed `1`, construct a transformed vector with the same zero sum and the same defect `D`, at most one coordinate strictly above `1`, and comparison energy `E' >= E`;
3. characterize equality and iterate the operation to a canonical normal form;
4. determine whether the induced normal form actually solves the fixed-energy minimum of `D`, rather than only furnishing the particular WI-011 envelope comparison;
5. search for a standard majorization/convex-analysis formulation or prior theorem before making any novelty claim.

A counterexample in which preserving `D` and zero sum necessarily decreases the comparison energy, or in which a multi-large-coordinate configuration yields a lower defect at fixed energy than every one-large-coordinate normal form, would kill the stronger interpretation.

## Evidence boundary

The qwen-lean Gate-0 algebra supplies a concrete compression sufficient to repair the proposed WI-011 global envelope, and that gate received an independent `PASS`. The corresponding Lean proof is not yet the evidence source for this clue, and neither the Mathia finding nor its current adversarial review establishes a general extremal or majorization theorem.

No claim is made here that the compression is novel, optimal, unique, or valid for profiles beyond the exact WI-011 setting. This remains a research question for the Weil-inertia Research Watch to reconstruct, stress-test, and check against prior art before any new finding is materialized.

## Research disposition

Outcome: supported

Resolved by:
- [[research/weil_inertia/findings/WI-020-trace-energy-envelope-sharp-one-spike-extremizers.md]]

The exact WI-011 profile admits a sharp fixed-energy theorem: `min D = Phi_m(E)`, with a unique high-energy eigenvalue multiset consisting of one super-threshold spike and a flat complementary spectrum. The same excess-compression proof extends to the scaled class of quadratic penalties continued by their tangent affine branch. WI-020 also gives quantitative slack for multiple super-threshold coordinates and for variance in the complementary spectrum. The broader statement for arbitrary convex profiles with affine tails is not asserted.