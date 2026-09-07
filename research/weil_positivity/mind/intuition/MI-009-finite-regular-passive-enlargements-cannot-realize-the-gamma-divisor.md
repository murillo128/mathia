# MI-009 — Dissipative positivity survives only after a source-forced completed-channel lift

**Evidence level:** exact/literature-backed passive, de Branges--Rovnyak, and Pythagorean-completion analysis through WP-182

## Core intuition

The passive Gamma boundary is no longer captured by a simple “too rigid or too flexible” dichotomy. Scalar lossless order is too rigid for the sign-changing Gamma phase, while scalar dissipation makes the phase flexible and the canonical positive kernel singular. WP-182 shows that a **vector completion** can nevertheless retain dissipation, cancel the boundary pole by a positive subkernel, and preserve a finite positive form.

The price is exact: positivity no longer controls the scalar target phase. It controls the weighted phase balance of the target channel and a compensating defect channel. A viable Weil mechanism must therefore derive that completed channel from Mathia's source geometry before scalarization; universal completion of an already fitted response is a matched control, not an explanation.

## Strongest justified principle

WP-178--WP-179 classify modified-determinant phase order. Ordinary determinant and `det_2` inherit one-sided phase motion from positive delay, while every higher modified determinant has a sign-changing scalar symbol even on a pure-delay control. WP-180 shows the parallel dissipative freedom: the elementary positive-real one-port `S(s)=(s+a)/(s+b)` has a tunable sign-changing boundary phase derivative.

WP-181 inserts the canonical scalar de Branges--Rovnyak kernel. At a regular dissipative boundary point its diagonal expansion is

`(1-|S|^2)/(2x) - |S|^2 theta_S' + O(x)`.

The positive absorption pole diverges, and subtracting only that scalar asymptotic leaves the sign-indefinite phase term. Thus ordinary scalar kernel positivity does not supply a finite signed boundary observable.

WP-182 identifies the exact non-scalar escape. For a non-extreme Schur function, the outer Pythagorean mate `A` satisfies `|S|^2+|A|^2=1`. The completed column `F=(S,A)` has a positive kernel equal to `K_S` minus the full positive Hardy defect kernel. The dissipative pole is absorbed before taking the boundary limit and the remaining finite diagonal obeys

`-|S|^2 theta_S' - |A|^2 theta_A' >= 0`.

The resistor--inductor matched control realizes this architecture with an explicit rank-one positive completed kernel while `theta_S'` still changes sign. Completion therefore restores order at the **coupled** level without making the scalar phase arithmetic.

## Counterevidence / boundary

WP-182 does not derive the Pythagorean mate from prime geometry, produce Mangoldt coefficients, identify the Gamma factor, or prove a global Weil form. Non-extreme scalar Schur completion is universal function theory. Matrix-valued, singular, or source-derived completions may contain more information, but they still need an independent theorem fixing the compensating channel and its coupling.

## Epistemic status

**Proved category boundary and positive completion control; open source-forced realization.** The Mathia synthesis is that the missing order may live on a completed relational object rather than a scalar component.

## Falsification criterion

Produce a scalar dissipative Schur theorem that forces the required one-sided target phase despite WP-180/WP-181; invalidate the WP-182 positive-kernel decomposition; or derive a Mathia-native completed channel whose finite-prime and real-place pieces arise from one source construction and whose positive boundary form yields the required Weil sign. The last outcome would be the intended escape.