# Intuition-fertility pre-test v0

## Status

This document is the working scientific contract produced under issue #30. It narrows the earlier `concepts -> conceptual dimensions -> intuition -> fertility` hypothesis enough to support a small pre-test without turning the current vocabulary into a permanent Mathia ontology or training pipeline.

The pre-test has two purposes before Mathia-specific post-training begins:

1. measure how much compact strategic mathematical guidance the exact Qwen base and a strong frontier teacher can already generate from theorem statements; and
2. test whether such frozen guidance causally changes the verified whole-proof generation yield of the current qwen-lean formal worker under matched inference budgets.

The second purpose is the critical gate. If a strong reference intuition cannot measurably change qwen-lean outcomes, qwen-lean is not yet a useful reward instrument for training Mathia, regardless of how good the intuition sounds.

This is a calibration experiment, not a held-out mathematical-discovery benchmark. Famous and likely pretraining-exposed theorems are allowed for the intuition generator. Exact target-proof exposure during qwen-lean post-training is treated differently and is excluded below.

## What #30 resolves and what it deliberately does not

#30 resolves a provisional concept substrate, a smaller set of behaviorally distinguishable conceptual moves, an intuition-generation task, a proof-leakage policy, an initial theorem panel, the qwen-lean guidance intervention, controls, and interpretation semantics.

It does not decide a final concept curriculum, dataset schema, SFT format, preference/RL algorithm, final model size, model merging, or three-layer orchestration. The labels below exist to make the experiment discriminating; later evidence may merge, split, rename, or discard them.

## 1. Provisional concept substrate

The first pre-test does not need a complete map of mathematics. The following concept families are enough to exercise the working hypothesis across several domains.

### Maps, composition, and information flow

A map is viewed as a transformation that may preserve, identify, or discard distinctions. Composition propagates those effects. The semantic target is not function evaluation but reasoning about what information can reach the output and how properties behave through composed transformations.

### Reversibility and inverse structure

Reversibility means that the information relevant to a transformation can be recovered. Left/right inverses, injectivity, surjectivity, and bijectivity are related but should not collapse into one memorized slogan. The model should reason about which direction of reversibility is actually needed.

### Equivalence, fibers, kernels, and quotients

These concepts describe controlled indistinguishability. If a transformation cannot distinguish two inputs, an equivalence-like relation or fiber structure records the lost distinction; quotienting can turn that loss into a new representation on which the transformation becomes faithful to the remaining information.

### Decomposition, products, and partitions

Objects or problems can often be split into parts with different roles and later reconstructed or counted from those parts. This family includes componentwise/product viewpoints, partitioning into classes or cases, and decompositions induced by a map or constraint.

### Symmetry, actions, orbits, stabilizers, and invariants

A symmetry/action separates meaningful variation from redundant motion. Orbits describe what can change under the action; stabilizers describe transformations that leave an object unchanged; invariants survive the allowed transformations.

### Representation, factorization, and bridges

The same mathematical situation may admit several descriptions. A useful intermediate object, quotient, equivalence, factorization, coordinate system, or other bridge may expose the mechanism and reduce irrelevant structure.

`Necessary/sufficient condition` is not retained as a separate concept family in this pre-test. It is a reasoning relation used especially by generalization and stress-testing.

## 2. Provisional conceptual moves

The earlier Mathia brainstorming contained more than a dozen labels. For #30 they are reduced to eight moves that can be distinguished by mathematical behavior rather than terminology alone.

### Transfer

Recognize that roles and relations from one mathematical setting instantiate the same mechanism in another setting, then import consequences while respecting differences between the domains.

**Discriminator:** abstraction may identify a mechanism, but transfer is the act of applying it to a new realization. Recognizing that quotient-by-redundancy explains both kernel/range and orbit/stabilizer is abstraction; using the kernel/range viewpoint to propose the orbit/stabilizer quotient is transfer.

### Decompose

Split an object, domain, constraint system, or proof obligation into structurally meaningful parts whose separate roles become easier to analyze.

**Discriminator:** Hall-style separation into a tight subset and its complement is decomposition without changing the mathematical language of the problem.

### Synthesize

Combine independently obtained components, viewpoints, or partial constructions into a coherent whole.

**Discriminator:** solving two sides of a Hall decomposition and joining the two matchings is synthesis. It is not merely identifying an intermediate representation.

### Abstract / compress

Remove presentation-specific detail and identify a smaller mechanism that explains several local facts or apparently different statements.

**Discriminator:** the output is a more general structural description, not necessarily a new representation of the same individual problem.

### Reframe / bridge

Change mathematical representation, or introduce an intermediate object that translates the original problem into a space where the relevant relation is easier to see.

**Discriminator:** quotienting a domain by a kernel and identifying the quotient with the range is a reframe/bridge. The underlying source object has not merely been split into cases.

`Bridge construction` is therefore treated as a subtype of reframing in v0 rather than a separate dimension.

### Generalize / weaken assumptions

Identify which assumptions or presentation details are stronger than the mechanism requires, and formulate a broader or sharper statement suggested by that mechanism.

**Discriminator:** this move proposes a new statement or assumption boundary. It differs from stress-testing, which probes where the current mechanism breaks.

### Stress-test

Apply counterfactual changes or search for a falsifying structural situation to identify the first obstruction, missing condition, or limit of an analogy.

`Counterfactual reasoning` and `falsification` are merged here because both intervene on the proposed mechanism to locate failure. They may be separated later if data show behaviorally distinct skills.

### Select

Choose among several legitimate representations or strategies according to expected downstream mathematical utility for the current target.

`Simplification`, `naturalness/canonicality`, and related aesthetic signals are treated as possible selection criteria or outcomes rather than independent moves. `Multiple perspectives` is treated as repeated generation of reframings, followed by selection.

## 3. Rejected or merged dimension labels in v0

The following labels are not discarded as mathematical ideas; they are simply not retained as independent train/evaluation dimensions in this experiment.

- **simplification** -> desired consequence of a reframe or selection;
- **multiple perspectives** -> generating multiple reframings, not a separate operation;
- **naturalness / canonicality** -> criterion for selecting a representation;
- **prediction** -> consequence of any sufficiently specific intuition and therefore part of evaluation;
- **falsification + counterfactual** -> merged as `stress-test`;
- **bridge construction** -> included in `reframe / bridge`;
- **fertility** -> downstream evaluation signal, not a conceptual move.

This reduction is intentionally provisional. A later training corpus should not encode these labels as ground-truth ontology without independent evidence that the distinction helps learning or evaluation.

## 4. What counts as an intuition in the pre-test

For this experiment an intuition is a **compact strategic proposal** for how a theorem should be approached. It may identify a mechanism, a useful representation, an intermediate object, one or two likely subgoals, an assumption that carries the conclusion, or an obstruction worth testing.

It is not required to match a canonical historical explanation. It is not required to be immediately true in every detail. It must, however, be specific enough that giving it to a separate formal worker could plausibly change what proofs that worker generates.

The unit of evaluation is one frozen intuition. If several substantially different strategies are desired, generate and evaluate them as separate samples rather than placing a menu of strategies inside one response and making credit assignment ambiguous.

## 5. Intuition-generator input

The intuition generator receives a generic mathematical presentation of the theorem and only the background needed to understand the statement.

For the primary pre-test:

- hide the theorem/declaration name from the intuition generator;
- do not provide the reference proof, neighboring source lemmas, source-file comments, historical explanation, teacher intuition, or qwen-lean result;
- preserve generic objects, relations, assumptions, and structural roles;
- do not introduce concrete numeral instances as mathematical evidence;
- alpha-rename incidental identifiers where this can be done without changing mathematical meaning;
- preserve enough type/structural information that the task remains mathematics rather than an underspecified verbal riddle.

The private formal target may retain Lean syntax and literal implementation details. The no-concrete-instance constraint applies to Mathia-facing primary mathematical content, not to the formal worker or verifier.

For a formal target whose exact Lean declaration contains an incidental literal required by its implementation statement, #31 may render a semantically equivalent generic natural-language presentation for the intuition generator. That mapping must be reviewed for faithfulness and kept separate from the qwen-lean prompt.

## 6. Intuition-generator request

The exact surface wording can be tuned during #30 audit, but its semantic contract is:

> Given the theorem statement, propose one compact mathematical strategy for why the result should hold and how a proof might be organized. Identify the main mechanism or representation and at most one or two intermediate mathematical goals if useful. Mention a relevant obstruction or assumption only when it materially guides the route. Do not write the proof.

Primary intuition output must not contain:

- Lean code;
- tactic names;
- mathlib theorem/lemma identifiers;
- the source file or original declaration name;
- a line-by-line derivation;
- a near-complete informal proof that leaves only transcription to the formal worker.

A bounded short response is required so that `more tokens` is not itself the treatment. #32 freezes the exact token limit; #31 only needs to preserve and hash the accepted output exactly.

## 7. Proof-leakage policy

Proof leakage is a scientific failure because an almost-complete proof can trivially improve a proof generator without demonstrating strategic intuition.

Each generated intuition used in the primary comparison must receive a pre-qwen-lean leakage classification:

- **strategic** — mechanism/representation/subgoal guidance while substantial derivation remains;
- **borderline** — contains enough local derivation that causal interpretation is doubtful;
- **proof-like** — essentially supplies the proof or library-specific implementation route.

Only `strategic` outputs enter the primary fertility comparison. Borderline/proof-like rates are reported as generator behavior, not silently sanitized. Once a generated intuition is frozen, it cannot be rewritten after qwen-lean outcomes are observed.

The classifier may combine deterministic rules with independent mathematical review. An AI judge may assist, but it is not mathematical ground truth.

## 8. Initial theorem panel

The panel is deliberately small and heterogeneous. It mixes easy calibration items, medium representation-change items, and proof-bearing harder items. All formal targets are available in the qwen-lean pinned mathlib line (`v4.32.0` / its resolved source revision), but exact Phase-2 split membership still has to be checked against the local qwen-lean artifact before #30 can freeze the panel.

| Role | Private formal target | Source file | Main concepts/moves | Reason for inclusion |
|---|---|---|---|---|
| easy/floor | `Subgroup.card_subgroup_dvd_card` | `Mathlib/GroupTheory/Coset/Card.lean` | quotient, decomposition | Lagrange: cosets/factorization give a simple known strategy; useful for testing whether the guidance channel works at all. |
| medium | `LinearMap.rank_range_add_rank_ker` | `Mathlib/LinearAlgebra/Dimension/RankNullity.lean` | kernel, quotient, information loss, bridge | Rank-nullity: quotient by invisible information and identify the quotient with the range. |
| medium | `MulAction.card_orbit_mul_card_stabilizer_eq_card_group` | `Mathlib/GroupTheory/GroupAction/Quotient.lean` | action, orbit, stabilizer, quotient, transfer | Tests transfer of the quotient/redundancy pattern from maps to group actions. |
| hard | `Function.Embedding.schroeder_bernstein_of_rel` | `Mathlib/SetTheory/Cardinal/SchroederBernstein.lean` | injections, decomposition, synthesis, fixed-point reframe | Proof-bearing core theorem: choose a stable region for the forward injection and use the inverse of the other injection on the complement. |
| hard | `HallMarriageTheorem.hall_hard_inductive` | `Mathlib/Combinatorics/Hall/Finite.lean` | tightness, decomposition, synthesis, stress-test | Proof-bearing core: distinguish slack everywhere from a tight subset, recurse appropriately, and combine. |
| diversity/medium | `IsCompact.image_of_continuousOn` | `Mathlib/Topology/Compactness/Compact.lean` | preservation under maps, transport, reframe | Adds topology and a transport/preservation mechanism so the panel is not dominated by quotient/group language. |

The named famous theorem may be presented differently from the exact private declaration. The intuition generator should see a name-free generic statement. The qwen-lean worker receives the exact formal target under its normal formal semantics.

### Split-exposure gate

The current qwen-lean Phase-2 corpus assigns entire file/components to `train`, `validation`, or `heldout`, and the current full SFT phase fits only eligible records from `train`. Therefore the target proof for this pre-test must not have been used in optimizer training for the qwen-lean checkpoint being measured.

Before freezing the panel, resolve each target against the exact Phase-2 artifact and the exact qwen-lean checkpoint lineage:

- target record must exist as an eligible theorem/lemma in the Phase-2 corpus or be represented by an explicitly equivalent local target accepted by the same verifier contract;
- target record/component must not be in the optimizer-training split for the selected qwen-lean checkpoint;
- validation targets are permitted for this calibration only if they were not used for qwen-lean fitting; if checkpoint selection used validation, mark this as model-selection exposure;
- heldout is preferred when available;
- if a proposed target is in `train`, return that row to #30 design and replace it deliberately. #31 must not choose a convenient substitute on its own.

Qwen-base pretraining familiarity is recorded but is **not** an exclusion rule for this calibration. Direct qwen-lean SFT exposure to the target proof is an exclusion rule because it can saturate or distort the fertility measurement.

## 9. qwen-lean is currently a whole-proof generator

The first fertility experiment must match the capability that qwen-lean actually exposes. The current qwen-lean contract asks the model to generate a complete Lean continuation after `by`, and Lean verifies the raw continuation. Tactic-level interactive proof search is a later qwen-lean milestone.

Therefore #30 uses **verified whole-proof generation fertility**, not tactic-search fertility, as the first hard signal.

Do not make intermediate search-node count, proof-state navigation, or automatically generated intermediate lemmas primary metrics in v0 unless qwen-lean has acquired those explicit capabilities before #32 is frozen.

## 10. qwen-lean guidance intervention

Keep Mathia/Qwen/Codex intuition generation separate from the formal worker.

For every theorem and intuition, freeze the intuition before any corresponding guided qwen-lean result exists. The guided condition should make the smallest possible change to the existing qwen-lean proof request: append a bounded natural-language mathematical strategy as a Lean comment before the declaration/proof continuation while preserving the exact theorem declaration, model/checkpoint, tokenizer, generation settings, candidate budget, verifier, and all other prompt bytes.

Conceptually:

```text
/- Complete the proof below ... -/
/- Strategic hint: <frozen intuition> -/
<exact declaration> := by
  <qwen-lean continuation>
```

The actual serializer belongs to #31, but it must make byte-level condition differences inspectable and keep the strategy outside the generated Lean continuation. No hidden source proof or reference lemma list may be added in guided conditions.

The unguided condition remains the existing qwen-lean proof request with no strategic comment.

## 11. Control conditions

The pre-test needs more than `no intuition` versus `good intuition` because extra relevant text can prime a language model even when it carries no strategy.

Required conditions are:

### `no_guidance`

Existing qwen-lean proof request with no additional mathematical text.

### `factual_control`

A short same-theorem, strategy-free restatement of information already explicit in the declaration. Match length to the strategic hints as closely as practical without adding new mathematical content. This controls for extra tokens, local vocabulary, and theorem-specific semantic priming.

### `cross_theorem_strategy`

A strategic hint frozen for another theorem. Pairing should avoid trivially unrelated vocabulary when possible. The goal is to test relevance, not whether qwen-lean can detect a topic mismatch from surface words.

A cross-theorem strategy is allowed to help if the underlying abstraction genuinely transfers. Such cases are mathematically interesting and must not be relabeled as control failures after results are known.

### `qwen_base_intuition`

One or more strategic samples produced by the exact common Qwen base under the frozen intuition task.

### `codex_reference_intuition`

One or more strategic samples produced by the recorded frontier/Codex configuration. This is a strong reference and a channel diagnostic, not an independent held-out judge.

### later `mathia_intuition`

The same interface must accept future Mathia checkpoints without changing the scientific meaning of the comparison.

A documented human strategy may be added as an auxiliary reference only if it is rendered through the same bounded interface and leakage policy.

## 12. Fertility outcomes

Because v0 uses whole-proof generation, the primary evidence is simple and verifier-grounded.

### Primary outcomes

Per theorem and condition record:

- number and fraction of raw candidates accepted by Lean;
- pass@k / whether at least one verified proof is found within the frozen candidate budget;
- matched uplift versus `no_guidance` and `factual_control` on the same theorem.

Do not collapse theorem-level behavior immediately into one opaque global score. Ceiling and floor theorems have different diagnostic meaning.

### Secondary cost outcomes

When a verified proof exists, record as secondary evidence:

- candidate index/rank of the first verified proof under deterministic candidate ordering;
- generated tokens consumed up to the first verified candidate;
- generation and verification runtime when comparable.

These are imperfect proxies for search cost under independent sampling, so they must not be described as tactic-search complexity.

### Non-primary observations

AI judgments about elegance, similarity to documented intuition, naturalness, or explanatory quality are auxiliary. They may help interpret why an intuition worked but cannot override formal outcomes.

## 13. Interpreting the channel before training Mathia

The pre-test is not positive merely because Codex writes plausible strategies.

The proposed qwen-lean reward channel is considered informative only if the data contain a separable causal signal. In particular:

- at least some non-ceiling targets must respond to relevant strategic guidance;
- Codex/reference guidance should outperform `no_guidance`/`factual_control` on some targets without the gain being attributable to proof leakage;
- shuffled/cross-theorem guidance should not reproduce the same pattern indiscriminately;
- there should be enough difference between Qwen-base and strong-reference guidance, or enough within-model intuition variance, to make later specialization measurable.

If Codex/reference guidance produces no interpretable uplift, do not start Mathia fertility optimization. Possible explanations include a poor intervention interface, inappropriate theorem difficulty, an already-saturated formal worker, or a formal worker that cannot exploit natural-language strategy.

If all conditions are at ceiling or floor, revise theorem difficulty rather than treating the result as evidence for or against intuition.

## 14. Main alternative explanations and required attacks

### Explanation-style distillation

Mathia could learn to sound like Codex without increasing verified proof yield. Teacher similarity must therefore remain separate from fertility.

### Near-proof leakage

A detailed hint can function as a hidden proof. The leakage classifier and compact-output constraint are mandatory.

### Extra-token or vocabulary priming

Relevant words alone may improve next-token generation. `factual_control` exists specifically to attack this explanation.

### Solver-specific prompt optimization

An intuition could become a prompt hack specialized to one qwen-lean checkpoint. v0 can establish only solver-conditional fertility. Later transfer should vary notation/presentation and, when practical, formal-worker checkpoint or solver.

### Formal-worker target memorization

If qwen-lean trained directly on the exact target proof, success under a hint is difficult to interpret. The split-exposure gate excludes this.

### Base-model theorem familiarity

Qwen base may remember famous theorem proofs. This is permitted in the calibration but limits claims about novel generalization. Hide theorem names from the intuition generator and later add less canonical/protected evaluations if training proceeds.

### Strategy/reference leakage through repository context

Reference proof, source comments, nearby lemmas, human/Codex strategy, and private theorem documentation must not enter the intuition generator input or primary factual control.

### Genericity failure

Where a theorem presentation permits it, generate alpha-renamed or notation-swapped intuition inputs. A candidate conceptual ability that disappears under incidental renaming is not strong evidence of semantic understanding.

## 15. What #31 must be able to implement without scientific invention

Once the split-exposure gate and independent audit pass, #31 should only need to implement mechanics:

- materialize the accepted theorem targets and name-free intuition presentations;
- capture/freeze/hash Qwen-base and Codex intuition samples;
- classify/record leakage before qwen-lean outcomes;
- construct `no_guidance`, `factual_control`, deterministic cross-theorem, and relevant-guidance qwen-lean prompts;
- preserve exact condition parity and provenance;
- run/import matched whole-proof candidate generations;
- link every proof success to Lean verification;
- compute the accepted per-theorem fertility summaries.

If #31 has to decide what `intuition` means, choose theorem replacements, invent a new control, choose which outputs count as proof-like, or redefine the reward because current qwen-lean does not expose it, #30 is not finished.

## 16. Remaining pre-freeze evidence required by #30

This design is not yet `PASS` solely because it is written down. Before #30 closes:

1. resolve the exact Phase-2 split and qwen-lean training exposure of all proposed panel targets;
2. replace any train-exposed target deliberately in #30;
3. produce exact name-free Mathia-visible statements for the retained panel and verify that they preserve theorem meaning without concrete-instance dependence;
4. produce at least one example `factual_control` and one strategic reference hint per retained theorem so leakage/length/relevance can be audited concretely;
5. run a fresh-context independent adversarial review of the full target, especially dimension redundancy, proof leakage, token/vocabulary priming, target exposure, and qwen-lean channel semantics;
6. fix material findings and repeat review until `PASS`, genuinely non-material `PASS_WITH_NOTES`, or `BLOCKED`.

Only then should #31 implement the harness.
