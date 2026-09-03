# MI-009 — Lipschitz quotient repair is an exact operator-extension defect; range, regularity, and naturality remain separate gates

**Evidence level:** supported by AF-078--AF-093; exact in the Banach/Lipschitz-free category stated there

## Core intuition

The question “can information be repaired after a quotient?” is category-relative, but in the Lipschitz Banach setting the nonlinear-versus-linear gap is now much more precise than a hierarchy of examples. For an extension `0 -> K -> E -> F -> 0`, Lipschitz repair exists exactly when its extension class dies after pullback along the barycenter map of the Lipschitz-free space. The killed obstruction is concretely **operator data on the forgotten barycentric kernel modulo data that extend to the full pre-compression free space**.

Thus a category change helps exactly by making a previously nonextendable fiber datum extendable. It does not automatically provide quantitative stability, source naturality, equivariance, or a repair in a stricter category.

## Strongest justified principle

AF-078 identifies the linear endpoint: bounded linear repair is equivalent to splitting the quotient. AF-081 shows that nonlinear geometry can select canonical continuous homogeneous representatives even when linear splitting fails, while AF-082/AF-084 identify regularity thresholds that force linearity back.

AF-087--AF-090 clarify locality and range. A Lipschitz section on one nontrivial ball globalizes in the relevant category; bidual relaxation always yields strong linear structure, so “repair exists after completion” is weaker than original-range repair.

AF-091 closes a large part of that apparent escape. If the forgotten kernel `K` is an ultrasummand, any local Lipschitz quotient repair already forces the original exact sequence to split linearly. Hence a genuinely Lipschitz-but-not-linear example must simultaneously evade target-side separable linearization and kernel-side bidual descent.

AF-092 gives the exact homological classifier. If `xi in Ext(F,K)` is the extension class and `beta_F : F(F) -> F` is the Lipschitz-free barycenter map, then

`Lipschitz repair <=> beta_F^*(xi)=0`,

while linear repair is `xi=0`. The nonlinear defect is therefore `ker beta_F^*`, with the optimal Lipschitz constant equal to the optimal norm of the corresponding linear lift on the free space.

AF-093 resolves that kernel into concrete fiber data. Writing `Z_F=ker beta_F`,

`ker beta_F^* ~= L(Z_F,K) / {restrictions of bounded operators F(F)->K}`.

A nonzero nonlinear-repair class is exactly a bounded operator on the forgotten barycentric fiber that does not extend linearly across the full free space. Target lifting property and ultrasummand coefficients are two independent mechanisms forcing every such operator to extend.

## Evidence synthesis and boundaries

This classification is algebraic/category-exact, not yet a quantitative stability theorem. The quotient of operator spaces need not have a closed range or canonical norm measuring distance to extendability. Nor does the free-space section automatically respect arithmetic provenance, group actions, positivity, locality, or a stricter admissible recovery class.

Discriminator-specific recovery can also require much less than a full quotient section. The exact extension model applies when complete representative recovery is the claimed task.

## Status / novelty

Lipschitz-free spaces, barycenter maps, Banach `Ext`, pushouts, operator extension, and ultrasummand theory are classical. The persisted synthesis is the fidelity interpretation: **nonlinear repair forgets precisely a class of nonextendable operators on the compression fiber**.

## Falsification criterion

Produce a Lipschitz-splittable extension whose class is not killed by `beta_F^*`, or a nonzero class in `ker beta_F^*` whose corresponding barycentric-kernel operator nevertheless extends. For an arithmetic application, a positive must additionally derive the required range, stability, and naturality from the source.

## Lean-formalizable core

- Lipschitz section/free-space linearization equivalence.
- Pullback splitting criterion `beta_F^*(xi)=0`.
- Long-homology identification of the kernel with an operator-extension quotient.
- Ultrasummand and target-lifting injectivity gates.
