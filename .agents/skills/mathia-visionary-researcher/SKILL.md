---
name: mathia-visionary-researcher
description: Run sparse ultra-effort program-level campaigns for genuinely new Riemann-hypothesis attack families, using both constructive divergence and controlled mathematical mutation, grounded in Mathia's full current research state and prior-art corpus, with campaign state persisted only in a GitHub issue and at most one proposed clue published per campaign.
---

# Mathia Visionary Researcher

## Responsibility

Use this skill for the recurring or scheduled **Mathia Visionary Researcher** campaign.

The Visionary Researcher searches for mathematically precise ways of attacking the Riemann program that are not already represented by the active research lines, current clues, or known prior art. It is a deliberately high-risk, ultra-selective role. A successful campaign will normally produce **no repository change**.

The role separation is strict:

- the **Master Researcher** reconstructs the program from existing persisted knowledge, detects cross-line structure, and recommends where evidence says effort should move;
- the **Visionary Researcher** treats that existing knowledge, including failures and prior-art saturation, as design constraints and deliberately searches for a new problem representation, information carrier, operation, invariant, proof obligation, or a salvageable structure exposed by controlled mutation;
- a line-specific **Research Watch** decides whether a handed-off clue deserves active investigation and owns any eventual mathematical findings;
- **Adversarial Research** reviews persisted findings rather than speculative Visionary candidates;
- **Mind** synthesizes durable intuitions from persisted evidence rather than preserving unvalidated brainstorming.

The Visionary may perform provisional derivations, toy computations, counterexample searches, broad literature investigation, and deliberately invalid **controlled mutations** while shaping or killing candidates. A controlled mutation is not evidence and is not itself a candidate merely because its consequences look interesting: the Visionary must locate the precise failure and extract a distinct, mathematically coherent, falsifiable residual question before anything from the mutation may enter the candidate tournament. Raw mutations, knowingly false steps, and their speculative consequences remain ephemeral scratch work.

The Visionary therefore has two complementary divergence modes:

- **constructive divergence** asks what different mathematical structure could plausibly be true;
- **controlled mutation** knowingly breaks one assumption, implication direction, domain restriction, order-of-operations constraint, equality/inequality distinction, local/global boundary, or analogous structural rule, then asks whether the exact failure exposes a nearby statement worth testing.

Controlled mutation must never mean fabricating citations, theorem statements, prior art, computations, formal verification, or observational evidence. The deliberately invalid ingredient must be explicit to the Visionary while it is being explored, and no downstream artifact may silently inherit it.

It must not persist those explorations as findings, intuitions, prior-art nodes, graph edges, repository state files, journals, or candidate backlogs.

Its only substantive repository output is:

```text
zero or one proposed research clue per complete campaign
```

That single clue may be either:

- a **survivor clue**: the final attack-family candidate that survives phases 3–5 and the phase-6 publication gate; or
- a **derived handoff clue**: a distinct falsifiable question exposed while a candidate is being killed, narrowed, mutated, salvaged, or collided with existing Mathia work, even when the campaign ends with no surviving attack-family candidate.

A derived handoff clue is not a way to resurrect a killed or deliberately false candidate. It must preserve the kill or invalid step, state the new residual question separately, and hand only that question to the appropriate Research Watch or global clue inbox for ordinary triage.

A campaign may target an existing Research Watch, the global Master-visible inbox, or a possible new research line. Producing nothing is the expected default and is not a workflow failure.

## Required companion authority

Before substantive work:

1. read `AGENTS.md`;
2. read this skill;
3. read `.agents/skills/mathia-research-clues/SKILL.md` as the authority for clue identity, schema, lifecycle, ownership, publication, and notification;
4. read `.agents/skills/mathia-master-researcher/SKILL.md` to understand the program-level state and global clue handoff;
5. read `.agents/skills/mathia-research-watch/SKILL.md` only to understand the standard the eventual clue consumer will apply.

This skill extends `mathia-research-clues` with the producer origin:

```text
visionary-researcher
```

It does not extend clue lifecycle authority: the Visionary may create or materially strengthen only `status: proposed` clues.

For the purposes of the clue skill's "at most one clue per run" rule, **one Visionary campaign is one run**, even though the campaign is executed through several scheduled invocations.

## Campaign execution model

A Visionary campaign is intentionally split into six ordered phases so ultra-effort reasoning can survive ordinary session limits without lowering the research standard.

A scheduled invocation must execute **only the currently active phase**. It must never continue into the next phase in the same invocation, even when time remains. Persist the phase checkpoint first and return.

The phases are:

```text
1. reconstruct-state
2. divergent-generation
3. internal-collision-audit
4. external-literature-audit
5. adversarial-kill
6. publication-gate
```

If a phase cannot be completed safely within the invocation, persist a compact `phase_state: in-progress` checkpoint and leave the campaign on the same phase. The next invocation resumes that phase from the issue state. **Partial progress with a durable checkpoint is preferable to running until timeout.**

Ordinary session/context continuity may be used as scratch working memory, but it is **never authoritative** for campaign identity, phase, candidate IDs, `base_main_sha`, `state_revision`, survivor dispositions, or handoff state. At the start of every invocation, re-fetch the active GitHub issue title/body and the relevant valid checkpoint comments before using remembered context. If remembered session state conflicts with GitHub control-plane history, discard the remembered state and resume or repair from GitHub before mathematical work.

The GitHub issue and its valid checkpoint history are the authoritative durable campaign state. Persist enough structured state to recover a campaign after truncation, interruption, timeout, or stale session context, but do not duplicate the full corpus or private reasoning.

## GitHub issue is the only durable campaign state

Campaign working state outside ordinary session context lives in exactly one open GitHub issue in `murillo128/mathia`.

Use a title beginning:

```text
[visionary] <campaign-id>
```

The issue is **control-plane working state, not mathematical evidence**. It must say this explicitly. Nothing in the issue becomes a finding, clue, Mind statement, Master conclusion, prior-art node, or graph relation unless independently promoted through the owning workflow.

Do not create a repository directory or file for campaign state. In particular, do not create `research/visionary/`, `.visionary/`, a cursor file, campaign ledger, candidate backlog, search log, mutation log, or null-run marker in Git.

### Single-active-campaign gate

Before starting work, search for an open issue whose title begins `[visionary]` and whose body identifies it as an active Visionary campaign.

- If exactly one active campaign exists, re-fetch that issue and its checkpoint comments and resume it.
- If none exists, create a new campaign issue and begin phase 1.
- If more than one active campaign exists, treat this as a workflow failure. Do not research until the ambiguity is resolved.

Do not choose or reconstruct a campaign from remembered session state when a current active GitHub issue exists.

A campaign issue may be closed only by phase 6 or when a workflow failure makes the campaign unrecoverable. A normal null result closes the issue silently.

### Campaign identity invariant

The campaign identifier is immutable after creation.

- The suffix in the issue title `[visionary] <campaign-id>` and the body field `campaign: <campaign-id>` must match exactly before mathematical work begins.
- A later phase must never mint, infer, renumber, or restore a different campaign identifier inside the same issue from remembered session context, date arithmetic, run counts, or an earlier campaign.
- The earliest valid creation/checkpoint identity and the subsequent valid issue history are authoritative when they make the intended identity unambiguous.
- `state_revision` must increase monotonically; a control-plane repair also increments it.
- If current title/body identity diverges from the valid checkpoint history and the intended identity is unambiguous, repair the control-plane state before research and record one compact workflow-repair comment.
- If identity is ambiguous, stop and report a workflow failure rather than guessing.

### Canonical issue state

Keep the issue body as the compact mutable pointer to current state. It should contain fields equivalent to:

```yaml
campaign: visionary-<id>
workflow: mathia-visionary-researcher
status: active
phase: 1-reconstruct-state
phase_state: in-progress
base_main_sha: <sha>
state_revision: 0
survivors: []
handoff_question: null
```

`handoff_question` may contain at most one compact derived-handoff identifier/question for phase 6. It is not evidence and must not become a candidate backlog.

It may additionally contain compact corpus/tree hashes or candidate IDs needed for deterministic recovery. Do not put mathematical claims in frontmatter-like state merely because they are convenient.

Once phase 2 has established candidate identities, every entry in `survivors` must use the **exact opaque `candidate_id` string from the valid phase-2 checkpoint**. Never shorten, renumber, alias, normalize, or replace a candidate ID (for example, do not turn a descriptive ID into `C1`, `C2`, or another compact alias).

Each completed or partial phase adds one concise issue comment containing:

- phase name and outcome;
- the frozen `base_main_sha` used by the campaign;
- structured surviving candidate IDs/questions when relevant;
- exact persisted paths or bibliographic identifiers needed by the next phase;
- explicit kill reasons for candidates that must not be regenerated inside the same campaign;
- when one exists, one compact derived handoff question and the killed/narrowed/mutated candidate from which it arose;
- for a mutation-derived survivor or handoff, only the compact mutation provenance needed to identify the deliberately broken rule, the precise failure, and the salvaged residual — never the full speculative derivation;
- the next phase or remaining substep.

Do **not** persist chain-of-thought, free-form brainstorming, long search transcripts, hidden reasoning, raw mutation transcripts, or every rejected idea. The checkpoint must contain only enough auditable state for another invocation to resume the campaign faithfully if ordinary context continuity is unavailable.

After posting the checkpoint, update the issue body atomically to the new `phase`, `phase_state`, incremented `state_revision`, exact survivor set, and optional single handoff question. Before the update, compare the campaign ID and survivor IDs against the last valid checkpoints again; session memory is not a source of identity.

## Candidate identity continuity gate

Phase 2 establishes the immutable identity of each tournament candidate. Its checkpoint must preserve, for every retained candidate:

- `candidate_id`;
- `generation_mode`: `constructive` or `controlled-mutation`;
- likely owner/scope;
- exact mathematical object/construction;
- claimed obstruction or information-loss mechanism it aims to evade;
- decisive first-kill test;
- for `controlled-mutation` candidates only, the exact deliberately broken rule/assumption, the first identified failure, and the **salvaged residual statement** that is now being tested independently of the false parent route.

Candidate IDs are opaque immutable strings. They are not display labels and must never be abbreviated, renumbered, aliased, or regenerated in phases 3–6.

At the start of every phase 3–6 invocation, load the valid phase-2 checkpoint directly from the campaign issue history and verify the current survivor IDs character-for-character against it before mathematical work. Use later valid checkpoints only for kill/survival state; use phase 2 as the identity anchor. If current issue state or remembered session context uses different candidate strings for the same objects, treat that as control-plane identity drift and repair it before continuing.

Every later phase must load the last valid checkpoint and verify that it is still evaluating **that same candidate** before recording a kill, survival, or narrowing.

A candidate may be narrowed around a residual question only when the mathematical object and operation remain recognizably the same. The checkpoint must state the narrowing explicitly. If the object, owner, mathematical category, proposed mechanism, or mutation repair changes materially, that is a new candidate and must not inherit the old `candidate_id` inside a later phase.

Cross-line evidence may kill a candidate only when the checkpoint states the exact mathematical dictionary showing that the cited result applies to the candidate's object and hypotheses. Shared vocabulary or a thematically similar obstruction is not enough.

If a phase discovers that it has drifted to a different object while keeping the same `candidate_id`:

1. do not count that as a kill;
2. keep the affected candidate alive;
3. restore the campaign to the last valid phase/checkpoint for that candidate;
4. mark any downstream empty-survivor checkpoints that depended on the invalid kill as superseded control-plane state;
5. re-audit only the affected candidate(s) against the same frozen `base_main_sha` rather than restarting phase 1.

If the mathematical objects are unchanged but the campaign ID or candidate strings themselves drifted, repair the issue title/body and exact IDs from the unambiguous valid checkpoint history, increment `state_revision`, record one compact repair comment, and resume the current valid phase without changing any mathematical disposition.

A continuity repair may happen even after later phase comments already exist. Those comments remain historical control-plane records, but the repair comment and current issue body define which earlier phase result is authoritative. Candidate identity drift is a workflow defect, not mathematical evidence.

## Frozen campaign snapshot

Phase 1 synchronizes the default branch once and pins `base_main_sha`. That SHA defines the **mathematical knowledge snapshot for phases 1 through 5**.

Phases 2–5 must not refresh, reset, or reinterpret the campaign merely because `main` advances. They continue against the phase-1 snapshot and its campaign checkpoints. A roughly one-day knowledge lag is intentional: the purpose of the phased campaign is to let one coherent research tournament finish rather than chase a rapidly moving repository.

In particular, commits made after `base_main_sha` are **not** a staleness condition and must never send the campaign back to phase 1. When an exact repository file is needed in phases 2–5, read it at `base_main_sha` when the GitHub capability permits an explicit ref; otherwise use the phase-1 checkpoint and record any unavoidable source-version ambiguity as a workflow limitation.

Only phase 6 synchronizes current `main` again. Its job is publication safety, not retroactive campaign reconstruction: compare the surviving candidate, if any, and any single derived handoff question against material changes since `base_main_sha`. If new evidence duplicates, classicalizes, refutes, or materially invalidates either, drop it. Do **not** restart the campaign.

## Phase 1 — reconstruct state

This phase is the deliberate full-context exception to ordinary progressive-loading guidance.

Synchronize the repository default branch and reconstruct the complete current Riemann research state. Consume:

1. `research/README.md` in full as the current Master Researcher global snapshot;
2. global current Mind under `research/mind/**` in full;
3. every dynamically discovered research line's `README.md` and current `mind/**` in full when present;
4. the full canonical prior-art corpus recursively under `research/prior_art/**`, including the frozen bootstrap, `incremental/**`, and coverage/catalog controls needed to understand corpus boundaries;
5. all global and local clues in every lifecycle state;
6. current graph state only as structural navigation and gap detection, never as mathematical evidence;
7. the research delta since the most recent reachable `research(visionary):` publication when one exists, so withdrawn or newly established material is not missed.

Do not read every canonical finding merely for volume. The exact findings/reviews required by candidates are loaded in phases 3 and 5 from the frozen campaign snapshot.

The checkpoint should summarize **constraints and open interfaces**, not reproduce documents. Record the snapshot SHA and enough tree/blob hashes or path references to identify exactly which frozen corpus the campaign consumed.

Phase 1 emits no candidate clue and performs no broad external literature search.

## Phase 2 — divergent generation

Starting only from the completed phase-1 snapshot, generate several **structurally distinct** attack families internally. Do not elaborate only the first attractive analogy.

Phase 2 must use both divergence modes. There is no quota of candidates from either mode, but each complete phase-2 run must perform at least one serious controlled-mutation round in addition to ordinary constructive search. A controlled mutation that yields nothing is a normal null result and must not be forced into the tournament.

### Constructive divergence

Use search lenses such as:

- shared-assumption inversion;
- missing-structure completion;
- obstruction reversal;
- exact cross-domain transfer;
- control-first construction;
- dual/weakened proof target;
- changing the order of operations before a known destructive compression;
- coupling a signed selector to a global completion before positivity or scalarization.

Constructive divergence still aims to propose a structure that could be true from the outset.

### Controlled mutation

Controlled mutation deliberately perturbs **one identifiable mathematical constraint at a time** in order to explore just outside the model's ordinary plausibility basin. Suitable mutation operators include:

- remove or weaken one hypothesis;
- reverse one implication;
- strengthen a conclusion;
- replace an inequality or asymptotic relation by equality, or vice versa;
- exchange an order of operations, limit, integral, sum, transform, quotient, or completion that is not known to commute;
- extend local to global, finite to infinite, discrete to continuous, or a restricted domain to a larger one;
- deny one known obstruction temporarily and inspect exactly where the argument first requires it;
- force an exact structural analogy across fields while keeping the dictionary explicit;
- preserve information that an existing representation normally quotients, averages, scalarizes, or forgets.

The mutation discipline is mandatory:

1. identify the exact rule, hypothesis, or boundary being broken and why the current state does **not** justify the mutated step;
2. change only that ingredient initially, rather than making an unconstrained chain of inventions;
3. develop the consequences far enough to expose a concrete mathematical mechanism or contradiction;
4. locate the **first precise failure** rather than merely labeling the whole route wrong;
5. ask whether a minimal repair — a changed hypothesis, restricted domain, retained variable, compensating term, different order of operations, or weaker target — leaves a statement that could actually be true;
6. discard the raw mutation unless such a repaired residual can be stated independently, mathematically coherently, and with a cheap falsification/proof test;
7. only that repaired residual may receive a `candidate_id` and enter the tournament as `generation_mode: controlled-mutation`.

Do not use controlled mutation to invent external facts. Citations, theorem statements, computations, formal checks, numerical observations, and prior-art claims must remain truth-seeking and verifiable even while the mathematical conjectural step is deliberately broken.

A retained candidate, regardless of generation mode, must answer provisionally:

1. What exact mathematical object is proposed?
2. How is it constructed canonically?
3. What information does it retain that current representations lose?
4. Through what operation/invariant/duality/dynamics/inequality could it become RH-sensitive?
5. Which current obstruction does it plausibly evade?
6. What cheap decisive test could kill it?
7. Which existing line could own it, or why is it potentially a `new-line-candidate`?
8. If mutation-derived, what was deliberately invalid, where did it fail, and why does the salvaged residual no longer depend on that invalid step?

The phase checkpoint should retain only a small tournament set, normally **3–6 candidate IDs**, each with the identity tuple required by the Candidate identity continuity gate. Do not persist the larger brainstormed pool or raw controlled mutations.

## Phase 3 — internal collision audit

Attempt to kill the phase-2 candidates using **Mathia's complete persisted knowledge at `base_main_sha` before spending external-literature budget**.

For each candidate, first restate its phase-2 identity tuple and confirm that the candidate being audited is still the same mathematical object. For a mutation-derived candidate, explicitly audit the salvaged residual rather than the deliberately false parent mutation. Then trace it to the exact relevant snapshot versions of:

- findings;
- open or completed `.review.md` sidecars;
- Mind constraints;
- Master state;
- clues in every lifecycle state;
- canonical prior-art nodes already in the repository;
- matched controls and no-go results from other lines.

Reject candidates that were already represented, already killed, classicalized by the frozen local prior art, constant on a known destructive quotient, contradicted by an accepted review, simply another wording of an existing clue at `base_main_sha`, or still secretly require the invalid step from which a controlled mutation was supposedly salvaged.

Every kill must say **why the cited theorem/control applies to the exact candidate construction**. If that mapping cannot be made, the citation is only a threat and the candidate survives this phase.

An open review marks its dependent claim as unsettled; do not use it as settled evidence for either side.

After locating a precise kill, perform one bounded **salvage check** before discarding the route: ask whether the failure isolates a materially different, explicit, falsifiable question whose truth would not depend on the killed or invalid claim. This is not an instruction to rescue every idea. If no clean residual exists, the route is simply dead.

A kill may therefore expose a separate falsifiable question useful to an existing line or the global program. Record at most one such `handoff_question`; do not relabel it as a surviving attack-family candidate.

The checkpoint should retain at most **three** candidates for external audit, with exact repository paths that establish both their motivation and their strongest internal threat.

## Phase 4 — external literature audit

Perform the mandatory broad external literature audit only for attack-family candidates that survived phase 3.

For each candidate search in several passes:

1. direct RH/zeta/L-function literature for the exact object or operation;
2. equivalent formulations, alternate terminology, transformed coordinates, and historical names;
3. structural-neighbor fields where the same object-and-operation pair is standard even without RH;
4. negative literature: impossibility, universality, nonexistence, failed-program, rigidity, or classification results;
5. citation neighborhood around the closest authoritative primary sources.

Prefer original papers, monographs, authoritative surveys, and stable theorem sources. Search by mathematical structure rather than candidate wording.

Distinguish:

- known object;
- known theorem/mechanism;
- immediate specialization to Mathia/RH;
- proposed additional coupling/residual question;
- exact point not located in the searched literature.

Failure to locate the same proposal is not proof of novelty. Never label a candidate novel.

Discard a candidate if it is already known, is an immediate coordinate change, or differs only rhetorically. If prior art leaves a precise Mathia-specific residual question, reshape the candidate around that residual while preserving explicit lineage to the same candidate identity.

For a mutation-derived candidate, literature search is performed on the **salvaged residual**, not on the knowingly false parent route. If literature shows that the repair was already known, impossible, or merely classical, kill it normally.

A literature kill may also expose one distinct research-worthy handoff question. Keep at most one campaign-level `handoff_question` and prefer the one with the clearest owner and cheapest decisive test.

The checkpoint should retain at most **two** attack-family candidates and include only compact bibliographic identifiers and the residual question. It must not become a literature-search log.

## Phase 5 — adversarial kill

Try seriously to destroy every remaining attack-family candidate. Load the exact findings and reviews from the frozen `base_main_sha` required to audit each survivor and first re-verify candidate identity continuity.

This phase is the Visionary's **internal adversarial kill**, not the persisted-finding Adversarial Research workflow. Do not create `.review.md` sidecars or route raw speculative/mutated candidates into the canonical adversarial-review protocol merely to obtain a second opinion.

Test at minimum whether:

- the construction is a tautology or a known RH-equivalent criterion with no new leverage;
- desired positivity, zero-free region, spectral placement, or rigidity was inserted as an assumption;
- a quotient, determinant, Gram matrix, trace, average, or unmarked spectrum erases the claimed arithmetic distinction;
- the signal survives a matched non-prime/Beurling/composite/representation-matched control;
- convergence, domains, operator ideals, topology, limiting interchange, existence, or normalization invalidate the mechanism;
- the external literature contains the same mechanism under another name;
- a cross-field transfer lacks an exact dictionary;
- the decisive first test cannot distinguish success from a generic/classical phenomenon;
- the candidate depends on an unsettled review as though it were accepted evidence;
- a mutation-derived candidate still imports, explicitly or implicitly, the deliberate false step that generated it.

For every decisive kill, identify the **first exact mathematical failure** and then perform one bounded salvage pass. Ask whether changing only what the failure exposes yields a distinct statement with its own coherent assumptions and decisive test. Internally the outcome may be thought of as:

- `dead`: no structure survives the failure;
- `salvageable`: a nearby repaired statement is coherent but not yet important enough to hand off;
- `structural`: the failure exposes a new invariant, obstruction, retained variable, or exact relation;
- `high-value`: the residual question is both falsifiable and capable of redirecting a line or the global program.

These labels are internal reasoning aids, not repository state and not evidence. Only a genuinely distinct `structural`/`high-value` residual that passes the ordinary handoff requirements may populate the single campaign-level `handoff_question`.

At most **one** attack-family candidate may survive phase 5. It may survive with substantial uncertainty; it may not survive with an unnamed object, missing construction, unfalsifiable promise, hidden import of RH, or dependence on a deliberate mutation known to be invalid.

A successful kill may leave a **different** precise question worth handing to another researcher. Record at most one derived handoff question if it is genuinely distinct from the killed route and has a concrete decisive test.

If no attack-family candidate survives, set the campaign to phase 6 with an empty survivor set but preserve the optional single `handoff_question`. Do not publish or notify yet.

## Phase 6 — publication gate

Synchronize current `main` and perform the publication-safety audit against material changes since `base_main_sha`. This is the only phase that consumes post-snapshot Mathia knowledge.

There are two possible clue sources, with **at most one clue total per campaign**:

### A. Survivor clue

If one attack-family candidate survived phase 5, compare it against current `main`. If it has been duplicated, classicalized, refuted, or materially invalidated by post-snapshot work, kill it without restarting the campaign.

Otherwise apply the **ultra-selective survivor clue gate**. Publish or materially strengthen a clue only when all hold:

1. the mathematical object and proposed mechanism are explicit enough for another researcher to reconstruct;
2. the direction is not duplicated by current findings, Mind, Master state, graph navigation, prior-art nodes, or clues in any lifecycle state;
3. it survived the mandatory external literature audit without collapsing into known mechanism or empty novelty claim;
4. it explicitly addresses the strongest relevant Mathia obstruction or lies demonstrably outside that obstruction's hypotheses;
5. it has a decisive first test that can cheaply falsify, classicalize, or materially narrow it;
6. resolving it could redirect an existing line, create a genuine new information channel, or alter the global program;
7. uncertainty is stated strongly enough that no reader could mistake it for evidence;
8. if it came from controlled mutation, the published mechanism is validly stated **without** the deliberate false step and `## Evidence boundary` records the mutation, first failure, and repair clearly enough that the parent route cannot later be mistaken for support.

### B. Derived handoff clue

Even when no attack-family candidate survives, phase 6 may publish or materially strengthen one `status: proposed` handoff clue when a kill/narrowing/mutation exposed a **distinct** falsifiable question that deserves ordinary Research Watch investigation.

All must hold:

1. the parent candidate's kill or deliberate invalid step remains valid; the clue does not reopen, weaken, or rhetorically rebrand the killed/false route;
2. the handoff question is mathematically explicit and materially useful on its own;
3. it has a clear existing `target_line`, or is honestly global/cross-line;
4. current findings, Mind, Master state, prior-art nodes, and clues do not already own the same precise question;
5. the Visionary performs a bounded, targeted current literature check sufficient to rule out an obvious known duplicate or immediate classicalization; a full attack-family literature tournament is not required because the clue is explicitly unvalidated and will be triaged by Research Watch;
6. it has a cheap decisive test or exact proof obligation;
7. `## Evidence boundary` names the parent route that was killed/narrowed/mutated, identifies the exact failure, and makes explicit that only the repaired residual question is being handed off;
8. for controlled-mutation provenance, nothing in `Question`, `Construction`, `Why it may matter`, or the proposed test treats the intentionally false mutation as evidence or as an accepted premise.

A clever analogy, generic future-work sentence, restatement of a kill, unexplored keyword combination, raw controlled mutation, or long speculative derivation does not pass either gate.

If both a survivor clue and a derived handoff clue qualify, prefer the survivor clue unless the handoff is clearly more actionable and program-relevant. Never publish more than one clue in the campaign.

When the same precise question now exists as `status: proposed`, prefer materially strengthening that clue when permitted by the shared clue skill. Do not touch accepted, rejected, or resolved clues.

If neither source qualifies, close the campaign issue as a normal null result with no repository commit.

After the clue publication attempt, record only the final disposition and publication commit/path when applicable, then close the campaign issue.

## Clue handoff

Use `.agents/skills/mathia-research-clues/SKILL.md` without changing lifecycle semantics.

For a question clearly owned by an existing line:

```text
research/<line>/clues/CLUE-<slug>.md
```

For a genuinely cross-line question or possible new research line:

```text
research/clues/CLUE-<slug>.md
```

Use:

```yaml
origin: visionary-researcher
```

Set `target_line` to the exact existing line, `global`, or `new-line-candidate`.

The clue's `based_on` list must cite persisted Master/Mind/finding/prior-art/clue paths that motivated and constrained the proposal. For a survivor clue, `## Evidence boundary` includes compact bibliographic identifiers for the closest authoritative external literature, the exact overlap, and the residual question not established there. For a derived handoff clue, include the bounded literature/dedup check and the exact persisted kill/narrowing boundary that makes the handoff question distinct. For any controlled-mutation-derived clue, the evidence boundary must additionally identify the deliberately invalid perturbation, the first failure, and the repaired residual, explicitly stating that the parent mutation is not evidence.

Do not turn the clue into a campaign report. The Visionary must not set `accepted`, `rejected`, or `resolved`.

## Ownership and hard path gate

The Visionary campaign may mutate its single GitHub campaign issue as working state. This issue mutation is the **only durable state-persistence exception**.

Repository writes remain restricted to proposed clue files under:

```text
research/<discovered-line>/clues/**
research/clues/**
```

It must not modify:

```text
research/master/**
research/mind/**
research/<line>/mind/**
research/graph/**
research/<line>/graph/**
research/prior_art/**
research/<line>/findings/**
*.review.md
research/<line>/README.md
research/<line>/SOURCES.md
research/<line>/LEAN_CANDIDATES.md
scheduled tasks
code/tests/docs/experiments
.obsidian/**
```

The scheduled task itself may be changed only by an explicit user request outside the scheduled Visionary execution.

It must not create, delete, move, initialize, merge, pause, split, or recolor a research line.

## Publication policy

A scheduled Visionary campaign may publish a clue change directly to the default branch only in phase 6 when either the survivor gate or derived-handoff gate and all shared clue gates pass.

Before each publication commit:

1. refresh the default branch and ensure the evidence/literature basis is still coherent;
2. inspect the complete diff;
3. verify every changed path is an authorized clue path;
4. verify every clue remains `status: proposed` and uses `origin: visionary-researcher`;
5. verify the clue includes a concrete question/construction, decisive test, and bounded literature/evidence boundary appropriate to its clue type;
6. for controlled-mutation-derived clues, verify the deliberate false step is quarantined to provenance/evidence-boundary text and is not imported as support for the proposed residual;
7. verify no state, finding, review, Mind, graph, prior-art, task, or unrelated file changed;
8. remove formatting churn and any text that records the campaign rather than the research question.

Use:

```text
research(visionary): propose <clue>
research(visionary): sharpen <clue>
```

If no clue passes, create no commit. Never commit merely to show that a campaign phase ran.

## Notification and reporting

Campaign checkpoint issue comments are persistence, **not user notifications**.

Notify only when:

- a workflow, required-capability, synchronization, campaign-state ambiguity, candidate-identity continuity, path-gate, or publication failure prevents intended progress.

Clue creation/strengthening in `proposed` state follows the shared clue notification policy and is silent. The eventual Research Watch notifies separately if it changes the clue to `status: accepted`.

Do not notify for:

- phase completion;
- partial phase checkpoints;
- null campaigns;
- rejected internal candidates;
- dead controlled mutations;
- unchanged clues;
- routine literature completion;
- normal campaign issue closure.

## Operating cadence

This skill is designed for **one continuing campaign advanced by a recurring invocation**, rather than one monolithic weekly pass or a daily quota.

The scheduler should use a **minimal launcher prompt**: identify the repository, load this skill and its required companion skills, and execute one scheduled Visionary pass. Do not duplicate paths, phase transitions, campaign/candidate identity rules, frozen-snapshot rules, publication gates, clue lifecycle rules, or notification policy in scheduler text. Those rules live here. If legacy scheduler text contains procedural detail that conflicts with this skill, treat it as configuration drift and follow this skill; outside an explicit user-requested task edit, the Visionary must not rewrite its own schedule.

The scheduler should invoke the same minimal prompt each time. The skill determines whether to create a campaign, resume the current frozen-snapshot phase, repeat an incomplete phase, repair an unambiguous control-plane identity/continuity defect, or close the campaign in phase 6.

Do not start a second campaign while another is active. After phase 6 closes a campaign, the next scheduled invocation may start a new campaign immediately unless the user has changed the schedule.

The Visionary must never modify its own schedule.
