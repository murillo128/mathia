# WI-379 — Inherited arithmetic translations defeat source-rank elimination

**Status:** `EXACT-DERIVED + PRIMARY-SOURCE-OPERATOR-AUDIT + SOURCE-CONDITIONED-ROUTE-SEPARATION + DECISIVE-NEGATIVE + PRIOR-ART-AUDITED + NON-ESTABLISHED-RH`.

## Claim

WI-378 proved that a source-only positive-pivot Schur coupling cannot repair the fixed-depth gamma-negative band on the old source-zero sector. That result deliberately left open a direct old--old arithmetic term. The exact localized operator in Marco Desogus's *The Three Gates: A Rooted-Operator Approach to Weil Positivity* shows that this surviving channel is structurally different from a sparse source correction: every already-active prime-power branch is a partial translation on the whole old interval, and those branches persist exactly under zero-extension compression.

For a single normalized shift `0<r<2`, define on `L^2(-1,1)`

\[
(S_rf)(x)=\mathbf 1_{(-1,1)}(x+r)f(x+r),
\qquad
T_r:=S_r+S_r^*.
\tag{1}
\]

Then `S_r` has infinite rank, and `T_r` has infinite-dimensional positive and negative quadratic-form subspaces. More strongly, for every sufficiently small positive-measure interval `E\subset(-1,1-r)` with `E` and `E+r` disjoint, the compression of `T_r` to

\[
\mathcal H_E=L^2(E)\oplus L^2(E+r)
\tag{2}
\]

is unitarily equivalent to

\[
\boxed{
\begin{pmatrix}0&U\\ U^*&0\end{pmatrix},
}
\tag{3}
\]

where `U` is translation from one copy of `L^2(E)` to the other. Hence the vectors `(h,\pm U^*h)` give respectively the two signs, with an infinite-dimensional choice of `h`. For the odd channel the same conclusion follows by odd extension of the two-cell construction once the cells and their reflections are chosen disjoint; for any fixed prime-power branch this is possible at all sufficiently large support radii because its normalized shift tends to zero.

Consequently an inherited arithmetic translation branch is **not** a finite-rank or current-source-rank correction. In particular, the source-rank obstruction of WI-378 cannot be extended to eliminate the inherited arithmetic channel merely by counting current source variables or by observing that a Schur coupling factors through the current-source map. The remaining question is spectral/coercive: whether the signed sum of inherited arithmetic translations supplies enough positive old--old energy on the actual source-zero gamma-negative band.

This does not show that it does. Each individual self-adjoint branch is itself indefinite, and the exact arithmetic operator carries the signed coefficient `-\Lambda(n)/\sqrt n`. Infinite rank is therefore only a route-separation fact, not a positivity estimate.

## 1. Primary-source operator and persistence

Desogus's exact normalized localized form writes the arithmetic part as

\[
-\sum_{2\le n<e^{2a}}
\frac{\Lambda(n)}{\sqrt n}
\bigl(S_{r_n}+S_{r_n}^*\bigr),
\qquad
r_n=\frac{\log n}{a}.
\tag{4}
\]

The source defines `S_r` exactly as in (1). In physical logarithmic coordinates this is translation by the fixed length `\log n`; the normalization to `(-1,1)` divides that length by `a`. This is the exact old-space arithmetic term, not a finite matrix surrogate or a source short.

The same preprint proves the zero-extension compression identity for the full localized form. Its arithmetic part has a particularly simple interpretation: if a prime-power branch is already active at the smaller radius `a`, its old--old action is unchanged at a larger radius `b`; a newly activated branch whose translation length exceeds the old diameter has zero old--old overlap. Thus already-active translations are inherited literally in the old sector rather than recreated through the new current-source variables.

These two primary-source statements are the only Desogus-specific inputs used below. No positivity theorem from that preprint is assumed, and in particular its claimed RH conclusion is not used as evidence.

## 2. Exact two-cell lemma

Choose an interval `E` of positive length so small that

\[
E,\quad E+r,\quad E-r,\quad E+2r
\tag{5}
\]

have no unwanted overlap inside the support; such an `E` exists whenever `0<r<2` after placing it in an overlap region of the translation and shrinking it if necessary. Let `P_E` be the orthogonal projection onto `\mathcal H_E` in (2).

Translation by `r` is a unitary identification between `L^2(E+r)` and `L^2(E)`. Calling that identification `U`, direct substitution in (1) gives

\[
P_ET_rP_E
=
\begin{pmatrix}0&U\\ U^*&0\end{pmatrix}.
\tag{6}
\]

Therefore

\[
\left\langle
(h,\pm U^*h),
P_ET_rP_E(h,\pm U^*h)
\right\rangle
=
\pm 2\|h\|_2^2.
\tag{7}
\]

Because `L^2(E)` is infinite-dimensional, both signs occur on infinite-dimensional subspaces. Equation (6) also implies immediately that `S_r` has infinite rank. Multiplication by the nonzero arithmetic coefficient in (4) only exchanges the two signs; it cannot turn the branch into a finite-rank perturbation.

The odd compression does not change this rank conclusion. For fixed `r<1` choose the cells in the positive half sufficiently far from the origin and boundary that their reflected copies are disjoint. Odd extension is then an isometric identification, up to the fixed normalization factor, of the two-cell space with an odd two-cell pair, and `T_r` commutes with reflection parity. Hence the odd restriction retains infinite-dimensional subspaces of both signs. For any fixed `n`, `r_n=(\log n)/a<1` once `a` is large.

## 3. The source-zero constraint does not convert inherited translations into sparse corrections

WI-377 identifies the true current-source set in physical logarithmic coordinates as

\[
S_k=
\bigcup_{\substack{2\le n\le k\\ \Lambda(n)>0}}
[\log k-\log n,\,\log(k+1)-\log n),
\tag{8}
\]

and proves that on every fixed fractional interior its total length tends to zero. The source-zero sector is

\[
Z_k=\{F:F=0\ \text{a.e. on }S_k\}.
\tag{9}
\]

Fix one inherited prime-power translation, for example any fixed `n_0` with `\Lambda(n_0)>0`, and write its physical shift as `\theta=\log n_0`. For all sufficiently large `k`, take a fixed fractional interior whose length tends to infinity. By WI-377 the union of the source slots there, together with its translate by `\pm\theta`, has vanishing total measure. Since for each fixed `k` it is a finite union of intervals, one can choose a positive-length cell `E_k` in the interior such that

\[
E_k\cup(E_k+\theta)
\subset S_k^c.
\tag{10}
\]

Shrinking the cell also enforces the disjointness needed for the two-cell lemma. Therefore the arithmetic branch has an infinite-dimensional two-sign compression **inside the old source-zero space** `Z_k` for every sufficiently large `k`.

This is stronger than saying only that the ambient operator has infinite rank. It rules out the specific dimensional shortcut in which inherited arithmetic is treated as if it were limited by the number/rank of the current source observations. The current source holes can annihilate a source-mediated coupling `C_kR_k` on `Z_k`, as in WI-378, but they do not annihilate an already-active translation acting between two old source-free cells.

There is no contradiction with WI-377's additive-repair tariff. An indefinite infinite-rank operator can have enough available rank while still failing the required lower bound. The point here is only that **rank scarcity is no longer the obstruction** for the inherited arithmetic term.

## 4. What route is closed, and what remains load-bearing

The following proposed no-go is now closed:

> Extend WI-378 by arguing that every arithmetic correction is mediated by the sparse/current source map, so its effective old-space rank is too small to repair the `\Omega(A_k)` gamma-negative sector.

That inference is false for the exact inherited branches. Equations (4), (6), and the zero-extension persistence show an old--old channel of infinite rank that survives independently of the current source short. Any decisive obstruction must therefore use more than rank or source dimension.

The surviving quantitative question is sharper. Let

\[
P_k^{\rm ar}
=-\sum_{n\ \mathrm{already\ active}}
\frac{\Lambda(n)}{\sqrt n}
\bigl(S_{r_{n,k}}+S_{r_{n,k}}^*\bigr)
\tag{11}
\]

be the inherited direct old--old arithmetic operator in the relevant normalization. WI-378 says a successful corrected form must supply, on the WI-377 depth-`\eta` spaces, at least `\eta` of old-sector coercivity before a source-only Schur channel can matter. WI-379 does not prove

\[
P_k^{\rm ar}\succeq \eta I
\quad\text{on those spaces};
\tag{12}
\]

indeed each summand has both signs. The next load-bearing audit is therefore a **restricted spectral estimate** for the signed translation sum on the actual digamma-negative/source-zero band, or an exact domain relation that removes those trial vectors. Symbol heuristics or ambient infinite rank are insufficient.

This also separates two arithmetic populations cleanly. Newly activated branches may have no old--old overlap and can enter through the new collar/source geometry. Already-active branches persist as direct old--old translations. A repair analysis that combines those populations into a single sparse source rank loses precisely the distinction relevant after WI-378.

## 5. Provenance, novelty audit, and falsification

The exact partial-translation formula (4) and old--old zero-extension persistence are from Marco Desogus, *The Three Gates: A Rooted-Operator Approach to Weil Positivity*, arXiv:2609.20367v1 (17 September 2026), especially the exact normalized localized form and zero-extension compression discussion. `S_r` as a truncated/zero-extension translation is standard operator theory; the two-cell flip compression (6) is an elementary exact deduction and no novelty is claimed for it.

A fresh primary-source audit on 21 September 2026 checked the public arXiv version directly. The literature-backed content used here is only the explicit operator representation and nesting identity. The new Mathia content is the consequence for the WI-378/WI-377 obstruction: inherited arithmetic cannot be discarded by **source-rank counting**, because an already-active branch has an extensive old-space action even on source-zero vectors. Search absence is not evidence of priority, and no priority claim is made.

The finding would be falsified if the exact corrected admissible category used in the proposed proof imposed an additional relation that excludes the two-cell source-zero vectors before the old--old arithmetic form is evaluated, or if the inherited term relevant to that category were not the partial-translation compression in (4). Neither follows from the current exact localized form. Conversely, proving that the signed sum in (11) is spectrally too weak or has the wrong sign on the WI-377 band would strengthen this finding into a genuine arithmetic no-go; that spectral estimate is not supplied here.

## Research consequence

WI-378 correctly forces any repair to act directly on the old source-zero sector, but **it cannot be upgraded to a rank-level elimination of the inherited arithmetic channel**. The exact arithmetic branches have enough operator-theoretic rank; what is unknown is their sign and coercivity on the certified gamma-negative modes. The next efficient test is therefore not another source-count argument. It is to compress the inherited signed translation operator to the WI-377 low-frequency/source-zero band and determine whether its lower spectral edge can meet the fixed-depth tariff required by WI-378. This is a route redirection, not evidence for or against RH.
