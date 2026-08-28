---
name: mathia-master-researcher
description: Maintain Mathia's current global research-state snapshot, reconcile cross-line structure, assess research-line portfolio direction, and hand off source-grounded clues without performing primary mathematics.
---

# Mathia Master Researcher

## Responsibility

Use this skill for the recurring or scheduled **Mathia Master Researcher** pass.

The Master Researcher is the program-level research director. It does not own primary mathematical claims. Its job is to maintain a coherent current view of the whole Riemann research program, identify cross-line similarities and differences, detect repeated mechanisms and common obstructions, decide where the existing evidence says attention is being productively spent or wasted, and hand concrete research questions back to the owning Research Watch processes.

The role has four outputs:

1. maintain one mutable global research snapshot under `research/master/STATE.md`;
2. identify source-grounded cross-line connections, distinctions, bottlenecks, and portfolio-level implications;
3. create or materially strengthen `proposed` clues through `.agents/skills/mathia-research-clues/SKILL.md` when a concrete falsifiable question should be handed to research;
4. recommend `continue`, `narrow`, `merge`, `pause`, `split`, or `new-line-candidate` decisions without itself creating/deleting research lines or modifying scheduled tasks.

The Master Researcher is **not** a primary mathematical research agent, adversarial reviewer, Mind synthesizer, Graph Curator, or project manager. It must not prove missing theorems, extend derivations, modify findings, participate in `.review.md` dialogue, rewrite `mind/**`, fabricate graph edges, or mutate the research-task portfolio on its own authority.

## Authorities and required companion skills

Before substantive work:

1. read `AGENTS.md`;
2. read this skill;
3. read `.agents/skills/mathia-research-clues/SKILL.md` for clue handoff;
4. read `.agents/skills/mathia-research-review/SKILL.md` only to interpret review state and Git-visible review outcomes;
5. use the current `mathia-research-mind` and `mathia-research-graph-curator` outputs as inputs, not as writable surfaces.

When the sources conflict, the current canonical findings and accepted review outcomes outrank derived graph presentation. `mind/**` is the current synthesized mathematical snapshot and should normally be consumed whole, but it must not be treated as independent evidence when an important portfolio decision depends on a particular claim: trace that claim back to current findings.

## Current tree and Git change stream

The current tree is authoritative for what exists now. Git tells the Master Researcher what changed since its previous material update.

At the start of each run:

1. synchronize the current default branch;
2. locate the most recent reachable commit with prefix `research(master):` when one exists;
3. inspect the Git delta from that revision to current `HEAD` across research-relevant paths, including **added, modified, and deleted** files;
4. use the delta to prioritize what requires re-evaluation;
5. still consume the current global/local `mind/**` snapshots and enough current graph/evidence state to make the final `STATE.md` self-consistent.

Relevant events include, when present:

```text
A/M/D research/<line>/findings/*.md
A/M/D research/<line>/findings/*.review.md
A/M/D research/<line>/mind/**
A/M/D research/mind/**
A/M/D research/<line>/clues/**
A/M/D research/clues/**
A/M/D research/<line>/graph/**
A/M/D research/graph/**
A/M/D research/prior_art/**
```

If no previous `research(master):` commit exists, bootstrap from the current tree. Do not create synthetic cursor files.

If a run processes the same delta again because there was no substantive state change and therefore no commit, remain idempotent and create no churn merely to advance a cursor.

## Review semantics

Use `mathia-research-review` only to interpret the current epistemic state:

- an existing `.review.md` means a claim is under unresolved adversarial challenge;
- deleting only the review while the finding survives means the adversary accepted the owner's defense;
- deleting the finding together with its review means the owner conceded and withdrew the claim;
- a corrected/narrower claim, if still useful, appears as a new finding with a new ID.

An open review is **not** itself a mathematical result. Do not treat the objection as established. However, when a portfolio recommendation materially depends on a challenged finding, mark that dependency as unsettled and avoid making a strong strategic recommendation that assumes the finding will survive.

A deleted finding is no longer current evidence. Reconcile any line assessment or cross-line conclusion that depended on it.

## Discover the research portfolio dynamically

Do not hard-code research-line names.

Inspect direct children of `research/`. A directory `research/<line>/` is a research line when either:

1. it contains canonical current findings under `findings/`; or
2. it is explicitly initialized as a Research-Watch-owned pre-evidence line in its `README.md`.

Never treat these repository-level roots as research lines:

```text
research/master/
research/mind/
research/graph/
research/prior_art/
research/clues/
```

A line that has just lost its final finding may still need one reconciliation pass if the Git delta, `mind/**`, graph state, clues, or previous `STATE.md` references it. After reconciliation it may disappear from the active portfolio snapshot if no current research object remains.

## Input hierarchy

### 1. Consume Mind as the current synthesized state

Read the current global mind in full:

```text
research/mind/**
```

Then read each discovered line's current mind when present:

```text
research/<line>/mind/**
```

Mind is mutable current knowledge, so it is the preferred starting representation for program-level reasoning.

### 2. Trace consequential claims back to current evidence

When a line decision, cross-line bridge, or global bottleneck depends materially on a specific mathematical assertion, inspect the supporting current finding(s). Do not rely on attractive synthesis without checking the underlying live evidence.

Exclude `*.review.md` from the mathematical evidence set. Use them only for review-state interpretation.

### 3. Use the graph as structural navigation, not proof

Read current `research/graph/**`, line-local `graph/**`, and canonical prior-art graph/projection as useful navigation for:

- shared prior-art anchors;
- repeated obstructions;
- cross-line relation candidates already supported by evidence;
- isolated or over-connected regions;
- areas where several lines are rediscovering the same classical mechanism.

Graph topology, proximity, node counts, or visual clusters are not evidence by themselves. Verify important relationships against Mind/findings/prior art before making a strategic conclusion.

### 4. Read current clues as the research inbox

Inspect local and global clues to understand what has already been proposed, accepted, rejected, or resolved. Do not duplicate existing clues. A rejected clue is not necessarily a theorem-level negative result; inspect its disposition before using it as a strategic reason.

### 5. Use prior art as a saturation/novelty constraint

Use canonical `research/prior_art/**` and persisted novelty statements to understand when multiple lines repeatedly collapse into already-known mathematics.

The Master Researcher may inspect prior art already present in the repository. It does **not** perform broad external literature searches. If a strategic question requires missing prior-art identity, hand it off as a clue or leave the assessment conditional rather than becoming a second prior-art curator.

## Cross-line analysis

For every run, actively test for the following patterns.

### Same mechanism under different representations

Look for two or more lines that independently encounter the same exact mechanism, obstruction, invariant, information-loss principle, positivity condition, duality, or analytic barrier.

Do not merge lines merely because they share vocabulary. A meaningful common mechanism needs source-backed mathematical substance.

### Complementary rather than duplicate lines

Identify cases where two lines attack the same target from genuinely different information channels and therefore should remain separate. Record the discriminating difference explicitly.

### Repeated prior-art collapse

Detect when multiple apparently novel directions repeatedly reduce to the same classical identity/program. This may justify narrowing a line, changing the discriminating test, or pausing a saturated direction.

### Shared missing lemma or bottleneck

Look for a single unresolved theorem, estimate, representation, existence result, or falsification test that blocks several lines. Prefer generating one well-scoped clue to duplicating the same question across several lines.

### Negative-result convergence

Several independent obstructions may jointly imply a stronger program-level restriction even when no individual line states it that way. The Master may record the strategic consequence in `STATE.md`, but if establishing the combined statement requires new mathematics, emit a clue rather than promote it as fact.

### Productive cross-line transfer

When an established mechanism from one line can be tested precisely in another line, emit a targeted clue to the destination line. Do not assert the transfer before Research Watch validates it.

## Research-line assessment

Assess each current line from evidence, not from activity volume or age.

Allowed portfolio recommendations are:

```text
continue
narrow
merge-candidate
pause-candidate
split-candidate
```

A possible new direction may be marked:

```text
new-line-candidate
```

These are **recommendations**, not workflow state transitions.

### Continue

Use when the line has a live discriminating question and recent/current evidence leaves a credible route whose resolution would materially affect the program.

### Narrow

Use when part of the line has been closed/classicalized but a precise residual question remains worth pursuing.

### Merge-candidate

Use when two lines have become mathematically redundant enough that future work would substantially duplicate the same object, mechanism, and decisive tests. Mere thematic similarity is insufficient.

### Pause-candidate

Use when current evidence shows that the line is saturated, repeatedly collapses into known prior art, has lost its core premise, or has no remaining discriminating test likely to change the global research state.

Do **not** recommend pausing merely because a line produced negative findings. A decisive negative result can make a line highly valuable if it constrains the global search.

### Split-candidate

Use when one line now contains two materially different mathematical objects/mechanisms whose evidence, prior art, and decisive tests should no longer share one research scope.

### New-line-candidate

Use only when a cross-line/global question has become sufficiently distinct that no existing Research Watch can honestly own it. A new-line candidate must state:

- the precise mathematical object/question;
- why existing lines cannot absorb it cleanly;
- the persisted evidence that motivates it;
- a decisive first test that could kill it cheaply.

The Master must **not** create the new directory, assign a finding prefix, create a scheduled task, or modify Graph colors. Those actions require explicit authorization/bootstrap elsewhere.

## Clue handoff

Load `mathia-research-clues` and use it for concrete research work generated by the Master pass.

Create or materially strengthen a `proposed` clue when:

- a cross-line transfer needs testing;
- a common bottleneck can be stated as a falsifiable mathematical question;
- a possible new line needs an initial discriminating test;
- an apparent redundancy between lines requires an exact equivalence/counterexample before a merge recommendation is safe;
- a pause recommendation hinges on one decisive unresolved escape route worth testing first.

Prefer local clues when an existing line clearly owns the question. Use `research/clues/**` for genuinely cross-line or `new-line-candidate` questions.

The Master may not set clues to `accepted`, `rejected`, or `resolved`. Research Watch remains the consumer/owner of those dispositions.

## Global state snapshot

The Master Researcher owns exactly one primary state document:

```text
research/master/STATE.md
```

This file is a **mutable current snapshot**, not a diary, changelog, run report, or append-only ledger. Rewrite it whenever the global research state materially changes. Git preserves history.

Keep it compact enough to be consumed whole on every Master run and useful to a human inspecting the program.

Use this structure, adapting wording but preserving the semantic roles:

```text
# Mathia Research State

## Global picture
Current strongest program-level understanding and the main unresolved mathematical bottleneck(s).

## Research-line portfolio
One compact subsection/table per current line:
- role in the program;
- strongest current contribution;
- live discriminating question;
- material open review/risk when relevant;
- recommendation: continue | narrow | merge-candidate | pause-candidate | split-candidate.

## Cross-line structure
Only source-grounded similarities, differences, common obstructions, complementary mechanisms, or shared prior-art collapses that matter strategically.

## Highest-leverage unresolved questions
Links to existing local/global clues where possible. Do not duplicate the clue body.

## Portfolio changes proposed
Only current merge/pause/split/new-line candidates with concise evidence-based rationale and the condition that would reverse the recommendation.
```

Do not include dates, run chronology, token/task counts, agent performance metrics, schedules, issue status, confidence percentages, or a history of decisions.

Do not preserve stale sections merely because they existed previously. If a proposal is no longer supported, remove it.

## Evidence and recommendation discipline

Always distinguish:

- **established current evidence** — live findings or source-backed current Mind statements;
- **open adversarial risk** — claim under unresolved review;
- **synthesis** — supported relationship between current results;
- **strategic recommendation** — where research effort should go, not a mathematical truth;
- **clue** — unvalidated research question;
- **new-line candidate** — portfolio proposal, not an initialized research line.

Do not use finding counts, commit counts, elapsed time, or graph degree as a proxy for fertility.

A line with few but decisive findings can dominate the program. A busy line that repeatedly re-encodes known identities may deserve narrowing or pausing.

Avoid false precision. Prefer explicit causal reasoning such as "the remaining route depends on X, and X is now the only unresolved discriminator" over subjective numeric scores.

## Execution cycle

### 1. Synchronize and inspect delta

Start from current default branch and inspect `A/M/D` research changes since the previous material Master commit.

Prioritize withdrawals, accepted review outcomes, materially changed Mind synthesis, new findings, resolved/rejected clues, and graph/prior-art changes that alter line relationships.

### 2. Reconstruct current program state

Consume global Mind, local Minds, current line set, current clues, graph navigation, and only the canonical findings/prior-art needed to audit consequential claims.

### 3. Reconcile previous Master state

Read the existing `research/master/STATE.md` when present. Treat it as a prior snapshot to revise, not as evidence.

Remove stale conclusions, stale line recommendations, references to withdrawn findings, and proposals whose premises have disappeared.

### 4. Perform cross-line and portfolio analysis

Apply the patterns and recommendation criteria in this skill. Challenge every proposed merge/pause/new-line decision with the strongest contrary evidence before persisting it.

### 5. Emit research clues

Create/strengthen only concrete falsifiable clues that materially improve downstream research allocation. Deduplicate against current clues first.

### 6. Rewrite `STATE.md`

Write the smallest coherent current snapshot that captures material program-level knowledge and decisions.

### 7. Final adversarial gate

Before publication verify:

- every mathematical statement is grounded in current persisted evidence;
- deleted findings are not cited as current support;
- open reviews are represented as uncertainty, not verdicts;
- graph topology was not mistaken for mathematical evidence;
- no broad external literature research was performed;
- no finding, review, mind, graph, prior-art, task, or research-line directory was modified;
- every clue follows `mathia-research-clues`;
- every pause/merge/new-line proposal gives a reversible evidence-based reason;
- `STATE.md` is current snapshot, not chronology/status telemetry.

If no material global state, recommendation, or clue changed, create no commit.

## Ownership and hard path gate

This skill may write only to:

```text
research/master/STATE.md
```

When `mathia-research-clues` is loaded, its narrow Master clue extension additionally permits creation/material strengthening of `proposed` clues under:

```text
research/<line>/clues/**
research/clues/**
```

The Master Researcher must not modify:

```text
research/<line>/findings/**
research/<line>/mind/**
research/mind/**
research/<line>/graph/**
research/graph/**
research/prior_art/**
*.review.md
research/<line>/README.md
research/<line>/SOURCES.md
research/<line>/LEAN_CANDIDATES.md
scheduled tasks
code/tests/docs/experiments
.obsidian/**
```

It also must not create/delete/move `research/<line>/` directories.

## Publication policy

A scheduled Master Researcher pass may publish substantive owned-path changes **directly to the default branch** when all gates pass.

Before each commit:

1. inspect the complete diff;
2. verify every path is `research/master/STATE.md` or a Master-authorized clue path;
3. verify the source revision is still coherent;
4. rerun the final adversarial gate;
5. remove unrelated formatting churn.

Use:

```text
research(master): <global research-state change>
```

Examples:

```text
research(master): isolate shared Weil bottleneck
research(master): narrow duplicate spectral branches
research(master): propose cross-line defect bootstrap
```

Do not commit merely to show the daily task ran.

## Notification and reporting

Routine snapshot refreshes may remain silent.

Notify only when the Master pass identifies one of these:

- a materially important new cross-line mechanism or common obstruction;
- a strong evidence-based `pause-candidate`, `merge-candidate`, or `split-candidate` recommendation;
- a genuinely distinct `new-line-candidate`;
- a global bottleneck whose resolution would affect several active lines;
- a review/finding withdrawal that materially changes the research program.

Report recommendations explicitly as recommendations, not mathematical facts.
