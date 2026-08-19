# Cross-source synthesis from the non-quota expansion

Read the expansion assignment and exact source units. Generate exactly eight
new synthesis candidates that add mathematical coverage beyond the first twelve
coverage-pass candidates. Every candidate must link two to five units from at
least two sources and must include at least one unit marked
`is_nonquota_expansion_unit=true`.

Use the additional units to identify a concrete shared role, transformation,
obstruction, proof interface, or relocated obligation that the one-unit-per-
source coverage pass could not expose. A shared topic or repeated vocabulary is
not enough. State what each source contributes, where the roles agree, and the
precise point where the transfer stops. Preserve proof, conditional theorem,
heuristic, proposed reformulation, computation, and OCR-limited evidence as
different statuses.

Write JSONL in order `riemann_synthesis_expansion_01` through `..._08` with
exactly:

```text
synthesis_id
title
source_unit_ids
shared_structure
synthesis
limits
historical_change
candidate_quality_note
```

Do not decide final acceptance and do not edit any other file.
