# WI-165 — positive mixtures of fixed-block scalar bounds cannot beat their best constituent

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + DECISIVE-NEGATIVE + BARRIER`. The first two-length test in `CLUE-four-point-weighted-cover-assembly` has an exact obstruction once each block construction has already been collapsed to a scalar global inequality. Any fixed finite geometry-independent nonnegative combination of such inequalities produces a bound that is a convex combination of the constituent ratios, so it cannot exceed the best single constituent. The algebra is the classical weighted-mediant identity; the Mathia consequence is that post-collapse mixing of block lengths cannot improve the four-point assembly. This does **not** prove optimality of uniform shifted blocks among adaptive or geometry-aware covers, because such covers may create a genuinely new domination inequality before scalar collapse.

No unconditional zero proportion changes in this finding.

## 1. Exact obstruction

Let `S=N_0^s(T,2T)` and `N=N(T,2T)`. Suppose a finite collection of fixed block constructions, indexed by `j=1,...,r`, has already been proved to give scalar asymptotic inequalities

\[
a_j S \ge b_j N-o_j(N),
\qquad a_j>0,
\tag{1}
\]

with each `o_j(N)/N -> 0`. Here `j` may encode a block length, a fixed shift-average rule, or any other construction whose geometry has already been eliminated and whose final information is only the pair `(a_j,b_j)`.

Take fixed weights

\[
\lambda_j\ge0,
\qquad
\sum_j\lambda_j a_j>0,
\tag{2}
\]

independent of `T` and of the realized zero/gap configuration. Multiplying (1) by `lambda_j` and summing gives

\[
\left(\sum_j\lambda_j a_j\right)S
\ge
\left(\sum_j\lambda_j b_j\right)N-o(N),
\tag{3}
\]

because a fixed finite positive combination of the `o_j(N)` terms is still `o(N)`. Hence the mixed asymptotic proportion is

\[
R(\lambda)
:=
\frac{\sum_j\lambda_j b_j}
     {\sum_j\lambda_j a_j}.
\tag{4}
\]

Put

\[
r_j:=\frac{b_j}{a_j},
\qquad
\omega_j:=
\frac{\lambda_j a_j}{\sum_k\lambda_k a_k}.
\tag{5}
\]

Then `omega_j>=0`, `sum_j omega_j=1`, and exactly

\[
\boxed{
R(\lambda)=\sum_j\omega_j r_j.
}
\tag{6}
\]

Therefore

\[
\boxed{
\min_j r_j
\le R(\lambda)
\le \max_j r_j.
}
\tag{7}
\]

In particular, no two-length positive mixture, and more generally no fixed finite positive mixture in this post-collapse class, can improve the best constituent ratio.

## 2. Equality and near-equality are rigid

Let

\[
R_*:=\max_j r_j,
\qquad
\Delta_j:=R_*-r_j\ge0.
\tag{8}
\]

Equation (6) gives the exact loss identity

\[
\boxed{
R_*-R(\lambda)
=
\sum_j\omega_j\Delta_j.
}
\tag{9}
\]

Thus equality in (7) occurs if and only if every constituent receiving positive effective denominator weight `omega_j` already attains `R_*`. A near-optimal mixture can place appreciable effective weight only on block rules whose own ratios are correspondingly near-optimal. There is no cancellation mechanism hidden in the positive mixing step.

For two lengths with `r_1>r_2`, this specializes to

\[
R(\lambda)
=r_1-\omega_2(r_1-r_2),
\tag{10}
\]

so every positive use of the inferior scalar bound makes the final ratio strictly worse.

## 3. Application to the WI-011 four-point assembly

WI-011 converts a fixed block length `m` and its already-established four-point/span accounting into a scalar global inequality of the form

\[
a_m S\ge b_m N-o(N).
\tag{11}
\]

For its displayed construction one may write

\[
a_m=m-\Gamma_m,
\qquad
b_m=mH_{\rm MT}-c_m,
\tag{12}
\]

where `Gamma_m` is the retained trace--energy contribution and `c_m` is the pressure/boundary charge produced by that particular block argument. The exact definitions can change when the local assembly is sharpened; the obstruction does not depend on their detailed formula. Once a block rule has been reduced to `(a_m,b_m)`, a fixed nonnegative mixture of several lengths has ratio

\[
\frac{\sum_m\lambda_m b_m}{\sum_m\lambda_m a_m}
=
\sum_m
\frac{\lambda_m a_m}{\sum_\ell\lambda_\ell a_\ell}
\frac{b_m}{a_m},
\tag{13}
\]

and therefore cannot beat the best chosen `m`.

This closes the clue's first proposed finite two-length experiment **if the experiment is performed only after each length has been separately shift-averaged and scalarized**. Searching over more lengths inside that same architecture can at most identify a better single constituent; mixing them provides no additional gain.

## 4. What this does not rule out

The hypothesis that matters is not merely positivity but **post-collapse scalarity**. Equation (6) does not apply when the cover is chosen or coupled before the geometry has been eliminated. In particular, this finding does not exclude:

- source- or gap-dependent placement whose weights depend on the realized configuration;
- a common pair-energy budget in which different block lengths dominate complementary Gram entries before any separate scalar inequalities are formed;
- nonlinear joint constraints between block families;
- adaptive rules whose proof yields a new universal domination inequality rather than a positive sum of pre-existing scalar bounds;
- new local certificates or new arithmetic input.

Any surviving weighted-cover proposal must therefore exhibit its advantage **before** the constituent constructions collapse to independent numbers `(a_m,b_m)`. If its final proof can be rearranged as (3) with fixed nonnegative coefficients, (7) kills the claimed improvement immediately.

This distinction is important for the current clue. It proves neither that uniform shifted blocks are globally optimal nor that a geometry-aware two-length cover is impossible. It only removes the nonadaptive positive-mixture subroute and sharpens the live question to whether overlap can exploit complementary local geometry without double spending Gram defect or span pressure.

## 5. Prior art and novelty audit

Identity (6) is the weighted mediant/convex-combination formula and is elementary classical algebra; no novelty is claimed for it. A structure-based search around weighted mediants, positive mixtures, block averaging, shifted blocks, and recent simple-zero/four-point assembly did not locate a prior Mathia finding or a zeta-specific source that states this exact post-collapse obstruction as the answer to the present two-length cover question. Absence from that search is not a priority claim.

The recent four-point input and scalar block bridge used as the application surface are already recorded and source-audited in WI-009 and WI-011. This finding adds only the exact barrier for combining already-produced scalar bounds; it does not upgrade the provenance of any constituent bound.

## 6. Decisive escape test and consequence

A claimed improvement from two or more block lengths escapes WI-165 only if its proof cannot be represented as a fixed finite nonnegative combination of separately valid scalar inequalities (1). Concretely, it must present a pre-collapse domination inequality whose admissible coefficients depend on shared local structure while remaining unconditional, and it must account exactly for every reused Gram-energy and pressure term.

Consequently, brute-force optimization of positive weights over a catalogue of already shift-averaged block-length bounds is mathematically exhausted. The live branch of `CLUE-four-point-weighted-cover-assembly` is the genuinely geometry-aware one: source-dependent placement, complementary pair coverage, or another coupled assembly that creates information before scalar collapse. A failure there would require a different dual/cover obstruction; WI-165 alone does not supply it.