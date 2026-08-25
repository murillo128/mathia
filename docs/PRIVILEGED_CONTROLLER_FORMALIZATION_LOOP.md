# Privileged-controller formalization loop

## Status

This document records a **downstream exploratory research-system hypothesis** for use after the local specialist models are trained enough to make the loop meaningful, in particular after Qwen-Mathia and a Qwen-Lean planner exist as usable components.

It is **not**:

- an active implementation plan;
- authorization to change the current Mathia training line;
- a new benchmark or quality-assessment program;
- a commitment to a permanent multi-agent framework;
- a claim that the listed target theorems are currently within reach.

The purpose is to preserve a concrete idea for turning the Mathia / planner / qwen-lean stack into a system that produces real Lean formalizations without making success depend on resolving the Riemann Hypothesis.

The central proposal is:

> For mathematically solved theorems whose Lean statement exists but whose proof is still missing, allow a strong frontier controller such as Codex to read the known mathematical proof as **privileged information**, while keeping that proof hidden from Mathia. Codex directs conceptual exploration; Mathia generates intuitions and hypotheses; a Lean planner translates useful intuitions into formal proof plans; qwen-lean attempts the proof; Lean provides exact evidence; Codex uses both the hidden proof and the observed evidence to decide where to spend the next round of local reasoning.

The known proof is therefore a **controller-side navigation oracle**, not a prompt to Mathia and not a trajectory that the system must imitate.

---

## Why this is useful

Using the Riemann Hypothesis itself as the only visible success criterion makes almost every intermediate improvement observationally useless: a substantially better research system can still return `no proof` for RH indefinitely.

A more productive downstream regime is to work on theorem statements for which:

1. the mathematics is already known to be true;
2. a mathematical proof exists in the literature;
3. the theorem has a usable Lean statement, ideally already accepted by a public formalization project;
4. the Lean proof is missing or incomplete.

Then the output is not merely an assessment score. The output is a mathematical artifact:

```text
existing Lean statement + known mathematics + no Lean proof
                         |
                         v
              controller-guided search
                         |
                         v
                  verified Lean proof
```

Closing such a `sorry` is concrete progress. If no complete Lean proof previously existed, it is a new formalization of known mathematics.

RH remains a long-horizon north star, but it is no longer the unit of work.

---

## Relationship to the existing Mathia architecture

This proposal is a concrete specialization of two existing downstream Mathia hypotheses:

- [`THREE_LAYER_RESEARCH_SYSTEM.md`](THREE_LAYER_RESEARCH_SYSTEM.md), which already gives Codex a possible later role as a scarce research director above Mathia and a formal specialist;
- [`CONCEPTUAL_FORMAL_SEARCH_WITH_PARTIAL_PROOFS.md`](CONCEPTUAL_FORMAL_SEARCH_WITH_PARTIAL_PROOFS.md), which already considers populations of intuitions, formal evidence, partial proofs, recursive obligations, branch revision, pruning, and allocation of local compute.

The new decision recorded here is specifically about **information asymmetry**:

> On solved-theorem formalization tasks, Codex may see the known proof while Mathia normally does not.

This lets the controller use information unavailable in genuinely open mathematics without training the local conceptual researcher to depend on that information.

---

## Candidate division of labor

```text
                         KNOWN HUMAN PROOF
                                |
                                | privileged information
                                v
                    +-------------------------+
                    |          CODEX          |
                    |    research controller  |
                    |                         |
                    | literature / proof      |
                    | research state          |
                    | Lean evidence           |
                    | branch selection        |
                    +------------+------------+
                                 |
                  directions / questions /
                 criticism / branch allocation
                                 |
                                 v
                    +-------------------------+
                    |       QWEN-MATHIA       |
                    |                         |
                    |   proof normally hidden |
                    |                         |
                    | intuitions              |
                    | representations         |
                    | hypotheses              |
                    | intermediate objects    |
                    | candidate lemmas        |
                    +------------+------------+
                                 |
                                 v
                    +-------------------------+
                    |   QWEN-LEAN-PLANNER     |
                    |                         |
                    | mathematical intuition  |
                    |          ->             |
                    | Lean-oriented plan      |
                    +------------+------------+
                                 |
                                 v
                    +-------------------------+
                    |       QWEN-LEAN         |
                    |                         |
                    | tactics / proof terms   |
                    | partial proofs          |
                    +------------+------------+
                                 |
                                 v
                               LEAN
                                 |
                 verified proof / obligations /
                  rejected reductions / errors
                                 |
                                 +-----------> CODEX
                                                |
                                                `----> repeat
```

A computational/tool layer may sit beside this loop for deterministic search, library lookup, falsification, simplification, or proof-state extraction.

---

## Information boundaries

The components should not all receive the same context.

### Controller-private information

Codex may receive:

- the theorem statement;
- the known mathematical proof or proofs;
- relevant papers and literature;
- known formalizations of neighboring results;
- the complete branch history;
- Lean proof attempts and diagnostics;
- partial-proof dependency trees;
- a compressed global research state;
- information about which local branches are redundant, promising, or sterile.

### Mathia-visible information

Mathia should normally receive only what is useful for conceptual mathematical work, for example:

- the current mathematical problem or selected subproblem;
- definitions and mathematical context;
- previously verified facts that the controller chooses to expose;
- selected earlier Mathia intuitions;
- abstracted mathematical feedback from formal attempts;
- a controller-selected conceptual question or direction.

The full known proof should normally remain hidden.

### Planner-visible information

The Lean planner may receive:

- the exact Lean theorem or current Lean goals;
- the relevant Mathia intuition or candidate route;
- available library declarations and previously verified local lemmas;
- formal context and types;
- proof-state information needed to turn the mathematical idea into a Lean-oriented sequence of reductions.

The planner is not intended to replace Mathia's conceptual role. Conversely, Mathia should not be forced to become a Lean tactic debugger.

### Qwen-Lean-visible information

The formal prover receives the exact proof task and planner guidance necessary to generate Lean code. Lean remains the final verifier.

---

## Why the known proof should normally be hidden from Mathia

### 1. The capability should survive the transition to open problems

For a solved theorem:

```text
Codex:  theorem + literature + known proof + research state
Mathia: theorem + selected research state
```

For an open theorem:

```text
Codex:  theorem + literature + research state
Mathia: theorem + selected research state
```

The Mathia interface can remain essentially unchanged. Only the controller loses its hidden oracle.

If Mathia instead learns to rely on:

```text
theorem + proof -> intuition
```

then the learned behavior is least useful exactly where the project ultimately cares most: problems for which no proof exists.

The desired reusable behavior is closer to:

```text
theorem + mathematical state
          |
          v
new representations / hypotheses / intuitions / subproblems
```

### 2. It avoids collapsing conceptual research into proof paraphrase

The goal is not for Mathia to summarize or compress the published proof. It is to operate as a local mathematical researcher under direction.

Codex may know that the published route uses positivity, a character argument, a decomposition, or a particular intermediate lemma. Instead of transmitting the route directly, it can pose a weaker mathematical research direction, for example:

> Investigate the positivity-based branch. Is there a natural auxiliary quantity whose sign is constrained by the hypotheses?

Mathia still has to produce the mathematical representation or mechanism.

### 3. It creates a controlled analogue of scientific supervision

A human research supervisor may know substantially more literature than a junior researcher without dictating every proof step. The supervisor can notice when a branch is near a known productive region, when it is repeating a dead end, or when a missing lemma deserves attention.

The privileged controller is intended to play an analogous role while abundant local inference performs much of the exploration.

---

## The known proof is an oracle of navigation, not a mandatory trajectory

The controller should not force every successful branch back onto the published proof.

Suppose the known proof is:

```text
A -> B -> C -> theorem
```

but Mathia proposes:

```text
X -> Y -> theorem
```

and Lean begins to certify `X`, `Y`, or the reduction from them to the theorem. That branch should remain live even if it does not resemble the published route.

The hidden proof gives Codex a strong prior about productive mathematics, but it should not erase potentially new formal or mathematical routes.

A useful policy distinction is:

```text
published route resembles branch
    -> strong reason to continue when formal evidence is compatible

branch differs from published route but gains verified structure
    -> continue; novelty is not a defect

branch differs and repeatedly yields no mathematical or formal structure
    -> controller may prune or redirect it
```

This is especially important because a new Lean formalization may naturally prefer a proof architecture different from the historical paper proof.

---

## Core research loop

A solved-theorem run could proceed as follows.

### 1. Controller preparation

Codex reads:

- the Lean theorem statement;
- the known mathematical proof(s);
- relevant Mathlib / Formal Conjectures context;
- already formalized neighboring lemmas;
- the current research state.

It identifies several possible conceptual regions worth exploring without exposing the complete proof.

### 2. Mathia exploration

Mathia generates a population of candidate perspectives, such as:

- a useful invariant;
- a positivity mechanism;
- a decomposition;
- a change of representation;
- a contradiction setup;
- an intermediate object;
- a bridge between two existing theories;
- a weakening or strengthening that exposes a reusable lemma.

Some branches may be spontaneous; others may be directed by Codex.

### 3. Planner translation

For selected Mathia branches, Qwen-Lean-Planner converts the conceptual idea into a Lean-oriented plan:

- which intermediate facts to prove;
- what objects to introduce;
- which library facts appear relevant;
- how the parent theorem may reduce to smaller goals;
- where explicit local lemmas should be inserted.

### 4. Formal attempts

Qwen-Lean attempts complete or partial proofs.

Useful outcomes include:

- a complete Lean proof;
- a checked proof skeleton with explicit remaining obligations;
- a verified intermediate lemma;
- a reduction that is formally valid modulo one or more extracted holes;
- evidence that a proposed reduction requires a stronger hypothesis than available;
- repeated failure that exposes a library or formalization bottleneck.

### 5. Evidence abstraction

Raw Lean errors should not automatically be sent to Mathia.

Where possible, Codex or deterministic tooling summarizes them mathematically, for example:

```text
The reduction is valid except for an obligation asserting compatibility
between the constructed object and the original action.
```

or:

```text
Several formal attempts need a property stronger than the current hypotheses.
The issue is mathematical, not merely syntactic.
```

This preserves the semantic / formal boundary.

### 6. Controller decision

Using both the hidden proof and the actual evidence, Codex can choose among:

- deepen a promising branch;
- ask Mathia to revise a branch while preserving its conceptual direction;
- decompose a remaining obligation;
- expose a verified fact to Mathia;
- ask for a different representation;
- allocate additional planner / qwen-lean samples;
- merge two branches;
- abandon a sterile branch;
- intervene with a stronger hint when local search has stalled.

### 7. Repeat until proof or a meaningful blocker

The loop ends with a verified proof or with a research state that clearly records the unresolved mathematical/formal bottleneck.

---

## Partial proofs as certified reductions

For difficult theorems, a checked proof skeleton can be more valuable than repeated all-or-nothing whole-proof generation.

Example:

```lean
by
  have h1 : L1 := by
    ...
  have h2 : L2 := by
    sorry
  ...
  exact ...
```

If Lean accepts the surrounding structure modulo `sorry`, the parent theorem has been reduced to the explicit obligation `L2`.

The interpretation is:

> a checked partial proof is a formally certified reduction of one theorem to a set of remaining goals.

However, `sorry` is never progress by itself. The degenerate output

```lean
by
  sorry
```

contains no useful reduction. The value of a partial proof comes from verified surrounding structure and, ultimately, from closing or productively decomposing its holes.

This mechanism allows the research process to become a tree of formally linked subproblems rather than a sequence of independent whole-proof guesses.

---

## What counts as success

This downstream line should not be framed primarily as another model-quality assessment.

The main useful outputs are:

1. a previously missing verified Lean proof;
2. reusable verified intermediate lemmas;
3. a checked reduction of a difficult theorem to clearer subproblems;
4. identification and closure of missing Mathlib infrastructure;
5. in the strongest case, a complete formalization of a mathematically solved theorem for which no complete Lean formalization previously existed.

Operational telemetry such as number of attempts, branches, or failures may still be useful for engineering and resource allocation, but it is secondary to producing verified mathematics.

---

## Candidate source repositories

### Mathia

Repository:

- <https://github.com/murillo128/mathia>

Relevant design documents:

- [`docs/THREE_LAYER_RESEARCH_SYSTEM.md`](THREE_LAYER_RESEARCH_SYSTEM.md)
- [`docs/CONCEPTUAL_FORMAL_SEARCH_WITH_PARTIAL_PROOFS.md`](CONCEPTUAL_FORMAL_SEARCH_WITH_PARTIAL_PROOFS.md)
- [`docs/CONCEPTS_DIMENSIONS_INTUITION.md`](CONCEPTS_DIMENSIONS_INTUITION.md)

### Qwen-Lean

Repository:

- <https://github.com/murillo128/qwen-lean>

The intended downstream role is the formal side of the stack: Qwen-Lean-Planner converts mathematical intuitions into formal plans, and Qwen-Lean executes proof search against Lean.

The exact planner/prover interfaces should be defined only after their training work is complete enough to justify integration.

### Google DeepMind Formal Conjectures

Repository:

- <https://github.com/google-deepmind/formal-conjectures>

This is a particularly useful source of target statements because it distinguishes categories including:

- `@[category research open]`
- `@[category research solved]`
- `@[category textbook]`
- `@[category API]`
- `@[category test]`

The `research solved` category provides a natural source of **known mathematics with formal Lean statements that may still contain `sorry`**.

Useful repository locations include:

- <https://github.com/google-deepmind/formal-conjectures/tree/main/FormalConjectures/ErdosProblems>
- <https://github.com/google-deepmind/formal-conjectures/tree/main/FormalConjectures/Wikipedia>
- <https://github.com/google-deepmind/formal-conjectures/tree/main/FormalConjectures/Paper>
- <https://github.com/google-deepmind/formal-conjectures/tree/main/FormalConjectures/Arxiv>

The repository also contains fixed subsets such as `FC100SolvedSet1`, but for this proposed downstream line the important use is **not another benchmark**. It is a source of real theorem holes to close.

### Mathlib

Repository:

- <https://github.com/leanprover-community/mathlib4>

Riemann-zeta / analytic-number-theory infrastructure already exists in Mathlib and provides both reusable dependencies and examples of serious completed formalization work.

Relevant files include:

- Riemann zeta infrastructure: <https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/NumberTheory/LSeries/RiemannZeta.lean>
- nonvanishing on `Re(s) >= 1`: <https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/NumberTheory/LSeries/Nonvanishing.lean>
- discreteness / finiteness of zeta zeros on compact sets: <https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/NumberTheory/LSeries/ZetaZeros.lean>

These results are useful both as infrastructure and as evidence that substantial analytic-number-theory formalization around zeta is now available in Lean.

---

## Concrete theorem/proof sources found so far

The following are **illustrative candidates and source material**, not a frozen target queue.

### 1. Erdős Problem 1141: a useful partially formalized dependency chain

Formal Conjectures statement:

- <https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/1141.lean>

The file records the main Erdős 1141 result as mathematically solved and links an existing conditional Lean formalization. That formalization depends on two deep external inputs that remain stated as `sorry` in Formal Conjectures:

- `erdos_1141.variants.pollack_1_3`
- `erdos_1141.variants.mertens_third`

This makes the theorem family especially attractive conceptually: the downstream result is already formalized conditionally, so the remaining holes are explicit and mathematically meaningful.

Existing conditional Lean proof by Yuta Oriike:

- <https://github.com/yuta0x89/ErdosProblems/blob/a1319f732cdee5140faf47d984e2c451c1184803/Erdos1141.lean>

The proof itself documents that it mirrors the paper and axiomatizes precisely the two deep analytic inputs.

Underlying 2026 paper used by that formalization:

- B. Alexeev, M. Putterman, M. Sawhney, M. Sellke, G. Valiant, *Short proofs in combinatorics, probability and number theory II*
- <https://arxiv.org/abs/2604.06609>

#### Pollack input

Formal Conjectures statement:

```lean
theorem erdos_1141.variants.pollack_1_3 ... := by
  sorry
```

The existing conditional formalization points to:

- P. Pollack, *Bounds for the First Several Prime Character Nonresidues*, Theorem 1.3
- <https://www.ams.org/journals/proc/2017-145-07/S0002-9939-2016-13432-1/S0002-9939-2016-13432-1.pdf>

This is a clear example of the intended workflow: Codex can read the paper theorem/proof and guide Mathia toward the conceptual ingredients without simply copying the proof into Mathia's context.

#### Mertens input

Formal Conjectures records a weakened form of Mertens' third theorem:

```lean
theorem erdos_1141.variants.mertens_third (n : ℕ) (hn : 3 ≤ n) :
    1 / (3 * Real.log n) ≤
      ∏ p ∈ (Finset.range (n + 1)).filter Nat.Prime,
        (1 - 1 / (p : ℝ)) := by
  sorry
```

The source cited there is:

- F. Mertens, *Ein Beitrag zur analytischen Zahlentheorie* (1874)

The conditional Erdős 1141 formalization also notes that it uses the same kind of Mertens input as Pietro Monticone's earlier Erdős 237 development.

This is interesting for the project because Mertens-style estimates lie substantially closer to primes / analytic number theory / zeta than unrelated olympiad-style proof tasks.

---

### 2. Riemann zeta values in Formal Conjectures

Source:

- <https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/Wikipedia/RiemannZetaValues.lean>

This file contains a mixture of open and solved statements, all already expressed as Lean theorems.

Solved statements with `sorry` include:

#### Apery: irrationality of `zeta(3)`

```lean
@[category research solved, AMS 11 33]
theorem irrational_three :
    ∃ x, Irrational x ∧ riemannZeta 3 = x := by
  sorry
```

Reference recorded by Formal Conjectures:

- R. Apéry (1979), *Irrationalité de ζ(2) et ζ(3)*, Astérisque 61, 11–13.

This is likely far harder than a first target, but it is an example of a solved zeta theorem whose statement is already present in Lean and whose formalization would be directly aligned with the long-term mathematical domain.

#### Rivoal: infinitely many odd zeta values are irrational

```lean
@[category research solved, AMS 11 33]
theorem infinite_irrational_at_odd :
    { n : ℕ | ∃ x, Irrational x ∧ riemannZeta (2 * n + 1) = x }.Infinite := by
  sorry
```

Reference recorded by Formal Conjectures:

- T. Rivoal (2000), *La fonction zeta de Riemann prend une infinité de valeurs irrationnelles aux entiers impairs*, Comptes Rendus de l'Académie des Sciences, Série I 331(4), 267–270.

#### Zudilin: one of `zeta(5), zeta(7), zeta(9), zeta(11)` is irrational

```lean
@[category research solved, AMS 11 33]
theorem exists_irrational_of_five_seven_nine_eleven :
    {5, 7, 9, 11} ∩
      { a | ∃ x, Irrational x ∧ riemannZeta a = x} |>.Nonempty := by
  sorry
```

Reference recorded by Formal Conjectures:

- W. Zudilin (2001), *One of the numbers ζ(5), ζ(7), ζ(9), ζ(11) is irrational*, Russian Mathematical Surveys 56(4), 774–776.

The individual irrationality statements for `zeta(5)`, `zeta(7)`, `zeta(9)`, `zeta(11)`, and the general odd-value irrationality statement remain open and are correctly marked `research open`; they are therefore not appropriate solved-proof oracles.

---

### 3. Existing Mathlib zeta proofs as infrastructure and exemplars

#### Zeta zeros are discrete

Mathlib file:

- <https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/NumberTheory/LSeries/ZetaZeros.lean>

Main results include:

```lean
isClosed_riemannZetaZeros
isDiscrete_riemannZetaZeros
IsCompact.inter_riemannZetaZeros_finite
```

So Lean already knows, in particular, that the zero set of the Riemann zeta function is discrete and that a compact set contains only finitely many zeta zeros.

#### Nonvanishing on `Re(s) >= 1`

Mathlib file:

- <https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/NumberTheory/LSeries/Nonvanishing.lean>

A main consequence is:

```lean
riemannZeta_ne_zero_of_one_le_re
```

which proves nonvanishing of the Riemann zeta function on the half-plane `Re(s) >= 1`.

The file develops the result through Dirichlet-character `L`-functions and positivity arguments. It is valuable infrastructure for future zeta work and also an example of the kind of long, layered analytic-number-theory proof that the eventual controller / Mathia / planner / qwen-lean system should be able to navigate.

---

## A possible progression of real formalization work

This is intentionally **not** a benchmark ladder and should not be frozen before the local models are ready.

A sensible progression could later choose theorem holes based on whether they advance useful mathematical infrastructure:

```text
explicit missing lemmas in an existing conditional formalization
                     |
                     v
Mertens / prime estimates / Dirichlet-character inputs
                     |
                     v
harder solved analytic-number-theory theorems
                     |
                     v
solved zeta-value theorems
                     |
                     v
new reusable intermediate results around zeta / primes
                     |
                     v
open mathematical questions
                     |
                     v
Riemann Hypothesis as long-horizon north star
```

The important shift is that each successful step produces verified mathematics rather than merely a score.

---

## Controller steering should be graded, not all-or-nothing

The privileged proof creates a risk that Codex simply solves the theorem itself and uses the local components as transcription workers.

A later implementation should therefore distinguish levels of intervention.

Possible controller actions, from weaker to stronger, include:

1. choose among Mathia-generated branches;
2. request more work within a conceptual region;
3. provide abstracted evidence from formal attempts;
4. ask for a missing type of intermediate object or relation;
5. point toward a broader mathematical mechanism used in the literature;
6. provide a more explicit intermediate lemma;
7. in the strongest fallback, expose a substantial part of the known proof.

The early levels preserve more local mathematical work. Stronger hints remain available when the purpose is to finish a real formalization rather than run a clean capability experiment.

Because this downstream line is oriented toward producing proofs rather than another quality assessment, there is no requirement that every completed theorem be attributed cleanly to one component. Still, provenance should be recorded so that the system can later learn which kinds of controller interventions are most useful.

---

## Research-state requirements

Long-running theorem work will need a compressed mathematical state rather than a transcript dump.

Likely information includes:

- current target theorem and extracted subgoals;
- verified local lemmas;
- unresolved dependencies;
- live conceptual branches;
- branches rejected by formal contradiction or missing assumptions;
- branches merely unproductive so far;
- equivalent or redundant formulations;
- known library gaps;
- useful definitions and bridge objects;
- provenance of controller hints;
- which information came from the hidden proof versus independent local discovery.

The exact state schema should not be designed prematurely. The main invariant is that the state captures mathematical content and evidence, not conversation chronology.

---

## Transition from solved to open mathematics

The strongest reason to preserve the information boundary is that the same research machinery can later operate when there is no known proof.

### Solved theorem mode

```text
Codex
  sees known proof
  uses it as privileged navigation information

Mathia
  does not normally see the proof

Planner + qwen-lean + Lean
  create and verify formal reductions
```

### Open theorem mode

```text
Codex
  no longer has a known-proof oracle
  relies on literature, global reasoning, and accumulated evidence

Mathia
  interface largely unchanged

Planner + qwen-lean + Lean
  interface largely unchanged
```

This avoids building a solved-theorem-only local researcher.

The hoped-for progression is not that solving known theorems proves the system can solve RH. Rather, solved theorems provide a productive environment in which the same conceptual / formal research dynamics can mature while generating useful mathematical artifacts.

---

## Main risks

### Controller domination

If Codex must reconstruct every proof step and feed it downstream, the architecture is not amplifying frontier reasoning; it is merely distributing transcription.

### Proof leakage into Mathia

If controller feedback becomes too explicit, Mathia may learn or execute proof paraphrase rather than conceptual exploration.

### Planner collapse into generic proving

If the planner ignores Mathia and directly solves the theorem, the intended conceptual-to-formal bridge is not functioning as designed.

### Mathia collapse into Lean debugging

Passing raw tactic errors back into Mathia may turn it into a syntax/formal-state model rather than a semantic mathematical specialist.

### Published-proof anchoring

The hidden proof may bias Codex so strongly that genuinely different productive branches are pruned before formal evidence can support them.

### Branch explosion

Abundant local inference can create many hypotheses without accumulating verified structure. Complexity of the search tree is not progress.

### Formal-library bottlenecks

A mathematically straightforward paper step may require substantial missing Mathlib infrastructure. This is still useful information and can itself define a concrete formalization target.

---

## Questions deliberately left open

This document does not decide:

- the exact controller prompt or API;
- how much of a known proof Codex may expose at each intervention level;
- how hidden proof material is stored or isolated from Mathia;
- the permanent research-state schema;
- the planner input/output format;
- whether partial proofs use literal `sorry`, extracted goals, metavariables, or another mechanism;
- branch-count or compute-allocation policies;
- which solved theorem should be attempted first;
- whether a completed formalization should be upstreamed to Formal Conjectures, Mathlib, or a dedicated repository;
- how much human review is required before an external contribution;
- when the system is mature enough to move from solved mathematics back toward genuinely open problems.

Those decisions should be made only after Qwen-Mathia and Qwen-Lean-Planner are available and the concrete integration constraints are known.

---

## Summary hypothesis

The proposed downstream system is:

```text
known proof (controller-only, when available)
                 |
                 v
        Codex research director
                 |
       conceptual direction
                 v
            Qwen-Mathia
                 |
       mathematical intuition
                 v
        Qwen-Lean-Planner
                 |
          formal strategy
                 v
             Qwen-Lean
                 |
                 v
                Lean
                 |
       exact checked evidence
                 |
                 `------> Codex -> repeat
```

The central design principle is:

> **Use known proofs to guide the controller, not to replace the local research process.**

This gives the project a path to produce verified, potentially novel Lean formalizations of known mathematics while preserving the same local conceptual-research interface that would later be needed when the proof is genuinely unknown.
