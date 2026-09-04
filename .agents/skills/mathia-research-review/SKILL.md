---
name: mathia-research-review
description: Shared sidecar protocol for adversarial review of Mathia research findings, with turn ownership, durable-math persistence, Git-visible convergence, clue handoff, and review-notification semantics.
---

# Mathia Research Review

## Responsibility

Use this skill whenever an adversarial process challenges a persisted Mathia research finding or the owning Research Watch responds to that challenge.

The protocol keeps the **claim** and the **review conversation** separate. The finding is the canonical current object consumed by other research processes; an adjacent `.review.md` file is temporary dispute state. Git preserves the historical conversation and every previous version of the finding, so the current tree should contain the best current mathematical formulation rather than review history.

This skill defines procedure only. It does not decide which mathematical claims are true and does not grant a caller ownership of unrelated repository paths.

The current protocol applies only to Research-Watch-owned findings. Do **not** create reviews for `mind/**` yet.

## Core persistence principle

A review may discover mathematics that was not present in the target finding. That mathematics must not disappear merely because the sidecar is eventually deleted.

Use this identity rule:

```text
same mathematical claim + stronger/completed proof or evidence
    -> update the existing finding in place

materially different, weakened, corrected, or replacement claim
    -> withdraw the old finding and publish a new finding with a new stable ID

independent durable result discovered during the defense
    -> publish a separate new finding with a new stable ID
```

Never create `.v2`, `.v3`, or similar versioned finding paths. A stable finding ID denotes one stable mathematical claim. Git already versions its proof/exposition. If the claim identity changes materially, the finding identity changes.

Do not add an `Adversarial resolution`, review-history, changelog, or similar section merely to record the review. Integrate accepted mathematics into the natural claim/derivation/evidence/boundary sections of the finding. Git is the historical record.

An `M <finding>.md` event is intentionally part of the research change stream: Mind, Graph, Master, and other consumers can discover that the current evidence changed without requiring a new finding ID.

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

Do not add timestamps, run logs, confidence percentages, workflow statuses, TODO queues, or duplicated copies of the target claim. Git already records chronology.

## Turn ownership

The last substantive speaker determines whose turn it is:

```text
last speaker Adversary -> only the finding owner should answer or perform an owner-side persistence action
last speaker Owner     -> only the adversary should judge/continue/close
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

The first adversary comment should identify the exact claim under attack, give the strongest current argument against it, and state what would resolve the objection when knowable.

## Owner response

Before answering, the finding owner must independently reconstruct the relevant derivation and seriously test the objection. Do not defend a claim merely because the owner created it.

### Defend the current claim

If the objection can be answered while the **same mathematical claim** remains correct:

1. while the objection is still awaiting adversary judgment, keep the finding unchanged;
2. append an `## Owner` response with the decisive argument/evidence;
3. leave the sidecar in place for adversary judgment.

The owner response may contain mathematics not yet in the finding because the adversary has not accepted it yet. If that mathematics later becomes necessary to the accepted defense, it must be materialized before the review closes.

### Concede or materially change the claim

If the objection shows that the stored mathematical claim is materially wrong, overstated, or must change identity:

1. delete the target finding;
2. delete its `.review.md` sidecar in the **same commit**;
3. if a corrected/narrower/replacement claim remains substantively valuable, publish it as a new finding with a new stable ID;
4. never create `<old-id>.v2` or silently repurpose the old ID;
5. update other owner-controlled branch artifacts only when necessary and permitted by the owning skill.

The deletion is the resolution signal for the old claim. Do not leave a tombstone finding or `status: invalidated` replacement merely to preserve history.

If the owner cannot yet materially answer the objection, leave the review unchanged.

## Adversary judgment

When the last substantive speaker is `Owner`, the adversary re-evaluates the target from scratch using the response and relevant evidence.

There are three outcomes.

### 1. Objection remains

Append another `## Adversary` section containing only the unresolved issue or a materially stronger objection. Do not restate resolved points merely to continue the conversation.

### 2. Defense succeeds and adds no missing durable mathematics

If the target finding already contains everything needed for the accepted claim and the owner response only clarified/recombined material already persisted, delete **only** the `.review.md` sidecar. The target remains unchanged.

### 3. Defense succeeds but relies on new durable mathematics

If the objection is mathematically resolved **but the accepted resolution depends on a proof step, hypothesis analysis, source bridge, boundary argument, or other durable result not currently present in the canonical finding**, do **not** delete the sidecar yet.

Append a concise `## Adversary` turn stating that the mathematical objection is resolved but closure is pending persistence of the accepted mathematics. Identify what must be materialized, without dictating prose or requiring a review-history section.

This returns the turn to the owner.

The adversary never edits or deletes the target finding.

## Owner persistence after provisional acceptance

When the last `## Adversary` turn says the objection is resolved pending persistence, the owner must decide how the accepted new mathematics relates to the claim.

### Same claim: update in place

If the mathematical claim is unchanged:

1. update the existing finding in place (`M <finding>.md`);
2. integrate the accepted mathematics into the natural derivation/evidence/boundary sections;
3. do not add review-history prose;
4. append a concise `## Owner` turn confirming that the accepted mathematics is now persisted in the target;
5. leave the sidecar for final adversary verification.

This is the **sole protocol-authorized exception** to any caller rule saying that a target finding must remain byte-for-byte unchanged while a sidecar exists. It is allowed only after the adversary has accepted the mathematics and explicitly requested persistence.

### Independent durable result: new finding

If the defense produced a mathematically independent result that deserves its own stable claim:

1. keep the original target unchanged if its claim remains valid;
2. publish the independent result as a new finding with a new stable ID;
3. append a concise `## Owner` turn linking/identifying that new persisted result;
4. leave the sidecar for final adversary verification.

### Claim identity changed after all

If materialization reveals that the original claim must actually be weakened/corrected/replaced, follow the concession rule: delete the old target and sidecar together and create a new finding ID when warranted.

## Final adversary closure

When the owner has persisted accepted mathematics and the last speaker is `Owner`, the adversary verifies that:

- the current target still states the same claim that was defended;
- the accepted argument/evidence is actually present and no stronger than justified; or
- any independent new finding contains the durable result it was meant to preserve.

If verification passes, delete only the `.review.md` sidecar. If persistence introduced a material new problem, append a new `## Adversary` turn instead.

Thus a successful same-claim repair normally produces this Git-visible sequence:

```text
A/M  <finding>.review.md   objection / dialogue
M    <finding>.md          accepted mathematics materialized
M    <finding>.review.md   owner confirms persistence
D    <finding>.review.md   adversary closes
```

Other agents can therefore discover the durable mathematical change directly from `M <finding>.md`; they never need to reconstruct the deleted sidecar history.

## Review notification policy

Adversarial review is intentionally operated in **full-observability mode** while the protocol is being validated. Every material review state transition or dialogue turn is notification-worthy.

Notify for all of the following:

- creation of a new `.review.md` sidecar;
- every substantive `## Owner` response;
- every substantive follow-up `## Adversary` response, including provisional acceptance pending persistence;
- owner persistence of accepted new mathematics into an existing finding;
- an owner concession that withdraws the reviewed finding;
- a corrected, replacement, or independent finding created because of review;
- adversary deletion of the sidecar after a defense or persistence verification succeeds;
- any other material review-protocol transition that changes the mathematical disposition of the disputed claim.

Do not notify for merely observing an existing review, an unchanged review waiting for the other participant, acknowledgements, duplicate objections, or runs in which review state did not materially change.

To avoid duplicate notifications, **the process that authors the state change owns its notification**:

```text
Adversary opens/continues/provisionally accepts/finally closes -> Adversarial Research notifies
Owner answers/persists/concedes/replaces                         -> owning Research Watch notifies
```

A process must not notify merely because it later observes a transition authored by the other side.

Task-specific prompts should not duplicate this matrix unless intentionally imposing a stricter policy. This shared skill is the default authority for review notification semantics.

## Git as the change stream

The repository tree represents current knowledge; Git represents what changed.

Processes that consume research changes should, when they have a previous processed revision, inspect the Git delta rather than looking only for currently existing new files. Relevant events include:

```text
A  <finding>.md            new claim
M  <finding>.md            stronger/completed evidence for the same claim
D  <finding>.md            claim withdrawn
A  <finding>.review.md     new adversarial objection
M  <finding>.review.md     dialogue/persistence turn
D  <finding>.review.md     review converged
```

A deleted finding is no longer part of the current research corpus even though recoverable from history. A modified finding remains the same claim identity and is intentionally a discoverable new evidence event.

The current tree remains authoritative for whether a review is open.

## Resumable adversarial scan batches

Adversarial callers may checkpoint **scan coverage in Git commit messages** instead of creating a cursor file or other persistent run state. The checkpoint records repository history coverage, not a finding identity.

At the start of a new/changed-finding scan:

1. freeze the current default-branch commit as the immutable `scan target` for that pass; commits arriving after it belong to a later pass;
2. find the most recent trustworthy adversarial coverage trailer, when one exists;
3. inspect the Research-Watch-owned change stream after that coverage SHA through the frozen scan target in commit order;
4. keep Owner replies waiting for adversary judgment at the higher priority defined by the calling adversarial skill, without confusing review-dialogue priority with scan coverage.

Use exactly this trailer when persisting an advanced cursor:

```text
Adversarial-Reviewed-Through: <full-commit-sha>
```

The SHA is the **source/default-branch commit through which eligible research changes have been completely audited**. It is not the finding ID and it is not the adversarial commit's own SHA.

The cursor may advance only across a **contiguous fully reviewed prefix** of the frozen history window. In particular:

- every eligible new or materially changed canonical finding introduced by a source commit must be fully audited before the cursor may advance through that commit;
- when one source commit changes several eligible findings, all of them must be audited before that commit can become the cursor;
- never jump over a source commit containing an eligible finding that was only partially inspected or deferred;
- if execution stops part-way through the eligible findings associated with one source commit, keep the cursor at the preceding fully covered commit;
- commits after the frozen scan target never affect the truth of the cursor for the current pass; they are discovered in the next pass.

### Batch publication

Do **not** commit once per finding. Accumulate substantive sidecar/clue changes across several completed reviews or source commits and publish them as a small coherent batch. A batch boundary should be chosen when one of these is true:

- several findings have been fully audited and there is material review state worth persisting;
- a natural contiguous source-commit boundary has been completed;
- the remaining execution budget is becoming too small to safely complete another finding plus refresh/publication gates;
- an expensive next audit would put already completed material work at unnecessary risk of being lost.

Before starting another finding, inspect the remaining execution/time/tool-call/token budget when the runtime exposes such a signal. Start another audit only when there is comfortable margin to finish its mathematical check, refresh the affected target, run the publication/path gates, and persist any resulting batch. When no explicit remaining-budget signal is available, use a conservative heuristic based on work already performed and the expected complexity of the next audit rather than continually starting one more finding.

Before each batch commit, refresh every affected target and sidecar against the current default branch and re-run the ordinary turn, path, and publication gates. If a target changed after the frozen scan target, do not publish a stale objection unless it still applies to the current canonical target; the later source change itself remains outside the frozen window for the next pass.

When a material batch also establishes new contiguous scan coverage, include `Adversarial-Reviewed-Through: <sha>` in that commit message using the furthest fully covered source commit. Multiple review transitions may therefore share one commit and one cursor advancement.

Do **not** create an empty commit merely to persist scan progress. If a completed clean batch produces no repository change, commit nothing. A clean suffix may consequently be re-audited after interruption; this small amount of repeated computation is preferable to turning Git history into a run log. If the same run later accumulates a material batch, its trailer may advance across those previously completed clean commits as long as the whole prefix is genuinely covered.

If no trailer exists yet, use the caller's existing legacy boundary rule for the transitional scan. The first later material batch that has a truthful contiguous coverage boundary may establish the trailer. Never infer or invent coverage for history that was not actually audited.

## Clues discovered during review

A review may expose a valuable question or cross-connection that is **not itself the resolution of the reviewed claim**. Either participant may hand that off through `.agents/skills/mathia-research-clues/SKILL.md` when the caller has loaded that skill.

Examples include:

- the objection reveals the same obstruction in another research line;
- the defense exposes a new invariant worth testing independently;
- resolving the dispute suggests a discriminating experiment or theorem outside the target claim;
- an unexpected equivalence between two mechanisms appears during the dialogue.

Do not bury such a lead in a long review thread when it deserves independent research. Conversely, do not create a clue merely to summarize the dispute.

## Ownership extension

This skill grants only the narrow actions required by the protocol.

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

It may:

- delete target + sidecar atomically when conceding;
- after explicit adversary acceptance-pending-persistence, modify the existing target **only when the mathematical claim remains the same**;
- create a new finding ID for a materially different/replacement or independent durable claim.

The Research Watch's own skill remains authoritative for all other finding-path writes.

Clue writes require `mathia-research-clues`; this skill does not independently grant clue ownership.

## Publication gate

Before publishing any review-protocol change:

1. verify the target exists unless the owner is atomically withdrawing it;
2. verify the sidecar name exactly matches the target;
3. verify it is the caller's turn;
4. verify any in-place target modification occurs only after explicit adversary acceptance-pending-persistence and preserves the same mathematical claim;
5. verify any materially changed/replacement claim gets a new finding ID rather than `.v2` or silent repurposing;
6. verify the diff contains no unauthorized mind, graph, prior-art, code, experiment, or unrelated changes;
7. ensure every comment or persistence edit materially advances the mathematical dispute;
8. ensure a convergence deletion follows the exact owner/adversary rules above;
9. when an adversarial commit carries `Adversarial-Reviewed-Through`, verify that the SHA is a truthful contiguous coverage boundary and that no eligible finding event through it remains partially reviewed or skipped;
10. never create an empty commit solely to advance adversarial scan coverage.

Review dialogue is not a run log. If nothing material changed, commit nothing.
