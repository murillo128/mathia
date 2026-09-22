# NB-290 — multiplicative dilations contract canonical Nyman Gram pivots

- **Date:** 2026-09-22
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-002, NB-014, NB-016, NB-287, NB-288, NB-289
- **Classification:** `EXACT-DERIVED + CANONICAL-NYMAN-SOURCE + DILATION-SEMIGROUP + GRAM-SCHMIDT-PIVOTS + SCHUR-COMPLEMENT + DIVISIBILITY-CONTRACTION + COMPOSITE-INDEX-DECAY + SOURCE-METRIC-COUPLING + TARGET-RATE-NOT-CLAIMED + PRIOR-ART-AUDITED`

## Claim

`NB-288` and `NB-289` show that bounded sampling Grams, bounded right inverses, and even the exact future Dirichlet zero-sample table do not force a quantitative finite-section rate. An abstract Hilbert model can retain arbitrary lethargy while satisfying all of those constraints. A useful next invariant therefore has to use metric relations among the **actual Nyman source vectors**, not only their sampled values.

Use

\[
g_n(x)=\left\{\frac1{nx}\right\}-\frac1n\left\{\frac1x\right\},
\qquad
V_n:=\operatorname{span}\{g_2,\ldots,g_n\},
\]

with `V_1={0}`, and define the one-step innovation

\[
w_n:=(I-P_{V_{n-1}})g_n,
\qquad
\sigma_n:=\|w_n\|,
\qquad n\ge2.
\tag{1}
\]

Finite independence from `NB-014` gives `sigma_n>0`. For `m>=2`, let

\[
(A_mf)(x)=
\begin{cases}
\sqrt m\,f(mx),&0<x\le1/m,\\
0,&1/m<x<1.
\end{cases}
\tag{2}
\]

The exact Nyman covariance identity is

\[
A_mg_j
=
\sqrt m\left(g_{mj}-\frac1j g_m\right).
\tag{3}
\]

After quotienting by all canonical generators preceding the product index `mn`, one obtains

\[
\boxed{
P_{V_{mn-1}^{\perp}}A_mw_n
=
\sqrt m\,w_{mn}.
}
\tag{4}
\]

Consequently

\[
\boxed{
\sigma_{mn}\le\frac{\sigma_n}{\sqrt m}
\qquad(m,n\ge2).
}
\tag{5}
\]

Equivalently, for

\[
\tau_n:=\sqrt n\,\sigma_n,
\]

one has the divisibility monotonicity

\[
\boxed{n\mid N\quad\Longrightarrow\quad \tau_N\le\tau_n.}
\tag{6}
\]

This is a source-metric restriction absent from the arbitrary-lethargy controls of `NB-288`--`NB-289`. It does **not** yet control normalized first-free samples or the target-aligned Parseval tail of `NB-287`, so it is not by itself a Nyman-distance rate.

## 1. Exact quotient transport

Equation (2) is an isometry because

\[
\|A_mf\|_2^2
=
\int_0^{1/m}m|f(mx)|^2\,dx
=
\int_0^1|f(u)|^2\,du.
\tag{7}
\]

Equation (3) follows directly from the fractional-part definition. On `x<=1/m`, the two `{1/x}` terms cancel and leave `sqrt(m) g_j(mx)`. On `x>1/m`, both `1/(mx)` and `1/(mjx)` lie in `(0,1)`, so the right side of (3) cancels to zero, matching `A_mg_j`.

If `j<n`, equation (3) uses only `g_m` and `g_(mj)`, with

\[
m<mn,
\qquad
mj\le m(n-1)<mn.
\]

Hence

\[
\boxed{A_mV_{n-1}\subseteq V_{mn-1}.}
\tag{8}
\]

Since `w_n=g_n-P_(V_(n-1))g_n`, applying `A_m` gives

\[
A_mw_n
=
\sqrt m\,g_{mn}
-\frac{\sqrt m}{n}g_m
-A_mP_{V_{n-1}}g_n.
\tag{9}
\]

The last two terms belong to `V_(mn-1)`. Projecting onto its orthogonal complement leaves exactly `sqrt(m) w_(mn)`, proving (4). Projection is contractive and `A_m` is isometric, so `sqrt(m) sigma_(mn) <= sigma_n`, which proves (5)--(6).

This differs from `NB-002`. A copied block `A_mV_N` preserves its internal Gram geometry exactly. Here the copied innovation is tested against the **full canonical section** preceding `mn`, which contains many directions outside the copied block. Those extra directions can only absorb more of the innovation.

## 2. Retention coefficients form a multiplicative cocycle

Normalize

\[
\psi_n:=\frac{w_n}{\sigma_n}.
\tag{10}
\]

Equation (4) becomes

\[
P_{V_{mn-1}^{\perp}}A_m\psi_n
=
c_{m,n}\psi_{mn},
\qquad
c_{m,n}:=\frac{\sqrt m\,\sigma_{mn}}{\sigma_n}.
\tag{11}
\]

Thus

\[
0<c_{m,n}\le1,
\qquad
\boxed{\langle A_m\psi_n,\psi_{mn}\rangle=c_{m,n}.}
\tag{12}
\]

The coefficient obeys the exact consistency law

\[
\boxed{c_{km,n}=c_{k,mn}\,c_{m,n}}
\qquad(k,m,n\ge2),
\tag{13}
\]

because

\[
\frac{\sqrt{km}\,\sigma_{kmn}}{\sigma_n}
=
\left(\frac{\sqrt k\,\sigma_{kmn}}{\sigma_{mn}}\right)
\left(\frac{\sqrt m\,\sigma_{mn}}{\sigma_n}\right).
\]

So the fraction of normalized novelty surviving along a multiplicative ray is governed by a scalar cocycle. This is stronger source-metric information than the pointwise future sample table imposed in `NB-289`.

## 3. Schur-complement and composite-index consequences

Let `G_n` be the Gram matrix of `g_2,...,g_n`. Positive definiteness and the block determinant formula give

\[
\boxed{
\sigma_n^2
=
\frac{\det G_n}{\det G_{n-1}},
}
\tag{14}
\]

with `det G_1:=1`. Squaring (5) yields

\[
\boxed{
\frac{\det G_{mn}}{\det G_{mn-1}}
\le
\frac1m
\frac{\det G_n}{\det G_{n-1}}.
}
\tag{15}
\]

Thus a multiplicatively inherited canonical direction contributes at most a `1/m` fraction of its predecessor's one-step Gram volume.

Let `N=mp` be composite with `p` its smallest prime factor. Since `p<=sqrt(N)`,

\[
\sigma_N
\le
\sigma_p\sqrt{\frac pN}.
\tag{16}
\]

Fractional parts are bounded by one, so

\[
|g_p(x)|\le1+\frac1p\le\frac32,
\qquad
\sigma_p\le\|g_p\|\le\frac32.
\]

Therefore

\[
\boxed{
\sigma_N\le\frac32N^{-1/4}
\qquad(N\text{ composite}).
}
\tag{17}
\]

Along multiples of any fixed `n>=2`, the stronger estimate is

\[
\boxed{
\sigma_N
\le
\sigma_n\sqrt{\frac nN}
\ll_nN^{-1/2}
\qquad(n\mid N).
}
\tag{18}
\]

In particular,

\[
\sigma_{p^r}\le\sigma_p p^{-(r-1)/2}.
\tag{19}
\]

This does **not** assert that prime pivots are large. It says only that a composite index has a proper multiplicative predecessor from which its one-step novelty is quantitatively inherited. Prime indices are the only indices `n>=2` for which this particular predecessor mechanism is unavailable.

The result complements `NB-016`: there, multiplication-table overlaps make the quotient range of a whole dilation-enrichment frame sparse. Here, in the ordinary nested canonical ordering, every composite one-step pivot is already metrically dominated by a smaller divisor pivot.

## 4. Relation to the active finite-section obstruction

`NB-289` can prescribe the exact future first-free zero-sample table while retaining arbitrary finite-section lethargy because its abstract construction leaves metric relations among raw generators essentially free. Equations (4)--(6) are precisely a restriction that construction does not encode: canonical Nyman sections cannot assign Gram--Schmidt novelty independently at multiplicatively related indices.

But (5) alone does not bound the target-aware excess of `NB-287`,

\[
\mathfrak A_M
=
\sum_{r\ge M}|\langle h_M,q_{r+1}\rangle|^2.
\tag{20}
\]

The `q_r` there are **normalized** future null-innovations for the first-free sampling problem. A small raw pivot can still have a large normalized sample profile or target correlation; division by `sigma_r` can amplify the quantity the sampler uses. Therefore this finding does not claim decay of `||L psi_n||`, decay of the `q_n`, a rate for `mathfrak A_M`, convergence of `d_N`, or any implication for RH.

The next discriminant should couple the new source metric to the actual sample/target geometry, for example through

\[
\|L_Z\psi_n\|,
\qquad
\langle h_M,q_n\rangle,
\tag{21}
\]

or a weighted combination in which the `sigma_n` contraction survives normalization. A bound depending only on point-sample identities is ruled out by `NB-289`; a bound depending only on `sigma_n` ignores the normalization problem.

## 5. Adversarial review and prior-art audit

The proof uses only the concrete isometry (2), the exact covariance (3), and the one-way inclusion (8); no reducing-subspace assumption is made. Both the transferred old-section term and the `g_m` correction in (9) are placed inside the full preceding section before projection. The normalization direction is checked explicitly: (4) gives `sqrt(m) sigma_(mn) <= sigma_n`, not the reverse. The composite estimate assumes no lower bound on prime pivots, and no target conclusion is imported from raw source geometry.

The result does not resolve `CLUE-visible-semigroup-defect-controls-section-enrichment`, whose missing step is residual-specific visibility and a quantitative target-distance decrement. It supplies a new exact metric restriction on canonical source enrichment, not that missing coupling.

The dilation/semigroup structure itself is classical. Bagchi's 2006 survey, *On Nyman, Beurling and Baez-Duarte's Hilbert space reformulation of the Riemann hypothesis*, treats the Hilbert-space criterion with its semigroup viewpoint; inside this repository, (3) is already used by `NB-002`, `NB-014`, `NB-016`, `NB-039`, and the accepted visible-semigroup clue. No novelty is claimed for (3), projection contraction, or the Schur-complement formula.

A fresh search found Hugh Carvill's 2025 preprint *Beurling Nyman Geometry and Gram Matrix Structure, Ladder Density and Polynomial Decay via Mellin Smoothing* (arXiv:2510.18132), which proves polynomial off-diagonal Gram decay and block compressibility on a multiplicative `2^(-j)3^(-k)` ladder after Mellin smoothing. That is adjacent source-metric structure, but the searched material does not state (4), (5), or the cocycle (13). Werner Ehm's 2024 *On certain Gram matrices and their associated series* studies formulas and decompositions for Nyman--Beurling Gram matrices, again adjacent but not a substitute for the quotient transport above.

The theorem is self-contained from identities already established in the repository. No external result is load-bearing, so `SOURCES.md` is unchanged. No `mind/**` file is updated because the relevance of the contraction to the Ford/Nyman target obstruction still depends on normalized sample coupling.

## Research disposition

Keep as a source-metric advance after `NB-289`. The abstract controls permit arbitrary lethargy because they do not enforce

\[
\boxed{
\sqrt{mn}\,\sigma_{mn}
\le
\sqrt n\,\sigma_n.
}
\]

Canonical one-step novelty is not free along multiplicative rays, and every composite pivot is quantitatively inherited from a smaller divisor. The next useful pass should test whether the actual first-free sample/target coupling neutralizes or preserves this divisibility contraction after normalization.