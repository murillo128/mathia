---
name: mathia-formalization-design
description: Design a Mathia-owned Lean formalization issue with a blocking statement/adversarial/prior-art/mathlib-reuse gate and structured handoff of mathematical discoveries back into Mathia research.
---

# Mathia Lean Formalization Design

## Responsibility

Use this skill when Mathia wants to test, sharpen, falsify, or machine-check a mathematical claim in Lean.

This is a thin specialization of the canonical merged repository skill:

```text
.agents/skills/design-github-issue/SKILL.md
```

Load that file from the current Mathia repository as the generic issue-design authority. Do not use a PR, feature branch, historical copy, or external duplicate of the skill as procedure authority unless a controlling issue explicitly pins historical workflow behavior for reproducibility.

The **task represented by the controlling Mathia issue** owns the scientific question. Codex, Lean, and the independent reviewer are actors inside that task.

## Repository boundary

For Mathia formalization work:

- the controlling issue lives in this Mathia repository;
- Lean source and formalization evidence are developed on a Mathia feature branch;
- the implementation PR targets Mathia;
- mathematical discoveries flow back through the controlling Mathia issue.

Do not move scientific ownership or proof execution to another repository merely because another project already has a Lean environment.

The issue chooses the smallest sensible Mathia-local path for the formal artifact. Do not freeze a permanent repository layout or formalization framework from this skill alone.

## Lean environment

Use the canonical pinned Lean/mathlib environment in Mathia when one exists.

If Mathia does not yet contain a Lean project, the first formalization issue that requires one may authorize the **smallest pinned local Lean setup** needed for reproducible work, for example the minimal `lean-toolchain` / Lake configuration and imports needed by the bounded target.

That setup must:

- live in Mathia;
- pin the material Lean/mathlib revision;
- avoid importing another repository's project structure as an implicit dependency;
- remain proportionate to the current formalization rather than becoming a general framework by default.

If creating or materially changing the Lean environment is not authorized by the controlling issue, return to design rather than improvising it during proof work.

## Formalization Gate 0

Every nontrivial formalization issue must begin with a blocking **statement / adversarial / prior-art / mathlib-reuse gate** before proof implementation.

Design Gate 0 to reconstruct the intended claim independently, including as relevant:

- exact quantifiers and theorem surface;
- domains, side conditions, singularities, and definedness;
- normalization, sign, indexing, orientation, gauge, and convention choices;
- boundary and degenerate cases;
- the relation between informal notation and the proposed Lean object;
- whether the Lean target is weaker, stronger, or equivalent to the persisted claim;
- which surrounding consequences remain outside the formal theorem.

The gate must actively try to falsify the proposed statement rather than merely translate notation.

Also require when material:

- search for exact or stronger prior mathematical/formal results;
- search current mathlib and existing Mathia Lean code for reusable declarations;
- an explicit dependency/import decision before rebuilding generic infrastructure;
- exact Lean/mathlib pins used by the proof target.

Allowed gate outcomes should include, with task-specific names if useful:

- safe progression to proof;
- reuse-only / already formalized / no material delta;
- statement repair required;
- mathematical conflict or counterevidence.

A negative gate result is a successful scientific outcome when it prevents proving the wrong statement.

## Formal success boundary

The issue must state what a successful Lean theorem establishes and what it does not.

Keep separate:

- fidelity of the Lean statement to the intended mathematics;
- success of the Lean proof;
- validity of wider Mathia findings or research programs;
- novelty or prior-art status;
- analytic, geometric, asymptotic, computational, or representation bridges excluded from the formal theorem.

A compiling theorem must never silently certify surrounding prose that was not formalized.

## Research-handoff contract

Every formalization issue must require Codex to report material mathematical discoveries to the **controlling Mathia issue**.

The executor does not directly create Mathia adversarial sidecars, clues, or replacement findings as part of Lean execution. The issue comment is transport to the issue-owning review/orchestration session.

A material handoff should contain:

- the exact mathematical observation;
- whether it threatens/corrects the target or is independent of it;
- exact evidence: derivation, counterexample, Lean theorem/check, file/commit, or failed statement;
- the affected Mathia object/path when applicable;
- why the observation is mathematically material rather than proof-engineering trivia;
- whether execution can safely continue before disposition.

The issue-review session classifies each handoff using the canonical merged research skills in this repository.

### Persisted-finding challenge

If the observation could make a persisted finding false, overstrong, under-specified, or unsafe at its current strength, load:

```text
.agents/skills/mathia-research-adversarial/SKILL.md
.agents/skills/mathia-research-review/SKILL.md
```

and create or continue the adjacent `.review.md` according to those skills.

### Separate research lead

If the observation exposes a distinct potentially fertile mechanism, invariant, equivalence, generalization, obstruction, or cross-line question whose truth is not required to settle the current formalization target, load:

```text
.agents/skills/mathia-research-clues/SKILL.md
```

and create or strengthen only a `status: proposed` clue. Research Watch owns acceptance, rejection, resolution, and any later substantive finding.

### Both

One discovery may require both a review and a clue. Keep their roles distinct: the review challenges a persisted claim; the clue poses a separate research question.

### Proof-engineering only

A smaller Lean proof route, useful mathlib declaration, import simplification, tactic workaround, or implementation convenience that does not materially alter the mathematics remains issue/PR evidence.

Do not inflate every Lean observation into research state.

## Blocking semantics

If Gate 0 or later Lean work exposes a mathematical defect that makes progression unsafe, require the executor to stop at the checkpoint after posting the structured handoff.

The issue-owning review session decides disposition and whether a repaired target needs new design before proof work resumes.

Non-blocking research leads may wait until the next declared checkpoint, but they must not disappear from final handoff.

## Lean proof-integrity contract

Unless the issue explicitly establishes a narrower or stronger boundary, an accepted formalization should require:

- compilation under Mathia's pinned Lean/mathlib environment;
- no `sorry` or `admit` in accepted theorem dependencies;
- no new axioms introduced to discharge the target;
- no `unsafe` proof shortcuts;
- no floating-point/sample evidence used as proof premises;
- no unchecked generated/CAS certificates;
- `#print axioms` or an equivalent Lean trust-footprint inspection on principal theorems;
- theorem statements unchanged from the Gate-0 accepted boundary;
- fresh final review of statement fidelity, proof integrity, and research-handoff completeness.

Use the canonical merged independent-review skill when the issue requires a separate technical review:

```text
.agents/skills/codex-independent-review/SKILL.md
```

The independent reviewer remains read-only; its mathematical findings are inputs to the issue-owning review session.

## Issue shape

Compose with `design-github-issue`; do not duplicate its generic workflow or copy reusable procedure into every issue.

A Mathia Lean formalization issue should make only the task-specific boundaries explicit:

1. authoritative Mathia target(s);
2. intended Lean theorem boundary;
3. Gate-0 falsification/prior-art/mathlib-reuse risks specific to the target;
4. exact Lean environment or authorization to introduce the minimal local one;
5. target-specific proof-integrity or dependency constraints beyond this skill;
6. surrounding Mathia conclusions that remain out of scope;
7. any target-specific checkpoint/final-review conditions.

The research-handoff, issue-driven execution, Git/GitHub, and independent-review procedures remain owned by their canonical repository skills and should not be recopied into each issue.
