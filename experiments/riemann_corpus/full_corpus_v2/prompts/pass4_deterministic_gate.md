# Riemann–Mathia v2 deterministic non-revision gate

This rubric applies only after a fresh isolated critic has returned `accept_as_is`, `reject`, or `quarantine`. No model revision is run.

- Map `accept_as_is` to final `accepted`, `reject` to `rejected`, and `quarantine` to `quarantined`.
- Preserve the directed candidate's conceptual interpretation, exact source-grounded mathematics, and representation/bridge fields without rewriting them.
- Combine the candidate's stated boundary/uncertainty with critic inference and context/OCR risks as `speculation_status`.
- Combine the critic's supported, unsupported/imported, and paraphrase/style findings as `quality_reason`.
- Never promote a negative critic decision, reconstruct formulas, or add mathematical claims.

Only `revise` decisions proceed to the model-based pass-4 revision prompt.
