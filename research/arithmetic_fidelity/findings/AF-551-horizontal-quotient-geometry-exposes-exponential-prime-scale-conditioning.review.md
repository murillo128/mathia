---
type: adversarial-review
target: research/arithmetic_fidelity/findings/AF-551-horizontal-quotient-geometry-exposes-exponential-prime-scale-conditioning.md
---

# Adversarial review

## Adversary

**Target.** The general claim immediately following (2), and its proof in (14)–(16), that `d_ref` is a metric on the common-postcomposition quotient for labelled families of same-orientation diffeomorphisms `I` onto unspecified target intervals. Those hypotheses do not require the different branches within one family to have the same range.

**Counterexample.** Take `I=[0,1]`, `m=2`, and increasing smooth diffeomorphisms onto their respective target intervals
\[
f_1(s)=g_1(s)=s,\qquad f_2(s)=s/2,\qquad g_2(s)=s/3.
\]
The relative transitions are `H_2^F(s)=s/2` and `H_2^G(s)=s/3`. In the direction specified by (2),
\[
(H_2^F)^{-1}\circ H_2^G(s)=2s/3
\]
is defined on all of `I`, yielding `d_ref([F],[G])=1/3`. In the opposite direction,
\[
(H_2^G)^{-1}\circ H_2^F(s)=3s/2
\]
is only defined for `0\le s\le 2/3`, because `H_2^G(I)=[0,1/3]`. Thus `d_ref([G],[F])` is not defined on all of `I`. More generally, (1) itself need not be globally defined if a branch's target interval extends outside its reference branch's range.

**Why material.** Formula (14) requires a homeomorphism of `I` onto `I`; the warps in (2) are not necessarily such homeomorphisms under the stated assumptions. Therefore (14)–(16) cannot establish a metric on the declared class, and the unconditional metric assertion is false as stated.

**Resolution.** Require all branches of each individual family to be diffeomorphisms *onto the same interval* (`f_i:I\to J_F` for all `i`, `g_i:I\to J_G` for all `i`), as in AF-550. Then every `H_i^F,H_i^G` is a bijective self-map of `I`, their comparison warp is a homeomorphism `I\to I`, and the proposed metric proof can apply. An alternative is an explicitly restricted class with matching full transition ranges, with domains specified. The Dirichlet-tail specialization already has the common-range property, so this objection concerns the theorem's advertised generality rather than independently refuting the tail asymptotics (9)–(13).
