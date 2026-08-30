---
name: mathia-research-watch
description: Run recurring Mathia mathematical research watches with durable findings, adversarial review response and persistence, prior-art audit, clue triage, strict path ownership, direct-main publication gates, and low-noise notifications.
---

# Mathia Research Watch

## Responsibility

Use this skill for recurring or scheduled mathematical research watches that maintain one research-evidence line under `research/<line>/`.

The Research Watch owns the line's **canonical findings and evidence**. Its job is to discover, derive, falsify, audit, preserve, strengthen, and, when necessary, withdraw mathematical claims so that later synthesis, graph curation, adversarial review, or formalization can reuse the current corpus.

It does not maintain project status, a changelog, a daily diary, a roadmap, an issue queue, or chronological research notes. It does not write to `mind/`, `graph/`, or `research/master/`.

Every Research Watch must also load:

```text
.agents/skills/mathia-research-review/SKILL.md
```

That skill is the procedural authority for adversarial `.review.md` sidecars, including turn ownership, claim identity, accepted-mathematics persistence, closure, and review-notification ownership.

When local clues exist or the run needs to create/update a clue, also load:

```text
.agents/skills/mathia-research-clues/SKILL.md
```

## Task-specific inputs

Each research-watch prompt should supply only scheduler/runtime identity and any stricter operational override:

- the research line, such as `prime_circle`, `prime_flute`, `prime_lattice`, `weil_positivity`, or `weil_inertia`;
- the stable finding prefix, such as `PC`, `PF`, `PL`, `WP`, or `WI`;
- any notification threshold stricter than the defaults in the loaded skills.

The line's `research/<line>/README.md` owns **what mathematics to investigate**: its canonical `## Research mandate` defines the mathematical object, objective, scope, priorities, exclusions, prior-art surface, and relationship to other lines. The scheduled prompt must not duplicate or independently redefine that scientific contract. This skill owns **how to investigate, handle reviews, persist evidence, and publish it**.

Every valid Research Watch line must therefore have `research/<line>/README.md` with an explicit `## Research mandate`. If it is missing or materially ambiguous, stop rather than inventing or recovering the objective from scheduler memory, chat history, old prompts, or derived state.

Routine Research Watch runs must not modify the `## Research mandate` section. Reorientation of the line is explicit repository maintenance outside the ordinary recurring research cycle. Other stable README context may still be maintained when allowed below.

## Load context progressively

Before substantive work:

1. read `AGENTS.md`;
2. read this skill;
3. read `.agents/skills/mathia-research-review/SKILL.md`;
4. read `research/<line>/README.md` and verify that its canonical `## Research mandate` is present and usable;
5. inventory filenames under `research/<line>/findings/`, distinguishing canonical findings from adjacent `*.review.md` sidecars;
6. inspect every open sidecar whose last substantive speaker is `Adversary`; these form the owner's review inbox;
7. inspect `research/<line>/clues/**` when present, using `mathia-research-clues` for their semantics;
8. read `research/<line>/SOURCES.md` and `LEAN_CANDIDATES.md` when relevant;
9. use `research/<line>/graph/index.md` when present only as derived navigation, never as mathematical evidence;
10. read only the individual findings and dependencies needed for the live review, candidate, clue, or duplication question.

Other Mathia research lines and `mind/` may be read as context or evidence, but are read-only for this role. Treat every `graph/` subtree as regenerable derived state and verify substantive claims against canonical findings or sources.

Do not preload all findings or complete repository history unless a dependency, deletion, review, or novelty question requires it.

When a previous processed revision is available, use Git as a change stream: added, modified, and deleted findings/reviews can all be meaningful events. In particular, `M <finding>.md` may represent newly accepted mathematics for the same claim identity.

## Review inbox comes before optional new exploration

At the start of the mathematical cycle, make a serious attempt to process open reviews owned by this line before spending the run entirely on unrelated exploration.

For each sidecar whose last substantive speaker is `Adversary`:

1. reconstruct the target claim and derivation independently;
2. verify the objection rather than assuming either participant is right;
3. inspect exact dependencies or sources needed to decide it;
4. determine whether this is an ordinary objection turn or an adversary **acceptance-pending-persistence** turn;
5. follow `mathia-research-review` exactly.

### Ordinary owner response

If the objection remains open and the same claim can be defended:

- keep the target unchanged while the defense still awaits adversary judgment;
- append an `## Owner` response with the decisive argument/evidence;
- leave the sidecar for adversary judgment.

If the claim must materially change, concede it instead of rewriting the identity in place:

- delete target + sidecar atomically;
- create a corrected/narrower/replacement result with a **new stable finding ID** when substantive;
- never use `.v2`, `.v3`, or silently repurpose the old ID.

### Owner persistence after adversary acceptance

If the last `## Adversary` turn states that the objection is mathematically resolved but closure is pending durable persistence, the Research Watch must preserve the accepted new mathematics before the sidecar can disappear.

Classify the accepted material using the shared protocol:

**Same mathematical claim:**

1. modify the existing canonical finding in place;
2. integrate the accepted proof/evidence naturally into the claim, derivation, source bridge, boundaries, or audit sections where it belongs;
3. do not add review-history or `Adversarial resolution` prose;
4. append a concise `## Owner` turn confirming that the accepted mathematics is now persisted;
5. leave the sidecar for final adversary verification.

This is the sole exception to the normal rule that a target stays unchanged while a review is open.

**Independent durable result:**

1. keep the target unchanged if its claim remains valid;
2. create a separate new finding with a new stable ID;
3. append a concise owner persistence turn identifying the new result;
4. leave the sidecar for adversary verification.

**Materially changed claim:**

Withdraw the old target and sidecar and create a new finding ID if a replacement remains valuable.

A review response is not fully resolved merely because the mathematics appeared in the temporary sidecar. If that mathematics is necessary to the accepted defense, it must survive in the canonical finding corpus.

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
- finite-versus-infinite products, topology, measure, limiting arguments, and operator-domain assumptions;
- whether a quantity is gauge-, coordinate-, or parametrization-dependent;
- telescoping, coboundary, pure-gauge, quotient, or endpoint-only reductions;
- universal geometric/spectral background that erases arithmetic data;
- local-versus-global information loss;
- whether an apparent symmetry is merely a known functional equation or duality in disguise;
- whether a proposed spectral/geometric object exists with the required hypotheses;
- boundary cases, matched controls, counterexamples, and degenerate instances.

Important negative results are first-class research results when they rule out a natural branch, expose hidden universality, or establish a reusable impossibility principle.

This self-audit does not replace the independent `mathia-research-adversarial` process.

### 4. Run a serious prior-art and novelty check

Search the closest classical and modern literature only after the candidate is precise enough to search for.

Prefer primary papers, monographs, authoritative surveys, or original theorem sources over secondary summaries. Determine separately:

- what theorem or identity is already standard;
- what specialization to the Mathia construction is immediate;
- what consequence was derived here;
- whether the proposed organization or mechanism is genuinely additional structure;
- whether the candidate is only a restatement in new coordinates.

Do not claim novelty because exact wording was not found. Search by mathematical structure, equivalent formulations, and neighboring fields.

### 5. Classify the result honestly

Use the line's established vocabulary when it is more specific. Common evidence labels include:

- `EXACT-DERIVED`;
- `LITERATURE+DERIVED`;
- `CLASSICAL-IDENTITY`;
- `CANDIDATE-NEW-STRUCTURE`;
- `NEGATIVE/OBSTRUCTION` or `DECISIVE-NEGATIVE`;
- `CONJECTURAL`;
- `NEEDS-AUDIT`.

Labels may be combined when needed, but exactness, provenance, novelty, and remaining uncertainty must be unambiguous. Never silently upgrade evidence.

## Substantive-finding gate

Persist a research update only when at least one of these happened materially:

- a new exact or literature-backed mathematical claim was derived;
- a nontrivial candidate mechanism or invariant became precise and falsifiable;
- an important route was disproved or sharply restricted;
- a previous finding was materially corrected, replaced, withdrawn, strengthened, or refuted;
- an adversarial review was materially answered, persisted, or conceded;
- prior art showed that a supposedly new mechanism is classical and materially redirected the investigation;
- a decisive boundary condition, existence condition, or counterexample changed what can plausibly work;
- a clue was substantively triaged under `mathia-research-clues`.

The following are not sufficient by themselves:

- another search pass with no changed conclusion;
- adding a paper that does not change or support a stored claim;
- speculative prose without a precise claim or test;
- renaming/repackaging known zeta or prime identities;
- recording what was attempted today;
- acknowledging an adversarial review without materially answering or persisting it;
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

`LEAN_CANDIDATES.md` is an optional finite formalization queue. `clues/` is an optional research-direction inbox governed by `mathia-research-clues`.

`graph/` is owned by the graph curator. `mind/` is synthesis owned by the Mind. `research/master/` is owned by the Master Researcher. Research Watch does not maintain any of them.

### `README.md`

The README has two roles:

- `## Research mandate` is the canonical, externally maintained scientific contract for the line and is **read-only to routine Research Watch runs**;
- the remaining README may hold stable line context such as conventions, research stance, evidence vocabulary, file map, and durable high-level interpretation.

Do not use any part of the README as a run log. A routine watch may update non-mandate README context only when a substantive finding materially changes that stable interpretation and the edit remains consistent with the canonical mandate.

### Individual findings

New detailed findings belong under:

```text
research/<line>/findings/<PREFIX>-NNN-<slug>.md
```

These are the canonical current source of truth for research claims. Adjacent `*.review.md` files are temporary challenges/dialogue, not replacement evidence.

Use stable three-digit IDs. Before allocating an ID, inspect all existing finding filenames for that prefix and any preserved legacy IDs, then choose an integer greater than every existing ID. Never recycle holes or IDs of findings later deleted through review.

A stable ID denotes a stable **mathematical claim identity**, not an immutable byte sequence:

```text
same claim + stronger/completed accepted proof/evidence -> M existing finding
materially changed/replacement claim                   -> D old + A new ID
independent durable result                             -> A new ID
```

Never create `.v2`/`.v3` finding variants. Git versions the same claim; new IDs represent new claims.

A durable finding should contain, with headings adapted to the mathematics:

1. the precise claim or obstruction;
2. evidence/status classification;
3. derivation, theorem bridge, computation, or falsifying argument;
4. relevance to the Mathia construction;
5. prior-art and novelty assessment;
6. boundary conditions, counterarguments, and failure modes;
7. a decisive falsification/audit test when the claim is not already exact;
8. consequences for the research line.

Preserve enough equations/reasoning that a later researcher or adversary can audit the claim without reconstructing chat or deleted review history.

Do not add special review-history sections. When a review strengthens the same claim, edit the natural mathematical exposition so the current finding is simply the best current version.

### Review sidecars

Review files live adjacent to their targets:

```text
research/<line>/findings/<finding>.review.md
```

Their lifecycle, turn-taking, persistence handshake, deletion semantics, and notification ownership are defined by `mathia-research-review`. Do not invent local variants.

### `SOURCES.md`

Maintain literature anchors used to support or falsify stored findings. Record stable bibliographic information and briefly what theorem/role each source provides. Do not turn it into search history.

### `LEAN_CANDIDATES.md`

When present, keep only high-value finite statements with a natural formal core. Separate local formalizable lemmas from external analytic/spectral theorems that remain assumptions. Formalizability does not upgrade evidence.

## Clue consumer and producer behavior

When `research/<line>/clues/**` exists, use `mathia-research-clues` as the authority for triage and lifecycle.

Research Watch may create a clue when primary research or a review response exposes a promising question that is not yet a finding. Keep clues explicitly below the evidence threshold.

Global/cross-line clue creation is permitted only as defined by `mathia-research-clues` and should be genuinely cross-line.

## Ownership and hard path gate

For a Research Watch on `research/<line>/`, writable evidence is limited to:

```text
research/<line>/README.md            # never alter ## Research mandate in routine runs
research/<line>/SOURCES.md
research/<line>/LEAN_CANDIDATES.md   # only when applicable
research/<line>/findings/**
```

Within `README.md`, the canonical `## Research mandate` is protected from routine Research Watch mutation even though other stable README context remains writable under the substantive gate.

Within `findings/**`, writes to `*.review.md` must obey `mathia-research-review`; ordinary Research Watch ownership does not override turn-taking.

An in-place modification of a target with an open review is allowed **only** in the acceptance-pending-persistence stage defined by `mathia-research-review`, and only when the mathematical claim identity is unchanged.

When `mathia-research-clues` is loaded, its clue-path extension also applies.

Do **not** write to:

- `research/<line>/graph/**`;
- `research/<line>/mind/**`;
- `research/mind/**`;
- `research/master/**`;
- another line's evidence;
- `research/prior_art/**` unless another explicit skill grants it;
- `docs/`, `experiments/`, code, tests, prompts, or unrelated repository files.

## Publication policy

Scheduled Research Watches publish substantive research-knowledge improvements directly to the repository default branch. They do not open a PR for routine evidence/review maintenance.

Before every commit:

1. refresh the default branch and inspect the complete planned diff;
2. verify every changed path is inside the allowed evidence/clue/review area;
3. verify no `graph/`, `mind/`, `master/`, code, experiment, or unrelated file changed;
4. if `README.md` changed, verify the canonical `## Research mandate` is byte-for-byte unchanged from the run's base revision;
5. verify the update passes the substantive gate;
6. for review changes, verify `mathia-research-review` turn ownership and persistence stage;
7. if updating a reviewed target in place, verify the adversary explicitly accepted the mathematics pending persistence and the claim identity remains the same;
8. if claim identity changes, verify target+sidecar withdrawal and a new non-recycled ID rather than `.v2`;
9. verify `README.md`, `SOURCES.md`, or `LEAN_CANDIDATES.md` agree with current canonical findings;
10. remove unrelated formatting churn.

Research-watch commits use:

```text
research(<line>): <mathematical outcome>
```

Examples:

```text
research(prime_circle): rule out projective Hill spectrum
research(prime_flute): persist critical-line cusp defense
research(prime_lattice): withdraw invalid mixing claim
```

Use `research:` only for repository-level maintenance of shared research machinery. Do not use a bare line-name prefix.

If no substantive mathematical or review outcome improved, do not commit merely to prove the task ran.

## Notification policy

Persistence and notification are separate thresholds. The default Research Watch channel is a **low-noise interruption channel**, except that adversarial review remains fully observable while the protocol is being validated.

Notify only for:

1. **Workflow/publication failure:** an error, conflict, missing required capability, path/publication-gate failure, or other workflow problem prevents intended persistence.
2. **Extraordinary mathematical success:** a result that materially changes the RH research program or crosses a comparably high bar. Ordinary positives/refinements/classicalizations/closures do not qualify merely because they are persistable.
3. **Clue acceptance:** a clue changes to `status: accepted`.
4. **Owner-side adversarial review events:** every material owner-authored transition defined by `mathia-research-review`, including substantive `Owner` responses, persistence of accepted new mathematics into a finding, concessions, corrections, replacements, independent findings arising from review, and withdrawals.

Do **not** notify for ordinary positive findings, routine negatives/dead ends, ordinary prior-art redirects, routine commits, source additions, clue proposal/rejection/resolution, unchanged searches, or unchanged runs.

Do not notify merely because this watch observes an adversary-side review event. The authoring adversarial process owns those notifications, preventing duplicates.

Task-specific prompts should normally inherit this policy rather than restating it.

## Reporting

At the end of a run, surface only notifications allowed above. Persist routine substantive work silently when notification thresholds are not met.

Do not produce project-status recaps, timelines, or daily journals.