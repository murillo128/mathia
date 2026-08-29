---
name: mathia-formalization-executor
description: Execute an approved Mathia-owned Lean formalization issue through Gate 0, proof engineering, Lean validation, and structured research handoff without directly mutating Mathia findings, adversarial sidecars, or clues.
---

# Mathia Lean Formalization Executor

## Responsibility

Use this skill when Codex is implementing an approved Mathia Lean formalization issue in this repository.

This is a thin specialization of the canonical repository skill:

```text
.agents/skills/spec-driven-codex-loop/SKILL.md
```

Load that file from the current Mathia repository as the generic execution authority. Repository skills on the default branch are procedure authority; do not substitute copies from old PRs or unrelated repositories.

The controlling Mathia issue owns the scientific question. The executor owns Lean proof engineering and evidence only within that contract.

## Repository and branch boundary

All ordinary formalization execution happens in Mathia:

- work from a Mathia feature branch governed by the controlling issue;
- keep Lean source, Gate evidence, validation evidence, and implementation changes in that branch/PR;
- target the Mathia default branch with the formalization PR;
- report mathematical discoveries to the controlling Mathia issue.

## Entry gate

Before proof implementation:

1. load `AGENTS.md`;
2. load the controlling Mathia issue;
3. load the canonical `spec-driven-codex-loop` skill;
4. confirm the issue has exactly one valid execution state and is safe to work;
5. inspect the Lean tooling available on the machine, Mathia's current local Lean/Lake setup, and relevant existing formalization source;
6. confirm the issue defines a blocking Gate 0 and that it has not been bypassed.

### Lean environment

Use the Lean tooling currently available on the execution machine and Mathia's current local Lean/Lake setup.

Do **not** require a predetermined Lean or mathlib version. Record the actual environment used when it helps reproduce or diagnose the run, but version identity is execution evidence rather than a scientific progression gate.

If no Lean project exists in Mathia yet, the executor may add the **smallest local Lake/Mathlib setup** needed for the bounded formalization. Keep it in Mathia, keep it minimal, and do not turn initial setup into a general framework.

## Gate 0 is blocking

Do not begin proof implementation simply because the intended theorem looks plausible.

Execute the issue-defined statement/adversarial/prior-art/mathlib-reuse audit first. The gate must inspect the intended theorem surface, not merely propose Lean syntax.

At minimum, test the material risks named by the issue around:

- domains, side conditions, singularities, and definedness;
- quantifiers and hidden hypotheses;
- normalization, sign, indexing, orientation, gauge, and conventions;
- boundary and degenerate cases;
- fidelity between the persisted mathematical claim and the Lean target;
- exact or stronger prior formalizations;
- reusable mathlib or existing Mathia Lean declarations;
- dependency/import choices.

Publish the exact Gate target and obtain the required independent verdict before proof implementation.

If Gate 0 requires statement repair or finds mathematical conflict, do not weaken or alter the theorem in implementation. Return to the controlling Mathia issue/design boundary.

## Proof engineering

After a safe Gate verdict, implement the smallest coherent Lean theorem chain that proves the frozen mathematical target.

Prefer existing mathlib and existing Mathia Lean infrastructure over bespoke generic machinery when practical. Do not force the prose proof route if a smaller exact Lean proof establishes the same frozen theorem.

A proof-engineering simplification is allowed when it preserves the theorem. A mathematical target change is not.

Unless the controlling issue explicitly declares another proof boundary, accepted delivered theorems must contain no:

- `sorry`;
- `admit`;
- new axioms introduced to discharge the target;
- `unsafe` proof shortcuts;
- floating-point or sampled evidence used as proof premises;
- unchecked generated or CAS certificates.

Run `#print axioms` on principal public theorems, or the issue-defined equivalent Lean trust-footprint inspection, and preserve the result.

## Formalization is also an observation surface

During statement reconstruction, proof search, debugging, and review, actively notice when Lean is exposing mathematics rather than merely syntax.

Material observations include, for example:

- a missing or unnecessary hypothesis;
- a counterexample or degenerate case;
- a stronger or weaker exact theorem boundary;
- a sign, normalization, indexing, orientation, or gauge subtlety;
- an unexpected invariant or equivalent formulation;
- a proof that only works in a narrower domain than the persisted claim;
- a genuinely simpler exact mathematical route;
- a plausible generalization or obstruction suggested by the formal derivation.

Do not silently absorb such observations into implementation.

## Structured research handoff

The executor reports material mathematical observations to the **controlling Mathia issue**. It does not directly write Mathia research knowledge files as part of this role.

For each material observation, post a concise `Formalization research handoff` containing:

```text
Observation:
<exact mathematical content>

Relation to target:
<threatens/corrects target | independent lead | both | implementation-only candidate>

Evidence:
<Lean theorem/file/commit, derivation, counterexample, or failed statement>

Affected Mathia object:
<finding/path if applicable>

Materiality:
<why this can change the scientific interpretation>

Progression:
<safe to continue | block pending issue-review disposition>
```

The headings are a checklist, not a new permanent schema.

### No direct research-tree writes

As part of formalization execution, do **not** create/update/delete:

```text
research/**/findings/*.review.md
research/**/clues/**
```

Do not rewrite a canonical finding, create a new finding, or change clue disposition.

The issue-owning review/orchestration session consumes the handoff and, when warranted, loads the canonical Mathia research skills:

```text
.agents/skills/mathia-research-adversarial/SKILL.md
.agents/skills/mathia-research-review/SKILL.md
.agents/skills/mathia-research-clues/SKILL.md
```

That session decides whether to materialize an adversarial review, a proposed clue, both, or neither. Research Watch owns clue disposition and any later substantive finding.

An informal `Mathia feedback` comment is not a substitute for a structured handoff when the observation may be mathematically material.

## Blocking discoveries

If an observation materially challenges the frozen theorem or a persisted finding in a way that makes proof progression unsafe:

1. publish the handoff immediately to the controlling Mathia issue;
2. stop at the checkpoint;
3. do not prove a repaired or narrowed theorem under the old contract;
4. resume only after the issue-level task has disposed of the challenge and, when necessary, design has frozen a repaired target.

Non-blocking independent research leads may be collected until the next declared checkpoint, but final handoff must account for them.

## Independent review

Use the canonical independent-review skill when the controlling issue requires Gate or final technical review:

```text
.agents/skills/codex-independent-review/SKILL.md
```

The independent reviewer remains read-only. It may discover material mathematics; those findings become inputs to the issue-owning review session.

A technical `PASS` means the exact reviewed Lean target is safe at that checkpoint. It does not:

- merge the PR;
- close the controlling issue;
- resolve an open Mathia adversarial sidecar;
- accept or resolve a clue;
- create a new finding;
- establish research novelty;
- validate unformalized surrounding claims.

## Final validation

Before ready-for-review handoff, verify as required by the controlling issue:

- the exact Lean source compiles/checks successfully with the Lean environment available on the execution machine;
- no forbidden `sorry`, `admit`, new axiom, `unsafe`, or unchecked-certificate dependency remains in the accepted theorem boundary;
- principal `#print axioms` results or equivalent trust evidence are recorded;
- theorem statements still match the Gate-0 frozen contract;
- no numerical falsification or exploratory computation was promoted into proof evidence;
- material imports/dependencies used by the proof are recorded when relevant;
- all material mathematical discoveries have structured handoffs in the controlling Mathia issue, or explicitly record `Formalization research handoff: none`;
- fresh final technical review covers theorem fidelity, proof integrity, and completeness of research handoffs.

Use the repository-native Lean command defined by Mathia's current Lean project. If no command is yet canonical, use the simplest command that checks the bounded formalization and record it in the execution evidence.

## Delivery

The formalization PR lives in Mathia and follows `spec-driven-codex-loop`:

- one focused PR per controlling issue unless the issue explicitly decomposes delivery;
- keep it draft while implementation/checkpoint review remains incomplete;
- move it to ready-for-review only after required Lean validation and independent review pass;
- stop for user/ChatGPT review and merge decision.

The executor never merges, enables auto-merge, closes the controlling Mathia issue, accepts/resolves a clue, authors a replacement finding, or writes adversarial/clue research state directly.
