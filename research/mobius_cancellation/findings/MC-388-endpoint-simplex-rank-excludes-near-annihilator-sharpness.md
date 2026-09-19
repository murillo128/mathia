# MC-388 — Endpoint simplex rank excludes near-annihilator sharpness

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `FRONTIER-ADVANCE` · `DECISIVE-NEGATIVE` · `STRUCTURAL-OBSTRUCTION` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the exact endpoint partition of `MC-296` and the source-frame setting of `MC-381`, `MC-386`, and `MC-387`. Let

\[
\mathcal R_y=D_1\sqcup\cdots\sqcup D_R,
\qquad d_z:=|D_z|/|\mathcal R_y|>0,
\qquad \sum_{z=1}^R d_z=1,
\]

and let

\[
W\le \mathbf F_2^R,
\qquad d:=\dim W,
\qquad H:=|W|.
\]

For `I\in W`, write `v_I` for the normalized shell row and

\[
G_{I,J}=g(I+J)
\]

for its Cayley Gram kernel. Identify `\widehat W` with the restrictions to `W` of linear functionals on `\mathbf F_2^R`, and let

\[
\pi:\mathbf F_2^R\to\widehat W,
\qquad
\pi(a)(I)=\langle I,a\rangle.
\]

Then the finite Bochner measure of `g` is not an arbitrary rank-`R` probability measure. It is exactly the push-forward of the endpoint defect weights on the `R` affine-simplex vertices

\[
a_z=\mathbf1+e_z:
\qquad
p=\sum_{z=1}^R d_z\,\delta_{\pi(a_z)},
\tag{1}
\]

with equal atoms combined when two projections coincide. Hence, for

\[
S:=\operatorname{supp}p=\{\pi(\mathbf1+e_z):1\le z\le R\},
\]

one has the exact affine-rank identity

\[
\boxed{
\dim\operatorname{aff}(S)
=d-\dim\bigl(W\cap\langle\mathbf1\rangle\bigr)
\ge d-1.
}
\tag{2}
\]

Consequently, for every affine coset `C=\xi_0+L\subset\widehat W`,

\[
\boxed{
|S\setminus C|
\ge d-1-\dim L.
}
\tag{3}
\]

In particular, the near-annihilator conclusion of `MC-387` is **incompatible with every surviving endpoint subspace of linear dimension**. If the hypotheses of `MC-387` held with

\[
\sum_{K\in W}|g(K)|^2\le(1+o(1))\frac HR
\]

and with all but `o(H/R)` of that energy concentrated on `(1+o(1))H/R` physical modes, then `MC-387` would produce a coset `C=\xi_0+L` satisfying

\[
|S\triangle C|=o(R),
\qquad
|L|=(1+o(1))R.
\tag{4}
\]

But `(3)` and `(4)` imply

\[
d\le 1+\log_2|L|+o(R)=o(R).
\tag{5}
\]

Thus no sequence with `d\ge cR` for a fixed `c>0` can approach the abstract subgroup/annihilator sharpness model of `MC-386`.

This applies directly to the rank-linear source-cost branch. Under the trial regime used in `MC-381`, the fixed-power source cutoff leaves a subspace with

\[
d\ge 3R/4.
\]

Therefore the exact endpoint source frame in that regime cannot realize, or asymptotically approach, the `H/R`-supported annihilator extremizer. The surviving sharpness witness from `MC-386` is an admissible abstract PSD Cayley frame but **not an admissible high-dimensional endpoint partition frame**.

This resolves the live high-dimensional branch of `CLUE-cayley-welch-near-extremizer-geometry` negatively without needing a further primitive-conductor argument. It does not yet improve the `H/R` exceptional-count scale quantitatively: a frame may stay away from the near-extremal concentration regime while still place substantial correlation energy on `Theta(H/R)` differences. A new quantitative energy/concentration gap would be needed for that stronger conclusion.

No estimate for `M(x)` follows.

## 1. The endpoint partition fixes the Bochner atoms

For a shell prime `r\in D_z`, the endpoint rule of `MC-296` says that the generator indexed by `z` takes sign `+1` and every other selected generator takes sign `-1`. Therefore, for every mode `I\subseteq[R]`,

\[
\chi_I(r)
=(-1)^{|I|+1_{z\in I}}
=(-1)^{\langle I,\mathbf1+e_z\rangle}.
\tag{6}
\]

Restricting to `I\in W` and averaging over the partition gives

\[
g(I)
=\sum_{z=1}^R d_z(-1)^{\langle I,\mathbf1+e_z\rangle}.
\tag{7}
\]

Equation `(7)` is already the finite Fourier representation of `g` on `W`. Since every `d_z` is positive, combining equal projected atoms gives exactly `(1)` and the stated support `S`.

This identifies what the abstract Fourier support in `MC-387` means for an exact endpoint: it is the projection to `W^*` of a translated coordinate simplex. The support is therefore much more rigid than a generic set of at most `R` characters.

## 2. The projected simplex has affine dimension at least `d-1`

Translation by `\pi(\mathbf1)` does not change affine dimension, so the direction space of `\operatorname{aff}(S)` is

\[
\operatorname{span}\{\pi(e_z+e_1):1\le z\le R\}.
\tag{8}
\]

The vectors `e_z+e_1` span the even-weight hyperplane

\[
E:=\{x\in\mathbf F_2^R:\langle x,\mathbf1\rangle=0\}.
\tag{9}
\]

Hence the direction space in `(8)` is `\pi(E)`. Its annihilator inside `W` is

\[
\{I\in W:\langle I,x\rangle=0\text{ for all }x\in E\}
=W\cap E^\perp
=W\cap\langle\mathbf1\rangle.
\tag{10}
\]

Duality therefore gives

\[
\dim\pi(E)
=d-\dim(W\cap\langle\mathbf1\rangle),
\]

which proves `(2)`. The possible loss is exactly one dimension, according to whether the all-ones mode belongs to `W`.

Equivalently, the coordinate restrictions `I\mapsto I_z` are the columns of a generator matrix for the binary code `W`; they span `W^*`. Translating those columns by their total sum can reduce affine rank by at most one. This is ordinary binary linear algebra, not a new coding-theory theorem.

## 3. A high-rank projected simplex cannot be close to a small-dimensional coset

Let `C=\xi_0+L` and put `k=|S\setminus C|`. If `S\cap C` is nonempty, start with the affine space `C`, of dimension `\dim L`, and add the `k` points outside it one at a time. Each point raises affine dimension by at most one, so

\[
\dim\operatorname{aff}(S)\le \dim L+k.
\tag{11}
\]

If `S\cap C` is empty, then `k=|S|` and the same inequality is trivial because `\dim\operatorname{aff}(S)\le|S|-1`. Combining `(2)` and `(11)` proves `(3)`.

Now apply `MC-387`. Its near-Welch plus minimal-physical-concentration hypotheses force a coset with `(4)`. Since a subgroup of `\widehat W` has power-of-two cardinality,

\[
\dim L=\log_2|L|=O(\log R).
\tag{12}
\]

Equation `(3)` then forces

\[
|S\setminus C|
\ge d-1-O(\log R).
\tag{13}
\]

For `d\ge cR`, the right side is `\Omega(R)`, contradicting `|S\triangle C|=o(R)`. This proves `(5)` and the high-dimensional exclusion.

The argument is stronger than asking whether the primitive quadratic source characters themselves form an approximate subgroup. It shows that the **shell-side Bochner support forced by the endpoint partition** already has too much affine rank to approximate the low-dimensional coset demanded by near-annihilator sharpness.

## 4. Consequence for the source-cost frontier

`MC-381` obtains its rank-linear source-cost contradiction after deleting source coordinates above a fixed shell power. Under its trial bound it retains

\[
\dim W\ge3R/4.
\tag{14}
\]

The exact endpoint partition remains valid after restricting the row index from the full mode cube to this `W`, so `(1)`--`(3)` apply unchanged. Any annihilator-type extremizer with Fourier support of size about `R` would live in an affine space of dimension only `O(\log R)`, whereas the actual endpoint Bochner support has affine dimension at least `3R/4-1`.

Thus the third escape listed in `MC-386`—that about `H/R` exceptional differences might realize the abstract subgroup/annihilator concentration—is not available in the high-dimensional source-cost branch in its exact or near-extremal form.

This does **not** by itself prove that fewer than `H/R` exceptional source differences suffice for contradiction. The frame could carry more than the Welch-minimal total energy, or distribute near-minimal energy over a larger physical set. What has been removed is the specific sharpness mechanism that made `H/R` unavoidable under the generic PSD-Cayley hypotheses. The next useful target is therefore quantitative: bound how much extra physical spread or additive-energy deficit is forced by the affine-rank lower bound `(2)`.

## Prior art and novelty boundary

The finite-harmonic stability input is exactly `MC-387`. Its prior-art audit uses Xuancheng Shao, *Additive energies of subsets of discrete cubes*, Proceedings of the Royal Society of Edinburgh Section A: Mathematics **156** (2026), 944–965, DOI `10.1017/prm.2024.126`, together with classical finite-group uncertainty/coset extremizers including Aline Bonami and Saifallah Ghobber, *Equality cases for the uncertainty principle in finite Abelian groups*, Acta Scientiarum Mathematicarum **79** (2013), 507–528. A fresh source check on 19 September 2026 confirms Shao's article was published online by Cambridge University Press on 18 November 2024 and treats near-maximal additive energy as an inverse-structure problem.

The generator-matrix interpretation of the coordinate restrictions and the fact that matrix rank equals the span dimension of its columns are elementary coding theory/linear algebra; the simplex/Hamming viewpoint has already been used and prior-art audited in `MC-282` and the Walsh column calculations in `MC-375`. No novelty is claimed for any of these ingredients.

A targeted search on 19 September 2026 found the standard additive-energy/coset-stability and coding-rank ingredients but no source was used to claim the endpoint-specific composition `(1)`--`(5)`. Absence from that search is not evidence of novelty. The durable result is the exact identification of the `MC-387` Bochner support with the projected endpoint simplex and the resulting exclusion of near-annihilator sharpness in the high-dimensional source-cost regime.

## Boundaries and falsification tests

- **Exact endpoint partition is load-bearing.** Equation `(6)` uses the one-defect-per-shell-prime rule of `MC-296`. Overlapping defects or an additional common cell change the Bochner atoms.
- **High-dimensional `W` is load-bearing for the asymptotic exclusion.** Equation `(3)` is exact for every `W`, but a subspace with `d=O(\log R)` can in principle have its projected simplex lie in, or near, an `R`-point coset.
- **No claim that all `Theta(H/R)` exceptional patterns are impossible.** The theorem excludes the exact/near subgroup-annihilator concentration certified by `MC-387`, not every frame with that exceptional cardinality scale.
- **No primitive-conductor theorem is used.** This is a stronger early obstruction for the accepted clue, not evidence that conductor reduction or character multiplication would independently forbid the same pattern.
- **Positive defect weights matter only for support identity.** If some `D_z` were empty, the corresponding atom could disappear; the canonical endpoint mandate assumes all `R` defect cells are nonempty.
- **No RH or global Möbius conclusion.** The result narrows an internal endpoint/source-frame escape and supplies no estimate for `M(x)`.

## Research consequence

The abstract sharpness example of `MC-386` is now separated from the actual endpoint geometry. `MC-387` says every near-minimal concentrated frame must approach a coset/annihilator pair; `(2)`--`(5)` say an exact high-dimensional endpoint frame cannot do so because its Fourier support is a projected simplex of affine rank `\Theta(R)`.

The live question is no longer whether primitive quadratic source conductors can realize that particular near-coset pattern. The sharper next question is whether the affine-rank obstruction can be made **quantitative**: derive an explicit additive-energy deficit, physical-spread lower bound, or improved exceptional-mode budget for high-dimensional projected endpoint simplices. Such a result could turn the qualitative inadmissibility proved here into a stronger source-frame contradiction.