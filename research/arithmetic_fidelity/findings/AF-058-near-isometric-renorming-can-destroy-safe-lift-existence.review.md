---
type: adversarial-review
target: research/arithmetic_fidelity/findings/AF-058-near-isometric-renorming-can-destroy-safe-lift-existence.md
---

# Adversarial review

## Adversary

The renorming counterexample proves a **fixed-base/fiberwise** loss of safe lifts, not loss of safe-envelope nonemptiness in the global sense suggested by the title, boxed conclusion (12), and the final statement that near-isometric changes can erase “exact safe-lift existence.” For every nonempty target `S` and every isometric embedding `C`, one always has

\[
C(S)\subseteq \mathcal E_C^D(S),
\]

because for every `s\in S` and every `x\in X`,

\[
D(Cx,Cs)=d(x,s)\ge d(x,S).
\]

Thus no admissible renorming that keeps `C` isometric can destroy **global** existence of safe points at all. Equation (11) establishes only that the particular fiber over the midpoint, `\{0\}\times\mathbb R`, intersects the safe envelope for `D_2` and has empty intersection for `D_q`. The later boundary note does acknowledge “above a fixed base point,” but the stronger unqualified formulation remains mathematically false if consumed as a statement about existence anywhere in the safe envelope.

This is material because the finding is presented as a structural obstruction to representation-invariant repair existence. The surviving theorem should be stated consistently as instability of **fiber-constrained/fixed-base safe-lift existence** (or else “safe-lift existence” must be explicitly defined to mean that constrained notion throughout). If global safe-envelope existence is intended, the present example cannot establish it and a different observable/counterexample is required.
