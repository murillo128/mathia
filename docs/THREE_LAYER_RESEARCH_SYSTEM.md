# Three-layer mathematical research system hypothesis

## Status

This document records a **downstream exploratory integration hypothesis**. It is not the active experiment, a settled architecture, an orchestration specification, or a commitment to a particular model size.

The active first priority remains issue `#30`: establish whether a computation-free semantic-intuition signal exists at all.

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

> **At matched local compute, does a model specialized for semantic mathematical intuition generate more fertile research moves than a generic local reasoner?**

## Candidate division of labor

```text
                         Codex
                scarce frontier director
          strategy / critique / prioritization
                            |
                +-----------+-----------+
                |                       |
                v                       v
             Mathia                formal specialist
       semantic / conceptual      e.g. qwen-lean
       abundant local search      abundant local checking
                |                       |
                +-----------+-----------+
                            |
                     checked evidence
                            |
                     state revision
                            |
                     next direction
```

A separate computational tool layer may also be used for private instantiation, search, or falsification when it is cheaper/more reliable than either language model.

The important distinction is functional. Concrete models may be replaced when capacity/hardware evidence justifies it.

## Codex: scarce research direction

Codex is not assumed to be weaker than Mathia. The opposite is the realistic initial assumption.

Its scarce reasoning should therefore be spent on high-leverage decisions such as:

- maintaining the high-level mathematical state;
- comparing independent approaches;
- identifying redundancy or equivalence between branches;
- deciding which uncertainty is worth reducing next;
- asking for discriminating experiments;
- identifying the weakest assumption or key missing lemma;
- deciding whether formal evidence changes the conceptual picture;
- pruning dead/low-information paths;
- injecting its own mathematical ideas when local specialists stall;
- selecting results for human expert review.

The amplification hypothesis fails if Codex must inspect and solve every local proposal itself.

## Mathia: abundant semantic intuition

The semantic-intuition reset clarifies Mathia's candidate role.

Mathia does **not** need to be the component that evaluates every calculation. Its specialty may instead be producing moves such as:

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

The core output can remain generic.

A possible interaction is:

```text
research state
      |
      v
Mathia: "the mechanism may be information preservation under T"
      |
      +--> predicts what should remain invariant
      +--> predicts where failure should occur
      +--> suggests a more natural representation
      |
      v
private computation / formal layer tests consequences
```

Mathia is useful only if these proposals are more fertile than compute-matched generic local reasoning. Learning a recognizable conceptual style is insufficient.

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

The formal specialist should not be treated merely as a machine asked to solve the final theorem.

Potential roles include:

- formalizing an intermediate generic claim;
- checking that a proposed implication really holds;
- proving a weakened/restricted statement;
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

## The core research loop

A productive loop might be:

```text
intuition
   |
   v
structural predictions
   |
   v
criticism / competing intuition
   |
   v
private instantiation / formalization / tests
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

The local layers should be able to explore, criticize, and eliminate large numbers of ideas between frontier interventions.

## Research state is likely a key bottleneck

Millions of local tokens are useless if the system repeatedly forgets discoveries or floods the director with transcripts.

A future system will need some form of **compressed mathematical research state** containing things like:

- live hypotheses;
- verified consequences;
- refuted branches;
- unresolved dependencies;
- equivalent/redundant formulations;
- known obstacles;
- promising representations;
- provenance and confidence/evidence type.

Do not design a permanent schema now. The important research hypothesis is that useful state should summarize **mathematical content and dependency**, not conversation history.

## Frontier budget must be measured

When comparing systems, keep Codex usage visible.

Otherwise a run may appear to demonstrate Mathia capability while the frontier director actually supplied the decisive mathematics.

Useful later ablations include:

```text
frontier director only

frontier director + generic local mathematical worker

frontier director + Mathia

frontier director + generic worker + formal specialist

frontier director + Mathia + formal specialist
```

Hold frontier budget and approximate local compute fixed enough to identify what each component contributes.

## What counts as progress on an open problem

For a genuinely open problem, final proof is too sparse a metric.

Possible intermediate progress signals include:

- a false auxiliary claim eliminated by verified counterexample;
- a nontrivial implication formally verified;
- an equivalent reformulation established;
- a special/restricted case extended;
- an assumption weakened;
- an independently rediscovered known result;
- a new lemma proved;
- a new conjecture that survives substantial falsification;
- a representation that repeatedly unlocks later work;
- convergence of independent branches on the same mechanism.

Human mathematical review may still be necessary to judge novelty or significance.

## Formalized open conjectures as a later substrate

Collections of open mathematical statements already formalized in Lean are attractive **later** because the top-level target is precise even when no proof is known.

They could let the system test intermediate claims against a formal environment while preserving the conceptual/formal distinction.

However:

- a Lean statement compiling does not prove it faithfully captures the intended informal conjecture;
- open-problem status can change;
- public conjectures are contamination risks for training/evaluation;
- `sorry`, unapproved axioms, or weakened targets must not count as proof;
- the first Mathia experiment should not jump directly to an open problem before establishing the semantic-intuition signal.

The earlier PR exploring this idea was deliberately closed during the semantic reset rather than merged against a stale repository narrative. The idea remains valid as a downstream hypothesis.

## Long-horizon fertility as future training feedback

A mature research loop creates a possible training signal unavailable in simple benchmarks.

An early Mathia intuition might later:

- generate several useful subclaims;
- survive independent criticism;
- produce a verified lemma;
- prune competing branches;
- be reused by another approach;
- cause Codex to allocate more research effort.

This suggests a future objective like:

```text
early idea
   -> downstream research utility
   -> credit assigned back to the idea/policy that produced it
```

That is a difficult long-horizon credit-assignment problem. It is not the current RL plan and should not be implemented before simpler semantic fertility has been demonstrated.

## Component-specific scaling

The architecture is useful only if bottlenecks can be diagnosed.

### Conceptual bottleneck

Local Mathia proposals are mostly shallow/false while a stronger model produces fertile mechanisms from the same state.

Possible response: scale/further train the conceptual specialist.

### Formal bottleneck

Conceptual proposals appear strong, but the formal worker cannot formalize or check even manageable consequences.

Possible response: improve formal model/search/tooling.

### Coordination bottleneck

Good results are produced but forgotten, duplicated, or never combined.

Possible response: improve research-state management/director policy, not GPU size first.

### Throughput bottleneck

The process works but is too slow.

Possible response: increase local hardware/parallelism.

The first small models are diagnostic components, not commitments to a permanent scale.

## Failure modes

The three-layer story can fail in several ways:

- Mathia produces high-volume conceptual prose with little mathematical fertility;
- filtering local noise costs more frontier reasoning than it saves;
- the formal specialist returns too many ambiguous failures to guide search;
- branch state grows faster than it can be compressed;
- agents converge on mutually reinforcing but false abstractions;
- the director dominates all decisive reasoning, making local specialization irrelevant;
- concrete verifier tasks leak back into Mathia training until it becomes another execution model;
- increased hardware only produces more low-quality search.

These should be tested, not narrated away.

## Relationship to the current epic

Nothing in this document authorizes building the system now.

The active sequence is:

```text
#30: establish a credible computation-free semantic benchmark
      |
#31: implement only the required plumbing
      |
#32: test the unchanged local base model
      |
credible semantic-intuition signal?
      |
only then consider training/integration experiments
```

The three-layer architecture becomes worth testing only after Mathia has some independently demonstrated conceptual behavior to contribute.
