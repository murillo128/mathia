# Final revision of expansion syntheses

Read the expansion candidates, the fresh critic, and all linked exact source
units. Follow material critic findings. Keep a candidate accepted only when the
revised synthesis names a concrete shared mathematical role and its limits;
otherwise reject it, or quarantine it when source/context/representation quality
is the blocker. Do not rescue a weak bridge with more general prose.

Write one JSONL record per candidate in exact order with exactly:

```text
synthesis_id
decision                 # accepted | rejected | quarantined
title
source_unit_ids
synthesis
limits
historical_change
quality_reason
```

Do not edit any other file.
