# MI-045 — Uniformly dominated moving readouts still collapse to fixed scalarization

**Evidence level:** exact synthesis from [WP-341](../../findings/WP-341-cross-prime-stationary-hilbert-transport-contains-the-arithmetic-log-square.md), [WP-342](../../findings/WP-342-positive-scalarization-does-not-let-stationary-operator-valued-transport-escape-the-arithmetic-log-square.md), and [WP-343](../../findings/WP-343-uniformly-dominated-state-dependent-readouts-collapse-to-fixed-scalarization.md).

WP-342 shows that stationary operator-valued order-CND transport cannot evade the scalar arithmetic log-square classification when the destination uses one fixed positive linear functional. WP-343 identifies the larger invariant class behind that argument: the readout may move with the source state, provided the whole family is uniformly dominated by one fixed positive functional.

Let `Psi(alpha)` be a positive stationary operator-valued transport object and let `phi_alpha` be positive functionals satisfying

`0 <= phi_alpha <= C omega`

for one fixed positive `omega`. If the moving readout has the required tail

`phi_alpha(Psi(alpha)) >= a L(alpha)^2`,

then positivity immediately gives

`omega(Psi(alpha)) >= (a/C) L(alpha)^2`.

The supposedly adaptive architecture has therefore produced a fixed positive scalarization with the same quadratic arithmetic growth, up to a constant. WP-341--WP-342 then force the arithmetic logarithm into the scalar Levy--Khinchin quadratic sector as a bounded Hilbert covector. The moving readout has not created a new sign mechanism; it has only selected pieces of a fixed scalar shadow that already contains the needed direction.

This closes a particularly broad finite-dimensional escape. In a finite-dimensional `C*`-algebra every state is bounded above by a constant multiple of one faithful trace. Hence arbitrary state-dependent expectations, including states chosen from top eigenspaces, fall under the domination theorem. The same applies to continuous nonnegative degree-one homogeneous readouts on a finite-dimensional positive cone: compactness of the trace-one section supplies a uniform trace envelope. Common spectral norms, Ky Fan-type positive readouts and determinant-root-type homogeneous observables therefore do not escape merely by being nonlinear in presentation if their positive-cone value is uniformly trace-dominated.

The genuine boundary is **failure of uniform domination or scalarization before the sign theorem**. Infinite-dimensional singular/vector states may have no common domination constant; an operator-level positivity argument may use mixed noncommutative relations before any scalar shadow is taken; nonstationary/basepoint-dependent transport may leave the Levy--Khinchin category. Those are materially different architectures and require their own source-selectivity and sign analysis.

The audit rule is thus stronger than “fixed scalarization fails.” Whenever a state-dependent positive readout is proposed, first ask whether the admissible readout family is uniformly dominated by one fixed positive functional on the actual positive cone. If yes, the stationary arithmetic log-square obstruction has already returned.

**Boundary.** WP-343 does not rule out infinite-dimensional singular readouts without a common envelope, genuinely operator-level positivity, non-positive functionals with an independent sign theorem, nonstationary geometry, or noncommutative source structure. It also does not prove Weil positivity. The conclusion is a no-escape theorem for uniformly dominated moving positive readouts of stationary operator-valued transport.