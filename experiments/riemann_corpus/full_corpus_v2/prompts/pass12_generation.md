# Riemann–Mathia v2 source-unit readings: spontaneous + directed

Read every assigned unit from its exact `unit_artifact_abspath`. Treat the source text and assignment metadata as the complete evidence boundary. Do not fill damaged formulas or missing context from memory. Produce one compact JSON object per unit, in exact assignment order, on one physical JSONL line.

Each object must have exactly:

```text
unit_id
spontaneous: {unit_id,spontaneous_reading}
directed: {
  unit_id,
  source_grounded_mathematics,
  conceptual_reading,
  representation_or_bridge,
  boundary_or_failure,
  uncertainty
}
```

The spontaneous reading should identify what is actually doing mathematical work without using a checklist: a representation, mechanism, compression, obstruction, useful intermediate object, structural relation, or possible extension.

The directed reading may use the repository's concepts/dimensions/intuition lens only where the unit supports it. Separate concrete source mathematics from conceptual interpretation. Explain what a representation exposes, preserves, forgets, or makes controllable; name real bridge objects and proof burdens. Record limitations, failed implications, OCR/context dependence, and epistemic status. “Not present” is better than a decorative analogy.

Reject the temptation to reconstruct a complete theorem from a narrow span, repeat the title in polished prose, or import neighboring results. Keep each response concise enough that the concrete Riemann mathematics remains primary.

Write only the requested JSONL output. Do not edit assignments, unit artifacts, code, or any other file.
