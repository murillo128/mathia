---
name: mathia-formalization-executor
description: Execute an approved Mathia-owned formalization issue through Gate 0, Lean proof engineering, proof validation, and structured research handoff without directly mutating Mathia findings, adversarial sidecars, or clues.
---

# Mathia Formalization Executor

## Responsibility

Use this skill when Codex is implementing an approved Mathia formalization issue.

This skill is a thin specialization of:

```text
.agents/skills/spec-driven-codex-loop/SKILL.md
```

Load that skill first. It owns the normal issue-driven execution lifecycle, branch/PR discipline, validation, checkpoint publication, and ready-for-review handoff.

The controlling Mathia issue owns the scientific question. The executor owns proof engineering and evidence only within that contract.

## Entry gate

Before proof implementation:

1. load `AGENTS.md`;
2. load the controlling Mathia issue;
3. confirm the issue is execution-ready/in-progress under the generic workflow;
4. identify the exact execution host, toolchain, source revision, and formal-library revision required by the issue;
5. confirm Gate 0 exists and has not been bypassed.

If Lean work is hosted in another repository, preserve the Mathia issue as the controlling authority and link any child issue/PR back to it.

## Gate 0 is blocking

Do not begin the proof simply because the intended theorem looks plausible.

Execute the issue-defined statement/adversarial/prior-art/reuse audit first. The gate must inspect the actual intended theorem surface, not merely propose Lean syntax.

At minimum, test the risks named by the issue around:

- domains and singularities;
- quantifiers and hidden hypotheses;
- normalization/sign/indexing/gauge conventions;
- boundary and degenerate cases;
- equivalence between the informal claim and the formal target;
- exact/stronger prior formalizations;
- reusable formal-library declarations and dependencies.

Publish the exact gate target and obtain the required independent verdict before proof implementation.

If Gate 0 requires statement repair or finds mathematical conflict, do not weaken or alter the target in implementation. Return to the controlling Mathia issue/design boundary.

## Proof engineering

After a safe gate verdict, implement the smallest coherent theorem chain that proves the frozen mathematical target.

Prefer existing mathlib/Lean infrastructure over bespoke generic machinery when practical. Do not force the prose proof route if a smaller exact route proves the same frozen theorem.

A proof-engineering simplification is allowed when it preserves the theorem. A mathematical target change is not.

Unless the issue explicitly declares another proof boundary, accepted delivered theorems must contain no:

- `sorry`;
- `admit`;
- new axioms introduced to discharge the target;
- `unsafe` proof shortcuts;
- floating-point or sampled evidence used as proof premises;
- unchecked generated/CAS certificates.

Run `#print axioms` or the issue-defined equivalent on principal theorems and preserve the result.

## Formalization is also an observation surface

During statement reconstruction, proof search, debugging, and review, actively notice when Lean is exposing mathematics rather than merely syntax.

Material observations include, for example:

- a missing or unnecessary hypothesis;
- a counterexample or degenerate case;
- a stronger/weaker exact theorem boundary;
- a sign, normalization, indexing, orientation, or gauge subtlety;
- an unexpected invariant/equivalence;
- a proof that only works in a narrower domain than the persisted claim;
- a genuinely simpler exact mathematical route;
- a potential generalization or obstruction suggested by the formal derivation.

Do not silently absorb such observations into implementation.

## Structured research handoff

The executor reports material mathematical observations to the **controlling Mathia issue**. It does not directly write Mathia research knowledge files.

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

Use prose rather than a new machine schema; the fields above are a checklist, not a permanent data format.

### No direct research-tree writes

As part of this executor role, do **not** create/update/delete:

```text
research/**/findings/*.review.md
research/**/clues/**
```

Do not rewrite a finding, create a new finding, or change clue disposition.

The issue-owning review/orchestration session consumes the handoff and, when warranted, loads the Mathia adversarial-review or clue skill to materialize the durable research object.

A comment such as `Mathia feedback` is not itself durable research disposition; it must contain enough evidence for the task-level review to route it.

## Blocking discoveries

If an observation materially challenges the frozen theorem or the persisted finding in a way that makes proof progression unsafe:

1. publish the handoff immediately to the controlling Mathia issue;
2. stop at the checkpoint;
3. do not prove a repaired/narrowed theorem under the old contract;
4. resume only after the issue-level task has disposed of the challenge and, when necessary, design has frozen a repaired target.

Non-blocking independent research leads may be collected until the next declared checkpoint, but final handoff must account for them.

## Independent review

Use the issue-required fresh independent reviewer for Gate 0 and final proof review.

The independent reviewer remains read-only. It may discover material mathematics; record those findings in the checkpoint evidence so the issue-owning review session can route them through adversarial-review/clue protocols when warranted.

A technical `PASS` means the exact reviewed formal target is safe at that boundary. It does not:

- merge the PR;
- close the controlling issue;
- resolve an open Mathia adversarial sidecar;
- accept a clue;
- establish research novelty;
- validate unformalized surrounding claims.

## Final validation

Before ready-for-review handoff, verify as required by the controlling issue:

- exact theorem source compiles under the pinned toolchain;
- placeholder/new-axiom/unsafe checks are clean;
- principal axiom footprints are recorded;
- theorem statements still match the Gate-0 frozen contract;
- no numerical falsification aid was promoted into proof evidence;
- external dependencies and source revisions are exact;
- all material formalization discoveries have structured handoffs in the controlling Mathia issue, or explicitly record `Formalization research handoff: none`;
- fresh final technical review covers theorem fidelity, proof integrity, and completeness of the research handoff.

## Cross-repository delivery

If implementation lives outside Mathia:

- keep the child PR focused on formal artifacts/evidence;
- link it to the controlling Mathia issue prominently;
- do not create an external scientific authority competing with the Mathia issue;
- keep research disposition in Mathia.

The executor ends with the implementation PR ready for user/ChatGPT review according to `spec-driven-codex-loop`. It never merges, enables auto-merge, closes the Mathia issue, accepts/resolves a clue, or authors a replacement Mathia finding.
