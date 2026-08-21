# Pre-OpenAlex audit checkpoint

This directory preserves the completed independent Riemann-v2 audit immediately
before the two frozen issue #46 handoffs were incorporated. It is immutable
execution evidence, not the active audit output.

The active audit may carry a prior decision only when its full canonical
`object_id` remains an exact match after the handoff-derived expansion. Objects
with changed content, parents, or identity are assigned to a fresh isolated
review context.
