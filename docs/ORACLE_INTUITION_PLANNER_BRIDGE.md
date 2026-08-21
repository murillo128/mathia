# Oracle intuition and planner bridge

## Status

This document records the accepted conceptual boundary between Mathia and a separate downstream proof-search planner. It is a durable architecture note, not a roadmap phase, execution order, training schedule, or authorization to modify the frozen #32 experiment.

Controlling design issue: #52.

The purpose is to isolate two different capabilities that were previously conflated:

1. producing a useful mathematical intuition;
2. converting that intuition into an operational proof-search strategy for a Lean prover.

## The gap in the current layered picture

The existing Mathia direction deliberately separates conceptual mathematics from formal execution. The missing bridge is that a compact conceptual intuition may still be too abstract for a whole-proof prover to exploit reliably.

The refined conceptual architecture is:

```text
Mathia
meaning / mechanism / representation / intuition
                |
                v
qwen-lean-planner
proof-search strategy / operational decomposition
                |
                v
qwen-lean
formal proof generation / search
                |
                v
Lean
exact verification
```

`qwen-lean-planner` is owned by the qwen-lean repository. Mathia owns the semantic interface that feeds it.

## ACCEPTED — train the bridge first under an oracle-intuition condition

Current Mathia capability is not yet established. Planner research should therefore first assume the conceptual layer succeeds rather than make planner learning depend on theorem-only Mathia quality.

For known verified theorems, a proof-aware oracle mode may use the complete source proof as privileged input to generate a compact natural-language intuition:

```text
Lean theorem + verified proof
              |
              v
proof-aware oracle intuition generator
              |
              v
accepted natural-language intuition
              |
              v
qwen-lean-planner
```

This is an upper-bound/bootstrap condition. It does **not** show that Mathia can discover the same intuition from the theorem alone.

The source proof exists only to make the conceptual input unusually favorable while the planner interface is being studied.

## ACCEPTED — the stable Mathia interface is natural mathematical language

The intuition passed across the Mathia boundary should remain natural mathematical language rather than Lean, a tactic script, a proof term, or a new formal DSL.

Allowed content includes:

- mathematical mechanisms and representations;
- symmetry, invariance, decomposition, contradiction, quotienting, factorization, monotonicity, duality, and similar concepts;
- qualitative intermediate mathematical goals;
- equations and ordinary mathematical notation;
- explanations of what information matters or can be ignored;
- why a transformation or reduction should expose the core difficulty;
- alternative conceptual routes when materially different.

The interface should remain usable later when Mathia sees only the theorem/problem state.

## ACCEPTED — the source proof must not cross the boundary

The planner must never receive the source proof directly or through a hidden artifact field.

The downstream artifact may contain:

- theorem/public mathematical context;
- accepted intuition text;
- generator identity/configuration needed to interpret the experiment;
- leakage classification and rejection metadata;
- compact provenance needed for matched evaluation.

It must not contain the source proof or a retrievable source-proof payload.

## ACCEPTED — leakage is rejected, not repaired

Because the oracle generator has seen the proof, its output requires an explicit leakage gate before it can be used as conceptual input.

A response that fails the gate is discarded as a whole. Do not strip tactics, rewrite code into prose, remove identifiers, or otherwise transform a rejected output into an accepted one.

A bounded regeneration policy may be used, but it must finish before any downstream planner/prover result is observed and must never be conditioned on proof-search success.

## Two different leakage problems

### Generic Lean/formal leakage

Reject output that materially resembles Lean implementation, including characteristic combinations of:

- Lean code fences;
- `:= by` and proof-script structures;
- `have`, `exact`, `apply`, `refine`, `rw`, `simp`, `simpa`, `aesop`, `linarith`, and similar tactic syntax when used as code/instructions rather than ordinary prose;
- Lean proof terms or goal-state syntax;
- qualified formal identifiers and mathlib APIs when they transmit implementation detail;
- executable or near-executable proof fragments.

Individual English words are not enough for rejection. Detection should rely on characteristic syntactic/structural patterns and hard-reject signatures.

### Source-proof-specific leakage

Natural prose can still transmit the proof implementation. The oracle pipeline should therefore extract suspicious implementation features from the exact source proof, such as:

- tactic names and tactic sequences;
- lemma/theorem identifiers;
- qualified names;
- unusual local/formal identifiers;
- distinctive short implementation fragments.

An intuition with suspicious overlap can then be rejected even when it contains no code block.

Example of unacceptable conceptual output:

> Apply `Foo.bar`, rewrite with `Baz.qux`, and finish using `Real.someLemma`.

The problem is not prose style; it is transmission of the privileged implementation.

## ACCEPTED — mechanically auditable gate first

The primary leakage gate should be deterministic and independently testable. An LLM judge may be used as a secondary semantic audit, but not as the sole mechanism deciding whether privileged proof information crossed the boundary.

At minimum preserve reason categories conceptually equivalent to:

```text
accepted
rejected_lean_syntax
rejected_formal_identifier
rejected_source_proof_overlap
rejected_proof_like
```

The exact implementation and thresholds are owned by #52.

## ACCEPTED — oracle quality is not Mathia quality

A successful proof-aware intuition is evidence only that the downstream system was given a useful conceptual representation under privileged conditions.

Do not report oracle-planner gains as evidence that theorem-only Mathia can discover the intuition.

This distinction creates a useful upper-bound comparison:

```text
qwen-lean alone
        |
        v
formal baseline

proof-aware oracle intuition
        |
        v
planner + qwen-lean
        |
        v
oracle-intuition performance

later theorem-only Mathia intuition
        |
        v
planner + qwen-lean
        |
        v
learned-intuition performance
```

The gap between oracle-intuition and theorem-only Mathia performance is evidence about the conceptual layer rather than the planner layer, provided the downstream components are frozen.

## ACCEPTED — future Mathia reward should be downstream utility

Once a useful planner/prover channel exists, a later Mathia experiment can hide the source proof and optimize theorem-only intuitions by what they enable downstream:

```text
theorem/problem state
        |
        v
      Mathia
        |
 accepted natural-language intuition
        |
        v
 frozen qwen-lean-planner
        |
        v
 frozen qwen-lean
        |
        v
       Lean
        |
        v
 downstream reward to Mathia
```

The desired signal is not similarity to the proof-aware oracle wording or to a frontier teacher. A different intuition is acceptable if it produces greater downstream formal utility.

The exact Mathia optimization method remains OPEN.

## Boundary with qwen-lean-planner

Mathia should express **what mathematical mechanism matters**.

The planner may express **how a Lean-aware proof search should operationalize that mechanism**.

This means Mathia should not be trained to become a tactic selector merely because tactic-level text is easier to reward. Conversely, the planner is allowed to be Lean-aware; preventing all Lean-specific planning belongs neither to this document nor to the Mathia leakage rule.

The critical invariant is that privileged source-proof implementation does not leak through Mathia into the planner.

## OPEN design questions

The Mathia-side design issue must still settle:

- the initial proof-aware oracle generator/checkpoint;
- exact prompt and output length policy;
- deterministic hard-reject patterns;
- source-proof feature extraction and overlap thresholds;
- mathematical-notation allowances;
- bounded regeneration semantics;
- adversarial fixtures and false-positive controls;
- the compact cross-repository artifact contract.

These are implementation/design details, not reasons to collapse the semantic/planning boundary.

## Relationship to existing Mathia research

This refinement is compatible with:

- `CONCEPTS_DIMENSIONS_INTUITION.md`: concepts and conceptual moves may still be the substrate from which theorem-only intuition eventually emerges;
- `THREE_LAYER_RESEARCH_SYSTEM.md`: the formal worker remains a separate reality-checking layer;
- `CONCEPTUAL_FORMAL_SEARCH_WITH_PARTIAL_PROOFS.md`: conceptual diversity can still organize formal search;
- `RIEMANN_AGENTIC_RESEARCH_LOOP_REFERENCE.md`: Riemann remains a later research consumer of the layered system.

The new point is that there is now an explicit learned planning boundary between conceptual intuition and formal proof execution.

## Non-goals

This document does not:

- change #32;
- define when planner work occurs in the roadmap;
- choose the planner RL algorithm;
- train Mathia;
- claim proof-aware oracle outputs are theorem-only reasoning;
- create gold tactic plans;
- authorize open-conjecture/Riemann execution;
- require Mathia and qwen-lean to share or merge weights.
