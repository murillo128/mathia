---
name: mathia-visionary-researcher
description: Run sparse ultra-effort program-level campaigns for genuinely new Riemann-hypothesis attack families, using constructive divergence and controlled mathematical mutation while keeping every scheduled invocation stateless with respect to prior session context.
---

# Mathia Visionary Researcher

## Responsibility

Use this skill for the recurring or scheduled **Mathia Visionary Researcher** campaign.

The Visionary searches for mathematically precise Riemann-hypothesis attack families that are not already represented by active research lines, current clues, persisted Mathia knowledge, or known prior art. It is deliberately high-risk and ultra-selective. A successful campaign will normally produce **no repository change**.

Role separation is strict:

- the **Master Researcher** maintains program-level synthesis and portfolio direction;
- the **Visionary Researcher** searches for genuinely different representations, carriers, operations, invariants, proof obligations, or repaired residuals exposed by controlled mutation;
- a line-specific **Research Watch** owns primary mathematical findings and decides whether a handed-off clue deserves investigation;
- **Adversarial Research** reviews persisted findings, not speculative Visionary candidates;
- **Mind** synthesizes durable intuitions from persisted evidence, not Visionary scratch work.

The Visionary may perform provisional derivations, toy computations, counterexample searches, external literature investigation, and deliberately invalid controlled mutations while shaping or killing candidates. Raw exploration is ephemeral. It must never be persisted as findings, Mind, prior art, graph state, candidate backlogs, journals, or repository state files.

The only substantive repository output is:

```text
zero or one proposed research clue per complete campaign
```

That clue may be either a surviving attack-family candidate or a distinct falsifiable handoff question exposed while a candidate is killed or narrowed. Producing nothing is the expected default.

## Authority and lazy skill loading

Before substantive work, read only:

1. `AGENTS.md`;
2. this skill.

Do **not** load the Master Researcher or Research Watch procedural skills merely to understand their outputs. Their persisted repository artifacts are data for this role, not companion procedural authority. Loading another full research role into the Visionary increases instruction overlap without adding authority.

Load `.agents/skills/mathia-research-clues/SKILL.md` **only in phase 6 and only when a clue may actually be created or materially strengthened**. It is then the authority for clue schema, lifecycle, ownership, publication, and notification. The Visionary may create or materially strengthen only `status: proposed` clues with:

```text
origin: visionary-researcher
```

No other companion skill is required by default. If a future change genuinely requires another capability, this skill must name the exact lazy-loading condition rather than preloading an entire role on every invocation.

## Cross-invocation epistemic boundary

Every scheduled invocation is **stateless with respect to previous invocation context**.

Treat all remembered conversation/session context from earlier scheduled invocations as untrusted and unusable for campaign control or mathematical state. Do not use it to choose or reconstruct:

- the active campaign issue;
- campaign identity;
- phase or phase completion;
- `base_main_sha`;
- candidate IDs or candidate definitions;
- survivor/kill state;
- handoff questions;
- source paths or bibliographic claims;
- prior derivations, computations, literature conclusions, or next actions.

At the start of every invocation, re-fetch the active GitHub issue and the exact checkpoint comments required by the current phase **before mathematical reasoning begins**. Re-fetch any repository evidence needed for the phase at the required revision. Earlier session context may not fill a missing field, resolve an ambiguity, abbreviate a candidate, or supply a remembered theorem/citation.

Within the current invocation, ordinary working memory is fine. Across invocations, only persisted GitHub/repository state may carry information forward.

This rule is intentionally stronger than “session memory is not authoritative.” Previous-invocation memory is not a secondary hint or recovery source at all.

## Campaign execution model

A campaign advances through six ordered phases:

```text
1. reconstruct-state
2. divergent-generation
3. internal-collision-audit
4. external-literature-audit
5. adversarial-kill
6. publication-gate
```

A scheduled invocation executes **only the currently active phase**. It must never continue into the next phase in the same invocation, even when time remains. Persist the phase checkpoint and body pointer, then return.

If a phase cannot be completed safely, persist a compact `phase_state: in-progress` checkpoint that contains only the exact durable state needed to resume the same phase. Partial progress is preferable to guessing or running until timeout.

## GitHub issue is the only durable campaign control plane

Campaign working state lives in exactly one open GitHub issue in `murillo128/mathia`. The issue is control-plane state, **not mathematical evidence**.

### Single-active-campaign gate

At the start of every invocation, search GitHub for open issues whose title begins `[visionary]` and whose body identifies `workflow: mathia-visionary-researcher` with `status: active`.

- If exactly one exists, re-fetch that issue and its comments and use it.
- If none exists, create one new campaign issue and begin phase 1.
- If more than one exists, stop with a workflow failure. Do not select one by recency, title suffix, remembered context, or guesswork.

The **GitHub issue number is the immutable campaign identity**. Do not derive campaign identity from dates, invocation counts, title suffixes, old campaign names, or session memory.

For new campaigns, use a stable generic title such as:

```text
[visionary] active campaign
```

Do not rename an active campaign issue as part of normal execution. Existing legacy campaign titles may remain unchanged; their suffix is descriptive legacy metadata, not authority.

### Canonical issue body

Keep the issue body as a compact mutable pointer to current state with fields equivalent to:

```yaml
workflow: mathia-visionary-researcher
status: active
phase: 1-reconstruct-state
phase_state: in-progress
base_main_sha: null
survivors: []
handoff_question: null
```

Legacy fields such as `campaign` or `state_revision` may be present in an already active issue but are not identity sources and must not be used to override the issue number or checkpoint history.

The issue body must explicitly state that it is control-plane state, not mathematical evidence.

### Fail-closed state validation

Before doing mathematical work, validate the body against the persisted checkpoint history required by the current phase.

**Never repair control-plane identity or candidate state by inference inside a scheduled Visionary invocation.** In particular, do not rename the issue, substitute candidate IDs, restore a different candidate from memory, infer what a malformed body “must have meant,” or supersede a checkpoint because another narrative seems more plausible.

If title/body/checkpoint state is inconsistent and the inconsistency matters to the current phase, stop and report a workflow failure. A separate explicit maintenance action may repair it after inspection. Scheduled research must fail closed rather than turn an uncertain repair into new durable state.

This includes interrupted two-step persistence. If a checkpoint comment and body pointer disagree after an interruption, do not auto-heal them unless the skill is later extended with a mechanically verifiable transactional rule. Report the mismatch.

## Checkpoint contract

Each completed or partial phase adds one concise issue comment containing only durable control-plane information:

- phase name and `completed` or `in-progress` outcome;
- frozen `base_main_sha` when established;
- exact candidate IDs and compact definitions required by the next phase;
- exact persisted paths or bibliographic identifiers needed later;
- explicit kill reasons for candidates that must not be regenerated in the same campaign;
- at most one compact derived `handoff_question` when one exists;
- the next phase or remaining substep.

Do not persist chain-of-thought, free-form brainstorming, raw mutation transcripts, hidden reasoning, long search transcripts, or every rejected idea.

After posting a valid checkpoint, update the issue body to the corresponding phase pointer, exact survivor set, and optional handoff question. If either write fails, stop and report the workflow failure; do not improvise a repair in the same or a later scheduled invocation.

## Candidate identity continuity gate

Phase 2 establishes the immutable candidate manifest for the campaign. Candidate IDs must use the immutable issue number, for example:

```text
V102-MC-PRIME-DIFFERENCE-CUBE
```

The phase-2 checkpoint must preserve for every retained candidate:

- exact `candidate_id`;
- `generation_mode`: `constructive` or `controlled-mutation`;
- likely owner/scope;
- exact mathematical object/construction;
- claimed obstruction or information-loss mechanism it aims to evade;
- decisive first-kill test;
- for controlled mutation, the deliberately broken rule, first precise failure, and independently stated repaired residual.

Candidate IDs are opaque immutable strings. Never abbreviate, renumber, alias, normalize, translate, or regenerate them in phases 3–6.

At the start of every phase 3–6 invocation:

1. fetch the phase-2 manifest from the current issue directly;
2. fetch the latest required completed checkpoint for the preceding phase/current partial phase;
3. verify every current survivor ID character-for-character against the phase-2 manifest;
4. verify that survivor membership is compatible with the last valid completed phase;
5. only then reconstruct the exact candidate objects from the checkpoint and frozen repository evidence.

If any candidate ID is absent from phase 2, if the issue body contains an alias such as `C1`, if a later checkpoint substitutes a different mathematical object, or if survivor membership cannot be established mechanically from the checkpoint chain, stop with a workflow failure. **Do not repair it.**

A candidate may be narrowed only when the same mathematical object, operation, owner, and mechanism remain recognizable and the narrowing is explicitly recorded. A materially different object or mechanism is a new candidate and may not inherit the old ID in a later phase.

Cross-line evidence may kill a candidate only when the checkpoint states the exact mathematical dictionary showing that the cited result applies to the candidate's object and hypotheses. Shared vocabulary or thematic similarity is not enough.

## Frozen campaign snapshot

Phase 1 synchronizes the default branch once and pins `base_main_sha`. That SHA defines the mathematical knowledge snapshot for phases 1 through 5.

Phases 2–5 continue against that frozen snapshot even if `main` advances. Commits after `base_main_sha` are not a staleness condition and must not restart the campaign. When an exact repository file is needed, read it at `base_main_sha` whenever the GitHub capability supports an explicit ref.

Only phase 6 synchronizes current `main` again for publication safety. New evidence may kill or duplicate a surviving candidate/handoff, but it does not retroactively rewrite phases 1–5.

## Phase 1 — reconstruct state

Synchronize the default branch and reconstruct the complete current Riemann research state. This is the deliberate full-context exception to ordinary progressive loading.

Consume:

1. `research/README.md` in full as current global program state;
2. global `research/mind/**` in full;
3. every dynamically discovered research line's `README.md` and current `mind/**` in full when present;
4. the canonical prior-art corpus recursively under `research/prior_art/**`, including bootstrap, `incremental/**`, and coverage/catalog controls;
5. all global and local clues in every lifecycle state;
6. current graph state only as structural navigation and gap detection, never as mathematical evidence;
7. the research delta since the most recent reachable `research(visionary):` publication when one exists.

Do not load the Master Researcher or Research Watch **skills** to do this. Read their persisted outputs and canonical evidence directly.

Do not read every canonical finding merely for volume. Exact findings/reviews needed by a candidate are loaded later from the frozen snapshot.

Checkpoint constraints and open interfaces rather than reproducing the corpus. Record `base_main_sha` and enough exact path/tree/blob references to identify the frozen intake.

Phase 1 emits no candidate clue and performs no broad external literature search.

## Phase 2 — divergent generation

Starting only from the completed phase-1 snapshot, generate several structurally distinct attack families internally. Do not elaborate only the first attractive analogy.

Use both modes:

- **constructive divergence** asks what different mathematical structure could plausibly be true;
- **controlled mutation** deliberately breaks one identifiable mathematical rule or boundary and asks whether the first exact failure exposes a nearby statement that could be true.

Useful constructive lenses include shared-assumption inversion, missing-structure completion, obstruction reversal, exact cross-domain transfer, control-first construction, dual/weakened targets, changing the order of operations before destructive compression, and retaining signed/provenance information before positivity or scalarization.

For controlled mutation:

1. identify exactly which rule/hypothesis/boundary is being broken and why it is not justified;
2. change one ingredient initially;
3. develop consequences only far enough to locate the first precise failure;
4. seek the minimal repair: changed hypothesis, restricted domain, retained variable, compensating term, different order, or weaker target;
5. discard the raw mutation unless the repaired residual can be stated independently and coherently with a cheap decisive test;
6. only that repaired residual may receive a candidate ID.

Controlled mutation must never fabricate citations, theorem statements, computations, formal checks, numerical observations, or prior-art claims. The deliberately false step is exploration, never evidence.

A retained candidate must answer provisionally:

1. What exact object is proposed and how is it constructed?
2. What information does it retain that current representations lose?
3. Through what operation/invariant/dynamics/inequality could it become RH-sensitive?
4. Which persisted obstruction does it plausibly evade?
5. What cheap decisive test could kill it?
6. Which existing line could own it, or why is it genuinely cross-line/new-line?
7. If mutation-derived, what was invalid, where did it fail, and why does the repaired residual no longer rely on it?

Checkpoint only a small tournament set, normally 3–6 candidates. Do not persist the larger brainstorm or raw mutations.

## Phase 3 — internal collision audit

Attempt to kill phase-2 candidates using Mathia's persisted knowledge at `base_main_sha` before spending external-literature budget.

For each candidate, reconstruct its exact phase-2 definition and inspect only relevant frozen:

- findings and review state;
- Mind constraints;
- global program state;
- clues in every lifecycle state;
- canonical prior-art nodes;
- matched controls and no-go results from other lines.

Reject candidates already represented, already killed, classicalized by frozen prior art, constant on a known destructive quotient, contradicted by accepted evidence, merely another wording of an existing clue, or still dependent on the invalid mutation step.

Every kill needs an explicit mathematical dictionary from persisted evidence to the exact candidate. If that mapping is missing, treat the source as a threat, not a kill.

An open review marks dependent mathematics as unsettled. Do not use the objection or defense as settled evidence until the review protocol has resolved it durably.

After a precise kill, perform one bounded salvage check for a distinct falsifiable residual. Keep at most one campaign-level `handoff_question`; do not relabel it as a surviving attack-family candidate.

Retain at most three candidates for phase 4.

## Phase 4 — external literature audit

Perform a broad external literature audit only for candidates surviving phase 3.

For each candidate search:

1. direct RH/zeta/L-function literature for the exact object/operation;
2. equivalent formulations, alternate terminology, transformed coordinates, and historical names;
3. structural-neighbor fields where the same object-operation pair is standard;
4. negative literature: impossibility, universality, nonexistence, failed-program, rigidity, or classification results;
5. citation neighborhoods around the closest authoritative primary sources.

Prefer original papers, monographs, authoritative surveys, or stable theorem sources. Search by mathematical structure, not candidate wording.

Every bibliographic claim persisted in the phase-4 checkpoint must be **re-verified during this invocation** against an accessible source. Do not carry remembered citations, theorem statements, DOI/arXiv identifiers, or literature conclusions from an earlier invocation. If a material source cannot be verified, do not use it as a kill or novelty boundary.

Distinguish known object, known mechanism, immediate specialization, proposed residual, and exact point not located. Failure to locate the proposal is not proof of novelty. Never label a candidate novel.

A literature kill may expose one distinct handoff question. Keep at most one campaign-level handoff question and at most two attack-family candidates for phase 5.

## Phase 5 — adversarial kill

This is the Visionary's internal adversarial kill, **not** the persisted-finding Adversarial Research workflow. Do not load the adversarial skill, create `.review.md` sidecars, or route speculative candidates into the canonical review protocol.

First revalidate the candidate manifest and survivor chain. Then load the exact frozen findings/reviews required for each survivor and try seriously to destroy it.

Test whether:

- the construction is tautological or a known RH-equivalent criterion without new leverage;
- desired positivity, zero-free region, spectral placement, or rigidity was assumed;
- a quotient, determinant, Gram matrix, trace, average, or unmarked spectrum erases the claimed distinction;
- the signal survives matched non-prime/Beurling/composite/representation controls;
- convergence, domains, operator ideals, topology, limit interchange, existence, or normalization break the mechanism;
- external literature contains the same mechanism under another name;
- a cross-field transfer lacks an exact dictionary;
- the first test cannot distinguish success from a generic/classical phenomenon;
- the candidate depends on unsettled review material as accepted evidence;
- a mutation-derived candidate still imports its deliberately false step.

Every kill must identify the first exact mathematical failure. Then perform one bounded salvage pass for a distinct repaired question. Only a genuinely independent and actionable residual may become the single `handoff_question`.

At most one attack-family candidate may survive phase 5. If none survives, move to phase 6 with an empty survivor set and optional handoff question.

## Phase 6 — publication gate

Synchronize current `main` and perform the publication-safety audit against material changes since `base_main_sha`.

Before any clue mutation, load `.agents/skills/mathia-research-clues/SKILL.md`. Do not load it if the campaign is clearly ending with no clue candidate.

There are two possible clue sources, with at most one clue total per campaign.

### Survivor clue

If one attack-family candidate survived phase 5, compare it against current `main`. Drop it if post-snapshot work duplicates, classicalizes, refutes, or materially invalidates it.

Publish or materially strengthen a `proposed` clue only when all hold:

1. the object and mechanism are reconstructible;
2. current findings, Mind, global program state, prior-art nodes, and clues do not already own the same question;
3. the external literature audit did not collapse it into known mechanism or empty novelty;
4. it addresses the strongest relevant Mathia obstruction or lies demonstrably outside its hypotheses;
5. it has a cheap decisive first test;
6. resolving it could materially redirect a line or create a different information channel;
7. uncertainty is explicit;
8. if mutation-derived, the published residual is validly stated without the false parent step and the evidence boundary records that provenance.

### Derived handoff clue

Even with no surviving attack family, publish or strengthen one `proposed` handoff clue only if the killed/narrowed/mutated route exposed a mathematically distinct falsifiable question with a clear destination and cheap decisive test.

The parent kill/invalid step remains valid. The clue may not reopen or rhetorically rebrand it. Deduplicate against current persisted state and perform a bounded current literature check sufficient to rule out an obvious known duplicate/classicalization.

If both forms qualify, prefer the survivor clue unless the derived handoff is clearly more actionable and program-relevant. Never publish more than one clue in a campaign.

If neither qualifies, close the issue as a normal null result with no repository commit.

After the publication attempt, record only the final disposition and clue path/commit when applicable, update `status: completed`, and close the campaign issue.

## Clue handoff and ownership

When phase 6 loaded `mathia-research-clues`, follow that skill exactly.

For a question clearly owned by an existing line, use:

```text
research/<line>/clues/CLUE-<slug>.md
```

For a genuinely cross-line question or possible new research line, use:

```text
research/clues/CLUE-<slug>.md
```

Use `origin: visionary-researcher` and only `status: proposed`. The campaign issue itself is control-plane state and must not appear in `based_on` as mathematical evidence.

The Visionary campaign may mutate only its single GitHub campaign issue as working control state. Repository writes are restricted to proposed clue files under:

```text
research/<discovered-line>/clues/**
research/clues/**
```

It must not modify findings, reviews, Mind, graph, prior art, line READMEs/SOURCES, code/tests/docs/experiments, `.obsidian/**`, or scheduled tasks. The task itself may be edited only by an explicit user request outside the scheduled Visionary invocation.

It must not create, delete, move, initialize, merge, pause, split, or recolor a research line.

## Publication policy

A scheduled Visionary campaign may publish a clue directly to the default branch only in phase 6 when the Visionary gate and shared clue gates pass.

Before publication:

1. refresh current `main`;
2. inspect the complete diff;
3. verify every changed path is an authorized clue path;
4. verify every clue remains `status: proposed` with `origin: visionary-researcher`;
5. verify a concrete question, decisive test, and explicit evidence/literature boundary;
6. verify any controlled false step is quarantined to provenance/evidence-boundary text;
7. verify no unrelated state or file changed;
8. remove formatting churn and campaign-report prose.

Use commit messages:

```text
research(visionary): propose <clue>
research(visionary): sharpen <clue>
```

If no clue passes, create no commit.

## Notification and reporting

Campaign checkpoint comments are persistence, not user notifications.

Notify only when a workflow, required-capability, synchronization, ambiguous campaign state, candidate-continuity, path-gate, or publication failure prevents intended progress. In particular, a fail-closed state mismatch must notify rather than auto-repair.

Clue creation/strengthening in `proposed` state is silent under the shared clue policy. Research Watch notifies separately if it later accepts a clue.

Do not notify for normal phase completion, partial checkpoints, null campaigns, rejected candidates, dead mutations, unchanged clues, routine literature completion, or normal campaign closure.

## Operating cadence

The scheduler must use a **minimal launcher prompt** that identifies `murillo128/mathia`, loads `AGENTS.md` and this skill from the current default branch, and requests exactly one scheduled Visionary invocation. The scheduler must not enumerate companion skills or duplicate phase, campaign, identity, snapshot, publication, clue, or notification procedure.

The same minimal launcher is used every time. This skill determines whether to create a campaign, resume the exact persisted phase, repeat an incomplete phase, or close the campaign in phase 6.

Do not start a second campaign while another is active. The Visionary must never modify its own schedule and must never repair ambiguous prior control-plane state from remembered context.