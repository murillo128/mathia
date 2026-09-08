# VIS-105 — the pre-frozen area-area chronology statistic is ordinary on the next disjoint zero-gap block

## Claim

The first fresh-source test of the canonical area-area chronology statistic from `VIS-104` is negative.

Keep the locally unfolded Riemann-zero gaps

`g_n = (gamma_(n+1)-gamma_n) log(((gamma_n+gamma_(n+1))/2)/(2 pi)) / (2 pi)`,

with `gamma_n` returned by `mpmath 1.3.0` `zetazero(n)`. Keep exactly the balanced ternary quantizer fixed from the disjoint training gaps `g_1,...,g_70` in `VIS-102`,

`q_1 = 0.7867599225271192`,
`q_2 = 1.1482531897489163`,

with embedding `e(0)=-1`, `e(1)=0`, `e(2)=+1`, and keep the ordinary three-delay polygonal path.

Because `VIS-104` was selected after inspection of the old confirmation block `g_71,...,g_106`, use the deterministic next disjoint 36-gap block

`g_107,...,g_142`

as fresh confirmation. It quantizes to

`112202002200212201020110121102110201`.

Condition exactly on this word's initial three-symbol context and complete length-four-block table, as in `VIS-099`--`VIS-100`. The exact Markov type has cardinality

`W=416`.

The canonical area-area projection `P_AA` from `VIS-104` is nondegenerate on this type class: its projected fourth-level coefficient vector takes `114` distinct values across the `416` compatible words.

Use the pre-frozen basis-independent statistic

`T_AA(X)=||P_AA ell_4(X)-E_null[P_AA ell_4]||^2`.

For the source word, exact rational arithmetic gives

`q_obs=(1/16,-63/16,-3/2)`,

while the exact conditional-null mean in the displayed orthogonal `B_1,B_2,B_3` coordinates is

`E_null[q]=(-2609/416,-63/16,2011/416)`.

Thus the centered coefficient vector is

`(2635/416,0,-2635/416)`

and, because each `B_j` has squared norm `8`,

`T_AA(obs)=6943225/10816 = 641.940181...`.

Exhaustive enumeration of all `416` compatible words gives the exact upper-tail probability

`p = #{T_AA >= T_AA(obs)}/416 = 183/416 = 0.439903846...`.

The fresh zeta block is therefore ordinary under this exact local-block-conditioned null. The area-area projection passes its admission gate but supplies no source separation in this first pre-frozen confirmation test.

**Evidence/status:** `COMPUTATIONAL-EXACT-CONDITIONAL-NULL + FINITE-EMPIRICAL-NEGATIVE + PRE-FROZEN-STATISTIC + NO-NOVELTY-CLAIM`.

This is a finite negative result for one fresh block and one already fixed ternary representation. It is not a theorem that zeta-zero chronology is null.

## 1. The confirmation design was fixed before evaluating the source residual

`VIS-101` and `VIS-102` used `g_71,...,g_106`. `VIS-103` then ruled out merely applying the same functional after the tensor logarithm, and `VIS-104` selected the canonical three-dimensional area-area subspace

`C_AA=[L_2(R^3),L_2(R^3)]`

and its centered squared projection norm `T_AA` without using any later source block.

The present test changes only the source material. Before evaluating `T_AA`, the design is fixed as the immediately following disjoint block `g_107,...,g_142`, with the unfolding convention, ternary thresholds, symbol embedding, delay dimension, endpoint treatment, conditional Markov type, projector `P_AA`, and upper-tail squared-distance statistic inherited unchanged from the preceding findings.

No window, threshold, component of `P_AA`, or tail direction is selected after inspecting this block. The upper tail is the natural pre-specified rule because `T_AA` is itself a nonnegative squared distance from the exact-null mean.

## 2. The exact conditional null is nondegenerate

The fresh quantized word begins at context `112` and ends at context `201`. It has `33` context transitions over `19` occurring three-symbol states.

Two independent exact counts agree on the type-class size. Memoized completion recursion gives `416` compatible words and exhaustive traversal produces exactly those `416` words. Independently, Whittle's formula from `VIS-100` gives cofactor

`C_(t,s)(B)=26/81`

and factorial factor

`prod_u r_u! / prod_(u,v) F_(uv)! = 1296`,

so

`W=1296*(26/81)=416`.

The stronger admission gate from `VIS-104` also passes. Across the complete type class, `P_AA S^4` takes `114` distinct coefficient vectors, so the statistic is not frozen by the admitted local four-block inventory.

## 3. The pre-frozen area-area statistic is central enough under the exact null

For the source word the projected coefficient vector is

`q_obs=(1/16,-63/16,-3/2)`.

The complete exact null has mean

`(-2609/416,-63/16,2011/416)`.

The middle projected coordinate therefore agrees exactly with its null mean, while the other two deviations are equal and opposite. With the orthogonal basis normalization from `VIS-104`, this yields the exact source statistic

`T_AA(obs)=6943225/10816`.

Exactly `183` of the `416` compatible words have `T_AA` at least this large. There is therefore no numerical-tail approximation, MCMC mixing issue, or simulation uncertainty in `p=183/416`.

The source vector itself occurs eight times in the type class, and the null contains `114` distinct `T_AA` values. The negative result is consequently not caused by a nearly degenerate projection or an accidentally singleton statistic.

## 4. Independent implementation checks reproduce the earlier exact boundaries

The calculation uses exact `Fraction` arithmetic for path-signature coefficients, the area-area projection, null moments, and tail comparison. Before applying it to the fresh block, the implementation reproduces three persisted exact checks:

- the `VIS-097` two-word collision has `(1,2,1,3)` fourth-level difference `1/4`;
- the corresponding `P_AA` coefficient difference is exactly `(1/4,0,-1/4)`, as in `VIS-104`;
- the `VIS-101` and `VIS-102` source coordinates reproduce `-214/3` and `-971/24` respectively.

A direct fourth-level log-signature calculation on all `416` fresh null words gives

`q(ell_4)-q(S^4)=(5/48,-5/48,-5/48)`

for every word. Thus the centered `P_AA` vectors and `T_AA` values are exactly identical between signature and log-signature, independently reproducing the affine-null consequence of `VIS-103`/`VIS-104` on this new type class.

Computational provenance is Python `3.13.5`, `mpmath 1.3.0`, `mp.dps=50`, exact rational signature/null arithmetic, and exhaustive enumeration of the finite type class. The closest fresh unfolded gap to either frozen quantizer threshold remains about `0.004269` away, so the reported symbol word is not sensitive to ordinary numerical rounding at the stated precision.

## 5. Prior art and novelty assessment

No new statistical or signature method is claimed. Chen/path-signature algebra, free-Lie/log-signature structure, Whittle Markov-type counting, and finite-size random-matrix baselines are classical ingredients already anchored in `SOURCES.md` and the preceding findings.

A targeted structural literature check did not identify a direct prior experiment combining this exact Riemann-zero gap quotient, area-area fourth-level projection, and exact Markov-type conditional null. That absence is not used as evidence of novelty. The present result is a finite negative application of the already established Mathia construction.

## Boundary and falsification

This finding establishes only that the stated fresh 36-gap block is ordinary for the pre-frozen ternary `P_AA` statistic under its exact quantized order-three Markov-type null.

It does not establish that:

- all zeta-zero windows are ordinary under `P_AA`;
- another independently fixed source scale or quantizer is null;
- the exact Markov type is a complete non-arithmetic source model;
- real-valued chronology discarded by the finite quotient is absent;
- a future positive conditional residual would be arithmetic-specific rather than generic spectral memory;
- zeta differs from an appropriate finite-size CUE or finite-height arithmetic control;
- any fourth-level statistic gives an RH criterion.

Falsify the finite claim by recomputing `gamma_107,...,gamma_143` with the stated unfolding and frozen thresholds and obtaining a different source word, by finding a type cardinality different from `416`, by showing `P_AA` is constant on that class, or by exact enumeration obtaining a different `q_obs`, null mean, `T_AA(obs)`, or tail count `183`.

## Visual consequence

No canonical PNG is retained. The decisive question is an exact finite conditional distribution of a pre-frozen coordinate-free statistic; rendering that distribution would add presentation but no mathematical information beyond the complete enumeration.

## Research consequence

The `VIS-104` admission mechanism works on fresh source material but the first clean source test is negative. The area-area channel should therefore not be treated as evidence of a zeta-specific chronology residual merely because it is an exact nonlocal information carrier in principle.

The accepted critical-strip multiscale clue remains open only in narrowed form. Repeating the same statistic on one window after another until an unusual block appears would be sequential search, not independent confirmation. A further `P_AA` program should predeclare a disjoint window family or height regime and its combined decision rule before inspecting those residuals; alternatively a materially different information carrier must be fixed and evaluated on new untouched material. Any positive conditional result would still require matched finite-size/random-matrix or finite-height arithmetic source controls before an arithmetic interpretation.