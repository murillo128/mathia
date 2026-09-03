# MI-009 — Quotient repair is a category, compactness, range, regularity, and naturality problem

**Evidence level:** supported by AF-078--AF-090; exact in the stated Banach, compact-fiber, bidual, and finite-dimensional models

## Core intuition

The statement that information can be recovered after a quotient is incomplete until the admissible category, gluing topology, and target range are named. Linear, continuous metric, globally Lipschitz, homogeneous, equivariant, order-compatible, differentiable, and locally conical repairs have different boundaries. Independently, local repairs globalize only when compatible choices cannot escape across finite subsets, and even exact globalization may land naturally in a completion rather than the original source.

Thus **existence with optimal fidelity, range fidelity, and naturality are separate gates**. A repair can globalize with no metric loss in the canonical bidual while still failing to provide an original-space linear section or a canonical arithmetic representative.

## Strongest justified principle

AF-078 identifies the linear endpoint: a bounded linear repair exists exactly when the quotient splits, with noncanonical shear freedom unless extra structure selects one. AF-081 shows that uniformly convex geometry can choose a canonical continuous homogeneous minimum-norm representative even for an uncomplemented quotient, so nonlinear metric repair is a real escape.

AF-082 and AF-084 locate rigidity thresholds: for separable Banach quotients, a global Lipschitz section forces linear splitting; for positive-homogeneous sections, a bounded-linear tangent at the apex forces global linearity. AF-083 and AF-085--AF-087 refine the surviving middle category by bounded-scale and tangent-cone moduli.

AF-088--AF-089 add the compactness axis. Local finite-subset Lipschitz selections globalize with exactly the same constant when compatible fiber slices are compact and the metric constraints are closed. Reflexivity is only one way to obtain that compactness; weak-star compact dual fibers give the same exact globalization in nonreflexive settings.

AF-090 identifies what remains when the original source lacks such compact fibers. Any local `L`-Lipschitz right inverse globalizes canonically at the level of existence to an `L`-Lipschitz section `F -> E**`. More strongly, the induced Lipschitz retraction onto the kernel forces local complementation, so `q**:E**->F**` has a bounded linear right inverse. The nonlinear local escape therefore cannot avoid linear structure indefinitely: after bidualization the exact sequence splits. The unresolved boundary is whether the required representatives stay inside `J_E(E)` with the desired quantitative fidelity and source naturality. The Aharoni--Lindenstrauss nonseparable control shows that original-space linear splitting cannot be inferred in full generality.

## Evidence synthesis and boundaries

These results do not make quotient repair canonical. Compactness or bidualization proves existence of compatible representatives, but does not supply equivariance, uniqueness, provenance preservation, measurability in external parameters, or a preferred section. Those properties can be exactly the arithmetic content a proposed representation needs.

Conversely, failure of original-space linear splitting is no longer evidence that local Lipschitz repair is an unconstrained nonlinear phenomenon. AF-090 forces local linear splitting of the kernel and full linear splitting after bidualization. A claimed escape must therefore name the range/category in which it genuinely survives.

## Status / novelty

Banach-space splitting, local complementation, Lipschitz retracts, compactness principles, minimum-norm selections, and the Aharoni--Lindenstrauss/Godefroy--Kalton boundaries are classical. The synthesis is the repair hierarchy together with the sharper rule: **compact or bidual compatibility can remove globalization loss while leaving original-range and naturality fidelity as independent arithmetic gates**.

## Falsification criterion

Exhibit a local Lipschitz quotient section covered by AF-090 whose kernel is not locally complemented or whose bidual quotient does not split linearly; or show that bidual splitting alone forces an original-space, source-natural repair in the unrestricted nonseparable setting. Alternatively, cross one of the stated regularity rigidity thresholds without inducing the corresponding split.

## Lean-formalizable core

- Linear section/complemented-kernel equivalence.
- Minimum-norm representative in strictly/uniformly convex spaces.
- Lipschitz-section implication to linear splitting in the separable case.
- Homogeneous-apex linearization rigidity.
- Compact-fiber finite-intersection globalization with preservation of the Lipschitz constant.
- Local Lipschitz patch `=>` Lipschitz kernel retraction `=>` local complementation `=>` bidual linear splitting.
