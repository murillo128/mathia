# MI-009 — Quotient repair is a category, regularity, and naturality problem, not one yes/no question

**Evidence level:** supported by AF-078--AF-087; exact in the stated Banach and finite-dimensional models

## Core intuition

The statement that information can be recovered after a quotient is incomplete until the admissible category is named. Linear, continuous metric, globally Lipschitz, homogeneous, equivariant, order-compatible, differentiable, and locally conical repairs have genuinely different existence and stability boundaries.

In particular, nonlinear geometry can bypass algebraic splitting, but demanding enough regularity or a linear tangent can silently reintroduce the original linear obstruction.

## Strongest justified principle

AF-078 identifies the linear endpoint: a bounded linear repair exists exactly when the quotient splits, and the space of repairs has a noncanonical shear freedom unless extra structure selects one. AF-081 shows that uniformly convex geometry can choose a canonical continuous homogeneous minimum-norm representative even for an uncomplemented quotient, so nonlinear metric repair is a real escape rather than a formal restatement.

AF-082 and AF-084 locate two rigidity thresholds. For separable Banach quotients, a global Lipschitz section already forces linear splitting; for any positive-homogeneous section, a bounded-linear first-order tangent at the homogeneity apex forces the section itself to be globally linear. AF-083 and AF-085--AF-087 refine the surviving middle category by bounded-scale, local, and tangent-cone moduli rather than pretending one global stability notion fits all geometries.

## Evidence synthesis and boundaries

The conclusion is category-relative, not a preference for nonlinear repair. A source application may legitimately force linearity, order, equivariance, or differentiability; if so, the stronger obstruction is the correct one. Conversely, failure of linear splitting is not evidence that a canonical continuous metric representative is impossible.

The arithmetic question is whether the chosen repair category is forced by the representation and preserves the target discriminator under its actual perturbations.

## Status / novelty

Banach-space splitting, Bartle--Graves/Godefroy--Kalton phenomena, and homogeneous differentiability are classical. The synthesis is the repair hierarchy and the requirement that an arithmetic application declare which rung it uses.

## Falsification criterion

Show that two supposedly different repair categories in this hierarchy coincide under the exact hypotheses of the arithmetic application, or exhibit an intrinsic repair with the claimed stability/naturality that crosses one of the stated rigidity thresholds without inducing the corresponding split.

## Lean-formalizable core

- Linear section/complemented-kernel equivalence.
- Minimum-norm representative in strictly/uniformly convex spaces.
- Lipschitz-section implication to linear splitting in the separable case.
- Homogeneous-apex linearization rigidity.
