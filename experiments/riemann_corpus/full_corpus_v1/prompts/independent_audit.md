# Fresh independent stratified release audit

This audit is independent of the generation contexts. For every assigned
interpretation, read the exact external source unit and the final interpretation.
For every synthesis, read all linked source units and the model-visible synthesis.
Current quality and eligibility labels are deliberately absent. Decide from the
source and candidate content only; downstream validation compares labels after
your output is written.

Check source faithfulness, a concrete operation beyond paraphrase, specificity,
representation gain/loss or an equally concrete mechanism, uncertainty and
heuristic discipline, context/OCR sufficiency, and recurring teacher-style
cadence. For synthesis, require an actual role-preserving shared structure plus
explicit mismatches. Use `quarantine` for insufficient source/context/essential
representation and `reject` for unsupported, generic, or style-only positive
material.

Write one JSONL record per assigned object in exact assignment order with exactly:

```text
object_id
decision                    # accept | reject | quarantine
faithfulness
nonparaphrase
specificity
representation_sensitivity
uncertainty_discipline
context_quality
style_risk
reason
```

Do not edit any other file.
