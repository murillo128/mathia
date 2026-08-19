# Corpus-scale spontaneous and directed readings

This is a bounded teacher-distillation pass over exact Riemann-corpus semantic
units. Read each assigned external unit file in full, its source metadata,
selection reason, context limit, OCR/partial flags, and the two controlling
conceptual documents. Stay inside the frozen unit. A famous theorem or a paper
title is not permission to import the surrounding proof from memory.

For the spontaneous role, identify what the span itself makes mathematically
active: a representation, mechanism, compression, bridge, obstruction,
comparison, epistemic limit, or useful intermediate object. Use concrete names,
conditions, and relations from the span. Do not use a checklist or a reusable
"the key insight is" template.

For the directed role, use `docs/CONCEPTS_DIMENSIONS_INTUITION.md` as a lens only
where supported. Separate what the source states from an interpretation. Explain
an actual representation gain/loss, preserved quantity, decomposition,
counterfactual failure, relocated obligation, or analogy limit. `Not present` is
better than invented depth. Do not call a paper's claimed RH proof established;
describe it as the source's claim unless the span is a standard proved result.
For OCR units, rely only on clearly readable prose and flag damaged formulas.

Write two raw records for every assigned unit, nested in one JSONL record:

```json
{
  "unit_id": "...",
  "spontaneous": {
    "unit_id": "...",
    "spontaneous_reading": "source-specific serious reading"
  },
  "directed": {
    "unit_id": "...",
    "source_grounded_mathematics": "what the span states",
    "conceptual_reading": "operation performed over that mathematics",
    "representation_or_bridge": "concrete representation choice, or not present",
    "boundary_or_failure": "condition or place the move stops",
    "uncertainty": "source/context/OCR/speculation boundary, or none"
  }
}
```

Use exactly those fields. Keep each field compact but mathematically substantive.
Do not decide final acceptance and do not edit any other file.
