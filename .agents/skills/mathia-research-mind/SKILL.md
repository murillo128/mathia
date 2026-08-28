---
name: mathia-research-mind
description: Synthesize durable local and global Mathia intuitions from all persisted research lines discovered under research/, excluding prior_art and derived graph state, with strict mind-only ownership and direct-main publication gates.
---

# Mathia Research Mind

## Responsibility

Use this skill for the recurring or scheduled **Mathia Research Mind** synthesis pass.

The mind owns **durable mathematical synthesis**, not primary research evidence. Its job is to read already-persisted research findings and extract structural principles, conjectural mechanisms, hidden equivalences, impossibility principles, reusable heuristics, cross-result deductions, and mathematically meaningful research lines.

Research-watch tasks own findings and source evidence. The graph curator owns derived graph views. The prior-art materializer owns `research/prior_art/`. This skill must not compete with those roles.

The mind may derive second-order or third-order conceptual consequences from persisted evidence, but it must not fabricate missing premises, silently strengthen a theorem, or treat a plausible mathematical connection as established evidence.

## Discover research lines dynamically

Do not hard-code active research-line names.

At the start of every run, inspect the direct children of:

```text
research/
```

A directory `research/<line>/` is a local research line for this skill when it contains durable research evidence, normally at least one of:

```text
research/<line>/FINDINGS.md
research/<line>/findings/
```

Always exclude these repository-level roots from local-line discovery:

```text
research/prior_art/
research/graph/
research/mind/
```

Also ignore any directory that contains only derived graph state or no durable findings.

This discovery rule is authoritative. A newly added research line should automatically participate in the next mind run without changing this skill or the scheduled-task prompt.

Process discovered lines in a deterministic order, for example lexicographic path order. Do not infer scientific priority from that execution order.

## Read-only evidence for each local line

For each discovered `research/<line>/`, read only the material needed for a coherent synthesis. Relevant evidence may include:

```text
research/<line>/README.md
research/<line>/FINDINGS.md
research/<line>/findings/**
research/<line>/SOURCES.md
research/<line>/LEAN_CANDIDATES.md
research/<line>/mind/**            # current local synthesis to revise
```

Do **not** use the line's `graph/**` directory as mathematical evidence. Graph content is derived presentation state.

Do **not** read `research/prior_art/**` as an input to this skill. Prior-art and novelty statements may be inherited from the research findings that already persisted them, but this mind pass does not independently reconcile against the canonical prior-art projection.

Do not use `experiments/**`, raw corpora, OpenAlex artifacts, or unrelated repository data merely to enlarge context. If a persisted finding points to a specific repository artifact that is essential to understand its exact claim, inspect only that exact dependency when necessary.

## External research boundary

The recurring mind pass is a synthesis process, not a literature-acquisition or novelty-search process.

Do not browse the web or run a new literature search to justify an intuition. Novelty/prior-art status should come from persisted research evidence.

If a candidate intuition depends on an external theorem, novelty claim, or mathematical premise that is not adequately persisted, keep the intuition at the weaker supported level or omit it and report the missing evidence. Leave evidence acquisition to the appropriate research watch or prior-art process.

## Local mind output

Each discovered research line may own:

```text
research/<line>/mind/
├── RESEARCH_LINES.md
└── intuition/
    └── MI-xxx-<slug>.md
```

Create these paths only when there is substantive synthesis to persist. Do not create empty placeholders merely because a research line exists.

Local minds describe what the findings of **that line** imply. Cross-line principles belong in the global mind instead of being duplicated into every local line.

## Global mind output

The program-level mind lives at:

```text
research/mind/
├── RESEARCH_LINES.md
└── intuition/
    └── MI-xxx-<slug>.md
```

The global mind is not a summary or concatenation of local minds. It should contain only genuinely cross-line principles, bridges, incompatibilities, common information-loss mechanisms, common preserved invariants, or constraints on the wider Mathia/Riemann program.

Build the global synthesis **after** all discovered local minds have been refreshed during the current run. The refreshed local minds and their underlying persisted findings are the inputs to the global pass.

## What belongs in an intuition

The purpose of an `MI-*` note is a durable mathematical idea useful to future reasoning.

Prefer a compact set of coherent intuitions. Revise, merge, strengthen, weaken, split, refute, or remove existing intuitions instead of appending one note per run or one note per finding.

A durable intuition should include, where mathematically relevant:

1. **Core intuition** — the structural idea in clear mathematical language.
2. **Strongest justified claim** — theorem-like principle, conjectural mechanism, or impossibility statement at the actual evidence level.
3. **Synthesis of evidence** — exact findings and relationships that support it.
4. **Counterevidence / boundary cases** — where it fails, what remains universal, conditional, or unresolved.
5. **Epistemic status** — exact, asymptotic, heuristic, speculative, etc.
6. **Novelty/prior-art status** — only as already supported by persisted evidence.
7. **Falsification criterion** — a calculation, theorem, counterexample, or control that would materially refute or narrow it.
8. **Lean-formalizable core** — when there is a natural finite formal statement.
9. **Evidence level** — use the established scale:

```text
speculative
plausible
supported
proved
refuted
```

Never silently upgrade evidence. A synthesis can be valuable while remaining `supported` or `plausible`.

Do not put TODOs, priorities, owners, schedules, implementation tasks, run dates, or a "next move" section inside an intuition note.

## What belongs in RESEARCH_LINES.md

Each local mind and the global mind maintain one compact `RESEARCH_LINES.md`.

A research line is a durable **mathematical question or discriminating mechanism**, not project status. It should state:

- the mathematical question or candidate bridge;
- links to the intuition(s) that motivate it;
- the decisive calculation, theorem, counterexample, matched control, or falsification test when known.

Prefer revising, merging, redirecting, or removing research lines over accumulating them indefinitely.

Do not include:

- dates or chronology;
- owners;
- priorities;
- issue/task status;
- schedules;
- implementation plans;
- completion checklists;
- daily/weekly history.

A research line may be removed when later findings make its mathematical premise obsolete or fully subsume it. Git history preserves chronology.

## Synthesis discipline

Actively look for nontrivial consequences across multiple findings rather than merely restating them.

High-value synthesis includes patterns such as:

- several independent negative results implying one broader impossibility principle;
- two constructions revealing the same invariant in different representations;
- an exact identity proving that an apparently new observable is only a coordinate change;
- a local-versus-global principle explaining repeated spectral failures;
- a repeated quotient/telescoping mechanism showing where information is lost;
- a mechanism showing which ordered or relational information survives localization, pinching, duality, lifting, or spectral compression;
- a bridge between two or more independently discovered research lines;
- apparently different branches imposing the same necessary condition on any credible RH mechanism.

Do not promote an intuition merely because several files use similar language. The relationship must be mathematically supported by the persisted claims.

## Adversarial synthesis gate

Before creating or strengthening an intuition or research line, try to kill it using the repository evidence.

Check, when applicable:

- whether one supporting finding is conditional or `NEEDS-AUDIT`;
- whether a later finding weakens, corrects, supersedes, or refutes an earlier one;
- whether the apparent mechanism is universal rather than prime-specific;
- whether a transform, determinant, trace, spectrum, or quotient loses the claimed information;
- whether a relationship is only analogy rather than an established bridge;
- whether constants, normalizations, topology, domains, convergence hypotheses, or operator categories differ materially;
- whether a supposed cross-line equivalence is only a shared classical coordinate system.

Important negative findings should prune or constrain the mind. Do not preserve an attractive intuition after its supporting mechanism has been decisively invalidated.

## Missing-information rule

Do not fill gaps by invention.

If a candidate synthesis requires a premise that cannot be recovered from the research line's persisted evidence:

1. do not strengthen or create the affected intuition as if the premise were established;
2. preserve any weaker statement that is genuinely supported;
3. report the exact missing evidence and relevant paths when it materially blocks synthesis.

Continue unrelated local or global synthesis only when doing so cannot hide the ambiguity or produce an internally inconsistent mind.

## Execution cycle

### 1. Synchronize source revision

Start from the current default branch and a coherent repository revision.

If the default branch advances materially while the run is synthesizing — especially through research-watch findings — refresh affected inputs before publishing.

### 2. Discover all local research lines

Inspect `research/` and apply the structural discovery rule. Do not rely on a task prompt listing active branches.

### 3. Refresh each local mind

For each discovered research line, in deterministic order:

1. inspect current findings and relevant branch context;
2. inspect its existing mind if present;
3. revise the intuition set adversarially;
4. refresh `RESEARCH_LINES.md` from the resulting intuition set;
5. avoid churn when no substantive mathematical synthesis changed.

### 4. Refresh the global mind

After all local lines are complete:

1. inspect the refreshed local minds and the persisted evidence needed to audit cross-line claims;
2. identify genuinely program-level principles or bridges;
3. revise `research/mind/intuition/**`;
4. refresh `research/mind/RESEARCH_LINES.md`;
5. do not duplicate local material merely to make the global mind look complete.

### 5. Final adversarial review

Before publication verify:

- every substantive statement is grounded in persisted research evidence;
- no finding was silently upgraded;
- no prior-art statement was invented or refreshed from external research;
- refuted/superseded evidence does not remain as positive support;
- local intuitions remain local and global intuitions are genuinely cross-line;
- research-line files contain mathematical questions, not project management;
- no chronology/status diary was introduced;
- the diff is entirely inside the allowed mind paths.

If an unsupported synthesis survives in the draft, weaken or remove it before commit.

## Ownership and hard path gate

This skill may write only to:

```text
research/mind/**
research/<discovered-line>/mind/**
```

where `<discovered-line>` is a research line identified by the structural discovery rule in the current run.

It must not modify:

```text
research/prior_art/**
research/graph/**
research/<line>/graph/**
research/<line>/README.md
research/<line>/FINDINGS.md
research/<line>/SOURCES.md
research/<line>/LEAN_CANDIDATES.md
research/<line>/findings/**
experiments/**
docs/**
code/tests/prompts outside mind ownership
```

Do not perform "minimal index/link updates" outside `mind/**`. The graph curator can discover and link mind output independently.

If the required correction belongs in a finding, prior-art note, graph, source list, code artifact, or experiment, report it to the owning process rather than crossing the path boundary.

## Publication policy

The scheduled Mathia Research Mind is the owner of mind synthesis and may publish substantive mind-only changes **directly to the repository default branch**.

Commit only when at least one mathematical intuition or mathematical research line was materially added, strengthened, weakened, merged, split, redirected, refuted, or removed.

Do not commit to record that the scheduled run occurred.

Before every commit:

1. inspect the complete diff;
2. verify every changed path passes the dynamic mind ownership gate;
3. verify no `prior_art/`, `graph/`, finding, code, experiment, or unrelated file changed;
4. verify the source revision is coherent and not stale against newly landed research evidence;
5. run the final adversarial review;
6. remove unrelated formatting churn;
7. use the commit prefix:

```text
research(mind): <mathematical synthesis>
```

Examples:

```text
research(mind): integrate prime-lattice information-loss constraints
research(mind): merge common relational-memory intuitions
research(mind): demote universal spectral threshold mechanism
```

## Reporting

At the end of a run, report only substantive mathematical synthesis:

- intuitions newly created, materially strengthened/weakened, merged, split, refuted, or removed;
- research lines materially added, redirected, merged, or removed;
- blockers caused by missing/contradictory persisted evidence that require an owning research process.

If nothing changed materially, say so concisely or remain silent when the scheduled task's notification policy permits it.

Do not produce a project-status recap, chronological summary, daily journal, or list of everything inspected.
