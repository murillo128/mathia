---
name: mathia-research-watch
description: Run recurring Mathia mathematical research watches with durable findings, adversarial review response, prior-art audit, clue triage, strict path ownership, direct-main publication gates, and low-noise notifications.
---

# Mathia Research Watch

## Responsibility

Use this skill for recurring or scheduled mathematical research watches that maintain one research-evidence line under `research/<line>/`.

The Research Watch owns the line's **canonical findings and evidence**. Its job is to discover, derive, falsify, audit, preserve, and, when necessary, withdraw mathematical claims so that later synthesis, graph curation, adversarial review, or formalization can reuse the current corpus.

It does not maintain project status, a changelog, a daily diary, a roadmap, an issue queue, or chronological research notes. It does not write to `mind/` or `graph/`.

Every Research Watch must also load:

```text
.agents/skills/mathia-research-review/SKILL.md
```

That skill is the procedural authority for responding to adversarial `.review.md` sidecars attached to this line's findings, including review-notification ownership.

When local clues exist or the run needs to create/update a clue, also load:

```text
.agents/skills/mathia-research-clues/SKILL.md
```

## Task-specific inputs

Each research-watch prompt should supply only the topic-specific contract:

- the research line, such as `prime_circle`, `prime_flute`, or `prime_lattice`;
- the stable finding prefix, such as `PC`, `PF`, or `PL`;
- the mathematical object and questions to investigate;
- any branch-specific definitions, known results, priority mechanisms, or exclusions;
- any notification threshold stricter than the default in this skill.

The prompt owns **what mathematics to investigate**. This skill owns **how to investigate, handle reviews, persist evidence, and publish it**.

## Load context progressively

Before substantive work:

1. read `AGENTS.md`;
2. read this skill;
3. read `.agents/skills/mathia-research-review/SKILL.md`;
4. read `research/<line>/README.md` when present;
5. inventory filenames under `research/<line>/findings/`, distinguishing canonical findings from adjacent `*.review.md` sidecars;
6. inspect every open sidecar whose last substantive speaker is `Adversary`; these form the owner's review inbox;
7. inspect `research/<line>/clues/**` when present, using `mathia-research-clues` for their semantics;
8. read `research/<line>/SOURCES.md` and `LEAN_CANDIDATES.md` when relevant;
9. use `research/<line>/graph/index.md` when present only as a derived navigation aid, never as mathematical evidence;
10. read only the individual findings and dependencies needed for the live review, candidate, clue, or duplication question.

Other Mathia research lines and `mind/` may be read as context or evidence, but are read-only for this role. Treat every `graph/` subtree as regenerable derived state and verify substantive claims against canonical findings or sources.

Do not preload all findings or complete repository history unless a dependency, deletion, review, or novelty question requires it.

When a previous processed revision is available, use Git history as a change stream: added, modified, and deleted findings/reviews can all be meaningful events. Do not assume that only files present in the current tree can represent new information.

## Review inbox comes before optional new exploration

At the start of the mathematical cycle, make a serious attempt to process open reviews on findings owned by this line before spending the run entirely on unrelated exploration.

For each sidecar whose last substantive speaker is `Adversary`:

1. reconstruct the target claim and derivation independently;
2. verify the objection rather than assuming either participant is right;
3. inspect exact dependencies or sources needed to decide it;
4. follow `mathia-research-review` exactly.

The owner has two main outcomes:

- **Defend:** keep the target unchanged, append an `## Owner` response with the decisive argument/evidence, and leave the sidecar for adversary judgment.
- **Concede:** delete the target finding and its sidecar in the same commit. If a corrected/narrower result remains valuable, publish it as a new finding with a new stable ID instead of silently repurposing the withdrawn claim.

Do not edit the target finding while its `.review.md` sidecar is open. Do not delete a sidecar merely because an owner response has been written. Closure after a defense belongs to the adversary.

If the objection cannot yet be materially answered, leave the sidecar untouched rather than add a placeholder response.

A review discussion may expose a separate useful research direction. In that case use `mathia-research-clues`; do not bury a cross-cutting lead in the review thread.

## Research cycle

### 1. Reconstruct the exact object

Start from the line's intrinsic mathematical construction and conventions. Check definitions, normalizations, indexing, domains, degeneracies, and which structure is genuinely present rather than imported by analogy.

Do not begin by wrapping a known zeta identity, generating function, operator, or transform around the data and calling the reformulation a mechanism.

### 2. Derive before interpreting

Prefer exact identities, invariants, reductions, controlled asymptotics, operator relations, explicit counterexamples, or obstructions before broad spectral or geometric analogies.

Numerical experiments may suggest or falsify a claim, but numerical coincidence is not a durable finding unless the task explicitly studies an empirical law. Preserve the distinction between exact derivation, literature theorem, computation, heuristic, conjecture, and proof-search failure.

### 3. Stress-test adversarially before publishing

Try to kill a candidate before promoting it. Check, when relevant:

- constants, signs, branch choices, normalization factors, and quantifiers;
- convergence domains and whether a claimed identity survives analytic continuation;
- finite-versus-infinite product, topology, measure, limiting, or operator-domain assumptions;
- whether a quantity is gauge-, coordinate-, or parametrization-dependent;
- telescoping, coboundary, pure-gauge, quotient, or endpoint-only reductions;
- universal geometric/spectral background that erases the arithmetic data;
- local-versus-global information loss;
- whether an apparent symmetry is merely a known functional equation or duality in disguise;
- whether a proposed spectral/geometric object exists with the required hypotheses;
- boundary cases, controls, counterexamples, and degenerate instances.

Important negative results are first-class research results when they rule out a natural branch, expose hidden universality, or establish a reusable impossibility principle.

This self-audit does not replace the independent `mathia-research-adversarial` process.

### 4. Run a serious prior-art and novelty check

Search the closest classical and modern literature only after the mathematical candidate is precise enough to search for.

Prefer primary papers, monographs, authoritative surveys, or original theorem sources over secondary summaries. Determine separately:

- what theorem or identity is already standard;
- what specialization to the Mathia construction is immediate;
- what consequence was derived here;
- whether the proposed organization or mechanism is genuinely additional structure;
- whether the candidate is only a restatement in new coordinates.

Do not claim novelty because exact wording was not found. Search by mathematical structure, equivalent formulations, and neighboring fields.

### 5. Classify the result honestly

Use the line's established vocabulary when it is more specific. The common evidence vocabulary is:

- `EXACT-DERIVED` — exact consequence derived from the explicit Mathia construction;
- `LITERATURE+DERIVED` — a published theorem plus a derived consequence for this construction;
- `CLASSICAL-IDENTITY` — exact but already standard;
- `CANDIDATE-NEW-STRUCTURE` — a potentially new organization/mechanism whose novelty is not established;
- `NEGATIVE/OBSTRUCTION` or `DECISIVE-NEGATIVE` — a tempting route is ruled out or materially narrowed;
- `CONJECTURAL` — depends on an unproved mechanism or statistical hypothesis;
- `NEEDS-AUDIT` — a promising claim still lacks a reliable proof/source bridge.

Labels may be combined when needed, but exactness, provenance, novelty, and remaining uncertainty must be unambiguous. Never silently upgrade evidence.

## Substantive-finding gate

Persist a research update only when at least one of these happened materially:

- a new exact or literature-backed mathematical claim was derived;
- a nontrivial candidate mechanism or invariant became precise and falsifiable;
- an important route was disproved or sharply restricted;
- a previous finding was materially corrected, replaced, withdrawn, strengthened, or refuted;
- an adversarial review was materially answered or conceded;
- prior art showed that a supposedly new mechanism is classical and materially redirected the investigation;
- a decisive boundary condition, existence condition, or counterexample changed what can plausibly work;
- a clue was substantively triaged under `mathia-research-clues`.

The following are not sufficient by themselves:

- another search pass with no changed conclusion;
- adding a paper that does not change or support a stored claim;
- speculative prose without a precise claim or test;
- renaming or repackaging known zeta/prime identities;
- recording what was attempted today;
- acknowledging an adversarial review without materially answering it;
- updating a timestamp, status diary, TODO, or next-step log.

If nothing passes the gate, create no repository churn.

## Evidence storage contract

The canonical evidence root is:

```text
research/<line>/
```

Core artifacts are:

```text
README.md
SOURCES.md
findings/
```

`LEAN_CANDIDATES.md` is an optional adjunct for a deliberately small formalization queue. `clues/` is an optional research-direction inbox governed by `mathia-research-clues`.

`graph/` is a derived view owned by the graph curator. `mind/` is synthesis owned by the mind process. Research Watch does not maintain either.

Legacy lines may predate one of the core artifacts or contain historical finding expositions outside `findings/`. Preserve such history unless a separate migration owns it. Do not create empty placeholders for symmetry.

### `README.md`

Keep stable line context only: primary mathematical object, conventions, research stance, evidence vocabulary, file map, and durable high-level interpretation. Do not use it as a run log.

### Individual findings

New detailed findings belong under:

```text
research/<line>/findings/<PREFIX>-NNN-<slug>.md
```

These files are the canonical source of truth for research claims. Adjacent `*.review.md` files are challenges/dialogue, not replacement evidence.

Use stable three-digit IDs. Before allocating an ID, inspect all existing finding filenames for that prefix and any explicitly preserved legacy IDs for the same line, then choose an integer greater than every existing ID. Never recycle holes or renumber existing findings, including IDs of findings later deleted through review. Git history preserves those identities.

Prefer one coherent finding over near-duplicates. A graph index may help locate candidates, but duplication decisions must be verified against canonical findings.

A durable finding should contain, with headings adapted to the mathematics:

1. the precise claim or obstruction;
2. evidence/status classification;
3. the derivation, theorem bridge, computation, or falsifying argument;
4. why the result is specific or relevant to the Mathia construction;
5. prior art and novelty assessment;
6. boundary conditions, counterarguments, and known failure modes;
7. a decisive falsification/audit test when the claim is not already exact;
8. consequences for the research line.

Preserve enough equations and reasoning that a later researcher or adversary can audit the claim without reconstructing the original chat.

Substantive changes to an existing published finding are discoverable through Git and must not silently change the identity into a different claim. In particular, never edit a finding while it has an open review. If a review forces a materially different claim, withdraw the old target and create a new finding ID as defined by `mathia-research-review`.

Minor exposition/source clarifications that leave the mathematical claim unchanged may update the existing finding normally when useful.

### Review sidecars

Review files live adjacent to their targets:

```text
research/<line>/findings/<finding>.review.md
```

Their complete lifecycle, ownership, turn-taking, deletion semantics, and notification ownership are defined only by `mathia-research-review`. Do not invent local variants.

### `SOURCES.md`

Maintain the literature anchors used to support or falsify stored findings. Record stable bibliographic information and, briefly, what theorem/role the source provides.

Do not turn `SOURCES.md` into a search history or reading diary. A source belongs there when it is a durable dependency or important novelty/prior-art anchor.

### `LEAN_CANDIDATES.md`

When present, keep only high-value finite statements with a natural formal core. Separate the local lemma that Lean can reasonably prove from any external analytic or spectral theorem that must remain an explicit assumption.

Formalizability does not upgrade mathematical evidence.

## Clue consumer and producer behavior

When `research/<line>/clues/**` exists, use `mathia-research-clues` as the authority for triage and lifecycle.

The Research Watch may also create a clue when its own research or a review response exposes a promising question that is not yet a finding. Keep the clue explicitly below the evidence threshold; do not use clues to avoid the finding gate.

Global/cross-line clue creation is permitted only as defined by `mathia-research-clues` and should be rare and genuinely cross-line.

## Ownership and hard path gate

For a Research Watch on `research/<line>/`, the writable evidence area is limited to:

```text
research/<line>/README.md
research/<line>/SOURCES.md
research/<line>/LEAN_CANDIDATES.md   # only when applicable
research/<line>/findings/**
```

Within `findings/**`, writes to `*.review.md` must obey `mathia-research-review`; ordinary Research Watch ownership does not override the review turn protocol.

When `mathia-research-clues` is loaded, its explicit clue-path extension also applies.

Do **not** write to:

- `research/<line>/graph/**`;
- `research/<line>/mind/**`;
- `research/mind/**`;
- another research line's evidence;
- `research/prior_art/**` unless another explicit skill grants it;
- `docs/`, `experiments/`, code, tests, prompts, or unrelated repository files.

If a candidate requires a code/experiment change, record the mathematical need in a finding or clue when substantive, but do not cross the ownership boundary without a separate task.

## Publication policy

Scheduled Mathia Research Watches publish substantive research-knowledge improvements directly to the repository default branch. They do not open a PR for routine evidence/review maintenance.

Before every commit:

1. refresh the default branch and inspect the complete planned diff;
2. verify every changed path is inside the allowed evidence/clue/review area;
3. verify no `graph/`, `mind/`, code, experiment, or unrelated file changed;
4. verify the update passes the substantive gate;
5. for review changes, verify `mathia-research-review` turn ownership and convergence rules;
6. when conceding a review, verify the target and sidecar disappear atomically and any replacement claim has a new non-recycled ID;
7. verify `README.md`, `SOURCES.md`, or `LEAN_CANDIDATES.md` updates agree with the current canonical findings;
8. remove unrelated formatting churn.

Research-watch commits use:

```text
research(<line>): <mathematical outcome>
```

Examples:

```text
research(prime_circle): rule out projective Hill spectrum
research(prime_flute): answer cusp-universality review
research(prime_lattice): withdraw invalid mixing claim
```

Use `research:` only for repository-level maintenance of shared research machinery. Do not use a bare line-name prefix.

If no substantive mathematical or review outcome improved, do not commit merely to prove the task ran.

## Notification policy

Persistence and notification are deliberately separate thresholds. The default Research Watch notification channel is a **low-noise interruption channel**, not a mirror of normal research activity.

Notify only for:

1. **Workflow/publication failure:** an error, conflict, missing required capability, path/publication-gate failure, or other workflow problem prevents the run from completing its intended research/review persistence correctly.
2. **Extraordinary mathematical success:** a result that materially changes the RH research program or crosses a comparably high bar. Ordinary positive findings, useful refinements, classicalizations, and routine branch closures do not qualify merely because they are substantive enough to persist.
3. **Clue acceptance:** a clue changes to `status: accepted`. Do not notify merely for clue proposal, rejection, or resolution; the resulting durable finding, when any, is governed by the ordinary research threshold above.
4. **Owner-side adversarial review events:** every material review-state change authored by this Research Watch, exactly as defined by `mathia-research-review`, including each substantive `Owner` response and any concession, correction, replacement, or withdrawal caused by review.

Do **not** notify for ordinary positive findings, routine negative results or dead-end/branch closures, routine prior-art redirects, ordinary commits, source additions, clue proposal/rejection/resolution, unchanged searches, or unchanged runs.

Do not notify merely because this watch observes an adversary-side review event. The authoring `mathia-research-adversarial` process owns those notifications under `mathia-research-review`, which prevents duplicate alerts.

A task-specific prompt may impose a stricter threshold, but should normally inherit this section instead of restating it.

## Reporting

At the end of a run, persist and internally summarize whatever the research workflow needs, but surface a user-facing notification only when the notification policy above fires. Review notifications must follow the exact event ownership in `mathia-research-review`.

Do not produce a project-status recap, timeline, daily journal, or routine success/closure message.
