# Draft research plan: concepts, conceptual dimensions, and intuition fertility

## Status

This is Mathia's current **draft research plan**. It remains exploratory: it does not freeze a final curriculum, training algorithm, dataset schema, model architecture, or long-term orchestration design.

The active operational plan is tracked by epic `#29` and issues `#30`–`#32`.

The main refinement is that **intuition is no longer assumed to be the first object that should be directly supervised**. The current working decomposition is:

```text
mathematical concepts
        |
conceptual dimensions / moves
        |
candidate intuitions emerge
        |
initial frontier-teacher distillation when useful
        |
downstream proof-search fertility
        |
possible later optimization for fertility
```

See `docs/CONCEPTS_DIMENSIONS_INTUITION.md` for the detailed hypothesis.

## Central research question

> **Can a local mathematical specialist learn semantic concepts and reusable conceptual moves well enough to generate strategic intuitions that measurably improve a separate formal prover's search?**

This is distinct from asking whether the model can calculate, reproduce a proof, or imitate mathematical explanation style.

## Experimental boundary

Primary Mathia-visible mathematical content should remain generic and should not rely on concrete numerical instances or arithmetic execution. Private generators, computation, falsifiers, and formal systems may instantiate or verify claims behind the experimental boundary.

The base model already knows arithmetic from pretraining. The goal is to make arithmetic execution irrelevant to the conceptual capability under study, not to erase that knowledge.

## Three capability levels

### Concepts

Train or evaluate semantic understanding of constructions and relationships such as composition, inverse, equivalence, quotienting, invariance, reversibility, information preservation, decomposition, factorization, and representation change.

A concept should be learned through multiple viewpoints and relations rather than one canonical definition.

### Conceptual dimensions

Train or evaluate reusable mathematical moves such as:

- structural similarity and transfer;
- decomposition;
- composition and synthesis;
- abstraction and compression;
- generalization;
- counterfactual reasoning;
- simplification;
- bridge construction;
- reframing / out-of-the-box representation change;
- multiple perspectives and perspective selection;
- naturalness/canonicality;
- prediction and falsification.

These dimensions should transfer across concepts and domains. Naming the move is not the target; performing it is.

### Intuition

Treat intuition provisionally as an emergent candidate mechanism or strategic representation: a compact proposal for how a theorem or problem should be seen and where a proof, counterexample, or useful reduction might come from.

An intuition can be wrong yet useful. Therefore immediate truth, stylistic quality, or similarity to a canonical explanation should not be the sole reward.

## Documented theorems as an intuition laboratory

Use a small panel of well-documented theorems for calibration. Useful material may include multiple known proofs, expository accounts of the key idea, alternative representations, important intermediate lemmas, and documented failed or less-natural approaches.

The Mathia-facing task should expose the theorem and necessary mathematical context but not the target proof or reference intuition. Ask for a strategic account: mechanism, promising representation, intermediate objects/lemmas, assumptions that matter, and plausible route to proof.

Famous theorems are acceptable for this **internal calibration** even though the base model may have encountered them during pretraining. The question is not whether the model knows the theorem; it is whether it can produce a compact strategy that causally helps another prover. Pretraining exposure still limits claims about novel generalization and must be reported as such.

## Initial teacher distillation

A strong frontier teacher such as Codex may generate and critique intuition candidates for the documented theorem panel.

This is explicitly a bootstrap/distillation stage. It is not independent evidence that Mathia has discovered the intuition itself.

Teacher or human-reference similarity may be measured as an auxiliary signal, but it should not define the final target. A mathematically different intuition can be valuable if it improves proof search.

## qwen-lean as a fertility instrument

Keep Mathia and qwen-lean separate initially.

For a theorem `T` and candidate intuition `I`, compare qwen-lean under a fixed proof-search budget:

```text
T -> qwen-lean -> outcome_base

T + frozen intuition I -> qwen-lean -> outcome_I
```

Lean or the formal environment verifies any claimed proof. The primary causal object is the matched change in proof-search outcome attributable to `I`.

Useful metrics may include:

- verified proof success;
- attempts/tokens/search cost to verified proof;
- verified intermediate lemmas or reductions;
- branch elimination by verified counterexample;
- other pre-registered proof-search efficiency measures.

Proof-search failure is ambiguous. It does not establish that the intuition or theorem is false.

## Controls for intuition fertility

At minimum compare some combination of:

- qwen-lean with no intuition;
- qwen-lean with an irrelevant/shuffled intuition;
- qwen-lean with Qwen-base intuition;
- qwen-lean with Mathia intuition when a trained checkpoint exists;
- qwen-lean with Codex intuition as a strong reference;
- optionally a documented human strategy represented through the same interface.

Hold theorem, formal target, proof-search budget, runtime semantics, and evaluation rules fixed enough that intuition is the intended changed variable.

A key pre-training validation is whether a strong Codex intuition can improve qwen-lean at all. If not, the interface, solver, or reward channel may be unsuitable and should be repaired before training Mathia against it.

## Current critical path

### #30 — scope the objects and causal measurement

Define and adversarially audit:

- a provisional concept set and conceptual-dimension set;
- a small documented-theorem panel;
- the Mathia intuition task and what information is withheld;
- the qwen-lean conditioning interface at the semantic level, without implementing a permanent protocol;
- matched baseline/control conditions;
- candidate proof-search fertility metrics;
- failure modes such as proof leakage, solver-specific prompt hacking, teacher-style imitation, and arithmetic confounds.

No model training or GPU run belongs in #30.

### #31 — build minimal pre-test/fertility plumbing

Implement only what the accepted #30 design requires: theorem materialization, intuition import, fixed qwen-lean conditioning, proof-result capture, exact Lean verification linkage, deterministic identities/provenance, and matched scoring.

Do not build a permanent orchestration framework or training pipeline.

### #32 — run the frozen base/reference pre-test

Before Mathia post-training, run a frozen calibration using at least:

- the exact Qwen base as the local intuition generator;
- Codex/frontier intuition as a strong reference;
- qwen-lean as the downstream formal worker under matched budgets.

The pre-test should answer two questions:

1. How much useful strategic intuition is already present in the base model?
2. Is the `intuition -> qwen-lean proof-search uplift` channel informative enough to support later training?

Only after an interpretable positive result should the project open concrete training execution issues.

## Provisional post-pretest training hypothesis

If #32 validates the measurement channel, later work may compare checkpoints conceptually like:

```text
M0 = exact base
MC = M0 + concept training
MD = MC + conceptual-dimension training
MI = MD + initial Codex intuition distillation
MF = MI + fertility-based optimization
```

These labels are experimental comparisons, not a requirement that every stage use a separate model or a predetermined optimization algorithm.

The intended two intuition passes are:

1. **bootstrap/distillation:** expose Mathia to strong examples of strategic mathematical thinking;
2. **fertility selection:** prefer Mathia outputs because they improve verified downstream proof search, not because they resemble the teacher.

RL is one possible mechanism for the second pass, but rejection sampling, preference methods, supervised filtering, or other optimization could be better. Do not choose the algorithm before the signal is measured.

## Main confounds

### Teacher imitation

If Mathia improves only in similarity to Codex or human reference text, the project may have distilled explanation style rather than mathematical capability.

### Proof leakage

If an "intuition" simply contains most of the proof, qwen-lean uplift does not establish useful conceptual compression. The intuition interface should be strategic enough to leave meaningful formal search to the prover.

### Solver-specific prompt hacking

Optimization against one qwen-lean checkpoint may learn prompts that exploit that solver rather than transferable mathematical intuitions. Later validation should vary notation, prompts, solver checkpoint, or solver family where practical.

### Formal-worker weakness

A strong intuition may receive no reward if qwen-lean cannot exploit it. The Codex-reference condition helps diagnose this: if even frontier intuition does not produce uplift, the reward channel is suspect.

### Pretraining exposure

Famous theorem success is useful for calibration but weak evidence of novel mathematical generalization. Later external evaluation must use more independent material.

## What would support the hypothesis

Evidence becomes stronger if:

- Qwen base produces weaker or less consistent proof-search uplift than frontier reference intuition;
- concept/dimension training later improves structural behavior beyond explanation style;
- Mathia intuitions increase qwen-lean verified proof success or reduce search cost;
- fertility optimization improves that uplift beyond teacher-similarity distillation;
- gains survive meaningful changes in presentation or formal worker.

## What would count against it

Important negative outcomes include:

- base Qwen already saturates the strategic task;
- Codex intuition does not help qwen-lean;
- concept/dimension training changes prose but not downstream utility;
- only proof-like leakage yields uplift;
- qwen-lean-specific reward does not transfer;
- the formal worker is too noisy for intuition-level credit assignment.

These outcomes should change the model of the experiment rather than automatically trigger larger models or more data.

## Success criterion for the current plan

The immediate milestone is not to train Mathia. It is to establish a credible causal instrument:

> **A strategic mathematical intuition, frozen before proof search, measurably changes qwen-lean's verified proof-search outcome under a matched budget, and a strong frontier reference produces enough signal to make later Mathia training testable.**

If this channel works, the concepts → dimensions → distillation → fertility hypothesis becomes experimentally actionable. If it does not, the project should repair or abandon the reward mechanism before post-training.
