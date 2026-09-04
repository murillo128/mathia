# MI-009 — Full bounded-depth scalar universality squeezes signed spectrum into a vanishing central boundary layer

**Evidence level:** proved for the scalar universality classes covered by WI-145--WI-152

## Core intuition

A scalar inequality can reject one isolated off-line pair without being a genuine universal inertia detector. Remote spectral mass can repair finitely many scalar tests. At the opposite extreme, sufficiently broad source-free universality classicalizes the profile toward Fourier positivity.

The bounded-depth middle regime is now quantitative rather than merely smoothed. Full finite-multiset universality at strip depth `B` forces every negative spectral feature either into an `O(B^-1)` neighborhood of the origin with total mass `O(phi(0)/B)`, or to pay an exponentially large central value if it remains at fixed spectral radius. The remaining scalar escape is therefore a **source-justified central spike**, not arbitrary moving signed mass.

## Strongest justified principle

WI-145 shows that one conjugate pair violates a tempting negative-tail scalar bound, while WI-146 supplies the adversarial repair: finite two-point constraints can be repaired by remote spectral mass. WI-147--WI-149 show the opposite boundary: universal compact/superexponential classes force Fourier positivity, and bounded depth initially yields Gaussian-smoothed positivity.

WI-150 uses the full bounded-depth scalar census to obtain exact lattice-alias positivity. WI-151 strengthens this with phase-masked combs: for an even continuous spectral profile with the stated exponential moment,

`phi(a) >= -2 phi(0) sech^2(2 pi B a)`.

Thus fixed-radius negative dips collapse exponentially as the admissible depth grows unless the central value compensates.

WI-152 combines that phase-mask floor with the real two-point consequence `H>=0`. Fourier inversion then makes `phi` positive definite and gives `|phi(t)|<=phi(0)`. Integrating the two bounds yields

`int phi_- <= [C_*/(pi B)] phi(0)`

with the persisted explicit constant `C_*`. Negative mass outside a fixed positive radius is exponentially smaller. Hence if `B->infinity` and `phi(0)=o(B)`, the entire signed profile approaches the normalized nonnegative cone in `L^1`, not merely after Gaussian smoothing.

## What remains possible

The universal scalar hypothesis does not itself prove `phi(0)=o(B)`. A profile may attempt to survive by concentrating an increasingly tall central spike on a shrinking scale. The next scalar gate is therefore source-specific: derive from the actual admissible test-function/kernel class an upper bound on `phi(0)` relative to available strip depth. Alternatively leave the one-scalar category through matrix/joint/inertia information or restrict configurations using independent zeta-source theorems.

## Status / novelty

Fourier positivity, Bochner theory, Fejer inversion, and hyperbolic-function bounds are classical. The synthesis is the bounded-depth squeeze: **finite scalar tests are repairable, broad universality classicalizes, and full finite-depth universality permits signed mass only through a quantitatively expensive central boundary layer**.

## Falsification criterion

Construct a profile satisfying the full WI-151/WI-152 finite-multiset hypothesis that violates the pointwise or integrated negative-mass bounds, or derive a zeta-source kernel family whose central value stays sublinear in depth and thereby closes the remaining scalar escape.

## Lean-formalizable core

- Remote repair of finite scalar constraints.
- Phase-masked pointwise spectral floor.
- Real two-point positivity to positive-definite spectral profile.
- `O(phi(0)/B)` total negative-mass budget and tail localization.
