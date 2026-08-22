# Riemann–Mathia v2 cross-source synthesis generation

Use the assigned index of accepted source-grounded interpretations to propose only high-value relations across distinct sources. This is not topic clustering or vocabulary-frequency summarization.

Emit compact one-line JSONL candidates with exactly:

```text
synthesis_id
title
parent_unit_ids[]
claim
historical_or_program_relation
limits
```

Every candidate must use at least two units from at least two distinct sources. Prefer a concrete shared mechanism, representation bridge, refinement, contradiction, obstruction, or historically changing proof burden. Include explicit limits that prevent distinct programs from collapsing into a vague analogy. Cover materially different RH viewpoints where evidence permits, and emit no candidate when the index does not support one.

Every `synthesis_id` must begin with the assignment's exact `required_synthesis_id_prefix`, followed by a unique short descriptive suffix.

Write only the requested JSONL output and do not modify any other file.
