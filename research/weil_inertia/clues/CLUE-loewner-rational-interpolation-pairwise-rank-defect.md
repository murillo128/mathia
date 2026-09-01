---
id: CLUE-weil-inertia-loewner-rational-interpolation-pairwise-rank-defect
type: research-clue
status: resolved
origin: independent-review
target_line: weil_inertia
based_on:
  - research/weil_inertia/findings/WI-081-pairwise-lcm-boundary-rank-controls-finite-window-ramanujan-leakage.md
  - research/weil_inertia/findings/WI-086-pairwise-ramanujan-rank-defect-starts-past-both-totient-dimensions.md
  - research/weil_inertia/formalization/WI081PairwiseRamanujanRank.lean
---

# Are residual pairwise Ramanujan rank defects exactly low-degree rational-interpolation defects of a cyclotomic Loewner matrix?

## Observation

The completed WI-086 representation makes the short-boundary cross Gram explicit through primitive-root Vandermonde factors. For primitive roots `z` of order `m` and `w` of order `n`,

\[
G_{z,w}=\sum_{x=0}^{\delta-1}(z^{-1}w)^x
=z^{1-\delta}\frac{z^\delta-w^\delta}{z-w}.
\]

The row factor is invertible, so the rank question is equivalent to the divided-difference matrix

\[
L_{z,w}=\frac{f(z)-f(w)}{z-w},\qquad f(X)=X^\delta,
\]

which is a Loewner matrix. WI-086 instead records the residual defect as an excess subspace-intersection dimension `tau` and notes that cyclotomic divisibility alone is only a reparameterization of orthogonality.

The known residual witness `(p,q,delta)=(11,13,47)` suggested a more structured explanation. On primitive 11th roots `z`, `z^47=z^3`; on primitive 13th roots `w`, `w^47=w^8`. The rational function

\[
R(X)=\frac{1+X^3+X^8}{1+X^5+X^8}
\]

agrees with those two restrictions and has degree `8`, matching the exact cross-Gram rank from WI-081.

More generally, for primes `p<q` with

\[
p\equiv2\pmod3,\qquad q\equiv1\pmod3,\qquad q<2p,
\]

set

\[
\alpha=\frac{2p-q}{3},\qquad
\beta=\frac{p+q}{3},\qquad
\delta=\frac{pq+p-q}{3}.
\]

Then `delta ≡ alpha (mod p)` and `delta ≡ beta (mod q)`, while

\[
\alpha+\beta=p,\qquad 2\beta-\alpha=q.
\]

The candidate interpolant was

\[
R_{p,q}(X)=
\frac{1+X^\alpha+X^\beta}
     {1+X^{\beta-\alpha}+X^\beta}.
\]

## Research question

Can the residual regime

\[
\delta>\max\{\varphi(m),\varphi(n)\}
\]

be recast as a rational-interpolation problem in which the pairwise cross-Gram rank is controlled by a low-degree rational congruence for `X^delta` on the two primitive-root node sets? In particular, does the prime family above satisfy

\[
\operatorname{rank}G_{p,q}^{(\delta)}=\beta=\frac{p+q}{3},
\]

and therefore

\[
\tau_{p,q}(\delta)
=(p-1)-\frac{p+q}{3}
=\frac{2p-q-3}{3}?
\]

## Why it may matter

WI-086 proves that generic pairwise rank improvement is impossible until both primitive-frequency dimensions have saturated, and its cyclotomic-divisibility normal form alone adds no information. A genuine Loewner/rational-interpolation characterization would add simultaneous structure across both cyclotomic node sets and could explain exceptional close-prime defects arithmetically rather than as unconstrained subspace intersections.

This remains pairwise structure only. Even a successful classification would not by itself evade the scalar aliasing/overcompleteness obstructions of WI-082--WI-085 or improve the current zeta zero-proportion bound.

## Decisive test

The intended decisive test was to:

1. prove the exact diagonal equivalence with the Loewner divided-difference matrix;
2. avoid an unjustified generic slogan equating Loewner rank with minimal rational degree, and instead establish the required rank through a theorem whose hypotheses are checked;
3. prove node-regularity, reducedness, and exact degree for the `(11,13,47)` interpolant;
4. test and then prove or refute the parametric prime formula;
5. check exact examples such as `(17,19)`, `(23,31)`, and `(29,31)`;
6. audit Loewner rational interpolation, Bezoutians/resultants, divided differences at roots of unity, and Ramanujan-subspace prior art before any novelty assessment.

## Evidence boundary

Before resolution, only the WI-086 max-totient threshold was established. The Loewner rewrite, rational explanation of `(11,13,47)`, parametric family, coprimality/minimality mechanism, and formula for `tau` were unvalidated. General scalar rational-interpolation theory also has multiple rank/degree cases, so the candidate could not be accepted merely by identifying a Loewner matrix.

## Research disposition

Outcome: supported

Resolved by:
- [[research/weil_inertia/findings/WI-087-close-prime-ramanujan-cross-grams-have-an-exact-loewner-bezout-rank-family]]

WI-087 proves the candidate prime-family rank formula by an explicit reduced three-term rational interpolant and a nonsingular Bezoutian/Vandermonde factorization, rather than by an unchecked generic interpolation-rank slogan. It also strengthens the conclusion: the prime number theorem in arithmetic progressions supplies close prime pairs with `q/p -> 1`, along which the residual defect satisfies `tau/(p-1) -> 1/3`. Thus the rational-interpolation mechanism is real, but its program-level effect is partly negative: residual pairwise transversality defect can be macroscopic, so a universal `tau=o(phi(p))` escape is closed.
