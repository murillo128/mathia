# AGENTS.md

Instructions for ChatGPT, Codex, and other coding/research agents working in this repository.

## Mission

Mathia is an exploratory research repository for **semantic and conceptual mathematical reasoning in language models**.

The active question is whether a model can learn mathematical concepts and reusable conceptual moves well enough that useful strategic intuitions emerge and can later be selected by downstream mathematical fertility.

Do not turn exploratory discussion into a settled architecture, permanent ontology, dataset DSL, training algorithm, or multi-agent framework unless an explicit issue authorizes that transition.

## Current research line

The active first line is GitHub epic `#29`.

The previous `gold-set-v0` pre-RL line is retired before target-model inference. Its history remains in Git and closed issues/PRs, but its experiment code and active documentation are intentionally removed from the current tree.

For the semantic/execution reset rationale, read `docs/RESEARCH_RESET_SEMANTIC_INTUITION.md`.

For the current training hypothesis, read `docs/CONCEPTS_DIMENSIONS_INTUITION.md`.

Current critical path:

1. `#30` — scope and adversarially audit concepts, conceptual dimensions, the documented-theorem intuition task, and qwen-lean proof-search fertility measurement;
2. `#31` — build only the minimal pre-test/fertility harness required by the accepted #30 contract;
3. `#32` — freeze and run the exact Qwen-base + Codex-reference intuition pre-test against matched qwen-lean proof search.

Do not begin Mathia post-training merely because the concepts/dimensions/intuitions story is plausible. First validate that the proposed downstream fertility channel is informative.

## Load context progressively

For non-trivial work, start with:

1. `AGENTS.md`;
2. the controlling GitHub issue;
3. `docs/CONCEPTS_DIMENSIONS_INTUITION.md` when the task touches training, intuition, or qwen-lean fertility;
4. `docs/RESEARCH_RESET_SEMANTIC_INTUITION.md` when the task touches mathematical content or the execution boundary;
5. only the exact additional repository documents, source, tests, data, model state, or evidence needed for the active task.

`docs/CONCEPTUAL_MATH_DIRECTION.md` and `docs/WORKING_SYNTHESIS.md` preserve research motivation and current hypotheses. They are context, not implementation specifications.

Do not preload every repository document, every skill, complete prior issue/PR history, or retired experiment artifacts. On resume, verify branch, source revision, worktree/PR state, and new material issue discussion since the last handoff.

## Source-of-truth hierarchy

1. Tests, experiment outputs, formal checks, and captured evidence establish observed behavior.
2. Explicit accepted specifications/decision documents establish only their declared scope.
3. The controlling GitHub issue establishes the bounded execution contract for its task.
4. Pull requests, checks, reviews, and Git history preserve implementation and evidence.
5. Exploratory research notes preserve hypotheses and motivation but do not silently become requirements.
6. Chat discussion is provisional until intentionally recorded in the repository or issues.

When sources materially conflict, document the conflict rather than silently choosing one.

## Active semantic/execution invariants

These rules apply to the current `#29` research line unless its controlling issue explicitly records a later evidence-based revision.

### Separate meaning from execution

Primary Mathia tasks should test what an operation, relation, transformation, or representation means, what it preserves or forgets, and what structural expectations follow.

Do not make arithmetic execution a hidden prerequisite.

A task is suspect if its intended solution materially depends on evaluating concrete arithmetic, running an arithmetic algorithm, enumerating a numerical domain, or reconstructing concrete numerical state.

### Generic model-visible mathematics

Primary Mathia-visible mathematical content should use generic objects, operations, relations, and structural roles rather than concrete numeral instances.

Do not satisfy this requirement superficially by replacing a numeral with a variable while preserving the same execution demand.

The relevant test is semantic:

> Could a model that understands the mathematical structure but cannot evaluate concrete arithmetic still perform the intended conceptual task?

### Private instantiation is allowed

Concrete instances may be used behind the model-visible boundary by:

- dataset generators;
- falsifiers;
- exhaustive computation;
- Python checks;
- qwen-lean;
- Lean or other formal systems;
- private truth/scoring code.

They must not leak into Mathia-visible primary content or become the conceptual shortcut the benchmark rewards.

### Genericity should be challenged

Where relevant, test whether the intended reasoning survives:

- alpha-renaming of objects/operations;
- notation changes;
- alternative representations;
- structurally equivalent realizations.

Surface robustness alone is not evidence of mathematical understanding, but failure under trivial renaming is strong evidence of a bad benchmark.

## Concepts, conceptual dimensions, and intuition

Keep these roles separate when designing data or evaluation.

### Concepts

Concepts are mathematical semantic objects and relationships: composition, inverse, quotienting, invariance, reversibility, decomposition, factorization, and similar constructions.

Prefer multiple viewpoints and relations over dictionary definitions.

### Conceptual dimensions / moves

These are reusable actions over mathematical representations, including structural similarity/transfer, decomposition, synthesis, abstraction/compression, generalization, counterfactual reasoning, simplification, bridge construction, reframing, multiple perspectives, perspective selection, naturalness/canonicality, and prediction/falsification.

Do not confuse being able to name a move with being able to perform it.

### Intuition

Treat a candidate intuition as a provisional strategic hypothesis about how to see a theorem or problem and where a useful proof route, lemma, representation, or obstruction may come from.

Do not assume intuition must be taught directly. The active hypothesis is that it may emerge from concepts plus conceptual moves and can be bootstrapped by teacher distillation.

## Teacher/distillation discipline

Codex or another strong frontier model may be used to:

- scope intuition examples on documented theorems;
- generate competing strategic interpretations;
- critique shallow or proof-like outputs;
- identify missing conceptual dimensions;
- provide a strong reference condition for the qwen-lean measurement channel.

This is teacher-generated evidence and, when used for training, **distillation**.

Do not report similarity to the teacher as independent mathematical validation. If teacher similarity improves while downstream proof-search utility does not, treat explanation-style imitation as a live alternative hypothesis.

## Intuition-fertility discipline

The current stronger signal is downstream effect on a separate formal worker.

For theorem `T` and intuition `I`:

- freeze `I` before proof search;
- compare qwen-lean under matched proof-search budgets with and without `I`;
- verify resulting proofs with Lean/the formal environment;
- preserve exact theorem, solver checkpoint, prompt/interface, budget, seeds, and provenance.

Useful controls include no intuition, shuffled intuition, base-Qwen intuition, Mathia intuition, and Codex intuition.

A failed qwen-lean proof search does not prove that `I` or `T` is false.

## Main confounds to attack

### Proof leakage

If an intuition contains most of the proof, uplift may reflect answer transmission rather than conceptual compression. The intuition interface should leave meaningful formal work to the prover.

### Solver-specific prompt optimization

A reward tied to one qwen-lean checkpoint may select text that exploits that checkpoint rather than generally useful mathematics. Preserve provenance and later test transfer across presentation, prompting, checkpoint, or solver where practical.

### Pretraining familiarity

Famous theorems are acceptable for internal channel calibration, but success on them is weak evidence of novel mathematical discovery. Report that limitation explicitly.

### Formal-worker bottleneck

If even a strong Codex intuition does not help qwen-lean, do not conclude that intuition is useless. Reconsider the interface, proof-search budget, theorem panel, or formal-worker capacity.

## Research discipline

Always distinguish:

- concept knowledge;
- conceptual-move ability;
- candidate intuition;
- teacher-generated or distilled interpretation;
- observed experimental evidence;
- accepted experimental constraint;
- computational evidence;
- formalization success;
- verified proof/refutation;
- proof-search failure;
- downstream research usefulness.

Do not collapse these signals.

In particular:

- formalization success does not imply proof;
- proof-search failure does not imply falsehood;
- a compiling formal statement may still misrepresent the intended informal claim;
- conceptual prose is not evidence of conceptual ability;
- teacher similarity is not mathematical truth;
- qwen-lean uplift is solver-conditional evidence until transfer is tested;
- a model's pretraining arithmetic knowledge cannot be assumed absent simply because the benchmark avoids arithmetic.

## Benchmark and experiment discipline

For material experiments, retain enough information to understand and compare what was run, including model/tokenizer, theorem/benchmark identity, qwen-lean checkpoint, source revisions, generation configuration, proof-search budget, evaluation method, and important limitations.

Freeze benchmark semantics and the primary analysis before protected target-model results when the controlling issue requires a frozen evaluation.

Do not tune a protected target against item-level model failures and then report it as held out.

When an experiment is superseded before execution, retire it explicitly rather than mutating it into a new hypothesis while preserving the old name.

## AI feedback and dataset generation

AI feedback can be useful for:

- generating competing intuitions;
- identifying superficial paraphrases;
- proposing adversarial interpretations;
- checking whether two representations are meaningfully different;
- ranking naturalness or diversity when no hard signal exists;
- constructing initial teacher/distillation corpora.

Keep AI feedback separate from exact correctness. Prefer to train/select ideas by what they enable on later tasks or checks when a credible behavioral signal exists.

When generating corpora, preserve enough source context and metadata to inspect faithfulness, licensing, contamination, and whether the data teaches mathematical capability rather than explanation style.

## Formal systems

Lean and qwen-lean may provide exact downstream feedback, but they should not dictate Mathia's conceptual language.

Use formal mathematics as a reality-checking and proof-search layer while keeping conceptual interpretation, formalization success, proof success, and solver failure distinct.

## Model and compute discipline

The first local diagnostic preserves the exact Qwen base ancestor already shared with qwen-lean for controlled comparison. The exact qwen-lean checkpoint used in #32 must be resolved and frozen from the related repository/runtime at execution time.

The shared Ada GPU remains a gated resource.

Do not increase model size or hardware merely because a small experiment is difficult. First distinguish:

- benchmark/design failure;
- intuition-interface failure;
- conceptual-model capacity bottleneck;
- formal-specialist bottleneck;
- coordination bottleneck;
- throughput-only bottleneck.

Scaling is appropriate when evidence identifies a capacity/throughput limit rather than a flawed task or reward channel.

## Role routing

Load repository skills lazily by role:

- design authority: `.agents/skills/design-github-issue/SKILL.md`;
- main executor: `.agents/skills/spec-driven-codex-loop/SKILL.md`;
- recurring mathematical research watch: `.agents/skills/mathia-research-watch/SKILL.md`;
- shared finding-review protocol for research owners and adversaries: `.agents/skills/mathia-research-review/SKILL.md`;
- recurring adversarial research watch: `.agents/skills/mathia-research-adversarial/SKILL.md`;
- recurring research mind synthesizer: `.agents/skills/mathia-research-mind/SKILL.md`;
- recurring research graph curator watch: `.agents/skills/mathia-research-graph-curator/SKILL.md`;
- recurring program-level master researcher: `.agents/skills/mathia-master-researcher/SKILL.md`;
- Git/GitHub mutation and publication: `.agents/skills/codex-github-operations/SKILL.md`;
- independent checkpoint/final review: `.agents/skills/codex-independent-review/SKILL.md`.

`AGENTS.md` owns repository-wide invariants and routing. Skills own reusable procedure. Issues own task-specific scope, commands, gates, and acceptance criteria. Avoid duplicating the same detailed procedure across all three.

## Artifact discipline

Large model weights, checkpoints, datasets, caches, and bulky logs belong outside Git.

Commit code, prompts/configuration, small fixtures, compact examples, audit notes, and concise evidence that helps inspection.

Never commit secrets, credentials, private data, or artifacts without redistribution rights.

## Git behavior

- Use feature branches for non-trivial work unless the user explicitly requests a direct default-branch change.
- Scheduled mathematical research watches routed through `.agents/skills/mathia-research-watch/SKILL.md`, scheduled adversarial research watches routed through `.agents/skills/mathia-research-adversarial/SKILL.md`, scheduled research-mind synthesis routed through `.agents/skills/mathia-research-mind/SKILL.md`, scheduled graph-curator watches routed through `.agents/skills/mathia-research-graph-curator/SKILL.md`, and scheduled Master Researcher passes routed through `.agents/skills/mathia-master-researcher/SKILL.md` are explicit exceptions: they may commit only changes inside their respective skill-owned paths directly to the default branch when all path and publication gates pass.
- Avoid unrelated formatting or cleanup.
- Commit messages should describe one intentional outcome.
- Executor workflows end at a ready-for-review pull request and handoff.
- Executors must not merge or enable auto-merge on their own authority.
- Merge requires explicit user authorization after review; CI success or independent-review `PASS` alone is not merge authorization.
- Never force-push or rewrite shared history without explicit user approval.

## Current scope

The repository has an explicit active research epic because the user requested one. That planning structure is limited to the current experiment and should not be extrapolated into a permanent Mathia roadmap.

The current scientific priority is **validate the causal fertility instrument before implementation-heavy post-training work**.
