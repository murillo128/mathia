# Three-layer mathematical research system hypothesis

## Status

This document records an **exploratory integration hypothesis**, not a settled Mathia architecture, execution roadmap, multi-agent framework specification, model-size commitment, or decision to make Lean the internal language of mathematical reasoning.

The hypothesis emerged from a practical asymmetry:

- frontier models such as Codex are likely to remain substantially stronger general mathematical reasoners than the first local Mathia model;
- frontier-model reasoning is comparatively scarce and quota-constrained;
- local specialist inference can be run for far larger token budgets at low marginal cost;
- formal verification can reject some classes of mathematical error exactly even when no frontier model is present.

The resulting question is not whether Mathia can outperform Codex in isolation. It is:

> **Can a strong but scarce research director obtain more useful mathematical progress by directing abundant local conceptual and formal specialists than by spending the same scarce frontier-model budget doing all exploration itself?**

A second, Mathia-specific question sits inside this system hypothesis:

> **At the same local inference budget, does a model specialized for conceptual mathematical fertility produce better research trajectories than a generic local mathematical reasoner?**

These are empirical questions. The three-layer organization below is a candidate way to ask them, not a commitment that the final system must have exactly three agents.

## Candidate division of labor

Conceptually, the proposed system has three different epistemic roles:

```text
                         Codex
                  scarce frontier layer
             direction / critique / prioritization
                            |
                +-----------+-----------+
                |                       |
                v                       v
             Mathia                  qwen-lean
       conceptual specialist       formal specialist
       abundant local search       abundant local checking
                |                       |
                +----------+------------+
                           |
                    accumulated evidence
                           |
                           v
                     next decision
```

The important distinction is functional rather than model-specific. Any of the concrete models may later be replaced if capacity or hardware proves insufficient.

### Codex: research direction under a scarce budget

Codex is not assumed to be weaker than Mathia. The opposite assumption is more realistic for the first experiments: Codex is the strongest general mathematical component in the system.

Its value therefore comes from **where its scarce reasoning is spent**. Candidate responsibilities include:

- maintaining a high-level view of the current mathematical state;
- deciding which approaches deserve more local compute;
- comparing independent lines of attack;
- detecting when apparently different branches are equivalent or redundant;
- asking for discriminating experiments rather than more unconstrained prose;
- identifying the weakest assumption, missing lemma, or most informative counterexample to pursue next;
- deciding when a formal result materially changes the conceptual picture;
- pruning dead or low-information branches;
- occasionally contributing its own mathematical ideas when local specialists stall;
- deciding what should be escalated to human mathematical review.

The intended use is **intermittent strategic intervention**, not putting Codex in every local generation loop. If Codex must reason through every proposal, proof attempt, and branch, the local specialists have failed to amplify the scarce resource.

### Mathia: abundant conceptual exploration

Mathia is the candidate conceptual specialist. Its target capability is not merely solving conventional problems or emitting elegant explanations.

It should be useful when asked to produce mathematical moves such as:

- changes of representation;
- candidate invariants;
- analogies across domains;
- assumption weakening;
- decompositions and recombinations;
- natural intermediate objects;
- candidate equivalences;
- conjectures and generalizations;
- informative examples and counterexamples;
- diagnoses of why an approach may be failing;
- alternative conceptual models of the same phenomenon.

The local-search advantage is that Mathia can be allowed to be wrong often. Thousands of cheap proposals may be worthwhile if criticism, computation, formalization, and later research use can strongly filter them.

This changes the unit of interest from average response quality to something closer to:

> **useful mathematical ideas produced per unit of local compute, after falsification and downstream use.**

A specialized Mathia model is interesting only if its proposals are more fertile than those of a compute-matched generic local model. Learning a recognizable style of conceptual prose would not be sufficient.

### qwen-lean: formal contact with mathematical reality

The formal specialist should not be treated merely as a theorem prover asked to solve the final conjecture.

Potentially more useful roles include:

- formalizing a proposed intermediate claim;
- checking that a claimed implication really follows;
- proving restricted or weakened versions of a conjecture;
- proving that two formulations are equivalent;
- verifying generated examples and counterexamples when they fit the formal environment;
- exposing missing assumptions;
- testing whether an apparently useful lemma is actually sufficient for a larger reduction;
- reusing previously verified lemmas in later branches;
- supplying exact evidence that can force conceptual revision.

Formal results have asymmetric meanings that must be preserved:

```text
proof verified                 -> strong positive evidence
counterexample verified        -> strong negative evidence
formalization succeeded        -> claim is precise, not necessarily true
proof search failed            -> weak/ambiguous evidence
formalization failed           -> may be tooling, representation, or claim ambiguity
```

A failed qwen-lean attempt must never be silently interpreted as evidence that a mathematical statement is false.

## Candidate research loop

The system is interesting because the layers can form a repeated empirical loop rather than a one-shot pipeline:

```text
conceptual proposal
        |
        v
critique / competing explanations
        |
        v
precise intermediate claim
        |
        v
formalization / computation / proof attempt
        |
        v
verified evidence or identified obstacle
        |
        v
conceptual revision
        |
        v
new branch, reduction, or conjecture
```

A concrete interaction might look like this:

1. Mathia proposes that a difficult phenomenon should be viewed through representation `R` and predicts that lemma `L` is the real bottleneck.
2. Local criticism attempts to break `L`, weaken it, or generate competing explanations.
3. qwen-lean checks whether `L` is formalizable, whether useful special cases can be proved, and whether `L -> target` can be verified.
4. Codex receives a compressed report rather than every raw trace.
5. Codex decides whether `L` deserves more search, should be weakened, should be connected to another branch, or should be abandoned.
6. Mathia explores the revised mathematical state at large local token budget.

This interaction can repeat many times without requiring the frontier model to generate the bulk of the tokens.

## Scarce direction, abundant exploration

The economic/computational hypothesis is central.

A frontier model may be much more capable per token while still being the wrong place to spend millions of routine exploratory tokens. Local models can instead absorb work with high expected waste:

- generating many candidate viewpoints;
- trying variants of an intermediate statement;
- looking for counterexamples;
- exploring consequences of a representation;
- repeatedly formalizing nearby claims;
- checking whether a dead branch can be repaired;
- rediscovering known structure from a new starting point.

The frontier layer should preferentially receive **selection problems**, not raw search volume.

This suggests a pattern such as:

```text
many local proposals
      -> local criticism / exact checks
      -> a small set of surviving branches
      -> frontier review and redirection
      -> another large local search wave
```

The exact batch sizes, intervention frequency, and communication protocol are intentionally undecided.

## The accumulated mathematical state matters more than the transcript

A long-running research process cannot repeatedly send millions of historical tokens back into every model.

The system therefore needs some way to preserve mathematical state at a higher level than raw conversation history. Conceptually, useful retained information might include:

- active conjectures and lemmas;
- established implications;
- verified results;
- counterexamples;
- abandoned approaches and why they failed;
- unresolved obstacles;
- relationships between branches;
- promising representations;
- which claims depend on which assumptions;
- questions whose resolution would most change the search.

This is a research problem in its own right. A good compression should preserve the mathematical structure needed for future reasoning without merely summarizing prose.

No storage schema, graph representation, DSL, or memory implementation is selected here. Prematurely fixing such a representation could constrain the conceptual layer before we understand what information useful mathematical research actually needs to retain.

## Progress on open problems without solving them

For sufficiently difficult open problems, final proof success is an unrealistic primary metric for small experiments. The system should still leave inspectable mathematical artifacts.

Candidate evidence of progress includes:

- rediscovery of known useful reformulations from limited context;
- independently convergent lines of reasoning;
- verified equivalences between formulations;
- correct weakening of assumptions;
- new proved special cases or auxiliary lemmas;
- falsification of plausible but incorrect intermediate conjectures;
- reductions whose sufficiency is formally verified;
- useful intermediate conjectures that survive substantial adversarial testing;
- connections to known mathematics that a human reviewer judges nontrivial and relevant;
- ideas that unlock later verified results elsewhere in the same search.

The last item is especially important for Mathia. A concept is mathematically **fertile** if it changes what can productively be done next.

A system that produces attractive explanations but no surviving consequences, reusable lemmas, discriminating experiments, or improved later search has not demonstrated the intended capability.

## Candidate controlled comparisons

The architecture should eventually be evaluated by ablation rather than by one impressive anecdote.

A useful comparison family could hold the frontier-model budget and local compute budget approximately fixed while varying the available specialists:

| Condition | Local mathematical worker | Formal worker | Frontier director |
|---|---|---|---|
| A | none | none | Codex |
| B | generic local model | none or simple checker | Codex |
| C | generic local model | qwen-lean | Codex |
| D | Mathia | none or simple checker | Codex |
| E | Mathia | qwen-lean | Codex |

The most diagnostic comparisons are not necessarily absolute leaderboard scores.

Examples:

- `B vs D`: does conceptual specialization improve local research fertility?;
- `D vs E`: does a formal specialist improve the trajectory rather than merely reject outputs?;
- `A vs E` at a fixed Codex budget: do abundant specialists amplify scarce frontier reasoning?;
- stronger local models substituted into `B/D/E`: is a failure caused by the process or by model capacity?;
- increased Codex budget with fixed local models: where does the marginal value of frontier direction saturate?

Metrics should distinguish at least:

- local proposal volume;
- survival after adversarial criticism;
- formalization rate;
- verified positive and negative results;
- duplication/redundancy rate;
- later reuse of an idea;
- frontier interventions consumed;
- human assessment of mathematical novelty/relevance for the small number of surviving outputs.

No single scalar "research quality" score is assumed to exist.

## Scaling is a component-level response, not a philosophical change

The first local models and the current single-Ada environment are experimental starting points, not claims about the compute ultimately required.

If a small implementation fails, the failure mode matters.

### Conceptual-capacity bottleneck

If Mathia generates many proposals but a strong director consistently finds them shallow while the same states elicit useful ideas from a stronger model, the conceptual worker may simply be too weak.

A larger Mathia model or more suitable mathematical base model is then a natural next test.

### Formal-capacity bottleneck

If conceptual proposals appear mathematically useful but qwen-lean repeatedly fails to formalize or prove consequences that stronger formal systems can handle, scale or replace the formal specialist.

### Coordination bottleneck

If useful results are produced but repeatedly forgotten, duplicated, isolated, or not used to redirect later search, more GPU may not help. The research-state and direction mechanism is the likely bottleneck.

### Throughput bottleneck

If all components behave usefully but exploration is simply too slow, additional hardware, batching, parallel specialists, or larger inference infrastructure are appropriate without changing the underlying research hypothesis.

This decomposition is important because "buy a larger GPU" should not become an unfalsifiable response to every negative result.

## Relationship to the current Mathia experiment

The current pre-RL conceptual-context study remains valuable and should not be redesigned around this three-layer hypothesis.

It tests a more elementary causal claim:

> Does a structurally useful mathematical representation improve held-out behavior for an unchanged local solver relative to strong controls?

That result is useful before deciding how to train a conceptual specialist.

The current critical path should therefore remain intact:

```text
freeze the pre-GPU experiment
        -> run the unchanged Qwen3-8B study
        -> analyze the evidence
        -> decide the next research-design question
```

A positive static-context result would strengthen the case that a specialist producing such representations can be useful inside a longer research loop.

A negative result must be interpreted more narrowly. It would weaken the specific static-context mechanism tested in that mathematical world. It would **not by itself falsify** a dynamic system where conceptual proposals are repeatedly challenged, formalized, tested, revised, and selected by a director.

Conversely, the existence of a compelling three-layer story is not a reason to skip the current signal experiment and immediately build orchestration infrastructure.

## Relationship to qwen-lean

The separate development of qwen-lean remains useful because it preserves an independently specialized formal model rather than assuming conceptual and formal abilities should be merged into one set of weights.

Possible later empirical outcomes remain open:

- two cooperating specialists outperform a joint model;
- a joint model is simpler and equally capable;
- conceptual training improves formal search enough that a separate formal model adds little;
- formal post-training improves the conceptual worker;
- a stronger off-the-shelf formal model replaces qwen-lean;
- only the verifier, rather than a learned formal specialist, proves necessary for some tasks.

The three-layer hypothesis therefore does not settle the existing open question of joint versus separate specialization.

## AI feedback and learning from the research process

The system could generate a particularly relevant source of training data for Mathia.

Codex and later mathematical outcomes can label distinctions such as:

- proposal was superficial;
- proposal duplicated an existing branch;
- proposal introduced a genuinely different representation;
- conjecture was quickly falsified;
- conjecture survived testing but led nowhere;
- lemma unlocked several later results;
- representation reduced formal search difficulty;
- branch was initially unattractive but ultimately fertile.

This creates examples of the form:

```text
mathematical research state
        + candidate mathematical move
        + later evidence
        -> estimated fertility / usefulness
```

That is closer to the desired Mathia signal than training directly on polished explanations.

However, teacher judgments must remain separate from mathematical truth. Codex preference can help prioritize search or bootstrap training data, but later verified consequences, counterexamples, transfer, and actual downstream usefulness should override stylistic preference when they disagree.

## Open-problem stress tests

Open problems are interesting because they prevent the experiment from collapsing into exact-answer imitation, but they should not all be treated equally.

A progression of stress tests could eventually include conjectures with:

- simple statements and cheap computational probes;
- rich existing surrounding theory;
- Lean-formalized top-level statements;
- many meaningful intermediate lemmas and equivalent formulations;
- enough difficulty that proof completion is not the expected outcome.

Problems such as Collatz, Goldbach, selected Erdos problems, and eventually much harder targets such as the Riemann hypothesis may be useful for different reasons.

For a Riemann-scale problem, the expected output of a bounded experiment is not a proof. The question is whether the system leaves behind mathematical structure worth inspecting: verified intermediate claims, useful reformulations, falsified branches, rediscovered methods, or genuinely promising hypotheses.

An impressive-looking final answer without such an inspectable research history would be weak evidence.

## Main risks

### Codex silently does all the mathematics

Because the director is stronger, a naive system may attribute progress to Mathia when Codex is actually generating the important mathematical ideas.

Controls need to record where ideas originated and compare compute-matched generic versus Mathia local workers under the same director budget.

### Local token volume becomes noise volume

Cheap inference is useful only if the system can reject, compress, and learn from failed branches. Scaling generation without improving selection may simply produce a larger pile of plausible mathematics.

### Formal fluency masquerades as mathematical progress

A model that emits type-correct Lean or proves easy consequences can appear productive without finding useful mathematics. Formal success must be interpreted relative to whether a result changes the research state.

### Proof-search failure is overinterpreted

The formal layer can be weak even when a conjecture is correct. Failure to prove must remain distinct from falsification.

### Research-state compression destroys the important idea

Aggressive summaries may erase precisely the representation, failed attempt, or unusual analogy needed later. Memory quality should itself be evaluated rather than assumed.

### Open-problem evaluation becomes anecdotal

A single interesting-looking run is not enough to support the architecture. Controlled comparisons on smaller environments and repeated research tasks remain necessary.

## Non-decisions

This document intentionally does **not** decide:

- the final number of agents;
- whether Codex is the permanent frontier director;
- the exact Mathia checkpoint or parameter count;
- the exact qwen-lean checkpoint or formal backend;
- whether workers run concurrently or sequentially;
- how often the frontier director intervenes;
- the research-state representation;
- a communication protocol or schema;
- a branch-search algorithm;
- an RL algorithm;
- whether specialist weights are eventually merged;
- which open conjecture should be the first long-running target;
- a fixed token budget for a future research run.

The durable hypothesis is narrower:

> **Use scarce frontier reasoning primarily for research direction and selection, abundant local conceptual reasoning for high-volume mathematical exploration, and formal methods for exact contact with mathematical consequences; then test whether the combination produces better research trajectories than its simpler ablations.**
