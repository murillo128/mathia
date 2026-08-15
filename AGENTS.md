# AGENTS.md

Instructions for ChatGPT, Codex, and other coding agents working in this repository.

## Mission

Mathia is an exploratory research repository for conceptual mathematical reasoning in language models. The current research direction is intentionally broad: investigate whether models can learn and use compact mathematical concepts, relationships, viewpoints, abstractions, analogies, generalizations, and conjectures at a level above formal theorem proving.

Do not turn exploratory discussion into a roadmap, phase structure, settled architecture, or durable technical decision unless the user explicitly asks for that transition.

## Load context progressively

For non-trivial work, start with:

1. `AGENTS.md`;
2. the controlling GitHub issue, when one exists;
3. only the exact repository documents, source, tests, data, model state, or evidence needed for the active task.

`docs/CONCEPTUAL_MATH_DIRECTION.md` preserves research motivation and hypotheses. It is context, not an implementation specification or accepted architecture.

Do not preload every repository document, every skill, complete prior issue/PR history, or large result directories. On resume, verify branch, `HEAD`, worktree state, and new material issue/PR discussion since the last handoff.

## Source-of-truth hierarchy

1. Tests, experiment outputs, and captured evidence establish observed behavior.
2. Explicit repository specifications or accepted decision documents, if introduced later, establish their declared scope.
3. A controlling GitHub issue establishes the bounded execution contract for its task.
4. Pull requests, checks, reviews, experiment outputs, and Git history preserve implementation and evidence.
5. Exploratory research notes preserve hypotheses and motivation but do not silently become requirements.
6. Chat discussion is provisional until intentionally recorded in an authoritative source.

When sources materially conflict, stop and document the conflict rather than silently choosing one.

## Role routing

Load skills lazily by role:

- design authority: `.agents/skills/design-github-issue/SKILL.md`;
- main executor: `.agents/skills/spec-driven-codex-loop/SKILL.md`;
- Git/GitHub mutation and publication: `.agents/skills/codex-github-operations/SKILL.md`;
- independent checkpoint/final review: `.agents/skills/codex-independent-review/SKILL.md`.

`AGENTS.md` owns repository-wide invariants and routing. Skills own reusable procedure. Issues own task-specific scope, commands, gates, and acceptance criteria. Avoid duplicating the same rule across all three.

## Research discipline

Mathia is exploratory. Agents must distinguish clearly between:

- hypothesis or intuition;
- synthetic/AI-generated interpretation;
- observed experimental evidence;
- accepted technical decision;
- formal or externally verified result.

Do not present AI-judged conceptual quality as mathematical truth. If formal systems such as Lean are later used, keep conceptual judgment, formalization success, proof success, and empirical task quality as separate signals.

Do not silently choose a model, dataset, conceptual representation, teacher/judge strategy, training method, evaluation protocol, or formal backend when the task has not settled that choice.

When generating mathematical corpora, preserve enough source context and metadata to inspect whether outputs are faithful, useful, licensed for the intended use, and contaminated with evaluation material.

## Experiment and artifact discipline

For material experiments, retain enough information to understand and compare what was run, normally including the model/tokenizer, dataset or source material, relevant generation/training configuration, evaluation method, and important limitations.

Large model weights, checkpoints, datasets, caches, and bulky logs belong outside Git. Commit code, prompts/configuration, small fixtures, compact examples, and concise evidence that helps inspection.

Never commit secrets, credentials, private data, or artifacts without redistribution rights.

## External dependencies

Respect licensing, attribution, privacy, and contribution rules for mathematical texts, datasets, models, formal libraries, and external repositories. Internal repository authorization does not override upstream terms.

Never force-push or rewrite shared history without explicit user approval.

## Git behavior

- Use feature branches for non-trivial work unless the user explicitly asks for a direct default-branch commit.
- Avoid unrelated formatting or cleanup.
- Commit messages should describe one intentional outcome.
- Codex/executor implementation workflows end at a **ready-for-review** pull request and handoff.
- Codex/executor must not merge or enable auto-merge on its own authority.
- Merge requires an explicit later user instruction after user/ChatGPT review; CI success, acceptance criteria, or independent-review `PASS` alone are not merge authorization.

## Current scope

There is intentionally no repository roadmap, phase plan, epic, or decision log yet. Do not create one merely to make the repository look complete. Introduce planning structure only when explicitly requested in a later project-design session.
