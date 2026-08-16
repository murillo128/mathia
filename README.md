# Mathia

Mathia is an exploratory research project about **semantic and conceptual mathematical reasoning in language models**.

The project asks whether a model can learn mathematical meaning, representations, structural mechanisms, analogies, invariants, generalizations, and useful intuitions at a level that is distinct from both arithmetic execution and formal theorem proving.

## Current research question

The active first line is intentionally narrow:

> **Can a model represent and use the meaning of mathematical operations and structural mechanisms without relying on concrete numerical instances or arithmetic execution?**

For the current experiment, Mathia-facing primary mathematics should be generic. Concrete instantiation may exist privately in generators, computation, falsification, or formal verification, but it should not be the substrate on which Mathia's conceptual reasoning depends.

The base model inevitably already knows arithmetic from pretraining. The experiment does not try to erase that knowledge; it makes arithmetic execution irrelevant to success.

## Why the project was reset

An earlier pre-RL line (`gold-set-v0`) tested whether structural context improved an unchanged solver on hidden mathematical tasks. That work produced useful benchmark, audit, and runner methodology, but its tasks still mixed conceptual understanding with concrete execution.

The line was retired **before target-model inference**. Its artifacts remain in Git history and closed issues/PRs, but the active tree has been cleaned so the new benchmark can be designed from first principles instead of inheriting the old task assumptions.

See [`docs/RESEARCH_RESET_SEMANTIC_INTUITION.md`](docs/RESEARCH_RESET_SEMANTIC_INTUITION.md).

## Active plan

The current critical path is deliberately short:

- **#29 — Epic: semantic mathematical intuition without arithmetic execution.**
- **#30 — Current gate:** design and adversarially audit a small computation-free semantic-intuition benchmark.
- **#31 — Later:** build only the minimal deterministic plumbing required by the accepted benchmark.
- **#32 — Later:** freeze, run, and interpret the first local base-model diagnostic.

No Mathia SFT/RL or three-layer orchestration is currently authorized by this plan. Those become design questions only if the semantic-intuition diagnostic establishes a useful signal.

## Repository map

- [`AGENTS.md`](AGENTS.md) — repository-wide instructions for ChatGPT, Codex, and reviewers.
- [`docs/RESEARCH_RESET_SEMANTIC_INTUITION.md`](docs/RESEARCH_RESET_SEMANTIC_INTUITION.md) — explains the scientific reset, what was retired, what was preserved, and the no-execution/no-instance boundary.
- [`docs/CONCEPTUAL_MATH_DIRECTION.md`](docs/CONCEPTUAL_MATH_DIRECTION.md) — current conceptual research direction.
- [`docs/WORKING_SYNTHESIS.md`](docs/WORKING_SYNTHESIS.md) — current hypotheses, accepted experimental constraints, and unresolved questions.
- [`docs/RESEARCH_PLAN_DRAFT.md`](docs/RESEARCH_PLAN_DRAFT.md) — falsifiable research plan from semantic intuition through possible later fertility training.
- [`docs/EVALUATION_METHODOLOGY.md`](docs/EVALUATION_METHODOLOGY.md) — evidence discipline and external-validation principles.
- [`docs/MODEL_AND_COMPUTE_CONSTRAINTS.md`](docs/MODEL_AND_COMPUTE_CONSTRAINTS.md) — common model ancestor and compute gates.
- [`docs/THREE_LAYER_RESEARCH_SYSTEM.md`](docs/THREE_LAYER_RESEARCH_SYSTEM.md) — downstream hypothesis: scarce frontier director plus abundant local conceptual and formal specialists.
- `.agents/skills/` — reusable repository workflows for issue design, implementation, GitHub operations, and independent review.

## Research stance

Mathia is not committed to a final architecture, ontology, dataset schema, RL algorithm, or formal backend.

Important distinctions should remain explicit:

```text
semantic meaning
!= arithmetic execution
!= AI preference
!= formalization success
!= proof success
!= downstream research usefulness
```

The project should change its operational model when evidence or clearer hypotheses require it. The current reset is an example of that principle in practice.
