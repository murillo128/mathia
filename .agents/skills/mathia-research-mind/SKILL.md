---
name: mathia-research-mind
description: Maintain concrete, source-grounded mathematical key points for agent reuse, reconciling finding withdrawals and accepted reviews with strict mind-only ownership and direct-main publication gates.
---

# Mathia Research Mind

## Responsibility

Use this skill for the recurring or scheduled **Mathia Research Mind** synthesis pass. Read `.agents/skills/mathia-research-representation/SKILL.md` before substantive mathematical work.

The mind owns **reusable mathematical key points**, not primary research evidence or a narrative about the program. Retain a specific mechanism, obstruction, reduction, simplification, counterexample, or connection that changes what a future researcher can infer or test. Generality is useful only when the objects, hypotheses and mathematical relation supporting it remain recoverable.

The mind is a **mutable current snapshot**. Revise, merge, weaken, split or delete intuitions when evidence or their mathematical usefulness changes. Git preserves history; `mind/**` should contain what is worth loading into a fresh agent context now. There is no quota of intuitions, no minimum output per pass, and no requirement that every finding or line produce a note.

Research Watch owns findings and source evidence. The adversarial process owns review sidecars. Graph Curator owns derived graph views. The prior-art materializer owns `research/prior_art/`. Mind must not compete with these roles.

A conjectural connection or second-order deduction is allowed, but must not fabricate premises, strengthen a theorem silently, or turn analogy into established evidence. An intuition need not contain a complete proof, experiment plan or Lean target. It is not another finding.

When review is present, read `.agents/skills/mathia-research-review/SKILL.md` only to interpret review-event semantics. Mind does not participate in review dialogue and must not create, edit or delete `.review.md` files.

## Current tree and Git change stream

The **current repository tree is authoritative for current knowledge**. Git identifies changes since the last reconciliation.

At the start of every pass:

1. synchronize the current default branch;
2. locate the most recent reachable `research(mind):` commit, when one exists;
3. inspect the delta to current `HEAD` for added, modified and deleted findings, review sidecars and affected mind files;
4. prioritize that delta, while reading enough current evidence for coherent synthesis.

Without a previous Mind commit, reconstruct from the current tree; do not invent a cursor. A no-change pass needs no commit. Reprocessing the same events must be idempotent rather than create churn to advance a cursor.

Review sidecars are workflow evidence, not mathematical evidence. Use them only to interpret challenges and accepted withdrawals.

## Review outcome semantics

Follow `mathia-research-review` exactly:

- an open `.review.md` means the finding is challenged and review has not converged;
- deletion of only the review while the finding survives means the adversary accepted the owner's defense;
- deletion of the finding and its review together means the owner conceded the objection and withdrew the claim;
- a corrected or narrower replacement is a new finding with a new stable ID and must be evaluated as new evidence.

An open objection is not an accepted mathematical result. It can prevent an unsupported upgrade, but weakening existing knowledge requires changed current evidence, a converged outcome or another persisted mathematical reason.

A deleted canonical finding is no longer current evidence. Treat its deletion as a high-priority reconciliation signal. Use history only to identify its claim and dependents; never cite it as positive current support. Inspect surviving evidence, revise or remove affected local intuitions and questions, then reconcile global dependents. Do not leave tombstone intuitions; Git already preserves history.

Deleting only a review is not an invalidation signal. Reason from the surviving finding.

## Discover research lines dynamically

Inspect the direct children of `research/`; do not hard-code line names. A current local line contains canonical evidence under `research/<line>/findings/`. Exclude repository roots `research/prior_art/`, `research/graph/`, `research/mind/` and `research/clues/`.

Include a line for reconciliation when the delta deletes a finding from it or it retains mind content potentially dependent on withdrawn evidence. Deleting a line's final finding must not hide its stale mind. Remove obsolete mind state rather than preserve empty directories for symmetry.

Process lines deterministically, for example lexicographically; execution order is not scientific priority.

## Read-only evidence

For each affected line, load only what coherent synthesis requires:

```text
research/<line>/README.md
research/<line>/findings/**
research/<line>/SOURCES.md
research/<line>/LEAN_CANDIDATES.md
research/<line>/mind/**
```

Current finding files are canonical evidence; exclude `*.review.md` from that evidence set. Inspect the actual source claim and its assumptions when rewriting an intuition, not just its title or the existing summary. Read exact linked artifacts only when essential to the finding's claim.

Do not use `graph/**` as mathematical evidence. Do not read `research/prior_art/**` for this pass or preload experiments, corpora, OpenAlex artifacts or unrelated data. Inherit prior-art status only when already persisted in findings.

This is synthesis, not literature acquisition. Do not browse or conduct a new novelty search. If an external theorem or premise is inadequately persisted, preserve only the weaker supported statement or omit it and report the exact gap. Evidence acquisition belongs to the relevant research role.

## Local and global output

Local output belongs to:

```text
research/<line>/mind/RESEARCH_LINES.md
research/<line>/mind/intuition/MI-xxx-<slug>.md
```

Global output belongs to:

```text
research/mind/RESEARCH_LINES.md
research/mind/intuition/MI-xxx-<slug>.md
```

Create files only for substantive content. Local notes preserve the useful mathematics of that line; global notes must add a concrete cross-line relation, transfer or obstruction, not concatenate local summaries. Similar vocabulary is not a bridge. Identify the actual correspondence and its hypotheses; mark analogies as analogies. Do not require each local insight to generalize across lines.

Reconcile affected local minds before global synthesis. Build global claims from refreshed local notes and their current underlying findings, not stale global narratives.

## What belongs in an intuition

An `MI-*` note is internal mathematical working memory. Preserve the **point that matters**: what object or construction is involved, what mechanism acts under which conditions, and what follows or becomes worth testing. These are meaning requirements, not mandatory fields or headings.

Concrete content can be a decisive formula with its domain, a counterexample and the exact class it excludes, a sufficient condition weaker than the one previously pursued, a suspected cancellation term, or an explicit mapping between constructions. Keep parameter dependencies and the distinction between necessary and sufficient conditions. Do not invent a numerical rate, constant or theorem merely to make a note look precise.

Reject generic methodological advice and elaborate restatements of the goal. Phrases such as "preserve structure", "need arithmetic coherence", "control the critical limit", or "prove the required estimate" are not standalone intuitions. State which term, map, norm, quantifier, coupling, factor or loss creates the issue and what has been learned beyond knowing that the problem is unsolved. If replacing the mathematical nouns leaves a note applicable to almost any problem, reconstruct it from sources or remove it.

Examples of the distinction:

- Instead of "separate geometric from arithmetic effects", retain the exact prime-to-integer control and which threshold it preserves; that threshold alone cannot distinguish the two inputs.
- Instead of "local bounds do not ensure global coherence", retain the specific off-diagonal sum or family-dependent norm that the available blockwise bound does not control.
- Instead of "exact recovery is not stable", retain the inverse or destination map and the stated loss, topology or parameter range in which transport fails.

Do not generalize a counterexample beyond the class it actually excludes. Conversely, a broader exclusion or a new connection is substantive only when the enlargement or correspondence is explicit.

### Representation and evidence

The body has **no prescribed language, format, section order or length**. Equations, terse points, pseudocode, mixed languages, diagrams, derivations and task-local notation are all allowed. No human-facing introduction, translation, prose duplicate, nine-part template or named "core intuition" section is required. Use enough definitions for a fresh agent to recover the content; compression must not hide a premise.

Preserve existing stable IDs and paths when the same idea survives, and retain machine-required metadata and valid source links. Do not recycle a deleted ID for a different idea. Link the current findings supporting the key claims and distinguish what is proved there from a conditional implication, plausible connection or speculation here. Sources are anchors, not a bibliography of everything inspected.

Use the established evidence scale when a level is recorded: `speculative`, `plausible`, `supported`, `proved`, `refuted`. Never upgrade evidence through rewriting. A synthesis supported by proved components is not automatically a proved global theorem. Do not repeat novelty, evidence level or caveats under several headings when one precise qualification suffices.

A falsification test is useful only if it can actually refute or narrow the stated conjecture or transfer. A check that merely confirms a warning is not its falsifier. Do not force a test onto an exact explanatory key point. Lean cores and prior-art notes are optional and belong only when they add mathematical information already supported by sources.

No TODOs, owners, priorities, schedules, execution dates, status diaries or task lists belong inside intuitions. Mathematical implications and discriminating tests are welcome; implementation planning belongs elsewhere.

### Reconstructing existing notes

During reconciliation or an explicitly requested corpus cleanup, read each affected note against its current sources. Extract the actual mechanism and boundaries; do not merely shorten the old prose or preserve its headings. Keep already-useful representations. Recover a missing condition from the source rather than inventing one.

Merge genuine duplicates, split only independently reusable ideas, and remove unsupported or purely generic notes. There is no target note count or compression ratio. Preserve a valid idea's ID/path when possible. Update dependent mind questions and links in the same publication. Search for incoming references before deleting or renaming; references outside Mind ownership are a handoff to their owner, not permission to edit those files during a scheduled pass. Do not leave misleading cross-line references after narrowing a claim.

## What belongs in RESEARCH_LINES.md

Each local/global mind may maintain one compact `RESEARCH_LINES.md` containing durable **mathematical questions**, not project status. Tie each retained question to current intuitions and name the decisive quantity, hypothesis, calculation, counterexample or matched control when known.

Do not inflate "obtain the missing uniformity/cancellation" into a research line without specifying the object, family and relevant condition. A genuinely unknown mechanism may remain open; say exactly what is known and what is not rather than adding invented precision. Questions can be expressed in any recoverable representation and need no fixed template.

Revise, merge or remove questions as evidence changes. Remove a question whose premise lost all current support. Do not retain dates, owners, priorities, issue/task status, schedules, implementation plans, checklists or history.

## Synthesis discipline

Seek nontrivial consequences, not one new slogan per finding. Valuable synthesis includes an explicit invariant correspondence, a demonstrated larger exclusion class, an identity showing an observable is only a coordinate change, a weaker sufficient condition, or a specific information-loss calculation.

For a cross-line bridge, identify the objects on both sides and the relation that survives their different assumptions. Several notes requesting "coherence" or "conditioning" do not establish a shared mathematical obstruction. Where the comparison remains suggestive, mark it as a candidate analogy and state the missing identification.

Source-backed retrospective explanation is not evidence that an intuition improves downstream research. Do not report note count, length, connectivity, citations or linguistic novelty as discovery or measured utility.

## Adversarial synthesis gate

Before creating or strengthening a note or question, challenge it against current evidence. Check conditional or `NEEDS-AUDIT` premises, disappeared findings, later corrections, universal rather than prime-specific effects, information lost by transforms/quotients, analogy mistaken for equivalence, and differences in constants, normalizations, topology, domains, convergence, quantifiers or operator categories.

Try the concrete counterexample or competing mechanism allowed by the sources. Check that removing generic advice leaves a mathematical point and that the claimed new content is not already present under another name. Keep a useful existing note unchanged when no substantive improvement exists.

Negative results and accepted withdrawals must constrain the snapshot. Never retain an attractive claim after its sole mechanism has been withdrawn or invalidated.

## Missing-information rule

Do not fill gaps by invention. If a required premise is not recoverable from current persisted evidence, do not create or strengthen the claim as established. Preserve a genuinely supported weaker point and report the exact missing evidence and paths when it blocks synthesis. Continue unrelated work only when it cannot hide the ambiguity or make the snapshot inconsistent.

## Execution cycle

1. **Synchronize.** Start from a coherent default-branch revision and inspect the delta from the previous Mind commit. Process deletions before modified/new evidence. Open reviews are advisory workflow state.
2. **Discover.** Apply structural, deletion-aware line discovery; do not rely on a task's static line list.
3. **Reconcile locally.** Read affected current notes and exact sources, remove withdrawn dependencies, reconstruct useful key points, and refresh their mathematical questions. Avoid churn and empty placeholders.
4. **Reconcile globally.** Audit the actual cross-line relation against refreshed local notes and evidence. Remove or narrow unsupported connections; do not duplicate local content for completeness.
5. **Review.** Check current support, evidence levels, quantifiers, valid references, useful concrete content, nonduplication and ownership. Verify that no deleted/refuted finding is positive support and no unresolved review is an accepted result.
6. **Refresh before publishing.** If main advanced materially, refresh affected inputs and repeat affected gates. A no-change pass ends without a commit.

## Ownership and hard path gate

This skill may write only:

```text
research/mind/**
research/<discovered-or-reconciliation-line>/mind/**
```

It may read Git history and review sidecars to interpret events, but must not modify:

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

Do not perform "minimal index/link updates" outside `mind/**`. Graph Curator can discover and link mind output independently. Corrections to findings, reviews, prior art, graphs, sources, code and experiments belong to their owning processes. This skill does not authorize editing itself or other skills during scheduled synthesis.

## Publication policy

The scheduled Mathia Research Mind owns mind synthesis and may publish substantive mind-only changes **directly to the default branch**. Commit only when a mathematical key point or question materially changes, including removal of generic/unsupported synthesis or reconciliation of a withdrawn source. Do not commit merely to record processing, impose a preferred language/template, or reformat an already-useful note.

Before every commit:

1. inspect the complete diff;
2. verify the dynamic Mind path gate and exclude all unrelated changes;
3. verify no note relies solely on deleted or withdrawn evidence;
4. check coherence against newly landed findings and accepted review outcomes;
5. run the final adversarial and stale-reference review;
6. remove unrelated formatting churn;
7. use `research(mind): <mathematical synthesis>`.

Use the repository Git/GitHub operations skill for transport and concurrency safety. Never force-push. A concurrent main change requires refreshing affected sources and gates rather than overwriting it.

## Reporting

Report substantive changes to mathematical key points and questions, accepted withdrawals affecting the snapshot, and exact missing/contradictory evidence requiring another role. Distinguish corpus cleanup from new mathematical discovery. Do not report a project-status recap, chronological diary or list of everything inspected.

When nothing changed materially, say so concisely or remain silent when the task's notification policy permits it.
