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

## Owner

The objection to the displayed `k >= 2` shortcut is correct as a proof-audit point, but the global envelope itself survives. Here is a direct repair, reconstructed independently from the scalar definitions.

For every large coordinate write

\[
x_i=1+z_i,\qquad z_i>0,
\]

and let

\[
Z=\sum_{i\in L}z_i=R-k.
\]

Replace the `k` large coordinates by

\[
1+Z,\underbrace{1,\ldots,1}_{k-1},
\]

leaving all other coordinates unchanged. This preserves the total sum, so the transformed vector is still feasible. It also preserves `D` exactly: before compression the large-coordinate contribution is

\[
\sum_{i\in L}(2x_i-1)=k+2Z,
\]

while afterwards it is

\[
(2(1+Z)-1)+(k-1)\Psi(2)=1+2Z+k-1=k+2Z.
\]

The energy cannot decrease. Before compression the large-coordinate contribution to `E` is

\[
k+2Z+\sum_{i\in L}z_i^2,
\]

whereas afterwards it is

\[
k+2Z+Z^2,
\]

and `Z^2 >= \sum z_i^2` because all `z_i >= 0`. Thus the transformed configuration has the same `D`, an energy `E' >= E`, and at most one coordinate strictly above `1`.

The already valid `k=0,1` argument therefore gives

\[
D= D'\ge \Phi_m(E').
\]

Since `Phi_m` is nondecreasing,

\[
\boxed{D\ge \Phi_m(E)}
\]

for arbitrary admissible `E`, including the original `k >= 2` case.

The pressure-transfer statement follows globally as well. If `E+P>=A` with `P>=0`, monotonicity and the 1-Lipschitz property of `Phi_m` give

\[
\Phi_m(A)\le \Phi_m(E+P)\le \Phi_m(E)+P\le D+P.
\]

So equation (3) is globally valid; the original `Phi_438(A)<2` observation is only a shorter proof for the numerical application. This resolves the mathematical gap without narrowing equations (1) or (3).

## Adversary

The compression repair resolves the objection. Concentrating the excess `z_i` of all `k >= 2` large coordinates into one coordinate preserves the total sum and `D`, increases (or preserves) `E` because `(\sum z_i)^2 >= \sum z_i^2`, and reduces to the already valid `k=0,1` case. Monotonicity of `\Phi_m` then gives the global `D >= \Phi_m(E)`, and the stated 1-Lipschitz property yields the pressure-transfer inequality.

Closure is therefore pending durable persistence of this compression argument, and its role in the global envelope/pressure-transfer claim, in the canonical WI-011 finding. The mathematical claim itself need not change.

## Owner

The accepted excess-compression argument and its global pressure-transfer consequence are now integrated into the canonical WI-011 derivation and adversarial checks. The mathematical claim and numerical bound are unchanged.