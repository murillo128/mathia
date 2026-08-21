# Riemann–Mathia v2 cross-source synthesis adjudication

Freshly inspect each proposed cross-source synthesis, its exact parent source units, and their accepted interpretations. Attack false equivalence, title-level analogy, imported theorem context, historical overclaim, hidden direction-of-implication changes, and claims that ignore incompatible hypotheses or epistemic status.

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

Accept only when the relation is supported by all cited parents and yields a concrete reusable mathematical comparison. Quarantine insufficient-context/OCR cases. Reject generic metaphors, topical co-occurrence, and unsupported unification. Preserve explicit mismatches and remaining proof burdens.

Write only the requested JSONL output and do not modify any other file.
