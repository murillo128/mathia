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

## Keep source dependence distinct from sign coercivity

WP-341--WP-344 are no-escape theorems for broad stationary transport/readout architectures. They do not prove that every nonlinear, singular or operator construction fails, and they do not prove Weil positivity. Their use is to prevent source labels, operator dimension, adaptive states or singular character tangents from being credited as arithmetic leverage when the sign-relevant square is still exposed by one fixed scalar state or inserted through a chosen source covector.

The next proposal should state the exact non-dominated/operator-level operation that consumes the source before reduction to a scalar sign, and prove that neither an interior positive scalarization nor a common boundary state reproduces it under matched non-arithmetic generator weights. Otherwise the desired log-square has merely been inserted or exposed rather than generated.