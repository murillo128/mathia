---
id: CLUE-weil-inertia-loewner-rational-interpolation-pairwise-rank-defect
type: research-clue
status: proposed
origin: independent-review
target_line: weil_inertia
based_on:
  - research/weil_inertia/findings/WI-081-pairwise-lcm-boundary-rank-controls-finite-window-ramanujan-leakage.md
  - research/weil_inertia/findings/WI-086-pairwise-ramanujan-rank-defect-starts-past-both-totient-dimensions.md
  - research/weil_inertia/formalization/WI081PairwiseRamanujanRank.lean
---

# Are residual pairwise Ramanujan rank defects exactly low-degree rational-interpolation defects of a cyclotomic Loewner matrix?

## Observation

The completed WI-086 formalization makes the short-boundary cross Gram explicit through the same primitive-root Vandermonde factors used in WI-081. Reconstructing its matrix entries for primitive roots `z` of order `m` and `w` of order `n` gives

\[
G_{z,w}=\sum_{x=0}^{\delta-1}(z^{-1}w)^x
=z^{1-\delta}\frac{z^\delta-w^\delta}{z-w}.
\]

The row factor `z^(1-delta)` is invertible, so the rank question is equivalent to that of the divided-difference matrix

\[
L_{z,w}=\frac{f(z)-f(w)}{z-w},\qquad f(X)=X^\delta,
\]

with the left nodes the primitive `m`-th roots and the right nodes the primitive `n`-th roots. This has the form of a Loewner matrix. WI-086 instead records the residual defect as an excess subspace-intersection dimension `tau` and notes that cyclotomic divisibility alone is only a reparameterization of orthogonality.

The known residual witness `(p,q,delta)=(11,13,47)` suggests a more structured explanation. On primitive 11th roots `z`, `z^47=z^3`; on primitive 13th roots `w`, `w^47=w^8`. The rational function

\[
R(X)=\frac{1+X^3+X^8}{1+X^5+X^8}
\]

formally satisfies `R(z)=z^3` when `z^11=1` and `R(w)=w^8` when `w^13=1`, because

\[
z^3(1+z^5+z^8)=1+z^3+z^8,
\qquad
w^8(1+w^5+w^8)=1+w^3+w^8.
\]

If the relevant Loewner rank/minimal-rational-degree correspondence applies faithfully to these two cyclotomic node sets, this would explain the observed rank `8` by a degree-8 rational interpolant rather than treating `tau=2` only as an exceptional abstract intersection.

There is also a candidate parametric family. For primes `p<q` with

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

These identities suggest the interpolant

\[
R_{p,q}(X)=
\frac{1+X^\alpha+X^\beta}
     {1+X^{\beta-\alpha}+X^\beta},
\]

which would agree with `X^delta` on both primitive root sets. The `(11,13,47)` witness is the first instance.

## Research question

Can the residual regime

\[
\delta>\max\{\varphi(m),\varphi(n)\}
\]

be recast exactly as a rational-interpolation problem in which

\[
\operatorname{rank}G_{m,n}^{(N)}
\]

is controlled, or under suitable hypotheses equals, the minimum McMillan/rational degree needed to interpolate `X^delta` simultaneously on the primitive `m`-th and `n`-th roots?

In particular, does the candidate prime family above satisfy the exact formula

\[
\operatorname{rank}G_{p,q}^{(\delta)}=\beta=\frac{p+q}{3},
\]

and hence

\[
\tau_{p,q}(\delta)
=(p-1)-\frac{p+q}{3}
=\frac{2p-q-3}{3}?
\]

More broadly, can low-rank residual defects be classified through low-degree rational congruences for `X^delta` modulo cyclotomic polynomials, rather than through unconstrained subspace intersections?

## Why it may matter

WI-086 proves that generic pairwise rank improvement is impossible until both primitive-frequency dimensions have saturated, and its cyclotomic-divisibility normal form alone adds no information. A genuine Loewner/rational-interpolation characterization would add a second constraint: not merely vanishing modulo one cyclotomic polynomial, but simultaneous low-degree rational realizability across both primitive-root sets.

If correct, the `(11,13,47)` defect would cease to be an isolated rank certificate and become the first member of an explicit arithmetic family with growing nonzero `tau`. That could expose the mechanism behind exceptional close-prime defects and supply algebraic tools such as rational interpolation, Bezoutians, resultants, or Euclidean-algorithm degree bounds for the residual regime.

This would still be only a pairwise structural mechanism; it would not by itself evade the scalar aliasing/overcompleteness obstructions of WI-082--WI-085 or improve the current zeta zero-proportion bound.

## Decisive test

1. Prove the exact diagonal equivalence between the WI-081/WI-086 short-boundary cross Gram and the Loewner divided-difference matrix for `f(X)=X^delta`, including the complementary-boundary phase convention.
2. State and verify the precise finite-node theorem relating the rank of this rectangular Loewner matrix to minimal rational interpolation degree, including possible poles on the node sets, numerator/denominator common factors, and rectangular-size saturation.
3. For `(11,13,47)`, prove that `(1+X^3+X^8)/(1+X^5+X^8)` is node-regular, reduced, and has minimal degree exactly `8`, then recover the existing rank-8 certificate without using its integer minor.
4. Test the parametric family. Prove that the numerator and denominator of `R_{p,q}` are coprime and nonzero on the primitive `p`- and `q`-th root sets, and determine whether the minimal rational degree is exactly `beta` rather than merely at most `beta`.
5. Check examples such as `(17,19)`, `(23,31)`, and `(29,31)` by exact arithmetic before generalizing. A single mismatch between the predicted rank `(p+q)/3` and the exact cross-Gram rank refutes the family as stated.
6. If the family survives, perform a serious prior-art audit of Loewner matrices on roots of unity, rational interpolation modulo cyclotomic polynomials, Bezoutians, and structured partial Fourier rank before making any novelty claim.

The direction should be rejected if Loewner rank here is merely another tautological encoding of `tau` with no arithmetic restriction beyond WI-086, or if minimal rational degree does not control the rectangular cross-Gram rank in the required way.

## Evidence boundary

Only the WI-086 max-totient rank threshold is Lean-checked. The Loewner rewrite, the application of rational-interpolation rank theory, the degree-8 explanation of `(11,13,47)`, the parametric prime family, its coprimality/minimality assertions, and the proposed formula for `tau` have not been formalized or accepted as findings.

The displayed rational identities are a source-motivated candidate explanation exposed by comparing the formal proof representation with WI-086's residual `tau` formulation. They require independent exact derivation, computational falsification, and prior-art review by the owning Research Watch. No novelty, zeta consequence, or global signed-inertia improvement is claimed.