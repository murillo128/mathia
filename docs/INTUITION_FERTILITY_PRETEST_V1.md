# Intuition-fertility pre-test v1

## Status

**Current #30 contract, pending target-split resolution and independent review.**

This v1 supersedes v0 as the current design target while retaining v0 and the self-audit as provenance. It incorporates the material internal-audit fixes: qwen-lean is treated as a whole-proof generator, direct target-proof SFT exposure is excluded, easy wrapper theorems are calibration rather than primary evidence, and a theorem-independent `generic_strategy_control` is added alongside factual and cross-theorem controls.

The pre-test remains deliberately small. Its goal is not to prove that Mathia has human-like intuition. It asks whether compact strategic mathematical guidance can cause a separate formal specialist to generate more Lean-verified proofs, and whether the exact base model leaves measurable headroom relative to a strong frontier reference.

## Core hypothesis under test

The broader training hypothesis is:

```text
mathematical concepts
        |
reusable conceptual moves
        |
candidate intuitions emerge
        |
initial teacher/distillation bootstrap
        |
downstream mathematical fertility
        |
possible later optimization
```

#30 tests only whether the conceptual objects and the proposed fertility channel can be operationalized cleanly enough to justify later training design.

## Provisional concepts

Use six concept families as an experimental substrate, not a permanent ontology:

- **maps / composition / information flow** — what a transformation preserves, identifies, or loses and how that propagates under composition;
- **reversibility / inverse structure** — recoverability and the structural roles of left/right inverse, injectivity, surjectivity, and bijectivity;
- **equivalence / fibers / kernels / quotients** — controlled indistinguishability and representations that forget exactly specified distinctions;
- **decomposition / products / partitions** — structurally meaningful splitting and reconstruction;
- **symmetry / actions / orbits / stabilizers / invariants** — meaningful variation versus redundant motion and what survives transformation;
- **representation / factorization / bridges** — equivalent, coarser, intermediate, or otherwise more useful descriptions.

`Necessary/sufficient condition` is used as a reasoning relation, not a seventh concept family in v1.

## Provisional conceptual moves

Retain eight moves because the current examples separate them behaviorally:

- **transfer** — recognize a mechanism in another realization and port it;
- **decompose** — split the current object/problem into meaningful parts;
- **synthesize** — combine independently understood constructions or viewpoints;
- **abstract/compress** — identify a smaller common mechanism by removing accidental presentation;
- **reframe/bridge** — change representation or introduce an intermediate translator;
- **generalize/weaken** — broaden a statement or remove assumptions according to the mechanism;
- **stress-test** — perturb/falsify the proposed mechanism to locate its first obstruction;
- **select** — choose among legitimate viewpoints according to expected downstream usefulness.

The following earlier labels are not independent dimensions in v1:

- simplification -> result/criterion of reframing or selection;
- multiple perspectives -> repeated reframing;
- naturalness/canonicality -> selection criterion;
- prediction -> consequence/evaluation of a specific intuition;
- falsification and counterfactual -> merged as stress-test;
- bridge construction -> part of reframe/bridge;
- fertility -> downstream evaluation signal.

These names are scaffolding for research design. Later data may merge or split them.

## Behavioral discriminators

The dimension list is useful only if the moves can be told apart on mathematics.

- **abstract vs transfer:** recognizing quotient-by-redundancy as common to kernel/range and orbit/stabilizer is abstraction; using that mechanism to propose the quotient in the second domain is transfer.
- **decompose vs reframe:** splitting a Hall problem into a tight block and its complement stays within the same representation; quotienting a linear-map domain by its kernel changes representation.
- **synthesize vs bridge:** joining independently built matchings is synthesis; constructing the quotient-to-range or orbit-to-coset correspondence is a bridge.
- **stress-test vs generalize:** stress-testing asks what breaks when an assumption/structure is perturbed; generalizing uses the discovered mechanism to propose a weaker or broader valid statement.
- **reframe vs select:** reframing generates a candidate viewpoint; selection decides which candidate viewpoint is worth using for the present goal.

The first theorem panel is not required to score every dimension uniformly. Its immediate function is to validate the intuition-to-formal-worker channel.

## Intuition unit

An intuition is one **compact strategic proposal**. It may state a mechanism, representation, intermediate object, small number of useful subgoals, relevant assumption, or obstruction.

A good intuition need not match the documented historical explanation. It need not be guaranteed true in every exploratory detail. It must be specific enough to alter the downstream formal worker's generation distribution without being a hidden proof.

One strategy is one frozen sample. Alternative strategies are generated/evaluated separately so downstream credit is attributable.

## Intuition-generator input

Primary generator input contains only a name-free generic theorem presentation and the structural background required to understand it.

Do not expose:

- theorem/declaration name;
- reference proof;
- neighboring source lemmas or source comments;
- human/frontier reference intuition;
- qwen-lean outputs;
- private formal-target metadata;
- concrete numeral instances as mathematical evidence.

Where possible, create an alpha-renamed or notation-varied presentation. This is a robustness check on the intuition generator only; it does not change the private formal theorem proved by qwen-lean.

The private formal target may contain Lean implementation syntax and literals because the Mathia semantic-input boundary does not constrain the verifier/formal specialist.

## Frozen semantic request

The v1 request semantics are:

> Propose one compact mathematical strategy for why the result should hold and how a proof might be organized. Identify the main mechanism or representation and a small number of useful intermediate mathematical goals if needed. Mention an obstruction or essential assumption only if it materially guides the route. Do not write the proof.

Surface wording and exact token limit freeze in #32, but they must preserve this semantic contract.

Disallowed output:

- Lean code;
- tactic names;
- library theorem/lemma identifiers;
- source/declaration names;
- line-by-line formal derivation;
- a near-complete informal proof whose remaining work is transcription.

## Leakage classification

Every generated intuition is classified **before** its corresponding qwen-lean outcome is known:

- `strategic` — useful mechanism/representation/subgoal guidance with substantial proof work remaining;
- `borderline` — enough derivation that causal interpretation is doubtful;
- `proof_like` — essentially supplies a proof or library implementation route.

Only `strategic` outputs enter the primary fertility comparison. Borderline/proof-like frequency is itself a generator result. Do not rewrite or sanitize generated samples after qwen-lean evidence exists.

## Candidate theorem panel

The exact Mathia-visible presentations, factual controls, audit-only strategy references, cross-pairing, and leakage notes live in `INTUITION_FERTILITY_PANEL_V0.md`. Human-readable external documentation is listed separately in `INTUITION_FERTILITY_SOURCES_V0.md` and is private from primary generation.

Candidate private formal targets:

| Role | Target | Reason |
|---|---|---|
| floor calibration | `Subgroup.card_subgroup_dvd_card` | simple coset/quotient decomposition; tests whether the guidance interface can matter at all |
| medium calibration | `LinearMap.rank_range_add_rank_ker` | information-loss / quotient-to-range representation |
| medium transfer | `MulAction.card_orbit_mul_card_stabilizer_eq_card_group` | quotient/redundancy mechanism in a group-action realization |
| hard | `Function.Embedding.schroeder_bernstein_of_rel` | stable decomposition plus piecewise bijection; substantive proof-bearing target |
| hard | `HallMarriageTheorem.hall_hard_inductive` | tight-set/slack dichotomy, recursion, and synthesis; substantive proof-bearing target |
| domain diversity | `IsCompact.image_of_continuousOn` | preservation/transport under continuous maps; non-group/non-cardinality surface |

Easy/medium items may be ceiling for a competent formal worker because nearby mathlib structure makes them short. Treat them as channel/floor calibration. Claims about useful strategic guidance should rely primarily on non-ceiling behavior, especially the proof-bearing hard targets.

## Documentation versus ground truth

Theorems are intentionally documented beyond their Lean proof. Public course/text references are kept for audit and post-hoc interpretation, not fed to the generator.

Possible uses after outputs/results are frozen:

- compare whether a generated strategy recovered a known mechanism;
- identify a different but productive mechanism;
- diagnose teacher imitation of canonical exposition;
- distinguish a mathematically useful strategy from the exact route taken by mathlib's proof.

Similarity to documentation is auxiliary evidence. Lean-verified downstream effect is the hard signal.

## qwen-lean target-exposure gate

The formal worker must not be evaluated on an exact proof it was directly fitted on.

qwen-lean Phase-2 uses file/component-disjoint `train`, `validation`, and `heldout` splits. Current SFT fitting consumes train records. Before v1 can freeze:

- resolve every candidate target's exact Phase-2 record identity and split from the actual artifact;
- record the exact qwen-lean checkpoint lineage to be used in #32;
- exclude every target used in optimizer fitting for that checkpoint;
- prefer heldout targets;
- permit validation only with explicit notation that checkpoint/model selection may have consulted validation;
- if a candidate is train-exposed, replace it deliberately under #30 and re-audit its statement/control/reference. #31 does not choose replacements.

Base-model pretraining familiarity is allowed for this calibration and reported as a limitation. Direct qwen-lean post-training exposure is an exclusion because it can saturate the proposed reward instrument.

## Current formal-worker semantics

The inspected qwen-lean runtime renders a plain whole-proof request ending in an exact declaration followed by `:= by`, generates the continuation, reconstructs the source, and accepts proof success only when Lean verifies the candidate.

Therefore v1 measures **verified whole-proof generation fertility**. It does not claim to measure interactive tactic-search quality.

Primary v1 metrics must not depend on search-node count, proof-state navigation, or automatically generated intermediate-lemma trees unless qwen-lean has explicitly acquired those capabilities before the #32 freeze.

## Guidance intervention

For theorem `T` and frozen guidance `I`, guided qwen-lean receives the same proof-generation request as baseline plus one bounded Lean comment carrying `I` immediately before the exact declaration/proof continuation.

Conceptual rendering:

```text
/- existing whole-proof instruction -/
/- Strategic hint: <frozen guidance> -/
<exact declaration> := by
  <generated continuation>
```

#31 owns serialization mechanics. Required scientific invariants:

- exact theorem declaration unchanged;
- exact formal-worker checkpoint/tokenizer unchanged;
- candidate budget and generation settings matched across conditions;
- verifier identical;
- guidance text is outside the generated proof continuation;
- no proof/reference lemma list/private source material enters guidance conditions;
- prompts can be diffed so only the intended intervention differs.

Any guidance text containing a Lean comment terminator/opener or other serialization-breaking material must be rejected/escaped by deterministic mechanics without changing its mathematical content post hoc.

## Controls

### `no_guidance`

The current qwen-lean whole-proof request with no added comment.

### `factual_control`

A theorem-specific but strategy-free restatement of facts already visible in the declaration. Render it in the same comment position and approximately the same length as strategic guidance. This controls extra tokens, theorem vocabulary, and theorem-specific semantic priming.

### `generic_strategy_control`

A theorem-independent, strategy-shaped comment. It controls the possibility that merely telling qwen-lean to think structurally helps.

Candidate frozen semantic content:

> Look for a representation that exposes the structural reason for the conclusion. Check whether the problem can be decomposed, whether an invariant or reversible transformation is relevant, and whether an equivalent formulation removes unnecessary casework or assumptions. Choose the viewpoint that makes the target most direct.

The exact final text/length freezes before #32 results and is identical across theorem targets except for mechanical escaping.

### `cross_theorem_strategy`

A frozen strategy generated for another theorem, using conceptually adjacent pairings so irrelevance is not obvious from style or topic words.

Initial derangement:

- subgroup-cardinality ↔ orbit/stabilizer;
- rank/kernel ↔ compact-image transport;
- two-injections ↔ Hall matching.

Cross guidance may genuinely help through transfer. Do not require a null effect; interpret its pattern.

### `qwen_base_intuition`

Strategic samples from the exact common base under the frozen intuition task.

### `codex_reference_intuition`

Strategic samples from the explicitly recorded Codex/frontier configuration under the same bounded task. This is a strong reference/channel probe, not an independent judge.

### future `mathia_intuition`

The exact same intervention accepts later Mathia checkpoints without redesigning the scientific comparison.

A human documented strategy can be auxiliary if it passes the same length/leakage interface.

## Primary fertility outcomes

For each theorem/condition under the fixed qwen-lean candidate budget:

- raw number and fraction of Lean-verified candidates;
- pass@k / whether any candidate verifies within the frozen budget;
- theorem-level uplift versus `no_guidance`;
- theorem-level uplift versus `factual_control`;
- theorem-level uplift versus `generic_strategy_control`.

Theorem-level results remain visible. Do not hide ceiling/floor behavior inside a single aggregate.

## Secondary outcomes

When a verified candidate exists:

- candidate index/rank of first verified proof under deterministic output ordering;
- generated tokens consumed through first verified candidate;
- generation/verification runtime when meaningfully comparable.

These are sampling-cost proxies, not tactic-search complexity.

## Candidate budget

Do not inherit the small qwen-lean heldout candidate count mechanically. This experiment has few theorem/condition cells and seeks an intuition-level yield signal; too few candidates will make the estimate uninformative.

#32 must freeze a candidate budget large enough to estimate within-theorem differences while remaining bounded by available compute. The budget must be chosen before comparative outcomes, not increased only for cells that look ambiguous.

## What validates the reward channel

The channel is not validated merely by good-looking teacher output. A useful #32 result needs:

- at least some non-ceiling targets where guidance condition changes verified yield;
- strong/reference relevant guidance outperforming unguided/factual/generic controls on at least part of the panel without proof leakage;
- no universal effect where every strategy-shaped comment helps equally;
- enough Qwen-base/reference gap or intuition-to-intuition outcome variance to create learnable headroom;
- theorem-specific patterns that can be explained mathematically rather than only by prompt length/style.

A cross-theorem hint can sometimes help. That is evidence of transfer if the mechanism fits, not a reason to erase the observation.

## What blocks the reward channel

Return to design rather than train Mathia if:

- strong reference guidance cannot change non-ceiling qwen-lean yield;
- effects are reproduced by factual or generic-strategy controls;
- relevant hints need to contain near-complete proofs to help;
- target-proof post-training exposure cannot be excluded;
- all retained targets are ceiling/floor;
- results depend mainly on serialization/comment artifacts;
- the formal worker cannot exploit natural-language strategic information at its current capacity.

A qwen-lean generation failure is not evidence that an intuition or theorem is false.

## Genericity and representation robustness

For each retained theorem, produce at least one name-free alpha-renamed or notation-varied intuition-generator presentation. This is intentionally small-scale.

A useful conceptual generator should not require the canonical theorem name or incidental symbol names. Variation is not a proof of understanding, but failure under trivial renaming is evidence against the task/model.

## Remaining #30 gates

### Gate A — target-split lookup

Using the actual qwen-lean Phase-2 artifact, resolve the six private targets to record IDs and splits and record the qwen-lean checkpoint exposure. This is CPU-only.

If any target is train-exposed, replace it under #30, update the panel/reference source set, and re-run internal leakage/fidelity checks.

### Gate B — exact panel freeze

After Gate A, freeze:

- private formal targets;
- exact name-free Mathia-visible statements;
- factual controls;
- generic-strategy control;
- deterministic cross-theorem mapping;
- documentation references;
- leakage-review examples;
- genericity variants.

### Gate C — fresh-context independent review

The reviewer must attack at least:

- concept/dimension redundancy;
- verbal/expository rather than strategic task behavior;
- theorem wording that leaks the intended representation;
- proof-like strategy leakage;
- factual controls that contain strategy;
- generic strategy reproducing relevant-guidance gains;
- comment/OOD/extra-token effects;
- cross controls that are trivial by style;
- exact target training exposure;
- whole-proof generation being mislabeled as search;
- teacher/reference similarity becoming truth;
- solver-specific prompt hacking;
- proof-generation failure being treated as refutation;
- arithmetic/theorem-name surface shortcuts;
- alpha-renaming/representation fragility;
- inability to produce evidence against the hypothesis.

Iterate `review -> fix -> fresh review` until `PASS`, genuinely non-material `PASS_WITH_NOTES`, or `BLOCKED`.

## Exit condition

#30 closes only after Gate A, Gate B, and Gate C are complete. At that point #31 should be able to implement mechanics without inventing theorem replacements, redefining intuition, choosing scientific controls, or reinterpreting the qwen-lean reward signal.
