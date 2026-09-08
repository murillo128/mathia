# VIS-102 — three-bin training-quantile zero-gap chronology is also null at the fixed level-four coordinate

## Claim

The first materially richer finite quantization of the source-specific chronology test from `VIS-101` is also negative.

Keep the same locally unfolded Riemann-zero gaps, untouched confirmation block, three-delay path, and previously selected direction-sensitive signature coordinate as in `VIS-101`, but replace the binary median quotient by a **three-bin quantizer fixed entirely from the disjoint training gaps** `g_1,...,g_70`.

Let

`g_n = (gamma_(n+1)-gamma_n) log(((gamma_n+gamma_(n+1))/2)/(2 pi)) / (2 pi)`,

where `gamma_n` is the ordinate returned by `mpmath 1.3.0` `zetazero(n)`.

Sort the 70 training gaps. Before evaluating the confirmation statistic, fix the two thresholds as the midpoints between training order statistics 23/24 and 47/48:

`q_1 = 0.7867599225271192`,
`q_2 = 1.1482531897489163`.

Map `g<=q_1` to symbol `0`, `q_1<g<=q_2` to symbol `1`, and `g>q_2` to symbol `2`, with embedding

`e(0)=-1`, `e(1)=0`, `e(2)=+1`.

The training-bin counts are `(23,24,23)`. Applying this frozen quantizer to the same untouched target block `g_71,...,g_106` gives the 36-symbol word

`012202102010212101210202110120111020`.

Form the ordinary three-delay polygonal path

`X_i=(e(b_i),e(b_(i+1)),e(b_(i+2)))`

and retain the coordinate already justified by the chronology-capacity result `VIS-097` and used in `VIS-101`:

`T=S^4(X)_(1,2,1,3)`.

Condition exactly on the target word's initial three-symbol context and complete length-four-block count table, i.e. its order-three Markov type from `VIS-099`. Whittle's formula gives the exact type-class cardinality

`W=1752`.

Independent exhaustive completion recursion enumerates exactly the same `1752` compatible words. Over that complete conditional null,

`T_obs = -971/24 = -40.458333...`,
`E_null[T] = -70301/1752 = -40.126141...`,
`Var_null(T) = 788039/42632 = 18.484683...`,
`sd_null(T) = 4.299382...`.

Using the same frozen two-sided rule as `VIS-101`,

`p = #{|T-E_null[T]| >= |T_obs-E_null[T]|}/W`,

the exact tail probability is

`p = 1672/1752 = 209/219 = 0.954337...`.

Thus enriching the finite quotient from two training-defined bins to three while holding the confirmation block and the pre-existing level-four coordinate fixed does **not** reveal a chronology residual beyond the complete quantized four-block table. The source statistic is even closer to the center of the exact conditioned null than in the binary experiment.

**Evidence/status:** `COMPUTATIONAL-EXACT-CONDITIONAL-NULL + FINITE-EMPIRICAL-NEGATIVE + PRE-FROZEN-REPRESENTATION + NO-NOVELTY-CLAIM`.

This is a finite negative result for one fixed three-bin quotient, one low-zero block, and one level-four coordinate. It is not evidence that all multi-bin quotients, all path-signature coordinates, higher zeros, or zeta-zero chronology are null.

## 1. The new information carrier was fixed independently of the confirmation residual

`VIS-101` closed the binary-median version of this experiment. The present test changes only the finite information carrier in a controlled way.

The training/confirmation split remains `g_1,...,g_70` versus `g_71,...,g_106`. The three-bin rule is fixed from training order statistics alone. With 70 training observations, the selected cut positions give the most nearly balanced deterministic three-bin partition without consulting the confirmation block: 23 training gaps fall below the first cut, 24 in the middle bin, and 23 above the second cut.

The confirmation window, local unfolding convention, delay dimension, symbol embedding order, and signature coordinate are not selected in response to the ternary target value. In particular, no search over alternative ternary thresholds, fourth-level coordinates, target windows, or tail conventions is performed after inspecting the result.

This makes the experiment materially different from `VIS-101` while changing only one major design axis. It asks specifically whether preserving more coarse amplitude information inside the finite quotient is enough to make the already established level-four chronology carrier source-specific.

## 2. The exact conditional sample space remains nondegenerate

The target begins at context `012` and ends at context `020`. Its complete ternary length-four-block table induces a directed multigraph on the observed three-symbol contexts.

Applying the Whittle cofactor-factorial count from `VIS-100` to that transition table gives

`W=1752>1`.

As an independent finite check, memoized recursion over the remaining transition multiset also returns `1752`. Exhaustively traversing that recursion enumerates all `1752` admissible symbol words with the same initial context and complete transition-count table.

The null is therefore neither a heuristic shuffle nor an MCMC approximation. Every sequence in the exact order-three Markov type receives mass `1/1752`, and the reported distribution of `T` is complete.

## 3. Exact level-four evaluation gives no source separation

The path-signature calculation uses Chen multiplication for the piecewise-linear three-delay path, with each edge contributing its truncated tensor exponential through degree four.

Before evaluating the zeta target, the implementation is checked against the exact collision in `VIS-097`. For the two scalar words displayed there it reproduces

`[S^4(X_a)-S^4(X_b)]_(1,2,1,3)=1/4`.

For the ternary target, `T_obs=-971/24`. Across the `1752` exact null assemblies the coordinate takes 83 distinct rational values, from `-1211/24` to `-695/24`; the observed value itself occurs 37 times.

The standardized displacement from the exact null mean is only

`z=-0.07727...`.

The two-sided exact tail probability `209/219` therefore gives no hint that this source word occupies an exceptional chronology position after conditioning on its full ternary four-block inventory.

The negative conclusion does not depend on a rendering. A histogram would show the same centrality but would add no mathematical information to the exact finite distribution and tail count, so no canonical PNG is retained.

## 4. Prior art and novelty assessment

No new statistical or signature method is introduced here.

The chronology carrier is the classical path-signature algebra already audited in `VIS-097`, with Chen multiplicativity and bounded-variation signatures anchored there to Hambly and Lyons. The finite conditional null is exactly the quantized Markov type established in `VIS-099`; its support size and uniform conditional law use Whittle's classical transition-count formula and the exact completion-count construction audited in `VIS-100`, with Whittle (1955), Cowan (1991), and Jacquet-Knessl-Szpankowski (2012) as source anchors.

Finite-size random-matrix corrections for Riemann-zero spacings are already recorded in `SOURCES.md` and `VIS-019`; they remain the relevant warning against turning any future low-height residual into arithmetic specificity without a matched source control.

A bounded literature search for the exact combination of Riemann-zero gaps, finite training-defined quantization, a fourth-level delay-path signature coordinate, and an exact Markov-type conditional null did not identify a direct prior experiment. That absence is not used as a novelty claim. This finding is only an exact finite negative instantiation of already-audited ingredients.

## Boundary and falsification

This finding closes only the stated ternary design. It does not establish that:

- a different independently fixed fourth-level or log-signature functional is null;
- a higher or longer untouched zero window gives the same result;
- a different finite quotient chosen *before* a new confirmation window is uninformative;
- real-valued information discarded inside the bins is irrelevant;
- the homogeneous order-three Markov type is a complete non-arithmetic source model;
- a positive residual under another design would be zeta-specific or arithmetic-specific.

Because `g_71,...,g_106` has now been inspected under both the binary and ternary quotients at the same coordinate, that block should no longer be used as fresh confirmation for further threshold or statistic search. A subsequent source-specific test that changes the representation or functional after these results must freeze the change first and use a new untouched confirmation window or an independently justified external specification.

Falsify the finite computation by reproducing the first 107 zero ordinates with the stated unfolding and obtaining different training thresholds or target symbols, by showing that Whittle's exact count is not `1752`, by exhaustive enumeration obtaining a different type-class size, by failing the `VIS-097` `1/4` signature cross-check, or by obtaining different exact target/null/tail values.

Computational provenance is Python `3.13.5`, `mpmath 1.3.0`, exact `Fraction` arithmetic for signature coordinates and null moments, exact rational/integer arithmetic for Whittle/count checks, and exhaustive enumeration of all admitted type-class words. No generated dataset or cache is persisted.

## Research consequence

The accepted `CLUE-zeta-critical-strip-multiscale-geometry` remains open but narrows again.

Two increasingly informative finite quotients of the same low-zero confirmation block — binary median in `VIS-101` and balanced training-defined ternary bins here — both place the same pre-existing direction-sensitive level-four coordinate well inside the exact conditioned Markov-type null.

That makes another threshold refinement on the same block a poor next experiment. A further chronology test should change a more substantive axis, such as the independently justified level-four/log-signature functional or the source scale, and must use fresh confirmation material if the choice is informed by these two negatives. The generic fact that level four can encode chronology remains true; these source tests show only that this particular coordinate has not yet turned that capacity into a zeta-specific residual.
