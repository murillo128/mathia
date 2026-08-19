# Source-linked cross-source synthesis candidates

Read the accepted interpretation assignment and the exact source units behind
any material you use. Generate exactly twelve candidate syntheses spanning the
requested mechanisms and eras. Each candidate must link two to five units from
at least two distinct sources. A recurring word such as "spectrum", "random",
or "transform" is not a shared mathematical structure.

State the concrete role played in each source, what is genuinely shared, what
obligation is relocated, and where the connection stops. A historical synthesis
must identify an actual change in viewpoint rather than merely sort papers by
date. Preserve disagreement, conditionality, and the difference between proved
results, heuristics, computations, and proposed physical reformulations.

Write JSONL with exactly:

```text
synthesis_id              # riemann_synthesis_candidate_01 ... 12
title
source_unit_ids
shared_structure
synthesis
limits
historical_change         # string or null
candidate_quality_note
```

Do not decide final acceptance and do not edit any other file.
