---
name: mathia-compute-executor
description: Execute one approved Mathia computational research issue independently, keep scratch work ephemeral, then run a bounded post-compute fertility/refinement audit before returning at most one materially justified proposed research clue directly to main.
---

# Mathia Computational Research Executor

## Responsibility

Use this skill when Codex is asked to execute an approved Mathia computational-research issue created under:

```text
.agents/skills/mathia-compute-design/SKILL.md
```

The controlling GitHub issue owns the exact computational question. Codex is an **independent machine-work executor**, not a second Research Watch and not a replacement mathematical researcher.

Its job is to carry out the bounded computation faithfully, classify what the result actually establishes, preserve mathematically meaningful structure exposed by the computation, and then run a bounded independent fertility/refinement audit. Only when one surviving direction materially changes the research frontier may it return one `status: proposed` clue directly to Mathia research.

There is deliberately:

- no implementation PR;
- no independent technical reviewer requirement;
- no durable published compute branch;
- no committed scripts, notebooks, generated datasets, result dumps, plots, logs, or fertility reports;
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

Do not create or publish a feature branch or pull request. Use temporary/ignored local files, scripts, virtual environments, notebooks, Lean scratch files, generated data, caches, and logs as needed for the computation, but do not commit them.

When launched by `.github/workflows/codex-execute-ready.yml`, a local `codex/issue-N` worktree/branch already exists as **infrastructure isolation**. Adopt that worktree; do not create another one, do not switch it to `main`, and do not publish the issue branch. The branch may temporarily hold the single candidate clue commit needed to perform the direct-main publication gate below, but it is not a durable delivery branch.

Keep scratch artifacts only as long as required to establish the result and complete the bounded fertility audit. Large or transient artifacts remain outside Git.

The only permitted repository mutation from this role is the proposed clue described below.

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

Do not broaden the **computation itself** into open-ended mathematical ideation. If answering the frozen question requires inventing a new representation, theorem, or major proof strategy that the issue did not specify, report the design gap rather than silently changing what is being computed.

The post-compute fertility stage below may investigate only mathematical structure actually exposed by this bounded execution and its immediate abstraction boundary. It is not permission to turn the executor into a general Research Watch.

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

## Computation is an observation surface

During implementation and result analysis, preserve **explicit mathematical audit surfaces** that could otherwise disappear when the computation is summarized to a scalar, plot, success/failure flag, or minimal witness.

Maintain a compact ephemeral compute-fertility handoff containing, when applicable:

- the exact classified result and strongest reproducible evidence behind it;
- minimal witnesses/counterexamples and nearby controls;
- intermediate exact objects exposed by the computation: kernels, nullspaces, orbit classes, recurrences, factorizations, normal forms, spectra, multiplicity patterns, symmetries, equivalence classes, or certificates;
- representation choices or coordinate changes introduced only for computation;
- aggregation/compression steps that discarded ordering, signs, correlations, block structure, multiplicities, phases, generators, or source labels;
- parameter boundaries, degenerate families, phase transitions, or unexpected invariances observed robustly;
- disagreements between independent implementations or between an expected formula and the computed object.

This packet is ephemeral process state, not a research artifact and not hidden chain-of-thought. Record concrete objects/results, not speculative narratives. Do not commit it.

## Mandatory fresh post-compute fertility audit

After the frozen computational question has been executed and its epistemic status classified, spawn a **fresh isolated subagent** for the fertility decision. It must load this skill and `.agents/skills/mathia-research-clues/SKILL.md` and receive:

- the controlling compute issue;
- the persisted mathematical inputs authorized by the issue;
- the exact classified compute result and compact reproducibility evidence;
- the ephemeral compute-fertility handoff as untrusted audit leads.

The fertility subagent must not inherit the executor's hidden reasoning. It must independently reconstruct any candidate from the concrete evidence before trusting it.

A null/routine headline result does **not** allow this stage to skip directly to "no clue". It must perform both discovery lenses below. Conversely, both lenses may legitimately conclude that nothing material was exposed.

### Discovery lens A: result-internal structure

Inspect the richer mathematical objects produced by the computation before they were compressed to the issue's headline answer.

Ask, as relevant:

1. Did a witness come as a family with a common normal form rather than an isolated point?
2. Did a nullspace/kernel expose coordinates, recurrences, orbit decompositions, generators, or multiplicities beyond its dimension?
3. Did a spectrum expose clustering, sign patterns, invariant subspaces, or rank transitions beyond the scalar statistic requested?
4. Did exhaustive classification reveal an exact dichotomy or congruence/orbit boundary?
5. Did controls show the phenomenon survives or disappears under a representation change, normalization, source-label shuffle, or arithmetic/non-arithmetic replacement?
6. Did the computation produce a finite certificate whose internal structure suggests a precise theorem stronger than "the search succeeded"?

Do not dismiss an intermediate object merely because the issue asked only for its cardinality, rank, minimum, maximum, or existence.

### Discovery lens B: mathematical-to-computational information loss

Independently reconstruct:

```text
source mathematical object -> computational representation/algorithm -> measured summary
```

Identify what the implementation intentionally forgot or treated as independent in order to compute the frozen target.

Ask, as relevant:

1. Were source-linked variables replaced by independent coordinates, matrix entries, samples, bins, or aggregate moments?
2. Were signs, order, conjugacy, common generators, Gram/tensor factors, multiplicities, phases, orbit labels, or correlations discarded?
3. Did a normalization quotient out a scale or symmetry that might itself carry the obstruction?
4. Did the algorithm collapse a structured object to a determinant, rank, eigenvalue, norm, count, histogram, or best-fit scalar?
5. If one restores one discarded relation while keeping the observed result, does a sharper compatibility condition, obstruction, classification, or falsifier appear?

This pass is mandatory even when result-internal discovery found no candidate. Some computational clues arise from realizing that the computation answered an easier problem only after forgetting a source coupling.

## Bounded candidate kill/refinement loop

After **both** discovery lenses, synthesize concrete candidate research questions. Several raw candidates may exist, but the workflow will publish at most one clue.

For every candidate that is more than a descriptive observation:

1. **Round 1 is mandatory.** Try to kill it using the existing issue inputs, local/global clue deduplication, immediate known mathematics, a minimal counterexample, or a cheap targeted recomputation/control when available. Reject candidates that are duplicate, already classical with no residual, unstable under modest recomputation, or merely artifacts of implementation choices.
2. If a candidate survives and Round 1 exposes a **new mathematical object, relation, factorization, information-loss boundary, exact residual, or sharper parameter boundary**, perform **one additional refinement round**. Tighten the research question and decisive test around the new structure, then try to kill it again.
3. Stop after at most **two refinement rounds after discovery**. Do not continue because wording can improve, more parameter sweeps are possible, or another speculative analogy can be invented.

Continue only when the previous round exposed genuinely new mathematical structure with a falsifiable unresolved consequence. The loop is not "keep brainstorming while something sounds interesting".

After killing/merging duplicates, rank surviving candidates by materiality and falsifiability. Publish **at most one**: the strongest direction whose decisive next test could genuinely redirect or narrow the originating research line.

## Clue creation gate

A successful computation does **not** automatically deserve a clue.

Create or materially strengthen one clue only when a direction survives the complete post-compute fertility audit and changes the mathematical research frontier in a concrete way, for example:

- an exact counterexample kills or materially narrows a candidate mechanism;
- a minimal witness belongs to an exact family revealing a previously unrecognized obstruction or boundary case;
- an exhaustive finite classification suggests a precise general theorem or dichotomy worth deriving;
- a matched control reproduces the phenomenon and therefore challenges the claimed arithmetic specificity;
- two formulas or implementations disagree in a way that exposes a precise revalidation question;
- a robust numerical pattern motivates a sharply stated conjecture with a decisive next test;
- a bounded Lean/symbolic check reveals a missing hypothesis, exact equivalence, or finite certificate with research consequences;
- an intermediate kernel/orbit/factorization/normal-form object carries unused structure that yields a distinct falsifiable question;
- restoring a source relation discarded by the computational abstraction makes previously independent measured quantities obey a concrete proposed compatibility condition.

Do **not** create a clue for:

- a routine confirmation of an already exact finding;
- a plot or numerical pattern with no precise research question;
- a null bounded search that does not materially change plausibility and exposes no structured residual;
- implementation/debugging details;
- performance or tooling observations;
- a result whose only value is "we ran the requested computation";
- a candidate that survived only because no bounded attempt was made to falsify, control, or deduplicate it.

If nothing passes this gate after both discovery lenses, make no repository change.

## Direct proposed-clue return

When the clue gate passes, load and obey `mathia-research-clues` for stable identity, deduplication, target-line selection, schema, and evidence boundary.

This skill is a narrow delegation extension to the clue workflow: Codex may create or materially strengthen **only one `status: proposed` clue** arising from the controlling compute issue.

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
- absence of a witness in a bounded domain is not a global theorem unless exhaustiveness over the theorem's complete finite universe was part of the issue;
- a structure exposed by an intermediate representation is not automatically source-valid if the source-to-compute bridge discarded additional constraints.

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
3. the fresh post-compute fertility audit completed both discovery lenses and the bounded kill/refinement procedure;
4. the single surviving clue passes the materiality gate above;
5. existing local/global clues were checked for duplication;
6. the only repository diff is one allowed clue creation or material strengthening;
7. the clue remains `status: proposed`;
8. the clue states the exact computational evidence boundary and does not present a bounded/numerical result as proof;
9. no scratch code, logs, generated data, plots, Lean source, fertility handoff/report, findings, reviews, or unrelated files are included.

Use a direct-main commit such as:

```text
research(<line>): propose compute-backed clue
```

or, for genuinely global scope:

```text
research: propose compute-backed clue
```

### Publication from an Action-created issue worktree

If execution is already isolated on local branch `codex/issue-N`, do not `checkout main` and do not push that branch as a branch. Instead:

1. fetch `origin/main` immediately before candidate publication;
2. verify/reconcile any concurrent change to the target clue path or evidence that affects the clue;
3. ensure the candidate commit is based on the current `origin/main` (rebasing the **unpublished local scratch branch** is allowed when safe; rerun any affected checks if the base movement changes relevant content);
4. verify `git diff --name-only origin/main..HEAD` contains exactly the one authorized clue path and no scratch artifacts;
5. verify `origin/main` is an ancestor of `HEAD` and the candidate is a fast-forward of current main;
6. publish with a normal non-force ref update equivalent to `git push origin HEAD:main`;
7. fetch and verify that `origin/main` now resolves to the published candidate commit.

A non-fast-forward rejection is a concurrency signal, not permission to force-push. Refresh/reconcile and re-check the gate. The local `codex/issue-N` branch remains host scratch state and must not be published merely because it contains the accepted commit.

Outside the Action-created worktree case, use the simplest safe direct-main mechanism consistent with `codex-github-operations` and the same path/concurrency gates.

## Issue completion

The compute issue is control-plane state, not a PR-backed implementation issue.

After successful execution:

- if a clue was published, leave a concise final issue comment linking the clue and summarizing the exact execution outcome;
- if no clue was warranted, leave a concise final issue comment stating the bounded result and that both post-compute discovery lenses found no surviving material direction after kill/refinement;
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