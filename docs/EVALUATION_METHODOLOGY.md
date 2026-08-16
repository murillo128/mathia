# Evaluation methodology: external validation of conceptual mathematical transfer

## Status

This document records a **methodological stance**, not an execution plan, benchmark commitment, phase structure, or roadmap.

Its purpose is to preserve how Mathia should distinguish evidence of transferable mathematical capability from improvements that may come from benchmark-specific optimization, extra problem-solving practice, or a learned style of conceptual explanation.

The central question is not merely whether a Mathia-trained model scores higher on mathematics benchmarks. It is whether training aimed at conceptual mathematical reasoning produces **out-of-distribution behavioral gains on external tasks that were not used to shape that training**.

## Core principle: external benchmarks are validation, not curriculum

Public mathematical benchmarks considered for external validation should not become Mathia training material, reward targets, prompt templates, curriculum sources, or routine development feedback.

The strongest form of evidence would be:

> Mathia training is designed without optimizing against a particular external benchmark, and the final trained model nevertheless improves on that benchmark in ways predicted by the conceptual-reasoning hypothesis.

This makes external evaluation analogous to a held-out scientific test rather than an engineering dashboard.

A benchmark can be technically absent from the training dataset and still become effectively part of model development if it is run repeatedly and training decisions are changed in response to its score. For that reason, **benchmark isolation is behavioral, not merely dataset-level**.

## Keep three kinds of evidence distinct

Mathia should distinguish at least three sources of evaluation evidence. These are categories of evidence, not sequential project phases.

### Development diagnostics

Small, cheap probes may be used to detect broken training, regressions, formatting failures, or absence of the intended learning signal.

These probes should be designed by Mathia and should not simply reproduce the external benchmarks later used as evidence of transfer.

### Internal held-out conceptual evaluation

Mathia may maintain its own unseen situations and interventions for questions directly tied to the research hypothesis, such as:

- invariance under changes of representation;
- transfer of the same mechanism across domains;
- assumption weakening;
- counterexample discovery;
- generation of useful generalizations;
- reframing and perspective selection;
- distinguishing structural content from rhetorical explanation.

These tests can guide research, but because they are designed by the project they are not sufficient external evidence by themselves.

### External validation

External suites should test whether Mathia's learned behavior transfers to independently designed mathematical tasks.

The important property is not that the benchmarks are fashionable or difficult. It is that they provide **independent pressure on capabilities that Mathia claims to improve**.

External validation should remain as close as practical to a sealed test: the suite, harness, metrics, and inference policy are fixed independently of the final model, and item-level failures are not used as iterative training feedback.

## Benchmark isolation and contamination discipline

For an external benchmark to provide strong evidence:

- its evaluation items should not be intentionally included in Mathia training or synthetic-data generation;
- benchmark solutions, labels, judge traces, and official examples should not be transformed into training targets;
- prompts should not be tuned specifically to maximize that benchmark after observing results;
- repeated item-level failure analysis should not drive changes to Mathia training;
- the exact inference configuration used for comparison should be recorded;
- contamination risks inherited from the base model should be acknowledged rather than treated as removable after the fact.

Public benchmarks are necessarily imperfect held-out tests because a pretrained base model may already have encountered some of their material. This increases the value of recent, refreshed, adversarial, or procedurally modified benchmarks whose items are less likely to have been present verbatim in pretraining.

If an external suite must be run before the final evaluation, aggregate scores may be retained while item-level outputs remain embargoed from training decisions. A cleaner alternative is to evaluate the base model and the final model under the same frozen harness only when the external validation is performed.

## What kinds of external benchmarks are interesting

No benchmark suite is selected here. The following are **candidate families** because they probe different failure modes and would provide complementary evidence.

### Structural robustness and perturbation

Benchmarks such as MATH-Perturb are interesting because they modify familiar mathematical problems so that superficial reuse of the original method becomes unreliable.

A disproportionate gain on hard perturbations relative to ordinary problem accuracy would be evidence consistent with better structural generalization.

### Falsification and counterexamples

Benchmarks such as CounterMATH test whether a model can reject plausible mathematical claims and construct valid counterexamples.

This is relevant to Mathia because a conceptual representation that cannot survive attempts to break it may be rhetorically attractive but mathematically sterile.

Refreshed adversarial suites such as BrokenArXiv are especially interesting when they use recent mathematical material and plausible-but-false modifications, because they reduce the value of memorized benchmark patterns.

### Mathematical construction

Benchmarks such as MathConstruct require the model to construct objects satisfying mathematical constraints rather than merely compute an answer.

Improvement here could indicate that learned representations are generative: they help synthesize mathematical objects, not just classify or solve familiar forms.

### Recent competition and research mathematics

Living or refreshed suites such as MathArena can provide a moving external reference based on recent problems, reducing some forms of benchmark saturation and contamination.

Research-derived collections such as ArXivMath are interesting as a stronger distribution shift away from textbook and competition templates.

### Capability ceiling

Suites such as FrontierMath can serve as a reference for high-end mathematical capability, but should not automatically become the primary Mathia metric. They may conflate many capabilities, have expensive inference requirements, and measure something broader than the conceptual mechanisms Mathia is trying to isolate.

## Compare upward, not only backward

Historical benchmark baselines are useful for checking reproducibility, but they are weak evidence of competitiveness if they contain models substantially older or less capable than the model family Mathia starts from.

External validation should therefore include **contemporary models that are stronger than the Mathia base model**, when comparable public results or feasible inference access exist.

The ideal comparison set is conceptually diverse rather than large. It may include:

- the exact base checkpoint used by Mathia;
- a stronger model from the same or successor model family;
- a strong contemporary open-weight reasoning model;
- one or more current frontier closed models;
- historical baselines only as context.

The identities of these models should remain replaceable as the frontier moves. The methodological requirement is to compare **toward the current ceiling**, not to freeze a leaderboard from the year a benchmark paper was released.

A small Mathia model does not need to beat the largest frontier model for the experiment to be scientifically interesting. A more diagnostic question is whether its **pattern of gains** moves disproportionately toward frontier behavior on the capabilities that conceptual training predicts should improve.

## Measure the profile of gains, not only a single score

The primary comparison should include the delta from the exact base model:

```text
Delta_mathia(B) = score(Mathia, B) - score(Base, B)
```

for benchmark or capability family `B`.

Absolute scores still matter, but the pattern across benchmarks is more informative about what changed.

For example, a hypothetical result of the form:

| Evaluation family | Base | Mathia | Delta |
|---|---:|---:|---:|
| ordinary competition solving | 70 | 71 | +1 |
| counterexample / falsification | 45 | 58 | +13 |
| hard structural perturbation | 38 | 50 | +12 |
| constrained construction | 25 | 34 | +9 |

would be much more suggestive of a changed mathematical capability profile than a uniform one-point gain everywhere.

Conversely, a large gain on Mathia's own conceptual-language evaluations combined with no improvement on external perturbation, falsification, construction, or transfer tasks would support the alternative hypothesis that training mainly taught a **style of mathematical explanation**.

This interpretation remains a hypothesis, not proof of a latent conceptual mechanism. Strong controls are still needed to distinguish conceptual post-training from simply giving the model more mathematics or more reasoning compute.

## Fair inference comparisons

Benchmark comparisons should record enough inference detail to distinguish model capability from test-time compute.

Relevant variables include:

- model/checkpoint and tokenizer;
- prompt and chat template;
- maximum output or reasoning budget;
- temperature and sampling policy;
- use of tools, code execution, retrieval, or external verifiers;
- number of attempts per problem;
- aggregation rule such as pass@1, majority vote, best-of-N, or judge score;
- effective throughput and hardware when runtime is reported.

When comparing Mathia with its base checkpoint, the default scientific comparison should hold these conditions fixed unless the experiment is explicitly about test-time scaling.

Published frontier scores should only be treated as directly comparable when their evaluation protocol is sufficiently compatible. Otherwise they are reference ceilings, not controlled experimental baselines.

## Repeated runs and benchmark variance

A single deterministic pass can be useful for cheap diagnostics, but stochastic reasoning models may require multiple attempts per problem for stable final estimates.

If a benchmark's official protocol uses repeated generations, Mathia should distinguish clearly between:

- a cheaper local pass@1 measurement;
- a protocol-compatible final measurement.

The number of repetitions should not be increased selectively after seeing disappointing results. Repetition policy is part of the frozen evaluation protocol.

## Approximate runtime and compute scale

Evaluation cost depends more on **generated reasoning tokens and aggregate decoding throughput** than on benchmark item count alone.

A useful first-order estimate is:

```text
wall_clock_hours ~=
    problems * attempts_per_problem * mean_generated_tokens
    / aggregate_tokens_per_second
    / 3600
```

The following numbers are deliberately only order-of-magnitude planning estimates. They assume reasoning-model outputs of the indicated length and ignore prompt-prefill overhead, judge cost, retries, and load imbalance.

| Candidate suite | Approx. items | Illustrative output budget | 1x at 100 tok/s | 1x at 500 tok/s | 4x at 500 tok/s |
|---|---:|---:|---:|---:|---:|
| CounterMATH | ~1,200 | 2k-4k tokens | ~7-14 h | ~1.4-2.8 h | ~5.5-11 h |
| MATH-P-Hard | ~280 | ~8k tokens | ~6 h | ~1.2 h | ~5 h |
| MathConstruct | ~125 | ~8k tokens | ~3 h | ~0.6 h | ~2.2 h |
| recent 30-problem competition set | 30 | ~30k tokens | ~2.5 h | ~0.5 h | ~2 h |
| recent 40-problem harder set | 40 | ~40k tokens | ~4.5 h | ~0.9 h | ~3.6 h |

`100 tok/s` and `500 tok/s` here are illustrative **aggregate** throughputs, not claimed hardware measurements for Mathia. Actual throughput can differ by an order of magnitude depending on model size, quantization, batching, context length, hardware, and serving stack.

A reasonably broad final external battery can therefore be expected to cost roughly **tens of GPU-hours per model**, rather than minutes, if long reasoning traces and repeated attempts are used. This is a reason to keep external validation selective and scientifically motivated, not a reason to convert it into a development loop.

## Interpretation against stronger models

For every external suite, three different questions should remain separate:

1. **Did Mathia improve over its exact base model?**
2. **Did Mathia improve more on conceptually diagnostic tasks than on ordinary solver tasks?**
3. **How much of the gap to contemporary stronger models remains?**

The first tests whether post-training changed behavior.

The second tests whether the direction of change matches the Mathia hypothesis.

The third provides an external capability scale and prevents a result from looking impressive only because it is compared with obsolete models.

These questions should not be collapsed into a single leaderboard rank.

## Negative results are valuable

Several outcomes would argue against the current Mathia hypothesis or against a particular training signal:

- conceptual-language quality improves but independent mathematical behavior does not;
- gains disappear under representational perturbations;
- a compute-matched ordinary solver baseline improves by the same amount;
- gains are concentrated in benchmark formats strongly resembling Mathia-generated data;
- repeated external evaluation is necessary to tune the model into showing the effect;
- improvement comes only from a larger inference budget;
- the model becomes more confident or verbose without becoming more falsifiable.

These should be treated as scientific evidence rather than benchmark engineering failures.

## What this document does not decide

This methodology intentionally does **not** decide:

- the final external benchmark suite;
- a required evaluation schedule;
- when particular benchmarks must be run;
- which frontier models must be purchased or queried;
- a pass/fail score threshold;
- an experiment phase structure;
- a set of implementation issues or milestones.

Those choices should be made only when a concrete experiment requires them and when the model, compute budget, benchmark state, and available contemporary baselines are known.

The durable methodological claim is narrower:

> **Mathia should treat independently designed mathematical benchmarks as protected evidence of transfer, compare against the exact base model and contemporary stronger models, and judge success from the structure of behavioral gains rather than from conceptual prose or a single aggregate score.**
