# MI-008 — Cross-scale fidelity and operator assembly require topology-matched collective non-escape

**Evidence level:** proved in the compact-target witness settings of AF-069--AF-075 and the operator-assembly settings of AF-105--AF-107

## Core intuition

Finite-stage success does not assemble automatically. For compact targets, witnesses may escape every compact set even when each cutoff has an excellent certificate. For operator-valued repairs, the corresponding obstruction depends on the topology and target category: weak compactness, weak-operator closed admissibility, and compactness require different family-level hypotheses.

The common invariant is **collective non-escape in the topology used by the final theorem**, not merely pointwise convergence or per-stage membership in a desirable class.

## Strongest justified principle

AF-069--AF-075 identify the compact-target witness gate. Compact-transversal margin, coherent approximant towers, precompact pooled witnesses, and vanishing Kolmogorov widths are equivalent ways of preventing finite witnesses from escaping across scale. Arbitrarily accurate but unrelated witnesses do not suffice.

AF-105 gives the original-range weak assembly analogue. A uniformly bounded repair family whose repaired orbit of each source point is relatively weakly compact has WOT cluster points that still land in the original Banach target rather than only its bidual. Collective weak compactness of the image of the source unit ball strengthens this to weakly compact operator assembly.

AF-106 separates assembly from admissibility. Equivariance, intertwining, positivity cones, and fixed affine identities survive bounded WOT limits because their defining classes are WOT closed. Weak compactness and compactness do not: finite-rank coordinate projections can converge strongly to the identity. Membership at every stage is therefore not a closure theorem.

AF-107 identifies the compact-operator endpoint exactly. Pointwise norm-compact orbits can give strong convergence while compactness is lost; collective norm compactness of the union of all repaired unit-ball images is the sufficient family-level gate that forces the assembled operator to remain compact.

## What remains possible

A concrete arithmetic application should derive the weakest collective compactness/coherence property appropriate to its destination category rather than impose compactness indiscriminately. Weak original-range recovery may require only pointwise weak non-escape; compact operators need collective norm compactness; additional algebraic/order constraints need their own closure audit.

## Status / novelty

Compactness, weak compactness, WOT/SOT convergence, Kolmogorov widths, and collective compactness are classical. The synthesis is their role as a hierarchy of exact fidelity/assembly gates: **per-scale success is weaker than a source-natural family theorem in the topology of the desired limit**.

## Falsification criterion

Exhibit an assembled repair in one of the covered categories that violates the stated collective/topological gate, or derive in a Mathia application a weaker source-forced condition that still preserves the required original range and operator class.

## Lean-formalizable core

- Compact-transversal and pooled-precompact witness criteria.
- Weak-orbit original-range assembly.
- WOT-closed preservation of equivariance/positivity identities.
- Collective norm compactness implying compact limit operator.
