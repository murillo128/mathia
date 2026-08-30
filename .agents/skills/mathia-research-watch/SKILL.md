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
- the generic rule that other research lines are read-only context/evidence;
- evidence labels, finding-ID rules, file maps, persistence rules, publication rules, notification policy, or review protocol;
- current findings, current branch status, research history, or a hand-maintained synthesis of the finding corpus.

A useful placement test is: **if a sentence could be copied unchanged into another research line, it probably belongs in this skill rather than in the README.** Keep only the line-specific specialization in the README.

If the README is missing, lacks the required structure, materially conflicts with itself, or does not define a usable scientific contract, stop rather than inventing or recovering the objective from scheduler memory, chat history, old prompts, graph state, or current findings.

The entire README is **read-only to routine Research Watch runs**. Reorientation, restructuring, or maintenance of the canonical mandate is explicit repository maintenance outside the recurring research cycle.

## Load context progressively

Before substantive work:

1. read `AGENTS.md`;
2. read this skill;
3. read `.agents/skills/mathia-research-review/SKILL.md`;
4. read `research/<line>/README.md` and verify that its canonical `## Research mandate` and required sections are present and usable;
5. inventory filenames under `research/<line>/findings/`, distinguishing canonical findings from adjacent `*.review.md` sidecars;
6. inspect every open sidecar whose last substantive speaker is `Adversary`; these form the owner's review inbox;
7. inspect `research/<line>/clues/**` when present, using `mathia-research-clues` for their semantics;
8. read `research/<line>/SOURCES.md` and `LEAN_CANDIDATES.md` when relevant;
9. use `research/<line>/graph/index.md` when present only as derived navigation, never as mathematical evidence;
10. read only the individual findings and dependencies needed for the live review, candidate, clue, or duplication question.

Other Mathia research lines and `mind/` may be read as context or evidence, but are read-only for this role. A cross-line mathematical claim must be traced to canonical findings or authoritative sources; a relationship stated in one line's README does not by itself establish evidence in another line. Treat every `graph/` subtree as regenerable derived state and verify substantive claims against canonical findings or sources.

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

If the machine task is really a request for more open-ended mathematical reasoning, keep it here instead of delegating it as compute. If the desired durable output is a reusable Lean theorem/proof, route to `mathia-formalization-design` rather than the lightweight compute path.

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
- creating a computational delegation issue without a mathematical result;
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

Computational delegation does **not** add a repository queue or compute-artifact directory. Its control plane is the GitHub issue created under `mathia-compute-design`; its only possible return to the research tree is a later proposed clue.

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

A clue created by `mathia-compute-executor` is likewise only a proposed research lead. Reconstruct its computational claim independently, respect its exact/numerical/bounded-search evidence boundary, and apply the normal Research Watch derivation, adversarial stress test, and prior-art gate before changing its status or creating a finding.

Global/cross-line clue creation is permitted only as defined by `mathia-research-clues` and should be genuinely cross-line.

## Ownership and hard path gate

For a Research Watch on `research/<line>/`, writable evidence is limited to:

```text
research/<line>/SOURCES.md
research/<line>/LEAN_CANDIDATES.md   # only when applicable
research/<line>/findings/**
```

`research/<line>/README.md` is deliberately excluded from routine write ownership.

Within `findings/**`, writes to `*.review.md` must obey `mathia-research-review`; ordinary Research Watch ownership does not override turn-taking.

An in-place modification of a target with an open review is allowed **only** in the acceptance-pending-persistence stage defined by `mathia-research-review`, and only when the mathematical claim identity is unchanged.

When `mathia-research-clues` is loaded, its clue-path extension also applies.

Creation of a compute GitHub issue under `mathia-compute-design` is a control-plane delegation operation, not a repository path write. It grants no additional repository write ownership to Research Watch.

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
8. verify `SOURCES.md` or `LEAN_CANDIDATES.md` agree with current canonical findings when changed;
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

1. **Workflow/publication failure:** an error, conflict, missing required capability, path/publication-gate failure, or other workflow problem prevents intended persistence.
2. **Extraordinary mathematical success:** a result that materially changes the RH research program or crosses a comparably high bar. Ordinary positives/refinements/classicalizations/closures do not qualify merely because they are persistable.
3. **Clue acceptance:** a clue changes to `status: accepted`.
4. **Owner-side adversarial review events:** every material owner-authored transition defined by `mathia-research-review`, including substantive `Owner` responses, persistence of accepted new mathematics into a finding, concessions, corrections, replacements, independent findings arising from review, and withdrawals.

Do **not** notify for ordinary positive findings, routine negatives/dead ends, ordinary prior-art redirects, routine commits, source additions, compute-issue creation, clue proposal/rejection/resolution, unchanged searches, or unchanged runs.

Do not notify merely because this watch observes an adversary-side review event. The authoring adversarial process owns those notifications, preventing duplicates.

Task-specific prompts should normally inherit this policy rather than restating it.

## Reporting

At the end of a run, surface only notifications allowed above. Persist routine substantive work silently when notification thresholds are not met.

Do not produce project-status recaps, timelines, or daily journals.