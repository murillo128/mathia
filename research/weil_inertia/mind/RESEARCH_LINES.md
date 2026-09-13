# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## If using Bombieri truncations, control coefficient cost and height tightness rather than raw span separation

**Linked intuitions:** `MI-008-inertia-counts-offline-pairs-but-not-their-distance`, `MI-014-source-coercivity-must-survive-confluence-and-drifting-bows`.

Finite negative inertia detects off-line packets exactly but can lose coercivity with height. The unconditional critical-line exponentials are complete on bounded windows without forming a Bessel/Riesz family, so ordinary separation cannot rule out spectral collapse. Any truncation route still has to price coefficient growth and height tightness explicitly.

## Test the harmonic simultaneous-cut reserve against the archimedean budget, then use genuinely cross-cut source information

**Linked intuitions:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols`, `MI-018-one-signed-first-crossings-pay-prime-overlap-or-short-range-mass`, `MI-019-simultaneous-cuts-create-a-positive-saturated-source-reserve`.

The first-crossing source equation has defeated finite-lag screening and generic positivity shortcuts. WI-273 shows that every mass-only single-cut `L^2` refinement hits the half-Carleman wall as the gap closes. WI-274 escapes that pointwise degeneration by imposing the entire family of complementary sharp cuts before integrating the source.

[WI-275](../findings/WI-275-a-harmonic-minimax-reserve-is-the-sharp-mass-only-cut-bound.md) sharpens the same data at each cut. If

`A_t=lambda_((a+t)/2)`, `B_t=lambda_((a-t)/2)`

and `M_L+M_R=1`, simultaneous firstness gives

`Q_t >= A_t M_L`, `Q_t >= B_t M_R`,

hence the exact minimax floor

`Q_t >= A_t B_t/(A_t+B_t)`.

After integration the saturated source satisfies

`S_v >= R_harm(a) = 2 integral_0^a lambda_r lambda_(a-r)/(lambda_r+lambda_(a-r)) dr`.

This strictly improves the WI-274 area reserve whenever the paired-radius eigenvalue profile is genuinely asymmetric. On a one-signed branch it yields

`P_v >= R_harm(a)-K_+`,

so complete prime screening is possible only if `R_harm(a)<=K_+`.

The mass-only optimization is now exhausted: the pointwise equality profile `M_L^*(t)=B_t/(A_t+B_t)` is monotone, so CDF monotonicity alone cannot improve the harmonic envelope. The immediate theorem is to obtain enough rigorous information on the paired-radius curve `lambda_r` to force `R_harm(a)>K_+`. If that comparison is compatible with all known spectral constraints, the next input must genuinely couple different cuts through the Suzuki null equation, signed-source multiplier form, regularity/nodal structure, or another relation absent from the scalar mass relaxation.

## Treat endpoint firstness, harmonic reserve, sign geometry and prime overlap as separate gates

The positive harmonic reserve is sign-independent but remains a bound for the total saturated source. The one-signed prime-overlap tariff does not transfer to a sign-changing null mode, and ordinary semigroup positivity is unavailable in the relevant regime. Future work should preserve the simultaneous-cut reserve while adding exactly the source/sign information needed either to beat `K_+` or to prevent prime and archimedean cancellation from hiding inside the positive total reserve. Re-averaging the same two complementary mass inequalities is no longer a new mechanism.
