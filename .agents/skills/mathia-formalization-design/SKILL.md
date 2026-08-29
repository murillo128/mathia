---
name: mathia-formalization-design
description: Design a Mathia-owned Lean formalization issue with a blocking statement/adversarial/prior-art/mathlib-reuse gate and structured handoff of mathematical discoveries back into Mathia research.
---

# Mathia Lean Formalization Design

## Responsibility

Use this skill when Mathia wants to test, sharpen, falsify, or machine-check a mathematical claim in Lean.

This is a thin specialization of the canonical repository skill:

```text
.agents/skills/design-github-issue/SKILL.md
```

Load that file from the current Mathia repository as the generic issue-design authority. Repository skills on the default branch are procedure authority; do not substitute copies from old PRs or unrelated repositories.

The **task represented by the controlling Mathia issue** owns the scientific question. Codex, Lean, and the independent reviewer are actors inside that task.

## Repository boundary

For Mathia formalization work:

- the controlling issue lives in this Mathia repository;
- Lean source and formalization evidence are developed on a Mathia feature branch;
- the implementation PR targets Mathia;
- mathematical discoveries flow back through the controlling Mathia issue.

The issue chooses the smallest sensible Mathia-local path for the formal artifact. Do not freeze a permanent repository layout or formalization framework from this skill alone.

## Lean environment

Use the Lean tooling available on the execution machine together with Mathia's current local Lean/Lake setup.

Do **not** make a predetermined Lean or mathlib version part of the scientific contract. The actual environment used may be recorded as execution evidence, but a formalization should not be blocked merely because the machine is running a different current Lean version than an older task.

If Mathia does not yet contain a Lean project, the first formalization that needs one may add the **smallest local Lake/Mathlib setup** required to compile the bounded target. Keep that setup inside Mathia and proportionate to the work; do not turn initial setup into a general formalization framework.

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
- an explicit dependency/import decision before rebuilding generic infrastructure.

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

The issue-review session classifies each handoff using the canonical research skills in this repository.

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

- successful compilation/checking with the Lean environment available on the execution machine;
- no `sorry` or `admit` in accepted theorem dependencies;
- no new axioms introduced to discharge the target;
- no `unsafe` proof shortcuts;
- no floating-point/sample evidence used as proof premises;
- no unchecked generated/CAS certificates;
- `#print axioms` or an equivalent Lean trust-footprint inspection on principal theorems;
- theorem statements unchanged from the Gate-0 accepted boundary;
- fresh final review of statement fidelity, proof integrity, and research-handoff completeness.

Use the canonical independent-review skill when the issue requires a separate technical review:

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
4. any target-specific Lean setup/import needs not already covered by Mathia's local environment;
5. target-specific proof-integrity or dependency constraints beyond this skill;
6. surrounding Mathia conclusions that remain out of scope;
7. any target-specific checkpoint/final-review conditions.

The research-handoff, issue-driven execution, Git/GitHub, and independent-review procedures remain owned by their canonical repository skills and should not be recopied into each issue.
