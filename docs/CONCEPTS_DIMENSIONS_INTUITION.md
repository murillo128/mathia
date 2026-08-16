# Concepts, conceptual dimensions, and intuition fertility

## Status

This document records the current **working training hypothesis** for Mathia after the semantic-intuition reset. It is not a final architecture, curriculum, dataset schema, RL algorithm, or claim that mathematical intuition has been operationally solved.

The main refinement is to stop treating intuition as necessarily the first object to supervise directly. The current hypothesis is:

> **Teach mathematical concepts; train reusable conceptual moves over those concepts; allow candidate intuitions to emerge; bootstrap their generation with a strong teacher when useful; then select them by downstream mathematical fertility.**

This separates what can plausibly be taught directly from what may be an emergent property of a sufficiently structured mathematical model.

## Layer 1: mathematical concepts

The first substrate is semantic knowledge of mathematical concepts and relationships. The target is not dictionary-style definition recall and not execution on concrete numerical instances.

A concept should be represented through multiple viewpoints, neighboring concepts, invariants, failure conditions, and relations to other constructions. Examples include:

- product and independent combination;
- composition;
- identity and inverse;
- equivalence and quotienting;
- invariance and symmetry;
- reversibility and information preservation;
- decomposition;
- factorization through another representation;
- necessary and sufficient conditions;
- representation and change of representation.

For example, reversibility should not reduce to one sentence. It may connect the ability to undo a transformation, preservation of enough information for reconstruction, an inverse role, and the absence of certain forms of information collapse.

The training question at this layer is approximately:

> Does the model understand what the construction means and how it relates to other mathematical structures, independently of carrying out arithmetic instances?

## Layer 2: conceptual dimensions or moves

The early Mathia brainstorming identified a second kind of object that is different from a mathematical concept. These are reusable **ways of operating on mathematical representations**.

The current candidate set includes, without claiming a final taxonomy:

- **structural similarity / transfer** — recognize one mechanism under a different mathematical appearance;
- **decomposition** — split an object or problem into components whose roles become clearer;
- **composition / synthesis** — combine ideas, transformations, or domains to obtain a viewpoint unavailable from either alone;
- **abstraction / compression** — replace many local facts by a smaller structural mechanism;
- **generalization** — identify which parts of a statement are accidental and which support a broader claim;
- **counterfactual reasoning** — predict what changes when an assumption or structural component is modified;
- **simplification** — find a representation in which the same question requires less work;
- **bridge construction** — introduce or identify an intermediate object that connects two mathematical descriptions;
- **reframing / out-of-the-box movement** — leave the representation in which a problem was posed and formulate it in a substantially different space;
- **multiple perspectives** — construct genuinely different views of the same phenomenon;
- **perspective selection** — choose which valid representation is useful for the current goal;
- **naturalness / canonicality** — distinguish constructions induced by the structure from arbitrary proof choices;
- **prediction and falsification** — extract consequences that would support or break a proposed interpretation.

Some terms can appear at both layers. Decomposition, for example, can be a mathematical construction in a particular theory and also a general conceptual move. The distinction is functional rather than ontological.

The important question is not whether the model can name these dimensions. It is whether it can **perform them across different mathematical concepts and domains**.

## Layer 3: intuition as an emergent candidate mechanism

The current hypothesis is that mathematical intuition may not need to be taught as a fixed target in the same way as concepts or conceptual dimensions.

After a model has learned a rich semantic network and reusable moves over it, it may begin to produce statements such as:

- the real mechanism may be reversibility rather than the stronger assumption in the theorem;
- the object should perhaps be viewed through an equivalence relation because the target construction cannot distinguish certain differences;
- a decomposition suggests that the apparent special case belongs to a broader product-like or distributive structure;
- a problem stated in one domain may become simpler after moving to another representation.

These are **candidate intuitions**: provisional hypotheses about how to see the problem and where a proof or counterexample may come from.

A candidate intuition need not be true to be useful. A false idea can still be fertile if it quickly exposes the missing condition, produces a useful counterexample, or narrows the search space. Therefore the project should avoid defining intuition quality as immediate correctness or rhetorical depth.

## Two passes after conceptual training

The current downstream hypothesis has two distinct passes.

### Pass A: initial intuition distillation / bootstrap

A strong frontier teacher such as Codex can be used to scope and demonstrate the activity of mathematical intuition on a set of documented theorems.

For each theorem, useful source material may include:

- the theorem statement;
- several known proofs when available;
- mathematical exposition explaining why the proof works;
- alternative representations;
- historically or pedagogically documented key ideas;
- important lemmas, reductions, and failed natural approaches where documented.

The teacher should produce a compact strategic account rather than simply emit the proof: what mechanism seems central, which representation is promising, what intermediate object or lemma might unlock the result, which assumptions matter, and what route it would investigate.

This is explicitly a form of **distillation**. That is acceptable as a bootstrap if it is measured honestly. The scientific question is then whether later training and selection produce a local specialist whose ideas are useful beyond merely imitating teacher phrasing.

Similarity to documented human or teacher intuition can be recorded as an auxiliary signal, but it should not be the final reward. Otherwise the model is pressured toward canonical explanations even when a different strategy would be equally or more useful.

### Pass B: select intuitions by proof-search fertility

The stronger signal is causal utility for a separate formal specialist such as qwen-lean.

Keep Mathia and qwen-lean as separate models initially. Do not merge weights merely to test this hypothesis.

For a fixed theorem and a fixed proof-search budget:

1. qwen-lean attempts the theorem without an intuition;
2. Mathia generates one or more candidate intuitions;
3. each intuition is frozen before the proof attempt;
4. qwen-lean attempts the same theorem under the same budget while conditioned on that intuition;
5. Lean or the formal environment checks any resulting proof;
6. the change in proof-search outcome is attributed to the intuition, subject to the experiment's controls.

The basic quantity of interest is conceptually:

```text
fertility(I) = proof-search outcome with I - matched proof-search outcome without I
```

This does not require the reward to be one scalar formula. Useful evidence may include:

- increased verified proof success;
- fewer attempts, tokens, or search steps for a verified proof;
- a verified useful intermediate lemma;
- a correct reduction that makes the remaining proof easier;
- elimination of a branch by verified counterexample;
- lower formal search cost under a frozen budget.

A failed qwen-lean proof search remains ambiguous. It is evidence about the utility of the intuition for that solver and budget, not evidence that the intuition or theorem is false.

## qwen-lean as a measurement instrument

This gives qwen-lean an earlier role than the eventual three-layer research system: it can act as an **experimental instrument for measuring intuition fertility**.

Important matched controls include:

- qwen-lean with no intuition;
- qwen-lean with a shuffled intuition from another theorem;
- qwen-lean with Mathia's intuition;
- qwen-lean with a Codex-generated intuition as a strong reference;
- where useful, a documented human strategy represented in the same interface.

The Codex condition is especially useful before Mathia training. If a high-quality frontier intuition does not improve qwen-lean under the proposed interface, then the measurement channel may be badly designed or qwen-lean may be unable to exploit this kind of guidance. Training Mathia against that channel would then be premature.

Conversely, if Codex guidance creates a measurable uplift while the base Qwen model does not, the experiment has identified both a usable downstream signal and room for a local intuition specialist to improve.

## Pre-test before Mathia post-training

Before spending compute on concept, dimension, or intuition training, run a small frozen pre-test on documented theorems.

The same theorem panel can be used to compare at least:

```text
M0 = exact Qwen base
C  = Codex / frontier teacher reference
```

Later ablations may add:

```text
MC = M0 + concept training
MD = MC + conceptual-dimension training
MI = MD + initial intuition distillation
MF = MI + fertility-based optimization
```

These names describe comparisons, not a commitment that every stage must be a separate checkpoint or use the same training algorithm.

The base-model pre-test answers a simple question: how much useful strategic intuition is already present before Mathia-specific training? A model may have seen the theorem and even its proof during pretraining while still failing to produce a compact strategy that helps another prover. For this internal diagnostic, famous theorems are therefore not automatically invalid.

Pretraining exposure still limits claims about novel generalization. The theorem panel should be described as a **calibration and causal-instrument test**, not as a clean held-out measure of mathematical discovery. Later evaluation can use lesser-known, transformed, or otherwise protected material.

## What an intuition prompt should ask for

The exact interface belongs to issue design, but the conceptual target is a strategic object rather than a proof transcript. It should encourage outputs such as:

- the mechanism likely controlling the theorem;
- a representation or reformulation worth trying;
- one or more intermediate lemmas or objects likely to matter;
- assumptions that appear essential or stronger than necessary;
- a plausible proof route;
- a predicted obstruction or failure mode.

The output should not be scored primarily for eloquence or similarity to one canonical explanation.

## Main confound: solver-specific prompt optimization

If Mathia is optimized only by qwen-lean proof success, it may learn to generate prompts that exploit idiosyncrasies of qwen-lean rather than generally useful mathematical intuitions.

This is a real alternative hypothesis, not an implementation detail. Later controls should test transfer across some combination of:

- changed notation or theorem presentation;
- alternate qwen-lean prompting;
- different qwen-lean checkpoints;
- another formal or mathematical solver;
- human or frontier review of the mathematical content;
- downstream tasks other than direct proof search.

The first experiment does not need to solve this completely, but it must preserve enough provenance to know which solver the reward optimized against.

## Revised working sequence

The current scientific sequence is therefore:

```text
scope concepts and conceptual dimensions
        |
define a documented-theorem intuition panel
        |
validate the intuition -> qwen-lean measurement channel
using Qwen-base and Codex reference
        |
if the channel is informative:
        |
concept training
        |
conceptual-dimension training
        |
initial Codex intuition distillation
        |
measure each Mathia intuition by qwen-lean proof uplift
        |
only then choose whether/how to optimize for fertility
```

This is a working causal decomposition, not a permanent training pipeline.

## What would support the hypothesis

Evidence would be stronger if the pattern looked like:

- the exact base has limited or inconsistent intuition fertility;
- concept training improves conceptual understanding without merely improving prose;
- dimension training improves transfer, decomposition, synthesis, reframing, or strategy selection;
- initial teacher distillation raises the rate of plausible strategic proposals;
- qwen-lean succeeds more often or with lower proof-search cost under some Mathia intuitions;
- fertility-based optimization improves this causal uplift beyond teacher-similarity training;
- the effect transfers beyond one exact qwen-lean prompt or checkpoint.

## What would count against it

Important negative outcomes include:

- the base model already saturates the intuition task, leaving little room for specialization;
- concept/dimension training changes explanation style but not proof-search utility;
- Codex intuitions do not help qwen-lean, so the proposed reward channel is not informative;
- Mathia intuitions help only through direct proof leakage rather than a useful strategic representation;
- qwen-lean-specific optimization fails to transfer to another solver or presentation;
- documented-intuition similarity rises while proof-search utility does not;
- the formal specialist is too weak or noisy for intuition-level credit assignment.

These outcomes should change the training hypothesis rather than automatically trigger more scale.
