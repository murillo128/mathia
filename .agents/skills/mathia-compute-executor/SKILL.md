---
name: mathia-compute-executor
description: Execute one approved Mathia computational research issue independently, keep scratch work ephemeral, and return only a materially justified proposed research clue directly to main.
---

# Mathia Computational Research Executor

## Responsibility

Use this skill when Codex is asked to execute an approved Mathia computational-research issue created under:

```text
.agents/skills/mathia-compute-design/SKILL.md
```

The controlling GitHub issue owns the exact computational question. Codex is an **independent machine-work executor**, not a second Research Watch and not a replacement mathematical researcher.

Its job is to carry out the bounded computation faithfully, classify what the result actually establishes, and -- only when the result is mathematically material -- return one `status: proposed` clue directly to Mathia research.

There is deliberately:

- no implementation PR;
- no independent reviewer requirement;
- no durable compute branch;
- no committed scripts, notebooks, generated datasets, result dumps, plots, or logs;
- no direct canonical finding update.

The issue is the execution contract. The clue, when justified, is the only durable repository output.

## Fresh-context independence

Treat the issue as if the originating Research Watch were unavailable.

Before execution:

1. read `AGENTS.md`;
2. read the controlling compute issue;
3. read this skill;
4. read only the persisted findings, clues, sources, definitions, or code explicitly required by the issue;
5. load `.agents/skills/mathia-research-clues/SKILL.md` for clue schema, deduplication, and evidence-boundary discipline.

Do not recover or ask for the Research Watch's hidden reasoning. Do not assume the expected result is correct merely because the issue was created by research.

If the issue is not self-contained enough to determine the mathematical object, comparison, bounds, or outcome semantics without inventing a material scientific decision, stop and return the issue to `design-required` rather than choosing a convenient interpretation.

## No-PR execution model

This workflow is intentionally not `spec-driven-codex-loop` implementation work.

Do not create a feature branch or pull request. Use temporary/ignored local files, scripts, virtual environments, notebooks, Lean scratch files, generated data, caches, and logs as needed for the computation, but do not commit them.

Keep scratch artifacts only as long as required to establish the result. Large or transient artifacts remain outside Git.

The only permitted direct repository mutation from this role is the proposed clue described below.

## Execute the frozen computational question

Implement the smallest trustworthy computation that answers the issue as written.

Appropriate tools include, as needed:

- Python;
- exact integer/rational/algebraic arithmetic;
- symbolic algebra or a CAS;
- arbitrary-precision numerical computation;
- exhaustive finite search;
- numerical linear algebra or spectral computation;
- a bounded Lean check used as a machine verifier rather than as a durable formalization artifact;
- multiple independent implementations when the issue specifically requires them or when one implementation is too fragile to trust alone.

Do not broaden the task into open-ended mathematical ideation. If answering the issue requires inventing a new representation, theorem, or major proof strategy that the issue did not specify, report the design gap rather than silently turning Codex into another Research Watch.

## Reproducibility and numerical discipline

The executor must be able to explain exactly what was computed.

Preserve in the issue or final clue, as proportionate to the task:

- exact input definitions and finite domains;
- algorithm or formula evaluated;
- exact arithmetic vs floating/arbitrary-precision distinction;
- precision and tolerances when numerical;
- random seeds when randomness is unavoidable;
- stopping/convergence criteria;
- matched controls;
- minimal counterexample/witness when one exists;
- enough compact command/code/evidence in the issue discussion to reproduce a material result without committing a compute project to the repository.

Never convert numerical stability or repeated empirical agreement into proof. Distinguish explicitly:

```text
exact certificate / counterexample
exhaustive finite verification
symbolic verification
bounded search with no witness
numerical evidence
heuristic pattern
inconclusive / unstable
execution failure
```

## Clue creation gate

A successful computation does **not** automatically deserve a clue.

Create or materially strengthen one clue only when the result changes the mathematical research frontier in a concrete way, for example:

- an exact counterexample kills or materially narrows a candidate mechanism;
- a minimal witness reveals a previously unrecognized obstruction or boundary case;
- an exhaustive finite classification suggests a precise general theorem or dichotomy worth deriving;
- a matched control reproduces the phenomenon and therefore challenges the claimed arithmetic specificity;
- two formulas or implementations disagree in a way that exposes a precise revalidation question;
- a robust numerical pattern motivates a sharply stated conjecture with a decisive next test;
- a bounded Lean/symbolic check reveals a missing hypothesis, exact equivalence, or finite certificate with research consequences.

Do **not** create a clue for:

- a routine confirmation of an already exact finding;
- a plot or numerical pattern with no precise research question;
- a null bounded search that does not materially change plausibility;
- implementation/debugging details;
- performance or tooling observations;
- a result whose only value is "we ran the requested computation".

If nothing passes this gate, make no repository change.

## Direct proposed-clue return

When the clue gate passes, load and obey `mathia-research-clues` for stable identity, deduplication, target-line selection, schema, and evidence boundary.

This skill is a narrow delegation extension to the clue workflow: Codex may create or materially strengthen **only a `status: proposed` clue** arising from the controlling compute issue.

Use the originating Research Watch as the mathematical provenance:

```yaml
origin: research-watch
```

Although Codex writes the file, `origin` records where the delegated research question came from. The clue's `Observation` must also name the controlling compute issue and state that the new evidence was obtained by independent compute execution.

Prefer:

```text
research/<originating-line>/clues/CLUE-<slug>.md
```

Use `research/clues/**` only when the issue itself establishes that the computational result is genuinely cross-line or cannot honestly be assigned to one existing line.

The clue must make the computational epistemic boundary explicit. In particular:

- finite search is finite search;
- numerical evidence is numerical evidence;
- a scratch Lean check is not a durable Mathia formalization;
- an exact counterexample is strong evidence but the clue is still not a canonical finding;
- absence of a witness in a bounded domain is not a global theorem unless exhaustiveness over the theorem's complete finite universe was part of the issue.

Use the clue's existing sections rather than inventing a compute-report schema. Put the compact computation provenance, issue reference, method, result, and reproducibility details into `Observation` and the exact next mathematical question into `Research question` / `Decisive test`.

## Hard research-tree boundary

This role must never create, update, or delete:

```text
research/**/findings/**
research/**/findings/*.review.md
research/**/mind/**
research/mind/**
research/**/graph/**
research/master/**
research/prior_art/**
research/**/SOURCES.md
research/**/LEAN_CANDIDATES.md
```

It must not:

- accept, reject, or resolve a clue;
- create a canonical finding;
- repair or withdraw a finding;
- open an adversarial review sidecar;
- update a line README;
- turn compute output into a novelty claim;
- change research strategy directly.

Research Watch remains the authority that later triages the proposed clue and independently decides whether it deserves further derivation, adversarial checking, prior-art search, and eventual finding status.

## Direct-main publication gate

A clue is published directly to the repository default branch with no PR only when all of these hold:

1. the controlling issue is an approved Mathia compute issue and names the originating line/scope;
2. the computation was executed against the exact issue-defined object and bounds;
3. the clue passes the materiality gate above;
4. existing local/global clues were checked for duplication;
5. the only repository diff is one allowed clue creation or material strengthening;
6. the clue remains `status: proposed`;
7. the clue states the exact computational evidence boundary and does not present a bounded/numerical result as proof;
8. no scratch code, logs, generated data, plots, Lean source, findings, reviews, or unrelated files are included.

Use a direct-main commit such as:

```text
research(<line>): propose compute-backed clue
```

or, for genuinely global scope:

```text
research: propose compute-backed clue
```

Before publishing, refresh `main` and re-check the clue path for concurrent creation/strengthening. Never overwrite another actor's clue changes.

## Issue completion

The compute issue is control-plane state, not a PR-backed implementation issue.

After successful execution:

- if a clue was published, leave a concise final issue comment linking the clue and summarizing the exact execution outcome;
- if no clue was warranted, leave a concise final issue comment stating the bounded result and why it did not change research state;
- close the compute issue as completed.

This no-PR compute workflow is an explicit exception to implementation workflows whose `completed` state follows a merge: here there is no PR or merge, and completion means the frozen computation was executed and any justified proposed clue was durably returned.

If execution is inconclusive because of a replaceable implementation defect, repair it within the bounded issue. If a material scientific/design ambiguity blocks trustworthy execution, return the issue to `design-required`. If a genuinely unavailable capability blocks it, use `blocked`.

## Terminal report

Keep the user-facing/executor handoff minimal:

- controlling issue;
- bounded computation outcome;
- whether a proposed clue was created/strengthened and its path;
- any real blocker.

Do not produce a research recap or pretend the compute result is accepted mathematics.