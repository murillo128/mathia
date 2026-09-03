# MI-009 — Quotient repair is a category, compactness, regularity, and naturality problem

**Evidence level:** supported by AF-078--AF-089; exact in the stated Banach, compact-fiber, and finite-dimensional models

## Core intuition

The statement that information can be recovered after a quotient is incomplete until both the admissible category and the gluing topology are named. Linear, continuous metric, globally Lipschitz, homogeneous, equivariant, order-compatible, differentiable, and locally conical repairs have different boundaries; independently, local repairs globalize only when their admissible fibers have enough compactness to prevent incompatible choices from escaping across finite subsets.

Thus **existence with optimal fidelity and naturality are separate gates**. A perfectly global repair may exist with the same local Lipschitz constant while still lacking a canonical, measurable, equivariant, or source-forced choice.

## Strongest justified principle

AF-078 identifies the linear endpoint: a bounded linear repair exists exactly when the quotient splits, with noncanonical shear freedom unless extra structure selects one. AF-081 shows that uniformly convex geometry can choose a canonical continuous homogeneous minimum-norm representative even for an uncomplemented quotient, so nonlinear metric repair is a real escape.

AF-082 and AF-084 locate rigidity thresholds: for separable Banach quotients, a global Lipschitz section forces linear splitting; for positive-homogeneous sections, a bounded-linear tangent at the apex forces global linearity. AF-083 and AF-085--AF-087 refine the surviving middle category by bounded-scale and tangent-cone moduli.

AF-088--AF-089 add a different axis. Local finite-subset Lipschitz selections can globalize **with exactly the same constant** when the compatible fiber slices are compact and the distance constraints are closed. Reflexivity is only one way to obtain that compactness; weak-star compact dual fibers give the same exact globalization in nonreflexive settings. The decisive resource is compact admissible fiber compatibility, not reflexivity itself.

## Evidence synthesis and boundaries

These results do not make quotient repair canonical. Compactness plus finite compatibility proves existence of a global selection, but does not by itself provide measurable dependence on external parameters, equivariance under source symmetries, uniqueness, or functoriality. Those properties can be exactly the arithmetic content a proposed representation needs.

Conversely, failure of linear splitting is not evidence that a continuous or optimally Lipschitz metric repair is impossible. The correct obstruction must be stated in the category actually forced by the arithmetic source.

## Status / novelty

Banach-space splitting, compactness principles, minimum-norm selections, and Lipschitz extension/selection theory are classical. The synthesis is the repair hierarchy together with the sharper local-to-global rule: **compact compatible fibers can remove globalization loss without removing the independent naturality gate**.

## Falsification criterion

Exhibit a system satisfying the AF-089 compact-fiber finite-compatibility hypotheses for which no global selection with the same Lipschitz constant exists, or show that those hypotheses alone force the equivariance/canonicity required by an arithmetic application. Alternatively, cross one of the stated regularity rigidity thresholds without inducing the corresponding split.

## Lean-formalizable core

- Linear section/complemented-kernel equivalence.
- Minimum-norm representative in strictly/uniformly convex spaces.
- Lipschitz-section implication to linear splitting in the separable case.
- Homogeneous-apex linearization rigidity.
- Compact-fiber finite-intersection globalization with preservation of the Lipschitz constant.
