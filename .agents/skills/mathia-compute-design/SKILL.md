---
name: mathia-compute-design
description: Let a Mathia Research Watch delegate a precise machine-checkable subquestion to an execution-ready GitHub issue, then return to research without owning the computation.
---

# Mathia Computational Delegation Design

## Responsibility

Use this skill when a Mathia Research Watch encounters a **concrete computational subquestion** whose answer could materially falsify, strengthen, distinguish, or redirect the current mathematical research, and where a machine can answer that subquestion more cheaply or reliably than another open-ended reasoning pass.

This is a thin specialization of:

```text
.agents/skills/design-github-issue/SKILL.md
```

Load that skill as the generic issue-design authority. The originating Research Watch owns the mathematical motivation only until the issue is published. The controlling issue then owns the delegated computational question.

The Research Watch does **not** execute the computation, monitor it, maintain a compute queue in the repository, or keep polling the issue. Once the issue is created, return to ordinary research. Any mathematically useful result comes back later through the normal clue inbox.

## Admission gate: delegate only a real computational question

Create a compute issue only when all of the following are true:

1. the mathematical question is already precise enough to state independently of the researcher's hidden reasoning;
2. there is a bounded machine task with explicit inputs/construction and interpretable outputs;
3. at least one possible outcome would materially change what the research line should believe or investigate;
4. the execution can be performed primarily by computation or mechanical checking -- for example Python, exact/symbolic algebra, exhaustive finite search, arbitrary-precision numerics, numerical linear algebra, a CAS, or a bounded Lean check;
5. the evidence semantics can be stated in advance: what would be an exact counterexample/certificate, what would be finite-range evidence only, and what would remain numerical/heuristic;
6. the task has a sensible resource/termination boundary.

Do **not** delegate merely to consume compute, produce plots, reproduce an exact derivation already stronger than the experiment, or obtain "more thinking" from another model.

Bad compute issues include:

- "explore this construction numerically and see what happens";
- "try many ideas for RH";
- recomputing thousands of examples when an exact proof already settles the same statement;
- asking Codex to invent the mathematical representation rather than evaluate a frozen one;
- using simulation as decorative confirmation of a theorem already derived exactly.

The key test is:

> **Could the executor perform the requested task correctly without having to invent the next mathematical idea?**

If not, keep the problem in Research Watch.

## Boundary with Lean formalization

A bounded Lean check may be part of a compute issue when Lean is simply a machine checker for a precise finite/local question and no durable formal artifact is requested.

If the actual objective is to create and retain a reusable Lean theorem/proof as a formal sidecar of Mathia, use:

```text
.agents/skills/mathia-formalization-design/SKILL.md
```

instead. Do not smuggle a formalization project into the lightweight compute path merely to avoid its stronger statement/proof-integrity workflow.

## Issue authority and independence

The compute issue must be self-contained for a **fresh Codex execution context**. Do not rely on the Research Watch's private chain of thought, scheduler session, or unstated intuition.

The issue should cite the exact persisted findings, clues, sources, or definitions needed to reconstruct the task. Those references are inputs, not authority for the expected answer.

The executor is expected to recompute independently and may return a result contrary to the researcher's expectation.

## Required issue contract

Compose with `design-github-issue` and make the issue `execution-ready` only when a fresh executor can run it without further scientific design.

A compute issue should normally contain these task-specific elements:

### Research provenance

- originating research line;
- exact finding/clue/source paths that motivate the question;
- why this computation could materially change the line.

### Computational question

State one precise question. Prefer a falsifiable form such as:

- does a counterexample exist in this exactly defined finite domain?;
- does this exact matrix/operator construction have property `P` for the declared family?;
- do two independently implemented formulas agree on the declared exact domain?;
- what is the minimal counterexample/witness?;
- does a conjectured invariant survive a matched control?;
- does a numerically defined asymptotic or spectral pattern persist under the predeclared scaling test?

### Exact construction and inputs

Define enough mathematics that the executor cannot silently choose a friendlier object, normalization, indexing convention, sample family, or comparison metric.

### Method freedom

Prefer specifying the question and evidence boundary rather than dictating implementation. Permit Python, exact arithmetic, symbolic tools, arbitrary precision, Lean, or another proportionate checker as appropriate.

If two independent implementations are materially useful, say so explicitly. Do not require redundant implementations by default.

### Outcome semantics

Predeclare what each kind of result means. Distinguish at least when relevant:

- exact finite counterexample/certificate;
- exhaustive proof over a genuinely finite declared universe;
- symbolic identity/check;
- bounded search with no witness found;
- numerical evidence;
- numerical instability/inconclusive result;
- execution/tooling failure.

Absence of a counterexample up to `N` is not a theorem about all `N` unless the issue proves that the searched domain is exhaustive for the claim.

### Resource and stop boundary

Set a bounded search domain, precision policy, convergence/stability test, or other termination rule. A compute executor must not turn one issue into an unbounded research campaign.

### Research return contract

Every compute issue must instruct the executor to load:

```text
.agents/skills/mathia-compute-executor/SKILL.md
```

The only durable repository output authorized by a successful compute execution is, when warranted, **one new or materially strengthened `status: proposed` research clue committed directly to `main`** under the owning line or global clue inbox.

The executor must not create or modify canonical findings, adversarial `.review.md` sidecars, `mind/`, graph state, master state, source ledgers, Lean source, experiment code, scripts, datasets, or result dumps as part of this workflow.

If the computation is null, confirmatory without changing the research frontier, inconclusive, or purely implementation-level, no clue is required and no repository file should be changed.

## Research Watch handoff semantics

After creating the issue:

- do not wait for it;
- do not poll it on later scheduled runs;
- do not maintain a repository TODO or compute-candidate file;
- do not treat issue creation as a finding, clue, or evidence;
- do not notify merely because a compute issue was created;
- continue the line using current canonical evidence.

If Codex later creates a `proposed` clue from the computation, the Research Watch encounters it through the ordinary `mathia-research-clues` intake and independently decides whether to accept, reject, resolve, or ignore it under the normal research procedure.

## Suggested compute-issue shape

Use the generic `design-github-issue` structure, with the computational contract expressed compactly. A useful task-specific core is:

```markdown
## Research provenance
<line + exact persisted basis + why this test matters>

## Computational question
<one precise machine-answerable question>

## Exact construction and inputs
<definitions, bounds, controls, conventions>

## Evidence semantics
<what each possible output does and does not establish>

## Resource / termination boundary
<bounded domain, precision, stop conditions>

## Research return
Execute with `.agents/skills/mathia-compute-executor/SKILL.md`.
Only a materially justified `status: proposed` clue may be persisted to `main`.
No PR and no other repository output.
```

Do not duplicate generic GitHub workflow text already owned by `design-github-issue`.