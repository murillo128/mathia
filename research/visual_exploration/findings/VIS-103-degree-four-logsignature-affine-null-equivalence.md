# VIS-103 — fixed lower signature levels make degree-four log-signature an affine copy of degree-four signature

## Claim

For any family of bounded-variation paths whose signature levels `S^1`, `S^2`, and `S^3` are fixed, the homogeneous degree-four log-signature carries exactly the same pairwise degree-four information as the homogeneous degree-four signature.

Write

`S(X)=1+s_1+s_2+s_3+s_4+...`

and

`L(X)=log S(X)=ell_1+ell_2+ell_3+ell_4+...`

in the tensor algebra, with `s_k=S^k(X)`. Then

`ell_4`
` = s_4`
`   - (1/2)(s_1 s_3 + s_2 s_2 + s_3 s_1)`
`   + (1/3)(s_1 s_1 s_2 + s_1 s_2 s_1 + s_2 s_1 s_1)`
`   - (1/4)s_1 s_1 s_1 s_1`.

Consequently, if paths `X` and `Y` have the same first three signature levels, then

`ell_4(X)-ell_4(Y)=s_4(X)-s_4(Y)`.

For the exact quantized order-three Markov-type null of `VIS-099` and `VIS-100`, the initial three-symbol context and complete quantized length-four-block table fix the oriented edge inventory of the ordinary three-delay path. By the local-edge boundary proved in `VIS-096`, every admissible assembly therefore has the same signature through degree three. Hence the entire degree-four log-signature tensor is a fixed translation of the degree-four signature tensor throughout each exact type class.

In particular, replacing a fixed tensor-linear statistic `lambda(s_4)` by the **same linear functional** applied to `ell_4` cannot change any centered exact-null test: the null distribution and observed value are translated by the same constant, so deviations from the null mean and exact two-sided tail probabilities are identical.

**Evidence/status:** `EXACT-DERIVED + INFORMATION-BOUNDARY + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This does not say that every degree-four Lie/log-signature statistic is equivalent to the already tested coordinate `S^4_(1,2,1,3)`. Choosing a genuinely different Lie-basis coordinate or linear projection changes the linear functional on the degree-four tensor and may still define a new test. The result rules out only a representation-only rescue in which one keeps the same degree-four functional and merely replaces signature by log-signature.

## 1. Homogeneous degree four of the tensor logarithm

Let

`u=s_1+s_2+s_3+s_4+...`.

By definition in the completed tensor algebra,

`log(1+u)=u-u^2/2+u^3/3-u^4/4+...`.

Collecting only homogeneous degree four gives four contributions.

From `u` one gets `s_4`. From `-u^2/2` one gets

`-(1/2)(s_1 s_3+s_2 s_2+s_3 s_1)`.

From `u^3/3` one gets

`(1/3)(s_1 s_1 s_2+s_1 s_2 s_1+s_2 s_1 s_1)`.

From `-u^4/4` one gets

`-(1/4)s_1^4`.

There are no other degree-four terms. Thus `ell_4-s_4` is a universal noncommutative polynomial in `s_1,s_2,s_3` alone.

Therefore, on any set of paths on which `s_1,s_2,s_3` are fixed, the correction term is fixed. The full tensor difference identity

`ell_4(X)-ell_4(Y)=s_4(X)-s_4(Y)`

follows immediately.

## 2. Application to the exact quantized local-block null

`VIS-099` conditions a finite-alphabet scalar word on its initial three-symbol context and complete length-four-block count table. Under the standard three-delay embedding, each length-four block is exactly one oriented edge between consecutive three-symbol delay states. Thus every admissible word in the type class has the same oriented edge multiset.

The transition-count balance together with the fixed initial context also fixes the terminal context for every admissible Euler trail. The hypotheses used by `VIS-096` are therefore common to the whole type class: fixed endpoints and fixed unordered oriented edge inventory.

`VIS-096` proves that these data determine the ordinary delay-path signature through level three. Hence there exist fixed tensors `c_1,c_2,c_3` such that every admissible word has

`s_1=c_1`, `s_2=c_2`, `s_3=c_3`.

The degree-four logarithmic correction is therefore one fixed tensor `C(c_1,c_2,c_3)`, and

`ell_4=s_4+C`

throughout the exact conditional null.

This conclusion is exact and independent of the number of admissible words, the particular finite alphabet, the symbol embedding, or whether the type class is enumerated exhaustively or sampled by completion counts. It uses only the fixed lower-level signature boundary.

## 3. Consequence for exact conditional tests

Let `lambda` be any fixed linear functional on the fourth tensor power, and define

`T_sig=lambda(s_4)`,

`T_log=lambda(ell_4)`.

On one exact type class,

`T_log=T_sig+lambda(C)`.

Therefore

`T_log-E[T_log]=T_sig-E[T_sig]`

pointwise on the finite null space. The complete centered distributions coincide exactly. Any exact decision rule based only on the centered scalar displacement — including the two-sided rule used in `VIS-101` and `VIS-102` — returns the same tail probability.

For the already closed coordinate `lambda(t)=t_(1,2,1,3)`, computing its tensor-log counterpart with the same coordinate cannot rescue either negative result. It is mathematically the same conditional test up to a deterministic shift.

The same observation applies to any statistic that depends only on pairwise differences or centered linear coordinates of degree four. A nonlinear statistic can of course change under translation unless made translation-invariant, and a different linear functional can expose a different direction in the degree-four quotient. Those are genuinely different hypotheses rather than a change of representation alone.

## 4. Relation to the level-four chronology mechanism

`VIS-097` identified the first exact chronology escape by swapping two closed three-delay cycles with nonparallel area tensors. The fourth-level signature difference is the area-area commutator

`S^2(A) tensor S^2(B)-S^2(B) tensor S^2(A)`.

For that pair the first three signature levels agree, so the present identity shows that the degree-four **log-signature difference is exactly the same tensor difference**. This is consistent with the classical Baker-Campbell-Hausdorff view: for closed pieces whose first nonzero terms are degree two, the first order-sensitive Lie interaction appears at total degree four.

The practical distinction is therefore not `signature` versus `log-signature`. The substantive choice is **which degree-four direction is tested**. A Lie-basis projection may be preferable because it removes shuffle redundancy and exposes a canonical free-Lie coordinate, but its usefulness must come from selecting a different degree-four functional, not from the logarithm itself.

## 5. Prior art and novelty assessment

The tensor logarithm, free-Lie interpretation of log-signatures, and Baker-Campbell-Hausdorff algebra are classical. Christophe Reutenauer, *Free Lie Algebras*, Oxford University Press (1993), Chapter 3, treats logarithms, exponentials, canonical projections to the free Lie algebra, and the Campbell-Baker-Hausdorff series. Ben Hambly and Terry Lyons, **Uniqueness for the signature of a path of bounded variation and the reduced path group**, *Annals of Mathematics* 171:1 (2010), 109–167, DOI `10.4007/annals.2010.171.109`, is the existing Mathia anchor for the standard path-signature framework.

A targeted literature check confirms that interpreting the logarithm of a group-like signature as a Lie series is standard. No novelty is claimed for the homogeneous logarithm formula, the affine relation under fixed lower levels, or the BCH interpretation.

The Mathia-specific value is the exact specialization to the `VIS-099`/`VIS-100` conditional type class: it closes a tempting next experiment by proving before computation that a same-coordinate signature-to-log-signature substitution cannot change the exact conditional result.

## Boundary and falsification

This finding does not establish that:

- the full degree-four signature is determined by the order-three Markov type;
- all degree-four coordinates have the same conditional distribution;
- a different degree-four Lie-basis coordinate or projection is null;
- a nonlinear degree-four statistic is equivalent after the affine translation;
- higher signature/log-signature degrees contain no additional chronology;
- any degree-four statistic is zeta-specific or relevant to RH.

The claim is falsified by exhibiting two paths with equal signature levels one through three for which the displayed degree-four tensor-log difference identity fails, or by showing that the exact quantized type class from `VIS-099` does not fix the first three delay-path signature levels as required by `VIS-096`.

## Visual consequence

No canonical PNG is retained. The useful object is an information diagram rather than a new picture: the exact local-block null fixes degrees one through three, and at degree four the logarithm only subtracts a tensor determined by those already-fixed lower levels. A rendering would not add mathematical information to the exact algebraic boundary.

## Research consequence

The accepted `CLUE-zeta-critical-strip-multiscale-geometry` should not treat “use log-signature instead of signature” as a materially new chronology test by itself.

A next source test must freeze a **genuinely different degree-four functional** — for example an independently justified Lie-basis coordinate or low-dimensional Lie projection motivated by the area-area commutator structure — and evaluate it on fresh confirmation material. The exact Markov-type null remains valid, but the new information claim must come from a new direction inside the degree-four quotient, not from changing coordinates from `S` to `log S` while keeping the same functional.