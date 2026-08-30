---
name: mathia-formalization-executor
description: Execute one approved Mathia Lean formalization issue autonomously through adversarial Gate 0, proof engineering, Lean validation, fresh subagent review, and direct-main publication.
---

# Mathia Lean Formalization Executor

## Responsibility

Use this skill when Codex is asked to execute an approved Mathia Lean formalization issue.

The controlling issue owns the exact mathematical question and theorem boundary. This skill owns the reusable execution procedure.

This is intentionally a **no-PR autonomous executor**, analogous to `mathia-compute-executor` but with a durable checked Lean artifact and stronger mathematical review gates.

There is deliberately:

- no implementation PR;
- no user review/merge checkpoint after successful autonomous review;
- no committed Gate-0 report;
- no committed independent-review report;
- no durable feature branch requirement.

A local branch/worktree may be used as scratch execution state. Publication is a direct commit to `main` only after every gate below passes.

## Authority and fresh-context independence

Before execution:

1. read `AGENTS.md`;
2. read the controlling formalization issue;
3. read this skill;
4. read the exact associated canonical finding(s), open adjacent review sidecars, and only the additional persisted mathematics needed to reconstruct the target;
5. inspect the current Mathia Lean/Lake setup and relevant existing formalization source;
6. load `.agents/skills/codex-independent-review/SKILL.md` for fresh Gate/final review semantics;
7. load `.agents/skills/codex-github-operations/SKILL.md` before publication;
8. load the research review/clue skills only when the routing rules below require them.

Treat the issue as the scientific contract and recompute independently from persisted evidence. Do not recover or depend on the originating Research Watch's hidden reasoning.

The current repository skill owns generic execution procedure. Boilerplate in an older issue that merely says "feature branch", "PR", "ready for review", or asks for a `*Gate*.md` file is superseded by this workflow unless that issue explicitly records a later target-specific reason for the exception.

If the issue is not self-contained enough to identify the intended theorem without inventing a material mathematical choice, return it to design rather than choosing a convenient theorem.

## No-PR execution model

Do not create a publication PR and do not wait for human review.

Use local uncommitted files, a scratch branch/worktree, temporary Lean files, exploratory scripts, or other ephemeral artifacts as useful during execution. Keep them out of the final repository diff unless they are part of the issue-authorized durable Lean theorem itself.

The durable outputs of a successful run are normally:

```text
1. issue-authorized Lean source / minimal Lean project wiring
2. optionally, one or more `status: proposed` clues produced by the fresh independent reviewer when genuinely warranted
```

A material challenge to the source finding is not a clue; route it through the adversarial review protocol described below.

## Lean environment

Use the Lean tooling currently available on the execution machine and Mathia's current local Lean/Lake setup.

Do **not** require a predetermined Lean or mathlib version. Record the actual environment only when it materially helps reproduce or diagnose the run.

If the bounded issue needs minimal Mathia-local Lean/Lake wiring that does not yet exist, add only what the issue requires. Do not broaden the task into a general formalization framework.

## Gate 0 is blocking and adversarial

Do not begin proof implementation because the theorem looks plausible.

Before implementation, spawn a **fresh isolated subagent** that has not inherited the executor's hidden reasoning. Give it the minimal review packet:

- `AGENTS.md`;
- this skill and `codex-independent-review`;
- the controlling issue;
- the authoritative finding/current review state;
- the proposed theorem surface;
- relevant existing Lean/mathlib declarations.

The Gate-0 reviewer must reconstruct and actively try to falsify the theorem, checking as relevant:

- exact quantifiers and hidden hypotheses;
- domains, side conditions, singularities, and definedness;
- normalization, sign, indexing, orientation, gauge, and conventions;
- boundary and degenerate cases;
- fidelity between the canonical finding and proposed Lean statement;
- whether the target is weaker, stronger, or equivalent;
- exact or stronger prior formalizations;
- reusable mathlib/current Mathia Lean declarations;
- dependency/import choices.

Map the result to exactly one operational outcome:

```text
safe progression
reuse-only / already formalized / no material delta
statement repair required
mathematical conflict / counterevidence
```

### No Gate artifact

Gate 0 is review process, not an additional repository document.

Do **not** create or commit files such as:

```text
*Gate.md
*_GATE0.md
*Gate0.md
```

When durable transport is useful, leave a concise comment on the controlling issue containing the frozen theorem surface, verdict, and any material blocking observation. Detailed review scratch remains ephemeral.

### Negative Gate outcomes

- `reuse-only`: verify the existing theorem really satisfies the issue, record that conclusion on the issue, and do not create repository churn merely to re-express it.
- `statement repair required`: do not silently weaken/change the theorem; return the issue to design with the exact repair needed.
- `mathematical conflict / counterevidence`: route the challenge through a fresh adversarial research subagent before any further proof progression.

## Research challenge routing

If Gate 0 or later Lean work exposes a material challenge to a persisted finding, spawn a fresh subagent and load:

```text
.agents/skills/mathia-research-adversarial/SKILL.md
.agents/skills/mathia-research-review/SKILL.md
```

The adversarial subagent independently reconstructs the challenge and owns any create/update/delete of the adjacent `.review.md` under those skills' normal publication rules.

Do not encode a direct objection to the finding as a clue merely to avoid the review protocol.

If the challenge makes theorem progression unsafe, stop the current formalization until the issue/finding boundary is repaired or the review establishes that the frozen theorem remains safe. Do not prove around the defect.

## Proof engineering

After a safe Gate verdict, implement the smallest coherent Lean theorem chain that proves the frozen target.

Prefer existing mathlib and existing Mathia Lean declarations over bespoke generic machinery when practical. A simpler proof route is welcome when it proves the same theorem. A change to the mathematical target is not.

Unless the controlling issue explicitly declares another proof boundary, accepted delivered theorems must contain no:

- `sorry`;
- `admit`;
- new axioms introduced to discharge the target;
- `unsafe` proof shortcuts;
- floating-point or sampled evidence used as proof premises;
- unchecked generated or CAS certificates.

Run `#print axioms` on principal public theorems, or the issue-defined equivalent trust-footprint inspection.

## The Lean file must explain what it proves

Every principal new formalization module must contain a module-level comment near the top that makes the durable artifact self-describing.

It must state:

1. the **exact canonical finding path** associated with the formalization;
2. the **ordinary-mathematics theorem/result actually proved** in the file;
3. any important surrounding claim that remains **outside** the formal theorem when omission could otherwise be misleading.

A natural shape is:

```lean
/-!
# <human theorem name>

Associated finding:
`research/<line>/findings/<finding>.md`

Formalized theorem boundary:
<concise statement of the theorem Lean proves>.

Not formalized:
<important surrounding claims, if any>.
-/
```

Do not use a Gate-file reference as a substitute. An issue number or finding ID alone is not enough when the exact repository path is available.

When one formalization spans multiple modules, every principal/public module should be locally intelligible; avoid duplicating long prose, but preserve enough finding/theorem context that an isolated `.lean` file is not anonymous.

## Formalization is an observation surface

During statement reconstruction, proof search, debugging, and review, actively notice when Lean exposes mathematics rather than syntax.

Material observations include, for example:

- a missing or unnecessary hypothesis;
- a counterexample or degenerate case;
- a stronger/weaker exact theorem boundary;
- a sign, normalization, indexing, orientation, or gauge subtlety;
- an unexpected invariant or equivalent formulation;
- a proof that works only on a narrower domain than the persisted claim;
- a genuinely different exact mathematical route;
- a plausible generalization or obstruction suggested by the formal derivation.

Challenges to the persisted finding use the adversarial-review route above. Distinct fertile directions are considered during final independent review below.

## Lean validation

Before final review, run the repository-native Lean command and verify as applicable:

- the exact durable Lean source compiles/checks successfully;
- no forbidden `sorry`, `admit`, new axiom, `unsafe`, floating/sample premise, or unchecked-certificate dependency remains;
- principal `#print axioms` results or equivalent trust evidence are clean and understood;
- theorem statements still match the Gate-0 frozen contract;
- no exploratory numerical computation was promoted into proof evidence;
- relevant dependencies/imports are proportionate to the bounded theorem;
- each principal `.lean` file satisfies the finding/theorem header-comment contract.

## Fresh final subagent review

After implementation and Lean validation, spawn a **new fresh independent-review subagent** over the exact final candidate diff. It must not inherit the executor's hidden reasoning or the Gate reviewer's reasoning.

Use `.agents/skills/codex-independent-review/SKILL.md` and require at least:

1. exact statement/finding correspondence;
2. proof-integrity and trust-footprint inspection;
3. independent reconstruction of the Lean theorem in ordinary mathematics;
4. independent reconstruction/compression of the proof as mathematics rather than tactics;
5. explicit statement of the unformalized boundary;
6. adversarial inspection of boundary cases, conventions, hidden assumptions, and accidental weakening;
7. a final verdict of `PASS`, `PASS_WITH_NOTES`, `FAIL`, or `BLOCKED`.

`FAIL` or `BLOCKED` prevents publication. Correct material defects and obtain a new fresh final review of the changed target.

### Reviewer-produced clues

If the formal-to-human reconstruction exposes a **genuinely distinct, falsifiable research direction**, the final reviewer may load:

```text
.agents/skills/mathia-research-clues/SKILL.md
```

and create or materially strengthen only a `status: proposed` clue under the owning research line or global clue inbox as that skill permits.

The reviewer, not the executor's convenience, decides whether the clue gate passes. A shorter tactic proof, useful lemma, or import simplification is not enough.

When a reviewer-generated clue is ready, the executor may include that exact proposed clue in the same final direct-main publication as the Lean artifact, preserving `origin: independent-review` and all normal clue deduplication/evidence-boundary rules. Research Watch alone owns later clue disposition and any substantive finding.

## Direct-main publication gate

Publish directly to the repository default branch with **no PR** only when all of these hold:

1. the controlling issue is approved/execution-ready and identifies the exact research target;
2. Gate 0 was performed by a fresh isolated subagent and returned `safe progression`;
3. the final theorem is unchanged in mathematical meaning from the Gate-0 frozen boundary;
4. repository-native Lean validation succeeds;
5. the exact final candidate passed a fresh independent-review subagent with `PASS` or `PASS_WITH_NOTES` and no material unresolved defect;
6. every principal Lean module satisfies the associated-finding/theorem-boundary comment contract;
7. the only implementation diff is issue-authorized Lean source plus the smallest necessary Mathia Lean project wiring;
8. no Gate report, review report, scratch script, generated log/data, or unrelated cleanup is included;
9. any research clue included was produced/strengthened by the final independent reviewer, remains `status: proposed`, and passes `mathia-research-clues` deduplication/path gates;
10. any material finding challenge has already been routed through the adversarial-review protocol rather than hidden in implementation;
11. `main` was refreshed immediately before publication and the relevant files were checked for concurrent changes.

If `main` moved in a way that touches the formalization target, dependencies, associated finding/review state, or clue path, reconcile and rerun the validation/review affected by that movement before publishing. Never force-push or overwrite another actor's changes.

Prefer one focused direct-main commit for the accepted Lean artifact plus any reviewer-produced proposed clue, for example:

```text
formalize(WP-014): prove two-point Schiffer indefiniteness
```

or:

```text
formalize(PC-063): prove anchor-Haar crossover
```

A finding-review sidecar created by an adversarial research subagent remains owned and published by that review workflow; do not fold unrelated review churn into the formalization commit merely for atomicity.

## Issue completion

The formalization issue is control-plane state, not a PR-backed implementation issue.

After successful direct-main publication:

- leave a concise final issue comment linking the commit and principal Lean file(s);
- state the exact bounded theorem outcome;
- mention any reviewer-produced proposed clue path;
- mention any surviving explicit unformalized boundary that matters for interpretation;
- close the issue as completed.

If Gate 0 concludes `reuse-only`, close the issue after recording the already-existing formal artifact and why it satisfies the target.

If a material statement-design defect prevents trustworthy execution, return the issue to `design-required` rather than inventing a repaired theorem. If an unavailable capability blocks execution, use `blocked`.

## Terminal report

Keep the executor/user-facing handoff minimal:

- controlling issue;
- principal Lean artifact/commit or reuse-only result;
- final independent-review verdict;
- any proposed clue path;
- any real blocker.

Do not ask for a PR review or merge decision after the direct-main publication gate has passed.