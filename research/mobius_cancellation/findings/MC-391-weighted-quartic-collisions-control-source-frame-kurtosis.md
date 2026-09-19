# MC-391 — Weighted quartic collisions control source-frame kurtosis

**Status:** `EXACT-DERIVED` · `FRONTIER-ADVANCE` · `STRUCTURAL-OBSTRUCTION` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the exact endpoint kernel of `MC-390`. Let

\[
W\le \mathbf F_2^R,
\qquad H:=|W|,
\qquad C:=W^\perp,
\]

and let the endpoint defect-cell masses satisfy

\[
d_z>0,
\qquad \sum_{z=1}^R d_z=1.
\]

For `I\in W`, write

\[
g(I)=(-1)^{\langle I,\mathbf1\rangle}Z(I),
\qquad
Z(I):=\sum_{z=1}^R d_z(-1)^{I_z}.
\tag{1}
\]

The low-dual-distance escape left by `MC-390` can be sharpened substantially. The second and fourth moments of `(1)` do **not** require full four-wise independence of the coordinate signs and do not care separately about dual words of weights `1` or `3`. Weight-`2` relations merely identify coordinate characters and can be merged exactly. After this merging, the only nontrivial contribution to the fourth moment comes from genuine four-character additive collisions.

Form the quotient group

\[
Q:=\mathbf F_2^R/C\cong \widehat W,
\qquad
\alpha_z:=e_z+C\in Q.
\tag{2}
\]

Let `A` be the set of distinct values among the `\alpha_z`, and aggregate equal coordinate characters by

\[
w_a:=\sum_{z:\alpha_z=a}d_z,
\qquad a\in A.
\tag{3}
\]

Then `w_a>0`, `\sum_aw_a=1`, and

\[
Z(I)=\sum_{a\in A}w_a\chi_a(I),
\qquad
\chi_a(I):=(-1)^{\langle I,a\rangle},
\tag{4}
\]

where the characters `\chi_a` are distinct. Put

\[
\sigma_A^2:=\sum_{a\in A}w_a^2
\tag{5}
\]

and define the weighted genuine four-collision mass

\[
\mathcal Q_4
:=
\sum_{\substack{\{a,b,c,d\}\subset A\\
a+b+c+d=0}}
w_aw_bw_cw_d,
\tag{6}
\]

where the sum is over four **distinct** elements of `A`.

For uniform `I\in W`, one has the exact identities

\[
\boxed{\mathbf E|g(I)|^2=\sigma_A^2}
\tag{7}
\]

and

\[
\boxed{
\mathbf E|g(I)|^4
=3\sigma_A^4-2\sum_{a\in A}w_a^4+24\mathcal Q_4.
}
\tag{8}
\]

Consequently Paley--Zygmund gives

\[
\boxed{
\Pr_{I\in W}\!\left(
|g(I)|\ge\sqrt{\sigma_A^2/2}
\right)
\ge
\frac1{12+96\,\mathcal Q_4/\sigma_A^4}.
}
\tag{9}
\]

Since `|A|\le R` and `\sum_aw_a=1`,

\[
\sigma_A^2\ge\frac1{|A|}\ge\frac1R.
\tag{10}
\]

Thus `(9)` always concerns correlations at least at the critical frame scale `1/\sqrt{2R}`.

The decisive consequence is that **a small number of low-weight dual relations is not an escape from `MC-390`**. If `\mathcal Q_4=0`, then `(9)` recovers the same positive-density bound `1/12` as `MC-390`, even if `C` contains weight-`1`, weight-`2`, or weight-`3` words. Weight-`2` words have already been absorbed into `(3)`; odd-weight words do not contribute to the even moments unless, together with other relations, they induce a genuine four-character collision already counted by `(6)`.

More quantitatively, suppose the high-rank branch of `MC-381` holds, so `H\ge2^{3R/4}`, and suppose an analytic good/bad decomposition has at most

\[
|B|\le K\frac HR
\tag{11}
\]

bad nonzero modes for a fixed `K>0`, while every other nonzero mode satisfies

\[
|g(I)|=o(R^{-1/2}).
\tag{12}
\]

For large `R`, every mode counted by `(9)` except possibly `I=0` must lie in `B`. Hence

\[
\frac1{12+96\,\mathcal Q_4/\sigma_A^4}
\le\frac KR+\frac1H,
\]

and therefore

\[
\boxed{
\frac{\mathcal Q_4}{\sigma_A^4}
\ge
\frac{R}{96K}-\frac18-o(1).
}
\tag{13}
\]

So an `O(H/R)` exceptional-set theorem at `o(R^{-1/2})` scale requires **linearly growing normalized quartic collision mass**. Mere existence of one weight-`4` dual word is nowhere near sufficient.

In the balanced special case where the distinct character classes have equal mass `w_a=1/r`, `r=|A|`, equation `(13)` becomes a literal counting requirement. If `N_4` is the number of four-element subsets of `A` summing to zero, then

\[
\frac{\mathcal Q_4}{\sigma_A^4}
=\frac{N_4}{r^2},
\]

so for `r\asymp R`,

\[
\boxed{N_4=\Omega(R^3).}
\tag{14}
\]

The surviving source-frame route therefore needs a highly non-Sidon projected endpoint character system, not merely a low-dual-distance codeword.

No estimate for `M(x)` and no RH consequence follows.

## 1. Weight-2 dual words are exactly duplicate coordinate characters

For `z,z'\in[R]`,

\[
\alpha_z=\alpha_{z'}
\iff e_z+e_{z'}\in C.
\tag{15}
\]

Thus a weight-`2` dual word says only that the two coordinate characters agree identically on `W`:

\[
(-1)^{I_z}=(-1)^{I_{z'}}
\qquad(I\in W).
\]

Combining their positive masses is therefore an exact identity, not an approximation. After the aggregation `(3)`, there are no remaining weight-`2` character collisions, and the frame kernel is unchanged.

This already sharpens the last paragraph of `MC-390`: classifying the mere existence of weight-`2` words is not enough. Their only effect at the moment level is to reduce the number of distinct coordinate characters and replace the original cell masses by their sums.

## 2. Exact second and fourth moments after aggregation

Character orthogonality on `W` gives

\[
\mathbf E_I\chi_a(I)\chi_b(I)
=\mathbf1_{a=b}.
\tag{16}
\]

Since the `a\in A` are distinct, `(7)` follows immediately.

For the fourth moment,

\[
\mathbf E_I\chi_a\chi_b\chi_c\chi_d
=\mathbf1_{a+b+c+d=0}.
\tag{17}
\]

In the elementary `2`-group `Q`, a zero four-sum has only two kinds of contribution:

1. the indices pair, producing the ordinary Rademacher fourth moment; or
2. four distinct character classes satisfy `a+b+c+d=0`.

The paired terms contribute

\[
\sum_aw_a^4+6\sum_{a<b}w_a^2w_b^2
=3\sigma_A^4-2\sum_aw_a^4.
\tag{18}
\]

Every unordered genuine four-collision in `(6)` has `4!=24` ordered realizations in the expansion, giving `(8)`.

This derivation shows exactly why dual weights `1` and `3` were stronger exclusions than the moment argument needed in `MC-390`. An odd-weight parity relation never appears by itself in an even fourth-moment expansion. It matters here only if the linear relation structure also creates an even four-character collision represented in `(6)`.

## 3. Paley--Zygmund turns additive collisions into an exception lower bound

Apply Paley--Zygmund to `Y=|g(I)|^2` at threshold `1/2`. From `(7)`--`(8)`,

\[
\Pr\left(Y\ge\frac12\sigma_A^2\right)
\ge
\frac{\sigma_A^4}{4\,\mathbf E|g|^4}
\ge
\frac1{12+96\mathcal Q_4/\sigma_A^4},
\]

which is `(9)`.

This exposes the actual structural parameter hidden by the coarse dual-distance split: the relevant quantity is the **weighted additive energy beyond the trivial pairings** of the projected coordinate characters. Positive-density anti-concentration survives whenever that excess is `O(\sigma_A^4)`. To compress all critical-scale correlations into only `O(H/R)` physical modes, the excess must instead be larger by a factor `\Omega(R)` as in `(13)`.

The balanced specialization `(14)` makes the scale transparent. A Sidon-like set, or even a set with only `o(R^3)` genuine four-collisions, cannot support an `O(H/R)` exceptional family when `r\asymp R`; the required quartic relation count is cubic.

## 4. Arithmetic meaning for the source-incidence span

For the exact source subspace of `MC-381`,

\[
C=W^\perp
=\operatorname{span}_{\mathbf F_2}\{c_p:p>y^{1/100}\}.
\tag{19}
\]

A relation among four distinct projected coordinate characters therefore means that some binary combination of the large-source incidence columns has endpoint support equal, after duplicate-character identification, to those four classes. In original coordinates it is a localized even parity relation among endpoint generators.

Equation `(13)` says that the live arithmetic problem is not simply

> does the source-incidence span contain a word of weight at most four?

The needed structure is much stronger. After exact weight-`2` collapse, the source package must produce enough genuine four-cell parity collisions, with enough endpoint mass on their supports, that their normalized weighted total grows like `R`. If the source incidence is generic enough to be Sidon-like after projection, the endpoint route is killed by `(9)` rather than helped by that pseudorandomness.

This also separates the role of weight-`3` relations. A weight-`3` word can be arithmetically interesting, but it is not by itself an escape from the even-moment obstruction. Any useful effect on `(8)` must materialize as an even four-character collision, possibly after combining it with another odd relation.

## 5. Relation to `MC-389` and `MC-390`

`MC-389` already identifies the fourth moment with the additive energy of the endpoint Bochner measure and proves a fixed gap above the abstract Welch exception floor from high affine rank. The present result resolves that energy into its exact trivial-pair and genuine-four-collision pieces. It does not replace the stronger affine-rank estimate of `MC-389`; rather, it identifies what the remaining arithmetic escape must contain.

`MC-390` obtains positive-density critical-scale correlations from the sufficient hypothesis `d^\perp(W)\ge5`, using the classical implication to four-wise independent coordinate signs. Equations `(7)`--`(9)` show that this hypothesis is stronger than necessary. Full strength-four orthogonal-array behavior is not required: duplicates can be merged exactly, odd dual relations are harmless to these even moments unless they induce an even collision, and the positive-density conclusion persists whenever the weighted four-collision excess is small.

Thus the next source-incidence classification should prioritize **weighted four-character collision structure** rather than treating weights `2`, `3`, and `4` symmetrically.

## Prior art and novelty boundary

The ingredients are classical. Finite-group character orthogonality, Plancherel, additive energy, Sidon/B2 sets, and Paley--Zygmund are standard. `MC-389` already audited additive-energy literature for the endpoint support, while `MC-390` audited the binary code/orthogonal-array correspondence through MacWilliams--Sloane and a modern orthogonal-array review.

A targeted literature search on 19 September 2026 also found Ingo Czerwinski and Alexander Pott, *Sidon sets, sum-free sets and linear codes*, Advances in Mathematics of Communications **18** (2024), 549--566, DOI `10.3934/amc.2023054`, which recalls the classical correspondence between sum-free Sidon sets in `\mathbf F_2^t` and binary linear codes of minimum distance at least five. That correspondence is adjacent but stronger than what is needed here: minimum distance at least five excludes all weights `1`--`4`, whereas the endpoint even-moment calculation can quotient weight-`2` duplicates and does not use odd-weight exclusion separately.

No novelty is claimed for the code/Sidon correspondence, the moment expansion, additive energy, or Paley--Zygmund. The Mathia-specific delta is the exact endpoint consequence `(9)`--`(13)`: the coarse low-dual-distance escape of `MC-390` collapses to a quantitative requirement for linearly growing **weighted genuine four-character collision mass** in the actual source frame.

## Boundaries and falsification tests

- **Exact endpoint kernel is load-bearing.** The positive masses and coordinate-character form `(1)` come from the endpoint partition used by `MC-390`.
- **Weight-2 merging is exact, not a deletion.** Aggregating equal characters changes neither `g` nor any moment; it can only increase the effective squared mass relative to treating duplicate cells separately.
- **Odd dual words are not declared irrelevant to all mathematics.** They are irrelevant *by themselves* to the second/fourth even moments. They may constrain the source arithmetic or combine to create the even collision structure counted by `(6)`.
- **One weight-4 word is not enough.** The quantitative requirement is weighted and scales as `(13)` for an `O(H/R)` exceptional family.
- **The balanced count `(14)` is only a specialization.** For unequal endpoint masses, `\mathcal Q_4`, not the raw number of four-relations, is the correct invariant.
- **No analytic good-mode theorem is supplied.** This result constrains what source geometry such a theorem would need; it does not prove character-sum cancellation.
- **No conflict with `MC-389`.** The affine-rank energy bound remains stronger for its fixed-threshold conclusion. This finding gives a finer algebraic interpretation of the low-weight/low-moment escape.
- **No Möbius or RH conclusion.** The result remains internal to the endpoint/source-frame strategy.

## Consequence for the research line

The structural frontier left by `MC-390` is narrower than `d^\perp(W)\le4`. A useful source package must survive exact duplicate-character aggregation and then exhibit a large weighted family of genuine four-character additive collisions. In the balanced rank-linear regime, reaching only `O(H/R)` critical-scale exceptions requires cubic-order four-relations.

Accordingly, the next arithmetic question is not a flat classification of dual weights `2`, `3`, and `4`. It is whether the actual large-source incidence system can generate the **weighted quartic relation mass** demanded by `(13)` while still respecting the conductor/source-cost constraints of the endpoint program. Generic high-distance or Sidon-like behavior is decisively hostile to that goal.