# Weil-positivity research lines

This file holds the current mathematical questions suggested by the durable Weil-positivity intuitions. It is not a roadmap, task queue, status page, or history.

## Identify a sign mechanism that survives stationary scalarization without inserting the arithmetic quadratic direction

**Linked intuitions:** `MI-039-stationary-negative-type-transport-needs-quadratic-drift-for-weil-tail-control` through `MI-046-singular-character-tangents-collapse-to-a-fixed-boundary-state`.

WP-339 isolates the tail requirement: any scalar transport cost that universally controls the moving Kadison defect must have quadratic growth in the arithmetic displacement. WP-340 shows that one-ray stationary Hilbert geometry obtains such growth only from a Euclidean drift sector.

WP-341 extends the classification to the prime-exponent group. A translation-invariant CND cost dominates `L(alpha)^2=(sum_p alpha_p log p)^2` only when its Levy--Khinchin quadratic sector already contains the arithmetic logarithm as a bounded Hilbert covector, equivalently a rank-one PSD direction. A stationary metric cannot manufacture the Weil log-square from its oscillatory sector.

WP-342 shows that stationary operator-valued order-CND lifts do not evade this when the Weil-facing readout is one fixed positive linear functional. WP-343 closes broad moving-state variants under uniform domination by one fixed positive functional. WP-344 tests a singular character-path escape and shows the normalized tangent merely moves the desired square to one common boundary character/state; alternative weights reproduce the same mechanism.

The surviving categories are narrower still. A genuinely new mechanism must use operator-level positivity before scalarization, a boundary/singular construction with no common fixed state carrying the target square, nonstationary/basepoint-dependent geometry, a genuinely noncommutative source domain, or an independent arithmetic theorem that derives the quadratic direction rather than selecting it in advance.

## Use the full Maaß--Selberg finite part, not the positive height boundary square

**Linked intuition:** `MI-047-positive-maass-selberg-boundary-square-can-be-divisor-blind`.

WP-345 tests the direct boundary-square escape left by the Arthur-truncation/Maaß--Selberg program. Differentiating the exact rank-one truncated Eisenstein norm with respect to `tau=log T` gives the pointwise positive source-defined response `|1+S(r)e^(-ir tau)|^2`, but annihilates the `T`-independent logarithmic-derivative block carrying the divisor. Scalar CDD matched controls preserve every boundary-square inequality while moving that divisor.

WP-346 strengthens the control to exact self-adjoint scattering: Robin half-line channels realize the squared CDD factor while retaining positive full truncated norms and positive boundary squares. Generic self-adjointness, unitarity on the axis and positivity of the complete norm therefore do not control the divisor-sensitive finite term.

WP-347 now moves the matched control inside a fixed finite-volume one-cusp hyperbolic surface. A real point scatterer is a genuine self-adjoint extension with perturbed Eisenstein series and exact relative scattering factor

`phi_(alpha,z0)(s)/phi(s)=S_(alpha,z0)(1-s)/S_(alpha,z0)(s)`.

The relative factor changes the continued resonance divisor while preserving the same cusp geometry, positive Hilbert space, self-adjoint source operator and Eisenstein/relative-trace framework. Thus **one-cusp hyperbolic realizability itself is still not selective enough**. The surviving hypothesis must be arithmetic-specific: Hecke equivariance, Euler/local-global normalization, a canonical arithmetic correspondence, or another rigidity principle destroyed by the point interaction.

The live Maaß--Selberg question is therefore no longer whether the desired normalizer has a genuine self-adjoint automorphic-looking scattering realization. It is whether the unperturbed arithmetic structure ties the divisor-sensitive finite part to a positive operator/global form in a way that excludes source-defined point-scatterer deformations *for an independently arithmetic reason*. A sign theorem that uses only hyperbolic geometry, self-adjointness, one-cusp scattering or Hilbert positivity remains matched-control blind.

## Keep source dependence distinct from sign coercivity

WP-341--WP-347 are no-escape theorems for broad stationary transport/readout and boundary-square/self-adjoint-scattering architectures. They do not prove Weil positivity and do not rule out a genuinely arithmetic automorphic mechanism. Their use is to prevent source labels, operator dimension, adaptive states, singular tangents, positive geometric norms, or even one-cusp self-adjoint realizability from being credited as arithmetic leverage when the sign-relevant square is inserted through a chosen covector or the continued divisor can still move inside the declared category.

The next proposal should identify the exact arithmetic structure that a matched point scatterer cannot preserve and show how that structure acts *before* scalar separation to constrain the divisor-sensitive coordinate. Otherwise the desired sign has merely been attached to a positive but divisor-mobile scattering architecture rather than generated.