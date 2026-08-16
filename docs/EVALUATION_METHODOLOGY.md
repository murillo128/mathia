# Evaluation methodology: evidence for semantic mathematical capability

## Status

This document records Mathia's methodological stance for evaluation. It is not a fixed benchmark suite or execution schedule.

The semantic-intuition reset changes the **internal diagnostic target**, but preserves the broader principle that Mathia should eventually be judged by mathematical behavior that transfers beyond its own training environment.

## Keep capability layers separate

Mathia should avoid collapsing several different questions into one score.

### Semantic / conceptual capability

Can the model understand and use mathematical meaning, representation, invariance, reversibility, information loss, analogy, and mechanism-level structure?

### Execution capability

Can it correctly carry out calculations, algorithms, symbolic manipulations, or other instance-level procedures?

### Formal capability

Can it formalize a claim precisely and produce a kernel-verified proof or counterexample?

### Research capability

Can its ideas improve a longer mathematical investigation: generating useful lemmas, reformulations, falsifiers, or directions?

These capabilities may interact, but improvement in one is not automatic evidence of improvement in another.

## Evidence classes

Mathia should distinguish at least four evidence classes.

### Development diagnostics

Small cheap checks for broken prompts, serialization, model loading, parsing, scoring, or obvious task defects.

They should not become the scientific result.

### Internal semantic-intuition evaluation

The current #29 line asks whether generic structural intuition improves unseen semantic interventions without arithmetic execution.

This benchmark may guide research because it directly tests the hypothesis. It should include strong controls and robustness transformations such as alpha-renaming and representation change.

Because Mathia designs this benchmark itself, success here is necessary evidence for the training signal but not sufficient evidence of broad mathematical improvement.

### External mathematical validation

Later, independently designed mathematical tasks should test whether any trained capability transfers outside Mathia's own environment.

These tasks should remain protected from repeated item-level tuning as far as practical.

Relevant external families may include structural perturbation, falsification/counterexamples, mathematical construction, research-level reasoning, and formal theorem proving. The final suite should be chosen when the trained model and contemporary baselines are known rather than frozen now.

### Open-ended research evidence

A later three-layer system may work on open or research-style problems where no final answer is known.

In that setting, evaluation should track intermediate mathematical progress such as:

- verified implications;
- formally proved restricted cases;
- verified counterexamples to proposed auxiliary claims;
- useful equivalent reformulations;
- reduction of assumptions;
- independently rediscovered known results;
- genuinely new intermediate claims that survive expert/formal scrutiny;
- later reuse/fertility of an idea.

Do not equate failure to solve the final problem with zero research progress, and do not equate plausible prose with progress.

## Current semantic benchmark: what must be controlled

The first semantic-intuition diagnostic must rule out simpler explanations.

### Arithmetic execution confound

Primary tasks should not require concrete calculation. If ordinary arithmetic competence can carry the result, the benchmark does not isolate the intended layer.

### Extra-token / information confound

Compare structural context with factual and local-rule controls rather than only with no context.

### Conceptual-rhetoric confound

Use fluent-but-sterile context to test whether mathematical-sounding prose is rewarded regardless of mechanism.

### Relevance confound

Use shuffled/irrelevant good intuitions to test whether any structural vocabulary helps.

### Wrong-mechanism sensitivity

A plausible wrong intuition should make at least one specific false downstream prediction. If wrong context never hurts, the solver may not be using the representation meaningfully.

### Surface-form confound

Use alpha-renaming, notation changes, and representation variants where possible. A semantic capability should not be tightly tied to arbitrary symbol names.

### Answer leakage

Structural context must not simply state the hidden intervention's answer in another form.

## Commit before the hidden intervention

The core causal structure remains:

```text
same generic situation
        |
candidate context / intuition
        |
     commit
        |
unseen intervention
        |
measured outcome
```

This makes it harder for the "intuition" to be a post-hoc solution tailored to the visible question.

## Measure interactions, not only aggregate accuracy

The desired effect is selective.

A structural intuition might help strongly on representation transfer or counterfactual reasoning while offering no advantage on a local rule question. That pattern is more informative than a single average score.

Pre-register breakdowns by:

- context condition;
- intervention family;
- mechanism family;
- representation/renaming variant where available.

Report uncertainty and small-cell limitations explicitly.

## Negative results

Treat the following as evidence rather than engineering failures:

- structural context does not beat strong controls;
- sterile context reproduces the gain;
- wrong context has no effect;
- renaming destroys performance;
- the benchmark is at ceiling/floor;
- the target model cannot exploit the representation;
- the benchmark cannot provide exact enough ground truth without reintroducing execution.

Different failures imply different next steps. Do not automatically respond with more training or larger hardware.

## AI-judged evidence

AI judges can be useful for dimensions that are hard to formalize, such as:

- whether two proposed intuitions are genuinely distinct;
- whether an explanation is merely a paraphrase;
- whether a representation is natural or ad hoc;
- whether a proposed bridge is conceptually meaningful;
- whether generated alternatives cover different mechanisms.

These judgments should be recorded as **soft evidence** and kept separate from mathematical correctness.

Where an AI judge is also a teacher or frontier director, avoid reporting its preference as independent validation of a student distilled from the same family of judgments.

## Formal verification evidence

Formal systems provide powerful exact signals but require careful interpretation.

Keep separate:

- informal-statement fidelity;
- formalization success;
- proof success;
- counterexample/refutation success;
- prover failure.

A proof checked by Lean is strong evidence for the exact formal proposition. A failed proof search is not evidence that the proposition is false. A well-typed formalization may still encode the wrong informal claim.

## Benchmark isolation and contamination

For external validation, the strongest evidence comes when:

- evaluation items are not intentionally used for Mathia training;
- solutions/judge traces are not converted into targets;
- prompts are not tuned against item-level failures;
- the final inference protocol is frozen before comparative results;
- contamination inherited from the base model is acknowledged.

Public benchmarks are imperfect held-out tests because the base model may have encountered related material in pretraining. Recent/refreshed or procedurally modified evaluations can be useful when they reduce verbatim contamination, but no suite should be treated as perfectly clean without evidence.

## Compare against the exact base and strong alternatives

The primary causal comparison for Mathia post-training should include the exact base checkpoint under matched inference conditions.

Also preserve adversarial baselines such as:

- compute-matched ordinary math/solver post-training;
- explanation-only SFT;
- generic local reasoning without Mathia specialization;
- stronger contemporary open/closed models as capability references when protocols are comparable.

A Mathia model does not need to beat a frontier model to produce scientifically interesting evidence. The key question is whether its **pattern of gains** matches the claimed conceptual capability and exceeds simpler training explanations.

## Fair inference comparison

Record enough inference detail to distinguish model quality from test-time compute:

- model/checkpoint and tokenizer;
- prompt/template;
- output/reasoning budget;
- sampling policy;
- tools/retrieval/formal verifiers;
- number of attempts;
- aggregation rule;
- hardware/throughput when runtime matters.

When comparing Mathia with its exact base, hold these fixed unless test-time scaling is itself the experiment.

## Scaling diagnosis

If the local model performs poorly, distinguish:

```text
bad benchmark
vs
no semantic signal
vs
model-capacity floor
vs
insufficient inference budget
```

A stronger model can be used to estimate whether the task is solvable as intended, but using it to redesign every item after seeing failures can contaminate the benchmark.

## External success profile

A particularly interesting future result would be:

- modest change on ordinary calculation;
- larger gains on representation transfer;
- larger gains on falsification/diagnosis;
- better structural perturbation robustness;
- better generation of valid generalizations or useful intermediate claims.

Such a profile would be more consistent with changed conceptual capability than a uniform accuracy gain everywhere.

Conversely, improvement only on Mathia-authored conceptual prose tasks with no external behavioral transfer would support the alternative hypothesis that training mainly teaches a style of explanation.

## Current methodological priority

Before external suites or open-conjecture stress tests matter, Mathia must first answer a simpler question cleanly:

> **Can we build an internal benchmark where generic structural intuition has measurable downstream mathematical consequences while arithmetic execution is genuinely irrelevant?**

Issue #30 is the current gate for that question.
