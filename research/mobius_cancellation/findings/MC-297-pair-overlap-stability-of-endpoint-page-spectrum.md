# MC-297 — Pair-overlap stability of the endpoint Page spectrum

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `FRONTIER-REFINEMENT` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the localized Legendre-shell notation and Page source-cost threshold from `MC-293` and the endpoint family of `MC-296`. Let

\[
\lambda_1,\ldots,\lambda_R\in H^*
\]

be linearly independent shell functionals, with preferred sign `-1`. Write

\[
D_i:=\{r\in\mathcal R_y:(-1)^{\lambda_i(s(r))}=+1\},
\qquad
d_i:=\frac{|D_i|}{N}.
\]

For a subset `I\subseteq[R]`, put

\[
\lambda_I:=\sum_{i\in I}\lambda_i,
\qquad
j:=|I|,
\qquad
d(I):=\sum_{i\in I}d_i,
\]

and at a shell point `r` let

\[
K_I(r):=\sum_{i\in I}\mathbf 1_{D_i}(r).
\]

Define the overlap correction

\[
\Omega_I
:=\frac1N\sum_{r\in\mathcal R_y}
\left\lfloor\frac{K_I(r)}2\right\rfloor
\]

and the pair-overlap budget

\[
B_I
:=\sum_{\{a,b\}\subseteq I}
\frac{|D_a\cap D_b|}{N}
=\frac1N\sum_{r\in\mathcal R_y}\binom{K_I(r)}2.
\]

Then the selected Fourier coefficient satisfies the exact identity

\[
\boxed{
 x_{\lambda_I}
 =(-1)^j\bigl(1-2d(I)+4\Omega_I\bigr).
}
\tag{1}
\]

Moreover

\[
0\le\Omega_I\le B_I,
\]

so

\[
\boxed{
\left|(-1)^j x_{\lambda_I}-(1-2d(I))\right|
\le4B_I.
}
\tag{2}
\]

This gives an approximate-partition stability theorem for the endpoint profile. In particular, **coverage of the shell is not required** for the exact `MC-296` multiplier: if the defect sets are pairwise disjoint, then `B_I=\Omega_I=0` for every `I`, and

\[
x_{\lambda_I}=(-1)^j(1-2d(I))
\]

whether or not `\bigcup_iD_i=\mathcal R_y`. Thus the `MC-296` boundary statement that an exact cover is load-bearing is too strong. Exact coverage was useful there to impose `\sum_i d_i=1` and model endpoint saturation; **pairwise disjointness**, not coverage, is the condition needed for its Fourier identity.

The formula also identifies precisely what changes once defects overlap: the correction is not an arbitrary higher-correlation remainder but the nonnegative parity-folding term `4\Omega_I`, controlled above by total pair intersections.

## 1. Exact derivation

For every selected coordinate,

\[
(-1)^{\lambda_i(s(r))}
=-(-1)^{\mathbf 1_{D_i}(r)}.
\]

Multiplying over `i\in I` gives

\[
(-1)^{\lambda_I(s(r))}
=(-1)^j(-1)^{K_I(r)}.
\]

For every nonnegative integer `k`,

\[
\mathbf 1_{k\text{ odd}}
=k-2\left\lfloor\frac k2\right\rfloor.
\]

Hence

\[
(-1)^k
=1-2k+4\left\lfloor\frac k2\right\rfloor.
\]

Averaging over the shell and using

\[
\frac1N\sum_rK_I(r)=\sum_{i\in I}d_i=d(I)
\]

proves `(1)`.

For every integer `k\ge0`,

\[
\left\lfloor\frac k2\right\rfloor
\le\binom{k}{2}.
\]

Averaging gives `\Omega_I\le B_I` and therefore `(2)`.

The exact correction is one-sided:

\[
(-1)^j x_{\lambda_I}\ge1-2d(I).
\tag{3}
\]

That asymmetry matters for the Page consequence below.

## 2. Page balance turns small overlap into source-cost inflation

Use the same `D_y` and `\varepsilon_y=O((\log y)^{-2})` as `MC-293`: apart from at most one nonzero Page-exceptional functional `\lambda_*`,

\[
Q(\lambda)\le D_y
\quad\Longrightarrow\quad
|x_\lambda|\le\varepsilon_y.
\tag{4}
\]

Because the `\lambda_i` are linearly independent, `I\mapsto\lambda_I` is injective and every nonempty `I` gives a nonzero functional. Combining `(2)` with `(4)` yields the robust exclusion

\[
\boxed{
|1-2d(I)|>\varepsilon_y+4B_I
\quad\Longrightarrow\quad
Q(\lambda_I)>D_y,
}
\tag{5}
\]

except when `\lambda_I=\lambda_*`.

The one-sided identity gives a sharper statement below half mass. If

\[
d(I)<\frac12,
\qquad
1-2d(I)>\varepsilon_y,
\tag{6}
\]

then `(3)` already implies `|x_{\lambda_I}|>\varepsilon_y`; **no overlap bound is needed**. Overlap can only increase the normalized coefficient on this side.

Above half mass, put

\[
g_I:=2d(I)-1>0.
\]

If a nonexceptional mode is Page-cheap, then `(1)` and `(4)` require

\[
|-g_I+4\Omega_I|\le\varepsilon_y,
\]

hence necessarily

\[
\boxed{
B_I\ge\Omega_I\ge\frac{g_I-\varepsilon_y}{4}
}
\tag{7}
\]

whenever `g_I>\varepsilon_y`. Thus an upper-half subset can remain cheap only by carrying enough multi-defect overlap to cancel its negative disjoint-profile bias back into the Page window.

## 3. Equal marginal defects: a stable version of the MC-296 endpoint

Assume now only the equal marginal condition

\[
d_1=\cdots=d_R=\frac1R,
\tag{8}
\]

without assuming that the `D_i` partition the shell. Let

\[
B:=\sum_{1\le a<b\le R}\frac{|D_a\cap D_b|}{N}.
\tag{9}
\]

Then `B_I\le B` for every subset `I`. For `j=|I|`, the disjoint-profile gap is

\[
g_j:=\left|1-\frac{2j}{R}\right|.
\]

Every lower-half mode `j<R/2` with `g_j>\varepsilon_y` is Page-expensive except possibly `\lambda_*`, independently of overlap. Every upper-half mode `j>R/2` is Page-expensive whenever

\[
g_j>\varepsilon_y+4B.
\tag{10}
\]

Consequently:

- if `R` is odd and `\varepsilon_y+4B<1/R`, every nonzero subset mode is Page-expensive except possibly the unique Page exception;
- if `R` is even and `\varepsilon_y+4B<2/R`, every nonzero subset mode outside the middle layer `j=R/2` is Page-expensive except possibly the unique Page exception.

These recover the sharp `MC-296` conclusions when `B=0`, while quantifying exactly how much pair overlap they tolerate.

There is also a layer-average statement that remains useful when the uniform bound `(10)` fails. For fixed `j\ge2`,

\[
\sum_{|I|=j}B_I
=\binom{R-2}{j-2}B,
\tag{11}
\]

because each pair `{a,b}` occurs in exactly `\binom{R-2}{j-2}` subsets of size `j`.

For an upper layer `j>R/2` with

\[
g_j:=\frac{2j}{R}-1>\varepsilon_y,
\]

every nonexceptional Page-cheap subset must satisfy `(7)`. Therefore the number `L_j` of nonexceptional Page-cheap subsets on that layer obeys

\[
\boxed{
L_j
\le
\frac{4\binom{R-2}{j-2}B}{g_j-\varepsilon_y}.
}
\tag{12}
\]

Equivalently, as a fraction of the layer,

\[
\boxed{
\frac{L_j}{\binom Rj}
\le
\frac{4j(j-1)}{R(R-1)}
\frac{B}{g_j-\varepsilon_y}.
}
\tag{13}
\]

At most one further subset over the entire selected span can be the Page-exceptional mode. Thus even when total overlap is too large for uniform exclusion, a sufficiently small aggregate pair-overlap budget still forces most upper-layer modes above the Page source-cost threshold.

## 4. Prior art and novelty boundary

The arithmetic input remains the classical Landau–Page/nonexceptional real-character estimate already audited in `MC-293`; no new exceptional-zero theorem is used.

The finite harmonic identity is ordinary Walsh-character parity bookkeeping on the Boolean cube. The background language is standard; see, for example, Ryan O'Donnell, *Analysis of Boolean Functions*, Cambridge University Press, 2014 (revised arXiv edition `2105.10386`). The inequality `\Omega_I\le B_I` is an elementary pair-intersection/Bonferroni-type bound, not a new combinatorial principle.

A targeted search on 14 September 2026 for combinations of Landau–Page character bounds, Legendre-symbol shell defect overlaps, and Boolean/Walsh parity did not surface a source stating the Mathia-specific composition `(1)`–`(13)`. **No standalone novelty claim is made.** The durable content is the exact correction and its consequence for the already-defined Page source-cost obstruction.

## Boundaries and falsification tests

- **This corrects one boundary statement in MC-296, not its theorem.** `MC-296` assumes an exact partition, so all of its displayed conclusions remain valid. What is superseded is only the claim that shell coverage itself is necessary for formula `(10)`; pairwise disjointness is enough.
- **Pair overlap is only an upper control.** `B_I` bounds `\Omega_I`; it does not determine it. Large pair overlap need not produce the parity cancellation needed for a cheap upper-half mode.
- **Equal marginal defects do not imply endpoint saturation.** Under `(8)`, `\sum_i d_i=1`, but overlaps may coexist with a positive common preferred-sign region. The present formulas account for that through `\Omega_I`.
- **Independence remains load-bearing.** Without linear independence, many subsets may represent the same functional, and the single Page exception can account for multiple subset labels.
- **No arithmetic overlap estimate is proved.** Nothing here shows that an actual Legendre shell has `B=o(1/R)` or any comparable bound. Establishing arithmetic control of pair/multi-defect overlap is now a concrete next gate.
- **Source cost is not quotient dimension.** Forcing many subset modes above `D_y` still does not prove that their high-cost realizations consume many independent source coordinates.
- **No Möbius or RH estimate follows.** The result is a structural restriction inside the localized Legendre-shell program and does not imply a bound for `M(x)` or move a zero-free boundary.

## Consequence for the research line

The approximate-partition question left open after `MC-296` has a clean answer at the finite-harmonic level. **Unused common preferred mass is harmless; overlapping defects are the only obstruction to the exact endpoint Fourier profile, and their effect is explicitly measurable.** This narrows the next arithmetic target from a vague stability problem to a quantitative one: control the pair-overlap budget, or more sharply the parity-folding quantities `\Omega_I`, for the Legendre-shell defect family.

The lower half of the subset spectrum is particularly rigid because overlap cannot rescue it at all. The upper half can remain Page-cheap only by spending overlap according to `(7)`, and `(11)`–`(13)` convert a global overlap budget into a multiplicity restriction. A further advance now requires arithmetic information about these overlaps or an independent source-side theorem limiting how many high-source-cost subset modes can coexist; additional generic entropy or coding bounds do not address that gate.