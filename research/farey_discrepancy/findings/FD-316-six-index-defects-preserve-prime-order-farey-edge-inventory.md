# FD-316 — Six index defects preserve the prime-order Farey edge inventory

**Status:** `EXACT-DERIVED + NEGATIVE/CONTROL-DESIGN + PRIME-ORDER-FAMILY + DENSITY-ONE-STITCH-NONRIGIDITY`.

`FD-314` shows that the complete directed inventory of genuine Farey denominator edges is too weak when the edges are treated as local labels. `FD-315` shows that requiring exact integer Farey index at every stitch is too strong: it reconstructs the canonical denominator orbit. The gap between those two controls is not governed by the *density* of valid stitches.

For every prime `p>=7`, there is a reflection-symmetric reassembly of the genuine directed denominator edges of `F_p` with exactly **six** noninteger Hall--Shiu indices and all remaining stitches unchanged from `F_p`. The defect fraction therefore tends to zero quadratically in `p`, yet the reassembly changes the rank of the genuine point `2/p` by order `p` positions.

Thus exact Farey-index compatibility on a density-one set of stitches is still nonrigid. Any useful quotient-level denominator control must remember where exceptional stitches occur, or retain another state-aware/nonlocal relation; a global statistic such as the fraction of valid triples is insufficient.

## 1. Prime-order excursion decomposition

Let `p>=7` be prime, and let

`q_0,q_1,...,q_(N_p)`

be the denominator word of `F_p`, where

`N_p = sum_(m<=p) phi(m)`

is the number of Farey gaps.

Because `p` is prime, denominator `p` occurs exactly at the fractions

`1/p,2/p,...,(p-1)/p`.

For `1<=a<=p-2`, let `E_a` be the denominator subword running from `a/p` to `(a+1)/p`, including the endpoint denominators `p` at both ends. Reflection of the Farey sequence gives

`E_(p-1-a) = reverse(E_a)`.

The ordinary denominator path is therefore

`1 · E_1 · E_2 · E_3 · ... · E_(p-4) · E_(p-3) · E_(p-2) · 1`,

with the repeated endpoint `p` identified when consecutive excursions are concatenated.

Define a new path by swapping the first two excursions and, symmetrically, their reflected partners:

`1 · E_2 · E_1 · E_3 · ... · E_(p-4) · E_(p-2) · E_(p-3) · 1`.

For `p=7`, the middle range consists only of `E_3`; the definition is still literal.

Each excursion is a closed path from denominator `p` back to denominator `p`. Permuting these closed paths changes no directed edge internal to any excursion and creates no new inter-excursion edge other than the already included first/last edge of the next excursion. The two external edges `1->p` and `p->1` are also unchanged.

Hence the alternative path preserves **exactly** the complete directed edge multiset

`multiset{(q_i,q_(i+1))}`

of the genuine `F_p` denominator word. The symmetric swap also preserves reflection.

## 2. Exactly six Farey-index defects

All triples strictly inside an unchanged excursion remain genuine Farey triples. All interfaces not touched by the two swaps remain the original interfaces. It is therefore enough to inspect the three modified stitches on the left; reflection produces the other three.

Let `r` be the inverse of `3 mod p`, chosen in `{1,...,p-1}`.

The first denominator after `2/p` is

`(p-1)/2`,

because the successor denominator of `a/p` is congruent to `-a^(-1) mod p`.

The last denominator before `3/p` is `r`. The first denominator after `1/p` is `p-1). The last denominator before `2/p` is `(p+1)/2`, and the first denominator after `3/p` is `p-r`.

Thus the three new left-hand stitches have denominator triples

1. `(1, p, (p-1)/2)`;
2. `(r, p, p-1)`;
3. `((p+1)/2, p, p-r)`.

Their Hall--Shiu indices are respectively

`(p+1)/(2p)`,

`(p-1+r)/p`,

and

`((p+1)/2 + p-r)/p`.

None is an integer for `p>=7`:

- the first numerator lies strictly between `0` and `p`;
- the second numerator lies in `[p,2p)` and would equal `p` only if `r=1`, impossible for an inverse of `3` modulo `p>=7`;
- the third numerator lies in `(0,2p)` and could be divisible by `p` only if `r=(p+1)/2`, which would identify the inverses of `3` and `2` modulo `p`, again impossible.

Reflection gives three distinct noninteger stitches on the right with the same index values. No other triple changes. Therefore

`boxed(number of noninteger Farey indices = 6)`

for every prime `p>=7`.

The denominator word of `F_p` has `N_p+1` vertices, hence `N_p-1` interior triples. Since

`N_p = sum_(m<=p) phi(m) ~ (3/pi^2) p^2`,

the defect density is

`6/(N_p-1) ~ 2 pi^2 / p^2 -> 0`.

So stitchwise Farey compatibility holds on a density-one set, indeed with only a fixed number of exceptions.

## 3. The six defects still move a genuine Farey point by order p ranks

The edge inventory is genuine, so assign to every directed denominator edge `(a,b)` its usual Farey gap `1/(ab)`, and reconstruct the alternative rational grid from `0`.

Every excursion `E_a` has total gap exactly `1/p`, because in the genuine Farey sequence it runs from `a/p` to `(a+1)/p`. Consequently, after the initial edge `0 -> 1/p` and the first swapped excursion `E_2`, the alternative grid still lands exactly on the genuine point `2/p`.

Only its **rank** has changed.

Let `L_1` and `L_2` be the numbers of edges in `E_1` and `E_2`.

Between `1/p` and `2/p`, every interior Farey fraction has numerator `1`, namely `1/q` with `p/2<q<p`. There are `(p-1)/2` such fractions, so

`L_1=(p+1)/2`.

Between `2/p` and `3/p`, an interior fraction can only have numerator `1` or `2`. Counting the admissible denominators separately for `p=6m+1` and `p=6m+5` gives exactly `floor(p/3)` interior fractions. Hence

`L_2=floor(p/3)+1`.

Therefore

`L_1-L_2 = (p-1)/6` if `p=1 mod 6`,

and

`L_1-L_2 = (p+1)/6` if `p=5 mod 6`.

In the genuine Farey grid, `2/p` occurs after `1+L_1` gaps. In the reassembled grid it occurs after `1+L_2` gaps. For rank-grid discrepancy

`D(x_k)=x_k-k/N_p`,

the discrepancy change at the same geometric point `2/p` is therefore

`boxed(D_alt(2/p)-D_Farey(2/p) = (L_1-L_2)/N_p)`.

Using `N_p~3p^2/pi^2`,

`D_alt(2/p)-D_Farey(2/p) ~ pi^2/(18p)`.

Thus six exceptional stitches, whose density is `Theta(p^-2)`, can move a genuine Farey point by `Theta(p)` rank positions and change its normalized rank discrepancy by `Theta(p^-1)`.

This does not give a nonvanishing asymptotic discrepancy gap; it shows that the effect is much larger than the raw defect density and that counting valid stitches alone loses the state information that controls global ordering.

## 4. Exact p=7 audit

For `p=7`, the genuine denominator word is

`(1,7,6,5,4,7,3,5,7,2,7,5,3,7,4,5,6,7,1)`.

After the symmetric excursion swap it becomes

`(1,7,3,5,7,6,5,4,7,2,7,4,5,6,7,5,3,7,1)`.

The six noninteger index values are exactly

`4/7, 11/7, 6/7, 6/7, 11/7, 4/7`.

The genuine point `2/7` moves from rank `5` to rank `4`, so its normalized discrepancy changes by `1/18`, matching the general formula.

As a finite additional audit, if

`E = sum_(k=1)^(N_p-1) (x_k-k/N_p)^2`,

then exact rational summation gives

`E(F_7)=197/7560`,

`E(alt)=2911/52920`,

and

`E(alt)-E(F_7)=383/13230>0`.

The family theorem does not claim a uniform lower bound for this energy difference as `p->infinity`; the exact `p=7` value is only a finite nondegeneracy check.

## 5. Consequence for the control hierarchy

The literal hierarchy around `FD-314` and `FD-315` now has three distinct levels.

1. **Complete genuine denominator-edge inventory:** too weak. `FD-314` gives nonintegrable reassemblies.
2. **Exact integer Farey index at every stitch:** too strong. `FD-315` reconstructs the canonical orbit.
3. **Exact index compatibility at all but finitely many stitches:** still too weak. The present prime family preserves every edge and has only six defective stitches, yet changes global ranks.

Therefore a useful intermediate control cannot be based only on the *proportion* of valid triples, even if that proportion tends to one. The locations and states of the exceptional stitches matter.

Promising nondegenerate quotients must retain state-aware information without fixing every transition: for example index-transition statistics conditioned on denominator strata, sparse compatibility constraints tied to specified states, selected mediant ancestry, or another invariant that distinguishes a bounded set of strategically placed defects from generic rare defects.

## 6. Prior-art and audit boundary

The integer-valued Farey index, the next-term denominator recurrence, and the BCZ/Farey-triangle dynamics are classical and already anchored in `SOURCES.md` through Hall--Shiu and the existing Farey-dynamics sources. The standard asymptotic

`sum_(n<=x) phi(n) ~ 3x^2/pi^2`

is also classical and already part of the line's Farey/totient background.

The targeted prior-art audit found work on the Farey index, parity-weighted Farey indices, and BCZ dynamics, but no result equivalent to the present matched-control statement: preserve the entire directed edge inventory of `F_p`, violate exactly six local indices, and quantify the induced rank displacement.

No novelty is claimed for the classical index formulas, Farey recurrence, reflection, or totient asymptotic. The Mathia-specific result is the control-design obstruction and its exact six-defect prime family.

## 7. Boundaries

- The reassembled denominator labels are not globally the actual reduced denominators of the reconstructed points at the six defective stitches.
- The construction is not another Farey sequence.
- The defect density tending to zero does not imply a nonzero limiting discrepancy gap; the proved rank-discrepancy shift is `Theta(1/p)`.
- No asymptotic lower bound for the quadratic energy difference is claimed.
- No Franel--Landau improvement, Möbius cancellation estimate, or RH consequence is claimed.
- The result rules out only controls that forget the *state/location* of a bounded number of stitch defects.
