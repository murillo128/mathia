# VIS-106 — the predeclared four-block area-area replication panel does not reject

## Claim

The frozen four-block replication panel predeclared in `CLUE-zeta-critical-strip-multiscale-geometry` is negative.

Keep exactly the locally unfolded Riemann-zero gaps

`g_n = (gamma_(n+1)-gamma_n) log(((gamma_n+gamma_(n+1))/2)/(2 pi)) / (2 pi)`,

with `gamma_n` returned by `mpmath 1.3.0` `zetazero(n)`, the balanced ternary thresholds from `VIS-102`

`q_1 = 0.7867599225271192`,
`q_2 = 1.1482531897489163`,

the embedding `e(0)=-1`, `e(1)=0`, `e(2)=+1`, the ordinary three-delay polygonal path, exact order-three Markov-type conditioning, the canonical area-area projector `P_AA` from `VIS-104`, and the upper-tail statistic

`T_AA(X)=||P_AA ell_4(X)-E_null[P_AA ell_4]||^2`.

Evaluate exactly once the four disjoint 36-gap blocks frozen before inspection:

- `g_143,...,g_178`;
- `g_179,...,g_214`;
- `g_215,...,g_250`;
- `g_251,...,g_286`.

Their quantized words are respectively

`200112020112101202110021020112002121`,

`120020202112101120020122010211112021`,

`011120200221012112020120111022100212`,

and

`021102002021220102210200211002202101`.

For the four exact conditional type classes, Whittle cardinalities are

`W=(132,84,40,1488)`,

and exhaustive completion recursion independently gives the same counts. The area-area projection is nonconstant on every class, taking respectively

`(78,29,32,225)`

distinct projected coefficient vectors.

The exact conditional upper-tail probabilities are

`p_143-178 = 84/132 = 7/11 = 0.636363...`,
`p_179-214 = 80/84 = 20/21 = 0.952381...`,
`p_215-250 = 26/40 = 13/20 = 0.65`,
`p_251-286 = 1254/1488 = 209/248 = 0.842742...`.

The predeclared family-wise rule rejects only if

`min_j p_j <= 0.0125 = 1/80`.

Here `min_j p_j=7/11`, so the panel does **not** reject. The third class has `W=40`, so its exact positive tail lattice has minimum possible value `1/40=0.025>1/80`; under the predeclared rule it is a non-rejection regardless of its observed statistic and is not replaced by another window.

Thus the same-carrier adjacent-block replication route gives four further finite negatives after `VIS-105`. Per the frozen design, these windows must not be extended post hoc and reported as the same confirmation experiment.

**Evidence/status:** `COMPUTATIONAL-EXACT-CONDITIONAL-NULL + PREDECLARED-FAMILYWISE-NEGATIVE + FINITE-EMPIRICAL-NEGATIVE + NO-NOVELTY-CLAIM`.

This is a finite panel result for one fixed quantizer, delay construction, exact local quotient, and area-area statistic. It is not a theorem that zeta-zero chronology is null and it is not an arithmetic-specific source comparison.

## 1. The panel was frozen before these residuals were inspected

`VIS-105` tested the first fresh block `g_107,...,g_142` and obtained the exact negative `p=183/416`. It explicitly ruled out sequentially trying further convenient windows. The accepted clue then froze the next four blocks, all inherited representation choices, and Bonferroni threshold `1/80` before their source residuals were inspected.

No block boundary, quantizer threshold, symbol embedding, delay dimension, conditional memory order, `P_AA` component, statistic, tail direction, family size, or rejection threshold is changed in the present calculation. All four blocks are reported, including the class whose p-value lattice cannot attain the family-wise threshold.

The experiment therefore answers the predeclared replication question rather than selecting an unusual-looking window after the fact.

## 2. Exact admission and Whittle counts

For each source word, condition on its initial three-symbol context and complete length-four-block transition table. The Whittle cofactor and factorial factors are:

| block | start/end | cofactor | factorial factor | `W` | distinct `P_AA` |
| --- | --- | ---: | ---: | ---: | ---: |
| `143–178` | `200/121` | `11/36` | `432` | `132` | `78` |
| `179–214` | `120/021` | `7/54` | `648` | `84` | `29` |
| `215–250` | `011/212` | `5/24` | `192` | `40` | `32` |
| `251–286` | `021/101` | `31/216` | `10368` | `1488` | `225` |

In every row the product of the Whittle factors equals the displayed integer `W`. A separate memoized completion recursion returns the same four support sizes, and exhaustive traversal produces every admitted word for all four classes.

The stronger `VIS-104` admission gate also passes in each class because `P_AA` is not constant. The third class nevertheless lacks enough tail resolution to attain `1/80`; this was itself an explicitly predeclared non-rejection condition.

## 3. Exact source statistics and tails

Write the `P_AA` coefficient vector in the orthogonal basis `B_1,B_2,B_3` from `VIS-104`. Exact rational arithmetic gives:

| block | `q_obs` | `E_null[q]` | `T_AA(obs)` | upper-tail count | `p` |
| --- | --- | --- | ---: | ---: | ---: |
| `143–178` | `(-43/8,51/16,11/2)` | `(-71/33,51/16,601/264)` | `724201/4356` | `84/132` | `7/11` |
| `179–214` | `(9/4,5/8,-4)` | `(129/112,5/8,-325/112)` | `15129/784` | `80/84` | `20/21` |
| `215–250` | `(271/16,-173/16,-147/16)` | `(1453/160,-173/16,-213/160)` | `1580049/1600` | `26/40` | `13/20` |
| `251–286` | `(-9/16,-49/16,5/8)` | `(685/248,-49/16,-1339/496)` | `2719201/15376` | `1254/1488` | `209/248` |

No Monte Carlo approximation enters these tails.

There is also a repeated exact finite-class simplification worth recording without promoting it to a general theorem. On each of these four complete type classes, the middle projected coordinate `q_2` is constant and `q_1+q_3` is constant; hence the centered `P_AA` support lies on a one-dimensional affine line. The same finite-class property was already visible in `VIS-105`. This may indicate that the nominally three-dimensional area-area carrier loses additional dimensions after the exact shifted-delay/local-block quotient, but no universal statement is claimed here. Deriving or falsifying that structural collapse is a separate next mathematical question.

## 4. Reproduction and numerical-stability checks

The computation uses Python `3.13.5`, `mpmath 1.3.0`, `mp.dps=50`, exact `Fraction` arithmetic for fourth-level signature coefficients, `P_AA`, null means, squared norms, and tail comparisons, plus exhaustive type-class enumeration.

Before evaluating the frozen panel, the implementation reproduces the persisted controls:

- the `VIS-102` ternary old-block coordinate `S^4_(1,2,1,3)=-971/24`;
- the complete `VIS-105` class size `416`;
- the `VIS-105` source vector `(1/16,-63/16,-3/2)`;
- the `VIS-105` null mean `(-2609/416,-63/16,2011/416)`;
- the `VIS-105` statistic `6943225/10816` and tail `183/416`.

For the four new blocks, the closest unfolded gap to either frozen ternary threshold is respectively about `0.002123`, `0.004688`, `0.011043`, and `0.018237`, so none of the reported symbol words is numerically marginal at the stated precision.

## 5. Prior art and novelty assessment

No new statistical, signature, Markov-type, or random-matrix method is introduced here. The area-area projection is the exact algebraic construction audited in `VIS-104`; the conditional finite null and Whittle count are the classical Markov-type machinery audited in `VIS-099`--`VIS-100`; and the need for finite-size/non-arithmetic source controls for zeta spacings remains anchored by the CUE literature recorded in `SOURCES.md` and `VIS-019`.

The only new evidence is the execution of the already frozen finite panel. No novelty claim is made for its ingredients or for the generic use of family-wise multiple-testing control. Because the panel does not reject its own local conditional nulls, the source-specific CUE/arithmetic comparison gate is not reached.

## Boundary and falsification

This finding establishes only the exact finite result of the predeclared four-block panel. It does not establish that:

- all later or higher zero windows are ordinary under `P_AA`;
- the exact order-three Markov type is a complete non-arithmetic source model;
- the apparent affine-line collapse of `P_AA` is universal;
- real-valued chronology discarded by ternary quantization is absent;
- another independently specified nonlocal carrier is null;
- zeta and matched finite-size CUE agree for this statistic;
- any statement about RH follows.

Falsify the finite claim by reproducing `gamma_143,...,gamma_287` with the stated unfolding and frozen thresholds and obtaining different symbol words, by obtaining a different Whittle or exhaustive class cardinality, by finding a different exact `P_AA` support or source statistic, or by obtaining different complete upper-tail counts.

## Visual consequence

No canonical PNG is retained. The decisive output is the complete exact finite conditional panel. Rendering four tail distributions would add presentation but no evidence beyond the enumerated supports and predeclared decision rule.

## Research consequence

The accepted `CLUE-zeta-critical-strip-multiscale-geometry` remains open only as a broader information-design question. The specific adjacent-window `P_AA` replication branch is now spent: the first fresh block in `VIS-105` and all four predeclared replication blocks are non-rejections, so more adjacent windows must not be appended post hoc to the same experiment.

Before another same-carrier source test is justified, the repeated affine-line collapse of `P_AA` under the exact type classes should be understood or a separately motivated height/source-scale hypothesis should be fixed independently. Otherwise the visual line should move to a materially different nonlocal information carrier with an explicit lower-information null and fresh confirmation material.
