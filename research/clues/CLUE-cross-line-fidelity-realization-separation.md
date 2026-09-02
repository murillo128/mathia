---
id: CLUE-global-cross-line-fidelity-realization-separation
type: research-clue
status: proposed
origin: graph-curator
target_line: global
based_on:
  - research/arithmetic_fidelity/findings/AF-023-regular-weil-test-points-have-positive-dimensional-beurling-fibers.md
  - research/arithmetic_fidelity/findings/AF-053-null-symbol-stabilization-collapses-zero-error-tv-repair-to-bayes-risk.md
  - research/prime_circle/findings/PC-120-divergent-scalar-hardy-amplification-destroys-det2-normality.md
  - research/prime_flute/findings/PF-159-canonical-selberg-quarter-boundary-is-one-ended-propagation.md
  - research/prime_lattice/findings/PL-106-zeta-dqpt-programmable-dirichlet-readout.md
  - research/weil_inertia/findings/WI-085-finite-window-ramanujan-scalarization-has-exact-alias-quotient.md
  - research/weil_positivity/findings/WP-099-passive-positive-auxiliary-elimination-cannot-sparsify-the-mixed-prime-completion.md
---

# Can source fidelity and destination realization be separated by one exact cross-line criterion?

## Observation

Several current lines now fail at mathematically different interfaces, and `AF-053` exposes a distinction that the earlier version of this clue did not isolate. A retained statistic can preserve the source experiment and even preserve its ambient discrepancy under a declared representation equivalence, while the distance to a structural target still changes because the target acquires non-descending realizations. Thus "the information survived" and "the metric is invariant" do not by themselves imply that the **target semantics** are intrinsic.

The newer RH-facing results expose complementary boundaries. `PC-120` keeps the source-derived Hardy corrector but scalar amplification either remains zero-free or leaves the finite Fredholm category. `PF-159` removes the canonical one-ended Selberg boundary and leaves a zero-free connected residual. `PL-106` preserves the logarithmic spectrum while showing that a zero divisor can be programmed through the observable. `WI-085` identifies an exact scalar finite-window alias quotient. `WP-099` preserves positivity under passive reduction but proves that the resulting order relation cannot produce the sparse target carrier. These are not evidence that one universal theorem already exists; they make the interfaces precise enough to test whether one can.

## Research question

Can a candidate mechanism be factored, under explicit hypotheses, into

1. a source-to-statistic map with an admissible source equivalence;
2. an equivalence-compatible **target family** for the claimed structural property;
3. a destination realization carrying the required topology/operator ideal/sign; and
4. a global assembly or quantitative transfer map,

so that fidelity loss, target-descent failure, realization failure, and assembly/information-budget failure are mathematically distinguishable?

The sharp subquestion introduced by `AF-053` is whether **target-descent failure is genuinely independent of realization failure**. If every compatible target can be encoded as part of the destination category, the taxonomy should collapse. If not, there should be an explicit example where source fidelity and destination continuity/realizability survive while an equivalent presentation changes the admissible structural target.

## Why it may matter

A theorem-level separation would prevent two opposite errors: treating every negative result as "information loss", and treating a representation-dependent target or programmable observable as an intrinsic realization merely because the source statistic is faithful. It would also give the program a reusable rule for deciding when adding coordinates, auxiliaries, quotients, regularizations, or equivalent presentations is harmless and when it silently changes the theorem being asked.

## Decisive test

Start with `AF-053`, where the source experiment and TV geometry are Blackwell-invariant but unrestricted zero-error target distance changes under null stabilization. Pair it with at least one RH-facing construction whose obstruction occurs after source retention, preferably `PC-120` or `WP-099`.

Write the exact source class, declared equivalence, retained object, target family, destination category, topology/order, and assembly map for both cases. Then prove one of the following:

- a proposition showing that target descent is always representable as an ordinary realization condition under explicit reusable hypotheses, and recover both cited line-specific obstructions as instances; or
- a counterexample satisfying source fidelity and destination realization/stability while changing the admissible target under an allowed equivalence, proving that target descent is a separate gate.

The result must reproduce the canonical line-specific obstruction rather than merely rename it. If neither direction can be made exact across two lines, narrow this clue to the smallest pair for which the distinction is theorem-level.

## Evidence boundary

No cross-line equivalence, factorization theorem, or four-way obstruction taxonomy is established here. Each cited finding supports only its own source, target, topology, or assembly statement. Graph topology and frontier telemetry are navigation aids only and are not evidence for this clue.
