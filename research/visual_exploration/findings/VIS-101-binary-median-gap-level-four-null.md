# VIS-101 — binary median zero-gap chronology shows no level-four residual under the exact Markov-type null

## Claim

For one fixed finite low-zero experiment implementing the accepted quantized chronology test from `VIS-097`, `VIS-099`, and `VIS-100`, the pre-selected fourth-level delay-signature coordinate does **not** separate the Riemann-zero gap sequence from its exact local-block-conditioned null.

Let `gamma_n` be the ordinates returned by `mpmath 1.3.0` `zetazero(n)`, and define the locally unfolded gaps

`g_n = (gamma_(n+1)-gamma_n) log(((gamma_n+gamma_(n+1))/2)/(2 pi)) / (2 pi)`.

Use `g_1,...,g_70` only to fix a binary quantizer at their median,

`q = 0.9792990674676084`,

and map `g<=q` to symbol `0`, `g>q` to symbol `1`. Embed the two symbols as `e(0)=-1`, `e(1)=+1`.

The target block is `g_71,...,g_106`, giving the 36-symbol word

`001101001000101000100101110110101010`.

Form the ordinary three-delay polygonal path

`X_i = (e(b_i), e(b_(i+1)), e(b_(i+2)))`

and fix the direction-sensitive fourth-level signature coordinate

`T = S^4(X)_(1,2,1,3)`.

Condition exactly on the target word's initial three-symbol context and complete length-four-block count table, i.e. on the order-three Markov type from `VIS-099`. Its Whittle cardinality is

`W = 94500`.

Exhaustive enumeration of all `94500` compatible words gives

`T_obs = -214/3`,
`E_null[T] = -4858/75 = -64.773333...`,
`sd_null(T) = 13.180025...`.

Using the fixed two-sided decision rule

`p = #{|T-E_null[T]| >= |T_obs-E_null[T]|} / W`

gives the exact finite-null value

`p = 62118/94500 = 493/750 = 0.657333...`.

Thus this specific binary-median, three-delay, level-four coordinate is entirely ordinary inside the exact conditional type class. It provides no evidence for chronology beyond the admitted quantized four-block table.

**Evidence/status:** `COMPUTATIONAL-EXACT-CONDITIONAL-NULL + FINITE-EMPIRICAL-NEGATIVE + NO-NOVELTY-CLAIM`.

This is a finite negative result for one fixed representation/statistic. It is not a theorem about all zeta-zero chronology, all quantizers, all fourth-level coordinates, high zeros, random-matrix controls, or RH.

## 1. Frozen design and information boundary

The experiment separates representation choice from target evaluation.

The first 70 unfolded gaps determine only the binary threshold `q`. The target uses the next 36 gaps without changing the threshold, observation length, delay dimension, symbol embedding, or statistic in response to its value.

The target statistic is the single coordinate `(1,2,1,3)` singled out by the exact chronology-capacity mechanism in `VIS-097`. No search over fourth-level coordinates, tensor projections, thresholds, or alphabet sizes is performed on the target block.

The conditional null preserves exactly:

- the initial three-symbol context;
- every transition count between three-symbol contexts;
- equivalently, the complete quantized length-four-block table.

It therefore removes every effect representable by a homogeneous order-three Markov model on this fixed binary quotient while retaining all counterfactual global assemblies compatible with those local counts.

The result applies only after quantization. It says nothing about information discarded inside the two real-valued gap bins.

## 2. Exact type-class admission and enumeration

For the target word the start and terminal contexts are respectively

`001` and `010`.

Writing each row as `(count appended-0, count appended-1)`, the observed three-context transition table is

`000:(0,2), 001:(4,1), 010:(4,4), 011:(2,1),`
`100:(2,2), 101:(5,2), 110:(0,3), 111:(1,0)`.

The Whittle cofactor-factorial formula from `VIS-100`, evaluated in exact rational/integer arithmetic, gives `W=94500>1`, so the representation passes the hard nondegeneracy gate.

As an independent finite check, a memoized completion recursion over the same transition multiset also returns `94500`. Exhaustively traversing that recursion enumerates exactly `94500` compatible symbol words; no Monte Carlo or MCMC approximation enters the reported null distribution.

The signature implementation was separately checked on the explicit two-word collision in `VIS-097`: with its original `0/1` embedding it reproduces

`S^4_(1,2,1,3)(a)-S^4_(1,2,1,3)(b)=1/4`.

This cross-check validates the coordinate calculation against an already-persisted exact example.

## 3. The observed coordinate is central under the exact null

The exact null support of `T` is discrete. The source value `-214/3` is shared by `9800` of the `94500` admissible assemblies.

Relative to the exact null mean, the standardized displacement is only

`z = -0.4977...`.

The exact two-sided tail probability `493/750` is therefore not suggestive of a residual chronology effect for this design. No visualization is needed to see the outcome: the source coordinate sits inside a high-mass central region of the conditioned type distribution.

This is stronger than a failed approximate shuffle test. The null sample space is the complete finite Markov type and the tail calculation is exhaustive, so simulation error and null-mixing uncertainty are zero for the stated statistic.

## 4. Prior art and novelty assessment

The mathematical ingredients are already classical or established in the preceding Mathia findings.

`VIS-097` supplies the exact fourth-level chronology carrier through Chen signature algebra. `VIS-099` identifies the finite-alphabet order-three Markov type as the parameter-free conditional null after quantization. `VIS-100`, anchored to Whittle's classical transition-count formula and later Markov-type/Eulerian counting literature in `SOURCES.md`, supplies the exact cardinality and completion-count interpretation.

The locally unfolded zeta-gap representation is a finite computational normalization, not a new spacing statistic. `VIS-019` already records the strong finite-size random-matrix baseline for low-order zero-gap geometry and prevents interpreting a finite low-zero anomaly as automatically arithmetic-specific.

A bounded structural literature search did not surface a direct match for this exact combination of a quantized three-delay fourth-level path-signature coordinate with an exact Markov-type conditional null on Riemann-zero gaps. That absence is not treated as evidence of novelty: the present result is a negative finite experiment, not a new general statistical method.

## Boundary and falsification

The result closes only the exact design stated above.

It does not establish that:

- another independently fixed quantizer or alphabet has no chronology residual;
- another pre-registered fourth-level/log-signature coordinate has no residual;
- higher or widely separated zeros behave the same way;
- a positive departure under another quotient would be arithmetic-specific;
- the binary quantization retains enough real-valued information to test every plausible source mechanism;
- the homogeneous order-three Markov type is a complete non-arithmetic source control.

The finite claim is falsified if reproducing the first 107 zeta-zero ordinates with the stated unfolding and threshold gives a different 36-symbol target word, if the exact conditioned type cardinality is not `94500`, if exhaustive compatible-word enumeration does not match the Whittle count, or if the exact signature/tail calculation differs from the values above.

Computational provenance for this check is Python `3.13.5`, `mpmath 1.3.0`, exact integer/rational arithmetic for the type count, and exhaustive enumeration of the admitted finite type class. No generated dataset or cache is persisted.

## Visual consequence

No canonical PNG is retained. The primary question here is whether one fixed direction-sensitive coordinate is exceptional under a completely enumerated finite null; a histogram would add presentation but no mathematical information beyond the exact distribution and tail count.

## Research consequence

The accepted `CLUE-zeta-critical-strip-multiscale-geometry` survives, but this first simple source-specific instantiation is closed.

Future work must not rerun or cosmetically re-render the same binary-median quotient and `(1,2,1,3)` statistic on the same target block. A further attempt needs a genuinely different **pre-registered** information carrier or scale — for example a principled multi-bin quantizer, a different direction-sensitive level-four/log-signature functional, or a higher/longer untouched source window — and any positive residual must still survive representation controls and matched non-arithmetic source models.

The correct lesson is narrow: level four can retain chronology in principle (`VIS-097`), but the first exact conditioned zeta-gap test gives no evidence that this particular chronology carrier is source-specific.
