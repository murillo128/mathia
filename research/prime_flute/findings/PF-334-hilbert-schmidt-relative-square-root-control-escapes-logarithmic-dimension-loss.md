# PF-334 — Hilbert–Schmidt relative square-root control escapes logarithmic dimension loss

**Status:** `EXACT-DERIVED + HILBERT-SCHMIDT-RELATIVE-SQUARE-ROOT + DIMENSION-FREE + ROUTE-SHARPENING`.

PF-333 shows that the relative square-root map can have a worst-case `log r` first-order constant in operator norm even for positive semidefinite normalized perturbations on an `r`-dimensional section. That generic obstruction is real, but it is specific to the operator-norm endpoint. The direct-angle route does not ultimately require operator norm: PF-318 shows that the weak-`S_1` endpoint is already closed by a Hilbert–Schmidt average on the logarithmic-rank local low band.

At exactly that `S_2` level, the relative square-root map has no dimension loss at all.

Let `Q>0`, let `E=E^*`, and define the first relative square-root derivative

\[
\mathcal R_Q(E)
:=
\left.\frac{d}{d\eta}\right|_{\eta=0}
\left(Q+\eta Q^{1/2}EQ^{1/2}\right)^{1/2}Q^{-1/2}.
\]

Then on every finite section

\[
\boxed{
\|\mathcal R_Q(E)\|_{\mathcal S_2}
\le 2^{-1/2}\|E\|_{\mathcal S_2}.
}
\tag{1}
\]

The constant is independent of the section dimension and of the condition number of `Q`. For arbitrary, not necessarily self-adjoint `E`, the same calculation gives the slightly weaker dimension-free bound

\[
\boxed{
\|\mathcal R_Q(E)\|_{\mathcal S_2}
\le \|E\|_{\mathcal S_2}.
}
\tag{2}
\]

More importantly, the `S_2` control persists nonlinearly for the positive pant insertion used by PF-332. Put

\[
A_\eta=Q+\eta\Lambda,
\qquad
K=Q^{-1/2}\Lambda Q^{-1/2}\ge0,
\qquad
F_\eta=A_\eta^{1/2}Q^{-1/2},
\]

with `0\le\eta\le1`. Then `F_0=I` and `G:=F_1-I` is the PF-332 relative completed square-root defect. One has

\[
\boxed{
\|G\|_{\mathcal S_2}
\le C_2(\|K\|)\,\|K\|_{\mathcal S_2},
}
\tag{3}
\]

where

\[
C_2(k)
=
\frac1{\sqrt2}\int_0^1\sqrt{1+\eta k}\,d\eta
=
\frac{\sqrt2}{3k}\bigl((1+k)^{3/2}-1\bigr)
\quad(k>0),
\]

and `C_2(0)=2^{-1/2}`. Consequently, on any family for which the normalized positive insertion `K` has a uniform operator-norm bound, the full nonlinear relative square-root step preserves Hilbert–Schmidt scale with a constant independent of retained rank and seam conditioning.

This does **not** prove the Prime-Flute locality estimate. It isolates a sharper fact: PF-333's generic logarithmic obstruction does not force an additional logarithmic loss in the `S_2` currency actually used by PF-318. Any remaining logarithmic-rank cost must enter through the pant/core insertion, its localization, or the geometry of the chosen low/high blocks—not merely through taking the relative square root.

## 1. The first relative derivative is a Schur multiplier with an `S_2` contraction bound

Diagonalize

\[
Q=S^2,
\qquad
S=\operatorname{diag}(s_1,\dots,s_r),
\qquad s_i>0.
\]

If

\[
X
=
\left.\frac{d}{d\eta}\right|_{\eta=0}
\left(Q+\eta SES\right)^{1/2},
\]

then differentiating the square identity gives the Sylvester equation

\[
SX+XS=SES.
\tag{4}
\]

Hence

\[
X_{ij}=\frac{s_is_j}{s_i+s_j}E_{ij},
\]

and right multiplication by `S^{-1}` gives the exact entrywise formula

\[
\boxed{
(\mathcal R_Q(E))_{ij}
=\frac{s_i}{s_i+s_j}E_{ij}.
}
\tag{5}
\]

For arbitrary `E`, every multiplier in (5) lies in `(0,1)`, so summing entry squares proves (2).

If `E=E^*`, pair the `(i,j)` and `(j,i)` entries. For `i<j`, their output contribution is

\[
\frac{s_i^2+s_j^2}{(s_i+s_j)^2}|E_{ij}|^2
\le |E_{ij}|^2,
\tag{6}
\]

whereas their input contribution is `2|E_{ij}|^2`. On the diagonal the multiplier is exactly `1/2`, so the squared output contribution is `|E_{ii}|^2/4`. Therefore

\[
\|\mathcal R_Q(E)\|_{\mathcal S_2}^2
\le\frac12\|E\|_{\mathcal S_2}^2,
\]

which proves (1).

The contrast with PF-333 is structural. The same Schur multiplier can have operator norm of order `log r` as a map on matrices equipped with spectral norm, while its action on Hilbert–Schmidt space is controlled directly by its entrywise coefficients. The retained dimension never enters (1).

## 2. Positive insertions give a nonlinear dimension-free `S_2` bound

Differentiate `F_\eta=A_\eta^{1/2}Q^{-1/2}`. Let

\[
X_\eta=\frac{d}{d\eta}A_\eta^{1/2}.
\]

Then

\[
A_\eta^{1/2}X_\eta+X_\eta A_\eta^{1/2}=\Lambda.
\tag{7}
\]

Define the relative perturbation seen at parameter `\eta` by

\[
E_\eta
:=A_\eta^{-1/2}\Lambda A_\eta^{-1/2}.
\tag{8}
\]

It is positive semidefinite. Since

\[
\Lambda=Q^{1/2}KQ^{1/2},
\]

we can write

\[
E_\eta=C_\eta K C_\eta^*,
\qquad
C_\eta=A_\eta^{-1/2}Q^{1/2}.
\tag{9}
\]

Because `A_\eta\ge Q`,

\[
C_\eta C_\eta^*
=A_\eta^{-1/2}QA_\eta^{-1/2}
\le I,
\]

so `\|C_\eta\|\le1` and therefore

\[
\boxed{
\|E_\eta\|_{\mathcal S_2}
\le\|K\|_{\mathcal S_2}.
}
\tag{10}
\]

Equation (7) says precisely that

\[
X_\eta A_\eta^{-1/2}
=\mathcal R_{A_\eta}(E_\eta).
\]

Thus

\[
F_\eta'
=\mathcal R_{A_\eta}(E_\eta)F_\eta.
\tag{11}
\]

The positive normalization also gives the exact identity

\[
F_\eta^*F_\eta
=Q^{-1/2}A_\eta Q^{-1/2}
=I+\eta K,
\]

hence

\[
\|F_\eta\|=\sqrt{1+\eta\|K\|}.
\tag{12}
\]

Combining (1), (10), (11), and (12),

\[
\|F_\eta'\|_{\mathcal S_2}
\le
\frac1{\sqrt2}
\|K\|_{\mathcal S_2}
\sqrt{1+\eta\|K\|}.
\tag{13}
\]

Integrating from `0` to `1` proves (3).

No eigenvalue lower bound for `Q` appears. The singular seam scale is already absorbed into the normalized insertion `K`; the square-root homotopy itself does not reintroduce a condition-number or dimension penalty at the Hilbert–Schmidt level.

## 3. Consequence for the PF-318/PF-332 endpoint

PF-318 requires local low/high blocks whose squared Hilbert–Schmidt mass is at reciprocal-prime scale times the logarithmic low-band rank. PF-333 warns that replacing this by a generic operator-norm perturbation theorem can cost `log r`. Equations (1)--(3) show that this warning should not be transferred automatically to the `S_2` route.

In particular, on any finite local section with a uniform bound `\|K\|\le M`, every compression of the completed relative defect obeys

\[
\boxed{
\|RGP\|_{\mathcal S_2}
\le C_2(M)\|K\|_{\mathcal S_2}
}
\tag{14}
\]

for orthogonal projections `P,R`. Thus a reciprocal-prime Hilbert–Schmidt estimate for the relevant normalized pant insertion is not degraded by the nonlinear relative square-root operation merely because the retained rank grows like `\log P_n`.

Equation (14) is intentionally only a route-sharpening statement. The actual PF-318 block is an energy-normalized low/high pant-crossing operator, not automatically the whole normalized positive insertion `K` appearing here. One still has to place the appropriate local compression inside the exact PF-317/PF-318 factorization, or prove a localized/off-diagonal version of the PF-332 resolvent formula. The point is narrower: **dimension growth by itself is no longer a valid reason to expect an extra logarithmic square-root loss in `S_2`.**

The obstruction branch also remains live. A bounded full `S_2` norm says nothing by itself about fixed-window packet concentration; a Hilbert–Schmidt-small average can coexist with exceptional directions, and a large full `\|K\|_{\mathcal S_2}` makes (3) useless. PF-328's positive-measure packet family and PF-332's resolvent-dressed translation/cutoff defects still decide whether the completed low normalization is sufficiently local.

## Prior-art and novelty audit

The abstract matrix-perturbation setting is classical. Roy Mathias, *A Bound for the Matrix Square Root with Application to Eigenvector Perturbation*, SIAM J. Matrix Anal. Appl. 18(4) (1997), 861--867, DOI `10.1137/S5089547989529577`, proves the logarithmic worst-case first-order constant in spectral norm used by PF-333. Ren-Cang Li, *Relative Perturbation Bounds for Positive Polar Factors of Graded Matrices*, SIAM J. Matrix Anal. Appl. 27(2) (2005), 424--433, DOI `10.1137/S0895479803437153`, treats scaled positive-polar differences for strongly graded matrices and explicitly extends that framework to square roots; Li also records classical Frobenius-norm stability of positive polar factors due to Kittaneh.

Accordingly, **no new general matrix square-root or polar-perturbation theorem is claimed here**. Equations (1)--(3) are a self-contained finite-dimensional derivation specialized to the exact normalized variable used in PF-332. Their project-specific value is the endpoint comparison: the generic logarithmic `S_\infty` obstruction isolated by PF-333 disappears in the `S_2` currency that PF-318 already proved sufficient for weak trace class. No quantitative theorem from Mathias or Li is imported into the proof of (1)--(3).

## Boundaries and adversarial checks

1. **No Prime-Flute Hilbert–Schmidt estimate is proved.** The theorem transfers an `S_2` bound from the normalized insertion `K`; it does not establish the required bound for the actual pant/core DtN block.
2. **A uniform operator-norm envelope for `K` is still needed for the nonlinear constant in (3).** If `\|K\|` grows, `C_2(\|K\|)` grows like a square root; the theorem does not make arbitrary positive insertions uniformly tame.
3. **Global `S_2` control is not locality.** Equation (14) is a compression bound, not spatial off-diagonal decay or a cutoff/translation commutator estimate. PF-332's locality problem remains separate.
4. **The PF-318 block identification remains to be proved.** One must not silently identify its low/high cross block with the whole `K` used here.
5. **The result is finite-section exact.** Infinite-boundary passage still requires the compatible limiting control already left open in PF-329--PF-333.
6. **No completed-angle lower or upper endpoint is closed.** PF-318's local Hilbert–Schmidt target and PF-328's positive-measure packet obstruction remain the two relevant directions.
7. **No determinant, scattering, zeta-zero, critical-line, or RH consequence follows.**

## Consequence for the research line

The next direct-angle estimate should be formulated in Hilbert–Schmidt terms before paying for operator norm. PF-333 rules out a dimension-free proof based only on positivity when the target norm is `S_\infty`; PF-334 shows that the relative square-root step itself is dimension-free in `S_2` and even admits the nonlinear bound (3) under a uniform normalized insertion envelope. Therefore the useful remaining question is whether the actual one-cusp-pant/core DtN insertion has the **localized reciprocal-prime `S_2` mass** needed by PF-318, or whether the PF-328 critical packets force a positive-measure lower obstruction after the resolvent-dressed transfer of PF-332. The square root no longer supplies an independent logarithmic-rank penalty at the averaged endpoint.