---
name: mathia-formalization-design
description: Design a Mathia-owned formalization issue for a mathematical claim, with a blocking statement/adversarial/prior-art/reuse gate and a structured research-handoff contract independent of the selected formal backend.
---

# Mathia Formalization Design

## Responsibility

Use this skill when Mathia wants to test, sharpen, falsify, or machine-check a mathematical claim with a formal system.

This is a thin specialization of the canonical merged repository skill:

```text
.agents/skills/design-github-issue/SKILL.md
```

Load that repository skill as the generic issue-design authority. Do not use a PR, feature branch, historical copy, or external duplicate of the skill as procedure authority unless a controlling issue explicitly pins a historical workflow for reproducibility.

The **task represented by the controlling Mathia issue** owns the scientific question. A formal backend, execution repository, proof engineer, reviewer, or chat session is an actor inside that task, not a separate scientific owner.

## Scientific ownership

When the mathematical target belongs to Mathia, keep the controlling scientific issue in this Mathia repository.

The formal artifact may be implemented in this repository or in another execution host when that is technically useful. The issue must decide the execution location from the needs of the target, not from historical precedent.

If execution is external:

- the Mathia issue remains authoritative for the mathematical target, scope, gates, and research consequences;
- the external issue or PR is only an execution record and must point back to the controlling Mathia issue;
- execution-host convenience must not determine, weaken, or silently reshape the mathematical claim.

Do not create an external controlling issue merely because a particular prover or toolchain is available there.

## Formalization Gate 0

Every nontrivial formalization issue must begin with a blocking statement/adversarial/prior-art/reuse gate before proof implementation.

Design Gate 0 to reconstruct the intended claim independently, including as relevant:

- exact quantifiers and theorem surface;
- domains, side conditions, singularities, and definedness;
- normalization, sign, indexing, orientation, gauge, or convention choices;
- boundary and degenerate cases;
- the relation between informal notation and the proposed formal object;
- whether the formal target is weaker, stronger, or equivalent to the persisted claim;
- which surrounding consequences are explicitly outside the formal theorem.

The gate must try to falsify the proposed statement rather than merely translate its notation.

Also require, when material:

- prior-art search for exact or stronger mathematical/formal results;
- an audit of reusable declarations, libraries, packages, theories, or proof infrastructure in the selected backend;
- an explicit dependency/version decision before importing or rebuilding external formal infrastructure;
- a clear trust boundary for computation, automation, generated certificates, or external solvers used by the backend.

Allowed gate outcomes should include, with task-specific names if useful:

- safe progression to proof;
- reuse-only / already formalized / no material delta;
- statement repair required;
- mathematical conflict or counterevidence.

A negative gate result is a successful scientific outcome when it prevents proving the wrong statement.

## Formal backend is issue-specific

This skill does not choose Lean, another prover, a CAS-backed certificate system, or any permanent Mathia formalization stack.

The controlling issue must identify the backend and the evidence needed for that backend. For example:

- for Lean, relevant evidence may include pinned Lean/mathlib revisions, compilation, placeholder checks, and `#print axioms`;
- for another prover, require the corresponding build/check command, admitted-hole policy, dependency pins, and trust/axiom footprint;
- for generated or externally checked certificates, define exactly what is trusted and independently verified.

Backend-specific procedure belongs in the issue only when it is material to the bounded target. Do not turn one successful backend into a project-wide architecture decision.

## Formal success boundary

The issue must state what a successful formal proof establishes and what it does not.

Keep separate:

- fidelity of the formal statement to the intended mathematics;
- success of the proof/check in the selected backend;
- validity of wider Mathia findings or research programs;
- novelty or prior-art status;
- analytic, geometric, asymptotic, computational, or representation bridges excluded from the formal theorem.

Do not let a checked theorem silently certify surrounding prose that was not formalized.

## Research-handoff contract

Every formalization issue must require the executor to report material mathematical discoveries to the **controlling Mathia issue**.

The executor does not directly write Mathia research sidecars or clues as part of formalization execution. The issue comment is transport to the issue-owning review/orchestration session.

A material handoff should contain:

- the exact mathematical observation;
- whether it threatens/corrects the target or is independent of it;
- exact evidence: derivation, counterexample, formal theorem/check, file/commit, or failed statement;
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

and materialize or continue the adjacent `.review.md` according to those skills.

### Separate research lead

If the observation exposes a distinct potentially fertile mechanism, invariant, equivalence, generalization, obstruction, or cross-line question whose truth is not required to settle the current formalization target, load:

```text
.agents/skills/mathia-research-clues/SKILL.md
```

and create or strengthen only a `status: proposed` clue. Research Watch owns acceptance, rejection, resolution, and any later substantive finding.

### Both

One discovery may require both a review and a clue. Keep their roles distinct: the review challenges a persisted claim; the clue poses a separate research question.

### Proof-engineering only

A smaller proof route, useful library declaration, import simplification, tactic/automation workaround, representation convenience, or backend-specific implementation detail that does not materially alter the mathematics remains issue/PR evidence.

Do not inflate every formalization observation into research state.

## Blocking semantics

If Gate 0 or later execution reveals a mathematical defect that makes progression unsafe, require the executor to stop at the checkpoint after posting the structured handoff.

The issue-owning review session decides disposition and whether a repaired target needs new design before proof work resumes.

Non-blocking research leads may wait until the next declared checkpoint, but they must not disappear from final handoff.

## Validation contract

For an accepted formal proof, require backend-appropriate evidence sufficient to establish:

- the exact target was checked under the pinned environment;
- no forbidden placeholder, admission, extra axiom, unsafe shortcut, or unchecked certificate crossed the issue's declared proof boundary;
- the principal theorem's trust/axiom footprint is understood using the selected backend's appropriate mechanism;
- the checked statement still matches the Gate-0 frozen target;
- final review covers statement fidelity, proof/check integrity, and completeness of research handoffs.

Use fresh independent technical review when the issue requires it. The independent reviewer remains read-only; its findings are additional inputs to the issue-owning review session.

## Issue shape

Compose with `design-github-issue`; do not duplicate its generic workflow.

A formalization issue should nevertheless make these boundaries explicit:

1. authoritative Mathia target(s);
2. intended formal theorem boundary;
3. Gate-0 falsification/prior-art/reuse requirements;
4. selected formal backend and execution location when already known;
5. backend-specific proof-integrity/trust requirements;
6. research-handoff contract;
7. surrounding Mathia conclusions that remain out of scope;
8. checkpoint/final-review conditions.

Do not design a permanent prover stack, formalization DSL, ontology, or repository layout unless a separate issue explicitly requires that decision.
