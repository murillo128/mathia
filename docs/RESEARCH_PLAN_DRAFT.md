# Draft research plan: learning conceptual mathematical reasoning

This document is the first research plan for **Mathia**. It is deliberately a **draft**: it turns the current philosophical hypothesis into falsifiable experiments without fixing a final architecture, dataset schema, reinforcement-learning algorithm, model family, or relationship to Lean.

The immediate goal is not to build the final Mathia system. It is to answer a more basic question:

> **Can we create a trainable signal for conceptual mathematical understanding that measures what a representation enables the model to do, rather than how insightful its explanation sounds?**

If the answer is no, the project should change its hypothesis or evaluation before scaling a corpus or training run.

## 1. Research hypothesis

The current working hypothesis is that a substantial part of deep mathematical reasoning consists of **searching for, constructing, composing, and selecting representations** in which apparently different facts become simple consequences of a small number of relationships.

This conceptual competence is related to, but not identical with, formal theorem proving.

A formal prover answers questions such as:

- does the conclusion follow from these assumptions?
- can the statement be formalized exactly?
- can a valid proof be constructed?

The conceptual layer should be able to ask and act on questions such as:

- what is really happening here?
- what information is accidental?
- what is invariant?
- what can be forgotten safely?
- what representation makes the phenomenon simple?
- what assumption is doing the real work?
- what other mathematical language makes this problem natural?
- can two ideas from different fields be composed?
- what conjecture should follow if this interpretation is correct?
- what alternative viewpoint might expose structure that the current one hides?

The intended output is not merely a better explanation. A conceptual representation should be **fertile**: it should improve subsequent mathematical behavior.

## 2. What we want to operationalize

The working synthesis identifies several candidate manifestations of mathematical understanding. These are not yet a dataset schema or a fixed taxonomy.

### Compression

Many local facts become manifestations of a smaller structural mechanism.

### Prediction

A conceptual interpretation allows the model to anticipate mathematical consequences that were not supplied when the interpretation was produced.

### Transfer

The same mechanism is recognized under a substantially different surface representation or in another mathematical domain.

### Counterfactual reasoning

The model can predict what changes when an assumption, object, operation, or representation is modified.

### Generation

The representation suggests useful lemmas, examples, counterexamples, generalizations, or conjectures.

### Simplification

The model finds a representation in which a problem requires less mathematical work or a simpler proof strategy.

### Composition / synthesis

Different concepts or fields are combined because neither alone gives the right viewpoint.

### Bridge construction

The model invents or identifies an intermediate mathematical object that translates a problem into a domain with better tools.

### Reframing

The model can find genuinely different interpretations of the same phenomenon, not merely paraphrases.

### Perspective selection

Given several legitimate viewpoints, the model chooses one that fits the current mathematical objective.

### Naturalness / canonicality

The model distinguishes constructions forced by the structure of the problem from arbitrary proof choices or ad hoc tricks.

### Simplicity / beauty

The model should develop a preference for representations and proofs with economy, unity, symmetry, minimal accidental choices, and explanatory inevitability — but only insofar as these properties correlate with mathematical usefulness. Beauty is a heuristic signal, not a correctness oracle.

## 3. Core experimental principle: commit before the hidden test

A central design idea is to separate **forming a conceptual representation** from knowing exactly how it will be used.

The basic interaction should look conceptually like:

```text
visible mathematical situation
            |
            v
construct a conceptual representation
            |
     commit / freeze
            |
            v
reveal an unseen intervention or question
            |
            v
measure what the representation enables
```

This matters because if the model sees the target task first — for example, "weaken this assumption" — it may learn a specialized solving trick rather than a reusable understanding of the mathematical situation.

A good representation should remain useful across several possible downstream questions.

This is the closest current operational approximation to the statement:

> "The model understood the object before it knew exactly what we were going to ask about it."

## 4. First mathematical world

The first environment should be deliberately small, inspectable, mathematically rich, and cheap to verify exactly.

The leading candidate is the connected world around:

```text
divisibility
<-> gcd
<-> congruence
<-> residue classes
<-> units / invertibility
<-> permutations and cycles
<-> finite group structure
```

This world is attractive because it contains many of the desired conceptual moves while allowing exact computational checking.

Examples include:

- recognizing that congruence forgets absolute value while preserving residue information;
- seeing coprimality as a reversibility condition;
- recognizing multiplication by a unit as a permutation of residue classes;
- weakening primality assumptions to invertibility/coprimality when appropriate;
- simplifying gcd problems through transformations that preserve common divisors;
- moving from arithmetic language to finite-group language;
- distinguishing genuine quotient-compatible structure from superficial analogies;
- finding small counterexamples when a proposed interpretation is too strong.

The purpose is not to declare number theory the preferred domain for Mathia. It is an experimental sandbox in which conceptual claims can be tested cheaply.

Other worlds — finite groups and linear maps/kernel/image/quotient in particular — should remain natural later comparisons.

## 5. Experimental unit: mathematical situations, not theorem explanations

The first dataset/environment should not primarily contain pairs of the form:

```text
theorem -> explanation
```

Instead, the unit of investigation should be a **mathematical situation** containing some mixture of:

- definitions;
- examples;
- counterexamples;
- related facts;
- partial theorem families;
- numerical or algebraic observations;
- competing patterns;
- possibly one or more proofs;
- deliberately hidden consequences.

The model is asked first to construct a compact way of seeing the situation.

Only after that commitment does the environment select a hidden test.

The exact serialization and schema should remain open until hand-designed examples reveal what information is genuinely useful.

## 6. Hidden interventions

The hidden tests are where conceptual quality becomes observable.

Candidate interventions include the following.

### Predict

Ask for a consequence not explicitly present in the visible material.

### Weaken or modify assumptions

Change an assumption and ask whether the mechanism should survive, what should replace it, or what is the first failure.

### Counterexample

Ask the model to find the smallest or most informative case that breaks its own interpretation.

### Transfer

Present a superficially different situation governed by the same mechanism and test whether the model recognizes the connection.

### Reframe

Ask for a genuinely different representation and compare which future questions each viewpoint makes easier.

### Simplify

Present a problem whose direct representation is cumbersome and test whether the conceptualization leads to a shorter or more robust solution path.

### Compose

Provide an additional concept or mathematical domain and ask whether constructing a bridge produces a useful new attack.

### Generalize

Ask which theorem or family should exist if the proposed mechanism is really the source of the observed facts.

### Diagnose failure

Provide a failed conjecture, proof attempt, or analogy and ask what part of the conceptual model needs repair.

Not every mathematical situation must support every intervention.

## 7. Reward philosophy: mathematical fertility over rhetorical depth

The central danger is training a model to reproduce the language of deep mathematical explanation:

- "at heart this is about symmetry";
- "the quotient forgets irrelevant information";
- "the key invariant is...";
- "from this viewpoint the theorem is inevitable".

These phrases may be correct, but they can also become stylistic tokens detached from mathematical capability.

The reward should therefore be grounded as much as possible in **consequences**.

### Harder / more objective signals

Examples include:

- exact prediction on held-out cases;
- computationally verified counterexamples;
- correct classification of when a weakened assumption succeeds or fails;
- successful transfer to a held-out representation;
- solving new problems that become easier given the conceptualization;
- generation of a conjecture that survives systematic testing;
- later, successful formalization or proof;
- later, reduced search cost or improved proof success for a formal prover.

### Soft / AI-judged signals

AI feedback can still be useful for dimensions that are difficult to verify mechanically:

- whether a candidate is merely paraphrasing the source;
- whether two proposed perspectives are genuinely different;
- whether a construction appears natural rather than ad hoc;
- whether an analogy captures the important structural relationship;
- whether a conceptual account is clear enough to act on;
- whether a proof appears unified or case-driven.

These signals should remain explicitly different from mathematical correctness.

The long-term target is not to maximize a teacher's preference score. It is to make conceptual representations **survive intervention**.

## 8. Teacher models should bootstrap the search space, not define its ceiling

Frontier models such as ChatGPT/Codex can be used aggressively, but not as the final oracle of mathematical understanding.

Useful teacher roles include:

- generating multiple competing interpretations of the same situation;
- producing deliberately plausible but shallow explanations;
- finding analogies and cross-domain connections;
- proposing generalizations;
- generating adversarial examples and counterexamples;
- criticizing conceptualizations produced by the student;
- proposing hidden interventions that discriminate between two viewpoints;
- ranking naturalness or explanatory usefulness when no hard verifier exists.

The teacher should preferably generate **diversity**, not one canonical conceptual answer.

This allows the student to discover representations that the teacher did not propose. If such a representation produces better verified consequences, the environment should reward it even if an AI judge initially prefers a different explanation.

This is the main route by which Mathia can in principle exceed its synthetic-data teacher instead of remaining a pure distillation of that teacher.

## 9. Validate the signal before doing RL

Before spending significant compute on post-training, test whether the proposed notion of conceptual fertility is measurable at all.

For a hand-designed set of mathematical situations:

1. generate several candidate conceptualizations `C1 ... Cn`;
2. commit each conceptualization before revealing hidden tasks;
3. evaluate the same family of hidden interventions conditioned on each conceptualization;
4. compare downstream mathematical performance;
5. compare those results with human/AI judgments of elegance, depth, and naturalness.

Conceptually, measure quantities such as:

```text
P(hidden task succeeds | conceptualization Ci)
```

The important question is whether some conceptualizations reliably improve future mathematical work.

Possible outcomes:

### Positive signal

Structurally better representations produce measurable gains on held-out consequences, transfer, generalization, or simplification.

This supports using the signal for post-training.

### No discriminative signal

"Deep" and ordinary explanations perform similarly.

Then the environment is probably measuring prose or redundant context rather than understanding.

### Solver-only signal

The best conceptualizations are simply those that leak or encode the eventual solution procedure.

Then commitment, hidden-task construction, or controls need redesign.

This pre-RL study is a required scientific check, not optional polish.

## 10. Cold-start data

If the signal is promising, create a small synthetic cold-start corpus to teach the model what kind of activity is expected.

The cold start should expose behaviors such as:

- searching for invariants;
- identifying information that can be forgotten;
- comparing representations;
- looking for reversibility;
- questioning assumptions;
- proposing and testing generalizations;
- constructing bridges into other mathematical domains;
- finding counterexamples to its own explanation;
- preferring reusable mechanisms over theorem-by-theorem paraphrase.

The cold start should remain small enough that it does not become the de facto definition of mathematical understanding.

Its purpose is to establish the game and vocabulary, not to provide all of the desired reasoning traces.

## 11. Reinforcement learning hypothesis

The leading training hypothesis is then:

```text
base mathematical model
        |
        v
small conceptual cold start
        |
        v
RL in mathematical worlds
        |
        v
representations selected by their downstream fertility
```

The exact RL method is deliberately undecided. PPO, GRPO-style methods, preference optimization, rejection-based methods, or other approaches should not be selected until the environment and reward are shown to contain the desired signal.

The important distinction from ordinary math RL is the object being optimized.

Ordinary mathematical RL often approximates:

```text
problem -> reasoning trajectory -> correct answer
```

Mathia should investigate:

```text
mathematical situation
        -> conceptual representation
        -> unknown future intervention
        -> mathematical consequences
```

The model receives credit when its representation proves useful across those consequences.

## 12. Baselines and controls

A conceptual-training result is not meaningful unless compared against strong simpler explanations.

At minimum, preserve comparisons with:

### Base model

No Mathia-specific post-training.

### Ordinary solver post-training

Comparable mathematical data/compute used for conventional problem solving or answer-verifiable RL.

This is the most important adversarial baseline. It tests whether ordinary improved mathematical competence produces the same apparent conceptual abilities.

### Explanation SFT

Train on teacher-generated conceptual explanations without fertility-based RL.

This tests whether the benefit comes merely from exposure to conceptual prose.

### Conceptual-context ablation

Run hidden tasks without providing or requiring the committed conceptualization.

This tests whether the representation itself contributes information rather than simply measuring the same underlying model twice.

### Style controls

Include fluent but mathematically sterile conceptualizations and less elegant but operationally useful ones.

This helps detect reward for rhetoric.

Where practical, data quantity, compute, and mathematical source coverage should be matched well enough that differences can be attributed to the training objective rather than simply more mathematics.

## 13. What success should initially mean

The first target should **not** be state-of-the-art theorem proving or competition-math accuracy.

A successful first result would show something narrower and more diagnostic:

> A model can construct a conceptual representation before it knows the downstream question, and that representation causes measurable improvements on held-out mathematical interventions relative to strong controls.

Particularly valuable evidence would include:

- improved cross-representation transfer;
- correct assumption weakening on unseen variants;
- better counterexample discovery;
- generation of valid generalizations;
- selection of lower-complexity solution representations;
- useful composition of ideas from different mathematical domains;
- gains that cannot be explained by explanation style alone.

Failure is also informative. If the environment cannot distinguish these capabilities from ordinary solver competence, Mathia should revise the operational notion of understanding before scaling.

## 14. Relationship to qwen-lean

Mathia does **not** need to wait for qwen-lean.

Starting conceptual experiments first is scientifically valuable because it preserves the ability to compare different training histories.

Let a common ancestor be `M0`.

Later we may obtain:

```text
MC = M0 + conceptual post-training
MF = M0 + formal / Lean post-training
```

This creates empirical questions rather than architectural assumptions:

- Does formal training improve conceptual reasoning even before Mathia training?
- Does conceptual training improve later formal reasoning?
- Is `formal -> conceptual` better than `conceptual -> formal`?
- Does a joint model outperform two cooperating specialists?
- Can independent adapters or model deltas be combined without destructive interference?
- Does conceptual guidance improve qwen-lean proof success, search efficiency, lemma generation, or assumption selection?

Possible later combinations include:

```text
formal -> conceptual sequential post-training
conceptual -> formal sequential post-training
joint/mixed post-training
two independent communicating agents
adapter or model-weight merging
further joint RL after independent specialization
```

None is selected yet.

The important experimental constraint is to preserve checkpoints and training provenance so these comparisons remain possible.

## 15. Formal verification as reality, not as the conceptual language

When qwen-lean or Lean becomes available, formal mathematics can provide powerful downstream evidence:

```text
conceptual interpretation
        |
        v
proposed theorem / weakening / generalization
        |
        v
formalization and proof attempt
        |
        v
verified consequence, counterexample, or failure evidence
        |
        v
conceptual revision
```

The conceptual model should not be forced to think in Lean-native representations simply because Lean supplies verification.

A useful principle is:

> **Do not use formal mathematics to dictate how Mathia must think; use formal mathematics as one of the realities against which Mathia's ideas must survive.**

A failed proof attempt is not automatically evidence that a conjecture is false. Prover weakness, formalization errors, insufficient lemmas, and genuine counterexamples must remain distinguishable.

## 16. Simplicity and beauty as empirical hypotheses

The project should investigate whether mathematical aesthetics carry useful information rather than assuming they do.

For example, compare candidate representations or proofs that differ in:

- number of independent mechanisms;
- amount of case splitting;
- arbitrary choices;
- symmetry;
- minimality of assumptions;
- reuse across problems;
- ability to generate generalizations.

Then measure whether representations judged more elegant also produce better hidden-task performance.

A particularly interesting result would be evidence that what mathematicians call beauty correlates with **representational compression and downstream fertility**.

The opposite result would also matter: aesthetics may be only weakly related to machine-useful representation in some domains.

## 17. Suggested order of experiments

This is an experimental ordering, not a permanent phase structure.

### A. Hand-design one excellent mathematical world

Create a small number of high-quality situations around gcd / congruence / units / cyclic behavior, including visible material and hidden interventions.

### B. Establish a no-training baseline

Use existing capable models to generate multiple conceptualizations and test whether the hidden-task protocol actually discriminates among them.

### C. Refine the evaluator before scaling data

Attack the environment with shallow conceptual rhetoric, direct solving strategies, leakage, memorized theorem statements, and adversarial cases.

### D. Build a small cold-start corpus

Only after the evaluator shows a meaningful signal.

### E. Run the first conceptual post-training experiment

Compare conceptual SFT and fertility-based RL against base and ordinary-math-training baselines.

### F. Expand across representations and domains

Only if gains survive held-out tests. Natural next worlds include finite groups and linear algebra, especially kernel/image/quotient and change-of-basis phenomena.

### G. Introduce qwen-lean as an experimental variable

Compare formal-first, conceptual-first, model combination, and agent cooperation once the formal model is mature enough.

The order should be revised aggressively if early evidence invalidates an assumption.

## 18. Immediate artifacts worth building

Without committing to implementation details, the next useful repository artifacts are likely to be small and inspectable:

- a hand-written collection of mathematical situations for the first world;
- hidden intervention examples;
- exact computational graders where possible;
- prompts/protocols for producing a conceptual commitment before the test is revealed;
- candidate teacher prompts that generate diverse interpretations rather than canonical answers;
- a simple evaluation harness comparing conceptualizations on downstream tasks;
- concise evidence from the no-training baseline.

Large synthetic corpora and expensive RL runs should wait until these artifacts show a discriminative signal.

## 19. Open decisions

The following remain intentionally unresolved:

- base model and size;
- whether the first Mathia model shares the exact qwen-lean base checkpoint;
- RL algorithm;
- SFT/RL mixture;
- natural-language output format for conceptualizations;
- exact dataset schema;
- whether rewards should be combined into one scalar or sampled as separate environments;
- how much AI-judge feedback to use;
- how to quantify proof/solution simplification;
- when to introduce multi-domain composition tasks;
- whether beauty/naturalness deserves explicit reward;
- whether conceptual and formal specialists should ultimately be merged or remain agents;
- model-merging/adaptor strategy;
- formalization interface to qwen-lean / Lean.

These should be resolved when an experiment requires them, not in advance.

## 20. Research stopping / decision criteria

Before scaling Mathia substantially, we should be able to answer at least the following.

1. **Does the commitment-before-test protocol distinguish useful conceptual representations from fluent but sterile explanations?**
2. **Does conceptual training improve held-out mathematical behavior beyond matched ordinary solver training?**
3. **Can at least part of the reward come from consequences that do not depend on the same teacher that generated the conceptual data?**
4. **Can the trained model discover useful conceptualizations not present in the synthetic teacher corpus?**
5. **Do gains transfer across surface representations or mathematical domains?**

If several of these fail, scaling the corpus or RL budget would likely train style rather than the capability Mathia intends to study.

## 21. Current working plan in one sentence

> **First demonstrate that conceptual representations have measurable mathematical fertility under hidden interventions; then use small teacher-generated cold-start data and reinforcement learning to select representations by the correct predictions, transfers, generalizations, simplifications, and formal consequences they enable, while keeping qwen-lean as a later independent variable rather than a prerequisite.**

The research umbrella for this plan is GitHub issue #2. Individual execution issues should be opened only when a concrete experiment is specified tightly enough to implement and evaluate without silently settling the remaining research questions.
