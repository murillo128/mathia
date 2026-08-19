# Non-quota whole-source semantic expansion

The earlier coverage pass retained one coherent unit from every assigned source.
That first unit is not a quota and is not assumed to exhaust the paper. Read each
whole normalized source again, together with its retained coverage-pass span,
and decide how many additional semantic units the mathematical content warrants.

Choose zero to four additional units per source. Zero is correct for a short,
partial, narrowly focused, or extraction-limited source whose useful mechanism
is already represented. Rich sources may contribute several units when they
expose genuinely different definitions, results, constructions, proof
mechanisms, obstructions, comparisons, computations, or changes of viewpoint.
Do not add a second unit merely to make counts uniform, and do not perform
comprehensive lemma-by-lemma fragmentation.

Each additional unit must be an exact contiguous normalized line span at the
smallest scale where its mechanism is intelligible. It may overlap the first
unit or another additional unit when shared setup is necessary, but it may not
repeat the same line range. Prefer 35–180 lines when coherence permits. Include
the premise, limitation, or conclusion needed to prevent an interpretation from
importing missing context.

For OCR sources, add a unit only when readable prose supports it without
reconstructing damaged formulas. For partial previews, remain strictly inside
the retained pages. Record essential/useful/provenance-only representation
dependencies; do not train text that pretends an unavailable essential figure
was preserved.

Write one JSONL envelope per assigned source, in exact assignment order, with:

```text
source_id
expansion_decision       # expanded | no_additional_unit | quarantined
expansion_reason         # source-specific reason for the variable count
additional_units         # zero to four objects, in source order
segmentation_provenance  # isolated-codex-nonquota-expansion
```

Every object in `additional_units` must contain exactly:

```text
line_start
line_end
source_pages
unit_type
selection_reason
context_limit
representation_dependency  # essential | useful | provenance_only | none
```

Use `quarantined` with an empty list when additional promising material exists
but extraction/context quality makes it unsafe. Do not edit source text, the
coverage-pass plan, or any other file.
