# Conceptual-formal search with diverse intuitions and partial proofs

## Status

This document records a **downstream exploratory design hypothesis**. It is not the active #32 protocol, a settled architecture, an implementation plan, or authorization to change any frozen experiment.

The hypothesis is motivated by two observations:

1. repeated qwen-lean sampling can recover substantial practical solve coverage relative to a much stronger one-shot reasoner, suggesting that local test-time search is an important resource;
2. Mathia may be more valuable if it changes and diversifies the formal worker's search distribution than if it merely produces one polished intuition before one long proof attempt.

The central question is therefore broader than whether a single intuition increases pass@k:

> **Can Mathia organize local test-time compute across multiple mathematical representations, use formal evidence to revise selected representations, and recursively reduce large proof obligations into smaller formally certified subproblems more effectively than flat proof sampling?**

This should remain falsifiable. A more elaborate loop is not evidence of mathematical reasoning unless it beats compute-matched simpler alternatives and survives controls against prompt optimization, proof leakage, and Lean-specific debugging.

## Motivation from repeated formal sampling

The qwen-lean cross-model assessment suggests that repeated direct samples from a relatively small formal specialist can close a meaningful fraction of the practical solve-rate gap to a much stronger reasoning model. This does not imply that the models or procedures are compute-matched, but it motivates treating **test-time diversity and search allocation** as first-class experimental variables.

A natural Mathia question follows:

```text
where should additional local compute go?

more formal samples under one representation
                    vs
more mathematical representations with fewer samples each
                    vs
adaptive revision/decomposition based on formal evidence
```

The working hypothesis is that useful conceptual diversity may reduce correlation between formal-worker failures. If two intuitions induce meaningfully different proof distributions, sampling both may cover more proof space than spending the same budget repeatedly under one intuition.

Conceptually:

```text
P(proof | theorem, intuition_1)
        !=
P(proof | theorem, intuition_2)
```

The scientific value of Mathia would then lie partly in producing **complementary search distributions**, not merely the individually highest-rated explanation.

## Mixed spontaneous and directed intuition search

A mature search process should probably preserve both **spontaneous** and **directed** conceptual exploration.

### Spontaneous intuition

Mathia generates several candidate perspectives without being told which conceptual move to use.

Purpose:

- preserve the possibility of discovering strategies outside the current human-authored taxonomy;
- test what diversity the model generates naturally;
- avoid defining mathematical creativity as compliance with a fixed list of conceptual labels.

Example shape:

```text
T
|- spontaneous S1
|- spontaneous S2
|- spontaneous S3
`- ...
```

### Directed intuition

Other branches are deliberately pushed toward different weak conceptual directions, for example:

- look for an invariant;
- decompose the object or statement;
- identify what information is preserved or lost;
- change representation;
- search for an obstruction or essential assumption;
- understand the result as a composition of simpler mechanisms;
- look for a bridge object or intermediate structure.

The direction should remain **conceptual rather than proof-prescriptive**. It should not supply a particular Lean lemma, tactic sequence, or nearly complete proof route.

Purpose:

- force coverage of conceptually different regions that stochastic sampling may otherwise miss;
- test whether candidate conceptual dimensions actually induce different mathematical behavior rather than different prose;
- provide controlled branches whose later revision can be studied.

### Why both matter

Only spontaneous search risks collapsing into many near-duplicate high-probability perspectives.

Only directed search risks injecting from outside exactly the diversity/capability Mathia is supposed to learn.

A mixture allows both questions to remain visible:

1. **What perspectives does Mathia find by itself?**
2. **Can Mathia productively operate within a deliberately selected conceptual perspective?**

A later comparison could separate free diversity from forced diversity under matched formal compute.

## First formal pass

Each spontaneous and directed intuition conditions a bounded qwen-lean search.

Conceptually:

```text
                          |- S1 -> qwen-lean x k
                          |- S2 -> qwen-lean x k
T -> intuition population |- D1 -> qwen-lean x k
                          |- D2 -> qwen-lean x k
                          `- D3 -> qwen-lean x k
```

The first pass should preserve more information than a binary theorem-level success flag. Useful evidence may include:

- complete verified proof;
- verified partial proof skeleton with explicit remaining obligations;
- repeated failure patterns around an unavailable assumption or impossible construction;
- generation failure or Lean rejection;
- candidate cost and overlap between branches.

The important scientific object is how the intuition changes the formal search, not whether the resulting Lean text sounds plausible.

## Feedback and selective revision

After the first formal pass, Mathia receives **abstracted mathematical feedback** about selected directed branches and may revise them before a second formal pass.

The initial hypothesis is to revise the **directed** branches while keeping spontaneous branches as an unrevised comparison. This creates three distinguishable objects:

1. spontaneous perspectives found naturally;
2. directed perspectives induced by a chosen conceptual direction;
3. directed perspectives revised using external formal evidence.

This lets us ask whether feedback produces something beyond additional independent samples.

### Feedback should be mathematical, not merely Lean debugging

Raw Lean errors may encourage Mathia to become a syntax/tactic debugger rather than a conceptual reasoner.

Where possible, formal outcomes should be summarized at a more mathematical level, for example:

```text
Several attempts from this perspective require a property
stronger than the available hypotheses.

The current reduction is formally valid except for obligation S.

Two generated routes construct the same intermediate object,
but neither establishes the needed compatibility condition.
```

The exact abstraction mechanism is deliberately undecided. It must not silently insert the missing mathematics from a stronger model.

### Constrained revision before free replacement

A useful first test is to ask a directed branch to **revise while preserving its assigned conceptual direction**.

For example:

```text
D = approach through decomposition

formal evidence
        |
        v
D' = revised decomposition-based approach
```

This distinguishes:

- repairing/evaluating a perspective;
- abandoning one perspective and generating a completely different one.

Both may ultimately be useful, but they should not be conflated experimentally.

A later condition can allow free reconsideration and compare it against constrained revision.

### Selection may matter as much as revision

Not every branch should necessarily receive equal additional compute.

The first pass may reveal:

```text
D1 -> complete proof found
D2 -> coherent reduction with one difficult obligation
D3 -> no stable formal structure / repeated uninformative failures
```

A later Mathia capability of interest is therefore **perspective selection**:

- exploit a successful/promising branch;
- revise a branch with informative failure;
- abandon or radically reframe a sterile branch.

This is a mathematical decision problem in its own right and should eventually be compared against simple mechanical allocation policies.

## Partial proofs and `sorry` as certified reductions

For large theorems, requiring every qwen-lean attempt to produce a complete proof may discard valuable mathematical progress.

A formal worker should eventually be allowed to construct proof skeletons containing explicit `sorry` holes, provided the surrounding term/script is checked and the holes are extracted as precise proof obligations.

Example:

```lean
by
  have h1 : L1 := by
    ...
  have h2 : L2 := by
    sorry
  ...
  exact ...
```

The key interpretation is:

> **A checked partial proof is a formally certified reduction of the original theorem to its remaining obligations.**

If Lean accepts the surrounding structure modulo `sorry`, then proving the extracted obligation(s) is sufficient for completing that route.

This is qualitatively richer feedback than treating every non-complete generation as zero.

## `sorry` is not success by itself

Allowing holes introduces an obvious degeneracy:

```lean
by
  sorry
```

or equivalently:

```lean
have h : T := by sorry
exact h
```

Such outputs contain no useful decomposition despite being syntactically expressible as partial proofs.

Therefore:

- the presence of a checked `sorry` must **not** itself count as progress or reward;
- a partial proof is primarily a proposal for a reduction;
- the strongest evidence that the reduction is useful comes from spending later compute on the extracted obligations and successfully composing the resulting proofs back into the parent theorem.

This avoids inventing a premature heuristic for "good sublemma" quality.

## Recursive subproblem search

A large theorem may naturally turn into a tree of formally linked obligations:

```text
T
|
|- S1  [proved]
`- S2
   |
   |- S2a [proved]
   `- S2b
      |
      |- S2b1
      `- S2b2
```

The unit of search then becomes neither simply an intuition nor a complete proof, but something closer to:

> **a formally certified reduction from one mathematical goal to a set of new goals.**

This connects directly to the conceptual capabilities Mathia is intended to explore:

- decomposition;
- simplification;
- change of representation;
- bridge construction;
- abstraction;
- perspective selection;
- diagnosis and revision.

Lean remains an external reality check rather than Mathia's conceptual language: it certifies that a proposed reduction really suffices, while Mathia remains free to represent and reason about the mathematics at a higher level.

## Feedback can choose between revising the parent and proving the hole

When a partial proof leaves an obligation `S`, the next action need not always be "prove S".

The feedback phase can consider alternatives such as:

1. attack `S` directly;
2. decompose `S` into smaller obligations;
3. find a weaker or differently stated lemma that is still sufficient;
4. revise the parent intuition so that `S` is avoided;
5. abandon the branch if the reduction appears sterile;
6. allocate more samples to an already promising sibling branch.

This produces a possible loop:

```text
intuition / perspective
        |
        v
formal attempt
        |
        v
complete proof OR certified remaining obligations
        |
        v
select: prove / decompose / revise / abandon
        |
        v
new formal attempts
        |
        `----> repeat
```

The loop should not be assumed to be superior merely because it is adaptive. It needs matched-budget comparisons against flat resampling.

## Candidate compute-matched experiments

The first useful tests should remain small and discriminating rather than implement a full research agent.

### Experiment A: where to allocate formal samples

Hold total qwen-lean generations fixed, for example 16 per theorem:

```text
1 intuition  x 16 proofs
2 intuitions x  8 proofs
4 intuitions x  4 proofs
8 intuitions x  2 proofs
16 intuitions x 1 proof
```

Measure theorem coverage and overlap between intuition-conditioned success sets.

The key question is whether conceptual diversity reduces correlated failure enough to beat deeper sampling under one representation.

### Experiment B: spontaneous vs directed diversity

At matched formal budget compare, for example:

```text
all spontaneous intuitions

mixed spontaneous + directed intuitions

all directed intuitions
```

This tests whether forced conceptual coverage adds value beyond ordinary stochastic diversity, while retaining the possibility that spontaneous search discovers better perspectives than the current taxonomy.

### Experiment C: feedback vs more independent samples

Compare equal total formal compute:

```text
initial intuitions
+ extra independent qwen-lean samples

vs

initial intuitions
+ formal feedback
+ revised directed intuitions
+ second qwen-lean pass
```

A gain in the second condition would be evidence that:

```text
idea -> evidence -> conceptual revision
```

adds something beyond additional sampling.

### Experiment D: whole-proof continuation vs subproblem continuation

When the first pass produces a checked skeleton with an obligation `S`, compare how to spend the remaining budget:

```text
continue sampling the original theorem T

vs

sample proofs of S and compose any success back into T
```

If pursuing `S` produces more completed parent proofs under matched compute, partial-proof decomposition has measurable search value.

### Experiment E: Mathia allocation vs mechanical allocation

Only after partial-proof search itself shows signal, compare Mathia's choice of:

```text
prove hole / decompose / revise parent / abandon
```

against simple baselines such as always pursuing the smallest hole, always resampling the parent, or uniform allocation.

This helps distinguish mathematical search policy from merely having access to a recursive formal mechanism.

## A provisional richer notion of intuition fertility

The current intuition-fertility experiment appropriately uses whole-proof success as a clean initial signal.

For later work, fertility may need to include whether a perspective:

- opens proof regions not reached by other perspectives;
- yields a formally valid and useful reduction;
- creates subgoals that are easier for the formal worker than the parent goal;
- survives or improves after formal feedback;
- helps choose which branch deserves additional compute;
- transfers to alternate presentations, checkpoints, or formal workers.

A useful population of intuitions may therefore be more important than the single best intuition.

Two individually weaker but complementary perspectives could have greater joint value than two near-duplicates of the strongest single strategy.

This suggests a future optimization target based on **joint coverage and complementary downstream utility**, not convergence toward one teacher-style explanation.

## Relationship to Mathia's conceptual hypothesis

A possible downstream conceptual picture becomes:

```text
concepts
   |
conceptual moves
   |
population of perspectives
   |
formal attempts / reductions
   |
checked evidence and obligations
   |
selection / revision / abandonment / decomposition
   |
new perspectives or subproblems
   |
...
   |
complete proof or other checked mathematical result
```

The deeper hypothesis is that the capability worth learning may be the **dynamics of conceptual exploration under mathematical evidence**, not only static generation of a high-quality intuition.

That would be a materially stronger claim than learning a conceptual explanation style.

## Main confounds and failure modes

### More compute disguised as better reasoning

Any adaptive loop must be compared under controlled total formal and conceptual compute. Otherwise gains may simply come from generating more candidates.

### Injected conceptual diversity

Directed prompts may supply the useful mathematical move externally. Improvements in directed branches do not by themselves prove that Mathia can discover or select those moves.

### Lean debugging instead of conceptual revision

If feedback exposes low-level errors or fixes, Mathia may optimize tactic/syntax behavior rather than mathematical representation. Transfer and feedback-abstraction controls are important.

### Trivial holes

`sorry` can represent no decomposition at all. Hole count, syntax validity, or partial-proof length must not become reward proxies without behavioral validation.

### Solver-specific steering

A perspective might merely be an effective prompt for one qwen-lean checkpoint. Later transfer should vary model checkpoint, prompt/presentation, or worker where practical.

### Branch explosion

Recursive reductions can create more obligations than they solve. A complex tree is not progress. The process must eventually show better completed-proof yield, cost, reusable verified lemmas, or another externally checked outcome.

### Premature search heuristics

Do not begin by designing an elaborate subgoal score, scheduler, DSL, or permanent proof-state schema. First establish whether decomposition, revision, and adaptive allocation provide a measurable advantage over simple controls.

## Relationship to the current #32 experiment

This document must **not change #32**.

The frozen #32 whole-proof intuition-fertility pre-test remains valuable because it asks a simpler causal question: can one compact strategic intuition change verified whole-proof yield from the fixed qwen-lean worker under a matched budget?

That clean result should come first.

The ideas in this document become relevant only after the current measurement channel is informative enough to justify a broader test-time-search experiment.

In particular, do not retrospectively reinterpret #32 as having tested:

- multiple intuition populations;
- directed vs spontaneous exploration;
- feedback revision;
- partial proofs with `sorry`;
- recursive subproblem solving;
- adaptive branch allocation.

Those are distinct downstream hypotheses.

## What remains deliberately undecided

This document does not choose:

- an orchestration framework;
- a permanent research-state representation;
- a subgoal scheduler;
- an RL objective;
- a reward formula for partial proofs;
- a fixed taxonomy of directed perspectives;
- how many spontaneous/directed branches should be used;
- how feedback should be summarized;
- whether Mathia, Codex, qwen-lean, or deterministic tooling should perform any future selection step;
- a maximum recursion depth;
- a final compute-allocation policy;
- an implementation roadmap.

Those decisions should follow evidence from the smallest experiments that can distinguish flat sampling, conceptual diversity, feedback-based revision, and certified decomposition.