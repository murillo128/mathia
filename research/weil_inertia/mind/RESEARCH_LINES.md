# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## If using Bombieri truncations, control coefficient cost and height tightness rather than raw span separation

**Linked intuitions:** `MI-008-inertia-counts-offline-pairs-but-not-their-distance`, `MI-014-source-coercivity-must-survive-confluence-and-drifting-bows`.

Finite negative inertia detects off-line packets exactly but can lose coercivity with height. The unconditional critical-line exponentials are complete on bounded windows without forming a Bessel/Riesz family, so ordinary separation cannot rule out spectral collapse. Any truncation route still has to price coefficient growth and height tightness explicitly.

## Test the combined harmonic and nilpotent-shift reserve against the archimedean budget

**Linked intuitions:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols`, `MI-018-one-signed-first-crossings-pay-prime-overlap-or-short-range-mass`, `MI-019-simultaneous-cuts-create-a-positive-saturated-source-reserve`.

The first-crossing source equation has defeated finite-lag screening and generic positivity shortcuts. WI-274 turns the whole family of complementary sharp cuts into a positive saturated source reserve. [WI-275](../findings/WI-275-a-harmonic-minimax-reserve-is-the-sharp-mass-only-cut-bound.md) computes the sharp mass-only envelope

`R_harm(a)=2 integral_0^a lambda_r lambda_(a-r)/(lambda_r+lambda_(a-r)) dr`.

Its equality mass profile is monotone, so scalar CDF information cannot strengthen it.

[WI-276](../findings/WI-276-cross-cut-energy-obeys-a-sharp-nilpotent-shift-reserve.md) adds genuinely cross-cut information. For `f(t)=sqrt(Q_t)`, two separated cuts and the PSD null-form geometry give `|F_v(r)-S_v|` bounded by the shift correlation of `f`. Compact support makes translation by `2r` nilpotent of order `ceil(a/r)`, so the sharp numerical-radius theorem yields

`S_v >= r lambda_r/(1+cos(pi/(ceil(a/r)+1)))`.

The sign-free source reserve is therefore bounded below by the maximum of this shift family and `R_harm(a)`. On a one-signed branch complete prime screening is possible only if that maximum stays at or below `K_+`.

The immediate theorem is quantitative: derive enough rigorous information on `lambda_r` to decide the combined budget test. If current spectral constraints permit both reserves to remain below `K_+`, further progress must use structure discarded by **both** sharp relaxations. WI-275 exhausts complementary masses; WI-276's coefficient is sharp for arbitrary nonnegative compactly supported cut-energy profiles. The surviving inputs are actual Weil-source shape, regularity/nodal constraints of the null eigenfunction, compatibility among several shifts, or a source-preserving compression of the exact multiplier form.

## Treat support-only sharpness as a boundary, not as source sharpness

WI-276's Haagerup--de la Harpe extremizer proves that compact support plus `Q_t>=0` cannot yield a better one-shift constant. It does not prove that an actual Suzuki first-crossing energy profile can realize that extremizer while also saturating the harmonic mass envelope and the signed source equation.

That compatibility question is now a precise opportunity. A multi-shift or finite-partition argument is useful only if it keeps constraints that an arbitrary nonnegative support profile does not satisfy. Replacing the exact source by another unsigned compact-support inequality cannot cross the new boundary.

## Keep endpoint firstness, source reserve, sign geometry and prime overlap as separate gates

The combined reserve is sign-independent but remains a bound for the total saturated source. The one-signed prime-overlap tariff does not transfer to a sign-changing null mode, and ordinary semigroup positivity is unavailable in the relevant regime. Future work should preserve the exact reserve while adding only the source/sign information needed either to beat `K_+` or to prevent prime and archimedean cancellation from hiding inside the positive total reserve.
