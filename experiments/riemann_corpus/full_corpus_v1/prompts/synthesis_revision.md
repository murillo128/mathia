# Fresh synthesis revision

Read every candidate, its fresh critique, and all linked source units. Revise
only what remains a source-specific shared mathematical move. Keep explicit
limits and mismatches in the training-facing content; do not hide them in audit
metadata. Reject or quarantine a candidate that cannot be repaired without
imported context or vague metaphor.

Write one JSONL record per candidate in exact order with exactly:

```text
synthesis_id
decision                 # accepted | rejected | quarantined
title
source_unit_ids
synthesis
limits
historical_change        # string or null
quality_reason
```

Do not edit any other file.
