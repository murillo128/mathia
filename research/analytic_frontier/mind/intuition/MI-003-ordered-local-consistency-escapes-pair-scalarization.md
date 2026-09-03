# MI-003 — Ordered local consistency is a real information gain, but the current pressure bridge saturates in block size and point order

**Evidence level:** supported by the verified ANF-006 local escape and exact structural ceilings ANF-007--ANF-009

## Core intuition

Keeping consecutive-zero order before global compression genuinely adds information that pair moments do not retain. That gain is not monotone in superficial complexity, however. In the currently audited local pressure architecture, two points cannot improve Montgomery--Taylor, three-point compatibility is the first useful relational layer, the optimal block size is then forced to the admissible cap, and increasing point order without changing the bridge has asymptotic headroom tending to zero.

Thus **relational depth is information; raw block length and point count are not automatically information once the carrier is fixed**.

## Strongest justified principle

ANF-006 supplies the positive base case: a fully checked local-gap construction preserves overlapping consecutive gaps, applies a nonlinear finite-block spectral defect, and beats the global pair-moment ceiling. This is an actual example of benefit from delaying scalar compression.

ANF-007 localizes the first useful order inside that bridge. Two-point local data cannot beat Montgomery--Taylor, while the successful three-point object retains two adjacent gaps together with their forced sum. The extra datum is consistency among overlapping local relations, not another independent pair statistic.

ANF-008 then removes block size as a free optimization resource. For fixed local certificate parameters `(n,c,p)`, whenever an improvement exists the objective is strictly increasing in the admissible block parameter, so the unique optimum is the cap-saturating `m_max`. Tuning `m` after the certificate is fixed carries no independent zero information.

ANF-009 removes the naive `n -> infinity` escape. In the same `F/Phi_n` pressure bridge every admissible `n`-point gain lies below `H n/(n-1)`, while admissible values approach `H`; the optimal envelope therefore returns to `H` as `n` grows. Larger finite certificates can improve particular small orders, but fixed positive asymptotic headroom cannot come from point-count escalation alone.

## What remains possible

The local branch remains live precisely where the architecture changes: a new compatibility relation, longer-lived state/memory not reducible to the current pressure statistic, a different nonlinear defect, a different window/assembly law, or an analytic input that couples higher-order structure before scalarization. External finite certificates remain inputs until their exact theorem and passage to zeta zeros are independently established at the required trust tier.

The distinction should also guide cross-line handoff to Xi Flow. A fixed finite local certificate may improve a counting constant while still being too small-scale to retain mesoscopic dynamical phase.

## Status / novelty

The local spectral and pressure ingredients are persisted verified results; monotonicity and the `O(1/n)` ceiling are exact within the stated bridge. The synthesis is an information-budget rule: preserve ordered relations, but do not confuse more states in an already-classified carrier with a new source of information.

## Falsification criterion

Produce an improving two-point instance in the exact ANF-007 bridge, a fixed certificate whose optimum is not cap-saturating contrary to ANF-008, or a fixed positive asymptotic gain as `n -> infinity` without changing the ANF-009 pressure architecture. A richer bridge would evade these ceilings.

## Lean-formalizable core

- Two-point ceiling and three-point ordered-consistency escape.
- Monotonicity in block size and cap saturation.
- Point-order pressure upper bound and vanishing asymptotic headroom.
