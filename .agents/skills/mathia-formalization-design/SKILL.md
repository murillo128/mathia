---
name: mathia-formalization-design
description: Design a Mathia-owned formalization issue for a persisted finding, clue, or research claim, including a blocking statement/adversarial/prior-art/reuse gate and a structured research-handoff contract for execution.
---

# Mathia Formalization Design

## Responsibility

Use this skill when Mathia wants to test, sharpen, falsify, or machine-check a mathematical claim through Lean or another formal system.

This skill is a thin specialization of:

```text
.agents/skills/design-github-issue/SKILL.md
```

Load that skill first. It owns the generic issue-design workflow. This skill adds only the formalization-specific scientific boundary.

The **task represented by the controlling Mathia issue** owns the scientific question. A Lean execution repository, proof engineer, reviewer, or chat session is an actor inside that task, not a separate scientific owner.

## Scientific ownership

When the target is a Mathia finding, clue, or research claim, create the controlling issue in `murillo128/mathia`.

A different repository such as `qwen-lean` may be selected as an execution host when its Lean toolchain, dependencies, or proof infrastructure are useful. In that case:

- the Mathia issue remains authoritative for the mathematical target, scope, gates, and research consequences;
- any external issue/PR is a child execution record and must point back to the Mathia issue;
- execution-host convenience must not determine the statement or silently narrow the research question.

Do not create a qwen-lean controlling issue merely because the proof will compile there.

## Formalization Gate 0

Every nontrivial formalization issue must begin with a blocking statement/adversarial/prior-art/reuse gate before proof implementation.

Design Gate 0 to require an independent reconstruction of the intended claim, including as relevant:

- exact quantifiers and theorem surface;
- domains and nonzero/singularity conditions;
- normalization, sign, indexing, orientation, and gauge conventions;
- boundary and degenerate cases;
- exact relation between informal notation and the proposed formal object;
- whether the proposed theorem is weaker, stronger, or merely equivalent to the persisted claim;
- what surrounding prose or consequences are explicitly outside the formal theorem.

The gate must actively try to falsify the statement rather than merely translate notation.

Also require:

- prior-art search for exact or stronger formalizations when material;
- a pinned mathlib/Lean reuse inventory or equivalent formal-library audit;
- a dependency decision before importing or rebuilding external formal infrastructure.

Allowed gate outcomes should include, with task-specific names if useful:

- safe progression to proof;
- reuse-only / already formalized / no material delta;
- statement repair required;
- mathematical conflict or counterevidence.

A negative gate result is a successful scientific outcome when it correctly prevents proving the wrong statement.

## Formal success boundary

The issue must state what a successful proof establishes and what it does not.

Keep separate:

- statement fidelity;
- formal proof success;
- validity of a wider Mathia finding or research program;
- novelty or prior-art status;
- any analytic/geometric/asymptotic bridge excluded from the finite theorem.

Do not let a compiling theorem silently certify surrounding prose that was not formalized.

## Research-handoff contract

Every formalization issue must require the executor to report material mathematical discoveries to the **controlling Mathia issue**.

The executor does not directly write Mathia research sidecars or clues as part of proof execution. The issue comment is transport to the issue-owning review/orchestration session.

A material handoff should contain:

- the exact mathematical observation;
- whether it threatens/corrects the target or is independent of it;
- exact evidence: derivation, counterexample, theorem, file/commit, or failed formal statement;
- the affected Mathia finding/path when applicable;
- why the observation is mathematically material rather than proof-engineering trivia;
- whether execution can safely continue before disposition.

Design the issue so the issue-review session can classify each handoff as:

### Persisted-finding challenge

If it could make a persisted finding false, overstrong, under-specified, or unsafe at its current strength, the issue-review session loads:

```text
.agents/skills/mathia-research-adversarial/SKILL.md
.agents/skills/mathia-research-review/SKILL.md
```

and materializes the adjacent `.review.md` according to that protocol.

### Separate research lead

If it exposes a distinct potentially fertile mechanism, invariant, equivalence, generalization, obstruction, or cross-line question whose truth is not required to settle the formalization target, the issue-review session loads:

```text
.agents/skills/mathia-research-clues/SKILL.md
```

and creates or strengthens only a `status: proposed` clue. Research Watch owns acceptance, rejection, resolution, and any later finding.

### Both

One discovery may legitimately require both a review and a clue. Keep their roles distinct: the review challenges the persisted claim; the clue asks a separate research question.

### Proof-engineering only

A smaller proof route, useful library lemma, import simplification, tactic workaround, or implementation convenience that does not materially alter the mathematics remains issue/PR evidence.

Do not inflate every Lean observation into research state.

## Blocking semantics

If Gate 0 or later execution reveals a mathematical defect that makes progression unsafe, the issue must require the executor to stop at the checkpoint after posting the structured handoff.

The issue-owning review session decides disposition and whether a repaired target needs design work before proof resumes.

Non-blocking research leads may wait until the next declared checkpoint, but they must not disappear from final handoff.

## Validation contract

For an accepted Lean proof, normally require:

- compilation under the pinned toolchain;
- no `sorry`, `admit`, new axioms, unsafe proof shortcuts, floating-point proof premises, or unchecked certificates unless the issue explicitly declares a different boundary;
- `#print axioms` or equivalent on principal theorems;
- exact theorem fidelity review;
- a final research-handoff audit showing all material observations reached the controlling issue.

Use fresh independent technical review when the issue declares it. The independent reviewer remains read-only; its findings are additional inputs to the issue-owning review session.

## Issue shape

Compose with `design-github-issue`; do not duplicate its full structure.

A formalization issue should nevertheless make these boundaries explicit:

1. authoritative Mathia target(s);
2. exact intended formal theorem boundary;
3. Gate-0 falsification/prior-art/reuse requirements;
4. execution host and pinned environment when already known;
5. proof-integrity requirements;
6. research-handoff contract;
7. surrounding Mathia conclusions that remain out of scope;
8. checkpoint/final-review conditions.

Do not design a permanent Lean DSL, ontology, or project-wide formalization architecture unless a separate issue explicitly requires it.
