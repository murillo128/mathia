# Riemann–Mathia v2 within-source synthesis adjudication

Independently inspect every candidate and all of its exact parent unit artifacts. Decide whether the source itself supports the claimed relation across its sections. Do not accept a synthesis merely because its title sounds coherent or because the same source mentions both topics.

Emit one compact JSON object per candidate, in exact assignment order, on one physical JSONL line, with exactly:

```text
synthesis_id
decision: accepted | quarantined | rejected
synthesis
source_support
nonparaphrase_operation
limits
quality_reason
```

Accept only if at least two distinct parent units jointly support a concrete mechanism, dependency, change of representation, refinement, obstruction, or limit that is not available from either parent alone. Preserve mismatches, hypotheses, proof burdens, and OCR/context risks. Quarantine source-defective cases; reject generic themes, unsupported causal stories, and paraphrase-only combinations.

Write only the requested JSONL output and do not modify any other file.
