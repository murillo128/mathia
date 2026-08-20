# Mathia

Mathia is an exploratory research project about **semantic and conceptual mathematical reasoning in language models**.

The project asks whether a model can learn mathematical meaning, representations, structural mechanisms, analogies, invariants, generalizations, and useful intuitions at a level distinct from arithmetic execution and formal theorem proving.

## Current working hypothesis

The active training hypothesis is now more structured:

```text
mathematical concepts
        |
conceptual dimensions / moves
        |
candidate intuitions emerge
        |
initial frontier-teacher distillation
        |
downstream mathematical fertility
```

The key distinction is that intuition is **not assumed to be the first thing we should directly supervise**.

Mathia may first need to learn concepts and reusable conceptual moves such as structural similarity, decomposition, synthesis, abstraction, generalization, reframing, bridge construction, and perspective selection. Candidate intuitions can then emerge from combinations of those capabilities.

A strong teacher such as Codex may provide an initial intuition bootstrap, but teacher similarity should not define the final target. The stronger proposed signal is whether a frozen Mathia intuition measurably improves a separate formal worker such as qwen-lean under a matched proof-search budget.

See [`docs/CONCEPTS_DIMENSIONS_INTUITION.md`](docs/CONCEPTS_DIMENSIONS_INTUITION.md).

## Semantic / execution boundary

For the current line, Mathia-facing primary mathematics should be generic and should not rely on concrete numerical instances or arithmetic execution.

Concrete instantiation may exist privately in generators, computation, falsification, qwen-lean, Lean, or other formal verification, but it should not be the substrate on which Mathia's conceptual reasoning depends.

The base model inevitably already knows arithmetic from pretraining. The experiment does not try to erase that knowledge; it makes arithmetic execution irrelevant to the conceptual capability under study.

## Why the project was reset

An earlier pre-RL line (`gold-set-v0`) tested whether structural context improved an unchanged solver on hidden mathematical tasks. That work produced useful benchmark, audit, and runner methodology, but its tasks still mixed conceptual understanding with concrete execution.

The line was retired **before target-model inference**. Its artifacts remain in Git history and closed issues/PRs.

See [`docs/RESEARCH_RESET_SEMANTIC_INTUITION.md`](docs/RESEARCH_RESET_SEMANTIC_INTUITION.md).

## Active plan

The current critical path remains deliberately short, but its purpose has been revised:

- **#29 — Epic:** concepts, conceptual dimensions, and intuition fertility.
- **#30 — Current gate:** scope and adversarially audit the concepts/dimensions/documented-theorem intuition and qwen-lean fertility contract.
- **#31 — Later:** build only the minimal pre-test/fertility harness required by #30.
- **#32 — Later:** freeze and run the Qwen-base + Codex-reference pre-test against matched qwen-lean proof search.

If #32 shows that the `intuition -> qwen-lean proof uplift` channel is informative, later work may design concept training, conceptual-dimension training, an initial Codex intuition distillation pass, and only then a second pass that selects intuitions by downstream fertility.

No permanent training pipeline or RL algorithm is currently fixed.

## Repository map

- [`AGENTS.md`](AGENTS.md) — repository-wide instructions for ChatGPT, Codex, and reviewers.
- [`docs/CONCEPTS_DIMENSIONS_INTUITION.md`](docs/CONCEPTS_DIMENSIONS_INTUITION.md) — current working training hypothesis and intuition-fertility design.
- [`docs/RESEARCH_RESET_SEMANTIC_INTUITION.md`](docs/RESEARCH_RESET_SEMANTIC_INTUITION.md) — explains the earlier scientific reset and semantic/execution boundary.
- [`docs/CONCEPTUAL_MATH_DIRECTION.md`](docs/CONCEPTUAL_MATH_DIRECTION.md) — broad conceptual research direction.
- [`docs/WORKING_SYNTHESIS.md`](docs/WORKING_SYNTHESIS.md) — current hypotheses, constraints, evidence, and alternatives.
- [`docs/RESEARCH_PLAN_DRAFT.md`](docs/RESEARCH_PLAN_DRAFT.md) — current falsifiable research plan.
- [`docs/EVALUATION_METHODOLOGY.md`](docs/EVALUATION_METHODOLOGY.md) — evidence discipline and intuition-fertility evaluation principles.
- [`docs/MODEL_AND_COMPUTE_CONSTRAINTS.md`](docs/MODEL_AND_COMPUTE_CONSTRAINTS.md) — common model ancestor and compute gates.
- [`docs/THREE_LAYER_RESEARCH_SYSTEM.md`](docs/THREE_LAYER_RESEARCH_SYSTEM.md) — downstream hypothesis for Codex + Mathia + formal specialist cooperation.
- [`experiments/agnostic_mathia_corpus`](experiments/agnostic_mathia_corpus/) — frozen domain-agnostic conceptual corpus release for issue #44.
- [`experiments/mathia_corpus`](experiments/mathia_corpus/) — shared #42/#44 corpus interchange, renderer, validator, and compatibility fixture.
- `.agents/skills/` — reusable repository workflows for issue design, implementation, GitHub operations, and independent review.

## Research stance

Mathia is not committed to a final architecture, ontology, dataset schema, RL algorithm, or formal backend.

Important distinctions should remain explicit:

```text
concept knowledge
!= conceptual-move ability
!= intuition generation
!= teacher similarity
!= arithmetic execution
!= formalization success
!= proof success
!= downstream research usefulness
```

The project should change its operational model when evidence or clearer hypotheses require it.
