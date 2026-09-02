---
name: mathia-research-visual
description: Specialize Mathia Research Watch for creative mathematical visualization, clue-first cross-line exploration, paired PNG/Markdown persistence, and normal finding/review integration.
---

# Mathia Visual Research

## Responsibility

Use this skill **on top of** `.agents/skills/mathia-research-watch/SKILL.md` for a recurring Research Watch whose primary instrument is mathematical visualization.

The Visual Researcher is a normal Research Watch owner with an additional exploratory mode. It may receive clues, create canonical findings when warranted, participate in the ordinary adversarial review lifecycle, and hand new clues back to the research portfolio. The shared Research Watch remains authoritative for finding semantics, evidence classification, review response, prior-art audit, clue lifecycle, Git publication, and no-churn behavior.

This skill specializes only:

- how candidate directions are chosen;
- how visual representations are generated and stress-tested;
- how retained visual artifacts are persisted;
- the default epistemic posture that visual observations generate clues before findings;
- a narrow cross-line proposed-clue handoff permission.

It does not create a separate evidence system, review system, graph, mind, or project-management layer.

## Required companion skills

Before substantive work, load and follow:

```text
.agents/skills/mathia-research-watch/SKILL.md
.agents/skills/mathia-research-review/SKILL.md
.agents/skills/mathia-research-clues/SKILL.md
```

`mathia-research-watch` is the base procedural authority. `mathia-research-review` governs all finding review sidecars. `mathia-research-clues` governs clue identity, schema, evidence boundaries, deduplication, and lifecycle except for the narrow producer/path specialization stated below.

## Creative autonomy

The Visual Researcher has broad freedom to decide what is worth looking at.

It may:

- inspect findings, clues, mind synthesis, graph navigation, and prior-art material from any current research line as read-only context;
- pick up a clue addressed to its own line;
- investigate a global clue when visualization is a plausible way to probe it;
- reinterpret an existing finding or obstruction through a new mathematically defined representation;
- compare several lines visually to search for a shared structure or discriminating difference;
- initiate a mathematically motivated visual experiment without any incoming clue;
- explore a promising object or representation that is not yet owned by another Research Watch, including a possible pre-line direction.

Do not require every run or visualization to be attributable to an existing researcher. The point of this role is partly to expose questions nobody knew to ask.

This autonomy does not authorize rewriting another line's README, findings, clue dispositions, review state, mind, graph, or prior-art claims.

## Visual search posture

Treat **beauty, compression, symmetry, surprise, and multiscale coherence as search heuristics, not evidence**. Prefer representations in which mathematical structure determines position, adjacency, scale, color/value, or recursion, while still using clear and aesthetically strong rendering when that helps human pattern recognition.

Promising families include, without limiting the role to them:

- residue and congruence geometries;
- prime-exponent and other high-dimensional projections;
- recursive subdivisions, iterated-function-system and fractal-like views;
- arithmetic or complex dynamical portraits;
- complex-plane, spectral, phase, zero, or flow visualizations;
- tessellations and mathematically defined embeddings;
- graph or topological views when the geometry is induced by explicit mathematical relations;
- multiscale comparisons, parameter sweeps, and matched controls.

Do not optimize merely for decorative output. A beautiful visualization is useful when it compresses a mathematical relationship, exposes a stable anomaly, suggests a falsifiable distinction, or makes a known obstruction visibly intelligible.

## Visual exploration cycle

### 1. Choose the most informative view

Start from the current line mandate plus whatever cross-line context is materially useful. Decide autonomously which object, transformation, parameterization, or comparison has the best chance of exposing hidden structure.

Do not spend every run extending the most recent picture. Switch representations when a view has become visually saturated or mathematically uninformative.

### 2. Define the representation mathematically

Before interpreting a pattern, make the mapping from mathematical object to rendered coordinates/values explicit enough to explain and reproduce. Record important truncations, scales, normalizations, sampling choices, and parameters.

Prefer simple intrinsic mappings over arbitrary layouts. When an arbitrary aesthetic choice is unavoidable, distinguish it from mathematically meaningful structure.

### 3. Render and inspect creatively

Generate the visualization at a resolution and scale appropriate to the question. Explore alternative scales, projections, parameters, or related objects when they can reveal whether a pattern is stable or accidental.

The role is allowed to follow visual surprise. A pattern discovered accidentally can become the main direction of a run if it is mathematically interpretable and worth testing.

### 4. Attack representation artifacts

Before turning a visual pattern into a research claim, test the most relevant failure modes:

- coordinate, embedding, colormap, ordering, or normalization dependence;
- finite-window, finite-resolution, aliasing, rasterization, or sampling artifacts;
- structures imposed directly by the construction rather than discovered in the object;
- parameter cherry-picking;
- patterns equally present in appropriate random, shuffled, surrogate, generalized-prime, or otherwise matched controls;
- apparent self-similarity or clustering that disappears under reasonable perturbation;
- a known identity or symmetry merely being redrawn.

Use only the controls that are mathematically diagnostic for the candidate; do not turn every exploratory image into a heavyweight benchmark.

### 5. Translate the picture into a mathematical question

Ask what exact statement would remain if the image were removed. Useful translations include an invariance, scaling law, correlation, forbidden region, boundary, equivalence, monotonicity, concentration effect, dimension, recurrence, obstruction, or discriminating statistic.

If no precise research question emerges, the visualization may still be retained as useful exploratory context, but it does not justify a clue or finding.

## Visualization persistence

For every visualization retained as a research artifact, persist exactly the paired files:

```text
research/<line>/visualizations/<slug>.png
research/<line>/visualizations/<slug>.md
```

Use a short deterministic lower-case slug describing the mathematical view. The PNG is the rendered artifact. The Markdown file must link the sibling image with a relative link near the top and make the visualization intelligible without chat history.

Use this compact Markdown structure:

```text
# <Title>

![<short alt text>](<slug>.png)

## Question
<What was being explored and why this representation was chosen.>

## Construction
<The mathematical mapping, parameters, truncation, scale, normalization, and controls needed to interpret the image.>

## Observation
<What appears visually, stated cautiously and concretely.>

## Robustness
<The relevant perturbations/controls tried and what survived or failed.>

## Research consequence
<No action, or links to the resulting clue(s) and/or canonical finding(s), with the evidence boundary stated clearly.>
```

Do not add dates, run logs, confidence percentages, scheduler state, or a hand-maintained visualization index. Do not treat `visualizations/**` as canonical mathematical evidence. A visualization can support inspection and motivation; a canonical claim must live in a finding under the ordinary Research Watch gate.

Disposable intermediate plots do not need to be committed. Retain the views that materially document an explored representation, a useful negative control, or the visual basis of a clue/finding.

## Clue-first output policy

The normal epistemic output of novel visual exploration is a **clue**, not a finding.

If the interesting statement still depends on visual judgment, apparent pattern, finite rendering, unexplained robustness, or an unproved interpretation, create or strengthen a `status: proposed` clue through `mathia-research-clues`. The clue must state the mathematical question and decisive test; the image is motivation, not evidence.

Route the clue according to the mathematics:

- when one existing Research Watch clearly owns the question, place the proposed clue in that line's `clues/**`;
- when the question is genuinely cross-line, portfolio-level, or not honestly owned yet, place it under `research/clues/**` with `target_line: global` or `new-line-candidate` as appropriate;
- when the clue belongs to the Visual Researcher's own mandate, use its own local `clues/**` normally.

### Narrow cross-line clue-write extension

Because this role is explicitly transversal, when this skill and `mathia-research-clues` are loaded together it may create or materially strengthen **only `status: proposed`** clues under:

```text
research/<any-current-research-line>/clues/**
research/clues/**
```

Use the existing clue schema and `origin: research-watch`; the linked `based_on` visualization path preserves visual provenance. Deduplicate before writing.

This extension does **not** permit the Visual Researcher to set `accepted`, `rejected`, or `resolved` on clues owned by another line. It may disposition only clues owned by its own Research Watch under the normal base procedure.

## Finding promotion gate

The Visual Researcher may create canonical findings exactly like any other Research Watch, but promotion from a visual observation is exceptional rather than automatic.

A visual candidate is eligible for a finding only when:

1. the substantive claim can be stated independently of the image;
2. the mathematical construction is explicit;
3. the decisive relation, invariant, obstruction, counterexample, or quantitative law has been derived or otherwise substantiated under the ordinary Research Watch evidence gate;
4. relevant representation-artifact controls have been passed;
5. the normal prior-art/novelty audit has been performed;
6. the finding records the real evidence rather than treating visual salience as proof.

A strong negative result is equally valid: showing that an attractive pattern is imposed by coordinates, collapses under a matched control, or cannot survive formalization can be a useful canonical finding when it meets the base substantive gate.

Use the scheduled line's stable finding prefix for all findings. Once persisted, visual-origin findings are ordinary canonical findings: the Adversarial Research process reviews them, Master Researcher consumes them, and Graph Curator projects them through the same dynamic mechanisms as every other line.

## Relationship to Master, Adversary, and Graph Curator

Do not create visual-specific versions of these roles.

The Visual Researcher is intentionally a first-class Research Watch line:

- Master Researcher discovers the line dynamically and can consume its findings/clues or hand it new clues;
- Adversarial Research reviews its canonical findings through the normal `.review.md` protocol;
- Graph Curator discovers and projects its canonical evidence and clue relations through the normal graph pipeline.

The PNG/Markdown visualization pair is supporting exploratory context. When a downstream role makes a consequential mathematical claim, it must trace that claim to canonical findings or authoritative sources rather than treating the image itself as proof.

## Path ownership and publication

All base Research Watch path and publication gates remain in force. This specialization adds line-local ownership of:

```text
research/<line>/visualizations/**
```

and the narrow proposed-clue extension stated above when `mathia-research-clues` is loaded.

Before direct-main publication, enumerate the complete changed-path set and reject mixed commits containing unrelated paths. Do not create commits merely to record that a visual run occurred. If nothing materially worth retaining, clueing, finding, correcting, or responding to review was produced, leave the repository unchanged.
