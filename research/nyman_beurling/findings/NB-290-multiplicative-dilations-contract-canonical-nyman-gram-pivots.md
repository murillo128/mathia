# NB-290 — multiplicative dilations contract canonical Nyman Gram pivots

- **Date:** 2026-09-22
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-002, NB-014, NB-016, NB-287, NB-288, NB-289
- **Classification:** `EXACT-DERIVED + CANONICAL-NYMAN-SOURCE + DILATION-SEMIGROUP + GRAM-SCHMIDT-PIVOTS + SCHUR-COMPLEMENT + DIVISIBILITY-CONTRACTION + COMPOSITE-INDEX-DECAY + SOURCE-METRIC-COUPLING + TARGET-RATE-NOT-CLAIMED + PRIOR-ART-AUDITED`

## Claim

`NB-288` and `NB-289` show that bounded sampling Grams, bounded right inverses, and even the exact future Dirichlet zero-sample table do not force a quantitative finite-section rate: an abstract Hilbert model can retain arbitrary lethargy while satisfying all of those constraints. A useful next invariant therefore has to use metric relations among the **actual Nyman source vectors**, not only their sampled values.

The canonical multiplicative dilation law supplies such a relation at the level of one-step Gram--Schmidt innovations.

Use

\[
g_n(x)=\left\{\frac1{nx}\right\}-\frac1n\left\{\frac1x\right\},
\qquad
V_n:=\operatorname{span}\{g_2,\ldots,g_n\},
\]

with `V_1={0}`. Let

\[
w_n:=(I-P_{V_{n-1}})g_n,
\qquad
\sigma_n:=\|w_n\|,
\qquad n\ge2.
\tag{1}
\]

Thus `sigma_n` is the one-step Gram--Schmidt pivot of the canonical section. The finite independence already proved in `NB-014` gives `sigma_n>0`.

For `m>=2` let

\[
(A_mf)(x)
=
\begin{cases}
\sqrt m\,f(mx),&0<x\le1/m,\\
0,&1/m<x<1.
\end{cases}
\tag{2}
\]

Then `A_m` is an isometry and the exact Nyman covariance identity is

\[
A_mg_j
=
\sqrt m\left(g_{mj}-\frac1j g_m\right).
\tag{3}
\]

The new observation is that after quotienting by **all** canonical generators preceding the product index `mn`, this identity becomes

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

This is a genuine source-metric constraint absent from the arbitrary-lethargy controls of `NB-288`--`NB-289`. It does **not** yet control the normalized first-free sample vectors or the target-aligned Parseval tail of `NB-287`, so it is not by itself a Nyman-distance rate.

## 1. Exact quotient transport of a source innovation

First verify that (2) is an isometry:

\[
\|A_mf\|_2^2
=
\int_0^{1/m}m|f(mx)|^2\,dx
=
\int_0^1|f(u)|^2\,du.
\tag{8}
\]

For completeness, (3) follows directly from the fractional-part definition. If `x<=1/m`,

\[
\begin{aligned}
\sqrt m\left(g_{mj}(x)-j^{-1}g_m(x)\right)
&=\sqrt m\left(
\left\{\frac1{mjx}\right\}
-\frac1{mj}\left\{\frac1x\right\}
-\frac1j\left\{\frac1{mx}\right\}
+\frac1{jm}\left\{\frac1x\right\}
\right)\\
&=\sqrt m\left(
\left\{\frac1{j(mx)}\right\}
-\frac1j\left\{\frac1{mx}\right\}
\right)\\
&=A_mg_j(x).
\end{aligned}
\tag{9}
\]

If `x>1/m`, then both `1/(mx)` and `1/(mjx)` lie in `(0,1)`, so the right side of (3) cancels to zero, again matching `A_mg_j(x)`.

Now take `j<n`. Equation (3) uses only the generators `g_m` and `g_(mj)`. Since

\[
m<mn,
\qquad
mj\le m(n-1)<mn,
\]

we have the exact section inclusion

\[
\boxed{A_mV_{n-1}\subseteq V_{mn-1}.}
\tag{10}
\]

Write

\[
w_n=g_n-P_{V_{n-1}}g_n.
\]

Applying `A_m` and using (3) at `j=n` gives

\[
A_mw_n
=
\sqrt m\,g_{mn}
-\frac{\sqrt m}{n}g_m
-A_mP_{V_{n-1}}g_n.
\tag{11}
\]

The last two terms lie in `V_(mn-1)` by (10) and `m<mn`. Projecting (11) onto its orthogonal complement therefore leaves

\[
P_{V_{mn-1}^{\perp}}A_mw_n
=
\sqrt m\,P_{V_{mn-1}^{\perp}}g_{mn}
=
\sqrt m\,w_{mn},
\]

which proves (4).

Orthogonal projection is contractive, while `A_m` is an isometry. Hence

\[
\sqrt m\,\sigma_{mn}
=
\|P_{V_{mn-1}^{\perp}}A_mw_n\|
\le
\|A_mw_n\|
=
\sigma_n,
\]

proving (5). Multiplying by `sqrt(mn)` gives (7).

The distinction from `NB-002` is important. `NB-002` says that a *copied finite block* `A_mV_N` preserves its internal Gram geometry exactly. Equation (5) asks a different question: after placing the copied innovation at index `mn`, how much survives projection against **every canonical generator with smaller index**, most of which are not in the copied block. The answer can only decrease, by the explicit factor in (5).

## 2. A canonical retention coefficient and an exact multiplicative cocycle

Normalize the one-step innovations,

\[
\psi_n:=\frac{w_n}{\sigma_n}.
\tag{12}
\]

Equation (4) becomes

\[
P_{V_{mn-1}^{\perp}}A_m\psi_n
=
c_{m,n}\psi_{mn},
\qquad
c_{m,n}:=rac{\sqrt m\,\sigma_{mn}}{\sigma_n}.
\tag{13}
\]

By (5),

\[
0<c_{m,n}\le1.
\tag{14}
\]

Thus `c_(m,n)` has an exact geometric meaning:

\[
\boxed{
\langle A_m\psi_n,\psi_{mn}\rangle=c_{m,n}.
}
\tag{15}
\]

It is the fraction of the normalized innovation at `n` that survives as the genuinely new canonical direction at the product index `mn`; the complementary component has already been absorbed by `V_(mn-1)`. More explicitly,

\[
A_m\psi_n
=c_{m,n}\psi_{mn}+u_{m,n},
\qquad
u_{m,n}\in V_{mn-1},
\tag{16}
\]

with

\[
\|u_{m,n}\|^2=1-c_{m,n}^2.
\tag{17}
\]

There is also an exact multiplicative consistency law. For `k,m,n>=2`,

\[
\boxed{
c_{km,n}=c_{k,mn}\,c_{m,n}.}
\tag{18}
\]

Indeed this is immediate from the pivot ratios:

\[
\frac{\sqrt{km}\,\sigma_{kmn}}{\sigma_n}
=
\left(
\frac{\sqrt k\,\sigma_{kmn}}{\sigma_{mn}}
\right)
\left(
\frac{\sqrt m\,\sigma_{mn}}{\sigma_n}
\right).
\tag{19}
\]

Therefore the canonical source does not merely obey isolated pairwise contraction inequalities. Its normalized pivot retention along a multiplicative ray is governed by a scalar cocycle. This is metric information that cannot be reproduced merely by prescribing the future point-sample vectors as in `NB-289`.

Equation (18) should not be misread as saying that the old-section remainders `u_(m,n)` themselves form a scalar semigroup. The exact statement concerns only the quotient coefficient selected by the canonical nested sections.

## 3. Schur-complement and composite-index consequences

Let `G_n` be the Gram matrix of `g_2,...,g_n`. Finite linear independence from `NB-014` makes `G_n` positive definite. Standard block determinant/Schur-complement algebra gives

\[
\boxed{
\sigma_n^2
=
\frac{\det G_n}{\det G_{n-1}},
}
\tag{20}
\]

with `det G_1:=1`. Squaring (5) yields the exact determinant-ratio inequality

\[
\boxed{
\frac{\det G_{mn}}{\det G_{mn-1}}
\le
\frac1m
\frac{\det G_n}{\det G_{n-1}}.
}
\tag{21}
\]

Thus a multiplicatively inherited canonical direction can contribute at most a `1/m` fraction of the predecessor's one-step Gram volume.

The inequality has an unconditional consequence for every composite index. Let `N` be composite, let `p` be its smallest prime factor, and write

\[
N=mp.
\]

Then `p<=sqrt(N)`, and (5) gives

\[
\sigma_N
\le
\sigma_p\sqrt{\frac pN}.
\tag{22}
\]

Pointwise,

\[
|g_p(x)|
\le1+\frac1p
\le\frac32,
\]

so `sigma_p<=||g_p||<=3/2`. Therefore

\[
\boxed{
\sigma_N\le\frac32 N^{-1/4}
\qquad(N\text{ composite}).
}
\tag{23}
\]

Much more strongly, along multiples of any fixed `n>=2`,

\[
\boxed{
\sigma_N
\le
\sigma_n\sqrt{\frac nN}
\ll_n N^{-1/2}
\qquad(n\mid N).
}
\tag{24}
\]

For instance,

\[
\sigma_{p^r}
\le
\sigma_p\,p^{-(r-1)/2}.
\tag{25}
\]

This does **not** assert that prime pivots are large. It says only that composite indices have a proper multiplicative predecessor from which their one-step novelty is quantitatively inherited and contracted. Prime indices are the only indices `n>=2` for which this particular predecessor mechanism is unavailable.

The result is complementary to `NB-016`. There, multiplicative overlaps make the quotient range of a whole dilation-enrichment frame sparse and multiplication-table controlled. Here, even for the ordinary nested canonical ordering, every composite one-step pivot is already metrically dominated by a smaller divisor pivot. Both effects come from the same multiplication structure, but they measure different objects.

## 4. Why this advances the post-NB-289 frontier, and why it is not yet a rate

`NB-289` constructs abstract section systems whose generators reproduce any prescribed future first-free zero-sample table while the finite-section excess follows an arbitrary decreasing profile. That construction leaves the metric relation among the raw generators essentially free. Equations (4)--(7) are therefore exactly the kind of source-native constraint that the control does not encode: canonical Nyman sections cannot assign their Gram--Schmidt novelty independently at multiplicatively related indices.

This is nevertheless **not sufficient** to bound the target-aware excess from `NB-287`. That quantity is

\[
\mathfrak A_M
=
\sum_{r\ge M}
|\langle h_M,q_{r+1}\rangle|^2,
\tag{26}
\]

where the `q_r` are normalized future null-innovations for the first-free sampling problem. Equation (5) controls the raw canonical pivot norm `sigma_r`; after normalization, a small pivot can still have a large sample profile or target correlation. Dividing by `sigma_r` can amplify exactly the quantity needed by the first-free sampler. Therefore none of the following is claimed:

- that `||L psi_n||` decays with `sigma_n`;
- that the `q_n` of `NB-287` are localized by (5);
- that `mathfrak A_M` has any rate;
- that `d_N` tends to zero; or
- that (23) has any direct implication for RH.

The next discriminant should couple the newly exposed metric law to the target/sample geometry rather than study either side alone. A useful estimate would control, for the actual first-free sampler `L_Z`, quantities such as

\[
\|L_Z\psi_n\|,
\qquad
\langle h_M,q_n\rangle,
\tag{27}
\]

or a weighted combination in which the `sigma_n` contraction survives normalization. A bound depending only on the point-sample identity is ruled out by `NB-289`; a bound depending only on `sigma_n` ignores the normalization problem above.

The retention cocycle (18) gives a second concrete target. If arithmetic structure forces cumulative loss

\[
\prod_j c_{m_j,n_j}
\]

along the multiplicative ancestry relevant to future null-relations, then the abstract lethargy construction cannot persist unchanged. Conversely, if normalized sample coupling compensates that loss, the new pivot contraction will be metrically real but target-irrelevant. This is now a precise source-versus-sample test.

## 5. Adversarial review

The derivation was checked against the main failure modes exposed earlier in the line.

First, no reducing-subspace assumption is made. The only semigroup input is the concrete isometry (2) and the exact generator identity (3). The crucial inclusion is one-way, `A_m V_(n-1) subset V_(mn-1)`; equality is neither used nor expected.

Second, (4) is stronger than merely observing that `A_m g_n` contains `g_(mn)`. The projection is taken against the **full** preceding canonical section. Both the transferred old-section term and the correction `g_m` are proved to lie in that section before the quotient is taken.

Third, the factor `sqrt(m)` is on the correct side. From (4), projection contraction gives `sqrt(m) sigma_(mn) <= sigma_n`, not the reverse. The same factor is consistent with the isometric normalization of `A_m` used in `NB-002`, `NB-014`, and `NB-039`.

Fourth, the composite estimate does not assume any lower bound on prime pivots. It uses only `sigma_p<=||g_p||<=3/2` and the elementary fact that the smallest prime factor of a composite integer is at most its square root.

Fifth, no target conclusion is smuggled in from source geometry. The finding explicitly stops before identifying raw Gram pivots with the normalized first-free null-innovations. This is load-bearing after the arbitrary-lethargy controls of `NB-288`--`NB-289`.

Finally, the result does not resolve `CLUE-visible-semigroup-defect-controls-section-enrichment`. That clue asks for residual-specific visibility and a quantitative target-distance decrement. The present theorem supplies a new exact metric constraint on canonical source enrichment, but not the missing residual coupling.

## 6. Prior-art and repository audit

The dilation/semigroup structure itself is classical in the Nyman--Beurling literature. Bagchi's 2006 survey, *On Nyman, Beurling and Baez-Duarte's Hilbert space reformulation of the Riemann hypothesis*, explicitly treats the Hilbert-space criterion together with its semigroup viewpoint. Inside this repository, the exact covariance identity (3) is already used in `NB-002`, `NB-014`, `NB-016`, `NB-039`, and the accepted visible-semigroup clue. No novelty is claimed for that identity, for orthogonal projection contraction, or for the Schur-complement determinant formula.

A fresh search also found Hugh Carvill's 2025 preprint *Beurling Nyman Geometry and Gram Matrix Structure, Ladder Density and Polynomial Decay via Mellin Smoothing* (arXiv:2510.18132), which proves polynomial off-diagonal Gram decay and block compressibility on a multiplicative `2^(-j)3^(-k)` ladder after Mellin smoothing. That is adjacent source-metric structure, but the searched material does not state the canonical nested-section quotient identity (4), the divisibility pivot contraction (5), or the cocycle (18). Werner Ehm's 2024 work *On certain Gram matrices and their associated series* studies formulas and decompositions for Nyman--Beurling Gram matrices, again adjacent but not a substitute for the quotient transport proved here.

The exact theorem is self-contained from identities already established in the repository, so no external result is load-bearing and `SOURCES.md` is unchanged. No `mind/**` file is updated: the theorem narrows the active frontier materially, but its relevance to the target-aware Ford/Nyman obstruction still depends on the missing normalized sample coupling.

## Research disposition

Keep as a source-metric advance after `NB-289`. The abstract negative controls showed that sample algebra and conditioning allow arbitrary lethargy. This finding identifies a concrete restriction they omit:

\[
\boxed{
\sqrt{mn}\,\sigma_{mn}
\le
\sqrt n\,\sigma_n.
}
\]

Hence canonical one-step novelty is not free along multiplicative rays, and every composite pivot is quantitatively inherited from a smaller divisor. The next useful pass should not seek another generic Gram condition. It should test whether the actual first-free sample/target coupling can neutralize or preserve this divisibility contraction after the innovations are normalized.