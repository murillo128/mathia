---
name: mathia-research-watch
description: Run recurring Mathia mathematical research watches with one shared evidence workflow, adversarial novelty audit, durable finding schema, strict path ownership, and direct-main publication gates.
---

# Mathia Research Watch

## Responsibility

Use this skill for recurring or scheduled mathematical research watches that maintain one research-evidence branch under `research/<line>/`.

The research watch owns **evidence**, not the Mathia mind. Its job is to discover, derive, falsify, audit, and preserve durable mathematical findings so that later synthesis, independent review, or formalization can reuse them.

It does not maintain project status, a changelog, a daily diary, a roadmap, an issue queue, or chronological research notes. It does not write intuitions into `mind/`.

## Task-specific inputs

Each research-watch prompt should supply only the topic-specific contract:

- the research line, such as `prime_circle`, `prime_flute`, or `prime_lattice`;
- the stable finding prefix, such as `PC`, `PF`, or `PL`;
- the mathematical object and questions to investigate;
- any branch-specific definitions, known results, or priority mechanisms;
- any notification threshold stricter than the default in this skill.

The prompt owns **what mathematics to investigate**. This skill owns **how to investigate, audit, persist, and publish it**.

## Load context progressively

Before substantive work:

1. read `AGENTS.md`;
2. read this skill;
3. read `research/<line>/README.md` when present;
4. inventory the filenames under `research/<line>/findings/` so stable IDs and existing topics are visible without preloading every finding;
5. read `research/<line>/SOURCES.md` and `LEAN_CANDIDATES.md` when present and relevant;
6. use `research/<line>/graph/index.md` when present only as a derived navigation aid, never as mathematical evidence;
7. read only the individual findings needed to understand the live candidate, its dependencies, or possible duplication.

Other Mathia research branches and `mind/` may be read as evidence, but are read-only for this role. Treat every `graph/` subtree as regenerable derived state: verify any substantive claim or relationship against the underlying finding, mind note, or prior-art source before relying on it.

Do not preload all findings or complete repository history unless a dependency or novelty question requires it.

## Research cycle

### 1. Reconstruct the exact object

Start from the branch's intrinsic mathematical construction and conventions. Check definitions, normalizations, indexing, domains, degeneracies, and which structure is genuinely present rather than imported by analogy.

Do not begin by wrapping a known zeta identity, generating function, operator, or transform around the data and calling the reformulation a mechanism.

### 2. Derive before interpreting

Prefer exact identities, invariants, reductions, asymptotics with controlled hypotheses, operator relations, or explicit obstructions before broad spectral or geometric analogies.

Numerical experiments may suggest or falsify a claim, but numerical coincidence is not a durable finding unless the task explicitly studies an empirical law. Preserve the distinction between exact derivation, literature theorem, computation, heuristic, and conjecture.

### 3. Stress-test adversarially

Actively try to kill the candidate before promoting it. In particular check, when relevant:

- constants, signs, branch choices, and normalization factors;
- convergence domains and whether a claimed identity survives analytic continuation;
- finite-versus-infinite product, topology, measure, and operator-domain assumptions;
- whether a quantity is gauge-dependent or coordinate-dependent;
- telescoping, coboundary, pure-gauge, or endpoint-only reductions;
- universal geometric/spectral background that erases the arithmetic data;
- local-versus-global information loss;
- whether an apparent symmetry is merely a known functional equation or duality in disguise;
- whether a proposed spectral object actually exists with the required hypotheses;
- boundary cases, counterexamples, and degenerate instances.

Important negative results are first-class research results. Preserve them when they rule out a natural branch, expose a hidden universality, or establish a reusable impossibility principle.

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

Use the research line's established vocabulary when it is more specific. The common evidence vocabulary is:

- `EXACT-DERIVED` — exact consequence derived from the explicit Mathia construction;
- `LITERATURE+DERIVED` — a published theorem plus a derived consequence for this construction;
- `CLASSICAL-IDENTITY` — exact but already standard;
- `CANDIDATE-NEW-STRUCTURE` — a potentially new organization/mechanism whose novelty is not established;
- `NEGATIVE/OBSTRUCTION` or `DECISIVE-NEGATIVE` — a tempting route is ruled out or materially narrowed;
- `CONJECTURAL` — depends on an unproved mechanism or statistical hypothesis;
- `NEEDS-AUDIT` — a promising claim still lacks a reliable proof/source bridge.

Labels may be combined when needed, but the finding must make **exactness, provenance, novelty, and remaining uncertainty** unambiguous.

Never silently upgrade evidence.

## Substantive-finding gate

Persist a research update only when at least one of these happened materially:

- a new exact or literature-backed mathematical claim was derived;
- a nontrivial candidate mechanism or invariant became precise and falsifiable;
- an important route was disproved or sharply restricted;
- a previous finding was corrected, weakened, strengthened, merged, or refuted;
- prior art showed that a supposedly new mechanism is classical and materially redirected the investigation;
- a decisive boundary condition, existence condition, or counterexample changed what can plausibly work.

The following are not sufficient by themselves:

- another search pass with no changed conclusion;
- adding a paper that does not change or support a stored claim;
- speculative prose without a precise claim or test;
- renaming or repackaging known zeta/prime identities;
- recording what was attempted today;
- updating a "latest" number, timestamp, status, TODO, or next-step log.

If nothing passed this gate, create no repository churn.

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

`LEAN_CANDIDATES.md` is an optional adjunct for a deliberately small formalization queue when the branch already uses one or when a task explicitly needs it. It is not a research diary.

`graph/` is a separate derived view owned by the graph curator. It may be used for navigation, but it is not evidence and the Research Watch does not maintain it.

Legacy branches may predate one of the core artifacts or contain historical finding expositions outside `findings/`. Preserve such history unless a separate migration explicitly owns it. Do not create empty placeholders merely for symmetry.

### `README.md`

Keep stable branch context only: the primary mathematical object, conventions, research stance, evidence vocabulary, file map, and durable high-level interpretation. Do not use it as a run log.

### Individual findings

New detailed findings belong under:

```text
research/<line>/findings/<PREFIX>-NNN-<slug>.md
```

The individual finding files are the **canonical source of truth** for research evidence. Do not maintain a second hand-written finding ledger or compact duplicate index.

Use stable three-digit IDs. Before allocating an ID, inspect all existing filenames under `findings/` for that prefix and any explicitly preserved legacy finding files for the same line, then choose an integer greater than every existing ID. Never recycle holes or renumber existing findings. If a legacy collision already exists, preserve it and allocate above the maximum rather than rewriting history during unrelated research.

Prefer revising an existing finding over creating a near-duplicate. A derived graph index may help locate candidates, but duplication decisions must be verified from the canonical finding files themselves.

A durable finding should contain, with headings adapted to the mathematics:

1. the precise claim or obstruction;
2. evidence/status classification;
3. the derivation, theorem bridge, or falsifying argument;
4. why the result is specific or relevant to the Mathia construction;
5. prior art and novelty assessment;
6. boundary conditions, counterarguments, and known failure modes;
7. a decisive falsification/audit test when the claim is not already exact;
8. consequences for the research line, including what the result rules in or rules out.

Preserve equations and enough reasoning that a later researcher can audit the claim without reconstructing the original chat.

When a later result corrects, weakens, supersedes, or refutes an earlier one, update the affected canonical finding files so the relationship and current status are explicit. The graph curator can then derive the corresponding navigation and relation views without duplicating the mathematical statement.

### `SOURCES.md`

Maintain the literature anchor list used to support or falsify stored findings. Record stable bibliographic information and, briefly, what theorem/role the source provides.

Do not turn `SOURCES.md` into a search history, reading diary, or dump of every page consulted. A source belongs there when it is a durable dependency or important novelty/prior-art anchor.

### `LEAN_CANDIDATES.md`

When present, keep only high-value finite statements with a natural formal core. Separate the local lemma that Lean can reasonably prove from any external analytic or spectral theorem that must remain an explicit assumption.

Formalizability does not upgrade mathematical evidence.

## Ownership and hard path gate

For a research watch on `research/<line>/`, the writable evidence area is limited to:

```text
research/<line>/README.md
research/<line>/SOURCES.md
research/<line>/LEAN_CANDIDATES.md   # only when applicable
research/<line>/findings/**
```

Do **not** write to:

- `research/<line>/graph/**`;
- `research/<line>/mind/**`;
- `research/mind/**`;
- another research line;
- `docs/`, `experiments/`, code, tests, prompts, or unrelated repository files.

The separate Mathia mind process owns synthesis into durable intuitions and research lines. The graph curator owns derived navigation and relation views. Research watches provide their canonical evidence; they do not compete with either layer.

If a candidate requires a code/experiment change, record the mathematical need in the finding when substantive, but do not cross the ownership boundary unless a separate task explicitly authorizes that work.

## Publication policy

Scheduled Mathia research watches using this skill publish substantive research-knowledge improvements **directly to the repository default branch**. They do not open a PR for routine evidence maintenance.

Before every commit:

1. inspect the complete planned diff;
2. verify every changed path is inside the allowed evidence area above;
3. verify no `graph/`, `mind/`, code, experiment, or unrelated file changed;
4. verify the update passes the substantive-finding gate;
5. verify any `README.md`, `SOURCES.md`, or `LEAN_CANDIDATES.md` updates agree with the canonical detailed findings;
6. use a concise commit message describing the mathematical outcome, not the fact that a scheduled run occurred.

Research-watch commits must use the branch-scoped form:

```text
research(<line>): <mathematical outcome>
```

where `<line>` is the exact research directory name, for example:

```text
research(prime_circle): rule out projective Hill spectrum
research(prime_flute): classify universal cusp continuum
research(prime_lattice): identify Bohr-lift obstruction
```

Use `research:` only for repository-level maintenance of the shared research machinery itself, not for a finding belonging to one research line. Do not use a bare `prime_circle:`/`prime_flute:` prefix: retaining the common `research(...)` namespace makes research commits easy to identify while preserving branch provenance.

If the diff fails the path gate, do not commit until the unrelated changes are removed.

If no substantive mathematical result improved, do not commit merely to prove the task ran.

## Notification policy

A stored finding and a user notification are separate thresholds. Routine substantive refinements may be committed silently.

Unless the task specifies a stricter rule, notify only for one of these:

1. a mathematically substantive mechanism connecting the construction to the target problem that survives a serious novelty check;
2. a precise new conjectural bridge with a clear falsification test;
3. prior art that essentially already contains the sought interpretation and materially redirects the investigation;
4. a decisive negative result that rules out an important natural branch.

Do not notify for unchanged searches, minor source additions, editorial cleanup, or ordinary incremental strengthening.

## Reporting

At the end of a run, report only substantive mathematical changes and their evidence level. If nothing material changed, say so concisely or remain silent when the automation's notification policy calls for silence.

Do not produce a project-status recap, timeline, or daily journal.
