# Riemann–Mathia v2 source-grounded revision

For every assigned unit, read the exact source artifact, the spontaneous/directed readings, and the fresh critic. Produce the final corpus-local interpretation without overwriting any earlier pass.

Emit one compact JSON object per unit, in exact assignment order, on one physical JSONL line, with exactly:

```text
unit_id
decision: accepted | rejected | quarantined
interpretation
source_support
nonparaphrase_operation
speculation_status
quality_reason
```

An accepted interpretation must preserve concrete mathematics and perform a supported conceptual operation beyond friendly restatement. Keep source fact, interpretation, cross-source suggestion, heuristic, and speculation visibly distinct. State what the representation/mechanism gains or loses, where the proof burden remains, and which assumptions matter. Apply the critic's corrections; do not defend the earlier prose by default.

Use `quarantined` for insufficient context or lower-confidence extraction that prevents reliable use. Use `rejected` for false, unsupported, generic, or paraphrase-only output. Retain a concise interpretation explaining the failure even for non-accepted records. Never repair corrupted formulas or missing hypotheses from memory.

Write only the requested JSONL output. Do not modify any other file.
