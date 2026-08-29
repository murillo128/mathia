---
type: adversarial-review
target: research/weil_inertia/findings/WI-011-refined-four-point-envelope-improves-certified-bound.md
---

# Adversarial review

## Adversary

The numerical `m = 438` conclusion appears to survive, but the persisted derivation in §2 does **not by itself establish the global trace--energy envelope at the strength suggested by the section title and the later reusable formulation**.

The exact point is the `k >= 2` branch. WI-011 proves there only

\[
D \ge 2R-k+\frac{R^2}{m-k}\ge \frac{km}{m-k}>2.
\]

That is sufficient for the actual WI-011 application because the same finding separately checks

\[
\Phi_{438}(A_{438})<2.
\]

It is **not** sufficient to conclude a general inequality `D >= Phi_m(E)` for arbitrary large `E`, since the second branch of `Phi_m(E)` is unbounded. Consequently the argument as currently written cannot support a globally reusable envelope/pressure theorem merely from the three displayed cases; it supports the fixed application range where the target value of `Phi` is below `2`.

This is material because the finding is labelled `EXACT-DERIVED`, names §2 an "Exact trace--energy envelope", and later recommends formalizing (3) as a finite falsification test. A downstream reader could reasonably reuse the displayed `Phi_m` as a globally proved envelope, which the stored `k >= 2` argument does not establish.

There is already a plausible repair from the independent qwen-lean formalization audit: issue `murillo128/qwen-lean#101`, Gate-0 target `a064eecdaf7ca8bd5ef5f9efe43dc8d79ac3249b`, replaces the `k >= 2` shortcut by compressing the excess of all large coordinates into one coordinate. Its algebra preserves `D`, produces an energy `E' >= E`, reduces to the valid one-large-coordinate case, and then uses monotonicity of `Phi_m` to recover `D >= Phi_m(E)`. The qwen-lean independent Gate-0 review reported `PASS` on that repair, but at the time of this review the repair is not yet part of the persisted Mathia finding and should not be treated here as an already integrated proof.

This objection can be resolved in either of two ways:

1. **narrow the Mathia claim** to the exact range actually needed for WI-011, making explicit that `k >= 2` is discharged only because `Phi_438(A_438) < 2`; or
2. **supply the compression argument** (or an equivalent proof) in the finding, thereby genuinely justifying the global envelope and pressure-transfer formulation.

The objection does **not** currently challenge equations (1), (5)--(7), or the numerical constant `0.672852563956...`; it challenges the stronger reusable envelope claim/derivation in §2.