# PC-009 — pairwise polygon-edge crossing counts collapse exactly to the GCD kernel

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE` + `BRANCH-CLOSED-AS-NOVELTY`

## Question

A natural out-of-the-box extension of the original prime-circle picture is to retain the **edges** of every regular polygon, not only its vertices, and ask whether crossings between polygon boundaries carry new arithmetic/spectral information.

Let `P_m` and `P_n` be the regular `m`- and `n`-gons inscribed in the same unit circle with the common vertex `1`, exactly as in the original construction. Let

\[
X(m,n)
\]

be the number of **transverse interior intersections** between their boundaries, excluding shared boundary vertices.

## Exact crossing formula

Assume without loss of generality that `m <= n`, and set

\[
g=\gcd(m,n).
\]

The two polygons have exactly `g` common vertices: the roots of unity whose order divides both `m` and `n`.

Consider a vertex `v` of `P_m` that is not a vertex of `P_n`. Because an `n`-arc has angular length `1/n <= 1/m`, `v` lies strictly between two consecutive `P_n` vertices, and those two vertices lie between the two neighboring `P_m` vertices around `v`. By the alternating-endpoint criterion for chords of a circle, the corresponding `P_n` side crosses **both** `P_m` sides incident at `v`.

Conversely, every transverse crossing arises this way: an `n`-side can cross the boundary of the coarser `m`-gon only by straddling a non-common `m`-vertex, and an `n`-arc contains at most one such `m`-vertex.

Hence every non-common vertex of the smaller polygon contributes exactly two crossings, while each common vertex contributes none:

\[
\boxed{
X(m,n)=2\bigl(\min(m,n)-\gcd(m,n)\bigr).
}
\]

For coprime levels this reduces to

\[
X(m,n)=2(\min(m,n)-1),
\]

and if one level divides the other then `X(m,n)=0`, as expected because the finer polygon refines the coarser polygon without transverse boundary crossings.

The standard no-shared-vertices fact that two concentric inscribed regular `m`- and `n`-gons (`m<n`) have `2m` boundary intersections is elementary and appears, for example, in olympiad/AMC solutions. The shared-vertex correction above is exactly the `2 gcd(m,n)` loss forced by the original common-vertex alignment.

## The normalized crossing kernel is an Archimedean-minus-multiplicative kernel

Normalize by the geometric mean of the numbers of sides:

\[
K_X(m,n):=
\frac{X(m,n)}{2\sqrt{mn}}.
\]

Then

\[
\boxed{
K_X(m,n)
=
\frac{\min(m,n)}{\sqrt{mn}}
-
\frac{\gcd(m,n)}{\sqrt{mn}}.
}
\]

The first term is exactly

\[
\frac{\min(m,n)}{\sqrt{mn}}
=
\exp\!\left(-\frac12|\log m-\log n|\right).
\]

For the second, introduce the standard multiplicative/lattice metric

\[
d_{\mathrm{mult}}(m,n)
:=
\log\frac{\operatorname{lcm}(m,n)}{\gcd(m,n)}
=
\sum_p |v_p(m)-v_p(n)|\log p.
\]

Since `lcm(m,n) gcd(m,n)=mn`, one has

\[
\frac{\gcd(m,n)}{\sqrt{mn}}
=
\exp\!\left(-\frac12 d_{\mathrm{mult}}(m,n)\right).
\]

Therefore the edge-crossing geometry gives the exact identity

\[
\boxed{
K_X(m,n)
=
 e^{-\frac12|\log(m/n)|}
-
 e^{-\frac12 d_{\mathrm{mult}}(m,n)}.
}
\]

This is a useful geometric interpretation: crossings measure the defect between the one-dimensional Archimedean projection `n -> log n` and the full `l^1` prime-valuation geometry. Indeed

\[
|\log(m/n)|
\le
\sum_p |v_p(m)-v_p(n)|\log p,
\]

with equality exactly when `m` and `n` are comparable by divisibility; precisely then the polygons do not cross.

Equivalently, with

\[
\Delta(m,n)=d_{\mathrm{mult}}(m,n)-|\log(m/n)|,
\]

one obtains

\[
\boxed{
\frac{X(m,n)}{2\min(m,n)}
=1-e^{-\Delta(m,n)/2}.
}
\]

So transverse edge crossings are an exact Euclidean visualization of the cancellation defect between positive and negative prime-valuation changes.

## Why this closes the pairwise crossing-count branch for RH novelty

The formula also gives immediately

\[
\gcd(m,n)
=
\min(m,n)-\frac12X(m,n).
\]

Thus the complete matrix of pairwise crossing **counts** contains no arithmetic information beyond the GCD matrix (plus the deterministic `min` kernel), and conversely it determines that GCD matrix exactly.

The normalized GCD kernel

\[
\frac{\gcd(m,n)}{\sqrt{mn}}
\]

is precisely the critical `alpha=1/2` GCD kernel studied extensively in the GCD-sum literature. Aistleitner--Berkes--Seip identify the general kernels

\[
\frac{\gcd(m,n)^{2\alpha}}{(mn)^\alpha}
\]

with Poisson integrals on an infinite-dimensional polydisc and study the associated GCD matrices, including the critical case `alpha=1/2`.

Therefore any proposed RH mechanism that uses only one scalar per pair of polygon levels derived from the **number of edge crossings**, or the corresponding level-level adjacency/count matrix, is only a repackaging of already-developed GCD-kernel mathematics.

This rules out as sources of novelty:

- raw pairwise boundary-crossing counts;
- normalized crossing densities;
- spectra/determinants of the level-level crossing-count matrix when no positional information about crossings is retained;
- interpreting the appearance of the half exponent in the normalized count as a new RH-critical `1/2` mechanism.

## What is not ruled out

This result does **not** close the full polygon-edge arrangement. The crossing **positions**, crossing angles, cyclic order, higher-order concurrency, and the planar graph obtained by retaining the individual intersections contain information discarded by `X(m,n)`. In particular, for coprime `m,n` the count is essentially trivial while the labeled crossing pattern still sees the residue permutation `k -> nk (mod m)`.

So if edge geometry contains genuinely new information, it must live beyond pairwise counts.

## Prior art / novelty check

- The elementary fact that two inscribed regular polygons with no shared vertices have `2 min(m,n)` crossings is standard; a recent accessible example is the solution of 2021 AMC 10B Fall Problem 21.
- The metric `log(lcm/gcd)` is a standard lattice-valuation metric on the divisibility lattice and equals the weighted `l^1` distance of prime-valuation vectors.
- C. Aistleitner, I. Berkes, K. Seip, *GCD sums from Poisson integrals and systems of dilated functions*, J. Eur. Math. Soc. 17 (2015), 1517–1546, studies the critical normalized GCD kernel and its spectrum/Poisson representation.

No novelty is claimed for those ingredients. The exact common-vertex crossing identity and its Archimedean-minus-multiplicative interpretation are recorded here mainly as a **negative research result**: a geometrically natural new branch collapses to already-known GCD data before reaching any new RH mechanism.
