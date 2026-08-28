---
name: mathia-research-mind
description: Synthesize the current mutable Mathia mind from persisted research evidence, including Git-visible finding withdrawals and accepted adversarial-review outcomes, with strict mind-only ownership and direct-main publication gates.
---

# Mathia Research Mind

## Responsibility

Use this skill for the recurring or scheduled **Mathia Research Mind** synthesis pass.

The mind owns **durable mathematical synthesis**, not primary research evidence. Its job is to read already-persisted research findings and maintain the best current structural model of the program: principles, conjectural mechanisms, hidden equivalences, impossibility principles, reusable heuristics, cross-result deductions, and mathematically meaningful research lines.

The mind is deliberately a **mutable current snapshot**. It may revise, merge, weaken, refute, or delete its own intuitions when the underlying evidence changes. Git preserves the history; `mind/**` should represent what Mathia should believe and reason from now.

Research-watch tasks own findings and source evidence. The adversarial process owns review sidecars under the shared review protocol. The graph curator owns derived graph views. The prior-art materializer owns `research/prior_art/`. This skill must not compete with those roles.

The mind may derive second-order or third-order conceptual consequences from persisted evidence, but it must not fabricate missing premises, silently strengthen a theorem, or treat a plausible mathematical connection as established evidence.

When adversarial review is present, read `.agents/skills/mathia-research-review/SKILL.md` **only to interpret review-event semantics**. The Mind does not participate in the review dialogue and must not create, edit, or delete `.review.md` files.

## Current tree and Git change stream

The **current repository tree is authoritative for current knowledge**. Git is the change stream that tells the Mind what changed since it last reconciled the snapshot.

At the start of every run:

1. synchronize the current default branch;
2. locate the most recent reachable commit with prefix `research(mind):` when one exists;
3. inspect the Git delta from that revision to current `HEAD` for relevant research paths, including **added, modified, and deleted** files;
4. use the delta to prioritize reconciliation, but still consume the current mind/evidence state needed for a coherent full synthesis.

If no previous `research(mind):` commit exists, reconstruct from the current tree without inventing a synthetic cursor.

If a prior run processed a delta but produced no mind change and therefore no commit, a later run may see the same events again. That is acceptable: reprocessing must be idempotent and must not create churn merely to advance a cursor.

Relevant change events include:

```text
A  research/<line>/findings/<finding>.md
M  research/<line>/findings/<finding>.md
D  research/<line>/findings/<finding>.md
A  research/<line>/findings/<finding>.review.md
M  research/<line>/findings/<finding>.review.md
D  research/<line>/findings/<finding>.review.md
```

Review sidecars are workflow evidence, not mathematical evidence. Their only role here is to help interpret whether a finding withdrawal came from the accepted review protocol.

## Review outcome semantics

Follow `mathia-research-review` exactly:

- an **open** `.review.md` means the finding is challenged but the review has not converged;
- deleting only `.review.md` while the finding remains means the adversary accepted the owner's defense and the finding remains current evidence;
- deleting the finding and its `.review.md` together means the owner conceded the material objection and **withdrew the claim**;
- a corrected/narrower replacement, when valuable, appears as a **new finding with a new stable ID** and must be evaluated as new evidence.

Do **not** mutate the mind merely because an objection is open. An unresolved adversarial comment is not itself an accepted mathematical result. It may prevent an unsupported *upgrade* during the current pass, but deletion or weakening of existing mind knowledge requires a change in the current evidence, a converged review outcome, or another persisted mathematical reason.

### Deleted finding rule

A deleted canonical finding is no longer current evidence, even though Git can recover its historical contents.

Treat every `D findings/<finding>.md` event as a **high-priority invalidation/reconciliation signal**:

1. use history only to identify what the deleted finding claimed and which mind notes depended on it;
2. never continue citing the deleted file as positive current evidence;
3. inspect current surviving findings for independent support;
4. revise, weaken, split, redirect, or delete affected local intuitions accordingly;
5. propagate the consequences into local `RESEARCH_LINES.md`;
6. then re-evaluate any global intuition or global research line that depended directly or transitively on the withdrawn claim.

Do not leave tombstone intuitions merely to record that a belief used to exist. Git already records that history.

### Deleted review rule

A `D *.review.md` event **without deletion of its target finding** is not an invalidation signal. It means the dispute converged in favor of the claim under the protocol. The Mind should simply reason from the surviving current finding.

## Discover research lines dynamically

Do not hard-code active research-line names.

At the start of every run, inspect the direct children of `research/`.

A directory `research/<line>/` is a current local research line when it contains canonical durable research evidence under:

```text
research/<line>/findings/
```

Always exclude these repository-level roots:

```text
research/prior_art/
research/graph/
research/mind/
research/clues/
```

Also include a line **for reconciliation only** when either:

- the Git delta contains a deleted finding from that line; or
- the line still has `mind/**` content that may depend on evidence deleted in the delta.

This prevents the important edge case where deleting the final finding of a line would otherwise make the line disappear from discovery before its stale mind could be cleaned up.

A reconciliation-only line may cease to be a current research line after its obsolete mind state has been removed. Do not preserve empty mind directories merely for symmetry.

Process lines in a deterministic order, for example lexicographic path order. Do not infer scientific priority from execution order.

## Read-only evidence for each local line

For each discovered or reconciliation-only line, read only the material needed for coherent synthesis:

```text
research/<line>/README.md
research/<line>/findings/**
research/<line>/SOURCES.md
research/<line>/LEAN_CANDIDATES.md
research/<line>/mind/**            # current local snapshot to revise
```

The individual current files under `findings/**` are canonical research evidence. Exclude `*.review.md` from the evidence set.

Do **not** use the line's `graph/**` directory as mathematical evidence. Graph content is derived presentation state.

Do **not** read `research/prior_art/**` as an input to this skill. Prior-art and novelty statements may be inherited from findings that already persisted them, but this mind pass does not independently reconcile against the canonical prior-art projection.

Do not use `experiments/**`, raw corpora, OpenAlex artifacts, or unrelated repository data merely to enlarge context. If a current finding points to a specific repository artifact essential to its exact claim, inspect only that exact dependency when necessary.

## External research boundary

The recurring mind pass is synthesis, not literature acquisition or novelty search.

Do not browse the web or run a new literature search to justify an intuition. Novelty/prior-art status should come from persisted current research evidence.

If a candidate intuition depends on an external theorem, novelty claim, or mathematical premise that is not adequately persisted, keep the intuition at the weaker supported level or omit it and report the missing evidence. Leave evidence acquisition to the appropriate research watch or prior-art process.

## Local mind output

Each current research line may own:

```text
research/<line>/mind/
├── RESEARCH_LINES.md
└── intuition/
    └── MI-xxx-<slug>.md
```

Create these paths only when there is substantive synthesis to persist. Do not create empty placeholders merely because a research line exists.

Local minds describe what the **current surviving findings** of that line imply. Cross-line principles belong in the global mind instead of being duplicated into every local line.

## Global mind output

The program-level mind lives at:

```text
research/mind/
├── RESEARCH_LINES.md
└── intuition/
    └── MI-xxx-<slug>.md
```

The global mind is not a summary or concatenation of local minds. It should contain only genuinely cross-line principles, bridges, incompatibilities, common information-loss mechanisms, common preserved invariants, or constraints on the wider Mathia/Riemann program.

Build the global synthesis **after** all affected local minds have been reconciled during the current run. The refreshed local minds and their current underlying findings are the inputs to the global pass.

## What belongs in an intuition

The purpose of an `MI-*` note is a durable mathematical idea useful to future reasoning.

Prefer a compact set of coherent intuitions. Revise, merge, strengthen, weaken, split, refute, or remove existing intuitions instead of appending one note per run or one note per finding.

A durable intuition should include, where mathematically relevant:

1. **Core intuition** — the structural idea in clear mathematical language.
2. **Strongest justified claim** — theorem-like principle, conjectural mechanism, or impossibility statement at the actual evidence level.
3. **Synthesis of evidence** — current findings and relationships that support it.
4. **Counterevidence / boundary cases** — where it fails, what remains universal, conditional, or unresolved.
5. **Epistemic status** — exact, asymptotic, heuristic, speculative, etc.
6. **Novelty/prior-art status** — only as already supported by persisted evidence.
7. **Falsification criterion** — a calculation, theorem, counterexample, or control that would materially refute or narrow it.
8. **Lean-formalizable core** — when there is a natural finite formal statement.
9. **Evidence level** — use the established scale:

```text
speculative
plausible
supported
proved
refuted
```

Never silently upgrade evidence. A synthesis can be valuable while remaining `supported` or `plausible`.

Do not keep a deleted finding in `Synthesis of evidence`, even as a historical citation. If the historical path matters to understanding a present idea, the surviving/current evidence must still independently justify the idea.

Do not put TODOs, priorities, owners, schedules, implementation tasks, run dates, or a "next move" section inside an intuition note.

## What belongs in RESEARCH_LINES.md

Each local mind and the global mind maintain one compact `RESEARCH_LINES.md`.

A research line is a durable **mathematical question or discriminating mechanism**, not project status. It should state:

- the mathematical question or candidate bridge;
- links to the current intuition(s) that motivate it;
- the decisive calculation, theorem, counterexample, matched control, or falsification test when known.

Prefer revising, merging, redirecting, or removing research lines over accumulating them indefinitely.

Do not include dates, owners, priorities, issue/task status, schedules, implementation plans, completion checklists, or daily/weekly history.

A research line should be removed when withdrawal of its supporting evidence makes its mathematical premise obsolete and no current independent support remains. Git history preserves chronology.

## Synthesis discipline

Actively look for nontrivial consequences across multiple current findings rather than merely restating them.

High-value synthesis includes patterns such as:

- several independent negative results implying one broader impossibility principle;
- two constructions revealing the same invariant in different representations;
- an exact identity proving that an apparently new observable is only a coordinate change;
- a local-versus-global principle explaining repeated spectral failures;
- a repeated quotient/telescoping mechanism showing where information is lost;
- a mechanism showing which ordered or relational information survives localization, pinching, duality, lifting, or spectral compression;
- a bridge between two or more independently discovered research lines;
- apparently different branches imposing the same necessary condition on any credible RH mechanism.

Do not promote an intuition merely because several files use similar language. The relationship must be mathematically supported by current persisted claims.

## Adversarial synthesis gate

Before creating or strengthening an intuition or research line, try to kill it using the current repository evidence.

Check, when applicable:

- whether one supporting finding is conditional or `NEEDS-AUDIT`;
- whether a supporting finding has disappeared from the current tree;
- whether a later current finding weakens, corrects, supersedes, or refutes an earlier surviving one;
- whether the apparent mechanism is universal rather than prime-specific;
- whether a transform, determinant, trace, spectrum, or quotient loses the claimed information;
- whether a relationship is only analogy rather than an established bridge;
- whether constants, normalizations, topology, domains, convergence hypotheses, or operator categories differ materially;
- whether a supposed cross-line equivalence is only a shared classical coordinate system.

Important negative findings and accepted withdrawals should prune or constrain the mind. Do not preserve an attractive intuition after its only supporting mechanism has been decisively invalidated or withdrawn.

## Missing-information rule

Do not fill gaps by invention.

If a candidate synthesis requires a premise that cannot be recovered from the current persisted evidence:

1. do not strengthen or create the affected intuition as if the premise were established;
2. preserve any weaker statement that is genuinely supported;
3. report the exact missing evidence and relevant paths when it materially blocks synthesis.

Continue unrelated local or global synthesis only when doing so cannot hide the ambiguity or produce an internally inconsistent mind.

## Execution cycle

### 1. Synchronize and inspect the change stream

Start from the current default branch and a coherent repository revision. Determine the relevant `A/M/D` delta from the previous `research(mind):` commit when available.

Process **deletions first**, because they can invalidate already-materialized mind knowledge. Then process modified/new evidence. Open reviews are advisory workflow state, not accepted evidence changes.

If the default branch advances materially while the run is synthesizing, refresh affected inputs before publishing.

### 2. Discover current and reconciliation-only lines

Inspect `research/` and apply the structural and deletion-aware discovery rules. Do not rely on a task prompt listing active branches.

### 3. Reconcile each local mind

For each affected line, in deterministic order:

1. identify deleted findings and current findings from the delta/tree;
2. inspect current local mind if present;
3. remove or rewrite dependencies on withdrawn evidence;
4. resynthesize from surviving current evidence;
5. refresh `RESEARCH_LINES.md` from the resulting intuition set;
6. remove obsolete mind files rather than leaving tombstones;
7. avoid churn when no substantive mathematical synthesis changed.

### 4. Refresh the global mind

After local reconciliation:

1. inspect refreshed local minds and current persisted evidence needed to audit cross-line claims;
2. identify genuinely program-level principles or bridges;
3. revise `research/mind/intuition/**`;
4. refresh `research/mind/RESEARCH_LINES.md`;
5. remove or weaken global synthesis whose local/current support disappeared;
6. do not duplicate local material merely to make the global mind look complete.

### 5. Final adversarial and stale-reference review

Before publication verify:

- every substantive statement is grounded in **current** persisted research evidence;
- no deleted finding remains cited as positive support;
- no open review was mistaken for a converged mathematical result;
- no finding was silently upgraded;
- no prior-art statement was invented or refreshed from external research;
- refuted/superseded/withdrawn evidence does not remain as positive support;
- local intuitions remain local and global intuitions are genuinely cross-line;
- research-line files contain mathematical questions, not project management;
- no chronology/status diary or tombstone note was introduced;
- the diff is entirely inside allowed mind paths.

If unsupported synthesis survives, weaken or remove it before commit.

## Ownership and hard path gate

This skill may write only to:

```text
research/mind/**
research/<discovered-or-reconciliation-line>/mind/**
```

It may **read** Git history and review sidecars to interpret events, but it must not modify:

```text
research/prior_art/**
research/graph/**
research/<line>/graph/**
research/<line>/README.md
research/<line>/SOURCES.md
research/<line>/LEAN_CANDIDATES.md
research/<line>/findings/**
experiments/**
docs/**
code/tests/prompts outside mind ownership
```

Do not perform "minimal index/link updates" outside `mind/**`. The graph curator can discover and link mind output independently.

If the required correction belongs in a finding, review, prior-art note, graph, source list, code artifact, or experiment, leave it to the owning process.

## Publication policy

The scheduled Mathia Research Mind is the owner of mind synthesis and may publish substantive mind-only changes **directly to the repository default branch**.

Commit only when at least one mathematical intuition or mathematical research line was materially added, strengthened, weakened, merged, split, redirected, refuted, or removed — including changes required because a reviewed finding was withdrawn.

Do not commit merely to record that a delta was processed.

Before every commit:

1. inspect the complete diff;
2. verify every changed path passes the dynamic mind ownership gate;
3. verify no `prior_art/`, `graph/`, finding, review sidecar, code, experiment, or unrelated file changed;
4. verify no current mind note depends solely on a deleted finding;
5. verify the source revision is coherent and not stale against newly landed research evidence/review resolutions;
6. run the final adversarial review;
7. remove unrelated formatting churn;
8. use the commit prefix:

```text
research(mind): <mathematical synthesis>
```

Examples:

```text
research(mind): remove synthesis based on withdrawn flute claim
research(mind): integrate prime-lattice information-loss constraints
research(mind): merge common relational-memory intuitions
research(mind): demote universal spectral threshold mechanism
```

## Reporting

At the end of a run, report only substantive mathematical synthesis:

- intuitions newly created, materially strengthened/weakened, merged, split, refuted, or removed;
- research lines materially added, redirected, merged, or removed;
- review-converged finding withdrawals that materially changed the current mind;
- blockers caused by missing/contradictory current evidence that require an owning research process.

If nothing changed materially, say so concisely or remain silent when the scheduled task's notification policy permits it.

Do not produce a project-status recap, chronological summary, daily journal, or list of everything inspected.
