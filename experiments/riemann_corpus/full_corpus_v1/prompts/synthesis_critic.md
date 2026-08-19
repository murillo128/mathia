# Fresh adversarial synthesis critic

Read every candidate and every linked exact source unit. Attack unsupported
abstraction more aggressively than a unit-level interpretation. Check that the
claimed role appears in each source, that the sources are not merely discussing
the same topic, that directionality and hypotheses are preserved, and that the
limits are mathematically substantive. Reject vague metaphors, historical lists,
teacher-template prose, and syntheses that silently treat a heuristic or proposed
RH proof as established.

Write one JSONL record per candidate in exact order with exactly:

```text
synthesis_id
critic_decision          # accept_as_is | revise | reject | quarantine
source_link_check
shared_structure_check
limits_check
unsupported_abstraction
style_risk
revision_instructions
```

Do not edit any other file.
