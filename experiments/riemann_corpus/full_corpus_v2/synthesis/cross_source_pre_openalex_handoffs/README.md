# Pre-OpenAlex-handoff cross-source snapshot

This directory preserves the exact raw generation/adjudication assignments,
outputs, combined candidates, and final records that existed before the frozen
`riemann_fulltext_v1` handoff was incorporated into cross-source synthesis.

It is superseded execution evidence, not the current release input. The active
`../cross_source/` tree must be regenerated from assignments that include the
15 useful handoff sources before Riemann v2 is frozen. Keeping this snapshot
prevents the new bounded rerun from overwriting earlier raw teacher evidence.
