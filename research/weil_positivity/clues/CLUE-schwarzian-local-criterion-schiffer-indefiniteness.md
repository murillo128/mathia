---
id: CLUE-weil-positivity-schwarzian-local-criterion-schiffer-indefiniteness
type: research-clue
status: proposed
origin: adversarial
target_line: weil_positivity
based_on:
  - research/weil_positivity/findings/WP-014-exact-schiffer-kernel-is-not-positive-definite.md
  - formalization/mathia/WP014SchifferIndefinite.lean
---

# Can the two-point Schiffer obstruction be detected from the local Schwarzian geometry?

## Observation

For a smooth locally injective real map `V`, the Schiffer-type kernel

\[
K_V(x,y)=\frac{V'(x)V'(y)}{(V(y)-V(x))^2}-\frac1{(y-x)^2}
\]

has diagonal limit governed by the Schwarzian derivative,

\[
K_V(x,x)=\frac16 S(V)(x),
\qquad
S(V)=\frac{V'''}{V'}-\frac32\left(\frac{V''}{V'}\right)^2.
\]

WP-014 shows that for `V(x)=pi*cot(pi/x)` the kernel is pointwise positive but every distinct pair in the tail domain has negative `2 x 2` Gram determinant.  The alternative finite proof found during formalization suggests that this failure may be readable from local differential data rather than from the full global pole expansion.

A formal Taylor calculation suggests the near-diagonal expansion

\[
K_V(x,x+h)=\frac S6+\frac{S'}{12}h+\left(\frac{S''}{40}+\frac{S^2}{60}\right)h^2+O(h^3),
\]

with all Schwarzian quantities evaluated at `x`.  Combining this with the diagonal expansion at `x+h` suggests that the `2 x 2` determinant begins at order `h^2` with coefficient

\[
\frac{S S''-S^3}{180}-\frac{(S')^2}{144}.
\]

If correct, the sign of this local differential invariant would give an immediate near-diagonal PSD/indefiniteness test.

## Research question

Is there a rigorous local criterion, expressed in the Schwarzian derivative and finitely many of its derivatives, that determines whether a Schiffer kernel leaves the positive-semidefinite cone already at the `2 x 2` level?

In particular, does the candidate coefficient above correctly control the first nonzero variation of

\[
K_V(x,x)K_V(x+h,x+h)-K_V(x,x+h)^2,
\]

and can its sign explain the WP-014 obstruction or a wider class of examples?

## Why it may matter

A successful criterion would turn WP-014 from a special cotangent counterexample into a local geometric mechanism.  It would connect Schiffer-kernel positivity directly to projective differential geometry and could distinguish which endpoint maps are structurally incapable of producing a positive Weil pairing before any global arithmetic or operator analysis is attempted.

It would also explain why a finite Taylor certificate can see the same obstruction as the global Mittag--Leffler proof: both could be manifestations of a local Schwarzian sign condition.

## Decisive test

First derive the near-diagonal expansion of the Schiffer kernel and its `2 x 2` determinant rigorously for a sufficiently smooth locally injective `V`, checking all coefficients and sign conventions independently.

Then:

1. evaluate the resulting invariant for the WP-014 map `V(x)=pi*cot(pi/x)` and verify whether it predicts negative determinant on a nontrivial tail interval;
2. test the criterion on controls such as Möbius maps, for which the Schwarzian and Schiffer kernel vanish;
3. find examples with positive, zero, and negative candidate coefficient to determine whether the criterion is only infinitesimal or extends to a useful finite-separation statement.

Failure of the proposed expansion or a family with the predicted local sign but opposite actual near-diagonal Gram sign would refute the current candidate criterion while still leaving open the broader Schwarzian question.

## Evidence boundary

The diagonal Schwarzian relation is classical structure, but the displayed higher-order kernel and determinant expansions are currently an exploratory calculation, not a persisted theorem or independently checked formal result.  WP-014 proves only the concrete cotangent-kernel obstruction.  No general Schwarzian criterion for Schiffer-kernel indefiniteness has yet been established.