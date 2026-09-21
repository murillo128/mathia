# WI-378 — Pure Schur coupling cannot repair the source-zero gamma band

**Status:** `EXACT-DERIVED + CLASSICAL-LINEAR-ALGEBRA + SOURCE-CONDITIONED-SCHUR-NOGO + QUANTITATIVE-NEGATIVE-INDEX + DECISIVE-REPAIR-BARRIER + PRIMARY-SOURCE-CRITICAL-AUDIT + PRIOR-ART-AUDITED + NON-ESTABLISHED-RH`.

## Claim

WI-375 left open a genuinely source-conditioned old--new Schur coupling as a possible way to transport fresh endpoint reserve into the inherited gamma-negative bulk. WI-376--WI-377 then showed that, even after imposing the true arithmetic source-zero constraints, the corrected archimedean block retains a full fixed-depth negative-index profile. Combining those facts with elementary Hermitian block geometry closes the **coupling-only** version of that escape.

Write

\[
L_k=\log(k+1),
\qquad
\mathcal A_k:=\mathcal A_{L_k},
\]

for the corrected archimedean form from WI-369, and let `R_k` denote the current-source observation map, normalized only so that

\[
Z_k:=\ker R_k
=\{F:F=0\ \text{a.e. on }S_k\}.
\tag{1}
\]

For `0\le \eta<C_\Gamma`, WI-377 supplies subspaces `V_{\eta,k}\subset Z_k` with

\[
\mathcal A_k[F]\le-\eta\|F\|_2^2
\qquad(F\in V_{\eta,k})
\tag{2}
\]

and

\[
\liminf_{k\to\infty}
\frac{\dim V_{\eta,k}}{L_k}
\ge \frac{q_\eta}{\pi}.
\tag{3}
\]

Consider an enlarged Hermitian quadratic form on old variables `F` and new/source variables `u` of the schematic exact block form

\[
\mathcal Q_k(F,u)
=
\mathcal A_k[F]+\mathcal P_k[F]
+2\operatorname{Re}\langle B_kF,u\rangle
+\mathcal D_k[u].
\tag{4}
\]

Here `\mathcal P_k` is the **direct old-space repair** already present before eliminating `u`; all off-diagonal old--new effects are in `B_k`. Assume the exact repaired domain contains `V_{\eta,k}\times\{0\}`. Then positivity of the enlarged form forces

\[
\boxed{
\mathcal P_k[F]\ge \eta\|F\|_2^2
\qquad(F\in V_{\eta,k}).
}
\tag{5}
\]

Indeed, set `u=0` in (4). No strength of the coupling `B_k`, no size of a positive pivot `\mathcal D_k`, and no later same-vector response identity can contribute on that principal subspace. In particular, if `\mathcal P_k=0`, then

\[
\boxed{
\operatorname{ind}_{\le-\eta}(\mathcal Q_k)
\ge \dim V_{\eta,k},
}
\tag{6}
\]

in the variational sense: `V_{\eta,k}\times\{0\}` itself is a depth-`\eta` negative subspace.

There is a stronger statement for the specific **source-mediated positive-pivot Schur** mechanism. Suppose

\[
B_k=C_kR_k,
\tag{7}
\]

and `\mathcal D_k` is represented by a strictly positive Hermitian pivot `D_k`. Completing the square gives the short in the new variables,

\[
\mathcal Q_k^{\rm short}[F]
=
\mathcal A_k[F]+\mathcal P_k[F]
-\langle D_k^{-1}B_kF,B_kF\rangle.
\tag{8}
\]

The Schur correction is negative semidefinite, and (1), (7) imply the exact identity

\[
\boxed{
\mathcal Q_k^{\rm short}[F]
=
\mathcal A_k[F]+\mathcal P_k[F]
\qquad(F\in Z_k).
}
\tag{9}
\]

Thus a source-only positive-pivot Schur channel gets **exactly zero credit** toward repairing the WI-377 negative band. Any successful corrected proof must already place enough positive old-space coercivity into `\mathcal P_k` on the source-zero complement before that source short, or else use a genuinely different admissible category in which the WI-377 vectors are not available as `(F,0)`.

## 1. Quantitative budget separation

Equation (5) does more than rule out finite-rank coupling tricks. On every WI-377 depth subspace, the direct old-space repair itself must dominate the missing gamma energy.

If `\mathcal P_k` is represented on the relevant finite-dimensional compression by a self-adjoint operator `P_k`, min--max applied to (5) gives

\[
N^{\ge}_{P_k}(\eta)
\ge \dim V_{\eta,k},
\tag{10}
\]

where `N^{\ge}_{P_k}(\eta)` counts eigenvalues at least `\eta`. Therefore

\[
\boxed{
\liminf_{k\to\infty}
\frac{N^{\ge}_{P_k}(\eta)}{L_k}
\ge \frac{q_\eta}{\pi}
\qquad(0<\eta<C_\Gamma).
}
\tag{11}
\]

At depth zero one retains the rank consequence

\[
\boxed{
\liminf_{k\to\infty}
\frac{\operatorname{rank}_+(P_k)}{L_k}
\ge \frac{q_0}{\pi}
=2.0021169777\ldots
}
\tag{12}
\]

under the same positivity premise. Equation (12) is obtained from (11), not from the semidefinite `\eta=0` inequality alone: for every fixed `\eta>0`, `\operatorname{rank}_+(P_k)\ge N^{\ge}_{P_k}(\eta)`, and then `\eta\downarrow0` gives `q_\eta\to q_0`. These are the same spectral tariffs that WI-377 placed on a generic additive repair, but now the budget is **partitioned**: an off-diagonal source Schur channel cannot be counted toward them. The entire tariff must be carried by a term that acts directly on the old source-zero sector before elimination (or by an exact domain constraint that removes that sector).

For the common situation in which one only wants positivity of the short rather than of the full block, (9) yields the identical conclusion. A stronger positive source pivot cannot help: it only shrinks the magnitude of the negative Schur debit away from `Z_k`, while the debit remains identically zero on `Z_k`.

## 2. What this changes in the Desogus repair audit

The printed Gate-II chain in Marco Desogus's *The Three Gates: A Rooted-Operator Approach to Weil Positivity* uses common-complement shorting, a positive inherited pivot, and a same-vector Schur response. WI-375 showed that the printed positive metric is downstream of the invalid gamma-free collar, but deliberately left open the possibility that a corrected source-conditioned old--new coupling could transport fresh endpoint reserve into the inherited gamma-negative modes.

The present finding removes one important interpretation of that possibility. **Cross coupling by itself cannot turn a negative old principal sector into a positive block**, and a positive-pivot Schur elimination cannot do so either. If the coupling factors through the current source data, it is additionally invisible on the exact source-zero sector where WI-377 constructs linearly many negative directions.

Consequently the next load-bearing audit target is not the size of the later response coupling or the positivity margin of the source pivot. It is the corrected **old--old term before the source short**. A viable Gate-II repair has to identify an inherited/global/arithmetic contribution `\mathcal P_k` that is already coercive on `Z_k` with at least the profile (11), or prove that the exact full admissible domain excludes the WI-377 vectors. Merely strengthening `B_k`, `D_k`, or the later same-vector identity does not address the obstruction.

This is intentionally not a refutation of Desogus's full rooted network. The inherited parent form, polar channel, or another global term could contribute directly to `\mathcal P_k`; the present argument does not estimate those terms. It also does not claim that every non-additive elimination factors through `R_k`. It rules out the narrower but natural mechanism in which the missing coercivity is supposed to be created **only** by adding source variables and coupling them to an unchanged old gamma-negative block.

## 3. Exact linear-algebra provenance

The principal-subspace step (5)--(6) is elementary: a nonnegative Hermitian form is nonnegative on every admissible subspace. The Schur identity (8) follows by completing the square. In finite dimensions it is the standard Schur-complement/Haynsworth setting; see E. V. Haynsworth, *Determination of the inertia of a partitioned Hermitian matrix*, Linear Algebra Appl. **1** (1968), 73--81, DOI `10.1016/0024-3795(68)90050-5`. Haynsworth's theorem is prior art for the block-inertia algebra, not a source of any zeta-specific claim here.

The quantitative input (2)--(3) is internal and exact: WI-377 proves it from the corrected gamma form, the exact digamma dispersion, and the true prime-power source-slot geometry. WI-375 supplies the audit context in which a corrected source-conditioned Schur mechanism remained a live repair possibility. No new arithmetic theorem, numerical certificate, zero-density estimate, or RH-dependent statement is used.

A fresh web audit on 21 September 2026 rechecked `arXiv:2609.20367`; the public record remained the 17 September 2026 preprint, and no public correction supplying a gamma-retaining common-cut theorem was located. Search absence is not evidence of priority. No novelty is claimed for the linear algebra; the new research content is the application of the WI-377 source-perforated fixed-depth index profile to separate the direct old-space repair budget from source-mediated Schur coupling.

## 4. Falsification and boundary

This barrier is falsified as a description of a proposed repair if one can exhibit, in the **corrected exact** localized form, either of the following before invoking the source short:

1. a direct old-space term `\mathcal P_k` whose restriction to the WI-377 source-zero band supplies the required fixed-depth coercivity (quantitatively, at least the profile (11)); or
2. an exact admissibility relation showing that the WI-377 vectors do not embed as `(F,0)` in the enlarged form even when `R_kF=0`.

A larger positive pivot, a stronger off-diagonal source coupling, or a sharper evaluation of the same Schur response does not falsify the result while the old source-zero vectors remain admissible, because (5) and (9) are identities on that sector.

## Research consequence

The source-facing repair problem has become more specific. WI-375's surviving phrase “genuinely source-conditioned old--new coupling” is too broad: **coupling is not itself a source of positive old-sector coercivity**. The viable mechanism must modify the old--old metric on the source-zero complement before elimination, or alter the exact domain/embedding so that the certified gamma-negative band is no longer an admissible principal sector. This is a structural no-go for the coupling-only route, not a proof or disproof of RH.
