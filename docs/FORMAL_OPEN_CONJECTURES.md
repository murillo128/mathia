# Formal open conjectures as a validation substrate

## Status

This note records an **exploratory research opportunity**, not a selected benchmark, implementation plan, training phase, or commitment to make Lean the internal representation of Mathia.

The observation is that there now exists a substantial corpus of genuinely open mathematical problems whose **statements have already been formalized in Lean 4**. This creates an unusual interface between conceptual mathematical reasoning and exact machine verification: Mathia can reason above the formal layer while Lean can later check sharply defined formal claims produced along the way.

The most relevant existing resource is Google DeepMind's [`formal-conjectures`](https://github.com/google-deepmind/formal-conjectures) project, a collection of formalized conjecture statements built on Mathlib. Its public site currently contains more than two thousand statements, including more than one thousand tagged as research-open, and the corpus is explicitly designed to evolve as conjectures are added, corrected, solved, or formally proved.

## What Lean verification does and does not give us

A Lean file containing a conjecture statement gives a stronger target than an informal natural-language problem, but "verified in Lean" needs to be decomposed carefully.

If Lean elaborates and type-checks a statement, then:

- all referenced definitions and quantified objects have precise formal meanings;
- the proposition is well-formed in Lean's logic under the imported environment;
- later proof terms for that proposition can be checked by the Lean kernel;
- candidate lemmas, equivalences, reductions, counterexamples, or special cases can also be made exact and kernel-checked once formalized.

It does **not** imply that:

- the conjecture has been proved;
- the formal statement is guaranteed to capture every nuance of the intended informal conjecture;
- the definitions chosen are the only or most conceptually useful representation of the mathematics;
- a model has demonstrated conceptual understanding merely because it emits Lean that type-checks.

Open-conjecture files typically contain an unfilled proof obligation represented during development by `sorry` or an equivalent placeholder mechanism. The proposition is therefore a precise target, not a theorem whose truth Lean has established.

The upstream `formal-conjectures` project explicitly warns about possible **misformalization**: a statement can be perfectly legal Lean while subtly failing to express the intended mathematics. Its maintainers use human review and plan automated checks to reduce that risk. Mathia should therefore keep at least four signals distinct:

1. **informal mathematical fidelity** — does the formal statement represent the intended problem?;
2. **conceptual fertility** — did the model produce useful mathematical ideas, representations, analogies, invariants, or conjectures?;
3. **formalization success** — can a proposed claim be expressed correctly in Lean?;
4. **proof success** — does Lean verify a proof of that claim without `sorry` or unapproved assumptions?

Collapsing these into one score would make it easy to mistake formal fluency for mathematical capability.

## Why this is interesting for Mathia

Most mathematical benchmarks ask for a final answer to a problem known to be solvable. Formal open conjectures offer a different regime: the top-level problem is deliberately beyond the known frontier, so success cannot normally mean "solve the item".

That makes them potentially useful for probing whether a conceptual model can produce **mathematical progress-shaped behavior** rather than only polished explanations.

Possible observable outputs include:

- discovering or proposing invariants;
- finding alternative representations of the same conjecture;
- generating nontrivial equivalent formulations;
- identifying assumptions that can be weakened or strengthened;
- deriving formally checkable special cases;
- producing reductions to better-understood subproblems;
- generating intermediate lemmas whose truth can be checked;
- constructing counterexamples to over-strong variants;
- connecting a conjecture to a theorem or structure from another domain;
- generating new auxiliary conjectures that are both nontrivial and empirically or formally testable.

This is closer to the capability Mathia is trying to investigate than asking whether a model can imitate the prose style of a conceptual mathematician.

At the same time, a model could generate large numbers of trivial true lemmas, verbose reformulations, or vacuous consequences and score well under a naive verifier-only metric. Formal validity therefore cannot by itself be the reward or evaluation criterion for conceptual progress.

## Representative candidate problems

A first exploratory sample could favor problems whose informal statements are simple even when their solutions are deep. Examples already represented in Lean/Mathlib ecosystems include:

| Problem family | Why it is conceptually interesting |
|---|---|
| Collatz | Very small definition with rich dynamical behavior; invites invariants, stopping-time structure, parity encodings, and alternative representations. |
| Goldbach | Simple additive statement with many natural changes of representation: residues, density, additive structure, computational evidence, and reductions. |
| Legendre's conjecture | Connects an elementary interval statement to prime gaps and several levels of number-theoretic machinery. |
| Twin primes | Simple infinitude statement that exposes the gap between local heuristics, sieve structure, and global proof. |
| Selected Erdős problems | Large and diverse source of combinatorial and number-theoretic problems, including many statements whose conceptual core is much simpler than their technical frontier. |
| Riemann hypothesis | Useful as a ceiling/reference example with substantial Mathlib infrastructure, but probably a poor first probe because almost any useful partial progress requires heavy surrounding theory. |

The selection criterion should not simply be fame or difficulty. For Mathia, a better candidate may be a problem with a compact conceptual core, several meaningful representations, accessible finite experiments, and many potentially useful intermediate claims.

## A possible evaluation role: verified partial progress

The strongest opportunity may be to use the formal statement as an **anchor** while evaluating intermediate mathematical work rather than demanding a complete proof.

For example, suppose the target is Collatz. A model might propose that a certain encoding exposes a monotone quantity on a restricted family of trajectories. That proposal can be examined at multiple levels:

- Is the encoding mathematically meaningful or merely a relabeling?
- Does it expose a reusable relationship or invariant?
- Is the proposed restricted claim actually true?
- Can the claim be formalized without distorting its content?
- Can Lean prove it from existing definitions and previous verified lemmas?
- Does it make later reasoning easier, shorten a proof search, or connect previously separate facts?

This produces a richer signal than `proof succeeded / proof failed`. It also creates a natural adversarial test for Mathia's central hypothesis: if conceptual training only teaches an explanatory style, it should not systematically increase the rate of **novel, nontrivial, formally valid intermediate progress** on unseen conjectures.

## Important benchmark hygiene

`formal-conjectures` is not automatically a clean held-out benchmark for Mathia.

### Public and famous problems are contamination-prone

Many conjectures, attempted proofs, standard reductions, and explanatory texts are likely present in base-model pretraining. Famous problems such as Riemann, Goldbach, Collatz, and twin primes are especially unsuitable as evidence of novelty if evaluated only by natural-language similarity to known ideas.

Less famous problems and recently added conjectures may provide stronger probes, but contamination still needs to be treated as an empirical risk rather than assumed absent.

### The corpus is dynamic

Statements can move from open to solved, be corrected, or receive formal proofs. `formal-conjectures` therefore provides immutable benchmark tags in addition to its evolving main branch.

Any serious evaluation should pin:

- the exact repository benchmark/version tag;
- the Lean and Mathlib versions;
- the set of problems and their category at selection time;
- any auxiliary definitions added outside Mathlib;
- the informal source used to judge semantic fidelity.

The live number of open statements should not be treated as a stable dataset identifier.

### Formal success must reject loopholes

A proof-like artifact should not count as success merely because a file compiles. Evaluation must detect or prohibit at least:

- `sorry` / admitted goals;
- new axioms introduced to assume the target;
- equivalent trust escapes or unsafe shortcuts;
- accidental weakening or alteration of the target statement;
- circular dependencies on a theorem equivalent to the conjecture when those dependencies are not part of the allowed environment.

The exact policy can be chosen later; the methodological point is simply that **kernel acceptance under a controlled environment** is the relevant formal signal.

## Relationship to external benchmark validation

This resource should not replace the external validation strategy in [`EVALUATION_METHODOLOGY.md`](./EVALUATION_METHODOLOGY.md).

Standard external suites answer questions such as: did Mathia improve at independently designed mathematical tasks relative to its base model and stronger contemporary models?

Open formal conjectures could answer a different question:

> When the final answer is not known and cannot be trained toward, does the model produce more useful, falsifiable, and formally checkable mathematical intermediate structure?

Those two kinds of evidence are complementary. A model that improves only on formal open-conjecture artifacts might simply have learned Lean or theorem-proving tactics. A model that improves only on conceptual-language judgments might simply have learned a style. The interesting result would be a pattern of transfer across conceptual interventions, ordinary external tasks, and formally checkable mathematical progress.

## Research hypotheses worth testing later

These are hypotheses, not decisions:

- **H1 — conceptual fertility:** conceptual post-training increases the rate of nontrivial verified intermediate claims on open conjectures relative to the exact base model.
- **H2 — representation transfer:** gains are strongest when useful progress requires changing representation rather than extending an obvious symbolic derivation.
- **H3 — verifier complementarity:** Lean is most valuable as a downstream falsifier/checker of conceptual outputs, not as the representation that must generate those outputs.
- **H4 — anti-style test:** if gains disappear when conceptual prose is hidden and only generated mathematical artifacts are scored, the intervention may mainly teach explanation style.
- **H5 — AI-feedback utility:** AI judges may help rank fertility, relevance, simplicity, or novelty, but their judgments become substantially more useful when paired with exact formal or computational checks of the claims they are judging.
- **H6 — theorem proving is not enough:** a theorem-proving-specialized baseline may produce more completed Lean proofs on tractable subgoals while producing fewer useful reframings or conjectures; that contrast would help separate conceptual reasoning from prover fluency.

## Open questions

Before treating this as an experiment rather than an opportunity, several questions remain deliberately unsettled:

- What counts as "nontrivial progress" on an unsolved target?
- Can usefulness be measured without rewarding verbosity or large numbers of easy lemmas?
- How should novelty be distinguished from retrieval of known literature?
- Should candidate subclaims be generated in natural language first, Lean first, or through multiple representations?
- How much human mathematical review is needed to validate semantic importance after formal verification?
- Can AI feedback reliably identify fertile intermediate claims when given both the informal context and formal verification results?
- Are less famous Erdős-style problems better probes than canonical famous conjectures because memorized narratives are weaker?
- Could formally verified negative results — failed conjectured lemmas, counterexamples, impossible generalizations — be as informative as successful lemmas?
- Does a conceptual intervention improve downstream theorem proving because it selects better intermediate goals, even if it does not directly improve tactic generation?

These questions are closely aligned with Mathia's broader aim: determine whether a model can acquire mathematical behavior that is structurally useful, transferable, and falsifiable, rather than merely producing mathematically styled language.

## References

- Google DeepMind, [`formal-conjectures`](https://github.com/google-deepmind/formal-conjectures): evolving Lean 4 / Mathlib corpus of formalized conjecture statements.
- [`formal-conjectures` browser and statistics](https://google-deepmind.github.io/formal-conjectures/): current categories, sources, subjects, and statement status.
- Firsching et al. (2026), *Formal Conjectures: An Open and Evolving Benchmark for Verified Discovery in Mathematics*, linked from the upstream repository.
- Mathlib documentation for formalized mathematical infrastructure and selected named conjectures.
