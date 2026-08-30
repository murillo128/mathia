---
name: mathia-research-line-bootstrap
description: Create and activate a new Mathia Research Watch line by defining its canonical README, unique line identity and finding prefix, and scheduled Research Watch task without duplicating scientific or workflow contracts.
---

# Mathia Research Line Bootstrap

## Responsibility

Use this skill for the **one-shot creation or activation of a new recurring mathematical research line** under:

```text
research/<line>/
```

The bootstrap owns only the transition from an explicitly authorized research idea to a valid Research Watch line:

1. decide the stable line slug and finding prefix;
2. verify that the proposed mandate is not already owned by another line;
3. create the canonical `research/<line>/README.md` scientific contract;
4. publish that README through the repository-authorized Git path;
5. create or repair the corresponding scheduled Research Watch task once the README is visible on the default branch;
6. verify that the line is discoverable and not duplicated.

This skill does **not** perform the line's mathematical research, create initial findings, synthesize `mind/`, curate graph state, modify Master Researcher state, or perform adversarial review.

Every bootstrap must also load:

```text
.agents/skills/mathia-research-watch/SKILL.md
.agents/skills/codex-github-operations/SKILL.md
```

`mathia-research-watch` is the authority for the canonical line README contract and for the recurring research procedure that the new task will later execute. `codex-github-operations` is the authority for Git/GitHub publication mechanics.

## Authorization gate

Creating a research line is a portfolio-level action. Run this skill only when the user has **explicitly asked to create or activate the line**.

A Master Researcher recommendation, Visionary clue, local clue, graph cluster, promising finding, or assistant suggestion may justify proposing a line, but none of them authorizes creation on its own.

Do not let a scheduled actor invoke this skill autonomously.

Repository publication still follows `AGENTS.md`. In particular, this skill does not manufacture direct-default-branch authority. If the user has not authorized a publication mode that puts the README on the default branch immediately, publish through the normal branch/PR route and **do not create the scheduler yet**. The Research Watch task is activated only after the canonical README is actually visible on the default branch.

## Task-specific inputs

A bootstrap needs a sufficiently concrete scientific idea plus, when supplied by the user, any preferred operational choices:

- human-readable line title;
- durable mathematical object/question the line should own;
- optional preferred repository slug;
- optional stable finding prefix;
- optional scheduler cadence or timing mode;
- optional notification override stricter than the Research Watch defaults.

Do not ask for mechanically derivable identity fields when the mathematics is already clear. Derive them deterministically and report what was chosen.

If the scientific mandate itself is too vague to distinguish the new line from existing lines, stop rather than inventing a research program from a name alone.

## Stable identity

### Line slug

Use a short lower-case snake-case slug:

```text
^[a-z][a-z0-9_]*$
```

Prefer a semantic name that will still make sense if the first attack route fails. Do not encode dates, issue numbers, temporary hypotheses, or version suffixes into the line name.

Examples:

```text
prime_circle
weil_positivity
arithmetic_fidelity
```

Before publication, verify that `research/<line>/` is not already an active Research Watch line and that no neighboring path would make the new name materially ambiguous.

### Finding prefix

Choose a compact upper-case stable prefix, normally 2-4 letters, for canonical finding IDs:

```text
PC
PF
PL
WP
WI
AF
```

The prefix must be unique across current Research Watch lines. Prefer a natural initialism. If the obvious initialism collides, extend it deterministically rather than silently sharing a prefix.

Once findings have been published, do not rename the line or prefix casually; both are durable research identity.

## Discovery and admission check

Before writing anything:

1. read `AGENTS.md`;
2. read this skill, `mathia-research-watch`, and `codex-github-operations`;
3. dynamically inventory current `research/*/README.md` files that satisfy the Research Watch README contract;
4. read the existing line READMEs closely enough to understand their primary objects, objectives, exclusions, and relationships;
5. inspect `research/master/STATE.md` only when it materially helps distinguish overlap or a proposed cross-line role;
6. inspect the current scheduled tasks so that a stale or duplicate watch is not created;
7. confirm that the intended scheduler capability is available before publishing an immediately active line.

A new line passes the admission check only when:

- it owns a durable mathematical object, transformation class, obstruction, or question that can be stated independently of one transient idea;
- its objective is meaningfully distinct from the owner question of every existing line;
- it has concrete priority questions that can produce falsifiable mathematical claims;
- it has line-specific controls or failure modes beyond the generic Research Watch discipline;
- its relationship to neighboring lines can be stated without pretending that one line's README is evidence for another;
- it is not merely a renamed duplicate, an implementation queue, a collection of clues, or a temporary subproblem better owned by an existing line.

A cross-cutting line is valid when the **cross-line mechanism itself** is the primary mathematical object. Shared inputs or applications do not make two lines duplicates if their owner questions are genuinely different.

If an existing line already honestly owns the proposed question, do not create another line. Report the overlap and prefer a separately authorized reorientation of the existing mandate when appropriate.

## Prior-art orientation before bootstrap

Run only enough prior-art orientation to prevent a blatantly redundant or misnamed mandate and to identify the mathematical domains the README should audit.

This is not the line's full novelty review. The recurring Research Watch will perform serious candidate-specific literature checks once precise findings exist.

Before bootstrap, determine at least:

- the closest established mathematical languages for the primary object;
- whether the proposed whole program is already a standard named theory;
- which literatures are particularly relevant to the line;
- whether obvious prior art requires narrowing the objective or changing terminology.

Do not claim novelty in the README merely because the exact Mathia framing was not found.

## Canonical README construction

Create exactly:

```text
research/<line>/README.md
```

The H1 is the human-readable line title. The file must contain exactly one:

```text
## Research mandate
```

and exactly these line-specific subsections in this order:

```text
### Primary object
### Objective
### Priority questions
### Scope and exclusions
### Line-specific falsification controls
### Prior-art domains
### Relationship to other lines
```

Follow the semantic contract from `mathia-research-watch`.

### Primary object

Define the intrinsic mathematical object, transformation class, structures, conventions, or fixed data needed to understand what the line studies.

Do not put current findings or a historical narrative here.

### Objective

State the durable scientific question. It should survive several failed approaches without needing a README rewrite.

Separate the desired explanatory mechanism from superficial reformulations that would not count as success.

### Priority questions

List concrete mechanisms, invariants, obstructions, equivalences, extremal questions, or theorem surfaces worth attacking.

These are priorities, not a sequential roadmap or TODO list.

### Scope and exclusions

State mathematical boundaries peculiar to this line. Explicitly exclude nearby reformulations that would create false progress or duplicate another line.

### Line-specific falsification controls

Name the matched objects, degeneracies, collapse modes, alternative models, or no-go tests that are especially diagnostic for this line.

Do not copy generic Research Watch adversarial procedure into this section.

### Prior-art domains

List only literatures particularly relevant to this line. This is an audit surface, not a bibliography and not a novelty claim.

### Relationship to other lines

Describe genuine upstream/downstream, complementary, supplying, consuming, or cross-cutting mathematical relationships.

Do not hard-code workflow dependencies that are already handled by dynamic discovery.

## README hygiene

The README contains the **scientific contract only**. Do not duplicate shared procedure already owned by `mathia-research-watch`, including:

- evidence labels or finding file format;
- derive-before-interpret discipline;
- generic prior-art or novelty procedure;
- generic matched-control discipline;
- review sidecar protocol;
- clue lifecycle;
- publication gates;
- notification policy;
- file maps or research history;
- current finding summaries;
- current portfolio recommendations.

A sentence that could be copied unchanged into several lines probably belongs in a shared skill, not the README.

## Repository footprint

Bootstrapping a line normally creates **only**:

```text
research/<line>/README.md
```

Do not create empty `findings/`, `clues/`, `mind/`, `graph/`, `SOURCES.md`, indexes, or placeholder files. Those artifacts are created later by the owning procedures only when warranted.

Do not modify `research/master/STATE.md`, graph state, other line READMEs, findings, or clues merely to register the line. Master, Mind, Graph Curator, and Adversary must discover valid lines dynamically.

## Publication order and atomicity

An enabled scheduler must never point at a scientific contract that exists only in chat, on an unmerged branch, or in a pending PR.

Use this order:

1. finish all identity, overlap, README, and scheduler preflight checks;
2. publish the README using the publication mode authorized by `AGENTS.md` and the user;
3. verify the exact README is visible on the default branch;
4. create or repair the scheduled task;
5. verify the task is enabled and targets the exact line/prefix/README;
6. report the completed bootstrap.

If publication requires a PR, stop after the ready-for-review handoff. Report that scheduler activation is intentionally pending until the README lands on the default branch. Do not schedule a task against the feature branch.

If a directly published **brand-new** README succeeds but task creation then fails, restore a coherent portfolio state. When the line did not previously exist and no other actor has added files under it, delete the just-created README again and report the scheduler/bootstrap failure. Do not leave a newly discoverable active line with no intended watch merely because the second control-plane operation failed.

Never roll back or delete a pre-existing line to repair scheduler failure.

## Scheduled Research Watch contract

Once the README is on the default branch, create one scheduled task for the line unless an equivalent task already exists.

If the user supplied no cadence, use the current Mathia baseline:

```text
RRULE:FREQ=HOURLY
```

with `exact_schedule` timing.

A user-specified cadence or stricter notification policy overrides that default.

Use a concise task title, normally:

```text
<Human line title> Research Watch
```

The task prompt must remain operational and must **not duplicate the scientific mandate**. Use this canonical shape, substituting only the line and stable prefix plus any explicit stricter runtime override:

```text
In GitHub repository `murillo128/mathia`, read `AGENTS.md` and `.agents/skills/mathia-research-watch/SKILL.md`. Follow `mathia-research-watch` as the procedural authority for the entire recurring research workflow, including any required companion review/clue procedures, novelty audit, evidence persistence, finding IDs, path ownership, publication gates, and no-churn behavior.

Research line: `<line>`.
Stable finding prefix: `<PREFIX>`.

Read `research/<line>/README.md` as the canonical research contract for this line: its mathematical object, objective, scope, priorities, exclusions, prior-art audit surface, and relationship to other research lines. Do not substitute remembered scheduler text for the current README and do not silently redefine the `## Research mandate` during routine research. If the canonical mandate is missing or materially ambiguous, treat that as a workflow failure rather than inventing a new objective.

Notification override: run silently for every successful outcome, including ordinary or extraordinary findings, dead ends, clue changes, adversarial-review events, corrections, commits, and unchanged runs. Notify me only when a workflow/publication error, conflict, missing required capability, path/publication-gate failure, or other execution failure prevents intended work from being completed or persisted correctly.
```

Do not paste the README objective, priority questions, prior-art list, or current findings into the scheduler prompt. The README must remain the sole scientific contract.

## Scheduler deduplication and repair

Before creating a task, inspect current tasks for an existing watch whose prompt identifies the same:

```text
Research line: `<line>`
```

If exactly one equivalent task exists, repair/update it instead of creating a duplicate when the intended identity is unambiguous.

If multiple active tasks claim the same line, do not create another. Resolve the duplicate control-plane state first and preserve the single intended watch.

After creation or repair, verify:

- the task is enabled;
- the prompt names the exact line and prefix;
- it reads the canonical README;
- it delegates procedure to `mathia-research-watch`;
- it does not redefine the scientific objective;
- the cadence and timing mode match the user's request or the default;
- no second active watch owns the same line.

## What not to do during bootstrap

Do not:

- create an initial finding merely to make the directory look populated;
- invent evidence for the new mandate;
- copy conclusions from another line as though they are established here;
- modify Master state to force recognition;
- manually add the line to Mind, Graph Curator, or Adversary hard-coded lists;
- create a scheduler before the README is on the default branch;
- create multiple tasks for different subquestions inside the same line;
- encode the current objective in both README and scheduler;
- treat task creation as mathematical evidence or a research success.

## Completion report

A fully activated bootstrap reports only the useful control-plane facts:

- new line title and path;
- stable finding prefix;
- README publication target/commit;
- scheduled task title and cadence;
- whether activation was fully verified.

If the README is only in a PR, report the PR/handoff and state clearly that scheduler creation is intentionally deferred until merge.

If any step failed, report the exact partial state and whether it was rolled back. Never claim a task or repository mutation that was not observed.