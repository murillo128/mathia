# NB-290 — multiplicative dilations contract canonical Nyman Gram pivots

- **Date:** 2026-09-22
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-002, NB-014, NB-016, NB-287, NB-288, NB-289
- **Classification:** `EXACT-DERIVED + CANONICAL-NYMAN-SOURCE + DILATION-SEMIGROUP + GRAM-SCHMIDT-PIVOTS + SCHUR-COMPLEMENT + DIVISIBILITY-CONTRACTION + COMPOSITE-INDEX-DECAY + SOURCE-METRIC-COUPLING + TARGET-RATE-NOT-CLAIMED + PRIOR-ART-AUDITED`

## Claim

`NB-288` and `NB-289` show that bounded sampling Grams, bounded right inverses, and even the exact future Dirichlet zero-sample table do not force a quantitative finite-section rate: an abstract Hilbert model can retain arbitrary lethargy while satisfying all of those constraints. A useful next invariant therefore has to use metric relations among the **actual Nyman source vectors**, not only their sampled values.

Use the canonical generators

\[
g_n(x)=\left\{\frac1{nx}\right\}-\frac1n\left\{\frac1x\right\},
\qquad
V_n:=\operatorname{span}\{g_2,\ldots,g_n\},
\]

with `V_1={0}`, and define the one-step source innovation

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

After quotienting by **all** canonical generators preceding the product index `mn`, one gets the exact transport law

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

Equivalently, the renormalized pivots

\[
\tau_n:=\sqrt n\,\sigma_n
\tag{6}
\]

are monotone along divisibility:

\[
\boxed{n\mid N\quad\Longrightarrow\quad \tau_N\le\tau_n.}
\tag{7}
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
\tag{8}
\]

For completeness, (3) follows directly from the fractional-part definition. On `x<=1/m`, the two `{1/x}` terms cancel and one obtains `sqrt(m) g_j(mx)`. On `x>1/m`, both `1/(mx)` and `1/(mjx)` lie in `(0,1)`, so the right side of (3) cancels to zero, matching `A_mg_j`.

If `j<n`, equation (3) uses only `g_m` and `g_(mj)`. Since

\[
m<mn,
\qquad
mj\le m(n-1)<mn,
\]

we have

\[
\boxed{A_mV_{n-1}\subseteq V_{mn-1}.}
\tag{9}
\]

Now write `w_n=g_n-P_(V_(n-1))g_n`. Applying `A_m` gives

\[
A_mw_n
=
\sqrt m\,g_{mn}
-\frac{\sqrt m}{n}g_m
-A_mP_{V_{n-1}}g_n.
\tag{10}
\]

The last two terms belong to `V_(mn-1)` by (9) and `m<mn`. Therefore

\[
P_{V_{mn-1}^{\perp}}A_mw_n
=
\sqrt m\,P_{V_{mn-1}^{\perp}}g_{mn}
=
\sqrt m\,w_{mn},
\]

which proves (4). Projection is contractive and `A_m` is isometric, hence

\[
\sqrt m\,\sigma_{mn}
\le
\sigma_n,
\]

proving (5) and (7).

This is distinct from `NB-002`. A copied block `A_mV_N` preserves its internal Gram geometry exactly. Here the copied innovation is compared with the **full canonical section** preceding `mn`, which contains many directions not present in the copied block. Those extra directions can only absorb more of the innovation.

## 2. Retention coefficients form a scalar multiplicative cocycle

Normalize the pivots by

\[
\psi_n:=\frac{w_n}{\sigma_n}.
\tag{11}
\]

Equation (4) becomes

\[
P_{V_{mn-1}^{\perp}}A_m\psi_n
=
c_{m,n}\psi_{mn},
\qquad
c_{m,n}:=\frac{\sqrt m\,\sigma_{mn}}{\sigma_n}.
\tag{12}
\]

Thus

\[
0<c_{m,n}\le1,
\qquad
\boxed{\langle A_m\psi_n,\psi_{mn}\rangle=c_{m,n}.}
\tag{13}
\]

Equivalently,

\[
A_m\psi_n
=c_{m,n}\psi_{mn}+u_{m,n},
\qquad
u_{m,n}\in V_{mn-1},
\tag{14}
\]

and orthogonality gives

\[
\|u_{m,n}\|^2=1-c_{m,n}^2.
\tag{15}
\]

The coefficient has an exact multiplicative consistency law. For `k,m,n>=2`,

\[
\boxed{c_{km,n}=c_{k,mn}\,c_{m,n}.}
\tag{16}
\]

Indeed,

\[
\frac{\sqrt{km}\,\sigma_{kmn}}{\sigma_n}
=
\left(\frac{\sqrt k\,\sigma_{kmn}}{\sigma_{mn}}\right)
\left(\frac{\sqrt m\,\sigma_{mn}}{\sigma_n}\right).
\tag{17}
\]

So the canonical source does not merely satisfy isolated pairwise contractions. The fraction of normalized novelty that survives along a multiplicative ray is governed by a scalar cocycle. Equation (16) concerns only the quotient coefficient; it does not assert a scalar semigroup law for the old-section remainders `u_(m,n)`.

## 3. Schur-complement and composite-index consequences

Let `G_n` be the Gram matrix of `g_2,...,g_n`. Positive definiteness and the block determinant formula give

\[
\boxed{
\sigma_n^2
=
\frac{\det G_n}{\det G_{n-1}},
}
\tag{18}
\]

with `det G_1:=1`. Squaring (5),

\[
\boxed{
\frac{\det G_{mn}}{\det G_{mn-1}}
\le
\frac1m
\frac{\det G_n}{\det G_{n-1}}.
}
\tag{19}
\]

Thus a multiplicatively inherited canonical direction contributes at most a `1/m` fraction of its predecessor's one-step Gram volume.

There is also an unconditional consequence for every composite index. Let `N=mp`, where `p` is the smallest prime factor of the composite integer `N`. Then `p<=sqrt(N)`, and

\[
\sigma_N
\le
\sigma_p\sqrt{\frac pN}.
\tag{20}
\]

Since fractional parts are bounded by one,

\[
|g_p(x)|\le1+\frac1p\le\frac32,
\qquad
\sigma_p\le\|g_p\|\le\frac32.
\]

Therefore

\[
\boxed{
\sigma_N\le\frac32 N^{-1/4}
\qquad(N\text{ composite}).
}
\tag{21}
\]

Along multiples of any fixed `n>=2`, the stronger estimate is

\[
\boxed{
\sigma_N
\le
\sigma_n\sqrt{\frac nN}
\ll_n N^{-1/2}
\qquad(n\mid N).
}
\tag{22}
\]

For example,

\[
\sigma_{p^r}
\le
\sigma_p\,p^{-(r-1)/2}.
\tag{23}
\]

This does **not** say that prime pivots are large. It says only that a composite index has a proper multiplicative predecessor from which its canonical one-step novelty is quantitatively inherited. Prime indices are the only indices `n>=2` for which this particular predecessor mechanism is unavailable.

This complements `NB-016`: there, multiplicative overlaps make the quotient range of a whole dilation-enrichment frame multiplication-table sparse. Here, in the ordinary nested canonical ordering, every composite one-step pivot is already metrically dominated by a smaller divisor pivot.

## 4. Relation to the active finite-section obstruction

`NB-289` constructs abstract section systems whose generators reproduce any prescribed future first-free zero-sample table while the finite-section excess follows an arbitrary decreasing profile. That construction leaves metric relations among the raw generators essentially free. Equations (4)--(7) are therefore the kind of source-native constraint that its control does not encode: canonical Nyman sections cannot assign Gram--Schmidt novelty independently at multiplicatively related indices.

But (5) alone does not bound the target-aware excess from `NB-287`,

\[
\mathfrak A_M
=
\sum_{r\ge M}
|\langle h_M,q_{r+1}\rangle|^2.
\tag{24}
\]

The vectors `q_r` there are **normalized** future null-innovations for the first-free sampling problem. A small raw source pivot can still have a large normalized sample profile or target correlation: division by `sigma_r` can amplify the very quantity the sampler uses. Hence this finding does not claim decay of `||L psi_n||`, decay of the `q_n`, a rate for `mathfrak A_M`, convergence of `d_N`, or any implication for RH.

The next discriminant should couple the metric law above to the actual sample/target geometry. Useful quantities include

\[
\|L_Z\psi_n\|,
\qquad
\langle h_M,q_n\rangle,
\tag{25}
\]

or a weighted combination in which the `sigma_n` contraction survives normalization. A bound depending only on point-sample identities is ruled out by `NB-289`; a bound depending only on `sigma_n` ignores the normalization problem.

The retention cocycle gives another concrete test. If the actual arithmetic source forces cumulative loss through products of the `c_(m,n)`, the arbitrary-lethargy construction cannot persist unchanged. If normalized sample coupling compensates that loss, the pivot contraction is metrically real but target-irrelevant. This is a source-versus-sample question rather than another generic conditioning question.

## 5. Adversarial review

The derivation was checked against the principal failure modes exposed earlier in the line.

First, no reducing-subspace assumption is made. The only semigroup input is the concrete isometry (2), the exact generator identity (3), and the one-way inclusion (9).

Second, the full preceding section matters. Both the transferred old-section term and the `g_m` correction in (10) are proved to lie in `V_(mn-1)` before projection. This is what turns block covariance into a canonical pivot inequality.

Third, the normalization is consistent: (4) implies `sqrt(m) sigma_(mn) <= sigma_n`, not the reverse. The same `sqrt(m)` convention is used in `NB-002`, `NB-014`, and `NB-039`.

Fourth, the composite estimate assumes no lower bound on prime pivots. It uses only the trivial upper bound `sigma_p<=||g_p||<=3/2` and `p<=sqrt(N)`.

Fifth, no target conclusion is imported from source geometry. The argument stops before identifying raw Gram pivots with the normalized first-free null-innovations. This distinction is load-bearing after `NB-288`--`NB-289`.

Finally, the result does not resolve `CLUE-visible-semigroup-defect-controls-section-enrichment`. That clue asks for residual-specific visibility and a target-distance decrement. The present theorem supplies a new exact metric constraint on canonical source enrichment, but not the missing residual coupling.

## 6. Prior-art and repository audit

The dilation/semigroup structure is classical in the Nyman--Beurling literature. Bagchi's 2006 survey, *On Nyman, Beurling and Baez-Duarte's Hilbert space reformulation of the Riemann hypothesis*, treats the Hilbert-space criterion together with its semigroup viewpoint. Inside this repository, the covariance identity (3) is already used in `NB-002`, `NB-014`, `NB-016`, `NB-039`, and the accepted visible-semigroup clue. No novelty is claimed for that identity, projection contraction, or the Schur-complement determinant formula.

A fresh search found Hugh Carvill's 2025 preprint *Beurling Nyman Geometry and Gram Matrix Structure, Ladder Density and Polynomial Decay via Mellin Smoothing* (arXiv:2510.18132), which proves polynomial off-diagonal Gram decay and block compressibility on a multiplicative `2^(-j)3^(-k)` ladder after Mellin smoothing. This is adjacent source-metric structure, but the searched material does not state the canonical nested-section quotient identity (4), the divisibility pivot contraction (5), or the cocycle (16). Werner Ehm's 2024 work *On certain Gram matrices and their associated series* studies formulas and decompositions for Nyman--Beurling Gram matrices, again adjacent but not a substitute for the quotient transport proved here.

The theorem is self-contained from identities already established in the repository, so no external result is load-bearing and `SOURCES.md` is unchanged. No `mind/**` file is updated: the result narrows the active frontier, but its relevance to the target-aware Ford/Nyman obstruction still depends on the missing normalized sample coupling.

## Research disposition

Keep as a source-metric advance after `NB-289`. The abstract negative controls showed that sample algebra and conditioning permit arbitrary lethargy. This finding identifies a concrete restriction they omit:

\[
\boxed{
\sqrt{mn}\,\sigma_{mn}
\le
\sqrt n\,\sigma_n.
}
\]

Canonical one-step novelty is therefore not free along multiplicative rays, and every composite pivot is quantitatively inherited from a smaller divisor. The next useful pass should test whether the actual first-free sample/target coupling neutralizes or preserves this divisibility contraction after normalization.