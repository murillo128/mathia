# MI-009 — Quotient repair separates algebraic defect, robust defect, and coefficient-category collapse

**Evidence level:** supported by AF-078--AF-096; exact in the Banach/Lipschitz-free categories stated there

## Core intuition

The question “can information be repaired after a quotient?” has several distinct levels even after the repair category is fixed. A defect may be algebraically nonrecoverable, quantitatively separated from all recoverable data, or disappear entirely when the coefficient space is moved into a stronger structural category.

For Lipschitz Banach repair the hierarchy is now exact. The nonlinear-versus-linear defect is an operator-extension quotient on the forgotten barycentric fiber, robustness is distance from the closure of extendable operators, and dual coefficient spaces do not create a natural weak-star witness layer: they collapse the complete defect itself by ultrasummand linearization.

## Strongest justified principle

AF-078--AF-093 identify the qualitative categories. Linear repair is splitting. Lipschitz repair is equivalent to killing the extension class under the Lipschitz-free barycenter pullback, and the resulting defect is

`L(Z_F,K) / ran R_{F,K}`,

where `R_{F,K}` restricts ambient operators to the forgotten barycentric kernel. Ultrasummand and lifting hypotheses can force this quotient to vanish.

AF-094 supplies the exact stability modulus:

`rho([T]) = dist(T, ran R_{F,K})`.

A nonzero algebraic class can nevertheless have `rho=0` precisely when it lies in the norm closure of the extendable operators. Hausdorffizing the defect replaces `ran R` by its closure, and closed range is exactly the condition under which every algebraic defect is robust. The same closed-range gate is equivalent to a uniform extension-cost bound for operators that are already extendable.

AF-095 dualizes that margin. `rho([T])` is the optimal value of a bounded linear functional annihilating every extendable fiber operator. Robust defects are exactly those separated by such a witness; closure-only defects are invisible to every bounded linear witness.

The corrected AF-096 closes the tempting predual escape. If the coefficient is explicitly dual, `K=Y^*`, then `Y^*` is automatically an ultrasummand. AF-091 therefore forces every operator `T:Z_F->Y^*` to extend to `F(F)`, so `R_{F,Y^*}` is surjective, the Lipschitz-versus-linear defect vanishes, the projective-tensor map `j tensor_pi I_Y` is bounded below, and both unrestricted and weak-star-normal witness spaces are zero. A genuine Banach predual supplies a natural weak-star category only after entering a coefficient class in which this particular defect has disappeared.

## Evidence synthesis and boundaries

A positive arithmetic application must therefore name both the repair category and the coefficient category. For a general non-ultrasummand coefficient, algebraic nonrecoverability and robust nonrecoverability remain distinct and are measured by AF-094--AF-095. But simply declaring the coefficient to be a dual Banach space cannot expose a hidden normal witness for this defect; it removes the defect.

None of these abstract classifications supplies arithmetic provenance, equivariance, positivity, order, locality, or a canonical non-ultrasummand coefficient. Those structures must be forced by the source representation.

## Status / novelty

Lipschitz-free spaces, Banach `Ext`, closed-range theory, quotient duality, Hahn--Banach separation, projective tensor products, and ultrasummands are classical. The persisted synthesis is the exact fidelity hierarchy: **algebraic defect, robust defect, and coefficient-category survival are separate gates, and dual coefficients close rather than enrich the current Lipschitz defect**.

## Falsification criterion

Produce a nonzero AF-093 defect with coefficient `Y^*`, or a nonzero weak-star-normal annihilator in that dual-coefficient setting, contradicting the ultrasummand extension theorem in AF-096. An arithmetic application can evade the no-go only by justifying a different, non-ultrasummand coefficient/recovery category.

## Lean-formalizable core

- Operator-extension quotient for Lipschitz repair.
- Distance-to-range stability seminorm and closed-range gate.
- Dual annihilator formula for robust margin.
- Surjectivity of restriction to dual coefficients via ultrasummand linearization.
