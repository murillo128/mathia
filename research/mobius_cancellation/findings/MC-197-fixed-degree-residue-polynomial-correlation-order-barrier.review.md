---
type: adversarial-review
target: research/mobius_cancellation/findings/MC-197-fixed-degree-residue-polynomial-correlation-order-barrier.md
---

# Adversarial review

## Adversary

The centered extension of the top-interaction argument is not established as written, and its universal formulation is false. In (7), `S/phi` and `Q/phi` are not source-independent constants: they are linear functions of all residue-class aggregates. Therefore centering is not an ordinary translation by fixed constants, and it can change or even cancel the highest homogeneous part after summing over classes.

There is an explicit counterexample to the stated claim for a general modulus. Take `phi=2` and `P(U,V)=U^3`. Then the centered variables satisfy `u_2=-u_1`, so

`sum_a P(u_a,v_a)=u_1^3+u_2^3=0`

identically, despite `P` having effective degree three. Thus the sentence that `sum_a P(u_a,v_a)` has the same nonzero top interaction order `d` for every effective-degree-`d>=2` polynomial is false, and the subsequent centered dichotomy does not follow from the supplied proof.

The active primorial regime may admit a repair rather than a collapse of the main route. For a pure degree-`d` monomial, the coefficient of the same-class top-order contribution after summing the centered classes is multiplied by

`lambda_(phi,d)=((phi-1)^d+(phi-1)(-1)^d)/phi^d`,

which is nonzero for `phi>2`; this suggests that the intended large-primorial statement can likely be proved by an explicit centering expansion. But that argument must also distinguish the surviving same-residue top interaction from the cross-residue interactions introduced by `S` and `Q`.

Please either prove the centered theorem under the actual primorial hypotheses with the correct `phi` restriction and explicit top-order expansion, or narrow/remove the universal centered claim. The uncentered collision-partition triangularity and the generic primorial restriction estimate appear unaffected by this objection.