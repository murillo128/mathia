# AGENTS.md

Instructions for ChatGPT, Codex, and other coding/research agents working in this repository.

## Mission

Mathia is an exploratory research repository for **semantic and conceptual mathematical reasoning in language models**.

The active question is whether a model can learn and use mathematical meaning, representations, structural mechanisms, and fertile intuitions at a level distinct from arithmetic execution and formal theorem proving.

Do not turn exploratory discussion into a settled architecture, permanent ontology, dataset DSL, training algorithm, or multi-agent framework unless an explicit issue authorizes that transition.

## Current research reset

The active first line is GitHub epic `#29`.

The previous `gold-set-v0` pre-RL line is retired before target-model inference. Its history remains in Git and closed issues/PRs, but its experiment code and active documentation are intentionally removed from the current tree.

For the rationale, read `docs/RESEARCH_RESET_SEMANTIC_INTUITION.md`.

Current critical path:

1. `#30` — design and adversarially audit a computation-free semantic-intuition benchmark;
2. `#31` — build minimal benchmark-specific plumbing only after `#30` accepts one exact semantic contract;
3. `#32` — freeze, run, and interpret the first local base-model diagnostic.

Do not revive the retired experiment merely because code exists in Git history.

## Load context progressively

For non-trivial work, start with:

1. `AGENTS.md`;
2. the controlling GitHub issue;
3. `docs/RESEARCH_RESET_SEMANTIC_INTUITION.md` when the task touches mathematical content, benchmark design, training, or evaluation;
4. only the exact additional repository documents, source, tests, data, model state, or evidence needed for the active task.

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

## Active semantic-intuition invariants

These rules apply to the current `#29` research line unless its controlling issue explicitly records a later evidence-based revision.

### Separate meaning from execution

Primary Mathia tasks should test what an operation, relation, transformation, or representation **means**, what it preserves or forgets, and what structural expectations follow.

Do not make arithmetic execution a hidden prerequisite.

A task is suspect if its intended solution materially depends on evaluating concrete arithmetic, running an arithmetic algorithm, enumerating a numerical domain, or reconstructing concrete numerical state.

### Generic model-visible mathematics

Primary Mathia-visible mathematical content should use generic objects, operations, relations, and structural roles rather than concrete numeral instances.

Do not satisfy this requirement superficially by replacing a numeral with a variable while preserving the same execution demand.

The relevant test is semantic:

> Could a model that understands the mathematical structure but cannot evaluate concrete arithmetic still solve the task perfectly?

### Private instantiation is allowed

Concrete instances may be used behind the model-visible boundary by:

- dataset generators;
- falsifiers;
- exhaustive computation;
- Python checks;
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

## Operational intuition discipline

Treat a candidate mathematical intuition as a **mechanism hypothesis with consequences**, not as a style of explanation.

Prefer intuitions that support falsifiable expectations such as:

- invariance;
- reversibility or information loss;
- factorization through a representation;
- assumption weakening;
- transfer across representations;
- a predicted failure mode;
- a generalization;
- a discriminating counterfactual.

AI judgment may help assess diversity, naturalness, or whether prose is sterile, but it must not be reported as mathematical truth.

## Research discipline

Always distinguish:

- hypothesis or intuition;
- synthetic/AI-generated interpretation;
- observed experimental evidence;
- accepted experimental constraint;
- computational evidence;
- formalization success;
- verified proof/refutation;
- downstream research usefulness.

Do not collapse these signals.

In particular:

- formalization success does not imply proof;
- proof-search failure does not imply falsehood;
- a compiling formal statement may still misrepresent the intended informal claim;
- conceptual prose is not evidence of conceptual ability;
- a model's pretraining arithmetic knowledge cannot be assumed absent simply because the benchmark avoids arithmetic.

## Benchmark and experiment discipline

For material experiments, retain enough information to understand and compare what was run, including model/tokenizer, source revision, benchmark identity, generation configuration, evaluation method, and important limitations.

Freeze benchmark semantics and the primary analysis before target-model results when the controlling issue requires a frozen evaluation.

Do not tune a protected target against item-level model failures and then report it as held out.

When an experiment is superseded before execution, retire it explicitly rather than mutating it into a new hypothesis while preserving the old name.

## AI feedback and dataset generation

AI feedback can be useful for:

- generating competing intuitions;
- identifying superficial paraphrases;
- proposing adversarial interpretations;
- checking whether two representations are meaningfully different;
- suggesting hidden interventions;
- ranking naturalness or fertility when no hard signal exists.

Keep AI feedback separate from exact correctness. Prefer to train/select ideas by what they enable on later tasks or checks rather than by teacher preference alone.

When generating corpora, preserve enough source context and metadata to inspect faithfulness, licensing, contamination, and whether the data teaches mathematical capability rather than explanation style.

## Formal systems

Lean and other formal systems may later provide exact downstream feedback.

Do not let the availability of Lean prematurely force Mathia to represent concepts in Lean-native syntax.

Use formal mathematics as a reality-checking layer when useful, while keeping conceptual interpretation, formalization success, and proof success distinct.

## Model and compute discipline

The first local diagnostic currently preserves the exact Qwen base ancestor shared with qwen-lean for controlled comparison. The shared Ada GPU remains a gated resource.

Do not increase model size or hardware merely because a small experiment is difficult. First distinguish:

- benchmark/design failure;
- conceptual-model capacity bottleneck;
- formal-specialist bottleneck;
- coordination bottleneck;
- throughput-only bottleneck.

Scaling is appropriate when evidence identifies a capacity/throughput limit rather than a flawed task.

## Role routing

Load repository skills lazily by role:

- design authority: `.agents/skills/design-github-issue/SKILL.md`;
- main executor: `.agents/skills/spec-driven-codex-loop/SKILL.md`;
- Git/GitHub mutation and publication: `.agents/skills/codex-github-operations/SKILL.md`;
- independent checkpoint/final review: `.agents/skills/codex-independent-review/SKILL.md`.

`AGENTS.md` owns repository-wide invariants and routing. Skills own reusable procedure. Issues own task-specific scope, commands, gates, and acceptance criteria. Avoid duplicating the same detailed procedure across all three.

## Artifact discipline

Large model weights, checkpoints, datasets, caches, and bulky logs belong outside Git.

Commit code, prompts/configuration, small fixtures, compact examples, audit notes, and concise evidence that helps inspection.

Never commit secrets, credentials, private data, or artifacts without redistribution rights.

## Git behavior

- Use feature branches for non-trivial work unless the user explicitly requests a direct default-branch change.
- Avoid unrelated formatting or cleanup.
- Commit messages should describe one intentional outcome.
- Executor workflows end at a ready-for-review pull request and handoff.
- Executors must not merge or enable auto-merge on their own authority.
- Merge requires explicit user authorization after review; CI success or independent-review `PASS` alone is not merge authorization.
- Never force-push or rewrite shared history without explicit user approval.

## Current scope

The repository now has an explicit active research epic because the user requested one. That planning structure is limited to the current semantic-intuition experiment and should not be extrapolated into a permanent Mathia roadmap.

The current scientific priority is **benchmark validity before implementation, implementation before GPU inference, and evidence before post-training**.
