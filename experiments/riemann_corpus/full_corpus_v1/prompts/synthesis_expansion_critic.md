# Fresh critic for expansion syntheses

Read every expansion candidate and all exact linked source units. Decide
`accept_as_is`, `revise`, or `reject`. Require a role-preserving mathematical
structure, not a broad theme; exact support for each imported claim; explicit
limits; and disciplined proof/heuristic/OCR status. Reject candidates that only
became possible by accumulating generic prose from more units.

Write one JSONL record per candidate in exact order with exactly:

```text
synthesis_id
critic_decision
source_link_check
shared_structure_check
limits_check
unsupported_abstraction
style_risk
revision_instructions
```

Do not edit any other file.
