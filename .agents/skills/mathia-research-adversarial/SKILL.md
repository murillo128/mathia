---
name: mathia-research-adversarial
description: Run recurring adversarial review over Mathia research findings using the shared sidecar protocol, without modifying canonical claims and while ensuring accepted new mathematics is durably persisted before closure.
---

# Mathia Adversarial Research

## Responsibility

Use this skill for a recurring or scheduled **Adversarial Research** pass over Mathia's persisted research findings.

The adversary is a mathematical peer reviewer, not the owner of the claims it audits. Its job is to find concrete reasons why a stored finding may be false, overstated, under-specified, classical rather than novel, dependent on a hidden assumption, or otherwise unsafe to treat at its current strength.

The adversary does **not** rewrite findings and does not maintain the Mathia mind, graph, prior-art projection, or project status. It communicates challenges through adjacent `.review.md` sidecars governed by:

```text
.agents/skills/mathia-research-review/SKILL.md
```

Load that skill before doing substantive review work. Its review lifecycle, durable-math persistence rules, and notification ownership are authoritative. When a review exposes a genuinely separate research lead, also load:

```text
.agents/skills/mathia-research-clues/SKILL.md
```

The current version reviews Research-Watch-owned findings only. Do **not** review or modify `mind/**` yet.

## Discover review scope dynamically

Do not hard-code research-line names.

At the start of every run, inspect direct children of:

```text
research/
```

A directory `research/<line>/` participates when it contains canonical findings under:

```text
research/<line>/findings/
```

Exclude repository-level infrastructure such as:

```text
research/prior_art/
research/graph/
research/mind/
research/master/
research/clues/
```

Within each participating line, canonical review targets are ordinary finding files matching the Research Watch convention and excluding `*.review.md`.

## Load context progressively

Before substantive work:

1. read `AGENTS.md`;
2. read this skill;
3. read `.agents/skills/mathia-research-review/SKILL.md`;
4. discover research lines structurally;
5. inventory finding filenames and existing `.review.md` sidecars without preloading every finding;
6. first inspect open reviews whose last substantive speaker is `Owner`;
7. then identify newly added or materially changed findings since the previous adversarial publication when Git history makes that boundary available;
8. read only the exact findings, dependencies, sources, and neighboring claims needed for a serious audit.

If no previous adversarial commit exists, treat the existing corpus as an initial backlog and review it progressively, prioritizing mathematically consequential or high-confidence claims rather than creating shallow reviews for everything at once.

The absence of an adversarial commit or sidecar is not an approval certificate.

## Review order

Use this order unless a task-specific prompt gives a stronger reason otherwise:

1. **Owner replies waiting for adversary judgment.** Re-evaluate and either continue the objection, close the review, or accept the mathematics pending durable persistence according to `mathia-research-review`.
2. **New or changed findings.** Audit claims that appeared or were materially strengthened since the previous adversarial pass. A Git `M <finding>.md` is a real new-evidence event even when the finding ID is unchanged.
3. **High-value unaudited backlog.** When capacity remains, attack older findings whose failure would materially affect a research line or several downstream claims.

Do not create repository churn merely to mark a finding as reviewed. A clean audit with no material objection produces no sidecar.

## Adversarial research method

Try to falsify before trying to improve the claim. Reconstruct enough mathematics to make the objection independent of the original author's reasoning.

Check, when relevant:

- definitions, quantifiers, indexing, normalization, constants, signs, branch choices, and domains;
- convergence regions versus analytic continuation;
- finite/infinite limiting transitions and hidden compactness/completeness assumptions;
- existence and domains of operators, measures, spectra, transforms, or geometric structures;
- boundary cases, degenerate instances, counterexamples, and simple controls;
- gauge, coordinate, parametrization, or representation dependence;
- telescoping, coboundary, endpoint-only, quotient, or information-loss reductions;
- whether the mechanism is universal background rather than specific to primes/the line's construction;
- local-versus-global information loss;
- whether a claimed implication actually follows from the derived identity;
- whether a numerical pattern is being promoted beyond what the computation establishes;
- whether a literature theorem has stronger hypotheses than the finding records;
- whether the novelty claim is contradicted by equivalent formulations or known prior art;
- whether the evidence/status label is stronger than the stored proof/source bridge warrants.

Important negative checks are useful only when they are precise. "This seems doubtful" is not an adversarial result.

## Lightweight hallucination and line-integrity scan

As a small part of the normal adversarial pass, perform a **lightweight sniff test** over the material already being inspected for signs that a research session may be hallucinating or that an unsupported premise may be propagating through a line. This is not a separate corpus audit and must not create persistent health state, scores, logs, or routine repository churn.

Cheap signals worth noticing include, when they arise naturally:

- a citation, theorem attribution, or source bridge that cannot be recovered or does not support the claim attributed to it;
- a claim that becomes materially stronger across artifacts without corresponding new evidence;
- contradiction with current canonical findings or accepted review outcomes that the line appears not to notice;
- repeated reuse of a premise that has already been invalidated, withdrawn, or left unsupported;
- definitions or notation drifting so later reasoning no longer concerns the same mathematical object;
- a dependency chain that relies on purported persisted mathematics which is not actually present in the repository or cited source.

A weak suspicion produces **no repository change**: no sidecar, clue, status marker, or notification. Do not classify a speculative hypothesis as hallucination merely because it is unproved and correctly labelled as speculative.

If a material signal appears, perform a focused deeper check only around the suspicious source, claim, and dependency chain. Prefer authoritative sources, current canonical artifacts, Git-visible withdrawals/corrections, and exact neighboring dependencies. Distinguish an ordinary local mathematical error, which belongs in the normal `.review.md` protocol, from a broader integrity concern suggesting that the line may be repeatedly building on unsupported or invented context.

Only when that focused check confirms a credible **line-level integrity risk** should the adversary load `mathia-research-clues` and create or materially strengthen one `status: proposed`, `origin: adversarial` clue. Encode the warning as a concrete falsifiable revalidation question compatible with the clue schema, preferably local to the affected line and global only when the suspected contamination crosses lines. The clue must cite the persisted artifacts or source mismatch that triggered it, state the precise suspected failure mode and potentially affected dependency scope, give a decisive revalidation test, and make clear in `Evidence boundary` that the warning is not itself proof that the line is corrupted.

The purpose of this exceptional clue is to make the integrity warning visible to the Master Researcher and the owning Research Watch without creating a parallel monitoring system. The adversary must not write a health score, restart marker, audit report, or automatic reset instruction. It supplies evidence and a falsifiable check; downstream research governance decides what strategic action, if any, follows.

## Prior-art use

A material novelty or theorem objection may require literature checking. Prefer primary papers, monographs, authoritative surveys, or original theorem statements.

Search by mathematical structure and equivalent formulation, not merely by the exact vocabulary used in the finding.

If the objection depends on a source, identify the exact theorem/statement and explain the mismatch in the review. Do not turn the review into a literature dump.

## Gate for opening a review

Open a `.review.md` sidecar only when there is a concrete mathematical or epistemic issue whose resolution could change whether the target should survive in its current form or at its current strength.

A good initial review states:

1. the exact target claim under attack;
2. the strongest argument, counterexample, missing hypothesis, or source conflict found;
3. why it is material;
4. what evidence or derivation would resolve the objection when known.

Do not open reviews for prose style, optional exposition, preference for another approach, or speculative research ideas that do not actually undermine the claim.

Follow the sidecar naming, dialogue format, turn ownership, convergence, durable-persistence, and notification rules in `mathia-research-review` exactly.

## Re-evaluating an owner response

When the last substantive speaker in a sidecar is `Owner`, do not defend the original objection automatically. Reconstruct the issue again using the owner's response and the current canonical finding.

There are three outcomes.

### Objection remains

Append a new `## Adversary` section containing only the unresolved issue or a materially stronger objection.

### Objection resolved with no missing durable mathematics

If the owner response merely clarifies or recombines mathematics already present in the current finding, delete only the `.review.md` sidecar. Do not edit the finding and do not add an approval marker.

### Objection resolved but accepted mathematics is not yet canonical

If the owner supplied a new proof step, boundary argument, source bridge, hypothesis analysis, or independent result that is necessary to the accepted resolution and is **not yet durably present in the current finding corpus**, do **not** delete the sidecar.

Append a concise `## Adversary` turn stating that the objection is mathematically resolved but closure is pending persistence, and identify the mathematical content that must be materialized. This returns the turn to the owner.

The owner then follows `mathia-research-review`:

- same claim -> update the existing finding in place and append an owner persistence turn;
- independent durable result -> create a new finding ID and append an owner persistence turn;
- materially changed claim -> withdraw the old finding and sidecar and use a new finding ID when warranted.

Never request `.v2`, `.v3`, review-history sections, or other versioned claim files.

## Final persistence verification

When the last speaker is `Owner` after an adversary acceptance-pending-persistence turn, verify the current tree rather than trusting the acknowledgement.

If the same claim was updated in place, confirm that the accepted mathematics is naturally integrated into the canonical finding and does not silently strengthen/change the claim identity.

If an independent result was created, confirm that the new finding actually preserves the durable mathematical content needed by the accepted defense.

If verification passes, delete only the `.review.md` sidecar. If persistence introduced a material mathematical issue, append another `## Adversary` turn.

If the owner instead withdrew the target and sidecar because the claim identity changed, there is nothing further to close; Git records the convergence.

## Clues from adversarial friction

A review sometimes exposes a mathematically interesting direction orthogonal to whether the target survives. In that case use `mathia-research-clues` rather than bloating the review thread.

The adversary may propose:

```text
research/<line>/clues/**
```

for a clue naturally owned by an existing line, or:

```text
research/clues/**
```

for a genuinely cross-line or new-line candidate, subject to the clue skill's schema, deduplication, and evidence-boundary rules.

The clue must cite the target/review paths that motivated it and must remain a research question, not a disguised finding.

The lightweight line-integrity scan above is the only additional case in which an adversarial clue may be used: it must remain a falsifiable revalidation question rather than a verdict or process-status record.

## Ownership and hard path gate

The adversary may write only the review sidecars authorized by `mathia-research-review`:

```text
research/<line>/findings/*.review.md
```

and, only when `mathia-research-clues` is also loaded, clue files authorized there.

It must never modify or delete:

```text
research/<line>/findings/<claim>.md
research/<line>/README.md
research/<line>/SOURCES.md
research/<line>/LEAN_CANDIDATES.md
research/<line>/mind/**
research/mind/**
research/**/graph/**
research/prior_art/**
research/master/**
docs/**
experiments/**
code/tests/prompts outside this skill's ownership
```

The adversary may read those sources as needed, but reading does not grant write authority.

## Publication policy

A scheduled adversarial pass may publish substantive sidecar/clue changes directly to the repository default branch when all path and protocol gates pass.

Before every commit:

1. refresh the default branch and ensure the target has not changed or disappeared while being reviewed;
2. inspect the complete diff;
3. verify every review path exactly corresponds to a current target finding unless the owner already withdrew target+sidecar;
4. verify turn ownership for every modified sidecar;
5. verify no canonical finding or forbidden path changed;
6. verify every new/continued objection is material and non-duplicative;
7. before deleting a sidecar, verify either that the accepted defense required no new durable mathematics or that any required new mathematics has already been persisted and checked;
8. never close a review while the strongest accepted argument exists only in the sidecar/Git history.

Use the commit prefix:

```text
research(adversarial): <review outcome>
```

Examples:

```text
research(adversarial): challenge prime-circle spectrum claim
research(adversarial): accept cusp defense pending persistence
research(adversarial): close persisted Bohr-flow review
research(adversarial): tighten convergence objection
```

Do not commit merely to record that a scheduled adversarial pass ran or that several findings looked correct.

## Notification policy

For adversarial-review activity, follow `mathia-research-review` in full-observability mode. This task notifies for every material adversary-side event it authors:

- opening a new review sidecar;
- every substantive follow-up `Adversary` turn;
- provisional acceptance pending durable persistence;
- closing/deleting a sidecar after the owner's response or persistence resolves the objection.

Also notify when a workflow/publication error prevents the adversarial process from completing or persisting its intended work correctly.

Do not notify for clean audits with no objection, merely observing an owner response before acting on it, ordinary findings that survive audit, clue creation/strengthening, routine commits, or unchanged runs. Owner-authored review events are notified by the owning Research Watch according to `mathia-research-review`; do not duplicate them.

Task-specific prompts should normally inherit this policy rather than restating it.

## Reporting

Surface only notifications permitted by the notification policy above. The repository sidecar remains temporary review state; accepted mathematical content must survive in canonical findings when required by the shared protocol.
