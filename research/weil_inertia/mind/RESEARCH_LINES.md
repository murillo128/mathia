# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## If using Bombieri truncations, control coefficient cost and height tightness rather than raw span separation

**Linked intuitions:** `MI-008-inertia-counts-offline-pairs-but-not-their-distance`, `MI-014-source-coercivity-must-survive-confluence-and-drifting-bows`.

Finite negative inertia detects off-line packets exactly but can lose coercivity with height. The unconditional critical-line exponentials are complete on bounded windows without forming a Bessel/Riesz family, so ordinary separation cannot rule out spectral collapse. Any truncation route still has to price coefficient growth and height tightness explicitly.

## Use source/eigenfunction structure beyond the scalar aperture profile

**Linked intuitions:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols`, `MI-018-one-signed-first-crossings-pay-prime-overlap-or-short-range-mass`, `MI-019-simultaneous-cuts-create-a-positive-saturated-source-reserve`.

WI-274--WI-277 progressively sharpen the first-crossing source reserve. Complementary masses give the sharp harmonic envelope; one shift gives a sharp nilpotent reserve; and finite commensurate families give the scalarized Toeplitz reserve based on the top eigenvalue of `H_N(alpha)`.

WI-279 shows that retaining the Hilbert orientation of the cut path gives strictly more information. The signed cut covariance obeys `F_v(kh/2)=S_v-C_k(h)`, and the same commensurate family yields the bottom-spectrum reserve

`S_v >= (sum alpha_k k r lambda_(kr))/(sum alpha_k-eta_N(alpha))`,

where `eta_N(alpha)=lambda_min(H_N(alpha))`. It is always no worse than the WI-277 reserve and can be strictly stronger; the `N=3`, two-shift example improves the denominator from `3` to `5/2`. The coefficient is sharp for abstract PSD null-partition geometry.

But WI-278 still blocks every reserve whose numerator is controlled only by the currently certified scalar function `a -> lambda_a`. Its explicit admissible profile keeps `sup a lambda_a` below `K_+`, and the WI-279 denominator cannot reverse that ceiling. The next theorem must therefore preserve **source/eigenfunction information that strengthens the numerator or creates a new compatibility constraint**, not merely optimize another universal coefficient around the same scalar profile.

Live candidates are the exact Suzuki signed-source multiplier equation, source-specific noncommensurate cut compatibility, nodal/regularity shape of the actual null mode, or archimedean sign geometry. Further scalar-profile optimization is no longer a live route.

## Keep scalar-profile exhaustion and Hilbert-orientation information distinct

WI-279 corrects an overstrong reading of WI-278. Passing from cut vectors to the norm profile `sqrt(Q)` really does discard usable covariance orientation, and restoring it can improve a multishift reserve. What is exhausted is the ability of the **current scalar `lambda_a` data** to force a budget crossing, not every geometric refinement of the cut path.

That distinction is the opportunity. A successful argument must couple the extra Hilbert/source structure to information not admitted by the WI-278 counterprofile. Another support-only or PSD-only extremal inequality cannot suffice, because WI-279 is already sharp at that generic level.

## Keep endpoint firstness, source reserve, sign geometry and prime overlap as separate gates

The reserves are sign-independent, while the prime-overlap tariff is currently one-signed. A successful source-specific reserve improvement does not by itself solve the sign-changing branch, and a sign theorem does not replace the quantitative reserve. Future work should state which gate is being crossed.
