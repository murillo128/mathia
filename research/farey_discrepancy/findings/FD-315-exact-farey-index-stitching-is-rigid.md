# FD-315 — Exact Farey index stitching is rigid

**Status:** `CLASSICAL-BCZ + EXACT-DERIVED + NEGATIVE/CONTROL-DESIGN + STITCHING-RIGIDITY`.

`FD-314` identifies triple/index integrability as the first compatibility lost when genuine Farey denominator edges are reassembled as local labels. The most literal repair is already rigid. Once every successor pair stays in the Farey triangle and every stitched triple has an integer Farey index, the next denominator is forced by the classical Farey/BCZ recurrence. Starting from the canonical boundary pair `(1,Q)`, there is no nontrivial matched path left to sample.

The mathematical ingredients are classical; the durable result here is the control-design consequence. Exact stitchwise index compatibility is not an intermediate null between the weak edge inventory and the fully identified Farey sequence.

## 1. Exact local stitch lemma

Fix an order `Q>=1` and positive integers `a,b,c<=Q`. Assume

- the successor pair is Farey-triangle admissible: `b+c>Q`;
- the stitched index `k=(a+c)/b` is a positive integer.

Then `c=kb-a`. The denominator bound `c<=Q` gives

`k <= (Q+a)/b`,

hence `k<=floor((Q+a)/b)`.

On the other hand, `b+c>Q` gives

`(k+1)b-a>Q`,

so `k+1>(Q+a)/b`. Since `k` is an integer,

`k>=floor((Q+a)/b)`.

Therefore both inequalities are equalities:

`k=floor((Q+a)/b)`

and

`c=floor((Q+a)/b)b-a`.

No coprimality or numerator information was used. The Farey-triangle inequality, the denominator cap, and integer index already determine the successor denominator.

## 2. Global reconstruction from the boundary pair

Let `q_0,q_1,...` be positive integers at most `Q` with canonical initial pair

`(q_0,q_1)=(1,Q)`.

Suppose every successor pair satisfies `q_i+q_(i+1)>Q` and every interior stitch has positive integer index

`nu_i=(q_(i-1)+q_(i+1))/q_i`.

Applying the lemma at each step gives

`q_(i+1)=floor((Q+q_(i-1))/q_i)q_i-q_(i-1)`.

This is exactly the classical next-term denominator recurrence for `F_Q`. Induction therefore forces the canonical Farey denominator word, up to its first terminal denominator `1`. With the usual fixed endpoints, the entire path is `F_Q)'s denominator path.

In particular, a matched control cannot remain nontrivial by preserving exact local Farey-triangle admissibility and then adding exact integer index at every stitch. The complete directed edge inventory is not even needed for this rigidity: the local admissibility plus stitch condition already forces the orbit once the boundary pair is fixed.

## 3. The FD-314 certificate fails at exactly this boundary

For `Q=8`, `FD-314` reassembles the genuine denominator-edge inventory into a path beginning

`(1,8,3,...)`.

Its first stitched index is `(1+3)/8=1/2`, so it fails the integer condition immediately. The lemma shows that an admissible integer-index repair at the same first two labels has no freedom:

`q_2=floor((8+1)/8)8-1=7`.

The same deterministic update then propagates through the whole word. Thus “repair the excursion permutation by enforcing exact triple/index compatibility” does not produce a stronger but still sampleable null; it collapses back to the canonical Farey orbit.

## 4. Prior art and novelty boundary

The integer-valued Farey index is classical and already anchored in `SOURCES.md` through Hall--Shiu. The next-term recurrence and its normalized Farey-triangle/BCZ dynamics are also classical; the existing Augustin--Boca--Cobeli--Zaharescu source in `SOURCES.md` is part of that prior-art boundary. No novelty is claimed for those identities or for the BCZ map.

The Mathia-specific conclusion is the matched-control boundary: `FD-314` showed that exact directed denominator-edge labels are too weak, while the present argument shows that adding exact stitchwise integer-index compatibility is already too strong once the canonical boundary pair is retained. The intended “middle” control therefore cannot preserve the full local BCZ branch choice at every step.

## 5. Consequence for the Farey discrepancy line

A nondegenerate denominator/mediant null must deliberately quotient the triple/index information rather than enforce it pointwise. Plausible classes include coarse index histograms detached from exact states, denominator strata, index transitions after state aggregation, sparse stitch constraints, or partial ancestry relations. Each candidate still has to pass both sides of the audit: it must admit genuinely different realizable paths, and its retained information must be strong enough to affect the discrepancy or spectral-allocation target rather than merely repackage the classical scalar criterion.

This result does not show that any such coarser statistic is coercive, does not give an asymptotic Farey discrepancy improvement, and has no direct RH consequence. It removes only the exact stitchwise-integrability repair as a nontrivial matched-control strategy.
