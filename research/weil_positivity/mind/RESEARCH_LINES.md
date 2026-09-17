# Weil-positivity research lines

This file holds the current mathematical questions suggested by the durable Weil-positivity intuitions. It is not a roadmap, task queue, status page, or history.

## Identify a sign mechanism that survives stationary scalarization without inserting the arithmetic quadratic direction

**Linked intuitions:** `MI-039-stationary-negative-type-transport-needs-quadratic-drift-for-weil-tail-control` through `MI-045-uniformly-dominated-moving-readouts-collapse-to-fixed-scalarization`.

WP-339 isolates the tail requirement: any scalar transport cost that universally controls the moving Kadison defect must have quadratic growth in the arithmetic displacement. WP-340 shows that one-ray stationary Hilbert geometry obtains such growth only from a Euclidean drift sector.

WP-341 extends the classification to the prime-exponent group. A translation-invariant CND cost dominates

`L(alpha)^2=(sum_p alpha_p log p)^2`

only when its Levy--Khinchin quadratic sector already contains the arithmetic logarithm as a bounded Hilbert covector, equivalently a rank-one PSD direction. A stationary metric cannot manufacture the Weil log-square from its oscillatory sector.

WP-342 shows that a stationary operator-valued order-CND lift does not evade this when the Weil-facing readout is one fixed positive linear functional. Positive scalarization is scalar CND, so the same quadratic-sector theorem applies.

WP-343 closes a broad state-dependent version of the remaining loophole. Let the positive readout vary with the source state, but suppose all readouts satisfy one uniform domination envelope `0<=phi_alpha<=C omega` for a fixed positive functional `omega`. If `phi_alpha(Psi(alpha))` controls `L(alpha)^2`, then the fixed scalarization `omega(Psi(alpha))` controls the same square up to `C`, and WP-341--WP-342 apply again. In finite-dimensional `C*`-algebras every state is uniformly dominated by a fixed faithful trace, so arbitrary moving states or top-eigenvector choices do not escape. More generally, continuous nonnegative degree-one homogeneous readouts on a finite-dimensional positive cone are trace-dominated and collapse to the same fixed scalar shadow.

The surviving categories are consequently narrower. A genuinely new mechanism must use operator-level positivity **before** scalarization, a nonlinear readout that is not uniformly dominated by one positive functional, an infinite-dimensional/singular moving state where no finite domination constant exists, nonstationary/basepoint-dependent geometry, a genuinely noncommutative source domain, or an independent arithmetic theorem that directly supplies the required quadratic log displacement. Calling a finite-dimensional moving state “adaptive” is not enough.

## Keep source dependence distinct from sign coercivity

WP-341--WP-343 are no-escape theorems for broad stationary transport/readout architectures. They do not prove that every nonlinear or singular operator construction fails, and they do not prove Weil positivity. Their use is to prevent source labels, operator dimension, state dependence or spectral readouts from being credited as arithmetic leverage when the sign-relevant quantity is still uniformly dominated by one fixed positive scalarization.

The next proposal should therefore state the exact non-dominated/operator-level operation that consumes the source before reduction to a scalar sign, and prove that this operation is not reproduced by matched non-arithmetic generator weights. Otherwise the desired log-square has merely been inserted or exposed through the stationary quadratic sector.