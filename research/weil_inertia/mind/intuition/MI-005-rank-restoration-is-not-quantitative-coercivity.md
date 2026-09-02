# MI-005 — Algebraic rank restoration is not quantitative coercivity

**Evidence level:** proved for the full-packed residual prime-pair family and the stated scalar/local/global linear reweighting classes

## Core intuition

A collection of arithmetic blocks can recover full algebraic rank while becoming asymptotically useless for quantitative inequalities. Distinct defect kernels may have trivial intersection and yet approach one another at vanishing principal angle, so the concatenated operator is full rank but increasingly ill-conditioned.

This is the quantitative version of the fidelity distinction between injectivity and stability. For the residual Weil-inertia blocks, scalar balancing, arbitrary target-local right preconditioning, and uniformly well-conditioned invertible global reparametrization cannot repair the collapse. Any fourth-moment gain needs a source-specific mechanism that creates a genuine lower singular-value scale, not merely one that removes the exact kernel.

## Strongest justified principle

WI-100--WI-103 finish much of the local residual geometry. Phase purity gives capacity tents, true prime resonances have gap-coprime odd denominators, full recurrent packing collapses to an exact finite circle rotation, and every positive-defect component in the boundary parameter is an exact triangular island. The exceptional structure is highly rigid rather than arbitrary.

WI-104 then gives a positive algebraic result: two distinct positive-defect fully packed interactions sharing one source prime at one observation length have trivial common source kernel, so their horizontal concatenation has full row rank.

WI-105 shows why this is not a quantitative gain. There are infinitely many simultaneous full-packing configurations whose two kernels are asymptotically parallel, with principal angle tending to zero. WI-106 turns this into a weight-independent condition-number obstruction for two blocks.

WI-107 extends the obstruction to every fixed target count and to `J=o(sqrt(p/log p))` scalar multi-target aggregation. WI-108 shows that arbitrary target-local right processing, including nonscalar changes of target basis and singular target-side compression, cannot rescue relative source coercivity. WI-109 closes the uniformly conditioned global linear escape: invertible source/target transformations can restore conditioning only by paying a condition-number product as large as the defect they remove. Whitening transfers the anisotropy; it does not eliminate it.

## What remains possible

The surviving route must introduce information that changes the source-side near-kernel geometry itself. Possibilities include a source-specific rectangular/noninvertible selection, genuinely cross-target processing before block separation, coefficient/operator weights tied to the arithmetic source, positive-slack regimes away from full packing, or cross-scale structure not captured by the simultaneous full-packed family.

The decisive quantity is a lower singular-value or frame/coercivity bound in the actual weighted source geometry. Exact intersection statements or rank counts should be treated only as the zero-order gate.

## Status / novelty

Principal angles, condition numbers, preconditioning inequalities, and circle-rotation structure are classical or exact. The Mathia synthesis is the arithmetic stability boundary: **full rank can coexist with vanishing quantitative fidelity, and any boundedly conditioned linear reparametrization preserves that failure up to its own conditioning cost**.

## Falsification criterion

Construct a source-natural family in the covered full-packing regime with a uniform lower singular-value ratio after a boundedly conditioned linear transformation, contradicting WI-105--WI-109; or derive a many-target source theorem that breaks the near-parallel kernel family by using information absent from those blocks.

## Lean-formalizable core

- Full-rank restoration from trivial kernel intersection.
- Principal-angle lower bound on concatenation conditioning.
- Multi-block common-near-kernel estimate.
- Invariance under target-local right processing.
- Condition-number transport under invertible global preconditioning.