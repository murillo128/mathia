---
id: CLUE-global-cross-line-fidelity-realization-separation
type: research-clue
status: proposed
origin: graph-curator
target_line: global
based_on:
  - research/arithmetic_fidelity/findings/AF-023-regular-weil-test-points-have-positive-dimensional-beurling-fibers.md
  - research/arithmetic_fidelity/findings/AF-053-null-symbol-stabilization-collapses-zero-error-tv-repair-to-bayes-risk.md
  - research/arithmetic_fidelity/findings/AF-054-maximal-safe-target-envelope-under-isometric-refinement.md
  - research/prime_circle/findings/PC-120-divergent-scalar-hardy-amplification-destroys-det2-normality.md
  - research/prime_flute/findings/PF-159-canonical-selberg-quarter-boundary-is-one-ended-propagation.md
  - research/prime_lattice/findings/PL-106-zeta-dqpt-programmable-dirichlet-readout.md
  - research/weil_inertia/findings/WI-093-extensive-prime-rank-defect-forces-bounded-metric-overlap.md
  - research/weil_positivity/findings/WP-099-passive-positive-auxiliary-elimination-cannot-sparsify-the-mixed-prime-completion.md
  - research/weil_positivity/findings/WP-102-exact-critical-prime-torus-completions-have-infinite-cylindrical-fisher-energy.md
  - research/arithmetic_fidelity/findings/AF-133-restricted-witness-composition-requires-quotient-compatible-recovery.md
  - research/prime_flute/findings/PF-168-tail-dirichlet-laplacians-are-norm-resolvent-composite-blind.md
  - research/weil_inertia/findings/WI-011-refined-four-point-envelope-improves-certified-bound.md
  - research/weil_inertia/findings/WI-164-schur-normalization-cancels-horizontal-collapse.md
---

# Can source fidelity, target transport, and destination realization be separated by one exact cross-line criterion?

## Observation

Several current lines fail at mathematically different interfaces, and AF-053--AF-054 now make one of those interfaces exact. A retained statistic can preserve the source experiment and even preserve its ambient discrepancy under an admitted representation equivalence while the distance to a structural target changes because the refined target acquires non-descending realizations. AF-054 identifies the unique maximal **safe target envelope** under an isometric refinement, so target-descent failure is no longer only a conceptual warning: it has an exact metric criterion in a broad model class.

The RH-facing results expose complementary failures after source information has survived. PC-120 keeps the source-derived Hardy corrector but scalar amplification either stays zero-free or leaves finite Fredholm normality. PF-159 preserves the separator geometry while identifying the apparent quarter boundary as a one-ended propagation term. PL-106 preserves the logarithmic spectrum while showing that a zero divisor can be programmed through the observable. WI-093 shows that an extensive algebraic rank defect can coexist with only bounded metric overlap. WP-099 preserves positivity under passive reduction but proves that the order relation cannot produce the sparse target carrier, while WP-102 shows that even arbitrary correlated positive completions with the exact target moments fail a destination regularity requirement through infinite cylindrical Fisher energy.

These are not evidence that one universal theorem already exists. They make the interfaces precise enough to test whether a reusable factorization can distinguish them without collapsing them into one vague notion of "information loss."

Two sharper controls make the target distinction actionable for Master-level cross-line synthesis. PF-168 compares a prime flute with `p_n+1`: that control is all-composite but preserves every ordered prime gap, and the theorem concerns fixed spectral filters on moving Dirichlet tails. WI-164 gives a different failure: its normalized Schur correction is exactly `K_V K_V^*`, which vanishes for an isolated off-line pair even though the intended positive charge for horizontal displacement would not. These have different implications: one transports much of the source data while identifying a restricted readout; the other directly falsifies the proposed universal charge within its finite configuration class.

AF-133 also makes the assembly gate precise in a finite model. For restricted witness bodies, recovery has a finite coefficient `kappa` exactly when it respects their invisible quotients; quantitative transport then requires control of that coefficient. An abstract scalar margin cannot automatically survive a change of witness geometry.

## Research question

Can a candidate arithmetic mechanism be factored, under explicit hypotheses, into

1. a source-to-statistic map together with an admitted source equivalence;
2. an equivalence-compatible **target transport/envelope** for the structural property being claimed;
3. a destination realization carrying the required metric, topology, regularity, operator ideal, or sign cone; and
4. a global assembly/quantitative transfer map,

so that source fidelity loss, target-descent failure, destination-realization failure, and assembly/information-budget failure are theorem-level distinct?

The sharpened subquestion is whether AF-054's safe-envelope notion can serve as the exact target-transport component of such a factorization while WP-102-type energy/domain obstructions remain genuinely independent destination conditions. If every target-descent condition can always be absorbed into the destination category without loss of explanatory power, the taxonomy should collapse. If not, one should be able to prove a counterexample where source fidelity and destination realizability survive but an admitted equivalent presentation changes the target outside the safe envelope.

Require the criterion to distinguish an admissible **target-different control** from a target-preserving re-encoding. Which exact hypotheses make matched-readout equality a no-go for an arithmetic implication, and which instead leave a universal mechanism usable once independent arithmetic assumptions are supplied? For approximate equality, what witness-transport modulus and target separation are required in the topology actually used by the final theorem?

## Why it may matter

A theorem-level separation would prevent two opposite errors: treating every negative result as source information loss, and treating a representation-dependent target or programmable observable as intrinsic merely because the source statistic is faithful. It would also give Mathia a reusable rule for deciding when adding coordinates, auxiliaries, quotients, regularizations, equivalent presentations, or singular domains is harmless and when it silently changes either the theorem being asked or the category in which the theorem must be proved.

AF-054 now provides a candidate exact invariant for one gate; WP-102 and WI-093 provide clean examples where the obstruction instead lies in destination metric/regularity after algebraic information is present. This makes the clue more falsifiable than a purely terminological taxonomy.

## Decisive test

Begin with a finite implication audit before attempting a universal taxonomy. Write the source class, all admitted hypotheses, the readout, and the transported target for the WI-164 isolated-pair control. Show exactly which universal charge it refutes. Contrast this with PF-168: state the gap-preserving shift, the moving-tail operator category, and whether a proposed destination target is even known to differ on the clone. Do not infer a target difference merely from composite labels.

Use WI-011 as a positive comparator: its local certificate is uniform over configurations, and the arithmetic consequence comes from a separate audited zeta bridge. A proposed fidelity criterion should not reject this kind of universal certificate simply because non-arithmetic configurations satisfy it. It should demand the explicit bridge and error budget instead. This is a compatibility check against a persisted derivation, not an assertion that the entire assembled WI-011 result has been replayed in Lean.

Formulate the smallest exact or quantitative separation criterion that classifies these examples correctly. Use AF-133's coefficient only after constructing its legitimate witness/channel instance; a deterministic operator analogue needs its own hypotheses. If the distinction is just standard sufficiency plus a continuity modulus, record that classical reduction rather than inventing a new obstruction taxonomy. The target-envelope comparison below remains the generalization test after these concrete cases.

Start with the AF-054 isometric-refinement theorem and one RH-facing case whose obstruction occurs strictly after source retention, preferably WP-102 or WI-093. Write explicitly the source class, admitted equivalence, retained statistic, target family, safe target envelope, destination category/metric, and assembly map.

Then prove one of the following:

- a factorization theorem under reusable hypotheses showing that target transport and destination realization are independent gates, with AF-054 and the chosen RH-facing obstruction as genuine instances; or
- a reduction theorem showing that target transport is always representable as an ordinary destination-realization condition in the relevant category, so the four-way taxonomy can be simplified without losing either example.

A useful stress test is PL-106: the source/log-spectrum realization is exact, but the observable is programmable. The framework should classify this as a target/selector issue rather than source loss. It should also classify WI-093 as metric-strength loss rather than rank/support loss, and WP-102 as regularity/domain failure rather than positivity or measure-class failure.

If neither direction can be made exact across two lines, narrow the clue to the smallest pair for which the distinction is theorem-level.

## Evidence boundary

No cross-line factorization theorem or universal obstruction taxonomy is established here. AF-054 proves an exact safe-envelope statement only in its metric refinement setting; WI-093 and WP-102 prove line-specific metric/regularity obstructions; PC-120, PF-159, and PL-106 support only their own operator, geometric, or readout claims. Graph topology and frontier telemetry are navigation aids only and are not evidence for this clue.

Neither this clue nor a count of matched controls establishes that a research family is exhausted. PF-168 does not discard all arithmetic information, WI-164 does not exclude source-specific operator charges, and AF-133 is not automatically a theorem about infinite-dimensional spectral assembly. Master can use a resolved distinction to route concrete local questions, but no scheduling, portfolio disposition, or mathematical acceptance is encoded here.
