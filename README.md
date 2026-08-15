# Mathia

Mathia is an exploratory research repository for conceptual mathematical reasoning in language models.

The project investigates whether a model can learn to work with compact mathematical ideas, abstractions, relationships, viewpoints, analogies, generalizations, and conjectures at a level above formal theorem proving, while still allowing later formalization and verification with systems such as Lean.

The project remains exploratory: the research hypothesis and experimental design should change when evidence requires it, and no final model architecture or conceptual/formal integration strategy has been settled.

## Repository information

- `AGENTS.md` defines how ChatGPT, Codex, and reviewers should operate in the repository.
- `docs/CONCEPTUAL_MATH_DIRECTION.md` preserves the conceptual and philosophical motivation for the project.
- `docs/WORKING_SYNTHESIS.md` captures the current brainstorming synthesis around mathematical understanding, representations, conceptual/formal layers, transfer, composition, reframing, simplicity, and beauty.
- `docs/RESEARCH_PLAN_DRAFT.md` turns that synthesis into a falsifiable draft research plan centered on hidden interventions, mathematical fertility, cold-start data, RL, controls, and later comparison with qwen-lean.
- GitHub issue `#2` is the research umbrella for validating whether conceptual mathematical reasoning provides a genuinely trainable signal.
- `.agents/skills/` contains reusable agent workflows for issue design, implementation, GitHub operations, and independent review.

The draft plan is intentionally provisional. Exact dataset schemas, RL algorithms, model combination strategies, and formal-backend integration should be settled only when concrete experiments require those decisions.
