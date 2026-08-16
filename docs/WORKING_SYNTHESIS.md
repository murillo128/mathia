# Working synthesis

## Status

This is the current research synthesis after the semantic-intuition reset and the subsequent refinement of the training hypothesis. It deliberately separates **accepted experimental constraints**, **working hypotheses**, **observed evidence**, and **open questions**.

It is not a final theory of mathematical understanding.

## Accepted experimental constraints for the current line

### Separate semantic understanding from execution

Primary Mathia-facing work should not require arithmetic execution, concrete numerical calculation, finite numerical enumeration, or algorithmic state reconstruction. The target is mathematical meaning, representation, and conceptual action.

### Use generic Mathia-visible mathematics

Primary model-visible mathematical content should use generic objects, operations, relations, transformations, and structural roles rather than concrete numeral instances.

The important constraint is semantic, not cosmetic: replacing a value with a variable does not make an execution task conceptual.

### Permit private instantiation and formal checking

Private generators, computation, falsifiers, qwen-lean, Lean, or other formal systems may instantiate and check abstract claims. Concrete instances belong on the experimental/verifier side of the boundary, not as the conceptual evidence Mathia relies on.

### Keep teacher judgment separate from mathematical utility

Codex or another frontier model may generate, critique, or rank conceptual material. Its judgment is teacher evidence, not mathematical truth.

In particular, similarity to a Codex or human intuition should not become the final reward when downstream mathematical utility can be measured.

### Validate the reward channel before post-training

Do not begin Mathia-specific concept/dimension/distillation/RL work merely because the training story is plausible. First establish that strategic guidance can causally change a downstream formal worker's verified proof-search outcome under controlled conditions.

### Preserve the retired experiment as provenance

The old `gold-set-v0` line remains in Git history. Issue #12 remains a completed engineering result. The new hypothesis should not rewrite earlier work as though it had always been the plan.

## Working hypothesis: concepts, dimensions, intuition

The current decomposition is:

```text
concepts
   -> conceptual dimensions / moves
   -> candidate intuitions
   -> initial teacher distillation
   -> downstream fertility selection
```

The sequence is a causal hypothesis, not a settled training pipeline.

### Concepts are directly teachable semantic objects

A concept may be learned more robustly through multiple representations, neighboring concepts, invariants, failure conditions, and relations rather than one canonical definition.

Candidate material includes:

- composition, identity, inverse;
- equivalence and quotienting;
- reversibility and information preservation;
- invariance and symmetry;
- product and decomposition;
- factorization through a representation;
- necessary/sufficient conditions;
- representation and change of representation.

The aim is not to execute these constructions on concrete instances but to understand what they preserve, forget, constrain, or make possible.

### Conceptual dimensions are operations over concepts

The earlier Mathia brainstorming identified reusable mathematical actions that are not themselves merely named mathematical concepts. The current candidates include:

- structural similarity / transfer;
- decomposition;
- composition / synthesis;
- abstraction / compression;
- generalization;
- counterfactual reasoning;
- simplification;
- bridge construction;
- reframing / out-of-the-box representation change;
- multiple perspectives;
- perspective selection;
- naturalness / canonicality;
- prediction and falsification.

The hypothesis is that these dimensions can be trained across mathematical domains. A model that knows what a quotient is may still fail to recognize **when quotienting is the right move**; this second ability belongs here.

### Intuition may be emergent rather than directly teachable

A candidate intuition is provisionally a compact strategic hypothesis about how a mathematical situation should be seen and where useful consequences may come from.

The model may acquire this ability by composing concepts and conceptual moves rather than by learning a fixed corpus of "the intuition is..." answers.

This remains unproven. Direct intuition examples may still be useful as a bootstrap, but the project should not assume that teacher imitation is the same thing as intuition.

## Initial intuition distillation

A strong frontier teacher such as Codex can provide an initial demonstration distribution over strategic mathematical thinking. On a documented theorem it may identify:

- the mechanism likely controlling the result;
- a promising change of representation;
- an intermediate object or lemma;
- an assumption that appears essential or unnecessarily strong;
- a plausible route toward proof;
- a likely obstruction or failure mode.

This is explicitly distillation. If Mathia later behaves like a cheaper local approximation to part of Codex's mathematical strategy, that is a real outcome and should be reported as such.

The important follow-up question is whether downstream mathematical selection can move the model beyond simple teacher similarity.

## Documented theorems as a calibration substrate

A small collection of famous or otherwise well-documented theorems can be used as an internal laboratory because their proofs, proof ideas, alternative viewpoints, and expository explanations are available for audit.

The fact that Qwen may have encountered these theorems or proofs during pretraining does not invalidate the calibration question. The target is not theorem recall but whether the model can produce a compact strategy that helps a separate prover.

This does limit claims about novel discovery. Later generalization evidence must use more independent material.

## qwen-lean as a fertility measurement instrument

The current stronger reward hypothesis is to measure each intuition by what it does to a separate formal worker.

For the same theorem and matched proof-search budget, compare qwen-lean:

- without intuition;
- with irrelevant/shuffled intuition;
- with Qwen-base intuition;
- later with Mathia intuition;
- with Codex intuition as a strong reference.

Each intuition is frozen before qwen-lean sees it. Lean verifies any proof produced.

The useful causal quantity is not "does this sound insightful?" but approximately:

```text
proof-search outcome with intuition
minus
matched proof-search outcome without intuition
```

Possible outcomes include proof success, reduced search cost, verified intermediate lemmas, or verified elimination of a false branch.

A qwen-lean proof-search failure remains weak evidence. It can mean the intuition is poor, the interface is poor, the formal worker is too weak, or the budget is insufficient.

## Why Codex is useful in the pre-test

Before training Mathia, Codex can serve as a strong reference for the `intuition -> formal search` channel.

If Codex-generated strategy improves qwen-lean while base-Qwen strategy does not, the experiment has evidence that:

1. qwen-lean can exploit strategic conceptual guidance;
2. the measurement channel has headroom for a local specialist.

If even Codex intuition does not help, Mathia training against qwen-lean uplift would be poorly motivated until the interface or formal worker is reconsidered.

## Evidence we actually have

At present, Mathia has **no target-model evidence** for the concepts/dimensions/intuition-fertility hypothesis.

The repository has process evidence from the retired experiment:

- benchmark defects can be exposed by iterative independent audit;
- deterministic model-agnostic plumbing can be built and reviewed;
- an experiment that sounds conceptual can still rely materially on execution;
- stopping before GPU inference when the target changes is preferable to preserving a stale experiment for momentum.

None of this establishes that the new training decomposition is correct.

## Provisional model comparisons

If the pre-test validates the reward channel, later experiments may compare checkpoints conceptually like:

```text
M0 = exact base
MC = M0 + concept training
MD = MC + conceptual-dimension training
MI = MD + initial Codex intuition distillation
MF = MI + fertility-based optimization
```

These labels are ablations, not a commitment to a fixed number of training phases or a particular algorithm.

A particularly informative result would be one where teacher similarity improves at `MI`, but qwen-lean proof-search uplift improves substantially only at `MF`. That would suggest the downstream signal is selecting something not captured by imitation alone.

## Main alternative hypotheses

### Explanation-style distillation

Concept/dimension/intuition training may teach the model to sound strategically mathematical without changing useful behavior.

### Solver-specific prompt optimization

Optimizing against qwen-lean may produce prompts specialized to one checkpoint or interface rather than generally fertile mathematical intuitions.

### Formal-worker bottleneck

Good intuitions may not receive credit because qwen-lean cannot exploit them.

### Base-model saturation

Qwen base may already generate enough strategic guidance on familiar theorems that the proposed specialization has little measurable headroom.

### Pretraining recall

A model may reconstruct a known proof idea from memory rather than derive it conceptually. This is acceptable for channel calibration but weak evidence of transfer.

## What would support the hypothesis

A useful evidence pattern would include some combination of:

- base-Qwen intuition has limited or inconsistent downstream value;
- Codex intuition measurably improves qwen-lean, validating the channel;
- concept training improves semantic robustness across representations;
- dimension training improves transfer, decomposition, synthesis, reframing, or perspective selection;
- initial distillation improves the frequency of plausible strategies;
- Mathia intuitions increase verified qwen-lean proof success or reduce proof-search cost;
- fertility-based optimization improves this causal effect beyond teacher similarity;
- the effect transfers across presentation or formal-worker changes.

## What would count against it

Important negative outcomes include:

- Codex intuition cannot improve qwen-lean;
- base Qwen saturates the task;
- training changes prose but not proof-search utility;
- only near-complete proof leakage creates uplift;
- solver-specific reward fails to transfer;
- teacher-reference similarity rises while downstream utility does not;
- the formal worker is too noisy for intuition-level credit assignment.

## Current action

The next action is issue `#30`: scope and adversarially audit the **concepts / conceptual dimensions / documented-theorem intuition / qwen-lean fertility** experimental contract before implementation or GPU work.

The detailed working hypothesis is in `docs/CONCEPTS_DIMENSIONS_INTUITION.md`.
