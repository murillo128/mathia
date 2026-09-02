---
id: CLUE-weil-inertia-sparse-loewner-kernel-orbit-classification
type: research-clue
status: proposed
origin: independent-review
target_line: weil_inertia
based_on:
  - research/weil_inertia/findings/WI-087-close-prime-ramanujan-cross-grams-have-an-exact-loewner-bezout-rank-family.md
  - research/weil_inertia/formalization/WI081PairwiseRamanujanRank.lean
---

# Is the sparse WI-087 Loewner kernel classified exactly by translation-orbit length?

## Observation

WI-087 proves nonsingularity through coprimality and the classical Bezoutian/resultant criterion.
The Lean formalization instead makes the coefficient matrix explicit.  For `0 < a < g`, it uses
the `(a+g) x (a+g)` matrix `B(a,g)` representing

\[
\frac{P(X)Q(Y)-Q(X)P(Y)}{X-Y},\qquad
P=1+X^a+X^{a+g},\quad Q=1+X^g+X^{a+g}.
\]

After reversing a kernel vector, the checked proof reduces its coordinates modulo `d=g-a` and
exposes the cyclic recurrence

\[
f(r+a)+f(r)+f(r-a)=0\qquad(r\in\mathbf Z/d\mathbf Z).
\]

The published prime family needs only the sufficient condition `d % 3 != 0`.  The recurrence
separates into translation-by-`a` orbits, suggesting a sharper exact boundary.

## Research question

Let

\[
d=g-a,\qquad h=\gcd(a,d),\qquad L=d/h.
\]

Is the exact complex nullity

\[
\dim_{\mathbf C}\ker B(a,g)=
\begin{cases}
2h,&3\mid L,\\
0,&3\nmid L?
\end{cases}
\]

Equivalently, is `B(a,g)` invertible exactly when the translation orbits of `a` in
`ZMod (g-a)` do not have length divisible by three?

## Why it may matter

This would replace the sufficient modulo-three condition used by the formalization with the exact
algebraic singularity locus of the whole three-term interpolant family.  Singular cases could
identify additional structured Loewner rank-defect families, while invertible cases with
`3 | (g-a)` would show that the raw difference modulo three is not the governing invariant.  This
remains pairwise structure and would not by itself evade the established scalar-inertia barriers.

## Decisive test

Prove that the kernel of `B(a,g)` is equivalent, not merely mapped injectively, to the solution
space of the cyclic recurrence.  Decompose `ZMod d` into its `h` translation orbits of length `L`
and compute the periodic solution dimension of the characteristic equation
`T^2 + T + 1 = 0`.  This should give two dimensions per orbit exactly when `3 | L`; any exact
counterexample to the displayed nullity formula kills the conjecture.  Only after that algebraic
classification should singular cases be tested for the denominator-regularity and Vandermonde
hypotheses needed to produce new Ramanujan cross-Gram rank formulas.

## Evidence boundary

Lean proves only the WI-087 family and only the vanishing implication needed when
`(g-a) % 3 != 0`.  It does not prove the proposed kernel equivalence, the nullity formula, or any
new cross-Gram family arising from singular matrices.  No novelty, asymptotic consequence,
many-modulus inertia consequence, or zeta consequence is established.
