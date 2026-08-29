---
name: mathia-research-review
description: Shared sidecar protocol for adversarial review of Mathia research findings, with turn ownership, convergence by deletion, Git-visible change semantics, clue handoff, and review-notification semantics.
---

# Mathia Research Review

## Responsibility

Use this skill whenever an adversarial process challenges a persisted Mathia research finding or the owning Research Watch responds to that challenge.

The protocol keeps the **claim** and the **review conversation** separate. The finding remains the canonical object consumed by the other research processes; an adjacent `.review.md` file is a temporary dispute sidecar. Git history preserves creation, replies, closure, and withdrawal, so there is no separate review archive or review-status database.

This skill defines procedure only. It does not decide which mathematical claims are true and does not grant a caller ownership of unrelated repository paths.

The first version of this protocol applies only to Research-Watch-owned findings. Do **not** create reviews for `mind/**` yet.

## Reviewable objects

A review target must be an existing canonical finding:

```text
research/<line>/findings/<PREFIX>-NNN-<slug>.md
```

Exclude:

- any existing `*.review.md` file;
- `README.md`, `SOURCES.md`, or `LEAN_CANDIDATES.md`;
- `mind/**`;
- `graph/**`;
- clues and prior-art projections;
- generated indexes or project/status prose.

Attack mathematical or epistemic claims, not formatting.

## Sidecar identity

For a target:

```text
<dir>/<name>.md
```

use exactly:

```text
<dir>/<name>.review.md
```

Example:

```text
research/prime_circle/findings/PC-023-projective-spectrum.md
research/prime_circle/findings/PC-023-projective-spectrum.review.md
```

The review path is derived from the target path. Do not allocate a separate review ID and do not move the review into a central directory.

A sidecar may disappear when a review converges and may later be recreated if materially new evidence reopens the unchanged target. Git history distinguishes review episodes.

## Minimal review format

Create the sidecar with compact frontmatter and an append-only dialogue:

```markdown
---
type: adversarial-review
target: research/<line>/findings/<finding>.md
---

# Adversarial review

## Adversary

<precise objection, counterexample, missing hypothesis, source conflict, or falsification argument>
```

The owner appends:

```markdown
## Owner

<response grounded in derivation, evidence, source, counterexample, or concession>
```

If the objection survives, the adversary appends another `## Adversary` section, and so on.

Do not add timestamps, run logs, confidence percentages, workflow statuses, TODO queues, or duplicated copies of the target claim. The Git history already records chronology.

## Turn ownership

The last substantive speaker determines whose turn it is:

```text
last speaker Adversary -> only the finding owner should answer
last speaker Owner     -> only the adversary should answer
```

Do not append another comment when it is not your turn. Do not create parallel sidecars for the same target.

A process that has nothing materially new to add should leave the review untouched rather than append an acknowledgement.

## Opening a review

The adversary opens a sidecar only for a **material** objection. Good reasons include:

- an incorrect derivation, sign, normalization, domain, branch, convergence condition, or quantifier;
- a missing hypothesis that materially weakens the claim;
- a counterexample or degenerate case;
- a known theorem or prior-art source that contradicts the stated novelty or implication;
- a universal/background mechanism being mistaken for structure specific to the research object;
- an information-loss, gauge, coordinate, telescoping, or equivalence argument that breaks the claimed mechanism;
- an evidence classification stronger than the stored derivation supports;
- a claimed consequence that does not follow from the premises.

Do not open a review for style, wording preference, desire for a prettier proof, an unrelated alternative research direction, or generic skepticism without a falsifiable objection.

The first adversary comment should identify the exact claim under attack, give the strongest current argument against it, and state what would resolve the objection when that is knowable.

## Owner response

Before answering, the finding owner must independently reconstruct the relevant derivation and seriously test the objection. Do not defend a claim merely because the owner created it.

The owner has two principal outcomes.

### Defend the claim

If the objection can be answered while the persisted finding remains materially correct:

1. keep the finding unchanged while the review is open;
2. append an `## Owner` response with the decisive argument/evidence;
3. leave the sidecar in place for the adversary to judge.

Do not delete the sidecar yourself after a defense. Closure in this direction belongs to the adversary.

### Concede the objection

If the objection shows that the persisted claim is materially wrong or no longer deserves to exist in its current form:

1. delete the target finding;
2. delete its `.review.md` sidecar in the **same commit**;
3. if a corrected or narrower claim remains substantively valuable, publish it as a new finding with a new stable finding ID rather than silently repurposing the withdrawn claim;
4. update other owner-controlled branch artifacts only when necessary to remove a now-invalid direct dependency and when the owning skill permits it.

The deletion is the resolution signal. Do not leave a tombstone finding or a `status: invalidated` replacement merely to preserve history; Git already preserves it.

If the owner is not yet able to resolve or materially answer the objection, leave the review unchanged. An open review is allowed to survive multiple scheduled runs.

## Adversary response and closure

When the last speaker is the owner, the adversary re-evaluates the claim from scratch using the response and relevant evidence.

If the owner has resolved the objection, the adversary deletes **only** the `.review.md` sidecar. The target remains. This means the review converged in favor of the claim.

If the objection remains, the adversary appends another `## Adversary` section explaining the remaining issue. Do not restate already resolved points merely to continue the conversation.

The adversary never edits or deletes the target finding.

## Review notification policy

Adversarial review is intentionally operated in **full-observability mode** while the protocol is being validated. Every material review state transition or dialogue turn is notification-worthy.

Notify for all of the following:

- creation of a new `.review.md` sidecar;
- every substantive `## Owner` response;
- every substantive follow-up `## Adversary` response;
- an owner concession that withdraws the reviewed finding;
- a corrected or replacement finding created because a review invalidated or materially narrowed the old claim;
- adversary deletion of the sidecar because the owner's defense resolved the objection;
- any other material review-protocol transition that changes the mathematical disposition of the disputed claim.

Do not notify for merely observing an existing review, an unchanged review waiting for the other participant, acknowledgements, duplicate objections, or runs in which the review state did not materially change.

To avoid duplicate notifications, **the process that authors the review-state change owns its notification**:

```text
Adversary opens/continues/closes review -> Adversarial Research notifies
Owner answers/concedes/replaces claim   -> owning Research Watch notifies
```

A process must not notify merely because it later observes a transition already authored by the other side.

Task-specific prompts should not duplicate this review-notification matrix unless they intentionally impose a temporary stricter policy. This shared skill is the default source of truth for review notification semantics.

## Git as the change stream

The repository tree represents current knowledge; Git represents what changed.

Processes that consume research changes should, when they have a previous processed revision, inspect the Git delta rather than looking only for currently existing new files. Relevant events include:

```text
A  <finding>.md            new claim
M  <finding>.md            changed claim
A  <finding>.review.md     new adversarial objection
M  <finding>.review.md     new dialogue turn
D  <finding>.review.md     review converged
D  <finding>.md            claim withdrawn
```

A deleted finding is no longer part of the current research corpus even though it remains recoverable from history.

The current tree remains authoritative for whether a review is open: if a sidecar exists, the target is under active challenge; if no sidecar exists, there is no open adversarial objection under this protocol.

## Clues discovered during review

A review may expose a valuable question or cross-connection that is **not itself the resolution of the reviewed claim**. Either participant may hand that off through `.agents/skills/mathia-research-clues/SKILL.md` when the caller has loaded that skill.

Examples include:

- the objection reveals the same obstruction in another research line;
- the defense exposes a new invariant worth testing independently;
- resolving the dispute suggests a discriminating experiment or theorem outside the target claim;
- an unexpected equivalence between two mechanisms appears during the dialogue.

Do not bury such a lead in a long review thread when it deserves independent research. Conversely, do not create a clue merely to summarize the dispute.

## Ownership extension

This skill grants only the narrow sidecar actions required by the protocol.

### Adversary

May create, append to, or delete:

```text
research/<line>/findings/*.review.md
```

It may never modify or delete the corresponding finding.

### Finding owner / Research Watch

May append owner responses to:

```text
research/<line>/findings/*.review.md
```

and, when conceding, may delete the target finding and its sidecar together. The Research Watch's own skill remains authoritative for all other finding-path writes.

Clue writes require `mathia-research-clues`; this skill does not independently grant clue ownership.

## Publication gate

Before publishing any review-protocol change:

1. verify the target exists unless the owner is atomically withdrawing it;
2. verify the sidecar name exactly matches the target;
3. verify it is the caller's turn;
4. verify the diff contains no unauthorized target, mind, graph, prior-art, code, experiment, or unrelated changes;
5. ensure the comment materially advances the mathematical dispute;
6. ensure a convergence deletion follows the exact owner/adversary rules above.

Review dialogue is not a run log. If nothing material changed, commit nothing.
