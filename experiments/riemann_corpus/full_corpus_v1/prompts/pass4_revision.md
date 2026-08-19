# Fresh source-grounded revision

Read the exact source unit and all three earlier records. Produce the final
training-facing interpretation only if the unit supports a concrete conceptual
operation beyond paraphrase. Follow the critic; do not rescue a weak item by
importing adjacent mathematics or by making the prose more impressive.

An accepted interpretation should be natural compact prose whose organization
follows the mathematics, normally two to four short paragraphs. Anchor it in
the span's actual definitions, hypotheses, transformations, or consequences.
Make the representation gain/loss, mechanism, obstruction, or failure condition
explicit. Clearly mark a paper's proposal, heuristic, analogy, or purported
proof as such. Do not reproduce a rigid checklist and do not expose QA metadata
inside the interpretation.

Use `rejected` for paraphrase, generic explanation, unsupported mathematics, or
teacher-style imitation. Use `quarantined` when source/context/OCR/essential
representation quality prevents a trustworthy positive object. For rejected or
quarantined records, keep `interpretation` as a concise audit-facing description
of what could not be made trainable; it will never enter the positive manifest.

Write one JSONL record per assigned unit in exact order with exactly:

```text
unit_id
decision                 # accepted | rejected | quarantined
interpretation
source_support
nonparaphrase_operation
speculation_status       # none | downgraded | explicitly_marked
quality_reason
```

Do not edit any other file.
