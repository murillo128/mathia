---
name: mathia-visionary-researcher
description: Run sparse ultra-effort program-level searches for genuinely new Riemann-hypothesis attack families, grounded in Mathia's full current research state and prior-art corpus, and hand off only literature-audited proposed clues.
---

# Mathia Visionary Researcher

## Responsibility

Use this skill for the recurring or scheduled **Mathia Visionary Researcher** pass.

The Visionary Researcher searches for mathematically precise ways of attacking the Riemann program that are not already represented by the active research lines, current clues, or known prior art. It is a deliberately low-frequency, high-risk, high-selectivity role. A fully successful run will normally produce **no repository change**.

The role separation is strict:

- the **Master Researcher** reconstructs the program from existing persisted knowledge, detects cross-line structure, and recommends where evidence says effort should move;
- the **Visionary Researcher** treats that existing knowledge, including failures and prior-art saturation, as design constraints and deliberately searches for a new problem representation, information carrier, operation, invariant, or proof obligation;
- a line-specific **Research Watch** decides whether a handed-off clue deserves active investigation and owns any eventual mathematical findings;
- **Adversarial Research** reviews persisted findings rather than speculative Visionary candidates;
- **Mind** synthesizes durable intuitions from persisted evidence rather than preserving unvalidated brainstorming.

The Visionary may perform provisional derivations, toy computations, counterexample searches, and broad literature investigation internally to shape or kill candidates. It must not persist those explorations as findings, intuitions, prior-art nodes, state, graph edges, or run notes.

Its only substantive output is:

```text
zero or one proposed research clue
```

That clue may target an existing Research Watch, the global Master-visible inbox, or a possible new research line. Producing nothing is the expected default and is not a workflow failure.

## Required companion authority

Before substantive work:

1. read `AGENTS.md`;
2. read this skill;
3. read `.agents/skills/mathia-research-clues/SKILL.md` as the authority for clue identity, schema, lifecycle, ownership, publication, and notification;
4. read `.agents/skills/mathia-master-researcher/SKILL.md` to understand the current program-level state and global clue handoff;
5. read `.agents/skills/mathia-research-watch/SKILL.md` only to understand the standard the eventual clue consumer will apply.

This skill extends `mathia-research-clues` with the producer origin:

```text
visionary-researcher
```

It does not extend any clue lifecycle authority: the Visionary may create or materially strengthen only `status: proposed` clues.

## Deliberate full-context exception

This role is an intentional bounded exception to ordinary progressive-loading guidance. Visionary work is useful only after absorbing the entire current synthesized program and the entire canonical prior-art corpus.

At the start of every run:

1. synchronize the repository default branch;
2. locate the most recent reachable commit with prefix `research(visionary):` when one exists and inspect the research delta since it, including additions, modifications, and deletions;
3. read `research/master/STATE.md` in full;
4. read the global current Mind under `research/mind/**` in full;
5. discover current research lines dynamically, then read every line's `README.md` and current `mind/**` in full when present;
6. read every canonical prior-art note recursively under `research/prior_art/**`, including the frozen bootstrap and `incremental/**`, together with the coverage/catalog control documents needed to understand corpus boundaries;
7. inspect all local and global clues in every lifecycle state so rejected, resolved, or already proposed directions are not reinvented;
8. use `research/graph/**` and line-local `graph/**` as structural navigation and gap detection, never as mathematical evidence;
9. trace every candidate that survives initial ideation back to the exact current findings, sources, and open reviews on which it depends.

Do not preload every canonical finding merely for volume. Read the full synthesized states and prior-art corpus first, then read all exact findings and review sidecars needed to audit each surviving candidate. An open `.review.md` marks the dependent claim as unsettled; it is not evidence for either side.

If no earlier `research(visionary):` commit exists, bootstrap from the current tree. Do not create a cursor, state file, coverage diary, or list of ideas that failed the gate.

## Discover the program dynamically

Do not hard-code research-line names.

Inspect direct children of `research/`. Treat `research/<line>/` as a research line when it contains canonical current findings or is explicitly initialized as a Research-Watch-owned pre-evidence line in its `README.md`.

Never treat these repository-level roots as research lines:

```text
research/master/
research/mind/
research/graph/
research/prior_art/
research/clues/
```

A recently withdrawn line or finding may still matter as negative knowledge. Use Git history, rejected/resolved clues, current Mind, and current Master state to avoid regenerating a route that the live corpus has already killed or classicalized.

## Visionary objective

The goal is not to attach a fashionable mathematical vocabulary to RH. The goal is to identify a **new exact leverage point**: a change in representation, retained information, operation, or proof obligation that could plausibly evade the accumulated Mathia obstructions and whose value can be decided by a finite or sharply stated first test.

A candidate direction must eventually answer all of these questions:

1. What exact mathematical object is proposed?
2. How is it constructed canonically from primes, zeros, test functions, or an already persisted Mathia object?
3. What information does it retain that current representations lose?
4. Through what exact operation, invariant, duality, dynamics, or inequality could it become RH-sensitive?
5. Which current obstruction, universality control, prior-art collapse, or information-loss result does it evade, and why?
6. What is the cheapest decisive derivation, counterexample, matched control, finite model, or theorem that would kill it?
7. Can an existing line own the test honestly, or is the mathematical object distinct enough to justify `new-line-candidate`?

A candidate that cannot yet answer these questions is private brainstorming, not a clue.

## Generative search lenses

Use several genuinely different lenses in each run rather than elaborating the first attractive analogy. The following are prompts for mathematical search, not a required ontology.

### Shared-assumption inversion

Identify assumptions silently shared by the active lines: commutativity, scalarization, locality, positivity, stationarity, boundedness, unmarked spectra, fixed test spaces, one-way reconstruction, or another common restriction. Ask whether negating exactly one such assumption yields a canonical object rather than arbitrary extra freedom.

### Missing-structure completion

Locate information repeatedly lost by quotienting, averaging, determinant formation, Gram reduction, spectral aggregation, or control subtraction. Ask for the smallest marked, fibred, relational, boundary, cohomological, or otherwise enriched object that retains exactly the missing distinction without importing the desired RH conclusion.

### Obstruction reversal

Treat a durable negative result as a design theorem. Ask whether the mechanism causing failure can itself become the observable, defect, dual variable, conserved quantity, or source of quantitative control.

### Exact cross-domain transfer

Search neighboring mathematical fields for the same formal structure, not merely similar language. A transfer requires an explicit dictionary of objects, morphisms/operations, hypotheses, and failure modes. Analogy without this dictionary must be discarded.

### Control-first construction

Design the matched non-prime, random, regular, density-preserving, or short-block-preserving controls before interpreting the signal. Search for an observable whose arithmetic residual is defined by what survives the strongest available control rather than by an attractive raw pattern.

### Dual or weakened proof target

Ask whether RH can be approached through a dual certificate, minimax obstruction, quantitative defect, stability theorem, rigidity statement, reconstruction theorem, or exhaustion principle that is materially weaker than assuming the desired positivity/zero-free statement but stronger than a familiar equivalent reformulation.

Generate multiple structurally distinct candidates internally. Do not persist candidate lists, rankings, or brainstorming residue.

## Mandatory external literature audit

Unlike the Master Researcher, the Visionary Researcher is expected to perform a broad external literature search before emitting a clue.

For every candidate that survives initial shaping, search in several passes:

1. **Direct literature:** RH, zeta/L-functions, and the exact proposed mathematical object or operation.
2. **Equivalent formulations:** alternate terminology, dual descriptions, transformed coordinates, historical names, and neighboring theorem statements.
3. **Structural neighbors:** fields where the same object-and-operation pair is standard, even when RH is not mentioned.
4. **Negative literature:** impossibility theorems, failed programs, universality results, nonexistence results, and known reasons the mechanism cannot carry arithmetic information.
5. **Citation neighborhood:** backward references and, where available, later work around the closest primary sources.

Prefer original papers, monographs, authoritative surveys, and stable theorem sources. Search by mathematical structure rather than by the candidate's invented wording.

The audit must distinguish:

- the known object;
- the known theorem or mechanism;
- the immediate specialization to Mathia/RH;
- the proposed additional coupling or residual question;
- the exact point not located in the searched literature.

Failure to locate the same proposal is **not** proof of novelty. Never label a clue novel. Use bounded language describing the closest located prior art, the searched equivalences, and the residual question that remains unverified.

If the candidate is already known, is an immediate coordinate change, or differs only rhetorically, discard it. If prior art leaves a precise Mathia-specific residual question, reshape the candidate around that residual rather than claiming a new theory.

## Internal adversarial kill pass

Before a clue may be persisted, try seriously to destroy it. At minimum test whether:

- the construction is a tautology or a known RH-equivalent criterion with no new leverage;
- the desired positivity, zero-free region, spectral placement, or rigidity was inserted as an assumption;
- a quotient, determinant, Gram matrix, trace, average, or unmarked spectrum erases the claimed arithmetic distinction;
- the signal is a universal geometric or spectral carrier that survives matched non-prime controls;
- convergence, domains, operator classes, topology, limiting interchange, existence, or normalization invalidate the mechanism;
- a current Mathia finding already rules out the proposed category;
- the closest literature contains the same object-and-mechanism pair under another name;
- the proposed cross-field transfer lacks an exact dictionary;
- the decisive first test cannot actually distinguish success from a generic or classical phenomenon.

A candidate may survive with substantial uncertainty. It may not survive with an unnamed object, missing construction, unfalsifiable promise, or hidden import of RH.

## Ultra-selective clue gate

Emit or materially strengthen at most **one** clue in a run, and only when all of the following hold:

1. the mathematical object and proposed mechanism are explicit enough for another researcher to reconstruct;
2. the direction is not duplicated by current findings, Mind, Master state, graph relations, prior-art nodes, or clues in any lifecycle state;
3. it survives the mandatory literature audit without collapsing into a known mechanism or empty novelty claim;
4. it explicitly addresses the strongest relevant Mathia obstruction or explains why it operates outside that obstruction's hypotheses;
5. it has a decisive first test that can cheaply falsify, classicalize, or materially narrow it;
6. resolving it could redirect an existing line, create a genuine new information channel, or alter the global program;
7. its uncertainty is stated strongly enough that no reader could mistake it for evidence.

A clever analogy, an unexplored keyword combination, or a long speculative derivation does not pass this gate.

When the same precise question already exists as `status: proposed`, prefer materially strengthening that clue with a sharper construction, stronger persisted basis, closer literature boundary, or more decisive test. Do not touch accepted, rejected, or resolved clues.

## Clue handoff

Use `.agents/skills/mathia-research-clues/SKILL.md` without changing its lifecycle semantics.

For a question clearly owned by an existing line, write:

```text
research/<line>/clues/CLUE-<slug>.md
```

For a genuinely cross-line question or a possible new research line, write:

```text
research/clues/CLUE-<slug>.md
```

Use:

```yaml
origin: visionary-researcher
```

Set `target_line` to the exact existing line, `global`, or `new-line-candidate` as appropriate. There is no separate Master inbox: the Master Researcher already consumes local and global clues, so a global Visionary clue is the handoff to Master.

The clue's `based_on` list must cite the persisted Master/Mind/finding/prior-art/clue paths that motivated and constrained the proposal. In `## Evidence boundary`, include compact bibliographic identifiers for the closest authoritative external literature, state what was searched, identify the exact overlap, and state the residual question not established there. Do not turn the clue into a literature review or search log.

The Visionary must not set `accepted`, `rejected`, or `resolved`. Research Watch remains responsible for independent reconstruction, literature verification, derivation, stress testing, and disposition.

## Ownership and hard path gate

This skill may write only to proposed clue files under:

```text
research/<discovered-line>/clues/**
research/clues/**
```

It must not modify:

```text
research/master/**
research/mind/**
research/<line>/mind/**
research/graph/**
research/<line>/graph/**
research/prior_art/**
research/<line>/findings/**
*.review.md
research/<line>/README.md
research/<line>/SOURCES.md
research/<line>/LEAN_CANDIDATES.md
scheduled tasks
code/tests/docs/experiments
.obsidian/**
```

It must not create, delete, move, initialize, merge, pause, split, or recolor a research line. Those remain explicit user/portfolio decisions.

Do not create a `research/visionary/` directory, state snapshot, candidate backlog, run ledger, source-search history, or empty marker file.

## Publication policy

A scheduled Visionary pass may publish a clue change directly to the default branch only when the ultra-selective gate and all shared clue gates pass.

Before each commit:

1. refresh the default branch and ensure the evidence/literature basis is still coherent;
2. inspect the complete diff;
3. verify every changed path is an authorized clue path;
4. verify every clue remains `status: proposed` and uses `origin: visionary-researcher`;
5. verify the clue includes a concrete construction, decisive test, and bounded literature/evidence boundary;
6. verify no state, finding, review, Mind, graph, prior-art, task, or unrelated file changed;
7. remove formatting churn and any text that records the run rather than the research question.

Use:

```text
research(visionary): propose <clue>
research(visionary): sharpen <clue>
```

If no candidate passes the gate, create no commit. Never commit merely to show that the weekly task ran or that literature was searched.

## Notification and reporting

This role has one deliberate exception to the shared low-noise clue default because a qualifying Visionary output is expected to be rare.

- Notify when the Visionary successfully creates or materially strengthens a `status: proposed` clue and publishes it to the default branch. This published clue is the task's positive result.
- Keep that notification compact: identify the clue path, `target_line`, exact research question, decisive first test, and publication commit. Do not describe discarded candidates or the complete literature search.
- The eventual Research Watch still notifies separately if it changes the clue to `status: accepted`.
- Notify when a workflow, required-capability, synchronization, path-gate, or publication failure prevents intended persistence.
- Do not notify for null runs, rejected internal candidates, unchanged clues, routine literature-search completion, or weekly status.

This exception applies only to the Visionary Researcher's own publication of a qualifying clue; it does not change notification policy for other clue producers.

## Operating cadence

This role is designed for a **weekly ultra-effort pass**, not a daily quota. The full-state read, broad literature audit, and adversarial candidate tournament need depth; running daily would mostly reprocess an almost unchanged search space, amplify recent anchoring, and create pressure to emit weak ideas.

A material program reset or a major new obstruction may justify an explicit extra run, but the Visionary must never modify its own schedule.
