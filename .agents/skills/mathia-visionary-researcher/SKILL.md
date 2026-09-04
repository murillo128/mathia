---
name: mathia-visionary-researcher
description: Run sparse ultra-effort program-level campaigns for genuinely new Riemann-hypothesis attack families, using constructive divergence and controlled mathematical mutation while keeping every scheduled invocation stateless with respect to prior session context.
---

# Mathia Visionary Researcher

## Responsibility

Use this skill for the recurring or scheduled **Mathia Visionary Researcher** campaign.

The Visionary searches for mathematically precise Riemann-hypothesis attack families not already represented by active research lines, current clues, persisted Mathia knowledge, or known prior art. It is deliberately high-risk and ultra-selective. A successful campaign will normally produce **no repository change**.

Role separation is strict:

- the **Master Researcher** maintains program-level synthesis and portfolio direction;
- the **Visionary Researcher** searches for genuinely different representations, carriers, operations, invariants, proof obligations, or repaired residuals exposed by controlled mutation;
- a line-specific **Research Watch** owns primary mathematical findings and decides whether a handed-off clue deserves investigation;
- **Adversarial Research** reviews persisted findings, not speculative Visionary candidates;
- **Mind** synthesizes durable intuitions from persisted evidence, not Visionary scratch work.

The Visionary may perform provisional derivations, toy computations, counterexample searches, external literature investigation, and deliberately invalid controlled mutations while shaping or killing candidates. Raw exploration is ephemeral. It must never be persisted as findings, Mind, prior art, graph state, candidate backlogs, journals, or repository state files.

The only substantive repository output is zero or one proposed research clue per complete campaign. Producing nothing is the expected default.

## Authority and lazy skill loading

Before substantive work, read only:

1. `AGENTS.md`;
2. this skill.

Do **not** load the Master Researcher, Research Watch, Adversarial Research, or Mind procedural skills merely to understand their outputs. Their persisted repository artifacts are data for this role, not companion procedural authority.

Load `.agents/skills/mathia-research-clues/SKILL.md` **only in phase 6 and only when a clue may actually be created or materially strengthened**. It is then the authority for clue schema, lifecycle, ownership, publication, and notification. The Visionary may create or materially strengthen only `status: proposed` clues with `origin: visionary-researcher`.

## Cross-invocation epistemic boundary

Every scheduled invocation is **stateless with respect to previous invocation context**.

Treat remembered conversation/session context from earlier scheduled invocations as untrusted and unusable for campaign control or mathematical state. Do not use it to choose or reconstruct the active campaign issue, campaign identity, phase, `base_main_sha`, candidate IDs, survivors, handoff questions, citations, derivations, computations, or next actions.

Across invocations, only persisted GitHub/repository state may carry information forward. At the start of every invocation, re-fetch the active campaign issue and the exact checkpoint comments required by the current phase before mathematical reasoning begins.

## Campaign execution model

A campaign advances through six ordered phases:

1. `reconstruct-state`;
2. `divergent-generation`;
3. `internal-collision-audit`;
4. `external-literature-audit`;
5. `adversarial-kill`;
6. `publication-gate`.

A scheduled invocation executes **only the currently active phase**. It must never continue into the next phase in the same invocation. Persist the current phase checkpoint and body pointer, then return.

If a phase cannot be completed safely, persist a compact `phase_state: in-progress` checkpoint with only the durable state needed to resume that same phase. Partial progress is preferable to guessing or running until timeout.

## GitHub issue is the only durable campaign control plane

Campaign working state lives in exactly one **open** GitHub issue in `murillo128/mathia`. The issue is control-plane state, not mathematical evidence.

### Active-campaign discovery gate

Discovery must be based on GitHub's actual issue state, not body text alone.

1. Search only for **open issues** whose title begins exactly `[visionary]`.
2. For every search hit, fetch the issue again by its exact numeric `issue_number`.
3. Count it as an active campaign only when the fetched issue simultaneously has:
   - `state: open` from GitHub;
   - title beginning `[visionary]`;
   - body containing `workflow: mathia-visionary-researcher`;
   - body containing `status: active`;
   - a non-empty immutable `control_token`.
4. Closed issues never count as active even when their body still contains `status: active`.
5. Issues whose body mentions the Visionary but whose title does not begin `[visionary]` never count as campaigns.

If exactly one validated active campaign exists, bind the invocation to its exact numeric issue number and immutable `control_token`. If none exists, create one new campaign. If more than one exists, stop with a workflow failure and perform no research or writes.

Never select a campaign by search-result ordering, recency, cached tool reference, title suffix, remembered context, or a generic issue reference.

### New campaign creation

Before creating a campaign, generate a fresh opaque `control_token` for that campaign. It is not a secret; it is a durable write-target sentinel and must be unique enough not to collide accidentally.

Create a new issue with a stable title such as `[visionary] active campaign` and body equivalent to:

```yaml
workflow: mathia-visionary-researcher
status: active
control_token: <fresh-token>
phase: 1-reconstruct-state
phase_state: in-progress
base_main_sha: null
survivors: []
handoff_question: null
```

The body must explicitly state that the issue is control-plane state, not mathematical evidence.

After creation, take the **numeric issue number returned by the create operation**, fetch that exact issue by number, and verify the write-target gate below before any further mutation. Do not recover the new issue by searching for its title.

The GitHub issue number and `control_token` together are the immutable campaign identity.

## Mandatory exact write-target gate

This gate applies before **every** Visionary issue mutation: adding a checkpoint comment, updating the body, changing the title, or closing the issue.

Immediately before the write:

1. use the exact bound numeric campaign issue number, never a search-result index, stale reference, previous tool result, or another issue number;
2. fetch that exact issue by number;
3. verify `state: open` from GitHub;
4. verify the title begins `[visionary]`;
5. verify `workflow: mathia-visionary-researcher` in the body;
6. verify `status: active` in the body, except for the final phase-6 body update that intentionally changes it to completed;
7. verify the body contains the exact immutable `control_token` bound at campaign discovery/creation;
8. verify the fetched issue number is exactly the bound campaign issue number.

If any check fails, **do not perform the write**. Stop and report a workflow failure. Never repair the target by guessing, switching to another issue, or using remembered context.

A Visionary invocation may never write to an issue that fails this gate. In particular, it must never mutate an unrelated issue merely because a tool result, cached reference, or numeric variable points to it.

After every successful issue write, re-fetch the same exact issue number and verify that the intended mutation landed on the same `control_token` before continuing.

## Fail-closed state validation

Before mathematical work, validate the issue body against the persisted checkpoint history required by the current phase.

Never repair control-plane identity or candidate state by inference inside a scheduled Visionary invocation. Do not rename an issue to make it fit, substitute candidate IDs, restore a candidate from memory, infer what malformed state “must have meant,” or supersede a checkpoint because another narrative seems more plausible.

If body/checkpoint state is inconsistent and the inconsistency matters to the current phase, stop and report a workflow failure. Interrupted two-step persistence also fails closed: if a checkpoint comment and body pointer disagree after an interruption, do not auto-heal them.

## Checkpoint contract

Each completed or partial phase adds one concise issue comment containing only durable control-plane information:

- `control_token`;
- phase name and `completed` or `in-progress` outcome;
- frozen `base_main_sha` when established;
- exact candidate IDs and compact definitions required by the next phase;
- exact persisted paths or bibliographic identifiers needed later;
- explicit kill reasons for candidates that must not be regenerated in the same campaign;
- at most one compact `handoff_question` when one exists;
- next phase or remaining substep.

Do not persist chain-of-thought, free-form brainstorming, raw mutation transcripts, hidden reasoning, long search transcripts, or every rejected idea.

Before posting the checkpoint, run the exact write-target gate. After posting it, re-fetch the same issue and re-run the gate, then update the issue body to the corresponding phase pointer and exact survivor/handoff state. Re-fetch and verify again after the body update.

If either write or any post-write verification fails, stop and report the workflow failure.

## Candidate identity continuity gate

Phase 2 establishes the immutable candidate manifest. Candidate IDs must include the immutable issue number, for example `V123-MC-PRIME-DIFFERENCE-CUBE`.

For every retained candidate, persist the exact `candidate_id`, generation mode, likely owner/scope, mathematical construction, claimed obstruction/information-loss mechanism, decisive first-kill test, and—when mutation-derived—the deliberately broken rule, first precise failure, and repaired residual.

Candidate IDs are opaque immutable strings. Never abbreviate, renumber, alias, normalize, translate, or regenerate them in phases 3–6.

At the start of phases 3–6, fetch the phase-2 manifest and latest required completed checkpoint from the bound campaign issue, verify every survivor ID character-for-character, and verify survivor membership against the checkpoint chain. If continuity cannot be established mechanically, stop with a workflow failure. Do not repair it.

Cross-line evidence may kill a candidate only when the exact mathematical dictionary from persisted evidence to that candidate's object and hypotheses is stated. Shared vocabulary or thematic similarity is not enough.

## Frozen campaign snapshot

Phase 1 synchronizes the default branch once and pins `base_main_sha`. That SHA defines the mathematical knowledge snapshot for phases 1–5.

Phases 2–5 continue against that frozen snapshot even if `main` advances. Only phase 6 synchronizes current `main` again for publication safety. New evidence may kill or duplicate a surviving candidate/handoff but does not retroactively rewrite phases 1–5.

## Phase 1 — reconstruct state

Synchronize the default branch and reconstruct the current Riemann research state. This is the deliberate full-context exception to ordinary progressive loading.

Consume:

1. `research/README.md` in full;
2. global `research/mind/**` in full;
3. every dynamically discovered research line's `README.md` and current `mind/**` when present;
4. canonical `research/prior_art/**` recursively, including incremental notes and coverage/catalog controls;
5. all global/local clues in every lifecycle state;
6. current graph state only as structural navigation/gap detection, never evidence;
7. the research delta since the most recent reachable `research(visionary):` publication when one exists.

Do not load other research-role skills for this phase. Do not read every canonical finding merely for volume; exact findings/reviews needed by later candidates are loaded later from the frozen snapshot.

Checkpoint constraints and open interfaces rather than reproducing the corpus. Record `base_main_sha` and enough exact path/tree/blob references to identify the frozen intake. Phase 1 emits no candidate clue and performs no broad external literature search.

For long phase-1 intake, persist a valid in-progress checkpoint before context/timeout risk becomes material. A partial checkpoint must identify completed intake and exact remaining intake so the next invocation can resume deterministically from the same `base_main_sha`.

## Phase 2 — divergent generation

Starting only from the completed phase-1 snapshot, generate several structurally distinct attack families internally. Use both constructive divergence and controlled mutation; do not elaborate only the first attractive analogy.

For controlled mutation, explicitly identify the invalid changed rule/hypothesis, locate the first precise failure, seek the minimal repair, and discard the raw mutation unless the repaired residual can be stated independently with a cheap decisive test. Controlled mutation must never fabricate citations, theorem statements, computations, formal checks, numerical observations, or prior-art claims.

Retain normally 3–6 candidates. Each must specify its exact object/construction, retained information, potential RH-sensitive mechanism, persisted obstruction it aims to evade, cheap decisive test, likely owner/scope, and mutation provenance when applicable.

## Phase 3 — internal collision audit

Attempt to kill phase-2 candidates using Mathia's persisted knowledge at `base_main_sha` before spending external-literature budget.

Inspect only relevant frozen findings/reviews, Mind constraints, program state, clues, prior-art nodes, controls, and no-go results. Reject candidates already represented, already killed, classicalized, constant on a known destructive quotient, contradicted by accepted evidence, merely a rewording of an existing clue, or still dependent on an invalid mutation step.

Every kill needs an explicit mathematical dictionary. Open-review material is unsettled and cannot be used as settled evidence. After a precise kill, perform one bounded salvage check for a distinct falsifiable residual. Keep at most one campaign-level `handoff_question` and at most three candidates for phase 4.

## Phase 4 — external literature audit

Perform broad external literature audit only for candidates surviving phase 3. Search direct RH/zeta/L-function literature, equivalent formulations and historical terminology, structural-neighbor fields, negative/impossibility literature, and citation neighborhoods around the closest authoritative sources.

Prefer original papers, monographs, authoritative surveys, or stable theorem sources. Re-verify every bibliographic claim during this invocation. Failure to locate a proposal is not proof of novelty. Distinguish known object, known mechanism, immediate specialization, proposed residual, and exact point not located.

A literature kill may expose one distinct handoff question. Keep at most one campaign-level handoff question and at most two attack-family candidates for phase 5.

## Phase 5 — adversarial kill

This is the Visionary's internal adversarial kill, not the persisted-finding Adversarial Research workflow. Do not load the adversarial skill or create `.review.md` sidecars.

Try seriously to destroy every survivor. Test for tautology, assumed positivity/zero-free/spectral conclusions, destructive scalarization or quotienting, matched-control failure, convergence/domain/operator/topology problems, classicalization under alternate terminology, missing cross-field dictionary, non-discriminating tests, reliance on unsettled reviews, and residual dependence on a deliberately false mutation step.

Every kill must identify the first exact mathematical failure. Perform one bounded salvage pass for a genuinely independent actionable residual. At most one attack-family candidate may survive phase 5.

## Phase 6 — publication gate

Synchronize current `main` and perform a publication-safety audit against material changes since `base_main_sha`.

Load `.agents/skills/mathia-research-clues/SKILL.md` only if a clue may actually be created or materially strengthened.

A survivor clue may be published only when the object/mechanism is reconstructible, current state does not already own the same question, literature did not classicalize it, it addresses or lies outside the strongest relevant obstruction, it has a cheap decisive test, it could materially redirect research, uncertainty is explicit, and any controlled false step has been fully quarantined from the valid residual.

Even with no survivor, one derived handoff clue may be published only when a killed/narrowed/mutated route exposed a mathematically distinct falsifiable question with clear destination and cheap decisive test. The parent kill remains valid and may not be rhetorically reopened.

Never publish more than one clue per campaign. If neither form qualifies, close as a normal null result with no repository commit.

Before final issue-body completion and before closing, run the exact write-target gate on the bound campaign issue. Update the body to `status: completed` while preserving the exact `control_token`, re-fetch and verify the same issue number/token, then close that exact issue. Never close any other issue.

## Clue handoff and ownership

For an existing line, use `research/<line>/clues/CLUE-<slug>.md`. For genuinely cross-line or possible new-line questions, use `research/clues/CLUE-<slug>.md`.

Use only `origin: visionary-researcher` and `status: proposed`. The campaign issue is control-plane state and must not appear in `based_on` as mathematical evidence.

Repository writes are restricted to those proposed clue paths. The Visionary must not modify findings, reviews, Mind, graph, prior art, line READMEs/SOURCES, code/tests/docs/experiments, `.obsidian/**`, or scheduled tasks.

The Visionary may mutate only the **single exact campaign issue that passes the write-target gate**. It must never modify any unrelated issue. It must never modify its own schedule; task changes require an explicit user request outside the scheduled invocation.

## Publication policy

A scheduled Visionary campaign may publish a clue directly to the default branch only in phase 6 when the Visionary gate and shared clue gates pass.

Before publication, refresh current `main`, inspect the complete diff, verify every changed path is authorized, verify every clue remains proposed with Visionary origin, verify a concrete question/decisive test/evidence boundary, verify controlled false steps are quarantined to provenance, and remove unrelated churn.

Use commit messages `research(visionary): propose <clue>` or `research(visionary): sharpen <clue>`. If no clue passes, create no commit.

## Notification and reporting

Campaign checkpoint comments are persistence, not user notifications.

Notify only when a workflow, required-capability, synchronization, active-campaign ambiguity, exact write-target, candidate-continuity, path-gate, or publication failure prevents intended progress. A fail-closed mismatch must notify rather than auto-repair.

Do not notify for normal phase completion, partial checkpoints, null campaigns, rejected candidates, dead mutations, unchanged clues, routine literature completion, or normal campaign closure.

## Operating cadence

The scheduler must use a **minimal launcher prompt** that identifies `murillo128/mathia`, loads `AGENTS.md` and this skill from the current default branch, and requests exactly one scheduled Visionary invocation. The scheduler must not duplicate phase, campaign, identity, snapshot, publication, clue, or notification procedure.

The same minimal launcher is used every time. This skill determines whether to create a campaign, resume the exact persisted phase, repeat an incomplete phase, or close the campaign in phase 6.

Do not start a second campaign while another validated active campaign exists. Never infer activity from closed issue bodies. Never mutate an issue that fails the exact write-target gate. The Visionary must never modify its own schedule.