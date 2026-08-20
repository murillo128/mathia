# Riemann agentic research loop — execution reference

## Status

This document records an **exploratory downstream design reference** for a future final-execution issue. It is intended to preserve the current research model, role boundaries, loop structure, compute intuition, and success/stop conditions discussed after the Riemann and domain-agnostic Mathia corpus work.

It is **not** itself an executable issue, a settled multi-agent architecture, authorization to change any frozen experiment, or a replacement for the current controlled Mathia/qwen-lean evaluation line.

Related context:

- `docs/CONCEPTUAL_FORMAL_SEARCH_WITH_PARTIAL_PROOFS.md` — prior exploratory design for conceptual-formal search, diverse intuitions, feedback, and checked partial proofs;
- `docs/CONCEPTS_DIMENSIONS_INTUITION.md` — current conceptual/intution training hypothesis;
- `docs/RESEARCH_RESET_SEMANTIC_INTUITION.md` — semantic/execution separation and research reset;
- `docs/EVALUATION_METHODOLOGY.md` — broader evaluation discipline.

The future final-execution issue should treat this document as a design input to be challenged and converted into a bounded, reproducible contract only when the prerequisites are ready.

---

## Core objective

The target is not a one-shot prompt such as:

```text
prove RH
```

The target is an **accumulative mathematical research process** in which conceptual search, mathematical precision, formalization, proof search, and exact verification have distinct roles.

The central hypothesis is:

> Mathia should generate and revise mathematical representations, conjectures, decompositions, intermediate problems, and research directions; Codex should provide deep global scientific review and faithfully compile sufficiently precise mathematical claims into Lean; qwen-lean should apply large amounts of cheap formal proof-search compute; Lean should determine what is actually certified.

The system should be capable of making meaningful progress even when the terminal event

```text
RH proved
```

remains `0` for essentially the whole run.

A single genuinely new, non-trivial, formally certified intermediate result or reformulation may be a major success event and should not be treated as merely a small increase in a success percentage.

---

## Role boundaries

### Mathia A — global mathematical rethink

Mathia A is the high-budget conceptual research mode.

Its job is to reconsider the current research frontier and answer questions such as:

- What have we actually learned?
- Which apparently different lines are converging on the same structure or obstruction?
- Which assumptions keep reappearing?
- Which representations should be abandoned, weakened, generalized, or changed?
- Which partial results suggest a new object or intermediate statement?
- Which known Riemann formulations or nearby mathematical results resemble the current frontier?
- What should be investigated next?

Mathia A should receive a large relevant context and a large reasoning budget, but not raw repetition from thousands of formal attempts. The preferred input is a consolidated research state plus targeted retrieval from the Riemann corpus.

Its output is a small population of research directions, not Lean.

### Mathia B — mathematical formulation

Mathia B turns a selected research line into a sufficiently precise mathematical claim.

This is **mathematical formalization**, not Lean formalization.

Mathia B should make explicit:

- mathematical objects;
- assumptions;
- target statement;
- implication/equivalence direction;
- hidden hypotheses discovered during refinement;
- alternate precise formulations when materially different;
- what remains uncertain.

It may need substantial reasoning budget because the act of making a vague idea precise can expose that the original intuition was ambiguous, too strong, circular, or aimed at the wrong object.

### Codex — two deliberately different roles

Codex should have two roles whose boundaries must not be conflated.

#### Codex global reviewer/director

On relatively infrequent global-review events, Codex may reason deeply about the accumulated evidence.

Its job is to prevent a random walk by critically reviewing:

- certified reductions and proofs;
- refuted or failed conjectures;
- repeated formal bottlenecks;
- convergence between branches;
- likely circularities or hidden restatements;
- whether a new subproblem is genuinely more informative;
- what literature/corpus retrieval should be requested next;
- which lines deserve the next expensive Mathia rethink.

This is a **scientific direction and critique role**. It may use a large reasoning budget, but it should be invoked sparsely relative to local formal search.

#### Codex Lean compiler

Once Mathia B has produced a mathematically precise claim, Codex should try to represent that exact claim faithfully in Lean/mathlib.

Its job includes:

- finding existing mathlib definitions and APIs;
- selecting faithful Lean types and structures;
- resolving imports, coercions, namespaces, and notation;
- introducing auxiliary formal definitions when they preserve the intended mathematics;
- producing a compiling theorem statement and proof scaffold.

Codex should **not** silently improve, weaken, strengthen, or replace the mathematical problem merely because a different statement is easier to formalize or prove.

If the claim cannot be faithfully formalized, that is not a terminal failure. It enters a feedback loop with Mathia B.

### qwen-lean — formal proof worker

qwen-lean should begin once the mathematical problem is already represented as an exact Lean goal.

Its primary task is proof search after the `:= by` boundary, including:

- whole-proof attempts;
- diverse stochastic attempts;
- checked partial proof skeletons;
- proofs of extracted sub-obligations;
- recomposition of verified subproofs where practical.

It should not be expected to take a vague informal research proposal, decide what theorem it means, invent a faithful Lean statement, and prove it all in one step.

### Lean — exact arbiter

Lean decides what is formally certified.

Lean success does not by itself establish novelty, significance, or faithful correspondence to the intended informal statement. Those require separate audit.

### Deterministic controller

A controller should handle routine orchestration without expensive mathematical reasoning where possible:

- queues;
- deduplication;
- proof checking;
- extraction of remaining obligations;
- branch bookkeeping;
- provenance;
- artifact freezing;
- triggering global review after meaningful events.

The controller is not intended to become another mathematical reasoner.

---

## The main loops

The current picture contains four interacting loops rather than one monolithic agent conversation.

### 1. Global research loop

```text
persistent research frontier
          |
          v
Codex deep global review
          |
          v
Mathia A deep rethink
  + Riemann retrieval
          |
          v
new/revised research lines
          |
          v
Codex prioritization / critique
          |
          v
selected lines enter local work
```

The global loop should be **deep and sparse**.

It is explicitly allowed to use substantial Codex reasoning because the purpose is to keep the research process directed rather than random. The cost control comes from invoking it only after informative state changes or after a meaningful amount of local work, not after every formal attempt.

### 2. Mathematical formulation loop

```text
selected line
     |
     v
Mathia B
     |
precise mathematical claim
     |
     v
Codex Lean formalization
     |
     +---- formalizable ----> exact Lean statement
     |
     `---- blocked ----------> precise feedback
                                  |
                                  v
                               Mathia B
```

A Codex formalization failure should generate actionable feedback such as:

- an ambiguous mathematical object has multiple inequivalent Lean interpretations;
- a hidden mathematical assumption is required;
- the intended topology/measure/structure is underspecified;
- mathlib lacks required infrastructure;
- the intended claim appears to mix incompatible domains/types;
- the literal formalization would change the meaning.

Mathia B then refines, disambiguates, weakens, strengthens, or rejects its own claim as mathematically appropriate.

A line may remain mathematically interesting even when it is blocked by missing formal infrastructure.

### 3. Brute-force formal loop

Once a non-trivial theorem statement is faithfully formalized, the strategy changes.

```text
exact Lean theorem
       |
       v
qwen-lean x large N
       |
       v
Lean verification
       |
       +--> complete proof
       |
       +--> checked partial proof
       |
       `--> structured failure / no useful progress
```

The formal layer should be **wide and comparatively cheap**.

For important targets, `N` may be large. The objective is not to have Codex repeatedly rethink each proof attempt; it is to let the formal specialist explore aggressively, with continuous batching and early deduplication where practical.

Diversity may come from seeds, temperature, proof length budgets, alternative proof scaffolds, whole-proof versus partial-proof modes, and recursive attacks on extracted obligations.

### 4. Evidence/consolidation loop

Raw formal attempts should be compressed before expensive global reasoning.

```text
many formal attempts
       |
       v
dedup / cluster / verify
       |
       v
extract:
- complete certified proofs
- checked reductions
- recurring holes
- repeated unavailable assumptions
- convergent proof skeletons
- uninformative failure families
       |
       v
update persistent frontier
       |
       v
trigger global review when informative
```

Codex and Mathia should consume **evidence summaries and selected representative artifacts**, not thousands of near-duplicate proof transcripts.

---

## Compute shape: deep-and-sparse above, wide-and-cheap below

The intended compute profile is deliberately asymmetric.

| Phase | Context | Reasoning budget | Sampling width |
|---|---:|---:|---:|
| Mathia A — global rethink | very large/relevant | very high | very small |
| Mathia B — mathematical formulation | large | high/very high | small |
| Codex global review | large | very high | occasional |
| Codex Lean compiler | focused | medium/high | limited retries |
| qwen-lean proof search | focused | task-dependent | large/very large |
| Lean checker/controller | deterministic | none | massive |

The intended pattern is approximately:

```text
one deep review/rethink
        |
        v
a few precise conjectures
        |
        v
a few Lean targets
        |
        v
hundreds/thousands of formal attempts where justified
        |
        v
compressed evidence
        |
        v
next deep review/rethink
```

The goal is not to minimize Codex reasoning at all costs. The goal is to avoid a system in which Codex has to reconstruct the mathematics behind every Mathia output and every qwen-lean attempt. Codex should think deeply at high-leverage global decisions and during faithful formalization, while routine search and validation are delegated.

---

## Riemann-specific progressive focusing

The research process should not repeatedly restart from a broad list of Riemann strategies.

As evidence accumulates, Mathia A should progressively focus retrieval and reasoning around the current frontier.

Example shape:

```text
broad RH search
      |
several perspectives
      |
independent lines converge on condition P
      |
P becomes a first-class research object
      |
retrieve known criteria/formulations near P
      |
identify narrower statement P'
      |
formalize/test P' and its relation to parent goals
```

The Riemann corpus is therefore not only training data. It may also be used as a retrieval substrate during the global rethink to answer questions such as:

- Does our current object already have a name?
- Does our condition resemble a known positivity, spectral, transform, or explicit-formula criterion?
- Are we rediscovering a historical reformulation?
- Is the apparent new object a restricted or generalized version of something known?
- Which exact difference separates the current frontier from an existing theorem?

The desired effect is to **center the target progressively** rather than generate unrelated ideas indefinitely.

---

## Persistent frontier instead of one-shot success rate

For RH, theorem-level solve percentage is not an informative global optimization target. The expected result may remain zero for the entire run; a single genuine success event may be scientifically exceptional.

The persistent frontier should preserve progress such as:

- exact verified lemmas;
- verified reductions between open statements;
- candidate equivalences;
- unresolved but precise conjectures;
- formalization-blocked claims;
- repeated bottlenecks;
- refuted directions;
- known-result rediscoveries;
- apparently novel statements awaiting prior-art review;
- provenance of where each idea entered the system.

Useful progress is a change in the mathematical state of knowledge, not an increase from `0%` to `1%` in a benchmark-style rate.

---

## Checked partial proofs and `sorry`

A checked partial proof can be a major research event even when the final theorem remains open.

Suppose qwen-lean produces:

```lean
by
  have h1 : A := by
    ...
  have h2 : S := by
    sorry
  ...
  exact finish h1 h2
```

The `sorry` itself is not the scientific certificate. The preferred normalization is to extract the hole as an explicit hypothesis and recheck the surrounding reduction without `sorry`:

```lean
theorem parent_from_S (hS : S) : Parent := by
  ...
```

If Lean accepts that theorem without holes, then the edge

```text
S -> Parent
```

is formally certified even though `S` remains open.

This can already be a major success if the reduction is non-trivial and novel.

### Reduction versus reformulation

These cases must be distinguished:

```text
S -> RH
```

is a formally certified sufficient condition/reduction.

```text
RH -> S
```

is a formally certified necessary consequence.

```text
RH <-> S
```

is a formally certified reformulation/equivalence.

A genuinely new, non-trivial `RH <-> S` would be a potentially major mathematical result even if `S` itself remains unsolved.

A genuinely new, non-trivial `S -> RH` may also be a major result because it has reduced RH to a different precise problem.

Partial proof search should therefore not be scored merely as `complete/fail`. It can discover useful formally certified reductions.

---

## Success and stop conditions

The search should have **absorbing review states**. When a rare strong result appears, the system should stop exploration long enough to understand exactly what happened.

### Candidate stop events

Examples include:

- a complete non-trivial Lean proof of a relevant claim;
- a novel non-trivial checked reduction `S -> T` whose parent is strategically important;
- a novel non-trivial equivalence/reformulation `S <-> T`;
- closure of a bottleneck shared by several previously independent branches;
- a result that appears to be mathematically new after initial prior-art comparison.

A novel partial proof with `sorry` should trigger the same attention when its holes can be extracted into explicit obligations and the surrounding reduction is verified without holes.

### Stop means switch to audit mode

A stop event should freeze the original artifact and switch from exploration to verification/audit.

The audit should preserve and independently recheck:

- exact statement;
- exact proof or checked reduction;
- all imports and environment revisions;
- model/checkpoint and generation provenance;
- any Mathia/Codex reformulations made along the way;
- absence of hidden `sorry`/`admit` or ad-hoc axioms;
- whether assumptions are consistent and genuinely weaker than the target;
- whether the statement faithfully represents the intended mathematics;
- whether the result is already known under another formulation;
- whether novelty survives expert/literature scrutiny.

Only after audit should the global search resume or terminate permanently.

---

## Triviality and false-success audit

Lean verification alone is not sufficient evidence of useful progress.

Before treating a result as a success, explicitly check for failure modes such as:

- the conclusion was already an assumption;
- a hypothesis equivalent to or stronger than the target was introduced;
- the assumptions are inconsistent and make the theorem vacuous;
- the target was weakened during Codex formalization;
- an RH-equivalent condition was merely hidden under a new definition;
- the theorem is already available in mathlib or the imported environment;
- the result is a direct definitional simplification;
- the claimed reduction direction was accidentally reversed;
- the new statement is just a syntactic restatement of a previously certified statement.

The right question is not only `does Lean accept this?`, but:

> What exactly has been proved, how does it relate to the intended claim, and what mathematical difficulty has actually been removed or reorganized?

---

## Formalization-blocked conjectures are not discarded

A mathematically interesting conjecture that Codex cannot faithfully formalize should enter a refinement loop rather than be thrown away.

Possible statuses include conceptually:

```text
mathematically_open
formalization_ambiguous
formalization_blocked_by_missing_assumption
formalization_blocked_by_mathlib_infrastructure
formalized
reduction_verified
subgoal_open
subgoal_solved
```

These labels are illustrative research states, not a proposal for a permanent DSL.

The important invariant is that `Codex could not formalize it` is kept distinct from `the mathematics is wrong`.

---

## Global review should be mathematically deep

The Codex global-review layer should not be reduced to success percentages or mechanical branch scores.

A useful review may conclude things like:

```text
- two formally unrelated branches now depend on the same positivity condition P;
- P appears in three independent constructions, so it may be structural rather than an artifact;
- every direct attempt at P introduces an unjustified stronger hypothesis H;
- a restricted P' may still be sufficient for intermediate result R;
- retrieval should now focus on criteria/formulations close to P/P', not on broad RH approaches;
- Mathia should reconsider whether the true object is the original operator or the induced quadratic form.
```

This review can be expensive. Its purpose is to prevent unstructured exploration and to give Mathia a high-quality research state to rethink.

---

## Provenance and two evaluation modes

Because Codex may reason deeply in the global loop, preserve idea provenance.

Useful provenance categories include:

- Mathia-generated idea;
- Mathia reformulation after formalization feedback;
- Codex critique;
- Codex-originated mathematical proposal;
- retrieval-originated connection;
- formal-feedback-derived subproblem;
- human-provided direction.

This allows two distinct modes later:

### Research mode

Use all useful components, including Codex-originated mathematical suggestions, to maximize the chance of making mathematical progress.

### Mathia evaluation mode

Constrain Codex so that it may critique, formalize, summarize evidence, and allocate compute without injecting a new mathematical solution, allowing cleaner attribution of Mathia's capability.

The same infrastructure may support both, but their claims must not be mixed.

---

## Provisional model choice

For the future Mathia specialist, the current preferred main base is:

```text
Qwen3.5-9B-Base
```

This is a downstream design preference, not authorization to modify the current frozen experiments that deliberately preserve other exact base/checkpoint choices for controlled comparison.

Possible trained checkpoints to preserve scientifically include:

- base control;
- general `qwen-mathia` trained on the domain-agnostic conceptual corpus;
- Riemann-only ablation;
- `qwen-mathia-riemann` obtained by adding Riemann specialization after/general-with the conceptual base.

The exact training order, mixing strategy, adapter/full-finetune choice, and ablation matrix should be frozen in the eventual training issue rather than assumed here.

---

## Provisional Ada x2 Small runtime mapping

A useful minimal runtime hypothesis for the final agentic experiment is an Ada x2 node with one specialist per GPU:

```text
GPU 0: qwen-mathia / qwen-mathia-riemann
GPU 1: qwen-lean
CPU:   orchestrator + Lean verification + deterministic consolidation
```

The intended behavior is:

- Mathia uses relatively few, long, high-thinking generations;
- qwen-lean uses high-throughput concurrent proof sampling;
- Lean verification runs in bounded CPU parallelism;
- while qwen-lean drains a formal batch, Mathia may prepare the next high-level reconsideration/revision when appropriate;
- the initial implementation should keep the two GPU roles fixed for clean measurement before considering dynamic adapter/model routing.

A likely scaling bottleneck may be CPU/RAM for Lean checking rather than GPU memory, so the final issue should measure queueing and utilization before deciding whether an x2 Medium or larger system is justified.

---

## What the final execution issue should freeze

When the project is ready to turn this reference into an executable issue, that issue should freeze at least:

- exact Mathia checkpoint(s);
- exact qwen-lean checkpoint;
- exact Lean/mathlib environment;
- exact Riemann research-state seed/frontier;
- retrieval corpus revisions and access rules;
- Mathia A and Mathia B interfaces;
- Codex global-review and Lean-compiler boundaries;
- formalization-feedback behavior;
- qwen-lean generation budgets and diversity controls;
- partial-proof/hole extraction procedure;
- deterministic dedup/consolidation rules;
- global-review trigger policy;
- success/stop/audit protocol;
- provenance requirements;
- hardware/runtime topology;
- how Codex cost and token usage are logged;
- which behaviors belong to research mode versus Mathia evaluation mode.

The final issue should prefer bounded discriminating tests before authorizing an indefinitely recursive search.

---

## Open questions intentionally left unresolved

This reference does **not** settle:

- the exact cadence for global Codex/Mathia reviews;
- how much context Mathia receives directly versus through retrieval;
- how the research frontier is serialized;
- whether Mathia A and Mathia B use different adapters/prompts or only different context/interface;
- the exact number of qwen-lean samples per theorem;
- the exact recursive depth for partial-proof decomposition;
- how much Codex-originated mathematics is allowed in research mode;
- the novelty/prior-art review mechanism;
- the threshold for promoting an intermediate reduction to a global stop event;
- whether later scaling should use larger dense or MoE bases;
- whether a shared base/adapters between Mathia and qwen-lean is ultimately beneficial.

These should be decided from evidence and from the concrete state of the trained specialists when the final execution issue is written.

---

## Compact reference picture

```text
                 PERSISTENT RESEARCH FRONTIER
                            |
                            v
                  CODEX GLOBAL REVIEW
                   deep, infrequent
                            |
                            v
                    MATHIA A RETHINK
             deep reasoning + Riemann retrieval
                            |
                            v
                    candidate directions
                            |
                            v
                  CODEX PRIORITIZATION
                            |
                            v
                     MATHIA B FORMULATE
                            |
              precise mathematical conjecture
                            |
                            v
                    CODEX -> LEAN
                     faithful compiler
                       /          \
                 blocked          formalized
                    |                 |
                    v                 v
                 Mathia B         QWEN-LEAN x N
                 feedback              |
                                       v
                                      LEAN
                                       |
                     +-----------------+----------------+
                     |                 |                |
                  proof          checked partial      failure
                     |                 |                |
                     +-----------------+----------------+
                                       |
                              consolidate evidence
                                       |
                               update the frontier
                                       |
                       informative event / stop event
                                       |
                          global review or audit mode
```

The intended research principle is:

> Spend expensive conceptual reasoning on deciding **where to drill and what the mathematical claim really is**; once a faithful Lean target exists, spend cheap parallel formal compute aggressively; preserve every informative failure and partial reduction; and interrupt exploration immediately when a non-trivial verified result or reformulation may have changed the mathematical state of the problem.
