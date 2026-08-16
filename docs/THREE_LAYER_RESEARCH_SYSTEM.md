# Three-layer mathematical research system hypothesis

## Status

This document records a **downstream exploratory integration hypothesis**. It is not the active experiment, a settled architecture, an orchestration specification, or a commitment to a particular model size.

The current active work is narrower: validate a training/evaluation decomposition in which Mathia learns concepts and conceptual moves, receives an initial intuition bootstrap from a strong teacher, and is later judged by whether its intuitions improve a formal worker's proof search.

## Motivation

The hypothesis comes from an asymmetry:

- frontier models such as Codex are likely to remain stronger general mathematical reasoners than the first local Mathia model;
- frontier reasoning is scarce and quota/cost constrained;
- local specialist inference can be run with much larger token budgets;
- formal/computational tools can provide exact feedback on some claims;
- a specialist does not need to outperform the director in isolation if it amplifies the director's scarce reasoning.

The system question is:

> **Can a strong but scarce research director obtain more useful mathematical progress by directing abundant local conceptual and formal compute than by spending the same frontier budget doing all exploration itself?**

The Mathia-specific question is:

> **At matched local compute, does a model specialized for semantic concepts and conceptual moves generate more fertile strategic intuitions than a generic local reasoner?**

## Candidate division of labor

```text
                         Codex
             strong teacher / later director
                            |
                +-----------+-----------+
                |                       |
                v                       v
             Mathia                formal specialist
       conceptual exploration      e.g. qwen-lean
       and strategic intuition     proof/search/checking
                |                       |
                +-----------+-----------+
                            |
                     checked evidence
                            |
                     state revision
                            |
                     next direction
```

A separate computational tool layer may also be used for private instantiation, search, or falsification when it is cheaper or more reliable than either language model.

The important distinction is functional. Concrete models may be replaced when capacity or hardware evidence justifies it.

## Codex has two possible roles

### Bootstrap teacher

Before Mathia is capable enough to generate useful strategic intuitions reliably, Codex can scope and demonstrate the activity on documented theorems. It may identify mechanisms, representations, intermediate lemmas, assumption weaknesses, or proof routes.

This is **distillation**, not independent evidence of Mathia capability. It is acceptable as a bootstrap if teacher contribution is tracked explicitly and later mathematical utility is measured separately from teacher similarity.

### Later scarce research director

If Mathia becomes a useful local specialist, Codex can shift toward high-leverage decisions such as:

- maintaining the high-level mathematical state;
- comparing independent approaches;
- identifying redundancy or equivalence between branches;
- choosing which uncertainty is worth reducing next;
- asking for discriminating experiments;
- identifying the weakest assumption or missing lemma;
- deciding whether formal evidence changes the conceptual picture;
- pruning dead or low-information paths;
- injecting its own mathematical ideas when local specialists stall;
- selecting results for human expert review.

The amplification hypothesis fails if Codex must inspect and solve every local proposal itself.

## Mathia: concepts, conceptual moves, and strategic intuition

Mathia does **not** need to be the component that evaluates every calculation. Its candidate specialization is built from two directly trainable substrates:

- **concepts and semantic relationships** — what constructions mean, what they preserve or forget, how representations connect;
- **conceptual dimensions / moves** — structural similarity, decomposition, synthesis, abstraction, generalization, reframing, bridge construction, counterfactual reasoning, simplification, and perspective selection.

The working hypothesis is that candidate intuitions can emerge from combining these resources.

Examples of useful Mathia moves include:

- alternative representations;
- candidate invariants;
- reversibility / information-loss hypotheses;
- quotient/factorization viewpoints;
- analogies across domains;
- assumption weakening;
- decompositions;
- natural intermediate objects;
- candidate equivalences;
- generalizations;
- structural falsification criteria;
- diagnoses of why an approach is failing;
- competing conceptual models of the same phenomenon.

Mathia is useful only if these proposals are more fertile than compute-matched generic local reasoning. Learning a recognizable conceptual style is insufficient.

## qwen-lean has an earlier experimental role

The formal specialist is not only a later research-system component. It can also be used much earlier as an **instrument for measuring intuition fertility**.

For a fixed theorem and proof-search budget:

```text
no intuition
    -> qwen-lean
    -> verified proof-search outcome

Mathia intuition I
    -> freeze I
    -> qwen-lean under matched budget
    -> verified proof-search outcome
```

The change in outcome gives a causal behavioral signal about the usefulness of `I` for that formal worker.

Matched reference conditions can include Qwen-base intuition, shuffled intuition, and Codex intuition. Lean verifies any resulting proof.

This does not mean qwen-lean defines mathematical intuition. A proof-search failure is ambiguous, and optimization against one formal worker may learn solver-specific prompts. Transfer checks are required before treating the reward as general mathematical fertility.

## The semantic / execution separation inside the system

A future research loop can deliberately separate:

```text
Mathia
meaning / mechanism / representation
           |
           v
experiment layer
instantiate / compute / search
           |
           v
formal specialist
formalize / prove / refute
           |
           v
Codex + Mathia
interpret evidence / revise direction
```

This separation allows concrete examples to be used aggressively as scientific instruments without making concrete arithmetic the conceptual language Mathia is trained to rely on.

## Formal specialist: contact with exact mathematical reality

Potential roles include:

- testing whether a strategic intuition improves proof search;
- formalizing an intermediate generic claim;
- checking that a proposed implication really holds;
- proving a weakened or restricted statement;
- verifying equivalence between formulations;
- exposing missing assumptions;
- formalizing a structural counterexample;
- checking that an intermediate lemma is actually sufficient for a larger reduction;
- reusing verified lemmas later.

Formal outcomes have asymmetric meanings:

```text
proof verified
    -> strong positive evidence for the exact proposition

counterexample/refutation verified
    -> strong negative evidence

formalization succeeded
    -> claim is precise, not necessarily true

proof search failed
    -> weak / ambiguous evidence

formalization failed
    -> may indicate ambiguity, missing definitions, or tool weakness
```

Never tell Mathia that a conjecture is false merely because qwen-lean failed to prove it.

## A possible training bridge into the later system

If the initial qwen-lean fertility instrument is informative, the training story can be conceptually decomposed as:

```text
concept training
      |
conceptual-dimension training
      |
Codex intuition distillation
      |
Mathia candidate intuitions
      |
qwen-lean matched proof-search tests
      |
verified fertility signal
      |
possible later optimization
```

The optimization method is deliberately undecided. The important point is that teacher imitation bootstraps the behavior while downstream mathematics can later select among intuitions.

## Main risk: optimizing for qwen-lean rather than mathematics

If Mathia is rewarded only by one qwen-lean checkpoint, it may learn strings that steer that model idiosyncratically rather than generally useful mathematical representations.

Later evidence should therefore test some combination of:

- changed theorem notation or presentation;
- alternate qwen-lean prompts;
- a different qwen-lean checkpoint;
- another formal or mathematical solver;
- transfer from proof search to generalization, diagnosis, or construction;
- frontier or human inspection of the mathematical content.

This is a central alternative hypothesis, not merely an implementation nuisance.

## The core research loop

A mature loop might be:

```text
intuition
   |
   v
structural predictions / proof route
   |
   v
criticism / competing intuition
   |
   v
private instantiation / formalization / proof search
   |
   v
checked evidence
   |
   v
conceptual revision
   |
   v
new intuition
```

Codex intervenes strategically rather than at every transition.

The local layers should eventually be able to explore, criticize, and eliminate large numbers of ideas between frontier interventions.

## Research state is likely a key bottleneck

Large local token budgets are useless if the system repeatedly forgets discoveries or floods the director with transcripts.

A future system will need some form of compressed mathematical research state containing things like:

- live hypotheses;
- verified consequences;
- refuted branches;
- unresolved dependencies;
- equivalent/redundant formulations;
- known obstacles;
- promising representations;
- provenance and confidence/evidence type.

Do not design a permanent schema now. The research hypothesis is that useful state should summarize mathematical content and dependency, not conversation history.

## Frontier budget must be measured

When comparing systems, keep Codex usage visible. Otherwise a run may appear to demonstrate Mathia capability while the frontier teacher/director actually supplied the decisive mathematics.

Useful later ablations include:

```text
frontier director only

frontier director + generic local mathematical worker

frontier director + Mathia

frontier director + generic worker + formal specialist

frontier director + Mathia + formal specialist
```

Hold frontier budget and approximate local compute fixed enough to identify what each component contributes.

## Long-horizon fertility as future training feedback

A mature research loop creates a possible signal beyond immediate proof search. An early Mathia intuition might later generate useful subclaims, survive criticism, produce a verified lemma, prune competing branches, or be reused by another approach.

This suggests a future objective like:

```text
early idea
   -> downstream research utility
   -> credit assigned back to the idea/policy that produced it
```

That long-horizon problem should not be conflated with the first qwen-lean proof-search fertility test.

## Component-specific scaling

### Conceptual bottleneck

Local Mathia proposals are mostly shallow or false while a stronger model produces fertile mechanisms from the same state.

Possible response: improve concept/dimension training or scale the conceptual specialist.

### Formal bottleneck

Codex or strong Mathia intuitions appear mathematically useful, but qwen-lean cannot exploit them under manageable budgets.

Possible response: improve formal model/search/tooling before using its outcomes as a reward.

### Coordination bottleneck

Good results are produced but forgotten, duplicated, or never combined.

Possible response: improve research-state management/director policy, not GPU size first.

### Throughput bottleneck

The process works but is too slow.

Possible response: increase local hardware/parallelism.

## Failure modes

The story can fail in several ways:

- concept/dimension training produces only polished conceptual prose;
- initial Codex distillation dominates all later behavior;
- qwen-lean cannot exploit even strong intuitions;
- qwen-lean reward selects solver-specific prompting rather than mathematics;
- filtering local noise costs more frontier reasoning than it saves;
- the formal specialist returns too many ambiguous failures to guide learning;
- branch state grows faster than it can be compressed;
- agents converge on mutually reinforcing but false abstractions;
- the director dominates all decisive reasoning;
- concrete verifier tasks leak back into Mathia training until it becomes another execution model.

These should be tested, not narrated away.

## Relationship to the current epic

The current sequence is:

```text
#30: scope concepts, conceptual dimensions,
     documented-theorem intuition, and fertility measurement
      |
#31: implement only the minimal pre-test/fertility harness
      |
#32: test Qwen-base and Codex-reference intuitions
     against matched qwen-lean proof search
      |
informative fertility channel?
      |
only then open concept/dimension/distillation/training execution work
```

The full three-layer research architecture remains downstream. The qwen-lean fertility instrument is an earlier experiment that may or may not justify that later system.
