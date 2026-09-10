# MI-023 — Sparse root-rate observability is a phase-recurrence problem, not a density problem

**Evidence level:** exact finite-mode observability classifications through AF-247

## Core intuition

Sparse output sampling preserves a finite-exponential root-rate discriminator according to how the sampling set approaches the zero geometry of the relevant phase orbit, not according to its natural density. Arbitrarily long consecutive blocks are one sufficient mechanism, but they are far from the intrinsic condition.

For a fixed finite mode family, the right object is the orbit closure on its compact phase torus together with the zero set of the induced trigonometric polynomial. Root-rate fidelity fails only when the sampled orbit approaches that zero set at an exponentially significant rate.

## Strongest justified principle

AF-244 proves that zero-density sets with arbitrarily long consecutive blocks preserve the exact finite-exponential root-rate discriminator. AF-245 recasts positive-amplitude tail observability as a uniqueness problem on the tail Bohr limit set: Bohr-dense tails work, but density is not the invariant.

AF-246 sharpens the root-rate question itself. A Lojasiewicz inequality on the finite-dimensional phase-orbit closure reduces fidelity to a shrinking-target exponent: the sampled orbit may approach zeros, but not exponentially fast enough to alter the `n`th-root limit. Thus positive amplitude is unnecessary.

AF-247 then shows that algebraic finite modes are rigid enough for the Subspace Theorem/nondegenerate recurrence machinery to eliminate exponentially small nonzero values. In that subclass, universal finite-mode root observability is equivalent to periodic completeness of the sampling set. This reduction is not available for the actual zeta zero phases without an additional algebraicity theorem.

## Program consequence

Treat output sparsification as a representation-specific recurrence problem. For the zeta/Li finite-mode families, identify the relevant phase orbit closures and prove a uniform subexponential shrinking-target bound, or find a structural class in which the problem collapses to an explicit combinatorial sampling condition. Do not use density or local thickness as a proxy once the phase geometry is available.

Keep source cost separate: a sparse faithful output set does not make the retained Li coefficients cheaper to construct.

## Counterevidence / boundary

The exact criterion is for finite exponential families. Uniform control as the number of relevant modes grows is a separate problem, and the algebraic periodic-completeness collapse does not apply to general zeta phases. A sampling set can be excellent for one finite family and poor for another.

## Epistemic status

**Exact finite-mode classification of sparse root-rate fidelity by phase-orbit zero approach, with periodic completeness only in the algebraic subclass; no cheap-source consequence is implied.**

## Falsification criterion

Exhibit a finite family and sampling set for which the AF-246 shrinking-target exponent is zero but the restricted root rate changes, or prove that density/thickness alone determines the same fidelity for all finite phase systems contrary to the persisted classifications.