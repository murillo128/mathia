# Weil-positivity research lines

This file holds the current mathematical questions suggested by the durable Weil-positivity intuitions. It is not a roadmap, task queue, status page, or history.

## Identify a sign mechanism that survives stationary scalarization without inserting the arithmetic quadratic direction

**Linked intuitions:** `MI-039-stationary-negative-type-transport-needs-quadratic-drift-for-weil-tail-control` through `MI-046-singular-character-tangents-collapse-to-a-fixed-boundary-state`.

WP-339 isolates the tail requirement: any scalar transport cost that universally controls the moving Kadison defect must have quadratic growth in the arithmetic displacement. WP-340 shows that one-ray stationary Hilbert geometry obtains such growth only from a Euclidean drift sector.

WP-341 extends the classification to the prime-exponent group. A translation-invariant CND cost dominates

`L(alpha)^2=(sum_p alpha_p log p)^2`

only when its Levy--Khinchin quadratic sector already contains the arithmetic logarithm as a bounded Hilbert covector, equivalently a rank-one PSD direction. A stationary metric cannot manufacture the Weil log-square from its oscillatory sector.

WP-342 shows that stationary operator-valued order-CND lifts do not evade this when the Weil-facing readout is one fixed positive linear functional. WP-343 closes broad moving-state variants under uniform domination by one fixed positive functional; in finite-dimensional `C*`-algebras arbitrary states remain trace-dominated and therefore collapse to the same scalar shadow.

WP-344 tests a seemingly singular escape. For a character path `chi_t(alpha)=exp(it h(alpha))`, normalize the chord by `t^2`. Every fixed interior `t` has purely oscillatory CND behavior and no Levy--Khinchin quadratic sector, while the `t->0` tangent recovers `h(alpha)^2`. On the source-generated `C*`-algebra, however, all normalized generators extend continuously to the same boundary point, and evaluation at that point is a **single fixed character/state** whose value is exactly `h(alpha)^2` and equals the norm on this transport family.

Thus the singular tangent has not escaped fixed scalarization: it has hidden it at the boundary. For the prime-exponent group, taking `h(alpha)=sum alpha_p log p` recovers the desired log-square only because that arithmetic covector was preloaded into the character path. Arbitrary alternative weights reproduce the same mechanism.

The surviving categories are narrower still. A genuinely new mechanism must use operator-level positivity before scalarization, a boundary/singular construction with **no common fixed state carrying the target square**, nonstationary/basepoint-dependent geometry, a genuinely noncommutative source domain, or an independent arithmetic theorem that derives the quadratic direction rather than selecting it in advance. A singular limit is not an escape if it converges to a fixed boundary readout.

## Use the full Maaß--Selberg finite part, not the positive height boundary square

**Linked intuition:** `MI-047-positive-maass-selberg-boundary-square-can-be-divisor-blind`.

WP-345 tests the direct boundary-square escape left by the Arthur-truncation/Maaß--Selberg program. Differentiating the exact rank-one truncated Eisenstein norm with respect to `tau=log T` gives the pointwise positive source-defined response

`|1+S(r)e^(-ir tau)|^2`.

But the same derivative annihilates the `T`-independent logarithmic-derivative block `m'/m` that carries the explicit-formula divisor. The sign theorem is therefore attached to the boundary phase rather than to the divisor-sensitive finite part.

An explicit meromorphic inner/CDD matched control makes the separation sharp. It preserves reciprocal symmetry and unitary-axis modulus, hence every direct boundary-square inequality, while inserting off-axis zero/pole pairs and changing `m'/m`. Positivity of the height boundary response is therefore **divisor-blind under the hypotheses that prove it**.

WP-346 strengthens that control from a scalar meromorphic toy to an exact self-adjoint scattering realization. A Robin half-line channel has reflection factor `(z-a)/(z+a)`; two identical channels realize the squared CDD factor exactly. Each channel has a positive full truncated Hilbert norm and positive boundary square, yet its finite logarithmic-derivative contribution can have either sign while the divisor has moved. Generic self-adjointness, unitarity on the axis and positivity of the complete truncated norm therefore still do not exclude the CDD deformation.

This does not close the automorphic route. The surviving question is now specifically whether **automorphic/source realizability couples the divisor-sensitive finite part to positive global geometry in a way generic self-adjoint scattering cannot imitate**: for example through Euler--Gamma structure, noncentral local/archimedean operators, correlated automorphic sectors, or a higher-rank truncation form with an independent sign theorem. A direct appeal to self-adjoint Hilbert-space positivity or boundary monotonicity is no longer an open mechanism.

## Keep source dependence distinct from sign coercivity

WP-341--WP-346 are no-escape theorems for broad stationary transport/readout and direct boundary-square/self-adjoint-scattering architectures. They do not prove that every nonlinear, singular, automorphic or operator construction fails, and they do not prove Weil positivity. Their use is to prevent source labels, operator dimension, adaptive states, singular character tangents, a genuine geometric boundary square or generic self-adjoint realization from being credited as arithmetic leverage when the sign-relevant square is still inserted through a chosen source covector, exposed by one fixed scalar state, or insensitive to divisor-changing matched controls.

The next proposal should state the exact automorphic/non-dominated operator-level operation that consumes the source before reduction to a scalar sign, and prove either that no interior or boundary scalarization reproduces the target square under matched non-arithmetic weights, or that the full source-realizability structure excludes divisor-changing inner factors for a reason independent of the desired zero sign. Otherwise the desired sign has merely been inserted, exposed or attached to a divisor-blind positive scattering response rather than generated.