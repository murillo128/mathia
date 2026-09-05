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

When a live mathematical question becomes a bounded machine-answerable subproblem worth delegating, load:

```text
.agents/skills/mathia-compute-design/SKILL.md
```

That skill governs whether computation is actually warranted, creation of the self-contained execution issue, and the handoff boundary after which Research Watch returns to ordinary research.

When a canonical finding matures into a stable, high-value Lean theorem target for **verification, reusable formal infrastructure, or structural fertility**, load:

```text
.agents/skills/mathia-formalization-design/SKILL.md
```

A theorem being prior art or classical does not by itself disqualify it from this handoff. The formalization-design skill decides whether the target has enough structural pressure to justify Lean rather than mere transcription. That skill governs deduplication, Gate 0, issue construction, and publication. A ready formalization candidate is handed off directly as a GitHub issue; Research Watch does not maintain a separate Lean-candidate queue.

## Task-specific inputs

Each research-watch prompt should supply only scheduler/runtime identity and any stricter operational override:

- the research line, such as `prime_circle`, `prime_flute`, `prime_lattice`, `weil_positivity`, or `weil_inertia`;
- the stable finding prefix, such as `PC`, `PF`, `PL`, `WP`, or `WI`;
- any notification threshold stricter than the defaults in the loaded skills.

The scheduled prompt must not duplicate or independently redefine the scientific contract. This skill owns **how to investigate, review, persist evidence, and publish it**. The line README owns **what mathematics that line investigates**.

## Canonical line README contract

Every valid Research Watch line must have:

```text
research/<line>/README.md
```

with exactly one `## Research mandate`. The directory path already identifies the line, so do not duplicate an `Identity` section inside the README.

The README is the canonical, externally maintained scientific contract for the line. Keep the same section structure across lines:

```text
## Research mandate

### Primary object
### Objective
### Priority questions
### Scope and exclusions
### Line-specific falsification controls
### Prior-art domains
### Relationship to other lines
```

These sections contain **line-specific mathematics only**:

- `Primary object`: intrinsic construction, definitions, conventions, and fixed mathematical data needed to know what is being studied;
- `Objective`: the durable scientific question or target of the line;
- `Priority questions`: line-specific mechanisms and questions worth attacking;
- `Scope and exclusions`: mathematical boundaries specific to this line;
- `Line-specific falsification controls`: controls, degeneracies, matched models, or no-go tests peculiar to the line;
- `Prior-art domains`: only the mathematical literatures particularly relevant to this line;
- `Relationship to other lines`: only genuine mathematical dependency, upstream/downstream structure, complementarity, or candidate supply relationships.

Do **not** duplicate shared Research Watch procedure in a README. In particular, the README should not restate:

- derive before interpreting;
- try to falsify candidates before publishing;
- treat important negative results as first-class findings;
- assess novelty by mathematical mechanism and equivalent formulation rather than wording;
- prefer primary/authoritative literature;
- generic matched-control, gauge, convergence, or boundary-case discipline already defined below;
- the generic line-local context-isolation procedure defined below;
- evidence labels, finding-ID rules, file maps, persistence rules, publication rules, notification policy, or review protocol;
- current findings, current branch status, research history, or a hand-maintained synthesis of the finding corpus.

A useful placement test is: **if a sentence could be copied unchanged into another research line, it probably belongs in this skill rather than in the README.** Keep only the line-specific specialization in the README.

If the README is missing, lacks the required structure, materially conflicts with itself, or does not define a usable scientific contract, stop rather than inventing or recovering the objective from scheduler memory, chat history, old prompts, graph state, or current findings.

The entire README is **read-only to routine Research Watch runs**. Reorientation, restructuring, or maintenance of the canonical mandate is explicit repository maintenance outside the recurring research cycle.

## Hard line-local read boundary

A Research Watch is deliberately **vertically isolated**. Cross-line synthesis and routing belong to the Master Researcher and Research Mind, not to line-specific watches.

After loading repository-wide procedural authority (`AGENTS.md` and the required skills), the watch's mathematical repository context is restricted to its own line:

```text
research/<line>/README.md
research/<line>/mind/**
research/<line>/findings/**
research/<line>/clues/**
research/<line>/SOURCES.md
```

The local `mind/**` is the preferred compact synthesis of already-persisted line knowledge. It is read-only and is not independent evidence: when a live argument materially depends on one of its claims, trace that claim only to canonical findings or authoritative external literature needed for this line.

Do **not** inspect, search, enumerate, or follow references into:

```text
research/<other-line>/**
research/mind/**
research/clues/**
research/README.md
research/graph/**
research/prior_art/**
```

and do not use another line's README, findings, mind, clues, reviews, SOURCES, or graph state as context/evidence during a Research Watch run. Program-level deduplication, cross-line comparison, and transfer discovery are responsibilities of Master/Mind/Graph roles.

Cross-line knowledge reaches a watch through a **local clue** under `research/<line>/clues/**`. A clue may cite another line's persisted artifact in `based_on` for provenance, but that citation is **not permission to traverse the source line**. Treat the transferred statement as unvalidated motivation and test the proposed analogue independently on the destination line's own object, using authoritative external literature when prior art is required. If the clue is not self-contained enough to perform its decisive test without opening another line, leave it `proposed` and let the Master/Mind strengthen the handoff rather than breaking isolation.

This read boundary overrides any generic clue/review instruction that would otherwise cause a line-specific watch to follow a repository path into another research line. External literature searches remain allowed and required by the prior-art gate.

## Load context progressively and incrementally

Before substantive work:

1. read `AGENTS.md`;
2. read this skill;
3. read `.agents/skills/mathia-research-review/SKILL.md`;
4. read `research/<line>/README.md` and verify that its canonical `## Research mandate` and required sections are present and usable;
5. read the current local `research/<line>/mind/**` when present as the compact starting synthesis;
6. discover the **local** review inbox and recent local evidence changes with targeted search/Git-delta methods; do not enumerate the complete findings corpus merely to establish context;
7. inspect every open local sidecar whose last substantive speaker is `Adversary`; these form the owner's review inbox;
8. inspect `research/<line>/clues/**` when present, using `mathia-research-clues` for their semantics;
9. read `research/<line>/SOURCES.md` when relevant;
10. read only the individual local findings and dependencies needed for the live review, candidate, clue, or local duplication question.

Prefer **delta discovery over corpus inventory**. A directory listing that may return dozens or hundreds of findings is not an acceptable default context-loading strategy. Use filenames/search/commit history narrowly enough to identify the relevant current frontier, and open full findings only when they become mathematically load-bearing. Full filename inspection remains permitted when a publication gate genuinely requires it, such as allocating a new stable ID or validating a deletion/replacement.

Do not preload all findings or complete repository history unless a local dependency, deletion, review, stable-ID, or novelty question genuinely requires it.

When a previous processed revision is available, use Git as a change stream: added, modified, and deleted findings/reviews can all be meaningful events. In particular, `M <finding>.md` may represent newly accepted mathematics for the same claim identity.

## Review inbox comes before optional new exploration

At the start of the mathematical cycle, make a serious attempt to process open reviews owned by this line before spending the run entirely on unrelated exploration.

For each sidecar whose last substantive speaker is `Adversary`:

1. reconstruct the target claim and derivation independently;
2. verify the objection rather than assuming either participant is right;
3. inspect exact local dependencies or authoritative external sources needed to decide it;
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

### 2a. Delegate bounded computation only when it buys information

Do not introduce computation merely because tools are available. Most exact structural arguments are better derived directly.

When a live question has become precise enough that a machine can answer a **bounded subproblem without inventing the next mathematical idea**, consider computational delegation. Useful cases include exact finite counterexample search, symbolic identity checks, matched-control experiments, finite classification, high-precision asymptotic/spectral diagnostics, or another machine test whose possible outcomes would materially alter the research frontier.

In that case load:

```text
.agents/skills/mathia-compute-design/SKILL.md
```

and apply its admission gate. If the gate passes, use its specialization of `design-github-issue` to create one self-contained `execution-ready` GitHub issue for an independent Codex executor.

The issue is a **delegation boundary**, not a new research artifact. After publication:

- do not execute the computation in this Research Watch;
- do not wait for or poll the issue;
- do not create `COMPUTE_CANDIDATES.md`, TODO state, or another queue in the repository;
- do not treat issue creation as evidence or a substantive finding;
- continue ordinary research from current canonical evidence.

A later compute result may re-enter only as a `status: proposed` clue produced under `mathia-compute-executor`; the Research Watch then triages that clue normally and independently.

If the machine task is really a request for more open-ended mathematical reasoning, keep it here instead of delegating it as compute. If the desired durable output is a reusable Lean theorem/proof, use the formalization handoff below rather than the lightweight compute path.

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

Apply the line-specific controls from its README in addition to these shared tests.

Important negative results are first-class research results when they rule out a natural branch, expose hidden universality, or establish a reusable impossibility principle.

This self-audit does not replace the independent `mathia-research-adversarial` process.

### 4. Run a serious prior-art and novelty check

Search the closest classical and modern literature only after the candidate is precise enough to search for. Use the README's `Prior-art domains` as line-specific coverage guidance, not as an exhaustive bibliography.

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

### 5a. Hand off mature Lean formalization targets

After the result has been reconstructed, stress-tested, checked against prior art, and classified, ask whether a canonical finding contains a **stable, bounded theorem surface** whose Lean formalization has material value for verification, reusable formal infrastructure, or **formalization fertility**.

Formalization fertility means that exact proof construction is plausibly useful as a conceptual pressure test even when the target theorem is already classical or known prior art. The expected value is not novelty of the theorem itself, but the possibility that formalization makes the proof's minimal hypotheses, load-bearing intermediate object, asymmetry, factorization, kernel/range structure, quotient, normal form, invariant, or alternate representation explicit enough to generate a new falsifiable question.

Do **not** formalize prior art indiscriminately. Prefer fertility targets where at least one of the following is true:

- the theorem marks an exact structural boundary such as equality, sharpness, rank, kernel/image, dimension, injectivity/surjectivity, extremality, or classification;
- there are multiple materially different human proof representations whose relation is not conceptually settled;
- hypotheses look non-minimal, overly symmetric, or application-specific;
- the proof appears to require a reusable structural lemma or exact finite certificate that the canonical finding does not currently foreground;
- an exceptional/counterexample regime is known but its structural cause remains opaque;
- the same bridge recurs across multiple findings and a minimal formal interface could clarify what is essential.

Routine identities, bulk prior-art transcription, and targets expected to collapse to a direct library theorem with no live structural question should not be delegated merely to increase formal coverage.

A finding is ready for automatic formalization handoff only when all of the following hold:

- the target is grounded in a canonical finding, not merely a clue, review-sidecar argument, transient computation, or speculative direction;
- the intended theorem surface and its important hypotheses can be stated precisely enough for Gate 0;
- the target is finite/bounded enough to be a sensible Lean task without requiring the formalizer to invent the next mathematical idea;
- formalization has material value as verification, reusable infrastructure, or a concrete fertility probe rather than serving only as documentation;
- when fertility is the main motive, the structural question is explicit enough to tell the final reviewer what kind of semantic delta to look for without presupposing that one exists;
- no unresolved adversarial review is likely to materially change the target statement;
- the target is not already controlled by an equivalent Mathia formalization issue or existing completed formal artifact exposing the same structural interface.

Prior-art status is recorded honestly but is **not** itself a rejection criterion. An existing Lean/mathlib formalization that already exposes the same theorem boundary and structural interface normally makes the handoff `reuse-only`; a merely classical human theorem does not.

When the gate passes:

1. load `.agents/skills/mathia-formalization-design/SKILL.md` and its required `design-github-issue` authority;
2. perform the deduplication required by that skill against open/closed Mathia issues and existing formalization artifacts;
3. if no equivalent control object exists, **create the Mathia formalization issue in the same Research Watch run**;
4. reference the exact canonical finding path/ID, isolate the smallest useful theorem boundary, and state the motive as `verification`, `fertility`, or `verification + fertility` when useful;
5. after publication, do not execute Lean here, wait for the issue, poll it, or create a repository candidate queue; continue ordinary research from current evidence.

Do not merely report that something "would be a good Lean candidate" when the gate passes. Issue creation is the required handoff. If GitHub write capability is unavailable or issue publication fails, treat that as a workflow/publication failure under the notification policy.

Issue creation is not evidence and does not by itself satisfy the substantive-finding gate. A later formalization that reports `no material fertility delta found` is still a successful formalization outcome; no clue or discovery is required.

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
- creating a computational delegation or formalization issue without a mathematical result;
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

`clues/` is an optional research-direction inbox governed by `mathia-research-clues`.

Computational delegation and Lean formalization do **not** add repository queues or task-artifact directories to the research line. Their control plane is the GitHub issue created under `mathia-compute-design` or `mathia-formalization-design`. A later compute result may return only as a proposed clue; a later formalization result returns through its controlling issue and the formalization research-handoff contract.

`graph/` is owned by the graph curator. `mind/` is synthesis owned by the Mind. `research/master/` is owned by the Master Researcher. Research Watch does not maintain any of them.

### `README.md`

`README.md` is the canonical line contract defined above, not a mutable research artifact. It contains only the stable line-specific mandate and must not contain:

- a run log or chronology;
- a hand-maintained summary of current findings;
- evidence labels or finding indexes;
- file-map or persistence instructions;
- shared Research Watch procedure.

Routine Research Watch runs never modify `README.md`. Explicit repository maintenance may revise a mandate when the line is intentionally reoriented or the contract structure itself changes.

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
independent durable result                             -> A new finding
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

## Clue consumer and producer behavior

When `research/<line>/clues/**` exists, use `mathia-research-clues` as the authority for triage and lifecycle.

Research Watch consumes only its **local** clue inbox. It does not inspect `research/clues/**` or another line's clues. Master/Mind are responsible for routing any cross-line knowledge that should reach this watch into a destination-local `proposed` clue.

For a local clue whose `based_on` includes another research line, keep that source path as provenance only. Do not open the source-line artifact. Validate or falsify the transferred mechanism independently against the destination line's own construction and authoritative external literature.

Research Watch may create a clue when primary research or a review response exposes a promising question that is not yet a finding. Keep clues explicitly below the evidence threshold.

A clue created by `mathia-compute-executor` is likewise only a proposed research lead. Reconstruct its computational claim independently, respect its exact/numerical/bounded-search evidence boundary, and apply the normal Research Watch derivation, adversarial stress test, and prior-art gate before changing its status or creating a finding.

Global/cross-line clue **creation** is permitted only as defined by `mathia-research-clues` and should be genuinely cross-line. This output permission does not grant permission to read the global clue inbox or another research line.

## Ownership and hard path gate

For a Research Watch on `research/<line>/`, writable evidence is limited to:

```text
research/<line>/SOURCES.md
research/<line>/findings/**
```

`research/<line>/README.md` is deliberately excluded from routine write ownership.

Within `findings/**`, writes to `*.review.md` must obey `mathia-research-review`; ordinary Research Watch ownership does not override turn-taking.

An in-place modification of a target with an open review is allowed **only** in the acceptance-pending-persistence stage defined by `mathia-research-review`, and only when the mathematical claim identity is unchanged.

When `mathia-research-clues` is loaded, its clue-path extension also applies.

Creation of a compute or formalization GitHub issue under `mathia-compute-design` or `mathia-formalization-design` is a control-plane delegation operation, not a repository path write. It grants no additional repository write ownership to Research Watch.

Do **not** write to:

- `research/<line>/README.md`;
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
3. verify no `README.md`, `graph/`, `mind/`, `master/`, code, experiment, or unrelated file changed;
4. verify the update passes the substantive gate;
5. for review changes, verify `mathia-research-review` turn ownership and persistence stage;
6. if updating a reviewed target in place, verify the adversary explicitly accepted the mathematics pending persistence and the claim identity remains the same;
7. if claim identity changes, verify target+sidecar withdrawal and a new non-recycled ID rather than `.v2`;
8. verify `SOURCES.md` agrees with current canonical findings when changed;
9. remove unrelated formatting churn.

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

1. **Workflow/publication failure:** an error, conflict, missing required capability, path/publication-gate failure, or other workflow problem prevents intended persistence or required control-plane handoff.
2. **Extraordinary mathematical success:** a result that materially changes the RH research program or crosses a comparably high bar. Ordinary positives/refinements/classicalizations/closures do not qualify merely because they are persistable.
3. **Clue acceptance:** a clue changes to `status: accepted`.
4. **Owner-side adversarial review events:** every material owner-authored transition defined by `mathia-research-review`, including substantive `Owner` responses, persistence of accepted new mathematics into a finding, concessions, corrections, replacements, independent findings arising from review, and withdrawals.

Do **not** notify for ordinary positive findings, routine negatives/dead ends, ordinary prior-art redirects, routine commits, source additions, compute-issue creation, formalization-issue creation, clue proposal/rejection/resolution, unchanged searches, or unchanged runs.

Do not notify merely because this watch observes an adversary-side review event. The authoring adversarial process owns those notifications, preventing duplicates.

Task-specific prompts should normally inherit this policy rather than restating it.

## Reporting

At the end of a run, surface only notifications allowed above. Persist routine substantive work silently when notification thresholds are not met.

Do not produce project-status recaps, timelines, or daily journals.