# FD-314 — Farey denominator-edge controls are nonintegrable or degenerate

**Status:** `EXACT-DERIVED + NEGATIVE/CONTROL-DESIGN + FAREY-PAIRWISE-NONINTEGRABILITY + TRUE-DENOMINATOR-RIGIDITY`.

`FD-313` leaves genuinely Farey-specific denominator or mediant structure as one possible escape from source-agnostic local-block controls. The most literal next control has a sharp obstruction in both directions.

If consecutive denominator pairs are treated only as local labels, even the complete directed pair inventory can be reassembled into a different reflection-symmetric rational grid with a different cumulative rank-grid energy. The obstruction is not that any individual edge is fake: every edge can be a genuine consecutive-denominator edge from one Farey sequence. What fails is the compatibility that stitches those edges into one Farey orbit.

Conversely, if the labels are required to remain the actual reduced denominators of all points while preserving the full denominator multiplicity profile of `F_Q`, then the control is already degenerate: that multiset contains every reduced rational of denominator at most `Q`, so increasing order reconstructs `F_Q` uniquely before any pair statistic is imposed.

Thus an exact denominator-pair matched null has a dichotomy: as abstract edge data it is too weak, while as exact pointwise denominator data it is too strong. A useful denominator control for `CLUE-farey-gap-order-bridge-suppression` must lie strictly between those extremes.

## 1. A genuine F8 edge inventory admits a non-Farey reassembly

Write the denominator word of the ordinary Farey sequence `F_8`, including endpoints, as

`q = (1,8,7,6,5,4,7,3,8,5,7,2,7,5,8,3,7,4,5,6,7,8,1)`.

Split the interior at returns to denominator `8`:

`A = (8,7,6,5,4,7,3,8)`,

`B = (8,5,7,2,7,5,8)`,

`C = (8,3,7,4,5,6,7,8)`.

The actual path is `1 · A · B · C · 1`. Since all three excursions begin and end at `8`, they can be permuted without changing any directed edge inside an excursion or either external edge. In particular,

`q* = 1 · C · B · A · 1`

is

`(1,8,3,7,4,5,6,7,8,5,7,2,7,5,8,7,6,5,4,7,3,8,1)`,

and satisfies the exact multiset identity

`multiset{(q_i,q_(i+1))} = multiset{(q*_i,q*_(i+1))}`.

Every directed pair in `q*` therefore occurs literally as a consecutive denominator pair in `F_8`, with exactly the same multiplicity as in the original sequence.

For a genuine Farey neighbor pair with denominators `a,b`, the gap is `1/(ab)`. Hence the directed-edge identity also preserves the complete induced gap multiset. Reconstruct a rational point grid from the alternative labels by

`x*_0 = 0`, and `x*_(k+1) - x*_k = 1/(q*_k q*_(k+1))`.

The gap multiset is the `F_8` gap multiset, so its sum is exactly `1`; all gaps are positive, so this is an increasing rational grid from `0` to `1`. The word `q*` is palindromic, hence the gap word is palindromic and

`x*_(22-k) = 1 - x*_k`.

Thus the reassembly also keeps exact reflection.

Let

`E(x) = sum_(k=1)^21 (x_k - k/22)^2`.

Direct exact summation gives

`E(F_8) = 1339/55440`,

`E(x*) = 541/7920`,

and therefore

`E(x*) - E(F_8) = 17/385 > 0`.

This is a finite exact separation, not an asymptotic estimate. It proves that the full directed inventory of genuine Farey denominator-edge types, together with the induced gap multiset and reflection, does not by itself determine cumulative rank-grid energy when the denominator values are treated as local edge labels.

## 2. The missing condition appears at the first stitched triple

The alternative labels do not form the denominator sequence of a Farey orbit. The failure is visible before any long-range statistic is considered.

For three consecutive denominators in `F_Q`, the Hall–Shiu Farey index

`nu_i = (q_(i-1) + q_(i+1)) / q_i`

is a positive integer and the homogeneous Farey vectors obey the corresponding next-term recurrence. This is the classical index algebra already used in `FD-011`.

At the four stitches created by the excursion permutation, `q*` gives

- `(1,8,3)`, with index `1/2`;
- `(7,8,5)`, with index `3/2`;
- `(5,8,7)`, with index `3/2`;
- `(3,8,1)`, with index `1/2`.

All interior triples of the unchanged excursions retain their original Farey compatibility; the failure is concentrated exactly at the new stitching interfaces.

The same defect is visible by reconstructing the points. After the first two gaps,

`x*_2 = 1/8 + 1/24 = 1/6`,

whose actual reduced denominator is `6`, not the label `3`. The labels in the pair inventory are therefore genuine local Farey edge labels but are not globally integrable as the actual denominators of the reconstructed path.

This distinguishes two statements that a denominator control must not conflate: pairwise edge realizability and orbit realizability. The first is preserved here; the second already needs triple/index compatibility.

## 3. Requiring the true complete denominator profile is degenerate

There is an opposite obstruction if the labels are required to be the actual reduced denominators.

For each integer `d` with `2 <= d <= Q`, there are exactly `phi(d)` reduced fractions `a/d` in `(0,1)`. Together with `0/1` and `1/1`, these are precisely all elements of `F_Q`.

Therefore suppose an increasing distinct rational grid in `[0,1]` has the same multiset of **actual reduced denominators** as `F_Q`. For each `d`, it must contain `phi(d)` distinct reduced fractions of denominator `d`, but there exist exactly `phi(d)` such fractions. Hence it contains every reduced fraction of denominator at most `Q`. Its point set is exactly `F_Q`, and increasing order is unique.

So preserving the full actual denominator multiset already fixes the Farey grid. Preserving the complete actual directed denominator-pair inventory is even stronger and cannot define a nontrivial matched ensemble.

## 4. Control-design consequence

The literal denominator-pair idea left open after `FD-313` therefore splits into two unusable extremes.

As an abstract local label statistic, it admits nonintegrable reassemblies such as the exact `F_8` certificate above and cannot coerce cumulative discrepancy. As a statistic of the true reduced denominators with the complete Farey multiplicity profile, it identifies the original point set and gives a degenerate control.

A nontrivial next denominator/mediant control must preserve an intermediate quotient of the structure: for example coarse denominator strata, selected pair or triple statistics, a partial index law, or bounded mediant/ancestry relations. Whatever is retained must be strong enough to test the suspected Farey mechanism but weak enough not to reconstruct the entire Farey sequence by definition. In particular, a generated control should be audited separately for pairwise edge validity, triple/index integrability, and accidental uniqueness.

This does not show that triple/index data, mediant ancestry, or any particular coarser denominator statistic is coercive. It only removes the naive complete-pair control as a discriminating matched null and identifies the first exact compatibility that the pair inventory forgets.

## 5. Prior art and audit boundary

The Farey-neighbor gap identity, the next-term recurrence, and the integer-valued Farey index are classical. Hall and Shiu's index theorem is already anchored in `SOURCES.md` and used in `FD-011`; no novelty is claimed for that algebra, Farey mediants, or the fact that `F_Q` contains all reduced rationals of denominator at most `Q`.

The Mathia-specific result is the control-design boundary proved above: a complete directed inventory made only from genuine `F_8` denominator edges can be reassembled with unchanged induced gaps and reflection while changing cumulative energy, but the reassembly fails exactly at Farey triple integrability; enforcing the full true denominator multiplicities instead collapses the matched-control sample space to the original Farey grid.

The decisive audit for any continuation is therefore explicit. If a proposed denominator null allows noninteger Hall–Shiu indices at its stitches, it has preserved only local labels rather than a Farey-realizable path. If it preserves all actual reduced-denominator multiplicities, check whether it has already become unique. A useful intermediate null must pass both tests.

No asymptotic separation, new Franel–Landau estimate, Möbius cancellation bound, or RH consequence is claimed.
