---
name: mathia-research-adversarial
description: Run recurring adversarial review over Mathia research findings using the shared sidecar review protocol, without modifying the claims being reviewed.
---

# Mathia Adversarial Research

## Responsibility

Use this skill for a recurring or scheduled **Adversarial Research** pass over Mathia's persisted research findings.

The adversary is a mathematical peer reviewer, not the owner of the claims it audits. Its job is to find concrete reasons why a stored finding may be false, overstated, under-specified, classical rather than novel, dependent on a hidden assumption, or otherwise unsafe to treat at its current strength.

The adversary does **not** rewrite findings and does not maintain the Mathia mind, graph, prior-art projection, or project status. It communicates challenges through adjacent `.review.md` sidecars governed by:

```text
.agents/skills/mathia-research-review/SKILL.md
```

Load that skill before doing substantive review work. When a review exposes a genuinely separate research lead, also load:

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

1. **Owner replies waiting for adversary judgment.** Re-evaluate and either close the review by deleting the sidecar or append the next adversary turn.
2. **New or changed findings.** Audit claims that appeared since the previous adversarial pass.
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

Follow the sidecar naming, dialogue format, turn ownership, and convergence rules in `mathia-research-review` exactly.

## Re-evaluating an owner response

When the last substantive speaker in a sidecar is `Owner`, do not defend the original objection automatically. Reconstruct the issue again using the owner's response.

If the response resolves the objection, delete only the `.review.md` file. Do not edit the finding and do not add an "approved" marker.

If a material problem remains, append a new `## Adversary` section containing only the unresolved issue or a materially stronger objection.

If the owner has withdrawn the target and sidecar, there is nothing to close. Git history is the record of convergence.

## Clues from adversarial friction

A review sometimes exposes a mathematically interesting direction that is orthogonal to whether the target survives. In that case, use `mathia-research-clues` rather than bloating the review thread.

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
3. verify every review path exactly corresponds to a current target finding;
4. verify turn ownership for every modified sidecar;
5. verify no canonical finding or forbidden path changed;
6. verify every new/continued objection is material and non-duplicative;
7. verify any deleted sidecar is being closed because the owner's response actually resolved the objection.

Use the commit prefix:

```text
research(adversarial): <review outcome>
```

Examples:

```text
research(adversarial): challenge prime-circle spectrum claim
research(adversarial): close resolved Bohr-flow review
research(adversarial): tighten convergence objection
```

Do not commit merely to record that a scheduled adversarial pass ran or that several findings looked correct.

## Reporting

Report only material events:

- a new serious review was opened;
- an owner response was accepted and the review closed;
- an objection survived and was materially sharpened;
- a review exposed an unusually consequential clue.

If no material objection or response exists, create no repository churn and keep reporting concise.
