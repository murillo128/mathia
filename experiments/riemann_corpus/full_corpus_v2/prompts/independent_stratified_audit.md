# Riemann–Mathia v2 independent stratified corpus audit

This is a fresh context. Current object labels are withheld. For each assigned item, inspect the exact source-parent artifact(s), then audit the proposed interpretation or synthesis. Do not infer quality from fluent prose, famous-source familiarity, or likely prior labels.

Emit one compact JSON object per item, in exact assignment order, on one physical JSONL line, with exactly:

```text
object_id
decision: accept | quarantine | reject
faithfulness
context_sufficiency
nonparaphrase_value
specificity
representation_sensitivity
uncertainty_discipline
duplicate_or_version_risk
conceptual_ecosystem_contribution: new_mechanism | refinement_or_relation | repeats_represented_mechanism | unresolved
notes
```

Test source contradiction, lost hypotheses or implication direction, formula reconstruction from memory/OCR, generic teacher-style prose, unsupported generalization, accidental duplicate/preprint over-representation, and whether a named representation actually explains a gain/loss. A synthesis must be supported by every parent and must preserve mismatches. Quarantine insufficient source/context quality; reject false, generic, or paraphrase-only material.

The ecosystem label is comparative audit evidence, not a truth label: use `new_mechanism` only for a materially new RH mechanism/representation/obstruction in this v2 panel, `refinement_or_relation` for added depth or a concrete relation among known mechanisms, `repeats_represented_mechanism` for genuinely redundant conceptual content, and `unresolved` when context is inadequate.

Write only the requested JSONL output and do not modify any other file.
