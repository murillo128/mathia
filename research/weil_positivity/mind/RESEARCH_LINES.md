# Weil-positivity research lines

This file holds the current mathematical questions suggested by the durable Weil-positivity intuitions. It is not a roadmap, task queue, status page, or history.

## Identify a sign mechanism that survives stationary scalarization without inserting the arithmetic quadratic direction

**Linked intuitions:** `MI-039-stationary-negative-type-transport-needs-quadratic-drift-for-weil-tail-control` through `MI-046-singular-character-tangents-collapse-to-a-fixed-boundary-state`.

WP-339 isolates the tail requirement: any scalar transport cost that universally controls the moving Kadison defect must have quadratic growth in the arithmetic displacement. WP-340 shows that one-ray stationary Hilbert geometry obtains such growth only from a Euclidean drift sector.

WP-341 extends the classification to the prime-exponent group. A translation-invariant CND cost dominates `L(alpha)^2=(sum_p alpha_p log p)^2` only when its Levy--Khinchin quadratic sector already contains the arithmetic logarithm as a bounded Hilbert covector, equivalently a rank-one PSD direction. A stationary metric cannot manufacture the Weil log-square from its oscillatory sector.

WP-342 shows that stationary operator-valued order-CND lifts do not evade this when the Weil-facing readout is one fixed positive linear functional. WP-343 closes broad moving-state variants under uniform domination by one fixed positive functional. WP-344 tests a singular character-path escape and shows the normalized tangent merely moves the desired square to one common boundary character/state; alternative weights reproduce the same mechanism.

The surviving categories are narrower still. A genuinely new mechanism must use operator-level positivity before scalarization, a boundary/singular construction with no common fixed state carrying the target square, nonstationary/basepoint-dependent geometry, a genuinely noncommutative source domain, or an independent arithmetic theorem that derives the quadratic direction rather than selecting it in advance.

## Use the full Maaß--Selberg finite part and separate the unramified zeta block from ramified arithmetic inner factors

**Linked intuitions:** `MI-047-positive-maass-selberg-boundary-square-can-be-divisor-blind`, `MI-048-arithmetic-ramification-itself-supplies-off-critical-reciprocal-inner-factors`, `MI-049-unitary-moving-compressions-have-no-berry-trace-escape`.

WP-345 tests the direct boundary-square escape left by the Arthur-truncation/Maaß--Selberg program. Differentiating the exact rank-one truncated Eisenstein norm with respect to `tau=log T` gives the pointwise positive source-defined response `|1+S(r)e^(-ir tau)|^2`, but annihilates the `T`-independent logarithmic-derivative block carrying the divisor. Scalar CDD matched controls preserve every boundary-square inequality while moving that divisor.

WP-346 strengthens the control to exact self-adjoint scattering: Robin half-line channels realize the squared CDD factor while retaining positive full truncated norms and positive boundary squares. Generic self-adjointness, unitarity on the axis and positivity of the complete norm therefore do not control the divisor-sensitive finite term.

WP-347 moves the matched control inside a fixed finite-volume one-cusp hyperbolic surface. A real point scatterer is a genuine self-adjoint extension with perturbed Eisenstein series and exact relative scattering factor `phi_(alpha,z0)(s)/phi(s)=S_(alpha,z0)(1-s)/S_(alpha,z0)(s)`. The continued resonance divisor moves while the cusp geometry, Hilbert positivity and Eisenstein/relative-trace framework remain. This kills generic hyperbolic/self-adjoint realizability as a selector.

WP-348 pushes the control **inside the arithmetic congruence category itself**. For squarefree `Gamma_0(N)`, each scattering eigenchannel is a common completed-zeta scalar `g(s)` times finitely many ramified factors `nu_(p,+/-)(s)`. Those bad-prime factors are reciprocal under `s -> 1-s` and unitary on `Re s=1/2`, yet carry explicit source-defined off-critical zero/pole lattices. Broad labels such as automorphic, Hecke, Euler or arithmetic therefore do not force the full scattering divisor onto the critical line.

The same factorization gives a fixed-channel obstruction. In the constant cusp eigenbasis, any fixed linear combination of logarithmic derivatives that removes one prime's `+/-` local factors identically also has zero coefficient on the common `g'/g` term. Constant positive channel geometry cannot strip ramification while retaining the unramified zeta block. Algebraically dividing by the known local factors is normalization after scalarization, not a positivity theorem.

WP-349 strengthens this obstruction to arbitrary **positive moving compression after logarithmic differentiation**. On `s=1/2+it`, the two ramified phase velocities at each bad prime have the same strict sign. Their local logarithmic-derivative operator satisfies

`F_p(t) <= -c_p I`, `c_p=2 log(p) sqrt(p)/(sqrt(p)+1)>0`.

Therefore every positive state or positive `t`-dependent compression of that already-differentiated local block remains strictly negative. Positive channel motion cannot average the ramified contribution away; summing over bad primes only strengthens the one-sign obstruction.

WP-350 closes the corresponding **unitary pre-differentiation moving-subspace** escape. If a moving compression `B(t)=V(t)^*U(t)V(t)` of the critical-line unitary scattering matrix remains unitary, then its moving range is a reducing sector of `U(t)`. In the compressed phase generator the Berry/connection terms are pure gauge in trace, so

`tr Q_B(t)=tr(V(t)^* Q_U(t) V(t))`.

The same one-sign bad-prime bounds therefore survive every nonzero unitary moving restriction. Pre-differentiation motion cannot strip ramification while preserving only the common unramified phase and inherited unitary scattering structure.

The live Maaß--Selberg question is now categorical rather than a choice of channel motion. A successful route must distinguish the **unramified global normalizer from ramified local dressing before scalarization without remaining inside a unitary reducing compression**. A proper contraction/nonunitary defect, or a genuinely noncommuting adelic/global construction, may still escape the classification, but then ordinary Maaß--Selberg/Wigner--Smith positivity is no longer inherited and a new source-forced sign theorem is required. Algebraic division by the known factorization remains normalization, not positivity.

## Keep source dependence distinct from sign coercivity

WP-341--WP-350 are no-escape theorems for broad stationary transport/readout and boundary-square/scattering architectures. They do not prove Weil positivity and do not rule out a genuinely arithmetic mechanism that treats ramified and unramified data differently before scalarization. Their use is to prevent source labels, operator dimension, adaptive states, singular tangents, positive geometric norms, hyperbolic self-adjointness, generic congruence arithmetic, positive post-differentiation channel selection, or unitary moving pre-differentiation channel selection from being credited as sign leverage when the target square is inserted through a chosen covector or the full divisor still contains independent source-defined inner factors.

The next proposal should specify the exact unramified arithmetic coordinate, the nonunitary or genuinely noncommuting pre-scalar structure that isolates it, the independent theorem forcing a sign in that new category, and the matched ramified control it defeats. Otherwise the desired zeta block has merely been selected algebraically or by a reducing subspace rather than generated by positivity.