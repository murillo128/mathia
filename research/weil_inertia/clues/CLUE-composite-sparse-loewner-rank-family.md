---
id: CLUE-weil-inertia-composite-sparse-loewner-rank-family
type: research-clue
status: proposed
origin: independent-review
target_line: weil_inertia
based_on:
  - research/weil_inertia/findings/WI-087-close-prime-ramanujan-cross-grams-have-an-exact-loewner-bezout-rank-family.md
  - research/weil_inertia/formalization/WI081PairwiseRamanujanRank.lean
  - research/weil_inertia/findings/WI-097-sparse-loewner-nullity-is-exact-orbit-three-resonance.md
---

# Does the WI-087 sparse Loewner rank family extend to coprime composite moduli?

## Observation

WI-087 states its exact Loewner--Bezout rank family for primes and proves denominator regularity on primitive node sets by the prime-order fact that three unit complex numbers summing to zero would force nontrivial cube roots of unity.  The Lean formalization exposes a weaker local mechanism.  For

\[
P(X)=1+X^a+X^{a+g},\qquad Q(X)=1+X^g+X^{a+g},
\]

its generic helper `wi087_Q_ne_zero_of_primitive` only uses that a node `z` has exact order `m`, that `0<a<g`, that `0<g-a<m`, and that the relevant interpolation identity gives either `P(z)=z^aQ(z)` or `P(z)=z^{a+g}Q(z)`.  If `Q(z)=0`, then also `P(z)=0`; subtracting gives `z^a=z^g`, hence `z^(g-a)=1`, contradicting exact order `m`.  No primality or modulo-three hypothesis is used in this local regularity step.

The same formalization's evaluation/rank bridge only needs enough distinct primitive nodes to inject `Fin beta` into each node set.  Separately, WI-097 classifies the sparse coefficient matrix exactly: it is invertible whenever the reduced translation-orbit length `(g-a)/gcd(a,g-a)` is not divisible by three.

This suggests that the prime packaging in WI-087 may be stronger than necessary for the finite exact-rank theorem.  A concrete candidate is: let `m<n<2m` be coprime integers with

\[
m\equiv2\pmod3,\qquad n\equiv1\pmod3,
\]

and define

\[
a=\frac{2m-n}{3},\qquad g=\frac{2n-m}{3},\qquad
\beta=a+g=\frac{m+n}{3},\qquad
\delta=\frac{mn+m-n}{3}.
\]

Then `g-a=n-m`, the same polynomial identities become

\[
P-X^aQ=1-X^m,\qquad P-X^\beta Q=(1+X^a)(1-X^n),
\]

and `n-m \equiv 2 (mod 3)`, so the WI-097 coefficient-matrix criterion predicts nonsingularity.  If additionally

\[
\beta\le \min\{\varphi(m),\varphi(n)\},
\]

the primitive-node Vandermonde factors have enough rows for the same exact rank argument.

For example, `(m,n)=(125,169)` satisfies the displayed arithmetic conditions, with

\[
(a,g,\beta,\delta)=(27,71,98,7027),
\qquad
\varphi(125)=100,\quad \varphi(169)=156.
\]

The formal proof architecture therefore predicts an exact composite-modulus cross-Gram rank `98` at boundary defect `7027` if no prime-only bridge has been overlooked.

## Research question

Prove or refute the following finite composite extension: for coprime `m<n<2m` with `m % 3 = 2`, `n % 3 = 1` and `beta=(m+n)/3 <= min(phi(m),phi(n))`, every `N` satisfying

\[
\operatorname{boundaryDefect}(m,n,N)=\delta=\frac{mn+m-n}{3}
\]

obeys

\[
\operatorname{rank}(\operatorname{crossGram}(m,n,N))=\beta.
\]

More generally, determine the weakest exact-order, coefficient-matrix and primitive-node-count hypotheses under which the sparse three-term Loewner construction gives an exact Ramanujan cross-Gram rank formula, without assuming that either modulus is prime.

## Why it may matter

A positive result would show that the WI-087 defect mechanism is not intrinsically a close-prime phenomenon but a broader exact-period/cyclotomic rational-interpolation mechanism whose prime instance is only the cleanest arithmetic packaging.  It would also give explicit composite residual-rank test cases for the generic WI-086 transversality invariant and clarify whether the relevant scale is governed by modulus size or by the primitive dimensions `phi(m),phi(n)`.

This would not by itself evade the established scalar pairwise-rank stopping rules, but it could matter if later source-labelled or simultaneous multi-modulus constructions need exact structured composite overlaps rather than prime-only examples.

## Decisive test

1. Reconstruct the WI-087 Loewner factorization for general coprime `m,n` under the displayed exponent identities, checking `delta < lcm(m,n)/2` and the exact nearest-boundary phase transport.
2. Replace the prime-order denominator argument by the exact-order lemma exposed in Lean and use WI-097's coefficient-matrix criterion rather than prime congruence as the nonsingularity gate.
3. Prove that `beta <= phi(m),phi(n)` is sufficient for both primitive-node evaluation maps to have rank `beta`, and identify whether any additional condition is hidden in the current formal proof.
4. Verify the concrete case `(125,169,7027)` exactly, not numerically: the target rank is `98`.
5. Search the Ramanujan-subspace, cyclotomic Loewner and rational-interpolation literature for an existing composite-modulus formulation before making any novelty claim.

A failure of the exact `(125,169)` case, or discovery of a genuinely prime-only step after the generic denominator/evaluation lemmas, would kill the stated extension.  If the theorem holds, the next question is to classify which composite pairs satisfy the totient-size gate and whether any family gives a qualitatively different defect fraction from the prime case.

## Evidence boundary

The current Lean artifact proves only the prime WI-087 theorem.  Its generic helper lemmas expose weaker local hypotheses, and WI-097 supplies an exact algebraic nonsingularity classification, but no checked theorem currently assembles those pieces into a composite Ramanujan rank statement.  The `(125,169)` rank value above is a theorem target inferred from that proof architecture, not persisted computational or formal evidence.  No asymptotic composite family, density statement, many-modulus inertia consequence, Yang consequence, zeta consequence, or novelty claim is established here.
